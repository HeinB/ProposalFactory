# APPSolve Tender Knowledge Base

**Purpose:** AI-assisted tender response system for APPSolve's three business units — Oracle, Acumatica, and BeBanking.

**Current phase:** Oracle Wave 3 HCM — W3S1-001 and W3S1-002 in Review_Required; ready for W3S1-003 Oracle Recruiting Cloud. Wave 1 COMPLETE (32 approved). Wave 2 COMPLETE (5 Oracle approved). Total approved: **32**. Review_Required: **2** (W3S1-001, W3S1-002).

**Last updated:** 2026-06-12 — W3S1-002 Oracle Talent Management Suite promoted to Review_Required; ORACLE_FACT_BASELINE Rules 21.4 (DFA) and 21.5 (Redpath Mining) added
**Wave 2 checkpoint:** `00_Governance/CHECKPOINT_ORACLE_WAVE2_2026-06-11.md`
**Wave 3 source discovery:** `00_Governance/WAVE3_HCM_SOURCE_DISCOVERY_REPORT.md`

---

## Business Units

| BU | Core services | Partner status |
|---|---|---|
| Oracle | OCI, Oracle EBS (R11/R12), Oracle Fusion (ERP, HCM, SCM, CRM, GRC), DBA, Managed Services | Oracle Level 1 Partner; Oracle VAR |
| Acumatica | ERP implementation, support, licensing | Acumatica Gold Partner; Acumatica VAR |
| BeBanking | Proprietary H2H banking integration product | — |

---

## Strategy: Extraction-First

The original plan assumed the Tender Pack was the primary IP source and that capability statements would be authored from scratch. This was replaced after discovery of the historical tender corpus.

**Current strategy:** Extract and modernise from `Parties/Customers/[Client]/RFP/`. APPSolve has 14 years of proposal history — 315 clients, approximately 18,400 files (2012–2026). The real IP is in this corpus. Content is curated, fact-checked, and approved through a three-stage pipeline before it can be cited in a tender response.

Content authoring from scratch is appropriate only where no source document exists.

---

## Repository Architecture

Two source repositories — both strictly read-only:

| Repository | Location | Purpose |
|---|---|---|
| Tender Pack | `APPSolve Company Docs/Tender Pack/` | Evidence, compliance documents, reference letters, certifications |
| Historical Tender Corpus | `APPSolve Company Docs/Parties/Customers/[Client]/RFP/` | Primary IP source — 315 clients, ~18,400 files, 2012–2026 |

Active proposal templates at `Parties/Customers/0. Proposal Templates/`:
- **Oracle Fusion Template** (Sept 2024) — primary Oracle Cloud template
- **Oracle EBS Template** — date unknown; parallel structure to Fusion template
- **Acumatica Proposal Template Sept 2025** — long-form; note Section 1 has HearX Group client content — do not reuse
- **Acumatica Short Proposal** (Apr 2025)

The TMPL document type was introduced 2026-06-08 to represent active reusable proposal templates in the register.

---

## Extraction Pipeline

All content must pass through three stages before it can be cited in a tender:

```
Source document (read-only)
        │
        ▼
Candidate_Content/          ← DRAFT file, metadata block, not approved
        │
        ▼
Review_Required/            ← Source verified, self-reviewed
        │
        ▼
Approved/                   ← BU lead signed off, approved_for_reuse: Yes
        │
        ▼
KB destination folder       ← Registered, available for tender use
```

Rules:
- `approved_for_reuse: Yes` may only be set by the BU lead reviewer — never by the extractor
- DRAFT suffix is removed only when a file reaches Approved/
- AI systems must not use content from Candidate_Content/ or Review_Required/ when drafting tender responses

---

## Architecture Decisions

| Decision ID | Title | Date | Status |
|---|---|---|---|
| D-ARCH-001 | APPTime as system of record for consultant profiles | 2026-06-10 | Accepted |

### D-ARCH-001 — APPTime as CV System of Record

**Decision:** APPTime is the authoritative source for consultant CV content. The Knowledge Base stores Consultant Index Records only — lightweight metadata records for AI skill-matching. Full CVs are generated from APPTime on demand and are not maintained in the KB.

**Rationale:** CV documents extracted from the Tender Pack `Rate Card/` folder would create a third source of truth (APPTime → Tender Pack → KB), with no reliable synchronisation mechanism. Drift risk is material and demonstrated by existing duplicate CV versions in the Tender Pack. The AI's requirement from CV data is skill-matching (who has the right skills?), not content generation — skill tags achieve this with minimal maintenance burden.

