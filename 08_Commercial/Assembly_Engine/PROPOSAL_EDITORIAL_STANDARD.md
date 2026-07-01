---
document_id: PEE-STANDARD-V1
title: "Proposal Editorial Standard v1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-30"
created_by: "PF2-008 — Proposal Editorial Engine"
---

# Proposal Editorial Standard v1.0

Defines the editorial principles, proposal structure, and quality standards applied by the Proposal Editorial Engine (PEE) and expected of all APPSolve client proposals.

---

## 1. Purpose

This standard governs:
- How the Proposal Editorial Engine (PEE) transforms assembled content into client-ready proposals
- What must and must not appear in each publication profile
- The structure and page budget of a standard APPSolve consulting proposal
- Editorial principles for customer language and tone

---

## 2. Core Editorial Principles

### 2.1 Source Material vs Proposal Content

All Knowledge Base assets (Capability Assets, Assumption Packs, Risk Registers, Methodology Assets) are **source material**.

They are not proposal sections.

Before any KB asset is published, the PEE must classify it:

| Classification | Description | V4 Destination |
|---|---|---|
| Publish in body | Key narrative summary suitable for client reading | Body section (concise) |
| Summarise in body | Too detailed for body; key points extracted | Body section (authored summary) |
| Move to appendix | Reference material — appropriate for appendix | Appendix (full or budgeted) |
| Internal review only | Governance/evidence content — no client value | INTERNAL WORKBOOK only |
| Traceability only | Source mapping / audit trail | TRACEABILITY REPORT only |

### 2.2 The Proposal Must Read Like a Proposal

The CLIENT proposal must read as if written by an experienced APPSolve Bid Manager who understands the client's context, not as a Knowledge Base export.

Specifically:
- Sections must flow logically from client need → solution → delivery → commitment
- Each section must have a clear client-facing purpose
- Capability evidence must serve the proposal argument, not just assert itself
- Internal governance language must be completely absent

### 2.3 Conciseness Over Completeness

If a section exceeds its page budget, the PEE summarises.

It does not continue publishing source material beyond the budget.

Full detail belongs in appendices, not the proposal body.

### 2.4 Customer Language

All proposal body text must be customer-facing.

| Prohibited | Replace With |
|---|---|
| "APPSolve account manager to confirm" | "Details available on request" |
| "OAR-C04 action pending" | (omit — internal only) |
| "BU Lead review required" | (omit — internal only) |
| "Governed under ASSUMPTION_GOVERNANCE" | (omit entirely) |
| "See Internal Review Workbook" | (omit — CLIENT has no review workbook) |
| "AI-generated content" | (omit or replace with pending notice) |
| "PLACEHOLDER" | (replace with neutral pending notice) |

---

## 3. Standard V4 Proposal Structure

### 3.1 Body Sections (11)

| # | Section | Purpose | Page Budget |
|---|---|---|---|
| 1 | Executive Summary | Win theme; why APPSolve is the right partner for this engagement | 2 pages |
| 2 | Understanding Requirements | Demonstrate understanding of client's specific context and challenge | 2 pages |
| 3 | Proposed Oracle HCM Solution | Specific scope proposed; what is and is not included | 6–8 pages |
| 4 | Why APPSolve | Credentials, track record, Oracle partnership, awards | 3 pages |
| 5 | Delivery Approach | How APPSolve will deliver; methodology phases | 5 pages |
| 6 | Project Governance | Governance framework; decision-making; reporting | 3 pages |
| 7 | Implementation Roadmap | Phase timeline; key milestones; indicative durations | 3 pages |
| 8 | Key Assumptions | Commercially material assumptions; cross-reference to App C | 2 pages |
| 9 | Key Project Risks | Top 5 project risks with mitigations | 2 pages |
| 10 | Commercial Inputs | Commercial model; inputs required before pricing | 2 pages |
| 11 | Next Steps (Customer Actions) | Clear action list for client before proposal progresses | 1 page |

**Total target: 35–45 pages excluding appendices.**

### 3.2 Appendices (5)

