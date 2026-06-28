#!/usr/bin/env python3
"""
Knowledge Registry Population Engine (KRPE) — Phase A+B
WP18E-IMP-A: CAP + ASP + ASM extraction
WP19C: RSK + REF + MTH + PAT + SEC extraction

Outputs (written to 00_Governance/Knowledge_Standards/):
  KNOWLEDGE_ASSET_REGISTRY.yaml
  KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml
  KNOWLEDGE_RELATIONSHIP_GRAPH.yaml
  KNOWLEDGE_LOOKUP_INDEX.yaml

Build report written to:
  08_Commercial/Reports/REGISTRY_BUILD_REPORT_YYYYMMDD-NNN.yaml

Usage:
  python3 krpe.py [--repo-root PATH] [--mode FULL|DRY_RUN]
"""

import os
import re
import sys
import time
import hashlib
import argparse
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip3 install pyyaml", file=sys.stderr)
    sys.exit(1)


# ─── Constants ────────────────────────────────────────────────────────────────

VERSION = "2.0"
SCHEMA_VERSION = "1.0"
POPULATION_RULES_VERSION = "1.0"

# Subdirectory → owner_business_unit
BU_MAP = {
    "HCM": "Oracle",
    "OIC": "Oracle",
    "ERP": "Oracle",
    "OCI": "Oracle",
    "AMS": "Oracle",
    "Acumatica": "Acumatica",
    "BeBanking": "BeBanking",
}

# CAP → proposal sections (from CONTENT_SOURCE_MATRIX.md — Phase A baseline)
_CAP_SECTION_MAP: dict[str, list[str]] = {
    "W1S1-001": ["S-03", "S-13"],
    "W1S1-002": ["S-04"],
    "W1S1-003": ["S-09"],
    "W1S1-004": ["S-10"],
    "W1S1-005": ["S-11"],
    "W1S1-006": ["S-05"],
    "W1S1-007": ["S-06"],
    "W1S1-008": ["S-07"],
    "W1S1-009": ["S-08"],
    "W1S2-001": ["S-23"],
    "W1S2-002": ["S-24"],
    "W1S2-003": ["S-27"],
    "W1S2-004": ["S-25"],
    "W1S2-005": ["S-26"],
    "W1S2-006-ACU-FieldServices": ["S-27"],
    "W1S2-007-ACU-PayrollIntegration": ["S-27"],
    "W1S2-009": ["S-27"],
    "W1S3-001": ["S-29"],
    "W1S3-002": ["S-29"],
    "W1S3-003": ["S-29"],
    "W1S3-004": ["S-29"],
    "W1S3-005": ["S-29"],
    "W1S3-006": ["S-29"],
    "W1S3-007": ["S-29"],
    "W1S3-008": ["S-29"],
    "W1S3-009": ["S-29"],
    "W1S3-010": ["S-29"],
    "W2S1-001": ["S-17"],
    "W2S1-002": ["S-18"],
    "W2S1-003": ["S-20"],
    "W2S1-004": ["S-21", "S-70"],
    "W2S1-005-ORA-ImplementationMethodology": ["S-34", "S-36", "S-37"],
    "W3S1-001-ORA-HCMCore": ["S-16"],
    "W3S1-002-ORA-TalentMgmt": ["S-16"],
    "W3S1-003-ORA-RecruitingCloud": ["S-16"],
    "W3S1-004-ORA-LearningCloud": ["S-16"],
    "W3S1-005-ORA-WorkforceCompensation": ["S-16"],
    "W3S1-006-ORA-HCMAnalytics": ["S-16"],
    "W3S1-007-ORA-WorkforceManagement": ["S-16"],
    "W3S1-008-ORA-HelpDesk-HRServiceDelivery": ["S-16"],
    "W3S1-009-ORA-PayrollInterface-Integration": ["S-16"],
    "W4-AI-002-ORA-AISkills": ["S-15"],
    "W4-ERP-001-ORA-FusionFinancials": ["S-17"],
    "W4-ERP-002-ORA-FusionProcurement": ["S-17"],
    "W4-ERP-003-ORA-PPM": ["S-17"],
    "W4-HCM-002-ORA-Journeys": ["S-16"],
    "W4-INT-001-ORA-OICAccelerators": ["S-19"],
    "W5-ACU-001-ACU-SupportManagedServices": ["S-28", "S-70"],
    "W5-METH-001-ERP-ImplementationMethodology": ["S-34", "S-36", "S-37"],
}

# CAP → cap_ext.platform (governs AV-006 platform filter in KVE)
_CAP_PLATFORM_MAP: dict[str, str] = {
    # Corporate / Cross-BU — applicable to all tenders
    "W1S1-001": "Corporate",
    "W1S1-002": "Corporate",
    "W1S1-006": "Corporate",
    "W1S1-007": "Corporate",
    "W1S1-008": "Corporate",
    "W1S1-009": "Corporate",
    # Cross-Platform Oracle (applicable to any Oracle tender)
    "W1S1-003": "Cross-Platform",
    "W2S1-003": "Cross-Platform",
    "W2S1-004": "Cross-Platform",
    "W2S1-005-ORA-ImplementationMethodology": "Cross-Platform",
    "W4-AI-002-ORA-AISkills": "Cross-Platform",
    "W5-METH-001-ERP-ImplementationMethodology": "Cross-Platform",
    # Oracle HCM Cloud
    "W3S1-001-ORA-HCMCore": "Oracle HCM Cloud",
    "W3S1-002-ORA-TalentMgmt": "Oracle HCM Cloud",
    "W3S1-003-ORA-RecruitingCloud": "Oracle HCM Cloud",
    "W3S1-004-ORA-LearningCloud": "Oracle HCM Cloud",
    "W3S1-005-ORA-WorkforceCompensation": "Oracle HCM Cloud",
    "W3S1-006-ORA-HCMAnalytics": "Oracle HCM Cloud",
    "W3S1-007-ORA-WorkforceManagement": "Oracle HCM Cloud",
    "W3S1-008-ORA-HelpDesk-HRServiceDelivery": "Oracle HCM Cloud",
    "W3S1-009-ORA-PayrollInterface-Integration": "Oracle HCM Cloud",
    "W4-HCM-002-ORA-Journeys": "Oracle HCM Cloud",
    # Oracle ERP Cloud (Fusion)
    "W2S1-001": "Oracle ERP Cloud",
    "W4-ERP-001-ORA-FusionFinancials": "Oracle ERP Cloud",
    "W4-ERP-002-ORA-FusionProcurement": "Oracle ERP Cloud",
    "W4-ERP-003-ORA-PPM": "Oracle ERP Cloud",
    # Oracle EBS
    "W2S1-002": "Oracle EBS",
    # Oracle Integration Cloud
    "W4-INT-001-ORA-OICAccelerators": "Oracle Integration Cloud",
    # Acumatica (Partner + modules)
    "W1S1-004": "Acumatica",
    "W1S2-001": "Acumatica",
    "W1S2-002": "Acumatica",
    "W1S2-003": "Acumatica",
    "W1S2-004": "Acumatica",
    "W1S2-005": "Acumatica",
    "W1S2-006-ACU-FieldServices": "Acumatica",
    "W1S2-007-ACU-PayrollIntegration": "Acumatica",
    "W1S2-009": "Acumatica",
    "W5-ACU-001-ACU-SupportManagedServices": "Acumatica",
    # BeBanking (Partner + modules)
    "W1S1-005": "BeBanking",
    "W1S3-001": "BeBanking",
    "W1S3-002": "BeBanking",
    "W1S3-003": "BeBanking",
    "W1S3-004": "BeBanking",
    "W1S3-005": "BeBanking",
    "W1S3-006": "BeBanking",
    "W1S3-007": "BeBanking",
    "W1S3-008": "BeBanking",
    "W1S3-009": "BeBanking",
    "W1S3-010": "BeBanking",
}

# ASP subdir → proposal sections (from CONTENT_SOURCE_MATRIX.md — Phase A baseline)
_ASP_SECTION_MAP: dict[str, list[str]] = {
    "HCM": ["S-30", "S-31", "S-33", "S-40", "S-41", "S-42", "S-45", "S-51", "A-01"],
    "ERP": ["S-30", "S-31", "S-33", "S-40", "S-41", "S-42", "S-45", "S-51", "A-01"],
    "OCI": ["S-30", "S-31", "S-33", "S-40", "S-45", "S-51", "A-01"],
    "OIC": ["S-30", "S-31", "S-33", "S-40", "S-51", "A-01"],
    "AMS": ["S-70", "S-71", "S-72", "S-73", "S-74", "S-75", "S-76", "S-51", "A-01"],
    "Acumatica": ["S-30", "S-31", "S-33", "S-40", "S-41", "S-42", "S-45", "S-51", "A-01"],
    "BeBanking": ["S-29", "S-30", "S-31", "S-51", "A-01"],
}

# Valid Cap ID pattern for MASTER_CAPABILITY_INDEX.md row filtering
# Matches: W1S1-001, W2S1-003, W3S1-009, W4-HCM-002, W5-ACU-001, W5-METH-001
CAP_ID_RE = re.compile(r"^W\d[A-Z]\d-\d{3}$|^W\d-[A-Z]+-\d{3}$")

# Assumption ID pattern: matches all four body formats
#   Format A: **HCM-ENV-001**          (multiline — text on next line)
#   Format B: **OCI-GEN-001.** text    (inline — period before closing **)
#   Format C: **BB-GEN-001:** text     (inline — colon before closing **)
#   Format D: **EBS-SLA-002 [REPLACES: ...]** text  (annotation in brackets)
# Note: [A-Z0-9]{2,8} allows digit-prefixed category codes (e.g. 3PT in HCM-3PT-001)
# Annotation suffix supports both bracket form [REPLACES: X] and em-dash form — Label
ASM_ID_RE = re.compile(
    r"^\*\*([A-Z][A-Z0-9]{0,6}-[A-Z0-9]{2,8}-\d{3}[A-Z]?"
    r"(?:\s+(?:\[.*?\]|[—–-]\s*[^*]+?))?)[.:]?\*\*\s*(.*)",
    re.MULTILINE,
)

# ─── Phase B: Source file paths ───────────────────────────────────────────────

_RSK_FILE = Path("08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_V1.md")
_REF_FILE = Path("00_Governance/REFERENCE_MASTER.md")
_PAT_FILE = Path("08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md")
_SEC_FILE = Path("08_Commercial/Assembly_Engine/PROPOSAL_SECTION_LIBRARY.md")

# ─── Phase B: Regex patterns ──────────────────────────────────────────────────

RSK_HDR_RE = re.compile(r"^### (RC-[A-Z]+-\d+) — (.+)$", re.MULTILINE)
REF_HDR_RE = re.compile(
    r"^### (REF-(?:ORA|ACU|BB)-\d+) — (.+?)(?:\s+⭐[^\n]*)?\s*$",
    re.MULTILINE,
)
REF_TIER_RE = re.compile(r"^## (Gold|Silver|Bronze) References?", re.MULTILINE)
PAT_SECTION3_RE = re.compile(r"^## 3\. Pattern Reference Table", re.MULTILINE)
SEC_CATEGORY_RE = re.compile(r"^## \d+\. Section Library — (.+)$", re.MULTILINE)
_KV_TABLE_RE = re.compile(
    r"^\|\s*\*{0,2}(.+?)\*{0,2}\s*\|\s*(.+?)\s*\|?\s*$",
    re.MULTILINE,
)
_BULLET_KV_RE = re.compile(r"^-\s+\*\*(.+?):\*\*\s*(.+)$", re.MULTILINE)

# ─── Phase B: Static PAT section scope (PROPOSAL_PATTERN_ENGINE.md v1.0 §4–6) ─

_CORE_ORACLE_IMPL: list[str] = [
    "S-01", "S-02", "S-03", "S-04", "S-05", "S-06", "S-07", "S-08", "S-09", "S-12",
    "S-13", "S-14", "S-15",
    "S-30", "S-31", "S-32", "S-33", "S-34", "S-35", "S-36", "S-37", "S-38",
    "S-39", "S-42", "S-43", "S-46",
    "S-49", "S-50", "S-51", "S-52",
    "S-55", "S-56", "S-57", "S-58", "S-59", "S-60", "S-61", "S-62",
    "S-67", "A-01", "A-04", "A-05",
]
_ORACLE_IMPL_EXCL: list[str] = [
    "S-10", "S-11", "S-17", "S-18", "S-19", "S-20", "S-21", "S-22",
    "S-23", "S-24", "S-25", "S-26", "S-27", "S-28", "S-29",
    "S-70", "S-71", "S-72", "S-73", "S-74", "S-75", "S-76",
]

