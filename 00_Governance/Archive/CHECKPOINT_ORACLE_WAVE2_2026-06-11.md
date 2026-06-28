---
checkpoint_id: "CHECKPOINT-ORA-W2-2026-06-11"
created: "2026-06-11"
created_by: "Claude (AI — checkpoint only; no extraction work performed)"
scope: "Wave 1 complete + Oracle Wave 2 Sessions 1 and 2 (W2S1-001 and W2S1-003)"
status: "Active — reference document for session restarts after 2026-06-11"
predecessor: "00_Governance/CHECKPOINT_WAVE1_2026-06-10.md"
---

# Oracle Wave 2 Checkpoint
**Date:** 2026-06-11 | **Owner:** Hein Blignaut | **Purpose:** Complete repository state snapshot after Wave 1 approval cycle and Oracle Wave 2 Sessions 1 and 2. Use this document to reconstruct context at session restart.

> **Scope constraint:** This checkpoint captures repository state only. No extraction work was performed and no Oracle deliverables were authored in creating this document.

---

## Section 1: Executive Summary

### What Was Accomplished

**Wave 1 — COMPLETE (2026-06-10).**
All 25 Wave 1 files approved by Hein Blignaut across three sessions: Session A (9 Cross-BU files, 2026-06-09), Session B (6 Acumatica module files, 2026-06-10), Session C (10 BeBanking H2H files including W1S3-005, 2026-06-10). Review_Required queue is empty. Three Acumatica STRUCTURE ONLY candidates (W1S2-006, W1S2-007, W1S2-008) remain blocked on BU lead decisions.

**Oracle Wave 2 — In progress (started 2026-06-11).**

**W2S1-001 Oracle Fusion Capability Statement — CANDIDATE created 2026-06-11.**
12 sections. Primary sources: Oracle Fusion Template (TMPL-001) and SAA HCM RFP (June 2025). Finance/ERP sections strengthened using Mpact Packaging (2024) and BankServAfrica (2025) proposals. Two material errors corrected during strengthening: Cape Union Mart misclassified as SCM reference (removed), Nala Energy cited as 4-country deployment without evidence (corrected to confirmed single-market). Factual risk FR-004 (SCM section — no approved reference client) requires BU Lead decision before promotion. Review items: A-001 through A-006, six client-status assumptions.

**W2S1-003 Oracle DBA Executive Summary — CANDIDATE created 2026-06-11.**
12 sections. Primary source: APPSolve MTN DBA RFP (RFX-1000004246, submitted April 2026, 1,495 lines). HIST-002 (MTN 2014, 95 lines) fully superseded by MTN-2026 — zero lines extracted from HIST-002. DFA (Dark Fibre Africa) excluded from all client-facing tables per BU Lead decision FR-D. Section 7.4 (regulatory alignment) is the only AI-authored section — flagged for BU Lead review. BU Lead decisions applied: FR-D (DFA exclusion), FR-F (capacity metric replaced with generic wording), FR-G (database count softened to "hundreds of databases"). Review items: Section 7.4, A-005 (24x7 universality), A-006 (CIM universality), A-007 (CSM at no cost universality).

**Three remaining Oracle Wave 2 deliverables — not yet started.**
W2S1-002 Oracle EBS Capability, W2S1-004 Oracle Managed Services Support Model (16 content blocks pre-assigned from W2S1-003 reuse map), W2S1-005 Oracle Implementation Methodology.

### Current Repository State

| Dimension | Count |
|---|---|
| Approved files | **25** |
| Oracle CANDIDATE files (not yet reviewed) | **2** (W2S1-001, W2S1-003) |
| Review_Required files | **0** |
| STRUCTURE ONLY candidates (blocked) | **2** (W1S2-006, W1S2-007) |
| Legacy DRAFT files in Candidate folder | **6** (W1S2-001 through W1S2-005, W1S2-009 — pre-approval copies; approved versions in Approved/Acumatica/) |
| Archived (superseded) | **18** |
| EXTRACTION_LOG.csv data rows | **30** |
| DOCUMENT_REGISTER.csv data rows | **42** |

