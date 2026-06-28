# APPSolve Tender Knowledge Base — Wave 4 Candidate Discovery Report

**Version:** 1.0 | **Created:** 2026-06-14 | **Owner:** Hein Blignaut (BU Lead)
**Purpose:** Identify Oracle capability areas not yet represented in the KB that have evidence basis in approved and registered source material. Establishes the Wave 4 extraction backlog.

> **Scope:** Search performed against ORACLE_FACT_BASELINE.md, WAVE3_HCM_SOURCE_DISCOVERY_REPORT.md (module coverage table), ORACLE_REFERENCE_GAP_REPORT.md, and all registered HIST source documents. No new source documents were read for this report — all findings are grounded in approved evidence already established in the KB.
>
> **Governance rule:** No capability statement may be created from this report without BU Lead extraction authorisation. This report is a planning document only.

---

## Part A — HCM Capability Extensions (Modules Not Yet Extracted)

These are Oracle HCM modules confirmed in the Wave 3 source discovery report's module coverage table (WAVE3_HCM_SOURCE_DISCOVERY_REPORT.md Section 3) but not extracted as standalone Wave 3 statements. They are natural candidates for Wave 4 extraction.

---

### W4-HCM-001 — Oracle Benefits Administration

| Field | Value |
|---|---|
| **Capability Area** | Oracle Fusion Benefits — employee benefits enrollment, life events, flex plan management, benefits reporting |
| **Evidence Available** | Yes — in Wave 3 source documents |
| **Evidence Source** | HIST-006 (SAA RFP Section 2 — Benefits confirmed as HCM module in scope) |
| **Evidence Tier** | **Tier 3 — Proposed Only.** SAA proposal is the only source. No confirmed go-live implementation of Benefits as a standalone module. DFA is known to use Oracle Fusion full suite (Rule 21.4 — internal only) which may include Benefits. |
| **Module Coverage in Wave 3 Source Documents** | HIST-006 (SAA): H (High — primary); HIST-014 (CCBA): M (Medium) |
| **Wave 3 Flag** | F-W3-001 — Benefits identified as requiring BU Lead confirmation (implemented vs proposed only) |
| **Recommendation** | **Defer until Tier 1 evidence obtained.** At Tier 3, a Benefits capability statement would be limited to "APPSolve has scoped and proposed Oracle Benefits" — not a strong tender position. Upgrade path: confirm if any current client (HB, DFA) has Benefits in live scope. If HB Phase 5+ includes Benefits, upgrade to Tier 1 upon go-live confirmation. |
| **Estimated Priority** | Low |

---

### W4-HCM-002 — Oracle Journeys (Employee Self-Service & Guided Journeys)

| Field | Value |
|---|---|
| **Capability Area** | Oracle Journeys — guided employee self-service workflows; personalised HR task checklists; onboarding journeys; life event journeys; HR process automation |
| **Evidence Available** | Yes — in Wave 3 source documents |
| **Evidence Source** | HIST-006 (SAA RFP Section 2 — "Journeys" confirmed as module in scope); HIST-014 (CCBA — supporting) |
| **Evidence Tier** | **Tier 2 — Platform Capability.** Journeys is an Oracle HCM standard module confirmed in both SAA and CCBA proposals. However, no standalone Journeys delivery has been confirmed as a primary deliverable. Within the Hollywood Bets scope, self-service workflows are likely embedded in Global HR delivery (W3S1-001) — may already be Tier 1 if confirmed as a defined HB deliverable. |
| **Distinction from Existing Content** | W3S1-001 (HCM Core) may capture basic self-service. A dedicated Journeys statement would cover the guided journey framework, onboarding automation, and life event management as a named capability. |
| **Wave 3 Flag** | F-W3-001 — "Journeys / Employee Self-Service" identified as a module requiring BU Lead implementation confirmation |
| **Recommendation** | **Medium priority extraction candidate.** Journeys is a high-frequency tender requirement for enterprise HCM. Confirm with BU Lead whether HB Phase 1 (Global HR go-live) included Journeys as a configured deliverable. If yes: Tier 1, extract in Wave 4A. If no: Tier 2 exception, extract with proposal-level framing. |
| **Estimated Priority** | Medium |

---

### W4-HCM-003 — Oracle Workforce Directory & Workforce Modelling

