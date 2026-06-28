# Approved Content Usage Guide
**Version:** 1.0 | **Created:** 2026-06-10 | **Owner:** Hein Blignaut (APPSolve BU lead)
**Status:** Active — governing document for all AI-assisted tender and knowledge-base activities

---

## 1. Purpose and Scope

### 1.1 Why this document exists

The Tender Knowledge Base now contains content at multiple maturity levels, sourced from multiple systems:

- Approved capability statements (safe for tender use)
- Files under review (verified but not yet approved)
- Draft extractions (unverified; extraction work only)
- Historical tender proposals (primary IP source; not inherently approved)
- Active proposal templates (structural guidance; not approved for direct reuse)
- Compliance documents sourced from the Tender Pack (some approved, some pending)
- Consultant metadata records sourced from APPTime (approved for skill-matching only)

Each class carries different rules. Using content from the wrong class in a live tender creates legal risk (incorrect claims), reputational risk (outdated product statements), and compliance risk (expired certifications). This guide provides a single authoritative reference so every AI session, every human editor, and every automated process operates under identical rules without needing to re-derive them.

### 1.2 What this document governs

| Repository | Governed? | Notes |
|---|---|---|
| `07_Approved_Content/` (all stages) | Yes | Core pipeline — full rules apply |
| `06_Capabilities/`, `08_Methodologies/`, `09_Executive_Summaries/` | Yes | KB destination folders; approved content only |
| `03_People/Resource_Profiles/` | Yes | Consultant Index Records — ADR-001 rules apply |
| `Parties/Customers/[Client]/RFP/` | Yes | Historical corpus — read-only; extraction source only |
| `Parties/Customers/0. Proposal Templates/` | Yes | Active templates — structural reference only |
| `Tender Pack/` | Yes | Evidence and compliance archive — read-only |
| APPTime | Yes (by reference) | System of record for consultant CVs — not a KB folder |
| `03_People/CVs/` | Yes | Not used — full CVs generated from APPTime only |

### 1.3 Relationship to AI_CONTEXT.md

`AI_CONTEXT.md` is the **operational fact reference** for AI sessions. It records confirmed facts, approved file locations, validated baselines, and prohibited claims. This document governs **how content classes are used** — the rules that sit above individual facts. When a conflict appears to exist between the two documents, this guide takes precedence on matters of process and content governance; `AI_CONTEXT.md` takes precedence on factual claims.

### 1.4 Relationship to ADR-001

`00_Governance/ADR-001-CV_SOURCE_OF_TRUTH.md` is an architecture decision record governing one specific content class: consultant CV content and APPTime as system of record. This document incorporates ADR-001 into the broader content governance framework in Sections 7 and 9. ADR-001 remains the definitive record for the CV architecture decision itself.

### 1.5 Relationship to EXTRACTION_WORKFLOW.md

`00_Governance/EXTRACTION_WORKFLOW.md` governs **pipeline mechanics**: entry criteria, metadata blocks, file naming, readiness ratings, and the register update checklist. This document governs **usage rules** — what may be done with content at each stage. The two documents are complementary. EXTRACTION_WORKFLOW.md is the extractor's operational manual; this document is the user's and AI's operational rulebook.

---

## 2. Source Classification Matrix

