import urllib.request
import urllib.error
import urllib.parse
import json
import datetime
import uuid
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

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
        with urllib.request.urlopen(req, context=ctx) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error create {table_name}: {e}")
        return None

transcript_text = """First Ai Squad - L1 - Daily Meeting - April 30
El Sprint 10 finalizó con un alto porcentaje de completitud técnica (100% de historias). Se detectó un cuello de botella grave en la concurrencia del GLUE durante pruebas de carga masiva.
"""

draft_content = """# Borrador de seguimiento - Daily April 30

## 1. Resumen ejecutivo
El Sprint 10 finalizó con un alto porcentaje de completitud técnica (100% de las tareas comprometidas: 27 story points, 5 historias + 2 bugs de performance cerrados). Se evidenció madurez en la Lambda Cleanup, estabilización en la migración de tablas maestras a Brain, y se realizó la primera prueba de carga que destapó un cuello de botella en el Glue (ingestión) para archivos pesados o múltiples.

## 2. Evolución / avances detectados
- **Lambda Cleanup:** Mayor robustez gracias a pruebas con data real, lo que permitió cubrir casos no mapeados inicialmente sin afectar tiempos de procesamiento (Rafa).
- **Tablas maestras migradas:** Entidad, tributo y compañía de energía ahora operan bajo la arquitectura de Brain y están integradas en Lambda Ingestion, Glue y ESS (Emmanuel).
- **Carga de archivos:** Se ajustó la validación de headers para ser más permisivos/tolerantes a errores de la comercializadora (Emmanuel / Rafa).
- **Componente ESS:** Se implementó el envío de correos. Se incrementó la memoria (CPU y RAM) para soportar escenarios de procesamiento elevado ante los fallos detectados por QA (Emmanuel).
- **Testing:** Se logró completar pruebas tempranamente a medida que se entregaban las historias, detectando cuellos de botella reales en performance.

## 5. Riesgos detectados
- **Cuello de botella en GLUE (Ingestión):** No soporta concurrencia o envíos de varios archivos pesados al mismo tiempo (ej. de 5 archivos solo toma 1 o 2). Pierde requests. (Riesgo Técnico / Arquitectura).
- **Sincronización de Tablas Maestras:** Riesgo de desactualización si se agregan nuevas empresas de energía o entidades, al no tener una sincronización automática fluida (Riesgo Operativo).
- **Capacidad de QA:** La dedicación de Ana compartida con otra lancha limita la capacidad de testing, lo que requiere vigilar la asignación de puntos para el próximo sprint.

## 7. Decisiones o definiciones pendientes
- Definición arquitectónica con Freddy/Jaime sobre cómo manejar el cuello de botella en GLUE para cargas concurrentes.
- Estrategia para mantener sincronizadas las tablas maestras cuando haya actualizaciones de negocio.

## 8. Compromisos / próximos pasos
- Grabar la demo mostrando los cambios de trazabilidad de versiones, limpieza de datos, y homologación de encabezados (Rafa, Ana, Jaime).
- Preparar la PPT de cierre de sprint / review basada en los logros (Sergio).
- Cerrar las historias formalmente en Jira antes de la Review/Refinamiento (Ana).
"""

now_str = datetime.datetime.utcnow().isoformat() + "Z"
meeting_id = f"MET-DLY-0430-{str(uuid.uuid4())[:4].upper()}"
project_name = "SILIN - Procesamiento inteligente FT"

meetings = [{
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Meeting Type": "Follow-up",
    "Meeting Date": "2026-04-30T00:00:00.000Z",
    "Participants": "Sergio Raul Ospina Tello, Emmanuel Ortega García, Jose Rafael Peña Mena, Ana Victoria Ospina Vásquez",
    "Source": "First Ai Squad - L1 - Daily Meeting - April 30",
    "Notes": "Daily de cierre Sprint 10. Completitud del 100% (27 SP, 5 HUs, 2 Bugs). Pruebas de performance destapan cuello de botella en GLUE. Se define agenda para grabar demo y PPT."
}]

transcripts = [{
    "Transcript ID": f"TRN-DLY-0430-{str(uuid.uuid4())[:4].upper()}",
    "Meeting ID": meeting_id,
    "Project": project_name,
    "Team": "First Ai Squad - L1",
    "Raw Transcript": transcript_text,
    "Immutable": True,
    "Imported At": now_str
}]

draft_insights = [{
    "Draft ID": f"DRF-{str(uuid.uuid4())[:8].upper()}",
    "Project": project_name,
    "Meeting ID": meeting_id,
    "Draft Type": "Summary",
    "Title": "Cierre Sprint 10 y Riesgos de Performance",
    "Content": draft_content,
    "Status": "Approved"
}]

followups = [
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Grabar la demo Sprint 10",
        "Commitment": "Grabar la demo mostrando los cambios de trazabilidad de versiones, limpieza de datos y homologación de encabezados.",
        "Owner": "Jose Rafael Peña Mena",
        "Status": "To Do",
        "Due Date": "2026-04-30"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Preparar PPT Review",
        "Commitment": "Preparar la PPT de cierre de sprint / review basada en los logros.",
        "Owner": "Sergio Raul Ospina Tello",
        "Status": "To Do",
        "Due Date": "2026-04-30"
    },
    {
        "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Cerrar Historias en Jira",
        "Commitment": "Cerrar las historias formalmente en Jira antes de la Review/Refinamiento.",
        "Owner": "Ana Victoria Ospina Vásquez",
        "Status": "To Do",
        "Due Date": "2026-04-30"
    }
]

create_risks = [
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Cuello de botella en GLUE ante concurrencia",
        "Description": "El GLUE no soporta envíos de varios archivos pesados al mismo tiempo, perdiendo requests (toma 1 o 2 de 5 archivos enviados concurrentemente).",
        "Impact": "High",
        "Probability": "High",
        "Status": "Open"
    },
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Desactualización de Tablas Maestras",
        "Description": "Riesgo operativo al no tener un mecanismo automático y sincronizado fluido de actualización si ingresan nuevas empresas de energía o entidades.",
        "Impact": "Medium",
        "Probability": "Medium",
        "Status": "Open"
    },
    {
        "Risk ID": f"RSK-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Capacidad de QA dividida",
        "Description": "Ana está asignada a otra lancha, lo cual limita su capacidad de atención exclusiva para QA en futuros Sprints, obligando a revisar cuidadosamente la asignación de puntos.",
        "Impact": "Medium",
        "Probability": "High",
        "Status": "Open"
    }
]

decisions = [
    {
        "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
        "Project": project_name,
        "Title": "Aumentar CPU y RAM en ECS/SS",
        "Description": "Se decidió aumentar la memoria RAM y CPU del componente SS tras los fallos detectados por cargas altas.",
        "Status": "Approved",
        "Date": now_str
    }
]

c = {}
# c["Meetings"] = create_records("Meetings", meetings)
# c["Transcripts"] = create_records("Transcripts", transcripts)
# c["Draft_Insights"] = create_records("Draft_Insights", draft_insights)
# c["Followups"] = create_records("Followups", followups)
c["Risks"] = create_records("Risks", create_risks)
c["Decisions"] = create_records("Decisions", decisions)

import builtins
builtins.print("=== SCRIPT COMPLETED ===")
for t, res in c.items():
    if res and 'records' in res:
        builtins.print(f"Created {len(res['records'])} in {t}: {[r['id'] for r in res['records']]}")