**Consequences:** CV_template.md redesigned as Consultant Index Record template; MIGRATION_ANALYSIS.md Priority 25 (CV migration) cancelled; `03_People/Resource_Profiles/` promoted as active folder; permanent rules encoded in AI_CONTEXT.md.

**Full record:** `00_Governance/ADR-001-CV_SOURCE_OF_TRUTH.md`

---

## Milestone History

| Milestone | Date | Notes |
|---|---|---|
| Wave 1 extraction complete | 2026-06-08 | 28 candidates created across 3 sessions |
| Session A complete | 2026-06-09 | 9 Cross-BU files approved; 6 archived DRAFTs |
| Session C BU baseline confirmed | 2026-06-10 | All 13 BU lead questions answered; SESSION_C_FACT_BASELINE.md created |
| Session C Batch 1 remediated | 2026-06-10 | W1S3-003, 004, 007 promoted to Review_Required |
| Acumatica payroll clarification | 2026-06-10 | Permanent rule established — Acumatica payroll not available in SA |
| **Milestone checkpoint** | **2026-06-10** | **See `00_Governance/MILESTONE_2026-06-10_SESSION_C_PROGRESS.md`** |
| **D-ARCH-001 — CV architecture** | **2026-06-10** | **APPTime designated as CV system of record; full CV migration cancelled; Consultant Index Records model adopted** |
| **Session C approved** | **2026-06-10** | **9 BeBanking H2H files approved; 6 approval decisions applied (D1–D6); total approved content: 18 files** |
| **CURRENT_STATE.md created** | **2026-06-10** | **Executive dashboard for session restarts — see `00_Governance/CURRENT_STATE.md`** |
| **Session B Part 1 remediation** | **2026-06-10** | **6 Acumatica module files remediated; promoted to Review_Required. Key corrections: IFRS 15 (W1S2-001), LIFO removed (W1S2-003), Manufacturing cascade table errors fixed (W1S2-004), AI rows flagged (W1S2-009)** |
| **W1S2-009 AI row verification** | **2026-06-10** | **Change Order Management confirmed; Manufacturing Integration confirmed with prerequisites; Intercompany Projects removed (not a Project Accounting feature). W1S2-009 now has 8 verified rows.** |
| **Session B approved** | **2026-06-10** | **6 Acumatica module files approved by Hein Blignaut; promoted to `Approved/Acumatica/`. Total approved content: 24 files.** |
| **W1S3-005 approved / Wave 1 complete** | **2026-06-10** | **BeBanking International and Forex Payments approved. Review_Required queue empty. Wave 1 total: 25 approved files. Authoritative checkpoint: CHECKPOINT_WAVE1_2026-06-10.md** |
| **W2S1-001 REVIEW_REQUIRED** | **2026-06-11** | **Oracle Fusion Capability Statement promoted to Review_Required by Hein Blignaut. BU Lead decisions: Nala Renewables confirmed Financials+Projects — 8-country footprint — 4 countries implemented by APPSolve — referenceable. A-003 Hollywood Bets go-live closed. FR-004 SCM restricted-use ruling applied (Option A).** |
| **W2S1-001 APPROVED** | **2026-06-11** | **Oracle Fusion Capability Statement approved by Hein Blignaut. Validation pass returned zero findings. Nala Renewables confirmed as referenceable Financials and Projects client. APPSolve supports 8-country Oracle Fusion footprint and implemented 4 countries (SA, Lithuania, Romania, Finland). Promoted to Approved/Oracle/. Total approved: 28. Oracle approved: 3.** |
| **W2S1-002 CANDIDATE** | **2026-06-11** | **Oracle EBS Capability Statement CANDIDATE created. 13 sections. 7 sources (TMPL-002, ATNS 2025, KPMG SADC 6-country, ARM OCI success story, Assore SOW EBS-on-OCI, ARM 2018 proposal, EBS Customer List). 25+ EBS clients. KPMG SADC rollout (Botswana Mauritius Mozambique Zambia Zimbabwe Namibia). All prohibited wording corrected. 4 BU Lead decisions required.** |
| **W2S1-003 CANDIDATE created** | **2026-06-11** | **Oracle DBA Executive Summary — 12 sections. MTN 2026 DBA RFP (April 2026) primary source; HIST-002 superseded. DFA excluded per BU Lead FR-D. Section 7.4 AI-authored — BU review required.** |
| **Oracle Wave 2 checkpoint** | **2026-06-11** | **CHECKPOINT_ORACLE_WAVE2_2026-06-11.md — complete repository state after Wave 1 + W2S1-001 + W2S1-003. 5 discrepancies documented. Recommended next: BU Lead review W2S1-003, then W2S1-004.** |
| **W2S1-003 APPROVED** | **2026-06-11** | **Oracle DBA Executive Summary approved by Hein Blignaut. Section 7.4 rewritten (POPIA framing). A-005 24x7 qualified. A-006 CIM confirmed. A-007 CSM "at no cost" removed. Promoted to Approved/Oracle/. Total approved: 26.** |
| **W2S1-004 APPROVED** | **2026-06-11** | **Oracle Managed Services Support Model approved by Hein Blignaut. 15 sections. 16 MTN-2026 content blocks. All 9 factual risks resolved. All 7 assumptions (A-W4-001 through A-W4-007) scoped and resolved. Promoted to Approved/Oracle/. Total approved: 27.** |
| **W2S1-002 APPROVED** | **2026-06-12** | **Oracle EBS Capability Statement approved by Hein Blignaut. 5 referenceable clients (ARM, Assore, Adcock Ingram, Harmony, Investec). Manufacturing excluded (BU-EBS-003). SARB restricted — separate BU approval required. BEE Level 3 confirmed. Promoted to Approved/Oracle/. Total approved: 29. Oracle approved: 4.** |
| **W2S1-005 APPROVED — Oracle Wave 2 COMPLETE** | **2026-06-12** | **Oracle Implementation Methodology approved by Hein Blignaut. 16 sections + Section 17 Approval Record. Sources: Hollywood Bets V5.0 (April 2023) + RedPath Mining RFI (March 2026). OUM basis confirmed. BU Lead decisions D-W5-001 and D-W5-002 CLOSED. Promoted to Approved/Oracle/. Total approved: 30. Oracle approved: 5. Oracle Wave 2 COMPLETE.** |
| **W1S2-006 Field Services APPROVED** | **2026-06-12** | **Acumatica Field Services Capability Statement APPROVED by Hein Blignaut. approved_for_reuse: Yes. 11 sections. Primary source: Interconnect Systems Proposal V2.0 §3.9 (paras 714–767). Interconnect Systems confirmed referenceable for Acumatica Field Services (BU decision 2026-06-12). All 6 risks mitigated. 4 standing pre-tender checks (PT-W6-001–004). Location: Approved/Acumatica/W1S2-006-ACU-FieldServices.md. KB copy: 06_Capabilities/Acumatica/Field_Services/. Total approved: 31. Acumatica approved: 8.** |
| **W1S2-007 Payroll Integration APPROVED** | **2026-06-12** | **Acumatica PaySpace Payroll Integration APPROVED by Hein Blignaut. approved_for_reuse: Yes. 8 sections + Section 17 Approval Record. Source: BU Lead decisions D-W7-001–D-W7-004 (no corpus source). APPSolve integration capability only — not native SA payroll. PaySpace is payroll system of record (owns PAYE/UIF/SDL/IRP5/EMP501). Acumatica is financial system of record. Integration method client-specific. No reference clients approved. 5 risks; 4 standing pre-tender checks (PT-W7-001–004). Location: Approved/Acumatica/W1S2-007-ACU-PayrollIntegration.md. KB copy: 06_Capabilities/Acumatica/Payroll_Integration/. Total approved: 32. Acumatica approved: 9.** |

