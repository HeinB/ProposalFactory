---
document_id: RISK-SELECTION-AUDIT-REG-BEB-P13
title: "Risk Selection Audit — REG-BEB-P13"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
---

# Risk Selection Audit — REG-BEB-P13

**Generated:** 2026-06-29 07:10  
**Engine:** RSE v1.0 | AREL V1.0  
**Tender:** REG-BEB-P13 | P13 | BeBanking | Implementation  

---

## Audit Summary

| Metric | Value |
|---|---|
| Risks evaluated | 40 |
| MANDATORY | 1 |
| OPTIONAL_SELECTED | 0 |
| EXCLUDED | 5 |
| PATTERN_EXCLUDED | 32 |
| DEFAULT_EXCLUDED | 2 |
| **Total selected** | **1** |
| Validation violations | 0 |

---

## Tender Context Used

| Field | Value |
|---|---|
| tender_id | REG-BEB-P13 |
| pattern | P13 |
| platform | BeBanking |
| engagement_type | Implementation |
| modules | BeBanking Core Banking, BeBanking Digital Channels |
| country | ZA |
| client_size | Enterprise |
| client_sector | Financial Services |
| payroll_integration | False |
| pricing_type | Time and Materials |
| fixed_price | False |
| integration_scope | True |
| security_in_scope | True |
| migration_scope | True |
| dr_in_scope | True |
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
| RC-CLIENT-001 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P11'] |
| RC-CLIENT-002 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3', 'P7', 'P8', 'P9', 'P11'] |
| RC-CLIENT-003 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P4'] |
| RC-CLIENT-004 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P5', 'P1', 'P2'] |
| RC-CLIENT-005 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2'] |
| RC-CLIENT-006 | **EXCLUDED** | `engagement_type != "AMS"` → TRUE | `engagement_type == "AMS" and help_desk_in_scope == TRUE` → FALSE | — | excluded_if → TRUE: engagement_type != "AMS" |
| RC-CLIENT-007 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-COMM-001 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2'] |
| RC-COMM-002 | **EXCLUDED** | `not help_desk_in_scope == TRUE` → TRUE | `help_desk_in_scope == TRUE and engagement_type == "AMS"` → FALSE | — | excluded_if → TRUE: not help_desk_in_scope == TRUE |
| RC-COMM-003 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P3', 'P6', 'P11'] |
| RC-COMP-001 | **DEFAULT_EXCLUDED** | — | `country == "ZA" and (personal_data_in_scope == TRUE or payroll_integration == TRUE)` → FALSE | `country != "ZA"` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-DATA-001 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-002 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P5', 'P1', 'P2'] |
| RC-DATA-003 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-004 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-005 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2'] |
| RC-INT-001 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-INT-002 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3', 'P6', 'P7', 'P8', 'P11'] |
| RC-INT-003 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P3', 'P6', 'P7', 'P8', 'P9', 'P11'] |
| RC-INT-004 | **EXCLUDED** | `not payroll_integration == TRUE` → TRUE | `payroll_integration == TRUE and (engagement_type == "Implementation" or engagement_type == "AMS")` → FALSE | — | excluded_if → TRUE: not payroll_integration == TRUE |
| RC-INT-005 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3', 'P6'] |
| RC-INT-006 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P3', 'P6', 'P7', 'P8', 'P9', 'P11'] |
| RC-INT-007 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P3', 'P11'] |
| RC-OPS-001 | **MANDATORY** | `engagement_type == "DBA"` → FALSE | `TRUE` → TRUE | — | mandatory_if → TRUE: TRUE |
| RC-PROJ-001 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-PROJ-002 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P2'] |
| RC-PROJ-003 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-PROJ-004 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3', 'P7', 'P8', 'P9', 'P11'] |
| RC-TECH-001 | **EXCLUDED** | `platform == "Acumatica" or platform == "BeBanking"` → TRUE | `platform contains "Oracle" and (engagement_type == "Implementation" or engagement_type == "AMS")` → FALSE | — | excluded_if → TRUE: platform == "Acumatica" or platform == "BeBanking" |
| RC-TECH-002 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-003 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-004 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-005 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-006 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-007 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-008 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2', 'P3', 'P7', 'P8', 'P9'] |
| RC-TECH-009 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-010 | **EXCLUDED** | `engagement_type != "AMS"` → TRUE | `engagement_type == "AMS" and digital_channels == TRUE` → FALSE | — | excluded_if → TRUE: engagement_type != "AMS" |
| RC-TECH-011 | PATTERN_EXCLUDED | — | — | — | Pattern P13 not in applicable patterns ['P4', 'P1', 'P2'] |
| RC-TECH-012 | **DEFAULT_EXCLUDED** | `country != "ZA"` → FALSE | `country == "ZA" and payroll_integration == TRUE` → FALSE | — | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |

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
