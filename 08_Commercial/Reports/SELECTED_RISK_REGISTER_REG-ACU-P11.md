---
document_id: SELECTED-RISK-REGISTER-REG-ACU-P11
title: "Selected Proposal Risk Register — REG-ACU-P11"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
tender_id: "REG-ACU-P11"
pattern: "P11"
platform: "Acumatica"
engagement_type: "Implementation"
---

# Selected Proposal Risk Register — REG-ACU-P11

**Generated:** 2026-06-29 07:10  
**Engine:** Risk Selection Engine v1.0 | AREL V1.0  
**Tender:** REG-ACU-P11 | Pattern: P11 (Acumatica)  
**Platform:** Acumatica | Engagement: Implementation  

---

## Summary

| Metric | Count |
|---|---|
| Risks evaluated | 40 |
| **Selected (total)** | **4** |
| — Mandatory | 4 |
| — Optional (selected) | 0 |
| Excluded (excluded_if TRUE) | 0 |
| Pattern-excluded | 31 |
| Default-excluded | 5 |
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

### RC-CLIENT-001 — Super-User Availability Insufficient During UAT **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-001 |
| **Category** | RC-CLIENT — Client Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Medium × Medium |
| **Assembly priority** | High |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `engagement_type = "Implementation"` |
| **Owner** | Project Manager |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | HCM-TST-001, HCM-TST-002, HCM-TST-003, HCM-TST-004, HCM-TST-005, HCM-TST-006, HCM-TST-007, HCM-TST-008, ERP-TST-001, ERP-TST-002, ERP-TST-003, ERP-TST-004, ERP-TST-005, ERP-TST-006 |
| **Applicable patterns** | P1, P2, P3, P4, P5, P6, P7, P8, P9, P11 |

> The client's business super-users (process owners who validate system behaviour during UAT) are not available for the planned UAT period due to competing business priorities. Insufficient super-user participation causes incomplete test coverage, deferred defect resolution, and delayed UAT sign-off.

### RC-CLIENT-002 — Client Prerequisite Systems or Accounts Not Available **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-002 |
| **Category** | RC-CLIENT — Client Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Low × High |
| **Assembly priority** | Standard |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `engagement_type = "Implementation"` |
| **Owner** | Project Manager |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | HCM-CUS-001, HCM-CUS-002, HCM-CUS-003, HCM-CUS-004, HCM-CUS-005, ERP-CUS-001, ERP-CUS-002, ERP-CUS-003 |
| **Applicable patterns** | P1, P2, P3, P7, P8, P9, P11 |

> The client's prerequisite systems (Oracle tenant provisioned, identity provider configured, network access granted, SSO established) are not ready at the time APPSolve begins the implementation. Missing prerequisites block the Configuration workstream from starting and consume project time while awaiting client action.

### RC-PROJ-004 — Configuration Milestone Changed After Sign-Off **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-PROJ-004 |
| **Category** | RC-PROJ — Project Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Low × High |
| **Assembly priority** | Standard |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: fixed_price == TRUE |
| **Source rule** | mandatory_if: `fixed_price = TRUE` |
| **Owner** | Project Manager |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Related assumptions** | HCM-ORG-001, ERP-GEN-001, ERP-GEN-002 |
| **Applicable patterns** | P1, P2, P3, P7, P8, P9, P11 |

> After the client has signed off a configuration milestone, the client requests changes to that milestone, requiring re-work of completed build artefacts. In fixed-price engagements, this is the primary source of margin erosion if not managed through formal change control.

---

## Excluded Risks (excluded_if TRUE)

| Risk ID | Title | Rating | Excluded If |
|---|---|---|---|

---

## Pattern-Excluded Risks

The following risks are not applicable to pattern P11 (Acumatica).

