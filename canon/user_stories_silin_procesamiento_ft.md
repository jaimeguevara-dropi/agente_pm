# User Stories - SILIN - Procesamiento inteligente FT

## Proyecto

SILIN - Procesamiento inteligente FT

## Propósito

Este documento consolida las historias de usuario normalizadas del proyecto, alineadas a las capacidades / épicas aprobadas. Incluye HUs activas, HUs fusionadas por duplicidad y elementos en revisión de alcance.

## Criterio de normalización

- `Active`: historia alineada al alcance vigente.

- `Merged`: historia duplicada o absorbida por otra HU más completa.

- `Scope Review`: historia útil, pero pendiente de decisión de alcance.

- `Needs Review`: requiere validación antes de quedar como HU activa.

- `Spike`: trabajo de análisis técnico o descubrimiento.


---

## CAP-FT-001 - Recepción de Lotes FT


### US-FT-001-001 - Recepción de archivos mayores a 6MB

- **Original Key:** 52716 / BRAI-174

- **Source Epic:** 52716

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema de procesamiento de información, quiero recibir y gestionar lotes de datos superiores a 6MB, para permitir la carga completa de información sin restricciones de tamaño que afecten la operación.


**Criterios de aceptación / escenarios consolidados**

Debe aceptar archivos mayores a 6MB, procesar la totalidad del lote sin pérdida de información, manejar errores de estructura o contenido sin caída del sistema, mantener estabilidad ante múltiples lotes grandes y confirmar recepción con trazabilidad.


**Notas**

Se mantiene dentro de CAP-FT-001 porque habilita la recepción técnica de lotes grandes.


### US-FT-001-002 - Recepción de archivos FT vía endpoint desde Plataforma SILIN

- **Original Key:** 52716

- **Source Epic:** 52716

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero exponer un endpoint técnico seguro para que Plataforma SILIN envíe archivos FT recibidos desde el portal, para encapsularlos como lote FT y registrarlos en el pipeline con trazabilidad desde el origen.


**Criterios de aceptación / escenarios consolidados**

Debe recibir archivo y metadatos mínimos; crear lote único; asignar identificador; registrar canal API_SILIN; marcar estado RECIBIDO; persistir entidad, periodo, comercializadora y tipo FT; no ejecutar validaciones estructurales, funcionales ni tributarias en esta etapa.


**Notas**

Esta HU reemplaza a la recepción genérica desde canales habilitados.


### US-FT-001-003 - Identificación única del lote FT

- **Original Key:** 52716

- **Source Epic:** 52716

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero asignar un identificador único a cada lote recibido, para permitir trazabilidad, reprocesamiento y seguimiento del ciclo de vida del lote.


**Criterios de aceptación / escenarios consolidados**

Debe generar identificador único al crear el lote; persistirlo en todo el flujo; permitir asociar reprocesos al lote original; agregar etiquetas operativas sin alterar la identidad del lote.


**Notas**

El identificador del lote debe ser inmutable.


### US-FT-001-004 - Asociación del lote a contexto tributario

- **Original Key:** 52716

- **Source Epic:** 52716

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero asociar cada lote a comercializadora, entidad y periodo tributario, para asegurar coherencia del procesamiento posterior con el contexto normativo.


**Criterios de aceptación / escenarios consolidados**

Debe asociar comercializadora, entidad y periodo cuando la información exista; si falta información mínima, el lote no debe avanzar a validación y debe quedar registrado como inconsistente.


**Notas**

Aunque menciona contexto tributario, aquí no se ejecutan validaciones tributarias profundas.


### US-FT-001-005 - Recepción de archivo FT desde canales habilitados

- **Original Key:** 52716

- **Source Epic:** 52716

- **Type:** User Story

- **Status:** Merged

- **Scope Treatment:** Merged into US-FT-001-002


**Descripción**

Como sistema SILIN, quiero recibir archivos FT desde canales habilitados para iniciar el proceso de gestión del lote de forma automatizada y trazable.


**Criterios de aceptación / escenarios consolidados**

Recepción por canal habilitado, almacenamiento en repositorio, creación de lote en estado Recibido y registro de fecha/canal. Si el canal no está habilitado, no aceptar y registrar intento fallido.


**Notas**

Se conserva como referencia, pero se absorbe en la HU más específica de endpoint desde Plataforma SILIN.


