---
document_id: ENTERPRISE-RISK-REGISTER-V1
title: "Enterprise Risk Register — V1.0 (Normalised)"
version: "1.0"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.1A — Enterprise Risk Library Normalisation"
supersedes: "ENTERPRISE_RISK_REGISTER_DRAFT.md (v0.1)"
approved_by: "BU Lead — WP18B-EXT.2 Governance Session"
approved_date: "2026-06-28"
approved_for_reuse: true
canonical_count: 40
schema_version: "RISK_METADATA_STANDARD V1.0"
categories_covered: 8
categories_with_no_source: "RC-RES, RC-INFRA, RC-CM, RC-MIG, RC-CUT, RC-3P, RC-SEC"
---

# Enterprise Risk Register — V1.0 (Normalised)

**Status:** APPROVED. All 40 canonical risks approved for reuse (WP18B-EXT.2 Governance Session, 2026-06-28). 39 risks approved as proposed; 1 rating reversion applied (RC-DATA-004: CRITICAL → HIGH per BU-RL-007 Option B). TD-001 resolved. AV-011 BLOCK unblocked.

**Schema:** All entries comply with RISK_METADATA_STANDARD V1.0. 18 normalisation fields added per entry versus the draft v0.1 register.

**Supersedes:** ENTERPRISE_RISK_REGISTER_DRAFT.md (v0.1) — retain draft for audit trail only.

---

## Risk Index

| Risk ID | Title | Rating | Platforms | Engagement |
|---|---|---|---|---|
| RC-PROJ-001 | Module design not signed off before build begins | HIGH | Oracle HCM Cloud | Implementation |
| RC-PROJ-002 | Upstream phase not stable when dependent phase begins | HIGH | Oracle HCM Cloud | Implementation |
| RC-PROJ-003 | Organisational design decisions made late | HIGH | Oracle HCM Cloud | Implementation |
| RC-PROJ-004 | Configuration milestone changed after sign-off | LOW | Oracle Cloud | Implementation |
| RC-DATA-001 | Legacy HR data quality causes migration delays | HIGH | Oracle HCM Cloud | Implementation |
| RC-DATA-002 | Client content format incompatible with platform | MEDIUM | Oracle Learning | Implementation |
| RC-DATA-003 | HCM data quality produces invalid payroll input | HIGH | Oracle HCM / OIC | Implementation |
| RC-DATA-004 | Biometric enrolment data does not match HR records | HIGH | Oracle WFM | Implementation |
| RC-DATA-005 | Demand/scheduling data unavailable | LOW | Oracle WFM | Implementation |
| RC-INT-001 | Payroll integration timeline not aligned to HCM go-live | HIGH | Oracle HCM / OIC | Implementation |
| RC-INT-002 | Third-party integration scope underestimated | MEDIUM | Oracle Cloud / OIC | Implementation |
| RC-INT-003 | Third-party API unavailable at integration build start | HIGH | Oracle OIC | Implementation |
| RC-INT-004 | Payroll API version changes post-go-live | MEDIUM | Oracle OIC | Implementation / AMS |
| RC-INT-005 | Integration schedule not aligned to payroll cutoff | HIGH | Oracle OIC | Implementation |
| RC-INT-006 | Integration field mapping errors produce incorrect data | HIGH | Oracle OIC | Implementation |
| RC-INT-007 | Bespoke payroll mapping beyond standard patterns | MEDIUM | Acumatica / Oracle | Implementation |
| RC-TECH-001 | Quarterly SaaS update breaks configured functionality | LOW | Oracle Cloud | Implementation / AMS |
| RC-TECH-002 | SETA/WSP/ATR extract complexity | MEDIUM | Oracle HCM | Implementation |
| RC-TECH-003 | Absence rules complexity exceeds standard scope | HIGH | Oracle WFM | Implementation |
| RC-TECH-004 | Time and labour rules complexity exceeds estimate | MEDIUM | Oracle WFM | Implementation |
| RC-TECH-005 | BCEA overtime calculation requires additional config | MEDIUM | Oracle WFM | Implementation |
| RC-TECH-006 | OAX licensing not confirmed before commitment | HIGH | Oracle HCM | Implementation |
| RC-TECH-007 | OAX data model not aligned to HCM configuration | LOW | Oracle HCM Analytics | Implementation |
| RC-TECH-008 | Oracle product licensing for dependent features not confirmed | HIGH | Oracle Cloud | Implementation |
| RC-TECH-009 | ODA scope added without separate license confirmation | LOW | Oracle Cloud | Implementation |
| RC-TECH-010 | Digital channel complexity beyond standard configuration | LOW | Oracle Help Desk | AMS |
| RC-TECH-011 | Career site design complexity exceeds standard scope | MEDIUM | Oracle Recruiting | Implementation |
| RC-TECH-012 | Annual SA legislative change not reflected in integrations | HIGH | Oracle OIC | Implementation / AMS |
| RC-CLIENT-001 | Super-user availability insufficient during UAT | MEDIUM | All Oracle | Implementation |
| RC-CLIENT-002 | Client prerequisite systems or accounts not available | LOW | Oracle Cloud | Implementation |
| RC-CLIENT-003 | Onboarding task and workflow ownership not defined | MEDIUM | Oracle Recruiting / HCM | Implementation |
| RC-CLIENT-004 | Learning catalog not ready at system go-live | HIGH | Oracle Learning | Implementation |
| RC-CLIENT-005 | Performance rating data unavailable for compensation cycle | MEDIUM | Oracle HCM | Implementation |
| RC-CLIENT-006 | Knowledge base content ownership undefined | MEDIUM | Oracle Help Desk | AMS |
| RC-CLIENT-007 | Cross-functional alignment on design frameworks | HIGH | Oracle HCM | Implementation |
| RC-COMM-001 | Analytics expectations misaligned with platform capability | HIGH | Oracle HCM | Implementation |
| RC-COMM-002 | Oracle HR Help Desk conflated with Oracle Service Cloud | HIGH | Oracle Help Desk | AMS |
| RC-COMM-003 | Integration method commitment in tender creates exposure | MEDIUM | Acumatica / Oracle | Implementation |
| RC-OPS-001 | First live operational cycle high-stakes risk | CRITICAL | Oracle HCM | Implementation |
| RC-COMP-001 | POPIA non-compliance in HR or payroll data handling | MEDIUM | Oracle HCM / OIC | Implementation / AMS |

---

## RC-PROJ — Project Risk (4 entries)

---

### RC-PROJ-001 — Module Design Not Signed Off Before Build Begins

| Field | Value |
|---|---|
| **Risk ID** | RC-PROJ-001 |
| **Category** | RC-PROJ — Project Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-002 (R-W2-001), W3S1-005 (R-W3-005-001) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Project Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Project Manager |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, W3S1-002, W3S1-005 |
| **Supersedes** | — |
| **Related risks** | RC-PROJ-003, RC-CLIENT-007 |
| **Related assumptions** | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Critical |
| **Mandatory if** | platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation" |
| **Optional if** | platform CONTAINS "Oracle ERP" AND engagement_type = "Implementation" |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Merged from two source risks: R-W2-001 (design approval) and R-W3-005-001 (module design sign-off). Both referenced the same root cause. See DG-001 in RISK_DUPLICATION_ANALYSIS.md. |

**Risk description:** APPSolve begins building and configuring HCM modules before client stakeholders have signed off the functional design. Build based on unapproved design produces rework when the client revises decisions mid-configuration, consuming contingency and extending the timeline.

**Standard mitigation:** Design sign-off is a defined project milestone in the APPSolve project plan. APPSolve will not release the Configuration workstream to begin build until the client's authorised representative has provided written approval of the agreed functional design per HCM-ORG-001. Unsigned design is tracked in the project RAID log and escalated weekly until resolved.

**Customisation guidance:** For phased implementations (Pattern 2), apply per phase: each phase requires its own design sign-off before that phase's build begins. For fixed-price engagements, emphasise that post-sign-off changes are Change Requests per HCM-ORG-001 and priced accordingly.

---

### RC-PROJ-002 — Upstream Phase Not Stable When Dependent Phase Begins

| Field | Value |
|---|---|
| **Risk ID** | RC-PROJ-002 |
| **Category** | RC-PROJ — Project Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-002 (R-W2-003), W3S1-003 (R-W3-003-003) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Project Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Project Manager |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-CUT-001, HCM-CUT-002, HCM-ORG-001, W3S1-002, W3S1-003 |
| **Supersedes** | — |
| **Related risks** | RC-PROJ-001, RC-OPS-001 |
| **Related assumptions** | HCM-CUT-001, HCM-CUT-002, HCM-CUT-003, HCM-CUT-004, HCM-CUT-005, HCM-CUT-006, HCM-CUT-007, HCM-CUT-008, HCM-ORG-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 2 |
| **Assembly priority** | High |
| **Mandatory if** | delivery_model = "Phased" |
| **Optional if** | delivery_model = "Single" AND phase_count > 1 |
| **Excluded if** | delivery_model = "Single" AND phase_count = 1 |
| **Governance notes** | Merged from R-W2-003 and R-W3-003-003 (DG-002). Only relevant for phased delivery; Pattern 2 is the primary applicability. |

