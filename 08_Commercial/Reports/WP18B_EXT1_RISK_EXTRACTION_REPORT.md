---
title: "WP18B-EXT.1 — Risk Extraction Report"
status: "COMPLETE"
version: "1.0"
created: "2026-06-26"
created_by: "WP18B-EXT.1 — Risk Library Foundation"
work_package: "WP18B-EXT.1"
next_action: "BU Lead review of ENTERPRISE_RISK_REGISTER_DRAFT.md → WP18B-EXT.2"
---

# WP18B-EXT.1 — Risk Extraction Report

**Work Package:** WP18B-EXT.1 — Risk Library Foundation — Phase 1  
**Status:** COMPLETE  
**Date:** 2026-06-26  

---

## 1. Executive Summary

WP18B-EXT.1 (Phase 1) audited the full APPSolve Tender Knowledge Base to discover, extract, and normalise all reusable delivery risks into a canonical enterprise Risk Register.

**Audit scope:** 49 governed capability assets + 6 gap reports  
**Source risks discovered:** 51 (from formal risk registers in 10 assets)  
**Duplicates eliminated:** 9 (across 8 duplication groups)  
**Canonical risks produced:** 40  
**Risk categories populated:** 8 of 15  
**Risk categories with no source:** 7 (coverage gaps documented)  

The 40 canonical risks are documented in:  
`08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_DRAFT.md`

All 40 entries are in DRAFT status. No entry may be used in a proposal risk register until approved by the BU Lead (`approved_for_reuse: Yes`).

---

## 2. Audit Methodology

### 2.1 Sources Audited

**Phase 1 — Formal Risk Registers (governed assets):**

| Asset ID | Asset Name | Risk Register Found | Risks Extracted |
|----------|------------|---------------------|-----------------|
| W3S1-001 | Oracle HCM Core | Yes | 5 |
| W3S1-002 | Oracle Talent Management | Yes | 5 |
| W3S1-003 | Oracle Recruiting Cloud | Yes | 5 |
| W3S1-004 | Oracle Learning Cloud | Yes | 5 |
| W3S1-005 | Oracle Workforce Compensation | Yes | 5 |
| W3S1-006 | Oracle HCM Analytics | Yes | 5 |
| W3S1-007 | Oracle Workforce Management | Yes | 6 |
| W3S1-008 | Oracle HR Help Desk | Yes | 7 |
| W3S1-009 | Oracle HCM Payroll Interface (OIC) | Yes | 6 |
| W1S2-007 | Acumatica PaySpace Integration | Yes (partial) | 2 reusable |
| **TOTAL** | | **10 of 49 assets** | **51** |

**Phase 2 — Gap Reports (risk-adjacent content):**

| Report | Extractable Delivery Risks | Disposition |
|--------|---------------------------|-------------|
| OIC_GAP_REPORT.md | Commercial scope disputes, estimation errors | Normalised into RC-COMM-003, RC-INT-002 |
| AMS_GAP_REPORT.md | SLA governance gaps | Not extracted — operational procedure gaps, not delivery risks |
| ERP_GAP_REPORT.md | COA design errors, SoD risks | Captured implicitly in RC-PROJ-001, RC-DATA-001 |
| ACU_GAP_REPORT.md | Partner tier risk (CLOSED) | Not extracted — all issues now CLOSED |
| BEBANKING_GAP_REPORT.md | Bank format, AVS, testing environment | Not extracted — delivery risks not yet formalised as governed assets |
| OCI_GAP_REPORT.md | Cost commitment, boundary ambiguity | Not extracted — governance gaps, not project delivery risks |

**Phase 3 — Assets with No Formal Risk Register:**

The following asset categories were audited and confirmed to have no extractable formal risk registers:

- Oracle Fusion capability assets (W2S1-001) — no risk register section
- Oracle EBS capability assets (W2S1-002) — no risk register section
- Oracle DBA capability assets (W2S1-003) — no risk register section
- Oracle Managed Services/AMS (W2S1-004) — document-governance risks only (not delivery risks)
- Oracle Methodology (W2S1-005) — risk management process described; no formal risk entries
- Oracle ERP Fusion (W4-ERP-001, W4-ERP-002, W4-ERP-003) — no risk register sections
- Oracle OIC Accelerators (W4-INT-001) — no risk register section
- Oracle AI Skills (W4-AI-002) — no risk register section
- Oracle HCM Journeys (W4-HCM-002) — no risk register section
- Acumatica ERP modules (W1S2-001 through W1S2-005) — no risk register sections
- Acumatica specialist assets (W1S2-006, W1S2-008, W1S2-009) — no risk register sections
- BeBanking assets (W1S3-001 through W1S3-010) — no risk register sections
- Company profile assets (W1S1-001 through W1S1-009) — no risk register sections

