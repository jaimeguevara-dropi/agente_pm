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
TABLE_NAME = "User_Stories"
PROJECT = "SILIN - Procesamiento inteligente FT"
MD_PATH = ROOT / "canon" / "user_stories_silin_procesamiento_ft.md"

STORIES: List[Dict[str, Any]] = [
    {
        "Order": "1",
        "Story ID": "US-FT-001-001",
        "Original Key": "52716 / BRAI-174",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-001",
        "Capability Name": "Recepción de Lotes FT",
        "Source Epic": "52716",
        "Title": "Recepción de archivos mayores a 6MB",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema de procesamiento de información, quiero recibir y gestionar lotes de datos superiores a 6MB, para permitir la carga completa de información sin restricciones de tamaño que afecten la operación.",
        "Acceptance Criteria": "Debe aceptar archivos mayores a 6MB, procesar la totalidad del lote sin pérdida de información, manejar errores de estructura o contenido sin caída del sistema, mantener estabilidad ante múltiples lotes grandes y confirmar recepción con trazabilidad.",
        "Notes": "Se mantiene dentro de CAP-FT-001 porque habilita la recepción técnica de lotes grandes.",
    },
    {
        "Order": "2",
        "Story ID": "US-FT-001-002",
        "Original Key": "52716",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-001",
        "Capability Name": "Recepción de Lotes FT",
        "Source Epic": "52716",
        "Title": "Recepción de archivos FT vía endpoint desde Plataforma SILIN",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero exponer un endpoint técnico seguro para que Plataforma SILIN envíe archivos FT recibidos desde el portal, para encapsularlos como lote FT y registrarlos en el pipeline con trazabilidad desde el origen.",
        "Acceptance Criteria": "Debe recibir archivo y metadatos mínimos; crear lote único; asignar identificador; registrar canal API_SILIN; marcar estado RECIBIDO; persistir entidad, periodo, comercializadora y tipo FT; no ejecutar validaciones estructurales, funcionales ni tributarias en esta etapa.",
        "Notes": "Esta HU reemplaza a la recepción genérica desde canales habilitados.",
    },
    {
        "Order": "3",
        "Story ID": "US-FT-001-003",
        "Original Key": "52716",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-001",
        "Capability Name": "Recepción de Lotes FT",
        "Source Epic": "52716",
        "Title": "Identificación única del lote FT",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero asignar un identificador único a cada lote recibido, para permitir trazabilidad, reprocesamiento y seguimiento del ciclo de vida del lote.",
        "Acceptance Criteria": "Debe generar identificador único al crear el lote; persistirlo en todo el flujo; permitir asociar reprocesos al lote original; agregar etiquetas operativas sin alterar la identidad del lote.",
        "Notes": "El identificador del lote debe ser inmutable.",
    },
    {
        "Order": "4",
        "Story ID": "US-FT-001-004",
        "Original Key": "52716",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-001",
        "Capability Name": "Recepción de Lotes FT",
        "Source Epic": "52716",
        "Title": "Asociación del lote a contexto tributario",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero asociar cada lote a comercializadora, entidad y periodo tributario, para asegurar coherencia del procesamiento posterior con el contexto normativo.",
        "Acceptance Criteria": "Debe asociar comercializadora, entidad y periodo cuando la información exista; si falta información mínima, el lote no debe avanzar a validación y debe quedar registrado como inconsistente.",
        "Notes": "Aunque menciona contexto tributario, aquí no se ejecutan validaciones tributarias profundas.",
    },
    {
        "Order": "5",
        "Story ID": "US-FT-001-005",
        "Original Key": "52716",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-001",
        "Capability Name": "Recepción de Lotes FT",
        "Source Epic": "52716",
        "Title": "Recepción de archivo FT desde canales habilitados",
        "Type": "User Story",
        "Status": "Merged",
        "Scope Treatment": "Merged into US-FT-001-002",
        "Description": "Como sistema SILIN, quiero recibir archivos FT desde canales habilitados para iniciar el proceso de gestión del lote de forma automatizada y trazable.",
        "Acceptance Criteria": "Recepción por canal habilitado, almacenamiento en repositorio, creación de lote en estado Recibido y registro de fecha/canal. Si el canal no está habilitado, no aceptar y registrar intento fallido.",
        "Notes": "Se conserva como referencia, pero se absorbe en la HU más específica de endpoint desde Plataforma SILIN.",
    },
    {
        "Order": "6",
        "Story ID": "US-FT-001-006",
        "Original Key": "52716",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-001",
        "Capability Name": "Recepción de Lotes FT",
        "Source Epic": "52716",
        "Title": "Notificación de recepción del lote",
        "Type": "User Story",
        "Status": "Scope Review",
        "Scope Treatment": "Out of current capability scope",
        "Description": "Como comercializadora y stakeholders internos, quiero ser notificado cuando un lote FT es recibido, para tener confirmación temprana del inicio del procesamiento.",
        "Acceptance Criteria": "Al recibir un archivo, el sistema debe emitir notificación con identificador de lote, entidad y periodo. Si falla la notificación, el fallo debe registrarse sin afectar el estado del lote.",
        "Notes": "Requiere decisión de alcance: canal, destinatarios y si se permite notificación automática dentro de esta fase.",
    },
    {
        "Order": "7",
        "Story ID": "US-FT-002-001",
        "Original Key": "52717",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-002",
        "Capability Name": "Validación estructural y funcional de archivo",
        "Source Epic": "52717",
        "Title": "Validación estructural del archivo FT",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero validar la estructura mínima del archivo FT, para detectar errores tempranos y evitar reprocesos costosos.",
        "Acceptance Criteria": "Debe verificar número esperado de columnas, orden de columnas y formato general. Si la estructura es válida, marcar como estructuralmente válido. Si es inválida, marcar el lote como estructuralmente inválido y registrar motivo de falla a nivel de lote.",
        "Notes": "No valida datos por registro.",
    },
    {
        "Order": "8",
        "Story ID": "US-FT-002-002",
        "Original Key": "52717",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-002",
        "Capability Name": "Validación estructural y funcional de archivo",
        "Source Epic": "52717",
        "Title": "Validación funcional por registro",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero validar cada registro del lote de forma independiente, para eliminar el bloqueo todo o nada del archivo FT.",
        "Acceptance Criteria": "Para un lote estructuralmente válido, cada registro debe evaluarse contra reglas funcionales definidas. Si cumple, se clasifica como válido. Si no cumple, se clasifica como inválido y se registra motivo.",
        "Notes": "Las reglas provienen de anexo técnico, reglas históricas y validaciones existentes documentadas.",
    },
    {
        "Order": "9",
        "Story ID": "US-FT-002-003",
        "Original Key": "52717",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-002",
        "Capability Name": "Validación estructural y funcional de archivo",
        "Source Epic": "52717",
        "Title": "Clasificación de registros del lote",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero clasificar los registros del lote según su resultado de validación, para permitir procesamiento parcial en fases posteriores.",
        "Acceptance Criteria": "Al finalizar la validación funcional, los registros deben quedar clasificados como válidos o inválidos. La clasificación debe persistirse y la coexistencia de registros válidos e inválidos no debe bloquear el flujo.",
        "Notes": "Esta HU soporta directamente el procesamiento parcial.",
    },
    {
        "Order": "10",
        "Story ID": "US-FT-002-004",
        "Original Key": "52717",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-002",
        "Capability Name": "Validación estructural y funcional de archivo",
        "Source Epic": "52717",
        "Title": "Persistencia de resultados de validación",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero persistir el resultado de validación de cada registro, para permitir reprocesos, auditoría y trazabilidad.",
        "Acceptance Criteria": "Cuando un registro sea validado, el sistema debe persistir el estado del registro y el motivo del resultado.",
        "Notes": "Base para consulta, análisis y revalidación futura.",
    },
    {
        "Order": "11",
        "Story ID": "US-FT-002-005",
        "Original Key": "52717",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-002",
        "Capability Name": "Validación estructural y funcional de archivo",
        "Source Epic": "52717",
        "Title": "Consolidado de resultados a nivel de lote",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como equipo tributario y de producto, quiero ver un resumen del resultado de validación del lote, para entender rápidamente su estado sin revisar registros uno a uno.",
        "Acceptance Criteria": "Cuando todos los registros sean validados, el sistema debe mostrar total de registros, cantidad de válidos y cantidad de inválidos.",
        "Notes": "Vista resumen técnica, no dashboard avanzado.",
    },
    {
        "Order": "12",
        "Story ID": "US-FT-002-006",
        "Original Key": "52717",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-002",
        "Capability Name": "Validación estructural y funcional de archivo",
        "Source Epic": "52717",
        "Title": "Análisis y consolidación de validaciones funcionales existentes",
        "Type": "Spike",
        "Status": "Active",
        "Scope Treatment": "Accepted as Spike",
        "Description": "Como sistema/equipo, quiero analizar, documentar y consolidar las validaciones funcionales existentes sobre archivos FT, para definir la estructura definitiva de reglas y preparar la migración hacia validación por registro.",
        "Acceptance Criteria": "Debe revisar código existente, identificar validaciones implícitas, duplicadas y acopladas al flujo todo o nada; analizar fuentes de reglas y documentar brechas.",
        "Notes": "Se carga como Spike porque es trabajo de descubrimiento técnico, no funcionalidad productiva directa.",
    },
    {
        "Order": "13",
        "Story ID": "US-FT-003-001",
        "Original Key": "52721",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-003",
        "Capability Name": "Gestión de registros inválidos",
        "Source Epic": "52721",
        "Title": "Mantener estado de registros inválidos",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero mantener el estado de cada registro inválido del lote FT, para permitir control operativo y trazabilidad básica sin bloquear el procesamiento parcial.",
        "Acceptance Criteria": "Un registro inválido debe quedar en estado PENDIENTE_DE_CORRECCIÓN, conservar lote origen y periodo, no bloquear válidos y no incluirse en archivos generados.",
        "Notes": "La gestión posterior ocurre por soporte/procesos externos, según alcance actual.",
    },
    {
        "Order": "14",
        "Story ID": "US-FT-003-002",
        "Original Key": "52721",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-003",
        "Capability Name": "Gestión de registros inválidos",
        "Source Epic": "52721",
        "Title": "Asociación de error por registro inválido",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero asociar a cada registro inválido el error específico que lo originó, para facilitar corrección y soporte operativo.",
        "Acceptance Criteria": "Cada registro inválido debe asociar código de error, descripción funcional y fecha de detección. La información debe mantenerse al consultarse posteriormente.",
        "Notes": "No implica corrección automática.",
    },
    {
        "Order": "15",
        "Story ID": "US-FT-003-003",
        "Original Key": "52721",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-003",
        "Capability Name": "Gestión de registros inválidos",
        "Source Epic": "52721",
        "Title": "Consulta de registros inválidos por lote",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como usuario de soporte, quiero consultar registros inválidos asociados a un lote FT, para facilitar control operativo y análisis de errores sin afectar el procesamiento.",
        "Acceptance Criteria": "Debe retornar registros inválidos del lote con estado y error asociado. La consulta no debe modificar estados, disparar reprocesos ni afectar el flujo.",
        "Notes": "Consulta informativa interna.",
    },
    {
        "Order": "16",
        "Story ID": "US-FT-003-004",
        "Original Key": "52721",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-003",
        "Capability Name": "Gestión de registros inválidos",
        "Source Epic": "52721",
        "Title": "No bloqueo del procesamiento parcial",
        "Type": "User Story",
        "Status": "Merged",
        "Scope Treatment": "Merged into US-FT-002-003 and US-FT-004-001",
        "Description": "Como sistema, quiero permitir procesamiento y dispersión de registros válidos aunque existan registros inválidos en el mismo lote.",
        "Acceptance Criteria": "Solo registros válidos deben procesarse y los inválidos no deben bloquear el proceso ni alterar su estado.",
        "Notes": "Comportamiento transversal ya cubierto por clasificación de registros y disponibilización de subconjunto válido.",
    },
    {
        "Order": "17",
        "Story ID": "US-FT-004-001",
        "Original Key": "52719",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-004",
        "Capability Name": "Disponibilización de registros válidos del lote FT para dispersión en SILIN",
        "Source Epic": "52719",
        "Title": "Identificación del subconjunto válido del lote",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero seleccionar automáticamente los registros marcados como válidos en un lote, para procesarlos sin depender de los inválidos.",
        "Acceptance Criteria": "Debe identificar subconjunto válido, excluir inválidos de disponibilización y marcar todos como aptos cuando el lote sea completamente válido.",
        "Notes": "Base de la disponibilización parcial.",
    },
    {
        "Order": "18",
        "Story ID": "US-FT-004-002",
        "Original Key": "52719",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-004",
        "Capability Name": "Disponibilización de registros válidos del lote FT para dispersión en SILIN",
        "Source Epic": "52719",
        "Title": "Generación de archivos FT para disponibilización FT-01 / FT-06",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero depositar y dejar disponibles archivos FT validados en repositorio controlado para que Plataforma SILIN ejecute la dispersión.",
        "Acceptance Criteria": "Debe depositar archivos en repositorio, registrar ruta/fecha/versión, mantener inmutabilidad, generar FT-01 y FT-06 independientes cuando aplique, permitir disponibilización parcial y prevenir duplicidad automática.",
        "Notes": "El sistema no ejecuta dispersión.",
    },
    {
        "Order": "19",
        "Story ID": "US-FT-004-003",
        "Original Key": "52719",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-004",
        "Capability Name": "Disponibilización de registros válidos del lote FT para dispersión en SILIN",
        "Source Epic": "52719",
        "Title": "Etiquetado e identificación de archivos disponibilizados",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero etiquetar cada archivo FT generado con identificadores múltiples, para garantizar trazabilidad y consumo controlado por SILIN.",
        "Acceptance Criteria": "Cada archivo generado debe asociar entidad, periodo tributario, lote origen, tipo de FT y fecha de generación.",
        "Notes": "Aplica a FT-01 y FT-06.",
    },
    {
        "Order": "20",
        "Story ID": "US-FT-004-004",
        "Original Key": "52719",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-004",
        "Capability Name": "Disponibilización de registros válidos del lote FT para dispersión en SILIN",
        "Source Epic": "52719",
        "Title": "Gestión de estado del lote por disponibilización",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero mantener un estado claro del lote según su nivel de disponibilización, para reflejar correctamente el avance del proceso.",
        "Acceptance Criteria": "Debe marcar DISPONIBILIZADO si todos los registros válidos fueron disponibilizados y DISPONIBILIZADO_PARCIALMENTE si existen inválidos excluidos.",
        "Notes": "Se relaciona con CAP-FT-007, pero aquí se conserva por evento específico de disponibilización.",
    },
    {
        "Order": "21",
        "Story ID": "US-FT-004-005",
        "Original Key": "52719",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-004",
        "Capability Name": "Disponibilización de registros válidos del lote FT para dispersión en SILIN",
        "Source Epic": "52719",
        "Title": "Gestión de reprocesos de archivos FT por incidencias reportadas por SILIN",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted with scope clarification",
        "Description": "Como sistema, quiero permitir gestión controlada de reprocesos de archivos FT a partir de incidencias reportadas por Plataforma SILIN mediante ticket.",
        "Acceptance Criteria": "Debe registrar incidencia externa asociada a lote/archivo; marcar INCIDENCIA_REPORTADA; permitir reproceso solo con autorización manual; regenerar y redisponibilizar conservando referencia al lote y versión anterior; bloquear reprocesos no autorizados.",
        "Notes": "Aclaración: no hay feedback automático de SILIN ni detección automática de errores de dispersión.",
    },
    {
        "Order": "22",
        "Story ID": "US-FT-004-006",
        "Original Key": "52719",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-004",
        "Capability Name": "Disponibilización de registros válidos del lote FT para dispersión en SILIN",
        "Source Epic": "52719",
        "Title": "Prevención de reprocesamiento y duplicidad",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero evitar la regeneración automática de archivos FT ya disponibilizados, para prevenir duplicidades y errores operativos.",
        "Acceptance Criteria": "Si un archivo ya fue disponibilizado, una solicitud de reproceso debe bloquear regeneración automática y requerir acción explícita de soporte.",
        "Notes": "Refuerza inmutabilidad y control de reproceso.",
    },
    {
        "Order": "23",
        "Story ID": "US-FT-005-001",
        "Original Key": "52722 / BRAI-45",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-005",
        "Capability Name": "Revalidación incremental de registros inválidos",
        "Source Epic": "52722",
        "Title": "Recepción de registros corregidos",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero recibir registros corregidos por los mismos canales de ingreso, para no crear flujos paralelos ni excepciones técnicas.",
        "Acceptance Criteria": "Debe aceptar registros corregidos por canales existentes y marcarlos como REPROCESO.",
        "Notes": "Mantiene un solo canal operativo.",
    },
    {
        "Order": "24",
        "Story ID": "US-FT-005-002",
        "Original Key": "52722",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-005",
        "Capability Name": "Revalidación incremental de registros inválidos",
        "Source Epic": "52722",
        "Title": "Identificación de reproceso y asociación al lote original",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero identificar que un registro corresponde a un reproceso, para asociarlo correctamente al lote original.",
        "Acceptance Criteria": "Un registro con estado previo PENDIENTE_DE_CORRECCIÓN debe asociarse al mismo lote original y conservar referencia al registro original.",
        "Notes": "No implica versionado complejo.",
    },
    {
        "Order": "25",
        "Story ID": "US-FT-005-003",
        "Original Key": "52722 / BRAI-47",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-005",
        "Capability Name": "Revalidación incremental de registros inválidos",
        "Source Epic": "52722",
        "Title": "Revalidación incremental del registro corregido",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero revalidar únicamente el registro corregido, para evitar reprocesos masivos innecesarios.",
        "Acceptance Criteria": "Debe aplicar validación estructural y funcional solo al registro marcado como REPROCESO, sin revalidar otros registros del lote.",
        "Notes": "Clave para romper reproceso masivo.",
    },
    {
        "Order": "26",
        "Story ID": "US-FT-005-004",
        "Original Key": "52722 / BRAI-48",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-005",
        "Capability Name": "Revalidación incremental de registros inválidos",
        "Source Epic": "52722",
        "Title": "Actualización del estado del registro corregido",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero actualizar el estado del registro corregido según el resultado, para reflejar correctamente su condición actual.",
        "Acceptance Criteria": "Si cumple validaciones, actualizar a VÁLIDO. Si no cumple, mantener PENDIENTE_DE_CORRECCIÓN y actualizar motivo de error.",
        "Notes": "El estado INVÁLIDO se conserva operativamente como pendiente de corrección.",
    },
    {
        "Order": "27",
        "Story ID": "US-FT-005-005",
        "Original Key": "52722 / BRAI-49",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-005",
        "Capability Name": "Revalidación incremental de registros inválidos",
        "Source Epic": "52722",
        "Title": "Incorporación automática al flujo de procesamiento",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero incorporar automáticamente los registros corregidos y válidos, para que continúen el flujo normal sin intervención humana.",
        "Acceptance Criteria": "Un registro corregido con estado VÁLIDO debe incorporarse al proceso de dispersión sin aprobación manual.",
        "Notes": "Debe respetar las reglas de disponibilización vigentes.",
    },
    {
        "Order": "28",
        "Story ID": "US-FT-005-006",
        "Original Key": "52722 / BRAI-50",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-005",
        "Capability Name": "Revalidación incremental de registros inválidos",
        "Source Epic": "52722",
        "Title": "Actualización del estado agregado del lote",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero actualizar el estado del lote cuando se corrigen registros, para reflejar su avance real.",
        "Acceptance Criteria": "Si un lote estaba PROCESADO_PARCIALMENTE y todos los inválidos fueron corregidos y validados, el lote debe actualizar su estado a PROCESADO.",
        "Notes": "El nombre del estado debe alinearse con los estados normalizados finales.",
    },
    {
        "Order": "29",
        "Story ID": "US-FT-005-007",
        "Original Key": "52722 / BRAI-51",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-005",
        "Capability Name": "Revalidación incremental de registros inválidos",
        "Source Epic": "52722",
        "Title": "Trazabilidad entre versiones del registro",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como equipo interno, quiero mantener trazabilidad entre el registro original y su corrección, para auditoría y control operativo.",
        "Acceptance Criteria": "Debe conservar referencia al registro original, fecha y resultado del reproceso.",
        "Notes": "No implica versionado complejo completo.",
    },
    {
        "Order": "30",
        "Story ID": "US-FT-005-008",
        "Original Key": "52722",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-005",
        "Capability Name": "Revalidación incremental de registros inválidos",
        "Source Epic": "52722",
        "Title": "Protección contra reprocesos indebidos",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero evitar reprocesar registros que ya fueron corregidos y procesados, para no duplicar efectos.",
        "Acceptance Criteria": "Si un registro tiene estado PROCESADO y se intenta reprocesar nuevamente, el sistema debe rechazar el reproceso y registrar el intento.",
        "Notes": "Control anti-duplicidad a nivel de registro.",
    },
    {
        "Order": "31",
        "Story ID": "US-FT-006-001",
        "Original Key": "52718",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Identificación de registros inválidos candidatos a rescate",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero identificar claramente los registros inválidos de un lote, para aplicar procesos de rescate sin afectar los registros válidos.",
        "Acceptance Criteria": "Debe identificar el conjunto de registros inválidos y mantener el motivo de invalidación de cada uno.",
        "Notes": "Se conserva como entrada al proceso de rescate.",
    },
    {
        "Order": "32",
        "Story ID": "US-FT-006-002",
        "Original Key": "52718 / BRAI-18",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Spike - Rescate: análisis y conexión con SILIN",
        "Type": "Spike",
        "Status": "Needs Review",
        "Scope Treatment": "Spike / possible duplicate with US-FT-002-006",
        "Description": "Analizar y documentar validaciones funcionales existentes sobre archivos FT para preparar reglas y brechas de rescate.",
        "Acceptance Criteria": "Debe revisar código existente, validaciones estructurales y funcionales, reglas históricas y fuentes documentales.",
        "Notes": "Contenido cercano al spike de validaciones existentes. Requiere decidir si se fusiona o si se mantiene por foco específico en rescate.",
    },
    {
        "Order": "33",
        "Story ID": "US-FT-006-003",
        "Original Key": "52718 / BRAI-21",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Intento de rescate de registros inválidos",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero intentar rescatar registros inválidos usando información histórica, para reducir reprocesos y devoluciones a la comercializadora.",
        "Acceptance Criteria": "Si existe información histórica suficiente, reconstruir el registro y cambiar estado a válido. Si no existe información suficiente, mantenerlo como inválido.",
        "Notes": "Debe apoyarse en llaves de búsqueda definidas.",
    },
    {
        "Order": "34",
        "Story ID": "US-FT-006-004",
        "Original Key": "52718 / BRAI-20",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Identificación de registros inválidos del lote",
        "Type": "User Story",
        "Status": "Merged",
        "Scope Treatment": "Merged into US-FT-006-001",
        "Description": "Como sistema, quiero identificar claramente los registros inválidos de un lote para aplicar procesos de rescate.",
        "Acceptance Criteria": "Identificar inválidos y mantener motivo de invalidación.",
        "Notes": "Duplicada con US-FT-006-001.",
    },
    {
        "Order": "35",
        "Story ID": "US-FT-006-005",
        "Original Key": "52718 / BRAI-22",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Uso de llaves de búsqueda para rescate",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero utilizar llaves de búsqueda definidas para el rescate, para aplicar criterios consistentes y auditables.",
        "Acceptance Criteria": "Debe usar ID de medidor como llave principal. Si un contribuyente tiene múltiples medidores, debe permitir múltiples coincidencias válidas y no asumir unicidad por contribuyente.",
        "Notes": "Hipótesis funcional explícita del TO-BE.",
    },
    {
        "Order": "36",
        "Story ID": "US-FT-006-006",
        "Original Key": "52718",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Mantener actualizado el estado del resultado del rescate",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero mantener actualizado el resultado del proceso de rescate, para evitar reprocesos repetidos y permitir trazabilidad.",
        "Acceptance Criteria": "Si el rescate es exitoso, actualizar estado a válido y registrar origen. Si falla, mantener inválido y registrar intento fallido.",
        "Notes": "Separa resultado exitoso y fallido.",
    },
    {
        "Order": "37",
        "Story ID": "US-FT-006-007",
        "Original Key": "52718 / BRAI-24",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Determinación de rechazo definitivo",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero marcar como rechazados los registros que no pudieron ser rescatados, para activar el proceso formal de notificación a interesados.",
        "Acceptance Criteria": "Si un registro inválido tuvo rescate fallido, debe marcarse como rechazado y asociarse motivo de rechazo.",
        "Notes": "No implica decisión tributaria legal.",
    },
    {
        "Order": "38",
        "Story ID": "US-FT-006-008",
        "Original Key": "52718",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Resumen del rescate previo a notificación",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Title adjusted",
        "Description": "Como equipo tributario y de producto, quiero ver un resumen del rescate aplicado al lote, para entender qué tanto se logró recuperar antes de notificar.",
        "Acceptance Criteria": "Debe mostrar número de registros rescatados y número de registros irrecuperables.",
        "Notes": "Se ajustó el título original porque el contenido hablaba de resumen, no de notificación directa a comercializadora.",
    },
    {
        "Order": "39",
        "Story ID": "US-FT-006-009",
        "Original Key": "52718",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Notificación de registros rechazados a interesados internos",
        "Type": "User Story",
        "Status": "Scope Review",
        "Scope Treatment": "Notification channel undefined",
        "Description": "Como actor interno interesado, quiero recibir visibilidad de los rechazos del lote, para dar seguimiento y soporte al proceso.",
        "Acceptance Criteria": "Debe notificar a interesados internos al finalizar rescate, indicar estado final del lote y número de registros rechazados.",
        "Notes": "Canal y destinatarios quedan pendientes de definición.",
    },
    {
        "Order": "40",
        "Story ID": "US-FT-006-010",
        "Original Key": "52718 / BRAI-27",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-006",
        "Capability Name": "Gestión, rescate y notificación de registros rechazados",
        "Source Epic": "52718",
        "Title": "Consolidado final del lote tras notificación",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como equipo de producto y tributario, quiero ver el estado final del lote tras las notificaciones, para confirmar el cierre correcto del proceso.",
        "Acceptance Criteria": "Luego de notificar rechazados, el lote debe reflejar registros válidos y rechazados, sin quedar en estado intermedio.",
        "Notes": "Cierre operativo del ciclo de error.",
    },
    {
        "Order": "41",
        "Story ID": "US-FT-007-001",
        "Original Key": "52723",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-007",
        "Capability Name": "Estados y trazabilidad transversal del procesamiento FT",
        "Source Epic": "52723",
        "Title": "Estados normalizados del lote FT",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero mantener un estado único y consistente del lote FT, para reflejar claramente su avance dentro del pipeline.",
        "Acceptance Criteria": "El estado debe actualizarse según evento ocurrido y ser único y consultable. Estados mínimos: RECIBIDO, VALIDADO, DISPONIBILIZADO, DISPONIBILIZADO_PARCIALMENTE, PROCESADO, PROCESADO_PARCIALMENTE, ERROR.",
        "Notes": "Debe alinear nombres con estados usados en otras HUs.",
    },
    {
        "Order": "42",
        "Story ID": "US-FT-007-002",
        "Original Key": "52723",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-007",
        "Capability Name": "Estados y trazabilidad transversal del procesamiento FT",
        "Source Epic": "52723",
        "Title": "Estados a nivel de registro individual",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero mantener el estado individual de cada registro del lote, para permitir trazabilidad granular sin reprocesos manuales.",
        "Acceptance Criteria": "Cada registro del lote debe tener su propio estado independiente.",
        "Notes": "Soporta gestión de válidos, inválidos, excluidos, reprocesados y rechazados.",
    },
    {
        "Order": "43",
        "Story ID": "US-FT-007-003",
        "Original Key": "52723",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-007",
        "Capability Name": "Estados y trazabilidad transversal del procesamiento FT",
        "Source Epic": "52723",
        "Title": "Disponibilización vía API para interesados internos",
        "Type": "User Story",
        "Status": "Active",
        "Scope Treatment": "Accepted",
        "Description": "Como sistema, quiero disponibilizar la información de estados y trazabilidad vía API, para que otros sistemas o equipos la consuman.",
        "Acceptance Criteria": "Un sistema autorizado debe poder consultar estado actual del lote y estados agregados de sus registros.",
        "Notes": "API interna, no contractual, alineada a consulta técnica.",
    },
    {
        "Order": "44",
        "Story ID": "US-FT-007-004",
        "Original Key": "52716",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-007",
        "Capability Name": "Estados y trazabilidad transversal del procesamiento FT",
        "Source Epic": "52716",
        "Title": "Visualización operativa de estados de lotes FT mediante Grafana",
        "Type": "User Story",
        "Status": "Scope Review",
        "Scope Treatment": "Moved from CAP-FT-001; dashboard excluded from current capability",
        "Description": "Como usuario interno, quiero una vista operativa en Grafana para consultar el estado de los lotes FT en tiempo casi real sin acceder a base de datos.",
        "Acceptance Criteria": "Debe visualizar lista de lotes, estado actual, fecha de recepción y canal de entrada; permitir filtros por entidad, periodo, comercializadora y estado; ser solo lectura.",
        "Notes": "Se movió a CAP-FT-007 por naturaleza de trazabilidad, pero queda en revisión porque dashboards gráficos están excluidos del alcance actual.",
    },
    {
        "Order": "45",
        "Story ID": "US-FT-007-005",
        "Original Key": "52716",
        "Project": PROJECT,
        "Capability ID": "CAP-FT-007",
        "Capability Name": "Estados y trazabilidad transversal del procesamiento FT",
        "Source Epic": "52716",
        "Title": "Gestión inicial de estados del lote",
        "Type": "User Story",
        "Status": "Merged",
        "Scope Treatment": "Merged into US-FT-007-001",
        "Description": "Como equipo operativo y tributario, quiero visualizar el estado básico del lote desde su recepción, para entender claramente en qué punto del proceso se encuentra.",
        "Acceptance Criteria": "El lote debe iniciar en estado Recibido y actualizar estado automáticamente conservando historial.",
        "Notes": "Se absorbe en estados normalizados del lote FT.",
    },
]

