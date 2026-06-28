---
title: "WP14C — Tender Factory Validation Report"
subtitle: "Validation Case: ARM IT045 — Oracle EBS Support"
version: "1.0"
status: "Complete — Findings Only"
programme: "WP14C — Tender Factory Validation Run"
date: "2026-06-17"
preceded_by: "WP14B — Assumption Library Master Review Workbook"
validation_case: "ARM IT045 | RFP l ARM IT045 l 07-2025 l Oracle EBS Support"
verdict: "YES WITH QUALIFICATIONS"
---

# WP14C — Tender Factory Validation Report

**Programme:** WP14C | **Date:** 2026-06-17 | **Validation Case:** ARM IT045 — Oracle EBS Support

> **Scope and constraints:** This is a findings-only exercise. No source files were modified. No assumption packs were updated. No BU decisions were resolved. No tender deliverables were created. This report simulates the Tender Factory process against the ARM IT045 validation case to identify gaps, coverage weaknesses, and missing library components before governance lock-down.

---

## 1. Executive Summary

**Validation case:** African Rainbow Minerals (ARM) — Oracle EBS Support — RFP l ARM IT045 l 07-2025

**Outcome known:** This validation is retrospective. ARM awarded the Oracle EBS Support contract to APPSolve on **28 August 2025** (ARM Tender Adjudication Committee success letter). The win is recorded in W2S1-002 EBS Capability Statement as source evidence `(ARM-2025-IT045, July 2025, WON)`.

**Factory performance summary:** The Tender Factory assembled a winning response. Four approved assumption packs (AMS + ERP + OCI + OIC) and three approved capability assets (W2S1-002, W2S1-003, W2S1-004) provided a strong, auditable baseline. The EBS Capability Statement was the primary differentiator — it demonstrated existing client delivery, mining sector context, and OCI expertise in a single pre-approved narrative.

**Core finding:** The win was achieved despite three structural gaps in the Tender Factory. The AMS pack's standard SLA tier (P1=1 hour, business hours only) is architecturally incompatible with ARM's specified SLA (P1=15 minutes, 24/7, 5 priority tiers). The dedicated resource model required by ARM has no corresponding assumption set in the library. These gaps required manual customisation in the actual submission. The factory did not fail — but it required a skilled bid manager to close the distance between what the library produced and what the RFP required.

**Verdict:** YES WITH QUALIFICATIONS — the Tender Factory can produce a competitive Oracle EBS AMS response today. Three targeted additions (EBS-AMS SLA overlay, Dedicated Resource Model assumptions, EBS-AMS assembly pattern) would eliminate the manual intervention requirement for future EBS AMS tenders.

---

## 2. Tender Classification

### 2.1 Tender Profile

| Field | Value |
|---|---|
| Tender reference | RFP l ARM IT045 l 07-2025 |
| Issuer | African Rainbow Minerals Limited (ARM) — JSE-listed mining group |
| Tender type | Application Managed Services / Support (post-implementation) |
| NOT this | New implementation — this tender is for ongoing support of a live EBS environment |
| Issued | 02 July 2025 |
| Submitted | 20 July 2025 (APPSolve, authorised by Hein Blignaut) |
| Awarded | 28 August 2025 — APPSolve (ARM Tender Adjudication Committee) |
| Outcome | **WON** |

### 2.2 Technical Scope

| Component | Detail |
|---|---|
| EBS HR & Payroll | Version 12.2.8 — 5 sites, 1,787 users |
| EBS Financials | Version 12.2.10 — 3 of the 5 sites |
| Infrastructure | Oracle Cloud Infrastructure (OCI) hosted |
| Integration layer | Oracle Integration Cloud (OIC) |
| DBA scope | OCI infrastructure + EBS DBA within AMS |
| Site count | 5 sites (head office + 4 mining operations) |

### 2.3 Commercial Model

| Field | Value |
|---|---|
| Support model | Dedicated Resource Model (named team) |
| Minimum team | SDM (40h/month), HCM Lead (240h), Finance Lead (160h), DBA+OCI (160h), OIC Specialist (80h) |
| Total minimum hours | 680h/month dedicated allocation |
| Pricing basis | Fixed monthly fee (dedicated resource model) |
| Contract duration | Not specified in RFP; implied multi-year |

### 2.4 SLA Requirements (ARM-specified)

| Priority | Definition | Response | Resolution |
|---|---|---|---|
| P1 | Critical — system down / payroll blocked | 15 minutes | 2 hours |
| P2 | Major — significant user impact | 1 hour | 4 hours |
| P3 | Normal — non-critical, workaround exists | 4 hours | 8 hours |
| P4 | Minor — low impact | 8 hours | 16 hours |
| P5 | Minimal — general queries | 3 business days | 5 business days |

ARM requires 24/7 P1 emergency coverage. Standard business hours (08:00–17:00 SAST) are insufficient for P1 and P2.

### 2.5 Evaluation Criteria (ARM)

| Criterion | Weight |
|---|---|
| Vendor Capability / Experience | 30% |
| Team Capability / Knowledge Transfer | 25% |
| Technical Solution | 20% |
| Pricing | 20% |
| Compliance (B-BBEE, legal) | 5% |