| Field | Value |
|---|---|
| **Capability Area** | Oracle Workforce Directory — org chart, people finder, team directories; Oracle Workforce Modelling — what-if restructuring simulations, headcount planning, scenario comparisons |
| **Evidence Available** | Yes — in Wave 3 source documents |
| **Evidence Source** | HIST-006 (SAA RFP Section 2 — "Workforce Directory" and "Workforce Modelling" both confirmed as modules in scope) |
| **Evidence Tier** | **Tier 2 — Platform Capability.** SAA proposal only. No confirmed standalone delivery. These are standard Oracle HCM modules likely included in any full HCM Core implementation (HB). |
| **Wave 3 Flag** | F-W3-001 — "Workforce Directory / Modelling" identified as requiring confirmation |
| **Recommendation** | **Low-medium priority.** These are typically bundled with HCM Core rather than tendered as standalone capabilities. Consider incorporating into W3S1-001 (HCM Core) update rather than standalone statement. Alternatively, combine with Journeys (W4-HCM-002) into an "Oracle HCM Employee Experience" capability statement covering self-service, directory, and modelling. |
| **Estimated Priority** | Low-Medium |

---

### W4-HCM-004 — Oracle Time and Labour (Standalone)

| Field | Value |
|---|---|
| **Capability Area** | Oracle Time and Labour — time capture, timesheets, shift scheduling, compliance enforcement, labor analytics; separate from Absence Management |
| **Evidence Available** | Yes — strong evidence in source documents |
| **Evidence Source** | HIST-006 (SAA RFP — Time and Labor); HIST-015 (Afrocentric Phase 4 — Time and Labor); HIST-016 (SABS ETS — Mr Price confirmed as HCM + **Time and Labour** client) |
| **Evidence Tier** | **Tier 1 — Mr Price Group confirmed (Time and Labour scope — SABS ETS + ORACLE_FACT_BASELINE Section 11).** Currently this evidence is folded into W3S1-007 (Workforce Management). Extracting T&L as a standalone statement would make the Mr Price T&L reference explicit and searchable. |
| **Current Coverage** | W3S1-007 covers Absence Management as primary and T&L as secondary. Time and Labour as a dedicated capability statement (including shift scheduling, T&L compliance, labor cost analytics) would strengthen proposals where T&L is the primary requirement (e.g., shift-based industry tenders). |
| **Recommendation** | **High priority.** Mr Price T&L reference is Tier 1. Separating T&L from W3S1-007 would allow the Mr Price reference to be cited specifically for T&L tenders without the broader Workforce Management framing. BU Lead decision: expand W3S1-007 or create W4-HCM-004 as separate statement. |
| **Estimated Priority** | High |

---

### W4-HCM-005 — Oracle Work Life Solutions

| Field | Value |
|---|---|
| **Capability Area** | Oracle Work Life — wellbeing, connections, volunteering, competitions, community platform embedded in Oracle HCM |
| **Evidence Available** | Limited |
| **Evidence Source** | HIST-006 (SAA RFP Section 2 — "Work Life" confirmed) |
| **Evidence Tier** | **Tier 3 — Proposed Only.** SAA proposal only; single source; no confirmed delivery. Niche tender requirement. |
| **Recommendation** | **Low priority. Defer.** Work Life is rarely a primary tender evaluation criterion. Extract only if a specific tender requirement arises. |
| **Estimated Priority** | Low |

---

## Part B — Oracle Experience & AI Capabilities (BU Lead Priority List)

### W4-AI-001 — Oracle Digital Assistant (ODA) within HCM

