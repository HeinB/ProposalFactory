---
document_id: SVR-W3S1-008
title: Source Validation Report — Oracle Help Desk & HR Service Delivery
version: "1.1"
status: "AUTHORISED — All 5 OI items CLOSED 2026-06-13 — BU Lead decisions applied — Proceed to Candidate Draft"
wave: "3"
deliverable: "W3S1-008"
created: "2026-06-13"
created_by: "Claude (AI — Wave 3 W3S1-008 SVR)"
---

> **STATUS: AUTHORISED — All 5 OI items CLOSED 2026-06-13 — Proceed to Candidate Draft generation**

---

# SVR-W3S1-008 — Oracle Help Desk & HR Service Delivery

**Source Validation Report | APPSolve Oracle Business Unit | Wave 3**

---

## Section 1: Executive Summary

This Source Validation Report covers the evidence available to support extraction of W3S1-008 Oracle Help Desk & HR Service Delivery as a Wave 3 Oracle HCM capability statement.

**Finding: Sufficient evidence exists to proceed to extraction, subject to one BLOCKING open item.**

Oracle HR Help Desk is confirmed as an implemented and referenceable module within the Hollywood Bets Oracle HCM go-live (July 2025, 7,000 users). This is Tier 1 evidence and establishes APPSolve as a confirmed Oracle HR Help Desk implementer.

Oracle HCM ER Case Management (employee relations cases — grievances, disciplinary actions, investigations) is the BLOCKING open item. The Hollywood Bets Annexure 2 scope was explicitly limited (chatbot/SMS + 4 routings) and does not mention ER Case Management. Separate evidence from the corpus suggests ER Case Management is a standard element of Oracle HR Help Desk, but no confirmed client implementation has been identified from the available sources with the scoping provided to this SVR.

Oracle Journeys is confirmed as included within the Oracle HCM Base license (B85800) — it is not separately licensed and is standard in every Oracle HCM implementation.

Oracle HR Knowledge Management (knowledge base within HR Help Desk) appears to be included within the Oracle HR Help Desk license (B87388) based on BOM evidence. ADVISORY OI item.

**Evidence tiers established:**
| Capability | Evidence Tier | Referenceable |
|---|---|---|
| Oracle HR Help Desk | Tier 1 — confirmed implementation (HB) | YES — Hollywood Bets |
| Oracle Journeys | Tier 1 — included in Oracle HCM Base | YES — every HCM implementation |
| Oracle HR Knowledge Management | Tier 1 probable (in Help Desk license) | Pending OI-W8-004 confirmation |
| Oracle HCM ER Case Management | BLOCKING — no confirmed implementation | Subject to OI-W8-002 decision |
| Oracle Digital Assistant | Tier 2 — Platform Capability Only | No implementation evidence |
| Oracle Redwood UX | Tier 2 — Platform UX standard | Standard in all current HCM implementations |

**BLOCKING item:** OI-W8-002 — Was Oracle HCM ER Case Management implemented at any client? Specifically: was ER Case Management within scope of the Hollywood Bets Help Desk implementation (Annexure 2)? Or is it Platform Capability Only?

**Open items requiring BU Lead decision:** 5 (1 BLOCKING, 4 ADVISORY)

---

## Section 2: Source Evidence Classification

### 2.1 Sources Reviewed

| HIST ID | Document | Date | Client | Classification |
|---|---|---|---|---|
| HIST-006 | APPSolve SAA HCM RFP Response | June 2025 | South African Airways | Tier 2 — Platform Capability Narrative. SAA not awarded. Not named. Comprehensive HR Help Desk capability description including ER Case Management. |
| HIST-007 | Hollywood Bets Accepted Proposal V5.0 | April 2023 | Hollywood Bets | **Tier 1 — Confirmed Implementation Evidence.** Annexure 2 = HR Help Desk scope (chatbot/SMS + 4 routings + knowledge base). Referenceable. |
| HIST-008 | RedPath Mining RFI Reply Detail | March 2026 | Redpath Mining | Tier 2 — technical capability reference. Only "Redwood" mentioned (Visual Builder Studio developer experience). No Help Desk content. |
| HIST-014 | CCBA HCM Solution V2.0 | 2025 | CCBA | **Restricted — SVR research only. CCBA never named.** Section 2.7 = Help Desk platform capability (same narrative as SAA). CCBA never named. |
| HIST-015 | Afrocentric HCM Proposal V4.0 | 2023 | Afrocentric Health | Delivery Methodology — current classification. Phase 1.6 = Help Desk (30 days). Mentions "grievances and disciplinaries." See Section 3.2. |
| HIST-016 | APPSolve SABS RFP Response | Dec 2025 | SABS | Essentially empty document (7,933 chars). Zero Help Desk content. Not a source for this statement. |
| HIST-017 | SAA Clarification Responses | 2025 | SAA | Not reviewed — no additional Help Desk content expected beyond HIST-006. |

### 2.2 Supplementary BOM Evidence

| Document | Client | Relevance |
|---|---|---|
| SAA HCM_BOM_V3.xlsx | SAA | Part B87388 "Fusion Human Resources Help Desk Cloud Service" in SAA proposed BOM (2,800 employees). Confirms Help Desk is a separately licensed product. SAA not awarded. |
| CCBA HCM_BOM_V3.xlsx | CCBA | Part B87388 in CCBA BOM (24,636 employees). **Scope comment: "Help Desk for ER management and reporting but also Case Management for long running ER cases and Document Management for management of HR Policy documentation."** CCBA never named. Internal evidence only. |
| HB V5.0 Annexure 2 | Hollywood Bets | Scope and pricing for Help Desk implementation. PM 0.25 FTE + Senior Functional 1 FTE + Senior Technical 0.5 FTE × 30 days = R435,375. |

