---
document_id: TENDER_ASSUMPTION_ASSEMBLY_RULES
title: "Tender Assumption Assembly Rules — Inheritance and Selection Logic"
version: "1.9"
created: "2026-06-15"
created_by: "WP11 — Commercial Assumptions Library"
last_updated: "2026-06-19"
last_updated_by: "WP16D — Oracle Journeys Post-Programme Enhancement"
status: "Active"
applies_to: "All Oracle, Acumatica, and BeBanking proposals and SOWs"
---

# Tender Assumption Assembly Rules

## 1. Purpose

This document defines the rules for automatically selecting and assembling assumption packs into proposals, SOWs, quotations, and tender responses. It implements an inheritance model: a base assumption pack is always loaded first, and module-specific packs are layered on top. This ensures:

- No proposal ships without the commercial baseline
- Module-specific assumptions extend the base without duplicating it
- Bid managers and proposal authors have a defined, repeatable selection process
- Commercially sensitive exclusions and customer responsibilities are never omitted

**Only assumptions with status `Approved` in `ASSUMPTION_REGISTER.csv` may be assembled into an external document. See ASSUMPTION_GOVERNANCE.md Rule 1.**

---

## 2. Assembly Principles

### 2.1 Inheritance Model

```
LEVEL 0 (Foundation)
└── HCM Base Assumptions (HCM_BASE_ASSUMPTIONS_V1.md)
    — Always loaded for ALL Oracle Fusion HCM proposals

LEVEL 1 (Module Extensions)
├── Recruiting Assumptions      [Approved v1.0 — 2026-06-19 (WP16C)]
├── Learning Assumptions        [Approved v1.0 — 2026-06-19 (WP16C)]
├── Talent Management Assumptions [Approved v1.0 — 2026-06-19 (WP16C)]
├── Workforce Compensation Assumptions [Approved v1.0 — 2026-06-19 (WP16C)]
└── OIC Assumptions             [Approved — 2026-06-15]

LEVEL 1 (ERP Track)
└── Oracle ERP Assumptions      [Approved — 2026-06-15]

LEVEL 2 (Infrastructure)
└── OCI Assumptions             [Approved v1.0 — 2026-06-16]

SEPARATE TRACKS (Non-Oracle)
├── Acumatica Base Assumptions  [Approved v1.0 — 2026-06-18 (WP15C)]
└── BeBanking Assumptions       [Approved v1.0 — 2026-06-18 (WP14F)]

OVERLAY PACKS (Additive — EBS AMS engagements only)
├── EBS AMS SLA Overlay         [Approved v1.0 — 2026-06-19 (WP15F) — all 4 decisions resolved]
└── EBS Dedicated Resource Model [Approved v1.0 — 2026-06-19 (WP15F) — all 5 decisions resolved]

CROSS-BU (Applies to all tracks)
└── Managed Services / AMS Assumptions [Approved — 2026-06-15]
```

### 2.2 Core Rules

**Rule A — Base First:** The relevant base assumption pack is always loaded before any module-specific pack. A module-specific pack is never used without its parent base.

**Rule B — Additive Only:** Module assumption packs add new assumptions. They do not override or remove assumptions from the base pack. If a base assumption is inapplicable to a specific tender, a BU Lead override is recorded (see ASSUMPTION_GOVERNANCE.md Rule 4).

**Rule C — No Duplication:** Where a base assumption and a module assumption address the same topic, the module assumption takes precedence and the base assumption is suppressed for that topic only (see Section 4 for conflict resolution rules).

**Rule D — Alphabetical BOM-to-Pack Mapping:** The assembly trigger is the Oracle BOM line items included in the proposal. Every BOM line item maps to one or more assumption packs. The mapping is defined in Section 3.

**Rule E — Exclusions Always Included:** The Explicit Exclusions section (HCM-EXC-XXX) of the base pack is always included in full. Exclusions must never be omitted from a proposal, even where space is a constraint.

