#!/usr/bin/env python3
"""
Proposal Section Assembly Engine (PSAE) — PF2-003
Deterministically assembles the Proposal Section Manifest for any tender.

Usage:
  python proposal_section_engine.py                          # full run
  python proposal_section_engine.py --regression             # 6 regression scenarios
  python proposal_section_engine.py --run-tests              # self-test suite (15+ tests)
  python proposal_section_engine.py --manifest TENDER_ID     # generate manifest for named scenario
"""

import os, sys, yaml, argparse
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime, timezone

ENGINE_VERSION = "1.0"
BUILD_DATE = "2026-06-29"

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from are import ARELEvaluator, ASSEMBLY_RULES, ASP_RULES, ALL_RULES, select_assets  # noqa: E402

MANIFESTS_DIR = os.path.join(_HERE, "..", "Proposals")
REPORTS_DIR   = os.path.join(_HERE, "..", "Reports")

# ── Section exclusions / ordering rules ─────────────────────────────────────

# SI-001: S-38 excluded for Pattern 13 AMS; S-73 is the AMS replacement
# Plus: project-delivery sections excluded for AMS
AMS_EXCLUDED = {
    "S-34", "S-35", "S-38", "S-39", "S-40",
    "S-41", "S-42", "S-43", "S-46", "S-47", "S-48",
}

# Sections only assembled when engagement_type == "AMS"
AMS_ONLY = {
    "S-70", "S-71", "S-72", "S-73", "S-74", "S-75", "S-76",
}

# Standard section assembly order
STANDARD_ORDER = [
    "S-01","S-02",
    "S-03","S-04","S-05","S-06","S-07","S-08","S-09","S-10","S-11","S-12",
    "S-13","S-14","S-15",
    "S-16","S-17","S-18","S-19","S-20","S-21","S-22",
    "S-23","S-24","S-25","S-26","S-27","S-28","S-29",
    "S-30","S-31","S-32","S-33","S-34","S-35","S-36","S-37","S-38",
    "S-39","S-40","S-41","S-42","S-43","S-44","S-45",
    "S-46","S-47","S-48",
    "S-49","S-50","S-51","S-52","S-53","S-54",
    "S-55","S-56","S-57","S-58","S-59","S-60","S-61",
    "S-62","S-63","S-64","S-65","S-66",
    "S-67","S-68","S-69",
    "S-70","S-71","S-72","S-73","S-74","S-75","S-76",
    "A-01","A-02","A-03","A-04","A-05","A-06",
]

# AMS order (Pattern 13): SI-005 References after Commercial; SI-001 S-73 replaces S-38
# AMS Support block order: S-74 → S-70 → S-71 → S-72 → S-73 → S-75 → S-76
AMS_ORDER = [
    "S-01","S-02",
    "S-03","S-04","S-05","S-06","S-07","S-08","S-09","S-10","S-11","S-12",
    "S-13","S-14","S-15",
    "S-16","S-17","S-18","S-19","S-20","S-21","S-22",
    "S-23","S-24","S-25","S-26","S-27","S-28","S-29",
    "S-30","S-31","S-32","S-33",          # Scope: inclusions / exclusions / deliverables / deps
    "S-36","S-37",                          # Governance / RAID
    "S-44","S-45",                          # DR, Security
    "S-74","S-70","S-71","S-72","S-73","S-75","S-76",   # AMS Support (SI-001, SI-007)
    "S-49","S-50","S-51","S-52","S-53","S-54",           # Commercial (SI-006: S-49 before S-52)
    "S-55","S-56","S-57","S-58","S-59","S-60","S-61",
    "S-62","S-63","S-64","S-65","S-66",
    "S-67","S-68","S-69",                   # SI-005: References AFTER Commercial/Compliance
    "A-01","A-02","A-03","A-04","A-05","A-06",
]

# ── Section Definitions ──────────────────────────────────────────────────────

# Each entry: name, mandatory_class, assembly_method, primary_source, secondary_source,
#             human_input_required, human_input_notes, placeholders, renderer_metadata,
#             governance_notes, si_rules