### US-FT-001-006 - Notificación de recepción del lote

- **Original Key:** 52716

- **Source Epic:** 52716

- **Type:** User Story

- **Status:** Scope Review

- **Scope Treatment:** Out of current capability scope


**Descripción**

Como comercializadora y stakeholders internos, quiero ser notificado cuando un lote FT es recibido, para tener confirmación temprana del inicio del procesamiento.


**Criterios de aceptación / escenarios consolidados**

Al recibir un archivo, el sistema debe emitir notificación con identificador de lote, entidad y periodo. Si falla la notificación, el fallo debe registrarse sin afectar el estado del lote.


**Notas**

Requiere decisión de alcance: canal, destinatarios y si se permite notificación automática dentro de esta fase.

---

## CAP-FT-002 - Validación estructural y funcional de archivo


### US-FT-002-001 - Validación estructural del archivo FT

- **Original Key:** 52717

- **Source Epic:** 52717

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero validar la estructura mínima del archivo FT, para detectar errores tempranos y evitar reprocesos costosos.


**Criterios de aceptación / escenarios consolidados**

Debe verificar número esperado de columnas, orden de columnas y formato general. Si la estructura es válida, marcar como estructuralmente válido. Si es inválida, marcar el lote como estructuralmente inválido y registrar motivo de falla a nivel de lote.


**Notas**

No valida datos por registro.


### US-FT-002-002 - Validación funcional por registro

- **Original Key:** 52717

- **Source Epic:** 52717

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero validar cada registro del lote de forma independiente, para eliminar el bloqueo todo o nada del archivo FT.


**Criterios de aceptación / escenarios consolidados**

Para un lote estructuralmente válido, cada registro debe evaluarse contra reglas funcionales definidas. Si cumple, se clasifica como válido. Si no cumple, se clasifica como inválido y se registra motivo.


**Notas**

Las reglas provienen de anexo técnico, reglas históricas y validaciones existentes documentadas.


### US-FT-002-003 - Clasificación de registros del lote

- **Original Key:** 52717

- **Source Epic:** 52717

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero clasificar los registros del lote según su resultado de validación, para permitir procesamiento parcial en fases posteriores.


**Criterios de aceptación / escenarios consolidados**

Al finalizar la validación funcional, los registros deben quedar clasificados como válidos o inválidos. La clasificación debe persistirse y la coexistencia de registros válidos e inválidos no debe bloquear el flujo.


**Notas**

Esta HU soporta directamente el procesamiento parcial.


### US-FT-002-004 - Persistencia de resultados de validación

- **Original Key:** 52717

- **Source Epic:** 52717

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero persistir el resultado de validación de cada registro, para permitir reprocesos, auditoría y trazabilidad.


**Criterios de aceptación / escenarios consolidados**

Cuando un registro sea validado, el sistema debe persistir el estado del registro y el motivo del resultado.


**Notas**

Base para consulta, análisis y revalidación futura.


### US-FT-002-005 - Consolidado de resultados a nivel de lote

- **Original Key:** 52717

- **Source Epic:** 52717

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como equipo tributario y de producto, quiero ver un resumen del resultado de validación del lote, para entender rápidamente su estado sin revisar registros uno a uno.


**Criterios de aceptación / escenarios consolidados**

Cuando todos los registros sean validados, el sistema debe mostrar total de registros, cantidad de válidos y cantidad de inválidos.


**Notas**

Vista resumen técnica, no dashboard avanzado.


### US-FT-002-006 - Análisis y consolidación de validaciones funcionales existentes

- **Original Key:** 52717

- **Source Epic:** 52717

- **Type:** Spike

- **Status:** Active

- **Scope Treatment:** Accepted as Spike


**Descripción**

Como sistema/equipo, quiero analizar, documentar y consolidar las validaciones funcionales existentes sobre archivos FT, para definir la estructura definitiva de reglas y preparar la migración hacia validación por registro.


**Criterios de aceptación / escenarios consolidados**

Debe revisar código existente, identificar validaciones implícitas, duplicadas y acopladas al flujo todo o nada; analizar fuentes de reglas y documentar brechas.


**Notas**

Se carga como Spike porque es trabajo de descubrimiento técnico, no funcionalidad productiva directa.

### US-FT-002-007 - Diseño y ejecución de pruebas de carga y estrés End-to-End (JMeter)

