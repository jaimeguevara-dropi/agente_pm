import os
import urllib.request
import urllib.error
import urllib.parse
import json
import uuid
import datetime

# Parse dotenv manually
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
    data = {
        "records": [{"fields": r} for r in records],
        "typecast": True
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error in {table_name}: {e.code} - {e.read().decode('utf-8')}")
        return None

# Read external text files
transcript_path = '/Users/jaime/Documents/Proyectos/agente_PM/antigravity_pm_os/scratch/transcript.txt'
with open(transcript_path, 'r', encoding='utf-8') as tf:
    raw_transcript = tf.read()

draft_path = '/Users/jaime/Documents/Proyectos/agente_PM/antigravity_pm_os/scratch/draft.txt'
with open(draft_path, 'r', encoding='utf-8') as df:
    draft_content = df.read()

project_name = "SILIN - Procesamiento inteligente FT"
source_refs = "Planning sprint 10"
meeting_id = f"MTG-PLAN-20260416-{str(uuid.uuid4())[:8].upper()}"

meetings = [{
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Meeting Type": "Planning",
    "Meeting Date": "2026-04-16T16:00:00Z",
    "Participants": "Sergio Raul Ospina Tello, Ana Victoria Ospina Vásquez, Jaime Darío Guevara Viteri, Fredi Yonatan Flórez Garzón, Jose Rafael Peña Mena, Emmanuel Ortega García, Juan David Lopez.",
    "Source": "https://fathom.video/share/qX3nEJoSyDPtt3P4vs2ptQx2yr-rJDAm",
    "Notes": "Planning Sprint 10. Aprobación y asignaciones para el refactor arquitectónico (Migración a ECS/SS Fargate), la estandarización de jerarquías en S3 y diseño del Spike del plan de pruebas sobre datos reales."
}]

transcripts = [{
    "Transcript ID": f"TRN-20260416-{str(uuid.uuid4())[:8].upper()}",
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Raw Transcript": raw_transcript,
    "Source URL": "https://fathom.video/share/qX3nEJoSyDPtt3P4vs2ptQx2yr-rJDAm",
    "Immutable": True,
    "Imported At": datetime.datetime.now(datetime.timezone.utc).isoformat()
}]

followups = [
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Team": "First Ai Squad - L1",
        "Title": "Estudiar y migrar lógica del procesamiento al componente SS",
        "Commitment": f"Mapear y migrar la lógica intensiva al SS asíncrono, con pruebas locales asegurando estabilidad de estados y entrega interna el martes.\n\nSource References: {source_refs}",
        "Owner": "Emmanuel Ortega García",
        "Due Date": "2026-04-21T00:00:00Z",
        "Status": "Open"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Team": "First Ai Squad - L1",
        "Title": "Implementar estándar de carpetas S3 y modificar trazabilidad",
        "Commitment": f"Enganchar Cleanup de forma asíncrona hacia el servicio SS, estructurar llaves en el bucket de S3 (Entidad/TaxID/CompanyID/Periodo/Tipo) y asegurar volcado de eventos de trazabilidad base.\n\nSource References: {source_refs}",
        "Owner": "Jose Rafael Peña Mena",
        "Due Date": "2026-04-21T00:00:00Z",
        "Status": "Open"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Team": "First Ai Squad - L1",
        "Title": "Spike: Diseño de plan de pruebas con Data Real",
        "Commitment": f"Crear y formalizar escenarios de prueba funcionales y regresión preparándose para recibir los refactores a mitad de semana.\n\nSource References: {source_refs}",
        "Owner": "Ana Victoria Ospina Vásquez",
        "Due Date": "2026-04-23T00:00:00Z",
        "Status": "Open"
    }
]

risks = [
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Curva de aprendizaje del componente SS frena tiempos",
        "Description": "Utilizar la nueva arquitectura requiere conocimiento previo o investigación durante el mismo sprint por parte de Desarrollo, comprimiendo el tiempo de construcción frente a la meta (martes).",
        "Impact": "High",
        "Probability": "Medium",
        "Mitigation": f"Acompañamiento y soporte por Fredi para proveer atajos de configuración e invocar directamente.\n\nSource References: {source_refs}",
        "Status": "Watching"
    },
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Tensión temporal en fase de aseguramiento de QA",
        "Description": "El volumen de cambios estructurales requiere una regresión 100% integral al flujo de las llaves, base de datos y procesamiento en dos días o menos.",
        "Impact": "High",
        "Probability": "High",
        "Mitigation": f"Iniciar en paralelo el Spike para trazar las pruebas desde antes y dejar todo listo a la espera del build a Staging.\n\nSource References: {source_refs}",
        "Status": "Watching"
    }
]

decisions = [
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Adopción de infraestructura orientada a lógica (ECS/SS)",
        "Decision": "Las revalidaciones intensas desechan AWS Glue a cambio de tareas ECS Fargate (conocido como SS).",
        "Rationale": f"AWS Glue es principalmente para proceso batcheado/moler datos. El proceso FT exige lógica de negocio profunda.\n\nSource References: {source_refs}",
        "Decision Date": "2026-04-16T16:00:00Z",
        "Status": "Active"
    },
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Estándar organizativo inmutable de directorios S3",
        "Decision": "Usar la agrupación: Entidad -> Tax ID -> Company ID -> Periodo -> Tipo de documento.",
        "Rationale": f"Lograr la independencia transaccional. Mantener Company ID como un formato agnóstico global para dar pie a archivos comerciales futuros.\n\nSource References: {source_refs}",
        "Decision Date": "2026-04-16T16:00:00Z",
        "Status": "Active"
    },
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Formato Dual para Salidas Trusted",
        "Decision": "Los flujos finales de salida de registros válidos exportarán en archivo plano original y .parquet.",
        "Rationale": f"Requisito nativo de dispersión y consolidación de SILIN expuesto durante revisión arquitectónica.\n\nSource References: {source_refs}",
        "Decision Date": "2026-04-16T16:00:00Z",
        "Status": "Active"
    }
]

milestones = [
    {
        "Milestone ID": f"MIL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Name": "Entregable Dev: Arquitectura Asíncrona (Sprint 10)",
        "Description": f"Liberación al ciclo de pruebas formales por parte de calidad tras la integración Rafa/Emmanuel.\n\nSource References: {source_refs}",
        "Target Date": "2026-04-21T00:00:00Z",
        "Status": "Upcoming"
    }
]

drafts = [
    {
        "Draft ID": f"DRF-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Meeting ID": meeting_id,
        "Draft Type": "Summary",
        "Title": "Seguimiento operativo - Sprint 10 Planning",
        "Content": f"{draft_content}\n\nSource References: {source_refs}",
        "Status": "Draft"
    }
]

created_counts = {}
all_ids = []

def process_table(name, records):
    res = create_records(name, records)
    if res and 'records' in res:
        created_counts[name] = len(res['records'])
        all_ids.extend([f"{name}: {r['id']}" for r in res['records']])
    else:
        created_counts[name] = 0

process_table("Meetings", meetings)
process_table("Transcripts", transcripts)
process_table("Followups", followups)
process_table("Risks", risks)
process_table("Decisions", decisions)
process_table("Milestones", milestones)
process_table("Draft_Insights", drafts)

print("COUNTS:")
print(json.dumps(created_counts, indent=2))
print("IDS:")
for aid in all_ids:
    print(aid)
