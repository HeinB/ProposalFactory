---
document_id: SVR-W3S1-007
title: "Source Validation Report — W3S1-007 Oracle Workforce Management"
version: "1.1"
status: "AUTHORISED — All 5 OI items CLOSED 2026-06-13 — BU Lead decisions applied"
created: "2026-06-13"
created_by: "Claude (AI — Wave 3 W3S1-007 SVR)"
extraction_target: "W3S1-007-ORA-WorkforceManagement-DRAFT.md"
kb_destination: "06_Capabilities/Oracle/Oracle_HCM/"
---

> **SVR v1.1 — AUTHORISED — All 5 OI items CLOSED 2026-06-13 — Extraction AUTHORISED — Proceed to Candidate Draft**

---

# Source Validation Report
## W3S1-007 — Oracle Workforce Management

**Date:** 2026-06-13 | **Extractor:** Claude (AI) | **Owner:** Hein Blignaut

---

## Section 1: Executive Summary

This SVR covers the full corpus review for W3S1-007 — Oracle Workforce Management. The target capability area encompasses: Absence Management, Time and Labor, Workforce Scheduling, mobile time capture, manager self-service workforce administration, and Workforce Health and Safety (scope TBD).

**Overall assessment:** Absence Management has strong Tier 1 implementation evidence. Time and Labor has confirmed client-level evidence but with an unresolved governance conflict that requires BU Lead adjudication before extraction. Workforce Scheduling is platform capability only — no confirmed APPSolve implementation. Health and Safety has zero evidence across all source documents — BU Lead must decide include or exclude. Mobile and manager self-service are standard platform capabilities embedded throughout the HCM suite.

**Extraction readiness: AUTHORISED 2026-06-13 — All 5 OI items CLOSED — Proceed to Candidate Draft**

| Module | Evidence quality | BU Lead decision required |
|---|---|---|
| Absence Management | Tier 1 — multiple confirmed implementations | No — confirmed |
| Time and Labor | Tier 1 candidate — governance conflict to resolve | YES — OI-W7-001 BLOCKING |
| Workforce Scheduling | Platform capability only — no implementation evidence | No (advisory framing question — OI-W7-002) |
| Manager Self-Service | Platform capability — standard HCM | No |
| Mobile Workforce | Platform capability + biometric integration (HB) | No |
| Health and Safety | ZERO evidence — gap confirmed | YES — OI-W7-003 BLOCKING |

---

## Section 2: Source Evidence Classification

Source documents reviewed in this SVR, in tier order:

| HIST ID | Document | Date | Tier | Workforce Management relevance |
|---|---|---|---|---|
| HIST-007 | Hollywood Bets Accepted Proposal V5.0 | April 2023 | Tier 1 (Implementation) | Absence Management confirmed in Phase 3.3.1 BOM; Biometric system integration confirmed; T&L and Workforce Scheduling absent from BOM |
| HIST-016 | SABS ETS Oracle Fusion RFP Response | Dec 2025 | Tier 1 (Client reference evidence) | Mr Price reference confirms "involvement in the rollout of Oracle Time and Labour to their stores across South Africa" — governance question on classification |
| HIST-006 | SAA HCM RFP Response | June 2025 | Tier 2 (Platform capability) | Full T&L and Workforce Scheduling platform capability narrative (paras 216–247); Absence Management section (paras 334–344); Manager self-service section (paras 520–535); Mobile capabilities (paras 538–550) |
| HIST-008 | RedPath Mining RFI Reply | March 2026 | Active pipeline | T&L not in Redpath scope (confirmed by RACI document); Absence Management confirmed in RACI |
| HIST-015 | Afrocentric HCM Proposal V4.0 | 2023 | Tier 3 (Delivery methodology) | T&L proposed as Option 1 (para 202–203); T&L delivery assumptions (paras 296–299); Absence in Phase 3.3.1; Workforce Compensation also in scope |
| HIST-014 | CCBA Oracle HCM Solution V2.0 | May 2025 | Tier 3 (Restricted — SVR research only) | No T&L section; No Workforce Scheduling section; No Health and Safety; modules = Core HR, Compensation, Recruiting, Talent, Help Desk, Learning, HCM Analytics |
| HIST-017 | SAA HCM Additional Information | June 2025 | Tier 2 (Supplementary) | No Workforce Management-specific content — support/maintenance SLA framing only |