**Risk description:** In a phased implementation, a subsequent phase commences before the preceding phase has achieved stability. Instability in earlier phases (unresolved configuration defects, unsigned-off processes, or deferred decisions) cascades into the next phase, causing parallel rework and schedule compression.

**Standard mitigation:** APPSolve's phased project plan includes phase-exit criteria. Each phase must achieve go/no-go readiness (confirmed by formal sign-off) before the next phase is released. Unresolved items from the prior phase are tracked in the RAID log and escalated before the next phase kick-off.

**Customisation guidance:** For Pattern 2 (HCM Full Suite Phased), list the specific phases and their entry criteria. Where the client has a hard commercial deadline, explicitly note that the phase-exit gate remains a prerequisite and document the risk of compressing it.

---

### RC-PROJ-003 — Organisational Design Decisions Made Late

| Field | Value |
|---|---|
| **Risk ID** | RC-PROJ-003 |
| **Category** | RC-PROJ — Project Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-004 (R-W3-004-001) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008, W3S1-004 |
| **Supersedes** | — |
| **Related risks** | RC-PROJ-001, RC-CLIENT-007 |
| **Related assumptions** | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Critical |
| **Mandatory if** | platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" OR platform = "OIC Standalone" |
| **Governance notes** | Rating recalculated in V1.0: likelihood revised from Medium to High based on observed frequency across HCM projects. |

**Risk description:** The client's organisational design (legal entity structure, business unit hierarchy, location structure, and job architecture) is not finalised before the HCM Scoping and Design phase begins. Oracle HCM Core HR configuration is built on top of the organisational structure; late org design decisions invalidate configuration already completed, requiring rework across multiple modules.

**Standard mitigation:** APPSolve's project plan includes an Organisational Design prerequisite milestone prior to Core HR configuration. APPSolve will conduct an Org Design workshop in Week 1–2 of the project. Client sign-off on the org design is required per HCM-ORG-001 before configuration of any org-dependent module commences.

**Customisation guidance:** Explicitly reference the client's current org structure maturity during tender. If the client is undergoing a restructure, increase likelihood to High and reference HCM-ORG-001 as a specific contractual boundary.

---

### RC-PROJ-004 — Configuration Milestone Changed After Sign-Off

| Field | Value |
|---|---|
| **Risk ID** | RC-PROJ-004 |
| **Category** | RC-PROJ — Project Risk |
| **Platforms** | Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-005 (R-W3-005-002) |
| **Likelihood** | Low |
| **Impact** | High |
| **Rating** | MEDIUM |
| **Owner** | Project Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Project Manager |
| **Owner business unit** | Cross-Platform |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | HCM-ORG-001, ERP-GEN-001, W3S1-005 |
| **Supersedes** | — |
| **Related risks** | RC-PROJ-001, RC-PROJ-003 |
| **Related assumptions** | HCM-ORG-001, ERP-GEN-001, ERP-GEN-002 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 1, 2, 3, 7, 8, 9, 11 |
| **Assembly priority** | Standard |
| **Mandatory if** | fixed_price = TRUE |
| **Optional if** | fixed_price = FALSE |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Rating LOW in draft; recalculated in V1.0 as MEDIUM (Low likelihood × High impact). |

**Risk description:** After the client has signed off a configuration milestone, the client requests changes to that milestone, requiring re-work of completed build artefacts. In fixed-price engagements, this is the primary source of margin erosion if not managed through formal change control.

**Standard mitigation:** All configuration decisions are documented in a sign-off register. Once signed off, changes are processed as formal Change Requests. APPSolve's project plan includes a Configuration Freeze gate before testing begins. The Change Request process is described in the proposal Change Control section (S-38).

**Customisation guidance:** For fixed-price engagements, explicitly reference the Change Request process in the risk mitigation and cross-reference S-38. For time-and-materials engagements, lower priority to Standard.

---

## RC-DATA — Data Risk (5 entries)

---

### RC-DATA-001 — Legacy HR Data Quality Causes Migration Delays

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-001 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-002 (R-W2-004) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-DAT-001, HCM-DAT-002, HCM-DAT-003, HCM-DAT-004, HCM-DAT-005, W3S1-002 |
| **Supersedes** | — |
| **Related risks** | RC-DATA-003, RC-OPS-001 |
| **Related assumptions** | HCM-DAT-001, HCM-DAT-002, HCM-DAT-003, HCM-DAT-004, HCM-DAT-005, HCM-DAT-006, HCM-DAT-007, HCM-DAT-008, HCM-DAT-009 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Critical |
| **Mandatory if** | platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Rating recalculated in V1.0: HIGH in draft. Observed frequency of HR data quality issues across multiple HCM projects warrants CRITICAL rating. |

**Risk description:** The client's legacy HR records contain structural inconsistencies, missing mandatory fields, duplicate employee records, or data that cannot be mapped to the Oracle HCM data model. Poor source data quality causes repeated extract-transform-load cycles, delays the data migration milestone, and can push back UAT and go-live.

**Standard mitigation:** APPSolve conducts a Data Assessment workshop in the first month of the project, producing a Data Quality Report. Data cleansing is the client's responsibility per HCM-DAT-001. APPSolve provides data templates and mapping guidance. A minimum of two data migration dress rehearsals are included before production migration.

**Customisation guidance:** If the client has known legacy system complexity (multiple HRIS sources, manual records, or significant contractor workforce data), increase likelihood to High and expand mitigation to include a dedicated data cleansing workstream with client-side resource commitment.

---

### RC-DATA-002 — Client Content Format Incompatible With Platform

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-002 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle Learning Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W1S2-007 (R-W1-001) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | Medium |
| **Source assets** | LRN-DAT-001, LRN-DAT-002, LRN-DAT-003, W1S2-007 |
| **Supersedes** | — |
| **Related risks** | RC-CLIENT-004 |
| **Related assumptions** | LRN-DAT-001, LRN-DAT-002, LRN-DAT-003, LRN-DAT-004 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 5, 1, 2 |
| **Assembly priority** | Standard |
| **Mandatory if** | modules CONTAINS "Oracle Learning" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | NOT modules CONTAINS "Oracle Learning" |
| **Governance notes** | — |

**Risk description:** The client has existing learning content (SCORM packages, videos, documents) in formats that are not natively supported by Oracle Learning Cloud. Content conversion or re-authoring is required, consuming time and budget outside the standard scope.

**Standard mitigation:** APPSolve conducts a Content Assessment during Scoping and Design. Supported content formats are documented in LRN-DAT-001. Content conversion is the client's responsibility unless explicitly scoped. APPSolve provides format specifications and a compatibility checklist.

**Customisation guidance:** If the client has a large existing content library, include a content inventory item in the proposal scope section. If content conversion is explicitly required, it must be separately scoped and priced.

---

### RC-DATA-003 — HCM Data Quality Produces Invalid Payroll Input

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-003 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle HCM Cloud / Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-009 (R-W9-001) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Oracle OIC |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-DAT-001, HCM-DAT-002, OIC-MAP-001, OIC-MAP-002, OIC-MAP-003, W3S1-009 |
| **Supersedes** | — |
| **Related risks** | RC-DATA-001, RC-INT-006, RC-INT-001 |
| **Related assumptions** | HCM-DAT-001, HCM-DAT-002, HCM-DAT-003, HCM-DAT-004, HCM-DAT-005, OIC-MAP-001, OIC-MAP-002, OIC-MAP-003 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Critical |
| **Mandatory if** | payroll_integration = TRUE AND platform CONTAINS "Oracle HCM" |
| **Optional if** | payroll_integration = FALSE AND platform CONTAINS "Oracle HCM" |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Rating recalculated in V1.0: CRITICAL (High × High). Payroll-linked data quality failures have direct financial impact. |

**Risk description:** Employee master data migrated from the legacy system into Oracle HCM contains errors (incorrect cost centres, missing job codes, duplicate employee numbers) that propagate through the OIC integration into the payroll system, producing invalid payroll runs. Payroll errors are high-impact: they affect employee pay and carry regulatory risk.

**Standard mitigation:** APPSolve includes a Payroll Data Validation workstream as part of integration testing. Integration field mapping is documented and signed off per OIC-MAP-001. Payroll parallel runs are conducted before production cutover. Data validation rules are agreed with the client's payroll team.

**Customisation guidance:** Always pair with RC-INT-001 in any proposal that includes payroll integration. Where the client has multiple payroll systems, increase likelihood to High.

---

