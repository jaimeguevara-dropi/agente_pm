import urllib.request
import urllib.parse
import json

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
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    data = {"records": [{"fields": r} for r in records], "typecast": True}
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error create {table_name}: {e}")
        return None

records = [
    {
        "Story ID": "US-FT-002-007",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Feature": "CAP-FT-002 - Validación estructural y funcional de archivo",
        "Title": "Diseño y ejecución de pruebas de carga y estrés End-to-End (JMeter)",
        "Narrative": "Como responsable de QA y Arquitectura, quiero diseñar y ejecutar un escenario de pruebas de carga masiva de punta a punta simulando múltiples lotes FT, para medir la capacidad del sistema, identificar cuellos de botella en la nueva infraestructura asíncrona (Lambda Cleanup + ECS/SS) y validar que los tiempos de procesamiento cumplen con las necesidades operativas de la cadena tributaria.",
        "Acceptance Criteria": "1. Definición del escenario de estrés documentado.\n2. Script de JMeter configurado inyectando archivos al sistema.\n3. Ejecución de pruebas en ambiente estabilizado (Staging/QA) tras integración de componentes.\n4. Informe de métricas (tiempos de respuesta, recursos, timeouts y recomendaciones).",
        "Status": "Approved"
    }
]

res = create_records("User_Stories", records)
if res:
    import builtins
    builtins.print(f"Created User Story: {[r['id'] for r in res['records']]}")