- **Original Key:** N/A (Propuesta en Daily)

- **Source Epic:** 52717

- **Type:** Spike

- **Status:** Active

- **Scope Treatment:** Accepted as Spike


**Descripción**

Como responsable de QA y Arquitectura, quiero diseñar y ejecutar un escenario de pruebas de carga masiva de punta a punta simulando múltiples lotes FT, para medir la capacidad del sistema, identificar cuellos de botella en la nueva infraestructura asíncrona (Lambda Cleanup + ECS/SS) y validar que los tiempos de procesamiento cumplen con las necesidades operativas de la cadena tributaria.


**Criterios de aceptación / escenarios consolidados**

Definición del escenario de estrés documentado. Script de JMeter configurado inyectando archivos al sistema. Ejecución de pruebas en ambiente estabilizado (Staging/QA) tras integración de componentes. Informe de métricas (tiempos de respuesta, recursos, timeouts y recomendaciones).


**Notas**

Se prioriza ejecutar posterior a la estabilización funcional. Mapeado a CAP-FT-002 por representar estrés sobre el núcleo de validación masiva.

### US-FT-002-008 - Homologación dinámica de nombres de columnas por Comercializadora

- **Original Key:** N/A (Diagnóstico Abril)

- **Source Epic:** N/A

- **Type:** User Story

- **Status:** Approved

- **Scope Treatment:** Approved


**Descripción**

Como sistema de procesamiento FT, quiero utilizar un diccionario o mapeo de columnas parametrizado por entidad comercializadora (Ej: según diagnóstico de G-Valle, mapear alias como "FECHA_INI PERIODO_FACT"), para que los archivos superen la validación estructural estricta sin obligar a la entidad a cambiar la estructura de sus exportaciones habituales.


**Criterios de aceptación / escenarios consolidados**

El sistema debe permitir almacenar una configuración de "alias" de columnas asociada a la entidad comercializadora, documentado en https://docs.google.com/spreadsheets/d/1aYp91e7w6AFsfhdgLVYwIwQURRSyUYcubA2Qdeb-6jY/edit?gid=1258681224#gid=1258681224. Durante la validación estructural, si una columna obligatoria no se encuentra, buscar en los alias. Si hace match, la validación pasa y reescribe el encabezado en memoria para el sistema.


**Notas**

Aborda el bloqueo del 80% de los archivos reales (29 de 35 rechazados por encabezados).

---

## CAP-FT-003 - Gestión de registros inválidos


### US-FT-003-001 - Mantener estado de registros inválidos

- **Original Key:** 52721

- **Source Epic:** 52721

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero mantener el estado de cada registro inválido del lote FT, para permitir control operativo y trazabilidad básica sin bloquear el procesamiento parcial.


**Criterios de aceptación / escenarios consolidados**

Un registro inválido debe quedar en estado PENDIENTE_DE_CORRECCIÓN, conservar lote origen y periodo, no bloquear válidos y no incluirse en archivos generados.


**Notas**

La gestión posterior ocurre por soporte/procesos externos, según alcance actual.


### US-FT-003-002 - Asociación de error por registro inválido

- **Original Key:** 52721

- **Source Epic:** 52721

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero asociar a cada registro inválido el error específico que lo originó, para facilitar corrección y soporte operativo.


**Criterios de aceptación / escenarios consolidados**

Cada registro inválido debe asociar código de error, descripción funcional y fecha de detección. La información debe mantenerse al consultarse posteriormente.


**Notas**

No implica corrección automática.


### US-FT-003-003 - Consulta de registros inválidos por lote

- **Original Key:** 52721

- **Source Epic:** 52721

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como usuario de soporte, quiero consultar registros inválidos asociados a un lote FT, para facilitar control operativo y análisis de errores sin afectar el procesamiento.


**Criterios de aceptación / escenarios consolidados**

Debe retornar registros inválidos del lote con estado y error asociado. La consulta no debe modificar estados, disparar reprocesos ni afectar el flujo.


**Notas**

Consulta informativa interna.


### US-FT-003-004 - No bloqueo del procesamiento parcial

- **Original Key:** 52721

- **Source Epic:** 52721

- **Type:** User Story

- **Status:** Merged

- **Scope Treatment:** Merged into US-FT-002-003 and US-FT-004-001


**Descripción**

Como sistema, quiero permitir procesamiento y dispersión de registros válidos aunque existan registros inválidos en el mismo lote.