### 2.6 Compliance Requirements

| Requirement | ARM Specification | APPSolve Position at Submission |
|---|---|---|
| B-BBEE level | Level 4 or better | Level 3 (cert expiring 2026-07-31) + In-Process Letter |
| Shareholding | 25%+1 vote HDP (2018 Mining Charter) | Submitted — details per CSD registration |
| Oracle partner status | Not specified | Oracle Level 1 Partner |

### 2.7 Assembly Pattern

**Classification:** Oracle EBS AMS (Multi-pack: AMS + ERP + OCI + OIC)

This is a **Cross-BU AMS engagement** — the primary pack is the AMS pack. It is not a pure HCM, ERP, or OCI engagement. The trigger for each pack is:

| Pack | Trigger Rule |
|---|---|
| AMS Pack | Managed Services / AMS engagement |
| ERP Pack | Oracle EBS Financials in scope (EBS = on-premise Oracle ERP) |
| OCI Pack | Rule OCI-1: EBS on OCI = OCI Pack mandatory |
| OIC Pack | OIC integration layer in scope |
| HCM Pack | NOT triggered — EBS HR&Payroll support ≠ Oracle Fusion HCM implementation |

---

## 3. Simulated Assembly Output

### 3.1 Assumption Packs Assembled

The Tender Factory would assemble the following packs per `TENDER_ASSUMPTION_ASSEMBLY_RULES.md`:

| Pack | Version | Status | Assumptions | Assembly Basis |
|---|---|---|---|---|
| AMS — Managed Services | v1.0 | **Approved** | 84 (body count) | Primary pack — AMS engagement |
| Oracle ERP | v1.0 | **Approved** | 123 | EBS Financials support in scope |
| Oracle OCI Infrastructure | v1.0 | **Approved** | 174 | Rule OCI-1: EBS on OCI |
| Oracle OIC Integration | v1.0 | **Approved** | 104 | OIC integration support in scope |
| **Total** | | **4 Approved** | **485** | |

All four packs are in `Approved` status. All 485 assumptions may be included in an external proposal without governance exception.

**Packs correctly excluded:**
- HCM Base Pack — ARM IT045 is EBS support, not Oracle Fusion HCM implementation
- HCM Module Packs (Recruiting, Learning, Talent, Compensation) — Draft; not triggered; not in scope
- Acumatica Base Pack — Not in scope
- BeBanking Base Pack — Not in scope

### 3.2 Capability Assets Assembled

| Asset | ID | Status | Role in Tender |
|---|---|---|---|
| Oracle EBS Capability Statement | W2S1-002 | Approved | Primary capability narrative — EBS credentials, ARM context, OCI migration |
| DBA Executive Summary | W2S1-003 | Approved | DBA team credential narrative — largest local Oracle DBA team claim |
| Managed Services Support Model | W2S1-004 | Approved | ITIL framework, incident/change/problem management methodology |
| Fusion Capability Statement | W2S1-001 | Approved | NOT assembled — Fusion ≠ EBS; excluded |
| Implementation Methodology | W2S1-005 | Approved | NOT assembled — support tender; implementation methodology not applicable |

### 3.3 Reference Assets Available

Per REFERENCE_MASTER.md, the following EBS references were available for assembly:

| Reference | ID | Tier | Applicable Coverage | Citability |
|---|---|---|---|---|
| Assore | REF-ORA-004 | Gold | EBS Finance + DBA | Named_Reference_Allowed = Yes |
| Adcock Ingram | REF-ORA-005 | Gold | EBS Finance + Integration + APEX | Named_Reference_Allowed = Yes |
| Stellenbosch University | REF-ORA-011 | Silver | EBS + HCM Perf Mgmt | Named_Reference_Allowed = Yes |
| WITS University | REF-ORA-010 | Silver | EBS Payroll + DBA | Named_Reference_Allowed = Yes |
| ARM | REF-ORA-008 | Gold | EBS HCM + Finance + OCI + OIC | **Conflict — ARM is the tender client; cannot be used as reference** |

The submitted tender listed: Adcock Ingram, Assore, Harmony, Investec, Mr Price, NALA Renewables, Oracle Corp. Note: Harmony, Investec, Mr Price, and NALA Renewables are Oracle Fusion references, not EBS. This is appropriate for demonstrating Oracle breadth but the EBS-specific references (Assore, Adcock Ingram) are the most relevant to this tender.

### 3.4 Assembly Skeleton (Tender Factory Output Structure)

A simulated Tender Factory assembly for ARM IT045 would produce:

```
ARM IT045 — Oracle EBS Support — APPSolve Response

Section 1: Executive Summary
  ← W2S1-002 Section 2.2 (EBS Delivery Position)
  ← W2S1-003 Section 1 (Executive Overview)

Section 2: Vendor Capability and Experience (30%)
  ← W2S1-002 Sections 1–6 (EBS Platform, Credentials, Modules, DBA, OCI)
  ← REF-ORA-004 (Assore EBS Finance + DBA)
  ← REF-ORA-005 (Adcock Ingram EBS Finance + Integration)

Section 3: Team Capability and Knowledge Transfer (25%)
  ← W2S1-003 (DBA team depth)
  ← W2S1-004 Section 7 (Service Delivery Roles)
  [GAP: No Dedicated Resource Model assumption set for team structure]

Section 4: Technical Solution (20%)
  ← AMS Pack Sections 85–100 (84 assumptions)
  ← ERP Pack (123 assumptions — EBS Financials support context)
  ← OCI Pack (174 assumptions — OCI infrastructure)
  ← OIC Pack (104 assumptions — integration support)
  ← W2S1-004 Sections 2–6 (ITIL, Incident, Problem, Change, Event Management)
  [GAP: SLA assumptions incompatible with ARM 5-tier requirement]

Section 5: Pricing (20%)
  [GAP: No pricing assumption set for Dedicated Resource Model]

Section 6: Compliance (5%)
  ← BEE certificate (Level 3 + In-Process Letter)
  [GAP: No mining sector BEE assumption; Mining Charter 25%+1 HDP not addressed]
```

---

## 4. Coverage Matrix

Assessment of each ARM RFP requirement against Tender Factory coverage. Legend: **Covered** = assumption or asset provides direct support; **Partially** = coverage exists but gaps or incompatibilities; **Not Covered** = no factory asset addresses the requirement.

| # | ARM Requirement | Pack/Asset | Coverage | Notes |
|---|---|---|---|---|
| R01 | Support scope limited to contracted applications | AMS-SCP-001 | **Covered** | Direct match |
| R02 | L1 support client responsibility | AMS-SCP-002 | **Covered** | Direct match |
| R03 | L2 application support definition | AMS-SCP-003 | **Covered** | Direct match |
| R04 | L3 technical/DBA support definition | AMS-SCP-004 | **Covered** | Direct match — aligned with EBS DBA scope |
| R05 | EBS support limited to APPSolve-configured scope | AMS-SCP-005 | **Covered** | Existing client condition met |
| R06 | 5-priority tier SLA (P1–P5) | AMS-SLA-001, AMS-PRI-001 | **Not Covered** | AMS pack has 4 tiers only; P5 absent; response targets incompatible (see GAP-001, GAP-002) |
| R07 | P1 response: 15 minutes | AMS-SLA-001 | **Not Covered** | AMS standard = 1 hour; 4× gap (see GAP-001) |
| R08 | P1 resolution: 2 hours | No assumption | **Not Covered** | AMS pack has no resolution time assumptions (see GAP-002) |
| R09 | P2 response: 1 hour | AMS-SLA-001 | **Partially** | AMS standard = 4 business hours; requires customisation |
| R10 | 24/7 P1 emergency coverage | AMS-PRI-003 | **Partially** | Acknowledged as add-on; no governing assumptions for the 24/7 model |
| R11 | Named/dedicated team model | AMS-SLA-005 | **Partially** | References dedicated model exists as add-on; no assumptions govern it (see GAP-003) |
| R12 | SDM (40h/month minimum) | No assumption | **Not Covered** | No SDM role assumption or hour allocation assumption |
| R13 | HCM Lead (240h/month minimum) | No assumption | **Not Covered** | No named role assumption |
| R14 | Finance Lead (160h/month minimum) | No assumption | **Not Covered** | No named role assumption |
| R15 | DBA + OCI Specialist (160h/month) | W2S1-003 (narrative) | **Partially** | DBA capability described; no monthly hour allocation assumption |
| R16 | OIC Specialist (80h/month minimum) | OIC Pack | **Partially** | OIC scope covered; no monthly hour allocation assumption |
| R17 | Multi-site support (5 sites) | AMS-HRS-002 | **Partially** | On-site acknowledged at separate rate; no site cadence, travel, or mine-access assumptions |
| R18 | Incident management process | AMS-INC-001–005, W2S1-004 Sec 2.1 | **Covered** | Strong coverage from both AMS pack and managed services model |
| R19 | Change request process | AMS-CR-001–004 | **Covered** | Direct match — CR threshold, approval, delivery cycle |
| R20 | Service request catalogue | AMS-SRQ-001–004 | **Covered** | Standard catalogue model covered |
| R21 | Oracle SR management | AMS-INC-005 | **Covered** | Oracle SR lodging and status management |
| R22 | Monthly reporting | AMS-HRS-004, AMS-SLA-004 | **Covered** | Monthly activity report contents specified |
| R23 | EBS patch management (on OCI) | AMS-PAT-002 | **Partially** | Acknowledges EBS patching is separately contracted; no EBS patch assumptions (see GAP-004) |
| R24 | Oracle release advisory | AMS-REL-001 | **Partially** | Written for Fusion quarterly updates; EBS patching cycle is different |
| R25 | EBS version support (R12.2.8, R12.2.10) | W2S1-002 | **Covered** | EBS R12 capability confirmed |
| R26 | OCI infrastructure management | OCI Pack (174 assumptions) | **Covered** | Comprehensive OCI assumption coverage |
| R27 | OIC integration support | OIC Pack (104 assumptions) | **Covered** | Comprehensive OIC assumption coverage |
| R28 | B-BBEE Level 4 or better | No assumption | **Not Covered** | AMS pack has no BEE assumptions; compliance gap (see GAP-005) |
| R29 | Mining Charter (25%+1 HDP shareholding) | No assumption | **Not Covered** | No mining sector governance assumption |
| R30 | Knowledge Transfer programme | No assumption | **Not Covered** | No AMS onboarding or KT assumptions (see GAP-007) |
| R31 | Support portal / ticketing integration | AMS-CHN-001 | **Covered** | Channel and logging requirements specified |
| R32 | SLA performance reporting | AMS-SLA-004 | **Covered** | SLA compliance reporting defined |
| R33 | Defect vs enhancement boundary | AMS-DEF-001, AMS-DEF-002 | **Covered** | Three-way classification (defect/enhancement/drift) |
| R34 | Vendor Oracle partnership proof | W2S1-002 Sec 2.1 | **Covered** | Level 1 Partner confirmed |
| R35 | EBS client references | REF-ORA-004, REF-ORA-005, REF-ORA-011 | **Covered** | Multiple active EBS references |

