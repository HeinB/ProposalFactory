---
document_id: SVR-W3S1-005
title: "Source Validation Report — Oracle Workforce Compensation"
version: "1.1"
status: "CLOSED — All blocking open items resolved 2026-06-13. Extraction AUTHORISED."
extraction_target: "W3S1-005-ORA-WorkforceCompensation"
created: "2026-06-13"
created_by: "Claude (AI — Wave 3 SVR)"
business_unit: "Oracle"
wave: "3"
---

# Source Validation Report
## SVR-W3S1-005 — Oracle Workforce Compensation (Oracle Fusion Workforce Compensation Cloud)

**Prepared:** 2026-06-13 | **Wave:** 3 | **BU:** Oracle | **Status:** BU Lead Decisions Required

---

## 1. Executive Summary

This Source Validation Report (SVR) covers W3S1-005 Oracle Workforce Compensation. A full corpus review has been conducted against all primary Wave 3 source documents.

**Primary finding:** Oracle Fusion Workforce Compensation Cloud is a well-documented platform capability across Wave 3 sources, with rich content available in HIST-006 (SAA HCM RFP) and HIST-014 (CCBA — restricted). However, **no Tier 1 referenceable implementation evidence currently exists for Oracle Fusion Workforce Compensation Cloud.** Hollywood Bets explicitly excluded Workforce Compensation from their accepted BOM. Neither DFA, Mr Price, nor any other confirmed referenceable client has Workforce Compensation in their confirmed scope.

The only active implementation evidence identified is:
- **Redpath Mining** — Workforce Compensation is confirmed in active implementation scope (ORACLE_FACT_BASELINE Section 21.5) but is not yet live and not referenceable under Rule 21.5.
- **Afrocentric Health** — Workforce Compensation was scoped as Phase 1.5, Option 1, in the V4.0 proposal, but Afrocentric is not a confirmed referenceable client and implementation status is unconfirmed.

Three open items are **extraction blocking** and require BU Lead decisions before extraction can proceed. The proposed document structure and coverage analysis are included below to enable efficient decision-making.

**Extraction Readiness:** ✅ AUTHORISED — All 3 blocking open items closed by BU Lead 2026-06-13. OI-W5-004 and OI-W5-005 advisory items resolved by conservative application during extraction.

---

## 2. Source Evidence Classification

### 2.1 Primary Wave 3 Sources — Compensation Search Results

| Source | HIST ID | Document | Date | Compensation Hits | Classification |
|---|---|---|---|---|---|
| Hollywood Bets Accepted Proposal V5.0 | HIST-007 | APPSolve_HollywoodBets_Oracle Implementation 3rd part_V5.0.docx | April 2023 | **1 (BOM header only — no Workforce Compensation content)** | Tier 1 — Primary implementation evidence; does NOT support Workforce Compensation |
| SAA HCM RFP Response | HIST-006 | APPSolve_SAA_RFP.docx | June 2025 | **69** | Tier 3 — Platform capability; reframe only; SAA never named |
| CCBA Oracle HCM Solution V2.0 | HIST-014 | APPSolve_CCBA_HCM_Solution_V2.0.docx | May 2025 | **45** | Tier 3 — RESTRICTED; extraction support only; CCBA never named |
| Afrocentric HCM Proposal V4.0 | HIST-015 | APPSolve Afrocentric - HCM Proposal V4.0.docx | 2023 | **9** | Tier 3 — Delivery methodology; Afrocentric not confirmed referenceable |
| Redpath Mining RFI Reply | HIST-008 | RedPath Mining_APPSolve_RFI Reply Detail.docx | March 2026 | **0** | Rule 21.5 — active pipeline only |
| SABS ETS Oracle Fusion | HIST-016 | APPSolve_SABS_RFP_Response.docx | December 2025 | **0** | Tier 3 — No Compensation content |
| SAA HCM Additional Information | HIST-017 | APPSolve_SAA_Additional Information.docx | June 2025 | **1 (word only)** | Tier 3 — No substantive Compensation content |

### 2.2 Hollywood Bets BOM — Confirmed Module List

Hollywood Bets Accepted Proposal V5.0, paragraph 56: *"The modules and associated functionality for the implementation are limited to one country only and the below Bill of Material:"*