## Current Pipeline Status (updated 2026-06-12 — Oracle Wave 2 COMPLETE)

| Stage | Count | Detail |
|---|---|---|
| Approved | **31** | W1S1-001–009 (Session A); W1S3-001–005, 006–010 (Session C); W1S2-001, 002, 003, 004, 005, 009 (Session B); W2S1-001–005 (Oracle, all approved 2026-06-11/12); **W1S2-006 Acumatica Field Services (approved 2026-06-12; Interconnect Systems referenceable)** |
| Review_Required | **0** | — Oracle Wave 2 COMPLETE |
| Candidate (Oracle — BU review required) | **0** | — |
| Review_Required | 0 | — |
| Approved | **32** | W1S2-007 Payroll Integration added 2026-06-12; Review_Required queue now empty |

---

## Approved Content — Wave 1 Session A

Nine files approved 2026-06-09 by Hein Blignaut. Physical location: `07_Approved_Content/Approved/Cross_BU/`.

| File | Content |
|---|---|
| W1S1-001-CORP-CompanyOverview.md | Company introduction, history, 50+ consultants, geography, 18 industries |
| W1S1-002-CORP-CompanyHistory.md | Founder background, geographic expansion, Oracle partnership history, awards |
| W1S1-003-ORA-OraclePartnership.md | Oracle Level 1 Partner, 5 expertise areas, VAR, 6 awards — annual OPN revalidation required |
| W1S1-004-ACU-AcumaticaPartnership.md | Acumatica Gold Partner credentials, VAR status, delivery experience |
| W1S1-005-BB-BeBankingOverview.md | BeBanking product overview, 7 capabilities, ERP compatibility |
| W1S1-006-CORP-AwardsRecognition.md | Award table (6 Oracle awards) unrestricted; success stories pending URL verification |
| W1S1-007-CORP-DeliveryModel.md | 8 service lines, Oracle Level 1 Partner credentials, DBA team, MRI Model |
| W1S1-008-CORP-GeographicPresence.md | Sub-Saharan (5 markets) and international (4 countries) footprint |
| W1S1-009-CORP-KeyDifferentiators.md | 7 differentiators, Hybrid Support Model, Continuous Improvement Model, costing models |

