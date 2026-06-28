---
document_id: WP15E-EBS-EMAIL-APPROVAL-PACK
title: "WP15E — EBS AMS Overlay: Email Approval Pack (Category A Decisions)"
version: "1.0"
status: "Awaiting BU Lead Response"
created: "2026-06-19"
created_by: "WP15E — EBS AMS Overlay Decision Harvest"
decisions_included: 6
decisions: "EBS-SLA-BU-001; EBS-DRM-BU-001; EBS-DRM-BU-002; EBS-DRM-BU-003; EBS-DRM-BU-004; EBS-DRM-BU-005"
reply_to: "AI work package (post-response)"
reply_deadline: "5 business days from dispatch"
---

# WP15E — EBS AMS Overlay: Email Approval Pack

**To:** EBS AMS BU Lead
**From:** APPSolve Tender Factory (WP15E)
**Subject:** EBS AMS Overlay Governance — 6 Decisions for Email Approval
**Reply deadline:** 5 business days

---

## Instructions

Six governance decisions require your approval before the EBS AMS SLA Overlay and EBS Dedicated Resource Model Overlay can be promoted to Approved v1.0. Each decision below:

- States the question
- Provides a recommended position with rationale
- States the impact of approval and the impact of rejection/modification
- Provides one-click approval wording for your reply

**To approve all recommended positions**, reply with:
> "I approve all recommended positions for EBS-SLA-BU-001 and EBS-DRM-BU-001 through EBS-DRM-BU-005 as stated."

**To approve with modifications**, reply with the decision ID and your preferred position for each modification.

---

## Decision 1 of 6 — EBS-SLA-BU-001

**Decision ID:** EBS-SLA-BU-001
**Pack:** EBS AMS SLA Overlay
**Assumption affected:** EBS-SLA-011 (response time table)

---

**Question:** Is the P1 15-minute response target the EBS AMS standard commitment (included by default in all EBS AMS proposals), or is it a client-configurable position (negotiated and defined in the AMS agreement schedule per engagement)?

**Recommended position:** **Client-configurable, defined in the AMS agreement schedule per engagement.**

**Rationale:** A 15-minute P1 response commitment is operationally aggressive as a universal default. Different EBS AMS clients have different risk profiles: a payroll processing client who runs nightly batch jobs has a different P1 exposure to a manufacturing client with 9-to-5 operations. Making it configurable allows APPSolve to offer 15 minutes where operationally justified (e.g., EBS on OCI with APPSolve monitoring contracted) while offering 30-minute or 1-hour options for clients with lower risk tolerance or without 24/7 monitoring.

**Impact if recommended position approved:**
The EBS-SLA-011 response time table is labelled "client-configurable" and the AMS agreement schedule becomes the definitive SLA document. APPSolve's proposal assembly instructions (TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3.5) include a note to populate P1 response target from the client's RFP or pre-sales discussion. ARM IT045 (P1=15min) remains the documented example. No change to the overlay assumption text is required — EBS-SLA-011 already states "15 minutes from ticket logging" as the target, which is correct for ARM IT045-type engagements.

**Impact if position changed to "Standard 15 minutes for all EBS AMS":**
EBS-SLA-011 would be updated to state that 15 minutes is the APPSolve EBS AMS default. This is a stronger market position but requires APPSolve to operationally guarantee 15-minute P1 response for every EBS AMS client — including those without 24/7 coverage contracted. The overlay would need a clarification that the 15-minute target applies 24/7 only where 24/7 is contracted; otherwise it applies within business hours only.

---

**One-click approval wording:**

> "I approve EBS-SLA-BU-001. Confirmed: P1 15-minute response target is client-configurable, defined in the AMS agreement schedule per engagement. The overlay should document 15 minutes as the target with a note that it is configurable."

---
---

## Decision 2 of 6 — EBS-DRM-BU-001

