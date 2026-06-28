---
title: WP15A.1 — Acumatica Commercial Director Review Pack
version: v1.0
status: Ready for Review
programme: WP15A.1
date: 2026-06-18
for: Commercial Director
decisions_covered: 1
decisions: BU-ACU-011
---

# Acumatica Commercial Director Review — BU-ACU-011

**To:** Commercial Director
**From:** Hein Blignaut / AI Tender Factory
**Re:** Acumatica non-PaySpace payroll engagement policy — Commercial Director input required
**Date:** 2026-06-18
**Reply by:** [Insert deadline — recommend 5 business days]

---

## Why This Requires Commercial Director Input

BU-ACU-011 determines whether APPSolve will engage clients running non-PaySpace payroll systems in Acumatica implementations. This is not a technical delivery decision — it is a **commercial policy decision** that determines which clients APPSolve will accept and which APPSolve may decline or redirect.

The BU Lead may express a delivery preference (e.g., "PaySpace is our standard, others are harder"). However, the Commercial Director must co-sign any policy that could result in APPSolve declining revenue or referring a client elsewhere. This is a commercial boundary, not an assumption governance matter.

---

## 1. Decision: BU-ACU-011 — Non-PaySpace Payroll Engagement Policy

**Decision question:** When a prospective Acumatica client runs a payroll system other than PaySpace, what is APPSolve's policy on engagement?

**Impacted pack assumption:** The Acumatica Base Pack (ACU_BASE_ASSUMPTIONS_V1.md) does not currently contain a clear policy on non-PaySpace payroll. The ACU-PAY section assumes PaySpace as the payroll integration target throughout. No assumption currently addresses what happens when a client presents with Sage Payroll 300, Sage 200, VIP Payroll, Pastel Payroll, or another SA payroll system.

---

## 2. The Options

### Option (a) — PaySpace Only: Decline Non-PaySpace Work

**Policy:** APPSolve only provides Acumatica-payroll integration services for PaySpace. Clients using other payroll systems are informed at pre-sales that payroll integration is out of scope.

**Revenue implication:** Any Acumatica prospect using non-PaySpace payroll must either migrate their payroll to PaySpace (additional sale opportunity) or accept that Acumatica integration does not include payroll.

**Margin implication:** Highest margin protection — APPSolve only does work it has proven capability for. No risk from unfamiliar payroll APIs.

**Market implication:** Restricts addressable market to PaySpace-running businesses. Sage Payroll 300 has substantial SA market share (SME segment), as does VIP.

**Delivery implication:** Clean delivery scope. No payroll integration complexity for non-PaySpace clients.

---

### Option (b) — PaySpace Standard; Others Assessed [RECOMMENDED]

**Policy:** PaySpace is the standard Acumatica payroll integration target. Clients using other payroll systems are assessed at pre-sales for integration feasibility. Where feasible, integration is scoped as a Custom Integration project (higher rate). Where not feasible, payroll integration is excluded from scope.

**Revenue implication:** APPSolve retains flexibility to engage non-PaySpace clients. Custom integration projects are typically higher-margin than standard integrations.

**Margin implication:** Assessment gate prevents APPSolve from committing to integrations it cannot deliver. Custom integration pricing covers the added complexity.

**Market implication:** Broadest addressable market. APPSolve can engage any Acumatica prospect regardless of current payroll stack.

**Delivery implication:** Requires pre-sales technical assessment for non-PaySpace clients. BU Lead (or senior consultant) must be available to assess feasibility before SOW sign-off.

**Recommended wording for pack:**
> "APPSolve's standard Acumatica payroll integration target is PaySpace. Clients using other SA payroll systems (Sage Payroll 300, Sage 200, VIP Payroll, Pastel Payroll) are assessed for integration feasibility at pre-sales. Where API or file-based integration is technically feasible, payroll integration is delivered as a Custom Integration (separately scoped and priced). Where integration is not technically feasible, payroll integration is excluded from the Acumatica implementation scope."

---

### Option (c) — PaySpace + Sage Payroll 300 as Dual Standard

**Policy:** APPSolve maintains two standard integration paths: PaySpace (primary) and Sage Payroll 300 (secondary). Both are included in standard integration scope. Other payroll systems are assessed as per option (b).

**Revenue implication:** Expands standard scope — Sage Payroll 300 integrations are quoted as standard, not custom.