REQUIRED_FIELDS = {
    "Story ID": "singleLineText",
    "Original Key": "singleLineText",
    "Project": "singleLineText",
    "Capability ID": "singleLineText",
    "Capability Name": "singleLineText",
    "Source Epic": "singleLineText",
    "Title": "singleLineText",
    "Type": "singleLineText",
    "Status": "singleLineText",
    "Scope Treatment": "singleLineText",
    "Description": "multilineText",
    "Acceptance Criteria": "multilineText",
    "Notes": "multilineText",
    "Order": "singleLineText",
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


def find_record(story_id: str) -> str | None:
    params = {
        "filterByFormula": f"{{Story ID}}='{story_id}'",
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


def write_markdown() -> None:
    MD_PATH.parent.mkdir(parents=True, exist_ok=True)

    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for story in STORIES:
        grouped.setdefault(story["Capability ID"], []).append(story)

    lines: List[str] = []
    lines.append("# User Stories - SILIN - Procesamiento inteligente FT\n")
    lines.append("## Proyecto\n")
    lines.append(f"{PROJECT}\n")
    lines.append("## Propósito\n")
    lines.append("Este documento consolida las historias de usuario normalizadas del proyecto, alineadas a las capacidades / épicas aprobadas. Incluye HUs activas, HUs fusionadas por duplicidad y elementos en revisión de alcance.\n")
    lines.append("## Criterio de normalización\n")
    lines.append("- `Active`: historia alineada al alcance vigente.\n")
    lines.append("- `Merged`: historia duplicada o absorbida por otra HU más completa.\n")
    lines.append("- `Scope Review`: historia útil, pero pendiente de decisión de alcance.\n")
    lines.append("- `Needs Review`: requiere validación antes de quedar como HU activa.\n")
    lines.append("- `Spike`: trabajo de análisis técnico o descubrimiento.\n\n")

    for capability_id in sorted(grouped.keys()):
        cap_name = grouped[capability_id][0]["Capability Name"]
        lines.append(f"---\n\n## {capability_id} - {cap_name}\n")
        for story in sorted(grouped[capability_id], key=lambda x: int(x["Order"])):
            lines.append(f"\n### {story['Story ID']} - {story['Title']}\n")
            lines.append(f"- **Original Key:** {story['Original Key']}\n")
            lines.append(f"- **Source Epic:** {story['Source Epic']}\n")
            lines.append(f"- **Type:** {story['Type']}\n")
            lines.append(f"- **Status:** {story['Status']}\n")
            lines.append(f"- **Scope Treatment:** {story['Scope Treatment']}\n")
            lines.append(f"\n**Descripción**\n\n{story['Description']}\n")
            lines.append(f"\n**Criterios de aceptación / escenarios consolidados**\n\n{story['Acceptance Criteria']}\n")
            if story.get("Notes"):
                lines.append(f"\n**Notas**\n\n{story['Notes']}\n")

    MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    require_env()
    ensure_fields()
    write_markdown()

    created = []
    updated = []
    status_count: Dict[str, int] = {}

    for story in STORIES:
        status_count[story["Status"]] = status_count.get(story["Status"], 0) + 1
        record_id = find_record(story["Story ID"])
        if record_id:
            update_record(record_id, story)
            updated.append(story["Story ID"])
        else:
            new_id = create_record(story)
            created.append({"story_id": story["Story ID"], "record_id": new_id})

    print(json.dumps({
        "table": TABLE_NAME,
        "project": PROJECT,
        "md_path": str(MD_PATH),
        "created": created,
        "updated": updated,
        "total": len(STORIES),
        "status_count": status_count,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
