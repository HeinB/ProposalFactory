---
title: "Enterprise Risk Register — Draft v0.1"
status: "DRAFT — Pending BU Lead Review"
version: "0.1"
created: "2026-06-26"
created_by: "WP18B-EXT.1 — Risk Library Foundation"
approved_for_reuse: "No — all entries pending BU Lead approval"
next_action: "BU Lead review and approval of all 40 entries → WP18B-EXT.2"
canonical_count: 40
source_risks_audited: 51
categories_covered: 8
categories_with_no_source: "RC-RES, RC-INFRA, RC-CM, RC-MIG, RC-CUT, RC-3P, RC-SEC"
---

# Enterprise Risk Register — Draft v0.1

**Work Package:** WP18B-EXT.1 — Risk Library Foundation  
**Status:** DRAFT — Pending BU Lead Review  
**Date:** 2026-06-26  

This file is the canonical enterprise risk register produced by the WP18B-EXT.1 audit. It consolidates 51 source risks from 10 governed capability assets into 40 deduplicated canonical risk entries. All entries use the schema defined in `RISK_LIBRARY_STANDARD.md`.

**No entry in this file may be used in a proposal risk register until `approved_for_reuse` is set to `Yes` by the BU Lead.**

---

## Quick-Reference Index

| Risk ID | Title | Category | Rating | Platforms | Engagement |
|---------|-------|----------|--------|-----------|------------|
| RC-PROJ-001 | Module design not signed off before build | RC-PROJ | HIGH | Oracle HCM | Implementation |
| RC-PROJ-002 | Upstream phase not stable when dependent phase begins | RC-PROJ | HIGH | Oracle HCM | Implementation |
| RC-PROJ-003 | Organisational design decisions made late | RC-PROJ | HIGH | Oracle HCM | Implementation |
| RC-PROJ-004 | Configuration milestone changed after sign-off | RC-PROJ | LOW | Oracle Cloud | Implementation |
| RC-DATA-001 | Legacy HR data quality causes migration delays | RC-DATA | HIGH | Oracle HCM | Implementation |
| RC-DATA-002 | Client content format incompatible with platform | RC-DATA | MEDIUM | Oracle Learning | Implementation |
| RC-DATA-003 | HCM data quality produces invalid payroll input | RC-DATA | HIGH | Oracle HCM / OIC | Implementation |
| RC-DATA-004 | Biometric enrolment data does not match HR records | RC-DATA | HIGH | Oracle WFM | Implementation |
| RC-DATA-005 | Demand/scheduling data unavailable | RC-DATA | LOW | Oracle WFM | Implementation |
| RC-INT-001 | Payroll integration timeline not aligned to HCM go-live | RC-INT | HIGH | Oracle HCM / OIC | Implementation |
| RC-INT-002 | Third-party integration scope underestimated | RC-INT | MEDIUM | Oracle Cloud / OIC | Implementation |
| RC-INT-003 | Third-party API unavailable at integration build start | RC-INT | HIGH | Oracle OIC | Implementation |
| RC-INT-004 | Payroll API version changes post-go-live | RC-INT | MEDIUM | Oracle OIC | Implementation / AMS |
| RC-INT-005 | Integration schedule not aligned to payroll cutoff | RC-INT | HIGH | Oracle OIC | Implementation |
| RC-INT-006 | Integration field mapping errors produce incorrect data | RC-INT | HIGH | Oracle OIC | Implementation |
| RC-INT-007 | Bespoke payroll mapping beyond standard patterns | RC-INT | MEDIUM | Acumatica / Oracle | Implementation |
| RC-TECH-001 | Quarterly SaaS update breaks configured functionality | RC-TECH | LOW | Oracle Cloud | Implementation / AMS |
| RC-TECH-002 | SETA/WSP/ATR extract complexity | RC-TECH | MEDIUM | Oracle HCM | Implementation |
| RC-TECH-003 | Absence rules complexity exceeds standard scope | RC-TECH | HIGH | Oracle WFM | Implementation |
| RC-TECH-004 | Time and labour rules complexity exceeds estimate | RC-TECH | MEDIUM | Oracle WFM | Implementation |
| RC-TECH-005 | BCEA overtime calculation requires additional config | RC-TECH | MEDIUM | Oracle WFM | Implementation |
| RC-TECH-006 | OAX licensing not confirmed before commitment | RC-TECH | HIGH | Oracle HCM | Implementation |
| RC-TECH-007 | OAX data model not aligned to HCM configuration | RC-TECH | LOW | Oracle HCM Analytics | Implementation |
| RC-TECH-008 | Oracle product licensing for dependent features not confirmed | RC-TECH | HIGH | Oracle Cloud | Implementation |
| RC-TECH-009 | ODA scope added without separate license confirmation | RC-TECH | LOW | Oracle Cloud | Implementation |
| RC-TECH-010 | Digital channel complexity beyond standard configuration | RC-TECH | LOW | Oracle Help Desk | Implementation |
| RC-TECH-011 | Career site design complexity exceeds standard scope | RC-TECH | MEDIUM | Oracle Recruiting | Implementation |
| RC-TECH-012 | Annual SA legislative change not reflected in integrations | RC-TECH | HIGH | Oracle OIC | Implementation / AMS |
| RC-CLIENT-001 | Super-user availability insufficient during UAT | RC-CLIENT | MEDIUM | All Oracle | Implementation |
| RC-CLIENT-002 | Client prerequisite systems or accounts not available | RC-CLIENT | LOW | Oracle Cloud | Implementation |
| RC-CLIENT-003 | Onboarding task and workflow ownership not defined | RC-CLIENT | MEDIUM | Oracle Recruiting / HCM | Implementation |
| RC-CLIENT-004 | Learning catalog not ready at system go-live | RC-CLIENT | HIGH | Oracle Learning | Implementation |
| RC-CLIENT-005 | Performance rating data unavailable for compensation cycle | RC-CLIENT | MEDIUM | Oracle HCM | Implementation |
| RC-CLIENT-006 | Knowledge base content ownership undefined | RC-CLIENT | MEDIUM | Oracle Help Desk | Implementation |
| RC-CLIENT-007 | Cross-functional alignment on design frameworks | RC-CLIENT | HIGH | Oracle HCM | Implementation |
| RC-COMM-001 | Analytics expectations misaligned with platform capability | RC-COMM | HIGH | Oracle HCM | Implementation |
| RC-COMM-002 | Oracle HR Help Desk conflated with Oracle Service Cloud | RC-COMM | HIGH | Oracle Help Desk | Implementation |
| RC-COMM-003 | Integration method commitment in tender creates exposure | RC-COMM | MEDIUM | Acumatica / Oracle | Implementation |
| RC-OPS-001 | First live operational cycle high-stakes risk | RC-OPS | CRITICAL | Oracle HCM | Implementation |
| RC-COMP-001 | POPIA non-compliance in HR or payroll data handling | RC-COMP | MEDIUM | Oracle HCM / OIC | Implementation / AMS |

---

## RC-PROJ — Project Risks

---

### RC-PROJ-001 — Module Design Not Signed Off Before Build Begins

| Field | Value |
|-------|-------|
| **Risk ID** | RC-PROJ-001 |
| **Category** | RC-PROJ — Project Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-002 (R-W2-001), W3S1-005 (R-W3-005-001) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Project Manager |

**Risk description:** Oracle HCM module architecture, configuration design, or functional specification is not completed and signed off by the client before the build phase begins. The project proceeds into configuration without an agreed blueprint, resulting in rework, missed milestones, and scope disputes when client stakeholders request design changes during or after build.

**Standard mitigation:** Mandate a formal Design Sign-Off Gate — no build activity commences until the module architecture and configuration workbook are approved in writing by the client product owner. Capture the sign-off date in the Config Decision Log and escalate to the Project Sponsor if approval is delayed beyond the agreed date.

**Customisation guidance:** Elevate Likelihood to High if the client organisation has multiple competing stakeholder groups (HR, Finance, IT, Business) whose alignment is unresolved at tender stage. Include additional Design Gate milestone in the project plan if module complexity is high (e.g., compensation with flex credit plans, talent with custom matrices).

