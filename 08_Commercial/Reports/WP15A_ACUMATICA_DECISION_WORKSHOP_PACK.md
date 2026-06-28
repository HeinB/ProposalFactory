---
title: WP15A — Acumatica BU Lead Decision Workshop Pack
version: v1.0
status: Ready for Workshop
programme: WP15A
date: 2026-06-18
author: AI (Claude)
for: Acumatica BU Lead + Commercial Director (BU-ACU-011 item)
pack_ref: ACU_BASE_ASSUMPTIONS_V1.md
decisions_covered: 13
decisions_high: 7
decisions_medium: 6
---

# WP15A — Acumatica BU Lead Decision Workshop Pack

**Prepared by:** AI (Claude) | **Date:** 2026-06-18 | **For:** Acumatica BU Lead

> **Preparation document only.** No pack files have been modified. All changes to ACU_BASE_ASSUMPTIONS_V1.md and ACU_ASSUMPTION_REGISTER.csv will be applied by AI after BU Lead decisions are confirmed and returned.

---

## Section 1 — Executive Summary

### Current Acumatica Pack Status

| Field | Value |
|---|---|
| Pack | Acumatica Base Assumption Pack (ACU) |
| Pack file | `08_Commercial/Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` |
| Sections | 120–139 (20 sections) |
| Assumption count | 152 |
| Current status | **Draft — Pending BU Lead Approval** |
| Approved for reuse | No — not until BU Lead approval complete |
| BU decisions pending | **13** |
| BU decisions resolved | 1 (BU-ACU-009 — Acumatica Gold Partner WP14G) |
| Current readiness score | 9.0 / 10 (structural — governance not yet complete) |
| Critical blockers | **0** (BU-ACU-009 resolved WP14G) |

### What These Decisions Unlock

Resolving all 13 decisions enables:
1. Promotion of the Acumatica Base Pack to **Approved v1.0**
2. All 152 Acumatica assumptions become available for tender assembly
3. Acumatica proposals can be assembled from the Tender Factory without manual commercial review of each assumption
4. Programme readiness improves from 6 of 11 packs to **7 of 11 packs approved**

### Promotion Path

```
Current state:  152 assumptions | Draft | 13 decisions pending
After workshop: 152 assumptions | Draft | 0 decisions pending → BU Lead sign-off → Approved v1.0
```

---

## Section 2 — Outstanding Decision Register

### HIGH Priority Decisions (7) — Wave 2 — target 2026-07-07

| ID | Topic | Assumption(s) Affected | Commercial Impact | Delivery Impact |
|---|---|---|---|---|
| BU-ACU-001 | PaySpace integration method | ACU-PAY-001, ACU-PAY-004 | Effort variance up to 5 days if wrong method assumed | API vs file-based changes architecture and testing approach |
| BU-ACU-002 | Integration tier definitions | ACU-INT-001 | Pricing inconsistency across proposals if tiers differ from AMS pack | Integration estimates may not align with AMS pricing model |
| BU-ACU-003 | BI connector scope | ACU-REP-004 | Power BI connector can add 3–8 days effort if wrongly included | Separate SOW line required if included — omission creates client expectation gap |
| BU-ACU-004 | ISV support list | ACU-EXT-003 | Uncontrolled ISV commitments in proposals expose APPSolve to unsupported delivery | Delivery risk if ISV product is committed without confirmed competency |
| BU-ACU-010 | Legacy data migration | ACU-MIG (multiple) | Opening balances only vs history: up to 15–30 day effort difference | Historical migration requires additional source system access, data cleansing, and validation cycles |
| BU-ACU-011 | Non-PaySpace payroll | ACU-PAY-008 | Non-PaySpace integration scope undefined; could be 10–25 additional days | Custom integration per payroll system; some may be unsupported |
| BU-ACU-012 | POPIA data residency | ACU-SEC-003 | Omitting POPIA disclosure in regulated sectors creates APPSolve liability | Client relies on APPSolve guidance; gaps create contractual exposure |

### MEDIUM Priority Decisions (6) — Wave 3 — target 2026-07-28

