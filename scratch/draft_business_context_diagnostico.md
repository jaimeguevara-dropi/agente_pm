# Business Context - SILIN - Diagnóstico de liquidación y potencial de recaudo

## Nombre del objetivo / proyecto
SILIN - Diagnóstico de liquidación y potencial de recaudo

## Contexto global del objetivo
SILIN (Sistema de Liquidación de Impuestos) requiere procesar archivos FT (FT-01, FT-03, FT-05, FT-06) provenientes de las comercializadoras de energía. Actualmente, el flujo desde la carga del archivo hasta la liquidación del impuesto y causación de deudas es fragmentado e involucra múltiples equipos (Tributaria, Analítica de Datos, Base de Datos/SILIN) con altos cuellos de botella operativos y revisiones manuales. 

El proyecto busca implementar un módulo de **"Diagnóstico de liquidación y potencial de recaudo"** que valide eficientemente la estructura de los archivos, calcule la liquidación del impuesto y muestre el valor total que el municipio podría recaudar. Esto servirá como herramienta de diagnóstico y demostración de valor económico para facilitar la venta del software completo de SILIN a las alcaldías.

## Expectativas de negocio y operativas
- **Generación de valor comercial:** Utilizar el módulo como herramienta de diagnóstico para demostrar el potencial de recaudo a las alcaldías, facilitando la venta del sistema SILIN.
- **Eficiencia operativa:** Reducir drásticamente el cuello de botella en el procesamiento de archivos FT, eliminando el trabajo manual en Excel y las validaciones "a ojímetro".
- **Trazabilidad temprana:** Implementar un flujo que permita disponibilizar información válida en minutos, no en días.
- **Respeto por la arquitectura core:** No modificar la lógica tributaria actual ni los procesos posteriores profundos de causación de SILIN; el objetivo es optimizar la validación inicial y el diagnóstico.

## Expectativas de cara al usuario (Front)
- **Validación en tiempo real:** El portal debe validar automáticamente en el momento del cargue (estructura, columnas, tipos de datos, completitud, extemporaneidad).
- **Gestión de novedades (Futuro):** Permitir la carga parcial de registros válidos y contar con un "portal de novedades" donde la comercializadora autogestione la corrección de registros inconsistentes sin detener el resto del archivo.
- **Visualización de diagnóstico:** La interfaz debe mostrar claramente la liquidación del impuesto generada y el potencial de recaudo municipal.
- **Eliminación de flujos alternos:** Sustituir la dependencia actual de enviar reportes de validación en Excel a través de correos y Slack.
