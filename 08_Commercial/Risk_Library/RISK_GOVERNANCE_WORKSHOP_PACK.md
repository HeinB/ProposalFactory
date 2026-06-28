---
document_id: RISK-GOVERNANCE-WORKSHOP-PACK-V1
title: "Risk Library — Governance Workshop Pack"
version: "1.0"
status: "AWAITING BU LEAD REVIEW"
created: "2026-06-26"
created_by: "WP18B-EXT.1B — Risk Library Decision Harvest"
approved_by: ""
approved_date: ""
category: "Commercial / Risk Library / Governance"
scope: "Workshop facilitation guide and pre-session email pack for BU Lead governance review of the Enterprise Risk Register V1.0. Target: ≤90 minutes."
related_documents:
  - ENTERPRISE_RISK_REGISTER_V1.md
  - RISK_GOVERNANCE_DECISION_REGISTER.md
  - RISK_AUTO_APPROVAL_REGISTER.md
  - WP18B_EXT1B_DECISION_HARVEST_REPORT.md
---

# Risk Library — Governance Workshop Pack

**Work Package:** WP18B-EXT.1B  
**Facilitator:** (APPSolve SA Practice Lead or Proposal Factory Owner)  
**BU Lead:** (Insert Name)  
**Target duration:** ≤90 minutes  
**Total decisions:** 20 Category B risks  
**Pre-session email:** 7 items (confirmation only; responses required before workshop)  
**Workshop decisions:** 13 items (CRITICAL rating confirmations + governance rules)  

---

## Pre-Session Checklist

Before the workshop, complete the following:

- [ ] Send **Section A** (Pre-Session Email) at least 24 hours before the workshop
- [ ] Confirm BU Lead has read ENTERPRISE_RISK_REGISTER_V1.md (or the relevant section summaries)
- [ ] Confirm BU Lead has reviewed RISK_AUTO_APPROVAL_REGISTER.md batch list
- [ ] Collect email responses (7 items — approve/revise/defer)
- [ ] Load decision status into the Decision Status Tracker (RISK_GOVERNANCE_DECISION_REGISTER.md) before the workshop starts
- [ ] Prepare ENTERPRISE_RISK_REGISTER_V1.md for annotation during the workshop
- [ ] Confirm Commercial Director is NOT required (no Commercial Director involvement needed for this review)

---

## SECTION A — PRE-SESSION EMAIL

*Send as a structured email to the BU Lead 24+ hours before the workshop. Request: reply with "Approve", "Revise [notes]", or "Defer to workshop" for each item.*

---

**Subject: Risk Library Governance — Pre-Session Review (7 items, responses needed before [date])**

Hi [BU Lead],

We're preparing the Enterprise Risk Library for governance approval. Before our [date] workshop, I need your confirmation on 7 straightforward items — either mergers of duplicate risks, or a single mathematical rating correction.

For each item below, reply with:
- **Approve** — proceed as proposed
- **Revise [notes]** — propose a change and I'll update the register
- **Defer** — move to the workshop agenda

---

**EMAIL-01 — RC-PROJ-001: Merger of two identical project scope risks**
Two approved KB assets both describe "module design not signed off before build begins." Proposed: one canonical entry, rating HIGH (unchanged).
→ Decision: Approve / Revise / Defer

**EMAIL-02 — RC-PROJ-002: Merger of two identical phase-dependency risks**
Two approved KB assets both describe "upstream phase instability causes downstream delay." Applies to phased HCM only (Pattern 2). Rating HIGH (unchanged).
→ Decision: Approve / Revise / Defer

**EMAIL-03 — RC-PROJ-004: Rating correction LOW → MEDIUM (matrix arithmetic)**
The original draft rated this risk LOW (Low likelihood × High impact). The 3×3 matrix requires MEDIUM for Low × High. This is a mathematical correction, not a commercial judgment.
→ Decision: Approve / Revise / Defer

