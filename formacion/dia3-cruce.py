import json
from pathlib import Path

import pandas as pd


RUTA_ALERTAS = Path("alertas.json")
RUTA_TRIVY = Path("trivy.json")
CARPETA_SALIDA = Path("formacion/resultados-cruce")


def cargar_json(ruta):
    """Carga JSON normal, JSON con páginas agrupadas o JSON concatenado."""
    if not ruta.exists():
        raise FileNotFoundError(
            f"No se encuentra '{ruta}'. Ejecuta primero la descarga o el escaneo."
        )

    texto = ruta.read_text(encoding="utf-8-sig").strip()

    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        # Permite leer varias respuestas JSON concatenadas por gh api --paginate.
        decodificador = json.JSONDecoder()
        elementos = []
        posicion = 0

        while posicion < len(texto):
            while posicion < len(texto) and texto[posicion].isspace():
                posicion += 1

            if posicion >= len(texto):
                break

            elemento, posicion = decodificador.raw_decode(texto, posicion)
            elementos.append(elemento)

        return elementos


def aplanar_alertas(datos):
    """
    Convierte estos formatos en una lista de alertas:
    - Lista directa de alertas.
    - Lista de páginas producida por --slurp.
    - Varias páginas JSON concatenadas.
    """
    if isinstance(datos, dict):
        if "message" in datos and "documentation_url" in datos:
            raise ValueError(
                f"GitHub devolvió un error: {datos['message']}. "
                "Comprueba gh auth status y el nombre del repositorio."
            )
        return [datos]

    if not isinstance(datos, list):
        raise ValueError("El formato de alertas.json no es una lista ni un objeto JSON.")

    alertas_planas = []

    for elemento in datos:
        if isinstance(elemento, list):
            alertas_planas.extend(elemento)
        elif isinstance(elemento, dict):
            alertas_planas.append(elemento)

    return alertas_planas


def texto(valor):
    """Normaliza valores vacíos para comparaciones y salidas."""
    if pd.isna(valor) or valor is None:
        return ""
    return str(valor).strip()


def resumen_por_id(tabla, columna_id, columna_paquete, columnas_extra=None):
    """Agrupa identificadores y conserva los paquetes y campos relevantes."""
    columnas_extra = columnas_extra or []

    if tabla.empty:
        return pd.DataFrame(columns=[columna_id, "paquetes"])

    filas = []

    for identificador, grupo in tabla.groupby(columna_id, dropna=True):
        if not texto(identificador):
            continue

        fila = {
            columna_id: identificador,
            "paquetes": ", ".join(
                sorted({texto(x) for x in grupo[columna_paquete] if texto(x)})
            ),
        }

        for columna in columnas_extra:
            valores = sorted({texto(x) for x in grupo[columna] if texto(x)})
            fila[columna] = ", ".join(valores)

        filas.append(fila)

    return pd.DataFrame(filas)


# --------------------------------------------------------------------------
# Carga y normalización de alertas de Dependabot
# --------------------------------------------------------------------------

datos_alertas = cargar_json(RUTA_ALERTAS)
lista_alertas = aplanar_alertas(datos_alertas)

alertas = pd.json_normalize(lista_alertas)

columnas_dependabot = [
    "number",
    "state",
    "security_advisory.ghsa_id",
    "security_advisory.cve_id",
    "dependency.package.name",
    "dependency.manifest_path",
    "security_advisory.severity",
]

# Si un campo no llega en la respuesta, se crea vacío para que el script continúe.
for columna in columnas_dependabot:
    if columna not in alertas.columns:
        alertas[columna] = pd.NA

dep = alertas[columnas_dependabot].copy()

dep = dep.rename(
    columns={
        "number": "numero_alerta",
        "state": "estado",
        "security_advisory.ghsa_id": "ghsa",
        "security_advisory.cve_id": "cve",
        "dependency.package.name": "paquete",
        "dependency.manifest_path": "manifiesto",
        "security_advisory.severity": "severidad",
    }
)

for columna in dep.columns:
    dep[columna] = dep[columna].map(texto)

# Para comparar con Trivy se prioriza el CVE, porque Trivy normalmente informa CVE.
# Si Dependabot no proporciona CVE, se conserva el GHSA.
dep["id_comparable"] = dep["cve"].where(dep["cve"] != "", dep["ghsa"])


# --------------------------------------------------------------------------
# Carga y normalización del informe de Trivy
# --------------------------------------------------------------------------

datos_trivy = cargar_json(RUTA_TRIVY)

filas_trivy = [
    {
        "id": texto(v.get("VulnerabilityID")),
        "paquete": texto(v.get("PkgName")),
        "version": texto(v.get("InstalledVersion")),
        "severidad": texto(v.get("Severity")),
        "fichero": texto(resultado.get("Target")),
    }
    for resultado in datos_trivy.get("Results", [])
    if isinstance(resultado, dict)
    for v in (resultado.get("Vulnerabilities") or [])
    if isinstance(v, dict)
]

trivy = pd.DataFrame(
    filas_trivy,
    columns=["id", "paquete", "version", "severidad", "fichero"],
)