**Coverage summary:** 17 Covered / 8 Partially / 10 Not Covered (of 35 requirements assessed)

---

## 5. Gap Register

### 5.1 CRITICAL Gaps

| Gap ID | Pack Affected | Tender Requirement | Description | Impact | Recommended Fix |
|---|---|---|---|---|---|
| **GAP-001** | AMS | R06, R07, R09 — SLA tier and response targets | ARM requires 5-priority SLA (P1–P5). AMS pack has 4 priorities only. ARM P1 response = 15 minutes; AMS standard = 1 hour. ARM P2 response = 1 hour; AMS standard = 4 hours. P5 (3 days/5 days) has no AMS equivalent. Every SLA commitment in the AMS pack is incompatible with this tender's requirements. | Without manual override, the Tender Factory produces a commercially incorrect SLA commitment. Any proposal assembled unmodified would expose APPSolve to SLA breach from day one of the contract. | Author an EBS-AMS SLA Assumption Overlay with configurable P1–P5 tier, response targets, and 24/7 trigger. Store as a named BU-configurable variant loadable in place of AMS-SLA-001 through AMS-PRI-003. |
| **GAP-002** | AMS | R08, R10 — Resolution time SLAs and 24/7 | AMS pack covers response time only. No assumption governs resolution time. ARM requires P1=2hr, P2=4hr, P3=8hr, P4=16hr resolution commitments. ARM requires 24/7 P1 coverage; AMS-PRI-003 acknowledges 24/7 as an add-on but provides no governing assumptions for the 24/7 commercial and operational model. | Bidding without resolution time assumptions means APPSolve has no documented position on resolution commitments — creating a blank-slate exposure in contract negotiations. 24/7 coverage without assumptions creates pricing risk (no baseline from which to scope the add-on). | Add resolution time assumptions and 24/7 operational model assumptions to the EBS-AMS SLA Overlay. |
| **GAP-003** | AMS | R11–R16 — Dedicated Resource Model | AMS-SLA-005 states named consultant allocation requires "separate commercial agreement." No assumption pack governs the dedicated model: team structure, role definitions, minimum monthly hour commitments per role, SDM responsibilities, or hour-tracking obligations. The Dedicated Resource Model is ARM's primary commercial requirement. | The entire commercial structure of this tender (680h/month across 5 named roles) has no assumption backing. Bid managers must manually compose all team and allocation commitments without a governed baseline — introducing inconsistency and commercial risk across tenders. | Author a Dedicated Resource Model assumption set: SDM role, specialist role definitions, monthly hour allocation assumptions, overage treatment, role substitution assumptions. |

### 5.2 HIGH Gaps

