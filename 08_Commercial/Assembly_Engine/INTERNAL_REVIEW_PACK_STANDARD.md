---
document_id: TD-022
title: Internal Review Pack Standard v1.0
version: "1.0"
status: APPROVED
date: "2026-06-30"
---

# Internal Review Pack Standard v1.0

## Purpose

The INTERNAL_REVIEW_PACK is the complete internal working document for every tender. It contains:
1. Everything that was authored for the Client Proposal (for review accuracy)
2. Everything that was NOT published to the client (full KB content, governance, traceability)
3. The pre-submission Action Register with owner and status

**Distribution: APPSolve INTERNAL USE ONLY. Never sent to clients.**

---

## Structure (INTERNAL_REVIEW_PACK_[TenderID].docx)

| Part | Content | Purpose |
|---|---|---|
| Internal Banner | Tender ID, date, platform version | Identify document |
| Action Register | All pre-submission actions, owners, status | QA checkpoint |
| Part 1 — Published to Client | All 11 authored sections (as sent to client) | Accuracy review |
| Part 2 — Not Published | All V2 KB sections, source evidence, full capability assets | Traceability |

---

## Action Register Contents

Every INTERNAL_REVIEW_PACK includes an Action Register covering:

| Priority | Action Type |
|---|---|
| P0 URGENT | B-BBEE certificate renewal (due 2026-07-31) |
| P1 | Executive Summary and Understanding sections (BU Lead / AM) |
| P1 | Scope confirmation from client (AM ownership) |
| P1 | Commercial Proposal (Commercial Director) |
| P2 | BU Lead review of all PAE-authored sections |
| P2 | Reference client approvals (AM) |
| P3 | Compliance document verification |

---

## What Part 2 Contains

Part 2 surfaces the full Knowledge Base content that was deliberately removed from the client proposal. This includes:

- **Oracle HCM/ERP/OIC capability assets** — complete feature detail, sub-module specs
- **Assumption schedules** — all assumptions with IDs, source, and status
- **Client references** — all reference data (named and anonymous)
- **Implementation methodology assets** — complete Oracle methodology documentation
- **Company profile assets** — full company history, headcount detail, geography
- **Governance records** — approval history, review states, asset IDs
- **AI-DRAFT and PLACEHOLDER sections** — with action callouts identifying pending work

---

## Review Protocol

Before a CLIENT_PROPOSAL is released:

1. BU Lead reads the Action Register — all P0/P1 items must be resolved
2. BU Lead reviews Part 1 (Published Sections) for factual accuracy
3. Account Manager reviews Next Steps and Reference claims
4. Commercial Director confirms no pricing is included in Part 1
5. P0: B-BBEE claim verified current

---

## Output File Naming

```
INTERNAL_REVIEW_PACK_[TenderID].docx
```

Examples:
- `INTERNAL_REVIEW_PACK_PLENNEGY-HCM-001.docx`

Produced by: `proposal_authoring_engine.py --tender [TenderID]`
