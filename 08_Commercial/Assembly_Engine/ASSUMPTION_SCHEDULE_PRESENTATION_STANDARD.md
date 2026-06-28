---
document_id: ASSUMPTION-SCHEDULE-PRESENTATION-STANDARD
title: "Assumption Schedule Presentation Standard — Consumption Model Specification"
version: "1.0"
status: "Approved"
created: "2026-06-22"
created_by: "WP17D-0A — Assumption Schedule Consumption Model"
category: "Assembly Engine / Presentation Standard"
scope: "Evaluates and approves the model for how assembled assumption schedules are presented to proposal readers. Covers Options A, B, and C with quantitative analysis for ARM IT045 (594 assumptions). Recommends Option B."
---

# Assumption Schedule Presentation Standard — Consumption Model Specification

**Version:** 1.0 | **Date:** 2026-06-22 | **Status:** Approved  
**Authority:** This document governs how assumption schedules are consumed by proposal readers.  
**Companion documents:** `ASSUMPTION_SCHEDULE_STANDARD.md` | `ASSUMPTION_GROUPING_RULES.md` | `EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md`

---

## 1. Design Context

### 1.1 The consumption problem

WP17D-0 established the format, numbering, and grouping standard for client-facing assumption schedules. It produced a single output: the complete assumption schedule, ordered by 8 client-facing sections (A–H).

However, "complete schedule" is not the same as "readable schedule." The Assembly Engine is capable of assembling 50 to 600+ assumptions depending on engagement type:

| Pattern | Net Assumptions | Page estimate |
|---------|----------------|---------------|
| OIC Standalone | 104 | ~10 pages |
| Acumatica Standalone | 152 | ~15 pages |
| HCM Full Suite | 267 | ~25 pages |
| BeBanking + OIC + AMS | 305 | ~28 pages |
| EBS AMS Full Stack (ARM IT045) | 594 | ~55–65 pages |

At 594 assumptions, the complete schedule is the length of a mid-size technical manual. The question is: where does it go in the proposal, and what does the evaluator see?

### 1.2 Baseline assumptions for this analysis

- Average assumption: ~40 words (range: 20–80 words depending on complexity)
- Page density in proposal format (single-column, numbered list, 12pt type): ~10 assumptions per page with section headers and spacing
- A typical APPSolve proposal body (ERP or AMS): 40–70 pages
- Client evaluator reading time: 30–60 minutes
- Client legal/commercial review time: 60–180 minutes

---

## 2. Option A — Full Schedule Only

### 2.1 Description

The complete assumption schedule (all assembled net assumptions, in 8-section order) is inserted directly into the proposal body. Every assembled assumption appears in sequence. The proposal contains one assumption section, one time.

### 2.2 Structural model

```
PROPOSAL BODY
├── Section 1: Executive Summary
├── Section 2: Company Profile
├── Section 3: Proposed Solution
├── Section 4: Implementation Approach
├── Section 5: Assumption Schedule          ← FULL SCHEDULE (all assumptions)
├── Section 6: Pricing
└── Appendices
```

### 2.3 Quantitative analysis for ARM IT045 (594 assumptions)

| Metric | Estimate | Notes |
|--------|---------|-------|
| Assumption count | 594 | Net after 6 suppressions |
| Estimated words | ~23,760 | 594 × avg 40 words |
| Formatted pages | **55–65 pages** | With section headings, numbering, spacing |
| Proposal total pages (typical ERP/AMS proposal) | 40–70 pages |  |
| Total proposal length with Option A | **95–135 pages** | Nearly doubles the document |
| Time to read assumptions at 2 min/page | **110–130 minutes** | Assumption section alone |

**Section breakdown within Option A full schedule:**

