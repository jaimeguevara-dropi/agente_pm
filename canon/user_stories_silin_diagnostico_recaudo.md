# User Stories / HUs - SILIN - Diagnóstico de liquidación y potencial de recaudo

## Proyecto
SILIN - Diagnóstico de liquidación y potencial de recaudo

## Propósito de este documento
Este documento consolida las Historias de Usuario (HUs) oficiales del proyecto, alineadas al mapa de capacidades (Capabilities) y Épicas previamente definidas. Actúa como el insumo base para el desarrollo y validación del módulo de diagnóstico.

---

## CAPABILITY 1: Ingesta de dataset de liquidación

### Épica 1.1: Ingesta de dataset de liquidación

#### HU 1.1.1 - Recepción de información
- **Como** sistema
- **Quiero** recibir la información necesaria para la liquidación
- **Para** iniciar el proceso de preparación de datos

**Escenarios:**
1. **Recepción exitosa**
   - **Dado que** se entrega información para liquidación
   - **Cuando** el sistema la recibe
   - **Entonces** el proceso inicia correctamente
   - **Y** la información queda disponible para preparación
2. **Información incompleta**
   - **Dado que** se entrega información incompleta
   - **Cuando** el sistema la recibe
   - **Entonces** el proceso se marca con inconsistencias
   - **Y** no continúa a la siguiente etapa
3. **Formato no válido**
   - **Dado que** la información no cumple condiciones mínimas
   - **Cuando** el sistema intenta procesarla
   - **Entonces** el proceso es rechazado
   - **Y** se informa que no es válida

#### HU 1.1.2 - Validación de información mínima
- **Como** sistema
- **Quiero** validar que la información tenga los elementos mínimos requeridos
- **Para** asegurar que puede ser utilizada en el cálculo

**Escenarios:**
1. **Información completa**
   - **Dado que** la información contiene todos los elementos requeridos
   - **Cuando** se valida
   - **Entonces** se marca como válida
   - **Y** puede continuar al siguiente paso
2. **Información con faltantes**
   - **Dado que** falta al menos un elemento requerido
   - **Cuando** se valida
   - **Entonces** se marca como inválida
   - **Y** se detalla el faltante
3. **Información parcialmente válida**
   - **Dado que** algunos registros cumplen y otros no
   - **Cuando** se valida
   - **Entonces** se identifican los registros inconsistentes
   - **Y** se permite continuar solo con los válidos, si aplica

#### HU 1.1.3 - Registro de contexto del proceso
- **Como** sistema
- **Quiero** registrar el contexto de la liquidación
- **Para** identificar el proceso de forma única

**Escenarios:**
1. **Registro exitoso**
   - **Dado que** se inicia un proceso de liquidación
   - **Cuando** se registra su contexto
   - **Entonces** queda identificado con municipio y periodo
   - **Y** se genera un identificador único
2. **Información de contexto incompleta**
   - **Dado que** falta información del contexto
   - **Cuando** se intenta registrar
   - **Entonces** el proceso no se crea
   - **Y** se solicita completar la información
3. **Proceso duplicado**
   - **Dado que** ya existe un proceso con el mismo contexto
   - **Cuando** se intenta registrar uno nuevo
   - **Entonces** el sistema advierte duplicidad
   - **Y** permite decidir si continuar o no

#### HU 1.1.4 - Organización de información
- **Como** sistema
- **Quiero** organizar la información según su uso
- **Para** facilitar el cálculo posterior

**Escenarios:**
1. **Separación correcta**
   - **Dado que** la información es válida
   - **Cuando** se organiza
   - **Entonces** se separa en información para cálculo y del contribuyente
2. **Información mixta**
   - **Dado que** la información viene combinada
   - **Cuando** se procesa
   - **Entonces** se clasifica correctamente según su uso
3. **Información ambigua**
   - **Dado que** un dato no es claramente clasificable
   - **Cuando** se organiza
   - **Entonces** se marca para revisión