### 2.3 Evidence Not Available in Corpus

| Item | Status |
|---|---|
| Hollywood Bets go-live confirmation (post July 2025) | Not in corpus — confirmed via ORACLE_FACT_BASELINE Section 19 (OI-W1-001 BU Lead CLOSED 2026-06-12) |
| ER Case Management delivery evidence for any client | Not confirmed — BLOCKING |
| DFA Help Desk | Not in ORACLE_FACT_BASELINE Section 19 DFA scope list — assumed excluded |

---

## Section 3: Module-Level Evidence Analysis

### 3.1 Oracle HR Help Desk

**Confirmed implementation evidence:**

**Hollywood Bets — Annexure 2 (HIST-007 V5.0):**
- Agreed during "further requirements confirmation workshops" — post-proposal addition
- Full Annexure 2 scope:
  - Submit inquiries via multiple channels
  - Route complex questions to correct person for personalized HR service delivery
  - Configure service request management system to handle complex HR rules (contractual terms and conditions)
  - Enable collaboration within each case via conversations and document sharing
  - Empower HR to curate a knowledge base readily available to workers and HR professionals
- **Scope limitations explicitly stated:**
  - "Inquiries to be submitted via the chat bot and SMS only"
  - "Only 4 routings are included for escalations and questions"
  - "Enhancements can be brought in as part of support"
- Pricing: R435,375 (PM 0.25 + Senior Functional 1 + Senior Technical 0.5 × 30 days)
- **ORACLE_FACT_BASELINE Section 19 confirmation:** Help Desk listed as part of HB go-live scope (OI-W1-001 CLOSED 2026-06-12)

**Platform capability narrative (HIST-006 SAA; HIST-014 CCBA — internal):**
- Oracle Fusion Helpdesk is a cloud-based case management solution embedded in Oracle Fusion HCM
- Specifically tailored for HR service delivery
- Multi-channel employee support (portal, chatbot, mobile, email)
- AI-powered knowledge base — auto-suggests articles based on case description
- Intelligent case routing — routes to correct HR specialist based on expertise and workload
- SLA management — set and enforce SLAs per case type
- HR analytics — dashboards for case resolution times, common issues, satisfaction trends
- Integration with Oracle HCM — agents see employee profile, job details, HR transactions in help desk view
- Role-based access control — confidential cases accessible only to authorized HR personnel
- AI-powered insights — recommend solutions, automate routine responses

**Evidence confidence:** HIGH — Tier 1 confirmed implementation (HB). Rich Tier 2 platform narrative available from HIST-006.

**Product name (authoritative):** "Fusion Human Resources Help Desk Cloud Service" — Part Number B87388. Must always use "Oracle HR Help Desk" in content — never "Oracle Service Cloud", "Oracle Fusion Service", or "Oracle B2C Service". These are separate products.

### 3.2 Oracle HCM ER Case Management

**Status: BLOCKING — OI-W8-002**

**Evidence reviewed:**

| Source | Content | Assessment |
|---|---|---|
| HB V5.0 Annexure 2 | No mention of ER Case Management, grievances, or disciplinary. Scope = chatbot/SMS + 4 routings + knowledge base. | Does NOT confirm ER Case Management was in HB Help Desk scope |
| CCBA BOM (internal — never named) | "Case Management for long running ER cases" explicitly noted as Help Desk scope | Internal evidence — validates Oracle HR Help Desk includes ER Case Management as standard product feature |
| CCBA BRS Section 7.1.2 (internal — never named) | Employee Relations sub-process: intake concerns (7.1.2.1), conduct investigation (7.1.2.2), facilitate resolution (7.1.2.3), conduct discipline due diligence (7.1.2.4), record disciplinary action (7.1.2.5) | Confirms ER Case Management was a CCBA requirement APPSolve was responding to — internal evidence |
| Afrocentric V4.0 Phase 1.6 (delivery methodology) | "HR Help Desk... Additionally managed processes such as grievances and disciplinaries can be tracked and managed in this module." | Afrocentric Phase 1.6 Help Desk (30 days) included grievances/disciplinaries — but current classification = delivery methodology only |
| SAA HIST-006 | "ER Case Management: Manage and track internal and external cases, such as grievances, disciplinary actions, and performance issues" — positioned as Help Desk capability | Platform capability narrative — SAA not awarded |
| ORACLE_FACT_BASELINE Section 19 | HB confirmed scope: "Help Desk" listed. No explicit ER Case Management sub-scope listed. | Ambiguous — Help Desk confirmed, but ER sub-scope not specified |

**Analysis:**
Oracle HR Help Desk (B87388) is a product that includes BOTH service request management AND ER case management as part of the same module. The CCBA BOM scope comment and Afrocentric V4.0 Section 3.3.6 both confirm that grievances and disciplinaries are features within the Oracle HR Help Desk product.

However, the Hollywood Bets Annexure 2 explicitly limited the scope to chatbot/SMS + 4 routings. ER Case Management (disciplinary processes, investigations, hearings) may or may not have been part of those 4 routings. This is ambiguous and requires BU Lead clarification.