| Field | Value |
|---|---|
| **Capability Area** | Oracle Digital Assistant — conversational AI chatbot for HR self-service; integrated into Oracle Fusion HCM; handles HR queries, leave applications, payroll enquiries |
| **Evidence Available** | Yes — in Wave 3 source documents |
| **Evidence Source** | HIST-006 (SAA BOM confirms Digital Assistant as in-scope HCM component); W3S1-008 (HR Help Desk — chatbot routing already mentioned as a Help Desk feature) |
| **Evidence Tier** | **Tier 2 — Platform Capability.** ODA is confirmed as an Oracle HCM platform component in the SAA BOM. Currently partially captured in W3S1-008 (Help Desk chatbot). A dedicated ODA statement would cover conversational AI architecture, HR self-service use cases, integration patterns, and multi-channel deployment across all HCM modules (not only Help Desk). |
| **Distinction from Existing Content** | W3S1-008 covers ODA in the Help Desk context only. A standalone ODA statement would position APPSolve as an ODA implementer across the full HCM suite — separate from Help Desk. |
| **Recommendation** | **Medium priority.** ODA is a differentiator in AI-forward tenders. Evidence is Tier 2 (SAA BOM — not a confirmed standalone ODA delivery). Frame as "Oracle Digital Assistant platform configuration and HCM integration" with Tier 2 evidence disclosure. Consider combining with W4-AI-003 into an "Oracle AI and Digital Experience" capability statement. |
| **Estimated Priority** | Medium |

---

### W4-AI-002 — Oracle AI-Based Skills Intelligence

| Field | Value |
|---|---|
| **Capability Area** | Oracle AI Skills — dynamic skills profiles, AI-powered job recommendations, skills gap analysis, AI-driven talent matching, career pathways |
| **Evidence Available** | Yes — confirmed module |
| **Evidence Source** | ORACLE_FACT_BASELINE Section 4.1: "AI-Based Skills | SAA Section 2 | —" |
| **Evidence Tier** | **Tier 2 — Platform Capability.** Confirmed Oracle HCM module. Whether APPSolve has specifically configured AI Skills for any client is unconfirmed. Hollywood Bets Phase 4 (Talent Management) may include AI Skills within the talent framework. |
| **Recommendation** | **Medium priority.** AI in HCM is a growing tender criterion. Confirm with BU Lead whether HB Talent Management (Phase 4) included AI Skills configuration. If yes: Tier 1 basis available. If no: Tier 2 platform capability statement. Could be combined with W4-AI-001 and W4-AI-003 into a single "Oracle HCM AI Capabilities" statement covering ODA, AI Skills, and Redwood UX. |
| **Estimated Priority** | Medium |

---

### W4-AI-003 — Oracle Redwood User Experience & Guided Journeys (OAX)

| Field | Value |
|---|---|
| **Capability Area** | Oracle Redwood UX — Oracle's modern responsive UI framework; Oracle Application Extension (OAX) / Experience Design Studio — low-code configuration of Oracle Fusion pages, guided journeys, personalisation |
| **Evidence Available** | Yes — confirmed in SAA BOM |
| **Evidence Source** | HIST-006 (SAA BOM — Redwood and OAX confirmed as in-scope HCM components); W3S1-008 notes referenced OAX capability |
| **Evidence Tier** | **Tier 2 — Platform Capability.** Redwood is the standard Oracle Fusion UX framework — all new implementations are Redwood by default. OAX is a configuration tool for Redwood. Whether APPSolve has delivered specific OAX customisations for clients requires BU Lead confirmation. |
| **Recommendation** | **Medium priority.** Redwood adoption is a tender differentiator showing Oracle HCM maturity. A short "Oracle Redwood & User Experience" section within an existing statement (e.g., W3S1-001) may be more efficient than a standalone statement. OAX (Experience Design Studio) is more specialist — extract only if APPSolve has specifically configured OAX for a client. |
| **Estimated Priority** | Medium (combine with existing HCM statements rather than standalone) |

---

### W4-AI-004 — Oracle Grow (Internal Talent Marketplace)

| Field | Value |
|---|---|
| **Capability Area** | Oracle Grow — internal talent marketplace; gig opportunities; learning recommendations; AI-powered career development within the organisation |
| **Evidence Available** | Unknown — not found in ORACLE_FACT_BASELINE or WAVE3_HCM_SOURCE_DISCOVERY_REPORT |
| **Evidence Source** | Not identified in current approved/registered sources |
| **Evidence Tier** | **Unknown — requires corpus search** |
| **Recommendation** | **Defer until evidence confirmed.** Oracle Grow is a newer Oracle Cloud HCM product (launched ~2022). Search HIST-006 (SAA RFP) and HIST-014 (CCBA) for "Grow" or "talent marketplace" references. If found, assess evidence tier. If not found in current sources, flag as evidence gap. **Do not extract without confirmed evidence.** |
| **Estimated Priority** | Low (pending evidence search) |

