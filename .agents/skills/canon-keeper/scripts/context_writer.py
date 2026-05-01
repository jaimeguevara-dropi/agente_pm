from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import quote

import requests
from dotenv import load_dotenv

ROOT = Path.cwd()
load_dotenv(ROOT / ".env")

API_URL = os.getenv("AIRTABLE_API_URL", "https://api.airtable.com/v0").rstrip("/")
TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TIMEOUT = 60
APPROVED_TABLE = "Approved_Context"
DRAFT_TABLE = "Draft_Insights"

TYPE_ALIASES = {
    "business context": ["Business Context", "Business_Context"],
    "business_context": ["Business_Context", "Business Context"],
    "asis": ["ASIS"],
    "tobe": ["TOBE"],
    "capability": ["Capability"],
    "feature": ["Feature"],
    "user story": ["User Story", "User_Story"],
    "user_story": ["User_Story", "User Story"],
    "risk": ["Risk"],
    "decision": ["Decision"],
    "operating rule": ["Operating Rule", "Operating_Rule"],
    "operating_rule": ["Operating_Rule", "Operating Rule"],
}

DRAFT_TYPE_ALIASES = {
    "business context": ["Business Context", "Business_Context"],
    "business_context": ["Business_Context", "Business Context"],
    "asis": ["ASIS"],
    "tobe": ["TOBE"],
    "capability": ["Capability"],
    "feature": ["Feature"],
    "user story": ["User Story"],
    "user_story": ["User Story"],
    "risk": ["Risk"],
    "decision": ["Decision"],
    "summary": ["Summary"],
    "open question": ["Open Question"],
    "open_question": ["Open Question"],
}


class ContextWriterError(Exception):
    pass


def require_env() -> None:
    missing = [name for name, value in {"AIRTABLE_TOKEN": TOKEN, "AIRTABLE_BASE_ID": BASE_ID}.items() if not value]
    if missing:
        raise ContextWriterError(f"Faltan variables de entorno: {', '.join(missing)}")


def headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }


def request_json(method: str, path: str, payload: Dict[str, Any] | None = None, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    url = f"{API_URL}{path}"
    resp = requests.request(method, url, headers=headers(), json=payload, params=params, timeout=TIMEOUT)
    if resp.status_code >= 400:
        raise ContextWriterError(f"Error {resp.status_code} en {method} {url}: {resp.text}")
    return resp.json() if resp.text.strip() else {}


def normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def get_schema() -> Dict[str, Any]:
    return request_json("GET", f"/meta/bases/{BASE_ID}/tables")


def get_field_choices(table_name: str, field_name: str) -> List[str]:
    schema = get_schema()
    for table in schema.get("tables", []):
        if table.get("name") == table_name:
            for field in table.get("fields", []):
                if field.get("name") == field_name:
                    choices = field.get("options", {}).get("choices", [])
                    return [choice.get("name") for choice in choices]
    return []


def resolve_choice(table_name: str, field_name: str, raw_value: str, aliases: Dict[str, List[str]]) -> str:
    existing = get_field_choices(table_name, field_name)
    if not existing:
        return raw_value

    raw_norm = normalize(raw_value)
    for choice in existing:
        if normalize(choice) == raw_norm:
            return choice

    for alias in aliases.get(raw_value.lower(), []):
        alias_norm = normalize(alias)
        for choice in existing:
            if normalize(choice) == alias_norm:
                return choice

    alias_list = aliases.get(raw_value.lower()) or [raw_value]
    return alias_list[0]


def read_content(args: argparse.Namespace) -> str:
    if args.content_file:
        return Path(args.content_file).read_text(encoding="utf-8")
    if args.content:
        return args.content
    data = sys.stdin.read()
    if data.strip():
        return data
    raise ContextWriterError("Debes enviar contenido con --content-file, --content o stdin")


def airtable_get_records(table_name: str, formula: Optional[str] = None, fields: Optional[List[str]] = None, sort: Optional[List[Dict[str, str]]] = None, max_records: int = 100) -> List[Dict[str, Any]]:
    params: Dict[str, Any] = {"maxRecords": max_records}
    if formula:
        params["filterByFormula"] = formula
    if sort:
        for idx, s in enumerate(sort):
            params[f"sort[{idx}][field]"] = s["field"]
            params[f"sort[{idx}][direction]"] = s.get("direction", "asc")
    if fields:
        for idx, field in enumerate(fields):
            params[f"fields[{idx}]"] = field
    data = request_json("GET", f"/{BASE_ID}/{quote(table_name)}", params=params)
    return data.get("records", [])


def airtable_create_records(table_name: str, records: List[Dict[str, Any]], typecast: bool = True) -> Dict[str, Any]:
    payload = {"records": records, "typecast": typecast}
    return request_json("POST", f"/{BASE_ID}/{quote(table_name)}", payload=payload)


def airtable_update_record(table_name: str, record_id: str, fields: Dict[str, Any], typecast: bool = True) -> Dict[str, Any]:
    payload = {"fields": fields, "typecast": typecast}
    return request_json("PATCH", f"/{BASE_ID}/{quote(table_name)}/{record_id}", payload=payload)


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip()).strip("-")
    return value.lower() or "item"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def latest_version(project: str, context_type: str) -> int:
    formula = f"AND({{Project}}='{project}', {{Context Type}}='{context_type}')"
    records = airtable_get_records(
        APPROVED_TABLE,
        formula=formula,
        fields=["Version"],
        sort=[{"field": "Version", "direction": "desc"}],
        max_records=100,
    )
    versions = [r.get("fields", {}).get("Version", 0) for r in records if isinstance(r.get("fields", {}).get("Version", 0), (int, float))]
    return int(max(versions)) if versions else 0