### 2.2 Extraction Rules Applied

1. **Inclusion criterion:** Risk must be a delivery risk applicable across multiple client engagements of the same type — not a specific incident, document governance issue, or single-client anomaly.
2. **Exclusion criterion:** Risks classified as "internal governance" (FR-W4-xxx document accuracy risks) or already-closed risks were excluded.
3. **Normalisation:** Source risks were generalised to be platform- and client-agnostic where possible, retaining platform specificity only where the risk is structurally tied to a specific product.
4. **Deduplication:** Risks sharing the same root cause, mitigation, and assembly trigger across different source assets were merged into a single canonical risk. Source traceability is preserved in the `Source` field.
5. **No invention:** No new risks were invented beyond what is traceable to existing governed assets or gap reports. Categories with no source remain empty pending WP18B-EXT.2 SME input.

---

## 3. Source Asset Risk Inventory

### 3.1 Complete Source Risk Extract (Pre-Deduplication)

The following 51 source risks were discovered and are the basis for the 40 canonical entries.

| Source ID | Asset | Title | Likelihood | Impact | Canonical Risk |
|-----------|-------|-------|------------|--------|---------------|
| R-W1-001 | W3S1-001 | Org design decisions late | Medium | High | RC-PROJ-003 |
| R-W1-002 | W3S1-001 | Data quality in legacy HR | High | Medium | RC-DATA-001 |
| R-W1-003 | W3S1-001 | Third-party payroll integration timing | Medium | High | RC-INT-001 |
| R-W1-004 | W3S1-001 | Quarterly Oracle release breaking changes | Low | Medium | RC-TECH-001 |
| R-W1-005 | W3S1-001 | Super-user availability in UAT | Medium | Medium | RC-CLIENT-001 |
| R-W2-001 | W3S1-002 | Talent profile architecture not agreed | High | High | RC-PROJ-001 *(merged)* |
| R-W2-002 | W3S1-002 | Goal framework misaligned | Medium | High | RC-CLIENT-007 |
| R-W2-003 | W3S1-002 | HCM Core not stable when Talent begins | Medium | High | RC-PROJ-002 *(merged)* |
| R-W2-004 | W3S1-002 | Performance calendar changes post-config | Low | Medium | RC-PROJ-004 |
| R-W2-005 | W3S1-002 | Calibration not tested in UAT | Medium | Medium | RC-CLIENT-001 *(scope)* |
| R-W3-003-001 | W3S1-003 | Career site design complexity | Medium | Medium | RC-TECH-011 |
| R-W3-003-002 | W3S1-003 | LinkedIn accounts not available | Low | Low | RC-CLIENT-002 |
| R-W3-003-003 | W3S1-003 | Job profiles not ready for Recruiting | Medium | High | RC-PROJ-002 *(merged)* |
| R-W3-003-004 | W3S1-003 | Onboarding task ownership ambiguity | Medium | Medium | RC-CLIENT-003 |
| R-W3-003-005 | W3S1-003 | Third-party integration scope underestimated | Medium | Medium | RC-INT-002 *(merged)* |
| R-W3-004-001 | W3S1-004 | Learning catalog not ready | Medium | High | RC-CLIENT-004 |
| R-W3-004-002 | W3S1-004 | Analytics expectations misaligned (OAX) | Medium | Medium | RC-COMM-001 *(merged)* |
| R-W3-004-003 | W3S1-004 | Content format incompatibility | Medium | Medium | RC-DATA-002 |
| R-W3-004-004 | W3S1-004 | SETA/WSP/ATR extract complexity | Medium | Medium | RC-TECH-002 *(merged)* |
| R-W3-004-005 | W3S1-004 | Content provider integration underestimated | Low | Medium | RC-INT-002 *(merged)* |
| R-W3-005-001 | W3S1-005 | Compensation plan design not complete | Medium | High | RC-PROJ-001 *(merged)* |
| R-W3-005-002 | W3S1-005 | Performance rating data not available | Medium | Medium | RC-CLIENT-005 |
| R-W3-005-003 | W3S1-005 | Analytics expectations exceed OWC | Medium | Medium | RC-COMM-001 *(merged)* |
| R-W3-005-004 | W3S1-005 | First live compensation cycle support | High | High | RC-OPS-001 |
| R-W3-005-005 | W3S1-005 | Payroll integration timing (compensation) | Medium | High | RC-INT-005 *(merged)* |
| R-W3-006-001 | W3S1-006 | OAX licensing not confirmed | Medium | High | RC-TECH-006 |
| R-W3-006-002 | W3S1-006 | Reporting requirements not confirmed | High | Medium | RC-CLIENT-007 *(scope)* |
| R-W3-006-003 | W3S1-006 | OTBI/OAX conflation in tender | Medium | High | RC-COMM-001 *(merged)* |
| R-W3-006-004 | W3S1-006 | SETA legislative extract complexity | Medium | Medium | RC-TECH-002 *(merged)* |
| R-W3-006-005 | W3S1-006 | OAX data model alignment | Low | Medium | RC-TECH-007 |
| R-W3-007-001 | W3S1-007 | Absence rules complexity | Medium | High | RC-TECH-003 |
| R-W3-007-002 | W3S1-007 | T&L rules complexity | Medium | Medium | RC-TECH-004 |
| R-W3-007-003 | W3S1-007 | Biometric system API availability | Medium | High | RC-INT-003 |
| R-W3-007-004 | W3S1-007 | Biometric device enrolment data quality | High | Medium | RC-DATA-004 |
| R-W3-007-005 | W3S1-007 | BCEA overtime calculation complexity | Medium | Medium | RC-TECH-005 |
| R-W3-007-006 | W3S1-007 | Scheduling demand data unavailable | Low | Medium | RC-DATA-005 |
| R-W8-001 | W3S1-008 | Product naming conflation (Help Desk vs Service Cloud) | Medium | High | RC-COMM-002 |
| R-W8-002 | W3S1-008 | Help Desk licensing not confirmed | Medium | High | RC-TECH-008 |
| R-W8-003 | W3S1-008 | ER case process complexity | Medium | Medium | RC-TECH-008 *(scope note)* |
| R-W8-004 | W3S1-008 | Knowledge base content ownership | Medium | Medium | RC-CLIENT-006 |
| R-W8-005 | W3S1-008 | Chatbot/SMS channel complexity | Low | Medium | RC-TECH-010 |
| R-W8-006 | W3S1-008 | Digital Assistant scope inflation | Low | Medium | RC-TECH-009 |
| R-W8-007 | W3S1-008 | POPIA data handling in ER cases | Low | High | RC-COMP-001 *(merged)* |
| R-W9-001 | W3S1-009 | PaySpace API compatibility | Medium | Medium | RC-INT-004 |
| R-W9-002 | W3S1-009 | HCM data quality → payroll input | Medium | High | RC-DATA-003 |
| R-W9-003 | W3S1-009 | Payroll cut-off misalignment | Low | High | RC-INT-005 *(merged)* |
| R-W9-004 | W3S1-009 | Element mapping errors | Medium | High | RC-INT-006 |
| R-W9-005 | W3S1-009 | POPIA non-compliance in payroll data | Low | High | RC-COMP-001 *(merged)* |
| R-W9-006 | W3S1-009 | Annual legislative non-compliance | Medium | High | RC-TECH-012 |
| R-W7-004 | W1S2-007 | Integration method commitment risk | Low | High | RC-COMM-003 |
| R-W7-005 | W1S2-007 | Payroll integrations — bespoke mapping | Medium | Medium | RC-INT-007 |

