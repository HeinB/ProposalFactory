---
title: WP15A.1 — Acumatica Email Approval Pack
version: v1.0
status: Ready for Dispatch
programme: WP15A.1
date: 2026-06-18
for: Acumatica BU Lead
decisions_covered: 10
decisions: BU-ACU-001, 002, 003, 005, 006, 007, 008, 010, 012, 015
---

# Acumatica BU Lead — Governance Decision Approval Request

**To:** Acumatica BU Lead
**From:** Hein Blignaut / AI Tender Factory
**Re:** Acumatica Base Assumption Pack — 10 governance decisions for email approval
**Date:** 2026-06-18
**Reply by:** [Insert deadline — recommend 5 business days]

---

## How to Respond

Each item below has a recommendation and approval options. For each item, reply with:
- **"Approved"** — confirms the recommended position exactly as written
- **"Approved with amendment: [your wording]"** — confirms the decision but changes the wording
- **"Rejected — defer to workshop"** — places this item on the workshop agenda instead

A single reply email covering all 10 items is sufficient. Reference item numbers (e.g., "Item 1: Approved, Item 2: Approved, Item 3: Approved with amendment...").

Once replies are received, the AI will apply all confirmed decisions to the Acumatica Base Assumption Pack and update the governance register. No further action is required from you after your reply.

**After this email pack, only 2 items remain for workshop discussion (ISV support list + PM threshold) and 1 item requires a brief Commercial Director review (non-PaySpace payroll policy). Those are covered in separate documents.**

---

## Item 1 — BU-ACU-001: PaySpace Integration Method Standard

**Decision:** What is APPSolve's standard Acumatica-PaySpace integration method?

**Background:** The pack currently lists all integration methods as options to be confirmed during Scope & Design. This is a correct position — the right method depends on the client's PaySpace licence tier. However, formalising this as our stated policy removes ambiguity from proposals.

**Current draft wording (ACU-PAY-004):**
> "The Acumatica-PaySpace integration uses one of the following methods, confirmed during Scope & Design: (a) API integration; (b) custom middleware; (c) structured file-based import; (d) manual journal import. The method is confirmed before SOW sign-off."

**Recommended position:**
> APPSolve's Acumatica-PaySpace integration method is confirmed at pre-sales based on the client's PaySpace licence tier and IT environment. API integration is recommended where the client's PaySpace licence includes API access. File-based integration is used where API access is unavailable. The confirmed method is documented in the SOW.

**Why recommended:** This protects APPSolve from committing to API integration for clients who cannot support it, while keeping proposals specific enough to be credible.

**Impact if approved:** ACU-PAY-004 is updated to reflect confirmed method-at-pre-sales policy. No effort impact on current engagements.
**Impact if rejected / deferred:** Pack retains open-ended wording; proposals list four methods with no standard position.

**[ ] Approved as recommended**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Item 2 — BU-ACU-002: Integration Tier Definitions

**Decision:** Should Acumatica integration complexity tiers align with the AMS Pack (Simple / Standard / Complex)?

**Background:** ACU-INT-001 references integration tiers but the AMS Pack tiers are the existing approved standard. This decision is whether to formally adopt AMS Pack tiers for Acumatica rather than defining separate ones.

**Current draft wording (ACU-INT-001):**
> "The standard integration complexity tiers apply: Simple (standard Acumatica connector or simple API), Standard (custom API with mapping), Complex (multi-step workflow, transformation logic, event-driven). [BU-ACU-002 pending]"

**Recommended position:**
> Adopt AMS Pack tier definitions exactly. No separate Acumatica tiers. Remove the pending tag and confirm the draft tier descriptions as the approved standard.

**Why recommended:** Consistent vocabulary across all packs reduces confusion when cross-selling Acumatica + AMS services. The descriptions in the draft already match AMS Pack intent.

**Impact if approved:** ACU-INT-001 pending tag removed; tier definitions locked as approved.
**Impact if rejected / deferred:** Integration tiers remain draft; pricing inconsistency risk between Acumatica and AMS proposals.

