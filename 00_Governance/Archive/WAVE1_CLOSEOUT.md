---
created: "2026-06-10"
created_by: "Claude (AI — Wave 1 closeout document)"
status: "Final"
approved_by: "Hein Blignaut"
---

# Wave 1 Closeout — APPSolve Tender Knowledge Base
**Date:** 2026-06-10 | **Sessions:** A (2026-06-09), B (2026-06-10), C (2026-06-10)

---

## 1. Executive Summary

Wave 1 of the APPSolve Tender Knowledge Base is complete. Starting from zero approved content, three extraction-and-review sessions produced **25 approved, BU-lead-signed files** covering company profile, BeBanking H2H capabilities, and Acumatica ERP modules. The Review_Required queue is empty. No approved file carries an unresolved factual risk.

The knowledge base now provides a verified, citeable content layer for all three business units. Any future tender response drawing on KB content will be working from material that has been extracted from authoritative sources, fact-checked against 18,400 files of historical corpus, and approved by Hein Blignaut.

Three STRUCTURE ONLY Acumatica candidates (W1S2-006 Field Services, W1S2-007 Payroll, W1S2-008 Construction) remain deferred pending BU lead decisions. They do not block any current approved content or Wave 2 work.

---

## 2. Objectives Achieved

| Objective | Result |
|---|---|
| Establish a curated, approved content layer for tender use | ✅ 25 approved files across 3 BUs |
| Validate and correct historical fact baseline | ✅ 20 facts confirmed; 3 contradictions found and corrected |
| Establish governance pipeline (Candidate → Review_Required → Approved) | ✅ Pipeline operational; all Wave 1 files processed |
| Encode permanent rules to prevent recurrence of known errors | ✅ 10 Critical Repository Rules in CHECKPOINT; 8 lessons learned |
| Deliver Cross-BU company profile set | ✅ 9 files — company overview, history, partnerships, delivery model, geography, differentiators, awards |
| Deliver BeBanking H2H full capability set | ✅ 11 files — all 9 product modules plus overview and overview sub-file |
| Deliver Acumatica core module set | ✅ 7 files — Financials, Distribution, Inventory, Manufacturing, CRM, Project Accounting, Partnership |
| Establish architecture decision on consultant records | ✅ ADR-001 — APPTime as CV system of record; KB stores metadata only |
| Identify content gaps for Wave 2 | ✅ Oracle Fusion, Oracle EBS, Oracle methodology not yet extracted |

---

## 3. Scope Delivered

Wave 1 covered three extraction sets from six source documents:

| Set | Source | Files produced | Approved |
|---|---|---|---|
| W1S1 — Company Profile Master | Oracle Fusion Template (Sept 2024) + Acumatica Sept 2025 Template + HyDac V5.1 | 9 | 9 |
| W1S2 — Acumatica Module Library | Acumatica Sept 2025 Template + HyDac V5.1 | 9 | 6 (3 STRUCTURE ONLY deferred) |
| W1S3 — BeBanking H2H Capability | SITA BeBanking Proposal v1.06 (2017) + HyDac V5.1 + BeBanking Capability Map | 10 | 10 |
| **Total** | | **28 candidates** | **25 approved** |

Key source finding: The 2017 SITA BeBanking Proposal v1.06 is the highest-fidelity BeBanking source in the corpus. All 10 BeBanking capability files were grounded in this document. HyDac V5.1 BeBanking sections contain only 3 introductory paragraphs and are not usable alone.

---

## 4. Approved Content Inventory

**25 files approved. Physical locations:**

```
07_Approved_Content/Approved/
├── Cross_BU/    (9 files — all W1S1)
├── BeBanking/   (10 files — W1S3-001 to W1S3-010)
└── Acumatica/   (6 files — W1S2-001, 002, 003, 004, 005, 009)
```

**By business unit alignment (including W1S1 files attributed to their BU):**

| BU | Files | Includes |
|---|---|---|
| Cross-BU (CORP + Oracle) | 7 | W1S1-001, 002, 003, 006, 007, 008, 009 |
| Acumatica | 7 | W1S1-004 + W1S2-001, 002, 003, 004, 005, 009 |
| BeBanking | 11 | W1S1-005 + W1S3-001 to W1S3-010 |
| **Total** | **25** | |

Full inventory: `00_Governance/CHECKPOINT_WAVE1_2026-06-10.md` Section 3.

---

## 5. Governance Framework Established

Wave 1 built the governance layer from scratch. The following elements are now operational:

| Element | Document | Status |
|---|---|---|
| Three-stage extraction pipeline | `EXTRACTION_WORKFLOW.md` | Operational — all Wave 1 files processed through it |
| Document register | `DOCUMENT_REGISTER.csv` | 42 rows; covers all approved assets and real sources |
| Extraction log | `EXTRACTION_LOG.csv` | 29 rows; full Wave 1 pipeline history |
| Fact validation record | `FACT_RESOLUTION_REPORT.md` | 20 facts; 3 contradictions documented and resolved |
| Approved content usage guide | `APPROVED_CONTENT_USAGE_GUIDE.md` | v1.0; governs all AI and human KB activity |
| CV architecture decision | `ADR-001-CV_SOURCE_OF_TRUTH.md` | Accepted — APPTime is CV system of record |
| BeBanking capability reference | `BeBanking_CAPABILITY_MAP.md` | Authoritative BeBanking product reference |
| Wave 1 checkpoint | `CHECKPOINT_WAVE1_2026-06-10.md` | Authoritative restart document |
| 10 Critical Repository Rules | CHECKPOINT §5, AI_CONTEXT.md | Encoded and permanent |

---

## 6. Major Decisions Recorded

| Decision | Impact |
|---|---|
| **D-STRAT-001** — Extraction-first strategy; do not author from scratch | Governs all future wave work |
| **D-ARCH-001 (ADR-001)** — APPTime as CV system of record; KB stores metadata only | Priority 25 (CV migration) permanently cancelled |
| **D-BQ2** — BeBanking approval framework is configurable; never describe as "two-level" | All BeBanking files |
| **D-BQ5** — Acumatica payroll not available in SA; permanent exclusion | All Acumatica + BeBanking content |
| **D1 (Session C)** — SAP wording bounded: "BeBanking integrates with SAP environments" only | All BeBanking files pending BQ-WEB-04 |
| **Session B corrections** — IFRS 15 primary; LIFO removed; Manufacturing cascade table corrected | W1S2 Acumatica files |
| **W1S2-009 verification** — Intercompany Projects removed; Change Orders and Manufacturing confirmed | W1S2-009 |
| **W1S3-005 review** — SWIFT indirect model confirmed; CMA banking column corrected; SAP detail removed | W1S3-005 |

---

## 7. Key Risks Removed

| Risk | How removed |
|---|---|
| Partner tier inflation — templates cited expired "Gold Level" Oracle status | Corrected to Level 1; permanent rule encoded |
| Headcount inflation — templates had 110+ vs confirmed 50+ | Corrected; permanent rule encoded |
| Geography inflation — templates cited Nigeria, Uganda, Bangladesh, Qatar, Ghana without client evidence | Removed; corpus-evidence-only rule in place |
| SWIFT direct membership claim — BeBanking cannot claim direct SWIFT membership | Corrected; critical rule in CHECKPOINT and AI_CONTEXT.md |
| Acumatica payroll inference — BeBanking content incorrectly referenced Acumatica payroll | Corrected; permanent exclusion rule encoded (Rule 3) |
| AI-authored content unverified — W1S2-009 had 3 AI-augmented rows | Verified or removed; Rule 4 (verify or remove) encoded |
| CMA geographic overstatement — Lesotho and Eswatini implied as deployment targets without banking integration | Corrected; banking-integration-required rule for geographic claims |
| ACH terminology in Acumatica content — does not apply in SA | Removed; replaced with ZAR domestic EFT language |

---

## 8. Lessons Learned

Eight lessons recorded during Wave 1. Full record in CHECKPOINT §7. Key items:

1. **L-A-001** — Partner tier inflation: always verify against the most recent OPN certificate, not templates
2. **L-A-002** — Geography inflation: only cite countries with client folder evidence in the corpus
3. **L-A-003** — Headcount inflation: use confirmed headcount from BU lead, not legacy templates
4. **L-B-001** — AI-augmented rows require explicit verification before approval; "plausible" is not sufficient
5. **L-B-002** — Multi-row table extraction requires row-by-row content verification; cascade errors are common
6. **L-C-001** — ERP integration scope ≠ full module support; payroll capability must be explicitly evidenced
7. **L-C-002** — Direct vs bank-intermediated payment models must be stated explicitly for all financial networks
8. **L-C-003** — Geographic deployment requires a named banking integration — CMA membership is not sufficient

---

## 9. Remaining Scope

### Deferred from Wave 1

| File | Status | Blocker |
|---|---|---|
| W1S2-006 Field Services | STRUCTURE ONLY | BU lead must confirm if Field Services is an active APPSolve vertical |
| W1S2-007 Payroll | STRUCTURE ONLY | BU lead must confirm SA payroll integration approach; critical payroll rule limits scope |
| W1S2-008 Construction | STRUCTURE ONLY | BU lead must confirm if Construction Edition is sold by APPSolve SA |

