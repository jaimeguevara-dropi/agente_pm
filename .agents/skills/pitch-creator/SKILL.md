---
name: pitch-creator
description: Use this skill when the user asks to create a pitch for a Dropi epic or initiative. Triggered by "crea un pitch para", "prepara el pitch de".
---

# Pitch Creator

## Objetivo

Generar un pitch ejecutivo para una épica o iniciativa de Dropi, orientado a convencer stakeholders o alinear al equipo.

## Cuándo usarlo

- "crea un pitch para [épica / iniciativa]"
- "prepara el pitch de [nombre]"
- Cuando se necesita presentar una iniciativa de forma persuasiva y concisa

## Instrucciones

1. Lee `canon/dropi_methodology.md` y el contexto de la épica si existe en `approved_context`.
2. Si falta contexto, pregunta al usuario por:
   - Nombre de la iniciativa
   - El problema central que resuelve
   - La audiencia del pitch (equipo de producto, liderazgo, toda la empresa)
3. Genera el pitch con esta estructura:

   **1. El problema (1-2 oraciones)**
   - Describe el dolor actual de forma concreta y memorable.

   **2. A quién afecta**
   - Tipo de usuario, magnitud del impacto (datos si existen, estimación si no).

   **3. La solución propuesta**
   - Qué vamos a hacer y cómo resuelve el problema.

   **4. Por qué ahora**
   - La razón estratégica o urgencia que justifica priorizar esto hoy.

   **5. Lo que vamos a lograr**
   - Métricas o resultados esperados (con placeholders si no hay datos duros).

   **6. Lo que necesitamos**
   - Recursos, equipo, tiempo aproximado.

   **7. Próximo paso**
   - Una sola acción clara que se pide al auditorio.

4. Tono: directo, orientado a impacto, sin jerga técnica innecesaria.
5. Longitud máxima: lo que cabe en 5 minutos de presentación.
6. Presenta como borrador para ajustes del usuario.

## Restricciones

- No inventar datos o métricas sin base; usar "[dato por confirmar]".
- Evitar lenguaje vago ("mejorar la experiencia"). Siempre anclar a impacto concreto.

## Salida esperada

Un pitch ejecutivo conciso, con estructura clara, listo para presentar o adaptar a slides.