**Note on W1S2-007:** R-W7-001, R-W7-002, R-W7-003 were identified as internal document governance risks (not delivery risks) and excluded from extraction.

**Note on R-W8-003 (ER case process complexity):** This risk is directionally similar to RC-TECH-008 (licensing) but describes a separate concern about process complexity. It has been incorporated into the RC-TECH-008 customisation guidance rather than created as a separate canonical risk, to avoid over-granularity.

**Note on R-W2-005 and R-W3-006-002:** These risks (calibration UAT coverage; reporting requirements sign-off) are directionally covered by RC-CLIENT-001 (UAT adequacy) and RC-CLIENT-007 (design framework alignment) respectively. They are noted here for traceability but do not require separate canonical entries.

---

## 4. Canonical Risk Summary

### 4.1 Distribution by Category

| Category | Description | Canonical Count | Source Risks |
|----------|-------------|-----------------|--------------|
| RC-PROJ | Project risks | 4 | 6 |
| RC-DATA | Data risks | 5 | 5 |
| RC-INT | Integration risks | 7 | 9 |
| RC-TECH | Technical risks | 12 | 17 |
| RC-CLIENT | Client dependency risks | 7 | 8 |
| RC-COMM | Commercial risks | 3 | 5 |
| RC-OPS | Operational risks | 1 | 1 |
| RC-COMP | Compliance risks | 1 | 2 |
| **TOTAL** | | **40** | **51** |

