# Capabilities / Épicas - SILIN - Diagnóstico de liquidación y potencial de recaudo

## Proyecto
SILIN - Diagnóstico de liquidación y potencial de recaudo

## Propósito de este documento
Este documento consolida las capacidades y épicas funcionales oficiales del proyecto. Actúa como el mapa canónico para entender la estructura funcional del módulo de diagnóstico, sobre el cual se estructurarán las historias de usuario.

---

# Mapa de Capacidades

## CAPABILITY 1 - Ingesta de dataset de liquidación

### Propósito de la capability
Recibir y organizar la información necesaria para iniciar el proceso de cálculo tributario, asegurando que cumpla con las condiciones mínimas requeridas.

### Épica 1.1 - Ingesta de dataset de liquidación
- **Propósito:** Recibir y organizar la información necesaria para iniciar el proceso de cálculo tributario, asegurando que cumpla con las condiciones mínimas requeridas.
- **Alcance funcional:**
  - Recibir la información proveniente de fuentes validadas
  - Verificar que la información tenga los campos mínimos requeridos
  - Registrar información del proceso (municipio, periodo, identificador del proceso)
  - Organizar la información en estructuras utilizables para el cálculo
- **Campos mínimos esperados:** `numero_medidor`, `periodo`, `consumo_kwh`, `tipo_usuario`, `estrato`, `destino_economico`.
- **Consideración:** Sí se incluyen datos de contribuyente, pero como parte del mismo flujo de lectura. Se separa la información en información para cálculo y del contribuyente.
- **Resultados esperados:** Información lista para ser utilizada en el cálculo tributario. Proceso preparado para iniciar la pre-liquidación.
- **Exclusiones:** Cálculo tributario, generación de indicadores, visualización, validación contra SILIN, registro definitivo en plataforma.

---

## CAPABILITY 2 - Cálculo de pre-liquidación tributaria

### Propósito de la capability
Determinar el valor del impuesto a partir de la información recibida y las reglas tributarias definidas.

### Épica 2.1 - Cálculo de pre-liquidación por contribuyente
- **Propósito:** Determinar el valor del impuesto a partir de la información recibida y las reglas tributarias definidas.
- **Alcance funcional:**
  - Aplicar reglas tributarias definidas
  - Aplicar tarifas correspondientes
  - Calcular el valor del impuesto por cada registro
  - Generar resultados de pre-liquidación
- **Consideración importante:** Las reglas ya existen en tablas/macros y deben quedar documentadas, entendidas y explícitas en historias.
- **Resultados esperados:** Valores calculados por cada registro. Información lista para análisis de cartera.
- **Exclusiones:** Causación del impuesto, validación manual, facturación, decisión de liquidación definitiva.

---

## CAPABILITY 3 - Análisis de cartera y generación de información para toma de decisiones

### Propósito de la capability
Transformar los resultados de la pre-liquidación en información clara que permita a la entidad entender su situación financiera y tomar decisiones (construir narrativa financiera: Perdí esto → estoy a punto de perder esto → puedo recuperar esto → con SILIN gano esto).

### Épica 3.1 - Clasificación y cuantificación de cartera
- **Propósito:** Clasificar la cartera tributaria y cuantificar el impacto financiero en cada estado.
- **Alcance funcional:** Calcular valor total de cartera prescrita, en riesgo y recuperable; asignar obligación a categoría y consolidar por municipio.
- **Resultados esperados:** Valor total de dinero perdido, valor en riesgo, universo de recaudo recuperable.
- **Exclusiones:** Visualización, proyecciones futuras.

### Épica 3.2 - Análisis temporal y envejecimiento de cartera
- **Propósito:** Analizar cómo evoluciona la cartera en el tiempo para entender su deterioro.
- **Alcance funcional:** Calcular edad de la deuda, agrupar por rangos (0-1, 1-3, 3-5, 5+), construir distribución temporal e identificar transiciones.
- **Resultados esperados:** Distribución temporal de la deuda, visual del deterioro, entendimiento del envejecimiento.
- **Exclusiones:** Predicción futura, intervención operativa.

### Épica 3.3 - No definida en este insumo
*(Nota: La numeración 3.3 no fue definida explícitamente en el mapa entregado y se deja esta referencia para mantener la trazabilidad sin inventar una nueva épica).*

### Épica 3.4 - Proyección de recaudo con y sin SILIN
- **Propósito:** Estimar el impacto financiero de implementar SILIN en la recuperación de cartera.
- **Alcance funcional:** Definir supuestos de recuperación, modelar mejora en recaudo, proyectar en el tiempo y estimar impacto a plazos.
- **Resultados esperados:** Escenario optimizado de recaudo, proyección de ingresos con SILIN.
- **Exclusiones:** Ejecución real de recaudo, automatización operativa.