| ID | Topic | Assumption(s) Affected | Commercial Impact | Delivery Impact |
|---|---|---|---|---|
| BU-ACU-005 | Parallel run default | ACU-CUT-002 | Parallel run scope is 3–8 additional days if wrongly included | Double data entry, reconciliation, and extended cutover resource |
| BU-ACU-006 | Standard reports per module | ACU-REP-001, ACU-CFG-005 | No cap = open-ended report development effort; can add 5–20 days | Without definition, scope creep risk is high during implementation |
| BU-ACU-007 | Training format default | ACU-TRN-002 | On-site training: travel/accommodation costs not budgeted if virtual assumed | Client expectations misaligned if format not confirmed in proposal |
| BU-ACU-008 | Hypercare duration | ACU-CUT-005 | 2-week vs 6-week hypercare = up to 10 day cost difference per engagement | AMS handover timing affected; client support expectations set at go-live |
| BU-ACU-014 | APPSolve PM inclusion | ACU-GEN-010 | PM role adds 10–25% project cost; wrong default over- or under-prices proposals | Under-resourced PM on full-suite implementations increases delivery risk |
| BU-ACU-015 | Multi-entity consolidation | ACU-ORG-006 | Consolidation if wrongly included: 5–15 additional days per implementation | Inter-company elimination, consolidation ledger, and reporting design — variable effort |

---

## Section 3 — Workshop Agenda

**Recommended duration:** 90 minutes (HIGH decisions) + optional 60-minute follow-up (MEDIUM decisions)

**Attendees:**
- Acumatica BU Lead — **mandatory all items**
- Commercial Director — **mandatory BU-ACU-011** (non-PaySpace policy has commercial pricing implications)
- Senior Acumatica Consultant — recommended for BU-ACU-001, 003, 004, 005, 006

---

### Wave 2 Workshop — HIGH Decisions (90 minutes)

| Time | Item | Decision | Notes |
|---|---|---|---|
| 0:00–0:05 | Context and objective | — | Pack status; what approval unlocks; 7 HIGH decisions today |
| 0:05–0:18 | PaySpace integration method | BU-ACU-001 | Recommendation: option (c) — method confirmed at pre-sales |
| 0:18–0:28 | Integration tier definitions | BU-ACU-002 | Recommendation: option (a) — align with AMS Pack |
| 0:28–0:38 | BI connector scope | BU-ACU-003 | Recommendation: option (b) — always separately scoped |
| 0:38–0:48 | ISV support list | BU-ACU-004 | Recommendation: option (a) — maintain published list |
| 0:48–0:58 | Legacy data migration default | BU-ACU-010 | Recommendation: option (a) — opening balances only |
| 0:58–1:18 | Non-PaySpace payroll policy | BU-ACU-011 | Recommendation: option (b) — PaySpace standard; others on assessment; **CD input needed** |
| 1:18–1:28 | POPIA data residency disclosure | BU-ACU-012 | Recommendation: option (a) — mandatory in all proposals |
| 1:28–1:30 | Confirm MEDIUM session date | — | Schedule Wave 3 workshop or async sign-off |

---

### Wave 3 Workshop — MEDIUM Decisions (60 minutes)

| Time | Item | Decision | Notes |
|---|---|---|---|
| 0:00–0:05 | Recap | — | Confirm HIGH decisions applied; MEDIUM impact overview |
| 0:05–0:15 | Parallel run default | BU-ACU-005 | Recommendation: excluded by default |
| 0:15–0:25 | Standard reports per module | BU-ACU-006 | Recommendation: standard Acumatica library — no custom development assumed |
| 0:25–0:35 | Training format default | BU-ACU-007 | Recommendation: virtual facilitated as standard |
| 0:35–0:45 | Hypercare duration | BU-ACU-008 | Recommendation: 4 weeks standard |
| 0:45–0:55 | APPSolve PM inclusion | BU-ACU-014 | Recommendation: full-suite / multi-module only |
| 0:55–1:00 | Multi-entity consolidation | BU-ACU-015 | Recommendation: always separately scoped |

> **Option:** All 6 MEDIUM decisions have clear recommended defaults and low commercial exposure. The BU Lead may choose to approve recommended defaults by email rather than in a workshop session.

---

## Section 4 — Decision Sheets

---

### BU-ACU-001 — PaySpace Integration Method Standard

**Priority:** HIGH | **Owner:** Acumatica BU Lead | **Assumption:** ACU-PAY-001, ACU-PAY-004

**Context:**
ACU-PAY-004 currently states that the integration method is "confirmed during Scope & Design" but lists all four options as valid. Without a standard position, proposals cannot confidently describe the integration approach, which creates inconsistent client expectations and makes pre-sales effort estimation unreliable.

**Current wording (ACU-PAY-004):**
> "The Acumatica-PaySpace integration uses one of the following methods, confirmed during Scope & Design: (a) API integration between PaySpace and Acumatica; (b) custom middleware-based integration; (c) structured file-based import (automated or manual); (d) manual journal import using Acumatica's import scenarios."