| # | Module | In BOM |
|---|---|---|
| 1 | Fusion Human Capital Management Base Cloud Service | ✅ |
| 2 | Fusion Recruiting Cloud Service | ✅ |
| 3 | Fusion Talent Management Cloud Service | ✅ |
| 4 | Fusion Goal Management Cloud Service | ✅ |
| 5 | Fusion Performance Management Cloud Service | ✅ |
| 6 | Fusion Talent Review and Succession Management | ✅ |
| 7 | Fusion Career Development Cloud Service | ✅ |
| 8 | Integration to 3rd Party Payroll (via OIC) | ✅ |
| — | **Fusion Workforce Compensation Cloud Service** | **❌ ABSENT** |
| — | Fusion Learning Cloud Service | ❌ ABSENT (Moodle retained) |
| — | Fusion Time and Labor | ❌ ABSENT |

**Finding:** Oracle Fusion Workforce Compensation Cloud was not licensed or implemented as part of the Hollywood Bets HCM implementation. This is a definitive exclusion, not an omission.

### 2.3 ORACLE_FACT_BASELINE — Current Recorded Position

| Field | Recorded fact | Section |
|---|---|---|
| Workforce Compensation listed as confirmed module | Yes — confirmed in SAA Section 2 | Section 4.1 |
| Workforce Compensation source | SAA Section 2 (platform capability only) | Section 4.1 |
| Hollywood Bets confirmed HCM modules | Core HR, Absence, Recruiting, Talent, Performance, Career Development, Succession, Help Desk — **Workforce Compensation NOT listed** | Section 19 |
| DFA confirmed HCM scope | Core HCM, Talent Management, Learning Cloud, Taleo Recruiting — **Workforce Compensation NOT listed** | Section 19 / Rule 21.4 |
| Redpath Mining HCM scope | Core HR, Absence, Recruiting & Onboarding, **Compensation**, Talent Management | Section 21.5 |

---

## 3. Coverage Analysis

The following table maps each expected validation area to available source evidence.

| Validation Area | HIST-006 (SAA) | HIST-015 (Afrocentric) | HIST-007 (HB V5.0) | HIST-014 (CCBA — restricted) | OFB Section | Evidence quality |
|---|---|---|---|---|---|---|
| 1. Compensation Planning | ✅ Rich — plans by segment, BU, location | ✅ "Rules-based plans" | ❌ | ✅ Rich | 4.1 | Platform capability — no implementation evidence |
| 2. Merit Increase Management | ✅ Paragraphs 216–218 | ❌ | ❌ | ✅ | — | Platform capability only |
| 3. Salary Review Processes | ✅ Paragraphs 207–209 (Managerial Reviews) | ✅ Implied | ❌ | ✅ | — | Platform capability only |
| 4. Variable Pay Administration | ✅ Paragraph 197 (bonuses, long-term incentives) | ❌ | ❌ | ✅ | — | Platform capability only |
| 5. Bonus Planning | ✅ Paragraphs 197, 876 | ❌ | ❌ | ✅ | — | Platform capability only |
| 6. Compensation Budgets | ✅ Paragraphs 202, 876 | ❌ | ❌ | ✅ | — | Platform capability only |
| 7. Manager Compensation Worksheets | ✅ Paragraphs 207–209 (Managerial Reviews, approval workflows) | ❌ | ❌ | ✅ | — | Platform capability only |
| 8. Compensation Approval Workflows | ✅ Paragraph 208 | ❌ | ❌ | ✅ | — | Platform capability only |
| 9. Total Compensation Statements | ✅ Paragraphs 210–213 | ❌ | ❌ | ✅ | — | Platform capability only |
| 10. Compensation Analytics | ✅ Paragraphs 229–231 (OWC built-in); 884–888 (OAX) | ❌ | ❌ | ✅ | — | **AMBIGUOUS — see OI-W5-004** |
| 11. Pay Equity Analysis | ✅ Paragraph 231 | ❌ | ❌ | ✅ | — | Platform capability only |
| 12. Compensation Self-Service | ✅ Paragraphs 234–235 | ❌ | ❌ | ✅ | — | Platform capability only |
| 13a. Integration — Core HR | ✅ Paragraph 221 | ❌ | ❌ | ✅ | — | Platform capability only |
| 13b. Integration — Talent Management | ✅ Paragraph 221 | ❌ | ❌ | ✅ | — | Platform capability only |
| 13c. Integration — Performance Management | ✅ Paragraph 221 | ❌ | ❌ | ✅ | — | Platform capability only |
| 13d. Integration — Goal Management | ✅ Paragraph 222 | ❌ | ❌ | ✅ | — | Platform capability only |
| 14. OIC Integration Requirements | ✅ Paragraph 873 (Compensation + Workforce Planning cited together) | ❌ | ❌ | ✅ | Section 7 | Standard — OIC mandatory per ORACLE_FACT_BASELINE Section 7 |
| 15. Compensation Security Model | ❌ Not explicitly covered | ❌ | ❌ | ❌ | — | No source coverage |
| 16. Individual Compensation Plans (ICPs) | ✅ Paragraphs 775–779 (travel allowance use case) | ❌ | ❌ | ✅ | — | Platform capability — ICP vs Workforce Comp distinction needed |
| 17. Salary Cost Planning | ✅ Paragraphs 872–879 (Compensation Management + Workforce Planning) | ❌ | ❌ | ❌ | — | **AMBIGUOUS — OWC + Workforce Planning overlap** |
| 18. Equity-based compensation | ✅ Paragraph 198 (stock options, equity grants) | ❌ | ❌ | ✅ | — | Platform capability — **applicability to SA context unclear** |
| 19. Implementation references | ❌ | ❌ Afrocentric = Option 1 (not confirmed) | ❌ | ❌ | — | **NO Tier 1 evidence — see OI-W5-001** |
| 20. Redpath Mining pipeline evidence | ❌ | ❌ | ❌ | ❌ | Section 21.5 | Confirmed in active scope — **see OI-W5-002** |

