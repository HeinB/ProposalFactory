---
document_id: TD-023
title: Proposal Publishing Standard v1.0
version: "1.0"
status: APPROVED
date: "2026-06-30"
engine: proposal_publishing_policy.py v1.0
platform_maturity: L6.3
---

# Proposal Publishing Standard v1.0

## Purpose

The Proposal Publishing Policy Engine (PPPE) is the policy enforcement layer between the Knowledge Base Renderer and customer-facing DOCX output. It does NOT modify Knowledge Assets, KRPE, KVE, or PSAE. All changes are isolated to publication policy.

PPPE enforces 10 deterministic publishing rules on every rendered proposal before customer distribution.

---

## Architecture Position

```
Knowledge Platform (KRPE → KVE → ARE → RSE → PSAE)
              ↓
     Proposal Renderer (proposal_renderer.py)
              ↓
     PROPOSAL_RENDERED_[Tender].md  (V2)
              ↓
  Proposal Publishing Policy Engine (PPPE)
       proposal_publishing_policy.py
              ↓
  ┌───────────┬─────────────┬──────────────┐
  │ CUSTOMER  │  INTERNAL   │   REVIEW     │
  │ PROPOSAL  │   REVIEW    │   PROPOSAL   │
  └───────────┴─────────────┴──────────────┘
```

---

## The 10 Publishing Rules

### R1 — Remove Internal Governance Information

The following content is NEVER published to customers:

| Category | Examples |
|---|---|
| Governance subsections | "Appendix A — Extraction Notes", "Appendix B — Fact Verification Summary" |
| Approval records | Any subsection headed "Approval Record", "Approval History" |
| BU Decision sections | Any subsection headed "BU Lead Decisions — Applied" |
| Governance comment segs | Internal governance notes rendered as comments |
| Review notes | "Review Notes", "Internal Review" subsections |

**Implementation:** Governance subsections are detected by heading pattern match. All content within the subsection is excluded until the next same-or-higher-level heading.

### R2 — Strip Internal Identifiers

All internal system identifiers are removed from customer-facing output. Removal leaves surrounding text intact.

| Pattern | Examples |
|---|---|
| Oracle HCM module IDs | `HCM-ENV-001`, `HCM-WFL-004` |
| Registry asset IDs | `CAP-...`, `ASM-...`, `ASP-...` |
| BU decision IDs | `BU-WP11-001`, `BU-WP11-003` |
| Risk IDs | `RC-OPS-001`, `RC-DATA-004` |
| KVE/ADR IDs | `AV-011`, `ADR-002`, `IG-001` |
| Technical document IDs | `TD-014`, `KB-...`, `DOC-...` |
| Work package IDs | `WP18F`, `WP19D` |

**Implementation:** Regex pattern match with word-boundary anchors. Surrounding text preserved; orphaned punctuation cleaned up.

### R3 — Remove Implementation Annotations

Inline annotations indicating change history are stripped from all rendered text.

| Pattern | Example |
|---|---|
| Inline update annotation | `*(Updated — BU-WP11-002)*` |
| Revision notice | `*(Revised — WP18B)*` |

**Implementation:** Inline regex substitution applied to all text-bearing segments.

### R4 — Remove BU Decision Tables

Tables whose header row contains "BU Decision" or "BU Lead Decision" or "BU-WP" references are removed entirely from customer output.

**Implementation:** Table header row is checked before rendering. Entire table excluded if match found.

### R5 — Assumption Executive Summaries

Full assumption libraries (hundreds of individual assumptions with internal IDs) are replaced with executive summaries of 3–8 business-relevant bullets per pack.

| Section | Treatment |
|---|---|
| Key Assumptions (Body Section) | Replaced with executive summary per pack |
| Complete Assumption Schedule | Replaced with executive summary per pack (appendix) |
| Commercial Assumptions | Excluded (internal-only duplicate) |

**Implementation:** H3-level pack headings are detected within the section. An authored executive summary is generated for each pack using a library of pre-authored summaries per Oracle module. Full assumption detail remains in the INTERNAL_REVIEW_PACK.