#### HU 1.1.5 - Preparación para cálculo
- **Como** sistema
- **Quiero** dejar la información lista para el cálculo
- **Para** iniciar la pre-liquidación

**Escenarios:**
1. **Preparación completa**
   - **Dado que** la información es válida
   - **Cuando** se prepara
   - **Entonces** queda lista para cálculo
2. **Información inconsistente**
   - **Dado que** existen inconsistencias
   - **Cuando** se prepara
   - **Entonces** el proceso se detiene
   - **Y** se notifica el error
3. **Preparación parcial**
   - **Dado que** solo parte de la información es válida
   - **Cuando** se prepara
   - **Entonces** se habilita el cálculo parcial, si aplica

---

## CAPABILITY 2: Cálculo de pre-liquidación tributaria

### Épica 2.1: Cálculo de pre-liquidación por contribuyente

#### HU 2.1.1 - Identificación de reglas aplicables
- **Como** sistema
- **Quiero** identificar las reglas que aplican a cada caso
- **Para** calcular correctamente el impuesto

**Escenarios:**
1. **Regla encontrada**
   - **Dado** un registro con características definidas
   - **Cuando** se evalúan las reglas
   - **Entonces** se identifica la regla aplicable
2. **Múltiples reglas posibles**
   - **Dado** un registro con múltiples condiciones
   - **Cuando** se evalúan las reglas
   - **Entonces** se selecciona la más específica
3. **Sin regla aplicable**
   - **Dado** un registro sin regla definida
   - **Cuando** se evalúa
   - **Entonces** se marca como no calculable

#### HU 2.1.2 - Aplicación de condiciones tributarias
- **Como** sistema
- **Quiero** aplicar las condiciones tributarias definidas
- **Para** determinar el valor base del impuesto

**Escenarios:**
1. **Aplicación correcta**
   - **Dado** un registro válido
   - **Cuando** se aplican las condiciones
   - **Entonces** se obtiene un valor base
2. **Condiciones incompletas**
   - **Dado** un registro con información incompleta
   - **Cuando** se aplican las condiciones
   - **Entonces** no se puede calcular
3. **Condiciones especiales**
   - **Dado** un registro con excepción tributaria
   - **Cuando** se aplica la condición
   - **Entonces** se ajusta el cálculo

#### HU 2.1.3 - Cálculo del valor
- **Como** sistema
- **Quiero** calcular el valor del impuesto por registro
- **Para** generar la pre-liquidación

**Escenarios:**
1. **Cálculo exitoso**
   - **Dado** un registro válido
   - **Cuando** se realiza el cálculo
   - **Entonces** se obtiene el valor del impuesto
2. **Error en cálculo**
   - **Dado** un registro inconsistente
   - **Cuando** se intenta calcular
   - **Entonces** se marca como error
3. **Cálculo parcial**
   - **Dado** múltiples registros
   - **Cuando** algunos fallan
   - **Entonces** los válidos se calculan correctamente

#### HU 2.1.4 - Consolidación de resultados
- **Como** sistema
- **Quiero** consolidar los resultados del cálculo
- **Para** habilitar el análisis de cartera

**Escenarios:**
1. **Consolidación completa**
   - **Dado** todos los registros calculados
   - **Cuando** se consolidan
   - **Entonces** se genera un resultado global
2. **Consolidación parcial**
   - **Dado** algunos registros fallidos
   - **Cuando** se consolidan
   - **Entonces** se incluyen solo los válidos
3. **Sin resultados**
   - **Dado que** no hay cálculos válidos
   - **Cuando** se consolida
   - **Entonces** se indica que no hay información disponible

---

## CAPABILITY 3: Análisis de cartera y generación de información para toma de decisiones

### Épica 3.1: Clasificación y cuantificación de cartera

#### HU 3.1.1 - Clasificación de obligaciones
- **Como** sistema
- **Quiero** clasificar cada obligación según su estado
- **Para** entender la situación de la cartera