**Redpath Mining RACI document (internal governance):** Confirmed Redpath implementation scope = Core HR, Absence Management, Recruitment & Onboarding, Compensation, Talent Management. **Time and Labor confirmed absent from Redpath scope.**

---

## Section 3: Module-Level Evidence Analysis

### 3.1 Absence Management

**Evidence status: CONFIRMED — Tier 1 implementation evidence**

Absence Management is the most consistently confirmed module across all APPSolve Oracle HCM implementations. It is standard Phase 1 content in every APPSolve HCM engagement.

| Evidence item | Source | Detail |
|---|---|---|
| Hollywood Bets Phase 3.3.1 | HIST-007 para 147 | "Human Capital (Core and **Absence** and Self Service)" — Phase 3.3.1 BOM confirmed |
| Redpath Mining RACI scope | Redpath RACI para 9 | "Core HR, **Absence Management**, Workforce Compensation, Talent Management, Recruiting" — active implementation |
| Afrocentric Phase 3.3.1 | HIST-015 para 193 | "Human Capital (Core and **Absence** and Self Service)" — confirmed delivery phase |
| SAA RFP Absence platform capability | HIST-006 paras 334–344 | Full absence management platform narrative: leave types, accruals, self-service requests, manager approval, payroll integration, real-time balance tracking |
| SAA RFP assumptions | HIST-006 para 788, 795 | "HCM Core, Absence and Self Service" delivery assumptions; "Legislative specific requirement for absence must be documented in a standardised format" |
| ORACLE_FACT_BASELINE Section 4.1 | Confirmed | Absence Management confirmed in SAA Section 2 and Hollywood Bets Phase 1 |

**Confirmed platform capabilities (from HIST-006 paras 334–344):**
- Leave type definitions (annual, sick, maternity, bereavement, etc.)
- Absence plan accruals and entitlement calculations
- Employee self-service leave requests
- Manager approval workflows
- Real-time leave balance visibility
- Payroll integration for absence deductions
- Legislative absence requirements (SA-specific framing available)

**APPSolve delivery framing:** "APPSolve configures and implements Oracle Absence Management as a standard deliverable in every Oracle Fusion HCM implementation. Absence Management is typically delivered in Phase 1 alongside Core HR."

**Sector confirmation:** Retail (Mr Price — support and implementation context); Mining (Redpath Mining — active pipeline); Professional Services (Afrocentric).

---

### 3.2 Oracle Time and Labor

**Evidence status: TIER 1 CANDIDATE — governance conflict requires BU Lead decision (OI-W7-001 BLOCKING)**

**The evidence:** HIST-016 SABS ETS reference table (Table 3) — Mr Price entry:
> *"Implementation and support of Oracle Fusion HCM and integration between this system and other 3rd party systems in our group. **This includes involvement in the rollout of Oracle Time and Labour to their stores across South Africa.**"*

This is the strongest available evidence for T&L. The language "involvement in the rollout" uses implementation language and describes a store-by-store deployment of Oracle Time and Labour across South Africa.

**The governance conflict:** Wave 3 governance rule C-W3-002 (ORACLE_FACT_BASELINE Section 21.2) states:
> *"Mr Price broader HCM = support only (except Learning Cloud and Opportunity Marketplace)"*

The T&L "rollout" statement in HIST-016 uses implementation language, but the existing C-W3-002 governance framework classifies Mr Price beyond Learning Cloud + Opportunity Marketplace as support only. There is a direct conflict.

