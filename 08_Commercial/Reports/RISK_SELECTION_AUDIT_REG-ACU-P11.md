---
document_id: RISK-SELECTION-AUDIT-REG-ACU-P11
title: "Risk Selection Audit — REG-ACU-P11"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
---

# Risk Selection Audit — REG-ACU-P11

**Generated:** 2026-06-29 07:10  
**Engine:** RSE v1.0 | AREL V1.0  
**Tender:** REG-ACU-P11 | P11 | Acumatica | Implementation  

---

## Audit Summary

| Metric | Value |
|---|---|
| Risks evaluated | 40 |
| MANDATORY | 4 |
| OPTIONAL_SELECTED | 0 |
| EXCLUDED | 0 |
| PATTERN_EXCLUDED | 31 |
| DEFAULT_EXCLUDED | 5 |
| **Total selected** | **4** |
| Validation violations | 0 |

---

## Tender Context Used

| Field | Value |
|---|---|
| tender_id | REG-ACU-P11 |
| pattern | P11 |
| platform | Acumatica |
| engagement_type | Implementation |
| modules | Acumatica Financial Management, Acumatica Project Accounting |
| country | ZA |
| client_size | Mid-Market |
| client_sector | Construction |
| payroll_integration | False |
| pricing_type | Fixed Price |
| fixed_price | True |
| integration_scope | False |
| security_in_scope | False |
| migration_scope | True |
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
| RC-CLIENT-003 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P4'] |
| RC-CLIENT-004 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P5', 'P1', 'P2'] |
| RC-CLIENT-005 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2'] |
| RC-CLIENT-006 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P13'] |
| RC-CLIENT-007 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-COMM-001 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2'] |
| RC-COMM-002 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P13'] |
| RC-COMM-003 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `integration_method_prescribed_in_tender == TRUE` → FALSE | `integration_method_prescribed_in_tender == FALSE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-COMP-001 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3', 'P12', 'P13'] |
| RC-DATA-001 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-002 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P5', 'P1', 'P2'] |
| RC-DATA-003 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-004 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-005 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2'] |
| RC-INT-001 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-INT-002 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `integration_count > 2` → FALSE | `integration_count <= 2` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-003 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle Integration Cloud" and third_party_api == TRUE` → FALSE | `platform contains "Oracle Integration Cloud" and third_party_api == FALSE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-004 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P3', 'P6', 'P13'] |
| RC-INT-005 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3', 'P6'] |
| RC-INT-006 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle Integration Cloud"` → FALSE | — | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-007 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `payroll_integration == TRUE and (platform == "Acumatica" or (platform contains "Oracle" and payroll_provider == "non-standard"))` → FALSE | — | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-OPS-001 | **MANDATORY** | `engagement_type == "DBA"` → FALSE | `TRUE` → TRUE | — | mandatory_if → TRUE: TRUE |
| RC-PROJ-001 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-PROJ-002 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P2'] |
| RC-PROJ-003 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-PROJ-004 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `fixed_price == TRUE` → TRUE | `fixed_price == FALSE` → FALSE | mandatory_if → TRUE: fixed_price == TRUE |
| RC-TECH-001 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P13'] |
| RC-TECH-002 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-003 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-004 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-005 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-006 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-007 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-008 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2', 'P3', 'P7', 'P8', 'P9'] |
| RC-TECH-009 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-010 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P13'] |
| RC-TECH-011 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P4', 'P1', 'P2'] |
| RC-TECH-012 | PATTERN_EXCLUDED | — | — | — | Pattern P11 not in applicable patterns ['P3', 'P6', 'P13'] |

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
