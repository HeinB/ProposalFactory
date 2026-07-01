---
document_id: SELECTED-RISK-REGISTER-REG-HCM-P3
title: "Selected Proposal Risk Register — REG-HCM-P3"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
tender_id: "REG-HCM-P3"
pattern: "P3"
platform: "Oracle HCM Cloud"
engagement_type: "Implementation"
---

# Selected Proposal Risk Register — REG-HCM-P3

**Generated:** 2026-06-29 07:10  
**Engine:** Risk Selection Engine v1.0 | AREL V1.0  
**Tender:** REG-HCM-P3 | Pattern: P3 (HCM + Payroll Integration)  
**Platform:** Oracle HCM Cloud | Engagement: Implementation  

---

## Summary

| Metric | Count |
|---|---|
| Risks evaluated | 40 |
| **Selected (total)** | **15** |
| — Mandatory | 15 |
| — Optional (selected) | 0 |
| Excluded (excluded_if TRUE) | 4 |
| Pattern-excluded | 15 |
| Default-excluded | 6 |
| Validation violations | 0 |

---

## Selected Risks

Sorted by assembly priority (Critical → High → Standard), then rating.

### RC-CLIENT-007 — Cross-Functional Alignment on Design Frameworks **[MANDATORY]** [CRITICAL]

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-007 |
| **Category** | RC-CLIENT — Client Risk |
| **Rating** | CRITICAL |
| **Likelihood × Impact** | High × High |
| **Assembly priority** | Critical |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation"` |
| **Owner** | Solution Architect |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Related assumptions** | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008, HCM-CHG-001, HCM-CHG-002, HCM-CHG-003, HCM-CHG-004 |
| **Applicable patterns** | P1, P2, P3 |

> Different client business units (HR, Finance, Payroll, IT) have conflicting views on how core HCM frameworks (job architecture, grade structure, position management approach) should be designed. Without a single client-side decision-maker with authority to resolve cross-functional disagreements, design workshops stall, rework cycles increase, and the project timeline expands.

### RC-DATA-001 — Legacy HR Data Quality Causes Migration Delays **[MANDATORY]** [CRITICAL]

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-001 |
| **Category** | RC-DATA — Data Risk |
| **Rating** | CRITICAL |
| **Likelihood × Impact** | High × High |
| **Assembly priority** | Critical |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation"` |
| **Owner** | Functional Consultant |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | HCM-DAT-001, HCM-DAT-002, HCM-DAT-003, HCM-DAT-004, HCM-DAT-005, HCM-DAT-006, HCM-DAT-007, HCM-DAT-008, HCM-DAT-009 |
| **Applicable patterns** | P1, P2, P3 |

> The client's legacy HR records contain structural inconsistencies, missing mandatory fields, duplicate employee records, or data that cannot be mapped to the Oracle HCM data model. Poor source data quality causes repeated extract-transform-load cycles, delays the data migration milestone, and can push back UAT and go-live.

### RC-DATA-003 — HCM Data Quality Produces Invalid Payroll Input **[MANDATORY]** [CRITICAL]

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-003 |
| **Category** | RC-DATA — Data Risk |
| **Rating** | CRITICAL |
| **Likelihood × Impact** | High × High |
| **Assembly priority** | Critical |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: payroll_integration == TRUE and platform contains "Oracle HCM" |
| **Source rule** | mandatory_if: `payroll_integration = TRUE AND platform CONTAINS "Oracle HCM"` |
| **Owner** | Integration Lead |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | HCM-DAT-001, HCM-DAT-002, HCM-DAT-003, HCM-DAT-004, HCM-DAT-005, OIC-MAP-001, OIC-MAP-002, OIC-MAP-003 |
| **Applicable patterns** | P1, P2, P3 |

> Employee master data migrated from the legacy system into Oracle HCM contains errors (incorrect cost centres, missing job codes, duplicate employee numbers) that propagate through the OIC integration into the payroll system, producing invalid payroll runs. Payroll errors are high-impact: they affect employee pay and carry regulatory risk.

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