| Section | Count | Pages |
|---------|-------|-------|
| A — Engagement & Commercial | ~24 | ~3 |
| B — Project & Implementation | ~30 | ~3 |
| C.1 — Oracle ERP | ~68 | ~7 |
| C.3 — Oracle Integration | ~55 | ~6 |
| D — Infrastructure (OCI) | ~152 | ~15 |
| E — Service Management | ~175 | ~17 |
| F — Security & Compliance | ~22 | ~2 |
| G — Client Responsibilities | ~40 | ~4 |
| H — Explicit Exclusions | ~39 | ~4 |
| **Total** | **~605** | **~61 pages** |

*Note: Indicative. Actual counts determined by WP17D-1 extraction. Section totals sum to ~605 due to rounding; actual net is 594.*

### 2.4 Reader experience

| Audience | Experience with Option A |
|----------|------------------------|
| Procurement evaluator | Overwhelmed. Will skim or skip. Likely skips entirely. |
| Technical evaluator | Reads relevant sections (ERP, OIC). Skips OCI infrastructure (152 pages). |
| Legal / contract manager | Reads all. Uses as contract reference. Suitable but slow. |
| Client project sponsor | Will not read. Will sign based on trust. |
| BU Lead (APPSolve) | Auditable. Complete. But client engagement is low. |

### 2.5 Evaluation usability

**Score: LOW.** An evaluator scoring an RFP response cannot practically navigate 60+ pages of assumptions to assess commercial fitness. The schedule becomes a legal exhibit, not an evaluation tool.

### 2.6 Advantages

| Advantage | Weight |
|-----------|--------|
| Maximum transparency — every assumption visible | High |
| Simplest assembly logic — single output file | Medium |
| Strongest contractual position — complete signed document | High |
| No risk of omitted assumptions | High |

### 2.7 Disadvantages

| Disadvantage | Weight |
|-------------|--------|
| 55–65 page assumption section in a 40–70 page proposal is disproportionate | High |
| Client obligations (Section G) buried at position 7 of 8 sections — easily missed | High |
| Evaluators do not read; commercial protection only effective if evaluators read and acknowledge | Medium |
| Proposal appears bloated — may reduce competitive attractiveness | Medium |
| Infrastructure assumptions (OCI, 152 items) irrelevant to commercial evaluator | Medium |

### 2.8 Verdict

Option A is appropriate for:
- Small engagements (OIC standalone, Acumatica: <200 assumptions, <20 pages)
- Internal validation and dry-run outputs
- Legal contract annexures (not the proposal itself)

Option A is **not recommended** as the standard for large engagements (>300 assumptions).

---

## 3. Option B — Executive Assumption Summary + Complete Schedule Appendix

### 3.1 Description

The proposal contains two assumption artefacts:

1. **In the proposal body:** A curated "Key Assumptions and Client Obligations" section containing the commercially and contractually critical assumptions. Selected by deterministic rules (no judgment required). Typically 50–150 assumptions for enterprise engagements.

2. **In the proposal appendix:** The complete assumption schedule (all assembled net assumptions in 8-section order). Identical to the Option A output. Referenced from the body section.

### 3.2 Structural model

```
PROPOSAL BODY
├── Section 1: Executive Summary
├── Section 2: Company Profile
├── Section 3: Proposed Solution
├── Section 4: Implementation Approach
├── Section 5: Key Assumptions and Client Obligations   ← SELECTED SUBSET (body)
│   ├── 5.1 Engagement and Commercial Assumptions
│   ├── 5.2 Service Management and SLA Summary (if AMS)
│   ├── 5.3 Client Responsibilities (ALL)
│   └── 5.4 Explicit Exclusions (ALL)
├── Section 6: Pricing
└── Appendices
    └── Appendix X: Complete Assumption Schedule          ← ALL ASSUMPTIONS (appendix)
        ├── A. Engagement and Commercial
        ├── B. Project and Implementation
        ├── C. Application Functional
        ├── D. Infrastructure
        ├── E. Service Management
        ├── F. Security and Compliance
        ├── G. Client Responsibilities
        └── H. Explicit Exclusions
```

### 3.3 Selection principle

The key assumptions (body section 5) are selected by **deterministic ID-code rules** — no reading of assumption text required:

