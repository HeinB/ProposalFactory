---
document_id: PROPOSAL-SECTION-ENGINE-V1
title: "Proposal Section Assembly Engine — Architecture"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-003 — Proposal Section Assembly Engine"
approved_by: "PF2-003"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Architecture / Engine Specification"
scope: "Defines the architecture, design decisions, input/output contracts, section inclusion rules, and governance enforcement for the Proposal Section Assembly Engine (PSAE) v1.0."
---

# Proposal Section Assembly Engine (PSAE) — Architecture

**Work Package:** PF2-003  
**Date:** 2026-06-29  
**Version:** 1.0  
**Status:** APPROVED  
**Platform Maturity:** L5.3 → **L5.4**

---

## 1. Purpose

The PSAE is the orchestration layer between the Knowledge Platform and the Proposal Renderer. It consumes a certified tender context and the enriched Knowledge Asset Registry, then deterministically produces a **Proposal Section Manifest** — a complete, ordered, traceable record of every section that will appear in the proposal.

The PSAE answers, for every proposal section:
- **Include or Exclude?** — deterministic; no human judgement required
- **Why?** — which rule or asset triggered the decision
- **Source assets** — which CAP/ASP registry assets contribute to this section
- **Assembly method** — how the section is assembled (DIRECT / EXTRACT / MERGE / TEMPLATE / AI-GENERATE / PLACEHOLDER)
- **Human input required?** — what a human must provide or review
- **Renderer metadata** — downstream rendering instructions

The PSAE generates **no proposal text**. It is a pure orchestration engine.

---

## 2. Position in the Proposal Factory

```
Tender Profile (TIL)
       ↓
Knowledge Asset Registry (enriched — BUILD-20260629-ARE-001)
       ↓
ARE Engine (are.py) — AREL asset selection
       ↓
RSE Engine (rse.py) — Risk selection
       ↓
PSAE (proposal_section_engine.py)  ←── THIS ENGINE
       ↓
Proposal Section Manifest (YAML)
       ↓
Proposal Renderer (next stage)
```

The PSAE runs after ARE and RSE have produced their selections. It combines:
1. ARE capability/ASP asset selections → drives section capability content
2. Risk selections → informs S-37 RAID and S-50 Risk Register
3. Tender context (platform, engagement type, industry, modules) → governs all pattern-based rules

---

## 3. Inputs

| Input | Source | Notes |
|---|---|---|
| Tender context (dict or YAML) | TIL output | platform, engagement_type, industry, modules, flags |
| AREL asset selections | are.py `select_assets()` | All 62 CAP+ASP rules evaluated against context |
| 82 section definitions | SECTION_DEFS (engine) | Name, mandatory class, assembly method, metadata |
| Asset-to-section mapping | ASSET_TO_SECTIONS (engine) | Which assets contribute to which sections |
| Section driver definitions | SECTION_ASSET_DRIVERS (engine) | Which assets trigger section inclusion |

---

## 4. Output

### 4.1 Proposal Section Manifest YAML

Written to `08_Commercial/Proposals/[TENDER_ID]/PROPOSAL_SECTION_MANIFEST_[TENDER_ID].yaml`

Per-section fields:

| Field | Type | Description |
|---|---|---|
| `section_id` | str | Section identifier (e.g., S-16) |
| `section_name` | str | Human-readable section name |
| `include_status` | enum | MANDATORY / OPTIONAL_SELECTED / EXCLUDED / DEFAULT_EXCLUDED |
| `rationale` | str | Explanation of the inclusion decision |
| `assembly_order` | int | Position in the assembly sequence |
| `assembly_method` | enum | DIRECT / EXTRACT / MERGE / TEMPLATE / AI-GENERATE / PLACEHOLDER |
| `merge_strategy` | str | Merge instructions when method=MERGE |
| `source_assets` | list[str] | CAP/ASP asset IDs that contribute to this section |
| `placeholders` | list[str] | Named placeholders requiring human input |
| `human_input_required` | bool | Whether human review/input is required |
| `human_input_notes` | str | Specific human input instructions |
| `renderer_metadata` | dict | Downstream renderer instructions |
| `governance_constraints` | list[str] | Active governance rules and restrictions |
| `si_rules_applied` | list[str] | Section Integrity rules applied (SI-001 to SI-007) |

---

## 5. Section Inclusion Logic

### 5.1 Evaluation Cascade

Each section is evaluated in strict priority order:

1. **AMS Exclusion (SI-001):** If `engagement_type == "AMS"` and section is in `AMS_EXCLUDED` → EXCLUDED
2. **AMS-Only Exclusion:** If section is AMS-only (S-70–S-76) and engagement is not AMS → EXCLUDED
3. **Always Mandatory:** If section is in `ALWAYS_MANDATORY` → MANDATORY
4. **Platform-Conditional:** COND-ORA / COND-ACU / COND-BB / COND-AMS / COND-HCM etc. → driven by asset selection
5. **Asset-Driven:** OPTIONAL / conditional sections → driven by driver asset selections
6. **Default:** DEFAULT_EXCLUDED

### 5.2 AMS Pattern 13 Exclusions (SI-001)

The following sections are excluded for all AMS proposals:

| Section | Name | Reason |
|---|---|---|
| S-34 | Implementation Methodology | Replaced by AMS Support block |
| S-35 | Project Plan / Timeline | No project delivery in AMS |
| S-38 | Change Control Framework | Replaced by S-73 (SI-001) |
| S-39 | Testing Strategy | No UAT/CRP in ongoing AMS |
| S-40 | Data Migration | No migration in AMS |
| S-41 | Training Plan | No training delivery in AMS |
| S-42 | Cutover / Go-Live Plan | No go-live in AMS |
| S-43 | Hypercare / Transition | No transition in AMS |
| S-46 | Team Structure | No project team assignment in AMS |
| S-47 | Named Consultant CVs | No project team in AMS |
| S-48 | Consultant Profiles | No project team in AMS |