---

## 3. BOM Line Item to Assumption Pack Mapping

### 3.1 Oracle Fusion HCM — Current (V1 Library)

| BOM Line Item | Oracle Part No. | Base Pack | Module Pack(s) | Notes |
|---|---|---|---|---|
| Oracle Fusion HCM Base Cloud Service | B85800 | HCM Base ✓ | — | Includes Core HR, Absence, Benefits, Journeys, Payroll Interface, Workforce Directory, OTBI, TDE, AI Dynamic Skills. Journey scope governed by HCM-JRN-001 (WP16D): 3 standard Journeys (Onboarding, Transfer/Promotion, Offboarding) included; additional Journeys = CR |
| Oracle Fusion Recruiting Cloud Service | B87675 | HCM Base ✓ | Recruiting [Approved v1.0 — 2026-06-19 (WP16C)] | HCM Base is loaded; Recruiting pack adds recruitment-specific assumptions |
| Oracle Fusion Workforce Compensation Cloud Service | B109620 | HCM Base ✓ | Compensation [Approved v1.0 — 2026-06-19 (WP16C)] | HCM Base is loaded; Compensation pack adds merit cycle, budget, and approval assumptions |
| Oracle Fusion Learning Cloud Service | B85242 | HCM Base ✓ | Learning [Approved v1.0 — 2026-06-19 (WP16C)] | HCM Base is loaded; Learning pack adds LMS, content, SETA/WSP/ATR assumptions |
| Oracle Fusion Talent Management Cloud Service | B94925 | HCM Base ✓ | Talent [Approved v1.0 — 2026-06-19 (WP16C)] | HCM Base is loaded; Talent pack adds performance, succession, goal management assumptions |
| Oracle Fusion Recruiting Booster Cloud Service | B95763 | HCM Base ✓ | Recruiting [Approved v1.0 — 2026-06-19 (WP16C)] | Booster is an extension of Recruiting; load both Recruiting pack and HCM Base |
| Oracle Fusion HR Help Desk Cloud Service | B87388 | HCM Base ✓ | Help Desk [FUTURE] | HCM Base is loaded; Help Desk pack adds service request, ER case, knowledge management assumptions |
| Oracle Integration Cloud Enterprise | B91110 | HCM Base ✓ | OIC [Approved] | OIC pack is standalone and mandatory — load alongside HCM Base, ERP Base, or BeBanking pack as applicable; adds 101 integration-specific assumptions |
| Oracle Fusion Financials Cloud Service | B86481 | — (ERP standalone) | ERP [Approved] | Load alongside OIC pack for all ERP engagements with integrations; ERP pack is the base for all ERP module packs |
| Oracle Fusion Procurement Cloud Service | B86482 | — | ERP [Approved] | Procurement is included in ERP pack scope; not a separately assembled pack |
| Oracle Fusion PPM Cloud Service | B86483 | — | ERP [Approved] | PPM is included in ERP pack scope; not a separately assembled pack |
| Oracle Analytics Cloud | — | HCM Base ✓ | OCI [Approved] | OAC is separately licensed; OCI pack (Sections 101–119) covers OAC provisioning and VCN access; OAC content development is a separate Analytics engagement |

### 3.2 Assembly Matrix — Current Library (V1)

All HCM module packs are Approved v1.0 (WP16C — 2026-06-19). The full active assembly matrix is:

```
Oracle HCM Core HR only:
= HCM Base (complete — includes HCM-JRN-001: 3 standard Journeys)

Oracle HCM Core HR + Recruiting:
= HCM Base (complete)
+ Recruiting Pack (Approved v1.0 — additive)

Oracle HCM Core HR + Learning:
= HCM Base (complete)
+ Learning Pack (Approved v1.0 — additive)

Oracle HCM Core HR + Talent Management:
= HCM Base (complete)
+ Talent Pack (Approved v1.0 — additive)

Oracle HCM Core HR + Workforce Compensation:
= HCM Base (complete)
+ Compensation Pack (Approved v1.0 — additive)

Oracle HCM Full Suite (Core HR + Recruiting + Learning + Talent + Compensation):
= HCM Base (complete)
+ Recruiting Pack (Approved v1.0 — additive)
+ Learning Pack (Approved v1.0 — additive)
+ Talent Pack (Approved v1.0 — additive)
+ Compensation Pack (Approved v1.0 — additive)

Oracle HCM Full Suite + OIC Enterprise:
= HCM Base (complete)
+ Recruiting Pack (Approved v1.0 — additive)
+ Learning Pack (Approved v1.0 — additive)
+ Talent Pack (Approved v1.0 — additive)
+ Compensation Pack (Approved v1.0 — additive)
+ OIC Pack (Approved — additive)

Oracle HCM Full Suite + OIC + OCI:
= All of the above
+ OCI Pack (Approved v1.0 — additive)

Oracle HCM Full Suite + Managed Services / AMS:
= All relevant implementation packs
+ Managed Services / AMS Pack (Approved — additive)
```

### 3.2a Oracle Journeys Scope Rule

**Rule JRN-1 — Journeys Scope Automatically Included with HCM Base:**
HCM-JRN-001 is part of the HCM Base pack and is included in every Oracle HCM proposal without a separate trigger. Because Oracle Journeys (B85800) is delivered as part of the Oracle Fusion HCM Base Cloud Service, the Journey scope assumption applies to all Core HR implementations regardless of which module packs are loaded.

| If the proposal includes... | HCM-JRN-001 applies? |
|---|---|
| Oracle Fusion HCM Base Cloud Service (B85800) | Yes — always |
| Any HCM module pack (Recruiting, Learning, Talent, Compensation) | Yes — inherited from HCM Base |
| Explicit mention of onboarding, offboarding, or employee lifecycle Journeys | Yes — confirm HCM-JRN-001 is present; flag if client expects more than 3 Journeys |
| Oracle Fusion Recruiting Cloud — onboarding trigger | Yes — HCM-JRN-001 defines the 3-Journey default; REC pack governs the Recruiting-to-HCM onboarding transition separately |

**Escalation trigger:** If the client's RFP, scope document, or workshop notes reference more than three (3) Journeys, or reference Journey categories not covered by the three standard types (Onboarding, Internal Transfer/Promotion, Offboarding), the proposal author must flag this as a scope addition before submission and include a corresponding Change Request priced item. HCM-JRN-001 is the commercial baseline — do not suppress or override without BU Lead approval.

### 3.2b OCI Assembly Rules

When OCI is included in any engagement (OCI migration, OCI hosting, EBS on OCI, OIC on OCI, BeBanking OCI):

**Rule OCI-1 — OCI Pack Mandatory for all OCI Workloads:**
Any proposal that includes Oracle workloads hosted on OCI, an OCI migration, OCI managed services, or BeBanking OCI hosting must include the OCI Pack. The OCI Pack is additive to the application pack — it does not replace it.

**Rule OCI-2 — OCI Pack NOT required for Oracle SaaS:**
Proposals for Oracle Fusion HCM Cloud or Fusion ERP Cloud (SaaS) do not require the OCI Pack. SaaS infrastructure is Oracle-operated.

**Rule OCI-3 — OCI Pack Triggers:**

| If the solution includes... | OCI Pack required? |
|---|---|
| Oracle Database on OCI (VM DB, ExaCS, ADB) | Yes |
| EBS on OCI | Yes |
| OIC on OCI (private endpoint) | Yes |
| APEX on OCI | Yes |
| BeBanking OCI hosting | Yes |
| AMS Managed OCI Services | Yes |
| Oracle Fusion HCM Cloud (SaaS) only | No |
| Oracle Fusion ERP Cloud (SaaS) only | No |
| OIC as SaaS (Oracle-managed) only | No |

