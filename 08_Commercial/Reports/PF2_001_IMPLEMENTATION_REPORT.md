---
document_id: PF2-001-IMPLEMENTATION-REPORT-V1
title: "PF2-001 — Risk Selection Engine — Implementation Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-29"
created_by: "PF2-001 — Proposal Factory Risk Selection Engine"
approved_by: "PF2-001"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Work Package Report"
scope: "Documents the design, implementation, and regression results for the Risk Selection Engine — the first Proposal Factory component that consumes the certified Knowledge Platform."
---

# PF2-001 — Risk Selection Engine — Implementation Report

**Work Package:** PF2-001  
**Date:** 2026-06-29  
**Status:** COMPLETE  
**Platform Maturity:** L5.1 → **L5.2**

---

## 1. Objective

Build the Proposal Factory Risk Selection Engine (RSE). The RSE selects proposal risks deterministically from the approved Enterprise Risk Library (40 RSK assets) using the tender context from a certified Assembly Manifest.

**Success criteria:**
- 100% deterministic selection
- No duplicate risks, no contradictory selections
- All mandatory risks included, excluded risks omitted
- AREL V1.0 compliance preserved
- 5 regression scenarios covering all platforms

---

## 2. Pre-Conditions Confirmed at PF2-001 Start

| Pre-condition | Status |
|---|---|
| Knowledge Platform Version 1.0 | COMPLETE — WP19D |
| Platform maturity | L5.1 |
| Registry V1.0 CERTIFIED | BUILD-20260628-150801; 213 core + 1,136 ASM |
| KVE v2.0 operational | 76 rules; AREL V1.0 evaluator 86/86 PASS |
| AREL V1.0 frozen | WP19B; grammar; 30 ARVAL rules; 80 test cases |
| Enterprise Risk Register | V1.0; 40/40 APPROVED |
| Risk Proposal Mapping | V1.0; DRAFT (pending BU review) |
| Risk Assumption Cross-Reference | V1.0; DRAFT (pending BU review) |
| AV-011 BLOCK | CLEARED — WP19C; RC-OPS-001 in registry |

---

## 3. Implementation

### 3.1 rse.py — Risk Selection Engine

**Location:** `08_Commercial/Assembly_Engine/rse.py`  
**Lines:** ~700  
**Dependencies:** PyYAML (stdlib otherwise)

**Key components:**

| Component | Description |
|---|---|
| `RSEARELEvaluator` | AREL V1.0 recursive-descent evaluator with list-aware `contains` |
| `RSEContext` | 20 KVE fields + 14 RSE extension fields (34 total) |
| `RSKRecord` | Parsed ERR risk entry (extracted from markdown) |
| `normalize_arel()` | Normalizes ERR expressions to AREL V1.0 syntax |
| `parse_risk_register()` | Parses ENTERPRISE_RISK_REGISTER_V1.md |
| `select_risks()` | Core selection cascade (6 steps) |
| `validate_selections()` | V-001, V-002, V-003 deterministic checks |

### 3.2 Self-Test Suite

17-test suite (`--run-tests`):

| Test | Result |
|---|---|
| platform contains 'Oracle HCM' | PASS |
| modules list-aware contains 'Oracle Learning' | PASS |
| modules contains 'Oracle WFM' → False | PASS |
| engagement_type == 'Implementation' | PASS |
| payroll_integration == FALSE (bool-safe) | PASS |
| payroll_integration == TRUE → False | PASS |
| not payroll_integration == TRUE | PASS |
| NULL var → False (null-safe) | PASS |
| NULL var for int comparison → False | PASS |
| compound AND expression | PASS |
| country == ZA | PASS |
| country != ZA → False | PASS |
| OIC alias: platform contains Oracle Integration Cloud | PASS |
| TRUE literal | PASS |
| not (payroll_integration == TRUE) via parentheses | PASS |
| platform == Acumatica → False | PASS |
| platform excluded check (OR) | PASS |
| **Total** | **17/17 PASS** |

---

## 4. AREL Expression Normalization

The Enterprise Risk Register uses a pre-standard expression syntax. Key normalization transformations:

| Issue | ERR Expression | Normalized |
|---|---|---|
| Uppercase operators | `CONTAINS`, `AND`, `OR`, `NOT` | Lowercase equivalents |
| Single equals | `engagement_type = "AMS"` | `engagement_type == "AMS"` |
| Platform abbreviation | `platform contains "OIC"` | `platform contains "Oracle Integration Cloud"` |
| Country code | Context `country: "RSA"` | Normalized to `"ZA"` at load time |