**EMAIL-04 — RC-INT-002: Merger of two identical integration scope risks**
Two approved KB assets both describe "third-party integration scope underestimated." Different HCM asset contexts; identical root cause and mitigation. Rating MEDIUM (unchanged).
→ Decision: Approve / Revise / Defer

**EMAIL-05 — RC-INT-005: Merger of two identical payroll-timing risks**
Two approved KB assets both describe "integration schedule not aligned to payroll cutoff." Different perspectives (integration readiness vs. project planning); identical consequence. Rating HIGH (unchanged).
→ Decision: Approve / Revise / Defer

**EMAIL-06 — RC-TECH-002: Merger of two identical SETA reporting risks**
Two approved KB assets both describe SETA/WSP/ATR extract complexity from different HCM module perspectives (Learning and Analytics). Rating MEDIUM (unchanged). South Africa-scoped only.
→ Decision: Approve / Revise / Defer

**EMAIL-07 — RC-COMP-001: Merger of two POPIA compliance risks**
Two approved KB assets both describe POPIA obligations arising from HR/payroll data handling. Proposed canonical entry covers all applicable data contexts (HCM, BeBanking). Rating MEDIUM (unchanged).
→ Note: Option available to expand BeBanking scope explicitly (BB-DAT-006 referenced in assumption cross-ref). Recommend Option A (approve merger) or Option C (expand to BeBanking explicitly). Please advise.
→ Decision: Approve (Option A) / Expand to BeBanking (Option C) / Revise / Defer

---

Please respond before [workshop date]. Items with no response will be moved to the workshop agenda.

---

## SECTION B — WORKSHOP AGENDA (≤90 MINUTES)

*Facilitator guide — decision items only. Auto-approvals (20 Category A risks) are confirmed as a batch via the RISK_AUTO_APPROVAL_REGISTER.md at item 9.*

---

### OPENING (5 minutes)

**Facilitator script:**

"Today's session governs the Enterprise Risk Library — 40 canonical risks extracted from 51 approved KB asset sources. We have already handled 20 risks via auto-approval (Category A — no decisions required; batch sign-off at the end). Of the remaining 20 risks, [X] were cleared via email before the session. We have [13 − X] decisions to make today.

All ratings in V1.0 were calculated against the approved 3×3 rating matrix. Where the matrix produced a higher rating than the original draft, those changes require your explicit sign-off. No approvals have been applied yet — all 40 risks remain DRAFT pending this session.

We are NOT modifying the Enterprise Risk Register today. We are recording your decisions, and I will apply them to the register after the session."

---

### BATCH 1 — WFM SCOPE RISKS (CRITICAL) [~15 minutes]

*Two highest-commercial-impact WFM risks. Most likely to affect WFM proposal pricing and risk register presentation.*

---

**WORKSHOP-01 — BU-RL-011 — RC-TECH-003: WFM Absence Rule Complexity (HIGH → CRITICAL)**

*Facilitator brief (read aloud):*
RC-TECH-003 is characterised as "the #1 WFM scope overrun." The V1.0 register proposes CRITICAL (High × High). The draft had it as HIGH.

"Do you confirm from WFM project history that absence rule complexity — union agreements, multi-employment-type leave, BCEA interaction with shift patterns — has caused scope overruns on more than half of Oracle WFM implementations?"

| Option | Label | Outcome |
|---|---|---|
| A | Confirm CRITICAL | High × High — WFM proposals lead with this risk |
| B | Revert to HIGH | Medium × High — register is less assertive |

**Decision recorded:** ___  
**Notes:** ___

---

**WORKSHOP-02 — BU-RL-007 — RC-DATA-004: WFM Biometric Data Mismatch (HIGH → CRITICAL)**

*Facilitator brief:*
RC-DATA-004 proposes CRITICAL for biometric device reconciliation failures at WFM go-live. Confidence level is **Medium** (limited project evidence compared to other CRITICAL risks). This is the most nuanced decision in the batch — the BU Lead's WFM implementation experience matters here.

"How frequently in WFM implementations have biometric device data mismatches caused material payroll errors? If fewer than 50% of WFM projects have encountered this, HIGH may be more appropriate than CRITICAL."

