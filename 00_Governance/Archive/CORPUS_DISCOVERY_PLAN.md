# Historical Tender Corpus — Discovery and Ingestion Design
**Date:** 2026-06-08
**Status:** Design only — no files moved, renamed, or modified
**Scope:** `APPSolve Company Docs/Parties/Customers/*/RFP/` repository

---

## Corpus Profile (as observed 2026-06-08)

Before any classification work begins, it is worth understanding what we are working with.

| Metric | Count |
|---|---|
| Customer directories | 608 |
| Customers with RFP subfolder | 315 |
| Total files in all RFP folders | ~18,400 |
| Total files across all customer folders | ~30,300 |
| Approximate date range | 2012 – 2026 |

**File type breakdown (RFP folders only):**

| Type | Count | Significance |
|---|---|---|
| PDF | ~10,400 | Final submitted documents, compliance packs, original RFPs, scanned forms |
| DOCX | ~3,950 | Working and submitted proposals, capability statements, SOWs |
| XLSX | ~1,810 | Pricing workbooks, costing models, rate cards, resource trackers |
| DOC | ~600 | Older proposals (pre-2015) |
| MPP | ~340 | Microsoft Project files — project plans submitted with tenders |
| PPTX | ~240 | Presentation decks |
| MSG | ~205 | Email correspondence — clarifications, awards, RFP issuance |
| ZIP | ~185 | Bundled submissions |

**Largest single customer repositories:**

| Customer | File Count | Notes |
|---|---|---|
| SARB | 4,640 | Primarily TES (Temporary Employment Services) panel — CVs, not ERP tenders |
| SASSA | 1,079 | Oracle EBS support tenders — rich formal tender content |
| Tiger Brands | 876 | Mixed: BeBanking, Oracle EBS, Acumatica, individual resource supply |
| MTN | 798 | Oracle support renewals, resource supply, DBA extensions |
| KPMG | 510 | Multiple engagements |
| ARM | 471 | Oracle EBS support, managed services |
| UJ | 467 | Oracle EBS and Fusion tenders, BI, Cloud migration |
| NHLS | 462 | Oracle DBA support, upgrade proposals |
| SAT (South African Tourism) | 429 | Oracle ERP tender — significant proposal content |
| Parliament | 345 | Oracle iExpense, APEX, BeBanking FX |
| Harmony | 337 | Oracle EBS support |

**Known internal subfolder convention** (observed across multiple customers):

```
[Customer]/RFP/[Engagement Name]/
    0.Submitted/     ← final documents submitted to client
    1.Working/       ← draft working documents
    2.Costing/       ← pricing workbooks
    3.Project Plan/  ← project plans
    4.Supporting Documentation/ or 5.Supporting Documents/
    5.Archived/ or Archived/
```

Not all customers follow this structure — older engagements may be flat.

---

## Part 1: Inventory and Classification Approach

### 1.1 Recommended Strategy

Given 18,400+ files across 315 customers, a full manual review of every file is impractical. The recommended approach is a **three-tier discovery**:

**Tier 1 — Structural inventory (automated, read-only)**
Build a filesystem manifest: for every file under `Parties/Customers/*/RFP/`, record the path, filename, extension, file size, and last-modified date. This can be done with a simple `find` command and exported to CSV. No files are opened or modified. This provides a complete inventory baseline.

**Tier 2 — Engagement-level profiling (semi-automated)**
Group files by engagement (the subfolder under `RFP/`). For each engagement, record the customer name, engagement folder name, file count, file types present, and the presence or absence of a `0.Submitted` folder. This gives a map of how many discrete tender engagements exist and which are structured vs. flat.

**Tier 3 — Document-level sampling (manual, prioritised)**
Open and read a representative sample of submitted documents (primarily DOCX and PDF in `0.Submitted` folders) from the highest-value engagements to understand what content is actually present. This is where human judgment is required — AI can assist but cannot replace a practitioner reading a proposal.

### 1.2 Priority Order for Tier 3 Sampling

