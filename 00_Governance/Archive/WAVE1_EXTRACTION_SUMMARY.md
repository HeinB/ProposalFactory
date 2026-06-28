# Wave 1 Extraction Summary
**Date:** 2026-06-08
**Status:** Complete — all candidates in Candidate_Content/. None approved for tender use.

---

## Candidates Created

**Total: 28 extraction candidate files**

| Set | Folder | Count | Files |
|---|---|---|---|
| Set 1 — Company Profile Master | `Cross_BU/` | 9 | W1S1-001 to W1S1-009 |
| Set 2 — Acumatica Module Library | `Acumatica/` | 9 | W1S2-001 to W1S2-009 |
| Set 3 — BeBanking H2H Capability | `BeBanking/` | 10 | W1S3-001 to W1S3-010 |

---

## Source Documents Used

| Source | Files Extracted | Notes |
|---|---|---|
| Oracle Fusion Template.docx (Sept 2024) | W1S1-001 to W1S1-003, W1S1-006 to W1S1-009 | Company Profile, Awards, Delivery Model, Key Differentiators |
| Acumatica Proposal Template Sept2025 BH.docx | W1S1-004, W1S2-001, W1S2-002, W1S2-003 | Acumatica Partnership, Financials, Distribution, Inventory |
| APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx | W1S1-005 | BeBanking Overview (intro only — 3 paragraphs) |
| APPSolve_HyDac_Proposal_20241211_V5.1.docx | W1S2-004, W1S2-005, W1S2-009 | Manufacturing, CRM, Project Accounting |
| APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx | W1S3-001 to W1S3-010 | Full BeBanking H2H suite |

---

## Readiness Distribution

| Readiness | Count | Files |
|---|---|---|
| DIRECT | 14 | W1S1-005; W1S2-001 to W1S2-005, W1S2-009; W1S3-001 |
| MODERNISE | 11 | W1S1-001 to W1S1-004, W1S1-006 to W1S1-009; W1S3-002 to W1S3-010 |
| STRUCTURE ONLY (content gap) | 3 | W1S2-006 (Field Services), W1S2-007 (Payroll), W1S2-008 (Construction) |

---

## Content Gaps Discovered

### Confirmed Gaps (no source content found)

1. **Acumatica Field Services** (W1S2-006)
   - Not in scope in any reviewed template
   - Only a one-line overview description in the component table
   - **Action:** Search historical corpus for field service client proposals; or source from Acumatica partner portal

2. **Acumatica Payroll** (W1S2-007)
   - Not in any reviewed template
   - Likely not applicable in South African context — Acumatica Payroll is US-focused
   - **Action:** Confirm APPSolve's SA payroll integration approach (VIP Payroll, Sage, etc.)

3. **Acumatica Construction Edition** (W1S2-008)
   - Not in any reviewed template
   - **Action:** Confirm if APPSolve sells Construction Edition; if so, identify relevant proposal in corpus

### Partial Gap

4. **BeBanking Forex Payments** (W1S3-005)
   - Automated Exchange Rates confirmed (SITA v1.06)
   - Full forex payment processing (SWIFT, TT) not confirmed
   - Parliament BeBanking FX Rates document found: `Parties/Customers/Parliament/APPSolve BeBanking Parliament FX Rates.docx` — review this in Wave 2
   - **Action:** Open Parliament FX Rates document to determine scope of forex capability

### Significant Finding: BeBanking H2H Content Source

**Important correction to Wave 1 plan:** The BeBanking section in HyDac V5.1 (both versions) contains only 3 introductory paragraphs — not a detailed capability breakdown. The detailed BeBanking product content is in the **SITA BeBanking Proposal v1.06 (June 2017)**, specifically in the Appendix: Product Module Summary and Proposed Engagement sections.

The SITA proposal is Oracle EBS-specific and 2017 vintage. All Wave 1 BeBanking candidates carry MODERNISE readiness and require Hein Blignaut / BeBanking BU lead review to confirm current capabilities, bank partnerships, and Acumatica integration model.

---

## Review Actions Required Before Any File Progresses

The following specific updates are flagged across all 28 files:

### Company Profile (Set 1)
- [ ] **Years in business:** Update "22 years" → confirm exact figure for 2026 (should be 24)
- [ ] **Staff count:** Verify current headcount (template says "110+ Senior Consultants")
- [ ] **Oracle partner tier:** Confirm Gold or higher — verify on Oracle Partner Network
- [ ] **Acumatica partner tier:** Confirm Gold Certified or higher
- [ ] **Awards since 2019:** Confirm no Oracle awards received between 2019 and 2026 are missing
- [ ] **Active geographies:** Verify which international markets are currently active
- [ ] **Contact details:** Hein, Andre, Jeanette — verify titles and roles are current
- [ ] **"19 years' experience"** in Hein's bio: Update to current years (2026 - 1996 ≈ 30)

### BeBanking (Set 3)
- [ ] **Bank partnerships:** Confirm full list of certified South African banks for 2026
- [ ] **Connect Direct vs. SFTP:** Confirm current primary bank channel
- [ ] **Acumatica integration architecture:** Document separately — SITA content is Oracle-only
- [ ] **H2H process flow diagram:** Open SITA v1.06 PDF Appendix 5.2 and extract/describe
- [ ] **Forex capability:** Review Parliament FX Rates document
- [ ] **Hosting model:** Confirm whether cloud-hosted BeBanking is now available
- [ ] **Monitoring dashboard:** Confirm whether a BeBanking monitoring/alerting UI exists

---

## Archive: Process Flow Diagram Not Extracted

The SITA BeBanking Proposal v1.06, Appendix 5.2 "Host to Host Process Flow" contains what is likely an architectural diagram. The DOCX XML parser extracted no text from this section, which is normal for image-only pages. This diagram should be extracted directly from the PDF version and catalogued separately once confirmed as current.

---

## Wave 2 Priorities

Based on Wave 1 findings, the following extractions should proceed next:

### Wave 2 — Oracle Capability and Methodology

1. **Oracle Fusion Capability Statement** (TMPL-001, Section "Oracle Fusion Information") — W2-ORA-001
2. **Oracle DBA Executive Summary** (HIST-002 MTN 2014, APPSolve Executive Summary.docx) — W2-ORA-002
3. **Oracle DBA Technical Solution / Methodology** (HIST-002, Section 2.1) — W2-ORA-003
4. **Oracle EBS Capability Overview** (TMPL-002, Oracle EBS Template) — W2-ORA-004

### Wave 2 — BeBanking Gap Closure

5. **Forex Payments** — review Parliament FX Rates document — W2-BB-001
6. **BeBanking Support Model / Hybrid Support** — from HIST-003 SITA Exec Summary — W2-BB-002
7. **BeBanking H2H Process Flow** — open SITA v1.06 PDF Appendix 5.2 — W2-BB-003

### Wave 2 — BeBanking Methodology (fills largest gap)

8. **BeBanking Implementation Methodology** (HIST-004 Mpact 2019) — W2-BB-004
9. **BeBanking Delivery Phases** (HIST-004 Mpact 2019) — W2-BB-005

### Wave 2 — Acumatica Gap Closure

10. **Acumatica Field Services** — search corpus for field service client proposals
11. **Acumatica Payroll** — confirm SA payroll integration approach with Hein

---

## Wave 1 Extraction Log Reference

All 28 extractions have placeholder rows in `00_Governance/EXTRACTION_LOG.csv`. When files progress through the review pipeline, update `extraction_date`, `extracted_by`, `review_status`, and `reviewer` fields in that CSV.
