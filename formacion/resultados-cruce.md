
# Respuestas a las preguntas (copiado de la consola)



## 1. Alertas frente a avisos distintos en cada fuente 
| Fuente | Alertas | Avisos distintos |
|---|---|---|
| Dependabot  | 6  |  6 |
|  Trivy | 155  | 148  |


## 2. Qué encuentra una fuente y no la otra (cuidado: Dependabot usa GHSA y Trivy suele usar CVE) 
Solo Dependabot: 6 aviso(s)
            id              paquetes                ghsa            cve manifiesto severidad
CVE-2016-10735 org.webjars:bootstrap GHSA-4p24-vmcr-4gqj CVE-2016-10735    pom.xml    medium
CVE-2018-14040 org.webjars:bootstrap GHSA-3wqf-4x89-9g79 CVE-2018-14040    pom.xml    medium
CVE-2018-14042 org.webjars:bootstrap GHSA-7mvr-5x2g-wfc8 CVE-2018-14042    pom.xml    medium
CVE-2018-20676 org.webjars:bootstrap GHSA-3mgp-fx93-9xv5 CVE-2018-20676    pom.xml    medium
CVE-2018-20677 org.webjars:bootstrap GHSA-ph58-4vrj-w6hr CVE-2018-20677    pom.xml    medium
 CVE-2019-8331 org.webjars:bootstrap GHSA-9v3m-8fp8-mj99  CVE-2019-8331    pom.xml    medium


 Solo Trivy: 148 aviso(s)
              id                                                                                                              paquetes        version fichero severidad
