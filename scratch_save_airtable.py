import os
import urllib.request
import urllib.error
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

import urllib.parse

followups = [{
    "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Title": "Seguimiento histórico consolidado: Reviews 1 al 7",
    "Commitment": "Análisis consolidado de los reviews 1 al 7. El proyecto avanzó en validación estructural y prevención de reprocesos, pero mantiene brecha frente a TO-BE en validación por registro y disponibilización.\n\nSource References: Reviews 1 al 7",
    "Status": "Open"
}]

risks = [
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Dependencia crítica de recursos individuales",
        "Description": "La ausencia de miembros clave frena HUs críticas completas.\n\nSource References: Reviews 1 al 7",
        "Status": "Active" 
    },
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Reglas funcionales estructurales no consolidadas",
        "Description": "Sin catálogo definitivo, hay riesgo de inconsistencias.\n\nSource References: Reviews 1 al 7",
        "Status": "Active"
    },
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Falta de integración operativa End-to-End",
        "Description": "No hay cadena operable demostrable o funcional en producción.\n\nSource References: Reviews 1 al 7",
        "Status": "Active"
    },
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Cuello de botella en DevOps e Infraestructura",
        "Description": "Retrasos por configuración AWS, CI/CD, etc.\n\nSource References: Reviews 1 al 7",
        "Status": "Active"
    },
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Alta tasa de registros inválidos",
        "Description": "Casi 90% invalidados, presión sobre rescate.\n\nSource References: Reviews 1 al 7",
        "Status": "Active"
    }
]

decisions = [
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Catálogo definitivo de reglas funcionales",
        "Decision": "¿Reglas finales y parametrización de obligatoriedad?",
        "Rationale": "\n\nSource References: Reviews 1 al 7",
        "Status": "Pending" 
    },
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Arquitectura final de persistencia",
        "Decision": "¿S3 vs Base de datos?",
        "Rationale": "\n\nSource References: Reviews 1 al 7",
        "Status": "Pending"
    },
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Mecanismo de notificación",
        "Decision": "¿Email, API o Portal para rechazos?",
        "Rationale": "\n\nSource References: Reviews 1 al 7",
        "Status": "Pending"
    },
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Gestión de duplicidades",
        "Decision": "¿Comportamiento ante cargue repetido?",
        "Rationale": "\n\nSource References: Reviews 1 al 7",
        "Status": "Pending"
    },
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Estrategia cargue mega masivo (250MB)",
        "Decision": "¿Pipeline para Enel u otros enormes?",
        "Rationale": "\n\nSource References: Reviews 1 al 7",
        "Status": "Pending"
    }
]

milestones = [
    {
        "Milestone ID": f"MIL-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Name": "Arranque e Infraestructura",
        "Description": "Config inicial. \n\nSource References: Reviews 1 al 7",
        "Status": "Done",
        "Target Date": "2026-02-18T00:00:00Z"
    },
    {
        "Milestone ID": f"MIL-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Name": "Validación Estructural",
        "Description": "Libera nivel estructura.\n\nSource References: Reviews 1 al 7",
        "Status": "Done",
        "Target Date": "2026-02-26T00:00:00Z"
    },
    {
        "Milestone ID": f"MIL-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Name": "Parcial Masivo y Cabecera",
        "Description": "Resiliencia de ID, mayor 6MB.\n\nSource References: Reviews 1 al 7",
        "Status": "Done",
        "Target Date": "2026-03-13T00:00:00Z"
    }
]

drafts = [
    {
        "Draft ID": f"DRF-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Draft Type": "Summary",
        "Title": "Desviación vs TO-BE",
        "Content": "Validación registro a registro y enrutamiento continúan pendientes. Integrar prueba E2E.\n\nSource References: Reviews 1 al 7",
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

process_table("Followups", followups)
process_table("Risks", risks)
process_table("Decisions", decisions)
process_table("Milestones", milestones)
process_table("Draft_Insights", drafts)

print("COUNTS:")
print(created_counts)
print("IDS:")
for aid in all_ids:
    print(aid)
