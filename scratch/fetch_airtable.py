import os
import urllib.request
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
}

def get_records(table_name):
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}?filterByFormula=" + urllib.parse.quote("{Project}='SILIN - Procesamiento inteligente FT'")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))['records']
    except Exception as e:
        print(f"Error {table_name}: {e}")
        return []

risks = get_records('Risks')
print("--- RISKS ---")
for r in risks:
    if r['fields'].get('Status') != 'Closed':
        print(f"ID: {r['id']} | Title: {r['fields'].get('Title')} | Status: {r['fields'].get('Status')} | Desc: {str(r['fields'].get('Description'))[:50]}...")

decisions = get_records('Decisions')
print("\n--- DECISIONS ---")
for d in decisions:
    if d['fields'].get('Status') != 'Superseded' and d['fields'].get('Status') != 'Rejected':
        print(f"ID: {d['id']} | Title: {d['fields'].get('Title')} | Status: {d['fields'].get('Status')} | Dec: {str(d['fields'].get('Decision'))[:50]}...")