**The conflict must be resolved by the BU Lead before extraction.**

**Option A — If BU Lead classifies Mr Price T&L as implementation:**
- Mr Price becomes a Tier 1 T&L implementation reference
- "APPSolve has implemented Oracle Time and Labor for a major retail client, including a multi-store rollout across South Africa"
- T&L = confirmed delivery capability in W3S1-007

**Option B — If BU Lead confirms Mr Price T&L as support engagement only:**
- No confirmed APPSolve T&L implementation client exists
- T&L framing = Platform Capability with confirmed delivery readiness (Afrocentric option scope)
- Same framing model as OAX in W3S1-006

**Additional T&L evidence (regardless of OI-W7-001 outcome):**
- HIST-015 Afrocentric para 202–203: T&L proposed as Option 1 scope; T&L delivery assumptions confirmed (paras 296–299):
  - "No Data migration to be done for Time and Labor"
  - "The only integrations in scope would be for a time logging/access control solution and a Payroll solution"
- HIST-006 SAA RFP paras 216–232: Full T&L platform capability narrative
- ORACLE_FACT_BASELINE Section 4.1: Time and Labor confirmed in SAA Section 2 and SABS ETS (Mr Price)

**Platform capability narrative available (from HIST-006 paras 218–230):**
- Time capture: web clock, time cards, physical clocks
- Automated time collection and approval workflows
- Labor policy enforcement and compliance
- Integration with Oracle Payroll, Absence Management, and Project Costing
- Real-time insights into time usage, productivity, and labor costs
- Rules-driven engine for overtime, shift differentials, and labor law compliance

---

### 3.3 Workforce Scheduling

**Evidence status: Platform Capability Only — no confirmed APPSolve implementation**

**Source evidence:** HIST-006 SAA RFP paras 233–247 only. No other source document references Workforce Scheduling. Not present in any client BOM reviewed.

**Platform capability narrative available (from HIST-006 paras 233–247):**
- Aligns workforce schedules with business demands
- Designed for complex staffing environments (retail, manufacturing, healthcare)
- Compliance with labor laws, union rules, and organizational policies
- Self-service scheduling options and shift preferences
- Integration with Oracle Time and Labor, Absence Management, and Payroll
- Labor cost control — aligning schedules with budgets, minimizing overtime

**Governance risk (OI-W7-002 — advisory):** The SAA RFP describes Workforce Scheduling as "part of Oracle Fusion Cloud HCM" (para 235). However:
- Workforce Scheduling may be a separately licensed module (like OAX — separately licensed despite being "part of" the HCM family)
- The BOM evidence shows no client has licensed and implemented Workforce Scheduling via APPSolve
- If Workforce Scheduling is separately licensed, the licensing boundary disclosure rule must apply (same as OAX and Predictive Analytics in W3S1-006)

**Proposed framing:** Platform Capability regardless of licensing outcome. If separately licensed, add licensing disclosure note equivalent to OAX in W3S1-006.

---

### 3.4 Manager Self-Service and Workforce Visibility

**Evidence status: Standard Platform Capability — no open items**

Confirmed standard Oracle Fusion HCM capability across all source documents. Not a separately licensed module.

**From HIST-006 paras 520–535:**
| Manager Self-Service Capability | Detail |
|---|---|
| Leave management | Approve/deny leave requests; submit absence requests on behalf of employees |
| Time management | Review and approve timecards; overtime approval (requires T&L in scope) |
| Team visibility | View employee profiles, leave balances, performance, learning progress for direct reports |
| Workforce actions | Initiate promotions, transfers, terminations with approval workflows |
| Recruitment participation | Review candidates, feedback, offer approvals for team positions |

---

### 3.5 Mobile Workforce Capabilities

**Evidence status: Platform Capability + one implementation integration (Hollywood Bets biometric)**

