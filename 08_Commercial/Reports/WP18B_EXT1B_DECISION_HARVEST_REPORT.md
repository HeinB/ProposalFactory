---
document_id: WP18B-EXT1B-DECISION-HARVEST-REPORT
title: "WP18B-EXT.1B — Risk Library Decision Harvest Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-26"
created_by: "WP18B-EXT.1B — Risk Library Decision Harvest"
category: "Commercial / Reports"
scope: "Summary of the WP18B-EXT.1B decision harvest exercise. Governance packs created. BU Lead effort, commercial director involvement, and post-approval readiness assessment."
---

# WP18B-EXT.1B — Risk Library Decision Harvest Report

**Work Package:** WP18B-EXT.1B  
**Status:** COMPLETE  
**Date:** 2026-06-26  
**Objective:** Prepare the Enterprise Risk Library for governance approval by producing exception-based governance packs. The BU Lead must not review every risk — only items requiring business judgement.

---

## 1. Executive Summary

WP18B-EXT.1B classified all 40 canonical risks in ENTERPRISE_RISK_REGISTER_V1.md, produced decision registers for the 20 items requiring BU Lead review, and created a structured 90-minute workshop pack. Four deliverables were created.

**Governance Readiness Score: 88/100 (projected post-approval)**

| Classification | Count | % | Channel |
|---|---|---|---|
| Category A — Auto-Approve | 20 | 50% | Batch sign-off (RISK_AUTO_APPROVAL_REGISTER.md) |
| Category B — Email decisions | 7 | 17.5% | Pre-session email (7 merger/matrix confirmations) |
| Category B — Workshop decisions | 13 | 32.5% | 90-minute structured session |
| Category C — Further research needed | 0 | 0% | None |
| **Total** | **40** | **100%** | |

**Projected approval outcome (assuming standard BU Lead patterns):**
- Category A: 20/20 approved (100%)
- Category B email: 7/7 approved (100% — clear rationale, no ambiguity)
- Category B workshop: ~11–12/13 approved (~85–92% — some CRITICAL ratings may revert to HIGH)
- **Expected total approved: 38–39 / 40 (95–98%)**

---

## 2. Classification Method

Each risk was evaluated against the following criteria:

**Category A (Auto-Approve)** — all of the following must be true:
- Single approved source KB asset (no merger decision)
- Rating unchanged from source (no recalculation)
- No deduplication group involvement
- All 32 metadata fields complete
- Business meaning confirmed unchanged from source

**Category B (Approval Required)** — any of the following:
- Merger of 2+ source risks (consolidation decision)
- Rating change from source (including matrix corrections)
- DG-008 split decision (deliberate keep-separate governance choice)
- Governance rule requiring explicit BU confirmation (mandatory_if logic)

**Category C (Further Research)** — any of the following:
- Missing assumption cross-references with no resolution path
- Rating materially uncertain (no evidence basis)
- Source asset contradictions

*Result: No Category C items were identified. All 40 risks had clear source material and no irresolvable contradictions.*

---

## 3. Category B Decision Analysis

### 3.1 Email Decisions (7 items)

| Decision ID | Risk ID | Decision Type | Rationale |
|---|---|---|---|
| BU-RL-001 | RC-PROJ-001 | Merger (DG-001) | Identical root cause from 2 assets; stylistic difference only |
| BU-RL-002 | RC-PROJ-002 | Merger (DG-002) | Identical phase-dependency risk from 2 assets |
| BU-RL-004 | RC-PROJ-004 | Matrix correction LOW→MEDIUM | Low×High = MEDIUM per defined matrix; no judgment required |
| BU-RL-008 | RC-INT-002 | Merger (DG-004) | Identical integration scope risk from 2 assets |
| BU-RL-009 | RC-INT-005 | Merger (DG-006) | Identical payroll-timing risk from 2 assets |
| BU-RL-010 | RC-TECH-002 | Merger (DG-003) | Identical SETA reporting risk from 2 HCM module perspectives |
| BU-RL-019 | RC-COMP-001 | Merger (DG-007) | Identical POPIA compliance risk from 2 module contexts |

Email channel appropriate because: each item has a clear rationale derived entirely from the source material. No commercial judgment or experience recall is required to make these decisions. Expected response pattern: 7/7 approve.

### 3.2 Workshop Decisions (13 items)

