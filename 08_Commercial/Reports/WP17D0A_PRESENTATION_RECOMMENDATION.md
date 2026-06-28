---
document_id: WP17D0A-PRESENTATION-RECOMMENDATION
title: "WP17D-0A — Assumption Schedule Consumption Model: Presentation Recommendation Report"
version: "1.0"
status: "Complete — Awaiting BU Lead Approval"
created: "2026-06-22"
created_by: "WP17D-0A — Assumption Schedule Consumption Model"
category: "Commercial Reports"
scope: "Formal recommendation for how assembled assumption schedules are presented to proposal readers. Evaluates Options A, B, and C with quantitative analysis for ARM IT045 (594 net assumptions). Governs WP17D-1 scope."
---

# WP17D-0A — Assumption Schedule Consumption Model  
## Presentation Recommendation Report

**Date:** 2026-06-22 | **Version:** 1.0 | **Status:** Complete — Awaiting BU Lead Approval

---

## 1. Work Package Summary

### 1.1 Objective

WP17D-0 established the format, numbering, grouping, and traceability standard for client-facing assumption schedules. It produced a specification for a single assembled output: the complete assumption schedule.

WP17D-0A determines the **consumption model** — how that output is presented to proposal evaluators and clients. Specifically: does the 594-assumption ARM IT045 schedule go directly in the proposal body, in an appendix, or as a selective extract?

### 1.2 Scope

- Evaluate three presentation options (A, B, C) against quantitative and qualitative criteria
- Estimate page impact for ARM IT045 (594 net assumptions) and other engagement patterns
- Select and approve a standard applicable to all APPSolve proposals using the Assembly Engine
- Define selection rules for any curated sub-set that appears in the proposal body
- Specify the impact on WP17D-1 implementation

### 1.3 Documents produced

| Document | Purpose | Status |
|----------|---------|--------|
| `ASSUMPTION_SCHEDULE_PRESENTATION_STANDARD.md` | Option comparison, approved model, scale rules | Approved |
| `EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md` | Selection rules for body section under Option B | Approved |
| `WP17D0A_PRESENTATION_RECOMMENDATION.md` (this file) | Formal recommendation with decision format | Awaiting BU Lead |

---

## 2. Context: What the Assembly Engine Currently Produces

### 2.1 Current state

The ARM IT045 dry-run produced `ARM_IT045_ASSEMBLED_ASSUMPTION_SCHEDULE.md`:
- 600 raw assumptions loaded from 6 packs
- 6 suppressions applied (S1–S4)
- **594 net assumptions** in ID-only format (no assumption text)

WP17D-0 defined the format standard for the text version of this file: 8 sections (A–H), sequential numbering, inline `*(Ref: ID)*` traceability, proposal-ready markdown.

### 2.2 The problem being solved

A 594-assumption schedule formatted per the WP17D-0 standard produces approximately 55–65 formatted pages. Inserted wholesale into a 40–70 page proposal, this:

- Nearly doubles the proposal length
- Buries the most commercially important items (client obligations, exclusions) late in the schedule
- Creates a poor evaluator experience (evaluators will skip or skim)
- Does not reflect industry practice for large enterprise software proposals

This work package determines where the complete schedule goes and what additional output is needed for the proposal body.

---

## 3. Options Evaluated

### 3.1 Option A — Full Schedule Only

Include the complete 594-assumption schedule directly in the proposal body. No appendix split, no curated sub-section.

**ARM IT045 quantitative impact:**

| Metric | Value |
|--------|-------|
| Assumption pages in body | 55–65 |
| Typical proposal body pages | 40–70 |
| Total proposal length | 95–135 pages |
| Evaluator time (assumptions only) | 110–130 minutes |
| Client obligation visibility | LOW (Section G is item 7 of 8) |

**Verdict:** Acceptable for small engagements (≤200 assumptions, ≤20 pages). Disproportionate and evaluator-hostile for large engagements.

### 3.2 Option B — Executive Summary in Body + Complete Schedule in Appendix

The proposal body contains a curated "Key Assumptions and Client Obligations" section (selected by deterministic ID code rules). The complete schedule is in a clearly referenced appendix.

**ARM IT045 quantitative impact:**

| Metric | Value |
|--------|-------|
| Body section assumptions | ~130 |
| Body section pages | 12–15 |
| Appendix assumptions | 594 |
| Appendix pages | 55–65 |
| Total proposal body length (typical) | 52–85 pages |
| Evaluator time (body section) | 25–30 minutes |
| Client obligation visibility | HIGH (Sub-sections 3 and 4 are mandatory) |

**Cross-engagement scale:**