**Escenarios:**
1. **Clasificación correcta**
   - **Dado** una obligación con información completa
   - **Cuando** se evalúa su estado
   - **Entonces** se clasifica como prescrita, en riesgo o recuperable
2. **Información insuficiente**
   - **Dado** una obligación con información incompleta
   - **Cuando** se intenta clasificar
   - **Entonces** se marca como no clasificable
3. **Regla ambigua**
   - **Dado** una obligación que cumple múltiples condiciones
   - **Cuando** se clasifica
   - **Entonces** se asigna la categoría más restrictiva

#### HU 3.1.2 - Cálculo de valores por categoría
- **Como** sistema
- **Quiero** calcular el valor total por cada categoría
- **Para** cuantificar el impacto financiero

**Escenarios:**
1. **Cálculo completo**
   - **Dado** obligaciones clasificadas
   - **Cuando** se suman los valores
   - **Entonces** se obtiene total por cada categoría
2. **Valores inconsistentes**
   - **Dado** obligaciones con valores inválidos
   - **Cuando** se calculan los totales
   - **Entonces** se excluyen los registros inconsistentes
3. **Sin datos**
   - **Dado que** no hay obligaciones en una categoría
   - **Cuando** se calcula el total
   - **Entonces** el valor es cero

#### HU 3.1.3 - Consolidación global
- **Como** sistema
- **Quiero** consolidar los valores a nivel general
- **Para** obtener visión financiera total

**Escenarios:**
1. **Consolidación exitosa**
   - **Dado** valores por categoría
   - **Cuando** se consolidan
   - **Entonces** se obtiene el total global
2. **Consolidación parcial**
   - **Dado** datos incompletos
   - **Cuando** se consolidan
   - **Entonces** se informa el nivel de cobertura
3. **Sin información**
   - **Dado** ausencia de datos
   - **Cuando** se consolida
   - **Entonces** se indica que no hay información disponible

### Épica 3.2: Análisis temporal y envejecimiento de cartera

#### HU 3.2.1 - Cálculo de antigüedad
- **Como** sistema
- **Quiero** calcular la antigüedad de cada obligación
- **Para** entender su envejecimiento

**Escenarios:**
1. **Cálculo correcto**
   - **Dado** una obligación con fecha definida
   - **Cuando** se calcula la antigüedad
   - **Entonces** se obtiene su edad en tiempo
2. **Fecha inválida**
   - **Dado** una obligación sin fecha válida
   - **Cuando** se calcula la antigüedad
   - **Entonces** se marca como no calculable
3. **Fecha futura**
   - **Dado** una obligación con fecha futura
   - **Cuando** se calcula la antigüedad
   - **Entonces** se ajusta a valor cero

#### HU 3.2.2 - Agrupación por rangos
- **Como** sistema
- **Quiero** agrupar obligaciones por rangos de tiempo
- **Para** analizar la distribución

**Escenarios:**
1. **Agrupación correcta**
   - **Dado** obligaciones con antigüedad
   - **Cuando** se agrupan
   - **Entonces** se distribuyen en rangos definidos
2. **Valores fuera de rango**
   - **Dado** valores extremos
   - **Cuando** se agrupan
   - **Entonces** se asignan al rango correspondiente
3. **Sin datos**
   - **Dado que** no hay obligaciones
   - **Cuando** se agrupa
   - **Entonces** no se generan rangos

#### HU 3.2.3 - Distribución de cartera
- **Como** sistema
- **Quiero** construir la distribución temporal
- **Para** entender el deterioro

**Escenarios:**
1. **Distribución completa**
   - **Dado** datos agrupados
   - **Cuando** se construye la distribución
   - **Entonces** se obtiene la proporción por rango
2. **Distribución parcial**
   - **Dado** datos incompletos
   - **Cuando** se construye la distribución
   - **Entonces** se indica cobertura parcial
3. **Sin información**
   - **Dado** ausencia de datos
   - **Cuando** se calcula la distribución
   - **Entonces** no se genera resultado

### Épica 3.3: No definida en este insumo
*(Nota: No se inventaron HUs para esta épica, respetando la estructura canónica).*