---

## Section 2: Repository Statistics

### File Counts by Folder

| Folder | File type | Count | Notes |
|---|---|---|---|
| `07_Approved_Content/Approved/Cross_BU/` | Approved content | 9 | W1S1-001 through W1S1-009 |
| `07_Approved_Content/Approved/BeBanking/` | Approved content | 10 | W1S3-001 through W1S3-010 |
| `07_Approved_Content/Approved/Acumatica/` | Approved content | 6 | W1S2-001, 002, 003, 004, 005, 009 |
| `07_Approved_Content/Candidate_Content/Oracle/` | Oracle candidates | 2 | W2S1-001, W2S1-003 |
| `07_Approved_Content/Candidate_Content/Acumatica/` | STRUCTURE ONLY + legacy DRAFTs | 8 | W1S2-006, W1S2-007 (active); W1S2-001–005, W1S2-009 DRAFTs (legacy — superseded by Approved/ versions) |
| `07_Approved_Content/Candidate_Content/_Archived_Superseded/` | Archived | 18 | 6 W1S1 + 11 W1S3 + W1S2-008 |
| `00_Governance/` | Governance documents | 25+ | See Section 7 for key file list |

**Total approved: 25** (9 Cross-BU + 10 BeBanking + 6 Acumatica)

### Extraction Log

| Log field | Value |
|---|---|
| Total rows in EXTRACTION_LOG.csv | 30 data rows (1 header row) |
| Status: Approved | 25 |
| Status: Candidate | 2 (W2S1-001, W2S1-003) |
| Status: STRUCTURE ONLY | 2 (W1S2-006, W1S2-007) |
| Status: Archived | 1 (W1S2-008, in log as archived) |

### Document Register

| Register field | Value |
|---|---|
| Total rows in DOCUMENT_REGISTER.csv | 42 data rows (1 header row = 43 total lines) |
| HIST-012 (MTN 2026 DBA RFP) | Recorded in ORACLE_FACT_BASELINE.md Section 18; **not yet registered in DOCUMENT_REGISTER.csv** — pending admin action |
| HIST-013 (MTN 2014 DBA summary) | Recorded in ORACLE_FACT_BASELINE.md Section 18; **not yet registered in DOCUMENT_REGISTER.csv** — pending admin action |

---

## Section 3: Approved Content Inventory

All 25 files approved as of 2026-06-10. Location: `07_Approved_Content/Approved/`. All have `approved_for_reuse: Yes` set by Hein Blignaut.

### Cross-BU — 9 files (`Approved/Cross_BU/`)

| File | Content | Restriction |
|---|---|---|
| W1S1-001-CORP-CompanyOverview.md | Company introduction, 23-year history, 50+ senior consultants, sub-Saharan + international footprint, 18 industries | None |
| W1S1-002-CORP-CompanyHistory.md | Founder background, geographic expansion, Oracle partnership history, award timeline | None |
| W1S1-003-ORA-OraclePartnership.md | Oracle Level 1 Partner, 5 expertise areas, Oracle VAR, 6 awards 2015–2024 | Annual OPN revalidation required for Cloud Excellence + Linux Specialist |
| W1S1-004-ACU-AcumaticaPartnership.md | Acumatica Gold Partner credentials, VAR status, delivery experience, industry footprint | None |
| W1S1-005-BB-BeBankingOverview.md | BeBanking product description, 7 capabilities, ERP compatibility | SAP: use "BeBanking integrates with SAP environments" only; no module claims until BQ-WEB-04 answered |
| W1S1-006-CORP-AwardsRecognition.md | 6 Oracle awards 2015–2024 | Award table: unrestricted. Success stories (Tiger Brands, USAID, UT Grain): pending URL verification before citing |
| W1S1-007-CORP-DeliveryModel.md | 8 service lines, Oracle Level 1 Partner credentials, DBA team claim, Monthly Recurring Invoice Model | None |
| W1S1-008-CORP-GeographicPresence.md | Sub-Saharan Africa (5 markets), international (4 countries), industries by geography | None |
| W1S1-009-CORP-KeyDifferentiators.md | 7 differentiators, Continuous Improvement Model, Hybrid Support Model, 3 costing models | None |