SECTION_DEFS: Dict[str, Dict] = {
    "S-01": {
        "name": "Cover Page / Transmittal",
        "mandatory_class": "M-ALL",
        "assembly_method": "TEMPLATE",
        "primary_source": ["TEMPLATE"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Client name, submission date, RFP/tender reference",
        "placeholders": ["client_name", "submission_date", "rfp_reference", "tender_title"],
        "renderer_metadata": {"section_type": "cover", "page_break_before": True},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-02": {
        "name": "Table of Contents",
        "mandatory_class": "M-ALL",
        "assembly_method": "TEMPLATE",
        "primary_source": ["AUTO"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify heading titles after assembly",
        "placeholders": [],
        "renderer_metadata": {"section_type": "toc", "auto_generate": True},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-03": {
        "name": "Company Overview",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-001"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 90},
        "governance_notes": "Never use old company profile; KB-approved content supersedes",
        "si_rules": [],
    },
    "S-04": {
        "name": "Company History",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-002"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 90},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-05": {
        "name": "Awards and Recognition",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-006"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify award table is current before submission",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-06": {
        "name": "Delivery Model",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-007"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 90},
        "governance_notes": "Headcount: 'more than 50 Senior Consultants' ONLY",
        "si_rules": [],
    },
    "S-07": {
        "name": "Geographic Presence",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-008"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 90},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-08": {
        "name": "Key Differentiators",
        "mandatory_class": "OPT",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-009"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "Included when W1S1-009 mandatory (always in corporate block)",
        "si_rules": [],
    },
    "S-09": {
        "name": "Oracle Partnership",
        "mandatory_class": "COND-ORA",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-003"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify OPN Level 1 revalidation; never cite Oracle Gold Partner",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "Never cite 'Oracle Gold Partner' — expired August 2021. Level 1 Partner only.",
        "si_rules": [],
    },
    "S-10": {
        "name": "Acumatica Partnership",
        "mandatory_class": "COND-ACU",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-004"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify certificate currency; Gold Partner — not Gold Certified",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "OAR-E03 Acumatica cert gap — flag if not obtained",
        "si_rules": [],
    },
    "S-11": {
        "name": "BeBanking Product Overview",
        "mandatory_class": "COND-BB",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S1-005"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-12": {
        "name": "B-BBEE Compliance Statement",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["COMPLIANCE_REGISTER"],
        "secondary_source": ["COMP-001"],
        "human_input_required": True,
        "human_input_notes": "Verify B-BBEE cert expiry date; never cite status after 2026-07-31 without renewal",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); flag if submission after that date",
        "si_rules": [],
    },
    "S-13": {
        "name": "Executive Summary",
        "mandatory_class": "M-ALL",
        "assembly_method": "AI-GENERATE",
        "primary_source": ["W1S1-001"],
        "secondary_source": ["TENDER_CONTEXT"],
        "human_input_required": True,
        "human_input_notes": "Mandatory human review; tailor to tender-specific win themes",
        "placeholders": ["client_name", "tender_title", "proposed_solution_summary"],
        "renderer_metadata": {"automation_pct": 20, "ai_assisted": True},
        "governance_notes": "Never use Candidate_Content/ or Review_Required/ in any tender",
        "si_rules": [],
    },
    "S-14": {
        "name": "Understanding of Requirements",
        "mandatory_class": "M-ALL",
        "assembly_method": "AI-GENERATE",
        "primary_source": ["REQUIREMENT_MATRIX"],
        "secondary_source": ["CAP_ASSETS"],
        "human_input_required": True,
        "human_input_notes": "Mandatory human review; drawn from tender RFP/RFQ document",
        "placeholders": ["rfp_requirements_summary"],
        "renderer_metadata": {"automation_pct": 10, "ai_assisted": True},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-15": {
        "name": "Proposed Solution Overview",
        "mandatory_class": "M-ALL",
        "assembly_method": "MERGE",
        "primary_source": ["CAP_ASSETS_PER_BOM"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Review merged content for coherence across modules",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 40, "ai_assisted": True},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-16": {
        "name": "Oracle Fusion HCM Capability",
        "mandatory_class": "COND-HCM",
        "assembly_method": "MERGE",
        "primary_source": ["W3S1-001"],
        "secondary_source": ["W3S1-002","W3S1-003","W3S1-004","W3S1-005","W3S1-006",
                              "W3S1-007","W3S1-009","W4-AI-002","W4-HCM-002"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "Section 14.2 (W3S1-008) and Section 13.2 (W3S1-009 payroll section) NEVER in external submissions",
        "si_rules": [],
    },
    "S-17": {
        "name": "Oracle Fusion ERP Capability",
        "mandatory_class": "COND-ERP",
        "assembly_method": "MERGE",
        "primary_source": ["W2S1-001"],
        "secondary_source": ["W4-ERP-001","W4-ERP-002","W4-ERP-003"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "AM-W4E3-001 ACTIVE — KPMG must NOT be named; anonymous reference only until signed letter registered",
        "si_rules": [],
    },
    "S-18": {
        "name": "Oracle EBS Capability",
        "mandatory_class": "COND-EBS",
        "assembly_method": "DIRECT",
        "primary_source": ["W2S1-002"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Vintage content 2012–2014 — flag for modernisation; verify statistics before submission",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-19": {
        "name": "Oracle OIC / Integration Capability",
        "mandatory_class": "COND-OIC",
        "assembly_method": "DIRECT",
        "primary_source": ["W4-INT-001"],
        "secondary_source": ["W3S1-009"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "HIST-018 billing (R825,170) MUST NEVER appear in external submissions. Section 13.2 (W3S1-009) NEVER external.",
        "si_rules": [],
    },
    "S-20": {
        "name": "Oracle DBA Capability",
        "mandatory_class": "COND-DBA",
        "assembly_method": "DIRECT",
        "primary_source": ["W2S1-003"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify stats are current before submission",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-21": {
        "name": "Oracle Managed Services Capability",
        "mandatory_class": "COND-AMS",
        "assembly_method": "DIRECT",
        "primary_source": ["W2S1-004"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 80},
        "governance_notes": "Oracle platforms only; excluded for Acumatica/BeBanking",
        "si_rules": [],
    },
    "S-22": {
        "name": "OCI Infrastructure",
        "mandatory_class": "COND-OCI",
        "assembly_method": "AI-GENERATE",
        "primary_source": ["OCI-ASSUMPTIONS-V1"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "No standalone OCI narrative yet; use OCI assumption pack as proxy; mandatory review",
        "placeholders": ["oci_scope_description"],
        "renderer_metadata": {"automation_pct": 20, "ai_assisted": True},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-23": {
        "name": "Acumatica Financials",
        "mandatory_class": "COND-ACU",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S2-001"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-24": {
        "name": "Acumatica Distribution",
        "mandatory_class": "COND-ACU",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S2-002"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-25": {
        "name": "Acumatica Manufacturing",
        "mandatory_class": "COND-ACU",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S2-004"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "HyDac sole KB source for manufacturing",
        "si_rules": [],
    },
    "S-26": {
        "name": "Acumatica CRM",
        "mandatory_class": "COND-ACU",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S2-005"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-27": {
        "name": "Acumatica Other Modules",
        "mandatory_class": "COND-ACU",
        "assembly_method": "DIRECT",
        "primary_source": ["W1S2-003","W1S2-006","W1S2-007","W1S2-009"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-28": {
        "name": "Acumatica Managed Services",
        "mandatory_class": "COND-ACU-AMS",
        "assembly_method": "DIRECT",
        "primary_source": ["W5-ACU-001"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 80},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-29": {
        "name": "BeBanking H2H Banking",
        "mandatory_class": "COND-BB",
        "assembly_method": "MERGE",
        "primary_source": ["W1S3-001","W1S3-002","W1S3-008"],
        "secondary_source": ["W1S3-003","W1S3-004","W1S3-005","W1S3-006","W1S3-007",
                              "W1S3-009","W1S3-010"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 85},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-30": {
        "name": "Scope of Work — Inclusions",
        "mandatory_class": "M-FIXED",
        "assembly_method": "EXTRACT",
        "primary_source": ["ASP_INC_SECTIONS"],
        "secondary_source": ["CAP_ASSETS"],
        "human_input_required": True,
        "human_input_notes": "Review extracted scope inclusions before submission",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 50},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-31": {
        "name": "Scope of Work — Exclusions",
        "mandatory_class": "M-FIXED",
        "assembly_method": "EXTRACT",
        "primary_source": ["ASP_EXC_SECTIONS"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Review extracted scope exclusions before submission",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-32": {
        "name": "Deliverables",
        "mandatory_class": "M-ALL",
        "assembly_method": "EXTRACT",
        "primary_source": ["DELIVERY_PATTERN"],
        "secondary_source": ["METHODOLOGY_ASSET"],
        "human_input_required": True,
        "human_input_notes": "Review deliverables list for completeness",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 50},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-33": {
        "name": "Dependencies",
        "mandatory_class": "M-FIXED",
        "assembly_method": "EXTRACT",
        "primary_source": ["ASP_DEP_SECTIONS"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Review client dependencies extracted from assumption packs",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-34": {
        "name": "Implementation Methodology",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["W2S1-005","W5-METH-001"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Tailor phases to tender-specific timeline; AMS: EXCLUDED (use S-73 instead)",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 65},
        "governance_notes": "SI-001: EXCLUDED for Pattern 13 AMS; W2S1-005 for Oracle; W5-METH-001 for Acumatica/BeBanking",
        "si_rules": ["SI-001"],
    },
    "S-35": {
        "name": "Project Plan / Timeline",
        "mandatory_class": "M-ALL",
        "assembly_method": "TEMPLATE",
        "primary_source": ["PROJECT_PLAN_TEMPLATES"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Insert project dates and resource assignments; EXCLUDED for AMS",
        "placeholders": ["project_start_date", "go_live_date", "project_duration_weeks"],
        "renderer_metadata": {"automation_pct": 50},
        "governance_notes": "EXCLUDED for Pattern 13 AMS",
        "si_rules": ["SI-001"],
    },
    "S-36": {
        "name": "Project Governance",
        "mandatory_class": "M-ALL",
        "assembly_method": "EXTRACT",
        "primary_source": ["W2S1-005"],
        "secondary_source": ["W5-METH-001"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-37": {
        "name": "RAID Framework",
        "mandatory_class": "M-ALL",
        "assembly_method": "MERGE",
        "primary_source": ["METHODOLOGY_ASSET"],
        "secondary_source": ["RSK_ASSETS"],
        "human_input_required": True,
        "human_input_notes": "Risk register populated from Risk Library; review before submission",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 30},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-38": {
        "name": "Change Control Framework",
        "mandatory_class": "M-FIXED",
        "assembly_method": "DIRECT",
        "primary_source": ["CR_PRICING_MODEL"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "Do not expose CR thresholds or rates; EXCLUDED for AMS — use S-73",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "SI-001: EXCLUDED for Pattern 13 AMS; S-73 is the single AMS change management section",
        "si_rules": ["SI-001"],
    },
    "S-39": {
        "name": "Testing Strategy",
        "mandatory_class": "OPT",
        "assembly_method": "EXTRACT",
        "primary_source": ["DELIVERY_PATTERN"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "EXCLUDED for AMS",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 50},
        "governance_notes": "EXCLUDED for Pattern 13 AMS",
        "si_rules": [],
    },
    "S-40": {
        "name": "Data Migration",
        "mandatory_class": "COND-MIG",
        "assembly_method": "EXTRACT",
        "primary_source": ["ASP_DAT_SECTIONS"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "EXCLUDED for AMS",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "EXCLUDED for Pattern 13 AMS",
        "si_rules": [],
    },
    "S-41": {
        "name": "Training Plan",
        "mandatory_class": "OPT",
        "assembly_method": "EXTRACT",
        "primary_source": ["ASP_TRN_SECTIONS"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "EXCLUDED for AMS",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 50},
        "governance_notes": "EXCLUDED for Pattern 13 AMS",
        "si_rules": [],
    },
    "S-42": {
        "name": "Cutover / Go-Live Plan",
        "mandatory_class": "M-FIXED",
        "assembly_method": "EXTRACT",
        "primary_source": ["ASP_CUT_SECTIONS"],
        "secondary_source": ["DELIVERY_PATTERN"],
        "human_input_required": True,
        "human_input_notes": "EXCLUDED for AMS (no cutover in ongoing AMS)",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 50},
        "governance_notes": "EXCLUDED for Pattern 13 AMS",
        "si_rules": [],
    },
    "S-43": {
        "name": "Hypercare / Post-Go-Live Transition",
        "mandatory_class": "COND-POST-GOLIVE",
        "assembly_method": "EXTRACT",
        "primary_source": ["DELIVERY_PATTERN"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "EXCLUDED for AMS",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 50},
        "governance_notes": "EXCLUDED for Pattern 13 AMS",
        "si_rules": [],
    },
    "S-44": {
        "name": "Disaster Recovery",
        "mandatory_class": "OPT",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["05_Methodologies/Disaster_Recovery/"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Disaster Recovery methodology folder is EMPTY — placeholder only",
        "placeholders": ["disaster_recovery_plan"],
        "renderer_metadata": {"automation_pct": 0, "gap": "DR methodology not authored"},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-45": {
        "name": "Security Architecture",
        "mandatory_class": "COND-OCI",
        "assembly_method": "EXTRACT",
        "primary_source": ["ASP_SEC_SECTIONS"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Included when security_in_scope or OCI in scope",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 30},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-46": {
        "name": "Team Structure",
        "mandatory_class": "M-ALL",
        "assembly_method": "TEMPLATE",
        "primary_source": ["CONSULTANT_INDEX"],
        "secondary_source": ["DELIVERY_PATTERN"],
        "human_input_required": True,
        "human_input_notes": "BU Lead selects named consultants; EXCLUDED for AMS",
        "placeholders": ["team_structure_diagram"],
        "renderer_metadata": {"automation_pct": 30},
        "governance_notes": "EXCLUDED for Pattern 13 AMS",
        "si_rules": [],
    },
    "S-47": {
        "name": "Named Consultant CVs",
        "mandatory_class": "OPT",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["APPTM"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "ADR-001: CVs from APPTime only — never from KB records; EXCLUDED for AMS",
        "placeholders": ["consultant_cvs"],
        "renderer_metadata": {"automation_pct": 0},
        "governance_notes": "ADR-001 applies always — never generate CV text from KB consultant records",
        "si_rules": ["ADR-001"],
    },
    "S-48": {
        "name": "Consultant Profiles (Summary)",
        "mandatory_class": "OPT",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["APPTM"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "ADR-001: APPTime is authoritative; EXCLUDED for AMS",
        "placeholders": ["consultant_profiles"],
        "renderer_metadata": {"automation_pct": 0},
        "governance_notes": "ADR-001: Never generate CV text from KB records",
        "si_rules": ["ADR-001"],
    },
    "S-49": {
        "name": "Key Assumptions (Body Section)",
        "mandatory_class": "M-FIXED",
        "assembly_method": "MERGE",
        "primary_source": ["ASSEMBLY_ENGINE_KEY_ASSUMPTIONS"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Governance sign-off required; SI-006: must appear BEFORE S-52 Pricing",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 95},
        "governance_notes": "SI-006: S-49 Key Assumptions assembled BEFORE S-52 Pricing in all proposals",
        "si_rules": ["SI-006"],
    },
    "S-50": {
        "name": "Risk Register",
        "mandatory_class": "M-FIXED",
        "assembly_method": "AI-GENERATE",
        "primary_source": ["RSK_ASSETS"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Mandatory human review; Risk Library standard defined (WP18B)",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 5, "ai_assisted": True},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-51": {
        "name": "Commercial Assumptions",
        "mandatory_class": "M-FIXED",
        "assembly_method": "MERGE",
        "primary_source": ["ASSEMBLY_ENGINE_ASS_SCHEDULE"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Governance sign-off required; extracted from selected assumption packs",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 95},
        "governance_notes": "Never assemble a fixed-price proposal without the commercial file",
        "si_rules": [],
    },
    "S-52": {
        "name": "Commercials / Pricing",
        "mandatory_class": "M-FIXED",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["COMMERCIAL_FRAMEWORK"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Commercial Director authority; never expose rates; SI-006: S-49 must precede this",
        "placeholders": ["pricing_table", "commercial_terms"],
        "renderer_metadata": {"automation_pct": 0},
        "governance_notes": "SI-006: S-49 Key Assumptions BEFORE S-52 Pricing in all proposals",
        "si_rules": ["SI-006"],
    },
    "S-53": {
        "name": "Rate Card Basis",
        "mandatory_class": "OPT",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["RATE_CARD_FRAMEWORK"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Never expose rate card values directly",
        "placeholders": ["rate_card_basis"],
        "renderer_metadata": {"automation_pct": 0},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-54": {
        "name": "Estimation Basis",
        "mandatory_class": "OPT",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["ESTIMATION_GUIDE"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "BU Lead sign-off",
        "placeholders": ["estimation_basis"],
        "renderer_metadata": {"automation_pct": 0},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-55": {
        "name": "Compliance Schedule",
        "mandatory_class": "M-ALL",
        "assembly_method": "EXTRACT",
        "primary_source": ["COMPLIANCE_REGISTER"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify all expiry dates > submission date; expired items flagged",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "Never submit a proposal with expired compliance documents",
        "si_rules": [],
    },
    "S-56": {
        "name": "Company Registration",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["02_Corporate/Resolutions/"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify CIPC registration current",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-57": {
        "name": "Tax Clearance",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["COMP-005"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify expiry date > submission date (current valid to 2027-02-23)",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-58": {
        "name": "Directors' Resolution",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["COMP-011"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Renewed 2026-06-15; confirm still valid at submission date",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-59": {
        "name": "B-BBEE Certificate",
        "mandatory_class": "M-SA",
        "assembly_method": "DIRECT",
        "primary_source": ["COMP-001"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Expires 2026-07-31 — do not submit after that date without renewal cert",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "OAR-C01/C02/A01: B-BBEE cert expires 2026-07-31; never cite BEE status after that date without renewal",
        "si_rules": [],
    },
    "S-60": {
        "name": "Public Liability Insurance",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["COMP-008"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Obtained 2026-06-15; confirm exact expiry from policy (OAR pending confirmation)",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-61": {
        "name": "Professional Indemnity",
        "mandatory_class": "OPT",
        "assembly_method": "DIRECT",
        "primary_source": ["01_Compliance/"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify expiry date > submission date",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-62": {
        "name": "Oracle OPN Certificate",
        "mandatory_class": "COND-ORA",
        "assembly_method": "DIRECT",
        "primary_source": ["COMP-007"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Level 1 Partner only; annual OPN revalidation; never cite Gold Partner",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "Never cite 'Oracle Gold Partner' — expired August 2021",
        "si_rules": [],
    },
    "S-63": {
        "name": "Acumatica Partner Certificate",
        "mandatory_class": "COND-ACU",
        "assembly_method": "DIRECT",
        "primary_source": ["COMP-016"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Gold Partner — not Gold Certified; OAR-E03 gap — flag if cert not obtained",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 30},
        "governance_notes": "OAR-E03 Acumatica partner cert gap",
        "si_rules": [],
    },
    "S-64": {
        "name": "ISO / Other Certifications",
        "mandatory_class": "OPT",
        "assembly_method": "DIRECT",
        "primary_source": ["01_Compliance/"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Verify expiry dates > submission date",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-65": {
        "name": "POPIA Policy",
        "mandatory_class": "OPT",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["OAR-E01"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "OAR-E01 — document not yet obtained; placeholder only",
        "placeholders": ["popia_policy"],
        "renderer_metadata": {"automation_pct": 0, "gap": "OAR-E01 not resolved"},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-66": {
        "name": "PAIA Manual",
        "mandatory_class": "OPT",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["OAR-E02"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "OAR-E02 — document not yet obtained; placeholder only",
        "placeholders": ["paia_manual"],
        "renderer_metadata": {"automation_pct": 0, "gap": "OAR-E02 not resolved"},
        "governance_notes": "",
        "si_rules": [],
    },
    "S-67": {
        "name": "Client References",
        "mandatory_class": "M-ALL",
        "assembly_method": "TEMPLATE",
        "primary_source": ["REFERENCE_MASTER"],
        "secondary_source": ["04_References/"],
        "human_input_required": True,
        "human_input_notes": "AM approval mandatory at each tender; only signed letters; vintage >5 years flagged",
        "placeholders": ["client_references_table"],
        "renderer_metadata": {"automation_pct": 50},
        "governance_notes": "Never cite DFA, CCBA, SAA. Never cite Redpath Mining until Rule 21.5 waived. Never name Hollywood Bets without AM approval. Never name KPMG in PPM/ERP until AM-W4E3-001 cleared.",
        "si_rules": ["SI-005"],
    },
    "S-68": {
        "name": "Case Studies",
        "mandatory_class": "OPT",
        "assembly_method": "AI-GENERATE",
        "primary_source": ["CAP_ASSETS"],
        "secondary_source": ["REF_LETTERS"],
        "human_input_required": True,
        "human_input_notes": "Mandatory human review; client naming restrictions apply; all facts from approved KB sources only",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 15, "ai_assisted": True},
        "governance_notes": "Client naming restrictions: no DFA/CCBA/SAA; all facts from approved KB sources only",
        "si_rules": [],
    },
    "S-69": {
        "name": "Reference Letters",
        "mandatory_class": "OPT",
        "assembly_method": "DIRECT",
        "primary_source": ["04_References/"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "AM approval; only signed, registered letters; REFERENCE_MASTER.csv canonical register",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "",
        "si_rules": ["SI-005"],
    },
    "S-70": {
        "name": "Support Model",
        "mandatory_class": "COND-AMS",
        "assembly_method": "MERGE",
        "primary_source": ["AMS-ASSUMPTIONS-V1"],
        "secondary_source": ["W2S1-004","W5-ACU-001"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 75},
        "governance_notes": "AMS-only section; assembled second in AMS Support block",
        "si_rules": ["SI-001"],
    },
    "S-71": {
        "name": "SLA Framework",
        "mandatory_class": "COND-AMS",
        "assembly_method": "EXTRACT",
        "primary_source": ["AMS-ASSUMPTIONS-V1"],
        "secondary_source": ["EBS-AMS-SLA-OVERLAY-V1"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 75},
        "governance_notes": "SI-007: SLA tier table ONLY (P1=1h, P2=4h, P3=1BD, P4=3BD); response ≠ resolution disclaimer; DO NOT include incident process — belongs in S-72",
        "si_rules": ["SI-001","SI-007"],
    },
    "S-72": {
        "name": "Incident Management",
        "mandatory_class": "COND-AMS",
        "assembly_method": "EXTRACT",
        "primary_source": ["AMS-ASSUMPTIONS-V1"],
        "secondary_source": ["EBS-AMS-SLA-OVERLAY-V1"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "SI-007: Incident classification process ONLY; escalation path; lifecycle (log→triage→assign→resolve→close→review); DO NOT re-state SLA tier values — reference as 'per S-71 SLA Framework'",
        "si_rules": ["SI-001","SI-007"],
    },
    "S-73": {
        "name": "Change Request Process",
        "mandatory_class": "COND-AMS",
        "assembly_method": "EXTRACT",
        "primary_source": ["AMS-ASSUMPTIONS-V1"],
        "secondary_source": ["CR_PRICING_MODEL"],
        "human_input_required": False,
        "human_input_notes": "Do not expose CR thresholds or BU decisions; use assumption pack language verbatim",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "SI-001: This section REPLACES S-38 for all AMS proposals (Pattern 13). Single governing change management section for AMS.",
        "si_rules": ["SI-001"],
    },
    "S-74": {
        "name": "Resource Model (AMS)",
        "mandatory_class": "COND-AMS",
        "assembly_method": "EXTRACT",
        "primary_source": ["AMS-ASSUMPTIONS-V1"],
        "secondary_source": ["EBS-DRM-ASSUMPTIONS-V1"],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "AMS-only; assembled FIRST in AMS Support block (before S-70)",
        "si_rules": ["SI-001"],
    },
    "S-75": {
        "name": "Release Management",
        "mandatory_class": "COND-AMS",
        "assembly_method": "EXTRACT",
        "primary_source": ["AMS-ASSUMPTIONS-V1"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "Oracle quarterly release advisory included; regression testing of patch = excluded unless scoped",
        "si_rules": ["SI-001"],
    },
    "S-76": {
        "name": "Monitoring and Reporting",
        "mandatory_class": "COND-AMS",
        "assembly_method": "EXTRACT",
        "primary_source": ["AMS-ASSUMPTIONS-V1"],
        "secondary_source": [],
        "human_input_required": False,
        "human_input_notes": "",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "Mailbox monitoring standard; proactive monitoring = separate scope unless contracted",
        "si_rules": ["SI-001"],
    },
    "A-01": {
        "name": "Complete Assumption Schedule",
        "mandatory_class": "M-FIXED",
        "assembly_method": "MERGE",
        "primary_source": ["ASSEMBLY_ENGINE_ASS_SCHEDULE"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Governance sign-off; all WP17D-1 validation checks must pass; counts match body sections",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 95},
        "governance_notes": "",
        "si_rules": [],
    },
    "A-02": {
        "name": "Consultant CVs",
        "mandatory_class": "OPT",
        "assembly_method": "PLACEHOLDER",
        "primary_source": ["APPTM"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "ADR-001: APPTime is authoritative — never generate from KB records",
        "placeholders": ["consultant_cvs"],
        "renderer_metadata": {"automation_pct": 0},
        "governance_notes": "ADR-001 applies always — never generate CV text from KB consultant records",
        "si_rules": ["ADR-001"],
    },
    "A-03": {
        "name": "Reference Letters",
        "mandatory_class": "OPT",
        "assembly_method": "DIRECT",
        "primary_source": ["04_References/"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "AM approval; signed only",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 60},
        "governance_notes": "",
        "si_rules": [],
    },
    "A-04": {
        "name": "Certifications and Compliance",
        "mandatory_class": "M-ALL",
        "assembly_method": "DIRECT",
        "primary_source": ["01_Compliance/"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "All expiry dates must be > submission date",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "Never submit a proposal with expired compliance documents",
        "si_rules": [],
    },
    "A-05": {
        "name": "B-BBEE Certificate",
        "mandatory_class": "M-SA",
        "assembly_method": "DIRECT",
        "primary_source": ["COMP-001"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "Expiry 2026-07-31; OAR-C01/C02/A01 BEE blocker",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "B-BBEE cert expires 2026-07-31; never cite BEE status after that date without renewal cert",
        "si_rules": [],
    },
    "A-06": {
        "name": "Company Registration",
        "mandatory_class": "OPT",
        "assembly_method": "DIRECT",
        "primary_source": ["02_Corporate/"],
        "secondary_source": [],
        "human_input_required": True,
        "human_input_notes": "CIPC current",
        "placeholders": [],
        "renderer_metadata": {"automation_pct": 70},
        "governance_notes": "",
        "si_rules": [],
    },
}

# ── Asset → Section mapping ──────────────────────────────────────────────────
# Maps CAP/ASP asset_id → list of section_ids it contributes to (as source)

ASSET_TO_SECTIONS: Dict[str, List[str]] = {
    # Corporate block (short IDs — match ARE canonical)
    "W1S1-001": ["S-03", "S-13"],
    "W1S1-002": ["S-04"],
    "W1S1-006": ["S-05"],
    "W1S1-007": ["S-06"],
    "W1S1-008": ["S-07"],
    "W1S1-009": ["S-08"],
    "W1S1-003": ["S-09", "S-62"],
    "W1S1-004": ["S-10", "S-63"],
    "W1S1-005": ["S-11", "S-29"],
    # Acumatica modules (short IDs match ARE)
    "W1S2-001": ["S-23"],
    "W1S2-002": ["S-24"],
    "W1S2-003": ["S-27"],
    "W1S2-004": ["S-25"],
    "W1S2-005": ["S-26"],
    "W1S2-006-ACU-FieldServices":       ["S-27"],
    "W1S2-007-ACU-PayrollIntegration":  ["S-27"],
    "W1S2-009": ["S-27"],
    # BeBanking assets (short IDs match ARE)
    "W1S3-001": ["S-29"],
    "W1S3-002": ["S-29"],
    "W1S3-003": ["S-29"],
    "W1S3-004": ["S-29"],
    "W1S3-005": ["S-29"],
    "W1S3-006": ["S-29"],
    "W1S3-007": ["S-29", "S-45"],
    "W1S3-008": ["S-29"],
    "W1S3-009": ["S-29"],
    "W1S3-010": ["S-29"],
    # Oracle capability (short W2S1-001..004 match ARE)
    "W2S1-001": ["S-17"],
    "W2S1-002": ["S-18"],
    "W2S1-003": ["S-20"],
    "W2S1-004": ["S-21", "S-70"],
    "W2S1-005-ORA-ImplementationMethodology": ["S-34", "S-36"],
    # Oracle HCM Wave 3 (full canonical IDs)
    "W3S1-001-ORA-HCMCore":                   ["S-16"],
    "W3S1-002-ORA-TalentMgmt":                ["S-16"],
    "W3S1-003-ORA-RecruitingCloud":            ["S-16"],
    "W3S1-004-ORA-LearningCloud":              ["S-16"],
    "W3S1-005-ORA-WorkforceCompensation":      ["S-16"],
    "W3S1-006-ORA-HCMAnalytics":              ["S-16"],
    "W3S1-007-ORA-WorkforceManagement":        ["S-16"],
    # W3S1-008-ORA-HelpDesk deliberately omitted: Section 14.2 NEVER in external submissions
    "W3S1-009-ORA-PayrollInterface-Integration": ["S-19"],
    # Oracle Wave 4 (full canonical IDs)
    "W4-AI-002-ORA-AISkills":          ["S-16"],
    "W4-ERP-001-ORA-FusionFinancials":  ["S-17"],
    "W4-ERP-002-ORA-FusionProcurement": ["S-17"],
    "W4-ERP-003-ORA-PPM":               ["S-17"],
    "W4-HCM-002-ORA-Journeys":          ["S-16"],
    "W4-INT-001-ORA-OICAccelerators":   ["S-19"],
    # Cross-platform Wave 5 (full canonical IDs)
    "W5-ACU-001-ACU-SupportManagedServices":     ["S-28", "S-70"],
    "W5-METH-001-ERP-ImplementationMethodology": ["S-34", "S-36"],
    # Assumption packs
    "HCM-BASE-ASSUMPTIONS-V1":         ["S-49", "S-51", "A-01"],
    "HCM-RECRUITING-ASSUMPTIONS-V1":   ["S-49", "S-51", "A-01"],
    "HCM-LEARNING-ASSUMPTIONS-V1":     ["S-49", "S-51", "A-01"],
    "HCM-TALENT-ASSUMPTIONS-V1":       ["S-49", "S-51", "A-01"],
    "HCM-COMPENSATION-ASSUMPTIONS-V1": ["S-49", "S-51", "A-01"],
    "OIC-ASSUMPTIONS-V1":              ["S-49", "S-51", "A-01"],
    "ERP-ASSUMPTIONS-V1":              ["S-49", "S-51", "A-01"],
    "OCI-ASSUMPTIONS-V1":              ["S-22", "S-45", "S-49", "S-51", "A-01"],
    "AMS-ASSUMPTIONS-V1":              ["S-49", "S-51", "S-70", "S-71", "S-72",
                                        "S-73", "S-74", "S-75", "S-76", "A-01"],
    "EBS-AMS-SLA-OVERLAY-V1":          ["S-71", "S-74"],
    "EBS-DRM-ASSUMPTIONS-V1":          ["S-74"],
    "ACU-BASE-ASSUMPTIONS-V1":         ["S-49", "S-51", "A-01"],
    "BEBANKING-BASE-ASSUMPTIONS-V1":   ["S-49", "S-51", "A-01"],
}

# Sections driven by specific CAP/ASP assets (any MANDATORY or OPTIONAL_SELECTED triggers inclusion)
# All IDs match ARE canonical asset_id values
SECTION_ASSET_DRIVERS: Dict[str, List[str]] = {
    "S-08": ["W1S1-009"],
    "S-09": ["W1S1-003"],
    "S-10": ["W1S1-004"],
    "S-11": ["W1S1-005"],
    "S-16": ["W3S1-001-ORA-HCMCore","W3S1-002-ORA-TalentMgmt","W3S1-003-ORA-RecruitingCloud",
             "W3S1-004-ORA-LearningCloud","W3S1-005-ORA-WorkforceCompensation",
             "W3S1-006-ORA-HCMAnalytics","W3S1-007-ORA-WorkforceManagement",
             "W3S1-009-ORA-PayrollInterface-Integration",
             "W4-AI-002-ORA-AISkills","W4-HCM-002-ORA-Journeys"],
    "S-17": ["W2S1-001","W4-ERP-001-ORA-FusionFinancials",
             "W4-ERP-002-ORA-FusionProcurement","W4-ERP-003-ORA-PPM"],
    "S-18": ["W2S1-002"],
    "S-19": ["W4-INT-001-ORA-OICAccelerators","W3S1-009-ORA-PayrollInterface-Integration"],
    "S-20": ["W2S1-003"],
    "S-21": ["W2S1-004"],
    "S-22": ["OCI-ASSUMPTIONS-V1"],
    "S-23": ["W1S2-001"],
    "S-24": ["W1S2-002"],
    "S-25": ["W1S2-004"],
    "S-26": ["W1S2-005"],
    "S-27": ["W1S2-003","W1S2-006-ACU-FieldServices",
             "W1S2-007-ACU-PayrollIntegration","W1S2-009"],
    "S-28": ["W5-ACU-001-ACU-SupportManagedServices"],
    "S-29": ["W1S3-001","W1S3-002","W1S3-003","W1S3-004","W1S3-005",
             "W1S3-006","W1S3-007","W1S3-008","W1S3-009","W1S3-010"],
    "S-34": ["W2S1-005-ORA-ImplementationMethodology","W5-METH-001-ERP-ImplementationMethodology"],
    "S-36": ["W2S1-005-ORA-ImplementationMethodology","W5-METH-001-ERP-ImplementationMethodology"],
    "S-45": ["OCI-ASSUMPTIONS-V1","W1S3-007"],
    "S-62": ["W1S1-003"],
    "S-63": ["W1S1-004"],
    "S-70": ["AMS-ASSUMPTIONS-V1","W2S1-004","W5-ACU-001-ACU-SupportManagedServices"],
    "S-71": ["AMS-ASSUMPTIONS-V1","EBS-AMS-SLA-OVERLAY-V1"],
    "S-72": ["AMS-ASSUMPTIONS-V1"],
    "S-73": ["AMS-ASSUMPTIONS-V1"],
    "S-74": ["AMS-ASSUMPTIONS-V1","EBS-DRM-ASSUMPTIONS-V1"],
    "S-75": ["AMS-ASSUMPTIONS-V1"],
    "S-76": ["AMS-ASSUMPTIONS-V1"],
}

# Sections that are always MANDATORY regardless of asset selection.
# AMS exclusions (AMS_EXCLUDED) are checked BEFORE this set, so M-ALL sections
# that are also in AMS_EXCLUDED will be EXCLUDED for AMS and MANDATORY for non-AMS.
ALWAYS_MANDATORY = {
    "S-01","S-02","S-03","S-04","S-05","S-06","S-07",
    "S-12","S-13","S-14","S-15","S-32","S-36","S-37",
    # M-ALL sections that are AMS-excluded: reach here only for non-AMS → MANDATORY
    "S-34","S-35","S-46",
    "S-49","S-50","S-51","S-52",
    "S-55","S-56","S-57","S-58","S-59","S-60",
    "S-67","A-01","A-04","A-05",
    # M-FIXED (all APPSolve tenders are fixed-price)
    "S-30","S-31","S-33","S-38","S-42",
}

# ── Section Decision ─────────────────────────────────────────────────────────

@dataclass
class SectionDecision:
    section_id: str
    section_name: str
    include_status: str          # MANDATORY / OPTIONAL_SELECTED / EXCLUDED / DEFAULT_EXCLUDED
    rationale: str
    assembly_order: int
    assembly_method: str
    merge_strategy: str
    source_assets: List[str]
    placeholders: List[str]
    human_input_required: bool
    human_input_notes: str
    renderer_metadata: Dict[str, Any]
    governance_constraints: List[str]
    si_rules_applied: List[str]


@dataclass
class SectionManifest:
    manifest_id: str
    tender_id: str
    tender_pattern: str
    platform: str
    engagement_type: str
    industry: str
    generated_at: str
    engine_version: str
    sections: Dict[str, SectionDecision] = field(default_factory=dict)
    assembly_sequence: List[str] = field(default_factory=list)
    mandatory_count: int = 0
    optional_count: int = 0
    excluded_count: int = 0
    default_excluded_count: int = 0
    validation_errors: List[str] = field(default_factory=list)
    validation_warnings: List[str] = field(default_factory=list)
    governance_flags: List[str] = field(default_factory=list)


# ── Engine ───────────────────────────────────────────────────────────────────

def build_section_manifest(tender_context: Dict[str, Any]) -> SectionManifest:
    """Deterministically assemble the section manifest for a tender context."""
    tid       = tender_context.get("tender_id", "UNKNOWN")
    pattern   = str(tender_context.get("tender_pattern", ""))
    platform  = tender_context.get("platform", "")
    eng_type  = tender_context.get("engagement_type", "Implementation")
    industry  = tender_context.get("industry", "")

    is_ams  = (eng_type == "AMS")
    is_ora  = platform in ["Oracle HCM Cloud","Oracle ERP Cloud","Oracle EBS",
                           "Oracle Integration Cloud"]
    is_acu  = (platform == "Acumatica")
    is_bb   = (platform == "BeBanking")

    # Step 1: get CAP/ASP selections from ARE (select_assets runs ALL_RULES: CAP + ASP)
    all_selections: Dict[str, str] = select_assets(tender_context)

    selected_statuses = {"MANDATORY", "OPTIONAL_SELECTED"}

    # Step 2: determine include_status for each section
    decisions: Dict[str, SectionDecision] = {}

    for sid, sdef in SECTION_DEFS.items():
        mc     = sdef["mandatory_class"]
        method = sdef["assembly_method"]
        hi     = sdef["human_input_required"]
        hin    = sdef["human_input_notes"]
        ph     = sdef.get("placeholders", [])
        rmeta  = dict(sdef.get("renderer_metadata", {}))
        gnotes = sdef.get("governance_notes", "")
        si     = sdef.get("si_rules", [])

        # Collect source assets that are selected
        driver_assets = SECTION_ASSET_DRIVERS.get(sid, [])
        active_assets = [a for a in driver_assets if all_selections.get(a) in selected_statuses]

        # Determine include status and rationale
        status   = "DEFAULT_EXCLUDED"
        rationale = "No selection rule triggered"

        # ── AMS exclusions (override everything) ──
        if is_ams and sid in AMS_EXCLUDED:
            status    = "EXCLUDED"
            rationale = f"EXCLUDED — AMS Pattern 13 exclusion; SI-001 applies" if sid == "S-38" else f"EXCLUDED — AMS Pattern 13 excludes {sid}"

        # ── AMS-only sections excluded for non-AMS ──
        elif sid in AMS_ONLY and not is_ams:
            status    = "EXCLUDED"
            rationale = f"EXCLUDED — {sid} applies to AMS engagements only"

        # ── Always mandatory ──
        elif sid in ALWAYS_MANDATORY:
            # S-38 excluded for AMS (above), S-42 excluded for AMS (above)
            # Special: S-36 needs a methodology asset
            if sid == "S-36":
                meth_assets = [a for a in ["W2S1-005","W5-METH-001"]
                               if all_selections.get(a) in selected_statuses]
                if meth_assets or (is_ams and all_selections.get("AMS-ASSUMPTIONS-V1") in selected_statuses):
                    status    = "MANDATORY"
                    rationale = "M-ALL — methodology asset selected or AMS; project governance mandatory"
                else:
                    status    = "MANDATORY"
                    rationale = "M-ALL — governance mandatory in all proposals"
            else:
                status    = "MANDATORY"
                rationale = f"{mc} — mandatory in all proposals"

        # ── Platform-conditional sections ──
        elif mc == "COND-ORA":
            if is_ora and active_assets:
                # Determine if mandatory or optional from selection
                m_assets = [a for a in driver_assets if all_selections.get(a) == "MANDATORY"]
                status    = "MANDATORY" if m_assets else "OPTIONAL_SELECTED"
                rationale = f"COND-ORA — platform={platform}; drivers: {active_assets}"
            elif is_ora:
                status    = "OPTIONAL_SELECTED"
                rationale = f"COND-ORA — Oracle platform; default optional"
            else:
                status    = "EXCLUDED"
                rationale = f"EXCLUDED — {sid} requires Oracle platform; platform={platform}"

        elif mc == "COND-ACU":
            if is_acu and active_assets:
                m_assets = [a for a in driver_assets if all_selections.get(a) == "MANDATORY"]
                status    = "MANDATORY" if m_assets else "OPTIONAL_SELECTED"
                rationale = f"COND-ACU — platform=Acumatica; drivers: {active_assets}"
            elif is_acu:
                status    = "OPTIONAL_SELECTED"
                rationale = "COND-ACU — Acumatica platform; optional"
            else:
                status    = "EXCLUDED"
                rationale = f"EXCLUDED — {sid} requires Acumatica platform"

        elif mc == "COND-ACU-AMS":
            if is_acu and is_ams and active_assets:
                status    = "MANDATORY"
                rationale = "COND-ACU-AMS — Acumatica AMS engagement; W5-ACU-001 mandatory"
            elif is_acu and active_assets:
                status    = "OPTIONAL_SELECTED"
                rationale = "COND-ACU — Acumatica support scope; W5-ACU-001 optional"
            else:
                status    = "EXCLUDED"
                rationale = f"EXCLUDED — {sid} requires Acumatica AMS"

        elif mc == "COND-BB":
            if is_bb and active_assets:
                m_assets = [a for a in driver_assets if all_selections.get(a) == "MANDATORY"]
                status    = "MANDATORY" if m_assets else "OPTIONAL_SELECTED"
                rationale = f"COND-BB — platform=BeBanking; drivers: {active_assets}"
            elif is_bb:
                status    = "OPTIONAL_SELECTED"
                rationale = "COND-BB — BeBanking platform"
            else:
                status    = "EXCLUDED"
                rationale = f"EXCLUDED — {sid} requires BeBanking platform"

        elif mc == "COND-AMS":
            if is_ams and active_assets:
                status    = "MANDATORY"
                rationale = f"COND-AMS — AMS engagement; drivers: {active_assets}"
            elif is_ams:
                status    = "MANDATORY"
                rationale = "COND-AMS — AMS engagement; section mandatory for support model"
            else:
                status    = "EXCLUDED"
                rationale = f"EXCLUDED — {sid} applies to AMS only"

        elif mc in ("COND-HCM","COND-ERP","COND-EBS","COND-OIC","COND-DBA","COND-OCI",
                    "COND-MIG","COND-POST-GOLIVE"):
            if active_assets:
                m_assets = [a for a in driver_assets if all_selections.get(a) == "MANDATORY"]
                status    = "MANDATORY" if m_assets else "OPTIONAL_SELECTED"
                rationale = f"{mc} — drivers: {active_assets}"
            else:
                status    = "DEFAULT_EXCLUDED"
                rationale = f"{mc} — no driver assets selected"

        elif mc in ("OPT", "M-SA"):
            if mc == "M-SA":
                status    = "MANDATORY"
                rationale = "M-SA — mandatory for South African entities (all APPSolve tenders)"
            elif active_assets:
                m_assets = [a for a in driver_assets if all_selections.get(a) == "MANDATORY"]
                status    = "MANDATORY" if m_assets else "OPTIONAL_SELECTED"
                rationale = f"OPT — driver assets selected: {active_assets}"
            else:
                status    = "DEFAULT_EXCLUDED"
                rationale = "OPT — no condition triggered; not in scope"

        # Determine all source assets for this section
        section_source_assets: List[str] = []
        for asset_id, sections_list in ASSET_TO_SECTIONS.items():
            if sid in sections_list and all_selections.get(asset_id) in selected_statuses:
                section_source_assets.append(asset_id)

        # Merge strategy
        merge_strategy = "N/A"
        if method == "MERGE":
            merge_strategy = "Ordered concatenation; primary asset first; secondary assets appended by module selection order"
        elif method == "EXTRACT":
            merge_strategy = "Extract designated sub-sections from source documents"

        # Governance constraints list
        gov_list = [gnotes] if gnotes else []

        decisions[sid] = SectionDecision(
            section_id=sid,
            section_name=sdef["name"],
            include_status=status,
            rationale=rationale,
            assembly_order=0,     # set below
            assembly_method=method,
            merge_strategy=merge_strategy,
            source_assets=section_source_assets,
            placeholders=list(ph),
            human_input_required=hi,
            human_input_notes=hin,
            renderer_metadata=rmeta,
            governance_constraints=gov_list,
            si_rules_applied=list(si),
        )

    # Step 3: build assembly sequence (order depends on AMS vs standard)
    base_order = AMS_ORDER if is_ams else STANDARD_ORDER
    sequence   = [sid for sid in base_order
                  if decisions[sid].include_status in ("MANDATORY","OPTIONAL_SELECTED")]

    for pos, sid in enumerate(sequence, start=1):
        decisions[sid].assembly_order = pos

    # Step 4: SI-006 validation — S-49 must precede S-52
    si6_violation = False
    if "S-49" in sequence and "S-52" in sequence:
        if sequence.index("S-49") > sequence.index("S-52"):
            si6_violation = True

    # Step 5: validation
    errors: List[str]   = []
    warnings: List[str] = []
    gov_flags: List[str] = []

    mandatory_included = {sid for sid, d in decisions.items() if d.include_status == "MANDATORY"}
    M_ALL_SECTIONS = {sid for sid, sdef in SECTION_DEFS.items()
                      if sdef["mandatory_class"] == "M-ALL"}
    m_all_ams_excluded = M_ALL_SECTIONS & AMS_EXCLUDED
    m_all_required = M_ALL_SECTIONS - (m_all_ams_excluded if is_ams else set())
    missing_mandatory = m_all_required - mandatory_included
    if missing_mandatory:
        errors.append(f"VAL-001 FAIL: M-ALL sections not MANDATORY: {sorted(missing_mandatory)}")

    # No duplicate sections in sequence
    if len(sequence) != len(set(sequence)):
        errors.append("VAL-002 FAIL: Duplicate sections in assembly sequence")

    # SI-006
    if si6_violation:
        errors.append("VAL-003 FAIL SI-006: S-49 Key Assumptions must appear before S-52 Pricing")

    # SI-007: S-71 and S-72 both present for AMS
    if is_ams:
        s71 = decisions.get("S-71")
        s72 = decisions.get("S-72")
        if s71 and s71.include_status != "MANDATORY":
            warnings.append("VAL-004 WARN SI-007: S-71 SLA Framework expected MANDATORY for AMS")
        if s72 and s72.include_status != "MANDATORY":
            warnings.append("VAL-005 WARN SI-007: S-72 Incident Management expected MANDATORY for AMS")

    # B-BBEE flag
    gov_flags.append("GOV-BBEE-001: B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); verify renewal before submission after that date")

    # ADR-001 flag
    gov_flags.append("GOV-ADR-001: CVs (S-47, S-48, A-02) from APPTime only — never from KB records")

    # S-18 vintage warning for EBS
    if platform == "Oracle EBS":
        warnings.append("GOV-EBS-001: S-18 Oracle EBS content is vintage 2012–2014; review and modernise before submission")

    manifest = SectionManifest(
        manifest_id=f"{tid}-PSM-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}",
        tender_id=tid,
        tender_pattern=pattern,
        platform=platform,
        engagement_type=eng_type,
        industry=industry,
        generated_at=datetime.now(timezone.utc).isoformat(),
        engine_version=ENGINE_VERSION,
        sections=decisions,
        assembly_sequence=sequence,
        mandatory_count=sum(1 for d in decisions.values() if d.include_status == "MANDATORY"),
        optional_count=sum(1 for d in decisions.values() if d.include_status == "OPTIONAL_SELECTED"),
        excluded_count=sum(1 for d in decisions.values() if d.include_status == "EXCLUDED"),
        default_excluded_count=sum(1 for d in decisions.values() if d.include_status == "DEFAULT_EXCLUDED"),
        validation_errors=errors,
        validation_warnings=warnings,
        governance_flags=gov_flags,
    )
    return manifest


# ── Output generators ────────────────────────────────────────────────────────

def manifest_to_dict(m: SectionManifest) -> Dict:
    sections_out = {}
    for sid, d in m.sections.items():
        sections_out[sid] = {
            "section_id":          sid,
            "section_name":        d.section_name,
            "include_status":      d.include_status,
            "rationale":           d.rationale,
            "assembly_order":      d.assembly_order,
            "assembly_method":     d.assembly_method,
            "merge_strategy":      d.merge_strategy,
            "source_assets":       d.source_assets,
            "placeholders":        d.placeholders,
            "human_input_required": d.human_input_required,
            "human_input_notes":   d.human_input_notes,
            "renderer_metadata":   d.renderer_metadata,
            "governance_constraints": d.governance_constraints,
            "si_rules_applied":    d.si_rules_applied,
        }
    return {
        "manifest_id":       m.manifest_id,
        "tender_id":         m.tender_id,
        "tender_pattern":    m.tender_pattern,
        "platform":          m.platform,
        "engagement_type":   m.engagement_type,
        "industry":          m.industry,
        "generated_at":      m.generated_at,
        "engine_version":    m.engine_version,
        "summary": {
            "mandatory_sections":        m.mandatory_count,
            "optional_sections":         m.optional_count,
            "excluded_sections":         m.excluded_count,
            "default_excluded_sections": m.default_excluded_count,
            "total_sections":            len(m.sections),
            "assembly_sequence_length":  len(m.assembly_sequence),
            "validation_status":         "PASS" if not m.validation_errors else "FAIL",
        },
        "assembly_sequence":    m.assembly_sequence,
        "validation_errors":    m.validation_errors,
        "validation_warnings":  m.validation_warnings,
        "governance_flags":     m.governance_flags,
        "sections":             sections_out,
    }


def write_manifest_yaml(m: SectionManifest, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        yaml.dump(manifest_to_dict(m), fh, default_flow_style=False,
                  allow_unicode=True, sort_keys=False, width=120)
    print(f"  → Manifest written: {output_path}")


def generate_assembly_report(manifests: List[SectionManifest]) -> str:
    lines = [
        "# Proposal Section Assembly Report — PF2-003",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Engine:** PSAE v{ENGINE_VERSION}  ",
        f"**Scenarios:** {len(manifests)}  ",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Tender | Pattern | Platform | Eng Type | Mandatory | Optional | Excluded | Seq | Errors | Warnings |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for m in manifests:
        val = "PASS" if not m.validation_errors else f"FAIL({len(m.validation_errors)})"
        lines.append(
            f"| {m.tender_id} | P{m.tender_pattern} | {m.platform} | {m.engagement_type} "
            f"| {m.mandatory_count} | {m.optional_count} | {m.excluded_count} "
            f"| {len(m.assembly_sequence)} | {val} | {len(m.validation_warnings)} |"
        )
    lines += ["", "---", ""]

    for m in manifests:
        lines += [
            f"## {m.tender_id}",
            "",
            f"**Platform:** {m.platform}  **Pattern:** P{m.tender_pattern}  "
            f"**Engagement:** {m.engagement_type}  **Industry:** {m.industry or 'N/A'}",
            "",
            "### Included Sections (assembly order)",
            "",
            "| Order | Section | Status | Method | Assets | Human |",
            "|---|---|---|---|---|---|",
        ]
        for sid in m.assembly_sequence:
            d = m.sections[sid]
            assets_str = ", ".join(d.source_assets[:3]) + ("…" if len(d.source_assets) > 3 else "")
            lines.append(
                f"| {d.assembly_order} | {sid} {d.section_name} | {d.include_status} "
                f"| {d.assembly_method} | {assets_str or '—'} | {'Yes' if d.human_input_required else 'No'} |"
            )
        if m.validation_errors:
            lines += ["", "### Validation Errors", ""]
            for e in m.validation_errors:
                lines.append(f"- **{e}**")
        if m.validation_warnings:
            lines += ["", "### Warnings", ""]
            for w in m.validation_warnings:
                lines.append(f"- {w}")
        if m.governance_flags:
            lines += ["", "### Governance Flags", ""]
            for f_ in m.governance_flags:
                lines.append(f"- {f_}")
        lines += ["", "---", ""]

    return "\n".join(lines)


def generate_traceability_report(manifests: List[SectionManifest]) -> str:
    lines = [
        "# Section Traceability Report — PF2-003",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Engine:** PSAE v{ENGINE_VERSION}  ",
        "",
        "---",
        "",
        "## Purpose",
        "",
        "For every proposal section, this report answers:",
        "- **Why it exists** — which rule selected it and what assets contributed",
        "- **Why it does not exist** — which exclusion rule removed it",
        "- **Which assets contributed** — CAP/ASP traceability back to registry",
        "- **Which SI rules applied** — section integrity constraints",
        "",
        "---",
    ]
    for m in manifests:
        lines += [
            f"## {m.tender_id} — {m.platform} {m.engagement_type}",
            "",
            "### Full Section Traceability",
            "",
            "| Section | Status | Rationale | Source Assets | SI Rules |",
            "|---|---|---|---|---|",
        ]
        for sid in STANDARD_ORDER:
            d = m.sections.get(sid)
            if not d:
                continue
            assets_str = ", ".join(d.source_assets) or "—"
            si_str     = ", ".join(d.si_rules_applied) or "—"
            lines.append(
                f"| {sid} {d.section_name} | {d.include_status} | {d.rationale} "
                f"| {assets_str} | {si_str} |"
            )
        lines += ["", "---", ""]
    return "\n".join(lines)


# ── Regression scenarios ─────────────────────────────────────────────────────

REGRESSION_CONTEXTS: Dict[str, Dict[str, Any]] = {
    "ARM-IT045": {
        "tender_id":       "ARM-IT045",
        "tender_pattern":  "13",
        "platform":        "Oracle EBS",
        "engagement_type": "AMS",
        "industry":        "Mining",
        "integration_scope": True,
        "modules": ["Oracle EBS Financials","Oracle EBS HRMS"],
        "security_in_scope": False,
        "oci_in_scope": False,
        "payroll_integration": False,
    },
    "REG-HCM-P3-MINING": {
        "tender_id":       "REG-HCM-P3-MINING",
        "tender_pattern":  "3",
        "platform":        "Oracle HCM Cloud",
        "engagement_type": "Implementation",
        "industry":        "Mining",
        "integration_scope": True,
        "payroll_integration": True,
        "oci_in_scope": False,
        "security_in_scope": False,
        "modules": ["Oracle HCM Core","Oracle Payroll Interface",
                    "Oracle Workforce Compensation","Oracle Time and Labor"],
    },
    "REG-OIC-P7": {
        "tender_id":       "REG-OIC-P7",
        "tender_pattern":  "7",
        "platform":        "Oracle Integration Cloud",
        "engagement_type": "Implementation",
        "industry":        "Financial-Services",
        "integration_scope": True,
        "oci_in_scope": False,
        "payroll_integration": False,
        "security_in_scope": False,
        "modules": ["Oracle Integration Cloud"],
    },
    "REG-ERP-P7-FULLSUITE": {
        "tender_id":       "REG-ERP-P7-FULLSUITE",
        "tender_pattern":  "7",
        "platform":        "Oracle ERP Cloud",
        "engagement_type": "Implementation",
        "industry":        "Manufacturing",
        "oci_in_scope": True,
        "integration_scope": True,
        "payroll_integration": False,
        "security_in_scope": False,
        "modules": ["Oracle Fusion Financials","Oracle Fusion Procurement","Oracle PPM"],
    },
    "REG-ACU-P11": {
        "tender_id":       "REG-ACU-P11",
        "tender_pattern":  "11",
        "platform":        "Acumatica",
        "engagement_type": "Implementation",
        "industry":        "Distribution",
        "integration_scope": False,
        "oci_in_scope": False,
        "payroll_integration": False,
        "security_in_scope": False,
        "modules": ["Acumatica Financials","Acumatica Project Accounting"],
    },
    "REG-BEB-P12": {
        "tender_id":       "REG-BEB-P12",
        "tender_pattern":  "12",
        "platform":        "BeBanking",
        "engagement_type": "Implementation",
        "industry":        "Banking",
        "integration_scope": True,
        "security_in_scope": True,
        "oci_in_scope": False,
        "payroll_integration": False,
        "modules": ["BeBanking Supplier Payments","BeBanking Payroll Payments"],
    },
}

# Expected minimums per regression scenario for key checks
REGRESSION_EXPECTATIONS: Dict[str, Dict[str, Any]] = {
    "ARM-IT045": {
        "engagement_type": "AMS",
        "ams_sections_present": True,
        "s38_excluded": True,
        "s73_mandatory": True,
        "s34_excluded": True,
        "s49_before_s52": True,
        "min_mandatory": 20,
    },
    "REG-HCM-P3-MINING": {
        "engagement_type": "Implementation",
        "s16_mandatory": True,
        "s38_mandatory": True,
        "ams_sections_absent": True,
        "min_mandatory": 30,
    },
    "REG-OIC-P7": {
        "engagement_type": "Implementation",
        "s19_mandatory": True,
        "s16_excluded_or_default": True,
        "ams_sections_absent": True,
        "min_mandatory": 25,
    },
    "REG-ERP-P7-FULLSUITE": {
        "engagement_type": "Implementation",
        "s17_mandatory": True,
        "s22_triggered": True,
        "ams_sections_absent": True,
        "min_mandatory": 30,
    },
    "REG-ACU-P11": {
        "engagement_type": "Implementation",
        "s10_mandatory": True,
        "s23_or_s24_mandatory": True,
        "s09_excluded": True,
        "ams_sections_absent": True,
        "min_mandatory": 25,
    },
    "REG-BEB-P12": {
        "engagement_type": "Implementation",
        "s11_mandatory": True,
        "s29_mandatory": True,
        "s09_excluded": True,
        "ams_sections_absent": True,
        "min_mandatory": 25,
    },
}


def run_regression() -> List[Tuple[str, bool, List[str]]]:
    results = []
    for scenario_id, ctx in REGRESSION_CONTEXTS.items():
        m      = build_section_manifest(ctx)
        exp    = REGRESSION_EXPECTATIONS[scenario_id]
        issues: List[str] = []

        if m.validation_errors:
            issues += m.validation_errors

        is_ams = (ctx["engagement_type"] == "AMS")

        def st(sid: str) -> str:
            d = m.sections.get(sid)
            return d.include_status if d else "DEFAULT_EXCLUDED"

        # AMS structural checks
        if exp.get("s38_excluded") and st("S-38") not in ("EXCLUDED","DEFAULT_EXCLUDED"):
            issues.append(f"FAIL: S-38 must be EXCLUDED for AMS; got {st('S-38')}")
        if exp.get("s73_mandatory") and st("S-73") != "MANDATORY":
            issues.append(f"FAIL: S-73 must be MANDATORY for AMS; got {st('S-73')}")
        if exp.get("s34_excluded") and st("S-34") not in ("EXCLUDED","DEFAULT_EXCLUDED"):
            issues.append(f"FAIL: S-34 must be EXCLUDED for AMS; got {st('S-34')}")
        if exp.get("ams_sections_present"):
            for ams_sid in ["S-70","S-71","S-72","S-73","S-74"]:
                if st(ams_sid) != "MANDATORY":
                    issues.append(f"FAIL: {ams_sid} must be MANDATORY for AMS; got {st(ams_sid)}")
        if exp.get("ams_sections_absent"):
            for ams_sid in ["S-70","S-71","S-72","S-73","S-74","S-75","S-76"]:
                if st(ams_sid) not in ("EXCLUDED","DEFAULT_EXCLUDED"):
                    issues.append(f"FAIL: {ams_sid} must be excluded for non-AMS; got {st(ams_sid)}")

        # SI-006
        if exp.get("s49_before_s52"):
            seq = m.assembly_sequence
            if "S-49" in seq and "S-52" in seq:
                if seq.index("S-49") > seq.index("S-52"):
                    issues.append("FAIL SI-006: S-49 not before S-52")

        # Capability sections
        if exp.get("s16_mandatory") and st("S-16") != "MANDATORY":
            issues.append(f"FAIL: S-16 expected MANDATORY; got {st('S-16')}")
        if exp.get("s17_mandatory") and st("S-17") != "MANDATORY":
            issues.append(f"FAIL: S-17 expected MANDATORY; got {st('S-17')}")
        if exp.get("s19_mandatory") and st("S-19") != "MANDATORY":
            issues.append(f"FAIL: S-19 expected MANDATORY; got {st('S-19')}")
        if exp.get("s10_mandatory") and st("S-10") != "MANDATORY":
            issues.append(f"FAIL: S-10 expected MANDATORY; got {st('S-10')}")
        if exp.get("s11_mandatory") and st("S-11") != "MANDATORY":
            issues.append(f"FAIL: S-11 expected MANDATORY; got {st('S-11')}")
        if exp.get("s29_mandatory") and st("S-29") not in ("MANDATORY","OPTIONAL_SELECTED"):
            issues.append(f"FAIL: S-29 expected selected for BeBanking; got {st('S-29')}")
        if exp.get("s22_triggered") and st("S-22") not in ("MANDATORY","OPTIONAL_SELECTED"):
            issues.append(f"FAIL: S-22 expected selected for OCI in scope; got {st('S-22')}")
        if exp.get("s09_excluded") and st("S-09") not in ("EXCLUDED","DEFAULT_EXCLUDED"):
            issues.append(f"FAIL: S-09 should be excluded for non-Oracle; got {st('S-09')}")
        if exp.get("s16_excluded_or_default") and st("S-16") not in ("EXCLUDED","DEFAULT_EXCLUDED"):
            issues.append(f"FAIL: S-16 should be excluded for non-HCM; got {st('S-16')}")
        if exp.get("s38_mandatory") and st("S-38") not in ("MANDATORY","OPTIONAL_SELECTED"):
            issues.append(f"FAIL: S-38 expected present for Implementation; got {st('S-38')}")
        if exp.get("s23_or_s24_mandatory"):
            if st("S-23") not in ("MANDATORY","OPTIONAL_SELECTED") and st("S-24") not in ("MANDATORY","OPTIONAL_SELECTED"):
                issues.append(f"FAIL: S-23 or S-24 expected for Acumatica; S-23={st('S-23')} S-24={st('S-24')}")

        if exp.get("min_mandatory") and m.mandatory_count < exp["min_mandatory"]:
            issues.append(f"FAIL: mandatory_count={m.mandatory_count} < min {exp['min_mandatory']}")

        passed = len(issues) == 0
        results.append((scenario_id, passed, issues))
    return results


# ── Self-test suite ──────────────────────────────────────────────────────────

def run_self_tests() -> Tuple[int, int]:
    passed = failed = 0

    def check(desc: str, condition: bool, detail: str = "") -> None:
        nonlocal passed, failed
        if condition:
            print(f"  PASS  {desc}")
            passed += 1
        else:
            print(f"  FAIL  {desc}{(' — ' + detail) if detail else ''}")
            failed += 1

    base_oracle_impl = {
        "tender_id": "TEST", "tender_pattern": "1",
        "platform": "Oracle HCM Cloud", "engagement_type": "Implementation",
        "industry": "Mining", "integration_scope": False,
        "oci_in_scope": False, "payroll_integration": False, "security_in_scope": False,
        "modules": ["Oracle HCM Core","Oracle Payroll Interface","Oracle Workforce Compensation"],
    }
    base_ebs_ams = {
        "tender_id": "TEST-AMS", "tender_pattern": "13",
        "platform": "Oracle EBS", "engagement_type": "AMS",
        "industry": "Mining", "integration_scope": False,
        "oci_in_scope": False, "payroll_integration": False, "security_in_scope": False,
        "modules": [],
    }
    base_acu = {
        "tender_id": "TEST-ACU", "tender_pattern": "11",
        "platform": "Acumatica", "engagement_type": "Implementation",
        "industry": "Retail", "integration_scope": False,
        "oci_in_scope": False, "payroll_integration": False, "security_in_scope": False,
        "modules": ["Acumatica Financials"],
    }
    base_bb = {
        "tender_id": "TEST-BB", "tender_pattern": "12",
        "platform": "BeBanking", "engagement_type": "Implementation",
        "industry": "Banking", "integration_scope": True, "security_in_scope": True,
        "oci_in_scope": False, "payroll_integration": False,
        "modules": ["BeBanking Supplier Payments"],
    }

    # T01: M-ALL sections mandatory in HCM Implementation
    m1 = build_section_manifest(base_oracle_impl)
    check("T01 S-01 Cover Page mandatory (M-ALL)",
          m1.sections["S-01"].include_status == "MANDATORY")

    # T02: S-03 Company Overview mandatory
    check("T02 S-03 Company Overview mandatory (M-ALL)",
          m1.sections["S-03"].include_status == "MANDATORY")

    # T03: S-16 HCM Capability mandatory when HCM Core selected
    check("T03 S-16 HCM Capability mandatory for Oracle HCM Cloud",
          m1.sections["S-16"].include_status == "MANDATORY",
          m1.sections["S-16"].include_status)

    # T04: S-38 present for Implementation
    check("T04 S-38 Change Control present for Implementation",
          m1.sections["S-38"].include_status in ("MANDATORY","OPTIONAL_SELECTED"),
          m1.sections["S-38"].include_status)

    # T05: S-09 Oracle Partnership for HCM Cloud
    check("T05 S-09 Oracle Partnership for Oracle HCM Cloud",
          m1.sections["S-09"].include_status in ("MANDATORY","OPTIONAL_SELECTED"),
          m1.sections["S-09"].include_status)

    # T06: SI-006 S-49 before S-52 in standard sequence
    seq = m1.assembly_sequence
    s49_pos = seq.index("S-49") if "S-49" in seq else 999
    s52_pos = seq.index("S-52") if "S-52" in seq else 999
    check("T06 SI-006 S-49 Key Assumptions before S-52 Pricing",
          s49_pos < s52_pos, f"S-49={s49_pos} S-52={s52_pos}")

    # T07: AMS — S-38 excluded
    m_ams = build_section_manifest(base_ebs_ams)
    check("T07 SI-001 S-38 EXCLUDED for AMS",
          m_ams.sections["S-38"].include_status == "EXCLUDED",
          m_ams.sections["S-38"].include_status)

    # T08: AMS — S-73 mandatory (replaces S-38)
    check("T08 SI-001 S-73 Change Request MANDATORY for AMS",
          m_ams.sections["S-73"].include_status == "MANDATORY",
          m_ams.sections["S-73"].include_status)

    # T09: AMS — S-34 excluded
    check("T09 S-34 EXCLUDED for AMS",
          m_ams.sections["S-34"].include_status == "EXCLUDED",
          m_ams.sections["S-34"].include_status)

    # T10: AMS — S-74 before S-70 in sequence
    ams_seq = m_ams.assembly_sequence
    s74_pos = ams_seq.index("S-74") if "S-74" in ams_seq else 999
    s70_pos = ams_seq.index("S-70") if "S-70" in ams_seq else 999
    check("T10 AMS Support Model order: S-74 before S-70",
          s74_pos < s70_pos, f"S-74={s74_pos} S-70={s70_pos}")

    # T11: AMS — SI-005 References (S-67) after Commercial (S-49)
    s67_pos = ams_seq.index("S-67") if "S-67" in ams_seq else 999
    s49_ams_pos = ams_seq.index("S-49") if "S-49" in ams_seq else 999
    check("T11 SI-005 S-67 References after S-49 Assumptions in AMS",
          s67_pos > s49_ams_pos, f"S-67={s67_pos} S-49={s49_ams_pos}")

    # T12: Acumatica — S-09 Oracle Partnership excluded
    m_acu = build_section_manifest(base_acu)
    check("T12 S-09 Oracle Partnership EXCLUDED for Acumatica",
          m_acu.sections["S-09"].include_status in ("EXCLUDED","DEFAULT_EXCLUDED"),
          m_acu.sections["S-09"].include_status)

    # T13: Acumatica — S-10 Acumatica Partnership present
    check("T13 S-10 Acumatica Partnership present for Acumatica",
          m_acu.sections["S-10"].include_status in ("MANDATORY","OPTIONAL_SELECTED"),
          m_acu.sections["S-10"].include_status)

    # T14: Acumatica — S-23 Acumatica Financials driven by module
    check("T14 S-23 Acumatica Financials present when module in scope",
          m_acu.sections["S-23"].include_status in ("MANDATORY","OPTIONAL_SELECTED"),
          m_acu.sections["S-23"].include_status)

    # T15: BeBanking — S-29 H2H Banking present
    m_bb = build_section_manifest(base_bb)
    check("T15 S-29 BeBanking H2H Banking present for BeBanking",
          m_bb.sections["S-29"].include_status in ("MANDATORY","OPTIONAL_SELECTED"),
          m_bb.sections["S-29"].include_status)

    # T16: BeBanking — S-09 Oracle Partnership excluded
    check("T16 S-09 Oracle Partnership EXCLUDED for BeBanking",
          m_bb.sections["S-09"].include_status in ("EXCLUDED","DEFAULT_EXCLUDED"),
          m_bb.sections["S-09"].include_status)

    # T17: S-59 B-BBEE mandatory (M-SA)
    check("T17 S-59 B-BBEE Certificate MANDATORY (M-SA)",
          m1.sections["S-59"].include_status == "MANDATORY",
          m1.sections["S-59"].include_status)

    # T18: AMS — S-70 to S-76 all mandatory
    ams_support = ["S-70","S-71","S-72","S-73","S-74","S-75","S-76"]
    all_mandatory = all(m_ams.sections[s].include_status == "MANDATORY" for s in ams_support)
    check("T18 AMS Support S-70–S-76 all MANDATORY",
          all_mandatory,
          str({s: m_ams.sections[s].include_status for s in ams_support if m_ams.sections[s].include_status != "MANDATORY"}))

    # T19: AMS non-support sections S-70–S-76 excluded for Implementation
    impl_ams_absent = all(m1.sections[s].include_status in ("EXCLUDED","DEFAULT_EXCLUDED") for s in ams_support)
    check("T19 AMS S-70–S-76 EXCLUDED for Implementation",
          impl_ams_absent)

    # T20: No duplicate sections in assembly sequence (deterministic)
    m2 = build_section_manifest(base_oracle_impl)
    check("T20 Assembly sequence deterministic (no duplicates)",
          len(m2.assembly_sequence) == len(set(m2.assembly_sequence)))

    # T21: OCI sections triggered when oci_in_scope=True
    oci_ctx = dict(base_oracle_impl)
    oci_ctx["oci_in_scope"] = True
    oci_ctx["platform"] = "Oracle ERP Cloud"
    m_oci = build_section_manifest(oci_ctx)
    check("T21 S-22 OCI triggered when oci_in_scope=True",
          m_oci.sections["S-22"].include_status in ("MANDATORY","OPTIONAL_SELECTED"),
          m_oci.sections["S-22"].include_status)

    # T22: S-47/S-48 ADR-001 placeholders noted
    check("T22 S-47 CV placeholder flagged with ADR-001",
          "ADR-001" in m1.sections["S-47"].si_rules_applied)

    return passed, failed


# ── CLI entry point ──────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=f"PSAE v{ENGINE_VERSION}")
    parser.add_argument("--regression",  action="store_true", help="Run 6 regression scenarios")
    parser.add_argument("--run-tests",   action="store_true", help="Run self-test suite")
    parser.add_argument("--manifest",    metavar="TENDER_ID",  help="Generate manifest for named scenario")
    parser.add_argument("--context",     metavar="YAML_FILE",  help="Generate manifest from a tender context YAML file")
    args = parser.parse_args()

    if args.context:
        with open(args.context, "r", encoding="utf-8") as fh:
            raw = yaml.safe_load(fh)
        ctx = raw.get("tender_context", raw)
        # Normalise pattern field: "P1" or 1 → tender_pattern: "1"
        if "pattern" in ctx and "tender_pattern" not in ctx:
            ctx["tender_pattern"] = str(ctx["pattern"]).lstrip("P")
        m   = build_section_manifest(ctx)
        tid = ctx.get("tender_id", "UNKNOWN")
        out_dir  = os.path.join(MANIFESTS_DIR, tid)
        out_path = os.path.join(out_dir, f"PROPOSAL_SECTION_MANIFEST_{tid}.yaml")
        os.makedirs(out_dir, exist_ok=True)
        write_manifest_yaml(m, out_path)
        print(f"[PSAE] Tender: {tid}")
        print(f"[PSAE] Context: {args.context}")
        print(f"[PSAE] Manifest: {out_path}")
        print(f"[PSAE] Sections: M={m.mandatory_count} O={m.optional_count} E={m.excluded_count}")
        if m.validation_errors:
            for err in m.validation_errors:
                print(f"[PSAE] ERROR: {err}")
        if m.validation_warnings:
            for w in m.validation_warnings:
                print(f"[PSAE] WARN: {w}")
        sys.exit(0)

    if args.run_tests:
        print(f"\nPSAE v{ENGINE_VERSION} — Self-Test Suite")
        print("=" * 55)
        p, f = run_self_tests()
        print(f"\n{'='*55}")
        print(f"Result: {p}/{p+f} PASS  ({f} FAIL)")
        sys.exit(0 if f == 0 else 1)

    if args.regression:
        print(f"\nPSAE v{ENGINE_VERSION} — Regression Suite")
        print("=" * 55)
        results = run_regression()
        manifests = []
        for scenario_id, ok, issues in results:
            ctx = REGRESSION_CONTEXTS[scenario_id]
            m   = build_section_manifest(ctx)
            manifests.append(m)
            status = "PASS" if ok else f"FAIL ({len(issues)} issues)"
            print(f"  {status:30s}  {scenario_id}  M={m.mandatory_count} O={m.optional_count} E={m.excluded_count}")
            for iss in issues:
                print(f"             {iss}")
        all_pass = all(ok for _, ok, _ in results)
        print(f"\nResult: {sum(ok for _,ok,_ in results)}/{len(results)} PASS")

        # Write reports
        rpt_path = os.path.join(REPORTS_DIR, "PROPOSAL_SECTION_ASSEMBLY_REPORT.md")
        trc_path = os.path.join(REPORTS_DIR, "SECTION_TRACEABILITY_REPORT.md")
        os.makedirs(REPORTS_DIR, exist_ok=True)
        with open(rpt_path, "w", encoding="utf-8") as fh:
            fh.write(generate_assembly_report(manifests))
        print(f"  → Assembly report: {rpt_path}")
        with open(trc_path, "w", encoding="utf-8") as fh:
            fh.write(generate_traceability_report(manifests))
        print(f"  → Traceability report: {trc_path}")
        sys.exit(0 if all_pass else 1)

    if args.manifest:
        ctx = REGRESSION_CONTEXTS.get(args.manifest)
        if not ctx:
            print(f"ERROR: Unknown tender ID '{args.manifest}'. Known: {list(REGRESSION_CONTEXTS)}")
            sys.exit(1)
        m = build_section_manifest(ctx)
        tid = ctx["tender_id"]
        out_dir  = os.path.join(MANIFESTS_DIR, tid)
        out_path = os.path.join(out_dir, f"PROPOSAL_SECTION_MANIFEST_{tid}.yaml")
        write_manifest_yaml(m, out_path)
        sys.exit(0)

    # Default: full run
    print(f"\nPSAE v{ENGINE_VERSION} — Full Run")
    print("=" * 55)

    print("\n[1/3] Self-tests …")
    p, f = run_self_tests()
    print(f"      {p}/{p+f} PASS")

    print("\n[2/3] Regression …")
    results  = run_regression()
    manifests = []
    for scenario_id, ok, issues in results:
        ctx = REGRESSION_CONTEXTS[scenario_id]
        m   = build_section_manifest(ctx)
        manifests.append(m)
        # Write per-tender manifest
        out_dir  = os.path.join(MANIFESTS_DIR, ctx["tender_id"])
        out_path = os.path.join(out_dir, f"PROPOSAL_SECTION_MANIFEST_{ctx['tender_id']}.yaml")
        write_manifest_yaml(m, out_path)
        status = "PASS" if ok else f"FAIL"
        print(f"      {status}  {scenario_id}  M={m.mandatory_count} O={m.optional_count} E={m.excluded_count}")
    reg_pass = sum(ok for _,ok,_ in results)
    print(f"      {reg_pass}/{len(results)} scenarios PASS")

    print("\n[3/3] Reports …")
    os.makedirs(REPORTS_DIR, exist_ok=True)
    rpt_path = os.path.join(REPORTS_DIR, "PROPOSAL_SECTION_ASSEMBLY_REPORT.md")
    trc_path = os.path.join(REPORTS_DIR, "SECTION_TRACEABILITY_REPORT.md")
    with open(rpt_path, "w", encoding="utf-8") as fh:
        fh.write(generate_assembly_report(manifests))
    print(f"      Assembly report → {rpt_path}")
    with open(trc_path, "w", encoding="utf-8") as fh:
        fh.write(generate_traceability_report(manifests))
    print(f"      Traceability report → {trc_path}")

    all_pass = f == 0 and reg_pass == len(results)
    print(f"\n{'='*55}")
    print(f"PSAE v{ENGINE_VERSION} — {'ALL PASS' if all_pass else 'ISSUES FOUND'}")
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
