# Wave 1 Review Pack
**Prepared:** 2026-06-08 | **Reviewer:** Hein Blignaut | **Total candidates:** 28
**Last updated:** 2026-06-09 — Session A fact validation complete; 6 candidates promoted to Review_Required

---

## Session A Progress — 2026-06-09

| ID | File | Status | Notes |
|---|---|---|---|
| W1S1-001 | Company Overview | **Review_Required** ✓ | Fact updates applied. Awaiting BU lead approval. |
| W1S1-002 | Company History | Candidate — blocking item | Fact updates applied. Founder bio approval from Hein required. |
| W1S1-003 | Oracle Partnership | Candidate — blocking item | Credential rewrite applied. Hein to confirm Oracle Level 1 language. |
| W1S1-004 | Acumatica Partnership | **Review_Required** ✓ | Fact updates applied. Awaiting BU lead approval. |
| W1S1-005 | BeBanking Overview | **Review_Required** ✓ | SAP removed, bank wording updated. Acumatica integration note flagged for BeBanking BU. |
| W1S1-006 | Awards and Recognition | Candidate — blocking item | 2024 awards added. URL verification for success stories still outstanding. |
| W1S1-007 | Delivery Model | **Review_Required** ✓ | Fact updates applied. Awaiting BU lead approval. |
| W1S1-008 | Geographic Presence | **Review_Required** ✓ | Geography revised. Awaiting BU lead approval. |
| W1S1-009 | Key Differentiators | **Review_Required** ✓ | Headcount corrected. Awaiting BU lead approval. |

**Session A review work:** `00_Governance/Session_A_Review_Workbook.md` | `00_Governance/FACT_RESOLUTION_REPORT.md`

---

This document guides the Wave 1 review. It assigns a priority to each candidate, explains the reasoning, groups related files for efficient review, and recommends a sequence that delivers the greatest increase in KB value with the least total review effort.

No extraction candidates are modified by this document.

---

## How to Use This Pack

1. Work through the **Recommended Review Sequence** (Section 3) in order.
2. For each file, open it, verify the flagged `[UPDATE]` items against current knowledge, and decide: **advance to Review_Required** (passes self-review) or **return with comments** (issues found).
3. Files that pass self-review go to `07_Approved_Content/Review_Required/` with `review_status: Review_Required` in the metadata block.
4. Files that cannot be advanced yet stay in `Candidate_Content/` — add a note to `EXTRACTION_LOG.csv` explaining the hold.
5. The three STRUCTURE ONLY gap files (W1S2-006, W1S2-007, W1S2-008) **cannot advance to Review_Required** without authored content. They are flagged separately.

---

## Section 1 — Priority Index (All 28 Candidates)

### Priority Definitions

| Priority | Meaning |
|---|---|
| **Critical** | Foundational content used across all tenders regardless of BU. Blocks multiple tenders while unapproved. |
| **High** | Significant value for one BU; likely to be needed in near-term tenders; low review effort relative to value. |
| **Medium** | Useful supplementary content; not typically the deciding section in a tender; can wait until Critical and High are resolved. |
| **Low** | Either a content gap (cannot approve without authoring) or content requiring external confirmation before self-review is possible. |

---

### Set 1 — Company Profile Master (Cross_BU/)

| ID | File | Source | BU | Content Type | Readiness | Priority | Rationale |
|---|---|---|---|---|---|---|---|
| W1S1-001 | Company Overview | Oracle Fusion Template Sept 2024 | Cross_BU | Corporate Profile | MODERNISE | **Critical** | Opens every tender response. Required by every BU. Single most-used section across the KB. |
| W1S1-002 | Company History | Oracle Fusion Template Sept 2024 | Cross_BU | Corporate Profile | MODERNISE | **Critical** | Used alongside Company Overview in all tenders. Reviews W1S1-001 facts — review together in one sitting. |
| W1S1-003 | Oracle Partnership | Oracle Fusion Template Sept 2024 | Oracle | Partnership Statement | MODERNISE | **Critical** | Required in every Oracle tender. Partner tier, certifications, and awards must be confirmed. Blocks all Oracle tenders while unapproved. |
| W1S1-004 | Acumatica Partnership | Acumatica Sept 2025 Template | Acumatica | Partnership Statement | MODERNISE | **Critical** | Required in every Acumatica tender. Analogous to W1S1-003. Review together with W1S1-003 — same factual categories. |
| W1S1-005 | BeBanking Overview | HyDac V5.1 Template BeBanking Dec 2024 | BeBanking | Product Overview | DIRECT | **Critical** | Required in every BeBanking tender. DIRECT readiness — lowest review effort in the entire set. Approve quickly. |
| W1S1-006 | Awards and Recognition | Oracle Fusion Template Sept 2024 | Cross_BU | Awards | MODERNISE | **High** | Strengthens all tenders. Award list current to 2019 — confirm whether newer awards exist. Review alongside W1S1-003. |
| W1S1-007 | Delivery Model | Oracle Fusion Template Sept 2024 | Cross_BU | Delivery Model | MODERNISE | **Critical** | Products and Services list + billing models. Required for most tenders when responding to "how do you deliver." Verify Gold partner tier and DBA headcount claim. |
| W1S1-008 | Geographic Presence | Oracle Fusion Template Sept 2024 | Cross_BU | Geographic Presence | MODERNISE | **High** | Frequently required for international or public sector tenders. Verify which geographies are currently active. |
| W1S1-009 | Key Differentiators | Oracle Fusion Template Sept 2024 | Cross_BU | Key Differentiators | MODERNISE | **Critical** | The "why choose APPSolve" section. Used in executive summaries and evaluation criteria responses. Structurally excellent — verify headcount figure only. |