Sample in this order:

1. **Customers with the most formal tender structure** (numbered subfolders, `0.Submitted` present) — these are the richest sources
2. **Government and parastatal clients** — these tenders have detailed capability requirements and structured responses
3. **Large enterprise clients with Oracle implementations** (not just support/resource supply)
4. **Customers with BeBanking engagements** — Parliament, Tiger Brands, Brilliant/Thirst/Uniq
5. **Customers with Acumatica implementations** — Tiger Brands, and any others found

### 1.3 Engagement Type Pre-classification

Before reading individual documents, it is possible to pre-classify many engagements by reading their folder names alone. Three broad categories are visible:

**Category A — Formal project tenders**: Folder names describe scope or RFP reference numbers (e.g., "FINANCE CONSOLIDATION ON A CENTRALIZED DIGITAL PLATFORM SOLUTION", "RFQ19292023 ORACLE ERP EBS CONSULTANT"). Rich proposal content expected.

**Category B — Ongoing support/managed services**: Folder names describe support periods (e.g., "ERP Support 2021", "DBA Extension 2024", "Hyperion 2027"). Shorter proposals, rate cards, SLAs.

**Category C — Resource supply (TES/staffing)**: Folder names describe individual roles (e.g., "BI Data Engineer", "Senior Project Manager", "CSD Business Analyst"). Content is primarily CVs and compliance docs — limited reusable tender content.

SARB's 4,640 files are almost entirely Category C. This significantly changes its value to the knowledge base — high for CV/resource templates, low for methodology or capability content.

---

## Part 2: Classification Framework

### 2.1 Primary Document Types

Each document in the register should be assigned exactly one primary type:

| Type Code | Document Type | Description | Typical File Names / Signals |
|---|---|---|---|
| `TENDER` | Tender Response | A formal response to a public or private tender (RFT/RFB/IFB). Typically includes all mandatory forms, capability proof, pricing, and supporting docs as a single submission package. | "APPSolve [Client] Tender Response", SBD/MBD forms present |
| `RFP_RESP` | RFP Response | A written response to an RFP (Request for Proposal). Less prescriptive than a formal tender; greater narrative/technical content. | "APPSolve [Client] RFP Response", "Proposal", "Solution Response" |
| `PROPOSAL` | Unsolicited or Proactive Proposal | A proposal submitted without a formal procurement process — typically at client request or account management activity. | "Proposal", "Technical Proposal", no RFP/tender number |
| `RFQ_RESP` | RFQ Response | A response to a Request for Quotation. Usually simpler than an RFP; focused on price and brief scope confirmation. | "Quote", "RFQ Response", pricing table with brief scope |
| `QUOTE` | Quote / Commercial Offer | A standalone commercial offer (rate card, pricing schedule, or statement of work for billing). Common in resource supply and support renewals. | "Rate Card", "Resource Quote", "Pricing Schedule" |
| `SOW` | Statement of Work | A formal scope document defining deliverables, timelines, and commercial terms for a specific engagement. | "Statement of Work", "SOW", "Scope of Work" |
| `CLAR` | Clarification Response | A formal written response to client clarification questions raised after initial submission. | "Clarification", "Addendum Response", "Q&A Response" |
| `PRICING` | Pricing Schedule / Costing Model | A standalone pricing workbook or schedule (Excel or PDF). Not a full proposal — pricing component only. | `.xlsx` workbooks, "Pricing", "Costing", "Annexure C Pricing" |
| `CONTRACT` | Contract / Agreement | A signed or draft legal agreement. Includes MSAs, NDAs, SLAs, service agreements. | "Master Service Agreement", "NDA", "SLA", "Contract" |
| `OTHER` | Other | Anything that does not fit the above categories. Includes: original client RFP documents, CVs, compliance documents, project plans, presentations, email correspondence. | Client's own RFP document, CV files, `.mpp` files, `.msg` files |

### 2.2 Sub-type Tags

Documents may also be tagged with one or more sub-types to support retrieval:

| Sub-type Tag | Meaning |
|---|---|
| `ORIGINAL_RFP` | The client's issued RFP/tender document (not APPSolve's response) |
| `COMPLIANCE_PACK` | BBBEE, tax clearance, CSD, COID, VAT registration — compliance-only content |
| `CV_BUNDLE` | A collection of staff CVs submitted as part of a tender |
| `PRESENTATION` | A presentation deck submitted or used in a pitch |
| `PROJECT_PLAN` | A project plan (`.mpp` or Gantt chart) |
| `REFERENCE_SUBMITTED` | A reference letter submitted as part of a tender (not from the reference library) |
| `DRAFT` | A working draft — not the final submitted version |
| `FINAL_SUBMITTED` | The final version submitted to the client |
| `AWARDED` | Document relating to an awarded engagement |
| `LOST` | Document relating to a tender that was not awarded |
| `REGRET_LETTER` | A regret/rejection letter from the client |

---

## Part 3: Document Register — Additional Metadata Fields

The current `DOCUMENT_REGISTER.csv` captures basic file metadata. For the historical tender corpus, the following additional fields are required:

### 3.1 Engagement Identity Fields

| Field | Type | Values / Notes |
|---|---|---|
| `engagement_id` | String | Unique identifier for the engagement. Suggest: `[CLIENT_CODE]-[YEAR]-[SEQ]` e.g., `SASSA-2024-001` |
| `client_name` | String | Normalised client name (from folder path) |
| `client_sector` | Enum | `Government`, `Parastatal`, `Financial Services`, `Retail`, `Mining`, `Healthcare`, `Education`, `Telecoms`, `Manufacturing`, `Energy`, `Professional Services`, `International`, `Other` |
| `client_geography` | Enum | `South Africa`, `Africa (ex-SA)`, `International` |
| `engagement_type` | Enum | `Implementation`, `Support/Managed Services`, `Resource Supply`, `Licensing`, `Health Check/Assessment`, `Upgrade`, `BeBanking Onboarding`, `Other` |
| `engagement_name` | String | The engagement folder name (verbatim from filesystem) |
| `submission_date` | Date | ISO 8601 date of submission (where determinable from file dates or document content) |
| `submission_year` | Integer | Year of submission — useful when exact date unknown |

### 3.2 Business and Outcome Fields

| Field | Type | Values / Notes |
|---|---|---|
| `primary_business_unit` | Enum | `Oracle`, `Acumatica`, `BeBanking`, `Cross-BU`, `TES/Staffing` |
| `business_units_covered` | Multi-select | `Oracle EBS`, `Oracle Fusion/Cloud`, `Oracle APEX`, `Oracle OCI`, `Oracle OIC`, `Oracle BI/EPM`, `Oracle DBA`, `Acumatica`, `BeBanking`, `Other` |
| `services_scope` | Text | Brief plain-text description of what APPSolve proposed (e.g., "Oracle EBS 12.2 upgrade — technical and functional, 6 months") |
| `outcome` | Enum | `Won`, `Lost`, `No Outcome Known`, `In Progress`, `Withdrawn`, `Regret Received` |
| `outcome_evidence` | String | File path or filename of award letter or regret letter if present |
| `contract_value_band` | Enum | `<R500k`, `R500k–R2m`, `R2m–R5m`, `R5m–R10m`, `>R10m`, `Unknown` |

### 3.3 Content Quality Fields

| Field | Type | Values / Notes |
|---|---|---|
| `reusable_content_score` | Integer (1–5) | 1 = not reusable (CVs, compliance only); 5 = highly reusable (full methodology + capability narrative) |
| `approved_for_reuse` | Boolean | Has this document been reviewed and approved for content extraction into the KB? |
| `content_reviewed_by` | String | Name of person who reviewed and scored the document |
| `content_reviewed_date` | Date | When the document was reviewed |
| `methodology_present` | Boolean | Does the document contain a methodology section? |
| `executive_summary_present` | Boolean | Does the document contain an executive summary? |
| `governance_model_present` | Boolean | Does the document contain a governance or project management section? |
| `support_model_present` | Boolean | Does the document contain a support/maintenance model section? |
| `pricing_model_present` | Boolean | Does the document contain a pricing or costing section? |
| `capability_statement_present` | Boolean | Does the document contain a capability or credential section? |
| `security_response_present` | Boolean | Does the document contain a security or information security section? |

