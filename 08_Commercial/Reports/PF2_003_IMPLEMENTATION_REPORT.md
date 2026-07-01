---
document_id: PF2-003-IMPLEMENTATION-REPORT-V1
title: "PF2-003 — Proposal Section Assembly Engine — Implementation Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-29"
created_by: "PF2-003 — Proposal Section Assembly Engine"
approved_by: "PF2-003"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Work Package Report"
scope: "Documents the design, implementation, and verification of the Proposal Section Assembly Engine (PSAE) — the orchestration layer between the Knowledge Platform and the Proposal Renderer."
---

# PF2-003 — Proposal Section Assembly Engine — Implementation Report

**Work Package:** PF2-003  
**Date:** 2026-06-29  
**Status:** COMPLETE  
**Platform Maturity:** L5.3 → **L5.4**

---

## 1. Objective

Build the Proposal Section Assembly Engine — the orchestration layer that consumes the enriched Knowledge Asset Registry and a certified tender context, then deterministically assembles a complete, ordered, traceable Proposal Section Manifest for every tender.

**Success criteria:**
- Every proposal section assembled deterministically from canonical rules
- Every section explains: why it exists; why it does not exist; which assets contributed; which rules selected it
- 22 self-tests, 0 failures
- 6 regression scenarios, 0 validation violations
- SI-001, SI-005, SI-006, SI-007 ordering rules verified
- GOV-010, ADR-001, B-BBEE constraints encoded
- The Proposal Factory becomes section-driven rather than capability-driven

---

## 2. Pre-Conditions Confirmed at PF2-003 Start

| Pre-condition | Status |
|---|---|
| Platform Maturity | L5.3 |
| Knowledge Platform v1.0 | COMPLETE — WP19D |
| Registry V1.0 CERTIFIED | BUILD-20260628-150801; enriched BUILD-20260629-ARE-001 |
| ARE operational | are.py v1.0; 20/20 tests; 6 regression 0 violations |
| RSE operational | rse.py v1.0; 17/17 tests; 5 regression 0 violations |
| AREL V1.0 FROZEN | WP19B; 20 context variables; 30 ARVAL rules |
| 82 sections defined | PROPOSAL_SECTION_LIBRARY.md v1.2 |
| Assembly sequence defined | PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 |
| Content source matrix defined | CONTENT_SOURCE_MATRIX.md v1.2 |
| SI-001/005/006/007 defined | WP18C.2 |

---

## 3. Architecture Decision

**Why PSAE as a separate engine from ARE?**

ARE governs which assets are included. PSAE governs which proposal sections those assets feed into and in what order. These are distinct responsibilities:

- ARE: `tender_context → asset_id → {mandatory_if, optional_if, excluded_if} → selection_status`
- PSAE: `selection_status + section_rules → section_id → include_status + assembly_order + source_assets`

The PSAE imports and calls `select_assets()` from ARE, consuming its output. It adds the section-mapping layer that transforms the flat asset list into a structured, ordered, traceable proposal skeleton.

This separation preserves: ARE as the single source of AREL asset truth; PSAE as the single source of section orchestration truth; no logic duplication between the two.

---

## 4. Implementation

### 4.1 proposal_section_engine.py

**Location:** `08_Commercial/Assembly_Engine/proposal_section_engine.py`  
**Version:** v1.0  
**Dependencies:** are.py (same directory); PyYAML  
**CLI:** `--regression`, `--run-tests`, `--manifest TENDER_ID`

**Key components:**

| Component | Description |
|---|---|
| `SECTION_DEFS` | 82 section definitions: name, mandatory_class, assembly_method, source, human_input, placeholders, governance_notes, SI rules |
| `ASSET_TO_SECTIONS` | 62 CAP/ASP asset IDs → section IDs (contribution map) |
| `SECTION_ASSET_DRIVERS` | 30 section IDs → driver asset lists (inclusion trigger map) |
| `ALWAYS_MANDATORY` | 36 sections always MANDATORY (M-ALL / M-FIXED / M-SA) |
| `AMS_EXCLUDED` | 11 sections excluded for Pattern 13 AMS (SI-001) |
| `AMS_ONLY` | 7 sections (S-70–S-76) included only for AMS |
| `STANDARD_ORDER` | 82-section standard assembly sequence |
| `AMS_ORDER` | AMS-specific assembly sequence (SI-001, SI-005 applied) |
| `build_section_manifest()` | Core engine: evaluates all 82 sections → SectionManifest |
| `manifest_to_dict()` | Serialises SectionManifest to YAML-compatible dict |
| `write_manifest_yaml()` | Writes manifest YAML to Proposals directory |
| `generate_assembly_report()` | Markdown assembly report for all regression scenarios |
| `generate_traceability_report()` | Full section traceability table per scenario |
| `run_regression()` | 6 canonical scenarios, structural and ordering checks |
| `run_self_tests()` | 22 self-tests covering all rule patterns and SI rules |

### 4.2 Section Inclusion Logic

The inclusion cascade in `build_section_manifest()`:

1. **AMS exclusions first** — 11 sections forced EXCLUDED for AMS before any other check
2. **AMS-only exclusions** — 7 AMS-only sections forced EXCLUDED for non-AMS
3. **ALWAYS_MANDATORY** — 36 sections forced MANDATORY (M-ALL / M-FIXED / M-SA)
4. **Platform-conditional** — COND-ORA / COND-ACU / COND-BB / COND-AMS — driven by asset selection
5. **Asset-driven** — conditional sections triggered by MANDATORY or OPTIONAL_SELECTED driver assets
6. **Default** — DEFAULT_EXCLUDED

### 4.3 Assembly Order Design

Standard order follows PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 natural section progression.

AMS order implements three SI rules simultaneously:
- **SI-001:** S-38 excluded; S-73 appears within AMS Support block
- **SI-005:** S-67–S-69 References assembled after S-49–S-52 Commercial
- **SI-007:** Within AMS Support block, S-74→S-70→S-71→S-72→S-73→S-75→S-76 enforces SLA/Incident separation

---

## 5. Self-Test Suite — 22/22 PASS

| Test | Coverage | Result |
|---|---|---|
| T01 S-01 Cover Page mandatory (M-ALL) | Unconditional M-ALL | PASS |
| T02 S-03 Company Overview mandatory (M-ALL) | Unconditional M-ALL | PASS |
| T03 S-16 HCM Capability mandatory for Oracle HCM Cloud | COND-HCM asset-driven | PASS |
| T04 S-38 Change Control present for Implementation | M-FIXED non-AMS | PASS |
| T05 S-09 Oracle Partnership for Oracle HCM Cloud | COND-ORA asset-driven | PASS |
| T06 SI-006 S-49 before S-52 | Ordering rule | PASS |
| T07 SI-001 S-38 EXCLUDED for AMS | AMS exclusion | PASS |
| T08 SI-001 S-73 MANDATORY for AMS | AMS S-38 replacement | PASS |
| T09 S-34 EXCLUDED for AMS | AMS exclusion | PASS |
| T10 AMS Support order: S-74 before S-70 | SI-007 ordering | PASS |
| T11 SI-005 S-67 after S-49 in AMS | AMS References ordering | PASS |
| T12 S-09 Oracle Partnership EXCLUDED for Acumatica | Platform exclusion | PASS |
| T13 S-10 Acumatica Partnership present for Acumatica | COND-ACU | PASS |
| T14 S-23 Acumatica Financials present when module in scope | Asset-driven conditional | PASS |
| T15 S-29 BeBanking H2H Banking present for BeBanking | COND-BB | PASS |
| T16 S-09 Oracle Partnership EXCLUDED for BeBanking | Platform exclusion | PASS |
| T17 S-59 B-BBEE MANDATORY (M-SA) | South African mandatory | PASS |
| T18 AMS Support S-70–S-76 all MANDATORY | AMS-only block | PASS |
| T19 AMS S-70–S-76 EXCLUDED for Implementation | Non-AMS exclusion | PASS |
| T20 Assembly sequence deterministic (no duplicates) | Deterministic ordering | PASS |
| T21 S-22 OCI triggered when oci_in_scope=True | Boolean-driven conditional | PASS |
| T22 S-47 CV placeholder flagged with ADR-001 | ADR-001 enforcement | PASS |
| **Total** | | **22/22 PASS** |

---

## 6. Regression Results — 6/6 PASS, 0 Violations

| Scenario | Platform | Pattern | Mandatory | Optional | Excluded | Default | Val Errors | Val Warnings |
|---|---|---|---|---|---|---|---|---|
| ARM-IT045 | Oracle EBS | P13 (AMS) | 43 | 2 | 21 | 16 | 0 | 1 |
| REG-HCM-P3-MINING | Oracle HCM Cloud | P3 | 41 | 1 | 18 | 22 | 0 | 1 |
| REG-OIC-P7 | Oracle Integration Cloud | P7 | 41 | 0 | 18 | 23 | 0 | 1 |
| REG-ERP-P7-FULLSUITE | Oracle ERP Cloud | P7 | 42 | 1 | 18 | 21 | 0 | 1 |
| REG-ACU-P11 | Acumatica | P11 | 41 | 3 | 13 | 25 | 0 | 1 |
| REG-BEB-P12 | BeBanking | P12 | 40 | 0 | 18 | 24 | 0 | 1 |

**All 6 scenarios: 0 validation errors. Deterministic across repeated execution.**

*Note: 1 validation warning per scenario is the governance B-BBEE flag (VAL-004 only for AMS) — informational, not blocking.*

### ARM-IT045 (Oracle EBS, AMS, Mining) — Key Section Decisions

