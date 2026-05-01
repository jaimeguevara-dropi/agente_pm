---
name: pm-bootstrap
description: Use this skill when the user wants to initialize or update the Airtable schema, generate the PM Operating System workspace files, validate required folders, or bootstrap the Antigravity project structure.
---

# PM Bootstrap

## Objetivo

Inicializar o actualizar de forma segura la estructura base del PM Operating System.

## Cuándo usarlo

- cuando el usuario quiera crear la base operativa por primera vez
- cuando falten tablas o campos en Airtable
- cuando falten archivos críticos en `.agents`, `schema` o `canon`
- cuando se quiera validar que el workspace sigue alineado con el esquema oficial

## Instrucciones

1. Revisa `schema/airtable_base.yaml`.
2. Revisa `canon/operating_rules.md`.
3. Verifica que la estructura del workspace exista.
4. Ejecuta el script Python del skill para crear tablas y campos faltantes.
5. Revisa el reporte generado en `logs/bootstrap_report.md`.
6. Resume diferencias entre esquema esperado y esquema actual.
7. No borres tablas, campos ni datos automáticamente.

## Restricciones

- nunca eliminar tablas o campos
- nunca reescribir `Approved_Context` por bootstrap
- si falta `AIRTABLE_TOKEN` o `AIRTABLE_BASE_ID`, detenerse y reportar el problema

## Salida esperada

- tablas creadas
- campos creados
- advertencias
- siguiente acción recomendada
