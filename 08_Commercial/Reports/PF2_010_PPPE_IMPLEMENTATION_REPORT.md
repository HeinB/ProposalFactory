---
document_id: PF2-010-IMPL-REPORT
title: PF2-010 Proposal Publishing Policy Engine — Implementation Report
work_package: PF2-010 (PPPE v1.0)
engine: proposal_publishing_policy.py
status: COMPLETE
date: "2026-06-30"
platform_before: L6.2
platform_after: L6.3
---

# PF2-010 — Proposal Publishing Policy Engine Implementation Report

## Summary

The Proposal Publishing Policy Engine (PPPE) is the policy enforcement layer between the Renderer and customer DOCX output. It sits between `proposal_renderer.py` (V2 source) and the DOCX generator, applying 10 deterministic publishing rules before any content reaches a customer.

This is an architectural enhancement — not a cosmetic change. PPPE owns the decision of what a customer is allowed to see.

---

## Architecture

```
proposal_renderer.py → PROPOSAL_RENDERED_[Tender].md (V2)
          ↓
proposal_publishing_policy.py (PPPE)
          ↓
  ┌─────────────┬────────────────┬──────────────┐
  │ CUSTOMER    │ INTERNAL       │ REVIEW       │
  │ 94 KB       │ 421 KB         │ 93 KB        │
  │ 33 sections │ 41 V2 sections │ Policy-ann.  │
  └─────────────┴────────────────┴──────────────┘
          +
  PPPE_POLICY_REPORT_[Tender].md
```

PPPE does NOT modify KRPE, KVE, ARE, RSE, PSAE, or any Knowledge Asset.

---

## Rules Applied — Plennegy-HCM-001 Results

| Rule | Description | Plennegy Result |
|---|---|---|
| R1 | Governance subsections removed | 64 subsections |
| R2 | Internal IDs stripped | 5 IDs (non-assumption sections; assumption IDs removed via R5) |
| R3 | Inline annotations removed | 0 (annotations in assumption sections — removed by R5) |
| R4 | BU decision tables removed | 0 (BU decision tables within assumption subsections — removed by R1/R5) |
| R5 | Assumption packs summarized | 10 packs (5 from body + 5 from appendix) |
| R6 | OUM → Oracle's Modern Best Practices | **48 replacements** |
| R7 | Roadmap condensed | Applied via R10 budget |
| R8 | Customer next steps | Enforced via section ordering |
| R9 | Evidence columns stripped | Applied per table |
| R10 | Page budget enforced | Per-section caps applied |

---

## Rule 6 Detail — OUM Replacement

OUM appeared 48 times in the rendered Plennegy proposal across:
- Implementation Methodology (phase table, method description)
- Oracle HCM Capability section (per-module delivery descriptions)
- Oracle ERP Capability section
- Oracle OIC / Integration Capability section
- Team Structure (role descriptions citing OUM governance)

All 48 occurrences replaced with "Oracle's Modern Best Practices". This enforces GOV-PAE-001 across the KB-sourced content, not just the PAE-authored content.

---

## Rule 5 Detail — Assumption Pack Summaries

The rendered Plennegy proposal contained 3 full assumption library sections (1,487 total segments). PPPE replaced these with 10 executive summaries (5 packs × 2 sections):

| Pack | Section(s) | Summary Bullets |
|---|---|---|
| Oracle HCM Core | Body + Appendix | 6 bullets each |
| Oracle Recruiting Cloud | Body + Appendix | 5 bullets each |
| Oracle Learning Cloud | Body + Appendix | 6 bullets each |
| Oracle Talent Management | Body + Appendix | 4 bullets each |
| Oracle Integration Cloud | Body + Appendix | 6 bullets each |

The "Commercial Assumptions" section (third duplicate) is excluded entirely from customer output.

---

## Outputs (Plennegy-HCM-001)

| File | Size | Description |
|---|---|---|
| `PPPE_CUSTOMER_PLENNEGY.docx` | 94 KB | 33-section customer proposal; 48 OUM fixes; 10 assumption summaries |
| `PPPE_INTERNAL_PLENNEGY.docx` | 421 KB | Unfiltered 41-section internal review pack |
| `PPPE_REVIEW_PLENNEGY.docx` | 93 KB | Customer content + policy annotations |
| `PPPE_POLICY_REPORT_PLENNEGY.md` | 2 KB | Governance audit of rules applied |

---

## Architecture Documents Delivered

| Document | ID | Description |
|---|---|---|
| `PROPOSAL_PUBLISHING_STANDARD.md` | TD-023 | 10 rules spec + integration architecture |
| `CUSTOMER_PROPOSAL_POLICY.md` | TD-024 | What goes in / never in a customer proposal |
| `INTERNAL_REVIEW_POLICY.md` | TD-025 | Internal review pack governance |

---

## Regression Results

| Engine | Status | Notes |
|---|---|---|
| `proposal_renderer.py` | PASS | RENDERED=21 PH=18 AI=3 NOT_FOUND=0 |
| `pee.py` (PEE) | PASS | CLIENT=94KB INTERNAL=97KB unchanged |
| `proposal_authoring_engine.py` (PAE) | PASS | CLIENT=61KB INTERNAL=431KB unchanged |
| `proposal_publishing_policy.py` (PPPE) | NEW | 4 outputs, 48 OUM fixes, 10 packs summarized |

**Total regression violations: 0**

---

## Relationship to PAE

PPPE and PAE are complementary engines reading the same V2 source:

| Dimension | PAE | PPPE |
|---|---|---|
| Approach | Authors from scratch (ignores KB content) | Filters/cleans rendered KB content |
| OUM coverage | Authored sections only | All 48 occurrences across all KB-sourced sections |
| Assumption handling | Authored summaries | Authored summaries (same quality) |
| KB fidelity | Low (fully rewritten) | High (KB content preserved and cleaned) |
| Use case | Final client submission | Policy-validated KB-faithful version |

---

## Platform Maturity

| Before | After |
|---|---|
| L6.2 | **L6.3** |

Platform L6.3: PPPE operational. 10-rule policy enforcement. 48 OUM occurrences corrected in rendered KB content. Assumption libraries replaced with executive summaries. Full Proposal Factory pipeline with two distinct publication paths (PAE authored / PPPE filtered).