**BLOCKING decision required from BU Lead:**
- Option A: ER Case Management = Confirmed delivery at HB (if the 4 routings included ER case types). Position as confirmed implementation evidence.
- Option B: ER Case Management = Platform Capability Only for this statement. HB Help Desk = service request routing only. ER Case Management included as platform capability ("APPSolve can configure Oracle HCM ER Case Management...").
- Option C: ER Case Management confirmed delivery — but not from HB. Reclassify Afrocentric Phase 1.6 Help Desk (which explicitly mentions grievances/disciplinaries) as internal implementation evidence (anonymous, not named). Requires BU Lead reclassification of Afrocentric status.

### 3.3 Oracle HR Knowledge Management

**Evidence:**
- HB Annexure 2: "Empower HR to curate a robust knowledge base of information that is readily available across workers and HR professionals" — explicitly in HB Help Desk scope
- SAA HIST-006: "AI-Powered Knowledge Base & Self-Service — HR Help Desk automatically suggests relevant articles based on case descriptions"
- CCBA BOM scope: "Document Management for management of HR Policy documentation" — within Help Desk (B87388)
- SAA BOM and CCBA BOM: No separate Knowledge Management license line — included within B87388 HR Help Desk license

**Assessment:** Oracle HR Knowledge Management (knowledge articles, HR policy documents, self-service knowledge base) is included within the Oracle HR Help Desk license (B87388). It is NOT the same as Oracle Knowledge Management Cloud (a separate product). See OI-W8-004 for BU Lead confirmation.

**Evidence confidence:** MEDIUM — HB Annexure 2 explicitly includes knowledge base. BOM evidence supports inclusion in Help Desk license.

### 3.4 Oracle Journeys

**Evidence:**
- CCBA BOM (B85800 Base HCM): "Oracle Fusion Journeys including Onboarding" — listed as included in Oracle HCM Base license
- SAA BOM (B85800 Base HCM): "Oracle Fusion Journeys including Onboarding" — included in base license
- SAA HIST-006: "Oracle Fusion Journeys — Employee Onboarding: Streamlines the onboarding process... Guided Processes: Provides step-by-step guides for various employee transitions... Personalized Experiences"
- CCBA BOM CCBA scope comment: "Journeys - Including Onboarding and Offboarding and Pre Hire Onboarding, Staff Movements including Global and Mass Movements"

**Assessment:** Oracle Journeys is INCLUDED in the standard Oracle Fusion HCM Base license (B85800). It is available to every Oracle HCM client by default. No separate licensing is required. Every Hollywood Bets, Afrocentric, and Redpath Mining implementation includes Journeys.

**Evidence confidence:** HIGH — Journeys is a standard HCM base module. BOM evidence is definitive.

**Framing:** Journeys capability is established by the base HCM license. It should be positioned as a standard Oracle HCM delivery capability in every HCM implementation, not as a separately scoped item. Omit from this statement OR include as brief integration point with HR Help Desk.

### 3.5 Oracle Digital Assistant

**Evidence:**
- SAA HIST-006: "Oracle Digital Assistant (Chatbot): Oracle offers an AI-powered chatbot that can be integrated with HCM. Employees can ask natural language questions... and receive immediate answers or be guided through processes"
- HB Annexure 2: "Inquiries to be submitted via the chat bot and SMS only" — this is the Help Desk chatbot submission channel, not necessarily Oracle Digital Assistant
- CCBA HIST-014: "Uses chatbots and digital assistants to provide career and performance guidance" (platform narrative)

**Assessment:** Oracle Digital Assistant is a separately licensed Oracle product that can integrate with Oracle HCM and Oracle HR Help Desk. The HB chatbot channel in Annexure 2 may be the Oracle HR Help Desk chatbot (native) rather than Oracle Digital Assistant (separate product). No confirmed Oracle Digital Assistant implementation evidence. Platform Capability positioning unless BU Lead can confirm Digital Assistant was part of a specific implementation.

**Evidence confidence:** LOW for confirmed delivery. Suitable only for platform capability description.

### 3.6 Redwood HR Service Delivery UX

**Evidence:**
- RedPath Mining RFI: APPSolve developers have "Visual Builder Studio (VB Studio) for Oracle Redwood pages for extensive personalisation of Redwood UI elements" — confirmed developer capability
- Context: Oracle Fusion HCM uses the Redwood UX design system as the standard interface for all modules since approximately 2022. All current implementations use Redwood.

**Assessment:** Redwood is not a separate module — it is Oracle's current UI design system for Oracle Fusion HCM. All Oracle HR Help Desk implementations delivered by APPSolve today use Redwood UX by default. APPSolve developers have confirmed Visual Builder Studio capability for Redwood page customization.

**Framing recommendation:** Do not present "Redwood HR Service Delivery" as a separate product or deliverable. Reference Redwood as the current Oracle HCM interface standard. Note APPSolve developer capability for Redwood page personalization where relevant.

**See OI-W8-005 for BU Lead guidance on whether explicit Redwood section is needed.**

---

## Section 4: Per-Source Analytics