---

### Set 2 — Acumatica Module Library (Acumatica/)

| ID | File | Source | BU | Content Type | Readiness | Priority | Rationale |
|---|---|---|---|---|---|---|---|
| W1S2-001 | Financials | Acumatica Sept 2025 Template | Acumatica | Capability Statement | DIRECT | **High** | Core module required in every Acumatica tender. Sept 2025 vintage — product marketing, very likely current. Low review effort. |
| W1S2-002 | Distribution | Acumatica Sept 2025 Template | Acumatica | Capability Statement | DIRECT | **High** | High-frequency module in SA distribution sector tenders. Low review effort. |
| W1S2-003 | Inventory Control | Acumatica Sept 2025 Template | Acumatica | Capability Statement | DIRECT | **High** | Always included with Distribution. Low review effort. Review W1S2-001, W1S2-002, W1S2-003 as a batch — same source, same verification. |
| W1S2-004 | Manufacturing | HyDac V5.1 Dec 2024 | Acumatica | Capability Statement | DIRECT | **High** | Manufacturing is APPSolve's strongest Acumatica vertical (HyDac won Dec 2024). Content is detailed and recent. Verify against current Acumatica release notes. |
| W1S2-005 | CRM | HyDac V5.1 Dec 2024 | Acumatica | Capability Statement | DIRECT | **Medium** | Useful supplementary module. Overview-level — may need supplementation from a CRM-specific proposal. Review after the core distribution/manufacturing modules. |
| W1S2-006 | Field Services | — | Acumatica | Capability Statement | STRUCTURE ONLY | **Low** | **Content gap — cannot advance.** No source content. Authoring or additional source search required before this file can progress. |
| W1S2-007 | Payroll | — | Acumatica | Capability Statement | STRUCTURE ONLY | **Low** | **Content gap — cannot advance.** SA payroll integration approach needs to be confirmed with Hein first. |
| W1S2-008 | Construction | — | Acumatica | Capability Statement | STRUCTURE ONLY | **Low** | **Content gap — cannot advance.** Confirm whether APPSolve actively sells Construction Edition before investing review effort. |
| W1S2-009 | Project Accounting | HyDac V5.1 Dec 2024 | Acumatica | Capability Statement | DIRECT | **High** | Increasingly common in Acumatica tenders (professional services, engineering). Dec 2024 vintage. Review with W1S2-004 — same source. |

---

### Set 3 — BeBanking H2H Capability (BeBanking/)

**Important context for all Set 3 files:** All detailed BeBanking product content was sourced from SITA BeBanking Proposal v1.06 (June 2017, Oracle EBS-specific). All Set 3 files carry MODERNISE readiness. The core architecture (H2H, two-level approval, Connect Direct) is unlikely to have changed, but bank partnerships, Acumatica integration, and hosting options must be confirmed before any file advances beyond Review_Required.

**Recommended approach:** Review W1S3-001 to W1S3-004 first to confirm the core product story. The remaining six files can follow once the product overview and core payment files are validated.