---

## 5. RSE Design Decisions

### 5.1 Source of RSK Data
The RSE reads directly from `ENTERPRISE_RISK_REGISTER_V1.md` (the source of truth), not from `KNOWLEDGE_ASSET_REGISTRY_V1.yaml`. The KRPE extraction of RSK `mandatory_if_engagement` fields has known data quality issues (null values for some fields). Parsing the markdown source avoids this dependency.

### 5.2 List-Aware Contains
The AREL `contains` operator, when applied to a list variable, performs substring matching on each list element. This is necessary because ERR expressions use partial module names (e.g., "Oracle Learning") while context module lists use full canonical names (e.g., "Oracle Learning Cloud").

### 5.3 Pattern Filter
The RSE uses the `proposal_patterns` field from each ERR entry (e.g., "P1, P2, P3") as a pre-filter before AREL evaluation. This ensures risks not applicable to the tender's proposal pattern are correctly classified as PATTERN_EXCLUDED without consuming evaluation cycles.

### 5.4 RSE Extension YAML
Fourteen risk-specific context fields are not in the base 20-variable AREL context set. These are provided via an optional RSE extension YAML (`--extension`). When absent, null-safe evaluation applies and affected risks resolve to DEFAULT_EXCLUDED.

---

## 6. Regression Results

### 6.1 Summary

| Scenario | Tender | Pattern | Platform | Selected | Mandatory | Optional | Violations |
|---|---|---|---|---|---|---|---|
| ARM-IT045 | ARM-IT045 | P1 | Oracle HCM Cloud | 14 | 13 | 1 | 0 |
| OracleHCM-P3 | REG-HCM-P3 | P3 | Oracle HCM Cloud | 15 | 15 | 0 | 0 |
| OIC-P7 | REG-OIC-P7 | P7 | Oracle Integration Cloud | 6 | 5 | 1 | 0 |
| Acumatica-P11 | REG-ACU-P11 | P11 | Acumatica | 4 | 4 | 0 | 0 |
| BeBanking-P13 | REG-BEB-P13 | P13 | BeBanking | 1 | 1 | 0 | 0 |

**All 5 scenarios: 0 validation violations, deterministic across repeated runs.**

### 6.2 ARM-IT045 (P1 — Oracle HCM Cloud, Implementation, ZA Government)

Modules: Oracle HCM Core, Oracle Recruiting Cloud, Oracle Learning Cloud  
payroll_integration: false

**Selected (14):**
- MANDATORY (13): RC-PROJ-001, RC-PROJ-003, RC-DATA-001, RC-DATA-002, RC-CLIENT-001, RC-CLIENT-002, RC-CLIENT-003, RC-CLIENT-004, RC-CLIENT-007, RC-TECH-001, RC-TECH-002, RC-TECH-011, RC-OPS-001
- OPTIONAL_SELECTED (1): RC-DATA-003 (optional_if: `payroll_integration == FALSE AND platform contains "Oracle HCM"`)

Key exclusions: RC-DATA-004/005 (no WFM), RC-INT-001/005 (no payroll integration), RC-TECH-003/004/005 (no WFM), RC-CLIENT-005 (no Compensation module)

### 6.3 OracleHCM-P3 (P3 — Oracle HCM Cloud + Payroll Integration, ZA Mining)

Modules: Oracle HCM Core, Oracle Payroll Cloud, Oracle Time and Labor  
payroll_integration: true, pricing_type: Fixed Price

**Selected (15):**  
All 15 MANDATORY including: RC-INT-001/005 (payroll integration), RC-DATA-003 (HCM + payroll), RC-TECH-012 (ZA legislative), RC-COMP-001 (POPIA + payroll), RC-PROJ-004 (Fixed Price)

Notable: payroll_integration=true activates 4 additional mandatory risks vs ARM-IT045. Fixed Price activates RC-PROJ-004.

### 6.4 OIC-P7 (P7 — Oracle Integration Cloud, Implementation, ZA Financial Services)

Platform: Oracle Integration Cloud, integration_scope: true  
*Note: P7 = ERP Multi-Module in proposal pattern map; OIC context used for regression.*

**Selected (6):** RC-OPS-001, RC-INT-006 (field mapping), RC-CLIENT-001, RC-CLIENT-002, RC-TECH-001, RC-PROJ-004 (optional — T&M pricing)

31 of 40 risks are PATTERN_EXCLUDED for P7 — most HCM-specific risks don't apply.