| Source | System of Record | May AI Read? | May AI Cite Directly? | May AI Paraphrase? | Requires Human Review? | Approved for Tender Use? | Notes |
|---|---|---|---|---|---|---|---|
| **Approved Content** (`07_Approved_Content/Approved/` or KB destination folders) | Knowledge Base | Yes | Yes | Yes | No — already reviewed | Yes | `approved_for_reuse: Yes` confirmed by BU lead. This is the only class safe for live tender use. |
| **Review_Required Content** (`07_Approved_Content/Review_Required/`) | Knowledge Base (staging) | AI may read for extraction work | No | No | Yes — BU lead review required | No | Source-verified by extractor; not yet approved. May not be used in any client-facing document. |
| **Candidate_Content** (`07_Approved_Content/Candidate_Content/`) | Knowledge Base (staging) | AI may read for extraction work only | No | No | Yes — extractor self-review + BU lead review | No | Raw extraction. Unverified. No client-facing use at any point until it reaches Approved. |
| **Historical Tenders** (`Parties/Customers/[Client]/RFP/`) | Historical Corpus (read-only) | Yes — extraction research only | No | No — extract and modernise only | Yes — full pipeline required | No | Primary IP source. Source documents only. Content must enter the extraction pipeline before it can be used. |
| **Historical Quotes** (`Parties/Customers/[Client]/` quote documents) | Historical Corpus (read-only) | Yes — research reference only | No | No | Yes — full pipeline required | No | Same rules as historical tenders. Never copy quote pricing or commercial terms — outdated and commercially sensitive. |
| **Templates** (`Parties/Customers/0. Proposal Templates/`) | Historical Corpus (read-only) | Yes — structural reference | No | No | Yes — extract and verify | No | Active templates are the highest-fidelity extraction starting point but are not inherently approved. Content must enter the pipeline. Document type: TMPL. |
| **Compliance Documents** (`01_Compliance/` or `Tender Pack/`) | Tender Pack (primary) | Yes | Conditional — check expiry | No | Check `expiry_date` before use | Conditional | BEE, CIPC, tax clearance, insurance. Check expiry before citing. BEE expires 2026-07-31. |
| **References** (`04_References/`) | Tender Pack (primary) | Yes | Signed PDFs only | No | Human to confirm signatory | Conditional | Only cite signed reference letters. Unsigned templates are not references. |
| **Certifications** (`Tender Pack/` and `03_People/Certifications/`) | Tender Pack (primary) | Yes | Conditional — check expiry | No | Check expiry before use | Conditional | Oracle Level 1 confirmed. Oracle Gold expired August 2021 — do not cite. Acumatica Gold Partner confirmed. |
| **Corporate Documents** (`01_Compliance/` — CIPC, B-BBEE, tax) | Tender Pack (primary) | Yes | Conditional — check expiry | No | Check expiry before use | Conditional | CIPC registration is permanent. Tax clearance and BEE have expiry dates — check before submitting. |
| **Consultant Index Records** (`03_People/Resource_Profiles/`) | Knowledge Base (metadata layer) | Yes — skill matching only | No — skill tags only | No | Yes — AI flags candidates; human confirms selection | Skill-matching only — not for CV generation | ADR-001 governs this class. Records contain metadata (skill tags, certifications, availability). Not a CV. |
| **APPTime CVs** | APPTime (authoritative — external) | No direct access | No | No | Yes — user generates from APPTime | Yes — after generation and review | Full CV content lives in APPTime only. AI instructs user to generate from APPTime; does not generate CV text from KB data. |

---

## 3. Content Usage Rules

### 3.1 Approved Content

**Approved content is the only content safe for live tender use.** Approved content has been extracted from a source document, verified by the extractor against the source, reviewed in full by a BU lead, and registered with `approved_for_reuse: Yes`.

Rules:
- May be cited verbatim in a tender response.
- May be paraphrased or adapted to fit tender format.
- May be combined with other approved content.
- The extractor may not set `approved_for_reuse: Yes` — this is a BU lead action only, performed after reading the full document.
- If content is approved with restrictions (`approved_for_reuse: Conditional`), those restrictions are recorded in the document's metadata block and must be respected. Read the restriction before using.
- Always confirm the file's `review_status` field reads `Approved` before citing it. The folder location alone is not sufficient.

Current approved files: see `AI_CONTEXT.md` — "Approved Content Available" section.

### 3.2 Review_Required Content

**Review_Required content has been extracted and verified by the extractor but has not been reviewed by a BU lead.** It is awaiting BU sign-off.

