---
title: WP14D — BeBanking Assumption Pack Remediation Report
version: v1.0
status: Complete
programme: WP14D — BeBanking Assumption Pack Remediation from Master Review Spreadsheet
date: 2026-06-18
preceded_by: WP14B — Assumption Library Master Review Workbook
source_of_authority: 08_Commercial/ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx
---

# WP14D — BeBanking Assumption Pack Remediation Report

**Programme:** WP14D | **Date:** 2026-06-18 | **Source:** ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx

> **Scope:** Apply all BU Lead review decisions from the ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx workbook to the BeBanking assumption pack artefacts. The spreadsheet is the sole authoritative source. All prior AI findings, gap reports, and remediation recommendations are subordinate to the spreadsheet where they conflict.

---

## 1. Remediation Summary

| Metric | Value |
|---|---|
| Total assumptions before remediation | **122** |
| Assumptions deleted | **5** |
| Assumptions modified | **15** |
| Assumptions added | **0** |
| Total assumptions after remediation | **117** |
| BU decisions outstanding before WP14D | **10** (BU-BB-001 through BU-BB-010) |
| BU decisions resolved by WP14D | **9** |
| BU decisions remaining after WP14D | **1** (BU-BB-002) |
| Validation status | **PASS** — MD/CSV/FM/Section-index all = 117 |
| Recommendation | **Ready for BU Lead Approval — 1 decision pending** |

---

## 2. Assumptions Deleted (5)

All deletions are from the ASSUMPTION_MASTER sheet with Review Action = D.

| Assumption ID | Section | Title | Reason |
|---|---|---|---|
| BB-PYR-006 | 143 BB-PYR | Third-Party Deductions Included in Payroll File Scope | BU Lead: out of scope for standard BeBanking; remove to avoid over-commitment |
| BB-RPT-005 | 148 BB-RPT | Regulatory Reporting Is Client Responsibility | BU Lead: covered by BB-EXT-006; redundant; remove |
| BB-ENV-006 | 149 BB-ENV | DR Capability Included — Client DR Tests Separately Scoped | BU Lead: DR RTO/RPO not confirmed; remove until formally documented; BU-BB-010 resolved by deletion |
| BB-ENV-007 | 149 BB-ENV | Linux Hosting — No Client OS or Infrastructure Access | BU Lead: implementation detail not needed in commercial assumption pack |
| BB-ENV-008 | 149 BB-ENV | Oracle DB EE — DBA Is APPSolve Responsibility | BU Lead: implementation detail not needed in commercial assumption pack |

---

## 3. Assumptions Modified (15)

All modifications are from the ASSUMPTION_MASTER sheet with Review Action = M. Wording applied is from the Proposed Wording column of the spreadsheet. Minor grammatical corrections applied where noted (typos in source spreadsheet corrected: "Monatary" → "Monetary"; "integraiton" → "integration"; bank list normalised for grammatical consistency).

| Assumption ID | Change Summary | BU Decision Resolved |
|---|---|---|
| BB-GEN-008 | Tier confirmation wording updated; BU-BB-003 reference removed | BU-BB-003 |
| BB-BNK-001 | Standard bank list expanded to include CMA country banking extensions (Namibia, Botswana, eSwatini, Lesotho, Zimbabwe); Citi Bank UK and Santander Chile repositioned as forex partners only; BU-BB-001 reference removed | BU-BB-001 |
| BB-BNK-009 | Confirmed: Namibia separately scoped; BU-BB-007 reference removed | BU-BB-007 |
| BB-PAY-004 | AVS trigger updated — new or changed bank account details trigger AVS (not all payments); "legal owner" of account confirms; charges simplified | — |
| BB-PAY-008 | Duplicate detection simplified — same beneficiary within configurable window; amount/reference matching removed | — |
| BB-PAY-009 | Same-day EFT removed; RTGS only with bank agreement | — |
| BB-PYR-002 | PaySpace added as confirmed supported payroll source alongside Oracle EBS Payroll; "other payroll systems" clarification added; BU-BB-008 reference removed | BU-BB-008 |
| BB-FX-002 | Forex banking partners updated: Citi Bank UK, ABSA, Nedbank, and FNB (Santander Chile removed); BU-BB-003 reference removed | BU-BB-003 |
| BB-INT-002 | PaySpace added as supported platform; SAP framing corrected to "SAP environments only" with no module-level claims | — |
| BB-SEC-004 | IP restriction removed from assumption text; MFA-only wording retained | — |
| BB-DAT-006 | "POPIA Data Processor" terminology confirmed; "client as Responsible Party" retained; BU-BB-009 reference removed | BU-BB-009 |
| BB-RPT-001 | Standard reporting pack expanded to 6 report types: Payment Batch Status, Payment Register, Bank Account Approval, Remittance Advice, Email Error, Roles Report; PDF only; BU-BB-005 reference removed | BU-BB-005 |
| BB-CUT-002 | Hypercare duration confirmed: first payment cycle (1–3 business days); BU-BB-004 reference removed | BU-BB-004 |
| BB-SUP-001 | Support confirmed as included in BeBanking subscription; BU-BB-006 reference removed | BU-BB-006 |
| BB-SUP-004 | "24×7 support across all priority levels requires a premium support tier" sentence removed per BU decision | — |