_PAT_SCOPE: dict[str, tuple[list[str], list[str]]] = {
    "1":  (_CORE_ORACLE_IMPL + ["S-16"], _ORACLE_IMPL_EXCL),
    "2":  (_CORE_ORACLE_IMPL + ["S-16"], _ORACLE_IMPL_EXCL),
    "3":  (_CORE_ORACLE_IMPL + ["S-16", "S-19"],
           [s for s in _ORACLE_IMPL_EXCL if s != "S-19"]),
    "4":  (_CORE_ORACLE_IMPL + ["S-16"], _ORACLE_IMPL_EXCL),
    "5":  (_CORE_ORACLE_IMPL + ["S-16"], _ORACLE_IMPL_EXCL),
    "6":  (
        [s for s in _CORE_ORACLE_IMPL if s not in ("S-39", "S-40", "S-41")] + ["S-19"],
        _ORACLE_IMPL_EXCL + ["S-39", "S-40", "S-41"],
    ),
    "7":  (_CORE_ORACLE_IMPL + ["S-17"],
           [s for s in _ORACLE_IMPL_EXCL if s != "S-17"]),
    "8":  (_CORE_ORACLE_IMPL + ["S-17"],
           [s for s in _ORACLE_IMPL_EXCL if s != "S-17"]),
    "9":  (_CORE_ORACLE_IMPL + ["S-18"],
           [s for s in _ORACLE_IMPL_EXCL if s != "S-18"]),
    "10": (
        [
            "S-01", "S-02", "S-03", "S-04", "S-05", "S-06", "S-07", "S-08", "S-09", "S-12",
            "S-13", "S-14", "S-15", "S-20",
            "S-30", "S-31", "S-32", "S-33", "S-36", "S-37",
            "S-49", "S-50", "S-51", "S-52",
            "S-55", "S-56", "S-57", "S-58", "S-59", "S-60",
            "S-67", "A-01", "A-04", "A-05",
        ],
        [
            "S-10", "S-11", "S-16", "S-17", "S-18", "S-19", "S-21", "S-22",
            "S-23", "S-24", "S-25", "S-26", "S-27", "S-28", "S-29",
            "S-34", "S-35", "S-38", "S-39", "S-40", "S-41", "S-42", "S-43",
            "S-70", "S-71", "S-72", "S-73", "S-74", "S-75", "S-76",
        ],
    ),
    "11": (
        [
            "S-01", "S-02", "S-03", "S-04", "S-05", "S-06", "S-07", "S-08", "S-10", "S-12",
            "S-13", "S-14", "S-15",
            "S-23", "S-24", "S-25", "S-26", "S-27",
            "S-30", "S-31", "S-32", "S-33", "S-34", "S-35", "S-36", "S-37", "S-38",
            "S-39", "S-40", "S-41", "S-42", "S-43", "S-46",
            "S-49", "S-50", "S-51", "S-52",
            "S-55", "S-56", "S-57", "S-58", "S-59", "S-60", "S-61", "S-63",
            "S-67", "A-01", "A-02", "A-03", "A-04", "A-05", "A-06",
        ],
        [
            "S-09", "S-11", "S-16", "S-17", "S-18", "S-19", "S-20", "S-21", "S-22",
            "S-28", "S-29", "S-70", "S-71", "S-72", "S-73", "S-74", "S-75", "S-76",
        ],
    ),
    "12": (
        [
            "S-01", "S-02", "S-03", "S-04", "S-05", "S-06", "S-07", "S-08", "S-11", "S-12",
            "S-13", "S-14", "S-15", "S-29",
            "S-30", "S-31", "S-32", "S-33", "S-36", "S-37",
            "S-49", "S-50", "S-51", "S-52",
            "S-55", "S-56", "S-57", "S-58", "S-59", "S-60",
            "S-67", "A-01", "A-04", "A-05",
        ],
        [
            "S-09", "S-10", "S-16", "S-17", "S-18", "S-19", "S-20", "S-21", "S-22",
            "S-23", "S-24", "S-25", "S-26", "S-27", "S-28",
            "S-34", "S-70", "S-71", "S-72", "S-73", "S-74", "S-75", "S-76",
        ],
    ),
    "13": (
        [
            "S-01", "S-02", "S-03", "S-04", "S-05", "S-06", "S-07", "S-08", "S-09", "S-12",
            "S-13", "S-14", "S-15", "S-21",
            "S-30", "S-31", "S-32", "S-33", "S-36", "S-37",
            "S-49", "S-50", "S-51", "S-52",
            "S-55", "S-56", "S-57", "S-58", "S-59", "S-60",
            "S-67", "S-70", "S-71", "S-72", "S-73", "S-74", "S-75", "S-76",
            "A-01", "A-03", "A-04", "A-05",
        ],
        [
            "S-10", "S-11", "S-16", "S-17", "S-18", "S-19", "S-20", "S-22",
            "S-23", "S-24", "S-25", "S-26", "S-27", "S-28", "S-29",
            "S-34", "S-35", "S-38", "S-39", "S-40", "S-41", "S-42", "S-43",
            "S-46", "S-47", "S-48",
        ],
    ),
}


# ─── YAML helpers ─────────────────────────────────────────────────────────────

class _Dumper(yaml.Dumper):
    pass


_Dumper.add_representer(
    bool,
    lambda d, v: d.represent_scalar("tag:yaml.org,2002:bool", "true" if v else "false"),
)
_Dumper.add_representer(
    type(None),
    lambda d, v: d.represent_scalar("tag:yaml.org,2002:str", ""),
)


def _dump(obj) -> str:
    return yaml.dump(obj, Dumper=_Dumper, default_flow_style=False,
                     allow_unicode=True, sort_keys=False, indent=2, width=120)


def _bool(val) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        return val.strip().lower() in ("true", "yes", "1", "y")
    return bool(val) if val is not None else False


def _str(val) -> str:
    return "" if val is None else str(val).strip()


def _list(val) -> list:
    if val is None:
        return []
    if isinstance(val, list):
        return [str(x).strip() for x in val if x is not None]
    s = str(val).strip()
    if not s:
        return []
    return [x.strip() for x in s.split(",") if x.strip()]


# ─── Source format adapters ───────────────────────────────────────────────────

def read_frontmatter(path: Path) -> tuple[dict, str]:
    """YAMLFrontmatterAdapter: extract --- delimited YAML block and body text."""
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise ValueError(f"Cannot read {path}: {exc}") from exc

    if not raw.startswith("---"):
        return {}, raw

    parts = raw.split("---", maxsplit=2)
    if len(parts) < 3:
        return {}, raw

    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML parse error in {path}: {exc}") from exc

    return meta, parts[2]


def parse_all_tables(content: str) -> list[list[dict]]:
    """MarkdownTableAdapter: parse all pipe tables in a string.

    Returns list of tables; each table is a list of row-dicts.
    """
    tables: list[list[dict]] = []
    headers: Optional[list[str]] = None
    rows: list[dict] = []

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            # Separator row: all cells are just dashes (and colons for alignment)
            if all(re.fullmatch(r"[:\- ]+", c) for c in cells if c):
                continue
            if headers is None:
                headers = cells
            elif len(cells) == len(headers):
                rows.append(dict(zip(headers, cells)))
        else:
            if headers and rows:
                tables.append(rows)
            headers = None
            rows = []

    if headers and rows:
        tables.append(rows)

    return tables


def extract_assumptions(body: str) -> list[dict]:
    """SectionStructuredAdapter (simplified): extract all ASM entries from a pack body.

    Handles Formats A/B/C/D. Returns list of {asset_id, raw_id, assumption_text}.
    """
    result: list[dict] = []
    current_id: Optional[str] = None
    current_clean_id: Optional[str] = None
    text_lines: list[str] = []

    for line in body.splitlines():
        m = ASM_ID_RE.match(line)
        if m:
            if current_clean_id:
                result.append({
                    "raw_id": current_id,
                    "asset_id": current_clean_id,
                    "assumption_text": " ".join(text_lines).strip(),
                })
            raw_id = m.group(1).strip()
            # Strip all annotation suffixes: [REPLACES: X] bracket form, or — Label em-dash form
            clean_id = re.sub(r"\s+(?:\[.*?\]|[—–]\s*.+)$", "", raw_id).strip()
            current_id = raw_id
            current_clean_id = clean_id
            text_lines = []
            inline = m.group(2).strip()
            if inline:
                # Remove trailing annotation markers like *(Updated — ...)*
                inline = re.sub(r"\s*\*\(.*?\)\*", "", inline).strip()
                if inline:
                    text_lines.append(inline)
        elif current_clean_id is not None:
            stripped = line.strip()
            if stripped.startswith(("# ", "## ", "### ")):
                # Section heading ends current assumption
                result.append({
                    "raw_id": current_id,
                    "asset_id": current_clean_id,
                    "assumption_text": " ".join(text_lines).strip(),
                })
                current_id = None
                current_clean_id = None
                text_lines = []
            elif stripped and stripped != "---":
                cleaned = re.sub(r"\s*\*\(.*?\)\*", "", stripped).strip()
                if cleaned:
                    text_lines.append(cleaned)

    if current_clean_id:
        result.append({
            "raw_id": current_id,
            "asset_id": current_clean_id,
            "assumption_text": " ".join(text_lines).strip(),
        })

    return result


# ─── Lifecycle normalisation ───────────────────────────────────────────────────

def normalise_status(raw: str) -> str:
    """Map source status strings to the 8-state canonical lifecycle."""
    _map = {
        "approved": "APPROVED",
        "draft": "DRAFT",
        "superseded": "SUPERSEDED",
        "archived": "ARCHIVED",
        "normalised": "NORMALISED",
        "direct": "APPROVED",
    }
    key = raw.strip().lower()
    # "approved v1.0", "approved v1.1 — ..." etc.
    if key.startswith("approved"):
        return "APPROVED"
    return _map.get(key, "APPROVED")


# ─── Discovery ────────────────────────────────────────────────────────────────

MASTER_INDEX_PATH = "06_Capabilities/MASTER_CAPABILITY_INDEX.md"

NON_PACK_PATTERNS = [
    r"GAP_REPORT",
    r"SCOPE_BOUNDARY",
    r"APPROVAL_CHANGE_LOG",
    r"IMPLEMENTATION_PATTERNS",
    r"WP\d",
]


def discover_cap_rows(repo_root: Path) -> list[dict]:
    """Parse MASTER_CAPABILITY_INDEX.md and return one dict per CAP row."""
    index_path = repo_root / MASTER_INDEX_PATH
    if not index_path.exists():
        return []

    content = index_path.read_text(encoding="utf-8", errors="replace")
    all_tables = parse_all_tables(content)

    rows = []
    for table in all_tables:
        # Only process main asset tables: must have both "Cap ID" (first column)
        # and "Capability Name". Excludes secondary tables (review, risk, etc.)
        # that also happen to contain a "Cap ID" column at a different position.
        if not table or "Capability Name" not in table[0]:
            continue
        for row in table:
            cap_id = row.get("Cap ID", "").strip()
            # Filter to valid Cap ID format — excludes any remaining section header rows
            if not CAP_ID_RE.match(cap_id):
                continue
            # Support both column name variants
            approved_doc = (row.get("Approved Document (KB copy)", "").strip() or
                            row.get("Approved Document", "").strip())
            # Strip backtick wrappers: `path/to/file.md`
            approved_doc = approved_doc.strip("`")

            rows.append({
                "cap_id": cap_id,
                "capability_name": row.get("Capability Name", "").strip(),
                "product_area": row.get("Product Area", "").strip(),
                "approved_document": approved_doc,
                "tier1_evidence": row.get("Tier 1 Evidence", "").strip(),
                "named_reference": row.get("Named Reference", "").strip(),
                "reference_client": row.get("Reference Client", "").strip(),
                "industry": row.get("Industry", "").strip(),
                "evidence_tier": row.get("Evidence Tier", "").strip(),
                "governance_restrictions": row.get("Governance Restrictions", "").strip(),
                "last_review": row.get("Last Review", "").strip(),
            })

    return rows


def _is_pack(path: Path, meta: dict) -> bool:
    """Return True if this file is an assumption pack (positive identification).

    A file qualifies when it has at least one approval signal AND at least one
    content signal (assumption_count or a document_id that looks like a pack).
    This allows for packs that omit document_id (e.g. BEBANKING_BASE_ASSUMPTIONS_V1).
    """
    # Must not live in the Governance subdirectory
    if "Governance" in path.parts:
        return False
    # Must not match exclusion patterns
    name = path.name
    for pat in NON_PACK_PATTERNS:
        if re.search(pat, name, re.IGNORECASE):
            return False
    # Approval signal: approved_for_reuse=true OR status starts with "Approved"
    afr = meta.get("approved_for_reuse")
    status = _str(meta.get("status", ""))
    approval_signal = (afr is not None and _bool(afr)) or status.lower().startswith("approved")
    if not approval_signal:
        return False
    # Content signal: assumption_count present (strongest signal)
    if meta.get("assumption_count"):
        return True
    # Weaker: has document_id (rules out non-governed files)
    if meta.get("document_id"):
        return True
    return False


def discover_asp_files(repo_root: Path) -> list[Path]:
    """Walk 08_Commercial/Assumptions/ and return all pack files."""
    base = repo_root / "08_Commercial" / "Assumptions"
    if not base.exists():
        return []

    packs: list[Path] = []
    for md in sorted(base.rglob("*.md")):
        try:
            meta, _ = read_frontmatter(md)
        except (ValueError, OSError):
            continue
        if _is_pack(md, meta):
            packs.append(md)

    return packs