### Épica 3.4: Proyección de recaudo con y sin SILIN

#### HU 3.4.1 - Definición de supuestos
- **Como** sistema
- **Quiero** establecer supuestos de recuperación
- **Para** proyectar escenarios

**Escenarios:**
1. **Supuestos definidos**
   - **Dado** parámetros definidos
   - **Cuando** se aplican
   - **Entonces** se establecen supuestos de recuperación
2. **Supuestos incompletos**
   - **Dado** parámetros faltantes
   - **Cuando** se evalúan
   - **Entonces** no se puede proyectar
3. **Supuestos extremos**
   - **Dado** valores fuera de rango
   - **Cuando** se aplican
   - **Entonces** se ajustan a límites válidos

#### HU 3.4.2 - Escenario sin intervención
- **Como** sistema
- **Quiero** estimar el recaudo sin acciones
- **Para** tener línea base

**Escenarios:**
1. **Proyección base**
   - **Dado** cartera actual
   - **Cuando** se proyecta sin intervención
   - **Entonces** se estima el recaudo esperado
2. **Datos incompletos**
   - **Dado** información parcial
   - **Cuando** se proyecta
   - **Entonces** se indica nivel de incertidumbre
3. **Sin datos**
   - **Dado** ausencia de información
   - **Cuando** se proyecta
   - **Entonces** no se genera escenario

#### HU 3.4.3 - Escenario con intervención
- **Como** sistema
- **Quiero** estimar el recaudo optimizado
- **Para** medir impacto

**Escenarios:**
1. **Proyección optimizada**
   - **Dado** supuestos definidos
   - **Cuando** se proyecta con intervención
   - **Entonces** se estima mejora en recaudo
2. **Supuestos inconsistentes**
   - **Dado** supuestos inválidos
   - **Cuando** se proyecta
   - **Entonces** se ajustan o se rechazan
3. **Comparación no posible**
   - **Dado** ausencia de base
   - **Cuando** se proyecta
   - **Entonces** no se puede comparar

#### HU 3.4.4 - Evolución en el tiempo
- **Como** sistema
- **Quiero** proyectar el recaudo en el tiempo
- **Para** visualizar evolución

**Escenarios:**
1. **Evolución completa**
   - **Dado** un escenario calculado
   - **Cuando** se proyecta en el tiempo
   - **Entonces** se obtiene evolución por periodos
2. **Periodos incompletos**
   - **Dado** información parcial
   - **Cuando** se proyecta
   - **Entonces** se muestran solo periodos válidos
3. **Sin horizonte definido**
   - **Dado** ausencia de periodo
   - **Cuando** se proyecta
   - **Entonces** no se genera evolución

### Épica 3.5: Cálculo de impacto financiero incremental

#### HU 3.5.1 - Comparación de escenarios
- **Como** sistema
- **Quiero** comparar escenarios
- **Para** entender la diferencia

**Escenarios:**
1. **Comparación válida**
   - **Dado** dos escenarios calculados
   - **Cuando** se comparan
   - **Entonces** se obtiene la diferencia de recaudo
2. **Escenario faltante**
   - **Dado** un escenario faltante
   - **Cuando** se compara
   - **Entonces** no se puede calcular la diferencia
3. **Valores inconsistentes**
   - **Dado** valores inconsistentes
   - **Cuando** se comparan
   - **Entonces** se ajustan o se excluyen

#### HU 3.5.2 - Cálculo de valor incremental
- **Como** sistema
- **Quiero** calcular el valor adicional generado
- **Para** medir beneficio

**Escenarios:**
1. **Cálculo incremental válido**
   - **Dado** dos escenarios válidos
   - **Cuando** se calcula el incremental
   - **Entonces** se obtiene valor adicional
2. **Diferencia negativa**
   - **Dado** diferencia negativa
   - **Cuando** se calcula
   - **Entonces** se refleja pérdida
