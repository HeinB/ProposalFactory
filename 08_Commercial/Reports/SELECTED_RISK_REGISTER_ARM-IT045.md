---
document_id: SELECTED-RISK-REGISTER-ARM-IT045
title: "Selected Proposal Risk Register — ARM-IT045"
version: "1.0"
status: "GENERATED"
generated: "2026-06-29 07:10"
engine: "RSE v1.0 / AREL V1.0"
tender_id: "ARM-IT045"
pattern: "P1"
platform: "Oracle HCM Cloud"
engagement_type: "Implementation"
---

# Selected Proposal Risk Register — ARM-IT045

**Generated:** 2026-06-29 07:10  
**Engine:** Risk Selection Engine v1.0 | AREL V1.0  
**Tender:** ARM-IT045 | Pattern: P1 (HCM Full Suite Single)  
**Platform:** Oracle HCM Cloud | Engagement: Implementation  

---

## Summary

| Metric | Count |
|---|---|
| Risks evaluated | 40 |
| **Selected (total)** | **14** |
| — Mandatory | 13 |
| — Optional (selected) | 1 |
| Excluded (excluded_if TRUE) | 8 |
| Pattern-excluded | 10 |
| Default-excluded | 8 |
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

### RC-DATA-003 — HCM Data Quality Produces Invalid Payroll Input **[OPTIONAL]** [CRITICAL]

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-003 |
| **Category** | RC-DATA — Data Risk |
| **Rating** | CRITICAL |
| **Likelihood × Impact** | High × High |
| **Assembly priority** | Critical |
| **Selection status** | OPTIONAL_SELECTED |
| **Why selected** | optional_if → TRUE: payroll_integration == FALSE and platform contains "Oracle HCM" |
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

### RC-CLIENT-004 — Learning Catalog Not Ready at System Go-Live **[MANDATORY]** [CRITICAL]

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-004 |
| **Category** | RC-CLIENT — Client Risk |
| **Rating** | CRITICAL |
| **Likelihood × Impact** | High × High |
| **Assembly priority** | High |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: modules contains "Oracle Learning" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `modules CONTAINS "Oracle Learning" AND engagement_type = "Implementation"` |
| **Owner** | Functional Consultant |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | LRN-CON-001, LRN-CON-002, LRN-CON-003, LRN-CON-004, LRN-CON-005, LRN-DAT-001, LRN-DAT-002, LRN-DAT-003, LRN-DAT-004 |
| **Applicable patterns** | P5, P1, P2 |

> The client's learning catalog (course library, learning items, specialisations, required training assignments) is not loaded or ready at the Oracle Learning go-live date. A learning system without content cannot be used by employees, undermining the business case for the implementation.

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

### RC-CLIENT-003 — Onboarding Task and Workflow Ownership Not Defined **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-003 |
| **Category** | RC-CLIENT — Client Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Medium × Medium |
| **Assembly priority** | Standard |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: modules contains "Oracle Recruiting" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `modules CONTAINS "Oracle Recruiting" AND engagement_type = "Implementation"` |
| **Owner** | Functional Consultant |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | HCM-CUS-001, HCM-CUS-002, HCM-CUS-003, HCM-CUS-004 |
| **Applicable patterns** | P1, P2, P4 |

> The business ownership of onboarding tasks, document checklists, and workflow approvals is not defined before Oracle Onboarding is configured. Without confirmed ownership, APPSolve cannot configure approval routing and task assignment, causing configuration to proceed with placeholder owners that must be reworked later.

### RC-DATA-002 — Client Content Format Incompatible With Platform **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-002 |
| **Category** | RC-DATA — Data Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Medium × Medium |
| **Assembly priority** | Standard |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: modules contains "Oracle Learning" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `modules CONTAINS "Oracle Learning" AND engagement_type = "Implementation"` |
| **Owner** | Functional Consultant |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | LRN-DAT-001, LRN-DAT-002, LRN-DAT-003, LRN-DAT-004 |
| **Applicable patterns** | P5, P1, P2 |

> The client has existing learning content (SCORM packages, videos, documents) in formats that are not natively supported by Oracle Learning Cloud. Content conversion or re-authoring is required, consuming time and budget outside the standard scope.

### RC-TECH-002 — SETA/WSP/ATR Extract Complexity **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-002 |
| **Category** | RC-TECH — Technical Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Medium × Medium |
| **Assembly priority** | Standard |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: country == "ZA" and modules contains "Oracle HCM" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `country = "ZA" AND modules CONTAINS "Oracle HCM" AND engagement_type = "Implementation"` |
| **Owner** | Functional Consultant |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Related assumptions** | HCM-RPT-001, HCM-RPT-002, HCM-RPT-003, HCM-RPT-004, HCM-RPT-005, HCM-RPT-006 |
| **Applicable patterns** | P1, P2 |

> South African SETA (Workplace Skills Plan and Annual Training Report) reporting requirements impose complex data extraction and transformation on the Oracle HCM Learning and HR data model. The extract logic often exceeds Oracle's standard reporting templates, requiring custom reporting configuration that is beyond the standard HCM implementation scope.