# ─── CAP extractor ────────────────────────────────────────────────────────────

_BU_NORMALISE = {
    "Cross_BU": "Corporate",
    "Cross-BU": "Corporate",
    "cross_bu": "Corporate",
    "Cross-Platform": "Corporate",
    "Corporate": "Corporate",
}

# Substring-match patterns for the less structured `bu:` field used by some Wave 5 files
def _bu_from_raw(raw: str) -> str:
    """Map free-text `bu` field values to canonical BU names."""
    raw_lower = raw.lower()
    if not raw or "cross" in raw_lower or "agnostic" in raw_lower or "platform" in raw_lower:
        return "Corporate"
    if "oracle" in raw_lower:
        return "Oracle"
    if "acumatica" in raw_lower:
        return "Acumatica"
    if "bebanking" in raw_lower or "banking" in raw_lower:
        return "BeBanking"
    return raw


def _derive_bu(index_row: dict, file_meta: dict) -> str:
    # Try standard field names first
    bu = _str(file_meta.get("business_unit", ""))
    if not bu:
        # Some Wave 5 files use the shorter `bu:` key
        bu = _str(file_meta.get("bu", ""))
        if bu:
            return _bu_from_raw(bu)
    if bu:
        return _BU_NORMALISE.get(bu, bu)
    pa = index_row.get("product_area", "")
    for keyword, mapped_bu in [
        ("Oracle", "Oracle"), ("Acumatica", "Acumatica"),
        ("BeBanking", "BeBanking"), ("beBanking", "BeBanking"),
        ("Corporate", "Corporate"), ("Cross", "Corporate"),
    ]:
        if keyword in pa:
            return mapped_bu
    return ""


def extract_cap(index_row: dict, repo_root: Path,
                errors: list, warnings: list) -> Optional[dict]:
    cap_id = index_row["cap_id"]
    rel_doc = index_row["approved_document"]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    file_meta: dict = {}
    source_file = rel_doc

    if not rel_doc:
        warnings.append({
            "warning_code": "NO_APPROVED_DOCUMENT",
            "severity": "WARNING",
            "asset_id": cap_id,
            "message": f"No Approved Document path in index for {cap_id}.",
            "action_taken": "REGISTERED_FROM_INDEX_ONLY",
        })
    else:
        fpath = repo_root / rel_doc
        if not fpath.exists():
            warnings.append({
                "warning_code": "FILE_NOT_FOUND",
                "severity": "WARNING",
                "asset_id": cap_id,
                "file_path": rel_doc,
                "message": f"Approved document not found: {rel_doc}",
                "action_taken": "REGISTERED_FROM_INDEX_ONLY",
            })
        else:
            try:
                file_meta, _ = read_frontmatter(fpath)
            except ValueError as exc:
                errors.append({
                    "error_code": "EXTRACTION_ERROR",
                    "severity": "ERROR",
                    "asset_id": cap_id,
                    "file_path": rel_doc,
                    "message": str(exc),
                    "action_taken": "REGISTERED_FROM_INDEX_ONLY",
                })

    # asset_id: prefer file frontmatter document_id, else cap_id from index
    file_doc_id = _str(file_meta.get("document_id", ""))
    asset_id = file_doc_id if file_doc_id else cap_id

    if file_doc_id and file_doc_id != cap_id:
        warnings.append({
            "warning_code": "ID_MISMATCH",
            "severity": "WARNING",
            "asset_id": cap_id,
            "file_path": rel_doc,
            "message": f"Index Cap ID '{cap_id}' differs from file document_id '{file_doc_id}'. Using '{asset_id}'.",
            "action_taken": "USING_FILE_DOCUMENT_ID",
        })

    title = _str(file_meta.get("title", "")) or index_row["capability_name"]
    version = _str(file_meta.get("version", "")) or "1.0"
    raw_status = _str(file_meta.get("status", "") or file_meta.get("review_status", ""))
    lifecycle_status = normalise_status(raw_status)

    raw_afr = file_meta.get("approved_for_reuse")
    if raw_afr is None:
        # Wave 1/2 files: derive from readiness or status
        readiness = _str(file_meta.get("readiness", ""))
        raw_afr = readiness if readiness else (lifecycle_status == "APPROVED")
    approved_for_reuse = _bool(raw_afr)

    owner_bu = _derive_bu(index_row, file_meta)

    # Derive platform / product area from KB destination or wave subdirectory
    kb_dest = _str(file_meta.get("kb_destination", ""))
    raw_platform = _str(file_meta.get("business_unit", "") or file_meta.get("bu", "")) or owner_bu
    platform = _BU_NORMALISE.get(raw_platform, raw_platform) if raw_platform in _BU_NORMALISE else owner_bu
    product_area_path = ""
    if kb_dest:
        parts = kb_dest.strip("/").split("/")
        if len(parts) >= 2:
            product_area_path = parts[-1].strip("/")

    return {
        "asset_id": asset_id,
        "asset_type": "CAP",
        "title": title,
        "version": version,
        "lifecycle_status": lifecycle_status,
        "approved_for_reuse": approved_for_reuse,
        "owner_role": "BU Lead",
        "owner_business_unit": owner_bu,
        "approval_authority": "BU Lead",
        "governing_standard": "KNOWLEDGE_ASSET_STANDARD.md",
        "registry_version_added": "1.0",
        "created": _str(file_meta.get("created", "") or file_meta.get("extraction_date", "")) or _str(index_row.get("last_review", "")),
        "created_by": _str(file_meta.get("created_by", "") or file_meta.get("extracted_by", "")) or "MASTER_CAPABILITY_INDEX",
        "approved_by": _str(file_meta.get("approved_by", "") or file_meta.get("reviewed_by", "")),
        "approval_date": _str(file_meta.get("approved", "") or file_meta.get("approval_date", "") or file_meta.get("review_date", "")),
        "source_file": source_file,
        "description": "",
        "confidence_level": "",
        "review_frequency": "annual",
        "last_reviewed": index_row.get("last_review", ""),
        "review_due": "",
        "governance_notes": _str(index_row.get("governance_restrictions", "")) or "None — governed by KNOWLEDGE_ASSET_STANDARD.md",
        "pattern_applicability": ["ALL"],
        "proposal_sections": _CAP_SECTION_MAP.get(asset_id, ["S-15"]),
        "tags": _list(file_meta.get("tags", [])),
        "source_assets": [],
        "related_assets": [],
        "supersedes": "",
        "superseded_by": "",
        "library_index_ref": MASTER_INDEX_PATH,
        "registry_last_synced": today,
        "validation_status": "",
        "validation_issues": [],
        "assembly_rules": {
            "mandatory_if": "",
            "optional_if": "",
            "excluded_if": "",
            "assembly_priority": 5,
            "section_placement": 0,
            "content_source_type": "CAPABILITY",
        },
        "cap_ext": {
            "source_document": _str(file_meta.get("source_document", "")),
            "source_status": _str(file_meta.get("source_status", "")),
            "prereq_statement": _str(file_meta.get("prereq_statement", "")),
            "kb_destination": kb_dest,
            "wave": _str(file_meta.get("wave", "")),
            "deliverable": _str(file_meta.get("deliverable", "")),
            "tier1_evidence": index_row.get("tier1_evidence", ""),
            "governance_restrictions": index_row.get("governance_restrictions", ""),
            "reference_clients": _list(index_row.get("reference_client", "")),
            "industry": index_row.get("industry", ""),
            "evidence_tier": index_row.get("evidence_tier", ""),
            "named_reference": index_row.get("named_reference", ""),
            "platform": _CAP_PLATFORM_MAP.get(asset_id, platform),
            "product_area_path": product_area_path,
        },
    }


# ─── ASP + ASM extractor ─────────────────────────────────────────────────────

def extract_asp_and_asms(pack_path: Path, repo_root: Path,
                          errors: list, warnings: list) -> tuple[Optional[dict], list[dict]]:
    try:
        meta, body = read_frontmatter(pack_path)
    except ValueError as exc:
        errors.append({
            "error_code": "EXTRACTION_ERROR",
            "severity": "ERROR",
            "file_path": str(pack_path.relative_to(repo_root)),
            "message": str(exc),
            "action_taken": "SKIPPED",
        })
        return None, []

    rel_path = str(pack_path.relative_to(repo_root))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Derive pack_id: prefer frontmatter document_id, else convert filename to kebab-upper
    raw_doc_id = _str(meta.get("document_id", ""))
    pack_id = raw_doc_id if raw_doc_id else pack_path.stem.replace("_", "-").upper()
    title = _str(meta.get("title", ""))
    version = _str(meta.get("version", "")) or "1.0"
    raw_status = _str(meta.get("status", ""))
    lifecycle_status = normalise_status(raw_status)

    raw_afr = meta.get("approved_for_reuse")
    approved_for_reuse = (
        _bool(raw_afr) if raw_afr is not None
        else (lifecycle_status == "APPROVED")
    )

    # Derive business unit from subdirectory
    try:
        assumptions_idx = next(
            i for i, p in enumerate(pack_path.parts)
            if p.lower() == "assumptions"
        )
        subdir = pack_path.parts[assumptions_idx + 1] if assumptions_idx + 1 < len(pack_path.parts) else ""
    except StopIteration:
        subdir = ""

    owner_bu = BU_MAP.get(subdir, "Oracle")
    pack_created_by = (
        _str(meta.get("created_by", ""))
        or _str(meta.get("approved_by", ""))
        or _str(meta.get("approval_programme", ""))
    )

    asp_entry = {
        "asset_id": pack_id,
        "asset_type": "ASP",
        "title": title,
        "version": version,
        "lifecycle_status": lifecycle_status,
        "approved_for_reuse": approved_for_reuse,
        "owner_role": "BU Lead",
        "owner_business_unit": owner_bu,
        "approval_authority": "BU Lead",
        "governing_standard": "KNOWLEDGE_ASSET_STANDARD.md",
        "registry_version_added": "1.0",
        "created": _str(meta.get("created", "") or meta.get("created_date", "")),
        "created_by": pack_created_by,
        "approved_by": _str(meta.get("approved_by", "")),
        "approval_date": _str(meta.get("approved_date", "") or meta.get("promoted", "")),
        "source_file": rel_path,
        "description": "",
        "confidence_level": "",
        "review_frequency": "annual",
        "last_reviewed": "",
        "review_due": "",
        "governance_notes": _str(meta.get("governance_notes", "")) or "BU Lead approved. Governed by KNOWLEDGE_ASSET_STANDARD.md.",
        "pattern_applicability": _list(meta.get("applies_to", [])) or ["ALL"],
        "proposal_sections": _ASP_SECTION_MAP.get(subdir, ["S-30", "S-51", "A-01"]),
        "tags": [],
        "source_assets": [],
        "related_assets": [],
        "supersedes": "",
        "superseded_by": "",
        "library_index_ref": "",
        "registry_last_synced": today,
        "validation_status": "",
        "validation_issues": [],
        "assembly_rules": {
            "mandatory_if": "",
            "optional_if": "",
            "excluded_if": "",
            "assembly_priority": 5,
            "section_placement": 0,
            "content_source_type": "ASSUMPTION_PACK",
        },
        "asp_ext": {
            "module_scope": _str(meta.get("scope", "")),
            "pack_scope": _str(meta.get("pack_code", "") or subdir),
            "assumption_count": 0,  # updated after ASM extraction
            "parent_pack": _str(meta.get("parent_pack", "")),
            "classification": _str(meta.get("classification", "")),
            "pending_decisions": len(_list(meta.get("bu_lead_decisions_pending", []))),
            "pattern_applicability": _list(meta.get("applies_to", [])),
        },
    }

    # Extract assumptions from body
    raw_asms = extract_assumptions(body)
    declared = meta.get("assumption_count") or 0

    if declared and len(raw_asms) != declared:
        warnings.append({
            "warning_code": "ASSUMPTION_COUNT_MISMATCH",
            "severity": "WARNING",
            "asset_id": pack_id,
            "file_path": rel_path,
            "message": (
                f"Declared assumption_count={declared} but extracted "
                f"{len(raw_asms)} assumptions."
            ),
            "action_taken": "USING_EXTRACTED_COUNT",
        })

    asp_entry["asp_ext"]["assumption_count"] = len(raw_asms)

    asm_entries: list[dict] = []
    for seq, asm_data in enumerate(raw_asms, start=1):
        asm_id = asm_data["asset_id"]
        asm_entries.append({
            "asset_id": asm_id,
            "asset_type": "ASM",
            "title": asm_id,
            "version": version,
            "lifecycle_status": lifecycle_status,
            "approved_for_reuse": approved_for_reuse,
            "owner_role": "BU Lead",
            "owner_business_unit": owner_bu,
            "approval_authority": "BU Lead",
            "governing_standard": "KNOWLEDGE_ASSET_STANDARD.md",
            "registry_version_added": "1.0",
            "created": _str(meta.get("created", "") or meta.get("created_date", "")),
            "created_by": pack_created_by,
            "approved_by": _str(meta.get("approved_by", "")),
            "approval_date": _str(meta.get("approved_date", "") or meta.get("promoted", "")),
            "source_file": rel_path,
            "description": "",
            "governance_notes": f"Governed by parent assumption pack {pack_id}.",
            "pattern_applicability": _list(meta.get("applies_to", [])) or ["ALL"],
            "proposal_sections": _ASP_SECTION_MAP.get(subdir, ["S-30", "S-51", "A-01"]),
            "tags": [],
            "related_assets": [],
            "supersedes": "",
            "superseded_by": "",
            "registry_last_synced": today,
            "validation_status": "",
            "validation_issues": [],
            "assembly_rules": {
                "mandatory_if": "",
                "optional_if": "",
                "excluded_if": "",
                "assembly_priority": 5,
                "section_placement": 0,
                "content_source_type": "ASSUMPTION",
            },
            "asm_ext": {
                "parent_pack_id": pack_id,
                "assumption_text": asm_data["assumption_text"],
                "rationale": "",
                "assumption_type": "COMMERCIAL",
                "dependency": "",
                "risk_exposure": "",
                "pending": False,
                "sequence": seq,
            },
        })

    return asp_entry, asm_entries


