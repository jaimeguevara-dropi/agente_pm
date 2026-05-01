# Estructura PPT - Sprint 10 Review & Retrospective

## Slide 1: Portada
**Título:** Sprint 10 Review - SILIN Procesamiento Inteligente FT
**Subtítulo:** Lancha 1 (First AI Squad)
**Fecha:** 30 de Abril
**Equipo:** Sergio Ospina, Emmanuel Ortega, Rafa Peña, Ana Ospina, Jaime Guevara, Freddy.

## Slide 2: Resumen Ejecutivo del Sprint
- **Objetivo del Sprint:** Finalizar migración de entidades a Brain, robustecer Lambda Cleanup y ejecutar pruebas End-to-End con data real.
- **Métricas:** 100% de Completitud.
- **Story Points Logrados:** 27 SP (5 historias de usuario terminadas).
- **Bugs Resueltos:** 2 bugs cerrados.

## Slide 3: Principales Logros y Entregables (Desarrollo)
- **Migración a Brain Completada (BRAI-26):** Tablas maestras (Entidad, Tributo y Compañía de Energía) operando 100% bajo Brain (Lambda Ingestion, Glue, ESS).
- **Flexibilización de Headers (US-FT-002-008):** Homologación dinámica que evita rechazos estructurales por nombres de columna alternativos enviados por las comercializadoras.
- **Robustez en Lambda Cleanup (BRAI-303):** Se resolvieron casos atípicos y se mejoró la codificación y limpieza gracias a la data real (sin afectar tiempos).
- **Gestión de Notificaciones en ESS:** Envío de correos implementado y optimización de infraestructura (Aumento de CPU y RAM) para soportar picos altos.

## Slide 4: Principales Logros y Hallazgos (QA & Pruebas)
- **Trazabilidad (BRAI-51):** Control y seguimiento entre versiones del registro.
- **Certificación Continua:** Pruebas tempranas ejecutadas progresivamente, logrando la certificación total.
- **Hallazgo Crítico en Pruebas de Carga (US-FT-002-007):** Se detectó un cuello de botella arquitectónico en el **GLUE** (Ingestión). Ante concurrencia (ej. 5 archivos grandes), solo toma 1 o 2 y se pierden los demás requests. No hay soporte configurado para concurrencia masiva sin colas.

## Slide 5: Demo
*(Espacio para presentar el video pre-grabado o hacer la demo en vivo)*
**Contenido de la Demo:**
1. Archivo con "2222" o "6666" demostrando limpieza y codificación.
2. Homologación de encabezados (archivo subido con nombres erróneos que son mapeados correctamente).
3. Trazabilidad visible del proceso.

## Slide 6: Riesgos y Deuda Técnica (Para Refinamiento)
- **Riesgo Técnico:** Cuello de botella en GLUE (Requiere definir con arquitectura cómo orquestar la concurrencia masiva, posible implementación de SQS).
- **Riesgo Operativo:** Mantener actualizadas las nuevas Tablas Maestras (Brain) sin una estrategia de sincronización fluida si se registran nuevas comercializadoras.
- **Capacidad Futura:** Tiempo de QA compartido (Ana) limita disponibilidad exclusiva para el próximo Sprint; se debe priorizar con cuidado.

## Slide 7: Próximos Pasos & Sprint 11
- Resolver definiciones pendientes con el equipo de Arquitectura (Freddy/Jaime) sobre el GLUE.
- Preparar Backlog y nuevas historias del Sprint 11.
- Iniciar Retrospectiva del equipo.
