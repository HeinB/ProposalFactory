---
document_id: SELECTED-RISK-REGISTER-REG-BEB-P13
title: "Selected Proposal Risk Register — REG-BEB-P13"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
tender_id: "REG-BEB-P13"
pattern: "P13"
platform: "BeBanking"
engagement_type: "Implementation"
---

# Selected Proposal Risk Register — REG-BEB-P13

**Generated:** 2026-06-29 07:10  
**Engine:** Risk Selection Engine v1.0 | AREL V1.0  
**Tender:** REG-BEB-P13 | Pattern: P13 (AMS)  
**Platform:** BeBanking | Engagement: Implementation  

---

## Summary

| Metric | Count |
|---|---|
| Risks evaluated | 40 |
| **Selected (total)** | **1** |
| — Mandatory | 1 |
| — Optional (selected) | 0 |
| Excluded (excluded_if TRUE) | 5 |
| Pattern-excluded | 32 |
| Default-excluded | 2 |
| Validation violations | 0 |

---

## Selected Risks

Sorted by assembly priority (Critical → High → Standard), then rating.

### RC-OPS-001 — First Live Operational Cycle High-Stakes Risk **[MANDATORY]** [CRITICAL]

| Field | Value |
|---|---|
| **Risk ID** | RC-OPS-001 |
| **Category** | RC-OPS — Operational Risk |
| **Rating** | CRITICAL |
| **Likelihood × Impact** | High × High |
| **Assembly priority** | Critical |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: TRUE |
| **Source rule** | mandatory_if: `TRUE` |
| **Owner** | Project Manager |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-71, S-72, S-12 |
| **Related assumptions** | HCM-CUT-001, HCM-CUT-002, HCM-CUT-003, HCM-CUT-004, HCM-CUT-005, HCM-CUT-006, HCM-CUT-007, HCM-CUT-008, HCM-HYP-001, HCM-HYP-002, HCM-HYP-003, HCM-HYP-004, HCM-HYP-005, AMS-SLA-001, AMS-SLA-002, AMS-SLA-005, ERP-CUT-001, ERP-CUT-002, ERP-CUT-003, ERP-CUT-004, ERP-CUT-005, ERP-HYP-001, ERP-HYP-002, ERP-HYP-003, ERP-HYP-004 |
| **Applicable patterns** | P1, P2, P3, P4, P5, P7, P8, P9, P11, P13 |

> The first live operational cycle (first payroll run, first month-end close, first HR report submission) on the new system is the highest-risk event in any implementation. Unforeseen system behaviour, data quality issues, or process gaps that were not surfaced during UAT manifest under real-world conditions, with direct impact on employees, finances, or regulatory reporting.

---

## Excluded Risks (excluded_if TRUE)

| Risk ID | Title | Rating | Excluded If |
|---|---|---|---|
| RC-COMM-002 | Oracle HR Help Desk Conflated With Oracle Service Cloud | CRITICAL | `NOT help_desk_in_scope = TRUE` |
| RC-CLIENT-006 | Knowledge Base Content Ownership Undefined | MEDIUM | `engagement_type != "AMS"` |
| RC-INT-004 | Payroll API Version Changes Post-Go-Live | MEDIUM | `NOT payroll_integration = TRUE` |
| RC-TECH-001 | Quarterly SaaS Update Breaks Configured Functionality | LOW | `platform = "Acumatica" OR platform = "BeBanking"` |
| RC-TECH-010 | Digital Channel Complexity Beyond Standard Configuration | LOW | `engagement_type != "AMS"` |

---

## Pattern-Excluded Risks

The following risks are not applicable to pattern P13 (AMS).