**Decision ID:** EBS-DRM-BU-001
**Pack:** EBS Dedicated Resource Model
**Assumptions affected:** EBS-DRM-012 (DBA hours), EBS-DRM-016 (HCM Lead hours), EBS-DRM-017 (Finance Lead hours), EBS-DRM-021 (OIC/Technical hours), EBS-DRM-025 (team total)

---

**Question:** Is the ARM IT045 team profile (SDM 40h/month + HCM Lead 240h/month + Finance Lead 160h/month + DBA+OCI 160h/month + OIC/Technical 80h/month = 680 hours/month total) the EBS AMS DRM standard, or is the hours model defined per engagement in the AMS agreement schedule?

**Recommended position:** **Per-engagement — hours model defined in the AMS agreement schedule.**

**Rationale:** The ARM IT045 model is a validated example for an EBS R12.2 client running HCM (payroll-heavy) and Finance on OCI with OIC integrations. A different EBS AMS client — for example, one running EBS Finance only with no HR modules and no OIC integrations — would not need an HCM Lead at 240h/month. Declaring the ARM model as "the standard" would either over-commit APPSolve's resources or require heavy proposal-level qualifications. A per-engagement model is more accurate, more flexible, and creates no risk of under-delivery.

**Impact if recommended position approved:**
The overlay assumptions that state specific hour minimums (EBS-DRM-012, 016, 017, 021, 025) are updated to state that the minimum hours per role are defined in the AMS agreement schedule. The ARM IT045 values (40/240/160/160/80) are documented as the reference example in the overlay's assembly pattern note. No commercial exposure is created.

**Impact if position changed to "ARM IT045 model is the EBS AMS DRM standard":**
All EBS AMS DRM proposals would default to 680 hours/month across the full 5-role team. Proposals for smaller EBS environments would need explicit scope reduction via the BU Lead. This creates pricing rigidity and may price APPSolve out of smaller EBS AMS opportunities.

---

**One-click approval wording:**

> "I approve EBS-DRM-BU-001. Confirmed: the ARM IT045 hours model is a reference example, not the EBS AMS DRM standard. Hours per role are defined per engagement in the AMS agreement schedule."

---
---

## Decision 3 of 6 — EBS-DRM-BU-002

**Decision ID:** EBS-DRM-BU-002
**Pack:** EBS Dedicated Resource Model
**Assumption affected:** EBS-DRM-030

---

**Question:** Do unused minimum hours in a given month roll over to the following month, or are they forfeited at month end?

**Recommended position:** **Forfeited — unused hours do not roll over.**

**Rationale:** Rollover is uncommon in professional services retainer models for three reasons: (a) it creates cumulative staffing demand that is difficult to plan and resource — a client who has 100h rollover and then doubles their call volume creates a peak that cannot be absorbed without additional recruitment; (b) it creates an accounts receivable complexity — rolled hours that are consumed months later are effectively services rendered in a prior period and billed in a future period, creating revenue recognition issues; (c) it motivates clients to bank hours rather than engage APPSolve proactively, which is the opposite of what a managed service relationship should look like. Forfeit is the industry standard for IT support retainer models.

**Mitigation for client concerns:** Where a client objects to forfeiture of unused hours, the SDM's monthly report (EBS-DRM-055) proactively flags underspend against the minimum so the client can redirect hours before month end. APPSolve also proposes proactive activities (EBS-DRM-056) to utilise uncommitted hours.

**Impact if recommended position approved:**
EBS-DRM-030 is confirmed as written: "unused minimum hours in a given month do not automatically roll over." Monthly billing model is clean.

**Impact if rollover is preferred:**
EBS-DRM-030 is updated to state rollover terms (e.g., 1 month rollover cap; maximum rolled hours = 20% of monthly minimum). Staffing and revenue recognition processes need updating. Commercial Director review required if rollover is chosen.

---

**One-click approval wording:**

> "I approve EBS-DRM-BU-002. Confirmed: unused minimum hours are forfeited at month end; no rollover applies unless explicitly stated in the AMS agreement."