### BeBanking — 10 files (`Approved/BeBanking/`)

| File | Content | Restriction |
|---|---|---|
| W1S3-001-BB-ProductOverview.md | BeBanking product overview, 9-module portfolio, ERP compatibility, geographic deployment | None |
| W1S3-002-BB-HostToHostBanking.md | H2H banking process (6 steps), supplier and payroll H2H, security model, 9-bank list | None |
| W1S3-003-BB-SupplierPayments.md | Supplier Bank Account Approval, AVS, Supplier H2H Payments, Supplier PDF Remittances | None |
| W1S3-004-BB-PayrollPayments.md | Payroll H2H workflow, ACB file processing, data segregation — Oracle EBS and Oracle Fusion only | Acumatica payroll permanently excluded (BQ5/L-C-001) |
| W1S3-005-BB-InternationalAndForexPayments.md | Module 9: AP-initiated cross-border payments; bank-intermediated SWIFT; CMA + UK + Chile | None |
| W1S3-006-BB-ERPIntegration.md | ERP integration detail — Oracle EBS, Oracle Fusion, Acumatica, SAP; module-level integration tables | SAP: environments only; BQ-WEB-04 pending |
| W1S3-007-BB-Security.md | Security design principles, access control, transmission security, POPIA compliance, GDPR roadmap | GDPR is roadmap — do not cite as current compliance |
| W1S3-008-BB-Architecture.md | API-first architecture, component architecture, deployment requirements, security architecture | H2H process flow diagram not extractable from DOCX XML — pending |
| W1S3-009-BB-HostingModel.md | Hosting model (on-premises + cloud), support model, subscription-only commercial model | None |
| W1S3-010-BB-MonitoringAutomation.md | 5 automated processes, bank statement management, exchange rate automation, monitoring and audit | None |

### Acumatica — 6 files (`Approved/Acumatica/`)

| File | Content | Restriction |
|---|---|---|
| W1S2-001-ACU-Financials.md | GL, AR, AP, Cash Management, Multi-Currency, Tax, Deferred Revenue (IFRS 15 primary), Mobile Approvals, Recurring Transactions, Fixed Assets | None |
| W1S2-002-ACU-Distribution.md | Order Management, Procurement, Sales and Customer Management, Financial Management Integration | None |
| W1S2-003-ACU-Inventory.md | FIFO/WAC/Standard costing (IFRS/IAS 2 compliant, no LIFO), Lot and Serial Tracking, Multi-Location, Replenishment | None |
| W1S2-004-ACU-Manufacturing.md | Manufacturing Platform, Discrete Manufacturing, MRP, Estimating, Engineering Change Control | Sole KB Manufacturing source |
| W1S2-005-ACU-CRM.md | Contact and Account Management, Sales Pipeline, Quote Management, Case Management, Customer Portal, Outlook Integration | None |
| W1S2-009-ACU-ProjectAccounting.md | Project Budget/WIP/Revenue Recognition/Billing Rules/Change Orders/Manufacturing Integration | 8 verified rows; Intercompany Projects removed (not a Project Accounting feature) |

---

## Section 4: Oracle Wave 2 Deliverables Status