| ID | File | Source | BU | Content Type | Readiness | Priority | Rationale |
|---|---|---|---|---|---|---|---|
| W1S3-001 | Product Overview | HyDac V5.1 + SITA v1.06 | BeBanking | Product Overview | DIRECT | **Critical** | Opens every BeBanking tender. DIRECT readiness — the introductory paragraphs are verbatim current APPSolve IP. Lowest review effort in Set 3. |
| W1S3-002 | Host-to-Host Banking | SITA v1.06 | BeBanking | Capability Statement | MODERNISE | **Critical** | Core H2H architecture description. Required in all BeBanking tenders. Must confirm: (1) two-level approval still current model, (2) bank partnerships for 2026. |
| W1S3-003 | Supplier Payments | SITA v1.06 | BeBanking | Capability Statement | MODERNISE | **Critical** | Supplier H2H is the most common BeBanking use case. High tender frequency. Review W1S3-002 and W1S3-003 together — closely related content. |
| W1S3-004 | Payroll Payments | SITA v1.06 | BeBanking | Capability Statement | MODERNISE | **High** | Second most common BeBanking module. Review alongside W1S3-003. Confirm ACB/SA payroll model is still current. |
| W1S3-005 | Forex Payments | SITA v1.06 (partial) | BeBanking | Capability Statement | STRUCTURE ONLY | **Low** | Partial gap — Automated Exchange Rates confirmed, full Forex processing not. Depends on Parliament FX Rates document review (Wave 2 action). Do not advance until Parliament doc reviewed. |
| W1S3-006 | ERP Integration | SITA v1.06 | BeBanking | Capability Statement | MODERNISE | **Medium** | Important for tenders that ask "how does BeBanking connect to your ERP." Currently Oracle EBS-specific — must add Acumatica integration before approving. Medium priority because it cannot be fully approved until the Acumatica integration model is documented. |
| W1S3-007 | Security | SITA v1.06 | BeBanking | Capability Statement | MODERNISE | **High** | Security and access control are evaluated in most formal tenders. Content is strong. Confirm Connect Direct vs. SFTP channel and whether MFA or POPIA obligations have been added since 2017. |
| W1S3-008 | Architecture | SITA v1.06 | BeBanking | Architecture | MODERNISE | **Medium** | Valuable for RFPs requiring technical architecture. Currently text-only — process flow diagram not extractable from DOCX. Advance as-is with a note; diagram to be added in a future cycle. |
| W1S3-009 | Hosting Model | SITA v1.06 | BeBanking | Hosting Model | MODERNISE | **Medium** | Needed when tenders ask about deployment model or commercial structure. Confirm whether cloud-hosted option now exists. |
| W1S3-010 | Monitoring and Automation | SITA v1.06 | BeBanking | Capability Statement | MODERNISE | **Medium** | Supports tenders requiring operational monitoring evidence. Confirm whether a BeBanking monitoring dashboard exists. |

---

## Section 2 — Priority Summary

| Priority | Count | Files |
|---|---|---|
| **Critical** | 8 | W1S1-001, W1S1-002, W1S1-003, W1S1-004, W1S1-005, W1S1-007, W1S1-009, W1S3-001 |
| **High** | 11 | W1S1-006, W1S1-008, W1S2-001, W1S2-002, W1S2-003, W1S2-004, W1S2-009, W1S3-002, W1S3-003, W1S3-004, W1S3-007 |
| **Medium** | 6 | W1S2-005, W1S3-006, W1S3-008, W1S3-009, W1S3-010, W1S3-005* |
| **Low** | 3 | W1S2-006, W1S2-007, W1S2-008 |

*W1S3-005 is assigned Medium rather than Low because the Automated Exchange Rates content within it is confirmed and can be extracted into a separate file — only the Forex Payment portion is a gap.

**Approving the 8 Critical files alone covers the core company profile and the opening BeBanking section — enough to assemble a near-complete tender response for any BU.**

**Approving Critical + High (19 files) provides full coverage of the company profile, Acumatica core modules, and BeBanking core payment capabilities — sufficient for most Acumatica and BeBanking tenders.**

---

## Section 3 — Recommended Review Sequence

Organised into four review sessions. Each session is designed to minimise context-switching and maximise value delivered per hour spent.

---

### Session A — Cross-BU Foundation (Critical priority)
**Effort estimate:** 2–3 hours | **Value:** Unblocks all three BUs

These files share the same factual update requirements (years in business, staff count, partner tiers, awards). Reviewing them together means the key facts are confirmed once and applied across all files in the session.

**Facts to confirm before starting Session A:**
- [ ] Current years in business (2026 − 2002 = 24)
- [ ] Current headcount (template says "110+ Senior Consultants")
- [ ] Oracle partner tier (template says Gold — confirm current status on Oracle Partner Network)
- [ ] Acumatica partner tier (template says Gold Certified — confirm current status)
- [ ] Any Oracle awards received since 2019
- [ ] Current active international geographies
- [ ] Hein's CV bio: "19 years' experience" — update to current years