**Assembly trigger:** Include in any Oracle HCM module implementation proposal where functional configuration design precedes a distinct build phase (excludes pure AMS / break-fix engagements).

**Related assumptions:** W3S1-002 assumptions (Talent configuration design), W3S1-005 assumptions (Compensation plan architecture). Reference Config Decision Log governance assumptions.

---

### RC-PROJ-002 — Upstream Phase Not Stable When Dependent Module Phase Begins

| Field | Value |
|-------|-------|
| **Risk ID** | RC-PROJ-002 |
| **Category** | RC-PROJ — Project Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-002 (R-W2-003), W3S1-003 (R-W3-003-003) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Project Manager |

**Risk description:** A downstream Oracle HCM module (e.g., Talent Management, Recruiting Cloud) begins its design or build phase before the foundational upstream module (e.g., HCM Core) has achieved a defined stability milestone. Configuration changes in the upstream module cascade into rework in the downstream module, causing schedule slippage and additional test cycles.

**Standard mitigation:** Define explicit stability gates between phases — e.g., "HCM Core CRP 2 sign-off required before Talent Design begins." Document the gate in the project plan as a formal milestone. Assign the Project Manager responsibility to enforce the gate and escalate if upstream delays threaten the downstream schedule.

**Customisation guidance:** Elevate Likelihood to High if the programme has a compressed timeline that forces parallel workstreams in HCM Core and a dependent module. Include a phase dependency matrix in the project charter if more than two modules are being implemented concurrently.

**Assembly trigger:** Include in any multi-module Oracle HCM implementation where two or more modules are implemented sequentially or in overlapping phases.

**Related assumptions:** W3S1-001 assumptions (HCM Core readiness and milestone governance), W3S1-002 assumptions (Talent dependency on Core HR data model).

---

### RC-PROJ-003 — Organisational Design Decisions Made Late

| Field | Value |
|-------|-------|
| **Risk ID** | RC-PROJ-003 |
| **Category** | RC-PROJ — Project Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-001 (R-W1-001) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Project Manager |

**Risk description:** The client organisation does not finalise its organisational structure (legal entity hierarchy, business unit design, grade/grade step ladder, position structure) before the Oracle HCM Core configuration phase. Late changes to the org design require reconfiguration of foundational data structures, impacting all dependent modules and data migration.

**Standard mitigation:** Mandate an Organisational Design Sign-Off milestone in the Mobilize phase, executed through the Journey Design Workshop. Obtain written client approval of the org hierarchy before any configuration begins. Document org design decisions in the Configuration Workbook and treat post-sign-off changes as formal change requests.

**Customisation guidance:** Elevate Likelihood to High if the client is undergoing a concurrent merger, restructure, or HRIS consolidation. Reduce Likelihood to Low if the client is replacing an existing Oracle instance with an equivalent org structure (like-for-like upgrade).

**Assembly trigger:** Include in all Oracle HCM Core implementation proposals.

**Related assumptions:** W3S1-001 assumptions (org structure sign-off, position management design).

---

### RC-PROJ-004 — Configuration Milestone Changed After Sign-Off

| Field | Value |
|-------|-------|
| **Risk ID** | RC-PROJ-004 |
| **Category** | RC-PROJ — Project Risk |
| **Platforms** | Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-002 (R-W2-004) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Project Manager |

**Risk description:** A configuration milestone — such as a performance cycle calendar, compensation plan structure, or UAT date — is changed by the client after the project plan has been baselined and configuration has commenced against those dates. Late changes require additional configuration effort, retesting, and potentially additional Oracle support engagement.

**Standard mitigation:** Lock all configuration-dependent milestones during the Design Workshop and document them in the Configuration Workbook. Treat post-sign-off changes as formal change requests with documented effort and cost impact. Include a milestone freeze clause in the project charter.

**Customisation guidance:** Elevate Likelihood to Medium if the client has a history of scope or milestone changes in prior projects, or if the project calendar includes an annual cycle (e.g., performance management) with external dependencies (e.g., board approval of pay scales).

**Assembly trigger:** Include in proposals where configuration is tied to an annual business cycle (compensation, performance management). Optional for standard implementation proposals with no cycle-dependent milestones.

**Related assumptions:** W3S1-002 assumptions (performance management calendar governance).

---

## RC-DATA — Data Risks

---

### RC-DATA-001 — Legacy HR Data Quality Causes Migration Delays

| Field | Value |
|-------|-------|
| **Risk ID** | RC-DATA-001 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-001 (R-W1-002) |
| **Likelihood** | High |
| **Impact** | Medium |
| **Rating** | HIGH |
| **Owner** | Technical Lead |

**Risk description:** Employee and organisational data in the client's legacy HR system (HRIS, payroll, spreadsheets) contains quality issues — missing fields, non-standard formats, duplicate records, or invalid references — that are discovered only during the data migration process. Cleansing and transformation extend the migration timeline and delay the go-live date.

**Standard mitigation:** Conduct a Data Readiness Assessment in the Mobilize phase using standardised migration templates. Produce a Data Quality Report before Design concludes. Assign data cleansing as a formal client responsibility with tracked milestones. Quarantine and escalate records that cannot be resolved to a defined quality standard before cut-over.

**Customisation guidance:** Elevate Likelihood to High if the client is migrating from multiple legacy systems or has no current HRIS (manual/spreadsheet records). Elevate Impact to High if data quality issues affect foundational objects (employee identifiers, org hierarchy) that block all dependent module configuration.

**Assembly trigger:** Include in all Oracle HCM Core implementation proposals where employee data migration from a legacy system is in scope.

**Related assumptions:** W3S1-001 assumptions (data migration scope, data readiness, client data cleansing responsibility).

---

### RC-DATA-002 — Client-Managed Content Format Incompatible With Platform

| Field | Value |
|-------|-------|
| **Risk ID** | RC-DATA-002 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle Learning Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-004 (R-W3-004-003) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Technical Lead |

**Risk description:** The client's existing learning content (courses, videos, SCORM packages, documents) is in a format that is incompatible with Oracle Learning Cloud's ingestion requirements. Content conversion or re-authoring is required, and this work is not within APPSolve's standard implementation scope, causing unexpected effort or delays in making content available to learners.

**Standard mitigation:** Conduct a Content Format Review in the Scope and Design phase. Identify all content types and validate compatibility with Oracle Learning Cloud's supported formats (SCORM 1.2, SCORM 2004, xAPI, video formats). Document content conversion as a client responsibility in the project charter. If conversion tools or external authoring are required, treat as a separate procurement.

**Customisation guidance:** Elevate Likelihood to High if the client has a large legacy content library in proprietary formats (e.g., legacy LMS-specific packages). Reduce to Low if the client is authoring new content from scratch aligned to OLC standards.

**Assembly trigger:** Include in all Oracle Learning Cloud implementation proposals where the client has existing learning content to be migrated or imported.

**Related assumptions:** W3S1-004 assumptions (content migration scope and format responsibility).

---

### RC-DATA-003 — HCM Data Quality Produces Invalid Payroll Integration Input

| Field | Value |
|-------|-------|
| **Risk ID** | RC-DATA-003 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle HCM Cloud / Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-009 (R-W9-002) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Technical Lead |

**Risk description:** HCM data records (employee assignments, element entries, absence balances) contain errors or inconsistencies that cause the OIC payroll integration to generate invalid payroll input. Payroll exceptions and calculation errors are discovered in parallel run testing, requiring remediation of both the root data and the integration logic.

**Standard mitigation:** Implement data validation rules in the OIC integration layer that quarantine exception records before they reach the payroll system. Produce exception reports in every integration run. Conduct parallel payroll runs in UAT to validate output accuracy before go-live. Assign exception resolution as a client responsibility with a defined SLA.

**Customisation guidance:** Elevate Likelihood to High if the HCM system is being used for the first time (no established data quality baseline). Elevate Impact to High if payroll is the primary go-live risk and errors cannot be corrected within the payroll cycle window.