### 3.4 Source Tracking Fields

| Field | Type | Values / Notes |
|---|---|---|
| `source_path` | String | Full path to the original file (read-only reference — no copying required initially) |
| `source_folder_structure` | Enum | `Formal (0.Submitted present)`, `Flat`, `Mixed`, `Unknown` |
| `has_editable_version` | Boolean | Is a DOCX/editable version present alongside the PDF? |
| `ocr_required` | Boolean | Is the PDF a scanned image that requires OCR before text extraction? |
| `duplicate_indicator` | String | Note if this document appears to be a version of another registered document |

---

## Part 4: Content Extraction Plan

The following categories of reusable content should be extracted from the historical corpus. Each category describes what to look for, where it is likely to be found, and what form it should take in the Knowledge Base.

### 4.1 Methodologies

**What to extract:** Written descriptions of how APPSolve delivers a project phase. Includes: project initiation, requirements gathering, design, build/configuration, testing, data migration, go-live/cutover, post-go-live stabilisation.

**Where to look:** `0.Submitted` DOCX files from formal implementation tenders. Section headings to search for: "Methodology", "Delivery Approach", "Implementation Approach", "Project Approach", "Our Approach". Top source candidates: NHLS (Oracle EBS Upgrade 2019), SASSA (EBS Support tenders), UJ (multiple), SAT, TCTA, ATNS, Vodacom (Oracle Cloud RFI), Parliament.

**Target format:** Extract the methodology section text verbatim, then structure into the `METH_template.md` format.

### 4.2 Executive Summaries

**What to extract:** Opening sections of proposals that describe APPSolve's value proposition, positioning, and understanding of the client's need. These age less well than methodologies but provide language patterns.

**Where to look:** First 1–3 pages of any proposal DOCX in `0.Submitted`. Section headings: "Executive Summary", "Introduction", "Our Understanding", "About APPSolve".

**Target format:** Extract verbatim, tag by BU and date. Newer summaries (2022+) are more relevant; older ones (pre-2018) may contain outdated product or partnership claims.

### 4.3 Governance Models

**What to extract:** Descriptions of project governance structure — steering committees, project boards, escalation paths, RACI matrices, reporting cadence. Often appears as a diagram (requires manual capture) or a table.

**Where to look:** Project management sections of formal implementation proposals. Also in SLA/MSA contract documents under governance schedules.

**Target format:** Extract tables and narrative, noting that diagrams will require manual redrawing for the KB.

### 4.4 Support Models

**What to extract:** Descriptions of how APPSolve delivers post-go-live or ongoing managed support — SLA tiers, incident response times, team structure, escalation, service desk, on-site vs. remote.

**Where to look:** Support renewal proposals (SASSA EBS Support, UJ ERP Support, ARM, FNB HRMS, NHLS DBA Support). Section headings: "Support Model", "Managed Services", "Service Level Agreement", "Service Delivery Model".

**Target format:** Extract tables (response times, severity levels) and narrative separately. Tables are immediately reusable; narrative needs light editing for new client context.

### 4.5 Managed Services Approaches

**What to extract:** Descriptions of APPSolve's managed services model beyond basic support — proactive monitoring, continuous improvement, roadmap management, license management, capacity planning.

**Where to look:** Oracle managed services proposals. Look specifically in MTN (multiple support engagements), ARM (EBS support), FNB (HRMS managed service).

**Target format:** Narrative description plus any service catalogue tables.

### 4.6 Security Responses