**Rule OCI-4 — Approved for Use:**
The OCI Pack is Approved v1.0 (2026-06-16). All 14 BU decisions are resolved (BU-OCI-007 withdrawn). OCI Pack assumptions may be used in client-facing proposals without qualification.

**Assembly patterns with OCI:**

```
Oracle ERP + OCI migration:
= ERP Pack (complete)
+ OCI Pack (additive)

Oracle ERP + OCI migration + AMS Managed OCI:
= ERP Pack (complete)
+ OCI Pack (additive)
+ AMS Pack (additive)

EBS on OCI + OIC:
= ERP Pack (complete)
+ OCI Pack (additive)
+ OIC Pack (additive)

BeBanking on OCI:
= BeBanking Pack (FUTURE)
+ OCI Pack (additive)

Oracle HCM (SaaS) + OIC (private OCI endpoint):
= HCM Base Pack (complete)
+ OIC Pack (complete)
+ OCI Pack (additive — for OCI private endpoint and VCN configuration)
```

---

### 3.3 Acumatica Assembly (V1 Library)

**Acumatica Base Pack status:** Approved v1.0 — 2026-06-18 (WP15C). 152 assumptions across Sections 120–139. All 14 BU decisions resolved (BU-ACU-001–015, excl. BU-ACU-013 which was not created). `approved_for_reuse: true`. **May be used in client-facing proposals without qualification.**

```
Acumatica ERP (any modules):
= Acumatica Base (Approved v1.0 — 2026-06-18)

Acumatica + PaySpace payroll integration:
= Acumatica Base (Approved v1.0)
[Note: BU-ACU-001 resolved — method confirmed at pre-sales per PaySpace licence tier]

Acumatica + BeBanking integration:
= Acumatica Base (Approved v1.0)
+ BeBanking Pack (Approved v1.0 — 2026-06-18)

Acumatica + AMS:
= Acumatica Base (Approved v1.0)
+ Managed Services / AMS Pack (additive — Approved 2026-06-15)

Acumatica + OCI (where client hosts on OCI):
= Acumatica Base (Approved v1.0)
+ OCI Pack (additive — Approved v1.0 — 2026-06-16)
```

**Governance constraints active in Acumatica Base Pack (do not override without BU Lead direction):**
- Partner tier: "Acumatica Gold Partner" only — never "Gold Certified" (Constraint 9)
- PaySpace is the standard Acumatica payroll integration; non-PaySpace assessed at pre-sales
- POPIA disclosure is mandatory in all Acumatica proposals regardless of client industry sector
- ISV: only ISVs on the published ISV Support List may be included in proposals
- Parallel run: excluded by default; SOW explicit inclusion required
- Legacy data migration: opening balances and open items only; history always separately scoped
- Hypercare: 4 weeks standard
- BeBanking Payroll H2H = Oracle EBS/Fusion payroll only — never Acumatica payroll (Constraint 15, permanent)

### 3.4 BeBanking Assembly (V1 Library — Approved v1.0)

**BeBanking Base Pack status:** Approved v1.0 — 2026-06-18 (WP14F). 117 assumptions approved. All 10 BU decisions resolved (BU-BB-001–010; BU-BB-006 CRITICAL withdrawn). `approved_for_reuse: true`. **May be used in client-facing proposals without qualification.**

```
BeBanking only:
= BeBanking Pack (Approved v1.0 — 2026-06-18)

BeBanking + Oracle integration:
= BeBanking Pack (Approved v1.0 — 2026-06-18)
+ OIC Pack (Approved — 2026-06-15)
```