if not trivy.empty:
    trivy["id_comparable"] = trivy["id"].map(texto)
else:
    trivy["id_comparable"] = pd.Series(dtype="object")


# --------------------------------------------------------------------------
# Alertas frente a avisos distintos
# --------------------------------------------------------------------------

alertas_dependabot = len(dep)
avisos_dependabot = dep["id_comparable"].replace("", pd.NA).nunique()

alertas_trivy = len(trivy)
avisos_trivy = trivy["id_comparable"].replace("", pd.NA).nunique()

resumen_fuentes = pd.DataFrame(
    [
        {
            "fuente": "Dependabot",
            "alertas": alertas_dependabot,
            "avisos_distintos": avisos_dependabot,
        },
        {
            "fuente": "Trivy",
            "alertas": alertas_trivy,
            "avisos_distintos": avisos_trivy,
        },
    ]
)


# --------------------------------------------------------------------------
# Avisos presentes solo en una fuente
# --------------------------------------------------------------------------

ids_dependabot = {
    identificador
    for identificador in dep["id_comparable"]
    if texto(identificador)
}

ids_trivy = {
    identificador
    for identificador in trivy["id_comparable"]
    if texto(identificador)
}

solo_dependabot_ids = ids_dependabot - ids_trivy
solo_trivy_ids = ids_trivy - ids_dependabot

solo_dependabot = resumen_por_id(
    dep[dep["id_comparable"].isin(solo_dependabot_ids)],
    "id_comparable",
    "paquete",
    ["ghsa", "cve", "manifiesto", "severidad"],
).rename(columns={"id_comparable": "id"})

solo_trivy = resumen_por_id(
    trivy[trivy["id_comparable"].isin(solo_trivy_ids)],
    "id_comparable",
    "paquete",
    ["version", "fichero", "severidad"],
).rename(columns={"id_comparable": "id"})


# --------------------------------------------------------------------------
# 5 paquetes con más avisos
# --------------------------------------------------------------------------

# Se cuenta cada aviso distinto por paquete.
# Se eliminan duplicados entre fuentes cuando tienen el mismo identificador comparable.
dependabot_para_top = dep[["id_comparable", "paquete"]].copy()
dependabot_para_top["fuente"] = "Dependabot"

trivy_para_top = trivy[["id_comparable", "paquete"]].copy()
trivy_para_top["fuente"] = "Trivy"

unificado = pd.concat(
    [dependabot_para_top, trivy_para_top],
    ignore_index=True,
)

unificado = unificado[
    (unificado["id_comparable"] != "") & (unificado["paquete"] != "")
].drop_duplicates(subset=["id_comparable", "paquete"])

top_5_paquetes = (
    unificado.groupby("paquete")["id_comparable"]
    .nunique()
    .reset_index(name="avisos_distintos")
    .sort_values(
        by=["avisos_distintos", "paquete"],
        ascending=[False, True],
    )
    .head(5)
)


# --------------------------------------------------------------------------
# Mostrar resultados y guardar archivos
# --------------------------------------------------------------------------

CARPETA_SALIDA.mkdir(parents=True, exist_ok=True)

dep.to_csv(
    CARPETA_SALIDA / "dependabot-normalizado.csv",
    index=False,
    encoding="utf-8-sig",
)

trivy.to_csv(
    CARPETA_SALIDA / "trivy-normalizado.csv",
    index=False,
    encoding="utf-8-sig",
)

solo_dependabot.to_csv(
    CARPETA_SALIDA / "solo-dependabot.csv",
    index=False,
    encoding="utf-8-sig",
)

solo_trivy.to_csv(
    CARPETA_SALIDA / "solo-trivy.csv",
    index=False,
    encoding="utf-8-sig",
)

top_5_paquetes.to_csv(
    CARPETA_SALIDA / "top-5-paquetes.csv",
    index=False,
    encoding="utf-8-sig",
)

print("\n" + "=" * 72)
print("1. ALERTAS FRENTE A AVISOS DISTINTOS")
print("=" * 72)
print(resumen_fuentes.to_string(index=False))


print("\n" + "=" * 72)
print("2. AVISOS ENCONTRADOS SOLO EN UNA FUENTE")
print("=" * 72)

print(f"\nSolo Dependabot: {len(solo_dependabot)} aviso(s)")
if solo_dependabot.empty:
    print("No hay avisos exclusivos de Dependabot según el identificador comparable.")
else:
    print(solo_dependabot.to_string(index=False))

print(f"\nSolo Trivy: {len(solo_trivy)} aviso(s)")
if solo_trivy.empty:
    print("No hay avisos exclusivos de Trivy según el identificador comparable.")
else:
    print(solo_trivy.to_string(index=False))


print("\n" + "=" * 72)
print("3. CINCO PAQUETES QUE CONCENTRAN MÁS AVISOS DISTINTOS")
print("=" * 72)

if top_5_paquetes.empty:
    print("No se han encontrado vulnerabilidades para calcular el ranking.")
else:
    print(top_5_paquetes.to_string(index=False))

print("\nArchivos de apoyo guardados en:")
print(CARPETA_SALIDA.resolve())