**What to extract:** Responses to security questionnaires or security-specific tender requirements — information security policy, POPIA compliance, ISO 27001 references, data handling, access control, cloud security.

**Where to look:** Supporting documentation folders in government tenders (SASSA, Parliament, TCTA). Also standalone security proposals (ABSA Capital Security Expert Proposal).

**Target format:** Q&A format if extracted from a questionnaire response, or structured narrative if from a proposal section.

### 4.7 Oracle Capability Statements

**What to extract:** Narrative descriptions of APPSolve's Oracle practice — certifications, partner status, module coverage, team composition, years of experience, notable clients (where not confidential).

**Where to look:** Capability sections of any Oracle proposal. Company profile sections within submissions. Oracle partner credential pages. Top sources: any formal Oracle EBS or Cloud implementation proposal.

**Target format:** Service-area capability statements in `CAP_template.md` format, tagged by Oracle product area.

### 4.8 Acumatica Capability Statements

**What to extract:** Same as above for Acumatica. Partner status, implementation experience, module coverage.

**Where to look:** Tiger Brands Acumatica folder and any other Acumatica engagements found during sampling. The `Acumatica Proposal Template` folder in the Customers directory root may contain a reusable template.

**Priority note:** Check the `Acumatica Proposal Template` customer folder — this may be a master template document rather than a client engagement.

### 4.9 BeBanking Capability Statements

**What to extract:** Descriptions of the BeBanking platform, integration capabilities, banking connectivity, and implementation approach.

**Where to look:** Parliament BeBanking FX (2024), Tiger Brands BeBanking (2020), Thirst via Brilliant, Uniq - Brilliant. The BeBanking folder structure visible under several customers indicates active sales. Check Tiger Brands BeBanking Cloud (2020) as an early engagement.

**Target format:** Product capability statements in `CAP_template.md` format, tagged by banking function.

### 4.10 Pricing Assumptions

**What to extract:** Rate card assumptions, day-rate structures, expenses policies, travel assumptions, price escalation clauses, discount frameworks.

**Where to look:** `2.Costing` subfolders across all customers. Pricing workbooks (`.xlsx` files). Narrative pricing assumptions embedded in proposals.

**Target format:** Two outputs: (1) Structured rate card tables (anonymised where needed) for the `13_Quote_Generator/Rate_Cards/` folder; (2) Narrative pricing assumptions text for the `13_Quote_Generator/Assumptions_Exclusions/` folder.

### 4.11 Standard Tender Responses

**What to extract:** Complete, well-written responses to common tender questions that can be reused with light editing: BEE commitment, POPIA compliance, project management approach, quality assurance, staffing methodology, training approach.

**Where to look:** Any formal tender response to government/parastatal clients. These tenders have mandatory standard sections, so submissions invariably contain these responses. SASSA, Parliament, NHLS, UJ are priority sources.

**Target format:** Structured content blocks in `07_Approved_Content/` once reviewed and approved.

---

## Part 5: Identifying High-Value and Reusable Content

### 5.1 High-Value Tenders

Indicators of a high-value tender (worth prioritising for content extraction):

- Formal `0.Submitted` subfolder present
- DOCX proposal document (editable) — not just a PDF
- Multiple proposal components: technical + pricing + project plan
- Government or large enterprise client
- Multiple years/renewals suggesting a successful ongoing relationship
- File count in the engagement folder is high (suggests comprehensive submission)

**Estimated count of high-value tenders:** Based on the 315 customers with RFP folders, and the proportion with formal subfolder structure (~40–50 customers show clear `0.Submitted` with proposal DOCX files), there are approximately **50–80 engagements** where rich, extractable content is likely to exist.

### 5.2 Winning Tenders

APPSolve does not appear to maintain a systematic win/loss record in the folder structure. However, winning tenders can be inferred by:

- The existence of a subsequent contract or SLA in the same customer folder
- The existence of an award letter (search for "award", "congratulations", "successful" in filenames and `.msg` subject lines)
- Multiple support renewal engagements for the same client (implies a previous implementation was won)
- Client appears in the active reference letter library

