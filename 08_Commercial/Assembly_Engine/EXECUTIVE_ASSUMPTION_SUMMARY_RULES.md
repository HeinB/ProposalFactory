---
document_id: EXECUTIVE-ASSUMPTION-SUMMARY-RULES
title: "Executive Assumption Summary Rules — Selection and Structure Standard"
version: "1.0"
status: "Approved"
created: "2026-06-22"
created_by: "WP17D-0A — Assumption Schedule Consumption Model"
category: "Assembly Engine / Presentation Rules"
scope: "Defines the deterministic selection rules for the Key Assumptions and Client Obligations section inserted in the proposal body under the Option B presentation model. Companion to ASSUMPTION_SCHEDULE_PRESENTATION_STANDARD.md."
---

# Executive Assumption Summary Rules — Selection and Structure Standard

**Version:** 1.0 | **Date:** 2026-06-22 | **Status:** Approved  
**Authority:** This document defines what appears in the proposal body (the Key Assumptions section) when the Option B presentation model is in use.  
**Companion documents:** `ASSUMPTION_SCHEDULE_PRESENTATION_STANDARD.md` | `ASSUMPTION_SCHEDULE_STANDARD.md` | `ASSUMPTION_GROUPING_RULES.md`

---

## 1. Purpose

Under Option B (the approved presentation model), the proposal body contains a "Key Assumptions and Client Obligations" section. This document defines:

1. Which assumptions are selected for that section
2. How they are structured and ordered
3. What numbering convention is used
4. What counts as mandatory vs selected
5. How the section cross-references the complete schedule appendix

The selection is **entirely deterministic** using assumption ID section codes — no reading of assumption text is required to determine inclusion.

---

## 2. Governing Principle

### 2.1 Two categories of inclusion

| Category | Rule | Reason |
|----------|------|--------|
| **Mandatory** | ALL items of this type must appear in the body section | Client must see these to understand obligations and what is excluded |
| **Selected** | Representative items from this category; subset only | Provides commercial context without overwhelming |

### 2.2 Priority of mandatory items

Mandatory items are never capped or filtered. If there are 60 explicit exclusions, all 60 appear in the body section. If there are 40 client responsibility items, all 40 appear.

The executive assumption summary is NOT a "short" document for large engagements. Its purpose is to surface the items that evaluators and clients must read before signing — not to minimise page count.

### 2.3 Core selection logic

```
FOR EACH assumption in the complete schedule:
    section_code := extract_section_code(assumption_id)
    IF section_code IN mandatory_codes THEN include → MANDATORY
    ELSIF section_code IN selected_codes THEN include → SELECTED
    ELSE exclude
```

The complete selection algorithm is defined in Section 4.

---

## 3. Section Structure of the Body Section

The Key Assumptions and Client Obligations section in the proposal body is organised into four sub-sections:

### Sub-section 1: Engagement and Commercial Assumptions

**Purpose:** Establishes scope, service model, and commercial framework up front.  
**Selection type:** SELECTED  
**Heading text:** `Engagement and Commercial Assumptions`

### Sub-section 2: Service Management and SLA Summary

**Purpose:** States SLA tier definitions, coverage hours, and priority framework.  
**Selection type:** SELECTED  
**Heading text:** `Service Management and SLA Summary`  
**Condition:** Only include if AMS pack is in the BOM (AMS-SLA-\* or EBS-SLA-\* assumptions exist after suppression).

### Sub-section 3: Client Responsibilities

**Purpose:** States all obligations on the client that are conditions of the engagement.  
**Selection type:** MANDATORY (ALL items)  
**Heading text:** `Client Responsibilities`

### Sub-section 4: Explicit Exclusions

**Purpose:** States all items explicitly out of scope.  
**Selection type:** MANDATORY (ALL items)  
**Heading text:** `Explicit Exclusions`

---

## 4. Deterministic Selection Rules

Rules are applied in priority order. A rule is applied if the assumption's section code matches. Rules are not cumulative — first match wins.