Rules:
- May be read by AI for pipeline work (comparing to source, checking consistency).
- Must never be cited in a tender response or proposal.
- Must never be paraphrased for client-facing use.
- Must never be treated as a signal of APPSolve's current capability — it is a candidate, not a confirmed statement.
- If a tender requires content that only exists in Review_Required, flag the gap and instruct the BU lead to review. Do not use the Review_Required version as a workaround.

### 3.3 Candidate_Content

**Candidate content is a raw extraction.** It has not been reviewed by anyone. It may contain outdated claims, client-specific language that was not fully removed, or AI errors.

Rules:
- May be read by AI when performing extraction or self-review work.
- Must never be cited, paraphrased, or used in any client-facing document.
- Must never be used as a source of fact for answering questions about APPSolve's capabilities.
- AI sessions that are not performing extraction work should treat Candidate_Content as if it does not exist.

### 3.4 Historical Tenders and Quotes

**Historical tenders are the primary IP source for the Knowledge Base, but they are not approved content.**

Rules:
- May be read for extraction purposes.
- Must not be cited directly in a tender. Text from a 2017 SITA proposal is not the same as a 2026 APPSolve capability statement.
- Content must enter the extraction pipeline (Candidate → Review → Approved) before it can be used.
- Won engagements carry stronger IP signal than unsuccessful bids. The readiness rating records this assessment.
- Never copy pricing, commercial terms, or SLA commitments from historical quotes. These are outdated and commercially sensitive.
- Source files are read-only — never move, copy, rename, or modify.

### 3.5 Templates

**Active proposal templates (`Parties/Customers/0. Proposal Templates/`) are the highest-fidelity extraction starting point.** They reflect APPSolve's current positioning more closely than older historical tenders.

Rules:
- May be used as a structural reference and extraction source.
- Must not be copied into a tender verbatim — they contain client-specific sections (e.g., the Acumatica September 2025 template contains HearX Group client content in Section 1 that must never be reused).
- Document type: TMPL in the register.
- Content extracted from templates enters the standard pipeline like any other source.

### 3.6 Compliance Documents, References, and Certifications

**These documents come from the Tender Pack.** They are evidence, not capability statements.

Rules:
- Check `expiry_date` before citing any document with an expiry. Expired documents must not be cited.
- **BEE certificate expires 2026-07-31.** Do not cite after this date without confirmed renewal.
- **Oracle Gold Partner — expired August 2021.** Do not cite. Cite "Oracle Level 1 Partner" only.
- Only cite signed reference letters. Unsigned templates are placeholders, not references. Do not present unsigned templates to a client.
- CIPC registration is permanent; no expiry check required.

### 3.7 APPTime Consultant Content

**APPTime is the authoritative source for all consultant CV content.** The rules for this class are governed by ADR-001 and encoded permanently in `AI_CONTEXT.md`.

Rules:
- AI may read Consultant Index Records in `03_People/Resource_Profiles/` for skill-matching.
- AI must not generate CV text, Professional Summaries, or project experience narratives from KB data.
- When a tender requires named consultant CVs, AI identifies candidates from index records and instructs the user: "The following consultants match this requirement: [list]. Please generate current CVs from APPTime for the selected consultant(s)."
- A consultant with `available_for_tenders: false` must not be proposed, regardless of skill match.
- APPTime overrides any consultant information found in historical tenders, the Tender Pack, or any KB record. Static documents for consultant data are always secondary to APPTime.

---

## 4. Approved Content Workflow

### 4.1 Full Pipeline

