# Propuesta de Nuevas Historias y Actividades - Siguiente Sprint

Basado en el cierre del Sprint 10 y los hallazgos técnicos recientes, se proponen las siguientes Historias de Usuario (HUs) y actividades clave (Spikes/Tareas) para ser incluidas en el próximo ciclo (Sprint 11).

## 1. Foco en Arquitectura y Performance (Ingesta)
El riesgo más crítico detectado fue el fallo de concurrencia en la ingesta durante las pruebas de carga (JMeter).

### Spike Técnico: Análisis y rediseño de concurrencia en Ingesta
- **Tipo:** Spike / Tarea Técnica
- **Descripción:** Como Arquitecto/Desarrollador, quiero analizar el cuello de botella en la capa de Ingesta que causa el descarte de archivos bajo carga concurrente, para proponer e implementar un rediseño que soporte el procesamiento paralelo (ej. ajuste de colas SQS, escalado de Lambdas, optimización de conexión de base de datos).
- **Criterios de Aceptación:** Identificación de la causa raíz del descarte. Propuesta arquitectónica aprobada. Ejecución exitosa de una prueba JMeter (ej. 5 usuarios concurrentes enviando archivos de 30MB) donde el 100% de los archivos pasen a las siguientes etapas sin pérdida por timeout o bloqueo.

## 2. Foco en Calidad de Datos y Homologación
Aún existen casos borde con archivos de comercializadoras que rompen la validación estructural.

### US-FT-XXX - Sanitización dinámica de separadores residuales (Caso Terpel)
- **Tipo:** User Story
- **Capacidad asociada:** CAP-FT-002 (Validación estructural)
- **Descripción:** Como sistema de procesamiento, quiero limpiar los separadores residuales (como "pipes" al final de línea) generados por sistemas externos, para evitar la creación de columnas "fantasma" que rompan la validación estructural estricta.
- **Criterios de Aceptación:** Al procesar un archivo, si la última columna está vacía y es precedida por el delimitador (pipe), el sistema debe ignorar esa "falsa columna" en la validación de estructura sin alterar el resto del registro. Los archivos con formato Terpel deben ser validados como correctos estructuralmente.

## 3. Foco en Cierre Operativo (Notificaciones)
La prueba de concepto (PoC) en ECS fue exitosa, ahora debe integrarse en el flujo.

### US-FT-006-XXX - Configuración e integración del servicio de notificaciones (ECS)
- **Tipo:** User Story
- **Capacidad asociada:** CAP-FT-006 (Gestión, rescate y notificación)
- **Descripción:** Como sistema, quiero configurar e integrar definitivamente el servicio de notificaciones por correo electrónico dentro del flujo ECS, para automatizar el aviso a interesados sobre el resultado del procesamiento y/o registros rechazados.
- **Criterios de Aceptación:** El componente ECS debe enviar un correo transaccional real (utilizando los parámetros del entorno de Staging/Prod) a los destinatarios configurados. Debe registrarse la traza del envío. La falla en el envío de correo no debe bloquear ni revertir el estado del lote en la base de datos.

## 4. Actividades Adicionales (Tareas de Arrastre o "Clean up")
- **Tarea QA:** Ejecutar la regresión completa de las correcciones del "trash" utilizando la entrega de la BRAI-303 (Rafa) en el nuevo ambiente.
- **Tarea Producto/PM:** Revisar las métricas de rendimiento extraídas por Ana para redefinir formalmente los SLA/SLO técnicos del TO-BE de procesamiento.
