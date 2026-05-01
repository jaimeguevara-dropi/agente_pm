# Capabilities / Épicas - SILIN - Procesamiento inteligente FT

## Proyecto
SILIN - Procesamiento inteligente FT

## Objetivo asociado
Procesamiento inteligente y parcial de archivos FT para habilitar la cadena tributaria en tiempos operativos mínimos.

## Propósito de este documento
Este documento consolida las capacidades / épicas funcionales del TO-BE del proyecto. Su objetivo es servir como mapa canónico para que el agente, el equipo de producto y los equipos técnicos puedan entender la estructura funcional del futuro procesamiento FT.

Estas capacidades derivan del TO-BE aprobado y representan los bloques principales sobre los cuales luego se estructuran features, historias de usuario, criterios de aceptación y seguimiento de implementación.

---

# Mapa de capacidades

## CAP-FT-001 - Recepción de Lotes FT

### Propósito
Permitir la recepción controlada de archivos FT y su conversión en una unidad formal de procesamiento llamada lote, garantizando trazabilidad, estados claros y control operativo desde el primer momento.

Esta capacidad no ejecuta validaciones estructurales, funcionales ni tributarias. Su función es encapsular el archivo como unidad operativa formal del pipeline.

### Definición clave: Lote FT
Un lote FT corresponde al conjunto completo de registros contenidos en un archivo FT original recibido, tratado como una única unidad de control para efectos de:

- trazabilidad,
- estados,
- procesamiento,
- reprocesos,
- consulta operativa.

Un lote no fragmenta ni altera registros. Únicamente los encapsula y los prepara para las siguientes etapas del pipeline.

### Alcance funcional
El sistema debe permitir:

- crear un lote único al recibir un archivo FT,
- asignar un identificador único de lote,
- registrar metadatos básicos,
- asociar el lote con comercializadora, entidad, periodo y tipo de archivo FT,
- manejar estados básicos del lote,
- actualizar automáticamente el estado conforme avanza el pipeline,
- conservar trazabilidad mínima desde la recepción.

### Estados iniciales posibles
- RECIBIDO
- VALIDADO
- PROCESADO
- PROCESADO_PARCIALMENTE
- RECHAZADO

El estado del lote debe cambiar únicamente en función del avance real del proceso, no por acciones manuales ni interpretaciones externas.

### Trazabilidad mínima
Desde la recepción, el lote debe conservar:

- fecha y hora de recepción,
- canal de recepción,
- estado actual,
- referencias de entidad, periodo y comercializadora.

### Resultado esperado
Al finalizar esta capacidad:

- todo archivo FT recibido existe como lote formal,
- el lote tiene identidad clara,
- el lote tiene estado consultable,
- el sistema queda listo para validación estructural, validación funcional y procesamiento parcial.

### Exclusiones
Esta capacidad no incluye:

- validaciones estructurales del archivo,
- validaciones funcionales por registro,
- validaciones tributarias,
- corrección automática de registros,
- interacción visual con comercializadoras,
- integraciones con facturación o cartera,
- autorizaciones humanas,
- visualizaciones gráficas o dashboards.

---

## CAP-FT-002 - Validación estructural y funcional de archivo

### Propósito
Validar que el archivo FT y sus registros cumplen condiciones técnicas mínimas para continuar el flujo de procesamiento, eliminando el bloqueo de tipo “todo o nada”, clasificando errores tempranamente y permitiendo continuidad operativa.

Esta capacidad no corrige datos, no ejecuta dispersión y no toma decisiones tributarias finales. Su objetivo es clasificar y preparar la información para el procesamiento parcial posterior.

### Objetivos funcionales
El sistema debe permitir:

- validar la estructura del archivo FT antes de cualquier procesamiento,
- evaluar cada registro de forma independiente,
- detectar fallas estructurales críticas que impiden continuar,
- clasificar registros como válidos o inválidos sin bloquear todo el lote,
- dejar evidencia clara y trazable del resultado de la validación.

### Validación estructural a nivel de lote
El sistema debe validar automáticamente, de acuerdo con el anexo técnico:

- número esperado de columnas,
- orden de columnas,
- formato básico del archivo,
- separadores,
- estructura general.