### 3.1 Coverage Confidence Summary

| Coverage area | Confidence | Limiting factor |
|---|---|---|
| Platform capability (Sections 1–9, 11–13) | HIGH | Rich HIST-006/HIST-014 content available |
| Compensation Security Model | LOW | No source coverage identified |
| Analytics boundary (OWC vs OAX) | MEDIUM — needs resolution | SAA paragraph 227 attributes analytics to OWC; paragraphs 884-888 place compensation dashboards in HCM Analytics |
| Individual Compensation Plans vs Workforce Compensation Plans | MEDIUM | SAA covers both but conflates in places |
| Equity-based compensation applicability | LOW | SA context uncertainty — stock options uncommon in listed SA co proposals |
| Implementation evidence | NONE — extraction blocking | No referenceable client; Redpath active; Afrocentric unconfirmed |

---

## 4. Implementation Evidence Assessment

### 4.1 Per-Client Assessment

| Client | Evidence type | Workforce Compensation status | Governance classification |
|---|---|---|---|
| Hollywood Bets | Accepted Proposal V5.0 (HIST-007) | **EXPLICITLY ABSENT** from BOM. Compensation not licensed, not scoped, not implemented. | Tier 1 — does NOT support W3S1-005 |
| Mr Price Group | ORACLE_FACT_BASELINE Section 19 | No evidence. Mr Price confirmed for Learning Cloud and Opportunity Marketplace only. | Not applicable to Compensation |
| DFA (Dark Fibre Africa) | ORACLE_FACT_BASELINE Section 19 / Rule 21.4 | **NOT CONFIRMED**. DFA scope confirmed as Core HCM, Talent, Learning, Taleo Recruiting. Workforce Compensation is not in the confirmed DFA scope. DFA Monthly Reports mention "Compensation Reporting" activities but this may refer to reporting on existing salary data rather than Oracle Workforce Compensation module. | Rule 21.4 — never named. Scope confirmation required (see OI-W5-003). |
| Redpath Mining | ORACLE_FACT_BASELINE Section 21.5 | **CONFIRMED IN ACTIVE SCOPE** — "Compensation" is listed in Redpath Mining's active implementation scope. Not yet live. Not referenceable. | Rule 21.5 — pipeline evidence only; requires BU Lead guidance on citation approach (see OI-W5-002) |
| Afrocentric Health | HIST-015 | **SCOPED AS OPTION 1** — Phase 1.5 includes Workforce Compensation in the V4.0 proposal. Implementation status unconfirmed (Option 1 may not have been taken). Not a confirmed referenceable client. | Tier 3 — Methodology; requires BU Lead confirmation (see OI-W5-005) |
| CCBA | HIST-014 | Rich Workforce Compensation content in proposal. CCBA PROHIBITED. | Never named — extraction support only |
| SAA | HIST-006 | Platform capability source only. SAA was not awarded. | Never named — platform content only |