CVE-2016-1000027                                                                                        org.springframework:spring-web          5.3.2 pom.xml  CRITICAL
  CVE-2020-36518                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml      HIGH
  CVE-2021-22060                                                                                       org.springframework:spring-core          5.3.2 pom.xml    MEDIUM
  CVE-2021-22096                                                                                       org.springframework:spring-core          5.3.2 pom.xml    MEDIUM
  CVE-2021-22118                                                                                        org.springframework:spring-web          5.3.2 pom.xml      HIGH
  CVE-2021-23463                                                                                                     com.h2database:h2        1.4.200 pom.xml      HIGH
   CVE-2021-2471                                                                                            mysql:mysql-connector-java         8.0.22 pom.xml    MEDIUM
  CVE-2021-25122                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2021-28170                                                                                              org.glassfish:jakarta.el          3.0.3 pom.xml    MEDIUM
  CVE-2021-42392                                                                                                     com.h2database:h2        1.4.200 pom.xml  CRITICAL
  CVE-2021-42550                                                                                           ch.qos.logback:logback-core          1.2.3 pom.xml    MEDIUM
  CVE-2021-43466                                                                                       org.thymeleaf:thymeleaf-spring5 3.0.11.RELEASE pom.xml  CRITICAL
  CVE-2021-46877                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml      HIGH
  CVE-2021-47621                                                                                       io.github.classgraph:classgraph         4.8.69 pom.xml    MEDIUM
   CVE-2022-1471                                                                                                    org.yaml:snakeyaml           1.27 pom.xml      HIGH
  CVE-2022-21363                                                                                            mysql:mysql-connector-java         8.0.22 pom.xml    MEDIUM
  CVE-2022-22950                                                                                 org.springframework:spring-expression          5.3.2 pom.xml    MEDIUM
  CVE-2022-22965 org.springframework.boot:spring-boot-starter-web, org.springframework:spring-beans, org.springframework:spring-webmvc   2.4.1, 5.3.2 pom.xml  CRITICAL
  CVE-2022-22968                                                                                    org.springframework:spring-context          5.3.2 pom.xml      HIGH
  CVE-2022-22970                                                                                      org.springframework:spring-beans          5.3.2 pom.xml      HIGH
  CVE-2022-23221                                                                                                     com.h2database:h2        1.4.200 pom.xml  CRITICAL
  CVE-2022-25857                                                                                                    org.yaml:snakeyaml           1.27 pom.xml      HIGH
  CVE-2022-38749                                                                                                    org.yaml:snakeyaml           1.27 pom.xml    MEDIUM
  CVE-2022-38750                                                                                                    org.yaml:snakeyaml           1.27 pom.xml    MEDIUM
  CVE-2022-38751                                                                                                    org.yaml:snakeyaml           1.27 pom.xml    MEDIUM
  CVE-2022-38752                                                                                                    org.yaml:snakeyaml           1.27 pom.xml    MEDIUM
  CVE-2022-41854                                                                                                    org.yaml:snakeyaml           1.27 pom.xml    MEDIUM
  CVE-2022-42003                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml      HIGH
  CVE-2022-42004                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml      HIGH
  CVE-2022-42252                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2022-45143                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2022-45868                                                                                                     com.h2database:h2        1.4.200 pom.xml      HIGH
   CVE-2023-1932                                                                           org.hibernate.validator:hibernate-validator    6.1.6.Final pom.xml    MEDIUM
  CVE-2023-20860                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml  CRITICAL
  CVE-2023-20861                                                                                 org.springframework:spring-expression          5.3.2 pom.xml    MEDIUM
  CVE-2023-20863                                                                                 org.springframework:spring-expression          5.3.2 pom.xml      HIGH
  CVE-2023-20873                                                           org.springframework.boot:spring-boot-actuator-autoconfigure          2.4.1 pom.xml  CRITICAL
  CVE-2023-20883                                                                    org.springframework.boot:spring-boot-autoconfigure          2.4.1 pom.xml      HIGH
  CVE-2023-22102                                                                                            mysql:mysql-connector-java         8.0.22 pom.xml      HIGH
  CVE-2023-24998                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2023-34055                                                                         org.springframework.boot:spring-boot-actuator          2.4.1 pom.xml    MEDIUM
  CVE-2023-41080                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2023-42795                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2023-44487                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2023-45648                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2023-46589                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
   CVE-2023-6378                                                           ch.qos.logback:logback-classic, ch.qos.logback:logback-core          1.2.3 pom.xml      HIGH
  CVE-2024-12798                                                                                           ch.qos.logback:logback-core          1.2.3 pom.xml    MEDIUM
  CVE-2024-12801                                                                                           ch.qos.logback:logback-core          1.2.3 pom.xml       LOW
  CVE-2024-21733                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2024-22243                                                                                        org.springframework:spring-web          5.3.2 pom.xml      HIGH
  CVE-2024-22259                                                                                        org.springframework:spring-web          5.3.2 pom.xml      HIGH
  CVE-2024-22262                                                                                        org.springframework:spring-web          5.3.2 pom.xml      HIGH
  CVE-2024-23672                                                                        org.apache.tomcat.embed:tomcat-embed-websocket         9.0.41 pom.xml    MEDIUM
  CVE-2024-24549                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2024-34750                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2024-38286                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2024-38808                                                                                 org.springframework:spring-expression          5.3.2 pom.xml    MEDIUM
  CVE-2024-38809                                                                                        org.springframework:spring-web          5.3.2 pom.xml    MEDIUM
  CVE-2024-38816                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml      HIGH
  CVE-2024-38819                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml      HIGH
  CVE-2024-38820                                                    org.springframework:spring-context, org.springframework:spring-web          5.3.2 pom.xml    MEDIUM
  CVE-2024-38828                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2024-50379                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2024-56337                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2025-11226                                                                                           ch.qos.logback:logback-core          1.2.3 pom.xml    MEDIUM
  CVE-2025-22233                                                                                    org.springframework:spring-context          5.3.2 pom.xml       LOW
  CVE-2025-22235                                                                                  org.springframework.boot:spring-boot          2.4.1 pom.xml      HIGH
  CVE-2025-24813                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml  CRITICAL
  CVE-2025-35036                                                                           org.hibernate.validator:hibernate-validator    6.1.6.Final pom.xml    MEDIUM
  CVE-2025-41242                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2025-41249                                                                                       org.springframework:spring-core          5.3.2 pom.xml      HIGH
  CVE-2025-46701                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml       LOW
  CVE-2025-48988                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2025-48989                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2025-49124                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2025-49125                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2025-49128                                                                               com.fasterxml.jackson.core:jackson-core         2.11.3 pom.xml    MEDIUM
  CVE-2025-52434                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2025-52520                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2025-52999                                                                               com.fasterxml.jackson.core:jackson-core         2.11.3 pom.xml      HIGH
  CVE-2025-53506                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2025-55668                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2025-55752                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2025-55754                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml       LOW
  CVE-2025-61795                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml       LOW
  CVE-2025-66614                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2026-10532                                                                                           ch.qos.logback:logback-core          1.2.3 pom.xml       LOW
   CVE-2026-1225                                                                                           ch.qos.logback:logback-core          1.2.3 pom.xml       LOW
  CVE-2026-19032                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml    MEDIUM
  CVE-2026-22733                                                                 org.springframework.boot:spring-boot-starter-actuator          2.4.1 pom.xml      HIGH
  CVE-2026-22735                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml       LOW
  CVE-2026-22737                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2026-22741                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml       LOW
  CVE-2026-22745                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2026-24880                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2026-25854                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2026-34483                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2026-34487                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2026-40477                                                              org.thymeleaf:thymeleaf, org.thymeleaf:thymeleaf-spring5 3.0.11.RELEASE pom.xml  CRITICAL
  CVE-2026-40478                                                              org.thymeleaf:thymeleaf, org.thymeleaf:thymeleaf-spring5 3.0.11.RELEASE pom.xml  CRITICAL
  CVE-2026-40973                                                                                  org.springframework.boot:spring-boot          2.4.1 pom.xml      HIGH
  CVE-2026-40984                                                                                         io.micrometer:micrometer-core          1.6.2 pom.xml      HIGH
  CVE-2026-41284                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2026-41293                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml  CRITICAL
  CVE-2026-41711                                                                          org.springframework.data:spring-data-commons          2.4.2 pom.xml    MEDIUM
  CVE-2026-41716                                                                          org.springframework.data:spring-data-commons          2.4.2 pom.xml      HIGH
  CVE-2026-41721                                                                          org.springframework.data:spring-data-commons          2.4.2 pom.xml    MEDIUM
  CVE-2026-41841                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2026-41842                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml      HIGH
  CVE-2026-41843                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2026-41844                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2026-41845                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml      HIGH
  CVE-2026-41846                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2026-41848                                                                                       org.springframework:spring-core          5.3.2 pom.xml       LOW
  CVE-2026-41849                                                                                 org.springframework:spring-expression          5.3.2 pom.xml      HIGH
  CVE-2026-41850                                                                                 org.springframework:spring-expression          5.3.2 pom.xml      HIGH
  CVE-2026-41851                                                                                 org.springframework:spring-expression          5.3.2 pom.xml    MEDIUM
  CVE-2026-41852                                                                                 org.springframework:spring-expression          5.3.2 pom.xml       LOW
  CVE-2026-41853                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml    MEDIUM
  CVE-2026-41901                                                              org.thymeleaf:thymeleaf, org.thymeleaf:thymeleaf-spring5 3.0.11.RELEASE pom.xml  CRITICAL
  CVE-2026-42498                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2026-43512                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml  CRITICAL
  CVE-2026-43513                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2026-43514                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml       LOW
  CVE-2026-43515                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml  CRITICAL
  CVE-2026-47884                                                                                     org.springframework:spring-webmvc          5.3.2 pom.xml  CRITICAL
  CVE-2026-49844                                                                                    org.apache.logging.log4j:log4j-api         2.13.3 pom.xml    MEDIUM
  CVE-2026-50193                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml    MEDIUM
  CVE-2026-53404                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2026-54512                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml      HIGH
  CVE-2026-54513                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml      HIGH
  CVE-2026-54514                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml    MEDIUM
  CVE-2026-54515                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml    MEDIUM
  CVE-2026-55276                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml  CRITICAL
  CVE-2026-55956                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml    MEDIUM
  CVE-2026-55957                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml      HIGH
  CVE-2026-59889                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml    MEDIUM
  CVE-2026-65182                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml  CRITICAL
  CVE-2026-65905                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml  CRITICAL
  CVE-2026-68494                                                                               com.fasterxml.jackson.core:jackson-core         2.11.3 pom.xml      HIGH
  CVE-2026-68525                                                                             org.apache.tomcat.embed:tomcat-embed-core         9.0.41 pom.xml  CRITICAL
  CVE-2026-77310                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml    MEDIUM
  CVE-2026-83557                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml    MEDIUM
  CVE-2026-89425                                                                               com.fasterxml.jackson.core:jackson-core         2.11.3 pom.xml      HIGH
  CVE-2026-91776                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml      HIGH
  CVE-2026-91777                                                                           com.fasterxml.jackson.core:jackson-databind         2.11.3 pom.xml      HIGH
   CVE-2026-9828                                                                                           ch.qos.logback:logback-core          1.2.3 pom.xml       LOW

Trivy ha encontrado muchas mas alertas/avisos que dependabot

## 3. Los cinco paquetes que concentran más avisos 
| Paquete | Avisos distintos |
|---|---|
| org.apache.tomcat.embed:tomcat-embed-core  | 47  |
|  org.springframework:spring-webmvc | 18  |
| com.fasterxml.jackson.core:jackson-databind  | 15  |
|  ch.qos.logback:logback-core | 8  |
| org.springframework:spring-expression  | 8  |

