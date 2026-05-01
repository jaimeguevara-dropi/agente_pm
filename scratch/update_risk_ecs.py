import urllib.request
import urllib.error
import urllib.parse
import json

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

risk_update = {
    "records": [
        {
            "id": "recRASjIArrlMzaSh",
            "fields": {
                "Description": "Se concentra simultáneamente en la validación lambda: rescate, trazabilidad y corrección. Mantener esta arquitectura hiper-acoplada representa un riesgo de escalabilidad por Timeout (15m).\n\n**Actualizado Daily Abril 21:** La migración a ECS está acotada exclusivamente a la `lbda-jikko-integration-trusted-business-model-function` (recuperación y corrección hacia trusted_ready). El resto del ecosistema (AWS Glue, otras Lambdas) se mantiene intacto. El riesgo de QA consiste en certificar la impecable integración de este contenedor ECS sin causar fallos ni regresiones en los componentes invariables."
            }
        }
    ],
    "typecast": True
}

url = f"https://api.airtable.com/v0/{base_id}/Risks"
req = urllib.request.Request(url, data=json.dumps(risk_update).encode('utf-8'), headers=headers, method='PATCH')
try:
    with urllib.request.urlopen(req) as r:
        res = json.loads(r.read().decode('utf-8'))
        print("Updated Risks:", [rec['id'] for rec in res.get('records', [])])
except Exception as e:
    print("Error:", e)
