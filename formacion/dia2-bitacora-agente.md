
Para este segundo día he hecho estas notas además de la bitacora para registrar mejor el trabajo
Lo que se pide en el documento esta en:

- Preguntas Lab6: linea 26
- Bitácora del agente: linea 57

## Configuracion github
Al activar las alertas, el code scaning y el pull request han saltado 8 alertas. Estas son menos que las que devolvía trivy (aunque algunas estaban repetedas) pero dan información muy parecida (código de la alerta, localización, código CVE...) pero con una mejor interfaz.

### Correccion Lab5
__Informe github:__
Bump org.webjars:bootstrap from 3.3.6 to 5.0.0 (#6)
Package: org.webjars:bootstrap (Maven)
Affected version >= 2.0.4, < 3.4.0
Patched version 3.4.0
CVE-2018-14041
GHSA-4p24-vmcr-4gqj
Severity: Moderate

Tras actualizar la version (y 6 funciones en \src\main\less\petclinic.less) se hizo push a la rama fix/correccion-manual.
Se realizaron los analisis, pasandolos todos y se hizo la PR y el merge.
No se localizan mas vulnerabilidades.
Se ha realizado este Lab en 50 min  (Analisis: 9min, Cambio: 30min, Build local: 4min, Pipeline: 4min y Cierre: 1min)


### Lab6

__¿Por qué el segundo escaneo sigue encontrando el secreto?__
Porque gitleaks ha escaneado los 992 commits anteriores y el archivo sigue estando en uno de ellos

__¿Por qué borrarlo no basta y quién tiene que rotarlo?__
Porque cualquiera con acceso al repositorio podría acceder al secreto. Deberia rotarlo el propietario del secreto

__¿Qué cambiarías para que no vuelva a pasar?__
No lo volveria a subir a girhub, metiendo el archivo en el .gitignore


### Lab7

Tras realizar el analisis con OpenRewrite (jdk8 y 17) ha devuelto lo siguiente por consola a pesar de introducir la vulnerabilidad del Lab5:

[INFO] Using active recipe(s) [com.ntt.formacion.SubirLibreria]
[INFO] Using active styles(s) []
[INFO] Validating active recipes...
[INFO] Project [petclinic] Resolving Poms...
[INFO] Project [petclinic] Parsing source files
[INFO] Running recipe(s)...
[INFO] Applying recipes would make no changes. No patch file generated.
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  22.761 s
[INFO] Finished at: 2026-11-19T12:21:44+01:00
[INFO] ------------------------------------------------------------------------


### Lab8

| Campo | Contenido |
|---|---|
| Alerta  | Bump org.webjars:bootstrap, CVE-2018-14041, GHSA-4p24-vmcr-4gqj (alerta #6) |
| Herramienta  | aXet.PlugIn: GPY-4o usado como agente |
| Instrucciones dadas  | A continuación de la tabla (Por el bien del formato no se incluye en la tabla directamente) |
| Plan propuesto  | El agente investigó la vulnerabilidad y analizó boostrap, tras lo cual pidió permiso para  buscar una nueva versión. Encontró que la mejor opción era la versión 5.3.7 y hacer pruebas con ./mvnw verify. Tras las pruebas se vio que no era suficiente y que era necesario modificar ciertas funciones del archivo .\src\main\less\petclinic.less. Tras 2 intentos compiló correctamente sin vulnerabilidad|
| Cambios aplicados  | pom.xml: linea 25 (versión de bootstrap), petclinic.less: lineas 180-202 y 215-237 (funciones que usaban métodos en versiones más nuevas) |
| Verificación  | Pruebas de gitgub, ./mvnw verify y comprobación con trivy |
| Errores o riesgos  | Dio por hecho que al cambiar la versión de bootstrap compilaría correctamente. Después de hacer una primera modificación a petclinic.less ocurrió el mismo error |
| Tiempos  | Análisis: 1min, Cambio: menos de 1min, Verificación: 12min, PR y cierre: 2min. Total con agente: 14min 30s, Total sin agente: 50 min |
| Consumo  | ------ |
| Conclusión  | El agente aporta mucha agilidad a la hora de encontrar en el código el problema y de buscar una solución pero necesita la guia y el contexto de un ser humano para ser realmente productivo o para no hacer cambios no deseados.  |


#### Instrucciones dadas:

En este repositorio hay una alerta de Dependabot sobre org.webjars:bootstrap (GHSA-4p24-vmcr-4gqj). 

1. Analiza de dónde viene la dependencia y si llega al artefacto desplegado. 

2. Propón un plan de corrección en el origen, sin overrides ni exclusiones si se puede evitar. 

3. No modifiques ningún fichero hasta que yo apruebe el plan. 

4. Cuando lo apruebe: aplica el cambio, ejecuta ./mvnw verify y vuelve a escanear con trivy. 

5. Resume qué has cambiado y cómo lo has verificado.


Enlace PR lab5: https://github.com/ManuelBravoRoig/resiliencia-practicas/pull/2
Enlace PR lab8: https://github.com/ManuelBravoRoig/resiliencia-practicas/pull/3