### Priority 1 — MANDATORY: Explicit Exclusions

**Include ALL** assumptions where the section code is: `-EXC-` or `-EXT-`

These always map to Sub-section 4 (Explicit Exclusions) in the body.

Rule: `IF pack_code ENDS_WITH "-EXC-" OR pack_code ENDS_WITH "-EXT-" THEN MANDATORY → Sub-section 4`

*There are no exceptions. All exclusions are mandatory.*

### Priority 2 — MANDATORY: Client Responsibilities and Dependencies

**Include ALL** assumptions where the section code is: `-CUS-`, `-CON-`, or `-DEP-`

These always map to Sub-section 3 (Client Responsibilities) in the body.

Rule: `IF section_code IN ["-CUS-", "-CON-", "-DEP-"] THEN MANDATORY → Sub-section 3`

*There are no exceptions. All client obligations are mandatory.*

### Priority 3 — SELECTED: SLA Definitions and Priority Framework

**Include ALL** assumptions from the SLA sub-section codes: `-SLA-` and `-PRI-`

These map to Sub-section 2 (Service Management and SLA Summary).

Rule: `IF section_code IN ["-SLA-", "-PRI-"] THEN SELECTED → Sub-section 2`

Rationale: SLA definitions are high-value, low-count items (typically 15–25 per AMS engagement). Including all of them is not burdensome and avoids the risk of selective omission affecting commercial position.

*Note: EBS-SLA-* items are SLA section code overrides (not EBS product pack items). Apply the same rule: EBS-SLA-* → Sub-section 2.*

### Priority 4 — SELECTED: General / Engagement Assumptions

**Include ALL** assumptions where section code is: `-GEN-`

These map to Sub-section 1 (Engagement and Commercial Assumptions).

Rule: `IF section_code = "-GEN-" THEN SELECTED → Sub-section 1`

Rationale: GEN assumptions define the overall engagement model and are typically 3–6 per pack. They are high commercial relevance and low count.

### Priority 5 — SELECTED: Commercial Constraints and Enhancement Rules

**Include ALL** assumptions where section code is: `-CR-` or `-ENH-`

These map to Sub-section 1 (Engagement and Commercial Assumptions).

Rule: `IF section_code IN ["-CR-", "-ENH-"] THEN SELECTED → Sub-section 1`

These are AMS-specific section codes covering out-of-scope change requests and enhancement treatment. They define the commercial boundary of the AMS service.

### Priority 6 — EXCLUDE

All other section codes are excluded from the body section. They appear only in the complete schedule appendix.

Section codes excluded from body: `-SCP-`, `-DAT-`, `-CUT-`, `-HYP-`, `-FUN-`, `-REP-`, `-INT-`, `-WF-`, `-CFG-`, `-MIG-`, `-LZ-`, `-DR-`, `-SEC-`, `-GOV-`, `-INF-`, `-NET-`, `-BCK-`, `-DRM-`, and any functional sub-section codes not listed in Priorities 1–5.

*Rationale: These assumptions are important for technical and delivery staff but are not the first thing a client evaluator or project sponsor needs to read.*

---

## 5. Summary of Selection Rules

| Priority | Section code(s) | Category | Sub-section | Cap |
|----------|----------------|----------|-------------|-----|
| 1 | `-EXC-`, `-EXT-` | MANDATORY | 4 — Explicit Exclusions | None |
| 2 | `-CUS-`, `-CON-`, `-DEP-` | MANDATORY | 3 — Client Responsibilities | None |
| 3 | `-SLA-`, `-PRI-` | SELECTED | 2 — Service Management & SLA | None |
| 4 | `-GEN-` | SELECTED | 1 — Engagement & Commercial | None |
| 5 | `-CR-`, `-ENH-` | SELECTED | 1 — Engagement & Commercial | None |
| 6 | All other codes | EXCLUDED | (appendix only) | — |

**No cap is applied to any category.** If a category has 60 items, all 60 appear. The selection rules are binary: include or exclude based on section code.

