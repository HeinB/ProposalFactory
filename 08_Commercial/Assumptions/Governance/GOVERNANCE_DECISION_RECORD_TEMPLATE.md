---
title: Governance Decision Record Template
version: v1.0
status: Template
programme: WP13 Governance Approval Campaign
date: 2026-06-16
---

# Governance Decision Record Template

**Programme:** WP13 | **Template version:** v1.0 | **Date:** 2026-06-16

> **Usage:** Copy this template for each BU decision resolved during governance workshops or asynchronous approvals. Save completed records as `DR_<ID>.md` in this folder (e.g., `DR_BU-ACU-001.md`). Do not modify this template file.

---

## How to Use This Template

1. Copy the full template below into a new file named `DR_<Decision-ID>.md`
2. Complete all fields — leave none blank; use "N/A" where genuinely not applicable
3. Obtain BU Lead signature (or email confirmation reference) before marking status as Approved
4. Once signed off, notify AI to implement the decision in the relevant assumption pack

---

```markdown
---
decision_id: BU-XXX-000
pack: [ACU | BB | REC | LRN | TLT | COM | OCI]
decision_title: [Short descriptive title]
priority: [CRITICAL | HIGH | MEDIUM | LOW]
status: [Draft | Under Review | Approved | Withdrawn]
approved_by:
approval_date:
implementation_status: [Not Started | In Progress | Complete]
---

# Decision Record: BU-XXX-000 — [Decision Title]

## 1. Context

**Pack:** [Pack name and code]
**Assumption(s) affected:** [List affected assumption IDs, e.g. ACU-GEN-001, ACU-GEN-002]
**Current wording in pack:**

> [Paste the exact current text of the assumption or policy being decided]

**Why this decision is required:**

[Explain what is ambiguous, undefined, or commercially sensitive about the current wording. Why does this need BU Lead resolution rather than a default?]

---

## 2. Options Considered

| Option | Description | Commercial Implication | Recommended? |
|---|---|---|---|
| (a) | [Option text] | [Implication] | [Yes / No] |
| (b) | [Option text] | [Implication] | [Yes / No] |
| (c) | [Option text] | [Implication] | [Yes / No] |

**Recommended option:** [State the AI or pre-sales recommendation and brief rationale]

---

## 3. Decision

**Approved option:** [State which option was selected — e.g. "(a)"]

**Approved wording (for implementation in assumption pack):**

> [Paste the exact approved text that should replace or supplement the current pack wording]

**Decision rationale:**

[Why was this option chosen? Reference any commercial constraints, policy alignment, or market factors that informed the decision.]

---

## 4. Governance

**Decision owner:** [Name and role of the person who made the final call]

**Approval method:** [Workshop / Asynchronous email / Call]

**Workshop / call reference:** [Date, attendees, or email subject line + date for async approvals]

**Approval date:** [YYYY-MM-DD]

**Approved by:** [Full name — BU Lead or Commercial Director as required by delegation map]

**Secondary approval (if required):** [Name — Commercial Director sign-off, if applicable]

---

## 5. Implementation

**Implementation required:** [Yes / No]

**Files to update:**

| File | Change Required |
|---|---|
| [e.g. ACU_BASE_ASSUMPTIONS_V1.md] | [e.g. Update ACU-GEN-001 text; update pack frontmatter] |
| [e.g. ACU_ASSUMPTION_REGISTER.csv] | [e.g. Update row ACU-GEN-001 status and notes fields] |

**Implementation owner:** AI (next work package)

**Implementation status:** Not Started

**Implementation completed:** [Date when AI confirms changes applied — fill in after implementation]

---

## 6. Follow-up Actions

| Action | Owner | Due Date | Status |
|---|---|---|---|
| [e.g. Update Velixo ISV list in Appendix A] | [AI / BU Lead / Commercial] | [Date] | [Open / Complete] |
| [e.g. Align BU-BB-009 POPIA wording to match this decision] | AI | [Date of next BB workshop] | Open |

**Cross-pack impacts:** [Note if this decision affects another pack — e.g. BU-ACU-008 answer feeds into BU-BB-004]

---

## 7. Risk if Deferred (original assessment)

**Priority:** [CRITICAL / HIGH / MEDIUM / LOW]

**Original risk statement:**

> [Paste the risk-if-deferred statement from GOVERNANCE_MASTER_DECISION_REGISTER.md]

**Risk resolved:** [Yes — decision taken / Partially — follow-up actions open / No — decision deferred]

---

*Decision Record | [Decision ID] | [Pack] | Approved: [Date] | BU Lead: [Name]*
```

---

## Naming Convention for Completed Records

| Pack | File naming pattern | Example |
|---|---|---|
| Acumatica | `DR_BU-ACU-001.md` through `DR_BU-ACU-015.md` | `DR_BU-ACU-009.md` |
| BeBanking | `DR_BU-BB-001.md` through `DR_BU-BB-010.md` | `DR_BU-BB-006.md` |
| Oracle Recruiting | `DR_BU-REC-001.md` through `DR_BU-REC-007.md` | `DR_BU-REC-005.md` |
| Oracle Learning | `DR_BU-LRN-001.md` through `DR_BU-LRN-005.md` | `DR_BU-LRN-002.md` |
| Oracle Talent | `DR_BU-TLT-001.md` through `DR_BU-TLT-004.md` | `DR_BU-TLT-002.md` |
| Oracle Compensation | `DR_BU-COM-001.md` through `DR_BU-COM-005.md` | `DR_BU-COM-004.md` |
| OCI | Not required — all decisions resolved in WP11H-A | — |

---

## Governance Constraints for Decision Records

The following constraints apply to all decision records in this programme. These cannot be overridden by any BU decision:

| Constraint | Source | Scope |
|---|---|---|
| BeBanking Acumatica payroll integration permanently prohibited | Programme Rule | BU-BB-008 cannot reopen this — even if BeBanking payroll sources are expanded, Acumatica remains excluded |
| No direct SWIFT membership claim | Programme Rule | BU-BB decisions on cross-border payments must not imply APPSolve holds direct SWIFT access |
| Oracle partner tier: Level 1 only | Programme Rule | BU-ACU-009 can confirm Acumatica Gold Partner; no decision can upgrade Oracle from Level 1 |
| `approved_for_reuse` flag set by BU Lead only | System Rule | AI sets `implementation_status` only — never `approved_for_reuse` |
| Assumption status `Approved` requires BU Lead sign-off | System Rule | AI cannot unilaterally promote pack status |

---

*Governance Decision Record Template v1.0 | WP13 | 2026-06-16*