**From HIST-006 paras 538–550:** Oracle HCM Cloud Mobile App (iOS and Android):
- Updating personal information
- Submitting and approving leave requests
- Viewing payslips and tax documents
- Accessing learning content (offline capability)
- Conducting performance check-ins
- Receiving push notifications for pending approvals

**Time-specific mobile capture (HIST-006 para 341):** "Employees can record their working hours through various methods (web clock, time cards, physical clocks)"

**Hollywood Bets biometric integration (HIST-007 para 64):** "The Biometric System" is a confirmed in-scope interface in the Hollywood Bets BOM — biometric time capture device integrated to Oracle Fusion HCM via OIC.

**Governance note for biometric integration:** Biometric integration is a custom integration deliverable (HCM → OIC → biometric device). The Oracle platform does not natively provide biometric hardware — the integration connects a third-party biometric system to Oracle HCM for time capture. Framing must reflect this.

---

### 3.6 Workforce Health and Safety

**Evidence status: ZERO EVIDENCE — GAP CONFIRMED (OI-W7-003 BLOCKING)**

**Finding:** Zero mentions of Workforce Health and Safety (OHS, OHSA, occupational health, safety incidents, hazard management, near-miss reporting, or injury-on-duty) in any of the following documents reviewed:
- HIST-007 Hollywood Bets V5.0 BOM
- HIST-016 SABS ETS client reference tables
- HIST-006 SAA HCM RFP
- HIST-008 RedPath Mining RFI
- HIST-015 Afrocentric HCM V4.0
- HIST-014 CCBA HCM V2.0
- Redpath Mining RACI

**Oracle platform note:** Oracle Fusion HCM does have an Oracle Workforce Health and Safety capability area that supports:
- Incident reporting and tracking
- Safety inspection management
- Near-miss logging
- Injury and illness case management
- Corrective action workflows
- Safety analytics

However, this capability is either:
a) Not typically included in APPSolve's standard HCM implementation scope (no BOM evidence), or
b) Not in scope for the client engagements reviewed

**The scope question for W3S1-007:** The BU Lead's instruction specifically included "Workforce Health and Safety" as a focus area. Zero evidence exists to support any implementation claim. BU Lead must decide:
- **Option A — Exclude:** Remove H&S from W3S1-007 scope entirely. Note scope boundary in document.
- **Option B — Include as Platform Capability:** Include a platform capability section — "Oracle Fusion HCM provides Workforce Health and Safety capabilities... APPSolve can configure and implement where required and in scope." No implementation evidence available.
- **Option C — Separate statement:** H&S is a distinct enough domain to warrant its own statement (W3S1-008 could be revised to include it, or a new statement created).

**This is BLOCKING** because including H&S without any implementation evidence creates a false capability impression for a topic specifically called out in the client's focus areas.

---

## Section 4: Per-Source Analytics

| Source | Absence Mgmt paras | T&L paras | Workforce Scheduling | Mobile | Manager SS | H&S |
|---|---|---|---|---|---|---|
| HIST-007 HB V5.0 | Phase 3.3.1 confirmed; para 147 | Absent from BOM | Absent from BOM | — | — | Zero |
| HIST-016 SABS ETS | Implicit in HCM scope | Table 3 — Mr Price T&L rollout | Not mentioned | — | — | Zero |
| HIST-006 SAA RFP | Paras 334–344 platform | Paras 216–232 platform | Paras 233–247 platform | Paras 538–550 | Paras 520–535 | Zero |
| HIST-008 Redpath RFI | Not detailed in RFI | Not in scope | Not in scope | — | — | Zero |
| HIST-015 Afrocentric | Para 193 Phase 3.3.1 | Paras 202–203, 296–299 | Not mentioned | — | — | Zero |
| HIST-014 CCBA | Para 287 Core + Absence | Not included | Not included | Mobile (general) | — | Zero |
| HIST-017 SAA Addl Info | Para 117 (SLA reference) | — | — | — | — | Zero |

---