| Step | File | Action | Note |
|---|---|---|---|
| A1 | W1S1-001 Company Overview | Update years, headcount, geographies. Check opening paragraph is still accurate. | Likely 15 min |
| A2 | W1S1-002 Company History | Update same facts as A1. This file references the same numbers — review directly after A1. | 15 min |
| A3 | W1S1-003 Oracle Partnership | Confirm Oracle partner tier and award list. | 10 min |
| A4 | W1S1-006 Awards and Recognition | Confirm no awards post-2019 are missing. Review alongside A3 — same source. | 10 min |
| A5 | W1S1-004 Acumatica Partnership | Confirm Acumatica partner tier and credentials. | 10 min |
| A6 | W1S1-007 Delivery Model | Confirm Gold partner tier and DBA headcount claim ("largest number of locally based Oracle Applications DBAs"). | 15 min |
| A7 | W1S1-009 Key Differentiators | Verify "100 senior resources" pool figure. Structurally strong — low effort. | 10 min |
| A8 | W1S1-008 Geographic Presence | Confirm which geographies are currently active. | 10 min |
| A9 | W1S1-005 BeBanking Overview | DIRECT readiness — 3 paragraphs, no factual claims to update. Confirm text is still current. | 5 min |

**Output of Session A:** 9 files advance to `Review_Required/`. Cross-BU foundation complete.

---

### Session B — Acumatica Module Library (High priority)
**Effort estimate:** 1.5–2 hours | **Value:** Completes Acumatica capability coverage for distribution and manufacturing tenders

These files are DIRECT readiness from Sept 2025 and Dec 2024 templates — minimal review required. The main verification is confirming no features have been deprecated or changed in the current Acumatica release.

**Confirm before starting Session B:**
- [ ] Current Acumatica release version (for release note verification)
- [ ] Whether the Shopify Commerce Connector, AI Insights, and Deferred Revenue modules are still current offerings (Sept 2025 template)

| Step | File | Action | Note |
|---|---|---|---|
| B1 | W1S2-001 Financials | Verify feature list against current Acumatica release. | 15 min |
| B2 | W1S2-002 Distribution | Same verification. Review as a batch with B1 and B3. | 10 min |
| B3 | W1S2-003 Inventory Control | Same verification. | 10 min |
| B4 | W1S2-004 Manufacturing | Review manufacturing module content. Dec 2024 HyDac win — high confidence in currency. Verify ECC and Estimating still current. | 20 min |
| B5 | W1S2-009 Project Accounting | Verify project accounting feature table against current release. | 15 min |
| B6 | W1S2-005 CRM | Overview-level content — verify it is still accurate. | 10 min |

**Output of Session B:** 6 files advance to `Review_Required/`. Acumatica module coverage complete for Distribution, Manufacturing, Financial Management, Inventory, Project Accounting, and CRM.

**Note on W1S2-006, W1S2-007, W1S2-008:** These three STRUCTURE ONLY files should not be opened for review in Session B. They require authoring, not reviewing. Log the required actions in `EXTRACTION_LOG.csv` and treat as Wave 2 / Wave 3 authoring tasks.

---

### Session C — BeBanking Core (Critical + High priority)
**Effort estimate:** 2–3 hours | **Value:** Enables BeBanking tender responses for the first time**

**Important pre-session action:** Before Session C, confirm the following with the BeBanking BU lead (or from current knowledge):

- [ ] Which South African banks does BeBanking currently certify? (Standard Bank confirmed; others?)
- [ ] Is Connect Direct still the primary bank channel, or has SFTP/API replaced it?
- [ ] Is the two-level approval architecture still the current BeBanking model?
- [ ] Is the ACB payroll format still the correct format for SA payroll H2H?
- [ ] Does BeBanking support the Acumatica integration — and if so, which Acumatica modules?
- [ ] Has the hosting model changed — is a cloud-hosted option now available?

These confirmations affect multiple files. Confirming them before Session C avoids re-opening files.

| Step | File | Action | Note |
|---|---|---|---|
| C1 | W1S3-001 Product Overview | DIRECT — confirm 3-paragraph intro is still accurate positioning. Add confirmed bank list. | 10 min |
| C2 | W1S3-002 H2H Banking | Confirm two-level approval architecture. Add confirmed bank list. Add Acumatica integration context. | 20 min |
| C3 | W1S3-003 Supplier Payments | Confirm AVS and Bank Account Approval model. Verify against current capability. | 15 min |
| C4 | W1S3-004 Payroll Payments | Confirm ACB format and payroll approval segregation. Add Acumatica context if applicable. | 15 min |
| C5 | W1S3-007 Security | Confirm Connect Direct vs. SFTP. Add POPIA reference if applicable. | 15 min |

