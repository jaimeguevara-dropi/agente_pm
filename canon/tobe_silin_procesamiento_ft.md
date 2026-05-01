# TO-BE - SILIN - Procesamiento inteligente y parcial de archivos FT

## Nombre del proyecto
SILIN - Procesamiento inteligente FT

## Propósito de este TO-BE
Este documento define el estado futuro esperado para el procesamiento de archivos FT en SILIN, orientado a habilitar la cadena tributaria en tiempos operativos mínimos mediante un procesamiento automático, parcial, inteligente y escalable.

El TO-BE busca reemplazar la lógica actual altamente manual, secuencial y bloqueante por una capacidad de procesamiento que permita extraer valor operativo desde etapas tempranas, sin depender de que el lote completo esté perfecto.

## Resumen ejecutivo del TO-BE
En el estado futuro, SILIN debe ser capaz de recibir archivos FT de gran volumen y convertirlos, de forma automática, inteligente y en tiempos operativos mínimos, en salidas útiles para la cadena tributaria, sin depender de que el lote completo esté perfecto ni de intervención humana constante.

El sistema ya no debe comportarse como un flujo rígido que espera la validación integral del archivo para generar valor, sino como una capacidad que:
- interpreta y procesa el lote por partes,
- identifica rápidamente qué registros son utilizables,
- aísla inconsistencias sin bloquear la operación,
- genera salidas parciales según propósito,
- y habilita oportunamente los pasos posteriores del negocio tributario.

La lógica central del TO-BE es que el valor del archivo FT no está en tenerlo cargado, sino en transformarlo rápidamente en información operable.

## Principio rector del TO-BE
El procesamiento del FT debe permitir que la operación avance con los registros válidos sin esperar a que todo el lote esté limpio, reduciendo al mínimo la fricción entre calidad de datos y continuidad operativa.

Esto implica que el sistema debe estar diseñado para:
- aprovechar valor parcial desde etapas tempranas,
- separar automáticamente lo válido, lo inválido y lo observacional,
- y disponibilizar resultados útiles para la cadena tributaria en el menor tiempo posible.

## Estado futuro esperado
Cuando un archivo FT ingrese al sistema en el estado futuro:

- se recibe y reconoce estructuralmente,
- se procesa de forma escalable sobre grandes volúmenes,
- se validan reglas clave del contenido,
- se detectan duplicados, inconsistencias y anomalías,
- se separan los registros según su condición y propósito,
- se generan salidas parciales listas para consumo operativo,
- y la cadena tributaria puede continuar con los registros habilitados, sin depender del saneamiento total del lote.

## Qué cambia frente al AS-IS
En el TO-BE, el archivo FT deja de ser un insumo monolítico que frena el proceso completo cuando presenta errores parciales.

Pasa a ser un insumo que el sistema puede tratar con una lógica más madura, donde:
- el lote no se maneja como un todo indivisible,
- los errores no detienen innecesariamente el avance de lo correcto,
- las salidas ya no son genéricas sino orientadas al negocio,
- y el procesamiento se mide por tiempo de habilitación operativa, no solo por ejecución técnica.

## Naturaleza del estado futuro
El TO-BE plantea un proceso:

- más automatizado,
- más observable,
- más escalable,
- menos dependiente de intervención humana operativa,
- capaz de soportar grandes volúmenes,
- con clasificación por registro,
- con avance parcial útil,
- y con trazabilidad transversal durante todo el ciclo del lote.

La intervención humana no desaparece por completo, pero debe concentrarse en control, supervisión, revisión excepcional y toma de decisiones, no en tareas repetitivas de revisión, recuperación o reproceso masivo.

## Capacidades del TO-BE

### 1. Recepción de lotes FT
El estado futuro arranca con una recepción controlada del archivo FT, donde cada archivo entra al sistema y se convierte desde el primer momento en un lote formal de procesamiento.

Ese lote debe tener:
- identidad propia,
- asociación mínima a comercializadora,
- entidad,
- período,
- tipo de archivo,
- trazabilidad inicial,
- estados claros,
- actualización automática de estado.

En esta etapa no se ejecutan validaciones profundas ni lógica tributaria final; el objetivo es encapsular el archivo como una unidad operativa formal del pipeline.

### 2. Validación estructural y funcional del archivo
Una vez creado el lote, el sistema debe validar primero la estructura del archivo y luego evaluar cada registro de forma independiente.

Aquí aparece uno de los cambios más importantes del TO-BE:
- si el archivo tiene un problema estructural, se rechaza el lote,
- pero si la estructura es válida, cada registro se clasifica individualmente como válido o inválido con su motivo,
- sin detener el procesamiento de los demás.

Esta capacidad no corrige datos ni toma decisiones tributarias finales; prepara la base para el procesamiento parcial posterior.

### 3. Gestión de registros inválidos
Los registros inválidos no deben desaparecer ni quedar difusos. Deben mantenerse controlados, clasificados y visibles.