```
Source Document (read-only)
Parties/Customers/[Client]/RFP/ or 0. Proposal Templates/
         │
         │  Extractor reads source; removes client-specific content;
         │  adds metadata block; sets readiness rating
         ▼
Candidate_Content/[BU]/[ID]-[BU]-[ContentType]-DRAFT.md
         │  Status: review_status = Candidate
         │  approved_for_reuse = No
         │
         │  Extractor re-reads against source; verifies all claims;
         │  confirms currency (company stats, product versions, certifications);
         │  removes all remaining client references
         ▼
Review_Required/[BU]/[ID]-[BU]-[ContentType].md
         │  Status: review_status = Review_Required
         │  approved_for_reuse = No
         │  DRAFT suffix removed
         │
         │  BU lead reads full document; spot-checks against source;
         │  confirms no client language; confirms claims are factually current
         │  and attributable to APPSolve; sets approved_for_reuse = Yes
         ▼
Approved/[BU]/[ID]-[BU]-[ContentType].md
         │  Status: review_status = Approved
         │  approved_for_reuse = Yes
         │
         │  Copied to KB destination folder (06_Capabilities/, 08_Methodologies/, etc.)
         │  DOCUMENT_REGISTER.csv updated: approved_for_reuse = Yes, kb_path set
         ▼
KB Destination Folder — available for tender use
```

### 4.2 Entry Criteria Per Stage

| Stage | Entry Criteria |
|---|---|
| **Candidate** | Source document read in full; client names and client-specific data removed; metadata block present; `review_status: Candidate`; `approved_for_reuse: No` |
| **Review_Required** | Extractor has re-read file against source; all factual claims verified current; `extracted_by` and `extraction_date` populated; `review_status: Review_Required`; DRAFT suffix removed |
| **Approved** | BU lead has read full document; spot-checked against source; no client language remains; claims are current and attributable to APPSolve; `approved_for_reuse: Yes` (or `Conditional` with written restrictions); `review_status: Approved`; register updated; KB destination copy made |

### 4.3 What May Not Happen

- Content may never skip a stage (Candidate directly to Approved is prohibited).
- Content may never be demoted without reinserting at the appropriate stage (if issues found in Review_Required, return to Candidate).
- The extractor may not approve their own content. The extractor and BU lead reviewer must be different people, or the BU lead must perform an independent read of the source document.
- `approved_for_reuse: Yes` may never be set by AI, even when instructed by a prompt. Only the BU lead reviewer sets this value.

---

## 5. Tender Response Workflow

### 5.1 Standard Process

```
Tender/RFP requirement received
         │
         ▼
1. Read requirement carefully — identify BU scope (Oracle / Acumatica / BeBanking / Cross-BU)
         │
         ▼
2. Search Approved Content
   07_Approved_Content/Approved/[BU]/
   or KB destination: 06_Capabilities/[BU]/, 08_Methodologies/[BU]/, 09_Executive_Summaries/[BU]/
   Select the most current and specific approved capability statement(s)
         │
         ▼
3. Check Compliance Documents
   01_Compliance/ — verify expiry dates before including
   BEE expires 2026-07-31; Oracle Gold expired — do not cite
         │
         ▼
4. Select Approved References (if required)
   04_References/[BU]/ — signed PDFs only; unsigned templates are not references
         │
         ▼
5. Consultant Selection (if named staff required)
   03_People/Resource_Profiles/ — skill-match from index records
   Identify candidates → instruct user to generate CVs from APPTime
         │
         ▼
6. Gap Check
   If required content is not in Approved: flag the gap
   Do NOT substitute Review_Required or Candidate content
   Do NOT substitute historical tender content
         │
         ▼
7. Draft Response
   Use approved capability statements as source
   Adapt to tender format and context
   Flag any AI-authored sections for human review before submission
         │
         ▼
8. Human Review Before Submission
   BU lead confirms all claims; checks no unapproved content was used
   Confirms compliance documents are current
   Confirms consultants are available
```

### 5.2 Explicit Prohibitions in Tender Responses

- **Never** cite or paraphrase content from `Candidate_Content/` or `Review_Required/` in a tender response.
- **Never** copy text from historical tenders or proposal templates directly into a tender without it first passing through the extraction pipeline.
- **Never** fabricate certifications, partner tiers, client references, awards, or headcount figures.
- **Never** claim capabilities not confirmed in source documents (e.g., BeBanking SAP integration — no corpus evidence; do not claim).
- **Never** cite an expired compliance document (BEE, tax clearance, ISO).
- **Never** use a consultant whose `available_for_tenders: false`.
- **Never** claim Oracle Gold Partner — Gold Membership expired August 2021.