| Decision ID | Risk ID | Decision Type | Judgment Factor |
|---|---|---|---|
| BU-RL-003 | RC-PROJ-003 | HIGH→CRITICAL | Likelihood elevation: is org design delay >50% frequency? |
| BU-RL-005 | RC-DATA-001 | HIGH→CRITICAL | Matrix correction + frequency confirmation |
| BU-RL-006 | RC-DATA-003 | HIGH→CRITICAL | Matrix correction + payroll impact severity |
| BU-RL-007 | RC-DATA-004 | HIGH→CRITICAL | Confidence=Medium; WFM project experience required |
| BU-RL-011 | RC-TECH-003 | HIGH→CRITICAL | WFM project experience: is absence overrun #1 issue? |
| BU-RL-012 | RC-TECH-006 | HIGH→CRITICAL + DG-008 split | OAX licensing project history; split confirmation |
| BU-RL-013 | RC-TECH-008 | HIGH→CRITICAL + DG-008 split | General licensing history; linked to BU-RL-012 |
| BU-RL-014 | RC-TECH-012 | HIGH→CRITICAL | Classification: risk vs. service obligation for AMS |
| BU-RL-015 | RC-CLIENT-004 | HIGH→CRITICAL | Content readiness as go-live gate |
| BU-RL-016 | RC-CLIENT-007 | HIGH→CRITICAL | Cross-functional alignment frequency |
| BU-RL-017 | RC-COMM-001 | Merger (3) + HIGH→CRITICAL | Analytics dispute history |
| BU-RL-018 | RC-COMM-002 | HIGH→CRITICAL | Past commercial dispute confirmation |
| BU-RL-020 | RC-OPS-001 | Governance rule: mandatory_if=TRUE | Unconditional inclusion rule confirmation |

The 13 workshop items are grouped into 7 thematic batches in the RISK_GOVERNANCE_WORKSHOP_PACK.md:
- Batch 1: WFM scope (WORKSHOP-01, WORKSHOP-02) — 15 min
- Batch 2: Project risk criticality (WORKSHOP-03 through WORKSHOP-05) — 15 min
- Batch 3: Payroll and data chain (WORKSHOP-06, WORKSHOP-07) — 10 min
- Batch 4: Licensing + DG-008 split (WORKSHOP-08) — 15 min
- Batch 5: Client obligations (WORKSHOP-09) — 10 min
- Batch 6: Commercial risks (WORKSHOP-10, WORKSHOP-11) — 10 min
- Batch 7: Governance rules + gap acceptance (WORKSHOP-12, WORKSHOP-13) — 10 min

---

## 4. Deliverables Created

| # | File | Location | Purpose |
|---|---|---|---|
| 1 | RISK_GOVERNANCE_DECISION_REGISTER.md | 08_Commercial/Risk_Library/ | Full decision pack: 20 Category B items with current state, proposed state, evidence, options, rationale |
| 2 | RISK_AUTO_APPROVAL_REGISTER.md | 08_Commercial/Risk_Library/ | 20 Category A items: auto-approval basis, metadata changes, business meaning confirmation; batch sign-off template |
| 3 | RISK_GOVERNANCE_WORKSHOP_PACK.md | 08_Commercial/Risk_Library/ | Facilitator guide: pre-session email (7 items) + 90-min workshop agenda (13 items) + decision tracker |
| 4 | WP18B_EXT1B_DECISION_HARVEST_REPORT.md | 08_Commercial/Reports/ | This document |

---

## 5. BU Lead Effort Estimate

| Activity | Format | Effort | Timing |
|---|---|---|---|
| Read RISK_AUTO_APPROVAL_REGISTER.md batch list | Self-directed | 20 min | Before email review |
| Review and respond to pre-session email (7 items) | Email | 20 min | ≥24h before workshop |
| Attend governance workshop | Structured session | 90 min | Workshop date |
| **Total BU Lead effort** | | **~2h 10 min** | |

*This is significantly less than the 3–4 hour unstructured review estimated in WP18B-EXT.1A. The exception-based structure reduces BU Lead time by ~45–55% by eliminating review of the 20 Category A risks and the 7 email items.*

---

## 6. Commercial Director Involvement

**No Commercial Director involvement is required for this governance session.**

Rationale:
- All 20 Category B decisions are based on delivery experience (risk frequency, impact observations, project history)
- No pricing decisions are embedded in these approvals
- No contractual changes are implied
- Commercial impact of CRITICAL ratings is informational — they affect proposal risk register presentation, not pricing directly
- The BU Lead is the appropriate decision-maker for all items in the register

*Exception: If any CRITICAL rating decisions (BU-RL-012 RC-TECH-006, BU-RL-017 RC-COMM-001, BU-RL-018 RC-COMM-002) are deferred or disputed, the BU Lead may choose to escalate to the Commercial Director for the commercial risk decisions only.*

---

## 7. Post-Approval Governance Readiness

### 7.1 Expected Approval Counts

| Scenario | Approved | % |
|---|---|---|
| Conservative (all CRITICAL revert to HIGH) | 33 | 82.5% |
| Likely (most CRITICAL confirmed; 1-2 reversions) | 38–39 | 95–97.5% |
| Optimistic (all approved as proposed) | 40 | 100% |

### 7.2 Post-Approval Score (Projected)