**Options:**

| Option | Wording for proposals | Effort implication | Risk |
|---|---|---|---|
| (a) API integration as default | "APPSolve's standard Acumatica-PaySpace integration uses PaySpace's REST API" | Medium-high (5–8 days) | Requires PaySpace API access — not all PaySpace licences include API |
| (b) File-based as default | "APPSolve's standard integration uses structured file exchange (automated SFTP or scheduled import)" | Low-medium (3–5 days) | Manual steps remain; risk of data sync issues |
| **(c) Method confirmed at pre-sales per client** *(Recommended)* | "The Acumatica-PaySpace integration method is confirmed at pre-sales based on the client's PaySpace licence tier and IT environment. APPSolve proposes the most appropriate method for each engagement." | Variable — accurate per client | No commitment before environment is understood |
| (d) No default — assessed per engagement | No standard wording | Assessed per engagement | Greatest flexibility; hardest to propose |

**Recommendation:** Option (c). The integration method depends on which PaySpace licence tier the client holds — not all clients have API access. Committing to API as default risks incorrect scope on lower-tier PaySpace clients. Option (c) protects APPSolve's pricing accuracy and ensures proposals are correct for each client.

**Exact wording to approve (if option c):**
> "APPSolve's standard Acumatica-PaySpace integration method is confirmed at pre-sales based on the client's PaySpace licence and IT environment. APPSolve recommends API integration where the client holds a PaySpace licence tier that includes API access. Where API access is not available, structured file-based integration is used. The confirmed method is documented in the SOW before project commencement."

**Consequences of deferring:** Proposals will continue to list four integration methods with no standard, requiring manual commercial review of every Acumatica-PaySpace proposal.

---

### BU-ACU-002 — Integration Tier Definitions

**Priority:** HIGH | **Owner:** Acumatica BU Lead | **Assumption:** ACU-INT-001

**Context:**
ACU-INT-001 references "standard integration complexity tiers: Simple, Standard, Complex" but these are defined in the AMS Pack. There is no confirmed alignment between the AMS Pack tier definitions and how Acumatica integrations are classified. Misalignment creates pricing inconsistencies where the same integration is priced differently in AMS vs Acumatica proposals.

**Current wording (ACU-INT-001):**
> "The standard integration complexity tiers apply: Simple (standard Acumatica connector or simple API), Standard (custom API with mapping), Complex (multi-step workflow, transformation logic, event-driven). [BU-ACU-002: pending BU Lead confirmation]"

**Options:**

| Option | Implication |
|---|---|
| **(a) Use AMS Pack tiers (Simple/Standard/Complex)** *(Recommended)* | Single tier definition across all packs — consistent pricing; lower training overhead |
| (b) Define Acumatica-specific tiers | Allows Acumatica-specific nuance but creates two-tier system; confusion when cross-selling AMS and Acumatica together |
| (c) No standard — confirmed per integration during Scope & Design | Maximum flexibility; no consistency; hardest for pre-sales pricing |

**Recommendation:** Option (a). The AMS Pack tier definitions (Simple / Standard / Complex) are already approved and understood by the delivery team. Adopting the same definitions for Acumatica creates a single pricing vocabulary across all integration work. If the BU Lead believes Acumatica integrations have meaningfully different complexity characteristics, option (b) is the alternative.

**Exact wording to approve (if option a):**
> "Acumatica integration complexity is classified using APPSolve's standard integration tiers as defined in the AMS Pack: Simple (standard connector or straightforward API with minimal mapping), Standard (custom API integration with data mapping and error handling), Complex (multi-step workflow, event-driven, transformation logic, or bi-directional sync). Tier classification is confirmed for each integration during Scope & Design."

---

### BU-ACU-003 — BI Connector Scope

**Priority:** HIGH | **Owner:** Acumatica BU Lead | **Assumption:** ACU-REP-004

**Context:**
ACU-REP-004 currently excludes BI tool integration from standard scope. BU-ACU-003 asks whether Power BI connector setup should be included as standard, since Acumatica has a native Power BI connector that requires configuration. The risk is that clients assume BI connectivity is included; if it is excluded, client expectations need to be actively managed.

**Current wording (ACU-REP-004):**
> "External BI tool integration (Power BI, Tableau, QlikView) with Acumatica data is not included in the standard implementation... [BU-ACU-003: pending BU Lead decision]"

**Options:**