---

## 6. Quote Generation Workflow

The Quote Generator (`13_Quote_Generator/`) is reserved — not yet built. These rules apply to any quote, proposal, or SOW generated with AI assistance.

### 6.1 Allowed Sources

| Content Type | Allowed Source |
|---|---|
| Company overview and history | Approved Cross-BU files (W1S1-001, W1S1-002 when approved) |
| Delivery model and service lines | W1S1-007 (approved) |
| Key differentiators | W1S1-009 (approved) |
| Geographic presence | W1S1-008 (approved) |
| Partnership credentials | Approved BU-specific files (W1S1-003, W1S1-004, W1S1-005) |
| Module/product capabilities | Approved capability statements only |
| Implementation methodology | Approved methodology files only (none yet in Wave 1 — flag as gap) |
| Pricing | Approved rate cards from `02_Commercial/` only |
| Company registration | `01_Compliance/` — CIPC (permanent) |
| BEE level | `01_Compliance/` — check expiry date before including |

### 6.2 Not Allowed in Quotes

- Candidate or Review_Required capability statements — await BU lead approval.
- Historical quote pricing — outdated and commercially sensitive; never copy rate cards or pricing from `Parties/Customers/`.
- CV narrative generated by AI — obtain CVs from APPTime.
- Claims not backed by an approved source (e.g., specific methodology details not yet extracted and approved).

### 6.3 Gap Handling

If a required section (e.g., Oracle Fusion methodology) does not yet have approved content, the correct action is:
1. Flag the gap to the user.
2. Note what source document exists that could be extracted (e.g., TMPL-001 Oracle Fusion template).
3. Do not fabricate the section.
4. Do not substitute an unapproved extraction.

---

## 7. Consultant Selection Workflow

### 7.1 Process

```
Tender requires named consultants
         │
         ▼
1. Read the requirement — identify role, skills, BU, experience level needed
         │
         ▼
2. Search Consultant Index Records
   03_People/Resource_Profiles/[BU]/CV-XXX.md
   Filter by: skill_tags, modules_or_products, active_certifications, available_for_tenders
         │
         ▼
3. Eliminate unavailable consultants
   available_for_tenders: false → remove from shortlist, no exceptions
         │
         ▼
4. Present candidate shortlist to user
   "The following consultants match this requirement: [CV-001, CV-003, CV-007]"
   Include: name, role, relevant skill_tags, relevant certifications
         │
         ▼
5. User selects consultant(s)
         │
         ▼
6. Instruct user to generate CVs from APPTime
   "Please generate current CVs from APPTime for the selected consultant(s) 
    and attach to the tender submission."
         │
         ▼
7. Human reviews generated CVs for accuracy before submission
```

### 7.2 What AI Must Never Do

```
Consultant Index Record → Generate CV narrative   ✗ PROHIBITED
Consultant Index Record → Write Professional Summary   ✗ PROHIBITED
Consultant Index Record → Infer project experience   ✗ PROHIBITED
Historical Tender → Extract consultant skills   ✗ UNRELIABLE — skills data ages; use APPTime
```

### 7.3 When No Index Records Exist

Consultant Index Records have not yet been created (pre-condition for CONSULTANT_INDEX_PROGRAMME.md rollout not yet met). Until records exist:
1. Instruct the user to select consultant(s) manually.
2. Instruct the user to generate CVs from APPTime.
3. Do not attempt to derive consultant profiles from historical tenders or Tender Pack CVs.

---

## 8. Future AI Session Guardrails

### 8.1 Core Rules — No Exceptions