---
---

## Decision 4 of 6 — EBS-DRM-BU-003

**Decision ID:** EBS-DRM-BU-003
**Pack:** EBS Dedicated Resource Model
**Assumptions affected:** EBS-DRM-034 (leave notice), EBS-DRM-035 (illness absorption)

---

**Question:** Are the following two operational policies confirmed as the EBS AMS DRM standard?
- **Advance leave notice:** Named resources notify the SDM of planned absences ≥ 3 consecutive days a minimum of **10 business days** in advance.
- **Illness absorption:** APPSolve absorbs unplanned illness absence up to **3 business days per named resource per calendar month** without commercial impact to the client.

**Recommended position:** **Confirm both as stated.**

**Rationale:** The 10 business day (two calendar week) advance notice is the minimum that gives the SDM enough time to arrange supplementary coverage for extended absences without disrupting the client. Any shorter notice (e.g., 5 BD) risks gaps in service for P1/P2 coverage. The 3-day illness absorption limit per resource per month is realistic for a professional services team — it corresponds to approximately one unplanned sick day per month per resource per quarter, which is within normal HR planning parameters. It also limits APPSolve's exposure: a single resource taking a week of unplanned sick leave in a month triggers the substitution procedure rather than APPSolve absorbing the full shortfall.

**Impact if confirmed:**
EBS-DRM-034 and EBS-DRM-035 are confirmed as written. No changes needed.

**Impact if policies are adjusted:**
Provide the preferred thresholds (e.g., 5 BD advance notice; 2 days illness per month) and the overlay assumptions will be updated accordingly before promotion.

---

**One-click approval wording:**

> "I approve EBS-DRM-BU-003. Confirmed: 10 business days advance leave notice and 3 business days per month illness absorption are the EBS AMS DRM standards."

---
---

## Decision 5 of 6 — EBS-DRM-BU-004

**Decision ID:** EBS-DRM-BU-004
**Pack:** EBS Dedicated Resource Model
**Assumptions affected:** EBS-DRM-039 (substitution notice), EBS-DRM-041 (equivalent grade)

---

**Question:** Two related confirmations required:
1. Is **30 business days** (six calendar weeks) the minimum notice APPSolve must provide the client for a planned permanent resource substitution?
2. Is an "equivalent grade" replacement defined as: same or greater years of Oracle EBS experience in the relevant domain; same or greater certifications; and demonstrated client-facing AMS delivery experience?

**Recommended position:** **Confirm 30 business days; confirm the proposed equivalent-grade criteria.**

**Rationale for 30 BD:** Six calendar weeks is the practical minimum for: BU Lead to identify and assess a replacement; arrange a client assessment meeting; complete the selection; and begin a structured 30-day knowledge transfer (which runs concurrent with the final weeks of the 30 BD notice period). A shorter notice period (e.g., 20 BD / 4 weeks) would compress the assessment and KT overlap uncomfortably. 30 BD is the same notice period used in senior executive contracts in South African professional services.

**Rationale for equivalent grade criteria:** The three criteria (EBS domain experience, certifications, client-facing AMS) map directly to the named resource's core value proposition in a DRM engagement. "Same role band" alone (e.g., Senior Consultant) would be insufficient — a Senior Consultant in OIC development is not equivalent to a Senior Consultant who has run EBS HCM payroll for 5 years. The proposed definition prevents grade-washing.

**Note on client approval right (EBS-DRM-040):** The overlay already states that the client has the right to assess and object to a proposed replacement. This right is preserved regardless of the notice period or grade definition confirmed here.

**Impact if confirmed:**
EBS-DRM-039 and EBS-DRM-041 are confirmed as written.

**Impact if adjusted:**
Provide preferred notice period (e.g., 20 BD) or grade definition, and the overlay will be updated accordingly.

---

**One-click approval wording:**

