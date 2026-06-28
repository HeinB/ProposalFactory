---
title: Assumption Library Master Review Report
version: v1.0
status: Ready for Human Review
programme: WP14B — Assumption Library Master Review Workbook
date: 2026-06-17
preceded_by: WP14A — Governance Baseline Correction Pass
deliverable: ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx
---

# Assumption Library Master Review Report

**Programme:** WP14B | **Date:** 2026-06-17 | **Preceded by:** WP14A

> **Scope:** This report documents the extraction, cross-validation, and findings from a full parse of all 11 assumption packs in the APPSolve Tender Knowledge Base. No assumptions were modified. No packs were altered. This report is a read-only audit product to support the human quality review process before governance lock-down.

---

## 1. Summary

| Metric | Value |
|---|---|
| Packs processed | 11 |
| Assumptions extracted (body count) | **1,025** |
| Total frontmatter count (governance-registered) | 1,060 |
| Gross discrepancy (frontmatter vs body) | **35** |
| Decisions loaded (GOVERNANCE_MASTER_DECISION_REGISTER) | **45** ✓ |
| Validation exceptions identified | **12** |
| Duplicate assumption IDs found | **0** ✓ |
| Packs with no CSV register | **5** (all HCM module packs) |
| Packs body/register aligned | **5 of 6** with registers |

---

## 2. Pack-by-Pack Counts

| Pack | Code | Status | Frontmatter Count | Body Count (Parsed) | Register Count | Body = FM? | Body = Reg? |
|---|---|---|---|---|---|---|---|
| HCM Base | HCM | Approved v1.0 | 114 | **114** | N/A | ✓ | N/A |
| HCM Recruiting | REC | Draft | 52 | **54** | N/A | ✗ +2 | N/A |
| HCM Learning | LRN | Draft | 43 | **37** | N/A | ✗ −6 | N/A |
| HCM Talent | TLT | Draft | 38 | **31** | N/A | ✗ −7 | N/A |
| HCM Compensation | COM | Draft | 40 | **30** | N/A | ✗ −10 | N/A |
| Oracle OIC | OIC | Approved v1.0 | 101 | **104** | 104 | ✗ +3 | ✓ |
| Oracle ERP | ERP | Approved v1.0 | 128 | **123** | 123 | ✗ −5 | ✓ |
| Oracle OCI | OCI | Approved v1.0 | 174 | **174** | 174 | ✓ | ✓ |
| Acumatica Base | ACU | Draft | 152 | **152** | 152 | ✓ | ✓ |
| BeBanking Base | BB | Draft | 122 | **122** | 122 | ✓ | ✓ |
| AMS | AMS | Approved v1.0 | 96 | **84** | 84 | ✗ −12 | ✓ |
| **Totals** | | | **1,060** | **1,025** | — | — | — |

**Notes on body count authority:** Where body count and register count agree and differ from frontmatter, the body/register figure is authoritative. The frontmatter `assumption_count` field should be corrected to match.

---

## 3. Validation Exceptions

### 3.1 Count Mismatches — Frontmatter vs Body

| Severity | Pack | FM Count | Body Count | Delta | Implication |
|---|---|---|---|---|---|
| Medium | HCM Recruiting | 52 | 54 | +2 | Body has 2 more assumptions than frontmatter claims; frontmatter undercounts |
| High | HCM Learning | 43 | 37 | −6 | 6 assumptions missing from body; frontmatter overcounts; possible incomplete authoring |
| High | HCM Talent | 38 | 31 | −7 | 7 assumptions missing from body; frontmatter overcounts; possible incomplete authoring |
| High | HCM Compensation | 40 | 30 | −10 | 10 assumptions missing from body; frontmatter overcounts; possible incomplete authoring |
| Medium | Oracle OIC | 101 | 104 | +3 | Body has 3 more than frontmatter; register confirms 104; frontmatter undercounts |
| Medium | Oracle ERP | 128 | 123 | −5 | 5 assumptions missing from body; register confirms 123; frontmatter overcounts |
| High | AMS | 96 | 84 | −12 | 12 assumptions missing from body; register confirms 84; frontmatter overcounts |

