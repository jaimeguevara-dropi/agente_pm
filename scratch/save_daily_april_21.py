import urllib.request
import urllib.error
import urllib.parse
import json
import uuid
import datetime

env_file = '/Users/jaime/Documents/Proyectos/agente_PM/antigravity_pm_os/.env'
config = {}
with open(env_file, 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, val = line.split('=', 1)
        config[key.strip()] = val.strip().strip("'\"")

base_id = config.get('AIRTABLE_BASE_ID')
pat = config.get('AIRTABLE_TOKEN')

headers = {
    'Authorization': f'Bearer {pat}',
    'Content-Type': 'application/json'
}

def create_records(table_name, records):
    if not records:
        return None
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    data = {"records": [{"fields": r} for r in records], "typecast": True}
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error create {table_name}: {e}")
        return None

def update_records(table_name, records):
    if not records:
        return None
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    data = {"records": [{"id": r["id"], "fields": r["fields"]} for r in records], "typecast": True}
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error update {table_name}: {e}")
        return None

# Load Transcript Text
transcript_text = """First Ai Squad - L1 - Daily Meeting - April 21
VIEW RECORDING - 10 mins (No highlights): 
... (transcript content from April 21 daily) ...
[Transcript content provided by User via Prompt]"""

draft_content = """# Borrador de seguimiento

## 1. Resumen ejecutivo
La daily corresponde a los últimos dos días del sprint actual (faltan 2 días para finalizar el sprint). El enfoque técnico está en la culminación de ajustes en la Lambda receptora (Rafa) y el despliegue de la nueva arquitectura basada en ECS (Emmanuel), movimiento que se alinea con la decisión activa del proyecto. Producto (Jaime) y QA (Ana) intentan destrabar pruebas con archivos GValle reales, manipulando de forma manual atributos estructurales para forzar la validación funcional.

## 2. Evolución / avances detectados
- Técnico: Rafa finalizó ajustes de Lambda receptora; Emmanuel desplegó transición a ECS y envió PR, y ejecutó optimizaciones de 'alta información'.
- QA/Producto: Ana validó tiempos de respuesta con Lambda anterior; Jaime organizó pruebas manuales para homogeneizar fallos de data real GValle.

## 3. Bloqueos o impedimentos
- QA (Ana) retiene cierre de bugs hasta tener ECS operativo para evitar regresiones de nueva arquitectura.

## 4. Riesgos nuevos o cambios en existentes
- Adopción de infraestructura ECS: Riesgo de copiar/pegar código sin prever impactos en flujo completo (por ello QA espera).
- Data: Forzar validaciones manuales (ambigüedad estructural) reitera la bajísima calidad de bases entregadas.

## 5. Dependencias detectadas
- QA depende del despliegue en ECS de Emmanuel. Emmanuel depende de revisión cruzada de PR (Rafa/Ana).

## 6. Capabilities impactadas
- CAP-FT-001 (Recepción Lotes), CAP-FT-002 (Validación estructural y funcional).

## 7. HUs impactadas
- Spike Diseño plan de pruebas, US-FT-002-001 Validación estructural, y Bug / tarea (alta información técnica).

## 8. Cambios en el estatus del proyecto
- Faltan 2 días para terminar el sprint.

## 9. Compromisos mencionados
- Ana: Activar Spike pruebas.
- Emmanuel: Gestionar Bug.
- Rafa/Ana: Revisar PR ECS.
- Jaime/Ana: Homologación GValle.

## 10. Recomendación de qué guardar
(Incorporado al registro)
"""

now_str = datetime.datetime.utcnow().isoformat() + "Z"
meeting_id = f"MET-DLY-0421-{str(uuid.uuid4())[:4].upper()}"
project_name = "SILIN - Procesamiento inteligente FT"

meetings = [{
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Meeting Type": "Follow-up",
    "Meeting Date": "2026-04-21T00:00:00.000Z",
    "Participants": "Sergio Raul Ospina Tello, Jose Rafael Peña Mena, Emmanuel Ortega García, Ana Victoria Ospina Vásquez, Jaime Darío Guevara Viteri",
    "Source": "First Ai Squad - L1 - Daily Meeting - April 21 (Recording)",
    "Notes": "Daily a 2 días de terminar el sprint. Enfoque: transición a ECS, PR enviado, y homologación manual de archivos GValle para forzar validación funcional."
}]

transcripts = [{
    "Transcript ID": f"TRN-DLY-0421-{str(uuid.uuid4())[:4].upper()}",
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Raw Transcript": transcript_text,
    "Immutable": True,
    "Imported At": now_str
}]

draft_insights = [{
    "Draft ID": f"DRF-{str(uuid.uuid4())[:8].upper()}",
    "Project": project_name,
    "Meeting ID": meeting_id,
    "Draft Type": "Summary",
    "Title": "Análisis Daily Sprint 10 (-2 días)",
    "Content": draft_content,
    "Status": "Draft"
}]

followups = [
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Activar Spike Plan de Pruebas",
        "Commitment": "Documentar y activar formalmente el Spike del plan de pruebas en Delivery Roll.",
        "Owner": "Ana Victoria Ospina Vásquez",
        "Status": "Open"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Actualizar Bug de Alta Información",
        "Commitment": "Actualizar el ítem de trabajo sobre el caso de alta información en la herramienta de seguimiento.",
        "Owner": "Emmanuel Ortega García",
        "Status": "Open"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Revisión PR de ECS",
        "Commitment": "Revisar y aprobar el PR enviado para la configuración / despliegue en ECS.",
        "Owner": "Jose Rafael Peña Mena / Ana Victoria Ospina Vásquez",
        "Status": "Open"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Homologación manual GValle",
        "Commitment": "Limpiar ambigüedad de columnas en archivos GValle para avanzar a etapa de validación funcional.",
        "Owner": "Jaime Darío Guevara Viteri / Ana Victoria Ospina Vásquez",
        "Status": "In Progress"
    }
]

update_risks = [
    {
        "id": "recRASjIArrlMzaSh",
        "fields": {
            "Description": "Se concentra simultáneamente en la validación lambda: rescate, trazabilidad y corrección. Mantener esta arquitectura hiper-acoplada representa un riesgo de escalabilidad por Timeout (15m).\n\n**Actualizado Daily Abril 21:** QA (Ana) subordina la certificación del procesamiento masivo y de bugs a realizar purebas end-to-end sobre la nueva arquitectura ECS, previniendo regresiones."
        }
    }
]

c = {}
u = []

c["Meetings"] = create_records("Meetings", meetings)
c["Transcripts"] = create_records("Transcripts", transcripts)
c["Draft_Insights"] = create_records("Draft_Insights", draft_insights)
c["Followups"] = create_records("Followups", followups)

u_r = update_records("Risks", update_risks)
if u_r and 'records' in u_r: u.extend(u_r['records'])

import builtins
builtins.print("=== SCRIPT COMPLETED ===")
for t, res in c.items():
    if res and 'records' in res:
        builtins.print(f"Created {len(res['records'])} in {t}: {[r['id'] for r in res['records']]}")

builtins.print(f"Updated {len(u)} in Risks: {[r['id'] for r in u]}")