| Source | Help Desk | ER Case Mgmt | Knowledge Mgmt | Journeys | Digital Asst | Redwood |
|---|---|---|---|---|---|---|
| HIST-007 HB V5.0 | ✅ **Tier 1** — limited scope (chatbot/SMS + 4 routings + KB). Annexure 2 | ❌ Not mentioned in HB scope | ✅ Explicitly in HB Annexure 2 scope | ✅ Part of base HCM license | ⚠️ Chatbot channel mentioned — may be Help Desk native, not ODA | ❌ Not mentioned |
| HIST-006 SAA | ✅ Rich platform capability | ✅ Platform narrative — grievances/disciplinary listed | ✅ Platform narrative — AI knowledge base | ✅ Platform narrative | ✅ Platform narrative | ❌ Not mentioned |
| HIST-014 CCBA (restricted) | ✅ Platform narrative (same as SAA) | ✅ BRS 7.1.2 — detailed ER process requirements | ✅ BRS 7.1.1 HR Knowledge Management | ✅ BOM — included in base license | ❌ Not mentioned | ❌ Not mentioned |
| CCBA BOM (restricted) | ✅ B87388 in scope — ER mgmt + Case Mgmt + Doc Mgmt | ✅ BOM scope comment explicitly includes ER case mgmt | ✅ Doc Management for HR Policy in Help Desk license | ✅ Base HCM includes Journeys | N/A | N/A |
| SAA BOM | ✅ B87388 in SAA BOM | ❌ Not separately noted | ❌ Not separately noted | ✅ Base HCM includes Journeys | N/A | N/A |
| HIST-015 Afrocentric | ✅ Phase 1.6 (30 days) — delivery methodology | ✅ Section 3.3.6 — "grievances and disciplinaries" in Help Desk | ❌ Not mentioned | ❌ Not mentioned | ❌ Not mentioned | ❌ Not mentioned |
| HIST-008 RedPath | ❌ Not mentioned | ❌ Not mentioned | ❌ Not mentioned | ❌ Not mentioned | ❌ Not mentioned | ✅ VB Studio developer capability |
| HIST-016 SABS ETS | ❌ Empty document | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## Section 5: Implementation Evidence Matrix (Per Client)

| Client | Help Desk Evidence | ER Case Mgmt | Referenceability | Governance |
|---|---|---|---|---|
| **Hollywood Bets** | ✅ CONFIRMED — Annexure 2 in go-live scope (ORACLE_FACT_BASELINE Section 19, OI-W1-001 CLOSED). Limited scope: chatbot/SMS + 4 routings + knowledge base. 30 days. July 2025 go-live. | ❌ NOT confirmed — Annexure 2 does not mention grievances/disciplinary. Scope was limited. | ✅ **REFERENCEABLE** — HB is confirmed Tier 1 reference. Help Desk is part of confirmed go-live scope. | Scope must be accurately framed as limited implementation (chatbot/SMS + 4 routings). Must not overstate as full ER Case Management implementation without OI-W8-002 resolution. |
| **DFA** | ❌ Not in confirmed DFA HCM scope (ORACLE_FACT_BASELINE Section 19: Core, Talent, Learning, Taleo, Compensation listed — Help Desk absent) | ❌ | Rule 21.4 — DFA never named regardless | N/A — Help Desk not confirmed for DFA |
| **Afrocentric Health** | ⚠️ Phase 1.6 = Help Desk (30 days) in proposal. Grievances and disciplinaries mentioned in scope description. Classification = delivery methodology — not confirmed implementation. | ⚠️ Mentioned in Phase 1.6 as tracked in Help Desk module | Not named — delivery methodology classification applies | See OI-W8-002 Option C — BU Lead can reclassify as anonymous internal evidence |
| **CCBA** | Proposed (BOM B87388, 24,636 employees, "ER management + Case Management + Document Management") — CCBA is restricted — never named | Proposed scope (BOM + BRS) | CCBA never named under any circumstances | Internal validation only — confirms Oracle HR Help Desk product includes ER Case Management as standard feature |
| **SAA** | Proposed (BOM B87388, 2,800 employees) — SAA not awarded | Described in platform narrative | SAA not named as client reference | Platform capability source only |
| **Redpath Mining** | ❌ Not in scope | ❌ | Active pipeline — Rule 21.5 (Absence is the Help Desk evidence from Redpath — not Help Desk) | Help Desk not part of Redpath scope |

---

## Section 6: Product Boundary Table

| Product | Included? | Licensing | Evidence | APPSolve position |
|---|---|---|---|---|
| Oracle HR Help Desk (service request mgmt) | YES | Separately licensed — B87388 | HB Annexure 2 (Tier 1) | **Confirmed delivery** |
| Oracle HR Help Desk (case routing) | YES | Within B87388 | HB Annexure 2 — 4 routings | **Confirmed delivery — limited scope** |
| Oracle HR Help Desk (chatbot channel) | YES | Within B87388 | HB Annexure 2 — chatbot/SMS | **Confirmed delivery** |
| Oracle HR Help Desk (knowledge base / knowledge articles) | YES | Within B87388 | HB Annexure 2 (explicit) + CCBA BOM scope | **Confirmed delivery** |
| Oracle HR Help Desk (SLA management) | YES | Within B87388 | SAA HIST-006 (platform capability) | Platform Capability |
| Oracle HR Help Desk (agent workspace / agent UI) | YES | Within B87388 | SAA HIST-006 (platform capability) | Platform Capability |
| Oracle HR Help Desk (queue management) | YES | Within B87388 | SAA HIST-006 (platform capability) | Platform Capability |
| Oracle HCM ER Case Management (grievances) | YES (product feature) | Within B87388 | CCBA BOM (internal); Afrocentric Phase 1.6 | **PENDING OI-W8-002** |
| Oracle HCM ER Case Management (disciplinary) | YES (product feature) | Within B87388 | CCBA BRS 7.1.2; Afrocentric Section 3.3.6 | **PENDING OI-W8-002** |
| Oracle HCM ER Case Management (investigations) | YES (product feature) | Within B87388 | CCBA BRS 7.1.2.2 | **PENDING OI-W8-002** |
| Oracle HCM ER Case Management (hearings) | YES (product feature) | Within B87388 | Not in available corpus | Platform Capability |
| Oracle HCM ER Case Management (action plans) | YES (product feature) | Within B87388 | Not explicitly confirmed | Platform Capability |
| Oracle Journeys | YES | INCLUDED in HCM Base (B85800) | CCBA BOM + SAA BOM confirmed | Standard HCM delivery — not separately positioned |
| Oracle Digital Assistant (chatbot AI) | YES — optional integration | Separately licensed | SAA HIST-006 (platform) | Platform Capability Only |
| Oracle Redwood UX | YES | Standard Oracle HCM UI | RedPath RFI (developer capability) | Standard UX — not separately positioned |
| Oracle Fusion Service (B2C Service) | NO — different product | Separate product family | N/A | **MUST NOT CONFLATE** with Oracle HR Help Desk |
| Oracle Service Cloud | NO — different product | Separate product family | N/A | **MUST NOT CONFLATE** with Oracle HR Help Desk |
| Oracle ITSM (Incident/Change Mgmt) | NO — ITSM product | Separate product | CCBA BRS Section 5 = ITSM (3rd level support) | **ITSM MUST NOT BLEED INTO HR HELP DESK CONTENT** |

