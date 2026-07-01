---
document_id: RISK-SELECTION-AUDIT-REG-HCM-P3
title: "Risk Selection Audit — REG-HCM-P3"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
---

# Risk Selection Audit — REG-HCM-P3

**Generated:** 2026-06-29 07:10  
**Engine:** RSE v1.0 | AREL V1.0  
**Tender:** REG-HCM-P3 | P3 | Oracle HCM Cloud | Implementation  

---

## Audit Summary

| Metric | Value |
|---|---|
| Risks evaluated | 40 |
| MANDATORY | 15 |
| OPTIONAL_SELECTED | 0 |
| EXCLUDED | 4 |
| PATTERN_EXCLUDED | 15 |
| DEFAULT_EXCLUDED | 6 |
| **Total selected** | **15** |
| Validation violations | 0 |

---

## Tender Context Used

| Field | Value |
|---|---|
| tender_id | REG-HCM-P3 |
| pattern | P3 |
| platform | Oracle HCM Cloud |
| engagement_type | Implementation |
| modules | Oracle HCM Core, Oracle Payroll Cloud, Oracle Time and Labor |
| country | ZA |
| client_size | Enterprise |
| client_sector | Mining |
| payroll_integration | True |
| pricing_type | Fixed Price |
| fixed_price | True |
| integration_scope | True |
| security_in_scope | False |
| migration_scope | False |
| dr_in_scope | False |
| integration_count | None |
| oax_in_scope | None |
| analytics_requirements_in_tender | None |
| personal_data_in_scope | None |
| help_desk_in_scope | None |
| feature_licensing_confirmed | None |
| delivery_model | — |

---

## Full Evaluation Trace

| Risk ID | Status | excl_if result | mand_if result | opt_if result | Reason |
|---|---|---|---|---|---|
| RC-CLIENT-001 | **MANDATORY** | `engagement_type == "AMS" or engagement_type == "DBA"` → FALSE | `engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: engagement_type == "Implementation" |
| RC-CLIENT-002 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: engagement_type == "Implementation" |
| RC-CLIENT-003 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P1', 'P2', 'P4'] |
| RC-CLIENT-004 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P5', 'P1', 'P2'] |
| RC-CLIENT-005 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P1', 'P2'] |
| RC-CLIENT-006 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P13'] |
| RC-CLIENT-007 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Impl |
| RC-COMM-001 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P1', 'P2'] |
| RC-COMM-002 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P13'] |
| RC-COMM-003 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `integration_method_prescribed_in_tender == TRUE` → FALSE | `integration_method_prescribed_in_tender == FALSE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-COMP-001 | **MANDATORY** | — | `country == "ZA" and (personal_data_in_scope == TRUE or payroll_integration == TRUE)` → TRUE | `country != "ZA"` → FALSE | mandatory_if → TRUE: country == "ZA" and (personal_data_in_scope == TRUE or payr |
| RC-DATA-001 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Impl |
| RC-DATA-002 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P5', 'P1', 'P2'] |
| RC-DATA-003 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `payroll_integration == TRUE and platform contains "Oracle HCM"` → TRUE | `payroll_integration == FALSE and platform contains "Oracle HCM"` → FALSE | mandatory_if → TRUE: payroll_integration == TRUE and platform contains "Oracle H |
| RC-DATA-004 | **EXCLUDED** | `not modules contains "Oracle WFM"` → TRUE | `modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: not modules contains "Oracle WFM" |
| RC-DATA-005 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P1', 'P2'] |
| RC-INT-001 | **MANDATORY** | `engagement_type == "AMS" or payroll_integration == FALSE` → FALSE | `payroll_integration == TRUE and platform contains "Oracle HCM"` → TRUE | — | mandatory_if → TRUE: payroll_integration == TRUE and platform contains "Oracle H |
| RC-INT-002 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `integration_count > 2` → FALSE | `integration_count <= 2` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-003 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle Integration Cloud" and third_party_api == TRUE` → FALSE | `platform contains "Oracle Integration Cloud" and third_party_api == FALSE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-004 | **MANDATORY** | `not payroll_integration == TRUE` → FALSE | `payroll_integration == TRUE and (engagement_type == "Implementation" or engagement_type == "AMS")` → TRUE | — | mandatory_if → TRUE: payroll_integration == TRUE and (engagement_type == "Implem |
| RC-INT-005 | **MANDATORY** | `engagement_type == "AMS" or payroll_integration == FALSE` → FALSE | `payroll_integration == TRUE and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: payroll_integration == TRUE and engagement_type == "Impleme |
| RC-INT-006 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle Integration Cloud"` → FALSE | — | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-007 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `payroll_integration == TRUE and (platform == "Acumatica" or (platform contains "Oracle" and payroll_provider == "non-standard"))` → FALSE | — | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-OPS-001 | **MANDATORY** | `engagement_type == "DBA"` → FALSE | `TRUE` → TRUE | — | mandatory_if → TRUE: TRUE |
| RC-PROJ-001 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | `platform contains "Oracle ERP" and engagement_type == "Implementation"` → FALSE | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Impl |
| RC-PROJ-002 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P2'] |
| RC-PROJ-003 | **MANDATORY** | `engagement_type == "AMS" or platform == "OIC Standalone"` → FALSE | `platform contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Impl |
| RC-PROJ-004 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `fixed_price == TRUE` → TRUE | `fixed_price == FALSE` → FALSE | mandatory_if → TRUE: fixed_price == TRUE |
| RC-TECH-001 | **MANDATORY** | `platform == "Acumatica" or platform == "BeBanking"` → FALSE | `platform contains "Oracle" and (engagement_type == "Implementation" or engagement_type == "AMS")` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle" and (engagement_type == "Impleme |
| RC-TECH-002 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-003 | **EXCLUDED** | `not modules contains "Oracle WFM"` → TRUE | `modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: not modules contains "Oracle WFM" |
| RC-TECH-004 | **EXCLUDED** | `not modules contains "Oracle WFM"` → TRUE | `modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: not modules contains "Oracle WFM" |
| RC-TECH-005 | **EXCLUDED** | `country != "ZA" or not modules contains "Oracle WFM"` → TRUE | `country == "ZA" and modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: country != "ZA" or not modules contains "Oracle WFM" |
| RC-TECH-006 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-007 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-008 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `feature_licensing_confirmed == FALSE and engagement_type == "Implementation"` → FALSE | `feature_licensing_confirmed == TRUE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-TECH-009 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-010 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P13'] |
| RC-TECH-011 | PATTERN_EXCLUDED | — | — | — | Pattern P3 not in applicable patterns ['P4', 'P1', 'P2'] |
| RC-TECH-012 | **MANDATORY** | `country != "ZA"` → FALSE | `country == "ZA" and payroll_integration == TRUE` → TRUE | — | mandatory_if → TRUE: country == "ZA" and payroll_integration == TRUE |

---

## AREL Normalization Applied

The following normalizations were applied to ERR expressions before evaluation:

| Transformation | Rule |
|---|---|
| `CONTAINS` → `contains` | Keyword case normalization |
| `AND` → `and`, `OR` → `or`, `NOT` → `not` | Keyword case normalization |
| Standalone `=` → `==` | Equality operator normalization (preserves `!=`, `>=`, `<=`) |
| `"OIC"` → `"Oracle Integration Cloud"` | Platform alias normalization |
| `country: "RSA"` → `"ZA"` | Country ISO 3166-1 alpha-2 normalization |
| List `contains` → substring per element | RSE list-aware contains |

*Generated by RSE v1.0 — 2026-06-29 07:10*