**Output of Session C:** 5 files advance to `Review_Required/`. Core BeBanking product story is reviewable by a second reviewer.

---

### Session D — BeBanking Supplementary (Medium priority)
**Effort estimate:** 1.5–2 hours | **Value:** Completes BeBanking capability coverage

Run Session D after the pre-session confirmations from Session C are complete. These files build on the core established in Session C.

| Step | File | Action | Note |
|---|---|---|---|
| D1 | W1S3-006 ERP Integration | Add Acumatica integration detail (from Session C confirmation). This file is Oracle-only without it — advance conditionally with an integration gap noted. | 20 min |
| D2 | W1S3-009 Hosting Model | Confirm whether cloud-hosted option now exists. Update licensing model names if changed. | 15 min |
| D3 | W1S3-010 Monitoring and Automation | Confirm whether a BeBanking monitoring dashboard exists. Advance the confirmed automation content; flag the monitoring question. | 15 min |
| D4 | W1S3-008 Architecture | Advance as-is with a note that the process flow diagram (SITA v1.06 PDF Appendix 5.2) has not yet been recovered. Architecture text is reviewable without it. | 15 min |
| D5 | W1S3-005 Forex Payments | **Hold for Wave 2.** The Automated Exchange Rates content is approvable; the Forex Payment claim is not confirmed. Consider splitting: advance the Exchange Rates content; retain the Forex gap as a Wave 2 research item. | 20 min |

**Output of Session D:** 4 files advance to `Review_Required/`. W1S3-005 either held or split.

---

## Section 4 — Files That Cannot Advance Without Additional Action

These files require action before they can enter the review pipeline. They should not be opened as review items.

| File | Issue | Required Action | Who | When |
|---|---|---|---|---|
| W1S2-006 Field Services | No source content exists | Search historical corpus for field service proposals; or source current product description from Acumatica partner portal | Hein Blignaut | Wave 2 |
| W1S2-007 Payroll | SA payroll compliance unclear; Acumatica Payroll is US-focused | Confirm APPSolve's SA payroll integration approach (VIP, Sage, other) | Hein Blignaut | Wave 2 |
| W1S2-008 Construction | No source content exists; unclear if APPSolve sells this edition | Confirm whether APPSolve actively sells Acumatica Construction Edition | Hein Blignaut | Wave 2 |
| W1S3-005 Forex Payments | Forex Payment processing (SWIFT/TT) not confirmed | Review `Parties/Customers/Parliament/APPSolve BeBanking Parliament FX Rates.docx` | Hein Blignaut | Wave 2 priority |
| W1S3-006 ERP Integration (Acumatica portion) | Oracle EBS integration documented; Acumatica integration undocumented | Document Acumatica integration architecture with BeBanking BU lead | Hein Blignaut | Before Session D |
| W1S3-008 Architecture (diagram) | Process flow diagram in SITA v1.06 PDF Appendix 5.2 not extracted | Open SITA v1.06 PDF, review diagram, describe or photograph it | Hein Blignaut | Session D prep |

---

## Section 5 — Expected Output After All Four Sessions

| Metric | Count |
|---|---|
| Files advanced to Review_Required | 24–25 |
| Files held pending additional action | 3–4 |
| Files not approvable without authoring (gaps) | 3 |
| Total | 28 |

Once files are in Review_Required, they are ready for BU lead sign-off. At that point they can be moved to `Approved/`, the register updated, and content copied to its KB destination folder — making it available for tender use.

**Completing Sessions A and C alone (14 files) is sufficient to begin writing a full tender response for any of the three BUs from approved KB content.**

---

## Section 6 — Review Checklist (per file)

When reviewing each file, use this checklist:

- [ ] All `[UPDATE]` markers have been addressed
- [ ] All factual claims are verified and current
- [ ] No client-specific language remains
- [ ] `review_status` changed from `Candidate` to `Review_Required` in the metadata block
- [ ] `extracted_by` and `extraction_date` fields are populated
- [ ] File moved to `07_Approved_Content/Review_Required/`
- [ ] `EXTRACTION_LOG.csv` row updated: `review_status` column set to `Review_Required`

---

*This pack does not modify any extraction candidate. All 28 files remain in `07_Approved_Content/Candidate_Content/` unchanged.*