| Body sub-section | Source | Rule | ARM IT045 count |
|-----------------|--------|------|----------------|
| 5.1 Engagement & Commercial | Section A + commercial items from E | ALL GEN + AMS-CR/ENH section | ~15 |
| 5.2 Service Management & SLA | Section E — SLA/PRI codes only | AMS-SLA-*, AMS-PRI-*, EBS-SLA-* (SLA definitions only) | ~20 |
| 5.3 Client Responsibilities | Section G | ALL CUS, CON, DEP | ~46 |
| 5.4 Explicit Exclusions | Section H | ALL EXC, EXT | ~49 |
| **Body total** | | | **~130** |

*Client Responsibilities (Section 5.3) and Explicit Exclusions (Section 5.4) always include ALL items — never capped.*

### 3.4 Quantitative analysis for ARM IT045 (594 assumptions)

**Body section (Key Assumptions and Client Obligations):**

| Metric | Estimate |
|--------|---------|
| Assumption count in body | ~130 |
| Estimated words | ~5,200 |
| Formatted pages | **12–15 pages** |

**Appendix (Complete Assumption Schedule):**

| Metric | Estimate |
|--------|---------|
| Assumption count in appendix | 594 |
| Estimated words | ~23,760 |
| Formatted pages | **55–65 pages** |

**Combined:**

| Metric | Estimate |
|--------|---------|
| Total assumption artefacts | 130 (body) + 594 (appendix) |
| Total pages (body + appendix) | 12–15 + 55–65 = **67–80 pages** |
| Proposal body length | 40–70 pages + 12–15 assumption pages = **52–85 pages** |
| Proposal readability | **HIGH** — body is proportionate |

### 3.5 Quantitative analysis for smaller engagements

| Pattern | Body count | Body pages | Appendix count | Appendix pages |
|---------|-----------|-----------|---------------|---------------|
| OIC Standalone | ~44 | ~4 | 104 | ~10 |
| Acumatica Standalone | ~30 | ~3 | 152 | ~15 |
| HCM Full Suite | ~68 | ~6 | 267 | ~25 |
| BeBanking + OIC + AMS | ~80 | ~7 | 305 | ~28 |
| EBS AMS Full Stack | ~130 | ~13 | 594 | ~58 |

The body section scales proportionately: smaller engagements have smaller bodies. Large engagements have longer bodies but the key content (client obligations and exclusions) is always surfaced.

### 3.6 Reader experience

| Audience | Experience with Option B |
|----------|------------------------|
| Procurement evaluator | Reads 12-15 pages of key assumptions in the body. Clear, navigable, proportionate. |
| Technical evaluator | Body gives commercial context; appendix consulted for technical detail as needed. |
| Legal / contract manager | Reviews appendix thoroughly. Full protection preserved. |
| Client project sponsor | Reads body section (5 sections, 12 pages). Understands scope and obligations clearly. |
| BU Lead (APPSolve) | Body = commercial engagement; appendix = complete protection. Both serve their purpose. |

### 3.7 Evaluation usability

**Score: HIGH.** The body section is evaluator-sized. The complete schedule is available for due diligence. Obligations are surfaced up front. Exclusions are prominent.

### 3.8 Traceability between body and appendix

Both the body and appendix use the **same sequential numbers** from the complete schedule. Numbers are assigned in the complete schedule first; the body section is a subset of those same numbers.

Example: ERP-CUS-001 may be assumption #412 in the complete schedule. It appears in the body as `412. [Text] *(Ref: ERP-CUS-001)*` — the same number as in the appendix.

This means:
- Any reference to "assumption 412" is unambiguous across both documents
- Client and APPSolve teams always reference the same number
- Revision tracking is straightforward (if ERP-CUS-001 changes, number 412 is updated in both)

### 3.9 Advantages