### Comportamiento ante estructura inválida
Si la estructura es inválida:

- el lote se marca como RECHAZADO_ESTRUCTURALMENTE,
- no se continúa con validaciones por registro,
- se registra el motivo del rechazo a nivel de lote,
- no se generan correcciones automáticas.

### Validación funcional mínima por registro
Para archivos estructuralmente válidos, el sistema debe:

- evaluar cada registro de manera independiente,
- aplicar reglas funcionales mínimas,
- usar reglas provenientes del anexo técnico tributario,
- considerar reglas históricas documentadas del proceso actual,
- considerar validaciones técnicas existentes en el sistema.

### Resultado por registro
Cada registro puede quedar como:

- VÁLIDO,
- INVÁLIDO, con motivo registrado.

La invalidación de un registro no bloquea el resto del lote.

### Clasificación del resultado del lote
Un lote puede quedar como:

- totalmente válido,
- parcialmente válido,
- estructuralmente rechazado.

### Trazabilidad esperada
Debe mantenerse relación entre:

- lote,
- registros,
- motivos de invalidación.

### Exclusiones
Esta capacidad no incluye:

- corrección automática de datos,
- rechazo definitivo tributario de registros,
- notificaciones a comercializadoras,
- procesamiento o dispersión de información,
- validación de calendarios tributarios o fechas,
- IA para rescatar registros,
- visualizaciones gráficas avanzadas.

---

## CAP-FT-003 - Gestión de registros inválidos

### Propósito
Mantener control, trazabilidad y visibilidad interna sobre los registros inválidos detectados durante la validación del lote FT, sin bloquear el procesamiento parcial ni asumir responsabilidades operativas que pertenecen a otros equipos.

Esta capacidad no gestiona tiempos, sanciones ni comunicaciones externas. Su función es clasificar, registrar y exponer información, no decidir ni actuar automáticamente.

### Alcance funcional
El sistema debe permitir:

- mantener identificados los registros clasificados como inválidos,
- garantizar que los registros inválidos no bloqueen el avance de los registros válidos del mismo lote,
- asociar cada registro inválido con su error,
- mantener persistente y consultable la información del error,
- marcar el estado operativo del registro,
- permitir consulta interna por lote, entidad y periodo,
- conservar trazabilidad mínima del registro inválido con el lote original.

### Asociación clara del error
Cada registro inválido debe quedar asociado a:

- tipo de error,
- campo afectado,
- motivo funcional o estructural.

### Estado operativo del registro
Los registros inválidos deben marcarse con estado:

- PENDIENTE_DE_CORRECCIÓN

Este estado indica que:

- el registro no fue procesado,
- requiere acción externa,
- el sistema no tomará acciones automáticas.

### Consulta interna
Debe permitirse consulta interna para soporte, producto o tributaria por:

- lote FT,
- entidad,
- periodo.

La consulta debe permitir visualizar:

- total de registros inválidos,
- detalle de errores asociados,
- estado actual del registro.

### Resultado esperado
Los registros inválidos quedan controlados, visibles y trazables, sin impedir que los registros válidos avancen.

### Exclusiones
Esta capacidad no incluye:

- validación de tiempos tributarios,
- seguimiento de SLAs o fechas límite,
- notificaciones automáticas internas o externas,
- comunicación con comercializadoras,
- corrección o rescate de registros inválidos,
- revalidación incremental automática,
- decisiones tributarias o legales,
- rechazo definitivo del archivo,
- dashboards avanzados o métricas.

---

## CAP-FT-004 - Disponibilización de registros válidos del lote FT para dispersión en SILIN

### Propósito
Permitir que los registros válidos de un lote FT sean preparados y disponibilizados en los formatos correspondientes, FT-01 y/o FT-06, sin bloquearse por la existencia de registros inválidos.

Esta capacidad elimina el modelo “todo o nada”. El sistema no ejecuta la dispersión, sino que prepara, identifica y deja disponibles los archivos FT validados para que Plataforma SILIN realice el proceso de dispersión.

### Alcance funcional
El sistema debe permitir:

- identificar el subconjunto de registros válidos del lote,
- generar archivos de salida correspondientes,
- permitir que un mismo lote origine FT-01 y/o FT-06,
- asociar cada archivo generado con identificadores claros,
- marcar el estado del lote según disponibilidad total o parcial,
- depositar archivos generados en repositorio controlado,
- recibir feedback técnico del proceso de dispersión,
- registrar el resultado del feedback recibido,
- evitar regeneraciones automáticas duplicadas.

### Archivos de salida
El sistema debe generar:

- FT-01 para registros válidos no excluidos,
- FT-06 para registros válidos con marca de exclusión.

### Identificadores de archivo generado
Cada archivo debe quedar asociado a:

- entidad,
- periodo,
- lote origen,
- tipo de archivo.

### Estados del lote
El lote puede marcarse como:

- DISPONIBILIZADO, cuando todos los registros son válidos,
- DISPONIBILIZADO_PARCIALMENTE, cuando existen registros inválidos no incluidos.

### Feedback técnico de dispersión
El sistema debe recibir y registrar feedback técnico indicando:

- éxito,
- error,
- error parcial.

### Resultado esperado
Al finalizar esta capacidad:

- los registros válidos quedan separados y disponibilizados en FT-01 y/o FT-06,
- Plataforma SILIN puede ejecutar dispersión sin reprocesar validaciones funcionales,
- el sistema conoce si el archivo fue dispersado correctamente, si hubo errores o si el proceso quedó incompleto,
- puede consultarse por lote el total de registros, registros enviados por tipo de FT y estado del feedback recibido.

### Exclusiones
Esta capacidad no incluye:

- ejecución directa de la dispersión en bases de datos de SILIN,
- causación,
- liquidación,
- facturación,
- corrección o rescate de registros inválidos,
- notificación directa a comercializadoras,
- validaciones de calendario o tiempos tributarios,
- revalidación incremental automática,
- visualización UI avanzada o dashboards,
- cambios en reglas tributarias o legales.

---

## CAP-FT-005 - Revalidación incremental de registros inválidos

### Propósito
Permitir que únicamente los registros previamente inválidos y corregidos sean revalidados y procesados, sin reprocesar el lote completo, manteniendo trazabilidad con el lote original.

### Alcance funcional
El sistema debe permitir:

- recibir registros corregidos usando los mismos canales de entrada,
- identificar que un registro corresponde a un reproceso,
- asociar el registro corregido al lote original,
- revalidar estructural y funcionalmente solo el registro corregido,
- actualizar el estado del registro,
- reincorporar automáticamente el registro al flujo normal si queda válido,
- actualizar el estado agregado del lote si aplica.

### Cambio de estado del registro
El registro puede cambiar de:

- PENDIENTE_DE_CORRECCIÓN

a:

- VÁLIDO,
- INVÁLIDO.

### Resultado esperado
Los registros corregidos pueden reincorporarse al flujo sin reprocesar todo el lote, reduciendo reprocesos masivos y mejorando eficiencia operativa.

### Exclusiones
Esta capacidad no incluye:

- detección automática de correcciones,
- versionado complejo de archivos,
- comparación semántica de cambios,
- reprocesamiento completo del lote.

---

## CAP-FT-006 - Gestión, rescate y notificación de registros rechazados

### Propósito
Cerrar el ciclo del error a nivel de registro, intentando rescatar lo recuperable, identificando lo irrecuperable y notificando oficialmente los registros rechazados.

La intención es eliminar la ambigüedad operativa sobre qué sigue, qué puede recuperarse y qué queda rechazado.

### Alcance funcional
El sistema debe permitir:

- intentar rescatar registros inválidos,
- determinar cuáles son irrecuperables,
- notificar registros rechazados,
- cerrar el ciclo del error a nivel de registro.

### Comportamiento esperado
A partir de esta capacidad:

- lo válido sigue su camino,
- lo rechazado queda oficialmente notificado,
- no hay más ambigüedad operativa.

### Hipótesis funcional explícita
- El ID del medidor es la llave principal de búsqueda.
- Un contribuyente puede tener múltiples medidores.

### Resultado esperado
El sistema deja claramente clasificados los registros que no podrán continuar, dejando evidencia de notificación y cierre operativo.

### Exclusiones
Esta capacidad no incluye:

- corrección automática de registros,
- reenvío automático por parte de la comercializadora,
- dispersión de registros válidos,
- validación tributaria legal,
- UI avanzada para comercializadoras.