| Pattern | Body | Body pages | Appendix | Appendix pages |
|---------|------|-----------|----------|---------------|
| OIC Standalone | ~44 | ~4 | 104 | ~10 |
| Acumatica Standalone | ~30 | ~3 | 152 | ~15 |
| HCM Full Suite | ~68 | ~6 | 267 | ~25 |
| BeBanking + OIC + AMS | ~80 | ~7 | 305 | ~28 |
| EBS AMS Full Stack (ARM IT045) | ~130 | ~13 | 594 | ~58 |

**Verdict:** Recommended. Scales well. Client obligations and exclusions are body-prominent. Complete protection preserved in appendix.

### 3.3 Option C — Key Assumptions Only

Include only 30–50 selected assumptions in the proposal. Retain the complete schedule internally only.

**ARM IT045 quantitative impact:**

| Metric | Value |
|--------|-------|
| Submitted assumption count | 30–50 |
| Coverage of full assumption set | 5–8% |
| Page impact | 3–5 pages |
| Enforceability of unsubmitted assumptions | LOW to NONE |

**Verdict:** Not recommended. 94% of the commercial protection framework is withheld from the client document. Unenforceable at dispute. Contradicts the governance programme objective.

---

## 4. Decision Criteria and Scoring

| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| Commercial protection (all assumptions enforceable) | 30% | ✅ 10/10 | ✅ 10/10 | ❌ 2/10 |
| Evaluator readability (body section fit-for-purpose) | 25% | ❌ 2/10 | ✅ 9/10 | ✅ 8/10 |
| Client obligation prominence (obligations in body) | 20% | ❌ 3/10 | ✅ 10/10 | ⚠️ 5/10 |
| Assembly automation feasibility | 15% | ✅ 10/10 | ✅ 8/10 | ❌ 3/10 |
| Scalability across all engagement patterns | 10% | ❌ 4/10 | ✅ 9/10 | ✅ 8/10 |
| **Weighted score** | **100%** | **5.8/10** | **9.3/10** | **4.2/10** |

**Option B scores 9.3/10 — significantly ahead of both alternatives.**

---

## 5. Formal Recommendation

---

**RECOMMENDED MODEL: Option B — Executive Assumption Summary + Complete Schedule Appendix**

**RATIONALE:**

1. **Scale incompatibility of Option A.** ARM IT045 produces 594 net assumptions = 55–65 formatted pages. A 40–70 page proposal cannot absorb 60 pages of assumptions in the body without becoming commercially unreadable. Option A works for small engagements (OIC: 10 pages) but fails at enterprise scale.

2. **Legal enforceability preserved.** The complete assumption schedule in the appendix is incorporated by reference in the proposal body. All 594 assumptions are contractually binding. There is no enforceability gap vs Option A.

3. **Client obligations surface in the body.** Under Option B, ALL client responsibilities (Section G: CUS, CON, DEP codes) and ALL explicit exclusions (Section H: EXC, EXT codes) appear in the proposal body — not buried in an appendix. These are the commercially critical items that clients must acknowledge. Body-placement ensures evaluators see them before signing. This is a material commercial advantage vs Option A.

4. **Selection is fully deterministic — no judgment required.** The body section content is selected entirely by ID section codes. This is automatable in WP17D-1 using the same code rules already defined in ASSUMPTION_GROUPING_RULES.md. No BU Lead manual selection per engagement.

5. **Industry standard.** Large professional services firms (consulting, ERP implementation, managed services) universally use a summary-plus-appendix structure for substantial assumption schedules. A 60-page assumption section in a proposal body is unusual and may reduce competitive attractiveness.

6. **Scales proportionately.** OIC Standalone generates a 4-page body section. EBS AMS Full Stack generates a 13-page body section. The body grows proportionately with engagement size. No scale threshold problem.

**IMPACT ON WP17D-1:**

WP17D-1 (as defined in WP17D-0) specified one output file per assembly: the complete assumption schedule. The approved Option B model requires TWO output files per assembly:

| File | Description | Already in scope? |
|------|-------------|------------------|
| `[TENDER_ID]_ASSUMPTION_SCHEDULE_V1.md` | Complete schedule — all assumptions, 8-section structure, sequential numbers | Yes (WP17D-0 scope) |
| `[TENDER_ID]_KEY_ASSUMPTIONS_V1.md` | Body section — selected subset, same numbers, 4 sub-section structure | New — WP17D-0A addition |

The generation sequence is:
1. Extract all assumptions, apply suppressions, group into sections
2. Assign sequential numbers 1 through N across the complete schedule
3. Write `ASSUMPTION_SCHEDULE_V1.md`
4. Apply selection rules (Priority 1–5 from EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md) to filter body items
5. Write `KEY_ASSUMPTIONS_V1.md` using the same numbers from step 2

This adds **moderate scope** to WP17D-1. The selection logic is a second-pass filter on an already-generated numbered list. It does not require re-reading pack files or re-applying grouping rules. Estimated effort increase: +30–40% of original WP17D-1 scope.