**[ ] Approved as recommended**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Item 3 — BU-ACU-003: Power BI / BI Connector Scope

**Decision:** Is Power BI or other BI tool connector configuration included in the standard Acumatica implementation?

**Background:** ACU-REP-004 already excludes BI integration from standard scope. This decision confirms that exclusion as the permanent approved position.

**Current draft wording (ACU-REP-004):**
> "External BI tool integration (Power BI, Tableau, QlikView) with Acumatica data is not included in the standard implementation... separately scoped using Acumatica's OData feed or Direct SQL access... [BU-ACU-003 pending]"

**Recommended position:**
> Confirm existing exclusion. BI connector configuration is always separately scoped and quoted as a distinct line item. Remove the pending tag.

**Why recommended:** BI connectivity effort is highly variable by client. Including it by default creates scope disputes. Clients who want BI clearly see it as a priced option, which is commercially cleaner.

**Impact if approved:** ACU-REP-004 confirmed as approved; BI tools always separately scoped.
**Impact if rejected / included as standard:** Power BI connector adds ~2–4 days to every implementation scope.

**[ ] Approved — BI tools always separately scoped (recommended)**
**[ ] Approved with amendment:** _______________
**[ ] Rejected — include Power BI connector as standard**
**[ ] Deferred to workshop**

---

## Item 4 — BU-ACU-005: Parallel Run Default

**Decision:** Is parallel run (running legacy system alongside Acumatica post-go-live) included or excluded by default?

**Background:** ACU-CUT-002 already states that parallel run is "not assumed by default." This decision formally confirms that position.

**Current draft wording (ACU-CUT-002):**
> "Parallel run... is not assumed by default for Acumatica implementations. Parallel run is a high-effort activity that requires double data entry and reconciliation. If the client requires a parallel run, this is explicitly included in the SOW with defined duration and scope. APPSolve assists with the first parallel run reconciliation cycle only — subsequent cycles are the client's responsibility."

**Recommended position:** Confirm current wording as the approved default.

**Why recommended:** Consistent with Oracle HCM and ERP Pack defaults. Parallel runs inflate scope unpredictably and should always be explicitly scoped.

**Impact if approved:** ACU-CUT-002 pending tag removed; parallel run excluded by default.
**Impact if rejected / included by default:** Every Acumatica proposal includes parallel run scope; effort increases by 3–8 days per implementation.

**[ ] Approved — parallel run excluded by default (recommended)**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Item 5 — BU-ACU-006: Standard Reports Per Module

**Decision:** What does "standard reports" mean in an Acumatica implementation — all factory-delivered Acumatica reports, or a curated subset?

**Background:** ACU-REP-001 states that "standard Acumatica reports" are included. The question is whether this means activating and configuring all of Acumatica's factory-delivered report library (for each module in scope) or a curated set.

**Current draft wording (ACU-REP-001):**
> "Standard Acumatica reports (financial statements, aging reports, inventory reports, purchase and sales reports) are included in the standard implementation. APPSolve configures the standard report set for each module in scope. Custom reports outside the standard Acumatica report library are delivered using Report Designer and are separately scoped."

**Recommended position:**
> Standard = all Acumatica factory-delivered reports for modules in scope. Activation and permissions configuration included. Custom Report Designer development is excluded. This removes the need to maintain a curated list per module.

**Why recommended:** Acumatica's factory reports are part of the platform — configuring them is module activation, not custom development. This is the most commercially straightforward position.

**Impact if approved:** Standard scope clearly defined. No per-module report count management required.
**Impact if curated list chosen:** BU Lead must publish and maintain a report list per module; adds governance overhead.

**[ ] Approved — all factory Acumatica reports for modules in scope (recommended)**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Item 6 — BU-ACU-007: Training Delivery Format Default

**Decision:** Is APPSolve's default Acumatica training format virtual (online) or on-site?