| Option | Included in base scope? | Effort | Risk |
|---|---|---|---|
| (a) Power BI connector included as standard | Yes — all implementations | +2–4 days | Clients who don't use Power BI get unnecessary setup; overscoping |
| **(b) Always separately scoped** *(Recommended)* | No | 0 base days | Clear scope exclusion; clients who want BI connectivity see it as a line item |
| (c) Included for clients with existing Power BI licence | Conditional | +2–4 days if applicable | Requires pre-sales licence verification; effort inconsistency |

**Recommendation:** Option (b). BI connectivity effort varies significantly by what the client wants to report on and how they've structured their Power BI environment. Including it as standard would create scope disputes. Option (b) keeps the base scope clean and allows BI to be added as a clearly priced line item per engagement.

**Exact wording to approve (if option b):**
> "Configuration of Power BI, Tableau, or other external BI tool connectivity to Acumatica data is not included in the standard implementation scope. Where the client requires BI tool integration, this is separately scoped using Acumatica's OData feed or permitted database access. BI connector configuration is quoted as a separate line item in the SOW."

---

### BU-ACU-004 — ISV Support List

**Priority:** HIGH | **Owner:** Acumatica BU Lead | **Assumption:** ACU-EXT-003

**Context:**
ACU-EXT-003 notes that APPSolve may assist with ISV configuration "where the ISV product is within APPSolve's competency" but does not define what APPSolve's competency covers. Without a published ISV support list, sales may commit to ISV implementation assistance that APPSolve cannot deliver.

**Current wording (ACU-EXT-003):**
> "...APPSolve may assist with ISV integration configuration where the ISV product is within APPSolve's competency — this assistance is separately scoped. [BU-ACU-004: pending BU Lead confirmation of which Acumatica ISV products APPSolve actively supports]"

**Options:**

| Option | Implication |
|---|---|
| **(a) Maintain a published APPSolve ISV support list** *(Recommended)* | Controlled ISV commitments; list updated quarterly by BU Lead; presales references the list |
| (b) Assess each ISV per engagement at pre-sales | Flexible but slow; creates inconsistency; BU Lead involved in every pre-sales assessment |
| (c) No ISV support — standard Acumatica only | Simplest but commercially limiting; closes doors for clients who need ISV-extended functionality |

**Recommendation:** Option (a). The BU Lead is best placed to define which ISVs APPSolve has delivered. A published list prevents sales from committing to unsupported products and gives pre-sales a clear reference without escalating every opportunity to the BU Lead.

**Action required from BU Lead (regardless of option chosen):**
The BU Lead must provide the initial ISV list at the workshop. Minimum: list ISV name + supported scope (configuration only / configuration + integration / configuration + integration + support).

**Exact wording to approve (if option a):**
> "APPSolve maintains a supported Acumatica ISV list updated quarterly by the Acumatica BU Lead. Assistance with ISV products not on the supported list requires a pre-sales assessment by the Acumatica BU Lead before scope commitment. ISV implementation assistance is always separately scoped and not included in the Acumatica base implementation SOW."

---

### BU-ACU-010 — Legacy Data Migration Default

**Priority:** HIGH | **Owner:** Acumatica BU Lead | **Assumption:** ACU-MIG (multiple)

**Context:**
Data migration scope is one of the largest variables in implementation effort. The current pack describes the migration process (3-cycle standard: pilot, dress rehearsal, production) but does not define what data is migrated by default. Without a default, proposals may include different migration scopes, making commercial comparisons across proposals inconsistent.

**Current assumption (implied by ACU-MIG section):**
Opening balance approach is described but not explicitly confirmed as the default. Historical transaction migration is not addressed.

**Options:**

| Option | What's included by default | Effort impact | Client impact |
|---|---|---|---|
| **(a) Opening balances only — no historical transactions** *(Recommended)* | GL opening balances, AR/AP open items as at go-live date | Standard — no extra cycles | Clients must retain legacy system for historical reporting; access to history via Acumatica is Day 1 onwards only |
| (b) Up to 12 months history as standard | 12 months of transactions migrated | +5–15 days depending on volume | Higher data quality risk; longer migration cycles; more client effort for data preparation |
| (c) History scope agreed per engagement — no default | Variable | Assessed per engagement | Requires BU Lead involvement at pre-sales for every migration scope discussion |

**Recommendation:** Option (a). Consistent with Oracle ERP Pack and Oracle HCM Pack defaults. Historical data migration is high-effort, high-risk, and highly variable — it should always be separately scoped. Opening balances + open items is the correct starting position for a clean Acumatica go-live.

