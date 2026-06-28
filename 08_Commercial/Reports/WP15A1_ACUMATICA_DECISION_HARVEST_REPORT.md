---
title: WP15A.1 — Acumatica Decision Harvest Report
version: v1.0
status: Complete — Findings Only
programme: WP15A.1
date: 2026-06-18
author: AI (Claude)
constraint: No assumption pack content modified. No decisions resolved. No governance status changes.
---

# WP15A.1 — Acumatica Decision Harvest Report

**Programme:** WP15A.1 | **Date:** 2026-06-18 | **Findings only — no changes applied**

---

## 1. Purpose

Classify all 13 remaining Acumatica governance decisions into one of three categories to reduce the BU Lead workshop from 90 minutes to approximately 30 minutes and close the maximum number of decisions via email before the workshop is scheduled.

---

## 2. Methodology

Each decision was assessed against three criteria:

1. **Draft wording exists and is already correct** — does the current ACU pack assumption already reflect the recommended position, such that the BU Lead is being asked to confirm rather than create?
2. **Commercial Director input required** — does the decision touch pricing, margin, contractual positioning, or client selection policy?
3. **New content must be created** — does the BU Lead need to author new material (e.g., a list, a threshold, a defined policy that doesn't yet exist anywhere in the KB)?

Decisions that pass criterion 1 and fail criteria 2 and 3 are Category A.
Decisions that meet criterion 2 are Category B.
Decisions that meet criterion 3 (or require significant strategic judgement with no clear recommended default) are Category C.

---

## 3. Decision Classification Table

| ID | Title | Priority | Current Recommendation | Category | Reason |
|---|---|---|---|---|---|
| BU-ACU-001 | PaySpace integration method standard | HIGH | (c) Method confirmed at pre-sales per client | **A — Email** | Option (c) formalises current practice; no commercial impact; draft ACU-PAY-004 already lists all methods with confirmation at Scope & Design |
| BU-ACU-002 | Integration tier definitions | HIGH | (a) Align with AMS Pack tiers | **A — Email** | Purely a terminology alignment decision; AMS Pack tiers already approved; no new policy needed |
| BU-ACU-003 | BI connector scope | HIGH | (b) Always separately scoped | **A — Email** | ACU-REP-004 draft wording already excludes BI tools from standard scope; BU Lead confirming existing exclusion |
| BU-ACU-004 | ISV support list | HIGH | (a) Maintain published ISV list | **C — Workshop** | BU Lead must CREATE the initial ISV list; no list exists anywhere in the KB; approval without content is meaningless |
| BU-ACU-005 | Parallel run default | MEDIUM | (a) Excluded by default | **A — Email** | ACU-CUT-002 draft wording already states parallel run is not assumed by default; BU Lead confirming existing position |
| BU-ACU-006 | Standard reports per module | MEDIUM | (a) Standard Acumatica library | **A — Email** | ACU-REP-001 already states standard Acumatica reports are included; no cap required if standard = factory library |
| BU-ACU-007 | Training delivery format | MEDIUM | (a) Virtual facilitated as standard | **A — Email** | ACU-TRN-002 already states "APPSolve's standard delivery format is virtual facilitated training"; direct text confirmation |
| BU-ACU-008 | Hypercare duration | MEDIUM | (b) 4 weeks | **A — Email** | ACU-CUT-005 already states "standard: four weeks"; identical to Oracle HCM and AMS Pack standards; BU Lead confirming alignment |
| BU-ACU-010 | Legacy data migration default | HIGH | (a) Opening balances only | **A — Email** | Consistent with Oracle ERP and HCM Pack defaults; draft migration section implies this approach; no new policy needed |
| BU-ACU-011 | Non-PaySpace payroll policy | HIGH | (b) PaySpace standard; others assessed | **B — Commercial** | Affects which clients APPSolve will and will not engage; has direct revenue and margin implications; Commercial Director must co-sign the "decline or assess" policy |
| BU-ACU-012 | POPIA data residency disclosure | HIGH | (a) Mandatory in all proposals | **A — Email** | ACU-SEC-003 draft wording already contains the disclosure; BU Lead is confirming existing protective wording as the mandatory standard |
| BU-ACU-014 | APPSolve PM inclusion default | MEDIUM | (b) Full-suite / multi-module only | **C — Workshop** | BU Lead must DEFINE the module threshold (e.g., 3+ modules) and/or value threshold; no threshold exists in any KB document; this requires active policy creation |
| BU-ACU-015 | Multi-entity consolidated reporting | MEDIUM | (b) Always separately scoped | **A — Email** | ACU-ORG-006 already states "not assumed by default for multi-entity implementations and is separately scoped"; BU Lead confirming existing position |

---

## 4. Classification Summary

| Category | Count | Decisions |
|---|---|---|
| **A — Email Approval** | **10** | BU-ACU-001, 002, 003, 005, 006, 007, 008, 010, 012, 015 |
| **B — Commercial Review** | **1** | BU-ACU-011 |
| **C — Workshop Required** | **2** | BU-ACU-004, 014 |

---

## 5. Why Category A Decisions Can Close by Email

All 10 Category A decisions share the same structural characteristic: **the recommended wording already exists in draft form within ACU_BASE_ASSUMPTIONS_V1.md.** The BU Lead is not being asked to invent a policy — they are being asked to endorse one. This is a materially different cognitive load and does not warrant a scheduled workshop.

The email approval pack (WP15A1_ACUMATICA_EMAIL_APPROVAL_PACK.md) presents each decision as a single confirmation page. The BU Lead's reply can be as simple as "Approved as recommended" against each item number.

---

## 6. Why BU-ACU-011 Requires the Commercial Director

BU-ACU-011 determines whether APPSolve will engage clients using non-PaySpace payroll. Option (b) — "PaySpace standard; non-PaySpace assessed as custom integration at pre-sales" — is commercially reasonable but implies that APPSolve will sometimes decline non-PaySpace work. That is a commercial policy, not an assumption governance decision. The Commercial Director must co-sign any client engagement policy that restricts revenue opportunities.

The BU Lead may express a delivery preference but cannot alone bind APPSolve's commercial position on engagement acceptance.

---

## 7. Why BU-ACU-004 and BU-ACU-014 Cannot Close by Email

**BU-ACU-004 (ISV support list):** Option (a) says "maintain a published ISV support list." The list is the decision. No list currently exists in the KB, in any governance document, or in any AI-accessible source. Approving option (a) without the list produces a governance entry that says "we have a list" when we don't. The workshop purpose is to have the BU Lead state which ISV products APPSolve supports — verbally, with AI taking minutes and drafting the list for ratification.

**BU-ACU-014 (PM inclusion threshold):** The recommended option (b) says "full-suite or multi-module implementations only." But "multi-module" is undefined. APPSolve needs to decide: is 2 modules "multi"? Is 3? Is the trigger a module count, a commercial value threshold, or both? This requires the BU Lead to make a judgment call that involves knowing APPSolve's typical project sizes, client expectations, and delivery model. It cannot be resolved by confirming existing wording because no threshold currently exists in the pack.

---

## 8. Cross-Pack Alignment Notes

| Decision Pair | Alignment Note |
|---|---|
| BU-ACU-008 (hypercare) + BU-BB-004 (BeBanking hypercare) | Both now resolved as 4 weeks. BeBanking WP14D confirmed 4-week hypercare. BU-ACU-008 email approval should note alignment with BeBanking standard. |
| BU-ACU-012 (POPIA disclosure) + BU-BB-009 (BeBanking POPIA) | BeBanking POPIA disclosure resolved WP14D. Acumatica POPIA wording should use consistent language. Email approval pack includes aligned wording. |
| BU-ACU-002 (tier definitions) + AMS Pack tiers | AMS Pack tiers are Approved v1.0. BU-ACU-002 simply adopts them — no conflict. |

---

## 9. Residual Risk: What Happens if Email Approvals Are Ignored

If the BU Lead does not respond to the email approval pack, the pack remains in Draft status. The 10 Category A decisions will not self-resolve. The workshop would then need to cover all 13 decisions, which is the current position.

Recommended escalation: If no response within 5 business days of email dispatch, schedule a 30-minute call to walk through the Category A pack together. The BU Lead can approve verbally; AI documents confirmation.

---

*WP15A.1 Decision Harvest Report v1.0 | 2026-06-18 | Findings only — no pack content modified | A:10 / B:1 / C:2*