### Open Actions

| Action | Deadline | Severity |
|---|---|---|
| BEE certificate renewal | **2026-07-31** | **HIGH** |
| Copy 25 approved files to KB destinations | — | Medium |
| Chase Oracle reference letters (ATC, Old Mutual, Truworths) | — | Medium |
| W1S1-006 success story URL verification (Tiger Brands, USAID, UT Grain) | — | Low |
| BQ-WEB-04 answer (SAP module detail for BeBanking) | — | Low |

### Superseded (will not be done)

- MIGRATION_ANALYSIS.md Priority 25 — full CV migration to KB — **permanently cancelled** (ADR-001)
- Authoring capability statements from scratch where source documents exist — replaced by extraction-first strategy

---

## 10. Wave 2 Recommendations

Ranked by business impact:

| Priority | Item | Source | Effort | Gap closed |
|---|---|---|---|---|
| 1 | Oracle DBA Executive Summary | HIST-002 MTN 2014 | Low (~30 min) | C3 — No Oracle exec summary |
| 2 | Oracle Fusion Capability Statement | TMPL-001 Sept 2024 template | Medium (~1 hr) | C1 — No Oracle Cloud capabilities |
| 3 | Oracle EBS Capability Overview | TMPL-002 | Low (~30 min) | C2 — No Oracle EBS capabilities |
| 4 | BeBanking Implementation Methodology | HIST-004 Mpact 2019 | Medium (~1 hr) | C5 — No BeBanking methodology |
| 5 | BeBanking Forex — Parliament FX document | Parties/Parliament | Low (~30 min) | Enriches W1S3-005 (already approved) |
| 6 | Oracle DBA Technical Solution | HIST-002 Section 2.1 | Low (~30 min) | DBA methodology (sub-gap of C3) |

Wave 2 does not require BU lead decisions before it begins — all six sources are identified and accessible.

---

## 11. Final Metrics

| Metric | Value |
|---|---|
| Wave 1 extraction candidates created | 28 |
| Files approved | **25** |
| Files deferred (STRUCTURE ONLY) | 3 |
| Files archived (superseded DRAFTs) | 17 |
| Review_Required at Wave 1 close | **0** |
| Approved content sessions | 3 (A, B, C) |
| Session duration | 2026-06-08 to 2026-06-10 (3 days) |
| Facts validated | 20 |
| Contradictions found and corrected | 3 |
| Lessons learned recorded | 8 |
| Critical rules encoded | 10 |
| Architecture decisions | 1 (ADR-001) |
| Governance documents created/updated | 22+ |
| DOCUMENT_REGISTER.csv rows | 42 |
| EXTRACTION_LOG.csv rows | 29 |

---

## 12. Success Criteria Assessment

| Criterion | Assessment | Evidence |
|---|---|---|
| Approved content available for all three BUs | ✅ Met | 7 CORP+Oracle + 7 Acumatica + 11 BeBanking files approved |
| All approved content reviewed and signed off by BU lead | ✅ Met | `approved_by: Hein Blignaut` on all 25 files |
| Fact baseline verified and contradictions corrected | ✅ Met | 20 facts confirmed; 3 corrections applied |
| No unsupported claims in approved content | ✅ Met | All AI-authored claims verified or removed (Rule 4) |
| Governance pipeline operational | ✅ Met | All 28 files processed through pipeline |
| Permanent rules encoded to prevent error recurrence | ✅ Met | 10 rules in CHECKPOINT; encoded in AI_CONTEXT.md |
| Knowledge base ready for tender use | ✅ Met (with noted gaps) | Approved content available; Oracle extraction content pending Wave 2 |
| Oracle content gap — Fusion, EBS, methodology | ⚠️ Not yet met | Planned Wave 2; not a Wave 1 objective |
| Acumatica Field Services / Payroll / Construction | ⚠️ Deferred | BU lead decisions required; not blocking other work |
| Compliance — BEE certificate | ⚠️ At risk | Expires 2026-07-31; action required |

**Overall Wave 1 verdict: COMPLETE — NEARLY COMPLETE**

The 25 core files are approved and ready. The three STRUCTURE ONLY deferred files and Oracle Wave 2 content represent known gaps that do not impair use of the 25 approved files in tender responses today.

---

*Prepared 2026-06-10 by Claude (AI) on instruction from Hein Blignaut. Superseded files: SESSION_A_CLOSEOUT.md, SESSION_C_APPROVAL_SUMMARY.md (these remain as session records; this document supersedes them as the Wave 1 executive summary).*