| ID | Deliverable | Status | Date | Key review items |
|---|---|---|---|---|
| W2S1-001 | Oracle Fusion Capability Statement | **CANDIDATE** | 2026-06-11 | FR-004 (SCM no reference client) — BU Lead decision. Cape Union Mart SCM error corrected. Nala Energy 4-country error corrected. Confirm A-001 through A-006 client status assumptions. |
| W2S1-002 | Oracle EBS Capability Statement | Not started | — | Primary source: TMPL-002. Confirm Oracle EBS Payroll (HRMS) scope before authoring. |
| W2S1-003 | Oracle DBA Executive Summary | **CANDIDATE** | 2026-06-11 | Section 7.4 (regulatory alignment — only AI-authored section). Confirm A-005 (24x7 universality), A-006 (CIM universality), A-007 (CSM at no cost universality). DFA excluded per FR-D. |
| W2S1-004 | Oracle Managed Services Support Model | Not started | — | 16 content blocks pre-assigned from W2S1-003 reuse map. Primary source: MTN 2026 DBA RFP + ATNS EBS 2025. |
| W2S1-005 | Oracle Implementation Methodology | Not started | — | Primary sources: Hollywood Bets V5.0 + RedPath Mining RFI + SAA RFP Section 5. |

### Oracle CANDIDATE Files — Physical Locations

| File | Physical path |
|---|---|
| W2S1-001 | `07_Approved_Content/Candidate_Content/Oracle/W2S1-001-ORA-FusionCapability.md` |
| W2S1-003 | `07_Approved_Content/Candidate_Content/Oracle/W2S1-003-ORA-DBAExecutiveSummary.md` |

### Pre-Work Readiness Assessment

| Deliverable | Gate document | Readiness report | Status |
|---|---|---|---|
| W2S1-001 | ORACLE_FACT_BASELINE.md | Implicit in ORACLE_WAVE2_EXECUTION_PLAN.md | CANDIDATE created |
| W2S1-003 | `00_Governance/W2S1-003_READINESS_REPORT.md` | Created 2026-06-11 — 21 domains, all FULL | CANDIDATE created |
| W2S1-002 | ORACLE_WAVE2_EXECUTION_PLAN.md (Deliverable 2) | Not yet created | Not started |
| W2S1-004 | W2S1-003 reuse map (16 blocks) | Embedded in W2S1-003 file | Not started |
| W2S1-005 | ORACLE_WAVE2_EXECUTION_PLAN.md (Deliverable 5) | Not yet created | Not started |

### W2S1-004 Pre-Assigned Content Blocks (from W2S1-003)

The following 16 content blocks from MTN 2026 DBA RFP are reserved exclusively for W2S1-004. They appear in W2S1-003 only as executive-level summaries. Do not expand them in W2S1-003.

| Block | MTN-2026 lines | Topic |
|---|---|---|
| B-001 | 435–445 | ITIL framework — Incident, Problem, Event, Change management |
| B-002 | 482–497 | CSI closed-loop model (4-stage CIM) |
| B-003 | 499–541 | Service Delivery Management — governance tables, SLA cadence |
| B-004 | 543–571 | Capacity and Demand Management |
| B-005 | 629–668 | CMDB governance |
| B-006 | 725–749 | Backup SOP table of contents |
| B-007 | 784–828 | Monthly report table of contents |
| B-008 | 993–1037 | Deployment framework |
| B-009 | 1040–1167 | Segregation of duties |
| B-010 | 352–480 | Migration factory approach and ETL |
| B-011 | Q14 | Capacity planning detail |
| B-012 | Q16 | Performance management detail |
| B-013 | Q19 | CMDB governance detail |
| B-014 | Q20 | 3-layer monitoring framework detail |
| B-015 | Q21 | Backup SOP detail |
| B-016 | Q22 | Monthly report detail |

---

## Section 5: Critical Governance Rules

The following rules are permanent and must be enforced in every AI session without exception. Violations have occurred in prior sessions — these rules exist to prevent recurrence.

### Partner Tier

1. **Oracle Level 1 Partner** — the only approved Oracle partner tier. Gold Membership expired August 2021 (evidenced by EXPIRED_APPSolve_OPN_202108.pdf). Never cite "Gold Partner", "Gold Level", or "Gold Membership" in any tender-facing document.
2. **Acumatica Gold Partner** — confirmed (not "Gold Certified").