**Assembly trigger:** Include in all Oracle HCM to payroll integration proposals (OIC-mediated or direct).

**Related assumptions:** W3S1-009 assumptions (data validation approach, parallel run requirements).

---

### RC-DATA-004 — Biometric Device Enrolment Data Does Not Match HR Records

| Field | Value |
|-------|-------|
| **Risk ID** | RC-DATA-004 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle WFM / Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-007 (R-W3-007-004) |
| **Likelihood** | High |
| **Impact** | Medium |
| **Rating** | HIGH |
| **Owner** | Technical Lead |

**Risk description:** Employee records in the biometric access or time-capture device are enrolled using identifiers (badge numbers, employee codes) that do not match the corresponding Oracle HCM employee identifiers. Mismatches prevent the OIC integration from matching device records to HCM assignments, causing time entries to be rejected or silently dropped.

**Standard mitigation:** Conduct a Data Mapping Workshop before integration build to agree on the employee identifier used across systems (HCM person number, payroll assignment number, or badge number). Validate identifier alignment across HCM, biometric, and payroll systems before any OIC development begins. Assign data reconciliation as a client responsibility.

**Customisation guidance:** Elevate Likelihood to High if the client manages biometric device enrolment independently from HR (e.g., Facilities or Security department). Reduce to Medium if the client uses Oracle-issued employee IDs as the biometric enrollment key.

**Assembly trigger:** Include in all proposals where Oracle WFM includes biometric or access-control device integration via OIC.

**Related assumptions:** W3S1-007 assumptions (biometric integration scope, employee identifier governance).

---

### RC-DATA-005 — Demand or Scheduling Data Unavailable for Planning Systems

| Field | Value |
|-------|-------|
| **Risk ID** | RC-DATA-005 |
| **Category** | RC-DATA — Data Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-007 (R-W3-007-006) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Technical Lead |

**Risk description:** Historical demand, headcount, or shift-pattern data required to configure Oracle Workforce Scheduling is unavailable, incomplete, or in an incompatible format. Without sufficient demand data, schedule optimisation produces poor-quality schedules that do not reflect actual business needs, reducing the value of the scheduling module at go-live.

**Standard mitigation:** Confirm data requirements in Scope and Design. If historical demand data is unavailable, configure standard shift-pattern scheduling as a fallback — document that schedule optimisation will be available once 2–3 cycles of operational data are collected. Set client expectations explicitly in the project charter.

**Customisation guidance:** Elevate Likelihood to Medium if the client has no prior workforce planning system. Reduce to Low if the client already has operational shift patterns that can be directly imported.

**Assembly trigger:** Include in proposals where Oracle WFM Workforce Scheduling is in scope with demand-based optimisation.

**Related assumptions:** W3S1-007 assumptions (scheduling data availability, shift pattern requirements).

---

## RC-INT — Integration Risks

---

### RC-INT-001 — Third-Party Payroll Integration Timeline Not Aligned to HCM Go-Live

| Field | Value |
|-------|-------|
| **Risk ID** | RC-INT-001 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle HCM Cloud / Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-001 (R-W1-003) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Project Manager |

**Risk description:** The third-party payroll system (PaySpace, SAP Payroll, VIP, or equivalent) implementation timeline is managed independently of the Oracle HCM programme, and the two systems are not ready to integrate at the agreed go-live date. This forces a delayed go-live, a manual payroll extraction bridge, or a parallel-run extension — all of which carry additional cost and risk.

**Standard mitigation:** Initiate payroll system readiness discussions in the Journey Workshop as a named dependency. List the payroll system vendor as a formal programme dependency in the project charter. Define a minimum integration readiness milestone (API available, test credentials issued, test environment active) with a date at least 6 weeks before go-live. If the milestone is missed, escalate to the Project Sponsor immediately.

**Customisation guidance:** Elevate Likelihood to High if the client is simultaneously replacing their payroll system and implementing HCM. Reduce to Low if the payroll system is already live and the integration is a known, tested pattern (e.g., existing PaySpace customer).

**Assembly trigger:** Include in all Oracle HCM implementation proposals where payroll integration is in scope.

**Related assumptions:** W3S1-001 assumptions (payroll system readiness, third-party dependency management).

---

### RC-INT-002 — Third-Party System Integration Scope Underestimated at Tender Stage

| Field | Value |
|-------|-------|
| **Risk ID** | RC-INT-002 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle Cloud / Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-003 (R-W3-003-005), W3S1-004 (R-W3-004-005) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Bid Manager / Project Manager |

**Risk description:** The scope and complexity of integrating Oracle modules with third-party systems (background screening providers, content delivery providers, learning management systems, recruitment platforms) is underestimated in the tender response. The actual integration requires more design, development, and testing effort than scoped, resulting in cost overruns or reduced integration quality.

**Standard mitigation:** Scope all third-party integrations as T&M unless full API documentation has been reviewed and confirmed before tender submission. Require the client to provide vendor API documentation before Scope and Design phase. Classify each integration by complexity tier (standard connector, custom OIC flow, or unsupported) in the proposal.

**Customisation guidance:** Elevate Likelihood to High if multiple unvalidated third-party integrations are in scope. Reduce to Low if using a pre-built APPSolve OIC accelerator with a known API pattern.

**Assembly trigger:** Include in all proposals where Oracle OIC third-party integrations beyond standard payroll are in scope.

**Related assumptions:** W3S1-003 assumptions (integration prerequisites), W3S1-004 assumptions (content provider API requirements).

---

### RC-INT-003 — Third-Party System API Unavailable or Incompatible at Integration Build Start

| Field | Value |
|-------|-------|
| **Risk ID** | RC-INT-003 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-007 (R-W3-007-003) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Technical Lead |

**Risk description:** The third-party system's API (biometric device, background check system, learning content provider, or other vendor) is not available, not documented, or incompatible with the agreed integration approach when OIC development is due to begin. The integration is blocked, causing programme delay and potentially requiring a manual data import fallback.

**Standard mitigation:** Require API documentation and test environment access from the third-party vendor as a formal programme pre-condition, documented in the project charter. Agree a fallback approach (manual import, file-based transfer) with the client in Scope and Design. Define a "vendor readiness gate" milestone at least 4 weeks before integration build begins.

**Customisation guidance:** Elevate Likelihood to High if the vendor has not previously integrated with Oracle OIC. Reduce to Low if using an APPSolve-managed OIC accelerator for a known vendor API pattern.

**Assembly trigger:** Include in all proposals where Oracle OIC integration with a third-party system requires vendor API access that is not yet confirmed.

**Related assumptions:** W3S1-007 assumptions (biometric vendor API prerequisites, manual fallback).

---

### RC-INT-004 — Payroll API Version Changes Post-Go-Live Require Unplanned Updates

| Field | Value |
|-------|-------|
| **Risk ID** | RC-INT-004 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle OIC |
| **Engagement types** | Implementation / AMS |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-009 (R-W9-001) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Technical Lead |

**Risk description:** The third-party payroll provider (PaySpace or equivalent) releases an API version update that breaks compatibility with the existing OIC integration flow. If the integration is not updated before the next payroll run, payroll data transfer fails or produces incorrect results. This is an ongoing risk for the duration of the engagement, not just at go-live.

**Standard mitigation:** Include annual OIC integration review in the AMS or maintenance scope. Subscribe to PaySpace (or equivalent) API changelog notifications. Test the integration against the new API version in a non-production environment before each annual update. Include an API compatibility check in the post-go-live hypercare checklist.

**Customisation guidance:** Elevate Likelihood to High if the payroll provider has a history of unannounced API changes. Reduce to Low if the integration uses a stable, versioned REST API with backward compatibility guarantees.

**Assembly trigger:** Include in all proposals with an OIC-mediated payroll integration where ongoing AMS or maintenance is in scope.

**Related assumptions:** W3S1-009 assumptions (integration maintenance scope, annual review obligation).

---