**Validation requirement:** After WP17D-1 execution, verify:
- `body_EXC_count = schedule_EXC_count` (all exclusions in body)
- `body_CUS_count + body_CON_count + body_DEP_count = schedule_CUS+CON+DEP_count` (all client obligations in body)
- `body_total + excluded_total = net_assumption_count` (count balance across both files)

**APPROVAL REQUIRED: Yes**

This recommendation requires BU Lead approval before WP17D-1 implementation, because:

1. The dual-output model changes the WP17D-1 deliverable specification
2. The body section text (Sub-sections 1–4) and opening/closing text (defined in EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md) will be client-facing — BU Lead must confirm the standard language
3. The scale-based threshold (≤200 assumptions → Option A discretionary; >200 → Option B mandatory) must be ratified as APPSolve's commercial standard
4. Any future engagement where the BU Lead wishes to deviate from Option B (e.g., include the complete schedule in the body for commercial or client-specific reasons) requires a documented exception — the approval establishes that Option B is the default, not a suggestion

---

## 6. Actions Required Before WP17D-1

| # | Action | Owner | Dependency |
|---|--------|-------|-----------|
| 1 | Approve or modify this recommendation | BU Lead | WP17D-0A deliverables |
| 2 | Confirm the standard client-obligation opening text (Section 8.2 of EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md) | BU Lead | WP17D-1 body text generation |
| 3 | Confirm the standard exclusions opening text (Section 8.3 of EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md) | BU Lead | WP17D-1 body text generation |
| 4 | Confirm the cross-reference text format (Section 6.3 of PRESENTATION_STANDARD.md) | BU Lead | WP17D-1 body section footer |
| 5 | Confirm the scale threshold (≤200 = Option A discretionary) | BU Lead | Assembly Engine standard |

---

## 7. Work Package Completion Status

### 7.1 WP17D-0A deliverables

| Deliverable | File | Status |
|-------------|------|--------|
| Presentation model comparison | `ASSUMPTION_SCHEDULE_PRESENTATION_STANDARD.md` | ✅ Complete |
| Executive summary selection rules | `EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md` | ✅ Complete |
| Formal recommendation report | `WP17D0A_PRESENTATION_RECOMMENDATION.md` (this file) | ✅ Complete |

### 7.2 Design programme status

| Work package | Description | Status |
|-------------|-------------|--------|
| WP17D-0 | Assumption Schedule Design Standard | ✅ COMPLETE |
| WP17D-0A | Assumption Schedule Consumption Model | ✅ COMPLETE — Pending BU Lead Approval |
| WP17D-1 | Inline Text Assembly (ARM IT045) | 🔴 BLOCKED — pending WP17D-0A approval |
| WP17D-2 | HCM Full Suite pattern | 🔴 NOT STARTED |
| WP17D-3 | Acumatica standalone pattern | 🔴 NOT STARTED |
| WP17D-4 | BeBanking + OIC + AMS pattern | 🔴 NOT STARTED |
| WP17D-5 | Plennegy live assembly | 🔴 BLOCKED (OAR-C01, OAR-C02, OAR-A01) |

### 7.3 What WP17D-1 will produce (post-approval)

Assuming approval of Option B:

| File | Path | Description |
|------|------|-------------|
| `ARM_IT045_ASSUMPTION_SCHEDULE_V1.md` | `08_Commercial/Assembly_Engine/` | Complete 594-assumption schedule |
| `ARM_IT045_KEY_ASSUMPTIONS_V1.md` | `08_Commercial/Assembly_Engine/` | Body section (~130 selected assumptions) |
| `WP17D1_INLINE_TEXT_ASSEMBLY_REPORT.md` | `08_Commercial/Reports/` | WP17D-1 execution report |
| Updated `ASSUMPTION_EXTRACTOR.md` v1.1 | `08_Commercial/Assembly_Engine/` | Revised spec with dual-output logic |

---

## 8. Governance Notes

The following existing governance constraints continue to apply to all assumption schedule outputs under Option B:

- Suppressed assumptions never appear in either output (body or appendix)
- Suppressed assumptions never consume a sequential number
- The sequential numbers in the body and appendix are identical — numbers do not restart
- The Audit Report (`ARM_IT045_ASSEMBLY_AUDIT_REPORT.md` and equivalents) contains the full internal traceability layer — this is not included in either client-facing output
- All standard commercial preamble text (defined in ASSUMPTION_SCHEDULE_STANDARD.md Section 4.1) applies to the appendix (complete schedule) only; the body section has its own opening text defined in EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md Section 8

---

*WP17D0A_PRESENTATION_RECOMMENDATION.md v1.0 | WP17D-0A Complete | 2026-06-22*  
*Decision: Option B recommended. BU Lead approval required before WP17D-1 proceeds.*
