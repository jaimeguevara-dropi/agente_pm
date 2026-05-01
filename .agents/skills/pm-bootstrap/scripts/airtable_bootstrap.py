from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import requests
import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[4]
load_dotenv(ROOT / ".env")

API_URL = os.getenv("AIRTABLE_API_URL", "https://api.airtable.com/v0").rstrip("/")
TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
REPORT_PATH = ROOT / os.getenv("BOOTSTRAP_REPORT_PATH", "logs/bootstrap_report.md")
SCHEMA_PATH = ROOT / "schema" / "airtable_base.yaml"
TIMEOUT = 60


class BootstrapError(Exception):
    pass


@dataclass
class ChangeLog:
    created_tables: List[str]
    created_fields: List[str]
    skipped_tables: List[str]
    skipped_fields: List[str]
    warnings: List[str]

    def __init__(self) -> None:
        self.created_tables = []
        self.created_fields = []
        self.skipped_tables = []
        self.skipped_fields = []
        self.warnings = []


def require_env() -> None:
    missing = [name for name, value in {"AIRTABLE_TOKEN": TOKEN, "AIRTABLE_BASE_ID": BASE_ID}.items() if not value]
    if missing:
        raise BootstrapError(f"Faltan variables de entorno requeridas: {', '.join(missing)}")


def headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }


def read_schema() -> Dict[str, Any]:
    if not SCHEMA_PATH.exists():
        raise BootstrapError(f"No existe el esquema esperado: {SCHEMA_PATH}")
    with SCHEMA_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def request_json(method: str, path: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
    url = f"{API_URL}{path}"
    response = requests.request(method, url, headers=headers(), json=payload, timeout=TIMEOUT)
    if response.status_code >= 400:
        detail = response.text
        raise BootstrapError(f"Error {response.status_code} en {method} {url}: {detail}")
    if response.text.strip():
        return response.json()
    return {}


def get_existing_tables() -> Dict[str, Dict[str, Any]]:
    data = request_json("GET", f"/meta/bases/{BASE_ID}/tables")
    return {table["name"]: table for table in data.get("tables", [])}


def normalize_field(field: Dict[str, Any]) -> Dict[str, Any]:
    field_type = field["type"]
    normalized: Dict[str, Any] = {"name": field["name"], "type": field_type}

    if field_type == "singleSelect":
        choices = field.get("choices", [])
        normalized["options"] = {
            "choices": [{"name": choice} for choice in choices]
        }
    elif field_type == "multipleSelects":
        choices = field.get("choices", [])
        normalized["options"] = {
            "choices": [{"name": choice} for choice in choices]
        }
    elif field_type == "dateTime":
        normalized["type"] = "dateTime"
        normalized["options"] = {
            "timeZone": "utc",
            "dateFormat": {"name": "iso"},
            "timeFormat": {"name": "24hour"},
        }
    elif field_type == "number":
        normalized["options"] = {"precision": 0}
    elif field_type == "url":
        pass
    elif field_type == "checkbox":
        normalized["options"] = {"icon": "check", "color": "greenBright"}
    elif field_type == "multilineText":
        normalized["type"] = "multilineText"
    elif field_type == "singleLineText":
        normalized["type"] = "singleLineText"
    else:
        raise BootstrapError(f"Tipo de campo no soportado en este scaffold: {field_type}")

    return normalized


def create_table(table_def: Dict[str, Any], changelog: ChangeLog) -> Dict[str, Any]:
    payload = {
        "name": table_def["name"],
        "description": table_def.get("description", ""),
        "fields": [normalize_field(field) for field in table_def.get("fields", [])],
    }
    created = request_json("POST", f"/meta/bases/{BASE_ID}/tables", payload)
    changelog.created_tables.append(table_def["name"])
    return created


def create_field(table_id: str, field_def: Dict[str, Any], table_name: str, changelog: ChangeLog) -> Dict[str, Any]:
    payload = normalize_field(field_def)
    created = request_json("POST", f"/meta/bases/{BASE_ID}/tables/{table_id}/fields", payload)
    changelog.created_fields.append(f"{table_name}.{field_def['name']}")
    return created


def ensure_tables_and_fields(schema: Dict[str, Any]) -> ChangeLog:
    changelog = ChangeLog()
    existing_tables = get_existing_tables()

    for table_def in schema.get("tables", []):
        table_name = table_def["name"]
        if table_name not in existing_tables:
            create_table(table_def, changelog)
            existing_tables = get_existing_tables()
        else:
            changelog.skipped_tables.append(table_name)

        existing_table = existing_tables[table_name]
        table_id = existing_table["id"]
        existing_fields = {field["name"]: field for field in existing_table.get("fields", [])}

        for field_def in table_def.get("fields", []):
            field_name = field_def["name"]
            if field_name in existing_fields:
                changelog.skipped_fields.append(f"{table_name}.{field_name}")
                continue
            create_field(table_id, field_def, table_name, changelog)

    return changelog


def write_report(schema: Dict[str, Any], changelog: ChangeLog) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report = f"""# Bootstrap report\n\n## Base objetivo\n\n- Base name (referencial): {schema.get('base_name', 'N/A')}\n- Airtable base id: {BASE_ID}\n\n## Tablas creadas\n\n{format_bullets(changelog.created_tables)}\n\n## Campos creados\n\n{format_bullets(changelog.created_fields)}\n\n## Tablas ya existentes\n\n{format_bullets(changelog.skipped_tables)}\n\n## Campos ya existentes\n\n{format_bullets(changelog.skipped_fields[:100])}\n\n## Advertencias\n\n{format_bullets(changelog.warnings)}\n\n## Política aplicada\n\n- No se borró ninguna tabla.\n- No se borró ningún campo.\n- Solo se agregaron elementos faltantes.\n"""
    REPORT_PATH.write_text(report, encoding="utf-8")


def format_bullets(items: List[str]) -> str:
    if not items:
        return "- Ninguno"
    return "\n".join(f"- {item}" for item in items)


def main() -> None:
    require_env()
    schema = read_schema()
    changelog = ensure_tables_and_fields(schema)
    write_report(schema, changelog)
    print(json.dumps({
        "created_tables": changelog.created_tables,
        "created_fields": changelog.created_fields,
        "report_path": str(REPORT_PATH),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except BootstrapError as exc:
        raise SystemExit(str(exc))