### R6 — Oracle Methodology Correction (PERMANENT PLATFORM RULE)

> **For all Oracle Fusion Cloud proposals, Oracle Unified Method (OUM) and Oracle Unified Methodology are replaced with "Oracle's Modern Best Practices".**
>
> This rule applies to all Fusion Cloud products: Oracle HCM Cloud, Oracle ERP Cloud, Oracle Recruiting Cloud, Oracle Learning Cloud, Oracle Talent Management, Oracle Integration Cloud.
>
> OUM is only permitted in proposals for Oracle E-Business Suite (EBS) legacy engagements.

**Implementation:** Regex match for "Oracle Unified Method", "Oracle Unified Methodology", "OUM" (with context). Replacement: `Oracle's Modern Best Practices`.

### R7 — Roadmap Condensation

Project Plan / Timeline sections are subject to the same page budget as other sections. Detailed phase descriptions are available in the Internal Review Pack.

**Implementation:** Per-section budget cap (Rule 10) applied.

### R8 — Customer Next Steps

The "Commercials / Pricing" section renders customer-action-oriented content only. APPSolve internal tasks are excluded from the customer proposal via section ordering policy.

**Implementation:** Section ordering enforces customer perspective. APPSolve-internal action sections are excluded from `_CUSTOMER_ORDER`.

### R9 — Remove Source Evidence

Tables containing source evidence, traceability, or internal reference columns have those columns removed. Text references to source documents, evidence, or KB references are treated as internal content.

**Implementation:** Table header columns are checked against `_EVIDENCE_COLS` set. Matching columns (and their data rows) are stripped.

### R10 — Page Budget Enforcement (Target 25–35 Pages)

Per-section content segment budgets are enforced. When a section exceeds its budget, content is truncated and a cross-reference to the Internal Review Pack is added.

| Section | Budget (content segs) | Approx Pages |
|---|---|---|
| Executive Summary | 24 | 3 |
| Understanding of Requirements | 20 | 2.5 |
| Proposed Solution Overview | 16 | 2 |
| Company sections (each) | 12–16 | 1.5–2 |
| Implementation Methodology | 40 | 5 |
| Oracle HCM Capability | 56 | 7 |
| ERP / OIC Capability (each) | 32 | 4 |
| Project Governance | 24 | 3 |
| Risk Register | 20 | 2.5 |
| Assumption Schedule | 48 | 6 |

---

## Publication Profiles

| Profile | Description | File Naming |
|---|---|---|
| `PROFILE_CUSTOMER` | Policy-filtered proposal — customer distribution | `PPPE_CUSTOMER_[Tender].docx` |
| `PROFILE_INTERNAL` | Unfiltered content — all V2 sections | `PPPE_INTERNAL_[Tender].docx` |
| `PROFILE_REVIEW` | Customer content + policy annotations | `PPPE_REVIEW_[Tender].docx` |

---

## What Is Never Published to a Customer

| Category | Reason |
|---|---|
| Approval records, governance reviews | Internal QA process only |
| Pre-tender checklist results | Internal process only |
| Asset IDs, KB IDs, document IDs | Internal reference system |
| Source evidence / traceability tables | Internal audit only |
| AI-draft notes | Internal authoring state only |
| OUM references (for Fusion Cloud) | GOV-PAE-001 / R6 methodology rule |
| BU decision tables | Internal commercial decision records |
| Full assumption libraries with IDs | Replaced by executive summaries |
| Duplicate assumption sections | Only one version published |

---

## Integration with Prior Engines

PPPE reads the V2 rendered Markdown output from `proposal_renderer.py`. It does NOT modify or depend on:
- KRPE (`krpe.py`)
- KVE (`kve_engine.py`)
- ARE (`are.py`)
- RSE (`rse.py`)
- PSAE (`proposal_section_engine.py`)

PPPE is an independent policy layer that operates on the rendered output. It is complementary to PAE (which authors from scratch). Both engines read the same V2 source.
