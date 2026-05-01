import os
import urllib.request
import urllib.parse
import json
import ssl
import datetime

ssl._create_default_https_context = ssl._create_unverified_context

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
headers = {'Authorization': f'Bearer {pat}', 'Content-Type': 'application/json'}
project_name = "SILIN - Procesamiento inteligente FT"

def get_records(table_name):
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}?filterByFormula=" + urllib.parse.quote(f"{{Project}}='{project_name}'")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))['records']
    except Exception as e:
        print(f"Error fetching {table_name}: {e}")
        return []

def update_record(table_name, rec_id, fields):
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}/{rec_id}"
    data = json.dumps({"fields": fields}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"Updated {rec_id} in {table_name}")
    except Exception as e:
        print(f"Error updating {rec_id} in {table_name}: {e}")

def create_record(table_name, fields):
    fields["Project"] = project_name
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    data = json.dumps({"fields": fields}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as resp:
            rec = json.loads(resp.read().decode('utf-8'))
            print(f"Created {rec['id']} in {table_name}")
    except Exception as e:
        print(f"Error creating in {table_name}: {e}")

print("Updating Risks...")
risks = get_records('Risks')
for r in risks:
    t = r['fields'].get('Title', '')
    if 'Alta tasa de registros inválidos' in t:
        old_mit = r['fields'].get('Mitigation', '')
        update_record('Risks', r['id'], {
            "Status": "Closed",
            "Mitigation": old_mit + "\n\nCERRADO: Completada y desplegada la capacidad de Revalidación Automática, notificaciones de rechazo y rescate de registros parciales."
        })
    elif 'Cuello de botella en DevOps' in t or 'Dependencia crítica de' in t:
        old_mit = r['fields'].get('Mitigation', '')
        update_record('Risks', r['id'], {
            "Mitigation": old_mit + "\n\nACTUALIZACIÓN SPRINT: El esfuerzo de transición de Lambda a ECS está controlado (esfuerzo de 1 semana). El riesgo radica netamente en la disponibilidad de foco (100%) del recurso de infraestructura para destrabar CI/CD, pero la complejidad técnica está dominada."
        })

print("Creating Decision...")
create_record('Decisions', {
    "Title": "Prueba Live-Data Integrado (QA, Producto, TI)",
    "Decision": "Se descarta generar un catálogo estático teórico definitivo de reglas antes de probar. En su lugar, se ejecutarán pruebas de live-data ingresando archivos diarios reales (FTs) para que el componente identifique inconsistencias vivas y afinar las respuestas automáticas.",
    "Status": "Active"
})

print("Creating Followup...")
today_str = datetime.datetime.now().strftime("%Y-%m-%d")
create_record('Followups', {
    "Title": "Estatus Ejecutivo Corte Abril",
    "Commitment": "Avances: Implementación exitosa de Revalidación y Rescate. Pivot a ECS de solo 1 semana definido.\nBloqueos: DevOps (ancho de banda) para materializar la arquitectura ECS.\nDecisiones: Pruebas con Live Data inter-equipos.",
    "Status": "Done"
})
print("Done.")