**Background:** ACU-TRN-002 already states that virtual facilitated training is APPSolve's standard format. This decision confirms that position.

**Current draft wording (ACU-TRN-002):**
> "Training delivery format is agreed with the client before the training schedule is finalised. Standard options: on-site facilitated training, virtual facilitated training (Teams/Zoom), or self-paced training using Acumatica's Open University. APPSolve's standard delivery format is virtual facilitated training. On-site training incurs travel and accommodation costs, which are billed separately."

**Recommended position:** Confirm current wording as the approved default. Virtual is standard; on-site is available at additional cost.

**Impact if approved:** Training delivery confirmed as virtual-first. On-site requests trigger a cost addendum.
**Impact if on-site becomes standard:** Travel and accommodation costs must be budgeted in every proposal by default; significant cost increase per engagement.

**[ ] Approved — virtual facilitated training as standard (recommended)**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Item 7 — BU-ACU-008: Hypercare Duration Standard

**Decision:** What is APPSolve's standard Acumatica hypercare period?

**Background:** ACU-CUT-005 already states four weeks as the standard. The BeBanking pack (now Approved v1.0) and the Oracle HCM Base pack both use a 4-week hypercare standard. This decision confirms cross-pack alignment.

**Current draft wording (ACU-CUT-005):**
> "APPSolve provides hypercare support for a defined period after go-live (standard: four weeks). Hypercare covers: answering user queries, resolving configuration defects, and providing guidance on Acumatica operations. Hypercare does not cover new configuration, new integrations, or scope changes — these are Change Requests."

**Recommended position:** Confirm current wording as approved. Four weeks is the Acumatica standard, consistent with all other APPSolve implementation packs.

**Impact if approved:** Hypercare locked at 4 weeks across Acumatica proposals.
**Impact if shorter (2 weeks):** Some clients may be underserved post-go-live; AMS handover happens before client is stable. Higher support escalation risk.
**Impact if longer (6 weeks):** AMS transition delayed; delivery team resource tied up longer per engagement.

**[ ] Approved — 4-week hypercare standard (recommended)**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Item 8 — BU-ACU-010: Legacy Data Migration Default

**Decision:** What data is migrated to Acumatica by default — opening balances only, or historical transactions?

**Background:** The Acumatica migration section describes the 3-cycle migration process but does not explicitly define the data scope. The Oracle ERP and Oracle HCM packs both use "opening balances only" as the approved default.

**Current implied position:** Opening balances and open items as at go-live date. Historical transaction migration not assumed.

**Recommended position:**
> Data migration covers: GL opening trial balance, open AR invoices and receipts, open AP invoices and payments, open purchase orders, open sales orders, and current inventory on-hand quantities (where inventory is in scope). Historical transaction migration (prior-period journals, closed invoices, historical purchase/sales history) is not included by default and is separately scoped.

**Why recommended:** Consistent with Oracle ERP and HCM Pack defaults. Historical migration is high-effort, high-risk, and highly variable. Clients who want it should explicitly scope and pay for it.

**Impact if approved:** Acumatica migration scope clearly defined. Proposals quote opening balances as the standard data migration.
**Impact if history included by default:** Every proposal includes 12-month historical migration; adds 5–15 days per engagement; higher data quality risk.

**[ ] Approved — opening balances only (recommended)**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Item 9 — BU-ACU-012: POPIA Data Residency Disclosure

**Decision:** Should Acumatica proposals include a mandatory POPIA data residency disclosure clause?

**Background:** ACU-SEC-003 already contains the disclosure language. The question is whether to make it mandatory in every proposal or conditional on client sector.

**Current draft wording (ACU-SEC-003):**
> "South African clients with regulatory requirements for data residency, data sovereignty, or POPIA compliance... must confirm Acumatica's data residency options and data processing agreements directly with Acumatica before engagement commences. APPSolve will assist with pre-sales data residency discussions but cannot contractually guarantee South African data residency for Acumatica SaaS."