---

## 4. BU Decision Resolution Summary

| Decision | Topic | Resolution |
|---|---|---|
| BU-BB-001 | Supported bank list | RESOLVED — BB-BNK-001 updated with confirmed bank list + CMA extensions |
| **BU-BB-002** | **New bank onboarding fee model post-go-live** | **OPEN — no explicit spreadsheet instruction; BB-EXT-008 (keep) implies CR but requires BU Lead explicit confirmation** |
| BU-BB-003 | Forex payment inclusion | RESOLVED — BB-FX-002 updated: Citi Bank UK, ABSA, Nedbank, FNB; BB-GEN-008 tag removed |
| BU-BB-004 | Standard hypercare duration | RESOLVED — BB-CUT-002 updated: first payment cycle (1–3 business days) |
| BU-BB-005 | Standard reporting pack | RESOLVED — BB-RPT-001 updated: 6 standard reports confirmed |
| BU-BB-006 | Post-go-live support model | RESOLVED — BB-SUP-001 updated: support included in subscription |
| BU-BB-007 | Multi-country scope | RESOLVED — BB-BNK-009 updated: Namibia separately scoped confirmed |
| BU-BB-008 | Payroll source support policy | RESOLVED — BB-PYR-002 updated: Oracle EBS Payroll and PaySpace confirmed |
| BU-BB-009 | POPIA operator disclosure | RESOLVED — BB-DAT-006 updated: "POPIA Data Processor" confirmed |
| BU-BB-010 | Disaster recovery testing | RESOLVED BY DELETION — BB-ENV-006 deleted; DR no longer asserted |

---

## 5. Typo Corrections Applied

The following corrections were made to proposed wording in the source spreadsheet before applying to pack content:

| Location | Source Spreadsheet Text | Correction Applied | Rationale |
|---|---|---|---|
| BB-BNK-001 | "Common Monatary Area" | "Common Monetary Area" | Spelling correction; intent clear |
| BB-INT-002 | "integraiton" | "integration" | Spelling correction; intent clear |
| BB-FX-002 | "Citi Bank UK, ABSA and Nedbank and FNB" | "Citi Bank UK, ABSA, Nedbank, and FNB" | Grammatical normalisation; no content change |

---

## 6. Files Updated

| File | Changes Applied |
|---|---|
| `BEBANKING_BASE_ASSUMPTIONS_V1.md` | 5 deletions, 15 modifications; frontmatter, header, section index, BU decision table, readiness assessment, footer all updated; version v1.0-Draft → v1.1-Draft |
| `BEBANKING_ASSUMPTION_REGISTER.csv` | 5 rows deleted; 15 rows modified (title, notes, bu_decision_ref fields); total 122→117 |
| `BEBANKING_GAP_REPORT.md` | GAP-BB-001 partially resolved; GAP-BB-002, GAP-BB-005, GAP-BB-006, GAP-BB-012 marked RESOLVED; BU decision alignment table updated; version v1.0-Draft → v1.1-Draft |
| `BEBANKING_SCOPE_BOUNDARY_GUIDE.md` | SB-BB-011 updated (24×7 wording); SB-BB-012 assumption reference corrected (BB-ENV-006 deleted); SB-BB-013 assumption reference corrected (BB-RPT-005 deleted); SB-BB-014 forex bank list updated; version v1.0-Draft → v1.1-Draft |