---

## Section 7: Governance Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| GR-W8-001 | **Oracle HR Help Desk vs Oracle Fusion Service conflation** — Draft describes Oracle HR Help Desk as "Oracle Service Cloud" or "Oracle Fusion Service" — these are entirely different product families | HIGH | HIGH | Mandatory product name: "Oracle HR Help Desk" or "Oracle Fusion Human Resources Help Desk" (B87388). Never: Oracle Service Cloud, Oracle Fusion Service, Oracle B2C Service, Oracle CX Service. Add explicit product boundary note in Section 2 of draft. |
| GR-W8-002 | **ITSM bleed** — CCBA BRS Section 5 describes ITIL v3 ITSM (Incident/Change/Service Request Management) and it could be confused with Oracle HR Help Desk | LOW | HIGH | Extraction must draw from Section 7 (Employee Support) only, not Section 5 (ITIL) from CCBA BRS. If any ITSM language enters the draft, flag immediately and remove. |
| GR-W8-003 | **ER Case Management unsupported claim** — Draft implies ER Case Management (disciplinary proceedings, investigations, hearings) was implemented at a client without confirmed evidence | HIGH (if not resolved) | HIGH | OI-W8-002 is BLOCKING for this reason. Extract only with explicit BU Lead decision on ER scope. |
| GR-W8-004 | **HB Help Desk scope overstated** — Draft implies a full, enterprise-scale HR Help Desk implementation at HB when Annexure 2 scope was limited (chatbot/SMS + 4 routings) | MEDIUM | HIGH | HB Help Desk reference must include accurate scope framing. Approved framing to be confirmed via OI-W8-003 BU Lead decision. |
| GR-W8-005 | **Afrocentric reclassification without authorization** — Phase 1.6 Help Desk (grievances/disciplinaries) used as implementation evidence without BU Lead reclassification | LOW | MEDIUM | Afrocentric remains "delivery methodology" unless BU Lead explicitly reclassifies. See OI-W8-002 Option C. |
| GR-W8-006 | **Wave 3 rules 21.1–21.5 breach** — DFA named; CCBA referenced; SAA presented as implementation; Redpath presented as completed implementation | LOW | HIGH | Standing rules applied throughout. All prohibited clients absent from draft. |
| GR-W8-007 | **Oracle Journeys positioned as separately licensed** — Draft implies Journeys requires additional licensing when it is included in HCM Base (B85800) | LOW | MEDIUM | Journeys = standard Oracle HCM capability. No separate licensing language. |

---

## Section 8: Proposed Document Structure

Proposed structure for W3S1-008 Oracle Help Desk & HR Service Delivery Candidate Draft. Structure subject to adjustment based on BU Lead decisions for OI-W8-001 through OI-W8-005.