### RC-PROJ-003 — Organisational Design Decisions Made Late **[MANDATORY]** [CRITICAL]

| Field | Value |
|---|---|
| **Risk ID** | RC-PROJ-003 |
| **Category** | RC-PROJ — Project Risk |
| **Rating** | CRITICAL |
| **Likelihood × Impact** | High × High |
| **Assembly priority** | Critical |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation"` |
| **Owner** | Solution Architect |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Related assumptions** | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008 |
| **Applicable patterns** | P1, P2, P3 |

> The client's organisational design (legal entity structure, business unit hierarchy, location structure, and job architecture) is not finalised before the HCM Scoping and Design phase begins. Oracle HCM Core HR configuration is built on top of the organisational structure; late org design decisions invalidate configuration already completed, requiring rework across multiple modules.

### RC-INT-001 — Payroll Integration Timeline Not Aligned to HCM Go-Live **[MANDATORY]** [HIGH]

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-001 |
| **Category** | RC-INT — Integration Risk |
| **Rating** | HIGH |
| **Likelihood × Impact** | Medium × High |
| **Assembly priority** | Critical |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: payroll_integration == TRUE and platform contains "Oracle HCM" |
| **Source rule** | mandatory_if: `payroll_integration = TRUE AND platform CONTAINS "Oracle HCM"` |
| **Owner** | Integration Lead |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | HCM-3PT-001, HCM-3PT-002, HCM-3PT-003, HCM-3PT-004, HCM-3PT-005, HCM-3PT-006, OIC-DES-001, OIC-DES-002, OIC-DES-003, OIC-END-001, OIC-END-002 |
| **Applicable patterns** | P1, P2, P3 |

> The third-party payroll system integration is not completed and tested in time to support the HCM go-live date. If payroll integration is not ready, employees cannot be paid from the live system, forcing a delay to go-live or a parallel payroll run. Payroll go-live delays carry significant regulatory and reputational risk.

### RC-INT-005 — Integration Schedule Not Aligned to Payroll Cutoff **[MANDATORY]** [HIGH]

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-005 |
| **Category** | RC-INT — Integration Risk |
| **Rating** | HIGH |
| **Likelihood × Impact** | Medium × High |
| **Assembly priority** | Critical |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: payroll_integration == TRUE and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `payroll_integration = TRUE AND engagement_type = "Implementation"` |
| **Owner** | Integration Lead |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | OIC-DES-001, OIC-DES-002, OIC-DES-003, HCM-3PT-001, HCM-3PT-002, HCM-CUT-001, HCM-CUT-002, HCM-CUT-003 |
| **Applicable patterns** | P1, P2, P3, P6 |

> The integration testing and cutover plan does not account for the fixed window imposed by the client's payroll processing cycle. Payroll cutoff dates are immovable; if integration testing extends past the cutoff window, the first live payroll run must be executed with the legacy system while the new integration is still being tested, creating a dual-run period that is operationally complex.

### RC-PROJ-001 — Module Design Not Signed Off Before Build Begins **[MANDATORY]** [HIGH]

| Field | Value |
|---|---|
| **Risk ID** | RC-PROJ-001 |
| **Category** | RC-PROJ — Project Risk |
| **Rating** | HIGH |
| **Likelihood × Impact** | Medium × High |
| **Assembly priority** | Critical |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: platform contains "Oracle HCM" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation"` |
| **Owner** | Project Manager |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Related assumptions** | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008 |
| **Applicable patterns** | P1, P2, P3 |

> APPSolve begins building and configuring HCM modules before client stakeholders have signed off the functional design. Build based on unapproved design produces rework when the client revises decisions mid-configuration, consuming contingency and extending the timeline.

### RC-TECH-012 — Annual SA Legislative Change Not Reflected in Integrations **[MANDATORY]** [CRITICAL]

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-012 |
| **Category** | RC-TECH — Technical Risk |
| **Rating** | CRITICAL |
| **Likelihood × Impact** | High × High |
| **Assembly priority** | High |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: country == "ZA" and payroll_integration == TRUE |
| **Source rule** | mandatory_if: `country = "ZA" AND payroll_integration = TRUE` |
| **Owner** | Integration Lead |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12, S-73 |
| **Related assumptions** | OIC-DES-001, AMS-REL-001 |
| **Applicable patterns** | P3, P6, P13 |