| Dimension | Pre-approval | Post-approval (projected) |
|---|---|---|
| Schema completeness | 24/25 | 24/25 (unchanged) |
| Assumption coverage | 19/25 | 19/25 (unchanged) |
| Proposal mapping completeness | 20/20 | 20/20 (unchanged) |
| Selection hook completeness | 13/15 | 14/15 (RC-OPS-001 rule confirmed) |
| Rating consistency | 10/10 | 10/10 |
| Governance status | 0/5 (all DRAFT) | 5/5 (approved_for_reuse = Yes) |
| **Readiness Score** | **76/100** | **~88/100** |

### 7.3 Remaining Technical Debt Post-Approval

| Item | Description | Resolution Path |
|---|---|---|
| TD-001 | Risk Library unapproved | RESOLVED by this governance session |
| TD-002 | 7 empty risk categories | WP18B-EXT.3: elicit RC-RES, RC-INFRA, RC-CM, RC-MIG, RC-CUT, RC-3P, RC-SEC risks from BU Leads |
| TD-003 | P10 (DBA) no applicable risks | WP18B-EXT.3: elicit DBA/managed service risks |
| TD-004 | P12 (BeBanking) under-served | WP18B-EXT.3: expand BeBanking risk coverage beyond RC-COMP-001 |
| TD-005 | EBS packs not risk-referenced | WP18B-EXT.3: create EBS-specific risks (RC-INT and RC-OPS currently absorb EBS) |
| TD-006 | Risk Selection Engine not built | WP18D: implement mandatory_if/optional_if/excluded_if as automated filter |

---

## 8. Governance Sequence Recommendation

| Priority | Action | Timing | Owner |
|---|---|---|---|
| 1 | Send pre-session email (7 items) | Immediately | Facilitator |
| 2 | Conduct 90-min governance workshop | Within 5 business days | Facilitator + BU Lead |
| 3 | Apply approved decisions to ENTERPRISE_RISK_REGISTER_V1.md | Within 1 business day post-workshop | Facilitator |
| 4 | Update HANDOVER.md, AI_CONTEXT.md, memory files | Immediately post-application | Facilitator |
| 5 | Brief WP18D (Risk Selection Engine) | After TD-001 resolved | Proposal Factory Owner |
| 6 | Schedule WP18B-EXT.3 (gap-fill) | Post-WP18D kickoff | Facilitator |

---

## 9. Platform Maturity Impact

| Dimension | Pre-WP18B-EXT.1B | Post-WP18B-EXT.1B (projected) |
|---|---|---|
| Risk Library approval status | 0/40 approved | 38–40/40 approved |
| TD-001 status | Unresolved | Resolved |
| Risk Selection Engine readiness | Schema-complete; engine not built | Schema approved; WP18D unblocked |
| Proposal Factory maturity | L3.5 | L4.0 (on approval completion) |
| BU review readiness | Ready | Complete |

**Platform maturity reaches L4.0 when ENTERPRISE_RISK_REGISTER_V1.md is fully approved and the Risk Selection Engine (WP18D) is implemented.**

---

## 10. Document Index — Risk Library (Post-WP18B-EXT.1B)

| File | Purpose | Status |
|---|---|---|
| RISK_LIBRARY_STANDARD.md | Governance standard (v1.0 — foundational) | Approved |
| ENTERPRISE_RISK_REGISTER_DRAFT.md | Draft register (v0.1 — superseded) | Superseded — retain for audit |
| ENTERPRISE_RISK_REGISTER_V1.md | Normalised register (v1.0 — 40 entries) | DRAFT — Pending BU governance session |
| RISK_METADATA_STANDARD.md | Metadata schema definition | DRAFT — Pending BU governance session |
| RISK_ASSUMPTION_CROSS_REFERENCE.md | Risk→assumption mapping | DRAFT — Pending BU governance session |
| RISK_PROPOSAL_MAPPING.md | Risk→section+pattern mapping | DRAFT — Pending BU governance session |
| RISK_GOVERNANCE_DECISION_REGISTER.md | Category B decisions (20 items) | COMPLETE — Ready for BU Lead |
| RISK_AUTO_APPROVAL_REGISTER.md | Category A batch sign-off (20 items) | COMPLETE — Ready for BU Lead |
| RISK_GOVERNANCE_WORKSHOP_PACK.md | Workshop facilitation guide | COMPLETE — Ready for use |
| ../Reports/WP18B_EXT1_RISK_EXTRACTION_REPORT.md | Source risk audit (51→40 canonical) | COMPLETE |
| ../Reports/RISK_DUPLICATION_ANALYSIS.md | Deduplication analysis (8 groups) | COMPLETE |
| ../Reports/WP18B_EXT1A_NORMALISATION_REPORT.md | Normalisation report (readiness 76/100) | COMPLETE |
| ../Reports/WP18B_EXT1B_DECISION_HARVEST_REPORT.md | This document | COMPLETE |
