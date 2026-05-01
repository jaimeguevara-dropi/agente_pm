# AS-IS - SILIN - Procesamiento inteligente y parcial de archivos FT

## Nombre del proyecto
SILIN - Procesamiento inteligente FT

## Propósito de este AS-IS
Este documento consolida el proceso operativo actual mediante el cual SILIN, junto con las áreas de Tributaria, Analítica, Datos y Producto, recibe, valida, limpia, transforma, procesa y habilita archivos FT para que puedan alimentar la cadena tributaria.

El objetivo de este AS-IS es representar cómo funciona hoy el proceso real, con sus validaciones manuales, pasos técnicos, dependencias entre equipos, ciclos de devolución y aprobación, y controles posteriores hasta llegar a producción.

## Resumen ejecutivo del proceso actual
Hoy el procesamiento de archivos FT en SILIN es un proceso secuencial, altamente dependiente de intervención humana, con múltiples validaciones manuales y técnicas distribuidas entre varias áreas.

El flujo actual no consiste simplemente en cargar un archivo y procesarlo. El archivo pasa por una cadena de revisión, validación, limpieza, transformación, validación sistémica, dispersión, revisión funcional en staging y finalmente replicación en producción.

A lo largo del proceso:
- Tributaria actúa como primer filtro funcional, normativo y jurídico,
- Analítica realiza correcciones, limpieza y transformaciones técnicas,
- Datos ejecuta validación sistémica y dispersión dentro del ecosistema SILIN,
- Tributaria valida el resultado funcional en staging,
- y solo después de su aprobación se autoriza el paso a producción.

## Naturaleza actual del proceso
El proceso actual tiene las siguientes características estructurales:

- es intensivo en trabajo manual,
- depende de validaciones fuera del sistema,
- se apoya fuertemente en Excel, archivos locales, consultas y revisión humana,
- tiene ciclos iterativos de devolución y corrección,
- involucra múltiples handoffs entre equipos,
- mezcla controles técnicos, operativos y jurídico-tributarios,
- y su velocidad depende en buena parte de la calidad del archivo recibido y de la capacidad de recuperación manual de datos.

## Actores principales
### Comercializadora
Entrega los archivos FT en SILIN o en las rutas operativas definidas.

### Tributaria
Actúa como primer filtro de negocio y cumplimiento formal. Revisa estructura, consistencia tributaria básica, cruces iniciales y decide si un archivo puede continuar o debe ser rechazado.

### Producto
Puede intervenir dando lineamientos sobre el inicio de ciertos procesos o consideraciones adicionales para la limpieza.

### Analítica
Recibe archivos autorizados, realiza limpieza y transformación, recupera datos manualmente cuando es posible, ejecuta validaciones técnicas y disponibiliza salidas válidas para continuar.

### Datos
Ejecuta la validación sistémica y la dispersión del archivo dentro del ecosistema SILIN, usando endpoints, rutas S3, web sockets y registros en base de datos.

### Tributaria post-cargue
Valida funcionalmente en staging que lo procesado por el sistema represente correctamente la realidad tributaria antes de autorizar producción.

## Fase 1 - Recepción lógica del archivo FT-01 por Tributaria
El proceso inicia cuando la comercializadora carga el archivo FT-01 en el portal o ruta correspondiente. Tributaria no participa en el cargue, no controla el momento exacto en que ocurre y no realiza validaciones automáticas en esta etapa.

Desde la perspectiva de Tributaria:
- el archivo ya existe en el sistema cuando ellos entran en acción,
- el archivo está disponible para revisión,
- todavía no ha sido aprobado,
- no ha sido autorizado para procesamiento,
- y no ha sido enviado al equipo de Datos.

El inicio real del trabajo ocurre cuando Tributaria descarga el archivo y lo lleva a un entorno local para revisión.

## Fase 2 - Revisión estructural y validación inicial por Tributaria
Una vez descargado, Tributaria abre el archivo en Excel y realiza una validación completamente manual. Esta fase tiene un alcance operativo y jurídico-tributario.

No se revisa solo si el archivo “abre”, sino si cumple con el requerimiento ordinario de información.

