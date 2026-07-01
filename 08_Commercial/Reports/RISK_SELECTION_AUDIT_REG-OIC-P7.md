---
document_id: RISK-SELECTION-AUDIT-REG-OIC-P7
title: "Risk Selection Audit — REG-OIC-P7"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
---

# Risk Selection Audit — REG-OIC-P7

**Generated:** 2026-06-29 07:10  
**Engine:** RSE v1.0 | AREL V1.0  
**Tender:** REG-OIC-P7 | P7 | Oracle Integration Cloud | Implementation  

---

## Audit Summary

| Metric | Value |
|---|---|
| Risks evaluated | 40 |
| MANDATORY | 5 |
| OPTIONAL_SELECTED | 1 |
| EXCLUDED | 0 |
| PATTERN_EXCLUDED | 31 |
| DEFAULT_EXCLUDED | 3 |
| **Total selected** | **6** |
| Validation violations | 0 |

---

## Tender Context Used

| Field | Value |
|---|---|
| tender_id | REG-OIC-P7 |
| pattern | P7 |
| platform | Oracle Integration Cloud |
| engagement_type | Implementation |
| modules | Oracle Integration Cloud, Oracle API Gateway |
| country | ZA |
| client_size | Enterprise |
| client_sector | Financial Services |
| payroll_integration | False |
| pricing_type | Time and Materials |
| fixed_price | False |
| integration_scope | True |
| security_in_scope | True |
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
| RC-CLIENT-003 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P4'] |
| RC-CLIENT-004 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P5', 'P1', 'P2'] |
| RC-CLIENT-005 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2'] |
| RC-CLIENT-006 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P13'] |
| RC-CLIENT-007 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-COMM-001 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2'] |
| RC-COMM-002 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P13'] |
| RC-COMM-003 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P3', 'P6', 'P11'] |
| RC-COMP-001 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3', 'P12', 'P13'] |
| RC-DATA-001 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-002 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P5', 'P1', 'P2'] |
| RC-DATA-003 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-004 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-DATA-005 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2'] |
| RC-INT-001 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-INT-002 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `integration_count > 2` → FALSE | `integration_count <= 2` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-003 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle Integration Cloud" and third_party_api == TRUE` → FALSE | `platform contains "Oracle Integration Cloud" and third_party_api == FALSE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-INT-004 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P3', 'P6', 'P13'] |
| RC-INT-005 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3', 'P6'] |
| RC-INT-006 | **MANDATORY** | `engagement_type == "AMS"` → FALSE | `platform contains "Oracle Integration Cloud"` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle Integration Cloud" |
| RC-INT-007 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P3', 'P11'] |
| RC-OPS-001 | **MANDATORY** | `engagement_type == "DBA"` → FALSE | `TRUE` → TRUE | — | mandatory_if → TRUE: TRUE |
| RC-PROJ-001 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-PROJ-002 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P2'] |
| RC-PROJ-003 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-PROJ-004 | **OPTIONAL_SELECTED** | `engagement_type == "AMS"` → FALSE | `fixed_price == TRUE` → FALSE | `fixed_price == FALSE` → TRUE | optional_if → TRUE: fixed_price == FALSE |
| RC-TECH-001 | **MANDATORY** | `platform == "Acumatica" or platform == "BeBanking"` → FALSE | `platform contains "Oracle" and (engagement_type == "Implementation" or engagement_type == "AMS")` → TRUE | — | mandatory_if → TRUE: platform contains "Oracle" and (engagement_type == "Impleme |
| RC-TECH-002 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-003 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-004 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-005 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2', 'P3'] |
| RC-TECH-006 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-007 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-008 | **DEFAULT_EXCLUDED** | `engagement_type == "AMS"` → FALSE | `feature_licensing_confirmed == FALSE and engagement_type == "Implementation"` → FALSE | `feature_licensing_confirmed == TRUE` → FALSE | No selection condition resolved to TRUE (conditions unresolvable or FALSE) |
| RC-TECH-009 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P1', 'P2'] |
| RC-TECH-010 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P13'] |
| RC-TECH-011 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P4', 'P1', 'P2'] |
| RC-TECH-012 | PATTERN_EXCLUDED | — | — | — | Pattern P7 not in applicable patterns ['P3', 'P6', 'P13'] |

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
