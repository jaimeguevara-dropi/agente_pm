import urllib.request
import urllib.parse
import json
import uuid
import datetime

env_file = '/Users/jaime/Documents/Proyectos/agente_PM/antigravity_pm_os/.env'
config = {}
with open(env_file, 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'): continue
        key, val = line.split('=', 1)
        config[key.strip()] = val.strip().strip("'\"")

base_id = config.get('AIRTABLE_BASE_ID')
pat = config.get('AIRTABLE_TOKEN')

headers = {
    'Authorization': f'Bearer {pat}',
    'Content-Type': 'application/json'
}

def create_records(table_name, records):
    if not records: return None
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    data = {"records": [{"fields": r} for r in records], "typecast": True}
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error create {table_name}: {e}")
        return None

meetings = [{
    "Meeting ID": "MET-DLY-0422-B798",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Team": "First Ai Squad - L1",
    "Meeting Type": "Follow-up",
    "Meeting Date": "2026-04-22T00:00:00.000Z",
    "Participants": "Sergio Raul Ospina Tello, Jose Rafael Peña Mena, Emmanuel Ortega García, Ana Victoria Ospina Vásquez, Jaime Darío Guevara Viteri, Fredi Yonatan Flórez Garzón",
    "Source": "First Ai Squad - L1 - Daily Meeting - April 22 (Recording)",
    "Notes": "Seguimiento diario. Avance exitoso en despliegue de SS en QA. Pruebas con archivos FT reales revelan fallos por inconsistencias en los nombres de las columnas. Fredi solicita pruebas JMeter."
}]

create_risks = [
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Title": "Inconsistencias en formato de archivos FT reales",
        "Description": "Las pruebas con data real muestran que las comercializadoras varían los nombres de columnas (ej. subinicial), impidiendo la validación estructural estricta. Requiere homologación dinámica.",
        "Impact": "High",
        "Probability": "High",
        "Status": "Open"
    }
]

res_m = create_records("Meetings", meetings)
res_r = create_records("Risks", create_risks)

print("=== RETRY COMPLETED ===")
if res_m and 'records' in res_m:
    print(f"Created Meetings: {[r['id'] for r in res_m['records']]}")
if res_r and 'records' in res_r:
    print(f"Created Risks: {[r['id'] for r in res_r['records']]}")