| Option | Label | Outcome |
|---|---|---|
| A | Confirm CRITICAL | High × High — strong signal for WFM proposals |
| B | Revert to HIGH | Medium × High — appropriate for limited evidence base |
| C | Confirm CRITICAL, set confidence_level to Low | CRITICAL rating with explicit evidence caveat |

**Decision recorded:** ___  
**Notes:** ___

---

### BATCH 2 — PROJECT RISK CRITICALITY (CRITICAL) [~15 minutes]

*Core HCM delivery risks. Affect every P1/P2 proposal risk register.*

---

**WORKSHOP-03 — BU-RL-003 — RC-PROJ-003: Late Org Design Decisions (HIGH → CRITICAL)**

*Facilitator brief:*
RC-PROJ-003 is raised from HIGH to CRITICAL on the basis that "late org design decisions are the most frequently observed HCM project risk." The likelihood is raised from Medium to High.

"In your experience across HCM implementations, does late org design sign-off occur in more than 50% of projects? If yes, High likelihood is justified and the rating becomes CRITICAL."

| Option | Label | Outcome |
|---|---|---|
| A | Confirm CRITICAL | High × High — leads every P1/P2 risk register |
| B | Revert to HIGH | Medium × High — more conservative |
| C | Confirm HIGH, elevate assembly_priority to Critical | Same commercial urgency; matrix rating unchanged |

**Decision recorded:** ___  
**Notes:** ___

---

**WORKSHOP-04 — BU-RL-005 — RC-DATA-001: HCM Data Quality at Cutover (HIGH → CRITICAL)**

*Facilitator brief:*
RC-DATA-001 proposes CRITICAL for HR data quality failures causing payroll cutover problems. The likelihood was already High in the draft; this is a matrix correction (High × High = CRITICAL, not HIGH).

"This is primarily a matrix arithmetic correction — the draft set it as HIGH when High × High = CRITICAL. Do you agree with the underlying High likelihood and High impact assessment?"

| Option | Label | Outcome |
|---|---|---|
| A | Confirm CRITICAL (matrix correction) | High × High — correct per matrix |
| B | Revise likelihood to Medium → HIGH | Register is more conservative |

**Decision recorded:** ___  
**Notes:** ___

---

**WORKSHOP-05 — BU-RL-016 — RC-CLIENT-007: Cross-Functional Alignment Failure (HIGH → CRITICAL)**

*Facilitator brief:*
RC-CLIENT-007 proposes CRITICAL on the basis that cross-functional alignment failures between HR, Finance, Payroll, and IT are "the primary cause of HCM design phase overruns." Likelihood raised from Medium to High.

"Is cross-functional alignment failure the most common cause of HCM design rework in your experience? If yes, High likelihood is justified."

| Option | Label | Outcome |
|---|---|---|
| A | Confirm CRITICAL | High × High — supports requirement for named Project Sponsor |
| B | Revert to HIGH | Medium × High — more conservative |

**Decision recorded:** ___  
**Notes:** ___

---

### BATCH 3 — PAYROLL AND DATA CHAIN (CRITICAL) [~10 minutes]

---

**WORKSHOP-06 — BU-RL-006 — RC-DATA-003: HCM Data Errors Propagate to Payroll (HIGH → CRITICAL)**

*Facilitator brief:*
RC-DATA-003 proposes CRITICAL for HCM data errors propagating to incorrect payroll runs. High × High = CRITICAL. Direct financial and regulatory consequence.

"Do you agree that data quality errors reaching payroll processing represent a High-likelihood, High-impact risk in payroll-integrated HCM implementations?"

| Option | Label | Outcome |
|---|---|---|
| A | Confirm CRITICAL | High × High — supports case for parallel payroll runs |
| B | Revise likelihood to Medium → HIGH | More conservative |

**Decision recorded:** ___  
**Notes:** ___

---

**WORKSHOP-07 — BU-RL-014 — RC-TECH-012: Annual SA Legislative Update (HIGH → CRITICAL)**