### RC-INT-005 — Integration Extraction Schedule Not Aligned to Payroll Processing Cutoff

| Field | Value |
|-------|-------|
| **Risk ID** | RC-INT-005 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle HCM / Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-009 (R-W9-003), W3S1-005 (R-W3-005-005) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Technical Lead / Project Manager |

**Risk description:** The OIC integration extraction schedule (the time at which HCM data is pulled and sent to payroll) is not aligned to the payroll system's processing cutoff time. HCM transactions (salary changes, new hires, terminations, leave entries) entered after the extraction runs are not included in the current payroll cycle, causing payroll exceptions that require manual correction or retroactive processing.

**Standard mitigation:** Design the integration extraction schedule in Scope and Design after confirming the payroll system's cutoff time and processing calendar with the client payroll team. Lock the extraction schedule in the OIC integration design document. Test timing alignment in UAT using live payroll cycle dates. Implement an automated escalation if any extraction fails within the cutoff window.

**Customisation guidance:** Elevate Likelihood to High if the client operates multiple payroll cycles (weekly, bi-weekly, monthly) with different cutoff times. Reduce to Low if the client has a single monthly payroll with a well-defined cutoff process already documented.

**Assembly trigger:** Include in all Oracle HCM to payroll integration proposals.

**Related assumptions:** W3S1-009 assumptions (payroll cycle calendar, cutoff alignment), W3S1-005 assumptions (compensation approval process timing).

---

### RC-INT-006 — Integration Field Mapping Errors Produce Incorrect Data in Target System

| Field | Value |
|-------|-------|
| **Risk ID** | RC-INT-006 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Oracle OIC |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-009 (R-W9-004) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Technical Lead |

**Risk description:** Field-level mapping between Oracle HCM and the target system (payroll, biometric, ERP) is incorrectly defined during integration design, causing financial calculation errors, rejected records, or silent data corruption in the target system. Errors may not be detected until parallel payroll run testing or (in worst case) post-go-live.

**Standard mitigation:** Produce a formal Field Mapping Specification document for each integration, reviewed and approved by the client systems owner and payroll team. Validate mapping during a structured parallel payroll run in UAT using at least one full payroll cycle. Implement automated reconciliation reporting to compare source and target record counts after each integration run.

**Customisation guidance:** Elevate Likelihood to High if the target system uses proprietary field codes or complex transformation logic. Reduce to Medium if using an APPSolve pre-built OIC accelerator with a validated field map.

**Assembly trigger:** Include in all Oracle OIC integration proposals where field-level data transformation is required between systems.

**Related assumptions:** W3S1-009 assumptions (field mapping validation approach, parallel run scope).

---

### RC-INT-007 — Payroll Integration Requires Bespoke Mapping Beyond Standard Patterns

| Field | Value |
|-------|-------|
| **Risk ID** | RC-INT-007 |
| **Category** | RC-INT — Integration Risk |
| **Platforms** | Acumatica / Oracle |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W1S2-007 (R-W7-005) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Technical Lead / Bid Manager |

**Risk description:** The client's payroll integration requires bespoke field mapping, validation logic, and reconciliation processes that exceed the standard integration pattern. Each client's payroll structure, earnings codes, deduction types, and cost centre allocation differs, making it impossible to commit to a fixed integration effort without scoping the specific payroll schema before tender submission.

**Standard mitigation:** Confirm payroll integration scope during Solution Design — do not commit to a fixed-effort payroll integration in the tender without reviewing the client's payroll element register and cost centre mapping. Scope payroll integration as T&M or include a Scoping Workshop cost line in the proposal if the payroll schema has not been reviewed.

**Customisation guidance:** Elevate Likelihood to High if the client uses multiple payroll streams (e.g., different pay frequencies for different employee categories) or has complex earning/deduction structures. Reduce to Low if using the APPSolve PaySpace standard integration package on a confirmed PaySpace environment.

**Assembly trigger:** Include in all Acumatica proposals where payroll integration is in scope, or any Oracle proposal where a non-standard payroll integration is included.

**Related assumptions:** W1S2-007 assumptions (PaySpace integration scope, client payroll schema review).

---

## RC-TECH — Technical Risks

---

### RC-TECH-001 — Quarterly SaaS Platform Update Introduces Breaking Changes

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-001 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Cloud (all SaaS modules) |
| **Engagement types** | Implementation / AMS |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-001 (R-W1-004) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Technical Lead |

**Risk description:** Oracle Cloud's quarterly update cycle introduces changes to configured functionality — UI changes, deprecated APIs, updated business rules, or changed default behaviours — that break existing configurations, integrations, or test scripts. The impact is typically contained but requires APPSolve intervention to assess and remediate in affected environments.

**Standard mitigation:** Conduct a Quarterly Release Impact Assessment before each Oracle Cloud update, reviewing Oracle's Release Notes for changes affecting the client's configured modules. Include quarterly release support as a named activity in AMS scope. Run regression tests against critical business processes after each update in a non-production environment before applying to production.

**Customisation guidance:** Elevate Likelihood to Medium if the implementation spans two or more quarterly update cycles during the build-and-test phase, or if the client has customised standard Oracle processes (fast formulas, BI publisher reports, integrations). Elevate Impact to High if the affected functionality is on the payroll integration path.

**Assembly trigger:** Include in all AMS proposals. Include in multi-phase implementation proposals spanning more than 6 months.

**Related assumptions:** W3S1-001 assumptions (Oracle update cycle management, regression testing responsibility).

---

### RC-TECH-002 — SETA/WSP/ATR Reporting Extract Complexity

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-002 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle HCM Cloud (Learning / Analytics) |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-004 (R-W3-004-004), W3S1-006 (R-W3-006-004) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Technical Lead |

**Risk description:** South African SETA, WSP (Workplace Skills Plan), and ATR (Annual Training Report) extract requirements are more complex than the standard Oracle Learning Cloud or Analytics report configuration. Additional custom report development or OTBI configuration is required to produce compliant output, adding effort beyond the standard scope estimate.

**Standard mitigation:** Confirm SETA reporting requirements in Scope and Design. Review the applicable SETA's report format against Oracle's standard SETA extract template. If additional fields or transformations are required, scope as additional custom report development and communicate as a change from standard scope. Include at least one SETA reporting cycle in the UAT test plan.

**Customisation guidance:** Elevate Likelihood to High if the client is subject to multiple SETA jurisdictions or has non-standard job categories that require manual mapping to OFO codes. Reduce to Low if using the standard Oracle SETA report with no bespoke requirements.

**Assembly trigger:** Include in all South African Oracle HCM Learning or Analytics proposals where SETA reporting is a stated requirement.

**Related assumptions:** W3S1-004 assumptions (SA legislative reporting scope), W3S1-006 assumptions (SETA extract requirements).

---

### RC-TECH-003 — Absence Management Rules Complexity Exceeds Standard Scope

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-003 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-007 (R-W3-007-001) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Technical Lead |

**Risk description:** The client's absence management policies (leave types, accrual rules, entitlements, carry-forward logic, encashment rules) are more complex than the standard Oracle WFM Absence Management configuration scope. The volume and complexity of rules requires additional design time, configuration effort, and regression testing beyond the standard estimate.

**Standard mitigation:** Require full documentation of all leave types and absence rules before Build commences. Agree the boundary between standard Oracle absence configuration and custom fast-formula development in Scope and Design. Produce an Absence Rules Register with each leave type, accrual rule, and entitlement — get client sign-off before configuration begins. Scope additional complexity as T&M if the agreed rule count is exceeded.

**Customisation guidance:** Elevate Likelihood to High if the client has more than 10 distinct leave types, carry-forward rules, or complex accrual algorithms (e.g., service-length-based accruals, pro-rata calculations). Reduce to Low if the client uses BCEA-standard leave types only with no custom entitlements.

**Assembly trigger:** Include in all Oracle WFM implementations where Absence Management is in scope.

**Related assumptions:** W3S1-007 assumptions (absence rules documentation, standard vs custom scope boundary).

---

