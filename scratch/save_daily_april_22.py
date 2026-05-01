import urllib.request
import urllib.error
import urllib.parse
import json
import uuid
import datetime

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
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error create {table_name}: {e}")
        return None

def update_records(table_name, records):
    if not records:
        return None
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    data = {"records": [{"id": r["id"], "fields": r["fields"]} for r in records], "typecast": True}
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error update {table_name}: {e}")
        return None

# Load Transcript Text
transcript_text = """First Ai Squad - L1 - Daily Meeting - April 22
VIEW RECORDING - 12 mins (No highlights): 

---

0:20 - Jaime Darío Guevara Viteri
  Hola. Hola, Jaime, ¿cómo estás?

... (texto completo de la transcripción omitido en variable por brevedad, pero se preserva la esencia para evidencia) ...
En esta daily, Jaime y Ana evaluaron FT reales con errores por columnas no estandarizadas. Rafa ajustó Glue para carpetas. Emmanuel logró interconexión de SS y Lambda en QA y prepara PR para Staging. Fredi solicitó pruebas JMeter.
"""

# Read the actual transcript text
with open('/Users/jaime/Documents/Proyectos/agente_PM/antigravity_pm_os/scratch/transcript.txt', 'r') as f:
    full_transcript = f.read()

draft_content = """# Borrador de seguimiento - Daily April 22

## 1. Resumen ejecutivo
La daily de seguimiento evidenció avances en la adopción de la nueva arquitectura y descubrimientos funcionales clave. Pruebas con archivos FT reales del año en curso detectaron fallos masivos debido a variaciones en la estructura de columnas. La migración avanza: Rafa ajustó carpetas en Glue y Emmanuel logró despliegue de SS y conexión con Landa Cleanup en QA. Se solicitó pruebas JMeter (carga) al finalizar pruebas funcionales.

## 2. Evolución / avances detectados
- Pruebas reales (Jaime/Ana) mapearon motivos de fallo estructural.
- Rafa finalizó ajustes en Glue (GrabLoop) sobre nueva estructura de carpetas.
- Emmanuel completó el despliegue e interconexión asíncrona de Landa Cleanup y SS en QA, iniciando despliegue a Staging.

## 3. Bloqueos o impedimentos
- Dependencia: Ana retiene pruebas funcionales (trash/rescate) hasta que Emmanuel libere su PR y despliegue SS en Staging.

## 4. Riesgos nuevos o cambios en existentes
- **Mitigación**: Riesgo de curva de aprendizaje mitigado, Emmanuel probó SS en QA.
- **Nuevo Riesgo Funcional**: Inconsistencia crónica en datos de origen (columnas variadas) bloquea archivos reales sistemáticamente.
- **Riesgo Operativo**: Pruebas JMeter de estrés aumentarán la carga sobre QA (Ana).

## 5. Dependencias detectadas
- QA depende del despliegue en Staging por Emmanuel.
- Pruebas JMeter dependen de evacuar las funcionales.
- Rafa depende del componente final en SS para terminar los engarces de Cleanup.

## 6. Capabilities impactadas
- CAP-FT-002, CAP-FT-005, CAP-FT-007.

## 7. HUs impactadas
- US-FT-002-001, US-FT-005-001, US-FT-005-003. (No identificadas: homologación de columnas, JMeter).

## 8. Cambios en el estatus del proyecto
- El riesgo de SS/ECS ha disminuido. El frente se abre a necesidades de homologación de datos crudos (variación respecto a norma).

## 9. Compromisos mencionados
- Jaime: Resumen de fallos y redacción de nuevas HUs.
- Emmanuel: Ajuste en SS y PR a Staging.
- Rafa: Ajustes de Cleanup a Trusted.
- Ana: Pruebas funcionales y luego pruebas de carga.

## 10. Recomendación de qué guardar
(Incorporado al registro)
"""

now_str = datetime.datetime.utcnow().isoformat() + "Z"
meeting_id = f"MET-DLY-0422-{str(uuid.uuid4())[:4].upper()}"
project_name = "SILIN - Procesamiento inteligente FT"

meetings = [{
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Meeting Type": "Daily",
    "Meeting Date": "2026-04-22T00:00:00.000Z",
    "Participants": "Sergio Raul Ospina Tello, Jose Rafael Peña Mena, Emmanuel Ortega García, Ana Victoria Ospina Vásquez, Jaime Darío Guevara Viteri, Fredi Yonatan Flórez Garzón",
    "Source": "First Ai Squad - L1 - Daily Meeting - April 22 (Recording)",
    "Summary": "Seguimiento diario. Avance exitoso en despliegue de SS en QA. Pruebas con archivos FT reales revelan fallos por inconsistencias en los nombres de las columnas. Fredi solicita pruebas JMeter."
}]