**Margin implication:** Lower margin for Sage Payroll 300 work (standard rate vs. custom rate). Risk if Sage API changes.

**Market implication:** Covers both dominant SA SME payroll vendors.

**Delivery implication:** Requires APPSolve to maintain Sage Payroll 300 integration skills alongside PaySpace skills. Two integration paths to document and support.

---

### Option (d) — Any SA Payroll with API: Full Openness

**Policy:** APPSolve will integrate Acumatica with any SA payroll system that provides a documented API or file-based integration method.

**Revenue implication:** Maximum market. No client excluded on payroll grounds.

**Margin implication:** Highest risk — APPSolve commits to integrations without knowing the payroll vendor's API stability, documentation quality, or support model.

**Market implication:** Broadest possible engagement.

**Delivery implication:** Cannot be standardised. Every non-PaySpace integration is custom. Resource planning for pre-sales assessment and delivery becomes unpredictable.

---

## 3. Recommendation

**Option (b) — PaySpace standard; non-PaySpace assessed as custom.**

Rationale:
1. **Protects delivery standards** without turning away revenue. The assessment gate is a controlled filter.
2. **Custom pricing for non-PaySpace** ensures higher complexity work is appropriately priced rather than absorbed into standard scope.
3. **Consistent with option (c) spirit** — Sage Payroll 300 can be added as a secondary standard in a later iteration once APPSolve has delivery evidence for it. Starting with option (b) doesn't close that door.
4. **Aligns with how AMS Pack handles integration tiers** — standard vs. custom is an established APPSolve commercial principle.

---

## 4. Commercial Impact Analysis

| Scenario | Option (a) | Option (b) | Option (c) | Option (d) |
|---|---|---|---|---|
| Client uses PaySpace | In scope | In scope | In scope | In scope |
| Client uses Sage Payroll 300 | Out of scope | Custom (assessed) | In scope | In scope |
| Client uses VIP Payroll | Out of scope | Custom (assessed) | Custom (assessed) | In scope |
| Client uses Pastel Payroll | Out of scope | Custom (assessed) | Custom (assessed) | In scope |
| Revenue at risk | HIGH | LOW | LOW | NONE |
| Margin risk | NONE | LOW | MEDIUM | HIGH |
| Delivery risk | NONE | LOW | MEDIUM | HIGH |

---

## 5. Specific Question for Commercial Director

**What is APPSolve's commercial policy on non-PaySpace payroll integration for Acumatica clients?**

Please confirm one of the following or provide your own wording:

**[ ] Option (a):** PaySpace only — non-PaySpace out of scope, no exceptions.

**[ ] Option (b) — Recommended:** PaySpace standard; non-PaySpace assessed at pre-sales and scoped as Custom Integration where feasible.

**[ ] Option (c):** PaySpace + Sage Payroll 300 as dual standard; other payroll assessed as per option (b).

**[ ] Option (d):** Any SA payroll with API — standard or custom depending on integration complexity.

**[ ] Custom position:** _______________

---

## 6. Next Steps After Commercial Director Confirmation

1. Commercial Director confirms option (or provides amended wording).
2. BU Lead is notified of the confirmed position.
3. AI updates the relevant ACU-PAY assumption with approved policy wording.
4. BU-ACU-011 is marked Resolved in GOVERNANCE_MASTER_DECISION_REGISTER.md.
5. Decision Record DR_BU-ACU-011.md is created.

If confirmed at the same time as the BU Lead email approval pack (10 Category A items), the Acumatica Base Pack will be ready for the final 2-item workshop (BU-ACU-004 ISV list, BU-ACU-014 PM threshold). After that workshop, pack promotion to Approved v1.0 can proceed.

---

> **Note to AI:** When Commercial Director confirms, create DR_BU-ACU-011.md per GOVERNANCE_DECISION_RECORD_TEMPLATE.md. Update ACU_BASE_ASSUMPTIONS_V1.md with confirmed payroll engagement policy. Update GOVERNANCE_MASTER_DECISION_REGISTER.md and GOVERNANCE_DASHBOARD.md (outstanding: 34→33; Acumatica: 13→12). Do not mark pack as approved — that follows completion of all 13 decisions plus formal BU Lead promotion session.

---

*WP15A.1 Acumatica Commercial Review Pack v1.0 | 2026-06-18 | 1 decision (BU-ACU-011) | For Commercial Director*