### RC-TECH-011 — Career Site Design Complexity Exceeds Standard Scope **[MANDATORY]** [MEDIUM]

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-011 |
| **Category** | RC-TECH — Technical Risk |
| **Rating** | MEDIUM |
| **Likelihood × Impact** | Medium × Medium |
| **Assembly priority** | Standard |
| **Selection status** | MANDATORY |
| **Why selected** | mandatory_if → TRUE: modules contains "Oracle Recruiting" and engagement_type == "Implementation" |
| **Source rule** | mandatory_if: `modules CONTAINS "Oracle Recruiting" AND engagement_type = "Implementation"` |
| **Owner** | Functional Consultant |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Related assumptions** | REC-SIT-001, REC-SIT-002, REC-SIT-003, REC-SIT-004, REC-SIT-005 |
| **Applicable patterns** | P4, P1, P2 |

> The client requests a career site design (branding, layout, custom pages, interactive elements) that exceeds Oracle's standard Career Site Builder capability. Custom HTML/CSS, animated components, or multi-page microsites require development effort beyond standard configuration scope per REC-SIT-002.

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
| RC-INT-001 | Payroll Integration Timeline Not Aligned to HCM Go-Live | HIGH | `engagement_type = "AMS" OR payroll_integration = FALSE` |
| RC-INT-005 | Integration Schedule Not Aligned to Payroll Cutoff | HIGH | `engagement_type = "AMS" OR payroll_integration = FALSE` |
| RC-DATA-004 | Biometric Enrolment Data Does Not Match HR Records | HIGH | `NOT modules CONTAINS "Oracle WFM"` |
| RC-CLIENT-005 | Performance Rating Data Unavailable for Compensation Cycle | MEDIUM | `NOT modules CONTAINS "Oracle Compensation"` |
| RC-TECH-004 | Time and Labour Rules Complexity Exceeds Estimate | MEDIUM | `NOT modules CONTAINS "Oracle WFM"` |
| RC-TECH-005 | BCEA Overtime Calculation Requires Additional Config | MEDIUM | `country != "ZA" OR NOT modules CONTAINS "Oracle WFM"` |
| RC-DATA-005 | Demand/Scheduling Data Unavailable | LOW | `NOT modules CONTAINS "Oracle WFM"` |

---

## Pattern-Excluded Risks

The following risks are not applicable to pattern P1 (HCM Full Suite Single).

| Risk ID | Title | Applicable Patterns |
|---|---|---|
| RC-CLIENT-006 | Knowledge Base Content Ownership Undefined | P13 |
| RC-COMM-002 | Oracle HR Help Desk Conflated With Oracle Service Cloud | P13 |
| RC-COMM-003 | Integration Method Commitment in Tender Creates Exposure | P3, P6, P11 |
| RC-INT-003 | Third-Party API Unavailable at Integration Build Start | P3, P6, P7, P8, P9, P11 |
| RC-INT-004 | Payroll API Version Changes Post-Go-Live | P3, P6, P13 |
| RC-INT-006 | Integration Field Mapping Errors Produce Incorrect Data | P3, P6, P7, P8, P9, P11 |
| RC-INT-007 | Bespoke Payroll Mapping Beyond Standard Patterns | P3, P11 |
| RC-PROJ-002 | Upstream Phase Not Stable When Dependent Phase Begins | P2 |
| RC-TECH-010 | Digital Channel Complexity Beyond Standard Configuration | P13 |
| RC-TECH-012 | Annual SA Legislative Change Not Reflected in Integrations | P3, P6, P13 |

---

## Default-Excluded Risks

Risks that are pattern-applicable but where no AREL condition resolved to TRUE.
These risks may become MANDATORY or OPTIONAL if additional RSE extension fields
are provided (e.g., oax_in_scope, integration_count, personal_data_in_scope).

| Risk ID | Title | Rating | Unresolved Conditions |
|---|---|---|---|
| RC-COMM-001 | Analytics Expectations Misaligned With Platform Capability | CRITICAL | mandatory_if: `oax_in_scope = TRUE OR analytics_requirements_in_tender = TRUE` | optional_if: `analytics_requirements_in_tender = FALSE` |
| RC-TECH-006 | OAX Licensing Not Confirmed Before Commitment | CRITICAL | mandatory_if: `oax_in_scope = TRUE AND engagement_type = "Implementation"` | optional_if: `analytics_requirements_in_tender = TRUE AND oax_in_scope = FALSE` |
| RC-TECH-008 | Oracle Product Licensing for Dependent Features Not Confirmed | CRITICAL | mandatory_if: `feature_licensing_confirmed = FALSE AND engagement_type = "Implementation"` | optional_if: `feature_licensing_confirmed = TRUE` |
| RC-COMP-001 | POPIA Non-Compliance in HR or Payroll Data Handling | MEDIUM | mandatory_if: `country = "ZA" AND (personal_data_in_scope = TRUE OR payroll_integration = TRUE)` | optional_if: `country != "ZA"` |
| RC-INT-002 | Third-Party Integration Scope Underestimated | MEDIUM | mandatory_if: `integration_count > 2` | optional_if: `integration_count <= 2` |
| RC-PROJ-004 | Configuration Milestone Changed After Sign-Off | MEDIUM | mandatory_if: `fixed_price = TRUE` | optional_if: `fixed_price = FALSE` |
| RC-TECH-007 | OAX Data Model Not Aligned to HCM Configuration | LOW | mandatory_if: `oax_in_scope = TRUE AND engagement_type = "Implementation"` |
| RC-TECH-009 | ODA Scope Added Without Separate License Confirmation | LOW | mandatory_if: `oda_in_scope = TRUE AND engagement_type = "Implementation"` |

---

*Generated by RSE v1.0 — 2026-06-29 07:10*
