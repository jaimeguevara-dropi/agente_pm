# AS-IS - SILIN - Diagnóstico de liquidación y potencial de recaudo

El proceso actual es un anti-patrón de integración, altamente fragmentado, manual y propenso a errores. Se compone de las siguientes fases principales:

## Carga y Revisión Tributaria
Las comercializadoras suben archivos TXT a un portal (repositorio simple). Tributaria descarga y revisa manualmente en Excel (delimitadores, columnas, formatos). Realiza cruces manuales (consumo vs recaudo) e identifica inconsistencias "a ojímetro". Si hay errores, se notifica a la comercializadora por correo solicitando la eliminación y recarga completa del archivo, deteniendo el flujo para todos los registros, incluso los válidos.

## Revisión y Limpieza por Analítica de Datos
El equipo de analítica (Julián) recibe archivos "prevalidados" por tributaria o directamente de incumbentes. Realiza una inspección visual y cruces manuales (FT-03 vs FT-01) para recuperar datos erróneos de periodos anteriores. Posteriormente sube el archivo a S3 para que un Lambda valide la estructura. Para que la base de datos lo acepte, elimina manualmente columnas que generan desalineación con el esquema de Base de Datos.

## Validación y Dispersión en Base de Datos (SILIN)
El equipo de Base de Datos (Sammy/Anyela) ejecuta la validación estructural vía Postman. Si pasa, se ejecuta un endpoint de "dispersión" (que requiere de adjuntos manuales como un pdf de seguridad inoperativo). El proceso interno de SILIN procesa en lotes, liquida el impuesto y actualiza vistas materializadas. Sin embargo, para archivos grandes (>500 registros), los triggers concurrentes bloquean la base de datos, lo que obliga a la eliminación de cargues, desactivación manual de triggers y reprocesos nocturnos.

## Cierre y Confirmación
Dado que el proceso es asíncrono y los websockets suelen desconectarse, la confirmación final se obtiene ejecutando un script de base de datos que exporta un reporte en Excel. Este reporte se envía por Slack a Tributaria para su revisión (muestral) y aprobación, previa a su pase al entorno de producción.