### RC-TECH-004 — Time and Labour Rules Complexity Exceeds Standard Estimate

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-004 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-007 (R-W3-007-002) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Technical Lead |

**Risk description:** The client's time and attendance rules (shift differentials, overtime triggers, break rules, public holiday premiums, rounding rules) are more numerous or complex than the standard estimate. Rule count directly governs implementation effort; undisclosed complexity discovered after project commencement creates a budget overrun.

**Standard mitigation:** Produce a Time and Labour Rules Document in Scope and Design that enumerates every distinct calculation rule. Get client sign-off on the rules document before Build. Agree a rule-count ceiling in the project charter; scope rules beyond the ceiling as T&M change requests. Include T&L rule complexity as a qualification criterion in the tender qualification process.

**Customisation guidance:** Elevate Likelihood to High if the client operates multiple award/agreement types with differing T&L rules (e.g., different industrial agreements per department or site). Reduce to Low if the client operates a simple fixed-shift structure with standard BCEA overtime rules only.

**Assembly trigger:** Include in all Oracle WFM implementations where Time and Labour is in scope.

**Related assumptions:** W3S1-007 assumptions (T&L rules documentation, rule count governance).

---

### RC-TECH-005 — BCEA Overtime Calculation Requires Additional Oracle WFM Configuration

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-005 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle WFM |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-007 (R-W3-007-005) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Technical Lead |

**Risk description:** South African BCEA overtime calculation requirements (daily/weekly overtime thresholds, compressed workweek rules, public holiday calculations) require additional Oracle WFM time rules configuration beyond the standard estimate. Client-specific policies layered above the BCEA floor (industry agreements, company policy) add further complexity.

**Standard mitigation:** Confirm BCEA compliance requirements and any client-specific overtime policies in Scope and Design. Configure BCEA as the base rules and layer client-specific policies above as explicit additional rules. Document the boundary between BCEA-standard and client-specific configuration and scope the client-specific layer separately.

**Customisation guidance:** Elevate Likelihood to High if the client operates in a highly regulated sector (mining, manufacturing, retail) with sector-specific overtime agreements. Reduce to Low for office-based, standard-hours clients with no shift work.

**Assembly trigger:** Include in all South African Oracle WFM proposals where overtime and time-capture are in scope.

**Related assumptions:** W3S1-007 assumptions (SA labour legislation compliance, BCEA rules documentation).

---

### RC-TECH-006 — Oracle Analytics Cloud (OAX) Licensing Not Confirmed Before Commitment

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-006 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle HCM Cloud (Analytics) |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-006 (R-W3-006-001) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Bid Manager |

**Risk description:** The implementation scope includes Oracle Analytics for HCM (OAX) functionality, but the client has not confirmed they hold the OAX licence before the project starts. OAX is a separate Oracle licence from Oracle HCM Cloud, and discovering this during implementation requires an unplanned procurement process that delays analytics delivery and may cause scope reduction.

**Standard mitigation:** Confirm OAX licensing status at project initiation — before any analytics configuration begins. Communicate explicitly in the tender response and project charter that OAX is a separate Oracle licence and is not included in the standard HCM Cloud subscription. If OAX is not confirmed, descope analytics to OTBI (included in standard HCM licence) only.

**Customisation guidance:** Elevate Likelihood to High if the tender response is positioned on OAX capability without a client confirmation of licensing. Reduce to Low if the client has confirmed OAX licensing in writing before tender submission.

**Assembly trigger:** Include in all Oracle HCM proposals where Oracle Analytics for HCM or OAX dashboards are listed as deliverables.

**Related assumptions:** W3S1-006 assumptions (OAX licensing confirmation, product boundary between OTBI and OAX).

---

### RC-TECH-007 — OAX Data Model Dimensions Not Aligned to HCM Configuration

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-007 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle HCM Cloud (Analytics) |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-006 (R-W3-006-005) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Technical Lead |

**Risk description:** Oracle Analytics for HCM (OAX) uses a data model with pre-defined dimensions (cost centre, job, grade, location). If the HCM configuration uses non-standard structures (e.g., custom descriptive flexfields, non-standard org hierarchy, atypical grade mapping) that do not align to OAX's expected dimensions, analytics outputs are incomplete, misleading, or require significant data transformation work.

**Standard mitigation:** Review OAX data model dimensions during HCM Core configuration design, specifically where HCM configuration choices affect OAX alignment. Flag any design decisions that deviate from OAX standard dimensions. Where OAX is in scope, include an OAX alignment review as a step in the HCM Core Design Workshop.

**Customisation guidance:** Elevate Likelihood to Medium if the client requires reporting on custom org dimensions not natively supported by OAX. Reduce to Low if using standard Oracle HCM configuration with no custom flexfields on key dimensional objects.

**Assembly trigger:** Include in proposals where both Oracle HCM Core configuration and OAX analytics are in scope.

**Related assumptions:** W3S1-006 assumptions (OAX data model review, HCM Core configuration design).

---

### RC-TECH-008 — Oracle Product Licensing for Dependent Features Not Confirmed

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-008 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-008 (R-W8-002) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Bid Manager |

**Risk description:** The implementation scope includes an Oracle product feature or module that requires a separate Oracle licence (e.g., Oracle HR Help Desk, Oracle Digital Assistant, OAX, Oracle Payroll Cloud). The client has not confirmed licensing before the project starts, and discovering the gap after project commencement requires an unplanned procurement cycle, delaying the affected scope and potentially causing a project pause.

**Standard mitigation:** Identify all Oracle licences required for the implementation scope before the tender is submitted. Include a licence prerequisites checklist in the proposal appendix. Make licence confirmation a formal project initiation condition. If any required licence is not confirmed by project start, descope the affected module until licensing is resolved.

**Customisation guidance:** Elevate Likelihood to High if multiple Oracle products are in scope from different Oracle subscription types (HCM, Service Cloud, Analytics, AI). This risk is especially relevant when the tender response was built on assumed licensing not verified with the client.

**Assembly trigger:** Include in all proposals where any Oracle product beyond the base HCM Cloud subscription is in scope. Includes HR Help Desk, OAX, ODA, Oracle Payroll Cloud, OCI, or Oracle Analytics Publisher.

**Related assumptions:** W3S1-008 assumptions (Help Desk licensing prerequisites). See also RC-TECH-006 (OAX) and RC-TECH-009 (ODA).

---

### RC-TECH-009 — Oracle Digital Assistant Scope Added Without Separate License Confirmation

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-009 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Cloud / ODA |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-008 (R-W8-006) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Bid Manager |

**Risk description:** Oracle Digital Assistant (ODA) chatbot functionality is requested or included in scope mid-project without confirming that the client holds the separate ODA licence. ODA is not included in the standard Oracle HCM Cloud or Help Desk subscription. Discovering the licensing gap after development has commenced requires procurement, scope suspension, and rework.

**Standard mitigation:** Treat ODA as a separate workstream with its own licence prerequisite check. Document in the proposal that ODA requires a separate Oracle licence. If ODA is raised during the project, confirm licensing before any design or development work begins. Do not include ODA implementation effort in the base implementation estimate unless ODA licensing is confirmed.

**Customisation guidance:** Elevate Likelihood to Medium if the client has expressed an interest in self-service HR chatbots during the sales process, as these discussions often create ODA expectations without a licensing conversation.

**Assembly trigger:** Include in proposals where Oracle Digital Assistant or chatbot functionality is listed as a deliverable or a client aspiration.

**Related assumptions:** W3S1-008 assumptions (ODA licence prerequisites, separate workstream designation).

---

### RC-TECH-010 — Digital Channel Complexity Beyond Standard Oracle Configuration

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-010 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Help Desk |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-008 (R-W8-005) |
| **Likelihood** | Low |
| **Impact** | Medium |
| **Rating** | LOW |
| **Owner** | Technical Lead |

**Risk description:** The implementation includes digital service channels beyond Oracle Help Desk's standard email/web portal interface — such as chatbot, SMS, WhatsApp, or social media integration. These channels require third-party service configuration and additional integration work beyond standard Oracle implementation scope, increasing effort and introducing vendor dependencies.