# ─── Phase B: Shared helpers ──────────────────────────────────────────────────

def _parse_kv_table(block: str) -> dict[str, str]:
    """Parse | **Key** | Value | or | Key | Value | table rows."""
    result: dict[str, str] = {}
    for m in _KV_TABLE_RE.finditer(block):
        key = m.group(1).strip()
        val = m.group(2).strip()
        if not key or key in ("---", "Field", "Section ID", "ID", "Pattern") or val in ("---", "Value"):
            continue
        result[key] = val
    return result


def _parse_list_field(val: str) -> list[str]:
    """Split comma-separated value into a list, discarding empties and '—'."""
    if not val or val.strip() in ("—", "-", ""):
        return []
    return [v.strip() for v in val.split(",") if v.strip() and v.strip() != "—"]


def _parse_section_ids(val: str) -> list[str]:
    """Extract S-NN / A-NN section IDs from strings like 'Primary: S-50. Secondary: S-37, S-38'."""
    return re.findall(r"[SA]-\d+", val)


def _parse_pattern_nums(val: str) -> list[str]:
    """Extract digit-only tokens from a comma/space-separated string."""
    return [v.strip() for v in re.split(r"[,\s]+", val) if v.strip().isdigit()]


def _parse_bool_cell(val: str) -> bool:
    v = val.strip().lower()
    return v.startswith("yes") or v == "true" or v == "1"


def _parse_pct(val: str) -> int:
    m = re.search(r"(\d+)%", val)
    return int(m.group(1)) if m else 0


def _extract_rsk_paragraphs(block: str) -> dict[str, str]:
    """Extract the three labeled body paragraphs from a RSK entry block."""
    result: dict[str, str] = {}
    for label in ("Risk description", "Standard mitigation", "Customisation guidance"):
        pat = re.compile(
            r"\*\*" + re.escape(label) + r":\*\*\s*(.+?)(?=\n\*\*[A-Z]|\n---|\n#{1,4} |\Z)",
            re.DOTALL,
        )
        m = pat.search(block)
        if m:
            result[label] = m.group(1).strip()
    return result


# ─── Phase B: RSK extractor ───────────────────────────────────────────────────

def extract_rsk(repo_root: Path, errors: list, warnings: list) -> list[dict]:
    """Extract RSK assets from ENTERPRISE_RISK_REGISTER_V1.md."""
    risk_file = repo_root / _RSK_FILE
    if not risk_file.exists():
        warnings.append({
            "warning_code": "SOURCE_FILE_MISSING",
            "severity": "WARNING",
            "file_path": str(_RSK_FILE),
            "message": "ENTERPRISE_RISK_REGISTER_V1.md not found — RSK extraction skipped.",
            "action_taken": "SKIPPED",
        })
        return []

    rel_path = str(_RSK_FILE)
    text = risk_file.read_text(encoding="utf-8")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    try:
        doc_meta, _ = read_frontmatter(risk_file)
    except Exception:
        doc_meta = {}

    doc_approved_by = _str(doc_meta.get("approved_by", ""))
    doc_approved_date = _str(doc_meta.get("approved_date", ""))
    doc_created = _str(doc_meta.get("created", ""))
    doc_created_by = _str(doc_meta.get("created_by", ""))
    doc_version = _str(doc_meta.get("version", "1.0"))

    headers = list(RSK_HDR_RE.finditer(text))
    entries: list[dict] = []

    for idx, hdr in enumerate(headers):
        risk_id = hdr.group(1).strip()
        title_raw = hdr.group(2).strip()
        start = hdr.end()
        end = headers[idx + 1].start() if idx + 1 < len(headers) else len(text)
        block = text[start:end]

        try:
            tbl = _parse_kv_table(block)
            paras = _extract_rsk_paragraphs(block)

            lifecycle_raw = tbl.get("Lifecycle status", "APPROVED")
            lifecycle_status = normalise_status(lifecycle_raw)
            afr_raw = tbl.get("Approved for reuse", "Yes")
            approved_for_reuse = afr_raw.strip().lower() in ("yes", "true")

            sections = _parse_section_ids(tbl.get("Proposal sections", ""))
            if not sections:
                sections = ["S-50"]
            patterns = _parse_pattern_nums(tbl.get("Proposal patterns", ""))

            source_assets = _parse_list_field(tbl.get("Source assets", ""))
            related_risks = _parse_list_field(tbl.get("Related risks", ""))
            related_assumptions = _parse_list_field(tbl.get("Related assumptions", ""))

            category = tbl.get("Category", "")
            platforms = tbl.get("Platforms", "")
            likelihood = tbl.get("Likelihood", "")
            impact = tbl.get("Impact", "")
            rating = tbl.get("Rating", "")
            owner = tbl.get("Owner", "")
            owner_role = tbl.get("Owner role", owner)
            owner_bu = tbl.get("Owner business unit", "")
            if not owner_bu:
                owner_bu = platforms.split("/")[0].strip() if platforms else "Oracle"
            review_freq = tbl.get("Review frequency", "Quarterly")
            last_reviewed = tbl.get("Last reviewed", "")
            next_review = tbl.get("Next review", "")
            confidence_level = tbl.get("Confidence level", "")

            supersedes = tbl.get("Supersedes", "")
            if supersedes in ("—", "-"):
                supersedes = ""

            governance_notes = tbl.get("Governance notes", "")
            mandatory_if = tbl.get("Mandatory if", "")
            optional_if = tbl.get("Optional if", "")
            excluded_if = tbl.get("Excluded if", "")
            assembly_priority_label = tbl.get("Assembly priority", "")

            sec_num = 0
            if sections and sections[0].startswith("S-"):
                try:
                    sec_num = int(sections[0].replace("S-", ""))
                except ValueError:
                    pass

            entries.append({
                "asset_id": risk_id,
                "asset_type": "RSK",
                "title": title_raw,
                "version": doc_version,
                "lifecycle_status": lifecycle_status,
                "approved_for_reuse": approved_for_reuse,
                "owner_role": owner_role or owner,
                "owner_business_unit": owner_bu,
                "approval_authority": "BU Lead",
                "governing_standard": "RISK_METADATA_STANDARD V1.0",
                "registry_version_added": "2.0",
                "created": doc_created,
                "created_by": doc_created_by,
                "approved_by": doc_approved_by,
                "approval_date": doc_approved_date,
                "source_file": rel_path,
                "description": paras.get("Risk description", ""),
                "confidence_level": confidence_level,
                "review_frequency": review_freq,
                "last_reviewed": last_reviewed,
                "review_due": next_review,
                "governance_notes": governance_notes or f"Governed by ENTERPRISE_RISK_REGISTER_V1.md.",
                "pattern_applicability": patterns or ["ALL"],
                "proposal_sections": sections,
                "tags": [],
                "source_assets": source_assets,
                "related_assets": related_risks,
                "supersedes": supersedes,
                "superseded_by": "",
                "library_index_ref": rel_path,
                "registry_last_synced": today,
                "validation_status": "",
                "validation_issues": [],
                "assembly_rules": {
                    "mandatory_if": mandatory_if,
                    "optional_if": optional_if,
                    "excluded_if": excluded_if,
                    "assembly_priority": 5,
                    "section_placement": sec_num,
                    "content_source_type": "RISK",
                },
                "rsk_ext": {
                    "category": category,
                    "platforms": platforms,
                    "engagement_types": tbl.get("Engagement types", ""),
                    "likelihood": likelihood,
                    "impact": impact,
                    "rating": rating,
                    "owner": owner,
                    "confidence_level": confidence_level,
                    "source_refs": tbl.get("Source", ""),
                    "source_assets": source_assets,
                    "related_risks": related_risks,
                    "related_assumptions": related_assumptions,
                    "proposal_patterns": patterns,
                    "assembly_priority_label": assembly_priority_label,
                    "risk_description": paras.get("Risk description", ""),
                    "standard_mitigation": paras.get("Standard mitigation", ""),
                    "customisation_guidance": paras.get("Customisation guidance", ""),
                },
            })

        except Exception as exc:
            errors.append({
                "error_code": "EXTRACTION_ERROR",
                "severity": "ERROR",
                "asset_id": risk_id,
                "file_path": rel_path,
                "message": str(exc),
                "action_taken": "SKIPPED",
            })

    return entries


# ─── Phase B: REF extractor ───────────────────────────────────────────────────

def extract_ref(repo_root: Path, errors: list, warnings: list) -> list[dict]:
    """Extract REF assets from REFERENCE_MASTER.md."""
    ref_file = repo_root / _REF_FILE
    if not ref_file.exists():
        warnings.append({
            "warning_code": "SOURCE_FILE_MISSING",
            "severity": "WARNING",
            "file_path": str(_REF_FILE),
            "message": "REFERENCE_MASTER.md not found — REF extraction skipped.",
            "action_taken": "SKIPPED",
        })
        return []

    rel_path = str(_REF_FILE)
    text = ref_file.read_text(encoding="utf-8")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Build tier position map
    tier_positions: list[tuple[int, str]] = [
        (m.start(), m.group(1)) for m in REF_TIER_RE.finditer(text)
    ]

    def _get_tier(pos: int) -> str:
        tier = "Unknown"
        for tp, tn in tier_positions:
            if tp <= pos:
                tier = tn
        return tier

    headers = list(REF_HDR_RE.finditer(text))
    entries: list[dict] = []

    for idx, hdr in enumerate(headers):
        ref_id = hdr.group(1).strip()
        title_raw = re.sub(r"\s+⭐.*$", "", hdr.group(2).strip()).strip()
        tier = _get_tier(hdr.start())

        start = hdr.end()
        end = headers[idx + 1].start() if idx + 1 < len(headers) else len(text)
        block = text[start:end]

        try:
            # Try pipe table first (Gold format), fall back to bullet list (Silver/Bronze)
            tbl = _parse_kv_table(block)
            if not tbl:
                for m in _BULLET_KV_RE.finditer(block):
                    tbl[m.group(1).strip()] = m.group(2).strip()

            client = tbl.get("Client", title_raw)
            industry = tbl.get("Industry", "")
            bu_raw = tbl.get("Business Unit", "") or tbl.get("BU", "")
            if not bu_raw:
                bu_raw = "Oracle" if "ORA" in ref_id else ("Acumatica" if "ACU" in ref_id else "BeBanking")
            letter_date = tbl.get("Letter Date", "")
            signatory = tbl.get("Signatory", "")
            products_raw = tbl.get("Products", "")
            products = [p.strip() for p in products_raw.split(",") if p.strip()] if products_raw else []
            contract_value = tbl.get("Contract Value", "")
            countries = tbl.get("Countries", "")
            named_raw = tbl.get("Named Reference Allowed", "Yes")
            named_reference_allowed = named_raw.strip().lower() in ("yes", "true")
            source_loc = tbl.get("Source", "")
            governance_notes = tbl.get("Governance", "") or tbl.get("Governance notes", "")
            cap_stmts = _parse_list_field(tbl.get("Capability Statements", ""))
            rel_start = tbl.get("Relationship Start", "") or tbl.get("Start", "")

            approved_for_reuse = named_reference_allowed

            if "Oracle" in bu_raw:
                pat_applicability = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "13"]
            elif "Acumatica" in bu_raw:
                pat_applicability = ["11"]
            elif "BeBanking" in bu_raw:
                pat_applicability = ["12"]
            else:
                pat_applicability = ["ALL"]

            entries.append({
                "asset_id": ref_id,
                "asset_type": "REF",
                "title": client,
                "version": "1.0",
                "lifecycle_status": "APPROVED",
                "approved_for_reuse": approved_for_reuse,
                "owner_role": "Account Manager",
                "owner_business_unit": bu_raw,
                "approval_authority": "Account Manager",
                "governing_standard": "KNOWLEDGE_ASSET_STANDARD.md",
                "registry_version_added": "2.0",
                "created": "2026-06-26",
                "created_by": "WP19C — Knowledge Registry Phase B",
                "approved_by": "",
                "approval_date": letter_date,
                "source_file": rel_path,
                "description": f"{client} — {industry}" if industry else client,
                "confidence_level": "",
                "review_frequency": "annual",
                "last_reviewed": "",
                "review_due": "",
                "governance_notes": governance_notes or "Account manager approval required for use in any tender.",
                "pattern_applicability": pat_applicability,
                "proposal_sections": ["S-67", "S-68", "S-69"],
                "tags": [tier.lower()],
                "source_assets": [],
                "related_assets": cap_stmts,
                "supersedes": "",
                "superseded_by": "",
                "library_index_ref": rel_path,
                "registry_last_synced": today,
                "validation_status": "",
                "validation_issues": [],
                "assembly_rules": {
                    "mandatory_if": "",
                    "optional_if": "",
                    "excluded_if": "",
                    "assembly_priority": 5,
                    "section_placement": 67,
                    "content_source_type": "REFERENCE",
                },
                "ref_ext": {
                    "client": client,
                    "industry": industry,
                    "tier": tier,
                    "letter_date": letter_date,
                    "signatory": signatory,
                    "products": products,
                    "contract_value": contract_value,
                    "countries": countries,
                    "named_reference_allowed": named_reference_allowed,
                    "source_location": source_loc,
                    "capability_statements": cap_stmts,
                    "relationship_start": rel_start,
                },
            })

        except Exception as exc:
            errors.append({
                "error_code": "EXTRACTION_ERROR",
                "severity": "ERROR",
                "asset_id": ref_id,
                "file_path": rel_path,
                "message": str(exc),
                "action_taken": "SKIPPED",
            })

    return entries