*Facilitator brief:*
This is the most conceptually interesting decision. The annual SA budget update (tax tables, UIF, SDL) is a certain annual event — the uncertainty is whether the integration update is completed before the effective date. The V1.0 register proposes CRITICAL for integration updates that miss the legislative effective date.

There is also a structural question: for AMS proposals, this is better expressed as a service obligation (AMS-REL-001 SLA) than a risk. For Implementation proposals, the risk is genuine.

"Should this remain as a CRITICAL risk for all applicable proposal types, or should it be split — retained as CRITICAL for Implementation proposals and moved to the AMS service framework for AMS proposals?"

| Option | Label | Outcome |
|---|---|---|
| A | Confirm CRITICAL — all applicable patterns | Single entry; simple |
| B | Confirm HIGH for all — more conservative | Less assertive |
| C | Confirm CRITICAL for Implementation; AMS scope to AMS-REL-001 | Architecturally correct; cleaner register |

**Decision recorded:** ___  
**Notes:** ___

---

### BATCH 4 — LICENSING AND ORACLE PRODUCT SCOPE [~15 minutes]

*Two linked decisions — DG-008 split must be decided first, then ratings.*

---

**WORKSHOP-08 — BU-RL-012 + BU-RL-013 — RC-TECH-006 / RC-TECH-008: DG-008 Split Decision**

*Facilitator brief (combined — handle as one discussion):*
The deduplication analysis (DG-008) identified RC-TECH-006 (OAX-specific licensing) and RC-TECH-008 (general Oracle product licensing) as potentially overlapping. The V1.0 recommendation is to KEEP THEM SEPARATE because they have different triggers and different mitigations.

- **RC-TECH-006 (OAX):** Triggered only when OAX Analytics is in scope. Mitigation: verify OAX licence before project kickoff.
- **RC-TECH-008 (General):** Triggered when any separately-licensed Oracle feature is included in scope. Mitigation: Oracle licensing review for all module dependencies.

"Do you agree that OAX licensing risk and general Oracle product licensing risk are distinct enough to warrant two separate canonical entries?"

| Option | Label | Outcome |
|---|---|---|
| A | Confirm split — two separate entries | RC-TECH-006 (OAX) + RC-TECH-008 (general) |
| B | Merge into one general licensing risk | Simpler register; loses OAX specificity |

**DG-008 Decision recorded:** ___

*Then — for each (if split confirmed):*

**RC-TECH-006 Rating (HIGH → CRITICAL):**
"Has an OAX licensing gap stopped or materially delayed an HCM analytics workstream in your experience?"

| Option | Label |
|---|---|
| A | Confirm CRITICAL — observed; strong project gate signal |
| B | Revert to HIGH — less assertive |

**RC-TECH-006 Rating Decision:** ___

**RC-TECH-008 Rating (HIGH → CRITICAL):**
"Has a general Oracle product licensing gap caused material project delay or commercial exposure in your experience?"

| Option | Label |
|---|---|
| A | Confirm CRITICAL |
| B | Revert to HIGH |

**RC-TECH-008 Rating Decision:** ___  
**Notes:** ___

---

### BATCH 5 — CLIENT OBLIGATIONS AND LEARNING [~10 minutes]

---

**WORKSHOP-09 — BU-RL-015 — RC-CLIENT-004: Learning System Empty at Go-Live (HIGH → CRITICAL)**

*Facilitator brief:*
RC-CLIENT-004 proposes CRITICAL for an Oracle Learning go-live where no content is loaded. The argument: "a learning system without content defeats the implementation objective."

"Do you agree that an empty content library at Learning go-live is a HIGH-impact outcome? If yes, and given that client content readiness is frequently delayed, does High likelihood hold?"

| Option | Label | Outcome |
|---|---|---|
| A | Confirm CRITICAL | Strong signal; supports content readiness requirement |
| B | Revert to HIGH | System is configured; content is client-owned |

**Decision recorded:** ___  
**Notes:** ___