### RC-DATA-004 — Biometric Enrolment Data Does Not Match HR Records

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-004 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-008 (R-W8-002) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | Medium |
| **Source assets** | HCM-DAT-001, HCM-DAT-002, W3S1-008 |
| **Supersedes** | — |
| **Related risks** | RC-DATA-001 |
| **Related assumptions** | HCM-DAT-001, HCM-DAT-002 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | High |
| **Mandatory if** | modules CONTAINS "Oracle WFM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | NOT modules CONTAINS "Oracle WFM" |
| **Governance notes** | V1.0 proposed CRITICAL (High × High). WP18B-EXT.2 BU-RL-007 (Option B): Rating reverted to HIGH (Medium × High). Likelihood reduced from High to Medium — confidence level is Medium; insufficient WFM biometric implementation evidence to sustain High likelihood. |

**Risk description:** Biometric devices (fingerprint scanners, access control systems) have enrolled employee records that do not match the employee numbers or identity data in the Oracle WFM system. Mismatches prevent time and attendance records from linking to the correct employee in WFM, producing unrecorded attendance and downstream payroll errors.

**Standard mitigation:** APPSolve includes a Biometric Data Reconciliation milestone in the WFM implementation plan. A data reconciliation exercise comparing biometric device employee records against HR master data is completed before WFM integration testing. Reconciliation is the client's operational responsibility; APPSolve provides the reconciliation template.

**Customisation guidance:** Only include in proposals where Oracle WFM or biometric time and attendance is explicitly in scope.

---

### RC-DATA-005 — Demand/Scheduling Data Unavailable

| Field | Value |
|---|---|
| **Risk ID** | RC-DATA-005 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-008 (R-W8-005) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2027-06-26 |
| **Confidence level** | Medium |
| **Source assets** | HCM-DAT-001, W3S1-008 |
| **Supersedes** | — |
| **Related risks** | RC-DATA-004 |
| **Related assumptions** | HCM-DAT-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2 |
| **Assembly priority** | Standard |
| **Mandatory if** | modules CONTAINS "Oracle WFM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | NOT modules CONTAINS "Oracle WFM" |
| **Governance notes** | — |

**Risk description:** Demand forecasting and scheduling data required to configure Oracle WFM scheduling rules is not available at the time of the WFM configuration workstream. Without historical demand data, scheduling optimisation rules cannot be configured accurately, requiring post-go-live tuning.

**Standard mitigation:** APPSolve documents the scheduling data requirements during Scoping and Design. The client is required to provide at least 12 months of historical demand or attendance data before WFM scheduling configuration begins. Where data is unavailable, initial scheduling rules are configured using industry benchmarks with a post-go-live tuning period.

**Customisation guidance:** Only include in proposals where Oracle WFM scheduling optimisation is in scope.

---

## RC-INT — Integration Risk (7 entries)

---

### RC-INT-001 — Payroll Integration Timeline Not Aligned to HCM Go-Live

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-001 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle HCM Cloud / Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-009 (R-W9-002) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Oracle OIC |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-3PT-001, HCM-3PT-002, HCM-3PT-003, OIC-DES-001, OIC-DES-002, OIC-END-001, W3S1-009 |
| **Supersedes** | — |
| **Related risks** | RC-INT-005, RC-DATA-003, RC-OPS-001 |
| **Related assumptions** | HCM-3PT-001, HCM-3PT-002, HCM-3PT-003, HCM-3PT-004, HCM-3PT-005, HCM-3PT-006, OIC-DES-001, OIC-DES-002, OIC-DES-003, OIC-END-001, OIC-END-002 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Critical |
| **Mandatory if** | payroll_integration = TRUE AND platform CONTAINS "Oracle HCM" |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" OR payroll_integration = FALSE |
| **Governance notes** | — |

**Risk description:** The third-party payroll system integration is not completed and tested in time to support the HCM go-live date. If payroll integration is not ready, employees cannot be paid from the live system, forcing a delay to go-live or a parallel payroll run. Payroll go-live delays carry significant regulatory and reputational risk.

**Standard mitigation:** APPSolve includes payroll integration as a critical path workstream. Integration testing with the payroll vendor is scheduled to complete at least four weeks before go-live per HCM-3PT-001. A parallel payroll run is conducted before production cutover. Integration readiness is a go-live gate criterion.

**Customisation guidance:** If the payroll vendor is a third party (not APPSolve), explicitly document third-party readiness as a client responsibility per HCM-3PT-001 and OIC-DES-001. Cross-reference RC-INT-005 (payroll cutoff alignment).

---

### RC-INT-002 — Third-Party Integration Scope Underestimated

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-002 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle Cloud / Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-003 (R-W3-003-005), W3S1-004 (R-W3-004-005) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Oracle OIC |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | OIC-DES-001, OIC-DES-002, OIC-SCP-001, HCM-3PT-001, W3S1-003, W3S1-004 |
| **Supersedes** | — |
| **Related risks** | RC-INT-003, RC-INT-006 |
| **Related assumptions** | OIC-DES-001, OIC-DES-002, OIC-DES-003, OIC-DES-004, OIC-DES-005, OIC-SCP-001, OIC-SCP-002, HCM-3PT-001, HCM-3PT-002 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 1, 2, 3, 6, 7, 8, 11 |
| **Assembly priority** | High |
| **Mandatory if** | integration_count > 2 |
| **Optional if** | integration_count <= 2 |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Merged from R-W3-003-005 and R-W3-004-005 (DG-004). Both expressed the same underestimation risk. |

**Risk description:** The number of data objects, transformation rules, or endpoint variations in a third-party integration is larger than estimated at scoping. Underestimated integration complexity extends the build timeline and consumes contingency, particularly when field mapping specifications are incomplete or when the third-party system has undocumented API behaviour.

**Standard mitigation:** APPSolve conducts an Integration Discovery workshop at project commencement. Each integration is documented in an Integration Design Specification per OIC-DES-001. APPSolve's integration scope is limited to the integrations and endpoints named in the SOW.

**Customisation guidance:** For proposals with more than three integrations, explicitly list each integration by name. Reference OIC-DES-001 as the boundary document. For Acumatica proposals (Pattern 11), reference ACU-INT instead of OIC-DES.

---

### RC-INT-003 — Third-Party API Unavailable at Integration Build Start

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-003 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-003 (R-W3-003-006) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Oracle OIC |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | OIC-END-001, OIC-END-002, OIC-END-003, OIC-DES-001, W3S1-003 |
| **Supersedes** | — |
| **Related risks** | RC-INT-002, RC-INT-006 |
| **Related assumptions** | OIC-END-001, OIC-END-002, OIC-END-003, OIC-END-004, OIC-END-005, OIC-END-006, OIC-DES-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 3, 6, 7, 8, 9, 11 |
| **Assembly priority** | High |
| **Mandatory if** | platform CONTAINS "OIC" AND third_party_api = TRUE |
| **Optional if** | platform CONTAINS "OIC" AND third_party_api = FALSE |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | — |

**Risk description:** The third-party system's API endpoint is not available (sandbox or production) when APPSolve's integration build is ready to begin. API unavailability causes idle time in the Integration workstream, compressing the remaining integration build and testing window.

**Standard mitigation:** APPSolve documents API endpoint readiness requirements per OIC-END-001. Third-party API availability is a client responsibility; the client is required to confirm API access at least four weeks before the integration build workstream commences. Unavailability is tracked in the RAID log and escalated immediately.

**Customisation guidance:** For OIC standalone proposals (Pattern 6), this is the primary integration risk. Where the third party is a public SaaS vendor (e.g., Salesforce, SAP), confirm sandbox access timelines explicitly during proposal qualification.

---

### RC-INT-004 — Payroll API Version Changes Post-Go-Live

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-004 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle OIC |
| **Engagement types** | Implementation / AMS |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-009 (R-W9-004) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Oracle OIC |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | OIC-DES-001, OIC-DES-002, AMS-REL-001, W3S1-009 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-001, RC-TECH-012 |
| **Related assumptions** | OIC-DES-001, OIC-DES-002, AMS-REL-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12, S-73 |
| **Proposal patterns** | 3, 6, 13 |
| **Assembly priority** | Standard |
| **Mandatory if** | payroll_integration = TRUE AND (engagement_type = "Implementation" OR engagement_type = "AMS") |
| **Optional if** | — |
| **Excluded if** | NOT payroll_integration = TRUE |
| **Governance notes** | AMS-applicable risk: included in Pattern 13 (S-73 as secondary). |

**Risk description:** The third-party payroll system vendor releases an API version update that is incompatible with the OIC integration deployed at go-live. Without advance notice of the breaking change, the integration fails at runtime, interrupting the payroll data feed.

**Standard mitigation:** APPSolve's OIC integration design documents the API version in use per OIC-DES-001. For AMS engagements, APPSolve monitors payroll vendor release communications and assesses compatibility per AMS-REL-001. API version change remediation is assessed as a change request.

**Customisation guidance:** For AMS proposals, include this risk and reference AMS-REL-001 explicitly. Secondary section S-73 should describe the change request process for integration updates.

---

