from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import quote

import requests
from dotenv import load_dotenv

ROOT = Path.cwd()
load_dotenv(ROOT / ".env")

API_URL = os.getenv("AIRTABLE_API_URL", "https://api.airtable.com/v0").rstrip("/")
TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = "Capabilities"
PROJECT = "SILIN - Procesamiento inteligente FT"

CAPABILITIES: List[Dict[str, Any]] = [
    {
        "Order": "1",
        "Capability ID": "CAP-FT-001",
        "Project": PROJECT,
        "Name": "Recepción de Lotes FT",
        "Purpose": "Permitir la recepción controlada de archivos FT y su conversión en una unidad formal de procesamiento llamada lote, garantizando trazabilidad, estados claros y control operativo desde el primer momento.",
        "Scope": "Creación del lote, identificador único, metadatos, asociación a comercializadora, entidad, periodo y tipo de archivo FT, estados iniciales y trazabilidad mínima.",
        "Expected Outcome": "Todo archivo FT recibido existe como lote formal, con identidad clara, estado consultable y listo para validación estructural, funcional y procesamiento parcial.",
        "Exclusions": "No incluye validaciones estructurales, funcionales, tributarias, corrección automática, interacción visual con comercializadoras, integraciones con facturación/cartera, autorizaciones humanas ni dashboards.",
        "Status": "Active",
        "Version": "1",
        "Source References": "Capacidades / épicas consolidadas del TO-BE",
    },
    {
        "Order": "2",
        "Capability ID": "CAP-FT-002",
        "Project": PROJECT,
        "Name": "Validación estructural y funcional de archivo",
        "Purpose": "Validar que el archivo FT y sus registros cumplen condiciones técnicas mínimas para continuar el flujo, eliminando el bloqueo todo o nada.",
        "Scope": "Validación estructural del archivo, evaluación independiente por registro, detección de fallas críticas, clasificación de válidos e inválidos y trazabilidad de motivos.",
        "Expected Outcome": "El lote queda totalmente válido, parcialmente válido o estructuralmente rechazado, manteniendo trazabilidad entre lote, registros y motivos de invalidación.",
        "Exclusions": "No incluye corrección automática, rechazo tributario definitivo, notificaciones, dispersión, validación de calendarios, IA de rescate ni visualizaciones avanzadas.",
        "Status": "Active",
        "Version": "1",
        "Source References": "Capacidades / épicas consolidadas del TO-BE",
    },
    {
        "Order": "3",
        "Capability ID": "CAP-FT-003",
        "Project": PROJECT,
        "Name": "Gestión de registros inválidos",
        "Purpose": "Mantener control, trazabilidad y visibilidad interna sobre registros inválidos sin bloquear el procesamiento parcial.",
        "Scope": "Identificación de inválidos, asociación de tipo de error, campo afectado y motivo, estado PENDIENTE_DE_CORRECCIÓN, consulta interna por lote, entidad y periodo.",
        "Expected Outcome": "Los registros inválidos quedan controlados, visibles y trazables, sin impedir que los registros válidos avancen.",
        "Exclusions": "No incluye SLAs, sanciones, notificaciones, comunicación con comercializadoras, corrección, rescate, revalidación incremental, decisiones legales ni dashboards avanzados.",
        "Status": "Active",
        "Version": "1",
        "Source References": "Capacidades / épicas consolidadas del TO-BE",
    },
    {
        "Order": "4",
        "Capability ID": "CAP-FT-004",
        "Project": PROJECT,
        "Name": "Disponibilización de registros válidos del lote FT para dispersión en SILIN",
        "Purpose": "Preparar y disponibilizar registros válidos en FT-01 y/o FT-06 sin bloquearse por la existencia de registros inválidos.",
        "Scope": "Identificación de válidos, generación FT-01/FT-06, asociación a entidad, periodo, lote y tipo de archivo, repositorio controlado, feedback técnico y control de duplicidades.",
        "Expected Outcome": "Los registros válidos quedan separados y disponibles para Plataforma SILIN, con feedback técnico trazable sobre dispersión.",
        "Exclusions": "No incluye dispersión directa, causación, liquidación, facturación, rescate de inválidos, notificación a comercializadoras, calendario tributario, dashboards ni cambios legales.",
        "Status": "Active",
        "Version": "1",
        "Source References": "Capacidades / épicas consolidadas del TO-BE",
    },
    {
        "Order": "5",
        "Capability ID": "CAP-FT-005",
        "Project": PROJECT,
        "Name": "Revalidación incremental de registros inválidos",
        "Purpose": "Permitir que solo los registros previamente inválidos y corregidos sean revalidados sin reprocesar el lote completo.",
        "Scope": "Recepción de registros corregidos, identificación de reproceso, asociación al lote original, revalidación individual, actualización de estado y reincorporación al flujo si queda válido.",
        "Expected Outcome": "Los registros corregidos pueden reincorporarse al flujo sin reprocesar todo el lote.",
        "Exclusions": "No incluye detección automática de correcciones, versionado complejo, comparación semántica ni reprocesamiento completo del lote.",
        "Status": "Active",
        "Version": "1",
        "Source References": "Capacidades / épicas consolidadas del TO-BE",
    },
    {
        "Order": "6",
        "Capability ID": "CAP-FT-006",
        "Project": PROJECT,
        "Name": "Gestión, rescate y notificación de registros rechazados",
        "Purpose": "Cerrar el ciclo del error a nivel de registro, intentando rescatar lo recuperable, identificando lo irrecuperable y notificando registros rechazados.",
        "Scope": "Rescate de inválidos, identificación de irrecuperables, notificación de rechazados y cierre operativo del error. Hipótesis: ID del medidor como llave principal.",
        "Expected Outcome": "Lo válido sigue su camino, lo rechazado queda oficialmente notificado y no hay ambigüedad operativa.",
        "Exclusions": "No incluye corrección automática, reenvío automático, dispersión, validación tributaria legal ni UI avanzada para comercializadoras.",
        "Status": "Active",
        "Version": "1",
        "Source References": "Capacidades / épicas consolidadas del TO-BE",
    },
    {
        "Order": "7",
        "Capability ID": "CAP-FT-007",
        "Project": PROJECT,
        "Name": "Estados y trazabilidad transversal del procesamiento FT",
        "Purpose": "Permitir seguimiento confiable del estado técnico del procesamiento FT desde recepción hasta validación y disponibilización.",
        "Scope": "Estado técnico del lote, estado por registro, historial básico, repositorio, validación posterior por Datos y consulta por entidad, periodo y lote.",
        "Expected Outcome": "El flujo queda observable y gobernable mediante estados técnicos, historial y trazabilidad por lote y registro.",
        "Exclusions": "No incluye calendario tributario, alertas, vencimientos, dispersión, integración directa con SILIN vía API, dashboards gráficos ni decisiones normativas.",
        "Status": "Active",
        "Version": "1",
        "Source References": "Capacidades / épicas consolidadas del TO-BE",
    },
]

