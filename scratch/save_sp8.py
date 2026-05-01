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
meeting_id = "MET-SPRINT8"

meetings = [{
    "Meeting ID": meeting_id,
    "Project": "SILIN - Procesamiento inteligente FT",
    "Team": "First Ai Squad - L1",
    "Meeting Type": "Follow-up",
    "Meeting Date": "2026-04-09T00:00:00.000Z",
    "Participants": "Sergio R. Ospina, Marisleidy Mora, Jaime Darío Guevara, Ana Victoria Ospina, Jose Rafael Peña, Emmanuel Ortega",
    "Source": "Jikkofirst Ai - L1 - Review - SP8.pdf y Transcripción de grabación de 43 mins",
    "Notes": "Review del Sprint 8. 27 Story points, 6 HUs cerradas. Se logró certificación estructural de archivos hasta 1.5 GB, conexión RDS y Polars. Bloqueadas HUs de rescate por descubrimiento de escenarios de negocio SILIN no contemplados."
}]

transcripts = [{
    "Transcript ID": "TRN-SPRINT8",
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
    "Title": "Brecha entre Tolerancia de Pipeline y Realidad Documental TO-BE",
    "Content": "Insight analítico: El Flujo E2E demostró tolerancia gigante (hasta 1.5 GB inyectados), pero funcionalmente hay fricción. El escenario de 'Múltiples contribuyentes por 1 ID' de SILIN inutilizó las reglas de recuperación impidiendo el procesamiento parcial inteligente pretendido.",
    "Status": "Draft"
}]

followups = [{
    "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Team": "First Ai Squad - L1",
    "Title": "Seguimiento histórico: Review Sprint 8",
    "Commitment": "El Sprint 8 evidenció importantes victorias técnicas en performance y trazabilidad, logrando procesar archivos de 1.5 GB y habilitando conexión RDS. Sin embargo, el esfuerzo funcional central E2E fue bloqueado funcionalmente por atributos SILIN (1 medidor multple contribuyente). 19 pendientes, retraso de 1 mes.",
    "Owner": "PMO",
    "Status": "Open"
}]

new_risks = [{
    "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Title": "Incumplimiento de Deadline Funcional 16 de Abril",
    "Description": "El pipeline técnico avanzó, pero el sprint quedó con 19 pendientes frente a 17 HUs. Se advierte 1 mes adicional estimado para estabilizar E2E.",
    "Status": "Open"
}]
update_risks = [
    {
        "id": "rec8eAeFKSJbflWIe",
        "fields": {
            "Description": "Actualizado Sprint 8: Hay continuidad entre lambdas y performance cruzado, pero el proceso lógico de negocio extremo a extremo sigue cayéndose por falta de resolución en las reglas funcionales de rescate."
        }
    },
    {
        "id": "recU8EiS0yQjaVmkk",
        "fields": {
            "Description": "Actualizado Sprint 8: Además de DevOps atascado, la nueva entrada (Ana) como QA se encuentra restringida al 50% impactando testing.\nLa ausencia de miembros clave frena HUs críticas completas."
        }
    },
    {
        "id": "recpI8xD7la9kz1Ex",
        "fields": {
            "Description": "Actualizado Sprint 8: Se reveló desconocimiento en deuda técnica y escenarios silentes de negocio (múltiples responsables para 1 servicio).\nSin catálogo definitivo, hay riesgo de inconsistencias."
        }
    }
]

new_decisions = [{
    "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Title": "Regla de Asignación Dúplice para Llaves",
    "Decision": "¿Bajo qué directriz se resuelve el rescate lógico cuando 1 medidor corresponde a múltiples contribuyentes en SILIN?",
    "Status": "Pending"
}]
update_decisions = [
    {
        "id": "recQLMx6Bnr9mlZa3",
        "fields": {
            "Status": "Superseded",
            "Rationale": "La duda de pesaje quedó despejada; QA certificó carga de 1.5GB sin problemas concurrentes (Sprint 8)."
        }
    }
]

new_milestones = [{
    "Milestone ID": f"MIL-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Name": "Estabilidad Estructural Mega Masiva y Cruce",
    "Description": "QA certificó E2E tolerancia extrema verificando cruce vía Polars/RDS sin que el sistema falle ante 1.5GB.",
    "Target Date": "2026-04-09T00:00:00.000Z",
    "Status": "Done"
}]

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

print("=== CREATED ===")
for t, res in c.items():
    if res and 'records' in res:
        for r in res['records']:
            print(f"{t}: {r['id']}")
print("=== UPDATED ===")
for r in u:
    print(f"Updated: {r['id']}")
