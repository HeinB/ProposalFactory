---
document_id: RISK-SELECTION-AUDIT-ARM-IT045
title: "Risk Selection Audit — ARM-IT045"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
---

# Risk Selection Audit — ARM-IT045

**Generated:** 2026-06-29 07:10  
**Engine:** RSE v1.0 | AREL V1.0  
**Tender:** ARM-IT045 | P1 | Oracle HCM Cloud | Implementation  

---

## Audit Summary

| Metric | Value |
|---|---|
| Risks evaluated | 40 |
| MANDATORY | 13 |
| OPTIONAL_SELECTED | 1 |
| EXCLUDED | 8 |
| PATTERN_EXCLUDED | 10 |
| DEFAULT_EXCLUDED | 8 |
| **Total selected** | **14** |
| Validation violations | 0 |

---

## Tender Context Used

| Field | Value |
|---|---|
| tender_id | ARM-IT045 |
| pattern | P1 |
| platform | Oracle HCM Cloud |
| engagement_type | Implementation |
| modules | Oracle HCM Core, Oracle Recruiting Cloud, Oracle Learning Cloud |
| country | ZA |
| client_size | Enterprise |
| client_sector | Government |
| payroll_integration | False |
| pricing_type | — |
| fixed_price | None |
| integration_scope | None |
| security_in_scope | None |
| migration_scope | None |
| dr_in_scope | None |
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
| RC-CLIENT-003 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `modules contains "Oracle Recruiting" and engagement_type == "Implementation"` → TRUE | `modules contains "Oracle HCM" and not modules contains "Oracle Recruiting"` → FALSE | mandatory_if → TRUE: modules contains "Oracle Recruiting" and engagement_type == |
| RC-CLIENT-004 | **MANDATORY** | `not modules contains "Oracle Learning"` → FALSE | `modules contains "Oracle Learning" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: modules contains "Oracle Learning" and engagement_type == " |
| RC-CLIENT-005 | **EXCLUDED** | `not modules contains "Oracle Compensation"` → TRUE | `modules contains "Oracle Compensation" and modules contains "Oracle Talent" and engagement_type == "Implementation"` → FALSE | `modules contains "Oracle Compensation" and not modules contains "Oracle Talent"` → FALSE | excluded_if → TRUE: not modules contains "Oracle Compensation" |
| RC-CLIENT-006 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P13'] |
| RC-CLIENT-007 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Impl |
| RC-COMM-001 | **DEFAULT_EXCLUDED** | — | `oax_in_scope == TRUE or analytics_requirements_in_tender == TRUE` → FALSE | `analytics_requirements_in_tender == FALSE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-COMM-002 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P13'] |
| RC-COMM-003 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P3', 'P6', 'P11'] |
| RC-COMP-001 | **DEFAULT_EXCLUDED** | — | `country == "ZA" and (personal_data_in_scope == TRUE or payroll_integration == TRUE)` → FALSE | `country != "ZA"` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-DATA-001 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Impl |
| RC-DATA-002 | **MANDATORY** | `not modules contains "Oracle Learning"` → FALSE | `modules contains "Oracle Learning" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: modules contains "Oracle Learning" and engagement_type == " |
| RC-DATA-003 | **OPTIONAL_SELECTED** | `engagement_type == "AMS"` → FALSE | `payroll_integration == TRUE and platform contains "Oracle HCM"` → FALSE | `payroll_integration == FALSE and platform contains "Oracle HCM"` → TRUE | optional_if → TRUE: payroll_integration == FALSE and platform contains "Oracle H |
| RC-DATA-004 | **EXCLUDED** | `not modules contains "Oracle WFM"` → TRUE | `modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: not modules contains "Oracle WFM" |
| RC-DATA-005 | **EXCLUDED** | `not modules contains "Oracle WFM"` → TRUE | `modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: not modules contains "Oracle WFM" |
| RC-INT-001 | **EXCLUDED** | `engagement_type == "AMS" or payroll_integration == FALSE` → TRUE | `payroll_integration == TRUE and platform contains "Oracle HCM"` → FALSE | — | excluded_if → TRUE: engagement_type == "AMS" or payroll_integration == FALSE |
| RC-INT-002 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `integration_count > 2` → FALSE | `integration_count <= 2` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-003 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P3', 'P6', 'P7', 'P8', 'P9', 'P11'] |
| RC-INT-004 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P3', 'P6', 'P13'] |
| RC-INT-005 | **EXCLUDED** | `engagement_type == "AMS" or payroll_integration == FALSE` → TRUE | `payroll_integration == TRUE and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: engagement_type == "AMS" or payroll_integration == FALSE |
| RC-INT-006 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P3', 'P6', 'P7', 'P8', 'P9', 'P11'] |
| RC-INT-007 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P3', 'P11'] |
| RC-OPS-001 | **MANDATORY** | `engagement_type == "DBA"` → FALSE | `TRUE` → TRUE | — | mandatory_if → TRUE: TRUE |
| RC-PROJ-001 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | `platform contains "Oracle ERP" and engagement_type == "Implementation"` → FALSE | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Impl |
| RC-PROJ-002 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P2'] |
| RC-PROJ-003 | **MANDATORY** | `engagement_type == "AMS" or platform == "OIC Standalone"` → FALSE | `platform contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Impl |
| RC-PROJ-004 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `fixed_price == TRUE` → FALSE | `fixed_price == FALSE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-TECH-001 | **MANDATORY** | `platform == "Acumatica" or platform == "BeBanking"` → FALSE | `platform contains "Oracle" and (engagement_type == "Implementation" or engagement_type == "AMS")` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle" and (engagement_type == "Impleme |
| RC-TECH-002 | **MANDATORY** | `country != "ZA"` → FALSE | `country == "ZA" and modules contains "Oracle HCM" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: country == "ZA" and modules contains "Oracle HCM" and engag |
| RC-TECH-003 | **EXCLUDED** | `not modules contains "Oracle WFM"` → TRUE | `modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: not modules contains "Oracle WFM" |
| RC-TECH-004 | **EXCLUDED** | `not modules contains "Oracle WFM"` → TRUE | `modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: not modules contains "Oracle WFM" |
| RC-TECH-005 | **EXCLUDED** | `country != "ZA" or not modules contains "Oracle WFM"` → TRUE | `country == "ZA" and modules contains "Oracle WFM" and engagement_type == "Implementation"` → FALSE | — | excluded_if → TRUE: country != "ZA" or not modules contains "Oracle WFM" |
| RC-TECH-006 | **DEFAULT_EXCLUDED** | `oax_in_scope == FALSE and analytics_requirements_in_tender == FALSE` → FALSE | `oax_in_scope == TRUE and engagement_type == "Implementation"` → FALSE | `analytics_requirements_in_tender == TRUE and oax_in_scope == FALSE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-TECH-007 | **DEFAULT_EXCLUDED** | `oax_in_scope == FALSE` → FALSE | `oax_in_scope == TRUE and engagement_type == "Implementation"` → FALSE | — | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-TECH-008 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `feature_licensing_confirmed == FALSE and engagement_type == "Implementation"` → FALSE | `feature_licensing_confirmed == TRUE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-TECH-009 | **DEFAULT_EXCLUDED** | `oda_in_scope == FALSE` → FALSE | `oda_in_scope == TRUE and engagement_type == "Implementation"` → FALSE | — | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-TECH-010 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P13'] |
| RC-TECH-011 | **MANDATORY** | `not modules contains "Oracle Recruiting"` → FALSE | `modules contains "Oracle Recruiting" and engagement_type == "Implementation"` → TRUE | — | mandatory_if → TRUE: modules contains "Oracle Recruiting" and engagement_type == |
| RC-TECH-012 | PATTERN_EXCLUDED | — | — | — | Pattern P1 not in applicable patterns ['P3', 'P6', 'P13'] |

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