### 6.5 Acumatica-P11 (P11 — Acumatica, Implementation, ZA Construction)

Modules: Acumatica Financial Management, Acumatica Project Accounting  
pricing_type: Fixed Price, payroll_integration: false

**Selected (4):** RC-OPS-001, RC-CLIENT-001, RC-CLIENT-002, RC-PROJ-004 (Fixed Price)

31 of 40 risks are PATTERN_EXCLUDED for P11. RC-TECH-001 is EXCLUDED (Acumatica platform explicitly excluded).

### 6.6 BeBanking-P13 (P13 — BeBanking, Implementation, ZA Financial Services)

Platform: BeBanking, engagement_type: Implementation, dr_in_scope: true

**Selected (1):** RC-OPS-001

32 of 40 risks PATTERN_EXCLUDED. 5 EXCLUDED (AMS-specific risks excluded by `engagement_type != "AMS"`). 2 DEFAULT_EXCLUDED (RC-TECH-012, RC-COMP-001 — extension fields needed).

**Note:** BeBanking canonical pattern is P12. This regression used P13 (AMS) per WP19D context. RC-OPS-001 patterns include P13 but not P12 — possible ERR oversight for P12. BeBanking P12 regression with RSE extension would activate RC-COMP-001 (POPIA) when `personal_data_in_scope=true`.

---

## 7. Platform Maturity Declaration

| Dimension | Before PF2-001 | After PF2-001 |
|---|---|---|
| Knowledge Platform | Complete (L5.1) | Complete (L5.1) — unchanged |
| RSE | Not implemented | **Operational — rse.py v1.0** |
| RSE self-tests | — | **17/17 PASS** |
| RSE regression | — | **5 scenarios, 0 violations** |
| AREL normalization | Not implemented | **ERR expressions normalized at evaluation** |
| RSE extension YAML | — | **14 extension fields; format defined** |
| Output documents | — | **SELECTED_RISK_REGISTER + RISK_SELECTION_AUDIT** |
| Platform maturity | L5.1 | **L5.2** |

---

## 8. Deliverables

| Deliverable | Location | Status |
|---|---|---|
| rse.py v1.0 | 08_Commercial/Assembly_Engine/rse.py | COMPLETE |
| RISK_SELECTION_ENGINE.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| RISK_SELECTION_REPORT_STANDARD.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| RISK_SELECTION_AUDIT_STANDARD.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| PF2_001_IMPLEMENTATION_REPORT.md | 08_Commercial/Reports/ | COMPLETE |
| SELECTED_RISK_REGISTER_ARM-IT045.md | 08_Commercial/Reports/ | COMPLETE |
| RISK_SELECTION_AUDIT_ARM-IT045.md | 08_Commercial/Reports/ | COMPLETE |
| SELECTED_RISK_REGISTER_REG-HCM-P3.md | 08_Commercial/Reports/ | COMPLETE |
| RISK_SELECTION_AUDIT_REG-HCM-P3.md | 08_Commercial/Reports/ | COMPLETE |
| SELECTED_RISK_REGISTER_REG-OIC-P7.md | 08_Commercial/Reports/ | COMPLETE |
| RISK_SELECTION_AUDIT_REG-OIC-P7.md | 08_Commercial/Reports/ | COMPLETE |
| SELECTED_RISK_REGISTER_REG-ACU-P11.md | 08_Commercial/Reports/ | COMPLETE |
| RISK_SELECTION_AUDIT_REG-ACU-P11.md | 08_Commercial/Reports/ | COMPLETE |
| SELECTED_RISK_REGISTER_REG-BEB-P13.md | 08_Commercial/Reports/ | COMPLETE |
| RISK_SELECTION_AUDIT_REG-BEB-P13.md | 08_Commercial/Reports/ | COMPLETE |

---

## 9. Known Gaps and Next Steps

| Item | Description | Priority |
|---|---|---|
| BeBanking P12 ERR gap | RC-OPS-001 patterns don't include P12 — ERR should be reviewed | High |
| RSE extension fields | 14 fields not in base context — produces DEFAULT_EXCLUDED | Medium |
| personal_data_in_scope | Should default to True for HCM/OIC ZA proposals | Medium |
| feature_licensing_confirmed | Should default to False for new Oracle implementations | Medium |
| ERR expression review | 40 risks use pre-standard AREL syntax — consider ERR update | Low |
| Assembly rules population | 49 CAP + 13 ASP mandatory_if still empty in registry | Next |

---

## 10. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-001 | Initial implementation report |