### RC-INT-005 — Integration Schedule Not Aligned to Payroll Cutoff

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-005 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-008 (R-W9-003), W3S1-005 (R-W3-005-005) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Oracle OIC |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | OIC-DES-001, HCM-3PT-001, HCM-CUT-001, W3S1-009, W3S1-005 |
| **Supersedes** | — |
| **Related risks** | RC-INT-001, RC-OPS-001 |
| **Related assumptions** | OIC-DES-001, OIC-DES-002, OIC-DES-003, HCM-3PT-001, HCM-3PT-002, HCM-CUT-001, HCM-CUT-002, HCM-CUT-003 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3, 6 |
| **Assembly priority** | Critical |
| **Mandatory if** | payroll_integration = TRUE AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" OR payroll_integration = FALSE |
| **Governance notes** | Merged from R-W9-003 and R-W3-005-005 (DG-006). |

**Risk description:** The integration testing and cutover plan does not account for the fixed window imposed by the client's payroll processing cycle. Payroll cutoff dates are immovable; if integration testing extends past the cutoff window, the first live payroll run must be executed with the legacy system while the new integration is still being tested, creating a dual-run period that is operationally complex.

**Standard mitigation:** APPSolve's integration project plan is built around the client's payroll cycle. Cutover dates and payroll cutoff windows are documented at project kick-off. Integration testing is scheduled to complete at least two full payroll cycles before production cutover.

**Customisation guidance:** Obtain the client's payroll calendar during qualification. Build integration testing milestones backward from the payroll cutoff. Cross-reference RC-INT-001 and RC-OPS-001.

---

### RC-INT-006 — Integration Field Mapping Errors Produce Incorrect Data

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-006 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-009 (R-W9-006) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Oracle OIC |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | OIC-MAP-001, OIC-MAP-002, OIC-MAP-003, OIC-TST-001, W3S1-009 |
| **Supersedes** | — |
| **Related risks** | RC-DATA-003, RC-INT-002 |
| **Related assumptions** | OIC-MAP-001, OIC-MAP-002, OIC-MAP-003, OIC-MAP-004, OIC-MAP-005, OIC-MAP-006, OIC-TST-001, OIC-TST-002, OIC-TST-003 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 3, 6, 7, 8, 9, 11 |
| **Assembly priority** | High |
| **Mandatory if** | platform CONTAINS "OIC" |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | — |

**Risk description:** The field mapping between the source and target systems is incorrectly defined, not validated against the live data model, or changed after the integration is built. Incorrect mapping produces silent data corruption: records transfer without error but contain wrong values, which may not be detected until the end-to-end testing phase.

**Standard mitigation:** APPSolve documents all field mappings in a signed-off Integration Field Mapping Specification per OIC-MAP-001 before integration build begins. All mappings are validated against actual source and target data samples. Integration testing includes data validation against the specification.

**Customisation guidance:** For proposals with complex transformation logic (calculated fields, value substitution tables, conditional mapping), increase likelihood to Medium and include a dedicated mapping review step in the project plan.

---

### RC-INT-007 — Bespoke Payroll Mapping Beyond Standard Patterns

| Field | Value |
|---|---|
| **Risk ID** | RC-INT-007 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Acumatica / Oracle |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-007 (R-W7-004) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Acumatica |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | Medium |
| **Source assets** | OIC-MAP-001, OIC-MAP-002, ACU-INT-001, W3S1-007 |
| **Supersedes** | — |
| **Related risks** | RC-INT-006, RC-COMM-003 |
| **Related assumptions** | OIC-MAP-001, OIC-MAP-002, OIC-MAP-003, ACU-INT-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 3, 11 |
| **Assembly priority** | Standard |
| **Mandatory if** | payroll_integration = TRUE AND (platform = "Acumatica" OR (platform CONTAINS "Oracle" AND payroll_provider = "non-standard")) |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Primary applicability is Acumatica (Pattern 11) and non-standard Oracle payroll integrations (Pattern 3). |

**Risk description:** The client's payroll system requires mapping that deviates from APPSolve's standard payroll integration patterns (e.g., non-standard earnings codes, split payment structures, multi-currency payroll, or proprietary payroll platform APIs). Bespoke mapping requires additional analysis and build effort beyond the standard integration scope.

**Standard mitigation:** APPSolve's standard payroll integration patterns are defined in the OIC Implementation Patterns document. At scoping, APPSolve conducts a Payroll Mapping Assessment. Non-standard mapping is identified, documented, and explicitly priced as an addition to scope.

**Customisation guidance:** For Acumatica proposals, verify the payroll system at qualification. For Oracle proposals with non-standard payroll vendors, include a payroll mapping assessment in the project methodology.

---

## RC-TECH — Technical Risk (12 entries)

---

### RC-TECH-001 — Quarterly SaaS Update Breaks Configured Functionality

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-001 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Cloud |
| **Engagement types** | Implementation / AMS |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-003 (R-W3-003-001) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2027-06-26 |
| **Confidence level** | High |
| **Source assets** | HCM-ENV-004, AMS-REL-001, W3S1-003 |
| **Supersedes** | — |
| **Related risks** | RC-INT-004, RC-TECH-012 |
| **Related assumptions** | HCM-ENV-004, AMS-REL-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12, S-73 |
| **Proposal patterns** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 13 |
| **Assembly priority** | Standard |
| **Mandatory if** | platform CONTAINS "Oracle" AND (engagement_type = "Implementation" OR engagement_type = "AMS") |
| **Optional if** | — |
| **Excluded if** | platform = "Acumatica" OR platform = "BeBanking" |
| **Governance notes** | — |

**Risk description:** Oracle's quarterly SaaS update cycle introduces changes to the platform that are incompatible with configuration or integrations delivered by APPSolve. While Oracle provides advance notice of breaking changes, the client is responsible for regression testing and confirming compatibility before each update is applied to production.

**Standard mitigation:** APPSolve documents the Oracle quarterly update responsibility boundary per HCM-ENV-004. For AMS engagements, APPSolve provides a quarterly update advisory service per AMS-REL-001. Regression testing is a client responsibility unless explicitly scoped as part of AMS.

**Customisation guidance:** For AMS proposals, expand the mitigation to describe the update advisory service and cross-reference AMS-REL-001. Include in S-73 (AMS Change Requests) as an operational risk.

---

### RC-TECH-002 — SETA/WSP/ATR Extract Complexity

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-002 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-004 (R-W3-004-004), W3S1-006 (R-W3-006-004) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | HCM-RPT-001, HCM-RPT-002, HCM-RPT-003, HCM-RPT-004, HCM-RPT-005, HCM-RPT-006, W3S1-004, W3S1-006 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-005 |
| **Related assumptions** | HCM-RPT-001, HCM-RPT-002, HCM-RPT-003, HCM-RPT-004, HCM-RPT-005, HCM-RPT-006 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2 |
| **Assembly priority** | Standard |
| **Mandatory if** | country = "ZA" AND modules CONTAINS "Oracle HCM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | country != "ZA" |
| **Governance notes** | Merged from R-W3-004-004 and R-W3-006-004 (DG-003). South Africa-specific legislative requirement. |

**Risk description:** South African SETA (Workplace Skills Plan and Annual Training Report) reporting requirements impose complex data extraction and transformation on the Oracle HCM Learning and HR data model. The extract logic often exceeds Oracle's standard reporting templates, requiring custom reporting configuration that is beyond the standard HCM implementation scope.

**Standard mitigation:** APPSolve conducts a SETA Reporting Assessment during Scoping and Design. Standard SETA extract configuration is included in scope for ZA-based implementations. Additional complexity (multiple SETA registrations, merged entity reporting, legacy data inclusion) is assessed and priced as a scope addition.

**Customisation guidance:** Mandatory for all South African HCM proposals. Where the client has multiple SETA registrations, explicitly scope the multi-SETA extract as a separate deliverable.

---

### RC-TECH-003 — Absence Rules Complexity Exceeds Standard Scope

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-003 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-008 (R-W8-001) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-WFL-001, HCM-WFL-002, HCM-WFL-003, HCM-WFL-004, W3S1-008 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-004, RC-TECH-005 |
| **Related assumptions** | HCM-WFL-001, HCM-WFL-002, HCM-WFL-003, HCM-WFL-004, HCM-WFL-005, HCM-WFL-006 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Critical |
| **Mandatory if** | modules CONTAINS "Oracle WFM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | NOT modules CONTAINS "Oracle WFM" |
| **Governance notes** | Rating recalculated in V1.0: CRITICAL (High × High). Absence rule complexity is the single most common WFM scope overrun. |

**Risk description:** The client's absence management policies (leave types, accrual rules, carryover rules, negative balance controls, shift-pattern leave calculations) are more complex than the Oracle WFM standard configuration scope allows. Bespoke absence rules require additional configuration workstream effort, often extending the project timeline.

**Standard mitigation:** APPSolve conducts an Absence Rules Assessment during Scoping and Design. Standard absence types (annual leave, sick leave, family responsibility) are in scope per HCM-WFL-001. Additional absence types or non-standard accrual logic are assessed and priced as scope additions.

**Customisation guidance:** Mandatory for all WFM proposals. Where the client has shift workers, multiple employment types, or union-negotiated leave entitlements, increase likelihood to High.

