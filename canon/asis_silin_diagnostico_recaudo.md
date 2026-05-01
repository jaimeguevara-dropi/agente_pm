---
type: asis
project: SILIN - Diagnóstico de liquidación y potencial de recaudo
status: active
version: 2.0
last_updated: 2026-04-23
---

# AS-IS - SILIN - Diagnóstico de liquidación y potencial de recaudo

## Nombre del proyecto
SILIN - Diagnóstico de liquidación y potencial de recaudo

## Propósito de este AS-IS
Este documento consolida el estado actual del proceso mediante el cual la información tributaria proveniente de archivos FT es recibida, revisada, corregida, transformada, cargada, liquidada y validada dentro del ecosistema SILIN, antes de cualquier visualización de valor económico para una alcaldía.

El objetivo de este AS-IS es representar cómo funciona hoy el proceso real, identificando actores, pasos operativos, dependencias, reprocesos, controles manuales, cuellos de botella y restricciones que explican por qué actualmente no existe un flujo ágil, trazable y comercialmente usable para demostrar de forma inmediata el potencial de recaudo de un municipio. El estado actual está distribuido entre revisión tributaria manual, limpieza y homologación analítica, validación y dispersión técnica en SILIN, y aprobación humana posterior antes de producción.

## Resumen ejecutivo del proceso actual
Hoy el valor económico que podría mostrarse a una alcaldía no surge de un módulo de diagnóstico directo ni de una experiencia preparada para venta o autoservicio. Surge, en cambio, de una cadena operativa fragmentada donde varias áreas deben intervenir de forma secuencial para que un archivo FT llegue a una liquidación utilizable.

El flujo comienza con el cargue de archivos por parte de la comercializadora en un portal, sigue con validaciones iniciales manuales por parte de tributaria en Excel, pasa luego por un proceso de limpieza y transformación altamente manual liderado por analítica, continúa con una validación técnica y dispersión en SILIN operada por datos/base de datos mediante endpoints y procesos asíncronos, y termina con reportes, revisiones humanas, aprobaciones en staging y repetición en producción. El resultado final es una operación viable, pero costosa en tiempo, altamente dependiente de personas clave y poco apta para mostrar valor comercial inmediato.

## Naturaleza actual del proceso
El proceso actual tiene estas características estructurales:
- está altamente fragmentado entre equipos;
- depende de validaciones manuales y revisiones visuales;
- combina herramientas no integradas como portal, Excel, S3, Slack, LACA, Postman, scripts Python y procedimientos de base de datos;
- requiere múltiples reprocesos cuando se detectan errores;
- no permite aprovechar tempranamente la parte válida de la información con una experiencia de negocio clara;
- y no ofrece una visualización inmediata y confiable del potencial de recaudo lista para uso comercial.

En el estado actual, la plataforma no funciona como una herramienta autónoma de diagnóstico. Funciona como una cadena técnica-operativa que debe ser empujada y validada manualmente en varios puntos antes de obtener un resultado confiable.

## Actores principales del AS-IS

**Comercializadora**
Carga archivos FT en el portal o los entrega según el esquema operativo vigente. También participa en los ciclos de corrección cuando la información es rechazada o requiere recargue.

**Equipo de Tributaria**
Actúa como primer filtro funcional y de negocio. Revisa manualmente los archivos, valida estructura, formatos, completitud, extemporaneidad y coherencia básica, realiza cruces entre FT-01, FT-03 y FT-05, registra hallazgos en Excel y aprueba o rechaza la información para avanzar. También revisa reportes de staging y producción.

**Equipo de Analítica**
Recibe archivos preaprobados o casos especiales, ejecuta limpieza y transformación, corrige delimitadores y codificación, revisa visualmente registros, recupera datos manualmente desde históricos, corre servicios y scripts, genera archivos válidos e inválidos, y entrega salidas listas para consumo técnico posterior.

**Equipo de Datos / Base de Datos / SILIN**
Toma los archivos validados por analítica, ejecuta validación técnica estructural y funcional mínima por endpoint, procesa la dispersión y liquidación en SILIN, genera errores y reportes, y habilita los datos para staging y luego producción. También asume reprocesos operativos cuando fallan conexiones o triggers.

**Producto / Liderazgo técnico**
Dispara o coordina algunos procesamientos, actúa como puente cuando hay discrepancias entre reglas de analítica, tributaria y SILIN, y ayuda a resolver devoluciones o ajustes de criterios.

