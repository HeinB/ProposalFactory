---
title: WP15A.1 — Acumatica Reduced Workshop Agenda
version: v1.0
status: Ready for Scheduling
programme: WP15A.1
date: 2026-06-18
for: Acumatica BU Lead
decisions_covered: 2
decisions: BU-ACU-004, BU-ACU-014
estimated_duration: 30 minutes
prerequisite: BU Lead email approval pack responses received; Commercial Director BU-ACU-011 confirmed
---

# Acumatica BU Lead — Reduced Workshop Agenda

**Session title:** Acumatica Base Pack — Final 2-Item Governance Workshop
**Estimated duration:** 30 minutes
**Recommended format:** Microsoft Teams (BU Lead + Hein Blignaut + AI note-taker)
**Schedule after:** BU Lead email approval pack responses received AND Commercial Director BU-ACU-011 confirmed

---

## Why Only 2 Items?

WP15A.1 classified all 13 outstanding Acumatica governance decisions:
- **10 decisions (Category A):** Closed by email — BU Lead confirms existing draft wording
- **1 decision (Category B):** Commercial Director review (BU-ACU-011 — non-PaySpace payroll policy) — separate pack
- **2 decisions (Category C):** Workshop required — BU Lead must **create** new content, not confirm existing content

The workshop covers only BU-ACU-004 and BU-ACU-014. The original 90-minute workshop has been reduced to 30 minutes by routing all confirmation decisions to email.

---

## Workshop Prerequisites

Before scheduling this workshop, confirm:

- [ ] BU Lead email approval pack (10 decisions) response received
- [ ] Commercial Director BU-ACU-011 response received
- [ ] BU Lead has reviewed this agenda and the two decision briefing notes below
- [ ] Hein Blignaut available as facilitator
- [ ] AI assistant active to record ISV list and PM threshold as stated

If prerequisites are not met, do not schedule the workshop — the Category A decisions need to close first so the BU Lead enters with full context on what has already been decided.

---

## Session Agenda

| Time | Item | Purpose |
|---|---|---|
| 00:00–02:00 | Opening — context reminder | Confirm 10 Category A decisions closed by email; Commercial Director BU-ACU-011 confirmed; 2 items remain |
| 02:00–15:00 | Item 1: BU-ACU-004 — ISV Support List | BU Lead states which ISVs APPSolve supports; AI records list verbatim |
| 15:00–27:00 | Item 2: BU-ACU-014 — PM Inclusion Threshold | BU Lead defines when a PM is included; AI captures the rule |
| 27:00–30:00 | Closing — approval confirmation | BU Lead confirms both items as stated; AI commits to creating Decision Records and updating pack post-session |

**Total: 30 minutes**

---

## Item 1 — BU-ACU-004: ISV Support List (13 minutes)

### What This Decision Is

Acumatica implementations often involve ISV (Independent Software Vendor) add-on products — e.g., eCommerce connectors, advanced WMS modules, payroll bridges, field service tools. APPSolve's proposals need to state which ISV products APPSolve can support (i.e., implement, configure, and maintain) and which are outside APPSolve's capability.

### Why This Cannot Close by Email

There is currently **no ISV list anywhere in the APPSolve Knowledge Base**. If the BU Lead approves "Option (a) — maintain a published ISV list" by email, the governance record says APPSolve has a list when none exists. The workshop purpose is for the BU Lead to **state the list verbally**. The AI will record it and draft it for ratification.

### Pre-Workshop Reading for BU Lead