---

### RC-TECH-004 — Time and Labour Rules Complexity Exceeds Estimate

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-004 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-008 (R-W8-003) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | HCM-WFL-001, HCM-WFL-002, W3S1-008 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-003, RC-TECH-005 |
| **Related assumptions** | HCM-WFL-001, HCM-WFL-002 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Standard |
| **Mandatory if** | modules CONTAINS "Oracle WFM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | NOT modules CONTAINS "Oracle WFM" |
| **Governance notes** | — |

**Risk description:** The client's time and labour configuration requirements (shift patterns, overtime triggers, time zone handling, rounding rules) exceed the standard WFM configuration estimate. Additional complexity drives build and testing overruns.

**Standard mitigation:** APPSolve scopes time and labour configuration based on a Time Rules Assessment. The number of distinct time rules is documented before configuration begins. Rules beyond the scoped volume are priced as Change Requests.

**Customisation guidance:** For shift-intensive industries (manufacturing, hospitality, healthcare), increase likelihood to High. Pair with RC-TECH-003.

---

### RC-TECH-005 — BCEA Overtime Calculation Requires Additional Config

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-005 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-008 (R-W8-004) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | HCM-WFL-001, W3S1-008 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-003, RC-TECH-004 |
| **Related assumptions** | HCM-WFL-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Standard |
| **Mandatory if** | country = "ZA" AND modules CONTAINS "Oracle WFM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | country != "ZA" OR NOT modules CONTAINS "Oracle WFM" |
| **Governance notes** | South Africa-specific. BCEA = Basic Conditions of Employment Act. |

**Risk description:** South African BCEA overtime provisions (1.5× for first two hours, 2× for Sunday/public holiday) require specific time calculation rules that interact with shift pattern, employee category, and sectoral determination. The interaction of BCEA rules with the client's specific employment categories may exceed the standard configuration scope.

**Standard mitigation:** APPSolve includes standard BCEA overtime configuration for permanent employees in the ZA standard scope. Sector-specific agreements (bargaining council determinations) or complex multi-rate overtime structures are assessed and priced separately.

**Customisation guidance:** Mandatory for all South African WFM proposals. Confirm whether the client has multiple employment categories subject to different overtime rates at qualification.

---

### RC-TECH-006 — OAX Licensing Not Confirmed Before Commitment

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-006 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-004 (R-W3-004-003) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Commercial Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Commercial Manager |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-RPT-003, W3S1-004 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-007, RC-TECH-008, RC-COMM-001 |
| **Related assumptions** | HCM-RPT-003 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2 |
| **Assembly priority** | Critical |
| **Mandatory if** | oax_in_scope = TRUE AND engagement_type = "Implementation" |
| **Optional if** | analytics_requirements_in_tender = TRUE AND oax_in_scope = FALSE |
| **Excluded if** | oax_in_scope = FALSE AND analytics_requirements_in_tender = FALSE |
| **Governance notes** | Rating recalculated in V1.0: CRITICAL (High × High). OAX licensing failures have been observed to stop projects. Deliberately kept separate from RC-TECH-008 (general licensing). See DG-008 in RISK_DUPLICATION_ANALYSIS.md. |

**Risk description:** APPSolve commits to delivering Oracle Analytics for HCM (OAX) as part of the implementation without confirming that the client holds an active OAX licence or that OAX is included in the Oracle subscription. OAX is a separately licensed product per HCM-RPT-003. Discovering the licence gap after project commencement forces a commercial conversation that delays the Analytics workstream.

**Standard mitigation:** APPSolve confirms OAX licence status as a pre-project prerequisite per HCM-RPT-003. If OAX is in scope, licence confirmation is a project kick-off gate criterion. Analytics configuration does not commence until the licence is confirmed active.

**Customisation guidance:** Always include in any HCM proposal that includes OAX or analytics deliverables. Reference HCM-RPT-003 explicitly. Cross-reference RC-COMM-001 (analytics expectation misalignment).

---

### RC-TECH-007 — OAX Data Model Not Aligned to HCM Configuration

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-007 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle HCM Analytics |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-004 (R-W3-004-006) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle Analytics |
| **Review frequency** | Annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2027-06-26 |
| **Confidence level** | Medium |
| **Source assets** | HCM-RPT-003, W3S1-004 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-006, RC-COMM-001 |
| **Related assumptions** | HCM-RPT-003 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2 |
| **Assembly priority** | Standard |
| **Mandatory if** | oax_in_scope = TRUE AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | oax_in_scope = FALSE |
| **Governance notes** | Deliberately kept separate from RC-TECH-006 (licensing). See DG-008. |

**Risk description:** Oracle Analytics for HCM (OAX) uses a pre-built data model that is dependent on the HCM configuration being aligned to Oracle's standard subject areas. Custom flexfields, non-standard job architecture, or deviations from the Oracle-prescribed data structure can cause OAX subject areas to produce incomplete or incorrect reports.

**Standard mitigation:** APPSolve includes an OAX Compatibility Review at the conclusion of Core HR configuration. Any HCM configuration deviations that affect the OAX data model are identified and resolved before Analytics configuration begins.

**Customisation guidance:** Only include in proposals where OAX is explicitly in scope. Pair with RC-TECH-006.

---

### RC-TECH-008 — Oracle Product Licensing for Dependent Features Not Confirmed

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-008 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-005 (R-W3-005-004) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Commercial Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Commercial Manager |
| **Owner business unit** | Cross-Platform |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-RPT-003, ERP-GEN-001, W3S1-005 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-006, RC-TECH-009 |
| **Related assumptions** | HCM-RPT-003, ERP-GEN-001, ERP-GEN-002 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3, 7, 8, 9 |
| **Assembly priority** | Critical |
| **Mandatory if** | feature_licensing_confirmed = FALSE AND engagement_type = "Implementation" |
| **Optional if** | feature_licensing_confirmed = TRUE |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Broader than RC-TECH-006 (which is OAX-specific). Applies to any Oracle feature with separate licensing dependency. See DG-008. |

**Risk description:** APPSolve's implementation scope includes Oracle features that are licensed separately from the core Oracle Cloud subscription (e.g., AI/ML capabilities, specific module extensions, additional user types). If the client's Oracle contract does not include these features, APPSolve cannot configure them until the commercial issue is resolved, delaying that deliverable.

**Standard mitigation:** APPSolve conducts a Licence Verification at project kick-off, cross-checking the delivery scope against the client's Oracle order document. Any licensing gaps are flagged within the first two weeks and resolved before the relevant workstream commences.

**Customisation guidance:** Cross-reference the client's Oracle order document during proposal preparation. Include a specific licence confirmation step in the project methodology.

---

### RC-TECH-009 — ODA Scope Added Without Separate License Confirmation

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-009 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-005 (R-W3-005-006) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Commercial Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Commercial Manager |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2027-06-26 |
| **Confidence level** | Medium |
| **Source assets** | HCM-RPT-003, W3S1-005 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-008 |
| **Related assumptions** | HCM-RPT-003 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2 |
| **Assembly priority** | Standard |
| **Mandatory if** | oda_in_scope = TRUE AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | oda_in_scope = FALSE |
| **Governance notes** | ODA = Oracle Digital Assistant. |

**Risk description:** Oracle Digital Assistant (ODA) is added to the HCM scope (e.g., as a conversational HR chatbot) without confirming that the client holds an ODA licence. ODA is separately licensed from Oracle HCM Cloud. Committing to ODA delivery without licence confirmation creates a commercial risk.

**Standard mitigation:** APPSolve confirms ODA licence status at project kick-off. ODA configuration does not commence until the licence is confirmed active in the client's Oracle tenancy.

**Customisation guidance:** Only include where ODA or chatbot/conversational HR is explicitly in the client's scope.

---

### RC-TECH-010 — Digital Channel Complexity Beyond Standard Configuration

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-010 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Help Desk |
| **Engagement types** | AMS |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-006 (R-W3-006-001) |
| **Likelihood** | Low |
| **Impact** | Low |
| **Rating** | LOW |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2027-06-26 |
| **Confidence level** | Medium |
| **Source assets** | AMS-CHN-001, AMS-CHN-002, AMS-CHN-003, AMS-CHN-004, W3S1-006 |
| **Supersedes** | — |
| **Related risks** | RC-CLIENT-006, RC-COMM-002 |
| **Related assumptions** | AMS-CHN-001, AMS-CHN-002, AMS-CHN-003, AMS-CHN-004 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-73, S-12 |
| **Proposal patterns** | 13 |
| **Assembly priority** | Standard |
| **Mandatory if** | engagement_type = "AMS" AND digital_channels = TRUE |
| **Optional if** | — |
| **Excluded if** | engagement_type != "AMS" |
| **Governance notes** | AMS-only risk. Pattern 13 exclusive. |

**Risk description:** The client requests digital HR service channel configuration (chatbot, employee self-service portal customisation, knowledge base taxonomy) that exceeds the standard Oracle Help Desk / HR Assist configuration scope under the AMS arrangement. Additional configuration effort is required that was not included in the AMS retainer.