| Risk ID | Title | Applicable Patterns |
|---|---|---|
| RC-CLIENT-001 | Super-User Availability Insufficient During UAT | P1, P2, P3, P4, P5, P6, P7, P8, P9, P11 |
| RC-CLIENT-002 | Client Prerequisite Systems or Accounts Not Available | P1, P2, P3, P7, P8, P9, P11 |
| RC-CLIENT-003 | Onboarding Task and Workflow Ownership Not Defined | P1, P2, P4 |
| RC-CLIENT-004 | Learning Catalog Not Ready at System Go-Live | P5, P1, P2 |
| RC-CLIENT-005 | Performance Rating Data Unavailable for Compensation Cycle | P1, P2 |
| RC-CLIENT-007 | Cross-Functional Alignment on Design Frameworks | P1, P2, P3 |
| RC-COMM-001 | Analytics Expectations Misaligned With Platform Capability | P1, P2 |
| RC-COMM-003 | Integration Method Commitment in Tender Creates Exposure | P3, P6, P11 |
| RC-DATA-001 | Legacy HR Data Quality Causes Migration Delays | P1, P2, P3 |
| RC-DATA-002 | Client Content Format Incompatible With Platform | P5, P1, P2 |
| RC-DATA-003 | HCM Data Quality Produces Invalid Payroll Input | P1, P2, P3 |
| RC-DATA-004 | Biometric Enrolment Data Does Not Match HR Records | P1, P2, P3 |
| RC-DATA-005 | Demand/Scheduling Data Unavailable | P1, P2 |
| RC-INT-001 | Payroll Integration Timeline Not Aligned to HCM Go-Live | P1, P2, P3 |
| RC-INT-002 | Third-Party Integration Scope Underestimated | P1, P2, P3, P6, P7, P8, P11 |
| RC-INT-003 | Third-Party API Unavailable at Integration Build Start | P3, P6, P7, P8, P9, P11 |
| RC-INT-005 | Integration Schedule Not Aligned to Payroll Cutoff | P1, P2, P3, P6 |
| RC-INT-006 | Integration Field Mapping Errors Produce Incorrect Data | P3, P6, P7, P8, P9, P11 |
| RC-INT-007 | Bespoke Payroll Mapping Beyond Standard Patterns | P3, P11 |
| RC-PROJ-001 | Module Design Not Signed Off Before Build Begins | P1, P2, P3 |
| RC-PROJ-002 | Upstream Phase Not Stable When Dependent Phase Begins | P2 |
| RC-PROJ-003 | Organisational Design Decisions Made Late | P1, P2, P3 |
| RC-PROJ-004 | Configuration Milestone Changed After Sign-Off | P1, P2, P3, P7, P8, P9, P11 |
| RC-TECH-002 | SETA/WSP/ATR Extract Complexity | P1, P2 |
| RC-TECH-003 | Absence Rules Complexity Exceeds Standard Scope | P1, P2, P3 |
| RC-TECH-004 | Time and Labour Rules Complexity Exceeds Estimate | P1, P2, P3 |
| RC-TECH-005 | BCEA Overtime Calculation Requires Additional Config | P1, P2, P3 |
| RC-TECH-006 | OAX Licensing Not Confirmed Before Commitment | P1, P2 |
| RC-TECH-007 | OAX Data Model Not Aligned to HCM Configuration | P1, P2 |
| RC-TECH-008 | Oracle Product Licensing for Dependent Features Not Confirmed | P1, P2, P3, P7, P8, P9 |
| RC-TECH-009 | ODA Scope Added Without Separate License Confirmation | P1, P2 |
| RC-TECH-011 | Career Site Design Complexity Exceeds Standard Scope | P4, P1, P2 |

---

## Default-Excluded Risks

Risks that are pattern-applicable but where no AREL condition resolved to TRUE.
These risks may become MANDATORY or OPTIONAL if additional RSE extension fields
are provided (e.g., oax_in_scope, integration_count, personal_data_in_scope).

| Risk ID | Title | Rating | Unresolved Conditions |
|---|---|---|---|
| RC-TECH-012 | Annual SA Legislative Change Not Reflected in Integrations | CRITICAL | mandatory_if: `country = "ZA" AND payroll_integration = TRUE` |
| RC-COMP-001 | POPIA Non-Compliance in HR or Payroll Data Handling | MEDIUM | mandatory_if: `country = "ZA" AND (personal_data_in_scope = TRUE OR payroll_integration = TRUE)` | optional_if: `country != "ZA"` |

---

*Generated by RSE v1.0 — 2026-06-29 07:10*