Think through the following product categories before the session. For each, identify whether APPSolve has delivered it, can deliver it (but hasn't yet), or explicitly cannot support it:

| Category | Acumatica ISV Examples | APPSolve Status? |
|---|---|---|
| eCommerce | Bigcommerce, Shopify, WooCommerce connectors (native Acumatica or ISV) | |
| Advanced WMS | Datalinx, RF Smart | |
| Payroll (beyond PaySpace) | Greentree Payroll, other ISVs | |
| Field Service | MetaViewer, FieldPoint | |
| Document Management | Velixo, Paperless Parts | |
| Advanced Reporting | Velixo Reports, SSRS | |
| CRM Integration | HubSpot, Salesforce connectors | |
| B2B / EDI | TrueCommerce, SPS Commerce | |
| Industry-specific | Any verticals APPSolve has delivered | |

### Workshop Output Required

The AI will record the ISV list verbatim as stated by the BU Lead. After the session, the AI will:
1. Draft a formatted ISV Support Statement for inclusion in ACU_BASE_ASSUMPTIONS_V1.md
2. Create DR_BU-ACU-004.md with the confirmed list as the resolution
3. Present the draft to the BU Lead for ratification before any pack update is applied

### Decision Options (for reference during workshop)

| Option | Position | Governance approach |
|---|---|---|
| **(a) Published ISV list — Recommended** | APPSolve maintains a list of supported ISV products. Proposals only include ISVs on the list. | List created in this workshop; updated by BU Lead as capabilities grow |
| **(b) Case-by-case only** | No published list. Every ISV request assessed at pre-sales. | Lower governance overhead; higher pre-sales variability |
| **(c) No ISV support stated** | Acumatica native modules only; ISV implementations declined | Narrowest scope; safest delivery risk |

**Facilitator prompt:** "For our standard Acumatica engagement, which ISV products can we confidently include in a proposal today? Let's go category by category. I'll record everything you say."

---

## Item 2 — BU-ACU-014: PM Inclusion Threshold (12 minutes)

### What This Decision Is

For Acumatica implementations, when does APPSolve include a dedicated Project Manager? Currently, ACU-GEN-010 states: "APPSolve provides project management where explicitly stated in the SOW." This means PM inclusion is currently entirely negotiated per-deal with no published default.

BU-ACU-014 asks the BU Lead to define the **rule for when a PM is automatically included** in the standard scope — so proposals are consistent and clients know what to expect.

### Why This Cannot Close by Email

No threshold currently exists anywhere in the pack. The email approval pack can only confirm *existing* wording. BU-ACU-014 requires the BU Lead to **define a new rule** (a module count, a project value, a duration trigger, or some combination). Defining this threshold is a policy authoring task, not a confirmation task.

### Pre-Workshop Reading for BU Lead

Think through the following before the session:

1. **What has been APPSolve's actual practice?** On which past Acumatica projects was a PM engaged? What was the project size (modules, value, duration)?
2. **What is the delivery risk without a PM?** At what project size does lack of a dedicated PM create meaningful delivery risk?
3. **What is the commercial impact?** PM time is a cost. At what scope does it become justified for inclusion in standard scope?

### Workshop Output Required

The AI will record the BU Lead's stated threshold verbatim. After the session, the AI will:
1. Draft a PM inclusion rule for ACU-GEN-010 based on the stated threshold
2. Create DR_BU-ACU-014.md with the confirmed threshold as the resolution
3. Present the draft to the BU Lead for ratification before any pack update is applied

### Suggested Options (for reference during workshop)

| Option | Threshold rule | Typical scope |
|---|---|---|
| **(a) Any multi-module** | PM included for all implementations with 2+ modules in scope | Broad inclusion; PM in most Acumatica proposals |
| **(b) 3+ modules or cross-department — Recommended** | PM included when 3+ modules in scope or when >1 business department is impacted | Moderate threshold; aligns with delivery complexity |
| **(c) Value threshold** | PM included when SOW value exceeds [amount] | Commercially clean; BU Lead to define the value |
| **(d) Duration threshold** | PM included when implementation duration exceeds [weeks] | Duration-based; predictable at SOW stage |
| **(e) BU Lead discretion only** | PM included "where explicitly stated in SOW" — no automatic threshold | Current position; maintains full flexibility |

**Facilitator prompt:** "On past Acumatica projects, at what point did you feel we needed a PM? Was it a module count, a rand value, a timeline? Let me note your answer and we'll turn it into the standard rule."

---

## Post-Workshop Commitments (AI)

Within 24 hours of the session:
1. Deliver draft ISV Support Statement (ACU-GEN section — new assumption) to BU Lead for ratification
2. Deliver draft PM Inclusion Rule (updated ACU-GEN-010) to BU Lead for ratification
3. Once ratifications received, create DR_BU-ACU-004.md and DR_BU-ACU-014.md
4. Update ACU_BASE_ASSUMPTIONS_V1.md with both confirmed assumptions
5. Update GOVERNANCE_MASTER_DECISION_REGISTER.md and GOVERNANCE_DASHBOARD.md
6. Notify Hein Blignaut that all 13 decisions are resolved and Acumatica Base Pack is ready for promotion review

---

## Programme Impact After Workshop Completion

| Metric | Before Workshop | After Workshop (all 13 resolved) |
|---|---|---|
| Outstanding BU decisions | 34 | **21** (13 Acumatica closed) |
| Acumatica decisions resolved | 1 (BU-ACU-009 WP14G) | **14** (all resolved) |
| Acumatica pack status | Draft | **Ready for promotion review** |
| Approved packs | 6 | **7** (after BU Lead promotion session) |
| Approved assumptions | 730 | **~882** (730 + ~152 Acumatica) |
| Remaining outstanding decisions | 34 | **21** (Oracle HCM module packs: REC/LRN/TLT/COM) |

---

## Scheduling Note

This workshop should be **last** in the sequence:
1. BU Lead email approval pack → 10 decisions closed (can happen any time)
2. Commercial Director BU-ACU-011 → 1 decision closed (can happen in parallel)
3. **This workshop → 2 decisions closed (requires 1 and 2 complete)**
4. Post-workshop ratification → AI applies all changes (within 24h)
5. BU Lead formal promotion session → Acumatica Base Pack promoted to Approved v1.0

Estimated elapsed time from email dispatch to Approved pack: **2–3 weeks** (email response + CD review + workshop scheduling + AI application + formal promotion sign-off).

---

*WP15A.1 Acumatica Reduced Workshop Agenda v1.0 | 2026-06-18 | 2 decisions (BU-ACU-004, BU-ACU-014) | Estimated duration: 30 minutes | Prerequisite: Category A email approval pack received*