**Criterios de aceptación / escenarios consolidados**

Solo registros válidos deben procesarse y los inválidos no deben bloquear el proceso ni alterar su estado.


**Notas**

Comportamiento transversal ya cubierto por clasificación de registros y disponibilización de subconjunto válido.

---

## CAP-FT-004 - Disponibilización de registros válidos del lote FT para dispersión en SILIN


### US-FT-004-001 - Identificación del subconjunto válido del lote

- **Original Key:** 52719

- **Source Epic:** 52719

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero seleccionar automáticamente los registros marcados como válidos en un lote, para procesarlos sin depender de los inválidos.


**Criterios de aceptación / escenarios consolidados**

Debe identificar subconjunto válido, excluir inválidos de disponibilización y marcar todos como aptos cuando el lote sea completamente válido.


**Notas**

Base de la disponibilización parcial.


### US-FT-004-002 - Generación de archivos FT para disponibilización FT-01 / FT-06

- **Original Key:** 52719

- **Source Epic:** 52719

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero depositar y dejar disponibles archivos FT validados en repositorio controlado para que Plataforma SILIN ejecute la dispersión.


**Criterios de aceptación / escenarios consolidados**

Debe depositar archivos en repositorio, registrar ruta/fecha/versión, mantener inmutabilidad, generar FT-01 y FT-06 independientes cuando aplique, permitir disponibilización parcial y prevenir duplicidad automática.


**Notas**

El sistema no ejecuta dispersión.


### US-FT-004-003 - Etiquetado e identificación de archivos disponibilizados

- **Original Key:** 52719

- **Source Epic:** 52719

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero etiquetar cada archivo FT generado con identificadores múltiples, para garantizar trazabilidad y consumo controlado por SILIN.


**Criterios de aceptación / escenarios consolidados**

Cada archivo generado debe asociar entidad, periodo tributario, lote origen, tipo de FT y fecha de generación.


**Notas**

Aplica a FT-01 y FT-06.


### US-FT-004-004 - Gestión de estado del lote por disponibilización

- **Original Key:** 52719

- **Source Epic:** 52719

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero mantener un estado claro del lote según su nivel de disponibilización, para reflejar correctamente el avance del proceso.


**Criterios de aceptación / escenarios consolidados**

Debe marcar DISPONIBILIZADO si todos los registros válidos fueron disponibilizados y DISPONIBILIZADO_PARCIALMENTE si existen inválidos excluidos.


**Notas**

Se relaciona con CAP-FT-007, pero aquí se conserva por evento específico de disponibilización.


### US-FT-004-005 - Gestión de reprocesos de archivos FT por incidencias reportadas por SILIN

- **Original Key:** 52719

- **Source Epic:** 52719

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted with scope clarification


**Descripción**

Como sistema, quiero permitir gestión controlada de reprocesos de archivos FT a partir de incidencias reportadas por Plataforma SILIN mediante ticket.


**Criterios de aceptación / escenarios consolidados**

Debe registrar incidencia externa asociada a lote/archivo; marcar INCIDENCIA_REPORTADA; permitir reproceso solo con autorización manual; regenerar y redisponibilizar conservando referencia al lote y versión anterior; bloquear reprocesos no autorizados.


**Notas**

Aclaración: no hay feedback automático de SILIN ni detección automática de errores de dispersión.


### US-FT-004-006 - Prevención de reprocesamiento y duplicidad

- **Original Key:** 52719

- **Source Epic:** 52719

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero evitar la regeneración automática de archivos FT ya disponibilizados, para prevenir duplicidades y errores operativos.


**Criterios de aceptación / escenarios consolidados**

Si un archivo ya fue disponibilizado, una solicitud de reproceso debe bloquear regeneración automática y requerir acción explícita de soporte.


**Notas**

Refuerza inmutabilidad y control de reproceso.

---

## CAP-FT-005 - Revalidación incremental de registros inválidos


### US-FT-005-001 - Recepción de registros corregidos

- **Original Key:** 52722 / BRAI-45

- **Source Epic:** 52722

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero recibir registros corregidos por los mismos canales de ingreso, para no crear flujos paralelos ni excepciones técnicas.


**Criterios de aceptación / escenarios consolidados**

Debe aceptar registros corregidos por canales existentes y marcarlos como REPROCESO.