| Section | Title | Evidence basis | Notes |
|---|---|---|---|
| 1 | Statement of Capability | All sources | Capability overview; product positioning; module-product boundary |
| 2 | Product Architecture — Oracle HR Service Delivery Suite | HIST-006 + BOM evidence | Clarify: HR Help Desk (B87388) vs HCM Base Journeys (B85800); distinguish from Oracle Fusion Service |
| 3 | Oracle HR Help Desk — Service Request Management | HIST-007 HB Annexure 2 (Tier 1) + HIST-006 | Full HR Help Desk capability; confirmed delivery at HB; scope accurately framed |
| 4 | Oracle HCM ER Case Management | **PENDING OI-W8-002** | If Platform Capability: Section 4 platform capability only. If Tier 1: confirmed delivery framing |
| 5 | Oracle HR Knowledge Management | HIST-007 Annexure 2 + HIST-006 + CCBA BOM | Knowledge articles; policy documents; self-service search; integrated in B87388 |
| 6 | Case Routing and SLA Management | HIST-007 (4 routings confirmed) + HIST-006 (platform) | Routing configuration; SLA management; escalation paths |
| 7 | Employee and Manager Self-Service Channels | HIST-006 (platform) | Portal, chatbot, mobile, email submission channels |
| 8 | HR Analytics and Reporting for Help Desk | HIST-006 (platform) + cross-ref W3S1-006 | Case resolution times; volume trends; SLA compliance; OTBI cross-reference |
| 9 | Oracle Journeys — HR-Guided Processes | BOM evidence + HIST-006 | Journeys = base HCM standard; onboarding; guided employee transitions; integration with Help Desk |
| 10 | Oracle Digital Assistant Integration | HIST-006 (platform) | Platform Capability — no confirmed implementation; standard positioning with qualification |
| 11 | Redwood HR Service Delivery UX | RedPath RFI (developer) | UX standard; Visual Builder Studio customization capability; brief section only |
| 12 | Integration Architecture | ORACLE_FACT_BASELINE + HIST-006 | OIC standard; Help Desk ↔ Core HR; Help Desk ↔ Journeys; notification integrations |
| 13 | APPSolve Delivery Capability | HIST-007 + HIST-015 | Practice description; confirmed implementations; delivery model |
| 14 | Implementation References | HIST-007 + ORACLE_FACT_BASELINE Section 19 | HB confirmed reference; scope accurately framed |
| 15 | Risk and Assumptions Register | This SVR | Licensing, scope, implementation risks |
| 17 | Approval Record | Governance | — |
| Appendix A | Source Mapping Table | This SVR | — |
| Appendix B | Governance Self-Review | Governance | — |
| Appendix C | Extraction Return Report | Governance | — |

---

## Section 9: Open Items Register

### OI-W8-001 — Oracle HR Help Desk Implementation Status
**Status:** ADVISORY — RESOLVED from corpus evidence. BU Lead guidance requested on framing.
**Question:** Has APPSolve implemented Oracle HR Help Desk for any client?
**Evidence:** YES — Hollywood Bets confirmed in ORACLE_FACT_BASELINE Section 19 (OI-W1-001 CLOSED 2026-06-12). Annexure 2 scope was limited: chatbot/SMS + 4 routings + knowledge base. R435,375. 30 days. Go-live July 2025.
**Decision required from BU Lead:**
- (A) CONFIRMED — use HB Help Desk as Tier 1 confirmed delivery reference. Frame as limited-scope implementation (chatbot/SMS channel + 4 service request routings + knowledge base).
- (B) CONFIRMED — use HB Help Desk as Tier 1 reference. Frame more broadly as APPSolve's first Oracle HR Help Desk implementation. Do not explicitly call out scope limitations in tender-facing content.
- (C) CONFIRMED — provide additional information about what the 4 routings covered (e.g., were ER cases one of the routing types?).
**Blocking?** ADVISORY — extraction can proceed for the non-ER Help Desk sections. Required to finalise Section 14 (Implementation References).

---

### OI-W8-002 — Oracle HCM ER Case Management Implementation Evidence ⚠️ BLOCKING
**Status:** OPEN — BLOCKING — CANNOT EXTRACT UNTIL RESOLVED
**Question:** Has APPSolve implemented Oracle HCM ER Case Management (employee relations cases — grievances, disciplinary processes, investigations) for any client? Was ER Case Management within the Hollywood Bets Help Desk Annexure 2 scope?
**Evidence reviewed:**
- HB Annexure 2: Does NOT mention ER Case Management, grievances, or disciplinary processes. Scope was limited to chatbot/SMS + 4 routings. No evidence ER cases were one of the 4 routing types.
- CCBA BOM (restricted): "Help Desk for ER management and reporting but also Case Management for long running ER cases" — confirms Oracle HR Help Desk includes ER as product feature, but CCBA is never named.
- Afrocentric V4.0 Phase 1.6 (current classification: delivery methodology): "grievances and disciplinaries can be tracked and managed in this module" — Help Desk phase was 30 days.
- SAA HIST-006 (not awarded): ER Case Management described as Help Desk capability.

**Options for BU Lead decision:**
- **Option A — Platform Capability Only:** ER Case Management is positioned as an Oracle platform capability APPSolve can configure and implement. No client implementation claim. Conservative — zero risk. Approved framing: "Oracle HR Help Desk includes ER Case Management capabilities for grievances, disciplinary processes, and workplace investigations. APPSolve can configure and implement these capabilities where required and in scope."
- **Option B — Confirmed delivery at HB:** BU Lead confirms that ER Case Management (grievances/disciplinary) was one of the 4 routings implemented at Hollywood Bets. Approved framing then includes HB as reference for ER Case Management. This requires BU Lead to confirm the routing types from the Hollywood Bets implementation.
- **Option C — Anonymous internal implementation (Afrocentric):** BU Lead reclassifies Afrocentric Phase 1.6 Help Desk as internal implementation evidence for ER Case Management (grievances, disciplinaries explicitly mentioned). Anonymous — "a South African healthcare sector client" — cannot be named. Afrocentric's ER classification requires an explicit BU Lead reclassification decision for this statement.

**Blocking reason:** Without this decision, Section 4 (ER Case Management) cannot be written with the correct evidence tier. Proceeding without resolution risks either (a) incorrectly claiming ER Case Management delivery, or (b) excluding a legitimate capability area that is valuable for tenders.

---

