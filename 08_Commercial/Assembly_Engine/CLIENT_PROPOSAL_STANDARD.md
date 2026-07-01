---
document_id: TD-021
title: Client Proposal Standard v1.0
version: "1.0"
status: APPROVED
date: "2026-06-30"
---

# Client Proposal Standard v1.0

## Structure (CLIENT_PROPOSAL_[TenderID].docx)

| Section | Heading | Target Length | Content Type |
|---|---|---|---|
| 1 | Executive Summary | 2 pages | BU Lead authored — win theme, positioning |
| 2 | Understanding of [Client]'s Requirements | 2 pages | AM authored — context, pain points |
| 3 | The Solution We Propose | 1–2 pages | PAE authored — scope table |
| 4 | Why APPSolve | 2–3 pages | PAE authored — credentials |
| 5 | How We Deliver | 3–4 pages | PAE authored — Oracle Modern Best Practices |
| 6 | What We Deliver for You | 4–6 pages | PAE authored — capability narrative |
| 7 | Project Governance | 2 pages | PAE authored — governance framework |
| 8 | Your Implementation Roadmap | 2 pages | PAE authored — phase timeline |
| 9 | Key Assumptions | 2 pages | PAE authored — category summary |
| 10 | Commercial | 1 page | PAE authored — inputs required |
| 11 | Your Next Steps | 1 page | PAE authored — client actions ONLY |
| App A | Assumption Schedule | ≤15 pages | KB assets — extracted by PAE |
| App B | Reference Summary | ≤3 pages | AM authored — anonymous summaries |

**Total target: 25–40 pages**

---

## What Never Appears in a Client Proposal

The following content categories are **permanently excluded** from CLIENT_PROPOSAL output:

| Category | Reason |
|---|---|
| Approval records and governance review notes | Internal process only |
| Pre-tender checklist results | Internal process only |
| Asset IDs (KB-xxx, CAP-xxx, DOC-xxx) | Internal reference system |
| Source evidence tables / Primary Source Evidence columns | Internal traceability only |
| Fact verification notes | Internal QA only |
| AI drafting notes or AI-Draft sentinel text | Internal authoring state only |
| Assumption IDs (ASM-xxx) | Internal reference |
| Oracle partnership tier: "Oracle Gold Partner" | Expired August 2021 — prohibited |
| Internal action callouts or TODO markers | Internal review pack only |
| BU Lead review comments or editorial notes | Internal review pack only |
| Named references (DFA, CCBA, SAA, Redpath Mining, Hollywood Bets) | See GOV-PAE-002 through 004 |
| BEE Level 3 claim after 2026-07-31 | Compliance risk — renewal required |

---

## Language Requirements

| Requirement | Rule |
|---|---|
| **Storytelling** | Introduce → Explain → Reassure → Close (for each major section) |
| **Perspective** | Write from the client's perspective — "you" and "your" preferred to "we" |
| **Oracle methodology** | Always "Oracle's Modern Best Practices" / "Oracle Success Navigator" for Fusion Cloud |
| **Section flow** | Each section opens with a single orienting paragraph before bullets or tables |
| **Bullet use** | Bullet lists supplement narrative — not replace it. No section is only bullets. |
| **Table language** | Tables carry facts; prose carries context. Both must be present for complex sections. |

---

## Output File Naming

```
CLIENT_PROPOSAL_[TenderID].docx
```

Examples:
- `CLIENT_PROPOSAL_PLENNEGY-HCM-001.docx`
- `CLIENT_PROPOSAL_CBHM-ERP-002.docx`

Produced by: `proposal_authoring_engine.py --tender [TenderID]`