# ─── Phase B: MTH discovery + extractor ──────────────────────────────────────

def discover_mth_files(repo_root: Path) -> list[Path]:
    """Discover methodology files in 05_Methodologies/ and cross-BU approved content."""
    found: list[Path] = []
    mth_root = repo_root / "05_Methodologies"
    if mth_root.exists():
        for p in sorted(mth_root.rglob("*.md")):
            if p.stem.upper() in ("METHODOLOGY_INDEX", "README", "METHODOLOGY_LIBRARY_STANDARD"):
                continue
            try:
                txt = p.read_text(encoding="utf-8")
                if txt.startswith("---") and "document_id:" in txt[:600]:
                    found.append(p)
            except Exception:
                pass

    # Also include files in 07_Approved_Content whose kb_destination targets 05_Methodologies/
    alt_root = repo_root / "07_Approved_Content" / "Approved" / "Cross_BU"
    if alt_root.exists():
        for p in sorted(alt_root.glob("*.md")):
            if p in found:
                continue
            try:
                txt = p.read_text(encoding="utf-8")
                if txt.startswith("---") and "document_id:" in txt[:600] and "05_Methodologies" in txt:
                    found.append(p)
            except Exception:
                pass

    return found


def extract_mth(mth_path: Path, repo_root: Path,
                errors: list, warnings: list) -> Optional[dict]:
    """Extract MTH asset from a methodology file."""
    try:
        meta, _ = read_frontmatter(mth_path)
    except ValueError as exc:
        errors.append({
            "error_code": "EXTRACTION_ERROR",
            "severity": "ERROR",
            "file_path": str(mth_path.relative_to(repo_root)),
            "message": str(exc),
            "action_taken": "SKIPPED",
        })
        return None

    rel_path = str(mth_path.relative_to(repo_root))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    doc_id = _str(meta.get("document_id", "")) or mth_path.stem.replace("_", "-").upper()
    title = _str(meta.get("title", ""))
    version_raw = _str(meta.get("version", "1.0"))
    version = version_raw.split()[0] if version_raw else "1.0"

    raw_status = _str(meta.get("source_status", "") or meta.get("status", ""))
    lifecycle_status = normalise_status(raw_status)

    afr_raw = meta.get("approved_for_reuse", None)
    approved_for_reuse = _bool(afr_raw) if afr_raw is not None else (lifecycle_status == "APPROVED")

    bu = _str(meta.get("bu", ""))
    scope = _str(meta.get("scope", ""))
    kb_dest = _str(meta.get("kb_destination", ""))
    wave = _str(meta.get("wave", ""))

    platforms_raw = meta.get("platforms", [])
    if isinstance(platforms_raw, list):
        platforms = platforms_raw
    elif isinstance(platforms_raw, str) and platforms_raw:
        platforms = [platforms_raw]
    else:
        platforms = []

    bu_lower = bu.lower()
    if "oracle" in bu_lower:
        pat_applicability = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    elif "acumatica" in bu_lower:
        pat_applicability = ["11"]
    elif "bebanking" in bu_lower:
        pat_applicability = ["12"]
    elif "cross" in bu_lower:
        pat_applicability = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12"]
    else:
        pat_applicability = ["ALL"]

    deployment_note = ""
    if kb_dest and "05_Methodologies" in kb_dest and "07_Approved_Content" in str(mth_path):
        deployment_note = f"Deployment anomaly: file in 07_Approved_Content/; target is {kb_dest}"
        if deployment_note:
            warnings.append({
                "warning_code": "MTH_DEPLOYMENT_ANOMALY",
                "severity": "WARNING",
                "asset_id": doc_id,
                "file_path": rel_path,
                "message": deployment_note,
                "action_taken": "EXTRACTED_FROM_CURRENT_LOCATION",
            })

    return {
        "asset_id": doc_id,
        "asset_type": "MTH",
        "title": title,
        "version": version,
        "lifecycle_status": lifecycle_status,
        "approved_for_reuse": approved_for_reuse,
        "owner_role": "BU Lead",
        "owner_business_unit": bu or "Oracle",
        "approval_authority": "BU Lead",
        "governing_standard": "METHODOLOGY_LIBRARY_STANDARD.md",
        "registry_version_added": "2.0",
        "created": _str(meta.get("created", "")),
        "created_by": _str(meta.get("created_by", "")),
        "approved_by": _str(meta.get("approved_by", "")),
        "approval_date": _str(meta.get("approval_date", "")),
        "source_file": rel_path,
        "description": scope,
        "confidence_level": "",
        "review_frequency": "annual",
        "last_reviewed": _str(meta.get("review_date", "")),
        "review_due": "",
        "governance_notes": _str(meta.get("review_notes", "")) or "Governed by METHODOLOGY_LIBRARY_STANDARD.md.",
        "pattern_applicability": pat_applicability,
        "proposal_sections": ["S-34"],
        "tags": [],
        "source_assets": [],
        "related_assets": [],
        "supersedes": "",
        "superseded_by": "",
        "library_index_ref": "05_Methodologies/METHODOLOGY_INDEX.md",
        "registry_last_synced": today,
        "validation_status": "",
        "validation_issues": [],
        "assembly_rules": {
            "mandatory_if": "",
            "optional_if": "",
            "excluded_if": "",
            "assembly_priority": 5,
            "section_placement": 34,
            "content_source_type": "METHODOLOGY",
        },
        "mth_ext": {
            "bu": bu,
            "scope": scope,
            "platforms": platforms,
            "kb_destination": kb_dest,
            "wave": wave,
            "deployment_note": deployment_note,
        },
    }


# ─── Phase B: PAT extractor ───────────────────────────────────────────────────

def extract_pat(repo_root: Path, errors: list, warnings: list) -> list[dict]:
    """Extract PAT assets from PROPOSAL_PATTERN_ENGINE.md Section 3."""
    pat_file = repo_root / _PAT_FILE
    if not pat_file.exists():
        warnings.append({
            "warning_code": "SOURCE_FILE_MISSING",
            "severity": "WARNING",
            "file_path": str(_PAT_FILE),
            "message": "PROPOSAL_PATTERN_ENGINE.md not found — PAT extraction skipped.",
            "action_taken": "SKIPPED",
        })
        return []

    rel_path = str(_PAT_FILE)
    text = pat_file.read_text(encoding="utf-8")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    sec3_match = PAT_SECTION3_RE.search(text)
    if not sec3_match:
        errors.append({
            "error_code": "EXTRACTION_ERROR",
            "severity": "ERROR",
            "file_path": rel_path,
            "message": "Section 3 (Pattern Reference Table) not found in PROPOSAL_PATTERN_ENGINE.md.",
            "action_taken": "SKIPPED",
        })
        return []

    # Limit search to Section 3 block (up to next ## heading)
    sec4_match = re.search(r"^## 4\.", text[sec3_match.end():], re.MULTILINE)
    sec3_end = sec3_match.end() + (sec4_match.start() if sec4_match else 2000)
    table_block = text[sec3_match.start():sec3_end]

    entries: list[dict] = []
    for line in table_block.splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 8:
            continue
        pat_num = cells[1].strip()
        if not pat_num.isdigit():
            continue
        name = cells[2].strip()
        platform = cells[3].strip()
        engagement = cells[4].strip()
        duration = cells[5].strip()
        methodology = cells[6].strip()

        if not name or not platform:
            continue

        sections_in, sections_ex = _PAT_SCOPE.get(pat_num, ([], []))

        if "Oracle" in platform or "EBS" in platform or "OIC" in platform:
            bu = "Oracle"
        elif "Acumatica" in platform:
            bu = "Acumatica"
        elif "BeBanking" in platform:
            bu = "BeBanking"
        else:
            bu = "ALL"

        mth_ref = methodology.strip() if methodology not in ("None", "—", "") else ""

        entries.append({
            "asset_id": f"PAT-{int(pat_num):02d}",
            "asset_type": "PAT",
            "title": name,
            "version": "1.0",
            "lifecycle_status": "APPROVED",
            "approved_for_reuse": True,
            "owner_role": "BU Lead",
            "owner_business_unit": bu,
            "approval_authority": "BU Lead",
            "governing_standard": "PROPOSAL_PATTERN_ENGINE.md",
            "registry_version_added": "2.0",
            "created": "2026-06-25",
            "created_by": "WP18C.3",
            "approved_by": "WP18C.3",
            "approval_date": "2026-06-25",
            "source_file": rel_path,
            "description": f"{engagement} pattern for {platform}.",
            "confidence_level": "",
            "review_frequency": "annual",
            "last_reviewed": "2026-06-25",
            "review_due": "",
            "governance_notes": "Governed by PROPOSAL_PATTERN_ENGINE.md v1.0. BU Lead approved via WP18C.3.",
            "pattern_applicability": [pat_num],
            "proposal_sections": sections_in,
            "tags": [engagement.lower()],
            "source_assets": [],
            "related_assets": [],
            "supersedes": "",
            "superseded_by": "",
            "library_index_ref": rel_path,
            "registry_last_synced": today,
            "validation_status": "",
            "validation_issues": [],
            "assembly_rules": {
                "mandatory_if": "",
                "optional_if": "",
                "excluded_if": "",
                "assembly_priority": 5,
                "section_placement": 0,
                "content_source_type": "PATTERN",
            },
            "pat_ext": {
                "pattern_number": int(pat_num),
                "platform": platform,
                "engagement": engagement,
                "typical_duration": duration,
                "methodology_ref": mth_ref,
                "sections_in_scope": sections_in,
                "sections_excluded": sections_ex,
            },
        })

    return entries


# ─── Phase B: SEC extractor ───────────────────────────────────────────────────