| Rule | Action |
|---|---|
| Content class is unknown | Assume Candidate — do not use in tender |
| Content is in `Candidate_Content/` or `Review_Required/` | Read for pipeline work only — never cite |
| No approved content exists for a required tender section | Flag the gap — do not substitute; do not fabricate |
| A compliance document has no confirmed expiry date | Do not cite — ask user to verify |
| A consultant index record shows `available_for_tenders: false` | Remove from shortlist — do not propose |
| A claim conflicts with the validated fact baseline in `AI_CONTEXT.md` | Use the baseline value — do not defer to template text or historical tender text |
| A historical tender source says one thing; an approved KB file says another | Use the approved KB file — it has been reviewed; the historical tender has not |
| User asks AI to approve content or set `approved_for_reuse: Yes` | Decline — this action is reserved for the BU lead reviewer only |
| User asks AI to skip a pipeline stage | Decline — the pipeline is mandatory; no shortcuts |

### 8.2 Escalation Triggers

Escalate to a human (Hein Blignaut / BU lead) before proceeding when:
- A new claim about APPSolve's capabilities, partnerships, or geographies would be the first time it appears in any KB document.
- A compliance document's expiry cannot be confirmed.
- A tender requires a consultant profile but no index records exist.
- A source document contradicts an approved KB file in a material way.
- A user instruction would require setting `approved_for_reuse: Yes` or skipping the pipeline.
- Content appears to be AI-authored and has not been flagged as such.

### 8.3 Session Start Checklist

At the start of any AI session involving tender work or KB maintenance:

1. Check `AI_CONTEXT.md` for the current approved file list and validated fact baseline.
2. Check `KNOWLEDGE_BASE_STATUS.md` for current pipeline counts and content coverage.
3. Check `HANDOVER.md` for pending actions and constraints from previous sessions.
4. Check `00_Governance/EXTRACTION_LOG.csv` for file locations if searching for specific content.
5. Do not proceed from memory alone — verify current state against actual files.

### 8.4 What "Approved" Does Not Mean

- Approved does not mean perpetually current. Facts age. If a fact in an approved file is superseded by a new BU lead confirmation, the file must be updated before continued use. A confirmed overriding fact goes into `AI_CONTEXT.md` immediately.
- Approved does not mean complete. An approved file may cover one capability area but not another. Do not extrapolate approved content to cover adjacent claims.
- Approved does not mean unrestricted. Some files are approved with `Conditional` restrictions. Read the restriction.

---

## 9. Relationship to ADR-001

### 9.1 Core Decision

Architecture Decision Record ADR-001 (`00_Governance/ADR-001-CV_SOURCE_OF_TRUTH.md`, adopted 2026-06-10) establishes:

- **APPTime is the authoritative source for all consultant CV content.** APPTime data overrides any other source.
- **The KB stores Consultant Index Records only** — lightweight metadata: name, role, BU, skill tags, active certifications, availability flag, APPTime reference ID.
- **Full CV extraction into the KB is permanently cancelled.** The original extraction plan (MIGRATION_ANALYSIS.md Priority 25) is void. CV documents in `Tender Pack/Rate Card/` are read-only evidence; they are not migrated.
- **`03_People/CVs/` contains no KB content.** Full CVs are generated from APPTime on demand.
- **`03_People/Resource_Profiles/` is the active consultant folder.** This is where Consultant Index Records live.

### 9.2 Why This Decision Was Made

APPSolve's APPTime system is the operational CV management platform. CVs are generated from APPTime for every tender, quote, and proposal. Extracting full CVs into the KB would create a third source of truth (APPTime → Tender Pack → KB) with no synchronisation mechanism and a demonstrated drift problem (multiple CV versions already exist in the Tender Pack for the same consultants). The KB's requirement from CV data is skill-matching, not content generation — Consultant Index Records satisfy this requirement with minimal maintenance burden.

### 9.3 Implications for KB Activities

| Activity | Before ADR-001 | After ADR-001 |
|---|---|---|
| CV extraction from Tender Pack | Planned — MIGRATION_ANALYSIS.md Priority 25 | Cancelled permanently |
| CV content in KB | Intended (full CV pages) | Not stored — APPTime only |
| `03_People/CVs/` folder | Intended destination | Unused — documented as not used |
| AI-generated CV narrative | Possible but risky | Prohibited — no exception |
| Consultant skill-matching | Not designed | Supported via index records |
| Tender CV content | KB-derived | APPTime-generated, human-reviewed |