**Recommended position:** Mandatory in all proposals. No sector filtering. Standard protective clause.

**Why recommended:** Every organisation processing personal data is subject to POPIA. Acumatica is a cloud SaaS platform hosted outside APPSolve's infrastructure. APPSolve cannot guarantee data residency for any client. Including this clause costs nothing and provides APPSolve with documented evidence of disclosure.

**Impact if approved:** POPIA data residency clause appears in all Acumatica proposals as standard.
**Impact if conditional (regulated sectors only):** Requires pre-sales sector classification; increases risk of omission for clients who are technically subject to POPIA but not in a "regulated" industry.

**[ ] Approved — mandatory in all Acumatica proposals (recommended)**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Item 10 — BU-ACU-015: Multi-Entity Consolidated Reporting

**Decision:** Is consolidated financial reporting (group-level) included by default for multi-entity Acumatica implementations?

**Background:** ACU-ORG-006 already states that consolidated reporting "is not assumed by default for multi-entity implementations and is separately scoped."

**Current draft wording (ACU-ORG-006):**
> "Consolidated financial reporting across multiple Acumatica entities... requires consolidation ledger configuration and inter-company elimination rules. Consolidated reporting is not assumed by default for multi-entity implementations and is separately scoped. The number of entities, elimination rules, and reporting periods covered by consolidation are confirmed during Scope & Design and documented in the SOW."

**Recommended position:** Confirm current wording as approved. Consolidated reporting always separately scoped.

**Why recommended:** Consolidation effort is highly variable depending on entity count, chart of accounts alignment, inter-company trading volume, and elimination complexity. It should always be explicitly scoped.

**Impact if approved:** Multi-entity proposals do not include consolidation by default. Clients who need it see a clearly priced SOW line item.
**Impact if included by default:** Every multi-entity proposal includes consolidation scope; adds 5–15 days per engagement regardless of whether the client needs it.

**[ ] Approved — consolidated reporting always separately scoped (recommended)**
**[ ] Approved with amendment:** _______________
**[ ] Deferred to workshop**

---

## Summary for Reply

| Item | Decision | Your Response |
|---|---|---|
| 1 | BU-ACU-001: PaySpace integration method | |
| 2 | BU-ACU-002: Integration tier definitions | |
| 3 | BU-ACU-003: BI connector scope | |
| 4 | BU-ACU-005: Parallel run default | |
| 5 | BU-ACU-006: Standard reports | |
| 6 | BU-ACU-007: Training format | |
| 7 | BU-ACU-008: Hypercare duration | |
| 8 | BU-ACU-010: Data migration default | |
| 9 | BU-ACU-012: POPIA disclosure | |
| 10 | BU-ACU-015: Multi-entity consolidation | |

**Separate actions in parallel:**
- Commercial Director review pack (BU-ACU-011 — non-PaySpace payroll policy) — sent separately
- Workshop required: 2 items only (BU-ACU-004: ISV list; BU-ACU-014: PM threshold) — agenda attached separately

Once all 10 items above are approved, the AI will apply the changes and the Acumatica Base Pack will be ready for workshop on the remaining 2 items, after which formal promotion to Approved v1.0 can proceed.

---

> **Note to AI:** When BU Lead replies to this pack, process all confirmed decisions, update ACU_BASE_ASSUMPTIONS_V1.md and ACU_ASSUMPTION_REGISTER.csv accordingly, create Decision Records (DR_BU-ACU-001.md through DR_BU-ACU-015.md format per GOVERNANCE_DECISION_RECORD_TEMPLATE.md), and update GOVERNANCE_MASTER_DECISION_REGISTER.md and GOVERNANCE_DASHBOARD.md. Do not update `approved_for_reuse` — BU Lead sets this in the final promotion session.

---

*WP15A.1 Acumatica Email Approval Pack v1.0 | 2026-06-18 | 10 decisions | For Acumatica BU Lead response*