---

## Part C — Oracle Integration Capabilities

### W4-INT-001 — Oracle Integration Cloud (OIC) Accelerators & Integration Patterns

| Field | Value |
|---|---|
| **Capability Area** | Oracle OIC Integration Accelerators — pre-built integration recipes and templates for Oracle HCM, ERP, and third-party systems; OIC architecture patterns; integration monitoring and governance |
| **Evidence Available** | **Yes — strong Tier 1 evidence** |
| **Evidence Source** | HIST-018 (ANN1-V4.1 — Hollywood Bets contractual — OIC ↔ PaySpace bidirectional; production confirmed); ORACLE_FACT_BASELINE Section 7 ("OIC is mandatory in every Oracle Fusion implementation"); W3S1-009 (Oracle HCM Payroll Interface — OIC as the standard integration layer) |
| **Evidence Tier** | **Tier 1 — Confirmed Delivery.** OIC is the mandatory integration layer in every APPSolve Oracle Fusion implementation (ORACLE_FACT_BASELINE Section 7). Hollywood Bets (HIST-018) provides contractual Tier 1 evidence for OIC payroll integration. DFA (Rule 21.4) provides internal evidence for OIC broader suite integration. |
| **Distinction from Existing Content** | W3S1-009 covers OIC specifically in the payroll interface context. A dedicated OIC capability statement would position APPSolve as an OIC integration specialist across all integration patterns — not just payroll. This would cover: ERP-to-HCM integration, H2H BeBanking integration via OIC, third-party system connectors, real-time and batch integration patterns. |
| **Recommendation** | **High priority extraction candidate.** OIC is APPSolve's most broadly applicable Oracle technical capability — every Fusion implementation uses it. A dedicated "Oracle Integration Cloud (OIC) Capability" statement would differentiate APPSolve from implementation partners who rely on third-party middleware. Evidence basis is Tier 1 (Hollywood Bets contractual). Consider pairing with an "OIC Integration Accelerators" section covering payroll, BeBanking, and ERP integration patterns already delivered. |
| **Estimated Priority** | **High** |

---

### W4-INT-002 — Oracle Visual Builder Studio (VBS) — Custom Application Development

| Field | Value |
|---|---|
| **Capability Area** | Oracle Visual Builder Studio (VBS) — low-code application development platform on OCI; custom application extensions to Oracle Fusion; mobile app development; custom workflow portals |
| **Evidence Available** | Uncertain — not found in ORACLE_FACT_BASELINE; may be referenced in technical sections of HIST-006 or HIST-008 (RedPath RFI) |
| **Evidence Source** | Not identified in current reviewed sources. RedPath Mining RFI (HIST-008) may contain VBS references given the technical depth of that document. |
| **Evidence Tier** | **Unknown — requires corpus search** |
| **Recommendation** | **Low-medium priority.** VBS is a differentiator for technically advanced Oracle partners. Before extracting, confirm: (1) APPSolve has delivered VBS custom applications for any client; (2) evidence is in an approved HIST document. If confirmed, VBS + OIC + OAX combined could form a strong "Oracle Low-Code & Integration" capability statement. |
| **Estimated Priority** | Low-Medium (pending evidence search) |

---

## Part D — Oracle ERP Expansion Capabilities

### W4-ERP-001 — Oracle Fusion Finance (Expanded Coverage)

| Field | Value |
|---|---|
| **Capability Area** | Oracle Fusion Finance — GL, AR, AP, Fixed Assets, Cash Management, Tax (dedicated statement beyond current W2S1-001 platform overview) |
| **Evidence Available** | **Yes — Tier 1 evidence available** |
| **Evidence Source** | Cape Union Mart (Oracle Fusion Finance + Procurement — ORACLE_FACT_BASELINE Section 11); Investec (Fusion Finance 3 countries — SA, USA, UK); NALA Renewables (Fusion Finance 8 countries — multi-country EU deployment) |
| **Evidence Tier** | **Tier 1 — Multiple confirmed clients.** Cape Union Mart, Investec, and NALA Renewables are confirmed Fusion Finance clients. Multi-country deployment (Investec 3 countries; NALA 8 countries) is a strong differentiator. |
| **Distinction from Existing Content** | W2S1-001 (Oracle Fusion Capability Statement) covers Fusion broadly. A dedicated Oracle Fusion Finance statement would enable module-level quoting, IFRS compliance positioning, and multi-country Finance differentiation. This directly addresses tenders asking specifically for Oracle Fusion Finance implementation experience. |
| **Recommendation** | **High priority extraction candidate.** Multi-country Oracle Fusion Finance is a rare and high-value differentiator. Three confirmed Tier 1 clients with confirmed Finance scope. Pending reference letter registration (Cape Union Mart, Investec, NALA Renewables), this would become one of the strongest finance-sector Oracle capability statements in the KB. |
| **Estimated Priority** | **High** |

