# Extraction Workflow
**Effective:** 2026-06-08 | **Applies to:** All content extracted from historical tender corpus

---

## Pipeline

```
Source document          Stage 1                Stage 2               Stage 3
(read-only, never    ──► Candidate_Content/ ──► Review_Required/ ──► Approved/
 moved or modified)      DRAFT file               Self-reviewed         BU lead signed off
                         metadata block added     source verified       register updated
                                                                        ──► Copy to KB destination
```

Content may only move **forward** through the pipeline. It may move **back** to Candidate at any stage if issues are found. It may never skip a stage.

---

## Stage Definitions

| Stage | Folder | What it means | Who acts |
|---|---|---|---|
| **Candidate** | `07_Approved_Content/Candidate_Content/` | Raw extraction. Client text removed. Metadata block added. Not yet reviewed. | Extractor |
| **Review Required** | `07_Approved_Content/Review_Required/` | Extractor has self-reviewed against source. Ready for BU lead. | BU lead reviewer |
| **Approved** | `07_Approved_Content/Approved/` | BU lead has read and signed off. Safe to use in tenders. | BU lead → register update → KB copy |

---

## Entry Criteria Per Stage

**To enter Candidate_Content:**
- [ ] Source document read in full
- [ ] All client names, client references, client-specific figures removed
- [ ] APPSolve's own text retained accurately (no paraphrasing that changes meaning)
- [ ] Extraction metadata block present (see template below)
- [ ] `review_status: Candidate`, `approved_for_reuse: No`

**To move to Review_Required:**
- [ ] Extractor has re-read extracted file against source document
- [ ] All factual claims verified current (company stats, certifications, product versions)
- [ ] `extracted_by` and `extraction_date` fields populated
- [ ] `review_status: Review_Required`

**To move to Approved:**
- [ ] BU lead has read the full extracted document (not just metadata)
- [ ] BU lead has spot-checked against source document
- [ ] No client-specific language remains
- [ ] All claims are factually current and attributable to APPSolve
- [ ] `approved_for_reuse: Yes` (or `Conditional` with written restrictions)
- [ ] `review_status: Approved`
- [ ] DOCUMENT_REGISTER.csv row updated: `approved_for_reuse = Yes`, `kb_path` set
- [ ] File copied to KB destination folder

---

## Extraction Metadata Block

Every extracted file must begin with this block. Template: `00_Governance/Templates/EXTRACTION_CANDIDATE.meta.md`

```yaml
---
source_document: ""          # Filename only — e.g. "Oracle Fusion Template.docx"
source_path: ""              # Full path within Parties/Customers/ — never a KB path
extraction_date: ""          # YYYY-MM-DD
extracted_by: ""             # Person's name
readiness: ""                # DIRECT | MODERNISE | STRUCTURE ONLY
approved_for_reuse: "No"     # No | Conditional | Yes — only BU lead may set Yes
business_unit: ""            # Oracle | Acumatica | BeBanking | Cross_BU
review_status: "Candidate"   # Candidate | Review_Required | Approved
---
```

The `review_status` value **must match** the folder the file is currently in.

---

## File Naming Convention

`[ExtractionID]-[BU]-[ContentType]-DRAFT.md`

| Token | Values | Example |
|---|---|---|
| ExtractionID | Code from EXTRACTION_PLAN.md | `1A`, `3A`, `7A` |
| BU | Oracle, Acumatica, BeBanking, Corp | `ORA`, `ACU`, `BB`, `CORP` |
| ContentType | Brief descriptor, no spaces | `ExecutiveSummary`, `CompanyProfile`, `H2HCapability` |
| Suffix | Always `DRAFT` until Approved | `DRAFT` |

Example: `3A-ACU-ModuleLibrary-Financials-DRAFT.md`

The `DRAFT` suffix is removed when the file reaches `Approved/` and is copied to its KB destination.

---

## Readiness Ratings

| Rating | Meaning | Action required before use |
|---|---|---|
| `DIRECT` | Factually current; use with minor name/date updates only | Update years in business, verify contact names |
| `MODERNISE` | Structurally sound; content needs updating | Update tech references, company stats, product versions, remove deprecated items |
| `STRUCTURE ONLY` | Framework is reusable; text must be written fresh | Use as outline; write new content against this structure |

---

## TMPL Document Type

Introduced 2026-06-08 as the 9th document type in the register. Use TMPL for documents that are maintained as reusable proposal templates (as opposed to HIST for submitted historical tenders).

| Field | TMPL value | Notes |
|---|---|---|
| `doc_type` | `TMPL` | |
| `sub_type` | `Active-Template` or `Deprecated-Template` | |
| `status` | `Active` or `Deprecated` | Not `Archived` |
| `approved_for_reuse` | `Conditional` | Most templates contain some client-specific content |
| `client_name` | Last client this template was deployed for | Not a blank template — note the client and mark sections accordingly |

Sidecar template: `00_Governance/Templates/TMPL_template.md`

---

## Prohibited Actions

- **Source files** in `Parties/Customers/` must never be moved, copied, renamed, or modified
- **Extracted content** must never enter `Approved/` directly from `Candidate_Content/`
- **Tender responses** must never cite files from `Candidate_Content/` or `Review_Required/`
- **AI systems** must not be given access to `Candidate_Content/` or `Review_Required/` folders
- **`approved_for_reuse: Yes`** must never be set by the extractor — only by the BU lead reviewer
- **DRAFT suffix** must not be removed from a filename until the file reaches `Approved/`

---

## Register Update Checklist (on approval)

When content is approved, update `00_Governance/DOCUMENT_REGISTER.csv` for the **source document row** (HIST-XXX or TMPL-XXX):

- [ ] `approved_for_reuse` → `Yes` (or `Conditional`)
- [ ] `kb_path` → path to the approved file in the KB destination folder
- [ ] `last_reviewed` → today's date
- [ ] `reusable_sections` → confirm list matches what was actually extracted