---

## CAP-FT-007 - Estados y trazabilidad transversal del procesamiento FT

### Propósito
Permitir el seguimiento confiable del estado técnico del procesamiento de archivos FT desde su recepción hasta su validación y disponibilización en repositorio, garantizando trazabilidad básica del lote y de sus registros.

Esta capacidad no interviene en tiempos tributarios, notificaciones ni procesos de dispersión.

### Alcance funcional
El sistema debe permitir:

- gestionar el estado técnico del lote FT,
- mantener estado individual por registro,
- registrar historial básico de cambios de estado,
- disponibilizar archivos FT en repositorio,
- registrar validación posterior del equipo de Datos,
- consultar el estado del procesamiento por entidad, periodo y lote.

### Estados técnicos del lote
Estados posibles de referencia:

- RECIBIDO,
- VALIDADO_TECNICAMENTE,
- DISPONIBILIZADO_EN_REPOSITORIO,
- VALIDADO_POR_DATOS,
- ERROR_TECNICO.

No existen estados asociados a fechas tributarias ni cumplimiento normativo dentro de esta capacidad.

### Estados por registro
Cada registro puede mantener estado individual como:

- válido,
- inválido,
- excluido, si aplica.

### Historial básico
El sistema debe registrar cambios de estado a nivel de:

- lote,
- registro.

El historial debe incluir:

- estado anterior,
- estado nuevo,
- timestamp.

Este historial no corresponde a auditoría legal ni fiscal.

### Disponibilización en repositorio
El sistema debe dejar los archivos FT-01 y/o FT-06 en un repositorio acordado y marcar el lote como disponibilizado en repositorio.

### Validación posterior por Datos
El sistema debe registrar el resultado del proceso Validate ejecutado por el equipo de Datos y reflejarlo en el estado del lote, por ejemplo:

- VALIDADO_POR_DATOS,
- ERROR_EN_VALIDACION_DE_DATOS.

### Consulta del estado
Debe permitirse consulta por:

- entidad,
- periodo,
- lote.

La información disponible debe incluir:

- estado actual,
- resumen de registros,
- historial básico.

La consulta puede ser interna, por base de datos, vista técnica o endpoint simple. No necesariamente debe ser una API contractual.

### Exclusiones
Esta capacidad no incluye:

- validación de fechas o calendario tributario,
- alertas o notificaciones automáticas,
- orquestación de tiempos o vencimientos,
- dispersión de datos,
- integración directa con SILIN vía API,
- dashboards gráficos,
- decisiones normativas, fiscales o legales.

---

## CAP-FT-008 - Próximamente / Nice to have (Backlog Futuro)

### Propósito
Mapear iniciativas de alto valor que exceden el alcance del MVP pero quedan registradas para futura evolución del producto. Estas iniciativas buscan optimizar la carga operativa sin interferir con el flujo normal de desarrollo actual.

### Iniciativas a registrar
- **Agente de IA pre-validador:** Para que las comercializadoras o el sistema detecten anomalías estructurales o de datos en una muestra de registros antes de procesar el lote completo, reduciendo costos de infraestructura y basura en la base de datos.
- **UX de pre-validación externa:** Interfaz para que la comercializadora homologue manualmente sus columnas o decida si procesar o corregir archivos con un alto porcentaje de error antes del envío definitivo.

### Exclusiones en MVP
- No se implementarán en la fase de estabilización actual.
- Quedan como insumo para discovery técnico en versiones posteriores.

---

# Relación con el TO-BE

Estas capacidades materializan el TO-BE aprobado del proyecto. En conjunto, permiten pasar de un procesamiento manual, secuencial y bloqueante hacia un procesamiento parcial, trazable, escalable y orientado a habilitar la cadena tributaria en tiempos operativos mínimos.

# Notas de uso para el agente

El agente debe usar este documento como mapa funcional canónico del proyecto.

Cuando analice historias de usuario, seguimientos o decisiones, debe relacionarlas con una de estas capacidades.

Cuando identifique nuevas features o HUs, debe proponerlas como derivadas de una capacidad existente o señalar explícitamente si se requiere crear una nueva capacidad.