### Épica 3.5 - Cálculo de impacto financiero incremental
- **Propósito:** Cuantificar el valor adicional generado por implementar SILIN.
- **Alcance funcional:** Calcular diferencia entre escenarios, estimar valor incremental recuperado, impacto durante periodo del alcalde e ingresos adicionales.
- **Resultados esperados:** Valor incremental claro, impacto financiero cuantificado, argumento comercial directo.
- **Exclusiones:** Detalle por contribuyente, ejecución de cobro.

---

## CAPABILITY 4 - Disponibilización de resultados del liquidador

### Propósito de la capability
Permitir que los resultados generados puedan ser utilizados por otras capas del sistema (frontend ejecutivo, otros sistemas SILIN, integraciones externas), garantizando que el liquidador sea reutilizable y desacoplado.

### Épica 4.1 - Consulta de estado de cartera
- **Propósito:** Exponer los indicadores agregados de cartera para consumo del frontend ejecutivo.
- **Alcance funcional:** Consulta por municipio/periodo; entrega de cartera prescrita, en riesgo y recuperable con totales agregados.
- **Resultados esperados:** Frontend puede consumir métricas en tiempo real; consistencia de datos entre backend y UI.
- **Exclusiones:** Detalle por contribuyente, lógica de cálculo.

### Épica 4.2 - Consulta de escenarios y comparativos
- **Propósito:** Exponer para consumo los escenarios de recaudo sin intervención, con intervención y su comparación.
- **Alcance funcional:** Consulta de escenario sin intervención, con intervención y consulta comparativa de escenarios.
- **Resultados esperados:** Integración desacoplada, habilita automatización futura, consumo de proyecciones por otras capas.
- **Exclusiones:** Orquestación de flujos, ejecución de procesos posteriores.

---

## CAPABILITY 5 - Preparación de información para visualización

### Propósito de la capability
Organizar la información de forma que pueda ser fácilmente interpretada en una interfaz, facilitando el consumo rápido, visualización clara y carga eficiente en frontend.

### Épica 5.1 - Información de resumen ejecutivo
- **Propósito:** Generar data consolidada con las métricas principales de cartera.
- **Alcance funcional:** Consolidar cartera prescrita, en riesgo y recuperable; calcular totales y estructurar respuesta simple.
- **Resultados esperados:** Data lista para cards principales del dashboard.
- **Exclusiones:** Visualización, análisis detallado.

### Épica 5.2 - Construcción de proyecciones
- **Propósito:** Preparar los datos necesarios para visualizar escenarios de recaudo.
- **Alcance funcional:** Estructurar proyección sin SILIN y con SILIN; organizar datos por periodos.
- **Resultados esperados:** Data lista para gráficos comparativos.
- **Exclusiones:** Lógica de simulación avanzada, edición de escenarios.

---

## CAPABILITY 6 - Visualización ejecutiva para entidades

### Propósito de la capability
Proveer una interfaz clara, directa y orientada a tomadores de decisión que permita entender en segundos el estado de la cartera, impacto financiero y valor de implementar SILIN.

### Épica 6.1 - Vista de estado de cartera (cards principales)
- **Propósito:** Mostrar de forma clara los tres estados principales de la cartera.
- **Alcance funcional:** Mostrar cartera prescrita, en riesgo, recuperable y totales con diseño claro tipo cards.
- **Resultados esperados:** Comprensión inmediata del estado financiero.
- **Exclusiones:** Drill-down, navegación a detalle.

### Épica 6.2 - Visualización de escenarios de recaudo
- **Propósito:** Comparar el comportamiento del recaudo con y sin SILIN.
- **Alcance funcional:** Gráfico comparativo, evolución en el tiempo y diferencia entre escenarios.
- **Resultados esperados:** Evidencia clara del impacto de SILIN.
- **Exclusiones:** Simulaciones dinámicas, ajustes manuales.

### Épica 6.3 - Visualización de impacto financiero
- **Propósito:** Comunicar el valor económico que SILIN genera.
- **Alcance funcional:** Mostrar valor incremental, impacto en periodo del alcalde e ingresos proyectados.
- **Resultados esperados:** Argumento comercial directo.
- **Exclusiones:** Cálculo complejo en frontend, personalización avanzada.

### Épica 6.4 - Narrativa ejecutiva de impacto
- **Propósito:** Traducir las métricas en un mensaje claro para tomadores de decisión.
- **Alcance funcional:** Mostrar mensaje tipo "cuánto se perdió, cuánto se puede perder, cuánto se puede recuperar" y estructurar storytelling.
- **Resultados esperados:** Comprensión inmediata, apoyo a venta.
- **Exclusiones:** Personalización por usuario, contenido dinámico complejo.