Cada registro inválido debe quedar asociado a:
- tipo de error,
- campo afectado,
- motivo funcional o estructural,
- estado `PENDIENTE_DE_CORRECCIÓN`,
- y trazabilidad con el lote original.

Además, debe existir consulta interna por lote, entidad y período para que soporte, producto o tributaria puedan ver cuántos inválidos hay y por qué.

Esta capacidad no asume sanciones, tiempos ni comunicaciones externas; su función es exponer y ordenar el problema.

### 4. Disponibilización de registros válidos del lote FT para dispersión en SILIN
Con el resultado de la validación, el sistema debe tomar únicamente los registros válidos y disponibilizarlos en los formatos de salida que correspondan, específicamente FT-01 y/o FT-06, según la composición del lote.

El sistema no ejecuta la dispersión, pero sí debe:
- dejar los archivos listos,
- identificados,
- depositados en un repositorio controlado,
- y registrar feedback técnico posterior de la dispersión.

También debe evitar regeneraciones automáticas duplicadas.

Aquí está el corazón del procesamiento parcial:
lo válido avanza aunque existan inválidos en el mismo lote.

### 5. Revalidación incremental de registros inválidos
El TO-BE define que no se debe reprocesar un lote completo solo porque algunos registros fueron corregidos.

En cambio, los registros previamente inválidos y luego corregidos deben poder:
- entrar por los mismos canales,
- asociarse al lote original,
- pasar por revalidación incremental,
- y reincorporarse automáticamente al flujo si quedan válidos.

Si aplica, esta revalidación también debe actualizar el estado agregado del lote.

Esta capacidad es clave para romper la dependencia de reprocesos masivos y mejorar eficiencia operativa.

### 6. Gestión, rescate y notificación de registros rechazados
Después de validar e intentar rescatar registros inválidos, el sistema debe cerrar el ciclo del error a nivel de registro.

Eso implica:
- intentar rescatar lo recuperable,
- identificar lo irrecuperable,
- y notificar oficialmente los registros rechazados.

La intención es eliminar la ambigüedad operativa sobre qué sigue y qué no.

En esta definición también aparece una hipótesis funcional importante:
el ID del medidor puede operar como llave principal de búsqueda, considerando que un contribuyente puede tener múltiples medidores.

### 7. Estados y trazabilidad transversal del procesamiento FT
De forma transversal a toda la cadena, el TO-BE incluye una capacidad específica de estados y trazabilidad.

El sistema debe:
- registrar el estado técnico del lote durante todo su ciclo de vida,
- mantener estado individual por registro,
- guardar historial básico de cambios,
- permitir consulta por entidad, período y lote,
- y reflejar eventos posteriores como validaciones o resultados técnicos sin mezclar estados técnicos con estados normativos.

Esta capacidad es la que vuelve observable y gobernable todo el flujo.

## Comportamiento esperado del sistema en el TO-BE
En el estado futuro, el sistema debe ser capaz de:

- reconocer formalmente el archivo como lote de procesamiento,
- distinguir entre rechazo estructural del lote y rechazo puntual de registros,
- clasificar y separar registros por condición,
- disponibilizar rápidamente lo procesable,
- mantener visibilidad de lo inválido,
- reincorporar correcciones sin reprocesos masivos,
- y sostener trazabilidad de punta a punta.

## Beneficios esperados del TO-BE
El TO-BE busca producir beneficios concretos para la operación:

- menor bloqueo por errores parciales,
- habilitación más rápida de la cadena tributaria,
- mejor aprovechamiento de registros válidos,
- reducción de reprocesos completos,
- mayor resiliencia frente a calidad de datos imperfecta,
- mejor gobernabilidad del procesamiento,
- trazabilidad más clara,
- y mejor compatibilidad con altos volúmenes de información.

## Relación del TO-BE con el AS-IS
Este TO-BE responde directamente a un AS-IS donde hoy existen:
- validaciones manuales intensivas,
- bloqueo por problemas parciales,
- handoffs múltiples entre equipos,
- dependencia de recuperación manual de datos,
- y una operación costosa en esfuerzo humano.

El estado futuro busca reducir precisamente esas dependencias sin perder control ni trazabilidad.

## Conclusión del TO-BE
El futuro esperado para este proyecto es que SILIN deje de tratar los archivos FT como una carga monolítica que debe estar completamente perfecta para generar valor.

En su lugar, debe tratarlos como una fuente de información parcialmente aprovechable, donde el sistema pueda identificar rápidamente lo que sí sirve, aislar lo que no sirve, y mover la operación con velocidad, criterio y continuidad.

Este TO-BE sienta la base para un procesamiento FT más automatizado, escalable, resiliente y alineado con una cadena tributaria que necesita operar en tiempos mínimos, incluso bajo condiciones de volumen alto y calidad parcial de datos.