**Customers confirmed as won (evidenced by reference letters or ongoing support):** SASSA (ongoing support won multiple times), Parliament (multiple awarded RFQs visible in folder names), MTN (multiple support extensions), NHLS (DBA support), UJ (multiple support engagements), ARM (support ongoing), Adcock Ingram (reference letter exists), WITS (reference letter exists), Investec (reference letter exists).

### 5.3 Frequently Reused Content

Content that appears across multiple engagements with minimal changes is the most valuable for the Knowledge Base. Signals of frequently reused content:

- Identical or near-identical passages appearing in proposals to different clients
- Section headings that recur across multiple proposal documents
- The same costing workbook template reused across multiple clients

To identify this without reading every document: focus on the `1.Working` folders (where draft/template versions are stored) and look for files named "template", "standard", "boilerplate", or containing an internal version number that is recycled across clients.

Also check: `0. Proposal Templates` — this appears as a top-level entry in the Customers directory and likely contains master proposal templates worth examining first.

### 5.4 Duplicate Content

Given 14 years of submissions, significant duplication is expected. Duplicates fall into:

- **Version duplicates**: same document at v1, v2, v3 — keep only the latest submitted version
- **Format duplicates**: `.docx` and `.pdf` of the same document — keep both (DOCX for editing, PDF as final reference)
- **Client duplicates**: same boilerplate section reused across clients — identify as "standard section" candidates
- **Period duplicates**: same support renewal submitted every year with minor updates

Duplicate detection should be based on content similarity, not filename — many files are renamed for each client submission. This requires a content-level comparison approach (not a simple file hash).

### 5.5 Candidates for 07_Approved_Content

Documents should be promoted to `07_Approved_Content` only after:

1. A content reviewer has read the document
2. All client-specific references and pricing have been removed or noted
3. The content is factually current (not outdated by product changes or new certifications)
4. A named APPSolve person has approved the content for reuse

**First-pass candidates likely to be approved quickly:**
- BEE commitment sections (appears in almost all tenders, changes infrequently)
- Company background narrative (stable content)
- Oracle partner credential descriptions (update when certs renew)
- Support model SLA tables (structure is reusable; specific terms change per client)
- CV format template (once one clean version is identified)

---

## Part 6: Reassessment of Current Content Gap Analysis

The current `CONTENT_GAP_ANALYSIS.md` was based on the Tender Pack (the evidence repository) and a count of three historical proposal documents. Now that the historical tender corpus has been identified, several of its findings require reassessment.

### 6.1 Findings Likely to Change

**"Methodology — Missing/Must Author from Scratch" (Oracle)**

This finding is almost certainly wrong. Based on the corpus profile:

- NHLS has a submitted `APPSolve NHLS Oracle ERP Upgrade Technical and Pricing Proposal 10062019 V1.docx` — this is almost certainly a detailed technical proposal with methodology content
- SASSA has multiple Oracle EBS support proposal submissions with structured response content
- UJ has at least 20 distinct Oracle engagements spanning 2020–2026 — multiple proposals must exist
- Parliament has Oracle iExpense, APEX, and BeBanking FX proposals
- TCTA (301 files), SAT (429 files), ATNS (171 files) all suggest formal structured submissions

**Revised assessment:** Oracle EBS and Cloud methodology content almost certainly exists across multiple proposals. The effort to extract and structure it is still significant, but the statement "must be authored from scratch" should be replaced with "must be extracted from [list of source documents] and structured."

**"Acumatica Standard Tender Responses — Missing, zero historical proposals"**

This may be wrong. The presence of:
- `Acumatica Proposal Template` as a top-level customer folder
- Tiger Brands Acumatica implementation folder
- Several other potential Acumatica clients

...suggests Acumatica proposal documents exist. They were simply not in the Tender Pack. Until the corpus is sampled, this finding should be changed to "Unknown — requires corpus sampling before authoring begins."

**"BeBanking — Essentially no content exists"**