**Files NOT modified:**
- HCM packs, ERP pack, OCI pack, OIC pack, AMS pack, Acumatica pack, Governance packs — all outside WP14D scope.

---

## 7. Validation Results

| Check | Result |
|---|---|
| MD body assumption count = 117 | PASS ✓ |
| CSV row count = 117 | PASS ✓ |
| Frontmatter `assumption_count` = 117 | PASS ✓ |
| Section index total = 117 | PASS ✓ |
| All MD IDs unique | PASS ✓ (117 unique IDs) |
| MD ↔ CSV cross-match | PASS ✓ (0 orphaned IDs in either direction) |
| Deleted IDs absent from MD | PASS ✓ |
| Deleted IDs absent from CSV | PASS ✓ |
| BU decision tags in MD body | PASS ✓ (0 tags — all resolved tags removed) |
| CSV `bu_decision_ref` for non-BU-BB-002 rows blank | PASS ✓ |
| BB-EXT-008 references BU-BB-002 correctly | PASS ✓ |

---

## 8. Governance Rules Verified (Standing Constraints)

All standing governance rules were verified during remediation. No violations were introduced:

| Rule | Status |
|---|---|
| BeBanking SWIFT rule: bank-intermediated model only | MAINTAINED — BB-BNK-002 and BB-EXC-008 unchanged |
| BeBanking Acumatica payroll rule: BB-PYR assumes Oracle EBS + PaySpace only | MAINTAINED — BB-PYR-002 updated to reflect confirmed sources; Acumatica payroll prohibition explicitly retained |
| BeBanking SAP rule: "SAP environments" only, no module claims | MAINTAINED — BB-INT-002 updated with correct framing |
| BU-OCI-007 PERMANENTLY WITHDRAWN: no BeBanking-specific OCI cost assumption | MAINTAINED — no such assumption introduced |
| Source pipeline: only Approved/ content in proposals | NOTED — pack remains Draft until BU-BB-002 resolved |
| Assumption status: only Approved assumptions may be assembled | NOTED — pack remains Draft; status will be promoted when BU-BB-002 resolved and BU Lead signs off |

---

## 9. Readiness Score

| Dimension | Pre-WP14D | Post-WP14D |
|---|---|---|
| Structural completeness | 8/10 | 9/10 |
| Governance consistency | 8/10 | 9/10 |
| Commercial protection | 8/10 | 9/10 |
| Technical accuracy | 8/10 | 9/10 |
| SA-specific coverage | 9/10 | 9/10 |
| BU Decision Register quality | 9/10 | 9/10 |
| **Overall** | **8.3/10** | **9.0/10** |

---

## 10. Recommendation

**Ready for BU Lead Approval — 1 decision pending (BU-BB-002).**

The BeBanking Base Assumption Pack is substantively remediated. 9 of 10 BU decisions have been resolved and applied. The pack is internally consistent, passes all structural validation checks, and is aligned with all standing governance rules.

**The only remaining blocker before Approved v1.0 is:**

> **BU-BB-002:** New bank onboarding fee model post-go-live — BeBanking BU Lead must explicitly confirm whether a new bank added after go-live is (a) always a Change Request, or (b) subject to other conditions. BB-EXT-008 positions it as CR, but an explicit BU decision is required before this is locked.

Once BU-BB-002 is resolved and the BU Lead signs off the pack, the following actions will follow:
1. Set pack `status` to `Approved v1.0`
2. Update `assumption_count` in frontmatter (already correct at 117)
3. Update governance registers (GOVERNANCE_MASTER_DECISION_REGISTER.md)
4. Update HANDOVER.md and AI_CONTEXT.md with BB pack approval

---

*WP14D_BEBANKING_REMEDIATION_REPORT v1.0 | WP14D | 2026-06-18*
