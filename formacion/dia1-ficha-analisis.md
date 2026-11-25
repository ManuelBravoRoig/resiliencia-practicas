# Glosario de términos

### CVE
Vulnerabilidades específicas que están presente en un sistema.

### CWE
Lista de fallo o debilidades en la programación que puede generar vulnerabilidades que ponen en peligro al sistema.

### CVSS
Un sistema que analiza las diferentes vulnerabilidades y las clasifica según su gravedad.

### GHSA
Alertas especificas de seguridad que da github que cada una trata una vulnerabilidad específica.

### SAST
Es un modo de análisis que consiste en analizar el código sin ejecutar de una aplicación para detectar vulnerabilidades.

### SCA
Análisis de las dependencias o librerias de una aplicación para detectar vulnerabilidades.

### Secreto
Cualquier dato o información que en un sistema debe ser privada y no ser expuesta. Normalmente tiene que ver con la autentificacion o autorización.

### Dependencia directa
Dependencias de Maven que están declaradas en el archivo pom.xml y son necesarias para el proyecto.

### Dependencia transitiva
Dependencia de Maven que no esta declarada en el archivo pom.xml pero que otras librerías o dependencias que si lo están dependen de ellas.

### Lockfile
Archivo que en un proyecto especifica las versiones exactas de las dependencias que son necesarias, tanto las directas como las transitivas.

### SBOM
La lista de componentes/librerias/partes que son necesarias para que funciones un sistema o aplicación.

### Severidad
Parecedo a CVSS, clasificar como de grave es una vulnerabilidad específica.

### Exposición
Cuando un sistema queda expuesto a la posibilidad de una amenazo o peligro.

### Aviso
El sistema indica que hay una vulnerabilidad en un componente, dando el identificador y en que paquete se encuentra.

### Alerta
Una herramienta emite una alerta cuando encuentra la vulnerabilidad en un manifiesto.


# Análisis de avisos

| Aviso (CVE o GHSA) | Componente y versión | Cadena de dependencia | Desarrollo o producción | ¿Llega a lo desplegado? | Corrección propuesta | Por qué |
|---|---|---|---|---|---|---|
| CVE-2023-6378 | 'ch.qos.logback:logback-classic:1.2.3' | 'spring-petclinic:2.4.0' -> 'spring-boot-starter-actuator:2.4.1' -> 'spring-boot-starter:2.4.1' -> 'spring-boot-starter-logging:2.4.1' -> 'logback-classic:1.2.3' | Producción | Si | Cambiar de versión a la 1.2.13  | Trivy asegura que arregla el CVE |
| CVE-2025-24813 | 'org.apache.tomcat.embed:tomcat-embed-core:9.0.41' | 'spring-petclinic:2.4.0' -> 'spring-boot-starter-web:2.4.1' -> 'spring-boot-starter-tomcat:2.4.1' -> 'tomcat-embed-core:9.0.41'| Producción | Si | Mejorar la versión a la 9.0.99 | Trivy recomienda cambiar a una corregida |
| CVE-2021-28170 | 'org.glassfish:jakarta.el:3.0.3' | 'spring-petclinic:2.4.0' -> 'spring-boot-starter-validation:2.4.1' -> 'jakarta.el:3.0.3' | Produccion | Si | Cambiar a la versión 3.0.4 | La nueva versión corrige el CVE |
| CVE-2022-33987 | 'got@8.3.2' | 'juice-shop@15.2.0' -> 'download@8.0.0' -> 'got@8.3.2' | Produccion | Si | Subir got a la version 11.8.5 | La nueva version de la dependencia no arregla la vulnerabilidad por si misma, asi que hay que actualizar la version de got |
| CVE-2023-32314 | 'vm2@3.9.17' | 'juice-shop@15.2.0' -> 'juicy-chat-bot@0.8.0' -> 'vm2@3.9.17' | Produccion | Si | Cambiar la dependencia directa juicy-chat-bot a la version 0.7.1 | Esta version de juicy-chat-bot deberia resolver la vulnerabilidad de vm2. Si no es asi subir vm2 a la version 3.9.18 |

En el Lab1.Paso4 se ha decidido corregir la dependencia logback-classic cambiando la version a la 1.2.13
En el archivo trivy-correccion-lockback-classic.txt se puede ver que han desaparecido todas las vulnerabilidades relacionadas con lockback-classic

### npm.cmd audit
137 vulnerabilities (5 low, 21 moderate, 96 high, 15 critical)

### npm.cmd audit --omit=dev
82 vulnerabilities (3 low, 13 moderate, 54 high, 12 critical)

No pasan 55 vulnerabilidades


## Diferencia con/sin Lockfile
Al usar trivy con un lockfile el análisis encuentra 167, pero si no lo utilizamos el análisis pasa a devolver 0 vulnerabilidades. La diferencia entre usar o no package-lock.json es muy importante.


## Lab 3 · SAST sobre WebGoat
### 1. java.spring.security.injection.tainted-sql-string.tainted-sql-string

Clasificación: Real
Justificación: En el archivo se usa un campo String en vez de instanciarlo, puede haber inyección de código

### 2. html.security.plaintext-http-link.plaintext-http-link

Clasificación: Falso positivo
Justificación: El riesgo es mínimo porque el link es solo informativo

### 3. yaml.github-actions.security.github-actions-mutable-action-tag.github-actions-mutable-action-tag

Clasificación: Real
Justificación: Se estan usando etiquetas mutables/modificables en githubActions que pueden suponer riesgos 

### 4. java.lang.security.audit.crypto.use-of-md5.use-of-md5

Clasificación: Real
Justificación: Se está usando MD5 para el hash, que es inseguro hoy en dia

### 5. package_managers.dependabot.dependabot-missing-cooldown.dependabot-missing-cooldown

Clasificación: Real
Justificación: Debería haber un tiempo de espera antes de descargar una actualización, por si es maliciosa


## Tiempos Dia1
__Lab1__: 2h 10 min
__Lab2__: 1h 30 min
__Lab3__: 45 min