**Notas**

Mantiene un solo canal operativo.


### US-FT-005-002 - Identificación de reproceso y asociación al lote original

- **Original Key:** 52722

- **Source Epic:** 52722

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero identificar que un registro corresponde a un reproceso, para asociarlo correctamente al lote original.


**Criterios de aceptación / escenarios consolidados**

Un registro con estado previo PENDIENTE_DE_CORRECCIÓN debe asociarse al mismo lote original y conservar referencia al registro original.


**Notas**

No implica versionado complejo.


### US-FT-005-003 - Revalidación incremental del registro corregido

- **Original Key:** 52722 / BRAI-47

- **Source Epic:** 52722

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero revalidar únicamente el registro corregido, para evitar reprocesos masivos innecesarios.


**Criterios de aceptación / escenarios consolidados**

Debe aplicar validación estructural y funcional solo al registro marcado como REPROCESO, sin revalidar otros registros del lote.


**Notas**

Clave para romper reproceso masivo.


### US-FT-005-004 - Actualización del estado del registro corregido

- **Original Key:** 52722 / BRAI-48

- **Source Epic:** 52722

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero actualizar el estado del registro corregido según el resultado, para reflejar correctamente su condición actual.


**Criterios de aceptación / escenarios consolidados**

Si cumple validaciones, actualizar a VÁLIDO. Si no cumple, mantener PENDIENTE_DE_CORRECCIÓN y actualizar motivo de error.


**Notas**

El estado INVÁLIDO se conserva operativamente como pendiente de corrección.


### US-FT-005-005 - Incorporación automática al flujo de procesamiento

- **Original Key:** 52722 / BRAI-49

- **Source Epic:** 52722

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero incorporar automáticamente los registros corregidos y válidos, para que continúen el flujo normal sin intervención humana.


**Criterios de aceptación / escenarios consolidados**

Un registro corregido con estado VÁLIDO debe incorporarse al proceso de dispersión sin aprobación manual.


**Notas**

Debe respetar las reglas de disponibilización vigentes.


### US-FT-005-006 - Actualización del estado agregado del lote

- **Original Key:** 52722 / BRAI-50

- **Source Epic:** 52722

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero actualizar el estado del lote cuando se corrigen registros, para reflejar su avance real.


**Criterios de aceptación / escenarios consolidados**

Si un lote estaba PROCESADO_PARCIALMENTE y todos los inválidos fueron corregidos y validados, el lote debe actualizar su estado a PROCESADO.


**Notas**

El nombre del estado debe alinearse con los estados normalizados finales.


### US-FT-005-007 - Trazabilidad entre versiones del registro

- **Original Key:** 52722 / BRAI-51

- **Source Epic:** 52722

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como equipo interno, quiero mantener trazabilidad entre el registro original y su corrección, para auditoría y control operativo.


**Criterios de aceptación / escenarios consolidados**

Debe conservar referencia al registro original, fecha y resultado del reproceso.


**Notas**

No implica versionado complejo completo.


### US-FT-005-008 - Protección contra reprocesos indebidos

- **Original Key:** 52722

- **Source Epic:** 52722

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero evitar reprocesar registros que ya fueron corregidos y procesados, para no duplicar efectos.


**Criterios de aceptación / escenarios consolidados**

Si un registro tiene estado PROCESADO y se intenta reprocesar nuevamente, el sistema debe rechazar el reproceso y registrar el intento.


**Notas**

Control anti-duplicidad a nivel de registro.

### US-FT-005-005 - Limpieza de codificación, validación de PIPE y rescate de contribuyente anónimo

- **Original Key:** N/A (Diagnóstico Abril)

- **Source Epic:** N/A

- **Type:** User Story

- **Status:** Approved

- **Scope Treatment:** Approved


**Descripción**

Como sistema de procesamiento, quiero rechazar archivos con delimitadores incorrectos (solo aceptar PIPE), limpiar caracteres de codificación, y aplicar una regla de rescate por Medidor cuando la identificación sea 2222222222, para garantizar consistencia legal y operativa en rescate.


**Criterios de aceptación / escenarios consolidados**