### OI-W8-003 — Hollywood Bets Help Desk Reference Framing
**Status:** ADVISORY — linked to OI-W8-001 and OI-W8-002
**Question:** How should the Hollywood Bets Help Desk implementation be presented in the capability statement, given the limited Annexure 2 scope (chatbot/SMS + 4 routings)?
**Context:** HB Help Desk was confirmed go-live, but the implementation was explicitly limited in scope. Overstating the scope in tender content risks misrepresentation.
**Options for BU Lead guidance:**
- (A) **Accurate limited scope framing:** "APPSolve implemented Oracle HR Help Desk for Hollywood Bets (go-live July 2025, 7,000 users), including chatbot and SMS service request submission, service routing, and a curated HR knowledge base." Explicitly limited — honest.
- (B) **Capability framing without scope qualification:** "APPSolve implemented Oracle HR Help Desk for Hollywood Bets (go-live July 2025, 7,000 users)." No scope qualification. Implies full implementation.
- (C) **BU Lead to advise** on what was actually implemented — the Annexure 2 was the proposal stage scope; the final go-live scope may have been different (expanded or reduced during implementation).

---

### OI-W8-004 — Knowledge Management Licensing Boundary
**Status:** ADVISORY — likely resolved from BOM evidence
**Question:** Is Oracle HR Knowledge Management included within the Oracle HR Help Desk license (B87388), or is it a separately licensed product?
**Evidence:** SAA BOM and CCBA BOM: B87388 "Fusion Human Resources Help Desk Cloud Service" includes no sub-licensing notation. CCBA BOM scope comment includes "Document Management for management of HR Policy documentation" within the Help Desk scope. HB Annexure 2 explicitly includes "knowledge base" as a Help Desk deliverable.
**Probable answer:** Oracle HR Knowledge Management (knowledge articles, HR policy documents, self-service knowledge base within HR Help Desk) is INCLUDED within the Oracle HR Help Desk license (B87388). It is not separately licensed.
**Caution:** This is DIFFERENT from Oracle Knowledge Management Cloud (separate standalone product). Do not conflate.
**BU Lead decision:** Confirm that Knowledge Base is included in Help Desk license. If confirmed: no separate licensing note required. If NOT included: add licensing note in Section 2 boundary table.

---

### OI-W8-005 — Redwood HR Service Delivery Differentiation
**Status:** ADVISORY — low materiality
**Question:** Should "Redwood HR Service Delivery" be positioned as a distinct capability area in the statement, or as a UX standard?
**Evidence:** All current Oracle Fusion HCM implementations use Redwood UX (standard since ~2022). RedPath RFI confirms APPSolve has Visual Builder Studio developer capability for Redwood customization.
**Recommendation:** Redwood is not a separate product or licensed module. It is Oracle's current HCM UX framework. It should NOT be positioned as a separate section. Reference Redwood as the standard Oracle HCM interface. Note APPSolve's VB Studio customization capability as a technical differentiator.
**BU Lead decision:** Confirm whether a dedicated Redwood section is needed, or whether a brief reference within the main sections is sufficient.

---

## Section 10: Extraction Readiness Assessment

| Item | Status |
|---|---|
| **Oracle HR Help Desk (service requests, routing, knowledge base)** | ✅ READY — sufficient Tier 1 evidence from HB Annexure 2 + ORACLE_FACT_BASELINE Section 19 |
| **Oracle HCM ER Case Management** | ❌ BLOCKED — OI-W8-002 unresolved |
| **Oracle HR Knowledge Management** | ⚠️ ADVISORY — OI-W8-004 pending |
| **Oracle Journeys** | ✅ READY — confirmed standard in Oracle HCM Base license |
| **Oracle Digital Assistant** | ✅ READY — Platform Capability framing; no implementation claim required |
| **Redwood UX** | ✅ READY — brief reference only; OI-W8-005 advisory |
| **Implementation References** | ⚠️ ADVISORY — OI-W8-003 pending for HB framing guidance |
| **Wave 3 governance rules 21.1–21.5** | ✅ All standing rules confirmed applicable |

**Overall extraction readiness: NOT READY — OI-W8-002 BLOCKING**

Estimated effort on BU Lead decision receipt: 3–4 hours to produce Candidate Draft.

---

## Section 11: Standing Governance Confirmations

The following Wave 3 standing governance rules (ORACLE_FACT_BASELINE Section 21) apply to W3S1-008:

| Rule | Applicability | Status |
|---|---|---|
| **21.1 Aviation PROHIBITED** | SAA not named; no aviation sector content | ✅ APPLIES |
| **21.2 Implementation vs Support distinction** | HB = implementation (Help Desk confirmed). Must distinguish confirmed delivery from platform capability. | ✅ APPLIES |
| **21.3 Opportunity Marketplace** | Not applicable to this statement | N/A |
| **21.4 DFA never named** | DFA Help Desk not confirmed in scope — DFA not named regardless | ✅ APPLIES |
| **21.5 Redpath Mining not referenceable** | Redpath = active pipeline; Help Desk not in Redpath scope | ✅ APPLIES — no Redpath Help Desk content |
| **CCBA never named** | CCBA BOM and BRS used for internal validation only — CCBA never named | ✅ CRITICAL |
| **ITSM must not bleed into HR Help Desk** | CCBA BRS Section 5 ITSM excluded from extraction | ✅ EXPLICIT RULE |
| **Oracle HR Help Desk ≠ Oracle Fusion Service** | Product names must be precise | ✅ CRITICAL |

**Additional standing rule for this statement:**
> **Oracle HR Help Desk (B87388) must never be described as "Oracle Service Cloud", "Oracle Fusion Service", "Oracle B2C Service", or "Oracle CX Service". These are entirely different products. Use "Oracle HR Help Desk" or "Oracle Fusion Human Resources Help Desk Cloud Service" exclusively.**