**Standard mitigation:** APPSolve's AMS scope defines the included digital channel configuration per AMS-CHN-001 through AMS-CHN-004. Channel enhancements beyond the defined scope are raised as Change Requests under the AMS Change Request process.

**Customisation guidance:** AMS proposals only. Include in the AMS risk section alongside RC-CLIENT-006 and RC-COMM-002.

---

### RC-TECH-011 — Career Site Design Complexity Exceeds Standard Scope

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-011 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Recruiting Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-006 (R-W3-006-005) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | Medium |
| **Source assets** | REC-SIT-001, REC-SIT-002, REC-SIT-003, REC-SIT-004, REC-SIT-005, W3S1-006 |
| **Supersedes** | — |
| **Related risks** | RC-CLIENT-003 |
| **Related assumptions** | REC-SIT-001, REC-SIT-002, REC-SIT-003, REC-SIT-004, REC-SIT-005 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 4, 1, 2 |
| **Assembly priority** | Standard |
| **Mandatory if** | modules CONTAINS "Oracle Recruiting" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | NOT modules CONTAINS "Oracle Recruiting" |
| **Governance notes** | — |

**Risk description:** The client requests a career site design (branding, layout, custom pages, interactive elements) that exceeds Oracle's standard Career Site Builder capability. Custom HTML/CSS, animated components, or multi-page microsites require development effort beyond standard configuration scope per REC-SIT-002.

**Standard mitigation:** APPSolve's career site configuration scope is defined per REC-SIT-001 and REC-SIT-002. Standard branding (logo, colour, typography) is included. Custom design elements beyond Oracle's standard builder toolset are assessed and priced as scope additions.

**Customisation guidance:** Mandatory for Recruiting Standalone proposals (Pattern 4). For full HCM suite proposals with Recruiting, include as a secondary risk. Obtain the client's employer brand guidelines at qualification.

---

### RC-TECH-012 — Annual SA Legislative Change Not Reflected in Integrations

| Field | Value |
|---|---|
| **Risk ID** | RC-TECH-012 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle OIC |
| **Engagement types** | Implementation / AMS |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-009 (R-W9-007) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Integration Lead |
| **Lifecycle status** | APPROVED |
| **Owner role** | Integration Lead |
| **Owner business unit** | Oracle OIC |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | OIC-DES-001, AMS-REL-001, W3S1-009 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-001, RC-INT-004, RC-COMP-001 |
| **Related assumptions** | OIC-DES-001, AMS-REL-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12, S-73 |
| **Proposal patterns** | 3, 6, 13 |
| **Assembly priority** | High |
| **Mandatory if** | country = "ZA" AND payroll_integration = TRUE |
| **Optional if** | — |
| **Excluded if** | country != "ZA" |
| **Governance notes** | Rating recalculated in V1.0: CRITICAL (High × High). Annual South African legislative changes (tax tables, UIF rates, SDL contributions) are certain events, not low-probability risks. |

**Risk description:** Annual South African legislative changes (National Budget tax table updates, UIF rate changes, SDL rate changes) require updates to payroll integration field mappings and transformation logic. If the integration is not updated before the legislative effective date (typically 1 March), the integration will produce non-compliant payroll output.

**Standard mitigation:** For AMS engagements, APPSolve includes an annual legislative update cycle per AMS-REL-001. Legislative updates affecting the OIC integration are assessed and scheduled before 1 March each year. For post-implementation support, APPSolve provides an annual update service under a separate support arrangement.

**Customisation guidance:** Mandatory for all South African OIC and payroll integration proposals. For AMS proposals, describe the annual update process in S-73. For implementation proposals, describe the post-go-live update scope boundary.

---

## RC-CLIENT — Client Risk (7 entries)

---

### RC-CLIENT-001 — Super-User Availability Insufficient During UAT

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-001 |
| **Category** | RC-CLIENT — Client Risk |
| **Platforms** | All Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-003 (R-W3-003-002) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Project Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Project Manager |
| **Owner business unit** | Cross-Platform |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | HCM-TST-001, HCM-TST-002, HCM-TST-003, ERP-TST-001, W3S1-003 |
| **Supersedes** | — |
| **Related risks** | RC-CLIENT-002 |
| **Related assumptions** | HCM-TST-001, HCM-TST-002, HCM-TST-003, HCM-TST-004, HCM-TST-005, HCM-TST-006, HCM-TST-007, HCM-TST-008, ERP-TST-001, ERP-TST-002, ERP-TST-003, ERP-TST-004, ERP-TST-005, ERP-TST-006 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 |
| **Assembly priority** | High |
| **Mandatory if** | engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" OR engagement_type = "DBA" |
| **Governance notes** | — |

**Risk description:** The client's business super-users (process owners who validate system behaviour during UAT) are not available for the planned UAT period due to competing business priorities. Insufficient super-user participation causes incomplete test coverage, deferred defect resolution, and delayed UAT sign-off.

**Standard mitigation:** APPSolve's project plan includes a UAT Resource Commitment requirement. The client is required to identify and commit named super-users per HCM-TST-001. UAT availability is confirmed at project kick-off and reviewed at each project steering committee. UAT defects cannot be signed off without super-user confirmation.

**Customisation guidance:** For all implementation proposals. Explicitly list the required number of super-users per workstream in the proposal's Client Responsibilities section.

---

### RC-CLIENT-002 — Client Prerequisite Systems or Accounts Not Available

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-002 |
| **Category** | RC-CLIENT — Client Risk |
| **Platforms** | Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-003 (R-W3-003-004) |
| **Likelihood** | Low |
| **Impact** | High |
| **Rating** | MEDIUM |
| **Owner** | Project Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Project Manager |
| **Owner business unit** | Cross-Platform |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | HCM-CUS-001, HCM-CUS-002, HCM-CUS-003, ERP-CUS-001, ERP-CUS-002, W3S1-003 |
| **Supersedes** | — |
| **Related risks** | RC-CLIENT-001 |
| **Related assumptions** | HCM-CUS-001, HCM-CUS-002, HCM-CUS-003, HCM-CUS-004, HCM-CUS-005, ERP-CUS-001, ERP-CUS-002, ERP-CUS-003 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3, 7, 8, 9, 11 |
| **Assembly priority** | Standard |
| **Mandatory if** | engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | — |

**Risk description:** The client's prerequisite systems (Oracle tenant provisioned, identity provider configured, network access granted, SSO established) are not ready at the time APPSolve begins the implementation. Missing prerequisites block the Configuration workstream from starting and consume project time while awaiting client action.

**Standard mitigation:** APPSolve provides a Pre-Project Prerequisites Checklist at contract signature. The checklist confirms Oracle tenant provisioning, SSO configuration, network access, and user access. Prerequisites must be confirmed complete before the project kick-off date.

**Customisation guidance:** For new Oracle tenants, confirm the Oracle provisioning lead time during qualification. For SSO implementations, confirm the client's identity provider readiness.

---

### RC-CLIENT-003 — Onboarding Task and Workflow Ownership Not Defined

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-003 |
| **Category** | RC-CLIENT — Client Risk |
| **Platforms** | Oracle Recruiting / Oracle HCM |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-004 (R-W3-004-007) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | Medium |
| **Source assets** | HCM-CUS-001, HCM-CUS-002, REC-SIT-003, W3S1-004 |
| **Supersedes** | — |
| **Related risks** | RC-CLIENT-007 |
| **Related assumptions** | HCM-CUS-001, HCM-CUS-002, HCM-CUS-003, HCM-CUS-004 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 4 |
| **Assembly priority** | Standard |
| **Mandatory if** | modules CONTAINS "Oracle Recruiting" AND engagement_type = "Implementation" |
| **Optional if** | modules CONTAINS "Oracle HCM" AND NOT modules CONTAINS "Oracle Recruiting" |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | — |

**Risk description:** The business ownership of onboarding tasks, document checklists, and workflow approvals is not defined before Oracle Onboarding is configured. Without confirmed ownership, APPSolve cannot configure approval routing and task assignment, causing configuration to proceed with placeholder owners that must be reworked later.

**Standard mitigation:** APPSolve includes an Onboarding Design workshop early in the Recruiting configuration workstream. Client stakeholders are required to confirm task ownership and workflow routing per HCM-CUS-001 before onboarding configuration begins.

**Customisation guidance:** Mandatory for Recruiting Standalone proposals (Pattern 4). Optional for full HCM suite proposals where Onboarding is in scope.

---

### RC-CLIENT-004 — Learning Catalog Not Ready at System Go-Live

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-004 |
| **Category** | RC-CLIENT — Client Risk |
| **Platforms** | Oracle Learning Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-006 (R-W3-006-002) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | LRN-CON-001, LRN-CON-002, LRN-CON-003, LRN-DAT-001, W3S1-006 |
| **Supersedes** | — |
| **Related risks** | RC-DATA-002 |
| **Related assumptions** | LRN-CON-001, LRN-CON-002, LRN-CON-003, LRN-CON-004, LRN-CON-005, LRN-DAT-001, LRN-DAT-002, LRN-DAT-003, LRN-DAT-004 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 5, 1, 2 |
| **Assembly priority** | High |
| **Mandatory if** | modules CONTAINS "Oracle Learning" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | NOT modules CONTAINS "Oracle Learning" |
| **Governance notes** | Rating recalculated in V1.0: CRITICAL (High × High). Learning system go-live without catalog content is operationally useless. |

