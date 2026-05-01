# TO-BE - SILIN - Diagnóstico de liquidación y potencial de recaudo

El proceso objetivo busca eliminar los silos de integración manuales y proveer un flujo continuo, desde la carga hasta el diagnóstico de la liquidación, de forma asíncrona y resiliente.

## Carga y Validación Automática
Las comercializadoras cargan los archivos FT a través de la plataforma. De manera inmediata, el sistema realiza la validación estructural y de completitud (columnas, formatos esperados, reglas básicas) sin intervención humana. El resultado de la validación inicial se notifica directamente en la plataforma.

## Procesamiento Parcial y Autogestión (Portal de Novedades)
El sistema permite el procesamiento asíncrono y en streaming (arquitectura ECS) de los registros válidos y aísla los registros erróneos. Estos registros erróneos se disponibilizan en un "portal de novedades" donde la comercializadora puede corregirlos en línea (autogestión), eliminando la necesidad de devolver archivos completos por correo electrónico y reiniciar el ciclo para todo el lote.

## Cálculo y Cruces Integrados
Una vez la información pasa la validación estructural, la plataforma ejecuta automáticamente los cruces requeridos (ej. consumo vs recaudo) y realiza el cálculo de la liquidación de impuestos, utilizando un motor de reglas unificado. Esto elimina la necesidad de pre-procesamiento ("ojímetro") o eliminación manual de columnas y unifica la lógica de negocio.

## Tablero de Diagnóstico Inmediato
En cuestión de minutos tras el cargue y validación parcial, el sistema despliega un tablero visual (diagnóstico). Este tablero muestra a la entidad territorial y al equipo interno de tributaria la liquidación del impuesto generada y el potencial de recaudo municipal, operando como una demostración del valor económico y facilitando la venta del sistema.