---

## Section 12: Source Paragraph Index

| Para / Section | Source | Content |
|---|---|---|
| Annexure 2 — pg 27 | HIST-007 HB V5.0 | HR Help Desk scope: purpose, limitations (chatbot/SMS + 4 routings), pricing (R435,375, 30 days, PM+FuncConsult+TechConsult) |
| "Help Desk" in go-live list | ORACLE_FACT_BASELINE Section 19 | HB confirmed go-live scope: "Help Desk" listed among confirmed modules (OI-W1-001 CLOSED 2026-06-12) |
| Section 3.3.6 | HIST-015 Afrocentric V4.0 | "HR Help Desk: The help desk enables support for the HR team... grievances and disciplinaries can be tracked and managed in this module" — Phase 1.6 (30 days) |
| Phase 1.6 project schedule | HIST-015 Afrocentric V4.0 | "Phase 1.6 - Help Desk 30 days 2023/11/13 2023/12/22" |
| Section 2.7 | HIST-014 CCBA V2.0 | Help Desk platform overview (same narrative as SAA) — CCBA restricted |
| BRS Section 7.1 | CCBA BRS V7.1 | Employee Support: 7.1.1 HR Knowledge Management, 7.1.2 Employee Relations (intake, investigate, facilitate, discipline, record), 7.1.3 Employee Contact Management — CCBA restricted |
| B87388 scope comment | CCBA BOM V3 | "Help Desk for ER management and reporting but also Case Management for long running ER cases and Document Management for management of HR Policy documentation" — CCBA restricted |
| B85800 included products | CCBA BOM V3 + SAA BOM V3 | "Oracle Fusion Journeys including Onboarding" — confirmed included in base HCM license |
| B87388 in SAA BOM | SAA BOM V3 | HR Help Desk separately licensed (2,800 employees) — SAA not awarded |
| Help Desk Overview | HIST-006 SAA RFP | Full platform capability narrative: benefits, key features table, ER Case Management, Knowledge Base, routing, SLA, Digital Assistant |
| Journeys section | HIST-006 SAA RFP | Journeys — Employee Onboarding, Guided Processes, Personalized Experiences, OCIPA integration |
| Digital Assistant | HIST-006 SAA RFP | Oracle Digital Assistant — AI chatbot — natural language HR queries — integrated with HCM |
| "Redwood" | HIST-008 RedPath RFI | "Visual Builder Studio (VB Studio) for Oracle Redwood pages for extensive personalisation of Redwood UI elements" |

---

## Section 13: Decisions Log

| Decision ID | Description | Status | BU Lead Decision |
|---|---|---|---|
| OI-W8-001 | HB Help Desk scope and framing | CLOSED 2026-06-13 | HB = confirmed Tier 1. Full delivered scope: HR Help Desk + ER + Knowledge Management + Chatbot + SMS + Routing + Workflows + KB curation. Do not over-emphasise project estimate/duration/pricing. Focus on delivered capability and outcomes. Go-live July 2025. ~7,000 users. Referenceable: YES. |
| OI-W8-002 | ER Case Management implementation | CLOSED 2026-06-13 | **CONFIRMED IMPLEMENTATION CAPABILITY.** ER Case Management, case tracking, grievance management, disciplinary process management, long-running ER case management, audit history, document management = all confirmed delivery. HB implemented full Oracle HR Help Desk including ER. CCBA corroborates. Afrocentric methodology aligns. |
| OI-W8-003 | HB reference framing | CLOSED 2026-06-13 | Anonymous: "APPSolve implemented Oracle HR Help Desk capabilities for a large South African gaming and entertainment organisation supporting approximately 7,000 users." Named: "APPSolve implemented Oracle HR Help Desk for Hollywood Bets, including Employee Relations case management, knowledge management, service request routing, chatbot capabilities and employee self-service support." |
| OI-W8-004 | Knowledge Management licensing | CLOSED 2026-06-13 | Knowledge Management INCLUDED within Oracle HR Help Desk. Confirmed implementation capability. No separate licensing discussion required in capability statement. |
| OI-W8-005 | Redwood positioning | CLOSED 2026-06-13 | Dedicated Redwood subsection required. Position as modern Oracle UX layer for Oracle HR Help Desk — not a separate product. Covers: Redwood HR Help Desk experience, Redwood employee self-service, Redwood agent workspace, Redwood case management experience. |

## Section 14: Extraction Readiness (v1.1 — AUTHORISED)

| Item | Status |
|---|---|
| Oracle HR Help Desk (service requests, routing, chatbot, SMS) | ✅ AUTHORISED — Tier 1 HB confirmed |
| Oracle HCM ER Case Management (grievances, disciplinary, investigations, long-running cases) | ✅ AUTHORISED — Confirmed implementation capability |
| Oracle HR Knowledge Management | ✅ AUTHORISED — Confirmed implementation capability (included in Help Desk) |
| Oracle Journeys | ✅ AUTHORISED — Standard HCM Base capability |
| Oracle Digital Assistant | ✅ AUTHORISED — Platform Capability framing |
| Redwood HR Service Delivery | ✅ AUTHORISED — Dedicated subsection; modern UX layer |
| Implementation References | ✅ AUTHORISED — HB approved framing confirmed |
| Wave 3 governance rules 21.1–21.5 | ✅ All in force |
| **Overall** | **✅ AUTHORISED — Proceed to Candidate Draft** |