| App | Title | Content | Page Budget |
|---|---|---|---|
| A | Oracle HCM Capability Summary | 2-table authored summary: delivery tier + commitments | 3 pages |
| B | Detailed Capability Catalogue | Full Oracle HCM, ERP, OIC capability from KB assets | up to 12 pages |
| C | Assumption Schedule | Complete assumption register for this engagement scope | up to 15 pages |
| D | Reference Projects | Anonymous concise reference summaries (AM approval required for named) | 6 pages |
| E | Glossary | Key terms: Oracle HCM, project management, APPSolve methodology | 2 pages |

---

## 4. Publication Profiles

### 4.1 CLIENT V4

**Audience:** Client evaluation team, procurement, executive sponsor  
**Purpose:** Persuade. Win the engagement.  
**Rules:** Apply all CF, BP, DD, BG, AU editorial rules. No internal content. No governance metadata. No AI markers. No source IDs.

### 4.2 INTERNAL REVIEW V4

**Audience:** APPSolve BU Lead, Account Manager, Delivery Manager, Commercial Director  
**Purpose:** Track what needs to be completed before submission.  
**Additional content:** Action register, editorial summary table, section status badges, editorial decision notes, action callouts for PLACEHOLDER and AI_DRAFT sections.

### 4.3 TRACEABILITY REPORT V4

**Audience:** APPSolve governance; future audit  
**Purpose:** Record editorial decisions, segment counts, budget compliance, V3→V4 transformation log.  
**Content:** Section-by-section editorial record (mode, budget, segs removed, segs authored).

---

## 5. Section Assembly Modes

| Mode | Description | CLIENT Behaviour |
|---|---|---|
| `authored` | PEE-authored Seg list — does not come from V3 | Render authored content directly |
| `budgeted` | V3 section → CF + BP + DD + BG pipeline | Render filtered/truncated content; pending notice if PLACEHOLDER/AI_DRAFT |
| `passthrough` | V3 section passed without budget enforcement | Render as-is after CF filter |

---

## 6. Editorial Quality Criteria

A V4 CLIENT proposal meets standard when all of the following are true:

| Criterion | Standard |
|---|---|
| Structure | 11 body sections + appendices A–E, correctly numbered |
| Page budget | Body sections within stated budgets; appendices within limits |
| No internal content | Zero governance metadata, AI markers, source IDs, engine metadata in CLIENT |
| No boilerplate | Zero Oracle marketing boilerplate paragraphs in body |
| No duplication | No repeated paragraphs across sections |
| Customer language | No internal operational language in any CLIENT section |
| Pending sections | Pending sections show neutral professional notice (not "PLACEHOLDER") |
| Authored sections | Authored content reviewed by BU Lead before submission |
| Governance compliance | All 12 PR (Publication) rules pass |
| B-BBEE | Not cited after 2026-07-31 unless renewal cert confirmed |

---

## 7. Human Review Requirements

The following authored sections must be reviewed by BU Lead before any V4 CLIENT is submitted:

| Section | Review Requirement |
|---|---|
| Sec 3: Proposed Oracle HCM Solution | Confirm scope accuracy, entity count, module list |
| Sec 7: Implementation Roadmap | Confirm indicative timelines appropriate for this engagement |
| Sec 9: Key Project Risks | Confirm top-5 risks are appropriate; adjust for client context |
| App A: HCM Capability Summary | Confirm delivery tier claims are accurate |
| App D: Reference Projects | Confirm reference approval status (OAR-C01 for Hollywood Bets) |

---

## 8. Relationship to Platform Architecture

```
Knowledge Platform (V1.0)
  └─ KRPE → KVE → ARE → RSE → PSAE → Renderer
                                         │
                                    V2 Markdown
                                         │
                               ppe.py (Publication)
                                         │
                               V2 DOCX (CLIENT/INTERNAL/TRACEABILITY)
                                         │
                             proposal_shaper.py (V3 Shaping)
                                         │
                               V3 DOCX (CLIENT/INTERNAL/TRACEABILITY)
                                         │
                                pee.py (V4 Editorial)
                                         │
                               V4 DOCX (CLIENT/INTERNAL/TRACEABILITY)
```

The PEE is the final editorial layer. It does not modify Knowledge Base assets. It applies editorial classification to V3 content and produces publication-ready V4 outputs.

---

*PROPOSAL_EDITORIAL_STANDARD.md v1.0 — PF2-008 Proposal Editorial Engine | 2026-06-30*
