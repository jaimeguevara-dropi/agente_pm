import os
import urllib.request
import urllib.error
import json
import uuid
from datetime import datetime
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
    'Content-Type': 'application/json'
}

def create_records(table_name, records):
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    data = {
        "records": [{"fields": r} for r in records],
        "typecast": True
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error in CREATE {table_name}: {e.code} - {e.read().decode('utf-8')}")
        return None

def fetch_all_records(table_name):
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}"
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8')).get('records', [])
    except urllib.error.HTTPError as e:
        print(f"Error in GET {table_name}: {e.code} - {e.read().decode('utf-8')}")
        return []

def update_record(table_name, record_id, fields):
    url = f"https://api.airtable.com/v0/{base_id}/{urllib.parse.quote(table_name)}/{record_id}"
    data = {
        "fields": fields,
        "typecast": True
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error in UPDATE {table_name}: {e.code} - {e.read().decode('utf-8')}")
        return None


mtg_id = f"MTG-{str(uuid.uuid4())[:8].upper()}"

meetings = [{
    "Meeting ID": mtg_id,
    "Project": "SILIN - Procesamiento inteligente FT",
    "Meeting Type": "Other",
    "Meeting Date": "2026-04-23T00:00:00Z",
    "Notes": "Sprint 10 Review - First Ai Squad"
}]

transcripts = [{
    "Transcript ID": f"TRN-{str(uuid.uuid4())[:8].upper()}",
    "Meeting ID": mtg_id,
    "Project": "SILIN - Procesamiento inteligente FT",
    "Source URL": "https://fathom.video/share/hSirixZsx7zkdzBL2kvBydSaeihDYTnx",
    "Raw Transcript": "Resumen/Transcripción: Se superó cuello de botella técnico con ECS. Se procesaron 35 archivos FT. 29 de 35 rechazados por estructura (nombres de cabeceras). Homologación manual exitosa. Riesgos de datos detectados a nivel de registro (ej. guiones en medidores).",
    "Immutable": True
}]

followups_content = """# Borrador de seguimiento: Sprint Review 10

## 1. Resumen ejecutivo del Sprint 10
El Sprint 10 demostró la viabilidad técnica al 100% del procesamiento parcial de archivos masivos. Se superó el cuello de botella histórico de caídas del sistema mediante el cambio arquitectónico de Lambda a ECS. Se procesó 35 archivos FT reales. Reto principal: variabilidad de cabeceras.

## 2. Avances reales del sprint
- Pruebas en vivo con datos reales.
- Cambio arquitectónico a ECS.
- Nueva estructura de almacenamiento S3.
- Homologación manual exitosa de columnas.
- Certificación de 4 HUs.

## 3. Bloqueos, dependencias y riesgos
- Riesgo: Alta variabilidad en cabeceras de archivos.
- Riesgo: Baja calidad de datos a nivel de registro.
- Dependencia: Definición de reglas funcionales de limpieza de datos.
- Tema discutido: Pre-validación con IA/UX enviada a backlog.

## 4. Capabilities impactadas
- CAP-FT-001 - Recepción de Lotes FT
- CAP-FT-002 - Validación estructural y funcional de archivo

## 5. HUs impactadas
- US-FT-001-001
- US-FT-002-007
- US-FT-002-008

## 6. Estatus actual del proyecto
Viable, estable, foco ahora en capa de datos.

## 7. Conclusiones a la fecha
El componente infraestructura ya no es riesgo. Trabajo enfocado en reglas por registro.

## 8. Riesgos a la fecha
Rechazos estructurales por nuevas comercializadoras. Volumen de basura en registros.

## 9. Logros de Emanuel
Cambio ECS exitoso.

## 10. Logros de Rafael
Ajuste Lambda receptora y nueva estructura carpetas.

## 11. Logros de Ana
Certificación 4 HUs y 2 bugs cerrados."""

followups = [{
    "Followup ID": f"FOL-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Title": "Seguimiento Operativo - Sprint 10 Review",
    "Commitment": followups_content,
    "Status": "Open"
}]

decisions = [{
    "Decision ID": f"DEC-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Title": "Pausar iniciativas de IA y UX pre-cargue",
    "Decision": "No integrar agente de IA ni flujos de validación UX externos en fase actual.",
    "Rationale": "Enviadas al backlog de mejoras futuras (Nice to have) para proteger MVP (15 de mayo).",
    "Status": "Active"
}]

milestones = [{
    "Milestone ID": f"MIL-{str(uuid.uuid4())[:8].upper()}",
    "Project": "SILIN - Procesamiento inteligente FT",
    "Name": "Procesamiento Masivo Estable (ECS)",
    "Description": "El sistema soportó prueba con 35 archivos reales (2026) sin caídas.",
    "Status": "Done",
    "Target Date": "2026-04-23T00:00:00Z"
}]

print("--- Creating new records ---")
create_records("Meetings", meetings)
create_records("Transcripts", transcripts)
create_records("Followups", followups)
create_records("Decisions", decisions)
create_records("Milestones", milestones)

print("--- Updating Risks ---")
existing_risks = fetch_all_records("Risks")
risk_updates = {
    "Alta tasa de registros inválidos": "Se detectó alta presencia de datos basura en prueba real (ej. Emcali con 305k inválidos por guiones en medidores). Casi 90% invalidados, presión sobre rescate.",
    "Reglas funcionales estructurales no consolidadas": "29 de 35 archivos fallaron por nombres de cabeceras en pruebas reales. Mitigación: estrategia de homologación dinámica (alias)."
}

for risk in existing_risks:
    fields = risk.get('fields', {})
    title = fields.get('Title', '')
    if title in risk_updates:
        print(f"Updating Risk: {title}")
        new_desc = risk_updates[title] + "\n\nSource References: Reviews 1 al 7, Sprint 10 Review"
        update_record("Risks", risk['id'], {"Description": new_desc, "Status": "Open"})

print("Done.")
