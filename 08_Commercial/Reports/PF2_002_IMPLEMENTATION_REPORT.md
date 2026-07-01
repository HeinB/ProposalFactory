---
document_id: PF2-002-IMPLEMENTATION-REPORT-V1
title: "PF2-002 — Assembly Rule Enrichment Engine — Implementation Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-29"
created_by: "PF2-002 — Assembly Rule Enrichment Engine"
approved_by: "PF2-002"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Work Package Report"
scope: "Documents the design, implementation, and verification of the Assembly Rule Enrichment Engine (ARE) and the enrichment of all 49 CAP + 13 ASP governed assets with deterministic AREL V1.0 assembly expressions."
---

# PF2-002 — Assembly Rule Enrichment Engine — Implementation Report

**Work Package:** PF2-002  
**Date:** 2026-06-29  
**Status:** COMPLETE  
**Platform Maturity:** L5.2 → **L5.3**

---

## 1. Objective

Populate deterministic AREL V1.0 assembly expressions (`mandatory_if`, `optional_if`, `excluded_if`) for all 49 CAP and 13 ASP governed assets in the Knowledge Asset Registry.

**Success criteria:**
- Every governed CAP and ASP asset has at least one populated AREL field
- All expressions are syntactically valid and use only AREL V1.0 vocabulary
- No contradictory rules (excluded_if ∩ mandatory_if = ∅ for any context)
- No duplicate logic across assets
- 6 regression scenarios, 0 violations
- GOV-010 Mining restriction correctly encoded

---

## 2. Pre-Conditions Confirmed at PF2-002 Start

| Pre-condition | Status |
|---|---|
| Platform Maturity | L5.2 |
| Knowledge Platform v1.0 | COMPLETE — WP19D |
| Registry V1.0 CERTIFIED | BUILD-20260628-150801; 213 core + 1,136 ASM |
| RSE operational | rse.py v1.0; 17/17 PASS; 5 regression, 0 violations |
| AREL V1.0 FROZEN | WP19B; 20 context variables; 30 ARVAL rules; 80 test cases |
| CAP assembly_rules status | All 49 empty (`mandatory_if: ''`) |
| ASP assembly_rules status | All 13 empty (`mandatory_if: ''`) |
| KRPE architecture | Hardcodes empty assembly_rules for CAP/ASP — rules must come from ARE |

---

## 3. Architecture Decision

**Why ARE instead of KRPE enrichment?**

KRPE (Knowledge Registry Population Engine) hardcodes `mandatory_if: ""` for all CAP and ASP entries. Unlike RSK entries, CAP/ASP assembly rules cannot be sourced from source markdown documents — they are derived from platform-specific business logic (BOM mappings, engagement type rules, governance constraints).

The ARE engine is the single authoritative source of AREL expressions for CAP and ASP assets. KRPE remains the source for structural metadata. This separation preserves the KRPE rebuild idempotency while enabling governed AREL enrichment.

---

## 4. Implementation

### 4.1 are.py — Assembly Rule Enrichment Engine

**Location:** `08_Commercial/Assembly_Engine/are.py`  
**Version:** v1.0  
**Dependencies:** PyYAML (stdlib otherwise)  
**CLI:** `--validate`, `--enrich`, `--regression`, `--coverage PATH`, `--run-tests`

**Key components:**

| Component | Description |
|---|---|
| `ARELEvaluator` | Standard AREL V1.0 recursive-descent evaluator; `contains` = exact list membership |
| `ASSEMBLY_RULES` | 49 CAP rule dicts — canonical AREL expressions |
| `ASP_RULES` | 13 ASP rule dicts — canonical AREL expressions |
| `ALL_RULES` | Combined dict (62 entries) |
| `validate_all_rules()` | Syntax + variable + null-context evaluation check |
| `select_assets()` | AREL cascade: excluded_if → mandatory_if → optional_if → DEFAULT_EXCLUDED |
| `validate_selection()` | V-001/V-002/V-003 constraint checks |
| `run_regression()` | 6 regression scenarios with canonical inline contexts |
| `enrich_registry()` | Load YAML → apply rules → write enriched registry |
| `generate_coverage_report()` | Markdown coverage report to `08_Commercial/Reports/` |
| `run_self_tests()` | 20 self-tests covering all rule patterns |

### 4.2 AREL Evaluator Design

The ARE evaluator uses standard AREL V1.0 semantics:
- `contains` on list variables: exact membership (`"Oracle Recruiting Cloud" in modules`)
- `contains` on string variables: substring membership
- Null-safe: absent variable → false for comparisons
- `not expr` is unary prefix (not `!=` syntax)
- Type-safe boolean comparisons: `payroll_integration == true`

This differs from the RSE ARELEvaluator which uses list-aware substring matching for ERR expressions. ARE rules are written canonically — module names match exactly — so standard AREL semantics apply.

### 4.3 Rule Design Authority

All 62 AREL expressions were derived from:

| Source | Used For |
|---|---|
| CAPABILITY_SELECTION_ENGINE.md | BOM-to-asset inclusion rules, platform requirements |
| ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md | AREL V1.0 variable vocabulary and semantics |
| TENDER_PROFILE_STANDARD.md | Context variable definitions and canonical values |
| Governance Rule GOV-010 | Mining-only restriction for W3S1-005 |
| BOM 16 AMS | W5-ACU-001 mandatory for Acumatica AMS |

---

## 5. Self-Test Suite

20 self-tests covering all rule patterns:

| Test | Rule Pattern | Result |
|---|---|---|
| T01 Company Overview TRUE | Unconditional mandatory | PASS |
| T02 Company History TRUE | Unconditional mandatory | PASS |
| T03 Oracle Partnership — HCM | Platform in-list mandatory | PASS |
| T04 Acumatica Partnership — Oracle | Cross-platform exclusion | PASS |
| T05 BeBanking Overview — BeBanking | Platform mandatory | PASS |
| T06 Oracle Partnership — BeBanking | Bidirectional exclusion | PASS |
| T07 HCM Core — Oracle HCM Cloud | Always mandatory for platform | PASS |
| T08 Recruiting mandatory when module in scope | Module contains mandatory | PASS |
| T09 Recruiting optional when module absent | Optional fallback | PASS |
| T10 Compensation excluded for non-Mining | GOV-010 exclusion | PASS |
| T11 Compensation optional for Mining (no module) | GOV-010 optional tier | PASS |
| T12 Oracle Methodology excluded for AMS | Engagement exclusion | PASS |
| T13 Oracle Methodology mandatory for Implementation | Engagement mandatory | PASS |
| T14 Oracle EBS mandatory for EBS platform | Platform mandatory | PASS |
| T15 EBS SLA overlay mandatory for EBS AMS | EBS + AMS mandatory | PASS |
| T16 EBS SLA overlay excluded for HCM Cloud | `not platform ==` exclusion | PASS |
| T17 OCI pack mandatory when oci_in_scope=true | Boolean mandatory | PASS |
| T18 OCI pack default-excluded when oci_in_scope=false | Boolean default exclusion | PASS |
| T19 AMS pack mandatory for AMS engagement | Engagement mandatory | PASS |
| T20 AMS pack excluded for Implementation | Engagement exclusion | PASS |
| **Total** | | **20/20 PASS** |

---

## 6. AREL Validation Results

| Check | Result |
|---|---|
| V-001 Syntax: all 62 expressions parse without error | PASS — 0 issues |
| V-002 Variables: all identifiers in AREL V1.0 vocabulary | PASS — 0 invalid variables |
| V-003 Coverage: all 62 assets have at least one populated field | PASS — 62/62 |
| Contradiction check: no context activates both mandatory_if and excluded_if | PASS — 0 contradictions |
| Duplicate logic check: no identical expressions across different assets | PASS — 0 duplicates |

---

## 7. Regression Results

Six canonical tender scenarios covering all supported platforms:

| Scenario | Platform | Eng Type | Pattern | Mandatory | Optional | Excluded | Default | Violations |
|---|---|---|---|---|---|---|---|---|
| ARM-IT045-EBS-AMS | Oracle EBS | AMS | P13 | 12 | 3 | 8 | 39 | 0 |
| REG-HCM-P3-MINING | Oracle HCM Cloud | Implementation | P3 | 15 | 12 | 8 | 27 | 0 |
| REG-OIC-P7 | Oracle Integration Cloud | Implementation | P7 | 11 | 0 | 11 | 40 | 0 |
| REG-ERP-P7-FULLSUITE | Oracle ERP Cloud | Implementation | P7 | 14 | 0 | 10 | 38 | 0 |
| REG-ACU-P11 | Acumatica | Implementation | P11 | 11 | 6 | 11 | 34 | 0 |
| REG-BEB-P12 | BeBanking | Implementation | P12 | 16 | 3 | 11 | 32 | 0 |

**All 6 scenarios: 0 validation violations. Deterministic across repeated execution.**

### ARM-IT045-EBS-AMS (Oracle EBS, AMS, Mining)

Mandatory (12): Corporate block (6) + Oracle Partnership + Oracle EBS + Oracle Managed Services + EBS-AMS-SLA + EBS-DRM + AMS Pack  
Optional (3): Oracle DBA + OIC Accelerators + OIC Assumptions (integration_scope=true)  
Excluded (8): Acumatica/BeBanking partnerships + Oracle Methodology (AMS) + ERP/HCM/ACU/BEB assumptions (wrong platform) + W5-METH-001 (AMS)

### REG-HCM-P3-MINING (Oracle HCM Cloud, Mining, Payroll)

Mandatory (15): Corporate block + Oracle Partnership + Oracle Methodology + HCM Core + Compensation (Mining+module) + WFM + Payroll Interface + Journeys + HCM Base + Compensation Assumptions  
Optional (12): Talent + Recruiting + Learning + Analytics + Help Desk + AI Skills + Fusion Cloud (integration) + OIC Accelerators (integration) + HCM Recruiting/Learning/Talent Assumptions + OIC Assumptions (integration)