---

### W4-ERP-002 — Oracle Fusion Procurement (Dedicated Coverage)

| Field | Value |
|---|---|
| **Capability Area** | Oracle Fusion Procurement — Purchasing, Sourcing, Supplier Management, Self-Service Procurement |
| **Evidence Available** | Yes — Tier 1 evidence available |
| **Evidence Source** | Cape Union Mart (Oracle Fusion Finance + Procurement — ORACLE_FACT_BASELINE Section 11); Investec (Fusion Finance + Procurement) |
| **Evidence Tier** | **Tier 1 (Cape Union Mart, Investec confirmed)** |
| **Recommendation** | **Medium priority.** Could be combined with W4-ERP-001 into an "Oracle Fusion Finance & Procurement" capability statement covering both areas with the same client evidence base. |
| **Estimated Priority** | Medium (combine with W4-ERP-001) |

---

### W4-ERP-003 — Oracle Project Portfolio Management (PPM)

| Field | Value |
|---|---|
| **Capability Area** | Oracle PPM — project planning, task management, project accounting, resource management, project analytics |
| **Evidence Available** | Yes — Tier 1 (KPMG confirmed; DFA confirmed — internal only) |
| **Evidence Source** | ORACLE_FACT_BASELINE Section 4.3: "Oracle PPM | SABS ETS (DFA, KPMG)"; DFA (Rule 21.4 — internal only); KPMG (verify reference availability) |
| **Evidence Tier** | **Internal Evidence (DFA — Rule 21.4) + Potential Tier 1 (KPMG — verify reference).** If KPMG provides a reference letter, PPM becomes Tier 1 referenceable. Without KPMG reference, PPM is internal evidence only. |
| **Recommendation** | **Medium priority pending KPMG reference confirmation.** If KPMG reference available: extract as Tier 1 PPM capability statement — strong differentiator given KPMG multi-country EBS + PPM scope. If KPMG not available: Tier 2 exception approach (internal evidence only). |
| **Estimated Priority** | Medium (dependent on KPMG reference) |

---

### W4-ERP-004 — Oracle Fusion HCM — Oracle Payroll Cloud (Native)

| Field | Value |
|---|---|
| **Capability Area** | Oracle Payroll Cloud — native SA payroll processing, gross-to-net calculations, payslip generation, tax compliance, statutory reporting |
| **Evidence Available** | Yes — internal evidence only |
| **Evidence Source** | ORACLE_FACT_BASELINE Section 4.1: "Payroll Interface (3rd party integration) | ... exception: DFA uses Oracle Payroll Cloud native" |
| **Evidence Tier** | **Internal Evidence Only (DFA — Rule 21.4 permanent).** DFA is the only confirmed Oracle Payroll Cloud native client. Rule 21.4 prohibits naming DFA. Without a referenceable client, a native Oracle Payroll capability statement has no external evidence basis. |
| **Recommendation** | **Do NOT extract without a referenceable client.** APPSolve's standard model is OIC integration to third-party payroll (W3S1-009). A native Oracle Payroll Cloud statement would require: (1) a new client implementing Oracle Payroll Cloud native; (2) Rule 21.4 override for DFA — not recommended. Defer until a referenceable Oracle Payroll client exists. |
| **Estimated Priority** | **Low — blocked until referenceable client secured** |

---

## Wave 4 Candidate Priority Summary