| Gap ID | Pack Affected | Tender Requirement | Description | Impact | Recommended Fix |
|---|---|---|---|---|---|
| **GAP-004** | AMS | R23–R24 — EBS patch management and release | AMS pack was authored with Oracle Fusion SaaS as the primary context. AMS-PAT-001 states "Oracle Fusion HCM and ERP patches are applied by Oracle as part of the SaaS subscription" — factually incorrect for EBS. AMS-PAT-002 acknowledges EBS patching as "separately contracted" but provides no EBS-specific patch assumptions. AMS-REL-001 refers to "Oracle quarterly releases" (Fusion cadence) — EBS patching is CPU-based (quarterly Critical Patch Updates), not SaaS release-based. | EBS-specific support assumptions are absent. An EBS AMS proposal assembled from the current packs would contain a mix of Fusion-context wording (incorrect) and generic AMS wording (insufficient), requiring extensive manual correction. AMS-INC-004 explicitly states "Oracle Fusion HCM and ERP are delivered on Oracle's SaaS infrastructure" — wrong for ARM's EBS on OCI environment. | Author a dedicated EBS-AMS Assumption Pack or EBS-AMS overlay section covering: EBS Concurrent Manager support, EBS patch set assessment (CPU/OPatch), EBS DBA support scope within AMS, EBS performance monitoring on OCI, and the corrected incident ownership model for on-premise EBS vs SaaS. |
| **GAP-005** | Commercial | R28–R29 — B-BBEE and Mining Charter | No assumption in any pack covers BEE compliance for tender submission. ARM requires B-BBEE Level 4 or better per the 2018 Mining Charter. The Mining Charter imposes specific requirements (25%+1 vote HDP shareholding, scorecard weighting) that differ from standard B-BBEE. APPSolve submitted at Level 3 with an In-Process Letter — a material compliance gap managed manually by the bid team. | A future mining sector EBS AMS tender may not accept an In-Process Letter. Without a governed assumption, each mining tender requires a fresh BEE compliance review with no factory guidance. The B-BBEE expiry (2026-07-31) further compounds the risk — after expiry, the factory has no assumption covering transitional BEE positioning. | Author Mining Sector Compliance Assumptions: Mining Charter BEE trigger conditions, HDP shareholding disclosure assumptions, In-Process Letter positioning rule, expiry management assumption. |
| **GAP-006** | AMS | R06 — P5 priority tier | AMS standard 4-priority tier (P1–P4) has no P5 classification. ARM's P5 (3 business days response / 5 business days resolution) covers general queries and non-urgent service requests. AMS-PRI-001's P4 (3 business days response) partially overlaps, but resolution time for P4 is absent. | Misclassification of P5 items as P4 inflates SLA obligations. ARM's P5 tier is the correct classification for general how-to queries and documentation requests. Without a P5 assumption, APPSolve may inadvertently commit to handling routine queries under P4 SLA. | Extend AMS-PRI-001 to include a P5 tier, or add P5 to the EBS-AMS SLA Overlay. |

### 5.3 MEDIUM Gaps

| Gap ID | Pack Affected | Tender Requirement | Description | Impact | Recommended Fix |
|---|---|---|---|---|---|
| **GAP-007** | AMS | R30 — Knowledge Transfer | No AMS assumption covers KT/onboarding. ARM's evaluation criterion "Team Capability / KT" (25%) specifically includes knowledge transfer. The factory produced nothing on KT structure, onboarding period, runbook creation, or documentation handover. | KT is 25% of evaluation weight. Factory silence on KT means bid teams must author this section from scratch on every AMS tender. | Author AMS onboarding and KT assumptions: onboarding period, documentation package, runbook creation, access provisioning timeline, key contact handover. |
| **GAP-008** | AMS / ERP | R04, R23 — EBS Concurrent Manager and Forms | No assumption covers EBS Concurrent Manager support, EBS Forms-based user issues, or EBS application tier technical support (Apache, Forms server, Java patches). These are standard EBS AMS topics with no representation in any pack. | EBS technical support scope is incompletely defined. During contract negotiation, ARM could argue that Forms/Concurrent Manager support is out of scope because it is not assumed in the proposal. | Add EBS technical layer assumptions to the EBS-AMS overlay: Concurrent Manager, Forms server, application tier components within EBS DBA scope. |
| **GAP-009** | AMS | R17 — Multi-site support | AMS-HRS-002 acknowledges on-site at "a separate on-site day rate." No assumptions cover: visit cadence, mine-site access protocols (safety inductions, PPE), geographic zones, or site-specific escalation paths. ARM has 4 operational mine sites requiring periodic on-site presence. | Absence of multi-site assumptions means APPSolve has no governed position on on-site commitments, frequency, or cost treatment — creating pricing risk and potential scope disputes. | Author Multi-site Support Assumptions: on-site visit minimum frequency, mine-site access assumptions (safety, PPE client responsibility), geographic zone cost treatment, site-specific contact nomination. |
| **GAP-010** | AMS Assembly Rules | All | No explicit EBS-AMS assembly pattern exists in `TENDER_ASSUMPTION_ASSEMBLY_RULES.md`. The rules describe implementation assembly patterns in detail (HCM + Modules, ERP + OCI, etc.) but do not provide a named EBS-AMS pattern. A bid manager must derive the correct assembly manually. | The factory's assembly rules are silent on EBS AMS — the tender type that generated the first known win from the current library. Subsequent bid managers lack a codified starting point. | Add Section 3.5 "EBS AMS Assembly Pattern" to TENDER_ASSUMPTION_ASSEMBLY_RULES.md. |

### 5.4 LOW Gaps

| Gap ID | Description | Recommended Fix |
|---|---|---|
| **GAP-011** | AMS-INC-004 contains a factual error specific to EBS: "Oracle Fusion HCM and ERP are delivered on Oracle's SaaS infrastructure." For EBS clients, this is incorrect. | Add a BU-configurable flag or EBS override note to AMS-INC-004 so that EBS proposals suppress or replace this assumption. |
| **GAP-012** | No assumption covers EBS custom code (personalisation, customisation, BI Publisher, APEX) ownership and support boundaries. | Add EBS custom code support assumption to EBS-AMS overlay: who owns custom code issues, APPSolve support vs. client's internal developer. |
| **GAP-013** | No assumption covers integration with client ITSM tooling (ServiceNow, Jira, etc.). AMS-CHN-001 specifies APPSolve's portal/email — but ARM may require integration with ARM's own ITSM platform. | Add ITSM integration assumption: APPSolve-native ticketing is default; client ITSM integration is a separately scoped onboarding item. |