> "I approve EBS-DRM-BU-004. Confirmed: 30 business days minimum substitution notice. Equivalent grade = same or greater Oracle EBS domain experience, same or greater certifications, and demonstrated AMS delivery experience."

---
---

## Decision 6 of 6 — EBS-DRM-BU-005

**Decision ID:** EBS-DRM-BU-005
**Pack:** EBS Dedicated Resource Model
**Assumptions affected:** EBS-DRM-045 (runbook creation), EBS-DRM-046 (runbook domains), EBS-DRM-047 (environment documentation)

---

**Question:** Are the 30-day Knowledge Transfer (KT) period and runbook creation obligation **standard in all EBS AMS DRM engagements** (included by default and not requiring client request), or are they **on-request only** (client must specifically request them)?

**Recommended position:** **Standard in all EBS AMS DRM engagements.**

**Rationale:** The runbook is APPSolve's primary operational protection mechanism for two scenarios: (a) resource substitution — if a named resource leaves and no runbook exists, the replacement resource starts from zero, creating a dangerous knowledge gap for P1 incident response; (b) contract termination — if the client terminates the DRM agreement, APPSolve must be able to hand over the environment documentation to the client or successor service provider in an orderly way. Making runbooks "on request" means they will not exist in many engagements, creating liability for APPSolve at substitution or termination. The 30-day KT period is the minimum for a new DRM resource to be productive and safe; it cannot be omitted without increasing P1 resolution risk.

**Making KT + runbook standard creates a consistent, defensible DRM product.** It is also a differentiator in EBS AMS tender responses — most competing AMS providers do not formally commit to knowledge management or runbook obligations in their proposals.

**Impact if confirmed as standard:**
EBS-DRM-044 through EBS-DRM-047 are confirmed. The KT period and runbook creation are included in every DRM engagement's commercial scope. The SDM owns runbook delivery. No additional client charge — these are included in the DRM fee.

**Impact if changed to on-request:**
EBS-DRM-045 is updated to state that runbook creation is available on client request. The risk note above should then be documented in the APPSolve internal delivery guide for EBS AMS.

---

**One-click approval wording:**

> "I approve EBS-DRM-BU-005. Confirmed: 30-day KT period and runbook creation are standard in all EBS AMS DRM engagements. These are included in the DRM fee and not separately charged."

---

## Summary — One-Click Full Approval

If you are satisfied with all six recommended positions, reply with:

> **"I approve all six recommended positions for WP15E EBS email decisions:**
> - **EBS-SLA-BU-001:** P1 response is client-configurable per AMS agreement schedule.
> - **EBS-DRM-BU-001:** Hours model is per-engagement; ARM IT045 profile is a reference example only.
> - **EBS-DRM-BU-002:** Unused hours are forfeited at month end; no rollover.
> - **EBS-DRM-BU-003:** 10 BD advance leave notice and 3 BD/month illness absorption are confirmed as standard.
> - **EBS-DRM-BU-004:** 30 BD minimum substitution notice confirmed. Equivalent grade = Oracle EBS domain experience + certifications + AMS experience.
> - **EBS-DRM-BU-005:** 30-day KT and runbook creation are standard in all DRM engagements.
>
> Approved by: [Name] | EBS BU Lead | [Date]"**

---

## Next Steps After BU Lead Response

1. BU Lead email responses are forwarded to the AI work package.
2. AI records each decision in a Decision Record file (DR_EBS-SLA-BU-001.md etc.) per the template.
3. AI updates the EBS overlay assumption files to reflect approved positions.
4. Promotion to Approved v1.0 follows after all 9 decisions are resolved (including Category B CD review and Category C workshop).

---

*WP15E EBS Email Approval Pack v1.0 | 2026-06-19 | WP15E — EBS AMS Overlay Decision Harvest*
*6 Category A decisions | EBS BU Lead approval required | Reply deadline: 5 business days*
*Overlay packs affected: EBS_AMS_SLA_OVERLAY_V1.md; EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md*