## Section 5: Implementation Evidence — Per Client Workforce Management Classification

| Client | Absence Mgmt | Time & Labor | Scheduling | Biometric | Reference status |
|---|---|---|---|---|---|
| **Hollywood Bets** | Confirmed — Phase 3.3.1 | **ABSENT from BOM** | Absent from BOM | Biometric interface confirmed (para 64) | Tier 1 — referenceable |
| **Mr Price** | Standard HCM scope | **"Rollout" stated — governance question OI-W7-001** | Not confirmed | Not mentioned | Governance question (C-W3-002) |
| **Redpath Mining** | Confirmed — RACI para 9 | **Absent from RACI scope** | Not confirmed | Not mentioned | Active pipeline — not live; not referenceable (Rule 21.5) |
| **DFA** | Likely (in "HCM" scope) | Not confirmed | Not confirmed | Not mentioned | NOT referenceable — never name (Rule 21.4) |
| **Afrocentric** | Phase 3.3.1 | Option 1 proposed | Not mentioned | Not mentioned | Delivery methodology source — not referenceable as client |
| **KPMG** | Not specified in HCM scope | Not specified | Not confirmed | Not mentioned | Taleo only in HCM — not applicable |
| **Investec** | HCM scope (HCM + Payroll) | Not confirmed | Not confirmed | Not mentioned | Finance primary — HCM secondary reference |

---

## Section 6: Product Boundary Table

| Capability | Module | Licensing | APPSolve confirmed delivery | Notes |
|---|---|---|---|---|
| Leave type definition and accruals | Oracle Absence Management | Included in Oracle HCM | **CONFIRMED** | Standard Phase 1 in all HCM implementations |
| Employee leave request self-service | Oracle Absence Management | Included | **CONFIRMED** | Standard |
| Manager absence approval | Oracle Absence Management | Included | **CONFIRMED** | Standard |
| Legislative absence types (SA) | Oracle Absence Management | Included | **CONFIRMED** | BCEA, FMLA-equivalent, sick leave |
| Payroll integration (absence) | Oracle Absence Management + HCM Extracts/OIC | Included | **CONFIRMED** | Standard in every implementation |
| Time entry (web clock, timecard) | Oracle Time and Labor | Included in Oracle HCM | Confirmed if OI-W7-001 Option A; Platform if Option B | OI-W7-001 pending |
| Overtime management and rules | Oracle Time and Labor | Included | OI-W7-001 dependent | |
| Timecard approval workflows | Oracle Time and Labor | Included | OI-W7-001 dependent | |
| Labor compliance rules engine | Oracle Time and Labor | Included | OI-W7-001 dependent | |
| Project costing integration | Oracle Time and Labor | Included | OI-W7-001 dependent | Relevant where PPM in scope |
| Employee shift schedules | Oracle Workforce Scheduling | **Licensing TBD — OI-W7-002** | Platform Capability | No implementation evidence |
| Schedule optimization vs demand | Oracle Workforce Scheduling | TBD | Platform Capability | No implementation evidence |
| Self-service shift preferences | Oracle Workforce Scheduling | TBD | Platform Capability | No implementation evidence |
| Labor law/union compliance in scheduling | Oracle Workforce Scheduling | TBD | Platform Capability | No implementation evidence |
| Manager dashboard (leave, time, team) | Oracle HCM Manager Self-Service | Included | CONFIRMED (standard) | Core to every HCM implementation |
| Mobile app (leave, approvals) | Oracle HCM Mobile | Included | CONFIRMED (standard) | iOS and Android |
| Mobile time entry | Oracle HCM Mobile + T&L | Included | OI-W7-001 dependent | Requires T&L in scope |
| Biometric system integration | OIC custom integration | Custom delivery | CONFIRMED — Hollywood Bets | Custom OIC interface; not Oracle standard |
| Occupational H&S incident reporting | Oracle Workforce H&S | TBD licensing | **NO EVIDENCE — OI-W7-003** | Zero corpus evidence |
| Safety inspection management | Oracle Workforce H&S | TBD | **NO EVIDENCE** | Zero corpus evidence |