### 4.2 Implementation Evidence Summary

| Tier | Classification | Client | Status |
|---|---|---|---|
| Tier 1 — Referenceable | **NONE IDENTIFIED** | — | No confirmed, referenceable Workforce Compensation client |
| Tier 2 — Internal Corroboration | DFA (pending confirmation) | Compensation not yet in confirmed DFA scope | Rule 21.4 — confirmation required |
| Active Pipeline | Redpath Mining | Compensation confirmed in active scope — not live | Rule 21.5 — pipeline citation requires BU Lead approval |
| Unconfirmed Proposal | Afrocentric Health | Scoped as Option 1 — status unknown | Requires BU Lead confirmation |

**Critical finding:** W3S1-005 has no Tier 1 referenceable implementation client. This is a materially different evidence position from W3S1-001 (Hollywood Bets), W3S1-002 (Hollywood Bets + Mr Price Opportunity Marketplace), W3S1-003 (Hollywood Bets Recruiting), and W3S1-004 (Mr Price Learning Cloud).

---

## 5. Proposed Source Hierarchy

This hierarchy is provisional, pending BU Lead decisions on open items.

| Tier | Source | HIST ID | Role | Applicable sections |
|---|---|---|---|---|
| **Tier 1A — Implementation Evidence (pending)** | Redpath Mining (if OI-W5-002 approved) | HIST-008 / ORACLE_FACT_BASELINE | Pipeline evidence only — "APPSolve is currently implementing Oracle Workforce Compensation for a mining-sector client" | Section 11 (References) |
| **Tier 1A — Internal Corroboration (pending)** | DFA (if OI-W5-003 confirmed) | ORACLE_FACT_BASELINE | Internal validation — never named | Capability confidence; Section 10 (APPSolve delivery) |
| **Tier 3A — Platform Capability** | SAA HCM RFP | HIST-006 | Primary platform capability narrative source | Sections 1–9, 11–14 |
| **Tier 3B — Restricted Support** | CCBA | HIST-014 | Extraction support — validation; content corroboration | Internal cross-check only |
| **Tier 3C — Delivery Methodology** | Afrocentric V4.0 | HIST-015 | Implementation assumptions and delivery framework | Implementation assumptions; delivery phasing |
| **Mandatory Standard** | ORACLE_FACT_BASELINE Section 7 | — | OIC as mandatory integration layer | Integration architecture |

**Note:** If all three extraction-blocking open items are resolved negatively (no Redpath, no DFA, no Afrocentric), the document will have no implementation evidence and must be scoped as a Platform Capability Statement only. BU Lead decision on acceptability of this positioning is required.

---

## 6. Proposed Document Structure

Subject to BU Lead decisions on open items, the following structure is proposed for the Candidate Draft:

| Section | Title | Source basis | Notes |
|---|---|---|---|
| 1 | Statement of Capability | HIST-006 (platform overview); Redpath/DFA (implementation evidence if confirmed) | Framing depends on OI-W5-001 resolution |
| 2 | Oracle Fusion Workforce Compensation Cloud — Module Overview | HIST-006 paragraphs 181–188 | Platform capability; APPSolve framing applied |
| 3 | Compensation Plans and Programs | HIST-006 paragraphs 195–204 | Merit, bonus, incentive, equity-based, flexible structures |
| 4 | Compensation Budgeting and Modelling | HIST-006 paragraphs 200–204, 876–879 | Budget cycles, what-if scenarios, forecasting |
| 5 | Compensation Review and Approval Workflows | HIST-006 paragraphs 205–209 | Managerial reviews, multi-level approvals, audit trail |
| 6 | Merit-Based and Performance-Driven Compensation | HIST-006 paragraphs 214–218 | Merit increases, performance metrics, pay-for-performance linkage |
| 7 | Total Compensation Statements | HIST-006 paragraphs 210–213 | Employee total rewards view |
| 8 | Employee and Manager Self-Service | HIST-006 paragraphs 234–235 | Self-service compensation access |
| 9 | Compensation Analytics and Reporting — Capability Scope and Boundaries | HIST-006 paragraphs 227–231, 884–888 | **OWC built-in vs OAX — pending OI-W5-004 resolution** |
| 10 | APPSolve Delivery Capability | ORACLE_FACT_BASELINE; HIST-015 delivery methodology | Practice, methodology, delivery approach |
| 11 | Implementation References | Redpath (if OI-W5-002) / DFA internal (if OI-W5-003) | Depends on open items |
| 12 | Integration Architecture | HIST-006 paragraph 221; ORACLE_FACT_BASELINE Section 7 | Core HR, Talent, Performance, Goal Management; OIC mandatory |
| 13 | Implementation Approach | HIST-015 Phase 1.5; ORACLE_FACT_BASELINE Section 17 (OUM) | OUM phases; compensation framework sequencing |
| 14 | Risk Register | SVR-based risk analysis | — |
| 15 | Assumptions Register | HIST-015 paragraphs 525–528; HIST-006 | Delivery assumptions for Workforce Compensation |
| 17 | Approval Record | — | Governance metadata |
| Appendix A | Source Mapping | — | — |
| Appendix B | Governance Self-Review | — | All Wave 3 rules confirmed |
| Appendix C | Extraction Return Report | — | — |