## Fase 1 - Cargue inicial y validación manual tributaria
El proceso actual inicia cuando la comercializadora carga archivos FT en el portal, normalmente FT-01, FT-03 y FT-05, junto con documentos de soporte como certificaciones o constancias de transferencia. Aunque el portal debería servir como punto de validación temprana, hoy en la práctica funciona más como repositorio de recepción que como motor de control. La detección automática de inconsistencias no resuelve el problema operativo principal.

Después del cargue, el equipo de tributaria descarga manualmente los archivos, los abre en Excel y realiza validaciones visuales y funcionales básicas: estructura de columnas, orden, tipos de datos, campos obligatorios, delimitadores, formatos, completitud y extemporaneidad. También realiza cruces manuales entre FT-01, FT-03 y FT-05 para detectar diferencias de recaudo, cartera y valores a facturar o saldos a favor. Este trabajo consume gran parte del tiempo del equipo, apoyándose además en archivos de control en Excel para seguimiento de hallazgos y transferencias.

Cuando encuentra inconsistencias, tributaria documenta observaciones y las comunica por correo. La comercializadora debe pedir la baja del archivo, corregirlo y volver a cargarlo. Entonces tributaria repite todo el ciclo de descarga y validación. Esta dinámica hace que el proceso sea lento, repetitivo y propenso a errores humanos.

## Fase 2 - Limpieza, homologación y validación previa por analítica
Una vez tributaria considera que un archivo puede avanzar, el área de analítica entra al proceso. El analista descarga el archivo desde S3, hace copias locales, corrige problemas de codificación y delimitadores, valida visualmente la cantidad de campos y examina anomalías como valores atípicos, identificaciones inválidas, caracteres extraños o datos faltantes. Cuando puede, corrige manualmente; cuando no, consulta a tributaria o intenta recuperar información desde bases históricas y archivos previos.

Luego habilita servicios locales, ejecuta procesadores, sube nuevamente el archivo a rutas específicas de S3 y dispara una cadena automatizada que genera salidas de válidos e inválidos. Sin embargo, esta fase sigue siendo muy dependiente del analista: hay validaciones “a ojímetro”, conflictos de puertos, procesos que dependen de rutas temporales en S3, y recuperación de datos basada en búsquedas manuales. Para archivos grandes o incumbentes, el proceso se vuelve todavía más pesado, obligando a cruzar múltiples periodos y resolver desalineaciones con scripts o intervenciones manuales adicionales. También existen reglas especiales, como la diferenciación entre FT-01 y FT-06 o el cruce manual entre FT-03 y FT-01.

Después de la transformación, analítica envía los resultados a tributaria para revisión. Si tributaria encuentra problemas de negocio, pide cambios y analítica reprocesa. Si aprueba, el archivo “válido” se sube a una ruta final para que el equipo de datos lo tome. Esta fase no produce todavía una experiencia de diagnóstico visible para alcaldías; produce un insumo técnico depurado.

## Fase 3 - Validación técnica, dispersión y liquidación en SILIN
Con el archivo ya preparado, el equipo de datos o base de datos ejecuta la siguiente etapa en SILIN. Primero mueve o renombra manualmente el archivo y lo deja en una ruta S3 específica. Luego invoca endpoints desde Postman para validar el archivo y, si la validación pasa, ejecuta un segundo endpoint para la dispersión. Este proceso requiere parámetros técnicos, tokens y en algunos casos archivos adicionales de certificación que hoy no agregan valor real, pero siguen siendo obligatorios.

Durante esta fase, SILIN valida la estructura del archivo, genera un identificador de cargue y procesa el contenido por lotes. En FT-01 crea contribuyentes, suscripciones, consumos y movimientos del impuesto calculado; en FT-03 aplica pagos a deudas. La liquidación del impuesto se ejecuta usando fórmulas, tarifas y parámetros configurados en base de datos por entidad y vigencia. El resultado queda como causación o deuda lista para procesos posteriores.

Sin embargo, esta etapa también tiene problemas fuertes: el monitoreo del procesamiento depende de WebSockets o revisión manual de sesiones de base de datos; los errores pueden ser genéricos; si se cae la conexión o falla el proceso, se debe limpiar manualmente la base de datos y volver a cargar con otro nombre; y los cargues grandes pueden bloquearse por conflictos de triggers y vistas materializadas, obligando a desactivar triggers en horario nocturno, repetir el proceso y reconstruir vistas. Esto limita severamente la estabilidad operativa y retrasa la disponibilidad de resultados.

