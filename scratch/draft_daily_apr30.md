# Borrador de seguimiento

## 1. Resumen ejecutivo
El Sprint 10 finalizó con un alto porcentaje de completitud técnica (100% de las tareas comprometidas: 27 story points, 5 historias + 2 bugs de performance cerrados). Se evidenció madurez en la Lambda Cleanup, estabilización en la migración de tablas maestras a Brain, y se realizó la primera prueba de carga que destapó un cuello de botella en el Glue (ingestión) para archivos pesados o múltiples.

## 2. Evolución / avances detectados
- **Lambda Cleanup:** Mayor robustez gracias a pruebas con data real, lo que permitió cubrir casos no mapeados inicialmente sin afectar tiempos de procesamiento (Rafa).
- **Tablas maestras migradas:** Entidad, tributo y compañía de energía ahora operan bajo la arquitectura de Brain y están integradas en Lambda Ingestion, Glue y ESS (Emmanuel).
- **Carga de archivos:** Se ajustó la validación de headers para ser más permisivos/tolerantes a errores de la comercializadora (Emmanuel / Rafa).
- **Componente ESS:** Se implementó el envío de correos. Se incrementó la memoria (CPU y RAM) para soportar escenarios de procesamiento elevado ante los fallos detectados por QA (Emmanuel).
- **Testing:** Se logró completar pruebas tempranamente a medida que se entregaban las historias, detectando cuellos de botella reales en performance.

## 3. Capabilities impactadas
- **CAP-FT-002 - Validación estructural y funcional de archivo:** Impactada por las pruebas de performance, la homologación dinámica de nombres de columna (headers) y la migración de tablas maestras de validación.
- **CAP-FT-005 - Revalidación incremental de registros inválidos:** Impactada por la HU de Trazabilidad entre versiones del registro.

## 4. HUs impactadas
- **US-FT-002-007 (Spike):** Diseño y ejecución de pruebas de carga y estrés (Ana y Jaime). *Completado*.
- **US-FT-002-008:** Homologación dinámica de nombres de columnas por Comercializadora (BRAI-302 - Emmanuel). *Completado*.
- **BRAI-51:** Trazabilidad entre versiones del registro (Rafa). *Completado*.
- **BRAI-303:** Mejoras de limpieza y casos específicos en Lambda Cleanup (Rafa / Emmanuel). *Completado*.
- **BRAI-26:** Análisis y migración de tablas maestras (entidad, tributo, compañía energía) (Emmanuel). *Completado*.

## 5. Riesgos detectados
- **Cuello de botella en GLUE (Ingestión):** No soporta concurrencia o envíos de varios archivos pesados al mismo tiempo (ej. de 5 archivos solo toma 1 o 2). Pierde requests. (Riesgo Técnico / Arquitectura).
- **Sincronización de Tablas Maestras:** Riesgo de desactualización si se agregan nuevas empresas de energía o entidades, al no tener una sincronización automática fluida (Riesgo Operativo).
- **Capacidad de QA:** La dedicación de Ana compartida con otra lancha limita la capacidad de testing, lo que requiere vigilar la asignación de puntos para el próximo sprint.

## 6. Deuda acumulada
- Falta de configuración de concurrencia o implementación de colas (SQS) para el ingreso de archivos por el GLUE, lo que provoca la caída de peticiones concurrentes.

## 7. Decisiones o definiciones pendientes
- Definición arquitectónica con Freddy/Jaime sobre cómo manejar el cuello de botella en GLUE para cargas concurrentes.
- Estrategia para mantener sincronizadas las tablas maestras cuando haya actualizaciones de negocio.

## 8. Compromisos / próximos pasos
- Grabar la demo mostrando los cambios de trazabilidad de versiones, limpieza de datos, y homologación de encabezados (Rafa, Ana, Jaime).
- Preparar la PPT de cierre de sprint / review basada en los logros (Sergio).
- Cerrar las historias formalmente en Jira antes de la Review/Refinamiento (Ana).

## 9. Desviación contra TO-BE
- Ninguna desviación estructural. La flexibilización de los headers y la limpieza temprana respaldan fuertemente la **CAP-FT-002**, permitiendo que menos archivos se bloqueen estructuralmente.

## 10. Recomendación de guardado
- El estado general es muy positivo, reflejando el cierre técnico del Sprint 10. Se recomienda **Aprobar este borrador** para guardar los riesgos, decisiones y seguimiento oficial en el OS del proyecto, sin modificar el AS-IS / TO-BE.