---

## 7. Governance Risks

| Risk ID | Risk | Severity | Mitigation |
|---|---|---|---|
| GR-W5-001 | No Tier 1 referenceable implementation evidence — capability statement may appear unsupported compared to peer W3S1 documents | HIGH | Resolve via OI-W5-001/OI-W5-002. If Redpath pipeline reference is approved, position clearly as active implementation. If not, position as platform capability only and note APPSolve's readiness to implement. |
| GR-W5-002 | Analytics overstatement — SAA attributes real-time dashboards and comparative analytics to Workforce Compensation (paragraphs 229–231), but pre-built dashboards and advanced compensation analytics are explicitly attributed to HCM Analytics in paragraphs 884–888 | HIGH | Do not extract SAA paragraphs 229–231 as OWC built-in without BU Lead guidance (OI-W5-004). May require the same OLC/OAX separation applied in W3S1-004. |
| GR-W5-003 | Equity-based compensation scope — SAA paragraph 198 cites stock options and equity grants. These are uncommon in South African implementations and may misrepresent typical APPSolve delivery scope for this market | MEDIUM | Qualify equity-based compensation as a platform capability applicable where relevant to client compensation strategy; do not present as standard South African implementation deliverable without BU Lead guidance |
| GR-W5-004 | Individual Compensation Plans (ICPs) vs Workforce Compensation Plans — these are distinct Oracle Fusion HCM constructs. SAA uses them interchangeably in places (e.g., paragraph 775 uses ICPs for travel allowances). Conflation could create misleading capability claims | MEDIUM | Separate ICP (individual management) from Workforce Compensation Plans (population-level planning cycles) in the document. Confirm ICP is a valid Workforce Compensation capability before including. |
| GR-W5-005 | Afrocentric implementation status unknown — Afrocentric V4.0 scopes Compensation as Option 1 but it is unconfirmed whether this option was accepted | MEDIUM | Resolve via OI-W5-005. Do not use Afrocentric as implementation evidence without BU Lead confirmation. |
| GR-W5-006 | Salary Cost Planning module boundary — SAA paragraph 872 addresses "Salary Cost Planning" across Compensation Management, Workforce Planning, and HCM Analytics as three distinct modules. Extracting salary cost planning as a Workforce Compensation capability may conflate three products | MEDIUM | Limit salary cost planning content to what is clearly within Workforce Compensation scope. Do not claim Workforce Planning or HCM Analytics capabilities as Workforce Compensation. |
| GR-W5-007 | Hollywood Bets cannot be cited — Hollywood Bets is the primary Tier 1 reference for all other W3S1 statements but is explicitly excluded from Workforce Compensation. Any attempt to imply Hollywood Bets implemented Workforce Compensation is a governance violation | HIGH | Enforce strict exclusion. Hollywood Bets must not appear in the implementation references section of W3S1-005. |

---

## 8. Open Items Register

### OI-W5-001 — Reference Hierarchy — **CLOSED (NO referenceable client) — BU Lead 2026-06-13**

**Description:** No Tier 1 referenceable Oracle Fusion Workforce Compensation implementation client has been identified. Hollywood Bets explicitly excluded Workforce Compensation from their BOM. No other confirmed, referenceable client is in scope.

