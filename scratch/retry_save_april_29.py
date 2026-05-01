import urllib.request
import urllib.error
import urllib.parse
import json
import uuid
import datetime
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

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
        with urllib.request.urlopen(req, context=ctx) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error create {table_name}: {e}")
        return None

now_str = datetime.datetime.utcnow().isoformat() + "Z"
meeting_id = f"MET-DLY-0429-{str(uuid.uuid4())[:4].upper()}"
project_name = "SILIN - Procesamiento inteligente FT"

meetings = [{
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Meeting Type": "Follow-up",
    "Meeting Date": "2026-04-29T00:00:00.000Z",
    "Participants": "Sergio Raul Ospina Tello, Emmanuel Ortega García, Jose Rafael Peña Mena, Jaime Darío Guevara Viteri, Ana Victoria Ospina Vásquez",
    "Source": "First Ai Squad - L1 - Daily Meeting - April 29",
    "Notes": "Penúltima daily Sprint 10. QA detecta falla de arquitectura en la ingesta ante concurrencia. Emmanuel y Rafa cierran desarrollos de ajustes estructurales, notificaciones y Clean up."
}]

create_risks = [
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Falla de ingesta ante concurrencia masiva",
        "Description": "Al simular concurrencia (5 usuarios enviando 30MB), el sistema descarta archivos en la etapa de Ingesta, procesando solo uno. Es un riesgo arquitectónico crítico que afecta el procesamiento masivo TO-BE.",
        "Impact": "High",
        "Probability": "High",
        "Status": "Open"
    },
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Fallo validación estructural por caracteres adicionales (Terpel)",
        "Description": "Archivos de Terpel tienen un pipe final residual que genera una falsa columna. Bloquea validación estructural.",
        "Impact": "Low",
        "Probability": "High",
        "Status": "Open"
    }
]

c = {}
c["Meetings"] = create_records("Meetings", meetings)
c["Risks"] = create_records("Risks", create_risks)

import builtins
builtins.print("=== SCRIPT COMPLETED ===")
for t, res in c.items():
    if res and 'records' in res:
        builtins.print(f"Created {len(res['records'])} in {t}: {[r['id'] for r in res['records']]}")