### Company Facts (use these values, not template values)

| Fact | Correct value | Prohibited |
|---|---|---|
| Years in business | "over 23 years" or "established in 2002" | "22 years", "over 22 years" |
| Headcount | "more than 50 senior consultants" | "100+", "110+", "over 100", "over 110" |
| DBA team | "one of the largest locally based Oracle Applications DBA teams in South Africa" | "largest number of Oracle DBAs" |
| Hein Blignaut career | "approximately 30 years' IT experience" | "19 years' experience" |
| Geographies | Botswana, Zambia, Mozambique, Namibia, Tanzania (sub-Saharan); USA, France, Abu Dhabi, Pakistan (international) | Nigeria, Uganda, Bangladesh, Qatar, Ghana |

### Client Reference Rules

3. **DFA (Dark Fibre Africa)** — NOT available as a named reference in any tender-facing document. BU Lead decision FR-D (2026-06-11). DFA may remain as internal corroborating evidence only.
4. **Approved client references** — only clients with confirmed active engagement or a signed reference letter may be cited in tender-facing documents. Client status must be confirmed before promotion to Review_Required.

### Content Governance

5. **APPTime is the authoritative source for consultant CVs.** KB stores Consultant Index Records only. AI must never generate CV text from KB records (ADR-001).
6. **Candidate content may never be cited in tenders.** Files in `Candidate_Content/` have `approved_for_reuse: No`. Only files from `Approved/` or confirmed KB destination folders may be cited.
7. **Prohibited wording register** — the following must never appear in any extracted or authored file:
   - "Gold Partner" / "Gold Level" / "Gold Membership"
   - "110 Senior Consultants" / "100 senior resources" / "100+ consultants"
   - "19 years' experience" (Hein Blignaut)
   - "over 22 years" / "22 years" (company age)
   - "Nigeria, Uganda, Bangladesh, Qatar, Ghana" (unsupported geographies)
   - "largest number of Oracle DBAs" / "largest number of locally-based Oracle Applications DBAs"
8. **Acumatica payroll — permanently excluded in South Africa.** Acumatica does not provide payroll functionality in SA. BeBanking Payroll H2H is supported from Oracle EBS and Oracle Fusion Applications payroll sources only. This rule applies to all BeBanking files (L-C-001).
9. **AI-authored content must be verified or removed.** No AI-generated capability claim may remain in an approved file unless verified against authoritative documentation. "Plausible but unverified" is not acceptable. W1S2-009 Intercompany Projects row is the canonical example of correct application of this rule.
10. **BEE Level 3** (RS-19451, August 2025) — current certificate. Expires **2026-07-31**. Do not cite BEE compliance in tenders after this date without renewal. Any reference to "BEE Level 2" in older files is incorrect — use "BEE Level 3".

### Oracle-Specific Rules

11. **ORACLE_FACT_BASELINE.md** — mandatory pre-extraction consultation for any Oracle document. The 20-section baseline is the authoritative reference for Oracle facts, approved wording, prohibited wording, and governance rules.
12. **MTN 2026 DBA RFP lines 1187–1410** — excluded from all extraction. This company profile section contains 9 prohibited wording instances. Technical DBA content (lines 47–1186) is clean for extraction.
13. **Client-specific metrics** — operational metrics, SLA achievement percentages, incident reduction percentages, performance improvement percentages, database counts, staffing numbers and response-time commitments must be treated as client-specific evidence and must not be used as generic APPSolve claims unless independently validated.
14. **"only African partner certified on OIC"** — this claim has not been independently validated. Do not use in any 2026 tender until BU Lead confirms current status.

---

## Section 6: Outstanding BU Lead Actions

These items require human review before the associated files can be promoted from Candidate to Review_Required or approved for tender use.

### W2S1-001 Oracle Fusion Capability Statement (CANDIDATE)