**Evidence reviewed:**
- HIST-007 Hollywood Bets V5.0: BOM does not include Workforce Compensation Cloud Service
- ORACLE_FACT_BASELINE Section 19: Hollywood Bets modules do not include Workforce Compensation
- No other confirmed referenceable client has Workforce Compensation in confirmed scope

**Decision required from BU Lead:**

Select one of the following:

A. **Confirm an alternative referenceable client** — If there is a client not yet in the ORACLE_FACT_BASELINE who implemented Workforce Compensation and is approved as referenceable, provide client name and scope.

B. **Approve Redpath Mining pipeline evidence** — Approve use of the mining-sector pipeline framing (as per W3S1-003 precedent: "APPSolve is currently implementing Oracle Workforce Compensation for a mining-sector client") as the primary evidence positioning. *(Dependent on OI-W5-002.)*

C. **Position as Platform Capability Statement only** — Accept that W3S1-005 will not include a named implementation reference, and position the document as demonstrating readiness and platform knowledge rather than confirmed delivery. Include APPSolve's active implementation pipeline as context.

---

### OI-W5-002 — Redpath Mining Pipeline Citation — **CLOSED (APPROVED) — BU Lead 2026-06-13**

**Description:** ORACLE_FACT_BASELINE Section 21.5 confirms Workforce Compensation is in Redpath Mining's active implementation scope. Rule 21.5 permits pipeline evidence where governance allows. The W3S1-003 Recruiting Cloud precedent approved the following framing for Redpath: *"APPSolve is currently implementing Oracle Recruiting and Onboarding capabilities for a mining-sector client."*

**Question for BU Lead:**
1. May the same pipeline framing be applied for Workforce Compensation in W3S1-005?
2. Proposed approved wording (if yes): *"APPSolve is currently implementing Oracle Workforce Compensation capabilities for a mining-sector client."*
3. Is this framing permitted even in the absence of any other implementation reference?

**Evidence:** ORACLE_FACT_BASELINE Section 21.5 — "Oracle HCM Core, Absence Management, Recruitment and Onboarding, **Compensation**, and Talent Management" confirmed in Redpath active scope.

**Governance note:** This citation must not name Redpath Mining, must not imply go-live, and must explicitly state "currently implementing" rather than "has implemented."

---

### OI-W5-003 — DFA Compensation Scope Confirmation — **CLOSED (CONFIRMED) — BU Lead 2026-06-13**

**Description:** ORACLE_FACT_BASELINE Section 19 confirms DFA's HCM scope as: Oracle HCM Core, Oracle Talent Management, Oracle Learning Cloud, Oracle Taleo Recruiting. Workforce Compensation is **not** in the confirmed DFA scope.

DFA Monthly Reports (from corpus) reference "Compensation Reporting" activities, which may indicate Workforce Compensation was implemented or may simply relate to reporting on salary data from Core HR.

**Question for BU Lead:**
1. Was Oracle Workforce Compensation Cloud implemented for DFA?
2. If yes, should ORACLE_FACT_BASELINE Section 19 (DFA row) be updated to include Workforce Compensation?
3. If yes, does this constitute additional internal corroboration evidence for W3S1-005 (under Rule 21.4 — DFA never named externally)?

**Impact of positive confirmation:** Adds DFA as Tier 2 internal corroboration, confirming APPSolve's delivered Workforce Compensation experience across industries. Does not change public-facing citation approach (DFA never named).

---

### OI-W5-004 — Analytics Boundary (EXTRACTION ADVISORY)

**Description:** SAA HCM RFP contains two distinct analytics representations for Workforce Compensation:

**Section A — Within Workforce Compensation module description (SAA paragraphs 229–231):**
*"Real-Time Analytics: Track compensation trends, allocation rates, and total costs with powerful real-time dashboards. Comparative Analytics: Compare compensation levels across roles, departments, or regions to ensure fairness and market competitiveness. Pay Equity: Monitor and analyse pay equity to ensure compliance with internal policies and external regulations."*

**Section B — Explicitly attributed to HCM Analytics / OAX (SAA paragraphs 884–888):**
*"Pre-built Dashboards and KPIs: Provides pre-built analytics and dashboards specifically for payroll and compensation costing. Drill-down Capabilities... Historical Analysis... Variance Analysis..."*