1) El sistema NO debe aceptar delimitadores diferentes a PIPE (sin TABs, sin espacios). 2) Se debe forzar o validar limpieza de codificación (''). 3) Si la cédula/ID viene como 2222222222 (protección legal de identidad), el sistema (fase Rescate) debe validar con el número de Medidor y buscar el último contribuyente asociado a ese medidor en la BD. Si no existe, devolver a corrección exigiendo el envío del registro completo al menos una vez para registrar el medidor.


**Notas**

Derivado de pruebas con data real de comercializadoras.

---

## CAP-FT-006 - Gestión, rescate y notificación de registros rechazados


### US-FT-006-001 - Identificación de registros inválidos candidatos a rescate

- **Original Key:** 52718

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero identificar claramente los registros inválidos de un lote, para aplicar procesos de rescate sin afectar los registros válidos.


**Criterios de aceptación / escenarios consolidados**

Debe identificar el conjunto de registros inválidos y mantener el motivo de invalidación de cada uno.


**Notas**

Se conserva como entrada al proceso de rescate.


### US-FT-006-002 - Spike - Rescate: análisis y conexión con SILIN

- **Original Key:** 52718 / BRAI-18

- **Source Epic:** 52718

- **Type:** Spike

- **Status:** Needs Review

- **Scope Treatment:** Spike / possible duplicate with US-FT-002-006


**Descripción**

Analizar y documentar validaciones funcionales existentes sobre archivos FT para preparar reglas y brechas de rescate.


**Criterios de aceptación / escenarios consolidados**

Debe revisar código existente, validaciones estructurales y funcionales, reglas históricas y fuentes documentales.


**Notas**

Contenido cercano al spike de validaciones existentes. Requiere decidir si se fusiona o si se mantiene por foco específico en rescate.


### US-FT-006-003 - Intento de rescate de registros inválidos

- **Original Key:** 52718 / BRAI-21

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero intentar rescatar registros inválidos usando información histórica, para reducir reprocesos y devoluciones a la comercializadora.


**Criterios de aceptación / escenarios consolidados**

Si existe información histórica suficiente, reconstruir el registro y cambiar estado a válido. Si no existe información suficiente, mantenerlo como inválido.


**Notas**

Debe apoyarse en llaves de búsqueda definidas.


### US-FT-006-004 - Identificación de registros inválidos del lote

- **Original Key:** 52718 / BRAI-20

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Merged

- **Scope Treatment:** Merged into US-FT-006-001


**Descripción**

Como sistema, quiero identificar claramente los registros inválidos de un lote para aplicar procesos de rescate.


**Criterios de aceptación / escenarios consolidados**

Identificar inválidos y mantener motivo de invalidación.


**Notas**

Duplicada con US-FT-006-001.


### US-FT-006-005 - Uso de llaves de búsqueda para rescate

- **Original Key:** 52718 / BRAI-22

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero utilizar llaves de búsqueda definidas para el rescate, para aplicar criterios consistentes y auditables.


**Criterios de aceptación / escenarios consolidados**

Debe usar ID de medidor como llave principal. Si un contribuyente tiene múltiples medidores, debe permitir múltiples coincidencias válidas y no asumir unicidad por contribuyente.


**Notas**

Hipótesis funcional explícita del TO-BE.


### US-FT-006-006 - Mantener actualizado el estado del resultado del rescate

- **Original Key:** 52718

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero mantener actualizado el resultado del proceso de rescate, para evitar reprocesos repetidos y permitir trazabilidad.


**Criterios de aceptación / escenarios consolidados**

Si el rescate es exitoso, actualizar estado a válido y registrar origen. Si falla, mantener inválido y registrar intento fallido.


**Notas**

Separa resultado exitoso y fallido.


### US-FT-006-007 - Determinación de rechazo definitivo

- **Original Key:** 52718 / BRAI-24

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero marcar como rechazados los registros que no pudieron ser rescatados, para activar el proceso formal de notificación a interesados.


**Criterios de aceptación / escenarios consolidados**

Si un registro inválido tuvo rescate fallido, debe marcarse como rechazado y asociarse motivo de rechazo.


**Notas**

No implica decisión tributaria legal.


### US-FT-006-008 - Resumen del rescate previo a notificación

- **Original Key:** 52718

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Title adjusted


**Descripción**

Como equipo tributario y de producto, quiero ver un resumen del rescate aplicado al lote, para entender qué tanto se logró recuperar antes de notificar.


**Criterios de aceptación / escenarios consolidados**

Debe mostrar número de registros rescatados y número de registros irrecuperables.