| Category | Sections | Key Rules |
|---|---|---|
| AMS-excluded | S-34,S-35,S-38,S-39,S-40,S-41,S-42,S-43,S-46,S-47,S-48 | SI-001 — AMS Pattern 13 |
| AMS Support block | S-74→S-70→S-71→S-72→S-73→S-75→S-76 | SI-001, SI-007 |
| Oracle EBS capability | S-18 (W2S1-002), S-21 (W2S1-004) | EBS platform; AMS |
| EBS overlays | S-71/S-74 enriched | EBS-AMS-SLA-OVERLAY-V1; EBS-DRM-ASSUMPTIONS-V1 |
| References after Commercial | S-67 after S-49 | SI-005 |

### REG-HCM-P3-MINING (Oracle HCM Cloud, Implementation, Mining)

| Category | Sections | Key Rules |
|---|---|---|
| HCM Capability | S-16 (MANDATORY — HCM Core + modules) | COND-HCM |
| Compensation (Mining) | S-16 includes W3S1-005 | GOV-010 / G-001 — Mining only |
| Payroll Integration | S-19 (OPTIONAL — W3S1-009) | payroll_integration in context |
| Methodology | S-34 (W2S1-005 Oracle Methodology) | M-ALL Implementation |
| AMS sections | S-70–S-76 all EXCLUDED | Non-AMS |

---

## 7. Manifests Generated

| Tender | Manifest Path |
|---|---|
| ARM-IT045 | `08_Commercial/Proposals/ARM-IT045/PROPOSAL_SECTION_MANIFEST_ARM-IT045.yaml` |
| REG-HCM-P3-MINING | `08_Commercial/Proposals/REG-HCM-P3-MINING/PROPOSAL_SECTION_MANIFEST_REG-HCM-P3-MINING.yaml` |
| REG-OIC-P7 | `08_Commercial/Proposals/REG-OIC-P7/PROPOSAL_SECTION_MANIFEST_REG-OIC-P7.yaml` |
| REG-ERP-P7-FULLSUITE | `08_Commercial/Proposals/REG-ERP-P7-FULLSUITE/PROPOSAL_SECTION_MANIFEST_REG-ERP-P7-FULLSUITE.yaml` |
| REG-ACU-P11 | `08_Commercial/Proposals/REG-ACU-P11/PROPOSAL_SECTION_MANIFEST_REG-ACU-P11.yaml` |
| REG-BEB-P12 | `08_Commercial/Proposals/REG-BEB-P12/PROPOSAL_SECTION_MANIFEST_REG-BEB-P12.yaml` |

---

## 8. Platform Maturity Declaration

| Dimension | Before PF2-003 | After PF2-003 |
|---|---|---|
| Section orchestration | Capability-list only; no section mapping | **Section manifest: 82 sections, deterministic** |
| Assembly sequence | Defined in docs; not enforced by engine | **Enforced in PSAE; SI-001/005/006/007 active** |
| Section traceability | None | **Full: every section explains itself** |
| AMS pattern enforcement | Manual; pattern engine docs only | **Automated: 11 AMS exclusions; S-73 replaces S-38** |
| Governance encoding | Manual reminders | **ADR-001, GOV-010, B-BBEE flags in every manifest** |
| PSAE engine | Not implemented | **proposal_section_engine.py v1.0 operational** |
| Self-tests | — | **22/22 PASS** |
| Regression | — | **6 scenarios, 0 violations** |
| Platform maturity | L5.3 | **L5.4** |

---

## 9. Deliverables

| Deliverable | Location | Status |
|---|---|---|
| proposal_section_engine.py v1.0 | 08_Commercial/Assembly_Engine/ | COMPLETE |
| PROPOSAL_SECTION_ENGINE.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| SECTION_MANIFEST_STANDARD.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| SECTION_TRACEABILITY_STANDARD.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| PROPOSAL_SECTION_MANIFEST_ARM-IT045.yaml | 08_Commercial/Proposals/ARM-IT045/ | COMPLETE |
| PROPOSAL_SECTION_MANIFESTS (5 regression) | 08_Commercial/Proposals/[TENDER]/ | COMPLETE |
| PROPOSAL_SECTION_ASSEMBLY_REPORT.md | 08_Commercial/Reports/ | COMPLETE |
| SECTION_TRACEABILITY_REPORT.md | 08_Commercial/Reports/ | COMPLETE |
| PF2_003_IMPLEMENTATION_REPORT.md | 08_Commercial/Reports/ | COMPLETE |

---

## 10. Known Gaps and Next Steps

| Item | Description | Priority |
|---|---|---|
| RSE integration | Risk selections from rse.py not yet fed into S-37/S-50 manifest entries | High |
| S-22 OCI capability | No standalone OCI capability asset; section uses assumption pack as proxy | High |
| Assumption sub-section extraction | S-30/S-31/S-33 extract from ASP by section tag; tagging standard defined but not automated | Medium |
| S-44 Disaster Recovery | Methodology folder empty; section always PLACEHOLDER | Medium |
| S-65/S-66 POPIA/PAIA | OAR-E01/E02 not resolved; sections always PLACEHOLDER | Medium |
| Proposal Renderer | Next stage: consume Section Manifest to produce formatted proposal document | Next |

---

## 11. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-003 | Initial implementation report |