SAA paragraph 873 explicitly names three separate products contributing to compensation analysis: **Compensation Management**, **Workforce Planning**, and **HCM Analytics**.

**Question for BU Lead:**
1. Should Oracle Workforce Compensation be presented as including built-in analytics (Compensation tracking, pay equity monitoring, comparative analytics at the plan level) — analogous to OLC's built-in completion tracking?
2. Or should the same strict separation applied in W3S1-004 (OLC tracking vs OAX analytics) be applied here?
3. Proposed position: Workforce Compensation includes built-in compensation tracking and plan-level analytics (completion of cycles, budget consumption, approval status). Advanced executive dashboards and cross-module analytics are delivered through Oracle HCM Analytics (OAX). Is this acceptable?

**Note:** This item is not extraction blocking — a standard separation can be applied conservatively — but BU Lead guidance will affect how Section 9 (Analytics) is framed.

---

### OI-W5-005 — Afrocentric Implementation Status (NON-BLOCKING)

**Description:** Afrocentric HCM Proposal V4.0 (HIST-015) includes Workforce Compensation as Phase 1.5, **Option 1 only** (R353,600 scoped). It is unknown whether Option 1 was selected and whether Workforce Compensation was implemented.

**Question for BU Lead:**
1. Was Workforce Compensation implemented for Afrocentric Health as part of the Oracle Fusion HCM engagement?
2. If yes, is Afrocentric Health approved as a referenceable client for any Wave 3 capability statement?
3. If yes and referenceable: this would provide a Tier 1 Healthcare sector implementation reference.

**Note:** This is not extraction blocking because Afrocentric would at most add to the methodology narrative; it does not change the fundamental reference hierarchy question in OI-W5-001.

---

## 9. Extraction Readiness Assessment

| Item | Status | Blocking |
|---|---|---|
| Source document review complete | ✅ Complete | — |
| Platform capability content available | ✅ Available — HIST-006 (69 hits); HIST-015 (9 hits) | — |
| Standing governance rules confirmed (21.1–21.5) | ✅ Applied | — |
| OIC mandatory standard confirmed | ✅ Confirmed | — |
| Hollywood Bets exclusion confirmed | ✅ Excluded — not in BOM | — |
| OI-W5-001 Reference Hierarchy | ❌ OPEN | **YES — extraction blocking** |
| OI-W5-002 Redpath Pipeline Citation | ❌ OPEN | **YES — extraction blocking** |
| OI-W5-003 DFA Compensation Scope | ❌ OPEN | **YES — extraction blocking** |
| OI-W5-004 Analytics Boundary | ❗ OPEN — Advisory | No — conservative default available |
| OI-W5-005 Afrocentric Status | ❗ OPEN — Non-blocking | No |
| Equity-based compensation applicability | ❗ Advisory | No — can be qualified as platform capability |
| ICP vs Workforce Compensation distinction | ❗ Advisory | No — can be resolved during extraction |

**Overall extraction readiness: ✅ AUTHORISED — 2026-06-13**

OI-W5-001 CLOSED (NO referenceable client — document positions without named Tier 1 reference; Redpath pipeline applies per OI-W5-002).
OI-W5-002 CLOSED (APPROVED — Redpath pipeline framing: "APPSolve is currently implementing Oracle Workforce Compensation capabilities for a mining-sector client").
OI-W5-003 CLOSED (CONFIRMED — DFA implemented Workforce Compensation; ORACLE_FACT_BASELINE Section 19 updated; Rule 21.4 unchanged — DFA never named).
OI-W5-004 ADVISORY — Conservative OWC/OAX separation applied (same model as W3S1-004).
OI-W5-005 ADVISORY — Afrocentric used for methodology and assumptions only; not as implementation evidence.

Estimated impact of open items on document scope:
- Positive resolution of OI-W5-002 (Redpath) → standard pipeline reference in Section 11
- Positive resolution of OI-W5-003 (DFA) → adds internal corroboration to Section 10; ORACLE_FACT_BASELINE Section 19 updated
- Negative resolution of all three blocking OIs → document restructures as Platform Capability Statement only; BU Lead to confirm acceptability of this positioning

---

## 10. Standing Governance Confirmations

The following Wave 3 governance rules have been confirmed applied during this SVR:

| Rule | Confirmation |
|---|---|
| Rule 21.1 — Aviation PROHIBITED | ✅ No aviation content identified in any compensation source; no aviation sector claims |
| Rule 21.2 — Implementation vs Support distinction | ✅ No support-only claims; implementation vs platform framing maintained throughout |
| Rule 21.3 — Opportunity Marketplace | ✅ Not applicable to Workforce Compensation |
| Rule 21.4 — DFA never named externally | ✅ DFA scope confirmation requested internally only (OI-W5-003); DFA will never appear in public-facing content |
| Rule 21.5 — Redpath Mining not referenceable | ✅ Redpath pipeline citation approach requested (OI-W5-002); Rule 21.5 framing applied strictly |
| CCBA PROHIBITED | ✅ HIST-014 used as extraction support only; CCBA will not appear in any content |
| SAA never cited as client | ✅ SAA used as platform capability source only; reframed throughout |
| OIC mandatory | ✅ Noted in integration architecture section proposal; ORACLE_FACT_BASELINE Section 7 applied |
| APPSolve framing | ✅ All platform capability will be framed as "APPSolve configures and enables" or "APPSolve implements" — not "Oracle does X" |
| Hollywood Bets exclusion from Workforce Compensation | ✅ Confirmed — HB BOM does not include Workforce Compensation; HB will not appear in W3S1-005 implementation references |
| Approved HCM sectors | ✅ Retail, Mining, Professional Services — no sector overreach identified |

---

## Appendix A: Evidence Reference Table

| Source | Paragraph references | Content |
|---|---|---|
| HIST-006 SAA | 181–235 | Full Workforce Compensation section: plans, budgeting, reviews, approvals, total comp statements, merit-based comp, flexible structures, analytics, self-service |
| HIST-006 SAA | 775–779 | Individual Compensation Plans — travel allowance use case |
| HIST-006 SAA | 872–889 | Salary Cost Planning — distinguishes Compensation Management, Workforce Planning, HCM Analytics |
| HIST-006 SAA | 314–315 | Integration cross-reference: Core HR, Workforce Compensation, Learning, Payroll — holistic talent strategy |
| HIST-015 Afrocentric | 340, 412–413, 435 | Phase 1.5 Workforce Compensation (Option 1) — module description and costing |
| HIST-015 Afrocentric | 525–528 | Workforce Compensation delivery assumptions (4 confirmed assumptions) |
| HIST-007 HB V5.0 | 56–64 | BOM — Workforce Compensation explicitly ABSENT |
| HIST-014 CCBA | 16, 212–260 | Full Workforce Compensation section — mirrors SAA structure (restricted — internal validation only) |
| ORACLE_FACT_BASELINE | Section 4.1 | Workforce Compensation listed; SAA Section 2 only |
| ORACLE_FACT_BASELINE | Section 19 | HB confirmed modules — Compensation absent; Redpath — Compensation confirmed in active scope |
| ORACLE_FACT_BASELINE | Section 21.5 | Redpath Mining — Compensation in active scope; not live; not referenceable until go-live + BU Lead approval |

---

## Appendix B: Afrocentric Delivery Assumptions — Workforce Compensation

The following assumptions were documented for Workforce Compensation in HIST-015 (Afrocentric V4.0, paragraphs 525–528):

1. Workforce Compensation is viewed as a Global function, and each country will utilise common business rules
2. Framework will be enabled but the development of individual compensation plans will be the responsibility of AFROCENTRIC
3. No data take-on will be required for Workforce compensation

*These assumptions are proposed for inclusion in the Assumptions Register of the Candidate Draft, subject to BU Lead confirmation of applicability.*

---

**SVR Prepared by:** Claude (AI — Wave 3 SVR engine)
**SVR version 1.0 date:** 2026-06-13
**SVR version 1.1 date:** 2026-06-13 — BU Lead decisions applied; open items closed
**BU Lead decisions:** OI-W5-001 CLOSED (NO referenceable client); OI-W5-002 CLOSED (Redpath pipeline APPROVED); OI-W5-003 CLOSED (DFA Workforce Compensation CONFIRMED; ORACLE_FACT_BASELINE updated)
**ORACLE_FACT_BASELINE updates:** Section 19 DFA row updated (Workforce Compensation added); Section 21.4 approved fact updated
**Extraction authorisation:** ✅ GRANTED — 2026-06-13