def supersede_existing(project: str, context_type: str) -> List[str]:
    formula = f"AND({{Project}}='{project}', {{Context Type}}='{context_type}', {{Status}}='Active')"
    records = airtable_get_records(APPROVED_TABLE, formula=formula, fields=["Status"], max_records=100)
    updated = []
    for record in records:
        airtable_update_record(APPROVED_TABLE, record["id"], {"Status": "Superseded"})
        updated.append(record["id"])
    return updated


def cmd_publish(args: argparse.Namespace) -> None:
    require_env()
    content = read_content(args)
    context_type = resolve_choice(APPROVED_TABLE, "Context Type", args.context_type, TYPE_ALIASES)
    next_version = latest_version(args.project, context_type) + 1
    superseded = supersede_existing(args.project, context_type)

    title = args.title or f"{context_type} v{next_version}"
    context_id = f"ctx-{slugify(args.project)}-{slugify(context_type)}-v{next_version}"
    fields = {
        "Context ID": context_id,
        "Project": args.project,
        "Context Type": context_type,
        "Title": title,
        "Approved Content": content,
        "Version": next_version,
        "Status": "Active",
        "Source References": args.source_refs or "",
        "Approved By": args.approved_by or "Jaime",
        "Approved At": now_iso(),
    }
    created = airtable_create_records(APPROVED_TABLE, [{"fields": fields}], typecast=True)

    if args.sync_file:
        sync_path = Path(args.sync_file)
        sync_path.parent.mkdir(parents=True, exist_ok=True)
        sync_path.write_text(content, encoding="utf-8")

    print(json.dumps({
        "action": "publish",
        "project": args.project,
        "context_type": context_type,
        "version": next_version,
        "superseded_record_ids": superseded,
        "created_record": created.get("records", [{}])[0],
        "synced_file": args.sync_file or None,
    }, ensure_ascii=False, indent=2))


def cmd_draft(args: argparse.Namespace) -> None:
    require_env()
    content = read_content(args)
    draft_type = resolve_choice(DRAFT_TABLE, "Draft Type", args.draft_type, DRAFT_TYPE_ALIASES)
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    draft_id = f"draft-{slugify(args.project)}-{slugify(draft_type)}-{ts}"
    fields = {
        "Draft ID": draft_id,
        "Project": args.project,
        "Meeting ID": args.meeting_id or "",
        "Draft Type": draft_type,
        "Title": args.title or draft_id,
        "Content": content,
        "Status": args.status or "Draft",
    }
    if args.version_hint is not None:
        fields["Version Hint"] = args.version_hint
    created = airtable_create_records(DRAFT_TABLE, [{"fields": fields}], typecast=True)
    print(json.dumps({
        "action": "draft",
        "project": args.project,
        "draft_type": draft_type,
        "created_record": created.get("records", [{}])[0],
    }, ensure_ascii=False, indent=2))


def cmd_show_active(args: argparse.Namespace) -> None:
    require_env()
    context_type = resolve_choice(APPROVED_TABLE, "Context Type", args.context_type, TYPE_ALIASES)
    formula = f"AND({{Project}}='{args.project}', {{Context Type}}='{context_type}', {{Status}}='Active')"
    records = airtable_get_records(
        APPROVED_TABLE,
        formula=formula,
        sort=[{"field": "Version", "direction": "desc"}],
        max_records=5,
    )
    print(json.dumps({
        "action": "show_active",
        "project": args.project,
        "context_type": context_type,
        "records": records,
    }, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Escritor de contexto oficial y borradores para el PM Operating System")
    sub = parser.add_subparsers(dest="command", required=True)

    pub = sub.add_parser("publish", help="Publica una nueva versión oficial en Approved_Context")
    pub.add_argument("--project", required=True)
    pub.add_argument("--context-type", required=True)
    pub.add_argument("--title")
    pub.add_argument("--content-file")
    pub.add_argument("--content")
    pub.add_argument("--approved-by")
    pub.add_argument("--source-refs")
    pub.add_argument("--sync-file", help="Ruta local a sincronizar con la versión vigente")
    pub.set_defaults(func=cmd_publish)

    dr = sub.add_parser("draft", help="Crea un borrador en Draft_Insights")
    dr.add_argument("--project", required=True)
    dr.add_argument("--draft-type", required=True)
    dr.add_argument("--meeting-id")
    dr.add_argument("--title")
    dr.add_argument("--content-file")
    dr.add_argument("--content")
    dr.add_argument("--status", default="Draft")
    dr.add_argument("--version-hint", type=int)
    dr.set_defaults(func=cmd_draft)

    show = sub.add_parser("show-active", help="Muestra la versión activa de un contexto")
    show.add_argument("--project", required=True)
    show.add_argument("--context-type", required=True)
    show.set_defaults(func=cmd_show_active)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except ContextWriterError as exc:
        raise SystemExit(str(exc))