> Annual South African legislative changes (National Budget tax table updates, UIF rate changes, SDL rate changes) require updates to payroll integration field mappings and transformation logic. If the integration is not updated before the legislative effective date (typically 1 March), the integration will produce non-compliant payroll output.

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

### RC-COMP-001 — POPIA Non-Compliance in HR or Payroll Data Handling **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-COMP-001 |
| **Category** | RC-COMP — Compliance Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Medium × Medium |
| **Assembly priority** | High |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: country == "ZA" and (personal_data_in_scope == TRUE or payroll_integration == TRUE) |
| **Source rule** | mandatory_if: `country = "ZA" AND (personal_data_in_scope = TRUE OR payroll_integration = TRUE)` |
| **Owner** | Solution Architect |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | OIC-SEC-001, OIC-SEC-002, OIC-SEC-003, OIC-SEC-004, OIC-SEC-005, OIC-SEC-006, BB-DAT-006, HCM-SEC-001, HCM-SEC-002, HCM-SEC-003, HCM-SEC-004, HCM-SEC-005, HCM-SEC-006, HCM-SEC-007, HCM-SEC-008 |
| **Applicable patterns** | P1, P2, P3, P12, P13 |

> HR and payroll data contains personal information regulated under POPIA. APPSolve processes this data as an operator (data processor) on behalf of the client (responsible party). Non-compliance risks arise from: inadequate data minimisation, unlawful cross-border data transfer, uncontrolled access to employee records, or integration patterns that expose personal data to non-compliant endpoints.

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

### RC-INT-004 — Payroll API Version Changes Post-Go-Live **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-004 |
| **Category** | RC-INT — Integration Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Medium × Medium |
| **Assembly priority** | Standard |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: payroll_integration == TRUE and (engagement_type == "Implementation" or engagement_type == "AMS") |
| **Source rule** | mandatory_if: `payroll_integration = TRUE AND (engagement_type = "Implementation" OR engagement_type = "AMS")` |
| **Owner** | Integration Lead |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12, S-73 |
| **Related assumptions** | OIC-DES-001, OIC-DES-002, AMS-REL-001 |
| **Applicable patterns** | P3, P6, P13 |

> The third-party payroll system vendor releases an API version update that is incompatible with the OIC integration deployed at go-live. Without advance notice of the breaking change, the integration fails at runtime, interrupting the payroll data feed.

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

### RC-TECH-001 — Quarterly SaaS Update Breaks Configured Functionality **[MANDATORY]** [LOW]

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-001 |
| **Category** | RC-TECH — Technical Risk |
| **Rating** | LOW |
| **Likelihood × Impact** | Low × Medium |
| **Assembly priority** | Standard |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: platform contains "Oracle" and (engagement_type == "Implementation" or engagement_type == "AMS") |
| **Source rule** | mandatory_if: `platform CONTAINS "Oracle" AND (engagement_type = "Implementation" OR engagement_type = "AMS")` |
| **Owner** | Solution Architect |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12, S-73 |
| **Related assumptions** | HCM-ENV-004, AMS-REL-001 |
| **Applicable patterns** | P1, P2, P3, P4, P5, P6, P7, P8, P9, P13 |

> Oracle's quarterly SaaS update cycle introduces changes to the platform that are incompatible with configuration or integrations delivered by APPSolve. While Oracle provides advance notice of breaking changes, the client is responsible for regression testing and confirming compatibility before each update is applied to production.

---

## Excluded Risks (excluded_if TRUE)