**Exact wording to approve (if option a):**
> "Data migration to Acumatica covers opening balances and open items as at the agreed go-live date: GL opening trial balance, open AR invoices and receipts, open AP invoices and payments, open purchase orders, open sales orders, and current inventory quantities on hand (where inventory is in scope). Historical transaction migration (prior period journals, closed invoices, historical purchase/sales history) is not included by default and is separately scoped where required."

---

### BU-ACU-011 — Non-PaySpace Payroll Integration Standard Position

**Priority:** HIGH | **Owner:** Acumatica BU Lead + Commercial Director | **Assumption:** ACU-PAY-008

**Context:**
ACU-PAY-008 states that non-PaySpace payroll integration "must be separately scoped" but does not define APPSolve's standard commercial position. The BU Lead and Commercial Director need to agree whether APPSolve will accept non-PaySpace payroll engagements and under what terms.

> **Note:** Regardless of this decision, the BeBanking Acumatica payroll rule is PERMANENT: BeBanking Payroll H2H is supported from Oracle EBS and PaySpace only. Acumatica payroll is not a BeBanking source. This decision does not affect that rule.

**Current wording (ACU-PAY-008):**
> "Clients using alternative South African payroll systems... require a separate payroll integration assessment at pre-sales. Non-PaySpace payroll integration is not covered by the ACU-PAY assumptions and must be separately scoped and explicitly included in the SOW."

**Options:**

| Option | Standard position | Commercial implication |
|---|---|---|
| (a) PaySpace only — decline non-PaySpace engagements | APPSolve will not scope Acumatica integrations to non-PaySpace payroll | Simplest; loses revenue from clients using VIP, Sage, SimplePay etc. |
| **(b) PaySpace standard; non-PaySpace assessed as custom at pre-sales** *(Recommended)* | PaySpace is the standard; any other payroll is a custom integration assessed before commitment | Balanced — protects standard scope; enables non-standard with appropriate assessment and pricing |
| (c) PaySpace + Sage Business Cloud Payroll as dual standards | Two standard integrations defined | Requires maintained Sage integration competency; increases standard scope |
| (d) Any SA payroll with REST or SFTP API — assessed per engagement | Open policy | Maximum flexibility; BU Lead assessment required for all non-PaySpace |

**Recommendation:** Option (b). PaySpace is the confirmed standard. Non-PaySpace clients are commercially valid opportunities but require individual pre-sales assessment of effort, risk, and competency. Option (b) does not close the door on non-PaySpace business but protects APPSolve from incorrectly scoping or under-pricing these integrations.

**Exact wording to approve (if option b):**
> "PaySpace is APPSolve's standard Acumatica payroll integration target. Proposals for clients using PaySpace as their payroll system follow the standard ACU-PAY assumptions. Clients using a payroll system other than PaySpace require a pre-sales payroll integration assessment by the Acumatica BU Lead before scope and effort can be confirmed. Non-PaySpace payroll integration is not covered by the standard ACU-PAY assumptions and is explicitly scoped and priced in the SOW. APPSolve does not guarantee integration capability for all payroll systems — capability is confirmed during the pre-sales assessment."

---

### BU-ACU-012 — POPIA Data Residency Disclosure

**Priority:** HIGH | **Owner:** Acumatica BU Lead | **Assumption:** ACU-SEC-003

**Context:**
ACU-SEC-003 already notes that data residency is outside APPSolve's control and that clients must confirm Acumatica's data residency position. BU-ACU-012 asks whether this disclosure should be mandatory in every proposal or conditional on client sector.

**Current wording (ACU-SEC-003):**
> "South African clients with regulatory requirements for data residency, data sovereignty, or POPIA compliance... must confirm Acumatica's data residency options and data processing agreements directly with Acumatica before engagement commences. APPSolve will assist with pre-sales data residency discussions but cannot contractually guarantee South African data residency for Acumatica SaaS."

**Options:**

| Option | Scope of disclosure | Risk if not disclosed |
|---|---|---|
| **(a) Mandatory in all Acumatica proposals** *(Recommended)* | Every proposal | Low — broadest protection for APPSolve |
| (b) Regulated-industry clients only (financial services, health, government) | Sector-filtered | Non-regulated clients may still have POPIA obligations; sector filtering introduces inconsistency |
| (c) Refer client to Acumatica privacy policy — no APPSolve disclosure | No APPSolve disclosure | Highest risk — APPSolve is the proposal author; omitting disclosure shifts liability perception to APPSolve |

