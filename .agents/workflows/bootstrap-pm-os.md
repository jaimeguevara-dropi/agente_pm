---
description: Inicializa o actualiza el PM Operating System en Airtable y en el workspace
---

Cuando el usuario ejecute `/bootstrap-pm-os`:

1. Actúa como **PM Systems Architect**.
2. Revisa `schema/airtable_base.yaml` y `canon/operating_rules.md`.
3. Verifica que existan `.agents/agents.md`, `schema/airtable_base.yaml` y `canon/operating_rules.md`.
4. Usa el skill `pm-bootstrap`.
5. Ejecuta el script `python .agents/skills/pm-bootstrap/scripts/airtable_bootstrap.py`.
6. Revisa `logs/bootstrap_report.md`.
7. Resume:
   - tablas creadas
   - campos creados
   - diferencias detectadas
   - próximos pasos
8. Nunca borres estructura automáticamente.