---

## 6. Numbering Convention

### 6.1 Consistency with complete schedule

The body section uses the **same sequential numbers** assigned in the complete schedule. Numbers are NOT restarted in the body section.

**Generation sequence:**
1. Generate complete schedule → assign sequential numbers 1 through N
2. Extract body assumptions using Selection Rules → carry forward the same numbers

### 6.2 Ordering within body sub-sections

Within each body sub-section, assumptions are ordered by their **full schedule sequential number** (ascending). This preserves the ordering logic of the complete schedule and ensures numbers always appear in ascending order within each sub-section.

### 6.3 Numbering example

```
[Complete schedule excerpt]
407. [OIC DEP-001 text]  *(Ref: OIC-DEP-001)*     ← CON/DEP → body: Sub-section 3
408. [OIC DEP-002 text]  *(Ref: OIC-DEP-002)*     ← CON/DEP → body: Sub-section 3
409. [OIC CFG-001 text]  *(Ref: OIC-CFG-001)*     ← CFG → appendix only
410. [OIC CFG-002 text]  *(Ref: OIC-CFG-002)*     ← CFG → appendix only
411. [AMS EXC-001 text]  *(Ref: AMS-EXC-001)*     ← EXC → body: Sub-section 4
412. [ERP CUS-001 text]  *(Ref: ERP-CUS-001)*     ← CUS → body: Sub-section 3

[Body section output (Sub-section 3 — Client Responsibilities)]
407. [OIC DEP-001 text]  *(Ref: OIC-DEP-001)*
408. [OIC DEP-002 text]  *(Ref: OIC-DEP-002)*
412. [ERP CUS-001 text]  *(Ref: ERP-CUS-001)*
```

The body sub-section 3 shows items 407, 408, 412 — skipping 409, 410, 411 (which appear in the appendix under their respective sections). Numbers are non-contiguous in the body, which is expected and correct.

---

## 7. ARM IT045 Indicative Output

For ARM IT045 (EBS AMS Full Stack, 594 net assumptions):

| Body sub-section | Source section codes | Estimated count |
|-----------------|---------------------|----------------|
| Sub-section 1 — Engagement & Commercial | -GEN-, -CR-, -ENH- | ~15 |
| Sub-section 2 — Service Management & SLA | -SLA-, -PRI- | ~20 |
| Sub-section 3 — Client Responsibilities | -CUS-, -CON-, -DEP- | ~46 |
| Sub-section 4 — Explicit Exclusions | -EXC-, -EXT- | ~49 |
| **Body total** | | **~130** |
| Appendix total | All 8 sections | **594** |

*Indicative counts. Actual counts determined by WP17D-1 extraction.*

ARM IT045 body section pages: ~13–15 pages.

---

## 8. Opening and Closing Text

### 8.1 Body section opening text

At the start of the Key Assumptions and Client Obligations section (before Sub-section 1), insert:

> This section presents the key commercial assumptions, service management definitions, client obligations, and explicit exclusions that govern this engagement. These assumptions form part of the complete Assumption Schedule provided in Appendix [X].
>
> **The complete Assumption Schedule in Appendix [X] contains all [N] governing assumptions and is incorporated by reference as a binding component of this proposal. Engagement of APPSolve's services constitutes client acknowledgement and acceptance of all assumptions in Appendix [X].**

### 8.2 Sub-section 3 (Client Responsibilities) opening text

At the start of Sub-section 3, before the first numbered item, insert:

> The following assumptions define obligations on the Client that are conditions of the engagement. APPSolve's commercial position, timeline, and pricing are contingent on the Client fulfilling these obligations as described. Material deviation from these obligations may require scope, timeline, or commercial renegotiation.

### 8.3 Sub-section 4 (Explicit Exclusions) opening text

At the start of Sub-section 4, before the first numbered item, insert:

> The following items are explicitly excluded from the scope of this engagement. Requests to include excluded items will be treated as change requests and priced separately. APPSolve has no obligation to perform any activity described in this section without a signed change order.