| Item | Description | Required action |
|---|---|---|
| FR-004 | SCM section (Manufacturing, Supply Chain) has no approved reference client after Cape Union Mart was removed | BU Lead decision: (a) keep SCM section with generic wording; (b) identify an approved SCM reference client; or (c) remove SCM section |
| A-001 | Tool competency reference clients (SAA, Ster-Kinekor, Makro, Cape Union Mart, Nala Energy, Mr Price) — are these clients willing to be cited? | BU Lead confirm all still current and willing |
| A-002 | Ster-Kinekor bankruptcy — BU Lead to confirm whether Ster-Kinekor references are still appropriate | BU Lead decision |
| A-003 | ARM, SA Reserve Bank, KPMG Africa listed as currently active clients | BU Lead confirm still active |
| A-004 | CIM (Continuous Improvement Model) described as standard across all engagements | BU Lead confirm scope (DBA-only or all Oracle) |
| A-005 | Cloud Excellence Implementer designation | BU Lead confirm current OPN status before any 2026 tender uses this claim |
| A-006 | Nala Energy deployment — corrected from 4 countries to confirmed single market | BU Lead confirm actual deployment scope |

### W2S1-003 Oracle DBA Executive Summary (CANDIDATE)

| Item | Description | Required action |
|---|---|---|
| Section 7.4 | Regulatory alignment (POPIA, PCI-DSS, GDPR context) — only AI-authored section in the document | BU Lead review and either confirm as accurate, edit, or remove |
| A-005 | 24x7 support described as universally available | BU Lead confirm whether 24x7 is standard for all DBA managed services or only specific engagement types |
| A-006 | CIM (Continuous Improvement Model) described as standard across all DBA engagements | BU Lead confirm scope |
| A-007 | Customer Success Manager described as included at no additional cost | BU Lead confirm whether CSM is standard across all managed services engagements |
| A-008 | ARM, SA Reserve Bank, KPMG Africa listed as currently active DBA managed services clients | BU Lead confirm still active |

### Acumatica STRUCTURE ONLY (blocked — not Wave 2)

| File | Blocker |
|---|---|
| W1S2-006 Field Services | No source content found. BU Lead must decide: search corpus further, source from Acumatica partner portal, or confirm scope not offered. |
| W1S2-007 Payroll | Acumatica Payroll is US-focused; SA compliance approach unconfirmed. BU Lead must confirm APPSolve SA payroll integration approach. |

---

## Section 7: Pending Admin Actions

These items do not block current work but must be completed before Wave 2 is closed out.

| # | Action | Priority | Notes |
|---|---|---|---|
| A1 | **BEE certificate renewal** | **CRITICAL** | Expires 2026-07-31 — approximately 50 days from checkpoint date. Initiate immediately. Cannot cite BEE compliance in any tender after expiry. |
| A2 | Register HIST-006 through HIST-013 in DOCUMENT_REGISTER.csv | High | HIST-012 (MTN 2026 DBA RFP) and HIST-013 (MTN 2014) referenced in ORACLE_FACT_BASELINE.md Section 18 but not in DOCUMENT_REGISTER.csv. Also register SAA HCM, Hollywood Bets, RedPath Mining, ATNS EBS 2025. |
| A3 | Copy 25 Wave 1 approved files to KB destination folders | Medium | `06_Capabilities/`, `08_Methodologies/`, `09_Executive_Summaries/` per EXTRACTION_LOG.csv destination paths. 30–45 min task. |
| A4 | Update AI_CONTEXT.md: BEE Level 2 → Level 3; fix folder references | Medium | Current AI_CONTEXT.md still references "BEE Level 2" in some sections. |
| A5 | Update CHECKPOINT_WAVE1_2026-06-10.md: BEE Level 2 → Level 3 | Low | Historical accuracy; minor fix. |
| A6 | Register MTN July 2025 and Stellenbosch University 2025 reference letters | Medium | Found in RedPath Mining folder during Wave 2 planning. Register in `04_References/Oracle/` and DOCUMENT_REGISTER.csv. |
| A7 | Chase Oracle reference letters | High | Zero signed Oracle reference letters in `04_References/Oracle/`. Chase ATC, Old Mutual, Truworths. Reference letters are a HIGH coverage gap for evaluated Oracle RFPs. |
| A8 | Legacy DRAFT files in Acumatica Candidate folder | Low | W1S2-001 through W1S2-005, W1S2-009 DRAFTs still in `Candidate_Content/Acumatica/`. Approved versions are in `Approved/Acumatica/`. Decide: archive or delete legacy copies. |
| A9 | Verify "only African partner certified on OIC" claim | High | Not independently validated. Do not use in any 2026 tender until BU Lead confirms. |