> **Important:** For OIC, ERP, and AMS, the body count and register count agree. This means the register was built from the body and both are internally consistent. The frontmatter `assumption_count` field is incorrect. Recommended action: correct frontmatter to match body/register.

> **For HCM module packs (Learning, Talent, Compensation):** These packs have no registers, so there is no independent cross-check. The body count is lower than the frontmatter. This may indicate: (a) assumptions that were planned and counted in frontmatter but not yet written into the body; (b) assumptions in a format not matched by the parser; or (c) frontmatter set optimistically before final content was complete. **Human review required** — scan each pack visually to confirm that the body count is the correct count.

### 3.2 Missing Registers

All five HCM packs (Base, Recruiting, Learning, Talent, Compensation) have no CSV assumption register.

| Pack | File Expected | Impact |
|---|---|---|
| HCM Base | `HCM/HCM_ASSUMPTION_REGISTER.csv` | No register cross-check; 114 assumptions unvalidated by register |
| HCM Recruiting | `HCM/HCM_RECRUITING_ASSUMPTION_REGISTER.csv` | No register; count discrepancy cannot be register-validated |
| HCM Learning | `HCM/HCM_LEARNING_ASSUMPTION_REGISTER.csv` | No register; count discrepancy cannot be register-validated |
| HCM Talent | `HCM/HCM_TALENT_ASSUMPTION_REGISTER.csv` | No register; count discrepancy cannot be register-validated |
| HCM Compensation | `HCM/HCM_COMPENSATION_ASSUMPTION_REGISTER.csv` | No register; count discrepancy cannot be register-validated |

**Recommended action:** Create registers for all HCM packs from the body content after human review confirms the correct body count.

### 3.3 Integrity Checks — PASS

| Check | Result |
|---|---|
| Duplicate assumption IDs | **0 duplicates found** ✓ |
| All assumption IDs parseable | ✓ |
| Decision register count | **45 ✓** (matches governance programme) |
| OCI body = OCI register | **174 ✓** (post-WP14A correction confirmed) |
| ACU body = ACU register | **152 ✓** |
| BeBanking body = BeBanking register | **122 ✓** |

---

## 4. Frontmatter Count Corrections Implied

The following frontmatter `assumption_count` fields should be corrected after human review confirms body counts:

| Pack | File | Current Frontmatter | Actual Body Count | Correction Needed |
|---|---|---|---|---|
| HCM Recruiting | HCM_RECRUITING_ASSUMPTIONS_V1.md | 52 | 54 | 52 → 54 |
| HCM Learning | HCM_LEARNING_ASSUMPTIONS_V1.md | 43 | 37 | 43 → 37 (after confirming no missing assumptions) |
| HCM Talent | HCM_TALENT_ASSUMPTIONS_V1.md | 38 | 31 | 38 → 31 (after confirming no missing assumptions) |
| HCM Compensation | HCM_COMPENSATION_ASSUMPTIONS_V1.md | 40 | 30 | 40 → 30 (after confirming no missing assumptions) |
| Oracle OIC | OIC_ASSUMPTIONS_V1.md | 101 | 104 | 101 → 104 |
| Oracle ERP | ERP_ASSUMPTIONS_V1.md | 128 | 123 | 128 → 123 |
| AMS | AMS_ASSUMPTIONS_V1.md | 96 | 84 | 96 → 84 |

> **Do not apply these corrections until the human review in ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx is complete.** If the review reveals that the frontmatter count was correct and assumptions are indeed missing from the body, those assumptions should be authored and added first.

---

## 5. Decision Coverage in Pack Body