**Recommendation:** Option (a). A standard POPIA data residency clause costs nothing to include in every proposal and provides clear evidence of disclosure. Attempting to filter by industry introduces judgment calls at pre-sales that may be wrong. Any Acumatica SaaS client is subject to POPIA if they process personal data — which every organisation does.

**Exact wording to approve (if option a):**
> "Acumatica's cloud SaaS platform hosts client data in Acumatica's infrastructure. APPSolve does not control data residency for Acumatica SaaS. South African clients with POPIA or data sovereignty obligations must obtain and review Acumatica's current Data Processing Agreement and confirm that Acumatica's data residency options meet their regulatory requirements before implementation commences. APPSolve can facilitate introductions to Acumatica's data privacy team but cannot provide contractual data residency guarantees for the Acumatica platform."

---

### BU-ACU-005 — Parallel Run Default

**Priority:** MEDIUM | **Owner:** Acumatica BU Lead | **Assumption:** ACU-CUT-002

**Context:**
ACU-CUT-002 already states that parallel run is "not assumed by default." BU-ACU-005 asks the BU Lead to formally confirm this position so it can be locked as an approved default rather than remaining a draft position.

**Current wording (ACU-CUT-002):**
> "Parallel run... is not assumed by default for Acumatica implementations. Parallel run is a high-effort activity that requires double data entry and reconciliation. If the client requires a parallel run, this is explicitly included in the SOW..."

**Options:** (a) Excluded by default *(Recommended and already in draft)*; (b) Included for first month end; (c) Client's decision with APPSolve assistance.

**Recommendation:** Option (a) — confirm the current draft position. Parallel runs are resource-intensive and create client dependency risks. They should be explicitly included in the SOW if required.

**Exact wording to approve:** Confirm current ACU-CUT-002 wording as approved.

---

### BU-ACU-006 — Standard Reports Per Module

**Priority:** MEDIUM | **Owner:** Acumatica BU Lead | **Assumption:** ACU-REP-001, ACU-CFG-005

**Context:**
ACU-REP-001 includes "standard Acumatica reports" but does not cap the count. In practice, Acumatica ships with hundreds of standard reports. The BU Lead needs to confirm what "standard" means in APPSolve proposals — all Acumatica factory reports, or a curated set.

**Current wording (ACU-REP-001):**
> "Standard Acumatica reports (financial statements, aging reports, inventory reports, purchase and sales reports) are included in the standard implementation. APPSolve configures the standard report set for each module in scope. Custom reports outside the standard Acumatica report library are delivered using Report Designer and are separately scoped."

**Options:** (a) Standard Acumatica library (all factory reports — no custom development); (b) Curated set of 5–10 key reports per module; (c) Reports defined during Scope & Design with no default count.

**Recommendation:** Option (a). "Standard Acumatica reports" means all factory-delivered reports — these require activation and permissions configuration, not custom development. Custom Report Designer output is already separately scoped in ACU-REP-001. This is the cleanest position. Option (b) would require maintaining a published list per module.

**Exact wording to approve (if option a):**
> "APPSolve activates and configures Acumatica's standard report library for each module in scope. Standard reports are those shipped with Acumatica — no custom Report Designer development is included by default. Custom reports, modified standard reports, and additional GIs beyond the agreed set are a Change Request."

---

### BU-ACU-007 — Training Delivery Format Default

**Priority:** MEDIUM | **Owner:** Acumatica BU Lead | **Assumption:** ACU-TRN-002

**Context:**
ACU-TRN-002 already states that "APPSolve's standard delivery format is virtual facilitated training" and that on-site training incurs additional costs. BU-ACU-007 asks the BU Lead to formally confirm this as the approved default.

**Current wording (ACU-TRN-002):**
> "APPSolve's standard delivery format is virtual facilitated training. On-site training incurs travel and accommodation costs, which are billed separately."

**Options:** (a) Virtual as standard *(Recommended and already in draft)*; (b) On-site by default; (c) Client chooses; (d) Hybrid.

**Recommendation:** Option (a) — confirm the current draft position. Virtual training is more cost-effective for clients and eliminates unbudgeted travel costs. On-site training should remain available as a priced option.

**Exact wording to approve:** Confirm current ACU-TRN-002 wording as approved.

---

### BU-ACU-008 — Hypercare Duration Standard

**Priority:** MEDIUM | **Owner:** Acumatica BU Lead | **Assumption:** ACU-CUT-005