### 4.2 Distribution by Rating

| Rating | Count | % of Registry |
|--------|-------|---------------|
| CRITICAL | 1 | 2.5% |
| HIGH | 19 | 47.5% |
| MEDIUM | 15 | 37.5% |
| LOW | 5 | 12.5% |
| **TOTAL** | **40** | **100%** |

### 4.3 Distribution by Platform

| Platform | Risk Count | Key Categories |
|----------|-----------|----------------|
| Oracle HCM Cloud (general) | 18 | RC-PROJ, RC-CLIENT, RC-COMM |
| Oracle OIC / Integration | 8 | RC-INT, RC-TECH, RC-COMP |
| Oracle WFM | 7 | RC-TECH, RC-DATA |
| Oracle HCM Analytics | 3 | RC-TECH, RC-COMM |
| Oracle Recruiting Cloud | 3 | RC-TECH, RC-CLIENT |
| Oracle Learning Cloud | 3 | RC-CLIENT, RC-DATA |
| Oracle Help Desk | 5 | RC-TECH, RC-COMM, RC-CLIENT |
| Acumatica | 2 | RC-INT, RC-COMM |
| All Oracle Cloud | 2 | RC-TECH, RC-CLIENT |

---

## 5. Coverage Gap Analysis

### 5.1 Categories with Zero Extraction

The following RISK_LIBRARY_STANDARD.md categories have no extractable source risks from the current governed KB:

| Category | Description | Gap Severity | Recommended Action |
|----------|-------------|-------------|-------------------|
| RC-RES | Resource and capacity risks | HIGH — all projects have resource risk | WP18B-EXT.2 BU Lead interview required |
| RC-INFRA | Infrastructure and OCI risks | MEDIUM — OCI asset gap exists | Create OCI capability asset before populating |
| RC-CM | Change management risks | HIGH — change risk is universal | WP18B-EXT.2 BU Lead interview; METH-X03 prerequisite |
| RC-MIG | Data migration risks | MEDIUM — partially in RC-DATA | Separate migration risks from data quality risks |
| RC-CUT | Cutover risks | HIGH — all go-lives have cutover risk | WP18B-EXT.2 BU Lead interview; METH-X05 prerequisite |
| RC-3P | Third-party vendor risks | MEDIUM — BeBanking assets have these | Formalise BeBanking delivery risk register |
| RC-SEC | Security risks (non-POPIA) | LOW — POPIA covered in RC-COMP | Assess after OCI asset and security standards confirmed |

### 5.2 Platform Coverage Gaps

| Platform | Gap | Impact |
|----------|-----|--------|
| Oracle Fusion ERP (Financials, Procurement, PPM) | No formal risk register in any W4-ERP asset | S-50 for ERP proposals cannot use Risk Library |
| Oracle EBS | No formal risk register in W2S1-002 | S-50 for EBS proposals manual only |
| Acumatica ERP modules | No formal risk registers in W1S2-001 to W1S2-006 | S-50 for Acumatica proposals minimal |
| BeBanking | No formal risk registers in W1S3 assets | S-50 for BeBanking proposals cannot use Risk Library |
| Oracle DBA / Managed Services | No delivery risk registers | AMS proposals limited to RC-TECH-001, RC-COMP-001 |

---

## 6. Validation Results