The workbook Sheet 3 (DECISION_DEPENDENCY_MAP) contains all 45 outstanding BU decisions mapped to the assumption IDs they affect. Summary by pack:

| Pack | Outstanding Decisions | Critical |
|---|---|---|
| Acumatica Base | 14 | 1 (BU-ACU-009) |
| BeBanking Base | 10 | 1 (BU-BB-006) |
| HCM Recruiting | 7 | 0 |
| HCM Learning | 5 | 0 |
| HCM Talent | 4 | 0 |
| HCM Compensation | 5 | 0 |
| **Total** | **45** | **2** |

---

## 6. Workbook Structure

The workbook `ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx` contains 5 sheets:

| Sheet | Purpose | Rows |
|---|---|---|
| ASSUMPTION_MASTER | One row per assumption; K/D/M/A review actions | 1,025 data rows |
| PACK_SUMMARY | Pack-level status and count validation | 11 rows |
| DECISION_DEPENDENCY_MAP | All 45 outstanding BU decisions with affected assumptions | 45 rows |
| CHANGE_SUMMARY | Formula-driven count totals; review progress tracking | Summary formulas |
| VALIDATION_EXCEPTIONS | All 12 exceptions identified in this report | 12 rows |

### How to use ASSUMPTION_MASTER

1. Open `ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx`
2. Filter to a pack (Column A) or status (Column E) as needed
3. For each assumption, choose a **Review Action** (Column H):
   - **K** = Keep — assumption is correct as written
   - **D** = Delete — assumption should be removed
   - **M** = Modify — enter revised wording in **Proposed Wording** (Column I)
   - **A** = Add — add a new row for a net-new assumption
4. Add **Reviewer Notes** (Column J) for any context or rationale
5. Mark **Applied** (Column K) as `Yes` when the change is made to the source pack

---

## 7. Recommended Actions Before Review Begins

| Priority | Action | Owner |
|---|---|---|
| HIGH | Visually scan HCM Learning, Talent, Compensation packs to confirm whether the lower body counts are correct (missing assumptions) or frontmatter is simply wrong | Oracle BU Lead |
| HIGH | Create assumption registers (CSV) for all 5 HCM packs after body count is confirmed | AI (next task) |
| HIGH | Correct frontmatter `assumption_count` for OIC (101→104), ERP (128→123), AMS (96→84) after human review confirms no missing assumptions | AI (next task) |
| MEDIUM | Correct frontmatter `assumption_count` for Recruiting (52→54) after confirming the 2 extra are legitimate | Oracle BU Lead |
| LOW | Decide whether total registered count needs updating from 1,060 to 1,025 (or the correct body count) after review | BU Lead + AI |

---

## 8. Corrected Programme Total Implied

If body counts are accepted as authoritative (register-confirmed where available):

| Metric | Frontmatter Total | Body Count Total |
|---|---|---|
| Total assumptions | 1,060 | **1,025** |
| Approved (5 packs) | 613 (OCI+OIC+ERP+AMS+HCM Base) | **599** (OCI 174 + OIC 104 + ERP 123 + AMS 84 + HCM Base 114) |
| Draft (6 packs) | 447 | **426** (REC 54 + LRN 37 + TLT 31 + COM 30 + ACU 152 + BB 122) |

> **Note:** Do not update governance documents with the body count totals until human review confirms the body counts are correct (i.e., no missing assumptions). This report is advisory only.

---

## 9. Files Produced

| File | Location | Description |
|---|---|---|
| `ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx` | `08_Commercial/` | Master review workbook — 1,025 assumption rows, 5 sheets |
| `ASSUMPTION_LIBRARY_MASTER_REVIEW_REPORT.md` | `08_Commercial/` | This report |

---

*Awaiting human review. No changes have been applied to any assumption packs.*

*ASSUMPTION_LIBRARY_MASTER_REVIEW_REPORT v1.0 | WP14B | 2026-06-17*