**Standard mitigation:** Confirm the channel architecture in the Mobilize phase before any digital channel configuration begins. Assess third-party channel service availability (SMS gateway, WhatsApp Business API, chatbot platform). Scope non-standard channels as additional workstreams with explicit effort estimates. Include channel architecture as a formal design decision in the project charter.

**Customisation guidance:** Elevate Likelihood to Medium if the client has an active digital HR initiative or is consolidating multiple HR channels onto a single platform. Reduce to Low if the implementation is limited to email and standard Help Desk web portal only.

**Assembly trigger:** Include in Oracle HR Help Desk proposals where digital channels beyond email and web portal are listed as deliverables.

**Related assumptions:** W3S1-008 assumptions (channel architecture scope, third-party channel prerequisites).

---

### RC-TECH-011 — Career Site Design Complexity Exceeds Standard Oracle Recruiting Scope

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-011 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle Recruiting Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-003 (R-W3-003-001) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Technical Lead / Bid Manager |

**Risk description:** The client expects a fully branded, custom-designed candidate-facing career site as part of the Oracle Recruiting Cloud implementation. APPSolve configures the standard Oracle Recruiting career site framework; custom web design, branding beyond Oracle's templates, or integration with external career marketing platforms requires additional effort and skills beyond standard implementation scope.

**Standard mitigation:** Clarify the career site design scope in Scope and Design. Document that APPSolve configures the Oracle Recruiting standard career site framework, including branding within Oracle's supported configuration options. If the client requires custom web design, HTML/CSS development, or external career site integration, scope this as a separate deliverable with its own estimate and potentially a third-party web design resource.

**Customisation guidance:** Elevate Likelihood to High if the client has an existing career site with custom branding and complex design requirements. Reduce to Low if the client accepts Oracle's standard career site template with APPSolve's standard branding implementation.

**Assembly trigger:** Include in all Oracle Recruiting Cloud proposals where career site configuration is in scope.

**Related assumptions:** W3S1-003 assumptions (career site scope, APPSolve configuration boundary).

---

### RC-TECH-012 — Annual SA Legislative Change Not Reflected in OIC Integrations

| Field | Value |
|-------|-------|
| **Risk ID** | RC-TECH-012 |
| **Category** | RC-TECH — Technical Risk |
| **Platforms** | Oracle OIC / Oracle HCM |
| **Engagement types** | Implementation / AMS |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-009 (R-W9-006) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Technical Lead |

**Risk description:** Annual South African legislative changes (Budget Speech tax tables, ETI changes, UIF rate changes, POPIA regulatory updates) are not reflected in OIC integration logic, causing incorrect payroll calculations or non-compliant data exports post-update. This is a recurring annual risk for all SA clients with active OIC payroll integrations.

**Standard mitigation:** Include an annual legislative review as a formal deliverable in the AMS or maintenance scope. Monitor SARS Budget Speech announcements and PaySpace/payroll vendor release notes annually. Test the integration against updated tax tables and legislative changes in a non-production environment before the new tax year (March 1 each year). Include Budget Speech patch testing as a named milestone in the annual support calendar.

**Customisation guidance:** Elevate Likelihood to High if the client has not confirmed an AMS or maintenance contract — without it, annual updates are not managed proactively. Reduce to Low if the integration uses PaySpace's own legislative update process and APPSolve's OIC integration is isolated from the legislative calculation logic.

**Assembly trigger:** Include in all South African Oracle OIC payroll integration proposals. Mandatory for AMS proposals covering OIC integrations.

**Related assumptions:** W3S1-009 assumptions (annual legislative compliance, AMS review cycle).

---

## RC-CLIENT — Client Dependency Risks

---

### RC-CLIENT-001 — Super-User Availability Insufficient During UAT

| Field | Value |
|-------|-------|
| **Risk ID** | RC-CLIENT-001 |
| **Category** | RC-CLIENT — Client Dependency Risk |
| **Platforms** | All Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-001 (R-W1-005) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Project Manager |

**Risk description:** The client's nominated super-users — who are responsible for executing UAT test scripts, validating business process outcomes, and confirming go-live readiness — are not available for the required duration or frequency during the UAT phase. Insufficient super-user engagement extends the UAT timeline, leaves defects undetected, and delays sign-off, pushing back the go-live date.

**Standard mitigation:** Formalise super-user availability as a project assumption in the project charter. Specify the required number of super-users, their time commitment (hours per week during UAT), and the escalation path if availability is not met. Escalate unavailability to the Project Sponsor immediately if it threatens the UAT timeline. Do not advance to go-live readiness review without super-user confirmation that all critical test cases are completed and signed off.

**Customisation guidance:** Elevate Likelihood to High if the client has not named specific super-users before project start, or if the organisation has historically made IT projects compete with BAU workload without backfilling super-user capacity.

**Assembly trigger:** Include in all Oracle HCM and ERP implementation proposals.

**Related assumptions:** W3S1-001 assumptions (super-user nomination, UAT resource commitment).

---

### RC-CLIENT-002 — Client Prerequisite Systems or Accounts Not Available at Project Start

| Field | Value |
|-------|-------|
| **Risk ID** | RC-CLIENT-002 |
| **Category** | RC-CLIENT — Client Dependency Risk |
| **Platforms** | Oracle Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-003 (R-W3-003-002) |
| **Likelihood** | Low |
| **Impact** | Low |
| **Rating** | LOW |
| **Owner** | Project Manager |

**Risk description:** The client has not established prerequisite third-party accounts, licences, or system access required for the implementation to proceed (e.g., LinkedIn Recruiter account for Oracle Recruiting integration, job board accounts, background screening provider contracts). Without these accounts, integration or configuration of dependent functionality cannot proceed on schedule.

**Standard mitigation:** Conduct a prerequisite check during tender qualification or project initiation. Include a Prerequisite Checklist in the project charter covering all third-party accounts, licences, and access credentials required before project start. Flag missing prerequisites as a project risk and assign the client a resolution deadline before the affected configuration phase begins.

**Customisation guidance:** Elevate Likelihood to Medium if multiple third-party system integrations are in scope and the client has not previously used these third-party systems. Reduce to Low if the client is an existing user of all required third-party services.

**Assembly trigger:** Include in Oracle Recruiting Cloud proposals where third-party job board or candidate sourcing integrations are in scope. Optionally include in other proposals with third-party system prerequisites.

**Related assumptions:** W3S1-003 assumptions (third-party account prerequisites, integration scope conditions).

---

### RC-CLIENT-003 — Onboarding Task and Workflow Ownership Not Defined

| Field | Value |
|-------|-------|
| **Risk ID** | RC-CLIENT-003 |
| **Category** | RC-CLIENT — Client Dependency Risk |
| **Platforms** | Oracle Recruiting / Oracle HCM |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-003 (R-W3-003-004) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Project Manager |

**Risk description:** Oracle Recruiting Cloud Onboarding task configuration requires a clear RACI for which tasks are completed by HR, IT, facilities, and the new employee respectively. If task ownership is not agreed before configuration, the onboarding checklist is configured on an assumed RACI that the client rejects during UAT, requiring significant reconfiguration of task assignments, notifications, and workflow routing.

**Standard mitigation:** Conduct an Onboarding Process Design Workshop in Scope and Design to map all onboarding tasks and agree the RACI. Document task ownership in the configuration workbook. Obtain formal client sign-off on the RACI before any onboarding task configuration begins. Treat post-sign-off RACI changes as change requests.

**Customisation guidance:** Elevate Likelihood to High if the client is implementing onboarding for the first time or if there are organisational ambiguities about HR vs IT vs Facilities responsibilities for new employee setup. Reduce to Low if the client has a well-defined onboarding process already documented in a RACI.

**Assembly trigger:** Include in all Oracle Recruiting Cloud proposals where Onboarding is in scope.

**Related assumptions:** W3S1-003 assumptions (onboarding RACI, task ownership design).