**Risk description:** The client's learning catalog (course library, learning items, specialisations, required training assignments) is not loaded or ready at the Oracle Learning go-live date. A learning system without content cannot be used by employees, undermining the business case for the implementation.

**Standard mitigation:** APPSolve includes a Learning Catalog Readiness milestone in the project plan. Content ownership and loading responsibility is assigned to the client per LRN-CON-001. APPSolve provides the catalog loading template and upload tooling. A minimum catalog of mandatory compliance courses must be ready two weeks before go-live.

**Customisation guidance:** Mandatory for Learning Standalone proposals (Pattern 5). For full HCM suite proposals with Learning, include as a high-priority risk. Confirm the client's L&D team resource commitment during qualification.

---

### RC-CLIENT-005 — Performance Rating Data Unavailable for Compensation Cycle

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-005 |
| **Category** | RC-CLIENT — Client Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-005 (R-W3-005-007) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Functional Consultant |
| **Lifecycle status** | APPROVED |
| **Owner role** | Functional Consultant |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | Medium |
| **Source assets** | TLT-PER-001, TLT-PER-002, TLT-PER-003, COM-DAT-001, W3S1-005 |
| **Supersedes** | — |
| **Related risks** | RC-CLIENT-007 |
| **Related assumptions** | TLT-PER-001, TLT-PER-002, TLT-PER-003, TLT-PER-004, TLT-PER-005, TLT-PER-006, COM-DAT-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2 |
| **Assembly priority** | Standard |
| **Mandatory if** | modules CONTAINS "Oracle Compensation" AND modules CONTAINS "Oracle Talent" AND engagement_type = "Implementation" |
| **Optional if** | modules CONTAINS "Oracle Compensation" AND NOT modules CONTAINS "Oracle Talent" |
| **Excluded if** | NOT modules CONTAINS "Oracle Compensation" |
| **Governance notes** | — |

**Risk description:** The first Oracle Workforce Compensation cycle requires performance ratings as an input to merit calculations. If the Talent Management module has not yet completed the first performance review cycle, or if historical performance ratings are not loaded, the compensation cycle cannot run as designed.

**Standard mitigation:** APPSolve's project plan sequences the Talent and Compensation modules so that the first performance review cycle completes before the Compensation cycle is configured. Historical performance data requirements are confirmed per TLT-PER-001 and COM-DAT-001 at project commencement.

**Customisation guidance:** Only include where both Talent Management and Compensation are in scope. Where Compensation is standalone without Talent, revise the mitigation to address proxy rating inputs.

---

### RC-CLIENT-006 — Knowledge Base Content Ownership Undefined

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-006 |
| **Category** | RC-CLIENT — Client Risk |
| **Platforms** | Oracle Help Desk |
| **Engagement types** | AMS |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-006 (R-W3-006-006) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Project Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Project Manager |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | Medium |
| **Source assets** | AMS-CHN-001, AMS-CHN-002, AMS-CHN-003, AMS-CHN-004, W3S1-006 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-010, RC-COMM-002 |
| **Related assumptions** | AMS-CHN-001, AMS-CHN-002, AMS-CHN-003, AMS-CHN-004 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-73, S-12 |
| **Proposal patterns** | 13 |
| **Assembly priority** | Standard |
| **Mandatory if** | engagement_type = "AMS" AND help_desk_in_scope = TRUE |
| **Optional if** | — |
| **Excluded if** | engagement_type != "AMS" |
| **Governance notes** | AMS-only. Pattern 13 exclusive. |

**Risk description:** The Oracle HR Help Desk knowledge base requires client HR team authorship and maintenance. If ownership of knowledge base content (articles, FAQs, HR policy summaries) is not assigned to a named client resource, the knowledge base remains empty or outdated, reducing self-service resolution rates and increasing ticket volumes.

**Standard mitigation:** APPSolve's AMS service includes knowledge base configuration and initial content seeding per AMS-CHN-001. Ongoing content authorship is the client's responsibility. APPSolve's AMS scope includes quarterly content review, not continuous authorship.

**Customisation guidance:** AMS proposals with Oracle HR Help Desk only. Include in the AMS risk section alongside RC-TECH-010 and RC-COMM-002.

---

### RC-CLIENT-007 — Cross-Functional Alignment on Design Frameworks

| Field | Value |
|---|---|
| **Risk ID** | RC-CLIENT-007 |
| **Category** | RC-CLIENT — Client Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-005 (R-W3-005-008) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-ORG-001, HCM-CHG-001, HCM-CHG-002, HCM-CHG-003, W3S1-005 |
| **Supersedes** | — |
| **Related risks** | RC-PROJ-001, RC-PROJ-003, RC-CLIENT-003 |
| **Related assumptions** | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008, HCM-CHG-001, HCM-CHG-002, HCM-CHG-003, HCM-CHG-004 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 1, 2, 3 |
| **Assembly priority** | Critical |
| **Mandatory if** | platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation" |
| **Optional if** | — |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Rating recalculated in V1.0: CRITICAL (High × High). The single most complex client-side governance risk in HCM implementations. |

**Risk description:** Different client business units (HR, Finance, Payroll, IT) have conflicting views on how core HCM frameworks (job architecture, grade structure, position management approach) should be designed. Without a single client-side decision-maker with authority to resolve cross-functional disagreements, design workshops stall, rework cycles increase, and the project timeline expands.

**Standard mitigation:** APPSolve requires a named Project Sponsor with authority to resolve cross-functional design disputes per HCM-ORG-001 and HCM-CHG-001. A Design Authority structure is established at project kick-off. Cross-functional disagreements that cannot be resolved within one sprint are escalated to the Project Sponsor.

**Customisation guidance:** Mandatory for all HCM full suite proposals. For clients undergoing organisational transformation (mergers, restructuring), increase likelihood to High and explicitly reference the change management risk cross-reference.

---

## RC-COMM — Commercial Risk (3 entries)

---

### RC-COMM-001 — Analytics Expectations Misaligned With Platform Capability

| Field | Value |
|---|---|
| **Risk ID** | RC-COMM-001 |
| **Category** | RC-COMM — Commercial Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-004 (R-W3-004-002), W3S1-005 (R-W3-005-003), W3S1-006 (R-W3-006-003) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle Analytics |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-RPT-003, W3S1-004, W3S1-005, W3S1-006 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-006, RC-TECH-007 |
| **Related assumptions** | HCM-RPT-003 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2 |
| **Assembly priority** | Critical |
| **Mandatory if** | oax_in_scope = TRUE OR analytics_requirements_in_tender = TRUE |
| **Optional if** | analytics_requirements_in_tender = FALSE |
| **Excluded if** | — |
| **Governance notes** | Merged from three source risks (DG-005): R-W3-004-002, R-W3-005-003, R-W3-006-003. All described analytics expectation misalignment with same root cause. Rating recalculated in V1.0: CRITICAL (High × High). |

**Risk description:** The client expects advanced people analytics dashboards, predictive modelling, or custom report development as part of the HCM implementation. Oracle HCM's native reporting (OTBI, HCM Extracts) and OAX have defined capabilities and data model constraints. Expectations that exceed these constraints (real-time streaming analytics, AI-predictive attrition models, external BI platform integration) require separate scoping and are not included in the standard implementation.

**Standard mitigation:** APPSolve conducts an Analytics Requirements workshop during Scoping and Design. Deliverable reports and dashboards are enumerated and confirmed against OAX and OTBI capability. Requirements outside standard capability are assessed for custom development (separately priced) or deferred. The analytics scope is documented in the Reporting Design Specification.

**Customisation guidance:** Mandatory for any proposal where analytics, reporting, or dashboards are mentioned in the tender. Reference HCM-RPT-003 as the licensing boundary. Cross-reference RC-TECH-006.

---

### RC-COMM-002 — Oracle HR Help Desk Conflated With Oracle Service Cloud

| Field | Value |
|---|---|
| **Risk ID** | RC-COMM-002 |
| **Category** | RC-COMM — Commercial Risk |
| **Platforms** | Oracle Help Desk |
| **Engagement types** | AMS |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-006 (R-W3-006-007) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Commercial Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Commercial Manager |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | AMS-CHN-001, AMS-CHN-002, W3S1-006 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-010, RC-CLIENT-006 |
| **Related assumptions** | AMS-CHN-001, AMS-CHN-002 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-73, S-12 |
| **Proposal patterns** | 13 |
| **Assembly priority** | Critical |
| **Mandatory if** | help_desk_in_scope = TRUE AND engagement_type = "AMS" |
| **Optional if** | — |
| **Excluded if** | NOT help_desk_in_scope = TRUE |
| **Governance notes** | Rating recalculated in V1.0: CRITICAL (High × High). This misidentification has been the source of commercial disputes on past proposals. |

