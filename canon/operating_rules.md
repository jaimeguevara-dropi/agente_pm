# Reglas operativas del PM Operating System

## Principios

1. **Transcripts es evidencia inmutable.**
   No se reescribe, no se resume encima y no se usa como verdad aprobada sin validación humana.

2. **Draft_Insights es memoria temporal.**
   Todo borrador, hipótesis o síntesis vive aquí hasta aprobación explícita.

3. **Approved_Context es memoria oficial.**
   Solo esta tabla se usa como contexto persistente para decisiones futuras, reportes y seguimiento.

4. **No usar borradores como verdad.**
   Ningún workflow operativo debe tratar iteraciones no aprobadas como fuente oficial.

5. **No borrar estructura automáticamente.**
   El sistema puede crear tablas y campos faltantes, pero no debe borrar tablas, campos ni datos sin instrucción humana explícita.

6. **Toda promoción debe dejar trazabilidad.**
   Cada elemento aprobado debe enlazar, al menos por referencia textual, a la transcripción o reunión de origen.

## Definición de aprobado

Un contenido se considera aprobado cuando el usuario confirma explícitamente que ese contenido representa la versión vigente del contexto, AS-IS, TO-BE, capacidad, feature, historia, decisión o riesgo.

## Definición de memoria activa

La memoria activa está compuesta únicamente por registros vigentes en `Approved_Context`, junto con tablas activas de ejecución como `OKRs`, `Milestones`, `Decisions`, `Risks`, `Features` y `User_Stories`.
