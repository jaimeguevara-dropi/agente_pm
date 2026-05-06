---
name: kickoff-creator
description: Use this skill when the user asks to create a kickoff document for a Dropi epic or project. Triggered by "crea un documento de kickoff para", "prepara el kickoff de".
---

# Kickoff Creator

## Objetivo

Generar el documento de kickoff de una épica o proyecto en Dropi, listo para presentar al equipo.

## Cuándo usarlo

- "crea un documento de kickoff para [épica / proyecto]"
- "prepara el kickoff de [iniciativa]"
- Cuando el usuario necesita estructurar la sesión de arranque de una iniciativa

## Instrucciones

1. Lee `canon/dropi_methodology.md` y el contexto de la épica si existe en `approved_context`.
2. Si falta contexto, pregunta al usuario por:
   - Nombre e identificador de la épica
   - Problema que resuelve y usuarios afectados
   - Equipo involucrado (UX, UI, Frontend, Backend, DBA, QA, etc.)
   - Fecha tentativa de kickoff
3. Genera el documento con las siguientes secciones:

   **1. Contexto y problema**
   - Qué problema resolvemos y por qué es importante ahora.

   **2. Objetivo de la épica**
   - Qué buscamos lograr (en términos de negocio y de usuario).

   **3. Usuarios afectados**
   - Tipos de usuario, países, marcas blancas.

   **4. Fases del proceso**
   - Tabla con fase, entregable esperado, posibles bloqueantes y responsable.

   **5. Criterios de éxito**
   - Métricas a impactar y cómo se medirá el éxito.

   **6. Alcance y fuera de alcance**
   - Qué está dentro y qué queda fuera de esta épica.

   **7. Equipo y roles**
   - Tabla con rol, persona/equipo responsable y expectativa.

   **8. Preguntas abiertas / bloqueantes**
   - Lista de decisiones pendientes antes de arrancar.

   **9. Documentación**
   - Placeholders para: Figma, FigJam, flujo general, documentos relacionados.

   **10. Próximos pasos**
   - Acciones concretas con responsable y fecha.

4. Presenta como borrador para aprobación.

## Restricciones

- No inventes responsables o fechas; usa placeholders claros.
- Mantener un tono ejecutivo y directo, orientado a acción.

## Salida esperada

Documento de kickoff completo, listo para compartir con el equipo en Notion, Confluence o Google Docs.