REQUIRED_FIELDS = {
    "Capability ID": "singleLineText",
    "Project": "singleLineText",
    "Name": "singleLineText",
    "Purpose": "multilineText",
    "Scope": "multilineText",
    "Expected Outcome": "multilineText",
    "Exclusions": "multilineText",
    "Status": "singleLineText",
    "Version": "singleLineText",
    "Order": "singleLineText",
    "Source References": "multilineText",
}


def require_env() -> None:
    missing = [k for k, v in {"AIRTABLE_TOKEN": TOKEN, "AIRTABLE_BASE_ID": BASE_ID}.items() if not v]
    if missing:
        raise SystemExit(f"Faltan variables de entorno: {', '.join(missing)}")


def headers() -> Dict[str, str]:
    return {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


def request_json(method: str, path: str, payload: Dict[str, Any] | None = None, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    url = f"{API_URL}{path}"
    response = requests.request(method, url, headers=headers(), json=payload, params=params, timeout=60)
    if response.status_code >= 400:
        raise SystemExit(f"Error {response.status_code} en {method} {url}: {response.text}")
    return response.json() if response.text.strip() else {}


def get_schema() -> Dict[str, Any]:
    return request_json("GET", f"/meta/bases/{BASE_ID}/tables")


def get_table(schema: Dict[str, Any], table_name: str) -> Dict[str, Any]:
    for table in schema.get("tables", []):
        if table.get("name") == table_name:
            return table
    raise SystemExit(f"No encontré la tabla {table_name}")


def create_field(table_id: str, name: str, field_type: str) -> None:
    request_json(
        "POST",
        f"/meta/bases/{BASE_ID}/tables/{table_id}/fields",
        payload={"name": name, "type": field_type},
    )


def ensure_fields() -> None:
    schema = get_schema()
    table = get_table(schema, TABLE_NAME)
    existing = {field["name"] for field in table.get("fields", [])}

    created = []
    for field_name, field_type in REQUIRED_FIELDS.items():
        if field_name not in existing:
            create_field(table["id"], field_name, field_type)
            created.append(field_name)

    if created:
        print(json.dumps({"created_fields": created}, ensure_ascii=False, indent=2))


def find_record(capability_id: str) -> str | None:
    params = {
        "filterByFormula": f"{{Capability ID}}='{capability_id}'",
        "maxRecords": 1,
    }
    data = request_json("GET", f"/{BASE_ID}/{quote(TABLE_NAME)}", params=params)
    records = data.get("records", [])
    return records[0]["id"] if records else None


def create_record(fields: Dict[str, Any]) -> str:
    payload = {"records": [{"fields": fields}], "typecast": True}
    result = request_json("POST", f"/{BASE_ID}/{quote(TABLE_NAME)}", payload=payload)
    return result["records"][0]["id"]


def update_record(record_id: str, fields: Dict[str, Any]) -> None:
    payload = {"fields": fields, "typecast": True}
    request_json("PATCH", f"/{BASE_ID}/{quote(TABLE_NAME)}/{record_id}", payload=payload)


def main() -> None:
    require_env()
    ensure_fields()

    created = []
    updated = []

    for capability in CAPABILITIES:
        record_id = find_record(capability["Capability ID"])
        if record_id:
            update_record(record_id, capability)
            updated.append(capability["Capability ID"])
        else:
            new_id = create_record(capability)
            created.append({"capability_id": capability["Capability ID"], "record_id": new_id})

    print(json.dumps({
        "table": TABLE_NAME,
        "project": PROJECT,
        "created": created,
        "updated": updated,
        "total": len(CAPABILITIES),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
