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
        "Story ID": "US-FT-002-008",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Feature": "CAP-FT-002 - Validación estructural y funcional de archivo",
        "Title": "Homologación dinámica de nombres de columnas por Comercializadora",
        "Narrative": "Como sistema de procesamiento FT, quiero utilizar un diccionario o mapeo de columnas parametrizado por entidad comercializadora (Ej: según diagnóstico de G-Valle, mapear alias como 'FECHA_INI PERIODO_FACT'), para que los archivos superen la validación estructural estricta sin obligar a la entidad a cambiar la estructura de sus exportaciones habituales.",
        "Acceptance Criteria": "El sistema debe permitir almacenar una configuración de alias de columnas asociada a la entidad comercializadora, documentado en https://docs.google.com/spreadsheets/d/1aYp91e7w6AFsfhdgLVYwIwQURRSyUYcubA2Qdeb-6jY/edit?gid=1258681224#gid=1258681224. Durante la validación estructural, si una columna obligatoria no se encuentra, buscar en los alias. Si hace match, la validación pasa y reescribe el encabezado en memoria para el sistema.",
        "Status": "Approved"
    },
    {
        "Story ID": "US-FT-005-005",
        "Project": "SILIN - Procesamiento inteligente FT",
        "Feature": "CAP-FT-005 - Revalidación incremental de registros inválidos",
        "Title": "Limpieza de codificación, validación de PIPE y rescate de contribuyente anónimo",
        "Narrative": "Como sistema de procesamiento, quiero rechazar archivos con delimitadores incorrectos (solo aceptar PIPE), limpiar caracteres de codificación, y aplicar una regla de rescate por Medidor cuando la identificación sea 2222222222, para garantizar consistencia legal y operativa en rescate.",
        "Acceptance Criteria": "1) El sistema NO debe aceptar delimitadores diferentes a PIPE (sin TABs, sin espacios). 2) Se debe forzar o validar limpieza de codificación (''). 3) Si la cédula/ID viene como 2222222222 (protección legal de identidad), el sistema (fase Rescate) debe validar con el número de Medidor y buscar el último contribuyente asociado a ese medidor en la BD. Si no existe, devolver a corrección exigiendo el envío del registro completo al menos una vez para registrar el medidor.",
        "Status": "Approved"
    }
]

res = create_records("User_Stories", records)
if res:
    import builtins
    builtins.print(f"Created User Stories: {[r['id'] for r in res['records']]}")