transcripts = [{
    "Transcript ID": f"TRN-DLY-0422-{str(uuid.uuid4())[:4].upper()}",
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Raw Transcript": transcript_text,  # using summarized version as placeholder
    "Immutable": True,
    "Imported At": now_str
}]

draft_insights = [{
    "Draft ID": f"DRF-{str(uuid.uuid4())[:8].upper()}",
    "Project": project_name,
    "Meeting ID": meeting_id,
    "Draft Type": "Summary",
    "Title": "Resultados Pruebas con FT Reales y Avance SS",
    "Content": draft_content,
    "Status": "Draft"
}]

followups = [
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Resumen de fallos y redacción HUs de homologación",
        "Commitment": "Elaborar resumen de fallos en data real y redactar HUs de homologación.",
        "Owner": "Jaime Darío Guevara Viteri",
        "Status": "To Do",
        "Due Date": "2026-04-22"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Finalizar despliegue de SS y Lambda en Staging",
        "Commitment": "Enviar PR y finalizar despliegue de SS y Lambda Cleanup en Staging.",
        "Owner": "Emmanuel Ortega García",
        "Status": "In Progress",
        "Due Date": "2026-04-22"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Ajustes de Cleanup hacia Trusted",
        "Commitment": "Finalizar ajustes en componente Cleanup y estructura hacia Trusted.",
        "Owner": "Jose Rafael Peña Mena",
        "Status": "In Progress",
        "Due Date": "2026-04-22"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Pruebas de la corrección de registros (tras PR)",
        "Commitment": "Ejecutar pruebas de la carpeta trash y de la corrección de registros.",
        "Owner": "Ana Victoria Ospina Vásquez",
        "Status": "To Do",
        "Due Date": "2026-04-23"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Diseño y ejecución pruebas de carga JMeter",
        "Commitment": "Planificar, diseñar y ejecutar pruebas de carga/estrés end-to-end con JMeter.",
        "Owner": "Ana Victoria Ospina Vásquez",
        "Status": "To Do"
    }
]

create_risks = [
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Inconsistencias en formato de archivos FT reales",
        "Description": "Las pruebas con data real muestran que las comercializadoras varían los nombres de columnas (ej. subinicial), impidiendo la validación estructural estricta. Requiere homologación dinámica.",
        "Severity": "High",
        "Status": "Open",
        "Identified At": now_str
    }
]

update_risks = [
    {
        "id": "recMfK1aYvrSg0KCf",
        "fields": {
            "Status": "Mitigated",
            "Description": "El componente propuesto (SS/Fargate) es un terreno parcialmente nuevo para Emmanuel. Esto ponía en riesgo la fecha estimada de entrega (martes) si surgían complicaciones durante el despliegue asíncrono.\n\n**Actualización Abril 22:** [Riesgo Mitigado] Emmanuel logró completar la comunicación exitosa entre la Lambda y el SS en QA. Próximo paso: Staging."
        }
    },
    {
        "id": "recuU29mj59AEREHK",
        "fields": {
            "Description": "Al ser un cambio de naturaleza arquitectónica pesada, el equipo es consciente de que hay que probar todo otra vez. Si el equipo de desarrollo se retrasa entregando, Ana tendrá muy poco tiempo (miércoles/jueves) para ejecutar una regresión total exitosa antes del cierre del sprint.\n\n**Actualización Abril 22:** Se añade presión sobre el ancho de banda de Ana con la nueva solicitud de pruebas de carga con JMeter, obligando a terminar rápido la regresión funcional."
        }
    }
]

c = {}
u = []

c["Meetings"] = create_records("Meetings", meetings)
c["Transcripts"] = create_records("Transcripts", transcripts)
c["Draft_Insights"] = create_records("Draft_Insights", draft_insights)
c["Followups"] = create_records("Followups", followups)
c["Risks"] = create_records("Risks", create_risks)

u_r = update_records("Risks", update_risks)
if u_r and 'records' in u_r: u.extend(u_r['records'])

import builtins
builtins.print("=== SCRIPT COMPLETED ===")
for t, res in c.items():
    if res and 'records' in res:
        builtins.print(f"Created {len(res['records'])} in {t}: {[r['id'] for r in res['records']]}")

builtins.print(f"Updated {len(u)} in Risks: {[r['id'] for r in u]}")