Entre las validaciones principales están:
- delimitador correcto,
- cantidad esperada de columnas,
- orden correcto de columnas,
- correspondencia con el requerimiento vigente,
- revisión básica de formatos y campos obligatorios,
- cruce inicial entre FT-01 y FT-03 cuando aplica,
- verificación de consistencia entre lo liquidado y lo recaudado.

El análisis se apoya en Excel, tablas dinámicas, sumatorias manuales y comparaciones directas.

Durante esta fase también se registran inconsistencias, periodos, rechazos y pendientes en archivos internos de seguimiento.

Si se encuentran inconsistencias, Tributaria comunica formalmente observaciones a la comercializadora. Estas observaciones no se entienden solo como errores técnicos, sino como posibles incumplimientos al deber formal de información.

Al cierre de esta fase, el archivo solo puede quedar en uno de dos estados:
- Validado por Tributaria
- Rechazado por Tributaria

No existen estados intermedios formales.

## Fase 3 - Recepción del archivo por Analítica
Una vez existe autorización para continuar, Analítica toma el archivo desde las rutas operativas en S3. Dependiendo del caso:
- puede tomarlo desde una carpeta de procesados revisados por Tributaria,
- o, cuando el archivo es muy grande, puede trabajar desde no procesados bajo una lógica distinta de priorización por periodos.

El proceso está atado a historias de usuario y seguimiento operativo en Azure DevOps.

## Fase 4 - Limpieza y transformación por Analítica
Analítica realiza una revisión técnica y de calidad de datos sobre el archivo.

Entre las actividades actuales están:
- corrección manual de separadores,
- corrección de codificación a UTF-8,
- validación de cantidad de campos,
- revisión de columnas trocadas,
- revisión de caracteres extraños,
- revisión de datos faltantes o errados,
- validación de códigos DANE,
- identificación de duplicados,
- identificación de exentos,
- recuperación manual de datos,
- consulta con Tributaria cuando faltan datos o el sentido del dato no es claro.

Cuando el volumen es muy alto o la validación manual no es viable, se usa una máquina virtual en AWS que ejecuta:
- validación estructural,
- generación de archivo validado,
- generación de archivo `.parquet`,
- y transformación con reglas predefinidas.

Luego del proceso, Analítica revisa resultados en CloudWatch y obtiene archivos de válidos e inválidos. Estos resultados se envían a Tributaria para validación y aceptación.

Si Tributaria no acepta el resultado:
- se ajusta,
- se corrige,
- se reprocesa,
- y se vuelve a enviar.

Cuando se aceptan los válidos, estos se cargan nuevamente a S3 para continuar el flujo y se notifica a los siguientes equipos por Slack.

## Fase 5 - Validación sistémica y dispersión por Datos
El área de Datos recibe la ruta del archivo procesado y autorizado. A partir de allí:
- descarga el archivo,
- revisa estructura mínima,
- renombra el archivo con UUID según exigencia de SILIN,
- lo carga en la ruta S3 correspondiente,
- y ejecuta endpoints de validación.

La validación sistémica revisa:
- formatos por columna,
- reglas mínimas de procesabilidad,
- conteo de filas,
- errores de formato,
- y cumplimiento de reglas parametrizadas en base de datos.

Si la validación falla, el proceso no continúa hasta corregir el archivo.
Si la validación es exitosa, se genera un identificador de cargue o validación.

Con ese identificador, Datos ejecuta la dispersión. Como resultado, el sistema puede:
- crear contribuyentes,
- crear suscripciones,
- crear consumos,
- registrar movimientos del impuesto calculado,
- y asociar impuestos con consumos creados.

En FT-03 ocurre una lógica similar, con validación, dispersión, consulta de resultados y control de registros procesados, errores y estados parciales.

Al finalizar, Datos genera reportes de movimientos desde base de datos y los comparte a Tributaria para revisión.

## Fase 6 - Validación funcional tributaria post-cargue en staging
Cuando la validación sistémica y la dispersión terminan, la información ya existe en el sistema, pero todavía no es definitiva.

En staging, Tributaria revisa el resultado funcional del proceso y valida que:
- el impuesto calculado corresponda al consumo reportado,
- las reglas tributarias se hayan aplicado correctamente,
- los recaudos estén donde corresponde,
- los saldos tengan sentido,
- y no existan inconsistencias relevantes frente a controles históricos.

