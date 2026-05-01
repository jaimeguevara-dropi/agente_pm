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
        "Project": "SILIN - Diagnóstico de liquidación y potencial de recaudo",
        "Context Type": "Business Context",
        "Summary": "Módulo de diagnóstico para liquidación y potencial de recaudo. Busca demostrar valor económico a la alcaldía validando archivos FT en tiempo real y gestionando el reproceso de forma parcial, sin alterar la lógica central de causación de SILIN.",
        "File Path": "canon/business_context_silin_diagnostico_recaudo.md",
        "Status": "Active"
    },
    {
        "Project": "SILIN - Diagnóstico de liquidación y potencial de recaudo",
        "Context Type": "ASIS",
        "Summary": "Proceso actual altamente manual y fragmentado en 4 fases. Incluye revisión visual en Excel por Tributaria, transformaciones manuales en Analítica para alinear columnas, y dispersión bloqueante en Base de Datos (triggers/vistas) que requiere operaciones asíncronas y reprocesos nocturnos.",
        "File Path": "canon/asis_silin_diagnostico_recaudo.md",
        "Status": "Active"
    },
    {
        "Project": "SILIN - Diagnóstico de liquidación y potencial de recaudo",
        "Context Type": "TOBE",
        "Summary": "Flujo automatizado que valida archivos FT al momento del cargue, permite la gestión de novedades parcial para registros erróneos, unifica el cálculo de impuestos y muestra el potencial de recaudo en un tablero visual en minutos.",
        "File Path": "canon/tobe_silin_diagnostico_recaudo.md",
        "Status": "Active"
    }
]

res = create_records("Approved_Context", records)
if res:
    import builtins
    builtins.print(f"Created Approved Context Records: {[r['id'] for r in res['records']]}")
