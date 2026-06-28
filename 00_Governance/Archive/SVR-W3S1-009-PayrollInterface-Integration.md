---
document_id: SVR-W3S1-009-PayrollInterface-Integration
title: "Source Validation Report — W3S1-009 Oracle HCM Payroll Interface & Integration"
version: "1.1"
status: "AUTHORISED — All 5 OI items CLOSED 2026-06-13 — BU Lead decisions applied"
extraction_status: "AUTHORISED — Proceed to Candidate Draft generation"
wave: "3"
deliverable: "W3S1-009"
created: "2026-06-13"
created_by: "Claude (AI — Wave 3 SVR)"
reviewed_by: "Pending BU Lead"
---

> **STATUS: AUTHORISED — All 5 OI items CLOSED 2026-06-13 — BU Lead decisions applied — Proceed to Candidate Draft generation**

---

# SVR — W3S1-009 Oracle HCM Payroll Interface & Integration

**Wave 3 | APPSolve Oracle Business Unit**
*Source Validation Report v1.0 | Created 2026-06-13*

---

## Section 1: Overview

This SVR covers capability statement W3S1-009 Oracle HCM Payroll Interface & Integration. The statement profiles APPSolve's capability to design, implement, and deliver Oracle Fusion HCM payroll integration using Oracle Integration Cloud (OIC) as the standard integration layer.

**Capability areas in scope:**
- Oracle Fusion HCM to third-party payroll integration (OIC architecture)
- Third-party payroll to Oracle Fusion HCM integration (bidirectional)
- PaySpace as primary confirmed third-party payroll target
- Integration architecture: OIC patterns, interface design, security, scheduling, monitoring
- HCM data elements: employee master, assignments, positions, organisations, cost centres, new hires, transfers, terminations, compensation changes
- Payroll return data: payroll results, payslip data, payroll balances, cost allocations, exception handling
- Integration governance: data ownership, reconciliation, audit, error management
- Payroll run reporting: validation runs, parallel testing, reconciliation reporting

**APPSolve positioning for this statement:**
APPSolve is positioned as an integration specialist and OIC implementation partner — NOT as a payroll processing provider. PaySpace remains the payroll system of record. APPSolve designs, implements, and configures the OIC-based integration between Oracle Fusion HCM and the third-party payroll platform.

---

## Section 2: Source Evidence Classification

| Source ID | Document | Classification | Payroll Integration Content | Governance |
|---|---|---|---|---|
| **HIST-007** | Hollywood Bets V5.0 Accepted Proposal (April 2023) | **Tier 1 — Implementation evidence** | "APPSolve has proposed an Oracle Applications solution which can integrate with the third-party Payroll solution." "Senior Technical Resource Responsible for the integration between 3rd party Payroll." Payroll Integration line item: R825,170.00. | Referenceable. See ORACLE_FACT_BASELINE Section 19. |
| **ANN1-V4.1** | Annexure 1_Oracle HCM Implementation V4.1.docx (contractual) | **Tier 1 — Contractual (highest authority)** | Explicit scope: "Integration to 3rd party payroll — Integration to be done Utilising Oracle Integration Cloud Service." Billing schedule heading: "Integration between Oracle Fusion HCM and PaySpace." Bidirectional: HCM to Payroll (Month 1-2) + Payroll to HCM (Month 3-4). Production Build Complete (Month 5). Data Migration (Month 6). Total R825,170.10. | Direct contractual evidence — highest evidential weight. Note: project plan heading says "Hollywood Bets EBS Payroll Implementation" — billing schedule takes precedence for naming (PaySpace). |
| **HIST-006** | SAA HCM RFP Response (June 2025) | **Tier 2 — Platform Capability** | "Oracle Fusion Payroll Interface Third-Party Payroll Integration: Provides the tools and interfaces necessary to integrate Oracle HCM with third-party payroll systems for seamless payroll processing." | SAA not awarded. Platform capability only. SAA never named as client. |
| **HIST-015** | Afrocentric HCM Proposal V4.0 (2023) | **Tier 3 — Methodology / Corroborative** | "The only integrations in scope would be for a time logging/access control solution and a Payroll solution." "It becomes a standardised feeder of data to payroll and other downstream systems and users of HCM data." | Delivery methodology evidence. Afrocentric never named. |
| **DFA Monthly Reports** | DFA Monthly Reports (2022–2023, internal) | **Tier 3 — Internal operational (NEVER NAMED)** | Oracle EBS Payroll operational support: post-run queries, dummy payslips, leave liability reconciliation, legislative patching (HRMS patchset + payroll legislative patches). OCI payroll infrastructure POC. "Payroll checking and interfaces." | Rule 21.4 — DFA never named. Evidence = Oracle EBS Payroll (NATIVE payroll), not OIC third-party integration. Corroborates payroll operational depth ONLY. |
| **ORACLE_FACT_BASELINE** | Section 19 (Hollywood Bets) | **Authoritative governance reference** | HB confirmed go-live July 2025 — payroll integration in Annexure 1 scope. | Sections 7, 19, 21. |