---

### RC-CLIENT-004 — Learning Catalog Not Ready at System Go-Live

| Field | Value |
|-------|-------|
| **Risk ID** | RC-CLIENT-004 |
| **Category** | RC-CLIENT — Client Dependency Risk |
| **Platforms** | Oracle Learning Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-004 (R-W3-004-001) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Project Manager |

**Risk description:** The client is responsible for populating the Oracle Learning Cloud catalog with learning items, courses, and content before go-live. If the catalog is not populated by go-live, the system is operational but has no meaningful content for learners — reducing perceived system value, adoption rates, and return on investment.

**Standard mitigation:** Establish a Catalog Population milestone in the project plan as a formal client deliverable with a date at least 4 weeks before UAT. Include catalog population as a named assumption in the project charter — APPSolve configures the catalog structure; the client populates content. Conduct a Catalog Readiness Review before UAT begins. If catalog is not populated, delay go-live or limit learner access until minimum viable catalog is ready.

**Customisation guidance:** Elevate Likelihood to High if the client has a large legacy learning library to migrate, or if catalog population depends on third-party content providers. Reduce to Low if the client is starting fresh with a small curated catalog and has a dedicated L&D resource assigned.

**Assembly trigger:** Include in all Oracle Learning Cloud proposals.

**Related assumptions:** W3S1-004 assumptions (catalog population responsibility, minimum viable catalog definition).

---

### RC-CLIENT-005 — Performance Rating Data Unavailable for Compensation Cycle

| Field | Value |
|-------|-------|
| **Risk ID** | RC-CLIENT-005 |
| **Category** | RC-CLIENT — Client Dependency Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-005 (R-W3-005-002) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Project Manager |

**Risk description:** Oracle Workforce Compensation is configured to drive merit increases based on performance ratings from the Oracle Performance Management module. If performance management is not implemented, or if performance ratings are not entered before the compensation cycle runs, the system cannot generate merit recommendations — requiring manual rating input, which defeats the automation purpose.

**Standard mitigation:** Confirm the performance management implementation timeline before committing to performance-based merit configuration in the Compensation module. If Performance Management is not yet live, configure the Compensation module to accept manual performance rating input as an interim measure for the first cycle. Document the configuration as a temporary workaround pending Performance Management go-live.

**Customisation guidance:** Elevate Likelihood to High if Performance Management and Compensation are being implemented concurrently with a compressed timeline. Reduce to Low if Performance Management is already live and ratings are populated before compensation cycle configuration begins.

**Assembly trigger:** Include in Oracle Workforce Compensation proposals where merit-based pay is in scope and Oracle Performance Management is the rating source.

**Related assumptions:** W3S1-005 assumptions (performance-compensation integration, manual rating fallback).

---

### RC-CLIENT-006 — Knowledge Base Content Ownership Undefined

| Field | Value |
|-------|-------|
| **Risk ID** | RC-CLIENT-006 |
| **Category** | RC-CLIENT — Client Dependency Risk |
| **Platforms** | Oracle Help Desk |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-008 (R-W8-004) |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Rating** | MEDIUM |
| **Owner** | Project Manager |

**Risk description:** Oracle HR Help Desk's self-service effectiveness depends on a well-maintained knowledge base (KB). The client has not assigned ownership of KB article authoring and maintenance to a specific HR team. Without a governance structure for KB content, article quality degrades over time, self-service resolution rates drop, and Help Desk ticket volumes remain high — undermining the business case for the implementation.

**Standard mitigation:** Define a KB Governance Model in Scope and Design — assign a named KB Owner (HR role), establish an article review cycle, and agree on APPSolve's initial seeding responsibility vs. ongoing client maintenance. APPSolve seeds an initial set of KB articles based on common HR queries; the client team is responsible for ongoing authoring. Train at least two HR team members on KB authoring before go-live.

**Customisation guidance:** Elevate Likelihood to High if the HR team is small, has no prior experience with knowledge management, or if the organisation has a history of poor content governance. Reduce to Low if a dedicated HR Knowledge Manager role exists.

**Assembly trigger:** Include in all Oracle HR Help Desk proposals.

**Related assumptions:** W3S1-008 assumptions (KB governance, initial content seeding responsibility).

---

### RC-CLIENT-007 — Cross-Functional Alignment on Key Design Frameworks Not Achieved Before Build

| Field | Value |
|-------|-------|
| **Risk ID** | RC-CLIENT-007 |
| **Category** | RC-CLIENT — Client Dependency Risk |
| **Platforms** | Oracle HCM Cloud |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-002 (R-W2-002) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Project Manager |

**Risk description:** Oracle HCM configuration of goal frameworks, talent profiles, grade structures, or job families requires cross-functional agreement between HR, Finance, Business Leaders, and senior management. If stakeholders do not reach alignment on these frameworks before configuration begins, the configuration is built on an assumed design that is subsequently rejected, requiring rework and delaying the programme.

**Standard mitigation:** Conduct a Cross-Functional Design Workshop before the Build phase, with all required stakeholder groups represented. Obtain formal sign-off from all stakeholder leads before any configuration begins on the affected framework. Document disagreements and escalation paths in the Config Decision Log. If cross-functional alignment cannot be achieved within the project schedule, descope the contentious framework from the initial go-live and add it to a subsequent phase.

**Customisation guidance:** Elevate Likelihood to High if the organisation is large, matrixed, or in transformation (merger, restructure) — these create conflicting stakeholder requirements. Reduce to Low for organisations with a single HR owner who has the authority to make all framework decisions independently.

**Assembly trigger:** Include in Oracle HCM implementations where goal management, performance calibration, talent profiles, or compensation grade structures are in scope.

**Related assumptions:** W3S1-002 assumptions (cross-functional workshop mandate, Config Decision Log governance).

---

## RC-COMM — Commercial Risks

---

### RC-COMM-001 — Analytics Expectations Misaligned With Platform Capability in Scope

| Field | Value |
|-------|-------|
| **Risk ID** | RC-COMM-001 |
| **Category** | RC-COMM — Commercial Risk |
| **Platforms** | Oracle HCM Cloud (Analytics) |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-004 (R-W3-004-002), W3S1-005 (R-W3-005-003), W3S1-006 (R-W3-006-003) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Bid Manager |

**Risk description:** The client's analytics expectations — formed during the tender or sales process — exceed the capability of the analytics platform included in the implementation scope. Common scenarios: the client expects OAX dashboard capability when only OTBI is licensed; the client expects out-of-the-box dashboards when custom reports are required; the client conflates Oracle Analytics for HCM with built-in module reporting. The mismatch creates a mid-project scope dispute and erodes client confidence.

**Standard mitigation:** Apply an explicit analytics boundary statement in the tender response and project charter, distinguishing between OTBI (standard HCM licence), OAX (separate licence), and any custom report development. Confirm client analytics expectations in the Scope and Design phase before any analytics configuration begins. If the client's expectations require OAX and OAX is not licensed, escalate immediately and offer a licensed upgrade path.

**Customisation guidance:** Elevate Likelihood to High if the tender response highlighted analytics capability as a differentiator without explicitly distinguishing product tiers. Reduce to Low if the client has confirmed their analytics licensing and reviewed the analytics boundary in writing.

**Assembly trigger:** Include in all Oracle HCM proposals where analytics, dashboards, or reporting is a stated requirement or client priority.

**Related assumptions:** W3S1-004, W3S1-005, W3S1-006 assumptions (analytics boundary, OAX licensing communication).

---

### RC-COMM-002 — Oracle HR Help Desk Conflated With Oracle Service Cloud

| Field | Value |
|-------|-------|
| **Risk ID** | RC-COMM-002 |
| **Category** | RC-COMM — Commercial Risk |
| **Platforms** | Oracle Help Desk |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-008 (R-W8-001) |
| **Likelihood** | Medium |
| **Impact** | High |
| **Rating** | HIGH |
| **Owner** | Bid Manager |