---

## Section 7: Cross-Document Consistency Checks

| Reference | W3S1-001 (HCM Core) | W3S1-007 (Workforce Mgmt — proposed) | Status |
|---|---|---|---|
| Absence Management | Phase 3.3.1 described briefly (part of Core phase); not a standalone section | Would become a full standalone section | Potential overlap — OI-W7-004 advisory |
| Manager Self-Service | Included as standard HCM feature | Relevant in Workforce Management context | Consistent — no conflict |
| Mobile capabilities | Not a specific section in W3S1-001 | Should be addressed in W3S1-007 | Cross-reference required |
| Time and Labor | Not addressed in W3S1-001 | Natural home in W3S1-007 | Clean delineation |

---

## Section 8: Governance Risks

| Risk ID | Risk | Likelihood | Impact | Recommendation |
|---|---|---|---|---|
| GR-W7-001 | **Mr Price T&L classification conflict** — HIST-016 "rollout" language conflicts with C-W3-002 "support only" rule for Mr Price broader HCM | HIGH | HIGH | BU Lead decision required (OI-W7-001) |
| GR-W7-002 | **Workforce Scheduling separately licensed** — if separately licensed, failing to disclose creates commercial risk (same as OAX) | MEDIUM | HIGH | BU Lead guidance (OI-W7-002) |
| GR-W7-003 | **Health and Safety inclusion without evidence** — including H&S as a capability claim with zero corpus evidence creates a false impression | HIGH | HIGH | BU Lead decision required (OI-W7-003) |
| GR-W7-004 | **Absence Management scope overlap with W3S1-001** — Phase 3.3.1 described in W3S1-001 already; repeating full detail in W3S1-007 creates inconsistency | LOW | LOW | Advisory — OI-W7-004; W3S1-007 can cross-reference W3S1-001 for Core HR context |
| GR-W7-005 | **Biometric integration over-claimed** — biometric is a custom OIC integration, not an Oracle standard feature. Framing as a standard capability would be inaccurate | MEDIUM | MEDIUM | Frame as custom integration deliverable; not Oracle product standard |
| GR-W7-006 | **Redpath Mining T&L** — Redpath scope excludes T&L; do not imply T&L is in all APPSolve HCM implementations | LOW | MEDIUM | T&L must be framed as "where in scope" not "always included" |

---

## Section 9: Proposed Document Structure for W3S1-007

The proposed 15-section structure, informed by BU Lead decisions still required:

| Section | Content | Governance dependency |
|---|---|---|
| 1 | Statement of Capability | None |
| 2 | Oracle Workforce Management Architecture — module hierarchy and scope | None |
| 3 | Absence Management — full standalone section | None — confirmed |
| 3.1 | Absence Management capability | None |
| 3.2 | Absence types and SA legislative requirements | None |
| 3.3 | Absence in APPSolve implementations | None |
| 4 | Oracle Time and Labor | OI-W7-001 — framing depends on outcome |
| 4.1 | T&L platform overview | None |
| 4.2 | T&L capabilities | None |
| 4.3 | T&L in APPSolve implementations (confirmed or platform) | OI-W7-001 |
| 5 | Workforce Scheduling | OI-W7-002 (licensing framing) |
| 6 | Manager Self-Service and Workforce Visibility | None |
| 7 | Mobile Workforce Capabilities | None |
| 8 | Time Capture and Biometric Integration | None (framing established) |
| 9 | Workforce Health and Safety | OI-W7-003 — include/exclude/platform only |
| 10 | APPSolve Delivery Capability | OI-W7-001 (T&L delivery claim) |
| 11 | Implementation References | OI-W7-001 |
| 12 | Integration Architecture | None |
| 13 | Implementation Approach | None |
| 14 | Risk Register | None |
| 15 | Assumptions Register | None |
| 17 | Approval Record | None |
| Appendix A | Source Mapping | None |
| Appendix B | Governance Self-Review | None |
| Appendix C | Extraction Return Report | None |