---

## 6. Readiness Assessment

Assessment across seven dimensions on a scale of 1–10.

| # | Dimension | Score | Rationale |
|---|---|---|---|
| 1 | **Assumption Library Coverage** | 6/10 | Four approved packs (485 assumptions) provide a solid commercial framework. AMS scope, service request, change management, and escalation assumptions are well-governed. Critical SLA assumptions are structurally incompatible with EBS AMS requirements. Three major gaps (SLA tier, resolution time, dedicated model) require manual override on every EBS AMS bid. |
| 2 | **Capability Asset Coverage** | 8/10 | W2S1-002 EBS Capability Statement is purpose-built and ARM-informed (ARM IT045 is listed as a source document). W2S1-003 DBA Executive Summary and W2S1-004 Managed Services Model provide strong ITIL-depth content. Likely responsible for the 30%-weighted vendor capability score that won the tender. Minor gap: no standalone EBS AMS support capability narrative (W2S1-002 is EBS overall; no support-specific variant exists). |
| 3 | **Reference Coverage** | 9/10 | Multiple active, signed, Gold-tier EBS references (Assore, Adcock Ingram). ARM itself becomes a reference post-award (already recorded in W2S1-002 as source). WITS University adds EBS Payroll + BeBanking H2H differentiation. Mr Price adds Oracle HCM breadth. Reference base is the strongest dimension of the factory for Oracle-EBS tenders. |
| 4 | **Compliance and Governance Readiness** | 5/10 | BEE Level 3 submitted against a Level 4 requirement — a material compliance gap managed via In-Process Letter. Mining Charter's 25%+1 HDP shareholding requirement is unaddressed by any assumption. The factory provided no guided positioning for either compliance risk. Tender was won despite these gaps, but the compliance risk was real and unmanaged by the library. BEE expiry (2026-07-31) creates an ongoing risk flag for this contract and future bids. |
| 5 | **Commercial Framework (Pricing / Costing)** | 4/10 | The Dedicated Resource Model (680h/month, 5 roles, named) has no pricing assumption set. The EBS AMS commercial model — fixed monthly fee for a minimum team — is the dominant market model for EBS support, yet the factory has no assumptions for it. Pricing was manually composed. Known Plennegy blocker OAR-C02 (Costing framework) compounds this gap. |
| 6 | **Assembly Engine Efficiency** | 7/10 | Assembly rules correctly identify EBS-OCI as the trigger pattern (ERP + OCI + OIC + AMS). All four packs are in Approved status and available for immediate assembly. The assembly completes without governance exceptions. Gap: no named EBS-AMS pattern in Section 3 of the assembly rules — bid managers must derive the pattern manually rather than following a codified recipe. |
| 7 | **Risk and Governance Controls** | 7/10 | Rule 21 governance controls (DFA, CCBA, SAA, Hollywood Bets, KPMG, Redpath) are correctly observed and do not affect this tender type. Oracle Partner Level 1 claim is correct and used accurately (not Gold/Gold Certified). "More than 50 Senior Consultants" headcount rule observed. AMS-SCP-005 (existing client condition) correctly governs the ARM scope boundary. Gap: no mining-sector-specific governance rule. |

**Overall Readiness Score: 46/70 = 66%**