3. **Datos incompletos**
   - **Dado** datos incompletos
   - **Cuando** se calcula
   - **Entonces** se marca como no disponible

#### HU 3.5.3 - Impacto en periodo de gobierno
- **Como** sistema
- **Quiero** estimar el impacto en el periodo del alcalde
- **Para** contextualizar el beneficio

**Escenarios:**
1. **Horizonte definido**
   - **Dado** horizonte definido
   - **Cuando** se calcula impacto
   - **Entonces** se obtiene valor en ese periodo
2. **Periodo incompleto**
   - **Dado** periodo incompleto
   - **Cuando** se calcula
   - **Entonces** se ajusta proporcionalmente
3. **Sin horizonte**
   - **Dado** ausencia de horizonte
   - **Cuando** se calcula
   - **Entonces** no se genera resultado

---

## CAPABILITY 4: Disponibilización de resultados del liquidador

### Épica 4.1: Consulta de estado de cartera

#### HU 4.1.1 - Consulta de estado de cartera
- **Como** consumidor de información
- **Quiero** consultar el estado de la cartera
- **Para** conocer la situación financiera

**Escenarios:**
1. **Contexto válido**
   - **Dado** un contexto válido de consulta
   - **Cuando** se solicita el estado de cartera
   - **Entonces** se obtiene la información de cartera prescrita, en riesgo y recuperable
2. **Contexto inválido**
   - **Dado** un contexto inválido
   - **Cuando** se consulta el estado de cartera
   - **Entonces** no se obtiene información
   - **Y** se indica que el contexto no es válido
3. **Sin información disponible**
   - **Dado que** no existe información disponible
   - **Cuando** se consulta el estado de cartera
   - **Entonces** se indica que no hay datos

#### HU 4.1.2 - Consulta de totales agregados
- **Como** consumidor de información
- **Quiero** consultar los totales de cartera
- **Para** entender el impacto global

**Escenarios:**
1. **Información disponible**
   - **Dado** información disponible
   - **Cuando** se consultan los totales
   - **Entonces** se obtiene el valor total por categoría
2. **Información parcial**
   - **Dado** información parcial
   - **Cuando** se consultan los totales
   - **Entonces** se informa el nivel de cobertura
3. **Ausencia de datos**
   - **Dado** ausencia de datos
   - **Cuando** se consultan los totales
   - **Entonces** se indica que no hay información disponible

### Épica 4.2: Consulta de escenarios y comparativos

#### HU 4.2.1 - Consulta de escenario sin intervención
- **Como** consumidor de información
- **Quiero** consultar el escenario sin intervención
- **Para** entender la línea base

**Escenarios:**
1. **Escenario base calculado**
   - **Dado** un escenario base calculado
   - **Cuando** se consulta
   - **Entonces** se obtiene la proyección de recaudo sin intervención
2. **Información incompleta**
   - **Dado** información incompleta
   - **Cuando** se consulta
   - **Entonces** se informa el nivel de incertidumbre
3. **Ausencia de escenario**
   - **Dado** ausencia de escenario
   - **Cuando** se consulta
   - **Entonces** no se obtiene resultado

#### HU 4.2.2 - Consulta de escenario con intervención
- **Como** consumidor de información
- **Quiero** consultar el escenario optimizado
- **Para** entender el potencial de mejora

**Escenarios:**
1. **Escenario optimizado**
   - **Dado** un escenario optimizado
   - **Cuando** se consulta
   - **Entonces** se obtiene la proyección con mejora
2. **Supuestos inválidos**
   - **Dado** supuestos inválidos
   - **Cuando** se consulta
   - **Entonces** se indica inconsistencia
3. **Ausencia de datos**
   - **Dado** ausencia de datos
   - **Cuando** se consulta
   - **Entonces** no se genera resultado

#### HU 4.2.3 - Consulta comparativa de escenarios
- **Como** consumidor de información
- **Quiero** comparar escenarios
- **Para** entender la diferencia de recaudo