---

## Section 8: Recommended Next Actions

Ordered by priority. First three actions are the critical path.

### Immediate — Required before Wave 2 can close

1. **BEE certificate renewal** (A1 above) — hard deadline 2026-07-31; ~50 days; external action; must be initiated immediately regardless of repository state.

2. **BU Lead review of W2S1-003** (Oracle DBA Executive Summary) — review Section 7.4 regulatory alignment and confirm A-005, A-006, A-007. W2S1-003 is the most recently completed deliverable and builds the foundation for W2S1-004.

3. **BU Lead review of W2S1-001** (Oracle Fusion Capability Statement) — decide FR-004 (SCM section); confirm A-001 client status, A-002 Ster-Kinekor, A-005 Cloud Excellence Implementer OPN status.

### Next Oracle extraction — ready to start

4. **W2S1-004 Oracle Managed Services Support Model** — 16 content blocks pre-assigned from W2S1-003 reuse map. Primary source: MTN 2026 DBA RFP (ITIL detail, SLA cadence, CSI model, capacity management, segregation of duties, CMDB governance) + ATNS EBS 2025. Requires reading the following MTN-2026 line ranges: 435–445, 482–571, 543–571, 629–668, 725–749, 784–828, 993–1037, 1040–1167. W2S1-004 can be started without waiting for W2S1-003 BU Lead review.

5. **W2S1-002 Oracle EBS Capability Statement** — primary source: TMPL-002. Confirm Oracle EBS Payroll (HRMS implementation) scope with Hein before authoring the HRMS section. Medium effort (~1 hour). Can run in parallel with W2S1-004.

6. **W2S1-005 Oracle Implementation Methodology** — primary sources: Hollywood Bets V5.0 + RedPath Mining RFI + SAA RFP Section 5. Lowest approval risk of the five Oracle Wave 2 deliverables.

### Admin (complete before Wave 2 closeout)

7. Register HIST-006 through HIST-013 in DOCUMENT_REGISTER.csv (A2).
8. Copy 25 approved files to KB destinations (A3).
9. Chase Oracle reference letters — ATC, Old Mutual, Truworths (A7).

---

## Appendix A: Key Governance File Register