---

## Section 10: Open Items Register

### OI-W7-001 — Mr Price Time and Labor Classification (CLOSED 2026-06-13)

| Field | Detail |
|---|---|
| **Status** | CLOSED — BU Lead decision 2026-06-13 |
| **Decision** | Mr Price T&L = proof-of-concept (PoC) implementation. APPSolve implemented Oracle Time and Labor as a PoC for Mr Price. The client did not proceed to production rollout. Classify as implementation evidence — not production deployment. |
| **Approved framing** | "APPSolve implemented Oracle Time and Labor capabilities as part of a proof-of-concept programme for a South African retail client." |
| **Prohibited framing** | "rollout", "go-live", "production deployment", "live implementation", "stores across South Africa" |
| **Effect on extraction** | T&L framed as confirmed implementation evidence with PoC qualifier. Mr Price not named. No production deployment claim. Retail sector confirmed (proof of concept). C-W3-002 stands — Mr Price broader HCM = support only; T&L = PoC implementation evidence. |

---

### OI-W7-002 — Workforce Scheduling Licensing Classification (CLOSED 2026-06-13)

| Field | Detail |
|---|---|
| **Status** | CLOSED — BU Lead decision 2026-06-13 |
| **Decision** | Workforce Scheduling = Platform Capability Only. No implementation evidence. No named client references. Framing: Oracle platform capability that APPSolve can configure and implement where required and in scope. |
| **Effect on extraction** | Section 5 — platform capability framing. No licensing disclosure required beyond standard platform capability positioning. |

---

### OI-W7-003 — Workforce Health and Safety — Include or Exclude (CLOSED 2026-06-13)

| Field | Detail |
|---|---|
| **Status** | CLOSED — BU Lead decision 2026-06-13 |
| **Decision** | Include as Platform Capability. No implementation evidence. No client references. Position as Oracle platform capability that APPSolve can support and configure where required and in scope. |
| **Effect on extraction** | Section 6 — platform capability framing. No implementation claims. No client references. |

---

### OI-W7-004 — Absence Management Scope Boundary with W3S1-001 (CLOSED 2026-06-13)

| Field | Detail |
|---|---|
| **Status** | CLOSED — BU Lead decision 2026-06-13 |
| **Issue** | W3S1-001 (Oracle HCM Core — in Review_Required) describes Phase 3.3.1 "Human Capital (Core and Absence and Self Service)" — Absence Management is referenced as part of Core HCM delivery. W3S1-007 would contain a full Absence Management section. There is potential overlap. |
| **Decision required** | Should W3S1-007 include a full standalone Absence Management section, or should it cross-reference W3S1-001 for the Absence section and focus W3S1-007 on T&L + Scheduling? |
| **Recommendation** | Full standalone Absence Management section in W3S1-007. Rationale: (1) Absence Management is distinct enough from Core HCM to warrant full treatment; (2) W3S1-001 describes the phase structure, not the module in depth; (3) Absence is a core component of Workforce Management; (4) Tenders will often ask for Absence specifically — a dedicated section is more useful. Cross-reference W3S1-001 for Core HR context. |
| **Impact on extraction** | ADVISORY — minimal impact; clarifies structure only |

---

### OI-W7-005 — Document Title (CLOSED 2026-06-13)

| Field | Detail |
|---|---|
| **Status** | CLOSED — BU Lead decision 2026-06-13 |
| **Issue** | The placeholder title is "Oracle Workforce Management" but the content profile is: Absence Management + Time and Labor + Workforce Scheduling + Mobile + Manager Self-Service. |
| **Options** | (A) "Oracle Workforce Management" — umbrella title; (B) "Oracle HCM Time, Absence and Workforce Management" — more explicit; (C) "Oracle Absence Management, Time and Labor & Workforce Scheduling" — most precise |
| **Recommendation** | Option A: "Oracle Workforce Management" — clear, concise, covers the full scope, consistent with Oracle's own module grouping |
| **Impact on extraction** | ADVISORY — no structural impact |