**Escenarios:**
1. **Ambos escenarios disponibles**
   - **Dado** ambos escenarios disponibles
   - **Cuando** se consultan
   - **Entonces** se obtiene la diferencia de recaudo
2. **Escenario faltante**
   - **Dado que** falta uno de los escenarios
   - **Cuando** se comparan
   - **Entonces** no se puede generar comparación
3. **Datos inconsistentes**
   - **Dado** datos inconsistentes
   - **Cuando** se comparan
   - **Entonces** se indica inconsistencia en resultados

---

## CAPABILITY 5: Preparación de información para visualización

### Épica 5.1: Información de resumen ejecutivo

#### HU 5.1.1 - Consolidación de métricas principales
- **Como** sistema
- **Quiero** consolidar las métricas principales
- **Para** facilitar su visualización

**Escenarios:**
1. **Métricas calculadas**
   - **Dado** métricas calculadas
   - **Cuando** se consolidan
   - **Entonces** se agrupan en una vista resumida
2. **Métricas parciales**
   - **Dado** métricas parciales
   - **Cuando** se consolidan
   - **Entonces** se indica cobertura parcial
3. **Ausencia de métricas**
   - **Dado** ausencia de métricas
   - **Cuando** se consolidan
   - **Entonces** no se genera resumen

#### HU 5.1.2 - Estructuración de información simplificada
- **Como** sistema
- **Quiero** estructurar la información de forma simple
- **Para** facilitar su consumo

**Escenarios:**
1. **Información consolidada**
   - **Dado** información consolidada
   - **Cuando** se estructura
   - **Entonces** se presenta de forma clara y directa
2. **Información compleja**
   - **Dado** información compleja
   - **Cuando** se estructura
   - **Entonces** se simplifica manteniendo significado
3. **Información inconsistente**
   - **Dado** información inconsistente
   - **Cuando** se estructura
   - **Entonces** se marca como no confiable

### Épica 5.2: Construcción de proyecciones

#### HU 5.2.1 - Organización temporal de información
- **Como** sistema
- **Quiero** organizar la información en el tiempo
- **Para** facilitar su análisis

**Escenarios:**
1. **Información disponible**
   - **Dado** información disponible
   - **Cuando** se organiza
   - **Entonces** se distribuye por periodos
2. **Información parcial**
   - **Dado** información parcial
   - **Cuando** se organiza
   - **Entonces** se muestran solo periodos válidos
3. **Ausencia de tiempo definido**
   - **Dado** ausencia de tiempo definido
   - **Cuando** se organiza
   - **Entonces** no se genera estructura temporal

#### HU 5.2.2 - Preparación de comparativos
- **Como** sistema
- **Quiero** preparar la información comparativa
- **Para** facilitar la visualización de escenarios

**Escenarios:**
1. **Dos escenarios disponibles**
   - **Dado** dos escenarios
   - **Cuando** se preparan
   - **Entonces** se alinean para comparación
2. **Escenarios incompletos**
   - **Dado** escenarios incompletos
   - **Cuando** se preparan
   - **Entonces** se indica limitación
3. **Un solo escenario**
   - **Dado** un solo escenario
   - **Cuando** se prepara
   - **Entonces** no se genera comparativo

---

## CAPABILITY 6: Visualización ejecutiva para entidades

### Épica 6.1: Vista de estado de cartera (cards principales)

#### HU 6.1.1 - Visualización de estados de cartera
- **Como** tomador de decisión
- **Quiero** ver el estado de la cartera
- **Para** entender rápidamente la situación

**Escenarios:**
1. **Métricas disponibles**
   - **Dado** métricas disponibles
   - **Cuando** se visualizan
   - **Entonces** se muestran cartera prescrita, en riesgo y recuperable
2. **Información parcial**
   - **Dado** información parcial
   - **Cuando** se visualiza
   - **Entonces** se indica cobertura parcial
3. **Ausencia de datos**
   - **Dado** ausencia de datos
   - **Cuando** se visualiza
   - **Entonces** se muestra estado vacío

### Épica 6.2: Visualización de escenarios de recaudo