def extract_sec(repo_root: Path, errors: list, warnings: list) -> list[dict]:
    """Extract SEC assets from PROPOSAL_SECTION_LIBRARY.md."""
    sec_file = repo_root / _SEC_FILE
    if not sec_file.exists():
        warnings.append({
            "warning_code": "SOURCE_FILE_MISSING",
            "severity": "WARNING",
            "file_path": str(_SEC_FILE),
            "message": "PROPOSAL_SECTION_LIBRARY.md not found — SEC extraction skipped.",
            "action_taken": "SKIPPED",
        })
        return []

    rel_path = str(_SEC_FILE)
    text = sec_file.read_text(encoding="utf-8")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Build category position map
    cat_positions: list[tuple[int, str]] = [
        (m.start(), m.group(1).strip()) for m in SEC_CATEGORY_RE.finditer(text)
    ]

    def _get_category(pos: int) -> str:
        cat = "General"
        for cp, cn in cat_positions:
            if cp <= pos:
                cat = cn
        return cat

    entries: list[dict] = []
    seen_ids: set[str] = set()
    lines_with_pos = [(i, line) for i, line in enumerate(text.splitlines())]

    # Compute character offset for each line to determine category
    char_offsets: list[int] = []
    offset = 0
    for line in text.splitlines():
        char_offsets.append(offset)
        offset += len(line) + 1

    for line_idx, line in lines_with_pos:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 12:
            continue
        sec_id = cells[1].strip()
        if not re.match(r"^[SA]-\d+", sec_id):
            continue
        if sec_id in seen_ids:
            continue
        seen_ids.add(sec_id)

        name = cells[2].strip()
        obligation = cells[3].strip()
        location = cells[4].strip()
        source_repo = cells[5].strip()
        deterministic = _parse_bool_cell(cells[6]) if len(cells) > 6 else False
        ai_assisted = _parse_bool_cell(cells[7]) if len(cells) > 7 else False
        human_review_raw = cells[8].strip() if len(cells) > 8 else ""
        human_review = _parse_bool_cell(human_review_raw) or (
            bool(human_review_raw) and human_review_raw.lower() not in ("no", "false", "0", "")
        )
        current_pct = _parse_pct(cells[9]) if len(cells) > 9 else 0
        target_pct = _parse_pct(cells[10]) if len(cells) > 10 else 0

        if not name or name.upper() in ("SECTION NAME", "NAME"):
            continue

        char_pos = char_offsets[line_idx] if line_idx < len(char_offsets) else 0
        category = _get_category(char_pos)

        # Pattern applicability
        obl_upper = obligation.upper()
        if "AMS" in obl_upper and "COND" in obl_upper:
            pat_applicability = ["13"]
        elif "ORA" in obl_upper:
            pat_applicability = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        elif "ACU" in obl_upper and "AMS" in obl_upper:
            pat_applicability = ["11"]
        elif "ACU" in obl_upper:
            pat_applicability = ["11"]
        elif "BB" in obl_upper:
            pat_applicability = ["12"]
        else:
            pat_applicability = ["ALL"]

        section_num = 0
        num_m = re.search(r"(\d+)", sec_id)
        if num_m:
            section_num = int(num_m.group(1))

        entries.append({
            "asset_id": sec_id,
            "asset_type": "SEC",
            "title": name,
            "version": "1.2",
            "lifecycle_status": "APPROVED",
            "approved_for_reuse": True,
            "owner_role": "BU Lead",
            "owner_business_unit": "ALL",
            "approval_authority": "BU Lead",
            "governing_standard": "PROPOSAL_SECTION_LIBRARY.md",
            "registry_version_added": "2.0",
            "created": "2026-06-26",
            "created_by": "WP18C.1",
            "approved_by": "WP18C.1",
            "approval_date": "2026-06-26",
            "source_file": rel_path,
            "description": f"{name} — {category}",
            "confidence_level": "",
            "review_frequency": "annual",
            "last_reviewed": "2026-06-26",
            "review_due": "",
            "governance_notes": "Governed by PROPOSAL_SECTION_LIBRARY.md v1.2.",
            "pattern_applicability": pat_applicability,
            "proposal_sections": [sec_id],
            "tags": [],
            "source_assets": [],
            "related_assets": [],
            "supersedes": "",
            "superseded_by": "",
            "library_index_ref": rel_path,
            "registry_last_synced": today,
            "validation_status": "",
            "validation_issues": [],
            "assembly_rules": {
                "mandatory_if": "",
                "optional_if": "",
                "excluded_if": "",
                "assembly_priority": 5,
                "section_placement": section_num,
                "content_source_type": "SECTION",
            },
            "sec_ext": {
                "section_id": sec_id,
                "section_category": category,
                "obligation": obligation,
                "typical_location": location,
                "source_repository": source_repo,
                "deterministic": deterministic,
                "ai_assisted": ai_assisted,
                "human_review_required": human_review,
                "current_automation_pct": current_pct,
                "target_automation_pct": target_pct,
            },
        })

    return entries


# ─── Relationship builder ─────────────────────────────────────────────────────

def build_relationships(core_registry: list[dict],
                        assumption_registry: list[dict]) -> list[dict]:
    """Build all relationship types: REL-001 through REL-005."""
    pack_to_asms: dict[str, list[str]] = {}
    for asm in assumption_registry:
        pid = asm["asm_ext"]["parent_pack_id"]
        pack_to_asms.setdefault(pid, []).append(asm["asset_id"])

    relationships: list[dict] = []

    # REL-001: ASP CONTAINS ASM (Phase A)
    for entry in core_registry:
        if entry["asset_type"] != "ASP":
            continue
        asp_id = entry["asset_id"]
        for asm_id in sorted(pack_to_asms.get(asp_id, [])):
            relationships.append({
                "source_id": asp_id,
                "source_type": "ASP",
                "relationship_type": "CON",
                "relationship_label": "CONTAINS",
                "target_id": asm_id,
                "target_type": "ASM",
                "declared_in": "KRPE REL-001 (asm_ext.parent_pack_id)",
                "rule_id": "REL-001",
                "resolved": True,
                "bidirectional": False,
            })

    # Phase B relationships
    cap_ids: set[str] = {e["asset_id"] for e in core_registry if e["asset_type"] == "CAP"}
    sec_ids: set[str] = {e["asset_id"] for e in core_registry if e["asset_type"] == "SEC"}

    # Build PAT num → asset_id map
    pat_by_num: dict[str, str] = {}
    for e in core_registry:
        if e["asset_type"] == "PAT":
            num = str(e["pat_ext"]["pattern_number"])
            pat_by_num[num] = e["asset_id"]

    # Build MTH lookup for fuzzy matching: includes MTH entries AND dual-purpose CAPs
    mth_by_prefix: dict[str, str] = {}
    for e in core_registry:
        if e["asset_type"] in ("MTH", "CAP"):
            eid = e["asset_id"]
            mth_by_prefix[eid] = eid
            parts = eid.split("-")
            if len(parts) >= 3:
                short = "-".join(parts[:3])
                mth_by_prefix.setdefault(short, eid)
            # Also index Wave IDs at W_S_ level (e.g. "W2S1-005" → "W2S1-005-ORA-...")
            if len(parts) >= 2 and re.match(r"W\d+S\d+-\d+", "-".join(parts[:2])):
                mth_by_prefix.setdefault("-".join(parts[:2]), eid)

    # REL-002: PAT INCLUDES SEC (Phase B)
    for pat in (e for e in core_registry if e["asset_type"] == "PAT"):
        pat_id = pat["asset_id"]
        for sec_id in pat["pat_ext"]["sections_in_scope"]:
            if sec_id in sec_ids:
                relationships.append({
                    "source_id": pat_id,
                    "source_type": "PAT",
                    "relationship_type": "INC",
                    "relationship_label": "INCLUDES",
                    "target_id": sec_id,
                    "target_type": "SEC",
                    "declared_in": "PROPOSAL_PATTERN_ENGINE.md §6 — section scope tables",
                    "rule_id": "REL-002",
                    "resolved": True,
                    "bidirectional": False,
                })

    # REL-003: PAT USES MTH (Phase B — also resolves to dual-purpose CAP entries)
    asset_type_by_id: dict[str, str] = {e["asset_id"]: e["asset_type"] for e in core_registry}
    for pat in (e for e in core_registry if e["asset_type"] == "PAT"):
        mth_ref = pat["pat_ext"].get("methodology_ref", "")
        if not mth_ref:
            continue
        resolved_mth = mth_by_prefix.get(mth_ref, "")
        if not resolved_mth:
            for k, v in mth_by_prefix.items():
                if mth_ref in k:
                    resolved_mth = v
                    break
        if resolved_mth:
            target_type = asset_type_by_id.get(resolved_mth, "MTH")
            relationships.append({
                "source_id": pat["asset_id"],
                "source_type": "PAT",
                "relationship_type": "USE",
                "relationship_label": "USES",
                "target_id": resolved_mth,
                "target_type": target_type,
                "declared_in": "PROPOSAL_PATTERN_ENGINE.md §3 — Methodology column",
                "rule_id": "REL-003",
                "resolved": True,
                "bidirectional": False,
            })

    # REL-004: REF SUPPORTS CAP (Phase B — Capability Statements column)
    for ref in (e for e in core_registry if e["asset_type"] == "REF"):
        for cap_id in ref.get("ref_ext", {}).get("capability_statements", []):
            if cap_id in cap_ids:
                relationships.append({
                    "source_id": ref["asset_id"],
                    "source_type": "REF",
                    "relationship_type": "SUP",
                    "relationship_label": "SUPPORTS",
                    "target_id": cap_id,
                    "target_type": "CAP",
                    "declared_in": "REFERENCE_MASTER.md — Capability Statements column",
                    "rule_id": "REL-004",
                    "resolved": True,
                    "bidirectional": False,
                })

    # REL-005: RSK APPLIES_TO PAT (Phase B — Proposal patterns field)
    for rsk in (e for e in core_registry if e["asset_type"] == "RSK"):
        for pat_num in rsk.get("rsk_ext", {}).get("proposal_patterns", []):
            if pat_num in pat_by_num:
                relationships.append({
                    "source_id": rsk["asset_id"],
                    "source_type": "RSK",
                    "relationship_type": "APP",
                    "relationship_label": "APPLIES_TO",
                    "target_id": pat_by_num[pat_num],
                    "target_type": "PAT",
                    "declared_in": "ENTERPRISE_RISK_REGISTER_V1.md — Proposal patterns field",
                    "rule_id": "REL-005",
                    "resolved": True,
                    "bidirectional": False,
                })

    return relationships


# ─── Index builder ────────────────────────────────────────────────────────────

def build_indexes(core_registry: list[dict],
                  assumption_registry: list[dict],
                  rel_graph: list[dict]) -> dict:
    all_entries = core_registry + assumption_registry

    # asset_by_type
    asset_by_type: dict[str, list[str]] = {}
    for e in all_entries:
        asset_by_type.setdefault(e["asset_type"], []).append(e["asset_id"])
    for t in asset_by_type:
        asset_by_type[t] = sorted(asset_by_type[t])

    # lifecycle_by_status
    lifecycle_by_status: dict[str, list[str]] = {}
    for e in all_entries:
        s = e.get("lifecycle_status", "")
        lifecycle_by_status.setdefault(s, []).append(e["asset_id"])
    for s in lifecycle_by_status:
        lifecycle_by_status[s] = sorted(lifecycle_by_status[s])

    # approved_assets
    approved_assets = sorted(
        e["asset_id"] for e in all_entries if e.get("approved_for_reuse")
    )

    # pack_to_assumptions / assumption_to_pack
    pack_to_assumptions: dict[str, list[str]] = {}
    assumption_to_pack: dict[str, str] = {}
    for asm in assumption_registry:
        pid = asm["asm_ext"]["parent_pack_id"]
        pack_to_assumptions.setdefault(pid, []).append(asm["asset_id"])
        assumption_to_pack[asm["asset_id"]] = pid
    for pid in pack_to_assumptions:
        pack_to_assumptions[pid] = sorted(pack_to_assumptions[pid])

    # platform_capability_map
    platform_cap_map: dict[str, dict[str, list[str]]] = {}
    for cap in core_registry:
        if cap["asset_type"] != "CAP":
            continue
        ext = cap.get("cap_ext", {})
        platform = ext.get("platform", "") or cap.get("owner_business_unit", "") or "Unknown"
        pa = ext.get("product_area_path", "") or "_default"
        platform_cap_map.setdefault(platform, {}).setdefault(pa, []).append(cap["asset_id"])
    for plt in platform_cap_map:
        for pa in platform_cap_map[plt]:
            platform_cap_map[plt][pa] = sorted(platform_cap_map[plt][pa])

    # supersession_chains
    supersession_chains: dict[str, dict] = {}
    for e in all_entries:
        sup = e.get("supersedes", "")
        sup_by = e.get("superseded_by", "")
        if sup or sup_by:
            supersession_chains[e["asset_id"]] = {
                "supersedes": sup,
                "superseded_by": sup_by,
            }

    # orphan detection (Phase A: CAP entries with no relationships)
    related_ids: set[str] = set()
    for rel in rel_graph:
        related_ids.add(rel["source_id"])
        related_ids.add(rel["target_id"])

    orphan_caps = sorted(
        e["asset_id"] for e in core_registry
        if e["asset_type"] == "CAP" and e["asset_id"] not in related_ids
    )

    # Phase B index construction
    pattern_to_sections: dict[str, list[str]] = {}
    section_to_patterns: dict[str, list[str]] = {}
    pattern_to_capabilities: dict[str, list[str]] = {}
    capability_to_sections: dict[str, list[str]] = {}
    risk_to_assumptions: dict[str, list[str]] = {}
    mandatory_risks: list[str] = []
    pattern_to_risks: dict[str, list[str]] = {}
    capability_to_references: dict[str, list[str]] = {}
    pattern_to_methodologies: dict[str, str] = {}

    all_entries = core_registry + assumption_registry

    for e in core_registry:
        atype = e["asset_type"]

        if atype == "PAT":
            pat_id = e["asset_id"]
            pat_num = str(e["pat_ext"]["pattern_number"])
            secs_in = e["pat_ext"]["sections_in_scope"]
            pattern_to_sections[pat_id] = secs_in
            for sec in secs_in:
                section_to_patterns.setdefault(sec, []).append(pat_id)
            mth_ref = e["pat_ext"].get("methodology_ref", "")
            if mth_ref:
                pattern_to_methodologies[pat_id] = mth_ref

        elif atype == "CAP":
            cap_id = e["asset_id"]
            secs = e.get("proposal_sections", [])
            if secs:
                capability_to_sections[cap_id] = sorted(set(secs))
            for pat_num in e.get("pattern_applicability", []):
                if pat_num != "ALL":
                    pattern_to_capabilities.setdefault(f"PAT-{int(pat_num):02d}", []).append(cap_id)

        elif atype == "RSK":
            rsk_id = e["asset_id"]
            ext = e.get("rsk_ext", {})
            related_asm = ext.get("related_assumptions", [])
            if related_asm:
                risk_to_assumptions[rsk_id] = sorted(related_asm)
            mif = e.get("assembly_rules", {}).get("mandatory_if", "")
            if mif:
                mandatory_risks.append(rsk_id)
            for pat_num in ext.get("proposal_patterns", []):
                pat_key = f"PAT-{int(pat_num):02d}" if pat_num.isdigit() else pat_num
                pattern_to_risks.setdefault(pat_key, []).append(rsk_id)

        elif atype == "REF":
            ref_id = e["asset_id"]
            for cap_id in e.get("ref_ext", {}).get("capability_statements", []):
                capability_to_references.setdefault(cap_id, []).append(ref_id)

    # Sort index lists
    for d in (pattern_to_sections, section_to_patterns, pattern_to_capabilities,
              capability_to_sections, risk_to_assumptions, pattern_to_risks,
              capability_to_references):
        for k in d:
            d[k] = sorted(set(d[k]))

    mandatory_risks = sorted(set(mandatory_risks))

    # Update orphan detection: CAPs with no relationships (Phase B: any relationship type)
    related_ids: set[str] = set()
    for rel in rel_graph:
        related_ids.add(rel["source_id"])
        related_ids.add(rel["target_id"])

    orphan_caps_b = sorted(
        e["asset_id"] for e in core_registry
        if e["asset_type"] == "CAP" and e["asset_id"] not in related_ids
    )

    return {
        "asset_by_type": asset_by_type,
        "lifecycle_by_status": lifecycle_by_status,
        "approved_assets": approved_assets,
        "pattern_to_sections": pattern_to_sections,
        "section_to_patterns": section_to_patterns,
        "pattern_to_capabilities": pattern_to_capabilities,
        "capability_to_sections": capability_to_sections,
        "cap_to_assumption_packs": {},
        "pack_to_assumptions": pack_to_assumptions,
        "assumption_to_pack": assumption_to_pack,
        "risk_to_assumptions": risk_to_assumptions,
        "mandatory_risks": mandatory_risks,
        "pattern_to_risks": pattern_to_risks,
        "capability_to_references": capability_to_references,
        "pattern_to_methodologies": pattern_to_methodologies,
        "platform_capability_map": platform_cap_map,
        "governance_category_map": {},
        "supersession_chains": supersession_chains,
        "orphan_detection": {
            "cap_assets_with_no_relationships_phase_b": orphan_caps_b,
            "note": "Phase B complete. CAPs with no relationships are listed above.",
        },
        "pattern_readiness_summary": {},
    }