---

### BATCH 6 — COMMERCIAL RISK DECISIONS [~10 minutes]

---

**WORKSHOP-10 — BU-RL-017 — RC-COMM-001: Analytics Expectation Disputes (HIGH → CRITICAL)**

*Facilitator brief:*
RC-COMM-001 merges three source risks (from Learning, Compensation, and Analytics KB assets) describing client analytics expectations exceeding Oracle HCM standard reporting. Also proposes CRITICAL rating.

Two decisions: (1) confirm the 3-into-1 merger; (2) confirm CRITICAL.

"Has analytics expectation misalignment caused commercial disputes or scope escalations in your experience? If yes, CRITICAL is defensible."

| Merger option | Label |
|---|---|
| A | Approve merger (3 → 1) |
| B | Keep separate |

| Rating option | Label |
|---|---|
| A | Confirm CRITICAL |
| B | Revert to HIGH |

**Merger Decision:** ___  
**Rating Decision:** ___  
**Notes:** ___

---

**WORKSHOP-11 — BU-RL-018 — RC-COMM-002: Oracle Help Desk vs Oracle Service Cloud Misidentification (HIGH → CRITICAL)**

*Facilitator brief:*
RC-COMM-002 proposes CRITICAL for proposal scope written against the wrong Oracle product (Oracle HR Help Desk confused with Oracle Service Cloud/B2C). The draft notes: "product misidentification has caused commercial disputes on past APPSolve proposals."

This decision depends on a factual claim about past project history.

"Can you confirm that a commercial dispute has occurred on an APPSolve proposal due to HR Help Desk / Oracle Service Cloud scope confusion? If yes, CRITICAL is the correct rating."

| Option | Label |
|---|---|
| A | Confirm CRITICAL — past incidents confirmed |
| B | Revert to HIGH — past incidents cannot be confirmed or were not material |

**Decision recorded:** ___  
**Notes:** ___

---

### BATCH 7 — GOVERNANCE RULES [~10 minutes]

---

**WORKSHOP-12 — BU-RL-020 — RC-OPS-001: mandatory_if = TRUE (Unconditional Inclusion)**

*Facilitator brief:*
RC-OPS-001 is the only risk in the register with `mandatory_if: TRUE` — meaning it appears in every proposal risk register regardless of platform, modules, or engagement type. The only exception is Pattern 10 (DBA/Managed Services — no go-live involved).

"Do you confirm that every implementation, AMS, and non-DBA proposal should include a go-live operational readiness risk? This is a governance rule decision — once approved, the Risk Selection Engine will include this risk automatically in every applicable proposal."

| Option | Label | Outcome |
|---|---|---|
| A | Confirm mandatory_if = TRUE, P10 exclusion only | Unconditional for all other patterns |
| B | Add additional exclusions | Specify which patterns should not include it |
| C | Convert to conditional engagement_type IN [Implementation, AMS] | Equivalent; explicitly stated |

**Decision recorded:** ___  
**Notes:** ___

---

**WORKSHOP-13 — Gap Acceptance: 7 Empty Categories + P10/P12**

*Facilitator brief:*
7 risk categories (RC-RES, RC-INFRA, RC-CM, RC-MIG, RC-CUT, RC-3P, RC-SEC) have no canonical risks. Pattern 10 (DBA) and Pattern 12 (BeBanking) are significantly under-served.

"Do you accept these as known gaps to be addressed in a future work package (WP18B-EXT.3), or do any of these gaps block the approval of the current register?"

| Option | Label | Outcome |
|---|---|---|
| A | Accept all gaps; approve register as-is | WP18B-EXT.3 scheduled for gap-fill |
| B | Block approval on specific gaps | Identify which categories must be filled first |

**Decision recorded:** ___  
**Notes:** ___

---

### AUTO-APPROVAL BATCH SIGN-OFF (5 minutes)

*Present the RISK_AUTO_APPROVAL_REGISTER.md batch summary.*

