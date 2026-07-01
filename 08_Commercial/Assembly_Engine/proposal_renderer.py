#!/usr/bin/env python3
"""
Markdown Proposal Renderer (PF2-004)
Consumes a certified Proposal Section Manifest and governed source assets
to generate a deterministically assembled proposal in Markdown.

Inputs:
  - Proposal Section Manifest YAML (from PSAE / proposal_section_engine.py)
  - Governed source assets in 07_Approved_Content/Approved/

Outputs:
  - PROPOSAL_RENDERED_[tender_id].md
  - PROPOSAL_RENDER_AUDIT_[tender_id].md

Usage:
  python proposal_renderer.py --tender ARM-IT045
  python proposal_renderer.py --regression
  python proposal_renderer.py --all
"""

import os
import re
import sys
import yaml
import argparse
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone

RENDERER_VERSION = "1.0"
BUILD_DATE = "2026-06-29"

_HERE = os.path.dirname(os.path.abspath(__file__))
_KB_ROOT = os.path.normpath(os.path.join(_HERE, "..", ".."))

CONTENT_ROOT = os.path.join(_KB_ROOT, "07_Approved_Content", "Approved")
ASSUMPTIONS_ROOT = os.path.join(_KB_ROOT, "08_Commercial", "Assumptions")
PROPOSALS_DIR = os.path.join(_HERE, "..", "Proposals")

RENDERABLE = {"MANDATORY", "OPTIONAL_SELECTED"}

APPENDIX_LABELS = {
    "A-01": "A", "A-02": "B", "A-03": "C",
    "A-04": "D", "A-05": "E", "A-06": "F",
}

REGRESSION_TENDERS = [
    "ARM-IT045",
    "REG-HCM-P3-MINING",
    "REG-OIC-P7",
    "REG-ERP-P7-FULLSUITE",
    "REG-ACU-P11",
    "REG-BEB-P12",
]


# ── Audit data classes ────────────────────────────────────────────────────────

@dataclass
class AuditEntry:
    section_id: str
    section_name: str
    include_status: str
    render_status: str
    assembly_method: str
    source_files: List[str] = field(default_factory=list)
    assets_found: List[str] = field(default_factory=list)
    assets_not_found: List[str] = field(default_factory=list)
    governance_constraints: List[str] = field(default_factory=list)
    si_rules_applied: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class RenderResult:
    tender_id: str
    manifest_id: str
    platform: str
    engagement_type: str
    rendered_at: str
    renderer_version: str
    sections_rendered: int
    sections_placeholder: int
    sections_ai_draft: int
    sections_not_found: int
    sections_skipped: int
    audit_entries: List[AuditEntry] = field(default_factory=list)
    governance_flags: List[str] = field(default_factory=list)
    validation_warnings: List[str] = field(default_factory=list)


# ── Asset Index ───────────────────────────────────────────────────────────────