## Fase 4 - Reporte, revisión humana y paso a producción
Una vez terminado el procesamiento en staging, se genera un reporte desde la base de datos con contribuyentes, suscripciones, consumos, impuesto calculado, recaudos y otros datos relevantes. Ese reporte se envía a tributaria por Slack o canales equivalentes para revisión y aprobación. Tributaria contrasta la información con sus registros y, normalmente por muestreo o revisión funcional, decide si el cargue puede aprobarse o debe corregirse. Si hay observaciones, se abre un nuevo ciclo de reproceso. Si aprueba, se repite el cargue completo en producción.

Después de la carga productiva, tributaria vuelve a revisar consistencia y, finalmente, en algunos casos revisa incluso las facturas generadas. Es decir, la confianza en el resultado no proviene de una trazabilidad automática robusta y visible desde el inicio, sino de validaciones humanas repetidas a lo largo del camino.

## Cómo se demuestra hoy el valor económico
Hoy no existe un módulo claro, autónomo y rápido que permita mostrar a una alcaldía el potencial de recaudo apenas se recibe y procesa la información. Lo que existe es una cadena de procesamiento cuyo resultado final puede derivar en reportes técnicos y liquidaciones, pero solo después de varias validaciones, cruces, correcciones y aprobaciones entre equipos. En la práctica, la demostración de valor está mediada por operaciones manuales y tiempos largos, no por una experiencia de producto preparada para diagnóstico comercial inmediato.

## Herramientas y medios usados hoy
El AS-IS actual depende de una combinación de herramientas y medios dispersos:
- Portal de Empresas de Energía
- Excel
- Correo electrónico
- Slack
- LACA / Alzu
- Buckets S3
- AWS CLI
- Scripts Python y SH
- Servicios locales y remotos
- Postman
- Endpoints de validación y dispersión
- Procedimientos y tablas de base de datos
- Reportes en Excel

Esta dispersión tecnológica hace que el proceso dependa más de coordinación humana que de una experiencia integrada de plataforma.

## Dependencias críticas del proceso actual
El proceso actual depende fuertemente de:
- la calidad del archivo entregado por la comercializadora;
- la revisión manual de tributaria;
- la capacidad del analista para corregir y recuperar datos;
- la estabilidad de servicios y rutas intermedias;
- la ejecución correcta de endpoints y tokens;
- la capacidad de la base de datos para soportar cargues grandes;
- y la aprobación humana en staging antes de producción.

## Principales fricciones y cuellos de botella del AS-IS
Las fricciones más importantes son:
- validación inicial manual en Excel;
- necesidad de correo y recargue completo ante rechazo;
- transformación intermedia manual y dependiente de conocimiento experto;
- recuperación manual de datos históricos;
- desalineación entre reglas de tributaria, analítica y SILIN;
- monitoreo técnico manual del procesamiento;
- errores genéricos y reintentos costosos;
- bloqueo del procesamiento por cargues grandes;
- y ausencia de una salida comercial clara, trazable y rápida para mostrar valor a una alcaldía.

## Lectura general del AS-IS
Hoy el proceso sí logra, en ciertos casos, llevar información FT hasta liquidación y disponibilidad en SILIN. Pero lo hace mediante una cadena operativa costosa, lenta, dependiente de personas clave y con baja capacidad para generar una experiencia inmediata de diagnóstico. El valor no está listo para mostrarse apenas entra el archivo; depende de que varias áreas limpien, interpreten, procesen, validen y aprueben la información. En ese sentido, el AS-IS actual es funcionalmente posible, pero comercialmente débil y operativamente frágil.

## Conclusión del AS-IS
El estado actual del proyecto no corresponde a un módulo de diagnóstico de liquidación y potencial de recaudo, sino a una cadena manual y fragmentada de preparación, validación, dispersión, liquidación y revisión. Esa cadena permite eventualmente llegar a resultados utilizables, pero no en tiempos ni con la claridad requeridos para convertirla en una herramienta inicial de venta para alcaldías.

Este AS-IS sirve como base para diseñar un TO-BE donde la plataforma pueda:
- recibir información FT ya estructuralmente válida;
- reducir los reprocesos manuales;
- procesar parcialmente sin bloquear el valor útil;
- consolidar trazabilidad y estados;
- ejecutar la liquidación de forma más controlada;
- y mostrar rápidamente el potencial de recaudo de un municipio en una experiencia comprensible, confiable y comercialmente potente.