# ─── Registry writers ─────────────────────────────────────────────────────────

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _counts_by_type(entries: list[dict]) -> dict:
    c: dict[str, int] = {}
    for e in entries:
        c[e["asset_type"]] = c.get(e["asset_type"], 0) + 1
    return c


def write_core_registry(out_dir: Path, build_id: str, build_mode: str,
                        repo_root: Path, core_registry: list,
                        assumption_registry: list) -> Path:
    by_type = _counts_by_type(core_registry)
    total = len(core_registry)

    meta = {
        "schema_version": SCHEMA_VERSION,
        "population_rules_version": POPULATION_RULES_VERSION,
        "generated_at": _now_iso(),
        "generated_by": f"KRPE v{VERSION}",
        "build_id": build_id,
        "build_mode": build_mode,
        "source_repo_root": str(repo_root),
        "total_entries": total,
        "entries_by_type": {
            "CAP": by_type.get("CAP", 0),
            "ASP": by_type.get("ASP", 0),
            "RSK": by_type.get("RSK", 0),
            "MTH": by_type.get("MTH", 0),
            "REF": by_type.get("REF", 0),
            "PAT": by_type.get("PAT", 0),
            "SEC": by_type.get("SEC", 0),
        },
        "health_summary": {
            "approved_count": sum(1 for e in core_registry if e.get("lifecycle_status") == "APPROVED"),
            "draft_count": sum(1 for e in core_registry if e.get("lifecycle_status") == "DRAFT"),
            "approved_for_reuse_count": sum(1 for e in core_registry if e.get("approved_for_reuse")),
        },
    }

    out_path = out_dir / "KNOWLEDGE_ASSET_REGISTRY.yaml"
    out_path.write_text(
        "---\n" + _dump({"registry_metadata": meta, "assets": core_registry}),
        encoding="utf-8",
    )
    return out_path


def write_assumptions_registry(out_dir: Path, build_id: str,
                                assumption_registry: list) -> Path:
    by_pack: dict[str, int] = {}
    for asm in assumption_registry:
        pid = asm["asm_ext"]["parent_pack_id"]
        by_pack[pid] = by_pack.get(pid, 0) + 1

    meta = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": _now_iso(),
        "build_id": build_id,
        "total_asm_entries": len(assumption_registry),
        "parent_pack_count": len(by_pack),
        "entries_by_pack": dict(sorted(by_pack.items())),
    }

    out_path = out_dir / "KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml"
    out_path.write_text(
        "---\n" + _dump({"registry_metadata": meta, "assumptions": assumption_registry}),
        encoding="utf-8",
    )
    return out_path


def write_relationship_graph(out_dir: Path, build_id: str,
                              rel_graph: list) -> Path:
    by_type: dict[str, int] = {}
    for rel in rel_graph:
        t = rel["relationship_type"]
        by_type[t] = by_type.get(t, 0) + 1

    meta = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": _now_iso(),
        "build_id": build_id,
        "total_relationships": len(rel_graph),
        "relationships_by_type": dict(sorted(by_type.items())),
        "phase": "A+B — CON/INC/USE/SUP/APP relationships. Full graph.",
    }

    out_path = out_dir / "KNOWLEDGE_RELATIONSHIP_GRAPH.yaml"
    out_path.write_text(
        "---\n" + _dump({"graph_metadata": meta, "relationships": rel_graph}),
        encoding="utf-8",
    )
    return out_path


def write_lookup_index(out_dir: Path, build_id: str, indexes: dict) -> Path:
    meta = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": _now_iso(),
        "build_id": build_id,
        "total_indexes": len(indexes),
        "phase": "A+B — CAP/ASP/ASM/RSK/MTH/REF/PAT/SEC. Full registry.",
    }

    out_path = out_dir / "KNOWLEDGE_LOOKUP_INDEX.yaml"
    out_path.write_text(
        "---\n" + _dump({"index_metadata": meta, "indexes": indexes}),
        encoding="utf-8",
    )
    return out_path


def write_build_report(reports_dir: Path, build_id: str, build_mode: str,
                       build_start: float, repo_root: Path,
                       files_scanned: int, core_registry: list,
                       assumption_registry: list, errors: list, warnings: list,
                       output_files: list, discovery_log: list) -> Path:
    duration = round(time.time() - build_start, 2)
    has_issues = bool(errors or warnings)
    build_status = "SUCCESS_WITH_WARNINGS" if has_issues else "SUCCESS"

    by_type = _counts_by_type(core_registry)

    recs: list[dict] = []
    mismatches = [w for w in warnings if w.get("warning_code") == "ASSUMPTION_COUNT_MISMATCH"]
    if mismatches:
        recs.append({
            "priority": "HIGH",
            "recommendation": (
                f"{len(mismatches)} packs have assumption_count mismatch. "
                "Review pack files and update frontmatter declaration."
            ),
        })
    recs.append({
        "priority": "INFO",
        "recommendation": (
            "Phase A+B complete. Registry V1.0 operational. "
            "Next: KVE Phase B (76-rule set), AREL evaluator, WP18D Risk Selection Engine."
        ),
    })

    report = {
        "build_metadata": {
            "report_type": "REGISTRY_BUILD_REPORT",
            "schema_version": SCHEMA_VERSION,
            "build_id": build_id,
            "build_mode": build_mode,
            "generated_at": _now_iso(),
            "generated_by": f"KRPE v{VERSION}",
            "source_repo": str(repo_root),
            "population_rules_version": POPULATION_RULES_VERSION,
            "build_duration_seconds": duration,
            "build_status": build_status,
            "phase": "A+B (CAP/ASP/ASM/RSK/MTH/REF/PAT/SEC)",
        },
        "summary": {
            "files_scanned": files_scanned,
            "total_assets_extracted": len(core_registry) + len(assumption_registry),
            "extraction_errors": len(errors),
            "extraction_warnings": len(warnings),
            "entries_by_type": {
                "CAP": by_type.get("CAP", 0),
                "ASP": by_type.get("ASP", 0),
                "ASM": len(assumption_registry),
                "RSK": by_type.get("RSK", 0), "MTH": by_type.get("MTH", 0),
            "REF": by_type.get("REF", 0), "PAT": by_type.get("PAT", 0),
            "SEC": by_type.get("SEC", 0),
            },
        },
        "extraction_errors": errors,
        "extraction_warnings": warnings,
        "duplicate_id_conflicts": [],
        "discovery_log": discovery_log,
        "output_files_written": output_files,
        "recommendations": recs,
    }

    today_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    existing = list(reports_dir.glob(f"REGISTRY_BUILD_REPORT_{today_str}-*.yaml"))
    seq = len(existing) + 1
    filename = f"REGISTRY_BUILD_REPORT_{today_str}-{seq:03d}.yaml"

    out_path = reports_dir / filename
    out_path.write_text("---\n" + _dump(report), encoding="utf-8")
    return out_path


def write_build_manifest(repo_root: Path, build_id: str,
                          processed_files: list) -> Path:
    state_dir = repo_root / ".krpe_state"
    state_dir.mkdir(exist_ok=True)

    manifest = {
        "manifest_metadata": {
            "build_id": build_id,
            "generated_at": _now_iso(),
            "krpe_version": VERSION,
            "schema_version": SCHEMA_VERSION,
            "population_rules_version": POPULATION_RULES_VERSION,
        },
        "files": processed_files,
    }

    out_path = state_dir / "BUILD_MANIFEST.yaml"
    out_path.write_text("---\n" + _dump(manifest), encoding="utf-8")
    return out_path


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ─── Main ─────────────────────────────────────────────────────────────────────