---

## Validated Facts (confirmed 2026-06-09)

Facts confirmed through external confirmation by Hein Blignaut and corpus research across 18,400 files. Do not override without a new confirmed source.

| Fact | Confirmed value |
|---|---|
| Founded | 2002 — "over 23 years" or "established in 2002" |
| Headcount | 50+ Senior Consultants |
| Oracle tier | Level 1 Partner (Gold Membership expired August 2021) |
| Oracle expertise | Fusion Cloud Financials; Fusion Cloud HCM Core; Oracle Integration; EBS Migration to OCI; OCI Migration |
| Acumatica tier | Gold Partner |
| Oracle awards | Business Impact Award EMEA 2024; Business Impact Award ECEMEA 2024 |
| Geography — sub-Saharan | Botswana, Zambia, Mozambique, Namibia, Tanzania |
| Geography — international | USA, France, Abu Dhabi, Pakistan |
| Removed geographies | Nigeria, Uganda, Bangladesh, Qatar, Ghana — no corpus evidence |
| BeBanking ERP integration | Oracle EBS (R11/R12), Oracle Fusion Applications, Acumatica, SAP (environments — pending BQ-WEB-04 for module detail) |
| BeBanking SAP rule | "BeBanking integrates with SAP environments" — no module claims until BQ-WEB-04 answered |
| BeBanking Acumatica payroll | Acumatica does not provide payroll functionality in South Africa. Payroll H2H from Oracle EBS and Oracle Fusion only. Do not infer payroll from Acumatica ERP integration. |
| Hein Blignaut IT career | Started 1996 at MTN — approximately 30 years' experience as of 2026 |

Full validation record: `00_Governance/FACT_RESOLUTION_REPORT.md`

---

## Wave 1 Summary

28 extraction candidates created 2026-06-08 across three sets:

| Set | Files | Status |
|---|---|---|
| Company Profile Master (W1S1) | 9 Cross-BU files | 9 Approved (Session A 2026-06-09) |
| Acumatica Module Library (W1S2) | 9 Acumatica files | 6 Approved (Session B 2026-06-10); 3 STRUCTURE ONLY (W1S2-006, 007, 008 — BU lead decisions needed) |
| BeBanking H2H Capability (W1S3) | 10 BeBanking files | 10 Approved (Session C 2026-06-10 — all including W1S3-005) |

Key discovery: BeBanking H2H content in HyDac V5.1 is intro-only. All detailed BeBanking product content sourced from SITA BeBanking Proposal v1.06 (2017, Oracle EBS-specific). All BeBanking candidates require BU lead currency confirmation.

---

## Next Steps

1. **Approve W1S3-005** — BeBanking International and Forex Payments in `Review_Required/BeBanking/`; BU lead approval pending
2. **BEE certificate renewal** — expires 2026-07-31; ~51 days; initiate now
3. **Copy 24 approved files to KB destinations** — `06_Capabilities/`, `08_Methodologies/`, `09_Executive_Summaries/` per EXTRACTION_LOG.csv
4. **Wave 2 extraction** — Oracle DBA Executive Summary (HIST-002), Oracle Fusion Capability Statement (TMPL-001), Oracle EBS Capability (TMPL-002), BeBanking Implementation Methodology (HIST-004)
5. **BU lead decisions** — W1S2-006 Field Services, W1S2-007 Payroll, W1S2-008 Construction (STRUCTURE ONLY gate)

---

## Objectives

- Maintain a single source of truth for tender responses
- Store approved company information with verified facts
- Store references, certifications, methodologies, and CVs
- Assist AI tools in generating accurate tender responses

## Knowledge Priorities

1. Approved Content
2. Capabilities
3. References
4. Methodologies
5. Historical Tenders
6. Compliance Documentation