This understates the known BeBanking history. The corpus reveals:
- Parliament BeBanking FX (2024 — very recent)
- Tiger Brands BeBanking Cloud (2020)
- Thirst via Brilliant (BeBanking)
- Uniq - Brilliant (BeBanking)
- Tiger Reference Letter BeBanking SAP.docx (already in Tender Pack but uninvestigated)

Four or more BeBanking engagements exist with associated proposal documents. The content may be there — it just has not been read.

**"Source material for Oracle methodology: Partial (Mauritius Telecom, SARB, PPro only)"**

This is now known to be a severe undercount. The actual source pool for Oracle methodology content is likely 15–30 formal proposals, not 3. The priority ranking and effort estimates in the Gap Analysis must be re-done after corpus sampling.

### 6.2 Findings Unlikely to Change

The following gaps remain valid regardless of the corpus size:

- **No sidecar metadata for reference letters** — the reference letters themselves exist in the Tender Pack; the problem is structured metadata, not the PDFs
- **Acumatica reference library is thin** — 5 signed references is still 5 signed references; historical tenders don't change this
- **BeBanking reference letters are old or unsigned** — confirmed; the corpus may contain proposal content but not new signed reference letters
- **POPIA compliance statement missing** — this is a governance document that must be authored; it is unlikely to exist in old proposals
- **No approved reusable content in the KB** — this is a fact about the Knowledge Base folder, not the historical corpus

### 6.3 Overall Reassessment

The single most important change is this: **the Gap Analysis assumed that "author from scratch" was the primary work ahead. It is now likely that "extract, structure, and curate" is the primary work** — which is different in character (requires reading source documents) but probably comparable in effort.

The total effort estimate of 53–74 days should be treated as provisional until the corpus has been sampled. It could be significantly lower if the extraction work is well-targeted.

**The authoring sequence in the Gap Analysis (Sections 6 and 7) should not be executed yet.** The first step is corpus sampling.

---

## Part 7: Phased Plan — Read-Only Analysis

All phases below are **read-only**. No source documents are moved, renamed, modified, copied, or reorganised. The outputs are new files created in the Tender Knowledge Base only.

### Phase 0 — Filesystem Manifest (1–2 hours, automated)

**Objective:** Create a complete inventory of the corpus without opening any file.

**Action:** Run a filesystem enumeration across `Parties/Customers/*/RFP/` and export to CSV with columns:
- `customer_name` (from folder path)
- `engagement_name` (subfolder under RFP)
- `sub_folder` (subfolder under engagement, if present)
- `filename`
- `file_extension`
- `file_size_kb`
- `last_modified_date`
- `full_path`

**Output:** `00_Governance/CORPUS_MANIFEST.csv` — the baseline inventory. This is the foundation for all subsequent work.

**Constraint:** No files are opened. No content is read. This is pure filesystem metadata.

### Phase 1 — Engagement Classification (2–3 days, manual with tool support)

**Objective:** For each of the ~315 RFP-holding customers, classify each engagement folder into Category A (formal tender), Category B (support/managed services), or Category C (resource supply), using folder names and file type indicators only.

**Action:**
1. Read each customer's RFP subfolder listing (no individual files opened yet)
2. Assign a primary category (A/B/C) to each engagement based on folder name and file types present
3. Note whether `0.Submitted` or equivalent is present
4. Flag engagements likely to contain methodology, proposal, or pricing content
5. Identify the top 50 engagement candidates for Phase 2 sampling

**Output:** `00_Governance/ENGAGEMENT_REGISTER.csv` with columns: `customer_name`, `engagement_name`, `category`, `has_submitted_folder`, `file_count`, `primary_file_types`, `priority_for_sampling`, `notes`.

**Constraint:** Only folder names and file extension counts are reviewed — no individual file content is read.

### Phase 2 — Priority Sample Reading (5–10 days, human-led)

**Objective:** Read and document the content of the top 50 engagements identified in Phase 1. Understand what reusable content actually exists in the corpus.