| Priority | Candidate | ID | Evidence Tier | Key Evidence |
|---|---|---|---|---|
| **High** | Oracle Integration Cloud (OIC) Accelerators | W4-INT-001 | Tier 1 | HIST-018 (HB contractual); OIC mandatory in all Fusion implementations |
| **High** | Oracle Fusion Finance (Expanded) | W4-ERP-001 | Tier 1 | Cape Union Mart, Investec (multi-country), NALA Renewables |
| **High** | Oracle Time and Labour (Standalone) | W4-HCM-004 | Tier 1 | Mr Price Group (confirmed T&L — SABS ETS + ORACLE_FACT_BASELINE) |
| **Medium** | Oracle Journeys / Guided Journeys | W4-HCM-002 | Tier 2 (pending HB confirmation) | HIST-006, HIST-014; possible Tier 1 if HB scope confirmed |
| **Medium** | Oracle AI-Based Skills Intelligence | W4-AI-002 | Tier 2 (pending HB Phase 4 confirmation) | ORACLE_FACT_BASELINE Section 4.1 |
| **Medium** | Oracle Digital Assistant (ODA) | W4-AI-001 | Tier 2 | HIST-006 (SAA BOM) |
| **Medium** | Oracle Fusion Procurement | W4-ERP-002 | Tier 1 | Cape Union Mart, Investec — combine with W4-ERP-001 |
| **Medium** | Oracle PPM | W4-ERP-003 | Internal + Tier 1 pending | DFA (internal); KPMG (verify reference) |
| **Low-Medium** | Oracle Workforce Directory & Modelling | W4-HCM-003 | Tier 2 | HIST-006 only — consider extending W3S1-001 instead |
| **Low-Medium** | Oracle Redwood UX / OAX | W4-AI-003 | Tier 2 | HIST-006 (SAA BOM) — consider embedding in existing statements |
| **Low-Medium** | Oracle VBS Custom Applications | W4-INT-002 | Unknown | Requires corpus search in HIST-006 or HIST-008 |
| **Low** | Oracle Benefits Administration | W4-HCM-001 | Tier 3 | HIST-006 only; no confirmed delivery |
| **Low** | Oracle Work Life Solutions | W4-HCM-005 | Tier 3 | HIST-006 only; single source; niche requirement |
| **Low** | Oracle Grow (Talent Marketplace) | W4-AI-004 | Unknown | Not found in reviewed sources; defer |
| **Blocked** | Oracle Payroll Cloud (Native) | W4-ERP-004 | Internal Only | DFA (Rule 21.4 permanent); no referenceable client |

---

## Wave 4 Execution Sequencing Recommendation

**Wave 4A — High Priority (can begin without new source documents):**
1. W4-INT-001 — Oracle OIC Integration Accelerators (Tier 1 basis in HIST-018)
2. W4-ERP-001 + W4-ERP-002 — Oracle Fusion Finance & Procurement combined (Tier 1 basis in existing fact baseline)
3. W4-HCM-004 — Oracle Time and Labour dedicated statement (Tier 1 basis in Mr Price SABS ETS)

**Wave 4B — Medium Priority (BU Lead confirmation required first):**
4. W4-HCM-002 — Oracle Journeys (BU Lead to confirm HB Phase 1 Journeys scope)
5. W4-AI-002 — Oracle AI Skills (BU Lead to confirm HB Phase 4 AI Skills scope)
6. W4-ERP-003 — Oracle PPM (dependent on KPMG reference letter confirmation)

**Wave 4C — Research Required (corpus search needed before scoping):**
7. W4-AI-001 — Oracle Digital Assistant (read HIST-006 Section 2 for ODA depth)
8. W4-AI-003 — Oracle Redwood / OAX (read HIST-006 BOM section)
9. W4-INT-002 — Oracle VBS (search HIST-006 and HIST-008 for VBS references)
10. W4-AI-004 — Oracle Grow (search HIST-006 and HIST-014 for "Grow" or "talent marketplace")

**Deferred indefinitely:**
- W4-HCM-001 (Benefits), W4-HCM-005 (Work Life), W4-ERP-004 (Oracle Payroll Cloud native) — insufficient or restricted evidence

---

*WAVE4_DISCOVERY_REPORT.md v1.0 — Created 2026-06-14 — Hein Blignaut (BU Lead)*
*Pre-extraction prerequisite: BU Lead authorisation per candidate. Do not begin extraction until authorisation is granted and HIST registration is confirmed for any source documents to be used.*