### REG-OIC-P7 (Oracle Integration Cloud, standalone)

Mandatory (11): Corporate block + Oracle Partnership + Fusion Cloud + Oracle Methodology + OIC Accelerators + OIC Assumptions  
Excluded (11): Acumatica/BeBanking partnerships + HCM/ERP/ACU/BEB base assumptions (wrong platform) + EBS overlays + AMS pack (Implementation)

### REG-ERP-P7-FULLSUITE (Oracle ERP Cloud, OCI in scope)

Mandatory (14): Corporate block + Oracle Partnership + Fusion Cloud + Oracle Methodology + Fusion Financials + Fusion Procurement + PPM + ERP Assumptions + OCI Assumptions  
Excluded (10): Acumatica/BeBanking partnerships + HCM/ACU/BEB base assumptions + EBS overlays + AMS pack + Compensation (non-Mining)

### REG-ACU-P11 (Acumatica, Financials + Project)

Mandatory (11): Corporate block + Acumatica Partnership + Financials (module match) + Project Accounting (module match) + ERP Methodology + ACU Base  
Optional (6): Distribution + Inventory + Manufacturing + CRM + Field Services + Payroll Integration (payroll=false)  
Excluded (11): Oracle Partnership + BeBanking + Oracle Managed Services (Acumatica) + Compensation (non-Mining) + HCM/ERP/BEB assumptions + EBS overlays + AMS pack

### REG-BEB-P12 (BeBanking, Supplier + Payroll Payments)

Mandatory (16): Corporate block + BeBanking Overview + BB Product Overview + BB H2H Banking + BB Supplier Payments (module) + BB Payroll Payments (module) + BB ERP Integration (integration) + BB Security (security) + BB Architecture + ERP Methodology + BeBanking Base  
Optional (3): BB Forex + BB Hosting + BB Monitoring  
Excluded (11): Oracle/Acumatica partnerships + Oracle Managed Services + Compensation (non-Mining) + HCM/ERP/ACU base assumptions + EBS overlays + AMS pack

---

## 8. Registry Enrichment

| Dimension | Value |
|---|---|
| Registry file | `00_Governance/Knowledge_Standards/KNOWLEDGE_ASSET_REGISTRY.yaml` |
| Build designation | BUILD-20260629-ARE-001 |
| CAP entries enriched | 49 / 49 |
| ASP entries enriched | 13 / 13 |
| Previous state | All 62 entries had `mandatory_if: ''`, `optional_if: ''`, `excluded_if: ''` |
| Post-enrichment state | All 62 entries populated with AREL V1.0 expressions |
| registry_last_synced | 2026-06-29 (all 62 entries) |

---

## 9. Platform Maturity Declaration

| Dimension | Before PF2-002 | After PF2-002 |
|---|---|---|
| Registry assembly_rules (CAP) | 49 × empty | **49 × populated AREL** |
| Registry assembly_rules (ASP) | 13 × empty | **13 × populated AREL** |
| ARE engine | Not implemented | **are.py v1.0 operational** |
| ARE self-tests | — | **20/20 PASS** |
| ARE regression | — | **6 scenarios, 0 violations** |
| AREL validation | — | **62/62 VALID, 0 issues** |
| GOV-010 encoding | Manual rule only | **Encoded in AREL excluded_if** |
| Capability Assembly | Governed but no rules | **Fully governed + rule-driven** |
| Platform maturity | L5.2 | **L5.3** |

---

## 10. Deliverables

| Deliverable | Location | Status |
|---|---|---|
| are.py v1.0 | 08_Commercial/Assembly_Engine/are.py | COMPLETE |
| KNOWLEDGE_ASSET_REGISTRY.yaml (enriched) | 00_Governance/Knowledge_Standards/ | COMPLETE — BUILD-20260629-ARE-001 |
| ASSEMBLY_RULE_COVERAGE_REPORT.md | 08_Commercial/Reports/ | COMPLETE |
| ASSEMBLY_RULE_ENRICHMENT_REPORT.md | 08_Commercial/Reports/ | COMPLETE |
| PF2_002_IMPLEMENTATION_REPORT.md | 08_Commercial/Reports/ | COMPLETE |

---

## 11. Known Gaps and Next Steps

| Item | Description | Priority |
|---|---|---|
| Module name canonicalization | TIL should normalize "Acumatica Financial Management" → "Acumatica Financials" | Medium |
| `industry` context field | Existing regression contexts lack industry — new TIL/context templates should populate it | High |
| `support_scope` | W5-ACU-001 optional when support_scope=true — ensure TIL captures this field | Medium |
| CAP assembly engine | Next step: consume enriched registry to drive proposal assembly section selection | Next |

---

## 12. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-002 | Initial implementation report |
