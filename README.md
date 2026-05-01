# PM Operating System para Antigravity + Airtable

Este workspace deja listo un sistema base para trabajar con:

- transcripciones crudas como evidencia inmutable
- iteración conversacional en borradores
- contexto aprobado como memoria oficial
- seguimiento contra decisiones, fechas y OKRs

## Estructura

```text
.agents/
  agents.md
  workflows/
  skills/
schema/
canon/
logs/
.env.example
requirements.txt
```

## Requisitos

- Antigravity instalado
- Python 3.11+
- una base independiente en Airtable
- un Personal Access Token con acceso a esa base

## Variables de entorno

Copia `.env.example` a `.env` y completa:

- `AIRTABLE_TOKEN`
- `AIRTABLE_BASE_ID`
- `AIRTABLE_API_URL` (normalmente no necesitas cambiarlo)
- `BOOTSTRAP_REPORT_PATH` (opcional)

## Scopes mínimos recomendados del token

- `schema.bases:read`
- `schema.bases:write`
- `data.records:read`
- `data.records:write`

Además, la cuenta dueña del token debe tener permisos de Creator o superiores sobre la base.

## Primer arranque

Desde la raíz del workspace:

```bash
python -m venv .venv
source .venv/bin/activate  # en Windows usa .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# edita .env
python .agents/skills/pm-bootstrap/scripts/airtable_bootstrap.py
```

El script:

- lee `schema/airtable_base.yaml`
- consulta el esquema actual de la base
- crea tablas faltantes
- crea campos faltantes
- no borra nada
- deja un reporte en `logs/bootstrap_report.md`

## Uso dentro de Antigravity

Abre el workspace en Antigravity y luego puedes usar:

- `/bootstrap-pm-os`
- `/ingest-transcript`
- `/promote-to-canon`
- `/weekly-control-tower`

## Flujo recomendado

1. Subes o pegas una transcripción.
2. El agente la clasifica y crea borradores en la capa temporal.
3. Iteras con el agente hasta cerrar AS-IS, TO-BE o decisiones.
4. Solo cuando apruebas, el sistema promueve esa versión a memoria oficial.
5. Los seguimientos posteriores comparan contra lo aprobado, no contra borradores viejos.

## Siguiente paso práctico

Después del bootstrap, prueba primero con una sola transcripción real y valida el comportamiento antes de ampliar automatizaciones o agregar más tablas.