def run(repo_root: Path, build_mode: str = "FULL") -> None:
    build_start = time.time()
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    build_id = f"BUILD-{ts}"

    output_dir = repo_root / "00_Governance" / "Knowledge_Standards"
    reports_dir = repo_root / "08_Commercial" / "Reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    errors: list[dict] = []
    warnings: list[dict] = []
    discovery_log: list[str] = []
    processed_files: list[dict] = []

    sep = "=" * 64
    print(f"\n{sep}")
    print(f"KRPE Phase A+B — {build_mode} build  |  {build_id}")
    print(f"Repository: {repo_root}")
    print(f"{sep}\n")

    # ── Phase 1: Discovery ─────────────────────────────────────────────────
    print("Phase 1 — Discovery")
    cap_rows = discover_cap_rows(repo_root)
    print(f"  CAP: {len(cap_rows)} rows from MASTER_CAPABILITY_INDEX.md")
    discovery_log.append(f"CAP: {len(cap_rows)} rows discovered from {MASTER_INDEX_PATH}")

    asp_files = discover_asp_files(repo_root)
    print(f"  ASP: {len(asp_files)} pack files discovered")
    for f in asp_files:
        discovery_log.append(f"ASP: {f.relative_to(repo_root)}")

    mth_files = discover_mth_files(repo_root)
    print(f"  MTH: {len(mth_files)} methodology files discovered")
    for f in mth_files:
        discovery_log.append(f"MTH: {f.relative_to(repo_root)}")

    files_scanned = len(cap_rows) + len(asp_files) + len(mth_files) + 4  # +4 for RSK/REF/PAT/SEC source files

    # ── Phase 2: Extraction ────────────────────────────────────────────────
    print("\nPhase 2 — Extraction")
    core_registry: list[dict] = []
    assumption_registry: list[dict] = []
    seen_ids: set[str] = set()

    # ASP + ASM first (dependency order)
    print(f"  Extracting {len(asp_files)} assumption packs ...")
    for pack_path in asp_files:
        asp_entry, asm_entries = extract_asp_and_asms(pack_path, repo_root, errors, warnings)
        if asp_entry is None:
            continue

        pack_id = asp_entry["asset_id"]
        if pack_id in seen_ids:
            errors.append({
                "error_code": "DUPLICATE_ID",
                "severity": "ERROR",
                "asset_id": pack_id,
                "file_path": asp_entry["source_file"],
                "message": f"Duplicate ASP ID: {pack_id}",
                "action_taken": "SKIPPED",
            })
            continue

        seen_ids.add(pack_id)
        core_registry.append(asp_entry)

        asm_seen: set[str] = set()
        for asm in asm_entries:
            asm_id = asm["asset_id"]
            if asm_id in seen_ids or asm_id in asm_seen:
                warnings.append({
                    "warning_code": "DUPLICATE_ASM_ID",
                    "severity": "WARNING",
                    "asset_id": asm_id,
                    "file_path": asp_entry["source_file"],
                    "message": f"Duplicate ASM ID '{asm_id}' in pack {pack_id} — skipped.",
                    "action_taken": "SKIPPED",
                })
                continue
            seen_ids.add(asm_id)
            asm_seen.add(asm_id)
            assumption_registry.append(asm)

        n_asm = len([a for a in assumption_registry
                     if a["asm_ext"]["parent_pack_id"] == pack_id])
        print(f"    {pack_id}: {n_asm} assumptions")

        processed_files.append({
            "path": str(pack_path.relative_to(repo_root)),
            "mtime": int(pack_path.stat().st_mtime),
            "sha256": _sha256(pack_path),
            "asset_ids_extracted": [pack_id],
            "asset_types": ["ASP", "ASM"],
            "asm_count": n_asm,
        })

    # CAP extraction
    print(f"\n  Extracting {len(cap_rows)} capability assets ...")
    for index_row in cap_rows:
        cap = extract_cap(index_row, repo_root, errors, warnings)
        if cap is None:
            continue

        asset_id = cap["asset_id"]
        if asset_id in seen_ids:
            errors.append({
                "error_code": "DUPLICATE_ID",
                "severity": "ERROR",
                "asset_id": asset_id,
                "file_path": cap["source_file"],
                "message": f"Duplicate CAP ID: {asset_id}",
                "action_taken": "SKIPPED",
            })
            continue

        seen_ids.add(asset_id)
        core_registry.append(cap)

        src = cap["source_file"]
        if src:
            fpath = repo_root / src
            if fpath.exists():
                processed_files.append({
                    "path": src,
                    "mtime": int(fpath.stat().st_mtime),
                    "sha256": _sha256(fpath),
                    "asset_ids_extracted": [asset_id],
                    "asset_types": ["CAP"],
                })

    # ── Phase B extraction (AD-007 order: PAT → SEC → MTH → REF → RSK) ────
    print(f"\n  [Phase B] Extracting PAT assets ...")
    for entry in extract_pat(repo_root, errors, warnings):
        pid = entry["asset_id"]
        if pid in seen_ids:
            errors.append({"error_code": "DUPLICATE_ID", "severity": "ERROR",
                           "asset_id": pid, "file_path": entry["source_file"],
                           "message": f"Duplicate PAT ID: {pid}", "action_taken": "SKIPPED"})
            continue
        seen_ids.add(pid)
        core_registry.append(entry)
    print(f"    {sum(1 for e in core_registry if e['asset_type'] == 'PAT')} PAT assets extracted")

    print(f"  [Phase B] Extracting SEC assets ...")
    for entry in extract_sec(repo_root, errors, warnings):
        sid = entry["asset_id"]
        if sid in seen_ids:
            continue  # SEC IDs like "S-01" are not globally unique — skip silently
        seen_ids.add(sid)
        core_registry.append(entry)
    print(f"    {sum(1 for e in core_registry if e['asset_type'] == 'SEC')} SEC assets extracted")

    print(f"  [Phase B] Extracting MTH assets ...")
    for mth_path in mth_files:
        mth = extract_mth(mth_path, repo_root, errors, warnings)
        if mth is None:
            continue
        mid = mth["asset_id"]
        if mid in seen_ids:
            # W2S1-005 / W5-METH-001 are already registered as CAP; note and skip
            warnings.append({
                "warning_code": "MTH_ALREADY_REGISTERED_AS_CAP",
                "severity": "WARNING",
                "asset_id": mid,
                "file_path": mth["source_file"],
                "message": (
                    f"MTH asset {mid} already registered as CAP — "
                    "methodology file is dual-purpose (CAP + MTH). Skipping MTH re-registration."
                ),
                "action_taken": "SKIPPED — CAP entry authoritative",
            })
            continue
        seen_ids.add(mid)
        core_registry.append(mth)
        processed_files.append({
            "path": mth["source_file"],
            "mtime": int(mth_path.stat().st_mtime),
            "sha256": _sha256(mth_path),
            "asset_ids_extracted": [mid],
            "asset_types": ["MTH"],
        })
    print(f"    {sum(1 for e in core_registry if e['asset_type'] == 'MTH')} MTH assets extracted (dual-purpose CAPs noted as warnings)")

    print(f"  [Phase B] Extracting REF assets ...")
    for entry in extract_ref(repo_root, errors, warnings):
        rid = entry["asset_id"]
        if rid in seen_ids:
            errors.append({"error_code": "DUPLICATE_ID", "severity": "ERROR",
                           "asset_id": rid, "file_path": entry["source_file"],
                           "message": f"Duplicate REF ID: {rid}", "action_taken": "SKIPPED"})
            continue
        seen_ids.add(rid)
        core_registry.append(entry)
    print(f"    {sum(1 for e in core_registry if e['asset_type'] == 'REF')} REF assets extracted")

    print(f"  [Phase B] Extracting RSK assets ...")
    for entry in extract_rsk(repo_root, errors, warnings):
        eid = entry["asset_id"]
        if eid in seen_ids:
            errors.append({"error_code": "DUPLICATE_ID", "severity": "ERROR",
                           "asset_id": eid, "file_path": entry["source_file"],
                           "message": f"Duplicate RSK ID: {eid}", "action_taken": "SKIPPED"})
            continue
        seen_ids.add(eid)
        core_registry.append(entry)
    print(f"    {sum(1 for e in core_registry if e['asset_type'] == 'RSK')} RSK assets extracted")

    # Sort core registry: CAP, ASP, PAT, SEC, MTH, REF, RSK — each alphabetically
    def _type_order(t: str) -> int:
        return {"CAP": 0, "ASP": 1, "PAT": 2, "SEC": 3, "MTH": 4, "REF": 5, "RSK": 6}.get(t, 9)

    cap_entries = sorted((e for e in core_registry if e["asset_type"] == "CAP"), key=lambda e: e["asset_id"])
    asp_entries = sorted((e for e in core_registry if e["asset_type"] == "ASP"), key=lambda e: e["asset_id"])
    pat_entries = sorted((e for e in core_registry if e["asset_type"] == "PAT"), key=lambda e: e["asset_id"])
    sec_entries = sorted((e for e in core_registry if e["asset_type"] == "SEC"), key=lambda e: e["asset_id"])
    mth_entries = sorted((e for e in core_registry if e["asset_type"] == "MTH"), key=lambda e: e["asset_id"])
    ref_entries = sorted((e for e in core_registry if e["asset_type"] == "REF"), key=lambda e: e["asset_id"])
    rsk_entries = sorted((e for e in core_registry if e["asset_type"] == "RSK"), key=lambda e: e["asset_id"])
    core_registry = cap_entries + asp_entries + pat_entries + sec_entries + mth_entries + ref_entries + rsk_entries

    # Sort assumptions: by pack_id then sequence
    assumption_registry.sort(
        key=lambda a: (a["asm_ext"]["parent_pack_id"], a["asm_ext"]["sequence"])
    )

    n_cap = len(cap_entries)
    n_asp = len(asp_entries)
    n_asm = len(assumption_registry)
    n_pat = len(pat_entries)
    n_sec = len(sec_entries)
    n_mth = len(mth_entries)
    n_ref = len(ref_entries)
    n_rsk = len(rsk_entries)
    print(f"\n  Phase A Totals: {n_cap} CAP | {n_asp} ASP | {n_asm} ASM")
    print(f"  Phase B Totals: {n_pat} PAT | {n_sec} SEC | {n_mth} MTH | {n_ref} REF | {n_rsk} RSK")

    # ── Phase 3: Augmentation already done at extraction time ─────────────
    print("\nPhase 3 — CAP/Phase B augmentation complete (merged at extraction time)")

    # ── Phase 4: Relationship linking ─────────────────────────────────────
    print("\nPhase 4 — Relationship linking")
    rel_graph = build_relationships(core_registry, assumption_registry)
    by_rel_type: dict[str, int] = {}
    for r in rel_graph:
        by_rel_type[r["relationship_type"]] = by_rel_type.get(r["relationship_type"], 0) + 1
    rel_summary = " | ".join(f"{k}:{v}" for k, v in sorted(by_rel_type.items()))
    print(f"  {len(rel_graph)} relationships ({rel_summary})")

    # ── Phase 5: Index building ────────────────────────────────────────────
    print("\nPhase 5 — Index building")
    indexes = build_indexes(core_registry, assumption_registry, rel_graph)
    print(f"  {len(indexes)} indexes built")

    if build_mode == "DRY_RUN":
        print(f"\n[DRY_RUN] No files written.")
        print(f"  Would produce: {n_cap} CAP | {n_asp} ASP | {n_asm} ASM")
        print(f"               {n_rsk} RSK | {n_ref} REF | {n_mth} MTH | {n_pat} PAT | {n_sec} SEC")
        print(f"  Errors: {len(errors)} | Warnings: {len(warnings)}")
        return

    # ── Phase 6: Write output files ────────────────────────────────────────
    print("\nPhase 6 — Writing output files")
    output_files_written: list[dict] = []

    reg_path = write_core_registry(output_dir, build_id, build_mode,
                                   repo_root, core_registry, assumption_registry)
    sz = reg_path.stat().st_size
    output_files_written.append({"path": str(reg_path.relative_to(repo_root)),
                                  "entries": len(core_registry), "size_bytes": sz})
    print(f"  {reg_path.name}: {len(core_registry)} entries ({sz:,} B)")

    asm_path = write_assumptions_registry(output_dir, build_id, assumption_registry)
    sz = asm_path.stat().st_size
    output_files_written.append({"path": str(asm_path.relative_to(repo_root)),
                                  "entries": n_asm, "size_bytes": sz})
    print(f"  {asm_path.name}: {n_asm} entries ({sz:,} B)")

    graph_path = write_relationship_graph(output_dir, build_id, rel_graph)
    sz = graph_path.stat().st_size
    output_files_written.append({"path": str(graph_path.relative_to(repo_root)),
                                  "entries": len(rel_graph), "size_bytes": sz})
    print(f"  {graph_path.name}: {len(rel_graph)} relationships ({sz:,} B)")

    idx_path = write_lookup_index(output_dir, build_id, indexes)
    sz = idx_path.stat().st_size
    output_files_written.append({"path": str(idx_path.relative_to(repo_root)),
                                  "entries": len(indexes), "size_bytes": sz})
    print(f"  {idx_path.name}: {len(indexes)} indexes ({sz:,} B)")

    manifest_path = write_build_manifest(repo_root, build_id, processed_files)
    print(f"  BUILD_MANIFEST.yaml → {manifest_path.parent.relative_to(repo_root)}/")

    # ── Phase 7: Build report ──────────────────────────────────────────────
    print("\nPhase 7 — Build report")
    report_path = write_build_report(
        reports_dir, build_id, build_mode, build_start, repo_root,
        files_scanned, core_registry, assumption_registry,
        errors, warnings, output_files_written, discovery_log,
    )
    print(f"  {report_path.name}")

    # ── Summary ────────────────────────────────────────────────────────────
    duration = time.time() - build_start
    status = "SUCCESS" if not errors else "SUCCESS_WITH_WARNINGS"
    print(f"\n{sep}")
    print(f"KRPE Phase A+B — {status}")
    print(f"  CAP: {n_cap}  |  ASP: {n_asp}  |  ASM: {n_asm}")
    print(f"  RSK: {n_rsk}  |  REF: {n_ref}  |  MTH: {n_mth}  |  PAT: {n_pat}  |  SEC: {n_sec}")
    print(f"  Total core assets: {len(core_registry)}")
    print(f"  Relationships: {len(rel_graph)}")
    print(f"  Errors: {len(errors)}  |  Warnings: {len(warnings)}")
    print(f"  Duration: {duration:.1f}s")
    print(f"{sep}\n")

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:15]:
            print(f"  [{e['error_code']}] {e.get('asset_id', e.get('file_path', '?'))}: {e['message']}")
        if len(errors) > 15:
            print(f"  ... and {len(errors) - 15} more (see build report)")

    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings[:15]:
            print(f"  [{w['warning_code']}] {w.get('asset_id', w.get('file_path', '?'))}: {w['message']}")
        if len(warnings) > 15:
            print(f"  ... and {len(warnings) - 15} more (see build report)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="KRPE Phase A+B — Knowledge Registry Population Engine"
    )
    parser.add_argument(
        "--repo-root",
        default=(
            "/Users/heinb/Library/CloudStorage/"
            "OneDrive-appsolve.co.za/APPSolve Company Docs/Tender Knowledge Base"
        ),
        help="Absolute path to repository root",
    )
    parser.add_argument(
        "--mode",
        choices=["FULL", "DRY_RUN"],
        default="FULL",
        help="Build mode",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root)
    if not repo_root.exists():
        print(f"ERROR: Repository root not found: {repo_root}", file=sys.stderr)
        sys.exit(1)

    run(repo_root, args.mode)


if __name__ == "__main__":
    main()