class AssetIndex:
    """
    Builds a lookup dict from asset_id → absolute file path by scanning
    07_Approved_Content/Approved/ and (optionally) additional roots such as
    08_Commercial/Assumptions/. Canonical IDs, short prefix IDs, and
    document_id values from YAML frontmatter are all indexed.
    """

    def __init__(self, content_root: str, additional_roots: Optional[List[str]] = None):
        self._index: Dict[str, str] = {}
        self._build(content_root, index_by_document_id=False)
        for root in (additional_roots or []):
            self._build(root, index_by_document_id=True)

    @staticmethod
    def _short_id(canonical: str) -> str:
        """
        Extract short prefix from canonical ID.
        W1S1-001-CORP-CompanyOverview  → W1S1-001
        W5-ACU-001-ACU-SupportManaged  → W5-ACU-001
        W4-INT-001-ORA-OICAccelerators → W4-INT-001
        Rule: take segments up to and including the first all-digit segment.
        """
        parts = canonical.split("-")
        for i, part in enumerate(parts):
            if part.isdigit():
                return "-".join(parts[: i + 1])
        return canonical

    @staticmethod
    def _extract_document_id(path: str) -> Optional[str]:
        """Parse YAML frontmatter and return document_id value, or None."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except OSError:
            return None
        if not lines or lines[0].strip() != "---":
            return None
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if line.startswith("document_id:"):
                return line.split(":", 1)[1].strip()
        return None

    def _build(self, root: str, index_by_document_id: bool = False) -> None:
        for dirpath, _, filenames in os.walk(root):
            for fn in filenames:
                if not fn.endswith(".md"):
                    continue
                path = os.path.join(dirpath, fn)
                if index_by_document_id:
                    doc_id = self._extract_document_id(path)
                    if doc_id and doc_id not in self._index:
                        self._index[doc_id] = path
                else:
                    canonical = fn[:-3]
                    self._index[canonical] = path
                    short = self._short_id(canonical)
                    if short != canonical and short not in self._index:
                        self._index[short] = path

    def get(self, asset_id: str) -> Optional[str]:
        return self._index.get(asset_id)

    def file_count(self) -> int:
        return len(set(self._index.values()))

    def id_count(self) -> int:
        return len(self._index)


# ── Content helpers ───────────────────────────────────────────────────────────

# Markers indicating the start of internal-only content in approved .md files.
# Tuples of (match_mode, text) where mode is "startswith" (checks stripped line prefix)
# or "contains" (checks anywhere in line).
_INTERNAL_MARKERS: List[Tuple[str, str]] = [
    ("contains", "Internal — Not for Tender Use"),
    ("contains", "Internal - Not for Tender Use"),
    ("contains", "Extraction Documentation (Internal"),
    ("startswith", "**Pre-tender"),       # catches all **Pre-tender ... variants
    ("startswith", "**Review notes"),     # catches **Review notes: and **Review notes**:
    ("startswith", "## Approval Record"),
    ("startswith", "**File location:"),   # internal approval record field
]


def strip_frontmatter(raw: str) -> str:
    """
    Remove YAML frontmatter, approval banners, and leading dividers from
    governed .md asset content, then strip trailing internal-only sections.
    Returns the renderable body only.
    """
    lines = raw.split("\n")
    i = 0

    # Strip YAML frontmatter block (--- ... ---)
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1  # advance past closing ---

    # Strip blank lines, approval banners (> **Approved...**), and dividers
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped == "" or stripped == "---" or stripped.startswith(">"):
            i += 1
        else:
            break

    body_lines = lines[i:]

    # Strip trailing internal-only sections
    cut = len(body_lines)
    for j, line in enumerate(body_lines):
        stripped_line = line.strip()
        for mode, marker in _INTERNAL_MARKERS:
            matched = (
                (mode == "startswith" and stripped_line.startswith(marker))
                or (mode == "contains" and marker in line)
            )
            if matched:
                # Walk back past blank lines to find preceding --- divider
                k = j - 1
                while k >= 0 and body_lines[k].strip() == "":
                    k -= 1
                if k >= 0 and body_lines[k].strip() == "---":
                    cut = min(cut, k)
                else:
                    cut = min(cut, j)
                break

    return "\n".join(body_lines[:cut]).rstrip()


def demote_headings(body: str, levels: int = 2) -> str:
    """
    Demote all Markdown ATX headings by `levels` levels so body content
    sits correctly under the section's ## heading.
    # → ###, ## → ####, ### → #####, etc. (capped at ######).
    """
    result = []
    for line in body.split("\n"):
        if line.startswith("#"):
            count = len(line) - len(line.lstrip("#"))
            rest = line[count:]
            new_count = min(count + levels, 6)
            result.append("#" * new_count + rest)
        else:
            result.append(line)
    return "\n".join(result)


def load_asset_body(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    body = strip_frontmatter(raw)
    return demote_headings(body)


def _governance_note_block(constraints: List[str], si_rules: List[str]) -> List[str]:
    """Generate a compact governance note block for inline insertion."""
    if not constraints and not si_rules:
        return []
    lines = ["", "<!-- GOVERNANCE -->"]
    for c in constraints:
        lines.append(f"<!-- GOV: {c} -->")
    for r in si_rules:
        lines.append(f"<!-- SI-RULE: {r} -->")
    return lines


# ── Section renderer ──────────────────────────────────────────────────────────

def render_section(
    section_def: dict,
    asset_index: AssetIndex,
    section_heading: str,
) -> Tuple[List[str], AuditEntry]:
    """
    Render a single section. Returns (content_lines, audit_entry).
    section_heading is the pre-built Markdown heading line.
    """
    sid = section_def["section_id"]
    name = section_def["section_name"]
    method = section_def["assembly_method"]
    source_assets = section_def.get("source_assets") or []
    placeholders = section_def.get("placeholders") or []
    human_input = section_def.get("human_input_required", False)
    human_notes = section_def.get("human_input_notes", "")
    gov_constraints = section_def.get("governance_constraints") or []
    si_rules = section_def.get("si_rules_applied") or []
    include_status = section_def.get("include_status", "")

    audit = AuditEntry(
        section_id=sid,
        section_name=name,
        include_status=include_status,
        render_status="",
        assembly_method=method,
        governance_constraints=gov_constraints,
        si_rules_applied=si_rules,
    )

    lines: List[str] = [section_heading, ""]

    # Append governance comments before content (invisible in rendered output)
    lines += _governance_note_block(gov_constraints, si_rules)
    if lines[-1:] == ["<!-- GOVERNANCE -->"]:
        pass  # non-empty block already added separator
    elif any(l.startswith("<!-- GOV") or l.startswith("<!-- SI") for l in lines):
        lines.append("")

    if method == "TEMPLATE":
        _render_template(sid, name, placeholders, human_notes, lines, audit)

    elif method == "AI-GENERATE":
        _render_ai_generate(sid, name, human_notes, lines, audit)

    elif method == "PLACEHOLDER":
        _render_placeholder(sid, name, placeholders, human_notes, lines, audit)

    elif method == "DIRECT":
        _render_direct(sid, name, source_assets, human_notes, asset_index, lines, audit)

    elif method == "MERGE":
        _render_merge(sid, name, source_assets, human_notes, asset_index, lines, audit)

    elif method == "EXTRACT":
        _render_extract(sid, name, source_assets, human_notes, asset_index, lines, audit)

    else:
        lines += [f"<!-- UNKNOWN ASSEMBLY METHOD: {method} -->", ""]
        audit.render_status = "PLACEHOLDER"
        audit.notes = f"Unknown assembly_method: {method}"

    # Human review callout (skip for cover/TOC and already-flagged draft/placeholder)
    if human_input and audit.render_status not in ("AI-DRAFT", "PLACEHOLDER") and sid not in ("S-01", "S-02"):
        review_note = human_notes or f"Human review required before submission."
        lines += ["", f"> **Human Review Required:** {review_note}"]

    lines.append("")
    return lines, audit


def _render_template(
    sid: str, name: str, placeholders: List[str],
    human_notes: str, lines: List[str], audit: AuditEntry
) -> None:
    if sid == "S-01":
        lines += [
            "| Field | Value |",
            "|---|---|",
            "| **Proposal Title** | `{{tender_title}}` |",
            "| **Prepared For** | `{{client_name}}` |",
            "| **RFP / Tender Reference** | `{{rfp_reference}}` |",
            "| **Submission Date** | `{{submission_date}}` |",
            "| **Prepared By** | APPSolve (Pty) Ltd |",
            "| **Version** | 1.0 |",
            "",
            "*Cover page requires human completion before submission.*",
        ]
    elif sid == "S-02":
        lines += [
            "*Table of Contents — generated from included sections; update after final assembly.*",
            "",
            "**[TOC_PLACEHOLDER]**",
        ]
    else:
        lines += [f"*Template section — complete placeholders before submission.*", ""]
        if placeholders:
            lines.append("**Required fields:**")
            for ph in placeholders:
                lines.append(f"- `{{{{{ph}}}}}`")
        if human_notes:
            lines += ["", f"> **Note:** {human_notes}"]
    audit.render_status = "RENDERED"
    audit.notes = f"TEMPLATE; placeholders: {placeholders}" if placeholders else "TEMPLATE rendered"


def _render_ai_generate(
    sid: str, name: str, human_notes: str,
    lines: List[str], audit: AuditEntry
) -> None:
    instruction = human_notes or f"Draft {name} tailored to this specific tender."
    lines += [
        f"<!-- AI-DRAFT REQUIRED: {name} -->",
        f"<!-- Instruction: {instruction} -->",
        "",
        f"> **AI-Draft Required:** This section requires AI-assisted drafting with mandatory human review.",
        f">",
        f"> *{instruction}*",
        "",
        "_[AI-generated content to be inserted here — must be reviewed and approved before submission]_",
    ]
    audit.render_status = "AI-DRAFT"
    audit.notes = f"AI-GENERATE: draft required; instruction: {instruction}"


def _render_placeholder(
    sid: str, name: str, placeholders: List[str],
    human_notes: str, lines: List[str], audit: AuditEntry
) -> None:
    note = human_notes or f"Provide {name} content before submission."
    lines += [
        f"<!-- PLACEHOLDER: {name} -->",
        "",
        f"> **Action Required:** {note}",
    ]
    if placeholders:
        lines += ["", "**Fields to complete:**"]
        for ph in placeholders:
            lines.append(f"- `{{{{{ph}}}}}`")
    audit.render_status = "PLACEHOLDER"
    audit.notes = f"PLACEHOLDER: {note}"


def _render_direct(
    sid: str, name: str, source_assets: List[str], human_notes: str,
    asset_index: AssetIndex, lines: List[str], audit: AuditEntry
) -> None:
    if not source_assets:
        note = human_notes or f"No governed source asset; provide {name} content before submission."
        lines += [
            f"<!-- PLACEHOLDER: {name} — no governed source asset declared -->",
            "",
            f"> **Action Required:** {note}",
        ]
        audit.render_status = "PLACEHOLDER"
        audit.notes = "DIRECT — no source_assets declared; rendered as PLACEHOLDER"
        return

    primary_id = source_assets[0]
    path = asset_index.get(primary_id)
    if path:
        body = load_asset_body(path)
        lines += [body]
        audit.render_status = "RENDERED"
        audit.source_files = [path]
        audit.assets_found = [primary_id]
        audit.notes = f"DIRECT: rendered from {os.path.basename(path)}"
    else:
        lines += [
            f"<!-- NOT_FOUND: {primary_id} -->",
            "",
            f"> **Content Not Found:** Governed asset `{primary_id}` not located in the Asset Index.",
            f"> Add to `07_Approved_Content/Approved/` before submission.",
        ]
        audit.render_status = "NOT_FOUND"
        audit.assets_not_found = [primary_id]
        audit.notes = f"DIRECT: source asset {primary_id} not in AssetIndex"


def _render_merge(
    sid: str, name: str, source_assets: List[str], human_notes: str,
    asset_index: AssetIndex, lines: List[str], audit: AuditEntry
) -> None:
    if not source_assets:
        note = human_notes or f"No governed source assets for merge; provide {name} content."
        lines += [
            f"<!-- PLACEHOLDER: {name} — MERGE with no source assets -->",
            "",
            f"> **Action Required:** {note}",
        ]
        audit.render_status = "PLACEHOLDER"
        audit.notes = "MERGE — no source_assets declared; rendered as PLACEHOLDER"
        return

    found_any = False
    for asset_id in source_assets:
        path = asset_index.get(asset_id)
        if path:
            body = load_asset_body(path)
            lines += [body, ""]
            audit.source_files.append(path)
            audit.assets_found.append(asset_id)
            found_any = True
        else:
            lines += [f"<!-- NOT_FOUND: {asset_id} — not in AssetIndex -->"]
            audit.assets_not_found.append(asset_id)

    if found_any:
        audit.render_status = "RENDERED"
        n_found = len(audit.assets_found)
        n_miss = len(audit.assets_not_found)
        audit.notes = f"MERGE: {n_found} asset(s) rendered; {n_miss} not found"
    else:
        audit.render_status = "NOT_FOUND"
        audit.notes = f"MERGE: all {len(source_assets)} source assets missing from index"


def _render_extract(
    sid: str, name: str, source_assets: List[str], human_notes: str,
    asset_index: AssetIndex, lines: List[str], audit: AuditEntry
) -> None:
    if not source_assets:
        note = human_notes or f"Extract content from source asset before submission."
        lines += [
            f"<!-- PLACEHOLDER: {name} — EXTRACT with no source assets -->",
            "",
            f"> **Action Required:** {note}",
        ]
        audit.render_status = "PLACEHOLDER"
        audit.notes = "EXTRACT — no source_assets declared; rendered as PLACEHOLDER"
        return

    primary_id = source_assets[0]
    path = asset_index.get(primary_id)
    if path:
        body = load_asset_body(path)
        lines += [
            body,
            "",
            f"<!-- AUDIT NOTE: EXTRACT method — full asset body included; "
            f"sub-section extraction not yet automated -->",
        ]
        if human_notes:
            lines += ["", f"> **Review Required:** {human_notes}"]
        audit.render_status = "RENDERED"
        audit.source_files = [path]
        audit.assets_found = [primary_id]
        audit.notes = (
            f"EXTRACT: full body of {os.path.basename(path)} included; "
            "sub-section extraction not automated — manual curation required"
        )
    else:
        lines += [
            f"<!-- NOT_FOUND: {primary_id} -->",
            "",
            f"> **Content Not Found:** Asset `{primary_id}` not in Asset Index. "
            f"Sub-section extraction cannot proceed.",
        ]
        audit.render_status = "NOT_FOUND"
        audit.assets_not_found = [primary_id]
        audit.notes = f"EXTRACT: source {primary_id} not in AssetIndex"


# ── Section heading builder ───────────────────────────────────────────────────

def build_heading(sid: str, name: str, proposal_seq: int) -> str:
    """Build the Markdown heading for a section."""
    if sid == "S-01":
        return f"# {name}"
    if sid == "S-02":
        return f"## Table of Contents"
    if sid.startswith("A-"):
        label = APPENDIX_LABELS.get(sid, sid)
        return f"## Appendix {label} — {name}"
    return f"## {proposal_seq}. {name}"


# ── TOC builder ───────────────────────────────────────────────────────────────

def build_toc(toc_entries: List[Tuple[str, str, str]]) -> str:
    """
    Build a Markdown TOC from (section_id, heading_text, anchor) tuples.
    toc_entries are collected during the section rendering pass.
    """
    lines = ["## Table of Contents", ""]
    for sid, heading_text, _ in toc_entries:
        # Indent appendices slightly
        prefix = "  " if sid.startswith("A-") else ""
        lines.append(f"{prefix}- {heading_text}")
    lines.append("")
    return "\n".join(lines)


# ── Document header / footer builders ────────────────────────────────────────

def build_document_header(manifest: dict, rendered_at: str) -> List[str]:
    tender_id = manifest.get("tender_id", "UNKNOWN")
    platform = manifest.get("platform", "")
    eng_type = manifest.get("engagement_type", "")
    industry = manifest.get("industry", "")
    summary = manifest.get("summary", {})
    manifest_id = manifest.get("manifest_id", "")

    lines = [
        "<!-- PROPOSAL RENDERED BY proposal_renderer.py v1.0 — PF2-004 -->",
        f"<!-- Tender: {tender_id} | Platform: {platform} | Type: {eng_type} | Industry: {industry} -->",
        f"<!-- Manifest: {manifest_id} -->",
        f"<!-- Rendered: {rendered_at} -->",
        f"<!-- Sections: M={summary.get('mandatory_sections',0)} "
        f"O={summary.get('optional_sections',0)} -->",
        "",
    ]

    # Governance flags as prominent warnings
    gov_flags = manifest.get("governance_flags", [])
    val_warnings = manifest.get("validation_warnings", [])
    if gov_flags or val_warnings:
        lines += [
            "---",
            "",
            "> **GOVERNANCE FLAGS — Review before submission:**",
        ]
        for flag in gov_flags:
            lines.append(f"> - {flag}")
        for warn in val_warnings:
            lines.append(f"> - WARNING: {warn}")
        lines += ["", "---", ""]

    return lines


def build_document_footer(result: RenderResult) -> List[str]:
    return [
        "",
        "---",
        "",
        "<!-- RENDER SUMMARY -->",
        f"<!-- Rendered: {result.rendered_at} | Renderer v{result.renderer_version} -->",
        f"<!-- RENDERED={result.sections_rendered} | PLACEHOLDER={result.sections_placeholder} | "
        f"AI-DRAFT={result.sections_ai_draft} | NOT_FOUND={result.sections_not_found} | "
        f"SKIPPED={result.sections_skipped} -->",
        "",
        "*End of document — assembled by APPSolve Proposal Factory v1.0*",
    ]


# ── Audit report builder ──────────────────────────────────────────────────────

def build_audit_report(result: RenderResult, manifest: dict) -> str:
    tender_id = result.tender_id
    platform = manifest.get("platform", "")
    eng_type = manifest.get("engagement_type", "")
    summary = manifest.get("summary", {})

    lines = [
        "---",
        f"document_id: RENDER-AUDIT-{tender_id}-V1",
        f'title: "Proposal Render Audit — {tender_id}"',
        f'version: "1.0"',
        f'status: "COMPLETE"',
        f'rendered_at: "{result.rendered_at}"',
        f'renderer_version: "{result.renderer_version}"',
        f'manifest_id: "{manifest.get("manifest_id","")}"',
        "---",
        "",
        f"# Proposal Render Audit — {tender_id}",
        "",
        f"**Tender:** {tender_id}  ",
        f"**Platform:** {platform}  ",
        f"**Engagement Type:** {eng_type}  ",
        f"**Rendered:** {result.rendered_at}  ",
        f"**Renderer Version:** {result.renderer_version}  ",
        "",
        "---",
        "",
        "## 1. Render Summary",
        "",
        "| Metric | Count |",
        "|---|---|",
        f"| Sections in manifest | {summary.get('total_sections', 82)} |",
        f"| Assembly sequence length | {summary.get('assembly_sequence_length', 0)} |",
        f"| RENDERED | {result.sections_rendered} |",
        f"| PLACEHOLDER | {result.sections_placeholder} |",
        f"| AI-DRAFT | {result.sections_ai_draft} |",
        f"| NOT_FOUND | {result.sections_not_found} |",
        f"| SKIPPED (excluded) | {result.sections_skipped} |",
        "",
        "---",
        "",
        "## 2. Governance Flags",
        "",
    ]

    if result.governance_flags:
        for flag in result.governance_flags:
            lines.append(f"- {flag}")
    else:
        lines.append("*No governance flags.*")

    lines += ["", "---", "", "## 3. Section Audit Trail", ""]
    lines += [
        "| Section | Name | Status | Render Status | Method | Assets Found | Assets Missing | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for entry in result.audit_entries:
        found = "; ".join(os.path.basename(f) for f in entry.source_files) if entry.source_files else "—"
        missing = "; ".join(entry.assets_not_found) if entry.assets_not_found else "—"
        si = ", ".join(entry.si_rules_applied) if entry.si_rules_applied else "—"
        note = entry.notes.replace("|", "/")
        lines.append(
            f"| {entry.section_id} | {entry.section_name} | {entry.include_status} "
            f"| {entry.render_status} | {entry.assembly_method} "
            f"| {found} | {missing} | {note} |"
        )

    lines += [
        "",
        "---",
        "",
        "## 4. Governance Constraint Detail",
        "",
    ]

    gov_sections = [e for e in result.audit_entries if e.governance_constraints]
    if gov_sections:
        for entry in gov_sections:
            lines.append(f"**{entry.section_id} — {entry.section_name}:**")
            for c in entry.governance_constraints:
                lines.append(f"- {c}")
            lines.append("")
    else:
        lines.append("*No section-level governance constraints recorded.*")

    lines += [
        "---",
        "",
        "## 5. Asset Not Found Register",
        "",
    ]
    missing_sections = [e for e in result.audit_entries if e.assets_not_found]
    if missing_sections:
        lines += [
            "| Section | Asset ID | Impact |",
            "|---|---|---|",
        ]
        for entry in missing_sections:
            for aid in entry.assets_not_found:
                impact = "PLACEHOLDER rendered" if entry.render_status == "PLACEHOLDER" else entry.render_status
                lines.append(f"| {entry.section_id} | {aid} | {impact} |")
    else:
        lines.append("*All referenced assets located in AssetIndex.*")

    lines += [
        "",
        "---",
        "",
        "## 6. Human Action Register",
        "",
        "Sections requiring human completion or review before submission:",
        "",
        "| Section | Name | Render Status | Action Required |",
        "|---|---|---|---|",
    ]

    for entry in result.audit_entries:
        if entry.render_status in ("PLACEHOLDER", "AI-DRAFT", "NOT_FOUND"):
            action = entry.notes[:80] if entry.notes else "Review required"
            lines.append(
                f"| {entry.section_id} | {entry.section_name} | {entry.render_status} | {action} |"
            )

    lines += [
        "",
        "---",
        "",
        f"*PROPOSAL_RENDER_AUDIT_{tender_id}.md | proposal_renderer.py v{RENDERER_VERSION} | {result.rendered_at}*",
    ]

    return "\n".join(lines)


# ── Main renderer ─────────────────────────────────────────────────────────────

def render_proposal(tender_id: str, asset_index: AssetIndex, verbose: bool = True) -> RenderResult:
    """
    Load manifest for tender_id and render the full proposal.
    Returns RenderResult with audit entries.
    """
    manifest_path = os.path.join(
        PROPOSALS_DIR, tender_id,
        f"PROPOSAL_SECTION_MANIFEST_{tender_id}.yaml"
    )
    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    rendered_at = datetime.now(timezone.utc).isoformat()
    assembly_sequence = manifest.get("assembly_sequence", [])
    sections_dict = manifest.get("sections", {})
    gov_flags = manifest.get("governance_flags", [])
    val_warnings = manifest.get("validation_warnings", [])

    result = RenderResult(
        tender_id=tender_id,
        manifest_id=manifest.get("manifest_id", ""),
        platform=manifest.get("platform", ""),
        engagement_type=manifest.get("engagement_type", ""),
        rendered_at=rendered_at,
        renderer_version=RENDERER_VERSION,
        sections_rendered=0,
        sections_placeholder=0,
        sections_ai_draft=0,
        sections_not_found=0,
        sections_skipped=0,
        governance_flags=gov_flags,
        validation_warnings=val_warnings,
    )

    # ── First pass: determine included sections and their proposal sequence numbers ──
    included_sequence: List[str] = []
    for sid in assembly_sequence:
        sec = sections_dict.get(sid, {})
        if sec.get("include_status") in RENDERABLE:
            included_sequence.append(sid)

    # Build proposal numbering (excluding S-01, S-02, appendices)
    seq_counter = 0
    proposal_numbers: Dict[str, int] = {}
    for sid in included_sequence:
        if sid in ("S-01", "S-02") or sid.startswith("A-"):
            proposal_numbers[sid] = 0
        else:
            seq_counter += 1
            proposal_numbers[sid] = seq_counter

    # ── Second pass: render sections ──────────────────────────────────────────
    doc_lines: List[str] = []
    toc_entries: List[Tuple[str, str, str]] = []  # (sid, heading_text, anchor)
    audit_all: List[AuditEntry] = []

    doc_lines += build_document_header(manifest, rendered_at)

    toc_placeholder_index: Optional[int] = None

    for sid in assembly_sequence:
        sec = sections_dict.get(sid, {})
        inc_status = sec.get("include_status", "DEFAULT_EXCLUDED")

        if inc_status not in RENDERABLE:
            # Record skipped section in audit
            audit_all.append(AuditEntry(
                section_id=sid,
                section_name=sec.get("section_name", sid),
                include_status=inc_status,
                render_status="SKIPPED",
                assembly_method=sec.get("assembly_method", ""),
                notes=f"Not in assembly sequence (status: {inc_status})",
            ))
            result.sections_skipped += 1
            continue

        seq_num = proposal_numbers.get(sid, 0)
        name = sec.get("section_name", sid)
        heading = build_heading(sid, name, seq_num)

        # Build TOC entry text (skip cover and TOC itself)
        if sid not in ("S-01", "S-02"):
            if sid.startswith("A-"):
                label = APPENDIX_LABELS.get(sid, sid)
                toc_text = f"Appendix {label} — {name}"
            else:
                toc_text = f"{seq_num}. {name}"
            toc_entries.append((sid, toc_text, sid.lower()))

        # Mark where TOC should be inserted
        if sid == "S-02":
            toc_placeholder_index = len(doc_lines)
            doc_lines.append("__TOC_PLACEHOLDER__")
            doc_lines.append("")
            # Audit entry for TOC
            audit_all.append(AuditEntry(
                section_id="S-02",
                section_name="Table of Contents",
                include_status=inc_status,
                render_status="RENDERED",
                assembly_method="TEMPLATE",
                notes="TOC auto-generated from assembly sequence",
            ))
            result.sections_rendered += 1
            continue

        section_lines, audit_entry = render_section(sec, asset_index, heading)
        doc_lines += section_lines
        audit_all.append(audit_entry)

        rs = audit_entry.render_status
        if rs == "RENDERED":
            result.sections_rendered += 1
        elif rs == "PLACEHOLDER":
            result.sections_placeholder += 1
        elif rs == "AI-DRAFT":
            result.sections_ai_draft += 1
        elif rs == "NOT_FOUND":
            result.sections_not_found += 1

    # Also capture skipped sections NOT in assembly_sequence (those were excluded at manifest level)
    for sid, sec in sections_dict.items():
        if sid not in assembly_sequence:
            inc_status = sec.get("include_status", "DEFAULT_EXCLUDED")
            audit_all.append(AuditEntry(
                section_id=sid,
                section_name=sec.get("section_name", sid),
                include_status=inc_status,
                render_status="SKIPPED",
                assembly_method=sec.get("assembly_method", ""),
                notes=f"Excluded from assembly sequence (status: {inc_status})",
            ))

    doc_lines += build_document_footer(result)
    result.audit_entries = sorted(audit_all, key=lambda e: e.section_id)

    # ── Replace TOC placeholder ───────────────────────────────────────────────
    toc_content = build_toc(toc_entries)
    if toc_placeholder_index is not None:
        doc_lines[toc_placeholder_index] = toc_content
    else:
        # No S-02 in sequence — prepend TOC after header
        doc_lines = doc_lines[:6] + [toc_content] + doc_lines[6:]

    # ── Write outputs ─────────────────────────────────────────────────────────
    output_dir = os.path.join(PROPOSALS_DIR, tender_id)
    os.makedirs(output_dir, exist_ok=True)

    proposal_path = os.path.join(output_dir, f"PROPOSAL_RENDERED_{tender_id}.md")
    with open(proposal_path, "w", encoding="utf-8") as f:
        f.write("\n".join(doc_lines))

    audit_report = build_audit_report(result, manifest)
    audit_path = os.path.join(output_dir, f"PROPOSAL_RENDER_AUDIT_{tender_id}.md")
    with open(audit_path, "w", encoding="utf-8") as f:
        f.write(audit_report)

    if verbose:
        print(f"  [RENDERED] {proposal_path}")
        print(f"  [AUDIT]    {audit_path}")
        print(
            f"  Summary: RENDERED={result.sections_rendered} "
            f"PLACEHOLDER={result.sections_placeholder} "
            f"AI-DRAFT={result.sections_ai_draft} "
            f"NOT_FOUND={result.sections_not_found}"
        )

    return result


# ── Smoke test / regression ───────────────────────────────────────────────────

def run_smoke_test(tender_id: str, result: RenderResult) -> List[str]:
    """
    Run basic structural checks on render result.
    Returns list of failure strings (empty = PASS).
    """
    failures = []

    # At least one section rendered
    if result.sections_rendered == 0:
        failures.append(f"{tender_id}: No sections rendered")

    # Cover page must be rendered
    cover = next((e for e in result.audit_entries if e.section_id == "S-01"), None)
    if cover and cover.render_status != "RENDERED":
        failures.append(f"{tender_id}: S-01 cover not rendered (status={cover.render_status})")

    # TOC must be rendered
    toc = next((e for e in result.audit_entries if e.section_id == "S-02"), None)
    if toc and toc.render_status != "RENDERED":
        failures.append(f"{tender_id}: S-02 TOC not rendered (status={toc.render_status})")

    # No render errors (all rendered sections must be RENDERED/PLACEHOLDER/AI-DRAFT)
    for entry in result.audit_entries:
        if entry.include_status in RENDERABLE and entry.render_status == "":
            failures.append(f"{tender_id}: {entry.section_id} has empty render_status")

    # Check rendered file exists
    proposal_path = os.path.join(
        PROPOSALS_DIR, tender_id, f"PROPOSAL_RENDERED_{tender_id}.md"
    )
    if not os.path.exists(proposal_path):
        failures.append(f"{tender_id}: Rendered file not created: {proposal_path}")

    # Audit file exists
    audit_path = os.path.join(
        PROPOSALS_DIR, tender_id, f"PROPOSAL_RENDER_AUDIT_{tender_id}.md"
    )
    if not os.path.exists(audit_path):
        failures.append(f"{tender_id}: Audit file not created: {audit_path}")

    return failures


def run_regression(asset_index: AssetIndex) -> bool:
    print("\n=== PF2-004 Proposal Renderer — Regression Suite ===\n")
    print(f"Asset Index: {asset_index.file_count()} files / {asset_index.id_count()} IDs indexed\n")

    all_pass = True
    results_summary = []

    # ARM-IT045 = full render; others = smoke tests
    tenders = [(REGRESSION_TENDERS[0], "FULL")] + [(t, "SMOKE") for t in REGRESSION_TENDERS[1:]]

    for tender_id, mode in tenders:
        manifest_path = os.path.join(
            PROPOSALS_DIR, tender_id, f"PROPOSAL_SECTION_MANIFEST_{tender_id}.yaml"
        )
        if not os.path.exists(manifest_path):
            print(f"  SKIP {tender_id}: manifest not found at {manifest_path}")
            results_summary.append((tender_id, "SKIP", 0, 0, 0, 0, []))
            continue

        print(f"  Rendering {tender_id} [{mode}]...")
        try:
            result = render_proposal(tender_id, asset_index, verbose=True)
            failures = run_smoke_test(tender_id, result)
            if failures:
                for f in failures:
                    print(f"    FAIL: {f}")
                all_pass = False
                status = "FAIL"
            else:
                status = "PASS"
            results_summary.append((
                tender_id, status,
                result.sections_rendered,
                result.sections_placeholder,
                result.sections_ai_draft,
                result.sections_not_found,
                failures,
            ))
        except Exception as exc:
            print(f"    ERROR: {exc}")
            all_pass = False
            results_summary.append((tender_id, "ERROR", 0, 0, 0, 0, [str(exc)]))
        print()

    # Results table
    print("\n── Regression Results ──────────────────────────────────────")
    print(f"{'Tender':<30} {'Status':<8} {'R':>5} {'PH':>5} {'AI':>5} {'NF':>5}")
    print("-" * 60)
    for row in results_summary:
        tid, st, r, ph, ai, nf, _ = row
        print(f"{tid:<30} {st:<8} {r:>5} {ph:>5} {ai:>5} {nf:>5}")
    print()

    overall = "PASS" if all_pass else "FAIL"
    print(f"Overall: {overall}")
    return all_pass


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Proposal Renderer v1.0 — PF2-004"
    )
    parser.add_argument(
        "--tender", metavar="TENDER_ID",
        help="Render proposal for a specific tender ID"
    )
    parser.add_argument(
        "--regression", action="store_true",
        help="Run full render for ARM-IT045 + smoke tests for 5 regression scenarios"
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Render all tenders in regression suite"
    )
    parser.add_argument(
        "--content-root", default=CONTENT_ROOT,
        help=f"Path to approved content root (default: {CONTENT_ROOT})"
    )
    args = parser.parse_args()

    print(f"Proposal Renderer v{RENDERER_VERSION} — PF2-004 | {BUILD_DATE}")
    print(f"Content root: {args.content_root}")

    asset_index = AssetIndex(args.content_root, additional_roots=[ASSUMPTIONS_ROOT])
    print(f"Asset Index: {asset_index.file_count()} files / {asset_index.id_count()} IDs\n")

    if args.regression or args.all:
        success = run_regression(asset_index)
        return 0 if success else 1

    if args.tender:
        try:
            result = render_proposal(args.tender, asset_index, verbose=True)
            failures = run_smoke_test(args.tender, result)
            if failures:
                for f in failures:
                    print(f"FAIL: {f}")
                return 1
            print(f"\nOK: {args.tender} rendered successfully")
            return 0
        except FileNotFoundError as e:
            print(f"ERROR: {e}")
            return 1

    # Default: render ARM-IT045 and run regression
    success = run_regression(asset_index)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
