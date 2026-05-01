import os
import urllib.request
import urllib.parse
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

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
        print(f"Title: {r['fields'].get('Title')} | Status: {r['fields'].get('Status')} | Desc: {str(r['fields'].get('Description'))[:50]}")

decisions = get_records('Decisions')
print("\n--- DECISIONS ---")
for d in decisions:
    if d['fields'].get('Status') != 'Superseded' and d['fields'].get('Status') != 'Rejected':
        print(f"Title: {d['fields'].get('Title')} | Status: {d['fields'].get('Status')} | Dec: {str(d['fields'].get('Decision'))[:50]}")

followups = get_records('Followups')
print("\n--- FOLLOWUPS ---")
for f in followups:
    print(f"Title: {f['fields'].get('Title')} | Date: {f['fields'].get('Date')} | Advances: {str(f['fields'].get('Advances'))[:50]}")

milestones = get_records('Milestones')
print("\n--- MILESTONES ---")
for m in milestones:
    print(f"Title: {m['fields'].get('Title')} | Date: {m['fields'].get('TargetDate')} | Status: {m['fields'].get('Status')}")