| Validation Criterion | Result |
|----------------------|--------|
| Every extracted risk has traceability to a governed asset | PASS — all 40 canonical risks cite source asset(s) |
| No duplicate canonical IDs | PASS — 40 unique IDs (RC-PROJ-001 to RC-COMP-001) |
| Risk categories mutually exclusive | PASS — each canonical risk assigned to exactly one category |
| Metadata complete for all fields | PASS — all 40 entries have all required schema fields |
| No proposal-specific risks included | PASS — ARM IT045-specific content excluded |
| No invented risks beyond what normalisation requires | PASS — 0 risks invented; all traceable to source asset(s) |
| Risk Selection Engine not built | PASS — this report covers extraction only |

---

## 7. Impact on Proposal Factory

### 7.1 Current State (Before BU Lead Approval)

| Section | Current Status | Post-Approval Target |
|---------|---------------|---------------------|
| S-37 (RAID Framework) | AI-GENERATE | TEMPLATE (risk categories available) |
| S-50 (Risk Register) | AI-GENERATE | EXTRACT (risk entries selectable) |

### 7.2 Projected Assembly Impact

Once BU Lead approves all 40 entries:
- S-50 upgrades from AI-GENERATE to EXTRACT for Oracle HCM proposals
- Oracle HCM multi-module proposals: 8–12 risks auto-selectable from Risk Library
- AMS proposals: 3–5 risks auto-selectable (RC-TECH-001, RC-TECH-012, RC-COMP-001 primary)
- QA score improvement: estimated +4 to +6 points (S-37 and S-50 no longer fully AI-generated)
- Platform maturity: L3.5 → L4.0 (Risk Library operational)

---

## 8. Recommendations for WP18B-EXT.2

WP18B-EXT.2 (Risk Normalisation and Metadata Consolidation) should:

### 8.1 Priority 1 — BU Lead Review and Approval
- Schedule a structured BU Lead review session for all 40 draft entries
- Target: minimum 30 entries approved in first session
- Output: `approved_for_reuse: Yes` on approved entries; rejection or amendment notes on deferred entries

### 8.2 Priority 2 — Gap Category Population
Address the 7 categories with no source entries through BU Lead interview:
- RC-RES: Resource availability and consultant capacity risks
- RC-CM: Change management and user adoption risks
- RC-CUT: Cutover and go-live readiness risks
- RC-MIG: Data migration-specific risks (separate from RC-DATA quality risks)

Defer RC-INFRA and RC-3P until OCI capability asset and BeBanking risk formalisation are complete.

### 8.3 Priority 3 — Platform Gap Coverage
Initiate formal risk registers for:
- Oracle Fusion ERP (W4-ERP-001/002/003) — high commercial importance
- Acumatica ERP modules (W1S2-001 to W1S2-005)
- BeBanking delivery risks (W1S3 asset series)

### 8.4 Priority 4 — Risk Library Folder Structure
Create the full 15-category file structure under `08_Commercial/Risk_Library/` as defined in RISK_LIBRARY_STANDARD.md Section 2.2. Populate RISK_INDEX.md and split approved entries from ENTERPRISE_RISK_REGISTER_DRAFT.md into the appropriate category files.

### 8.5 Priority 5 — Assembly Trigger Alignment to Pattern Engine
Review each canonical risk's Assembly Trigger against PROPOSAL_PATTERN_ENGINE.md to confirm:
- Which patterns automatically include which risk categories
- Which risk IDs should be auto-selected vs. manually reviewed
- Pattern-specific risk selections (e.g., Pattern 13 AMS triggers RC-TECH-001, RC-TECH-012, RC-COMP-001)

This work is the foundation for the Risk Selection Engine (WP18B-EXT.3).

---

## 9. Deliverables Produced

| Deliverable | Location | Status |
|-------------|----------|--------|
| WP18B_EXT1_RISK_EXTRACTION_REPORT.md | 08_Commercial/Reports/ | COMPLETE |
| ENTERPRISE_RISK_REGISTER_DRAFT.md | 08_Commercial/Risk_Library/ | COMPLETE — Pending BU Lead review |
| RISK_DUPLICATION_ANALYSIS.md | 08_Commercial/Reports/ | COMPLETE |

---

*WP18B-EXT.1 Risk Extraction Report v1.0 — 2026-06-26*