"The following 20 risks are proposed for auto-approval. They have a single source, no rating change, no merger decision, and have been confirmed as business-meaning-unchanged from their source material. Do you wish to review any individual entry, or do you confirm the batch?"

- [ ] Batch confirmed as presented
- [ ] Individual exceptions noted: ___

**Signed:** ___  
**Date:** ___

---

### CLOSE (5 minutes)

*Facilitator checklist:*

- [ ] All 13 workshop decisions recorded
- [ ] Email batch decisions recorded (from pre-session responses)
- [ ] Auto-approval batch signed off
- [ ] Gap acceptance decision recorded
- [ ] Total approvals: ___ / 40
- [ ] Post-session actions agreed (facilitator will update ENTERPRISE_RISK_REGISTER_V1.md)

*Post-session actions (facilitator):*
1. Apply all approved decisions to ENTERPRISE_RISK_REGISTER_V1.md (update `approved_for_reuse`, `approved_by`, `approved_date` per risk)
2. Apply rating changes for approved CRITICAL upgrades
3. Update HANDOVER.md and AI_CONTEXT.md to reflect approved register state
4. Create WP18B-EXT.3 brief for gap-fill exercise
5. Proceed to WP18D (Risk Selection Engine) once TD-001 is resolved

---

## Workshop Decision Summary

*Complete during the workshop. Carry forward to RISK_GOVERNANCE_DECISION_REGISTER.md status tracker.*

| Decision ID | Risk ID | Channel | Decision | Decided |
|---|---|---|---|---|
| BU-RL-001 | RC-PROJ-001 | Email | | |
| BU-RL-002 | RC-PROJ-002 | Email | | |
| BU-RL-003 | RC-PROJ-003 | Workshop | | |
| BU-RL-004 | RC-PROJ-004 | Email | | |
| BU-RL-005 | RC-DATA-001 | Workshop | | |
| BU-RL-006 | RC-DATA-003 | Workshop | | |
| BU-RL-007 | RC-DATA-004 | Workshop | | |
| BU-RL-008 | RC-INT-002 | Email | | |
| BU-RL-009 | RC-INT-005 | Email | | |
| BU-RL-010 | RC-TECH-002 | Email | | |
| BU-RL-011 | RC-TECH-003 | Workshop | | |
| BU-RL-012 | RC-TECH-006 | Workshop | | |
| BU-RL-013 | RC-TECH-008 | Workshop | | |
| BU-RL-014 | RC-TECH-012 | Workshop | | |
| BU-RL-015 | RC-CLIENT-004 | Workshop | | |
| BU-RL-016 | RC-CLIENT-007 | Workshop | | |
| BU-RL-017 | RC-COMM-001 | Workshop | | |
| BU-RL-018 | RC-COMM-002 | Workshop | | |
| BU-RL-019 | RC-COMP-001 | Email | | |
| BU-RL-020 | RC-OPS-001 | Workshop | | |
| GAP-001 | 7 empty categories + P10/P12 | Workshop | | |
| AUTO | 20 Category A risks | Batch | | |

---

## Post-Workshop: Approval Application Checklist

After the session, the facilitator applies decisions to ENTERPRISE_RISK_REGISTER_V1.md:

- [ ] All email-approved mergers: `approved_for_reuse: Yes`
- [ ] RC-PROJ-004 rating: update to MEDIUM if approved
- [ ] All CRITICAL confirmations: update `net_rating` field where applicable
- [ ] All CRITICAL reversions: retain HIGH, update `governance_notes`
- [ ] RC-TECH-006 / RC-TECH-008: apply DG-008 split decision
- [ ] RC-TECH-012 (if Option C selected): update `mandatory_if` to exclude AMS patterns; flag for AMS-REL-001 cross-reference
- [ ] RC-OPS-001: update `mandatory_if` per BU-RL-020 decision
- [ ] All auto-approved risks: set `approved_for_reuse: Yes`, `approved_by`, `approved_date`
- [ ] Update AI_CONTEXT.md, HANDOVER.md, MEMORY.md with approval counts and TD-001 resolution status