**Notas**

Se ajustó el título original porque el contenido hablaba de resumen, no de notificación directa a comercializadora.


### US-FT-006-009 - Notificación de registros rechazados a interesados internos

- **Original Key:** 52718

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Scope Review

- **Scope Treatment:** Notification channel undefined


**Descripción**

Como actor interno interesado, quiero recibir visibilidad de los rechazos del lote, para dar seguimiento y soporte al proceso.


**Criterios de aceptación / escenarios consolidados**

Debe notificar a interesados internos al finalizar rescate, indicar estado final del lote y número de registros rechazados.


**Notas**

Canal y destinatarios quedan pendientes de definición.


### US-FT-006-010 - Consolidado final del lote tras notificación

- **Original Key:** 52718 / BRAI-27

- **Source Epic:** 52718

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como equipo de producto y tributario, quiero ver el estado final del lote tras las notificaciones, para confirmar el cierre correcto del proceso.


**Criterios de aceptación / escenarios consolidados**

Luego de notificar rechazados, el lote debe reflejar registros válidos y rechazados, sin quedar en estado intermedio.


**Notas**

Cierre operativo del ciclo de error.

---

## CAP-FT-007 - Estados y trazabilidad transversal del procesamiento FT


### US-FT-007-001 - Estados normalizados del lote FT

- **Original Key:** 52723

- **Source Epic:** 52723

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero mantener un estado único y consistente del lote FT, para reflejar claramente su avance dentro del pipeline.


**Criterios de aceptación / escenarios consolidados**

El estado debe actualizarse según evento ocurrido y ser único y consultable. Estados mínimos: RECIBIDO, VALIDADO, DISPONIBILIZADO, DISPONIBILIZADO_PARCIALMENTE, PROCESADO, PROCESADO_PARCIALMENTE, ERROR.


**Notas**

Debe alinear nombres con estados usados en otras HUs.


### US-FT-007-002 - Estados a nivel de registro individual

- **Original Key:** 52723

- **Source Epic:** 52723

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero mantener el estado individual de cada registro del lote, para permitir trazabilidad granular sin reprocesos manuales.


**Criterios de aceptación / escenarios consolidados**

Cada registro del lote debe tener su propio estado independiente.


**Notas**

Soporta gestión de válidos, inválidos, excluidos, reprocesados y rechazados.


### US-FT-007-003 - Disponibilización vía API para interesados internos

- **Original Key:** 52723

- **Source Epic:** 52723

- **Type:** User Story

- **Status:** Active

- **Scope Treatment:** Accepted


**Descripción**

Como sistema, quiero disponibilizar la información de estados y trazabilidad vía API, para que otros sistemas o equipos la consuman.


**Criterios de aceptación / escenarios consolidados**

Un sistema autorizado debe poder consultar estado actual del lote y estados agregados de sus registros.


**Notas**

API interna, no contractual, alineada a consulta técnica.


### US-FT-007-004 - Visualización operativa de estados de lotes FT mediante Grafana

- **Original Key:** 52716

- **Source Epic:** 52716

- **Type:** User Story

- **Status:** Scope Review

- **Scope Treatment:** Moved from CAP-FT-001; dashboard excluded from current capability


**Descripción**

Como usuario interno, quiero una vista operativa en Grafana para consultar el estado de los lotes FT en tiempo casi real sin acceder a base de datos.


**Criterios de aceptación / escenarios consolidados**

Debe visualizar lista de lotes, estado actual, fecha de recepción y canal de entrada; permitir filtros por entidad, periodo, comercializadora y estado; ser solo lectura.


**Notas**

Se movió a CAP-FT-007 por naturaleza de trazabilidad, pero queda en revisión porque dashboards gráficos están excluidos del alcance actual.


### US-FT-007-005 - Gestión inicial de estados del lote

- **Original Key:** 52716

- **Source Epic:** 52716

- **Type:** User Story

- **Status:** Merged

- **Scope Treatment:** Merged into US-FT-007-001


**Descripción**

Como equipo operativo y tributario, quiero visualizar el estado básico del lote desde su recepción, para entender claramente en qué punto del proceso se encuentra.


**Criterios de aceptación / escenarios consolidados**

El lote debe iniciar en estado Recibido y actualizar estado automáticamente conservando historial.


**Notas**

Se absorbe en estados normalizados del lote FT.