**Action:**
1. Open the main proposal document(s) from the `0.Submitted` folder of each priority engagement
2. For each document, complete the content quality fields from the Document Register (Section 3.3 above): which sections are present, what they cover, quality rating, reusability rating
3. Note specific extractable passages by location (document name + section heading) — do not copy the content yet
4. Identify the single best-in-class example for each content category (methodology, executive summary, support model, governance, pricing narrative, etc.)

**Output:**
- `00_Governance/SAMPLE_READING_LOG.md` — notes from each document reviewed, with content pointers
- Updated `ENGAGEMENT_REGISTER.csv` with quality scores and approved_for_extraction flags
- `00_Governance/CONTENT_INVENTORY.md` — a map of which existing documents contain which KB content categories

**Constraint:** Documents are read but no content is copied or modified. Source paths are noted for later extraction. No files are moved.

### Phase 3 — Gap Analysis Revision (1 day, analytical)

**Objective:** Revise `CONTENT_GAP_ANALYSIS.md` using evidence from Phase 2 sampling.

**Action:**
1. For each content gap identified in the current Gap Analysis, update the status based on Phase 2 findings
2. Replace "must author from scratch" ratings with "extract from [source]" where applicable
3. Revise the priority ranking and effort estimates
4. Produce a revised authoring sequence that draws on confirmed source documents

**Output:** Revised `CONTENT_GAP_ANALYSIS.md` (with revision date and note that it is based on corpus sampling).

**Constraint:** No content authored yet — this is still analysis.

### Phase 4 — Document Register Population (3–5 days, data entry)

**Objective:** Populate the `DOCUMENT_REGISTER.csv` for all priority-tier engagements (Category A and high-value Category B from Phase 1).

**Action:**
1. Add one row per engagement to the Document Register
2. Complete all metadata fields defined in Section 3 above, using Phase 2 reading notes as source
3. Set `approved_for_reuse` to `false` for all entries — extraction approval comes later
4. Note which documents contain each of the 11 extractable content categories

**Output:** Populated `DOCUMENT_REGISTER.csv` covering ~50–100 priority engagements.

### Phase 5 — Extraction Planning (1–2 days, editorial)

**Objective:** Produce a prioritised extraction plan that specifies exactly which sections from which documents should be extracted into which KB folders.

**Action:**
1. From Phase 2 reading notes, identify the best-in-class source for each KB content category
2. For each extraction, specify: source document path, section heading(s), target KB folder, required editing (e.g., "remove client name", "update for 2026 certifications")
3. Group extractions into logical work packages (e.g., "Oracle methodology extraction — 3 documents, ~2 days")

**Output:** `00_Governance/EXTRACTION_PLAN.md` — a document-level extraction guide, ready to execute in Phase 6.

### Phase 6 — Controlled Extraction (ongoing, following approval)

**Objective:** Extract, edit, and load approved content into the Knowledge Base.

This phase is outside the scope of this plan — it begins only after Phases 0–5 are complete and the Extraction Plan has been reviewed and approved. No content should be extracted before Phase 3 (revised Gap Analysis) is signed off.

---

## Appendix: Immediate Actions

Three things can be done immediately, before Phase 0 begins:

1. **Check the `0. Proposal Templates` customer folder** — this top-level folder may contain master proposal templates that are the direct ancestors of all submitted proposals. It should be examined first as it may accelerate all subsequent phases.

2. **Check the `Acumatica Proposal Template` customer folder** — same reason. This may be a master Acumatica template.

3. **Check `APPSolve Internal` customer folder** — internal documents may include rate cards, standard terms, or internal methodology documents not otherwise visible in client-facing submissions.

---

*This plan is read-only by design. No files in `Parties/Customers/` should be moved, renamed, copied, or modified at any stage. All outputs are created in the Tender Knowledge Base only.*

*Review before commencing Phase 0: confirm the filesystem manifest command is acceptable and that the output location for CORPUS_MANIFEST.csv is correct.*