| Risk ID | Title | Applicable Patterns |
|---|---|---|
| RC-CLIENT-003 | Onboarding Task and Workflow Ownership Not Defined | P1, P2, P4 |
| RC-CLIENT-004 | Learning Catalog Not Ready at System Go-Live | P5, P1, P2 |
| RC-CLIENT-005 | Performance Rating Data Unavailable for Compensation Cycle | P1, P2 |
| RC-CLIENT-006 | Knowledge Base Content Ownership Undefined | P13 |
| RC-CLIENT-007 | Cross-Functional Alignment on Design Frameworks | P1, P2, P3 |
| RC-COMM-001 | Analytics Expectations Misaligned With Platform Capability | P1, P2 |
| RC-COMM-002 | Oracle HR Help Desk Conflated With Oracle Service Cloud | P13 |
| RC-COMP-001 | POPIA Non-Compliance in HR or Payroll Data Handling | P1, P2, P3, P12, P13 |
| RC-DATA-001 | Legacy HR Data Quality Causes Migration Delays | P1, P2, P3 |
| RC-DATA-002 | Client Content Format Incompatible With Platform | P5, P1, P2 |
| RC-DATA-003 | HCM Data Quality Produces Invalid Payroll Input | P1, P2, P3 |
| RC-DATA-004 | Biometric Enrolment Data Does Not Match HR Records | P1, P2, P3 |
| RC-DATA-005 | Demand/Scheduling Data Unavailable | P1, P2 |
| RC-INT-001 | Payroll Integration Timeline Not Aligned to HCM Go-Live | P1, P2, P3 |
| RC-INT-004 | Payroll API Version Changes Post-Go-Live | P3, P6, P13 |
| RC-INT-005 | Integration Schedule Not Aligned to Payroll Cutoff | P1, P2, P3, P6 |
| RC-PROJ-001 | Module Design Not Signed Off Before Build Begins | P1, P2, P3 |
| RC-PROJ-002 | Upstream Phase Not Stable When Dependent Phase Begins | P2 |
| RC-PROJ-003 | Organisational Design Decisions Made Late | P1, P2, P3 |
| RC-TECH-001 | Quarterly SaaS Update Breaks Configured Functionality | P1, P2, P3, P4, P5, P6, P7, P8, P9, P13 |
| RC-TECH-002 | SETA/WSP/ATR Extract Complexity | P1, P2 |
| RC-TECH-003 | Absence Rules Complexity Exceeds Standard Scope | P1, P2, P3 |
| RC-TECH-004 | Time and Labour Rules Complexity Exceeds Estimate | P1, P2, P3 |
| RC-TECH-005 | BCEA Overtime Calculation Requires Additional Config | P1, P2, P3 |
| RC-TECH-006 | OAX Licensing Not Confirmed Before Commitment | P1, P2 |
| RC-TECH-007 | OAX Data Model Not Aligned to HCM Configuration | P1, P2 |
| RC-TECH-008 | Oracle Product Licensing for Dependent Features Not Confirmed | P1, P2, P3, P7, P8, P9 |
| RC-TECH-009 | ODA Scope Added Without Separate License Confirmation | P1, P2 |
| RC-TECH-010 | Digital Channel Complexity Beyond Standard Configuration | P13 |
| RC-TECH-011 | Career Site Design Complexity Exceeds Standard Scope | P4, P1, P2 |
| RC-TECH-012 | Annual SA Legislative Change Not Reflected in Integrations | P3, P6, P13 |

---

## Default-Excluded Risks

Risks that are pattern-applicable but where no AREL condition resolved to TRUE.
These risks may become MANDATORY or OPTIONAL if additional RSE extension fields
are provided (e.g., oax_in_scope, integration_count, personal_data_in_scope).

| Risk ID | Title | Rating | Unresolved Conditions |
|---|---|---|---|
| RC-INT-003 | Third-Party API Unavailable at Integration Build Start | HIGH | mandatory_if: `platform CONTAINS "OIC" AND third_party_api = TRUE` | optional_if: `platform CONTAINS "OIC" AND third_party_api = FALSE` |
| RC-INT-006 | Integration Field Mapping Errors Produce Incorrect Data | HIGH | mandatory_if: `platform CONTAINS "OIC"` |
| RC-INT-002 | Third-Party Integration Scope Underestimated | MEDIUM | mandatory_if: `integration_count > 2` | optional_if: `integration_count <= 2` |
| RC-COMM-003 | Integration Method Commitment in Tender Creates Exposure | MEDIUM | mandatory_if: `integration_method_prescribed_in_tender = TRUE` | optional_if: `integration_method_prescribed_in_tender = FALSE` |
| RC-INT-007 | Bespoke Payroll Mapping Beyond Standard Patterns | MEDIUM | mandatory_if: `payroll_integration = TRUE AND (platform = "Acumatica" OR (platform CONTAINS "Oracle" AND payroll_provider = "non-standard"))` |

---

*Generated by RSE v1.0 — 2026-06-29 07:10*