| Advantage | Weight |
|-----------|--------|
| Complete commercial protection preserved (full schedule in appendix) | High |
| Client responsibilities and exclusions surfaced in body — evaluators see them | High |
| Body is proportionate (12–15 pages for large engagements) | High |
| Appendix is the same format as Option A — no duplication of work | High |
| Selection is deterministic — no judgment, no text-reading required | High |
| Scales correctly: small engagements have small bodies | Medium |
| Industry standard for large professional services proposals | Medium |

### 3.10 Disadvantages

| Disadvantage | Weight |
|-------------|--------|
| Produces two output files per assembly run (adds WP17D-1 scope) | Medium |
| Numbered assumptions span two documents (resolved by consistent numbering) | Low |
| Body section references appendix — evaluators must understand this relationship | Low |

### 3.11 Verdict

Option B is the **recommended standard** for all APPSolve proposal engagements. See Section 5 for final decision.

---

## 4. Option C — Key Assumptions Only

### 4.1 Description

The proposal contains a curated selection of assumptions (typically 30–50). The complete assumption schedule is retained internally but is NOT included in the proposal.

### 4.2 Structural model

```
PROPOSAL BODY
├── Section 5: Key Assumptions                         ← SELECTED (30-50 items)
└── [No appendix — full schedule held internally only]
```

### 4.3 Quantitative analysis

| Metric | Estimate |
|--------|---------|
| Assumption count | 30–50 |
| Formatted pages | 3–5 pages |
| Coverage of 594-assumption set | 5–8% |

### 4.4 Reader experience

**For the evaluator:** Easy to read. Clear. Short. Good surface appearance.

**For the commercial team at dispute:** Catastrophic. 94% of the assumption protection is absent from the signed document.

### 4.5 Governance and contractual risks

| Risk | Severity | Description |
|------|---------|-------------|
| Unenforceable assumptions | CRITICAL | Assumptions not submitted cannot be enforced. If a dispute arises over a scope item, APPSolve has no documentation of the assumption. |
| Scope creep exposure | CRITICAL | All technical, infrastructure, and service assumptions absent from client document. Any deviation = client claims it was always in scope. |
| Legal unenforceability | HIGH | "You didn't include this in your proposal" is a valid defence if the full schedule was withheld. |
| BU Lead escalation process breaks | HIGH | The assumption governance framework is designed around 100% publication. Selective publication requires a separate governance layer not currently built. |
| Regulatory and audit exposure | MEDIUM | Tender regulations in some jurisdictions require full disclosure of commercial terms. Selective schedules may conflict with this requirement. |

### 4.6 Verdict

Option C is **not recommended** under any circumstances for client-facing proposals. The Assembly Engine exists specifically to produce a complete, governed assumption set. Withholding the complete set defeats the programme objective.

Option C may only be used for:
- Internal preliminary reviews (not client-facing)
- Executive briefings (separate from the proposal document)

---

## 5. Comparison Summary

| Criterion | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Commercial protection | ✅ Complete | ✅ Complete (appendix) | ❌ Partial only |
| Evaluator readability | ❌ Low | ✅ High | ✅ High |
| Legal enforceability | ✅ Full | ✅ Full | ❌ Reduced |
| Proposal proportionality | ❌ Excessive body | ✅ Proportionate | ✅ Short |
| Client obligation visibility | ❌ Buried | ✅ Body-prominent | ⚠️ Selective |
| Assembly logic complexity | Low | Medium | Low |
| Scalability (50–600 assumptions) | ❌ Breaks at 300+ | ✅ Scales well | ✅ Scales (but selective) |
| Industry standard practice | ⚠️ Small contracts only | ✅ Yes — large contracts | ❌ No |
| Automation feasibility | ✅ Single output | ✅ Dual output (deterministic) | ⚠️ Requires manual selection |

---

## 6. Approved Presentation Standard

### 6.1 Decision

**APPROVED STANDARD: Option B — Executive Assumption Summary + Complete Schedule Appendix**

All APPSolve proposals using the Tender Factory Assembly Engine shall:

1. Include a **Key Assumptions and Client Obligations** section in the proposal body, generated from the assembly output using the selection rules in `EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md`.

2. Include a **Complete Assumption Schedule** in a proposal appendix, generated from the full assembly output per `ASSUMPTION_SCHEDULE_STANDARD.md` and `ASSUMPTION_GROUPING_RULES.md`.

3. Reference the appendix from the body section with standard text (see Section 6.3).

4. Use consistent sequential numbering across both documents.

### 6.2 Scale-based application

For small engagements where the complete schedule is ≤200 assumptions and ≤20 formatted pages, the Bid Manager may elect to use Option A (full schedule in body only, no appendix split) at their discretion. This threshold is:

| Total net assumptions | Recommended model |
|----------------------|-------------------|
| ≤ 200 | Option A or B (bid manager discretion) |
| 201 – 600 | Option B (mandatory) |
| > 600 (future large patterns) | Option B (mandatory) |

### 6.3 Standard cross-reference text

The following text is inserted at the end of the body section (Key Assumptions and Client Obligations):

> *This section presents the key commercial, scope, client obligation, and exclusion assumptions. The complete Assumption Schedule, containing all [N] governing assumptions, is provided in Appendix [X] and forms an integral part of this proposal. All assumptions in Appendix [X] are incorporated by reference into the commercial terms of this proposal.*

Where `[N]` = total net assumption count and `[X]` = appendix letter/number.

### 6.4 Numbering consistency rule

The complete schedule (appendix) is generated and numbered first (assumptions 1 through N). The body section (Key Assumptions) then references a subset of those same numbers. Numbers are not restarted in the body section.

**Implementation requirement for WP17D-1:** Generate complete schedule first → assign sequential numbers → extract subset for body using selection rules → preserve the same numbers in the body output.

### 6.5 What this standard does NOT change

The format decisions from `ASSUMPTION_SCHEDULE_STANDARD.md` are unchanged:
- Sequential numbering (1 to N)
- Inline Ref ID format: `*(Ref: ID)*`
- 8-section structure (A–H) in the complete schedule
- Proposal-ready markdown output format
- Two-layer traceability model

---

## 7. Impact on WP17D-1 Implementation

The dual-output model adds scope to WP17D-1 versus what was defined in WP17D-0.

### 7.1 New WP17D-1 deliverables

| Deliverable | Description | Path |
|-------------|-------------|------|
| `ARM_IT045_ASSUMPTION_SCHEDULE_V1.md` | Complete schedule — all 594 assumptions in 8-section structure | `08_Commercial/Assembly_Engine/` |
| `ARM_IT045_KEY_ASSUMPTIONS_V1.md` | Body section — selected subset per EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md | `08_Commercial/Assembly_Engine/` |

### 7.2 Generation sequence

1. Run ASSUMPTION_EXTRACTOR to read all pack files and extract full assumption text
2. Apply ASSUMPTION_GROUPING_RULES to assign each assumption to its section (A–H)
3. Number all assumptions sequentially (1 through N) across the complete schedule
4. Write the complete schedule (`ASSUMPTION_SCHEDULE_V1.md`)
5. Apply EXECUTIVE_ASSUMPTION_SUMMARY_RULES to select the subset for the body
6. Write the body section (`KEY_ASSUMPTIONS_V1.md`) using the same numbers from step 3
7. Verify count balance: complete schedule count = net assumption count from Audit Report

### 7.3 Updated ASSUMPTION_EXTRACTOR scope (v1.1)

The ASSUMPTION_EXTRACTOR must now produce two outputs, not one. The selection logic for the body section must be implemented as a second pass after the complete schedule is numbered.

---

*ASSUMPTION_SCHEDULE_PRESENTATION_STANDARD.md v1.0 | WP17D-0A Consumption Model | 2026-06-22*  
*Approved standard: Option B — Executive Assumption Summary + Complete Schedule Appendix.*  
*Companion: EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md | WP17D0A_PRESENTATION_RECOMMENDATION.md*