#### HU 6.2.1 - Comparación visual de escenarios
- **Como** tomador de decisión
- **Quiero** comparar escenarios visualmente
- **Para** entender el impacto

**Escenarios:**
1. **Escenarios disponibles**
   - **Dado** escenarios disponibles
   - **Cuando** se visualizan
   - **Entonces** se comparan claramente
2. **Escenarios incompletos**
   - **Dado** escenarios incompletos
   - **Cuando** se visualizan
   - **Entonces** se indica limitación
3. **Ausencia de escenarios**
   - **Dado** ausencia de escenarios
   - **Cuando** se visualiza
   - **Entonces** no se muestra comparación

#### HU 6.2.2 - Visualización temporal
- **Como** tomador de decisión
- **Quiero** ver la evolución en el tiempo
- **Para** entender tendencias

**Escenarios:**
1. **Datos en el tiempo**
   - **Dado** datos en el tiempo
   - **Cuando** se visualizan
   - **Entonces** se muestra evolución
2. **Datos incompletos**
   - **Dado** datos incompletos
   - **Cuando** se visualizan
   - **Entonces** se muestra parcial
3. **Sin datos**
   - **Dado** sin datos
   - **Cuando** se visualiza
   - **Entonces** no se muestra evolución

### Épica 6.3: Visualización de impacto financiero

#### HU 6.3.1 - Visualización de valor incremental
- **Como** tomador de decisión
- **Quiero** ver el valor adicional generado
- **Para** entender el beneficio

**Escenarios:**
1. **Valor calculado**
   - **Dado** valor calculado
   - **Cuando** se visualiza
   - **Entonces** se muestra el incremento
2. **Valor negativo**
   - **Dado** valor negativo
   - **Cuando** se visualiza
   - **Entonces** se muestra impacto negativo
3. **Sin cálculo**
   - **Dado** sin cálculo
   - **Cuando** se visualiza
   - **Entonces** no se muestra resultado

#### HU 6.3.2 - Visualización de impacto total
- **Como** tomador de decisión
- **Quiero** ver el impacto total
- **Para** entender el beneficio global

**Escenarios:**
1. **Impacto calculado**
   - **Dado** impacto calculado
   - **Cuando** se visualiza
   - **Entonces** se muestra valor total
2. **Datos incompletos**
   - **Dado** datos incompletos
   - **Cuando** se visualiza
   - **Entonces** se indica limitación
3. **Sin datos**
   - **Dado** sin datos
   - **Cuando** se visualiza
   - **Entonces** no se muestra impacto

### Épica 6.4: Narrativa ejecutiva de impacto

#### HU 6.4.1 - Generación de mensaje ejecutivo
- **Como** tomador de decisión
- **Quiero** ver un mensaje claro de impacto
- **Para** entender rápidamente la situación

**Escenarios:**
1. **Métricas disponibles**
   - **Dado** métricas disponibles
   - **Cuando** se genera el mensaje
   - **Entonces** se comunica cuánto se perdió, está en riesgo y se puede recuperar
2. **Información parcial**
   - **Dado** información parcial
   - **Cuando** se genera el mensaje
   - **Entonces** se indica limitación
3. **Ausencia de datos**
   - **Dado** ausencia de datos
   - **Cuando** se genera el mensaje
   - **Entonces** no se construye mensaje

#### HU 6.4.2 - Construcción de narrativa
- **Como** sistema
- **Quiero** estructurar la información como historia
- **Para** facilitar la toma de decisiones

**Escenarios:**
1. **Métricas completas**
   - **Dado** métricas completas
   - **Cuando** se construye la narrativa
   - **Entonces** se presenta secuencia lógica de impacto
2. **Métricas parciales**
   - **Dado** métricas parciales
   - **Cuando** se construye la narrativa
   - **Entonces** se presenta narrativa parcial
3. **Sin métricas**
   - **Dado** sin métricas
   - **Cuando** se construye la narrativa
   - **Entonces** no se genera historia
