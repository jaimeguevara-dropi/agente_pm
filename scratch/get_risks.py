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
        if not line or line.startswith('#'): continue
        key, val = line.split('=', 1)
        config[key.strip()] = val.strip().strip("'\"")

base_id = config.get('AIRTABLE_BASE_ID')
pat = config.get('AIRTABLE_TOKEN')

headers = {'Authorization': f'Bearer {pat}'}

url = f"https://api.airtable.com/v0/{base_id}/Risks?filterByFormula=" + urllib.parse.quote("{Project}='SILIN - Procesamiento inteligente FT'")
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        records = json.loads(response.read().decode('utf-8'))['records']
        for r in records:
            print(f"ID: {r['id']} | Title: {r['fields'].get('Title')}")
except Exception as e:
    print(f"Error: {e}")