### 5.3 AMS Support Block (S-70–S-76)

Active only when `engagement_type == "AMS"`. Assembly order within the AMS block:

```
S-74 (Resource Model) → S-70 (Support Model) → S-71 (SLA Framework) →
S-72 (Incident Management) → S-73 (Change Request) → S-75 (Release Mgmt) → S-76 (Monitoring)
```

**SI-007 Content Boundaries:**
- S-71: SLA tier table ONLY (P1–P4 response times, service hours, response ≠ resolution disclaimer)
- S-72: Incident classification process ONLY; references S-71 for SLA values; no tier table duplication

---

## 6. Assembly Sequence Design

### 6.1 Standard Sequence (Implementation)

```
Cover/TOC → Corporate → Understanding → Solution → Scope/Delivery → People →
Commercial (S-49 → S-52, SI-006) → Compliance → References → Appendices
```

### 6.2 AMS Sequence (Pattern 13)

```
Cover/TOC → Corporate → Understanding → Solution → Scope (reduced) → Governance →
AMS Support (S-74→S-70→S-71→S-72→S-73→S-75→S-76) →
Commercial (S-49→S-50→S-51→S-52, SI-006) → Compliance → References (SI-005) → Appendices
```

**SI-005:** References (S-67–S-69) assembled AFTER Commercial/Compliance in all AMS proposals.
**SI-006:** S-49 Key Assumptions assembled BEFORE S-52 Pricing in all proposals.

---

## 7. Governance Enforcement

| Constraint | Sections | Enforcement |
|---|---|---|
| ADR-001: No CV from KB records | S-47, S-48, A-02 | Forced PLACEHOLDER; governance_constraints populated |
| G-001 (GOV-010): Mining sector only | S-16 (W3S1-005) | ARE AREL `excluded_if: not industry == "Mining"` |
| B-BBEE expiry 2026-07-31 | S-59, S-12, A-05 | governance_flag in manifest |
| No Oracle Gold Partner | S-09, S-62 | human_input_notes warn |
| SI-001: S-38 AMS exclusion | S-38 | AMS_EXCLUDED enforced |
| SI-006: Assumptions before pricing | S-49, S-52 | Assembly order enforced; VAL-003 validates |
| SI-007: SLA/Incident boundaries | S-71, S-72 | Documented in governance_constraints |
| AM-W4E3-001: KPMG unnamed | S-17, S-67 | governance_notes warn; human_input_notes warn |
| DFA/CCBA/SAA prohibition | S-67, S-68 | governance_notes warn |
| Redpath Mining: Rule 21.5 | S-67 | governance_notes warn |

---

## 8. Validation

The PSAE runs four validation checks against every generated manifest:

| Check | Code | Condition | Outcome |
|---|---|---|---|
| M-ALL sections present | VAL-001 | All M-ALL sections MANDATORY (excluding AMS exclusions for AMS proposals) | FAIL if any missing |
| No duplicate sections | VAL-002 | Assembly sequence has no duplicates | FAIL if duplicates |
| SI-006 ordering | VAL-003 | S-49 appears before S-52 in assembly sequence | FAIL if violated |
| SI-007 AMS sections | VAL-004/005 | S-71 and S-72 both MANDATORY for AMS | WARN if missing |

---

## 9. Engine Architecture

```
proposal_section_engine.py
├── SECTION_DEFS          — 82 section definitions (metadata)
├── ASSET_TO_SECTIONS     — asset_id → [section_id, ...] contribution map
├── SECTION_ASSET_DRIVERS — section_id → [asset_id, ...] driver map
├── ALWAYS_MANDATORY      — set of unconditionally mandatory sections
├── AMS_EXCLUDED          — set of sections excluded for AMS
├── AMS_ONLY              — set of sections included for AMS only
├── STANDARD_ORDER        — 82-section standard assembly sequence
├── AMS_ORDER             — AMS-specific assembly sequence
├── build_section_manifest(context) → SectionManifest
├── manifest_to_dict(manifest) → dict
├── write_manifest_yaml(manifest, path)
├── generate_assembly_report(manifests) → str (Markdown)
├── generate_traceability_report(manifests) → str (Markdown)
├── REGRESSION_CONTEXTS   — 6 canonical regression contexts
├── run_regression() → [(scenario_id, passed, issues), ...]
└── run_self_tests() → (passed, failed)
```

**Import dependency:** `are.py` — imports `ARELEvaluator`, `ASSEMBLY_RULES`, `ASP_RULES`, `ALL_RULES`, `select_assets`. Both files must reside in the same directory.

---

## 10. Known Gaps

| Item | Description | Priority |
|---|---|---|
| S-50 Risk Register | RSE risk selections not yet fed into section manifest | High |
| Assumption pack sub-section extraction | S-30/S-31/S-33 extract from ASP by section tag; tagging standard defined but not automated | Medium |
| S-22 OCI standalone narrative | No standalone OCI capability asset; uses assumption pack as proxy | High |
| S-44 Disaster Recovery | Methodology folder empty; 0% automation | Medium |
| S-65/S-66 POPIA/PAIA | OAR-E01/E02 not resolved | Medium |

---

*PROPOSAL_SECTION_ENGINE.md v1.0 | PF2-003 — Proposal Section Assembly Engine | 2026-06-29*