| Risk ID | Title | Rating | Excluded If |
|---|---|---|---|
| RC-TECH-003 | Absence Rules Complexity Exceeds Standard Scope | CRITICAL | `NOT modules CONTAINS "Oracle WFM"` |
| RC-DATA-004 | Biometric Enrolment Data Does Not Match HR Records | HIGH | `NOT modules CONTAINS "Oracle WFM"` |
| RC-TECH-004 | Time and Labour Rules Complexity Exceeds Estimate | MEDIUM | `NOT modules CONTAINS "Oracle WFM"` |
| RC-TECH-005 | BCEA Overtime Calculation Requires Additional Config | MEDIUM | `country != "ZA" OR NOT modules CONTAINS "Oracle WFM"` |

---

## Pattern-Excluded Risks

The following risks are not applicable to pattern P3 (HCM + Payroll Integration).

| Risk ID | Title | Applicable Patterns |
|---|---|---|
| RC-CLIENT-003 | Onboarding Task and Workflow Ownership Not Defined | P1, P2, P4 |
| RC-CLIENT-004 | Learning Catalog Not Ready at System Go-Live | P5, P1, P2 |
| RC-CLIENT-005 | Performance Rating Data Unavailable for Compensation Cycle | P1, P2 |
| RC-CLIENT-006 | Knowledge Base Content Ownership Undefined | P13 |
| RC-COMM-001 | Analytics Expectations Misaligned With Platform Capability | P1, P2 |
| RC-COMM-002 | Oracle HR Help Desk Conflated With Oracle Service Cloud | P13 |
| RC-DATA-002 | Client Content Format Incompatible With Platform | P5, P1, P2 |
| RC-DATA-005 | Demand/Scheduling Data Unavailable | P1, P2 |
| RC-PROJ-002 | Upstream Phase Not Stable When Dependent Phase Begins | P2 |
| RC-TECH-002 | SETA/WSP/ATR Extract Complexity | P1, P2 |
| RC-TECH-006 | OAX Licensing Not Confirmed Before Commitment | P1, P2 |
| RC-TECH-007 | OAX Data Model Not Aligned to HCM Configuration | P1, P2 |
| RC-TECH-009 | ODA Scope Added Without Separate License Confirmation | P1, P2 |
| RC-TECH-010 | Digital Channel Complexity Beyond Standard Configuration | P13 |
| RC-TECH-011 | Career Site Design Complexity Exceeds Standard Scope | P4, P1, P2 |

---

## Default-Excluded Risks

Risks that are pattern-applicable but where no AREL condition resolved to TRUE.
These risks may become MANDATORY or OPTIONAL if additional RSE extension fields
are provided (e.g., oax_in_scope, integration_count, personal_data_in_scope).

| Risk ID | Title | Rating | Unresolved Conditions |
|---|---|---|---|
| RC-TECH-008 | Oracle Product Licensing for Dependent Features Not Confirmed | CRITICAL | mandatory_if: `feature_licensing_confirmed = FALSE AND engagement_type = "Implementation"` | optional_if: `feature_licensing_confirmed = TRUE` |
| RC-INT-003 | Third-Party API Unavailable at Integration Build Start | HIGH | mandatory_if: `platform CONTAINS "OIC" AND third_party_api = TRUE` | optional_if: `platform CONTAINS "OIC" AND third_party_api = FALSE` |
| RC-INT-006 | Integration Field Mapping Errors Produce Incorrect Data | HIGH | mandatory_if: `platform CONTAINS "OIC"` |
| RC-INT-002 | Third-Party Integration Scope Underestimated | MEDIUM | mandatory_if: `integration_count > 2` | optional_if: `integration_count <= 2` |
| RC-COMM-003 | Integration Method Commitment in Tender Creates Exposure | MEDIUM | mandatory_if: `integration_method_prescribed_in_tender = TRUE` | optional_if: `integration_method_prescribed_in_tender = FALSE` |
| RC-INT-007 | Bespoke Payroll Mapping Beyond Standard Patterns | MEDIUM | mandatory_if: `payroll_integration = TRUE AND (platform = "Acumatica" OR (platform CONTAINS "Oracle" AND payroll_provider = "non-standard"))` |

---

*Generated by RSE v1.0 — 2026-06-29 07:10*