Para archivos pequeños puede hacerse validación más detallada.
Para archivos grandes se trabaja por muestras, patrones y totales.

Al cierre de esta fase, Tributaria emite una decisión:
- Aprobado en Staging
- Observado

Si es observado, el proceso vuelve al equipo técnico y no avanza a producción.

## Fase 7 - Subida a producción y habilitación de la cadena tributaria
Si Tributaria aprueba en staging, el equipo técnico repite el flujo técnico en producción.

Esto implica ejecutar nuevamente:
- validación,
- dispersión,
- y cargue en ambiente productivo.

Cuando el cargue en producción finaliza correctamente:
- los consumos quedan oficialmente registrados,
- los impuestos quedan causados,
- los recaudos quedan aplicados,
- las deudas quedan visibles en cartera,
- y se habilitan procesos tributarios posteriores como facturación, gestión de cartera, acuerdos de pago, cobro coactivo y demás procesos dependientes.

En este punto el archivo deja de ser un insumo técnico en revisión y pasa a convertirse en base oficial de la operación.

## Herramientas y medios utilizados hoy
El proceso actual depende de una combinación de herramientas y medios dispersos:

- Portal SILIN
- Excel
- almacenamiento local
- AWS S3
- máquina virtual en AWS
- CloudWatch
- Azure DevOps
- Slack
- consultas a base de datos
- Postman / endpoints / web sockets

## Estados y decisiones relevantes del proceso actual
A lo largo del flujo actual existen múltiples puntos de decisión:

- archivo pendiente de validación por Tributaria,
- archivo validado o rechazado por Tributaria,
- archivo corregido o devuelto a comercializadora,
- resultado válido o inválido en Analítica,
- archivo listo o no listo para staging,
- validación sistémica exitosa o fallida,
- dispersión exitosa, parcial o no procesada,
- aprobado u observado en staging,
- cargue productivo exitoso o con necesidad de reproceso.

## Dependencias críticas del proceso actual
El AS-IS actual depende fuertemente de:
- la calidad inicial del archivo entregado por la comercializadora,
- la revisión manual de Tributaria,
- la capacidad de recuperación manual de Analítica,
- la ejecución técnica por Datos,
- la trazabilidad operativa en Slack, Azure DevOps y archivos internos,
- y la aprobación funcional final de Tributaria antes de producción.

## Principales fricciones y cuellos de botella del AS-IS
Las principales fricciones observables hoy son:

- alta dependencia de intervención humana,
- validación manual intensiva en Excel,
- corrección local y fuera del sistema,
- múltiples cambios de mano entre equipos,
- necesidad de recuperación manual de datos,
- iteraciones repetidas entre Analítica y Tributaria,
- dependencia de rutas, ambientes y pasos operativos delicados,
- reprocesos ante errores parciales,
- y dificultad para operar rápidamente cuando los archivos son muy grandes o tienen mala calidad.

## Lectura general del AS-IS
El proceso actual sí permite que los archivos FT lleguen finalmente a producción y habiliten la cadena tributaria, pero lo hace a través de una operación compleja, manual, altamente dependiente del conocimiento experto y con varias validaciones distribuidas entre negocio y tecnología.

Esto significa que hoy el valor del proceso no está solo en recibir archivos, sino en la capacidad humana de:
- interpretarlos,
- depurarlos,
- corregirlos,
- decidir si pueden continuar,
- validar lo que el sistema hizo,
- y autorizar su impacto real en la operación tributaria.

## Conclusión del AS-IS
Hoy el procesamiento de archivos FT en SILIN funciona como una cadena operativa híbrida entre validación tributaria, limpieza técnica, procesamiento sistémico y aprobación funcional final.

Es un proceso viable, pero costoso en esfuerzo humano, sensible a errores parciales, dependiente de herramientas externas y con varios puntos donde el avance puede frenarse o devolverse.

Este AS-IS sirve como base para diseñar un TO-BE donde el procesamiento sea más automatizado, más resiliente, más escalable y menos dependiente de revisión manual intensiva.
