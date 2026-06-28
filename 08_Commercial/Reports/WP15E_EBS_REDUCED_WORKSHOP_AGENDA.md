---
document_id: WP15E-EBS-REDUCED-WORKSHOP-AGENDA
title: "WP15E — EBS AMS Overlay: Reduced Workshop Agenda (Category C Decisions)"
version: "1.0"
status: "Draft — Schedule After Email + CD Review Complete"
created: "2026-06-19"
created_by: "WP15E — EBS AMS Overlay Decision Harvest"
decisions_to_resolve: 2
decision_ids: "EBS-SLA-BU-002; EBS-SLA-BU-003"
attendees_required: "EBS BU Lead + Commercial Director"
target_duration: "15 minutes"
prerequisite: "EBS BU Lead email responses received; EBS-SLA-BU-004 CD review complete"
---

# WP15E — EBS AMS Overlay: Reduced Workshop Agenda

**Workshop type:** Joint Decision Session — EBS BU Lead + Commercial Director
**Target duration:** 15 minutes
**Decisions to resolve:** 2 (EBS-SLA-BU-002 + EBS-SLA-BU-003)
**Prerequisite:** Category A email responses received from BU Lead; EBS-SLA-BU-004 CD review complete

---

## Why This Workshop is Necessary

Seven of the nine EBS AMS overlay decisions can be resolved independently by the BU Lead (email) or the Commercial Director (written review). These two decisions cannot:

**EBS-SLA-BU-002 (Resolution time SLAs)** and **EBS-SLA-BU-003 (24/7 commercial structure)** each require the BU Lead and Commercial Director to reach a shared position — because the operational answer (BU Lead) and the commercial answer (CD) are interdependent. Resolving them sequentially by email would require two full email cycles (BU Lead responds → CD reviews BU Lead's answer → CD responds → alignment confirmed), adding 5–10 business days and creating a risk of misalignment that requires a third exchange. A 15-minute joint session resolves both in one step.

**The workshop has been reduced to 2 agenda items covering exactly these interdependencies.** No other decisions are on the agenda — all others have been routed to faster channels.

---

## Pre-Workshop Preparation

### For BU Lead (complete before attending)

- [ ] Review EBS_AMS_SLA_OVERLAY_V1.md Section 4 (Resolution Time Commitments, EBS-SLA-016 through EBS-SLA-020)
- [ ] Review EBS_AMS_SLA_OVERLAY_V1.md Section 5 (24/7 Coverage Model, EBS-SLA-021 through EBS-SLA-027)
- [ ] Answer pre-read question A: Of the EBS AMS P1 incidents APPSolve has handled (including ARM IT045), what percentage were resolved within 2 hours? What are the most common reasons a 2-hour resolution is missed?
- [ ] Answer pre-read question B: How is the EBS AMS on-call roster currently structured? Fixed dedicated person? Rotation across a pool? What is APPSolve's internal cost per on-call resource per month?

### For Commercial Director (complete before attending)

- [ ] Review EBS-SLA-BU-004 response (service credits decision) — this informs the discussion of resolution SLA liability in EBS-SLA-BU-002
- [ ] Review the WP14C validation score (baseline 66%, target >90%) — context for why these SLA commitments matter commercially
- [ ] Answer pre-read question C: What is the maximum resolution SLA liability APPSolve can commercially accept on an EBS AMS engagement — assuming the service credit model from EBS-SLA-BU-004 applies?

---

## Workshop Agenda

**Total duration: 15 minutes**

| Time | Item | Lead | Purpose |
|---|---|---|---|
| 0:00–1:00 | Context brief | AI / Facilitator | 60 seconds: why these 2 decisions require joint resolution; what happens after this session (overlay promotion) |
| 1:00–8:00 | Decision 1: EBS-SLA-BU-002 | BU Lead opens; CD responds | Resolve resolution SLA default position |
| 8:00–13:00 | Decision 2: EBS-SLA-BU-003 | CD opens; BU Lead responds | Resolve 24/7 on-call commercial structure |
| 13:00–15:00 | Confirmation + next steps | Facilitator | Record decisions; confirm implementation path |

---

## Decision 1: EBS-SLA-BU-002 (8 minutes)

**Decision ID:** EBS-SLA-BU-002
**Assumptions affected:** EBS-SLA-016 through EBS-SLA-020

### The Question

Do APPSolve's EBS AMS resolution time commitments (P1=2hr, P2=4hr, P3=8 BH, P4=16 BH, P5=5 BD) apply as a **default offering** in all EBS AMS proposals using the SLA Overlay, or only **where explicitly contracted** in the AMS agreement?

### Why Both Parties Are Needed

| Party | Their required input | Why it can't be answered without the other |
|---|---|---|
| **BU Lead** | Is a 2-hour P1 resolution achievable reliably enough across all EBS AMS engagements to make it a default commitment? What are the failure scenarios (Oracle SR dependency, database corruption requiring Oracle DBA patch, OCI infrastructure failure)? | Without the BU Lead's operational assessment, the CD cannot price the liability or assess whether default credits are appropriate |
| **Commercial Director** | Given the service credit model from EBS-SLA-BU-004: is the financial exposure from a "default resolution SLA" position acceptable across the EBS AMS portfolio? What is the incremental pricing premium to clients if resolution SLAs are included by default? | Without the CD's credit model and pricing view, the BU Lead cannot assess whether resolution commitments are commercially deployable even if operationally achievable |

### Options

| Option | Position | BU Lead consideration | CD consideration |
|---|---|---|---|
| **A** | Resolution SLAs are the default — all EBS AMS proposals with SLA Overlay include resolution times unless explicitly excluded | Must confirm ≥80% of P1 incidents resolved within 2 hours; must confirm Oracle SR exclusion adequately protects against the remaining 20% | Must confirm credit exposure is bounded by the service credit cap from BU-004 and that the premium (if any) covers the risk |
| **B** | Resolution SLAs are on-request — included only where the client specifically requests them in the RFP or pre-sales discussion | Most conservative; no default liability; BU Lead must be able to offer resolution SLAs when asked | CD must be able to price them when requested without having pre-approved terms; or CD must co-approve each engagement that includes resolution SLAs |
| **C** | Resolution SLAs are on-request for P1 and P2; default excluded for P3, P4, P5 | Splits the risk: P1/P2 resolution SLAs are the most demanding operationally but also the most commercially valuable for ARM-type tenders | P3-P5 resolution SLAs add little value to the client but create sustained low-level credit risk across many incidents |

**Recommended position (for discussion):** **Option A for P1 resolution (2hr); Option B for P2–P5 resolution.**
Rationale: P1 2-hour resolution is the most commercially valuable commitment in EBS AMS tenders. ARM IT045 was won partly on this basis. Making P1 resolution the default (with robust Oracle SR and client dependency exclusions) is achievable and differentiating. P2–P5 resolution SLAs are less critical and on-request allows CD to manage their cumulative credit risk.

### Discussion Guide

1. BU Lead: What is your assessment of P1 2-hour resolution reliability? (Target response: 2 minutes)
2. BU Lead: Is the Oracle SR exclusion (EBS-SLA-032) sufficient to protect APPSolve in the scenarios where 2hr is missed? (Target: 2 minutes)
3. CD: Given BU-004 service credit position and BU Lead's reliability assessment — are you comfortable with P1 resolution as a default? (Target: 2 minutes)
4. Joint: Agree position for P2–P5 (on-request or excluded). (Target: 2 minutes)

### Expected Output

A clear statement of which resolution time assumptions are:
- Default (included in all EBS AMS SLA overlay assemblies)
- On-request (included when client RFP specifies or pre-sales recommends)
- Excluded (never offered)

---

## Decision 2: EBS-SLA-BU-003 (5 minutes)

**Decision ID:** EBS-SLA-BU-003
**Assumptions affected:** EBS-SLA-021 through EBS-SLA-027

### The Question

What is the commercial structure for 24/7 P1 (and optionally P1+P2) on-call coverage under EBS AMS?
- **Fixed monthly premium:** 24/7 on-call is priced as a fixed monthly add-on line item in the AMS agreement (e.g., R15,000/month on top of base AMS fee), payable regardless of whether any after-hours callouts occur.
- **Per-callout fee:** No standing monthly charge; client pays a per-callout fee only when the on-call resource is activated (e.g., R3,500 per callout exceeding 30 minutes).
- **Hybrid:** Fixed low monthly retainer (R5,000–R8,000/month) + per-callout charge for activations exceeding a threshold (e.g., first 2 callouts per month included; subsequent at R2,500/callout).

### Why Both Parties Are Needed

| Party | Their required input | Why it can't be answered without the other |
|---|---|---|
| **BU Lead** | What is APPSolve's internal cost of maintaining an EBS AMS on-call resource? Is it a fixed monthly cost (dedicated on-call person) or variable (shared on-call pool with per-activation cost)? How many callouts per month does a typical EBS AMS client generate? | Without the BU Lead's internal cost model, the CD cannot set a commercial price that covers cost + margin |
| **Commercial Director** | What is the appropriate client-facing price for 24/7 on-call coverage that (a) covers APPSolve's internal cost, (b) generates acceptable margin, and (c) is competitive in the EBS AMS market? | Without the CD's pricing decision, the BU Lead cannot confirm whether the proposed commercial model is viable for APPSolve to offer at scale |

### Options

| Option | Structure | Pros | Cons |
|---|---|---|---|
| **A — Fixed monthly premium** | Single line item; e.g., R15,000–R25,000/month for 24/7 P1; R30,000–R45,000/month for 24/7 P1+P2 | Simple; predictable revenue for APPSolve; predictable cost for client; no invoice surprises | Client pays even if no callouts occur; may lose to competitors with per-callout model in tenders where client perceives low after-hours risk |
| **B — Per-callout fee** | No monthly charge; R3,000–R6,000 per callout activation > 30 minutes | Client only pays for actual use; competitive in tenders where client believes callout frequency will be low | Revenue unpredictable; APPSolve bears on-call staffing cost regardless of activation; one bad month with many P1s generates large invoice (client may dispute) |
| **C — Hybrid** | Fixed monthly availability fee (R5,000–R10,000/month) + first 2 callouts per month included + R2,500–R3,500 per additional callout | Balances APPSolve's fixed staffing cost with client's desire for usage-based billing; bounded maximum client exposure | More complex to invoice and explain; may require custom billing logic |

**Recommended position (for discussion):** **Option A for DRM engagements (where 24/7 is part of the named team model); Option C for standard AMS engagements without DRM.**
Rationale: In a DRM engagement where the client is already paying for named resources, 24/7 on-call is a natural extension of the named resource model — a fixed monthly premium is consistent and simple. For standard AMS without DRM, clients may be more cost-sensitive and a hybrid model protects APPSolve's fixed on-call cost while giving clients some usage-based comfort.

### Discussion Guide

1. BU Lead: What is your internal on-call staffing cost per EBS AMS client per month? (Target: 1 minute)
2. BU Lead: What is a realistic average number of P1 after-hours callout activations per client per month, based on experience? (Target: 1 minute)
3. CD: Given BU Lead's cost and frequency data — which model achieves target margin? (Target: 2 minutes)
4. Joint: Confirm model for (a) DRM engagements and (b) standard AMS engagements. (Target: 1 minute)

### Expected Output

A confirmed commercial structure for 24/7 on-call under EBS AMS:
- Model type (fixed / per-callout / hybrid)
- Indicative price range for EBS AMS proposals (or "CD to advise per engagement" if not standardisable yet)
- Whether DRM and standard AMS have different 24/7 pricing models

---

## Confirmation and Recording (2 minutes)

At the close of the session, the facilitator confirms:

1. EBS-SLA-BU-002 — agreed position: [state agreed option]
2. EBS-SLA-BU-003 — agreed commercial structure: [state agreed model + price range]

Both parties verbally confirm the above. The facilitator (or AI) records the outcomes in:
- `DR_EBS-SLA-BU-002.md`
- `DR_EBS-SLA-BU-003.md`

---

## Post-Workshop Next Steps

**Immediate (same day as workshop):**
1. AI records both decisions in Decision Record files
2. AI updates EBS_AMS_SLA_OVERLAY_V1.md to reflect approved positions for EBS-SLA-BU-002 and EBS-SLA-BU-003
3. AI confirms all 9 decisions are now resolved

**Within 2 business days of workshop:**
4. AI applies all 9 decisions to both overlay files (EBS_AMS_SLA_OVERLAY_V1.md and EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md)
5. AI presents implementation summary to BU Lead for confirmation

**After BU Lead confirms implementation:**
6. BU Lead sets `approved_for_reuse: true` on both overlay packs
7. Both overlays promoted to Approved v1.0
8. OUTSTANDING_ACTION_REGISTER.md and GOVERNANCE_DASHBOARD.md updated
9. EBS AMS tenders with enhanced SLA or DRM requirements can now be assembled from Approved status

---

## Workshop Logistics

| Item | Detail |
|---|---|
| Duration | 15 minutes strict — pre-reading is mandatory to achieve this |
| Format | Video call or in-person (MS Teams preferred for AI observation) |
| Minimum attendees | EBS BU Lead + Commercial Director — no quorum without both |
| Documents open during session | EBS_AMS_SLA_OVERLAY_V1.md (Sections 4 and 5); this agenda; CD's EBS-SLA-BU-004 response |
| Decision recording | AI records during session or immediately after based on verbal confirmation |
| Deferrals | Neither decision may be deferred without rescheduling the workshop — both require the same attendees and they are connected |

---

## What Happens if Workshop Cannot Be Scheduled Within 5 Business Days

If the workshop cannot be held within 5 business days of the email responses being received, the overlay packs remain Draft and cannot be promoted. The EBS AMS SLA and DRM capabilities exist in the library but must not be assembled into client-facing proposals.

The impact on active tenders: any EBS AMS tender received before the workshop completes should be flagged to the BU Lead. For such tenders, APPSolve may assemble the standard assembly (ERP + OCI + OIC + AMS) and supplement with manually drafted SLA and resource model content — not using the overlay assumptions directly. This is less efficient but does not block the tender submission.

---

*WP15E EBS Reduced Workshop Agenda v1.0 | 2026-06-19 | WP15E — EBS AMS Overlay Decision Harvest*
*2 Category C decisions | Joint BU Lead + Commercial Director | 15 minutes | Prerequisites: Category A email responses + Category B CD response*
*Decisions: EBS-SLA-BU-002 (resolution SLAs) + EBS-SLA-BU-003 (24/7 commercial structure)*