**Source NOT used:**
- SADV Oracle Payroll/HCM Fusion proposal (Dec 2018) — stored in DFA folder; SADV = South African Digital Villages; governance uncertainty (possible DFA affiliate). Not used — cannot confirm award or client independence from DFA.
- HB "Payroll and HCM Shopping List_.docx" — pre-RFP requirements document (HB's shopping list before selecting Oracle/PaySpace). Not implementation evidence.
- HIST-016 SABS ETS — no payroll integration content confirmed.
- Redpath Mining RFI — no payroll integration in active scope.

---

## Section 3: Evidence Analysis — Scope Areas

### 3.1 Integration Scope and OIC Architecture

**Annexure 1 V4.1 (primary):**

Scope extract verbatim:
> "Integration to 3rd party payroll Integration to be done Utilising Oracle Integration Cloud Service"

Interface list explicitly includes:
> "Fusion HCM to Third Party Payroll"

OIC is explicitly mandated as the integration technology. This confirms OIC as the standard APPSolve integration layer for HCM-to-payroll integrations.

**HB V5.0 (corroborative):**
> "Senior Technical Resource Responsible for the integration between 3rd party Payroll."

A dedicated Senior Integration Technical Resource was scoped and billed at R1,021.25/hour — confirming OIC integration as a distinct technical deliverable.

**SAA platform description (Tier 2):**
> "Oracle Fusion Payroll Interface Third-Party Payroll Integration: Provides the tools and interfaces necessary to integrate Oracle HCM with third-party payroll systems for seamless payroll processing."

### 3.2 Bidirectional Integration Evidence

**Billing schedule from Annexure 1 V4.1 — heading: "Integration between Oracle Fusion HCM and PaySpace":**

| Month | Deliverable | Amount |
|---|---|---|
| Deposit | 15 Days from Signature | R123,775.50 |
| Month 1 | **Payroll Integration Design Completed: HCM to Payroll** | R116,899.10 |
| Month 2 | **Internal Testing of Integration Completed: HCM to Payroll** | R116,899.10 |
| Month 3 | **Payroll Integration Design Completed: Payroll to HCM** | R116,899.10 |
| Month 4 | **UAT and Training Delivered: Payroll to HCM** | R116,899.10 |
| Month 5 | **1. Successful Parallel Payroll Test 2. Production Build Complete** | R116,899.10 |
| Month 6 | **Data Migrated** | R116,899.10 |
| **Total** | | **R825,170.10** |

**Evidence conclusion:** Bidirectional integration (HCM→PaySpace AND PaySpace→HCM) was contractually scoped as separate deliverables with separate design, testing, and UAT phases. Production Build is explicitly included in Month 5 deliverable.

### 3.3 Payroll Integration Project Plan (Annexure 1)

The Annexure 1 document contains a detailed project plan titled "Hollywood Bets EBS Payroll Implementation" (see governance risk GR-W9-002 regarding this heading). The plan covers:

**Discovery Phase:**
- Pay Journey Discovery (10 days)
- Evaluate existing pay components
- Point of Clarification Questionnaire
- Workshop Agenda and Preparation

**Design Phase:**
- HCM Core design
- Payroll Core design
- Elements and Balances design
- Detailed Requirements Documents
- Requirements & Recommendation Playback + Sign-off

**Build Phase (Solution Reflection 1 + 2):**
- Build - HCM Core
- Build - Payroll Core
- Build - Elements and Balances
- Build - Security & Responsibility Definitions
- Sample Data Load

**Technical Build:**
- Development - Custom Functions (3 days)
- Development - Custom Payslip and reports (7 days)
- Complete Technical Documents

**Validation:**
- Training & Validation Run (10 days)
- Compile Training Documents
- Compile Validation Run Scripts
- Deliver Training
- Deliver Validation Run
- Resolve Issues
- Sign-Off Validation Run Results + Sign-Off Training

**Parallel Runs:**
- Consecutive (Production Like) Runs (24 days)
- Prepare Instance
- Data Migration
- Run - Consecutive Month 1
- Run - Consecutive Month 2
- Run Report
- Sign-Off Run Results

**Production Build (December 2023):**
- Prod Build (7 days)
- Data Migration
- Go / No-Go decision
- **Go-Live (milestone)**
- Final Configuration Documents

**Data Management:**
- Data Preparation (Pay Element Entries and Balance Take On)
- Data Load Trial 1 + 2
- Production Data Prep & Load
- Sign-Off Production Data

**Total planned duration:** 115 days (original plan Aug 2023 – Jan 2024)

### 3.4 PaySpace as Integration Target

Confirmed from billing schedule heading: "Integration between Oracle Fusion HCM and PaySpace"

PaySpace is the third-party payroll platform receiving HCM data and returning payroll results. APPSolve implements the OIC interface layer between Oracle Fusion HCM and PaySpace. PaySpace is the payroll system of record — APPSolve does not deliver payroll processing.

### 3.5 DFA Oracle EBS Payroll Evidence (Corroborative Only — DFA Never Named)

DFA Monthly Reports (2022–2023) confirm ongoing Oracle EBS Payroll operational support:

| Evidence item | Source | Relevance |
|---|---|---|
| Post-run queries, leave liability reconciliation, dummy payslips | Monthly Reports 2022–2023 | Payroll operational depth |
| "Payroll checking and interfaces" | May 2023 report | Oracle Payroll interface operations |
| HRMS patchset + payroll legislative patches — Test and Prod | May 2023 / Feb 2023 reports | Legislative compliance capability |
| OCI payroll infrastructure POC | May 2023 DBA section | Oracle Payroll on OCI migration capability |
| "November payroll tasks" — "Nov pay run checking" | Nov 2022 report | Payroll run support |
| Oracle Payroll license — 700 users perpetual (DFA Draft OD Payroll 2021 accepted) | License folder | Oracle Payroll licensed 700 users |

**Critical governance note:** DFA evidence is for Oracle EBS Payroll (native Oracle payroll product). This is categorically different from OIC-based integration to PaySpace. DFA evidence corroborates APPSolve's Oracle payroll depth (operations, legislative patching, run support) but does NOT corroborate OIC third-party integration architecture.

---

## Section 4: Per-Source Analytics

| Source | Chars | Payroll Integration Content | Integration Architecture | PaySpace specific | Production evidence | Legislative compliance |
|---|---|---|---|---|---|---|
| ANN1-V4.1 (CONTRACTUAL) | 23,400 | ★★★★★ | OIC mandated | ★★★★★ (billing heading) | ★★★★ (Production Build milestone) | Basic assumptions only |
| HIST-007 HB V5.0 | ~180k | ★★★★ | Senior tech resource | ★★★ (line item) | ★★★ (same cost) | ★★ |
| HIST-006 SAA RFP | large | ★★ (platform) | Platform description | None | None | None |
| HIST-015 Afrocentric | large | ★★ (methodology) | ★★ (feeder concept) | None | None | ★★ |
| DFA Monthly Reports | 15k each | ★★★ (EBS native) | ★★ (interfaces) | None | ★★★ (operational) | ★★★★ (patching) |

---

## Section 5: Implementation Evidence Matrix

| Client | Evidence type | Payroll Integration scope | Production | Reference status |
|---|---|---|---|---|
| **Hollywood Bets** | Contractual — Annexure 1 V4.1 signed | OIC integration: HCM to PaySpace (bidirectional). Production Build milestone included. Total R825,170. | **PENDING CONFIRMATION** (see OI-W9-001) | Tier 1 candidate — subject to OI-W9-001 |
| DFA | Internal operational — Monthly Reports | Oracle EBS Payroll native — post-run support, legislative patching, pay run management | Active operational | Rule 21.4 — NEVER NAMED; EBS native only; not OIC integration |
| Afrocentric | Methodology proposal | Payroll integration noted as planned scope | Not awarded (methodology only) | Not referenceable |
| SAA | Capability narrative | Platform description only | Not awarded | Not named; platform only |

---

## Section 6: Product Boundary Table

| Product / Concept | What it is | APPSolve positioning | Governance rule |
|---|---|---|---|
| **Oracle Integration Cloud (OIC)** | Oracle's cloud integration platform — the APPSolve standard for all Fusion HCM integration | APPSolve implements OIC as the integration layer between Oracle Fusion HCM and third-party systems | Standard in all Oracle Fusion HCM implementations |
| **Oracle Fusion HCM (B85800)** | Oracle's cloud HCM platform — the source of truth for employee and workforce data | APPSolve implements Oracle Fusion HCM — HCM is the sending system for employee data to payroll | Core product |
| **PaySpace** | Third-party payroll platform — APPSolve's confirmed integration target at Hollywood Bets | Payroll system of record. APPSolve integrates TO PaySpace via OIC. APPSolve does NOT implement or support PaySpace internally. | PaySpace remains payroll system of record |
| **Oracle Fusion Payroll (B85804)** | Oracle's NATIVE cloud payroll product — part of the Oracle HCM suite | APPSolve does NOT claim to implement Oracle Fusion Payroll natively in W3S1-009. This statement is about INTEGRATION to third-party payroll, not native Oracle Payroll configuration. | CRITICAL: Do not conflate Oracle Fusion Payroll (native) with Oracle Fusion HCM payroll integration (OIC to third party) |
| **Oracle EBS Payroll** | Oracle's legacy on-premise payroll product (runs on Oracle Database, not cloud) | APPSolve supports and maintains Oracle EBS Payroll (confirmed for internal unnamed client — DFA). This is separate from Oracle Fusion HCM third-party integration. | DFA EBS Payroll = operational support only; never named; different product |
| **PaySpace Payroll integration via Acumatica** | Acumatica-to-PaySpace integration (Cape Union Mart, City Lodge Hotels, CATS) | NOT applicable to Oracle Fusion HCM statements. Acumatica PaySpace evidence is Acumatica-only — must not cross to Oracle. | Standing governance rule — W3S1-009 and HANDOVER.md |
| **HCM-to-Payroll (outbound)** | Oracle Fusion HCM sends employee data, assignments, compensation changes, new hires, transfers, terminations to PaySpace | Primary integration direction — confirmed contracted deliverable (Month 1-2 in billing schedule) | Bidirectional confirmed |
| **Payroll-to-HCM (inbound)** | PaySpace returns payroll results, balances, payslip data, cost allocations to Oracle Fusion HCM | Secondary integration direction — confirmed contracted deliverable (Month 3-4 in billing schedule) | Bidirectional confirmed |
| **APPSolve as payroll processor** | APPSolve does NOT process payroll, calculate payroll, or manage pay runs | APPSolve's role = integration architecture, OIC configuration, interface design, data mapping, go-live support | Standing governance rule |

---

## Section 7: Governance Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| **GR-W9-001** | **BLOCKING — Payroll integration go-live status unconfirmed.** The Annexure 1 plan shows Dec 2023 as planned payroll integration go-live. Main HCM go-live was July 2025 — suggesting programme delays. Was payroll integration also delayed? Was it completed to production? If not yet in production, the payroll integration cannot be presented as confirmed delivery. | HIGH | HIGH | OI-W9-001 must be resolved before extraction. BU Lead to confirm production status. |
| **GR-W9-002** | **"EBS Payroll Implementation" project plan heading.** The project plan in Annexure 1 is titled "Hollywood Bets EBS Payroll Implementation" — but the billing schedule heading says "Integration between Oracle Fusion HCM and PaySpace." These are inconsistent. The billing schedule (commercial document) is the authoritative governance reference. The extraction must use "PaySpace" framing from the billing schedule and must NOT use "EBS Payroll" framing — that heading could imply Oracle EBS Payroll was implemented, which is not what the billing schedule confirms. | MEDIUM | HIGH | Use billing schedule heading as authoritative: "Integration between Oracle Fusion HCM and PaySpace." Never refer to this as "EBS Payroll" implementation. Raise with BU Lead via OI-W9-002. |
| **GR-W9-003** | **APPSolve payroll processing conflation.** Content could imply APPSolve delivers payroll processing if not carefully framed. | MEDIUM | HIGH | Frame consistently: "APPSolve designs, implements and supports Oracle Fusion HCM integrations with third-party payroll platforms." PaySpace calculates and processes payroll. APPSolve delivers the OIC interface layer. |
| **GR-W9-004** | **DFA payroll evidence misapplication.** DFA operational evidence (EBS Payroll support, legislative patching) could be used to support OIC integration claims — which it does not support. DFA has native Oracle EBS Payroll, not OIC third-party integration. | MEDIUM | HIGH | DFA evidence = operational depth only (corroborates APPSolve's payroll knowledge and legislative capability). Does NOT support OIC third-party integration claims. Never name DFA. |
| **GR-W9-005** | **Oracle Fusion Payroll vs third-party integration conflation.** Oracle offers native Oracle Fusion Payroll (cloud payroll — separate license). W3S1-009 is about OIC integration to third-party payroll, not native Oracle Fusion Payroll configuration. | MEDIUM | HIGH | Section 2 product boundary must explicitly distinguish. Never claim native Oracle Fusion Payroll implementation in this document unless separately evidenced and BU Lead approved. |
| **GR-W9-006** | **Acumatica PaySpace evidence bleed.** APPSolve has Acumatica-to-PaySpace integration evidence (Cape Union Mart, City Lodge Hotels, CATS). This is Acumatica ERP context and must never enter Oracle Fusion HCM capability statements. | LOW | HIGH | Standing governance rule confirmed. No Acumatica PaySpace evidence to be used in W3S1-009. |
| **GR-W9-007** | **Rule 21.4 breach.** DFA is never named in any KB output. Monthly report content and EBS Payroll evidence cannot include client name or identifiers. | LOW | CRITICAL | Rule 21.4 absolute. All DFA content rephrased as "internal oracle application support engagement" or similar. Never named. |

---

## Section 8: Proposed Document Structure

| Section | Content area | Evidence base | Confidence |
|---|---|---|---|
| 1 | Statement of Capability — overview; framing; module-boundary table; APPSolve positioning | ANN1-V4.1; HIST-007 | HIGH |
| 2 | Product Architecture — OIC as integration layer; Oracle Fusion HCM as HCM system of record; PaySpace as payroll system of record; product boundary (native payroll vs integration) | ANN1-V4.1; HIST-006 platform | HIGH |
| 3 | HCM-to-Payroll Integration — outbound interface; employee data; assignments; positions; organisations; cost centres; compensation changes; new hires; transfers; terminations; payroll input values | ANN1-V4.1; HIST-006 platform | HIGH (billing confirmed); data elements advisory |
| 4 | Payroll-to-HCM Integration — inbound interface; payroll results; payslip data; balances; cost allocations; leave balances; status feedback; exception handling | ANN1-V4.1 (billing confirmed); HIST-006 platform | MEDIUM (billing confirmed; element detail advisory) |
| 5 | OIC Integration Architecture — OIC patterns; interface design; security model; scheduling; monitoring framework; error handling | ANN1-V4.1 (OIC mandated); HIST-006 platform | HIGH (OIC confirmed); pattern detail = platform |
| 6 | Integration Delivery Approach — Pay Journey Discovery; design methodology; parallel payroll testing; consecutive run validation; go-live criteria | ANN1-V4.1 (project plan detail) | HIGH |
| 7 | Payroll Data Governance — data ownership; master data management; reconciliation; error handling; audit trail; POPIA compliance | HIST-015 methodology; DFA operational (never named); platform capability | MEDIUM |
| 8 | Payroll Run Validation and Parallel Testing — validation run design; consecutive month runs; sign-off process; go-live criteria | ANN1-V4.1 (project plan detail) | HIGH |
| 9 | Payroll Integration Monitoring and Operational Support — OIC monitoring framework; interface error alerts; post-go-live monitoring | DFA operational (never named; EBS context); platform; OIC standard | MEDIUM |
| 10 | Integration Security and Compliance — POPIA data handling; interface security; access controls; audit controls | Platform capability; DFA operational (never named) | MEDIUM |
| 11 | Legislative Compliance Support — SA payroll legislative patching; annual tax cycle; budget speech changes; PAYE/UIF/SDL | DFA operational (never named); platform | MEDIUM |
| 12 | APPSolve Delivery Capability — practice description; confirmed integrations; integration technical team | ANN1-V4.1; HIST-007 | HIGH |
| 13 | Implementation References — HB PaySpace integration (subject to OI-W9-001); positioning | ANN1-V4.1; OI-W9-001 | PENDING OI-W9-001 |
| 14 | Risk and Assumptions Register | SVR governance risks | Standard |
| 17 | Approval Record | — | Standard |
| App A | Source Mapping Table | — | Standard |
| App B | Governance Self-Review | — | Standard |
| App C | Extraction Return Report | — | Standard |

---

## Section 9: Open Items Register

### OI-W9-001 — BLOCKING: Hollywood Bets Payroll Integration Production Go-Live Status

| Field | Value |
|---|---|
| **OI ID** | OI-W9-001 |
| **Severity** | BLOCKING |
| **Topic** | Hollywood Bets PaySpace integration — production status |
| **Issue** | The Annexure 1 V4.1 billing schedule includes "Production Build Complete" (Month 5) and "Data Migrated" (Month 6) milestones, with a planned go-live in December 2023. The main HCM programme went live in July 2025 — a significant delay from the original plan (original plan: May 2024). Was the payroll integration to PaySpace also delayed? Did it reach production? At what date? |
| **Why blocking** | If the payroll integration has NOT yet reached production, it cannot be described as "confirmed delivery" or "implemented." The billing schedule is contractual evidence of scope and planned delivery — not confirmed production evidence. This distinction is critical for governance. |
| **Evidence available** | ANN1-V4.1 billing schedule: "Production Build Complete" (Month 5); project plan: "Go-Live" milestone December 2023. ORACLE_FACT_BASELINE Section 19: HCM go-live July 2025 (delay from plan). |
| **Options** | **Option A:** Payroll integration went live with the HCM programme (July 2025 or earlier) — confirm date and reference as Tier 1 production implementation. **Option B:** Payroll integration was delivered on a separate timeline (e.g., Dec 2023 as planned) — confirm go-live date and status. **Option C:** Payroll integration was partially delivered (e.g., HCM to Payroll direction only) — confirm what reached production. **Option D:** Payroll integration has not yet reached production — present as "implementation in progress" with confirmed contractual scope, not as completed delivery. |
| **BU Lead decision required** | YES — confirm production status, go-live date, and approved framing |
| **Extraction blocked** | Yes — cannot begin draft until this is resolved |

---

### OI-W9-002 — ADVISORY: PaySpace Integration Scope and "EBS Payroll" Heading

| Field | Value |
|---|---|
| **OI ID** | OI-W9-002 |
| **Severity** | ADVISORY |
| **Topic** | Exact PaySpace integration scope; "EBS Payroll" naming anomaly |
| **Issue** | The Annexure 1 billing schedule explicitly says "Integration between Oracle Fusion HCM and PaySpace" — confirming PaySpace as the integration target. However, the project plan section in Annexure 1 is titled "Hollywood Bets EBS Payroll Implementation," suggesting an Oracle EBS Payroll workstream. The exact data elements exchanged (employee fields, payroll elements, data mapping) are not specified in the contractual documents. |
| **Specific questions** | (a) Was the "EBS Payroll Implementation" project plan a separate Oracle EBS Payroll workstream or an internal label for the PaySpace integration project? (b) What exact data does HCM send to PaySpace (employee fields, payroll elements, cost centres)? (c) What does PaySpace return to HCM (payroll results, payslip data, balances)? |
| **Options** | **Option A:** "EBS Payroll Implementation" = internal project naming for the PaySpace configuration workstream — use PaySpace framing throughout (billing schedule is definitive). **Option B:** There was a separate Oracle EBS Payroll workstream alongside the PaySpace integration — scope the EBS workstream separately if it is a distinct APPSolve deliverable. |
| **BU Lead decision required** | YES — clarify EBS heading and confirm data element scope |
| **Extraction blocked** | No — use billing schedule (PaySpace) framing; flag EBS heading as internal |

---

### OI-W9-003 — ADVISORY: Payroll Reconciliation Reporting Scope

| Field | Value |
|---|---|
| **OI ID** | OI-W9-003 |
| **Severity** | ADVISORY |
| **Topic** | Payroll reconciliation reporting |
| **Issue** | The Annexure 1 project plan includes "Validation Run Scripts," "Run Report," and "Consecutive Production-Like Runs" milestones. Custom Payslip development is included in the Technical Build. These suggest payroll reporting and reconciliation were in scope. Was formal payroll reconciliation reporting (as a distinct deliverable) part of the integration delivery? |
| **Options** | **Option A:** Reconciliation reporting = confirmed deliverable — include as a dedicated capability in the statement. **Option B:** Reconciliation = validation run outputs only (not a separately reportable capability) — frame as part of go-live validation. |
| **BU Lead decision required** | YES — confirm scope of reconciliation reporting |
| **Extraction blocked** | No |

---

### OI-W9-004 — ADVISORY: Bidirectional Integration — Design vs Production

| Field | Value |
|---|---|
| **OI ID** | OI-W9-004 |
| **Severity** | ADVISORY |
| **Topic** | Bidirectional implementation status |
| **Issue** | The billing schedule confirms both HCM-to-Payroll (Month 1-2) and Payroll-to-HCM (Month 3-4) as contracted deliverables with UAT. Month 5 production build covers both directions. However, dependent on OI-W9-001, was BOTH directions implemented to production, or was only one direction delivered? |
| **Note** | If OI-W9-001 confirms full production delivery, bidirectional is confirmed. If partial delivery, BU Lead must specify which direction(s) reached production. |
| **Options** | **Option A:** Both directions confirmed in production — present as bidirectional implementation. **Option B:** Only HCM-to-Payroll reached production — present outbound as confirmed; inbound as designed/in progress. |
| **BU Lead decision required** | YES — dependent on OI-W9-001 outcome |
| **Extraction blocked** | No — dependent on OI-W9-001 |

---

### OI-W9-005 — ADVISORY: Payroll Monitoring — Implementation vs Managed Service

| Field | Value |
|---|---|
| **OI ID** | OI-W9-005 |
| **Severity** | ADVISORY |
| **Topic** | Payroll integration monitoring — implementation deliverable or managed service capability |
| **Issue** | W3S1-009 is an implementation capability statement. Payroll monitoring has two distinct aspects: (a) OIC monitoring framework setup (interface error alerts, monitoring dashboards — set up during implementation as a go-live deliverable) and (b) day-to-day payroll run support, post-run queries, patching (managed service / operational support). The Annexure 1 includes "800 hours of support" post go-live, but this is support time rather than an implementation deliverable. |
| **Recommendation** | OIC monitoring framework configuration = implementation deliverable (confirm via BU Lead). Day-to-day payroll operations support = separate managed service reference (cross-reference W2S1-004 Oracle Managed Services, not this document). |
| **Options** | **Option A:** Include OIC monitoring framework setup as implementation deliverable only; explicitly exclude day-to-day run support. **Option B:** Include both implementation monitoring setup AND describe operational support model — note that operational support is a separate managed service engagement. |
| **BU Lead decision required** | YES — confirm positioning preference |
| **Extraction blocked** | No |

---

## Section 10: Extraction Readiness

| Item | Status |
|---|---|
| Primary source identified and extracted | ✅ — ANN1-V4.1 full content extracted |
| OIC architecture confirmed | ✅ — explicitly mandated in Annexure 1 |
| PaySpace as integration target confirmed | ✅ — billing schedule heading |
| Bidirectional integration scope confirmed | ✅ — billing schedule Months 1-4 |
| Production Build milestone confirmed | ✅ — billing schedule Month 5 |
| Production go-live status confirmed | ❌ — **BLOCKING: OI-W9-001** |
| "EBS Payroll" heading clarified | ❌ — OI-W9-002 (advisory) |
| Data element detail (HCM→Payroll fields) confirmed | ❌ — OI-W9-002 (advisory) |
| Reconciliation reporting scope confirmed | ❌ — OI-W9-003 (advisory) |
| Monitoring positioning confirmed | ❌ — OI-W9-005 (advisory) |
| Rule 21.4 (DFA) — confirmed never-name | ✅ |
| Acumatica PaySpace boundary — confirmed excluded | ✅ |
| APPSolve-as-payroll-processor prohibition | ✅ |
| Product boundary (Oracle Fusion Payroll vs integration) | ✅ — flagged as governance risk GR-W9-005 |

**Extraction status: NOT READY — resolve OI-W9-001 before proceeding.**
Advisory items (OI-W9-002 through OI-W9-005) should be resolved before extraction to maximise content accuracy, but are not blocking.

---

## Section 11: Standing Governance Confirmations

All Wave 3 standing rules from ORACLE_FACT_BASELINE Section 21 apply:

| Rule | Confirmation |
|---|---|
| 21.1 Aviation PROHIBITED | Confirmed — no aviation content; SAA not named |
| 21.2 Implementation vs support distinction | Confirmed — implementation framing throughout; DFA operational = support context only |
| 21.3 Opportunity Marketplace | N/A for this statement |
| 21.4 DFA never named | **ABSOLUTE** — DFA Monthly Report evidence rephrased generically; DFA never appears in output |
| 21.5 Redpath not referenceable | Confirmed — Redpath not in payroll integration scope |
| CCBA not named | Confirmed — CCBA not a source for this statement |
| SAA not named as client | Confirmed — SAA source = platform capability only |

**Additional standing rules for W3S1-009:**
- APPSolve does NOT deliver payroll processing — PaySpace is the payroll system of record
- "EBS Payroll" framing prohibited — use "PaySpace" framing from billing schedule
- Oracle Fusion Payroll (native) must not be conflated with Oracle HCM third-party payroll integration
- Acumatica PaySpace evidence (Cape Union Mart, City Lodge Hotels, CATS) must never enter this document

---

## Section 12: Source Paragraph Index

| Evidence item | Source | Section |
|---|---|---|
| "Integration to 3rd party payroll — Integration to be done Utilising Oracle Integration Cloud Service" | ANN1-V4.1 — Scope of Engagement | 3.1 |
| "Fusion HCM to Third Party Payroll" — interface in scope | ANN1-V4.1 — Interface list | 3.1 |
| Billing schedule: "Integration between Oracle Fusion HCM and PaySpace" — Months 1-6 | ANN1-V4.1 — Billing schedule | 3.2 |
| Project plan: Pay Journey Discovery, Elements and Balances, Technical Build, Validation Runs, Production Build, Go-Live | ANN1-V4.1 — Project plan | 3.3 |
| Total Payroll Integration: R825,170.00 | ANN1-V4.1 — Cost summary | 3.2 |
| "Senior Integration Technical Resource — Payroll Integration — R1,021.25/hour" | ANN1-V4.1 — Rate table | 3.1 |
| "APPSolve has proposed an Oracle Applications solution which can integrate with the third-party Payroll solution" | HIST-007 HB V5.0 — Executive Summary | 3.1 |
| "Senior Technical Resource Responsible for the integration between 3rd party Payroll" | HIST-007 HB V5.0 — Team Roles | 3.1 |
| "Oracle Fusion Payroll Interface Third-Party Payroll Integration" | HIST-006 SAA RFP — Platform section | 3.1 |
| "The only integrations in scope would be for a time logging/access control solution and a Payroll solution" | HIST-015 Afrocentric | 3.5 |
| DFA: "Post run queries...leave liability reconciliation...general pay run support" | DFA Monthly Report May 2023 | 3.5 |
| DFA: "Apply latest HRMS patchset and payroll legislative patches on Dev or Test" | DFA Monthly Report May 2023 DBA | 3.5 |
| DFA: "Payroll checking and interfaces" | DFA Monthly Report May 2023 | 3.5 |
| DFA: "EBS Payroll non-production migration to Oracle Cloud Infrastructure: POC being done to test using OCI as infrastructure running Oracle Payroll" | DFA Monthly Report Nov 2022 DBA | 3.5 |

---

## Section 13: Decisions Log

| OI ID | Decision | Date | By |
|---|---|---|---|
| OI-W9-001 | **CLOSED** — Oracle Fusion HCM to PaySpace integration fully implemented, completed, and operating in production. Classification: Implementation YES; Production deployment YES; Go-live YES; Referenceable YES. Treat as completed Tier 1 implementation evidence. | 2026-06-13 | Hein Blignaut |
| OI-W9-002 | **CLOSED** — "EBS Payroll Implementation" heading = payroll workstream naming / historical context only. Authoritative evidence: Oracle Fusion HCM ↔ OIC ↔ PaySpace. Statement focuses on: Oracle Fusion HCM integration; OIC architecture; PaySpace integration; payroll data exchange; payroll validation; payroll reconciliation; payroll monitoring. Do not position as Oracle EBS Payroll implementation. | 2026-06-13 | Hein Blignaut |
| OI-W9-003 | **CLOSED** — Payroll reconciliation forms part of the validation framework. Position as: payroll validation; payroll reconciliation controls; data verification; parallel payroll validation; production readiness validation. Do not create a separate reconciliation-reporting capability unless source evidence explicitly supports it. | 2026-06-13 | Hein Blignaut |
| OI-W9-004 | **CLOSED** — Both integration directions confirmed in production: Direction 1: Oracle Fusion HCM → PaySpace; Direction 2: PaySpace → Oracle Fusion HCM. May describe: bidirectional integration architecture; employee master-data synchronisation; payroll feedback integration; payroll result synchronisation; controlled payroll data exchange. Confirmed implementation evidence. | 2026-06-13 | Hein Blignaut |
| OI-W9-005 | **CLOSED** — OIC monitoring = confirmed implementation deliverable. Include: interface monitoring; integration monitoring; error management; alerting framework; operational visibility; exception handling. Exclude: day-to-day payroll operations; payroll processing services; managed payroll execution. APPSolve position: integration implementation partner and support partner. NOT payroll outsourcing provider. | 2026-06-13 | Hein Blignaut |

---

## Section 14: Coverage Analysis Summary

### Evidence Confidence by Scope Area

| Scope Area | Evidence Source | Evidence Tier | Confidence |
|---|---|---|---|
| OIC as integration technology | ANN1-V4.1 explicit mandate | Contractual | **HIGH — CONFIRMED** |
| PaySpace as integration target | ANN1-V4.1 billing heading | Contractual | **HIGH — CONFIRMED** |
| HCM-to-Payroll (outbound) | ANN1-V4.1 billing Months 1-2 | Contractual | **HIGH — CONFIRMED** |
| Payroll-to-HCM (inbound) | ANN1-V4.1 billing Months 3-4 | Contractual | **HIGH — CONFIRMED** |
| Production Build and Go-Live | ANN1-V4.1 billing Month 5 + project plan milestone | Contractual | **PENDING OI-W9-001** |
| Parallel payroll test methodology | ANN1-V4.1 project plan — Consecutive Runs | Contractual | **HIGH** |
| Data migration | ANN1-V4.1 billing Month 6 | Contractual | **HIGH** |
| Custom payslip development | ANN1-V4.1 Technical Build — 7 days | Contractual | **HIGH** |
| OIC architecture patterns | HIST-006 platform; OIC standard | Platform capability | **MEDIUM — PLATFORM** |
| Security and monitoring (OIC) | Platform capability; DFA operational (never named) | Mixed | **MEDIUM — PLATFORM + CORROBORATIVE** |
| Data elements (specific fields) | NOT specified in ANN1-V4.1 | Inferred | **LOW — needs BU Lead confirmation** |
| Legislative compliance support | DFA monthly reports (never named) | Corroborative internal | **MEDIUM — CORROBORATIVE ONLY** |
| Payroll reconciliation reporting | ANN1-V4.1 (Validation Run Report) | Contractual (partial) | **MEDIUM — confirm with BU Lead** |

---

## Section 14: Extraction Readiness v1.1 (AUTHORISED)

| Item | Status |
|---|---|
| Primary source identified and extracted | ✅ AUTHORISED |
| OIC architecture confirmed | ✅ AUTHORISED |
| PaySpace as integration target confirmed | ✅ AUTHORISED |
| Bidirectional integration scope confirmed | ✅ AUTHORISED |
| Production Build confirmed | ✅ AUTHORISED — OI-W9-001 CLOSED |
| Production go-live status confirmed | ✅ AUTHORISED — OI-W9-001 CLOSED: "fully implemented, completed, and operating in production" |
| "EBS Payroll" heading clarified | ✅ AUTHORISED — OI-W9-002 CLOSED: use PaySpace framing; not EBS Payroll |
| Reconciliation positioning confirmed | ✅ AUTHORISED — OI-W9-003 CLOSED: payroll validation framework |
| Bidirectional production confirmed | ✅ AUTHORISED — OI-W9-004 CLOSED: both directions in production |
| Monitoring positioning confirmed | ✅ AUTHORISED — OI-W9-005 CLOSED: OIC monitoring = implementation deliverable |
| Rule 21.4 (DFA) | ✅ AUTHORISED — never named |
| Acumatica PaySpace boundary excluded | ✅ AUTHORISED |
| APPSolve-as-payroll-processor prohibition | ✅ AUTHORISED |
| Product boundary (Fusion Payroll vs integration) | ✅ AUTHORISED |

**Extraction status: AUTHORISED — Proceed to Candidate Draft generation.**

---

### HB Evidence Reliability Rating

The Hollywood Bets Annexure 1 V4.1 is the highest-quality source in the Wave 3 corpus for payroll integration:
- **Signed contractual document** — highest evidential weight
- **Explicit billing schedule** with PaySpace named in the heading
- **Bidirectional scope** confirmed in milestone deliverables
- **Production Build milestone** explicitly included
- **Dedicated billing track** — R825,170 separate from HCM implementation

The only gap is production confirmation (OI-W9-001) — whether the programme's known delays affected the payroll integration delivery.