**Context:**
ACU-CUT-005 states "standard: four weeks" but this is a draft assumption. The BU Lead must confirm whether 4 weeks is correct for Acumatica or whether it should differ from other packs.

> **Cross-pack alignment note:** Oracle HCM Base and AMS Pack both use a 4-week hypercare standard. Acumatica should align unless there is a specific reason to differ (e.g., shorter implementations justify shorter hypercare).

**Current wording (ACU-CUT-005):**
> "APPSolve provides hypercare support for a defined period after go-live (standard: four weeks). Hypercare covers: answering user queries, resolving configuration defects, and providing guidance on Acumatica operations."

**Options:** (a) 2 weeks; **(b) 4 weeks** *(Recommended)*; (c) 6 weeks; (d) Module-dependent.

**Recommendation:** Option (b) — confirm the 4-week standard. Consistent with other packs. Shorter (2 weeks) is insufficient for full-suite implementations. Longer (6 weeks) creates AMS transition delays and resource allocation challenges.

**Exact wording to approve:** Confirm current ACU-CUT-005 wording as approved (four weeks standard).

---

### BU-ACU-014 — APPSolve Project Manager Inclusion Default

**Priority:** MEDIUM | **Owner:** Acumatica BU Lead | **Assumption:** ACU-GEN-010

**Context:**
ACU-GEN-010 states that a dedicated PM is "included where explicitly stated in the SOW" — i.e., not by default. The BU Lead needs to confirm this position or select a different default. For small single-module implementations, a separate PM is usually not warranted. For full-suite or multi-module implementations, a PM is essential.

**Current wording (ACU-GEN-010):**
> "A dedicated APPSolve Project Manager is included where explicitly stated in the SOW. Where a dedicated APPSolve Project Manager is not in scope, the client's Project Manager is responsible for overall project coordination..."

**Options:**

| Option | PM included by default for... | Cost impact |
|---|---|---|
| (a) Always included | All implementations | +10–25% per project; overpriced for simple single-module implementations |
| **(b) Full-suite or multi-module implementations only** *(Recommended)* | Implementations with 3+ modules or >R500k SOW value | Appropriate resourcing calibrated to scope complexity |
| (c) Never by default — Lead Consultant acts as PM | All implementations | Risk of PM gap on complex projects; delivery risk |
| (d) Above a commercial value threshold | Value-based | Requires Commercial Director to set the threshold |

**Recommendation:** Option (b). A dedicated PM on a single-module implementation adds cost without proportionate value. A full-suite implementation without a dedicated PM creates coordination risk. Option (b) calibrates PM inclusion to implementation complexity. The BU Lead should define "multi-module" (recommend: 3 or more Acumatica modules in scope).

**Exact wording to approve (if option b):**
> "APPSolve includes a dedicated Project Manager for Acumatica implementations with three or more modules in scope, or for any implementation where the SOW value exceeds an agreed threshold confirmed by the Commercial Director. Single-module or two-module implementations are managed by the Lead Consultant, who acts as the APPSolve delivery lead without a separately defined PM role. A dedicated APPSolve PM may be included in any implementation where the client or APPSolve delivery lead identifies a project management risk."

---

### BU-ACU-015 — Multi-Entity Consolidated Reporting

**Priority:** MEDIUM | **Owner:** Acumatica BU Lead | **Assumption:** ACU-ORG-006

**Context:**
ACU-ORG-006 already states that consolidated reporting "is not assumed by default for multi-entity implementations and is separately scoped." The BU Lead needs to confirm this as the approved default.

**Current wording (ACU-ORG-006):**
> "Consolidated financial reporting across multiple Acumatica entities... requires consolidation ledger configuration and inter-company elimination rules. Consolidated reporting is not assumed by default for multi-entity implementations and is separately scoped."

**Options:** (a) Always included for multi-entity (up to 5 entities); **(b) Always separately scoped** *(Recommended and already in draft)*; (c) Included up to 3 entities, separately scoped above.

**Recommendation:** Option (b) — confirm the current draft position. Consolidation effort is highly variable depending on the number of entities, elimination rules, chart of accounts alignment, and reporting requirements. It should always be explicitly scoped and priced.

**Exact wording to approve:** Confirm current ACU-ORG-006 wording as approved.

---

## Section 5 — Promotion Impact Assessment

### If All 13 Decisions Are Resolved