**Risk description:** The client understands the implementation to include Oracle Service Cloud (a full customer-facing CRM service platform) rather than Oracle HR Help Desk (an internal HR case management and self-service product). This naming confusion — common in Oracle's product portfolio — creates misaligned expectations about functionality scope, leading to mid-project disputes about what was sold and what will be delivered.

**Standard mitigation:** Use "Oracle HR Help Desk" consistently and explicitly throughout the tender response, proposal, and project charter — never "Oracle Service Cloud," "Oracle CRM," or generic "help desk." Include a Product Boundary statement in the tender response clarifying that the implementation is Oracle HCM Cloud's HR Help Desk module, which is distinct from Oracle's Customer Service Cloud. Confirm the client's understanding in the Scope and Design phase.

**Customisation guidance:** Elevate Likelihood to High if the client's IT or procurement team (rather than HR) is the primary contact, as they are more likely to interpret "help desk" as an IT service product. Reduce to Low if the client has previously used Oracle HR Help Desk.

**Assembly trigger:** Include in all Oracle HR Help Desk proposals.

**Related assumptions:** W3S1-008 assumptions (product boundary, naming governance).

---

### RC-COMM-003 — Integration Method Commitment in Tender Creates Contractual Exposure

| Field | Value |
|-------|-------|
| **Risk ID** | RC-COMM-003 |
| **Category** | RC-COMM — Commercial Risk |
| **Platforms** | Acumatica / Oracle |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W1S2-007 (R-W7-004) |
| **Likelihood** | Low |
| **Impact** | High |
| **Rating** | MEDIUM |
| **Owner** | Bid Manager |

**Risk description:** A tender response commits APPSolve to a specific integration method (e.g., API-based real-time, file-based batch, pre-built connector) for a payroll or ERP integration before the client's systems have been assessed. If the agreed method is later found to be technically infeasible, unavailable, or unsupported by the third-party system, APPSolve is contractually bound to a method it cannot deliver, creating commercial and delivery exposure.

**Standard mitigation:** Use qualifying wording in all tender responses for integration scope: "Integration method to be confirmed during Solution Design based on available APIs and system capabilities." Do not commit to a specific integration architecture in the tender unless the third-party system's API has been reviewed and confirmed. Reference integration scope as indicative, with final design to be agreed in Scope and Design.

**Customisation guidance:** Elevate Likelihood to Medium if the tender specifies a named integration method for a third-party system not previously integrated by APPSolve. Reduce to Low if using an APPSolve-proven OIC accelerator for a known API pattern (e.g., standard PaySpace REST API).

**Assembly trigger:** Include in all proposals where payroll or ERP integration is in scope and the third-party system API has not been confirmed before tender submission.

**Related assumptions:** W1S2-007 assumptions (integration scoping pre-conditions, qualifying language governance).

---

## RC-OPS — Operational Risks

---

### RC-OPS-001 — First Live Operational Cycle High-Stakes Risk

| Field | Value |
|-------|-------|
| **Risk ID** | RC-OPS-001 |
| **Category** | RC-OPS — Operational Risk |
| **Platforms** | Oracle HCM Cloud (Compensation / Payroll) |
| **Engagement types** | Implementation |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-005 (R-W3-005-004) |
| **Likelihood** | High |
| **Impact** | High |
| **Rating** | CRITICAL |
| **Owner** | Project Manager / Technical Lead |

**Risk description:** The first live operational cycle following go-live — typically the first compensation cycle, first payroll run, or first performance review cycle — is inherently high-risk. Configuration errors, data quality issues, and process gaps that were not caught in UAT manifest in real financial or operational outcomes. Errors in the first live cycle can cause employee payment errors, regulatory non-compliance, or reputational damage to both the client and APPSolve.

**Standard mitigation:** Mandate post-go-live hypercare support through the first complete operational cycle. Include a Pre-Cycle Testing Checklist that is executed 2 weeks before the first live cycle (validating all element entries, approval workflows, integration timings, and exception reporting). Assign a named APPSolve support consultant for the first cycle with a defined escalation path and response SLA. Do not close the project until the first live cycle has been successfully completed and signed off.

**Customisation guidance:** Elevate Likelihood to Critical if the first live cycle occurs within the same week as go-live with no buffer. Reduce to High if UAT included a full simulation of the first cycle using live-data equivalents. The CRITICAL rating reflects the High × High matrix — do not reduce without strong UAT evidence.

**Assembly trigger:** Include in all Oracle Compensation, Payroll interface, or multi-module HCM proposals where an annual or recurring business cycle is directly enabled by the go-live.

**Related assumptions:** W3S1-005 assumptions (hypercare scope, first-cycle support obligation, pre-cycle testing checklist).

---

## RC-COMP — Compliance Risks

---

### RC-COMP-001 — POPIA Non-Compliance in HR or Payroll Data Handling

| Field | Value |
|-------|-------|
| **Risk ID** | RC-COMP-001 |
| **Category** | RC-COMP — Compliance Risk |
| **Platforms** | Oracle HCM Cloud / Oracle OIC |
| **Engagement types** | Implementation / AMS |
| **Version** | draft-0.1 |
| **Approved for reuse** | No — pending BU Lead review |
| **Source** | W3S1-008 (R-W8-007), W3S1-009 (R-W9-005) |
| **Likelihood** | Low |
| **Impact** | High |
| **Rating** | MEDIUM |
| **Owner** | Technical Lead / Project Manager |

**Risk description:** The implementation processes or transmits personal information (as defined under South Africa's POPIA) through Oracle HCM or OIC integrations without adequate access controls, data minimisation, or purpose limitation measures. Common scenarios include ER case records accessible to employees without proper role-based access, OIC payroll transmissions including personal data fields beyond what is required for payroll processing, or log files retaining personal data beyond permissible retention periods.

**Standard mitigation:** Apply POPIA-aligned access controls as a mandatory implementation standard for all South African clients: role-based access configured and tested before go-live; data field scope in OIC integrations limited to the agreed minimum required for the business process; log retention configured to comply with defined retention periods. Test access control compliance in UAT. Include a POPIA compliance check in the go-live readiness checklist.

**Customisation guidance:** Elevate Likelihood to Medium if the client handles sensitive categories of personal information (health records, disciplinary records, financial counselling) through Oracle. Reduce to Low if the implementation is limited to standard HCM modules with no ER case management or external data transmission.

**Assembly trigger:** Include in all South African Oracle HCM and OIC proposals. Mandatory for HR Help Desk proposals (ER case data) and OIC payroll integration proposals (financial personal data).

**Related assumptions:** W3S1-008 assumptions (POPIA access control testing), W3S1-009 assumptions (data minimisation in OIC, field scope governance).

---

## Coverage Gap Summary

The following risk categories from `RISK_LIBRARY_STANDARD.md` have **no extractable source risks** in the current governed capability asset library (as at WP18B-EXT.1):

| Category | Gap | Root Cause |
|----------|-----|------------|
| RC-RES | No resource risk entries | No capability asset includes consultant or client resource availability risks in a formal register |
| RC-INFRA | No infrastructure risk entries | OCI gap report contains governance issues, not delivery risks; no OCI capability asset risk register |
| RC-CM | No change management risk entries | Change management is described in methodology documentation but no formal risk register |
| RC-MIG | No migration risk entries | Data migration risks are captured under RC-DATA; no dedicated migration risk register exists |
| RC-CUT | No cutover risk entries | Cutover planning referenced in methodology; no formal cutover risk register in any asset |
| RC-3P | No third-party vendor risk entries | BeBanking bank format dependencies implied in gap report but not formalised as delivery risks |
| RC-SEC | Partially covered | POPIA risks captured under RC-COMP; no broader cybersecurity or platform security risk entries |

**Recommendation:** These gaps should be addressed in WP18B-EXT.2 through a BU Lead interview session to elicit risks from delivery experience before the Risk Selection Engine is built.

---

*Enterprise Risk Register Draft v0.1 — WP18B-EXT.1 — 2026-06-26*  
*All entries: DRAFT — Pending BU Lead approval. approved_for_reuse: No*