---

## Section 11: Extraction Readiness Assessment

| Dimension | Status | Notes |
|---|---|---|
| Absence Management evidence | READY | Multiple Tier 1 sources; no conflicts |
| T&L evidence | BLOCKED | OI-W7-001 — classification conflict |
| Workforce Scheduling evidence | READY (platform capability framing) | OI-W7-002 is advisory only |
| Mobile and self-service evidence | READY | Standard platform capability |
| Health and Safety evidence | BLOCKED | OI-W7-003 — include/exclude decision |
| Governance rules applied | CONFIRMED | Rules 21.1–21.5 reviewed and applied in this SVR |
| ORACLE_FACT_BASELINE reviewed | CONFIRMED | No conflicts with current baseline |
| Prohibited wording check | CLEAN | No violations found in evidence analysis |

**Overall extraction readiness: AUTHORISED 2026-06-13 — All 5 OI items CLOSED — Candidate Draft generation approved.**

---

## Section 12: Standing Governance Confirmations

| Rule | Confirmation |
|---|---|
| **21.1 Aviation PROHIBITED** | Not applicable to Workforce Management content. SAA used as platform capability source only. SAA not named. |
| **21.2 Implementation vs Support** | Hollywood Bets Absence confirmed implementation. Mr Price T&L classification pending (OI-W7-001). |
| **21.3 Opportunity Marketplace** | Not applicable to this statement. |
| **21.4 DFA — never named** | DFA not named. DFA implementation scope does not include confirmed T&L or Scheduling evidence. |
| **21.5 Redpath Mining — active, not live, not referenceable** | Redpath Absence confirmed active scope. T&L confirmed absent from Redpath scope. Redpath not named in any output. |
| **CCBA — never named** | CCBA reviewed for research only. Not named. No CCBA content extracted. |
| **SAA — source only, not named** | SAA used for platform capability narrative only. Not named as client. |
| **Sectors — Retail/Mining/Professional Services** | Confirmed: Retail (Mr Price); Mining (Redpath, Hollywood Bets context); Professional Services (Afrocentric). |

---

## Appendix: Source Paragraph Index

| Module | Source | Paras / location |
|---|---|---|
| Absence Management — platform narrative | HIST-006 SAA RFP | Paras 334–344 |
| Absence Management — Phase 3.3.1 | HIST-007 HB V5.0 | Para 147 |
| Absence Management — Phase 3.3.1 | HIST-015 Afrocentric | Para 193 |
| Absence Management — RACI confirmed | Redpath RACI | Para 9 |
| Absence Management — assumptions | HIST-006 SAA RFP | Paras 788, 795 |
| Time and Labor — platform overview | HIST-006 SAA RFP | Paras 216–232 |
| Time and Labor — Mr Price rollout claim | HIST-016 SABS ETS | Table 3 (Mr Price row) |
| Time and Labor — Option 1 delivery | HIST-015 Afrocentric | Para 202–203 |
| Time and Labor — delivery assumptions | HIST-015 Afrocentric | Paras 296–299 |
| Workforce Scheduling — platform narrative | HIST-006 SAA RFP | Paras 233–247 |
| Manager Self-Service | HIST-006 SAA RFP | Paras 520–535 |
| Mobile capabilities | HIST-006 SAA RFP | Paras 538–550 |
| Mobile time capture methods | HIST-006 SAA RFP | Para 341 |
| Biometric integration | HIST-007 HB V5.0 | Para 64 |
| Attendance and Leave summary | HIST-006 SAA RFP | Paras 332–344 |
| Health and Safety | ALL SOURCES | Zero — confirmed gap |