| Metric | Current | After Promotion |
|---|---|---|
| Acumatica pack status | Draft | **Approved v1.0** |
| Assumptions available for proposals | 0 (Acumatica pack not usable) | **152** |
| Approved packs | 6 of 11 | **7 of 11** |
| Approved assumptions | 730 | **882** |
| Pending assumptions | 325 | **173** (HCM modules only) |
| Outstanding BU decisions | 34 | **21** (HCM modules only) |
| Programme readiness | 55% (6/11 packs) | **64% (7/11 packs)** |

### What Cannot Be Done Until Pack Is Approved

- Any Acumatica proposal assembled from the Tender Factory
- Citing Acumatica assumptions in formal SOW documents
- Using the Acumatica BOM-to-assumption mapping in TENDER_ASSUMPTION_ASSEMBLY_RULES.md
- Assembling Acumatica + BeBanking joint proposals (BeBanking pack is Approved; Acumatica pack is not)

---

## Section 6 — Approval Checklist

### Decisions Requiring Acumatica BU Lead Only

| Decision | Can BU Lead approve independently? |
|---|---|
| BU-ACU-001 | Yes — standard integration method position |
| BU-ACU-002 | Yes — tier definitions alignment decision |
| BU-ACU-003 | Yes — BI connector scope decision |
| BU-ACU-005 | Yes — confirm current draft wording |
| BU-ACU-006 | Yes — confirm standard reports = factory library |
| BU-ACU-007 | Yes — confirm virtual training as standard |
| BU-ACU-008 | Yes — confirm 4-week hypercare |
| BU-ACU-010 | Yes — opening balances only (aligns with Oracle packs) |
| BU-ACU-012 | Yes — mandatory POPIA disclosure |
| BU-ACU-014 | Yes — PM inclusion threshold (if option b chosen) |
| BU-ACU-015 | Yes — confirm separately scoped |

### Decisions Requiring Commercial Director Input

| Decision | Why CD involvement needed |
|---|---|
| BU-ACU-011 | Non-PaySpace policy has pricing and commercial boundary implications; CD must agree the policy for declining or accepting non-standard integrations |
| BU-ACU-014 | If option (d) chosen (value threshold), CD must set the monetary threshold |

### Decisions That Can Be Closed Immediately (Pre-workshop)

The following 5 decisions have clear recommended defaults that match current draft wording. The BU Lead may confirm these by email without a workshop:

| Decision | Action |
|---|---|
| BU-ACU-005 | Confirm parallel run excluded by default — current draft wording approved |
| BU-ACU-006 | Confirm standard Acumatica report library as standard scope |
| BU-ACU-007 | Confirm virtual training as standard — current draft wording approved |
| BU-ACU-008 | Confirm 4-week hypercare — current draft wording approved |
| BU-ACU-015 | Confirm consolidated reporting always separately scoped — current draft wording approved |

### Decisions Requiring Factual Input at Workshop

| Decision | Factual input required |
|---|---|
| BU-ACU-004 | BU Lead must provide initial ISV support list at workshop (or shortly after) |
| BU-ACU-014 | BU Lead to define "multi-module" threshold (recommended: 3+ modules) |

---

## Output Summary

| Item | Value |
|---|---|
| Total decisions remaining | **13** |
| HIGH priority decisions | **7** (Wave 2 — target 2026-07-07) |
| MEDIUM priority decisions | **6** (Wave 3 — target 2026-07-28 or async) |
| Decisions requiring CD input | **1** mandatory (BU-ACU-011); 1 conditional (BU-ACU-014 option d) |
| Decisions closeable by email pre-workshop | **5** (BU-ACU-005, 006, 007, 008, 015) |
| Decisions requiring factual BU input | **2** (BU-ACU-004 ISV list; BU-ACU-014 module threshold) |
| Wave 2 workshop duration | **90 minutes** |
| Wave 3 workshop duration | **60 minutes** (or async email for 5 simple confirmations) |
| Expected decisions resolved after Wave 2 workshop | **7** (all HIGH) |
| Expected decisions resolved after Wave 3 workshop | **13** (all remaining) |
| Promotion readiness after both workshops | **Ready for Approved v1.0** |
| Programme impact | 6 → 7 approved packs; 730 → 882 approved assumptions; 34 → 21 outstanding decisions |

---

*WP15A Acumatica BU Lead Decision Workshop Pack v1.0 | 2026-06-18 | Preparation only — no pack files modified | 13 decisions covered | AI: apply decisions to ACU_BASE_ASSUMPTIONS_V1.md and ACU_ASSUMPTION_REGISTER.csv after BU Lead confirmation*