**Risk description:** The client (or the tender evaluator) misidentifies Oracle HR Help Desk (the HR service request management module within Oracle HCM) as Oracle Service Cloud (B2C customer service platform). The two products have fundamentally different architectures, licensing models, and implementation scope. A proposal written against Oracle Service Cloud requirements when the client has Oracle HR Help Desk (or vice versa) will be non-compliant.

**Standard mitigation:** APPSolve qualifies the specific Oracle product required at pre-sales. The proposal explicitly names the product ("Oracle HR Help Desk — part of Oracle HCM Cloud") and does not use the generic term "Service Cloud". The scope boundary is confirmed in the Scope section of the proposal and referenced in AMS-CHN-001.

**Customisation guidance:** Mandatory for all AMS proposals referencing Help Desk, HR service request management, or employee case management. Include the product clarification note in the proposal executive summary.

---

### RC-COMM-003 — Integration Method Commitment in Tender Creates Exposure

| Field | Value |
|---|---|
| **Risk ID** | RC-COMM-003 |
| **Category** | RC-COMM — Commercial Risk |
| **Platforms** | Acumatica / Oracle |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-007 (R-W7-005) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Commercial Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Commercial Manager |
| **Owner business unit** | Acumatica |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | Medium |
| **Source assets** | ACU-INT-001, OIC-DES-001, W3S1-007 |
| **Supersedes** | — |
| **Related risks** | RC-INT-002, RC-INT-007 |
| **Related assumptions** | ACU-INT-001, OIC-DES-001 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-38, S-12 |
| **Proposal patterns** | 3, 6, 11 |
| **Assembly priority** | Standard |
| **Mandatory if** | integration_method_prescribed_in_tender = TRUE |
| **Optional if** | integration_method_prescribed_in_tender = FALSE |
| **Excluded if** | engagement_type = "AMS" |
| **Governance notes** | Primarily relevant to Acumatica (Pattern 11) and OIC standalone (Pattern 6). |

**Risk description:** The tender document requires the proposer to commit to a specific integration method (API, file-based, middleware) before the full integration scope has been assessed. Committing to a specific method without conducting an Integration Discovery may expose APPSolve to claims that the committed method is not technically achievable, or may foreclose the use of a more appropriate method discovered during the project.

**Standard mitigation:** APPSolve's proposals note that integration method selection is subject to a formal Integration Discovery workshop at project commencement. The proposed method represents APPSolve's current best assessment based on available information. Confirmed method and scope is documented in the Integration Design Specification per OIC-DES-001 or ACU-INT-001.

**Customisation guidance:** Where the tender requires a specific method commitment, flag this risk explicitly. Include a qualification note in the proposal's integration section.

---

## RC-OPS — Operational Risk (1 entry)

---

### RC-OPS-001 — First Live Operational Cycle High-Stakes Risk

| Field | Value |
|---|---|
| **Risk ID** | RC-OPS-001 |
| **Category** | RC-OPS — Operational Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-009 (R-W9-008) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Project Manager |
| **Lifecycle status** | APPROVED |
| **Owner role** | Project Manager |
| **Owner business unit** | Cross-Platform |
| **Review frequency** | Quarterly |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-09-26 |
| **Confidence level** | High |
| **Source assets** | HCM-CUT-001, HCM-CUT-002, HCM-HYP-001, HCM-HYP-002, AMS-SLA-001, AMS-SLA-002, W3S1-009 |
| **Supersedes** | — |
| **Related risks** | RC-INT-001, RC-INT-005, RC-DATA-001, RC-DATA-003 |
| **Related assumptions** | HCM-CUT-001, HCM-CUT-002, HCM-CUT-003, HCM-CUT-004, HCM-CUT-005, HCM-CUT-006, HCM-CUT-007, HCM-CUT-008, HCM-HYP-001, HCM-HYP-002, HCM-HYP-003, HCM-HYP-004, HCM-HYP-005, AMS-SLA-001, AMS-SLA-002, AMS-SLA-005, ERP-CUT-001, ERP-CUT-002, ERP-CUT-003, ERP-CUT-004, ERP-CUT-005, ERP-HYP-001, ERP-HYP-002, ERP-HYP-003, ERP-HYP-004 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-71, S-72, S-12 |
| **Proposal patterns** | 1, 2, 3, 4, 5, 7, 8, 9, 11, 13 |
| **Assembly priority** | Critical |
| **Mandatory if** | TRUE |
| **Optional if** | — |
| **Excluded if** | engagement_type = "DBA" |
| **Governance notes** | Only risk in the register with mandatory_if = TRUE (unconditional inclusion). Applies to all implementation and AMS proposals. WP18B-EXT.2 BU-RL-020 (Option A): BU Lead confirmed mandatory_if = TRUE; Pattern 10 (DBA) exclusion is the sole exception. |

**Risk description:** The first live operational cycle (first payroll run, first month-end close, first HR report submission) on the new system is the highest-risk event in any implementation. Unforeseen system behaviour, data quality issues, or process gaps that were not surfaced during UAT manifest under real-world conditions, with direct impact on employees, finances, or regulatory reporting.

**Standard mitigation:** APPSolve's project plan includes a Hypercare period of a minimum of four weeks post-go-live, during which the implementation team provides elevated support per HCM-HYP-001. The Cutover Plan includes rollback procedures for critical failure scenarios per HCM-CUT-001. The first payroll run is conducted in parallel with the legacy system where commercially agreed.

**Customisation guidance:** Always include. For payroll-integrated implementations, cross-reference RC-INT-001 and RC-INT-005. For AMS proposals, the SLA framework (S-71) governs ongoing operational risk management. Include hypercare duration and exit criteria in the proposal methodology.

---

## RC-COMP — Compliance Risk (1 entry)

---

### RC-COMP-001 — POPIA Non-Compliance in HR or Payroll Data Handling

| Field | Value |
|---|---|
| **Risk ID** | RC-COMP-001 |
| **Category** | RC-COMP — Compliance Risk |
| **Platforms** | Oracle HCM Cloud / Oracle OIC |
| **Engagement types** | Implementation / AMS |
| **Version** | 1.0 |
| **Approved for reuse** | Yes |
| **Source** | W3S1-008 (R-W8-007), W3S1-009 (R-W9-005) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Solution Architect |
| **Lifecycle status** | APPROVED |
| **Owner role** | Solution Architect |
| **Owner business unit** | Oracle HCM |
| **Review frequency** | Bi-annually |
| **Last reviewed** | 2026-06-26 |
| **Next review** | 2026-12-26 |
| **Confidence level** | High |
| **Source assets** | OIC-SEC-001, OIC-SEC-002, HCM-SEC-001, HCM-SEC-002, BB-DAT-006, W3S1-008, W3S1-009 |
| **Supersedes** | — |
| **Related risks** | RC-TECH-012 |
| **Related assumptions** | OIC-SEC-001, OIC-SEC-002, OIC-SEC-003, OIC-SEC-004, OIC-SEC-005, OIC-SEC-006, BB-DAT-006, HCM-SEC-001, HCM-SEC-002, HCM-SEC-003, HCM-SEC-004, HCM-SEC-005, HCM-SEC-006, HCM-SEC-007, HCM-SEC-008 |
| **Proposal sections** | Primary: S-50. Secondary: S-37, S-12 |
| **Proposal patterns** | 1, 2, 3, 12, 13 |
| **Assembly priority** | High |
| **Mandatory if** | country = "ZA" AND (personal_data_in_scope = TRUE OR payroll_integration = TRUE) |
| **Optional if** | country != "ZA" |
| **Excluded if** | — |
| **Governance notes** | Merged from R-W8-007 and R-W9-005 (DG-007). Both described POPIA compliance risk in different but related contexts. POPIA = Protection of Personal Information Act (South Africa). |

**Risk description:** HR and payroll data contains personal information regulated under POPIA. APPSolve processes this data as an operator (data processor) on behalf of the client (responsible party). Non-compliance risks arise from: inadequate data minimisation, unlawful cross-border data transfer, uncontrolled access to employee records, or integration patterns that expose personal data to non-compliant endpoints.

**Standard mitigation:** APPSolve operates Oracle HCM, OIC, and BeBanking within the POPIA operator framework per HCM-SEC-001 through HCM-SEC-008, OIC-SEC-001 through OIC-SEC-006, and BB-DAT-006. The client, as responsible party, is accountable for the lawful basis for processing. APPSolve provides a Data Processing Agreement (DPA) as part of the implementation contract. POPIA compliance controls are documented in the Security Architecture section of the proposal.

**Customisation guidance:** Mandatory for all South African proposals involving personal data (HCM, payroll, BeBanking). For BeBanking proposals (Pattern 12), reference BB-DAT-006. Include a POPIA scope statement in the proposal's executive summary.