---

## 10. Recommendations

The following governance risks and improvements were identified while drafting this guide.

### 10.1 Risk: Approved Content Without a Centralised Index

**Risk:** Approved content is confirmed via `review_status: Approved` in individual file metadata, the EXTRACTION_LOG.csv, and an entry in `AI_CONTEXT.md`. There is no single authoritative list maintained in one location that is guaranteed current.

**Recommendation:** Treat `AI_CONTEXT.md` — "Approved Content Available" section — as the canonical approved file list. Update it immediately each time a file is promoted to Approved. Do not rely on folder scanning alone; metadata fields can fall out of sync with folder location if files are moved without updating the metadata block.

### 10.2 Risk: No Expiry Tracking for Approved KB Content

**Risk:** Approved capability statements extracted from 2017–2024 source documents may contain facts that age without a defined review trigger. There is currently no `review_by` or `content_expiry` field in the extraction metadata block.

**Recommendation:** Add a `next_review_date` field to the extraction metadata template. Set to 12 months from approval date for DIRECT-rated content; 24 months for AI-authored content; and trigger immediately if a BU lead confirms a material fact has changed. This is a template addition only — no existing approved files need to be retroactively updated unless content is known to have aged.

### 10.3 Risk: Review_Required Bottleneck

**Risk:** Nine BeBanking files are currently in Review_Required awaiting BU lead review. They cannot be used in a tender until approved. A tender arriving before the review is complete would force a choice between using unverified content or presenting no BeBanking capability. This is the current state.

**Recommendation:** Prioritise the BeBanking BU lead review of W1S3-001 through W1S3-010 (excluding W1S3-005) as the highest-value immediate action. This unblocks full BeBanking H2H capability coverage across all BeBanking tender sections. Effort estimate: 2–3 hours of BU lead reading time.

### 10.4 Risk: No Standard for AI-Authored Content Flagging

**Risk:** The source hierarchy in `AI_CONTEXT.md` includes AI-authored content as the lowest-priority source ("only when no source document exists"). There is no established convention for flagging AI-authored content within a KB file so that future reviewers know which sections were AI-authored versus source-extracted.

**Recommendation:** Establish a frontmatter field `ai_authored_sections: []` in the extraction metadata block. When AI authors one or more sections of a file (not extracting from source), list the section headings. This makes it explicit at review time which parts require closest human scrutiny.

### 10.5 Risk: CONTENT_GAP_ANALYSIS.md in Active Use

**Risk:** `00_Governance/CONTENT_GAP_ANALYSIS.md` was rated "unreliable — do not use until revised post-Wave 3" in `project_context.md`. If it is opened by an AI session without the warning, it may be used to make incorrect planning decisions.

**Recommendation:** Add a prominent deprecation notice at the top of CONTENT_GAP_ANALYSIS.md itself (not just in the memory file) so the warning is embedded where the risk arises. This is a single-line edit.

### 10.6 Recommended Next Activity

After this guide is confirmed as complete and accurate by Hein Blignaut:

**Priority 1 — BeBanking BU lead review (W1S3-001 through W1S3-010).** Nine files are sitting in Review_Required. This is the highest-value bottleneck. Two to three hours of BU lead reading time unlocks full BeBanking H2H coverage. Approval would bring the total approved file count from 9 to 18.

**Priority 2 — Deprecation notice in CONTENT_GAP_ANALYSIS.md.** Five-minute task; mitigates a real AI misdirection risk.

**Priority 3 — Session B (Acumatica module library).** Six of nine files are DIRECT-rated. Fast review cycle. Unlocks Acumatica module coverage for any module-specific tender.

---

*This document is maintained by Hein Blignaut. Update when: the pipeline structure changes; a new content class is introduced; a new BU or product line is added; or an AI session identifies a governance gap not covered here. Version history: 1.0 (2026-06-10) — initial creation.*