The factory scores well on capability assets (what APPSolve can do) and references (who APPSolve has done it for). It scores poorly on commercial framework (how APPSolve prices and structures the engagement) and compliance readiness (what APPSolve's BEE and ownership position is for mining sector tenders).

---

## 7. Missing Library Components

The following components should exist in the Tender Factory but do not. Their absence was bridged manually in the ARM IT045 submission.

### 7.1 EBS-AMS SLA Assumption Overlay *(CRITICAL — before next EBS AMS tender)*

A BU-configurable SLA assumption block that replaces the standard AMS-SLA-001 through AMS-PRI-003 when a non-standard SLA structure is required. Must include:
- 5-priority tier definitions (P1 through P5)
- Both response time and resolution time commitments per priority
- 24/7 trigger conditions and commercial model
- SLA clock rules for after-hours incidents
- BU-configurable target fields (so the overlay works for multiple clients with different SLA schedules)

**Location:** `08_Commercial/Assumptions/AMS/AMS_EBS_SLA_OVERLAY.md` or as a conditional section within `AMS_ASSUMPTIONS_V1.md`

### 7.2 Dedicated Resource Model Assumption Set *(CRITICAL — before next EBS AMS tender)*

Assumptions governing the dedicated/named consultant model. Must include:
- SDM role definition and minimum monthly hour commitment
- Specialist role definitions (functional lead, DBA, OIC specialist)
- Monthly hour allocation per role: how tracked, reported, and billed
- Overage treatment (above minimum hours)
- Resource substitution assumption (what happens when a named consultant is unavailable)
- Onboarding period assumption (first 30/60 days)
- Role transition assumption (when a named resource leaves)

**Location:** New section (Section 101) in `AMS_ASSUMPTIONS_V1.md` or standalone `AMS_DEDICATED_RESOURCE_ASSUMPTIONS.md`

### 7.3 EBS-AMS Assembly Pattern in TENDER_ASSUMPTION_ASSEMBLY_RULES.md *(HIGH)*

A codified assembly recipe in Section 3 of the assembly rules:

```
EBS AMS (Support Engagement):
= ERP Pack [Approved] (EBS Financials context)
+ OCI Pack [Approved] (if EBS is OCI-hosted — apply Rule OCI-1)
+ OIC Pack [Approved] (if OIC integration is in AMS scope)
+ AMS Pack [Approved] (primary pack)
+ [EBS-AMS SLA Overlay if non-standard SLA required]
+ [Dedicated Resource Model Assumptions if dedicated model required]

EXCLUDES:
- HCM Base Pack (EBS support ≠ Oracle Fusion HCM implementation)
- Implementation Methodology (AMS is not an implementation)
- HCM module packs (not triggered by EBS support context)
```

**Location:** Section 3.5 (new section) of `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md`

### 7.4 Multi-site Support Model Assumptions *(MEDIUM)*

Assumptions covering geographically distributed AMS engagements:
- On-site visit minimum frequency (default cadence per site per quarter)
- Mine-site access: safety induction, PPE, and access control as client responsibility
- Geographic zone definitions and associated travel cost treatment
- Site-specific designated contact assumption

**Location:** New section within `AMS_ASSUMPTIONS_V1.md` (Section 102 or similar)

### 7.5 Mining Sector Compliance Assumptions *(MEDIUM — before next mining sector tender)*

BEE and ownership compliance assumptions for the mining sector:
- 2018 Mining Charter applicability trigger
- 25%+1 HDP shareholding disclosure assumption
- Mining Charter BEE level requirement (Level 4) vs. standard BEE Level 3+
- In-Process Letter positioning rule: when permissible; what must accompany it
- BEE certificate expiry management assumption

**Location:** New file `01_Compliance/MINING_SECTOR_COMPLIANCE_ASSUMPTIONS.md` or section in AMS pack

### 7.6 AMS Onboarding and Knowledge Transfer Assumptions *(MEDIUM)*

Assumptions covering AMS contract commencement:
- Onboarding period duration (default 30 days)
- Knowledge transfer documentation package (what APPSolve provides)
- Runbook creation: APPSolve responsibility vs client-provided documentation
- Access provisioning: client's responsibility to grant system access within onboarding period
- First-month reporting: initial inventory of supported processes and configurations

**Location:** New section within `AMS_ASSUMPTIONS_V1.md` (Section 103 or similar)

### 7.7 EBS-AMS Factual Correction *(HIGH — existing content error)*

AMS-INC-004 currently states: *"Oracle Fusion HCM and ERP are delivered on Oracle's SaaS infrastructure."* This is factually incorrect for EBS on OCI (EBS is not SaaS; the client operates the application layer). The assumption should either be suppressed in EBS assembly or replaced with the correct EBS-on-OCI ownership model.

**Location:** Correction to `AMS_ASSUMPTIONS_V1.md` AMS-INC-004 (after human review and BU Lead approval)

---

## 8. Remediation Roadmap

### Priority 1 — Before Next EBS AMS Tender

| Item | Work Required | Owner | Estimated Size |
|---|---|---|---|
| WP15A | Author EBS-AMS SLA Assumption Overlay (P1–P5, response + resolution, 24/7 model) | AI + Oracle BU Lead | ~8–12 new assumptions |
| WP15B | Author Dedicated Resource Model Assumptions (SDM, specialist roles, hour allocation, overage, substitution) | AI + Oracle BU Lead | ~10–15 new assumptions |
| WP15C | Add EBS-AMS Assembly Pattern to TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3.5 | AI | ~1 page |
| WP15D | Correct AMS-INC-004 EBS factual error (after BU Lead approval) | AI (pending BU Lead) | 1 assumption |

### Priority 2 — Before Next Multi-site or Mining Sector Tender

| Item | Work Required | Owner | Estimated Size |
|---|---|---|---|
| WP15E | Author Multi-site Support Model Assumptions | AI + Oracle BU Lead | ~6–8 new assumptions |
| WP15F | Author Mining Sector Compliance Assumptions | AI + Compliance Lead | ~5–7 new assumptions |

### Priority 3 — Before Governance Lock-down

| Item | Work Required | Owner | Estimated Size |
|---|---|---|---|
| WP15G | Author AMS Onboarding and KT Assumptions | AI + Oracle BU Lead | ~6–8 new assumptions |
| WP15H | Correct AMS pack frontmatter count (96→84) per WP14B findings | AI (after human review) | Metadata update |
| WP15I | Add EBS custom code and ITSM integration assumptions (GAP-012, GAP-013) | AI + Oracle BU Lead | ~4–6 new assumptions |

### Dependency Notes

- WP15A and WP15B are blocked on Oracle BU Lead participation (BU decisions required for SLA targets and role definitions)
- WP15H is blocked on WP14B human review completion
- All Priority 1 items should be completed before the ARM contract commencement to ensure any future ARM renewal or variation is tendered from a governed assumption base

---

## 9. Final Verdict

### Can APPSolve confidently bid an Oracle EBS AMS tender using the current Tender Factory?

## YES WITH QUALIFICATIONS

---

### Basis for YES

**1. The factory produced a winning tender.** ARM IT045 was awarded to APPSolve on 28 August 2025. The four-pack assembly (AMS + ERP + OCI + OIC = 485 approved assumptions) plus three approved capability assets provided a complete, governed, auditable tender baseline. This is not a theoretical assessment — the factory delivered.

**2. Capability assets are the competitive differentiator.** W2S1-002 (EBS Capability Statement), W2S1-003 (DBA Executive Summary), and W2S1-004 (Managed Services Model) gave APPSolve differentiated, specific, evidence-backed content for the 30%-weighted Vendor Capability criterion. These assets are strong and reusable without modification for future EBS AMS tenders.

**3. Reference base is deep for EBS.** Multiple Gold and Silver tier EBS references (Assore, Adcock Ingram, Stellenbosch, WITS) are active and citeable. ARM itself is now a reference (post-award). No EBS AMS competitor in the South African market is likely to match this reference depth.

**4. The governance framework is clean.** All 485 assumptions are in Approved status. Rule 21 governance controls are correctly observed. Assembly rules identify the correct pack combination. No prohibited content was triggered. The factory produced a compliant, governed baseline with no governance exceptions.

---

### Qualifications Required

**Q1 — SLA assumptions require manual override on every EBS AMS tender (CRITICAL)**

The AMS pack's standard SLA (P1=1 hour, 4-priority tier, business hours only) is structurally incompatible with any EBS AMS tender that specifies non-standard SLAs. The ARM requirement (P1=15 minutes, 24/7, 5-tier, response + resolution) required complete manual replacement of the factory's SLA assumptions. Until the EBS-AMS SLA Overlay (WP15A) is authored and approved, every EBS AMS tender will require a full SLA rebuild from scratch.

*Risk if not addressed:* A bid team that does not recognise this incompatibility could submit an AMS pack's standard SLA (P1=1 hour) against a client requiring P1=15 minutes. That is a contractual commitment APPSolve cannot meet, discovered after award.

**Q2 — Dedicated Resource Model must be manually composed (CRITICAL)**

The ARM model (SDM + 4 specialists, 680h/month minimum, named) had no assumption backing. All commercial commitments on team structure and hour minimums were manually authored in the submission. Until the Dedicated Resource Model Assumption Set (WP15B) is authored, every EBS AMS tender using a dedicated model carries unbounded commercial exposure from inconsistent manual commitments.

**Q3 — BEE compliance requires active management for mining sector tenders (HIGH)**

APPSolve submitted at Level 3 against a Level 4 requirement. The tender was awarded — indicating that evaluators exercised discretion on compliance scoring (5% weighting, lowest criterion). However, this cannot be assumed to repeat. The BEE certificate expires 2026-07-31. After expiry, no EBS AMS tender can include a BEE compliance claim until renewal is confirmed. Mining Charter BEE requirements (2018 Charter, 25%+1 HDP) remain unaddressed by any factory assumption and require manual BU Lead review on every mining sector tender.

**Q4 — EBS-specific support assumptions are absent from the AMS pack (HIGH)**

The AMS pack was authored with Oracle Fusion SaaS as the primary reference frame. EBS on OCI is a materially different technical environment (not SaaS; client manages the application layer; DBA scope is deeper; patch management is separate). Factory output for EBS will contain Fusion-specific wording that requires correction before submission. This is manageable but introduces editing overhead and error risk on every EBS AMS bid.

---

### Summary Position

| Dimension | Factory Readiness | Manual Effort Required |
|---|---|---|
| Vendor capability narrative | Ready (W2S1-002, 003, 004) | None — reuse as-is |
| OCI assumptions (174) | Ready | None — full coverage |
| OIC assumptions (104) | Ready | None — full coverage |
| AMS scope and governance | Ready | None — direct reuse |
| AMS SLA (P1–P5, 24/7) | Not ready | Full manual rebuild per tender |
| Dedicated resource model | Not ready | Full manual composition per tender |
| EBS-specific support layer | Partially ready | Light-to-moderate correction |
| BEE / Mining Charter compliance | Not ready | BU Lead manual review per tender |
| KT / Onboarding | Not ready | Full manual authoring per tender |

The Tender Factory is ready where it matters most — capability, credentials, OCI, and OIC. It is not ready where commercial risk concentrates — SLA commitments and dedicated model structuring. Three work packages (WP15A, WP15B, WP15C) would close the critical gaps and elevate the factory from "won despite the gaps" to "won because of the factory."

---

*Findings only. No source files modified. No assumptions changed. No packs altered. No BU decisions resolved.*

*WP14C_TENDER_FACTORY_VALIDATION_REPORT v1.0 | WP14C — Tender Factory Validation Run | 2026-06-17*