**Governance constraints active in BeBanking Base Pack (do not override without BU Lead direction):**
- BeBanking bank-intermediated model only: do not claim direct SWIFT membership (Constraint 14)
- BeBanking Payroll H2H = Oracle EBS and PaySpace only — never Acumatica payroll (Constraint 15)
- BeBanking SAP: "integrates with SAP environments" only — no module-level claims until BQ-WEB-04 confirmed (Constraint 24)
- BU-OCI-007 permanently withdrawn: no BeBanking-specific OCI cost or pricing responsibility assumption (Constraint 1)

### 3.5 EBS Managed Services (AMS) Assembly Pattern (V1 Library — WP15D)

**Context:** Oracle EBS (R11, R12.1, R12.2) is not a SaaS product. Unlike Oracle Fusion HCM and ERP Cloud, EBS runs on client-managed infrastructure (on-premises or on OCI). EBS AMS tenders require a different assembly pattern to Oracle Fusion AMS tenders because: (a) EBS clients own the application layer; (b) DBA scope is broader and deeper; (c) SLA and resource model requirements differ materially from Fusion SaaS support.

**Applicable overlays:**

| Overlay | Trigger condition | Status |
|---|---|---|
| `EBS_AMS_SLA_OVERLAY_V1.md` | Client specifies SLA commitments that differ from AMS standard (5-tier, P1=15min, resolution times, 24/7 P1 coverage) | Draft — 4 BU decisions pending |
| `EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | Client specifies named/dedicated resource team rather than pooled AMS support | Draft — 5 BU decisions pending |

**Assembly Pattern — EBS AMS Standard (no special SLA or DRM)**

```
EBS AMS Standard (pooled support, standard AMS SLA):
= ERP Pack (Approved v1.0 — 2026-06-15)                  [EBS functional scope]
+ OCI Pack (Approved v1.0 — 2026-06-16)                  [MANDATORY if EBS runs on OCI — Rule OCI-1]
+ OIC Pack (Approved — 2026-06-15)                        [if OIC integrations in scope]
+ AMS Pack (Approved — 2026-06-15)                        [MANDATORY — AMS commercial baseline]

Note: Do NOT add HCM Base Pack for EBS HCM support. EBS HR/Payroll is within the ERP Pack scope.
Note: AMS Pack assumption AMS-INC-004 ("Fusion HCM/ERP delivered on Oracle's SaaS infrastructure")
      is NOT applicable to EBS. Suppress AMS-INC-004 for EBS AMS proposals via BU Lead override.
```

**Assembly Pattern — EBS AMS with Enhanced SLA (5-tier, P1=15min, 24/7)**

```
EBS AMS — Enhanced SLA:
= ERP Pack (Approved v1.0)
+ OCI Pack (if EBS on OCI — Rule OCI-1)
+ OIC Pack (if OIC in scope)
+ AMS Pack (Approved)
+ EBS AMS SLA Overlay (Approved v1.0 — 2026-06-19 WP15F)     [REPLACES AMS-SLA-001, AMS-PRI-001–003]

Trigger: client specifies any of the following in the tender or RFP:
  - P1 response target < 1 hour (e.g., 15 minutes, 30 minutes)
  - Resolution time commitments (in addition to response time)
  - 5-tier priority classification (P1–P5)
  - 24/7 P1 or 24/7 P1+P2 coverage
  - P5 priority tier (deferred/minimal queries)
```

**Assembly Pattern — EBS AMS with Dedicated Resource Model**

```
EBS AMS — Dedicated Resource Model (pooled AMS SLA):
= ERP Pack (Approved v1.0)
+ OCI Pack (if EBS on OCI — Rule OCI-1)
+ OIC Pack (if OIC in scope)
+ AMS Pack (Approved)                                         [AMS-SLA-005 REPLACED by EBS-DRM-001]
+ EBS Dedicated Resource Model Overlay (Approved v1.0 — 2026-06-19 WP15F)

Trigger: client specifies any of the following:
  - Named consultant(s) by role
  - Minimum monthly hours per named role
  - Ring-fenced (non-pooled) resource allocation
  - Dedicated SDM requirement
  - Named DBA / Named Functional Lead requirement