### 8.4 Body section closing text

After the last assumption in Sub-section 4, insert:

> *The complete Assumption Schedule for this engagement is provided in Appendix [X]. All [N] assumptions listed therein apply to this engagement regardless of whether they appear in this summary section. Please review Appendix [X] in full before executing this proposal.*

---

## 9. Conditional Application

### 9.1 AMS condition (Sub-section 2)

Sub-section 2 (Service Management and SLA Summary) is ONLY included if:
- AMS pack is in the BOM, AND
- At least one `-SLA-` or `-PRI-` assumption survives suppression in the assembled schedule

If the AMS SLA assumptions are fully suppressed by a replacement pack, Sub-section 2 is omitted. The replacement SLA assumptions will appear in Sub-section 2 if they carry `-SLA-` codes — but if the replacement assumptions use different section codes, Sub-section 2 may be empty and should be dropped.

### 9.2 No AMS pattern (body becomes 3 sub-sections)

For engagements without AMS (e.g., OIC Standalone, HCM Full Suite only):
- Sub-section 2 is omitted
- Body structure: Sub-section 1 → Sub-section 3 → Sub-section 4
- Renumber the sub-section headings accordingly (1, 2, 3) to avoid gaps

### 9.3 Empty sub-sections

If a sub-section would be empty (e.g., an engagement with no explicit exclusions, which should be extremely rare), omit the sub-section and its heading entirely. Do not render an empty section.

---

## 10. WP17D-1 Implementation Notes

### 10.1 Extraction logic

The ASSUMPTION_EXTRACTOR (v1.1) must implement the following passes:

**Pass 1 — Complete schedule:**
- Extract all assumptions for all packs in BOM
- Apply suppression rules (S1–S4)
- Group by section (A–H) using ASSUMPTION_GROUPING_RULES
- Number sequentially 1 through N
- Write `[TENDER_ID]_ASSUMPTION_SCHEDULE_V1.md`

**Pass 2 — Body section:**
- Filter assumptions from Pass 1 using Selection Rules in Section 4 of this document
- Group by body sub-section (1–4) in the order defined in Section 3
- Order within each sub-section by ascending sequential number (from Pass 1)
- Apply opening and closing text (Section 8)
- Write `[TENDER_ID]_KEY_ASSUMPTIONS_V1.md`

### 10.2 Numbering must be locked before Pass 2

The sequential numbers assigned in Pass 1 must not change after Pass 2 begins. The numbers in the body section are a read-only reference to the complete schedule numbers.

### 10.3 Section code extraction

To apply the selection rules, the ASSUMPTION_EXTRACTOR must extract the section code from each assumption ID. The ID format is `[PACK]-[SECTION]-[NNN]`. The section code is the middle segment: `-SECTION-`.

Special cases handled in ASSUMPTION_GROUPING_RULES apply here too:
- `EBS-SLA-NNN` → section code is `-SLA-` (not `-EBS-`)
- `EBS-DRM-NNN` → section code is `-DRM-` (excluded from body)
- OCI-EXT-NNN → section code is `-EXT-` (mandatory, Sub-section 4)

### 10.4 Validation check

After Pass 2, verify:
```
body_mandatory_EXC_count = complete_schedule_EXC_count  (must be equal)
body_mandatory_CUS_count = complete_schedule_CUS_count  (must be equal)
body_mandatory_CON_count = complete_schedule_CON_count  (must be equal)
body_mandatory_DEP_count = complete_schedule_DEP_count  (must be equal)
```

Any mismatch indicates a selection bug — all mandatory items must be present in the body, no exceptions.

---

*EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md v1.0 | WP17D-0A Consumption Model | 2026-06-22*  
*Approved selection model: Priority 1–5 rules applied by section code. No text reading required.*  
*Companion: ASSUMPTION_SCHEDULE_PRESENTATION_STANDARD.md | WP17D0A_PRESENTATION_RECOMMENDATION.md*
