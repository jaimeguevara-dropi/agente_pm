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
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    data = {"records": [{"id": r["id"], "fields": r["fields"]} for r in records], "typecast": True}
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error update {table_name}: {e}")
        return None

with open('/Users/jaime/Documents/Proyectos/agente_PM/antigravity_pm_os/scratch/transcript.txt', 'r', encoding='utf-8') as f:
    transcript_text = f.read()

now_str = datetime.datetime.utcnow().isoformat() + "Z"
meeting_id = "MET-SPRINT9"

meetings = [{
    "Meeting ID": meeting_id,
    "Project": "SILIN - Procesamiento inteligente FT",
    "Team": "First Ai Squad - L1",
    "Meeting Type": "Follow-up",
    "Meeting Date": "2026-04-16T00:00:00.000Z",
    "Participants": "Sergio R. Ospina, Fredi Flórez, Jaime Darío Guevara, Juan David Lopez, Diana Plata, Emmanuel Ortega, Jose Rafael Peña, Ana Victoria Ospina, Nicole Stephany Dosman",
    "Source": "Jikkofirst Ai - L1 - Review - SP9.pdf y Transcripción (62 mins)",
    "Notes": "Review del Sprint 9. Entrega al 33% (13 SP, 2 HUs). Se logró certificar el Rescate E2E y el cruce usando llaves. Bloqueo en Revalidación/Correcciones masivas debido a tiempo límite de 15 min de las Lambdas. Nuevo target al 16 de mayo (1 mes de retraso oficializado)."
}]

transcripts = [{
    "Transcript ID": "TRN-SPRINT9",
    "Meeting ID": meeting_id,
    "Project": "SILIN - Procesamiento inteligente FT",
    "Team": "First Ai Squad - L1",
    "Raw Transcript": transcript_text,
    "Immutable": True,
    "Imported At": now_str
}]

draft_insights = [{
    "Draft ID": f"DRF-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Meeting ID": meeting_id,
    "Draft Type": "Summary",
    "Title": "Confinamiento en Topología Serverless Límite de 15 Minutos",
    "Content": "Para procesar correcciones masivas con lógica cruzada para millones de registros se evidenció un límite duro para la arquitectura Lambda que mata el proceso a los 15 min. La reestructuración inminente a ECS es fundamental.",
    "Status": "Draft"
}]

followups = [{
    "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Team": "First Ai Squad - L1",
    "Title": "Seguimiento Histórico: Review Sprint 9",
    "Commitment": "Sprint 9 finaliza confirmando retraso de 4 semanas al 16 de Mayo. Se entregaron 13 SP enfocados al cierre definitivo de Rescate. La épica de Corrección quedó bloqueada por Timeout Lambda; lideres iniciarán migración a ECS.",
    "Owner": "PMO",
    "Status": "Open"
}]

new_risks = [{
    "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Title": "Sobrecarga Arquitectónica del Componente Trusted",
    "Description": "Se concentra simultáneamente en la validación lambda: rescate, trazabilidad y corrección. Mantener esta arquitectura hiper-acoplada representa un riesgo de escalabilidad por Timeout (15m).",
    "Status": "Active"
}]

new_decisions = [
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Migración de Procesamiento de Lote a ECS (Contenedores)",
        "Decision": "Se retira la lógica iterativa de correcciones gigantes a nivel Lambda Serverless y se migran funciones a componentes de mayor latencia y vida útil (SS/ECS) mitigando el límite de 15 min.",
        "Status": "Pending"
    },
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Aislamiento y Autonomía de Consumo con SILIN",
        "Decision": "Squad actúa únicamente como orquestador y disponibilizador API y en S3. Cero injerencia del Squad en desarrollos dentro del SILIN Antiguo o Lancha 2 para enganchar data.",
        "Status": "Active"
    }
]

new_milestones = [{
    "Milestone ID": f"MIL-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Name": "Cierre Funcional E2E de Epic Rescate (Llegada, Separación y Rescate)",
    "Description": "Capacidad fundamental CAP-FT-006 certificada. Sistema separa automáticamente válidos de inválidos y logra cruce con base maestra para rescatables.",
    "Target Date": "2026-04-16T00:00:00.000Z",
    "Status": "Done"
}]

update_risks = [
    {
        "id": "reckjWTCA5oVbf2kM",
        "fields": {
            "Description": "Actualizado Sprint 9: Oficializado el fallo del roadmap. El día del deadline el avance es 33% y quedan bloqueadas correcciones enteras. Desviación oficialmente empujada al 16 de Mayo."
        }
    },
    {
        "id": "rec8eAeFKSJbflWIe",
        "fields": {
            "Description": "Actualizado Sprint 9: End-to-End Base mitigado. Rescate demostró fluidez en QA, pero el ciclo sufre bloqueos estrictamente en la re-ingesta y cruces de correcciones."
        }
    }
]

update_decisions = [
    {
        "id": "recN7Y6CxyiwivC6t",
        "fields": {
            "Status": "Superseded",
            "Rationale": "QA certificó las HU asociadas a uso de llaves (Sprint 9). Resuelto."
        }
    }
]

c = {}
u = []

c["Meetings"] = create_records("Meetings", meetings)
c["Transcripts"] = create_records("Transcripts", transcripts)
c["Draft_Insights"] = create_records("Draft_Insights", draft_insights)
c["Followups"] = create_records("Followups", followups)
c["Risks"] = create_records("Risks", new_risks)
c["Decisions"] = create_records("Decisions", new_decisions)
c["Milestones"] = create_records("Milestones", new_milestones)

u_r = update_records("Risks", update_risks)
if u_r and 'records' in u_r: u.extend(u_r['records'])
u_d = update_records("Decisions", update_decisions)
if u_d and 'records' in u_d: u.extend(u_d['records'])

import builtins
builtins.print("=== CREATED ===")
for t, res in c.items():
    if res and 'records' in res:
        for r in res['records']:
            builtins.print(f"{t}: {r['id']}")
builtins.print("=== UPDATED ===")
for r in u:
    builtins.print(f"Updated {r['id']}")