```

**Assembly Pattern — EBS AMS Full Stack (Enhanced SLA + Dedicated Resource Model)**

```
EBS AMS — Full Stack (ARM IT045 pattern):
= ERP Pack (Approved v1.0)
+ OCI Pack (if EBS on OCI — Rule OCI-1)
+ OIC Pack (if OIC in scope)
+ AMS Pack (Approved)
+ EBS AMS SLA Overlay (Approved v1.0 — 2026-06-19 WP15F)     [REPLACES AMS-SLA-001, AMS-PRI-001–003]
+ EBS Dedicated Resource Model Overlay (Approved v1.0 — 2026-06-19 WP15F)

This pattern covers the ARM IT045 tender specification (680h/month, 5-tier SLA, P1=15min/2hr,
named SDM+DBA+2 functional leads+OIC specialist, 24/7 P1 coverage).
```

**Mandatory exclusions for all EBS AMS assemblies:**

| Item | Rule |
|---|---|
| HCM Base Pack (Oracle Fusion HCM) | Do NOT include — HCM Base covers Fusion SaaS only |
| AMS-INC-004 | Suppress for all EBS AMS proposals (AMS-INC-004 is factually incorrect for EBS — EBS is not SaaS) |
| Implementation Methodology Pack | EBS AMS is a support engagement, not an implementation — do not include implementation pack |
| Oracle Fusion ERP Pack | ERP Pack covers both Fusion ERP and EBS functional scope — include ERP Pack; do not add a second EBS-only module pack |

**Overlay precedence for EBS AMS:**

Where both the SLA Overlay and the DRM Overlay are assembled for the same engagement:
1. The SLA Overlay assumptions apply first (they replace AMS SLA assumptions)
2. The DRM Overlay assumptions apply next (they replace AMS-SLA-005 and extend the team model)
3. Where both overlays have assumptions that address the same topic, the DRM Overlay takes precedence (the DRM includes SLA commitments by role, which are more specific than the generic SLA targets)

**AMS-INC-004 suppression note (BU Lead awareness required):**

AMS-INC-004 states: "Oracle Fusion HCM and ERP are delivered on Oracle's SaaS infrastructure." This is correct for Oracle Fusion proposals. For EBS AMS proposals, this assumption is factually incorrect because EBS runs on client-managed infrastructure (on-premises or OCI). In the absence of the EBS SLA Overlay (which adds EBS-DRM-013 to explicitly correct this), the proposal author must suppress AMS-INC-004 via a BU Lead override for all EBS AMS proposals. The EBS SLA Overlay's assumption EBS-DRM-013 provides the replacement statement.

---

## 4. Conflict Resolution Rules

When a base assumption and a module assumption address the same topic:

| Conflict Type | Resolution |
|---|---|
| Module assumption is more specific than base assumption | Use module assumption; suppress base assumption for that topic. Record suppression in tender scope notes. |
| Module assumption contradicts base assumption | BU Lead resolves before proposal submission. One of the two assumptions is modified at the project level; library is flagged for update. |
| Base assumption is inapplicable to a specific module context | BU Lead approves suppression of the base assumption for this tender. Record in tender scope notes. |

---

## 5. Proposal Insertion Format

### 5.1 Proposal Section Title
Assembled assumptions are inserted into proposals under the standard heading:
> **Assumptions, Exclusions and Customer Responsibilities**

This section appears after the proposed solution description and before the costing table (or as a standalone section in SOWs).

### 5.2 Sub-Heading Structure
Within the assumptions section, use the following sub-headings aligned to the pack structure:

```
1. Environment Assumptions
2. Organisation Structure Assumptions
3. Security Assumptions
4. Workflow Assumptions
5. Data Migration Assumptions
6. Reporting Assumptions
7. Testing Assumptions
8. Training Assumptions
9. Cutover Assumptions
10. Hypercare Assumptions
11. Change Management Assumptions
12. Third-Party System Assumptions
13. Customer Responsibilities
14. General Assumptions
15. Explicit Exclusions
[16. Module-specific sections from additional packs]
```

### 5.3 Assumption ID Inclusion
Assumption IDs (e.g., HCM-ENV-001) may be included in parentheses after each statement in SOWs and fixed-price proposals to enable unambiguous reference in scope disputes. In RFP tender responses, IDs may be omitted for document cleanliness unless the tender format requires them.

### 5.4 BU Lead Items
Assumptions tagged `BU-WP11-XXX` as requiring BU Lead confirmation must have those items resolved before insertion into any external document. Do not insert BU Lead confirmation items — resolve them first.

---

## 6. Customer Responsibilities — Mandatory Inclusion Rule

The Customer Responsibilities section (HCM-CUS-001 through HCM-CUS-010 in the base pack, plus module-specific customer responsibilities from additional packs) must always be included in full in every proposal and SOW.

Customer Responsibilities must never be omitted, abbreviated, or moved to an appendix in a way that reduces their visibility. These items define the client's contractual obligations and are APPSolve's primary scope protection mechanism.

---

## 7. Explicit Exclusions — Mandatory Inclusion Rule

The Explicit Exclusions section (HCM-EXC-001 through HCM-EXC-012 in the base pack) must always be included in full in every proposal and SOW.

**Rationale:** Exclusions protect APPSolve from scope creep. An exclusion that is not stated is an exclusion that cannot be enforced. A client who is not told that Oracle Fusion Global Payroll is excluded will assume it is included.

---

## 8. Triggers for Assembly Rule Updates

This document must be updated when:
- A new assumption pack is approved and added to the library
- A BOM line item is added to APPSolve's product portfolio that does not yet have a mapped assumption pack
- An assembly conflict is resolved at the project level and the resolution should be standardised
- The inheritance model changes (for example, a Cross_BU base pack is introduced that precedes all BU-specific packs)

Updates to this document follow the same governance process as assumption pack documents (see ASSUMPTION_GOVERNANCE.md Section 5).

---

## 9. Current Library Status Summary

| Pack | File | Status | Assumptions | BU Review Items |
|---|---|---|---|---|
| HCM Base | `Assumptions/HCM/HCM_BASE_ASSUMPTIONS_V1.md` | **Approved v1.1 — WP16D 2026-06-19** | **115** | 0 (closed; BU-HCM-022 applied WP16D) |
| HCM Recruiting | `Assumptions/HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-19 (WP16C)** | **54** | 0 (all resolved — BU-REC-001–007 closed) |
| HCM Learning | `Assumptions/HCM/HCM_LEARNING_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-19 (WP16C)** | **37** | 0 (all resolved — BU-LRN-001/003/005 closed) |
| HCM Talent Management | `Assumptions/HCM/HCM_TALENT_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-19 (WP16C)** | **31** | 0 (all resolved — BU-TLT-001/003/004 closed) |
| HCM Workforce Compensation | `Assumptions/HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-19 (WP16C)** | **30** | 0 (all resolved — BU-COM-001/002/005 closed) |
| OIC (standalone) | `Assumptions/OIC/OIC_ASSUMPTIONS_V1.md` | **Approved — 2026-06-15** | **104** | 0 (closed) |
| Oracle ERP | `Assumptions/ERP/ERP_ASSUMPTIONS_V1.md` | **Approved — 2026-06-15** | **123** | 0 (closed) |
| HCM HR Help Desk | `Assumptions/HCM/HCM_HELPDESK_ASSUMPTIONS_V1.md` | NOT YET CREATED | 0 | — |
| OCI | `Assumptions/OCI/OCI_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-16** | 174 | 0 (all APPROVED; BU-OCI-007 WITHDRAWN) |
| Acumatica Base | `Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-18 (WP15C)** | 152 | 0 (all RESOLVED WP15C) |
| BeBanking Base | `Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-18 (WP14F)** | 117 | 0 (all RESOLVED WP14F) |
| Managed Services / AMS | `Assumptions/AMS/AMS_ASSUMPTIONS_V1.md` | **Approved — 2026-06-15** | **84** | 0 (closed) |
| EBS AMS SLA Overlay | `Assumptions/AMS/EBS_AMS_SLA_OVERLAY_V1.md` | **Approved v1.0 — 2026-06-19 (WP15F)** | **53** | 0 (all RESOLVED WP15F) |
| EBS Dedicated Resource Model | `Assumptions/AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-19 (WP15F)** | 62 | 0 (all RESOLVED WP15F) |
| Cross_BU | `Assumptions/Cross_BU/CROSS_BU_ASSUMPTIONS_V1.md` | NOT YET CREATED | 0 | — |

> **WP16A RECONCILIATION BASELINE — 2026-06-19:** All counts use **body/register-authoritative** figures. These are the single source of truth figures.

**Total assumptions (body count):** **1,136** (1,136 approved + 0 draft)
**Total approved for use:** **1,136** (all 13 packs — HCM Base 115 + Recruiting 54 + Learning 37 + Talent 31 + Compensation 30 + OIC 104 + ERP 123 + OCI 174 + AMS 84 + Acumatica 152 + BeBanking 117 + EBS SLA Overlay 53 + EBS DRM Overlay 62)
**Draft assumptions:** **0** — all 13 packs Approved v1.0 (GOVERNANCE PROGRAMME COMPLETE — WP16C 2026-06-19)

> **Approval status change WP15C (2026-06-18):** Acumatica Base promoted Draft → Approved v1.0; 152 assumptions added to approved pool.
> **Approval status change WP14F (2026-06-18):** BeBanking Base promoted Draft → Approved v1.0; 117 assumptions added to approved pool.
> **Approval status change WP15F (2026-06-19):** EBS SLA Overlay (53) + EBS DRM Overlay (62) promoted Draft → Approved v1.0; 115 assumptions added to approved pool. All 9 BU decisions resolved.
> **WP16A (2026-06-19):** All pack frontmatter and footer counts corrected to body/register-authoritative values. Total approved corrected 996→983; draft corrected 173→152.
> **WP16C (2026-06-19):** All 4 HCM module packs (Recruiting 54, Learning 37, Talent 31, Compensation 30) promoted Draft → Approved v1.0. Draft pool 152→0. Approved 983→1,135. GOVERNANCE PROGRAMME COMPLETE.
> **WP16D (2026-06-19):** HCM-JRN-001 added to HCM Base pack (BU-HCM-022 applied). HCM Base 114→115. Total 1,135→1,136. Approved 1,135→1,136. All 4 HCM module pack statuses propagated from WP16C.

---

*TENDER_ASSUMPTION_ASSEMBLY_RULES v2.0 | Updated: WP17C — Regression Test Suite: Section 3.5 code block labels corrected from "Draft" to "Approved v1.0 — 2026-06-19 WP15F" for both EBS SLA Overlay and EBS DRM Overlay (cosmetic fix; Section 2.1 was already correct) | 2026-06-22*
*Prior: WP16D — Oracle Journeys Post-Programme Enhancement + WP16C status propagation: HCM-JRN-001 added (BU-HCM-022); all 4 HCM module packs promoted Approved v1.0 (WP16C); Rule JRN-1 and Section 3.2a added; BOM table updated; approved 983→1,136; draft 152→0; total 1,135→1,136 | 2026-06-19*
*Prior update: WP16A — Library Reconciliation (all counts corrected to body/register-authoritative; EBS overlay packs promoted Approved v1.0; approved 882→983; total 1,174→1,135) | 2026-06-19*
*Next update trigger: New assumption pack added, BOM line item changes, or new Journey BU decision*