| File | Location | Purpose | Status |
|---|---|---|---|
| ORACLE_FACT_BASELINE.md | `00_Governance/` | Authoritative Oracle facts, approved/prohibited wording, 20 sections. Read before every Oracle extraction. | Current — updated 2026-06-11 (HIST-012, HIST-013 added) |
| ORACLE_WAVE2_EXECUTION_PLAN.md | `00_Governance/` | Five-deliverable Oracle Wave 2 plan — sources, effort, sequencing | Current — updated 2026-06-11 |
| ORACLE_TENDER_READINESS_ASSESSMENT.md | `00_Governance/` | Oracle RFP coverage by section — Covered / Partially / Missing | Current — updated 2026-06-11 |
| W2S1-003_READINESS_REPORT.md | `00_Governance/` | Pre-extraction readiness gate for W2S1-003 — DBA content coverage, source map, risk register | Created 2026-06-11 |
| CHECKPOINT_WAVE1_2026-06-10.md | `00_Governance/` | Wave 1 complete state — predecessor to this document | Current |
| CURRENT_STATE.md | `00_Governance/` | Executive dashboard — pipeline snapshot, next actions, reading order | Current |
| EXTRACTION_LOG.csv | `00_Governance/` | Pipeline tracking for all extractions (30 data rows) | Current |
| DOCUMENT_REGISTER.csv | `00_Governance/` | Master register of all KB documents (42 data rows) | Current — HIST-012, HIST-013 not yet registered |
| APPROVED_CONTENT_USAGE_GUIDE.md | `00_Governance/` | Rulebook — content class usage, AI guardrails, tender workflows | Current |
| AI_CONTEXT.md | Root | AI session context — validated facts, permanent rules, approved content list | Current — BEE Level 2 reference requires correction (see A4) |
| HANDOVER.md | Root | Current status, Wave 2 progress, lessons learned | Current — updated 2026-06-11 |
| PROJECT.md | Root | Strategy, architecture decisions, milestone history | Current — updated 2026-06-11 |

---

## Appendix B: Discrepancies Found During Checkpoint Creation

| ID | Discrepancy | Severity | Resolution |
|---|---|---|---|
| DISC-001 | HIST-012 (MTN 2026 DBA RFP) and HIST-013 (HIST-002 MTN 2014) referenced in ORACLE_FACT_BASELINE.md Section 18 but not formally registered in DOCUMENT_REGISTER.csv. CURRENT_STATE.md states 42 registered assets — this count is consistent with DOCUMENT_REGISTER.csv but does not include the two new sources. | Medium | Register HIST-012 and HIST-013 in DOCUMENT_REGISTER.csv (Admin action A2). Count will increase to 44 after registration. |
| DISC-002 | CURRENT_STATE.md Pipeline Snapshot shows "Candidate (active — not yet reviewed): 2 — W1S2-006 Field Services, W1S2-007 Payroll" but does not reflect the 2 new Oracle CANDIDATEs (W2S1-001, W2S1-003). The Oracle candidates are referenced in the Current Focus section but not in the formal pipeline table. | Medium | CURRENT_STATE.md pipeline table to be updated — see Section 8 of this checkpoint. Corrected in this checkpoint session. |
| DISC-003 | AI_CONTEXT.md still references "BEE Level 2" in some sections. BEE Level 3 certificate (RS-19451) has been current since August 2025. | Medium | Correct AI_CONTEXT.md (Admin action A4). Also correct CHECKPOINT_WAVE1_2026-06-10.md Validated Facts table (Admin action A5). |
| DISC-004 | Legacy DRAFT files (W1S2-001 through W1S2-005, W1S2-009) still present in `Candidate_Content/Acumatica/`. Approved versions exist in `Approved/Acumatica/`. This creates a risk that an AI session could read outdated Candidate versions. | Low | Archive or delete legacy DRAFTs (Admin action A8). Until then, always read from `Approved/Acumatica/` — not from `Candidate_Content/`. |
| DISC-005 | EXTRACTION_LOG.csv row count requires verification. Prior checkpoint (CHECKPOINT_WAVE1_2026-06-10.md) stated 29 rows. W2S1-001 and W2S1-003 were appended — expected count is 31. Count confirmed as 30 via tool call, suggesting the pre-Wave-2 baseline was 28 data rows (not 29). The off-by-one may relate to whether the header row was included in the prior count. | Low | Verify EXTRACTION_LOG.csv row count at next session start. Treat 30 data rows as the confirmed post-W2S1-003 count. |

---

*Checkpoint created 2026-06-11 by Claude (AI). No extraction work performed. No Oracle deliverables authored. Repository state captured from confirmed file reads and conversation context.*

*Next checkpoint recommended: after W2S1-002, W2S1-004, and W2S1-005 are created, or after BU Lead review of W2S1-001 and W2S1-003 — whichever comes first.*
