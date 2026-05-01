# Proyecto: SILIN - Diagnóstico de liquidación y potencial de recaudo

Este documento es un **BORRADOR** para recibir y estructurar la información inicial del proyecto. No se considerará memoria oficial hasta su aprobación explícita.

## 1. Business Context del proyecto
SILIN (Sistema de Liquidación de Impuestos) requiere procesar archivos FT (FT-01, FT-03, FT-05, FT-06) provenientes de las comercializadoras de energía. Actualmente, el flujo desde la carga del archivo hasta la liquidación del impuesto y causación de deudas es fragmentado e involucra múltiples equipos (Tributaria, Analítica de Datos, Base de Datos/SILIN) con altos cuellos de botella operativos y revisiones manuales. 

El proyecto busca implementar un módulo de **"Diagnóstico de liquidación y potencial de recaudo"** que valide eficientemente la estructura de los archivos, calcule la liquidación del impuesto y muestre el valor total que el municipio podría recaudar. Esto servirá como herramienta de diagnóstico y demostración de valor económico para facilitar la venta del software completo de SILIN a las alcaldías.

## 2. Expectativas de negocio
- **Generación de valor comercial:** Utilizar el módulo como herramienta de diagnóstico para demostrar el potencial de recaudo a las alcaldías, facilitando la venta del sistema SILIN.
- **Eficiencia operativa:** Reducir drásticamente el cuello de botella en el procesamiento de archivos FT, eliminando el trabajo manual en Excel y las validaciones "a ojímetro".
- **Trazabilidad temprana:** Implementar un flujo que permita disponibilizar información válida en minutos, no en días.
- **Respeto por la arquitectura core:** No modificar la lógica tributaria actual ni los procesos posteriores profundos de causación de SILIN; el objetivo es optimizar la validación inicial y el diagnóstico.

## 3. Expectativas del front
- **Validación en tiempo real:** El portal debe validar automáticamente en el momento del cargue (estructura, columnas, tipos de datos, completitud, extemporaneidad).
- **Gestión de novedades (Futuro):** Permitir la carga parcial de registros válidos y contar con un "portal de novedades" donde la comercializadora autogestione la corrección de registros inconsistentes sin detener el resto del archivo.
- **Visualización de diagnóstico:** La interfaz debe mostrar claramente la liquidación del impuesto generada y el potencial de recaudo municipal.
- **Eliminación de flujos alternos:** Sustituir la dependencia actual de enviar reportes de validación en Excel a través de correos y Slack.

## 4. AS-IS consolidado
El proceso actual es un anti-patrón de integración, altamente fragmentado, manual y propenso a errores:
- **Carga y Tributaria:** Las comercializadoras suben archivos TXT a un portal (repositorio simple). Tributaria descarga, revisa manualmente en Excel (delimitadores, columnas, formatos) y realiza cruces manuales (consumo vs recaudo). Si hay errores, notifican por correo solicitando la recarga completa del archivo.
- **Analítica de Datos (Julián):** Recibe archivos "prevalidados". Realiza revisión visual ("ojímetro") y cruces manuales (FT-03 vs FT-01) para recuperar datos erróneos. Sube a S3 para que un Lambda valide estructura, pero luego elimina manualmente columnas para que Base de Datos los acepte.
- **Base de Datos (Sammy/Anyela/SILIN):** Valida estructura vía Postman y ejecuta un endpoint de "dispersión". El proceso interno liquida el impuesto y actualiza vistas. Para archivos grandes (>500 registros), los triggers bloquean la base de datos, obligando a reprocesos manuales nocturnos. Los tokens expiran y hay caídas de websockets.
- **Cierre:** La confirmación final se da exportando un reporte en Excel de la base de datos que se envía por Slack a Tributaria para su aprobación, antes de pasar a producción.

## 5. TO-BE consolidado
- **Carga y Validación Automática:** Las comercializadoras cargan archivos en la plataforma, y la validación estructural y de completitud se realiza automáticamente en tiempo real, sin intervención humana.
- **Procesamiento Parcial:** El sistema permite el procesamiento de registros válidos y aísla los erróneos, eliminando la necesidad de devolver archivos completos.
- **Autogestión:** Las comercializadoras podrán corregir sus registros inconsistentes directamente en un portal de novedades.
- **Cálculo y Cruces Integrados:** La plataforma ejecuta automáticamente los cruces requeridos (consumo vs recaudo) y la liquidación de impuestos, unificando las reglas hoy dispersas entre Analítica y Base de Datos.
- **Tablero de Diagnóstico Inmediato:** Una vez procesado, el sistema muestra visualmente a la alcaldía el potencial de recaudo (liquidación generada) como demostración de valor y diagnóstico.

## 6. Capabilities (Capacidades)
*(Espacio para definir las capacidades técnicas y funcionales requeridas...)*

## 7. HUs (Historias de Usuario)
*(Espacio para detallar las historias de usuario...)*

## 8. Objetivos de diseño para prototipado
*(Espacio para recibir los objetivos antes de iniciar la construcción de pantallas...)*
