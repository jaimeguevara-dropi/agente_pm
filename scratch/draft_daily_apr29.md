# Borrador de seguimiento

## 1. Resumen ejecutivo
El equipo de la "Lancha 1" realizó el penúltimo daily del Sprint 10, enfocado en el cierre de pruebas (QA) y consolidación de funcionalidades del proyecto SILIN - Procesamiento inteligente FT. Se confirmó la superación de las validaciones estructurales de la mayoría de los archivos (excepto Terpel) gracias a los últimos ajustes, permitiendo avanzar con la elaboración del informe de sprint. El punto más crítico levantado es una falla de rendimiento y concurrencia en el componente de "ingesta", detectada durante las pruebas de carga, que requerirá revisión de arquitectura para el próximo sprint.

## 2. Evolución / avances detectados
- **QA (Ana):** Finalizó pruebas de funcionalidad base, actualizando la matriz de seguimiento. Todos los archivos pasan la validación estructural, con excepción de Terpel. Adicionalmente, se iniciaron pruebas de performance / carga concurrente (archivos de 30MB) que levantaron fallas en la Ingesta.
- **Desarrollo (Emmanuel):** Entregó las tareas asociadas a BRAI-26, incluyendo los ajustes necesarios para que los archivos superen la validación estructural. También implementó de forma preliminar el servicio de notificaciones desde ECS (prueba de envío de correo funcional), dejando la configuración definitiva para el próximo sprint.
- **Desarrollo (Rafa):** Trabajó en BRAI-303 (Clean Up). Realizó pruebas locales y envió un PR final para entregar a QA (Ana) en las próximas horas.

## 3. Capabilities impactadas
- **CAP-FT-002 - Validación estructural y funcional de archivo:** Impactada por la validación exitosa de los archivos de prueba, excepto Terpel, y por las pruebas de carga (JMeter).
- **CAP-FT-006 - Gestión, rescate y notificación de registros rechazados:** Impactada por la prueba de concepto funcional del servicio de notificaciones desde ECS implementado por Emmanuel.

## 4. HUs impactadas
- **US-FT-002-001 - Validación estructural del archivo FT:** Avance significativo, con la excepción del archivo de Terpel debido al "pipe" final.
- **US-FT-002-007 - Diseño y ejecución de pruebas de carga y estrés End-to-End:** En ejecución. Se encontró un cuello de botella grave en la concurrencia de la ingesta.
- **US-FT-002-008 - Homologación dinámica de nombres de columnas por Comercializadora:** Avances aplicados por Emmanuel para lograr el paso de los archivos a válidos.
- **US-FT-001-006 / US-FT-006-009 - Notificación:** Avance técnico (Spike / PoC) en ECS para el envío de correos, pendiente de configuración final.

## 5. Riesgos detectados
- **Riesgo Operativo / Arquitectura (Alto):** Falla en la ingesta ante concurrencia. De 5 usuarios enviando cargas de 30MB, el sistema pasa correctamente el "Designer" y el "Upload", pero en la fase de "Ingesta" solo procesa un archivo y descarta los demás. Esto compromete la capacidad del sistema para procesar múltiples lotes paralelos.
- **Riesgo de Datos (Bajo):** Caso borde con el formato de Terpel, donde un carácter "pipe" al final de la línea genera una falsa columna adicional, rompiendo la validación estructural tras el borrado de la primera línea en blanco.

## 6. Deuda acumulada
- Solución al manejo del "pipe" final en archivos con el formato de Terpel.
- Configuración definitiva del sistema de envío de notificaciones desde el ECS (se traslada como tarea para el próximo sprint).

## 7. Decisiones o definiciones pendientes
- **Arquitectura:** Definir con el equipo de arquitectura cómo se abordará y solucionará la limitación de concurrencia en la capa de ingesta para el próximo sprint.
- **Alcance Funcional:** Revisar junto a Rafa y Ana si la entrega de "Clean Up" cubre todas las necesidades respecto al "trash" remanente y manejo de descartes.

## 8. Compromisos / próximos pasos
- **Rafa:** Entregar BRAI-303 (Clean Up) a QA en un par de horas.
- **Jaime, Rafa y Ana:** Mesa de trabajo corta para revisar casos pendientes de mapeo y finalizar el informe de cierre de sprint.
- **Ana:** Publicar informes de pruebas generados al final del día y enviar copia a Freddy.

## 9. Desviación contra TO-BE
La falla en la ingesta concurrente representa una desviación parcial contra el objetivo TO-BE, el cual estipula que el sistema debe ser capaz de "soportar volúmenes altos y tiempos compatibles con la necesidad del negocio". Si la ingesta descarta archivos bajo carga paralela, el sistema no está logrando la resiliencia requerida en la recepción masiva.

## 10. Recomendación de guardado
**Se recomienda su aprobación y guardado oficial.**
El seguimiento proporciona insumos críticos para la planificación del próximo sprint, especialmente el riesgo arquitectónico en la ingesta. Dejar esto registrado en el PM OS asegura que la deuda técnica y el cuello de botella concurrente queden formalizados como riesgos a mitigar.
