---
created: "2026-06-10"
created_by: "Claude (AI — Wave 2 candidate decision record)"
status: "Awaiting BU lead decisions"
---

# Wave 2 Candidate Decisions
**Date:** 2026-06-10 | **Owner:** Hein Blignaut | **Purpose:** Decision record for the two remaining Acumatica STRUCTURE ONLY candidate files

These are the only two unresolved Acumatica candidates following the archival of W1S2-008 (Construction Edition). Both require a BU lead decision before any work can proceed. Neither is blocking Wave 2 Oracle extractions.

---

## W1S2-006 — Acumatica Field Services Edition

### Current Status

`STRUCTURE ONLY — Candidate`

File: `07_Approved_Content/Candidate_Content/Acumatica/W1S2-006-ACU-FieldServices-DRAFT.md`

Created 2026-06-08. No source content found in Wave 1. File contains structure template only — the capability description has not been authored.

The only Field Services content found in Wave 1 sources is a single one-line overview entry present in both the Acumatica Sept 2025 template and HyDac V5.1:
> *"Maintain a real-time view of customer activities across all your operations when field service operations are fully integrated with the back office."*

This is not sufficient for tender use.

### Business Value

**Moderate if confirmed, zero if not.**

Acumatica Field Services Edition addresses companies that dispatch technicians to client sites — HVAC contractors, electrical service companies, facilities management, medical equipment servicing, utilities field operations. If APPSolve actively serves or is targeting this market, an approved capability statement would be directly citeable in RFP responses.

APPSolve's confirmed Acumatica target industries (Manufacturing, Distribution, FMCG, Professional Services, Higher Education) do not currently include Field Services. The DRAFT file suggests ACSA and Air Products as potential corpus candidates, but this search has not been done.

### Evidence Available

- One-line product description from two proposal templates
- No submitted proposals for field-service clients found
- No corpus search of `Parties/Customers/[Client]/RFP/` for field-service scope has been performed

### Decision Required

BU lead must confirm whether Acumatica Field Services Edition is an active APPSolve product offering before any work is done.

### Exact BU Lead Question

> "Is Acumatica Field Services Edition a product that APPSolve currently sells and implements in South Africa? If yes, do we have any proposals submitted to field-service clients (e.g. ACSA, Air Products, or similar) where Field Services content appears?"

Expected answer options:
- **Yes, active offering, corpus proposals exist** → Search corpus, extract content, advance W1S2-006 as Wave 2 or Wave 3 item
- **Yes, active offering, no corpus proposals** → Author from Acumatica partner portal materials; medium effort; Wave 3
- **No, not currently offered** → Archive W1S2-006 (same as W1S2-008)

### Recommended Action

**Defer** — pending the BU lead answer above. Do not search the corpus or author content until confirmed.

If the answer is "Yes, active, corpus exists," elevate to Wave 2 and conduct corpus search before authoring. If "Not currently offered," archive immediately with the same rationale as W1S2-008.

### Reopen Criteria

- BU lead confirms Field Services is an active APPSolve offering, OR
- A Field Services tender RFP is received and the gap becomes a live blocker

---

## W1S2-007 — Acumatica Payroll Integration

### Current Status

`STRUCTURE ONLY — Candidate`

File: `07_Approved_Content/Candidate_Content/Acumatica/W1S2-007-ACU-Payroll-DRAFT.md`

Created 2026-06-08. No source content found in Wave 1. File contains structure template only.

**Critical governance constraint:** Critical Repository Rule 3 permanently prohibits implying Acumatica native payroll capability in South Africa: *"Acumatica does not provide payroll functionality in South Africa."* This file cannot be advanced as a native "Acumatica Payroll" document.

**However:** A reframed *"Acumatica Payroll Integration"* capability statement — describing how Acumatica integrates with South African payroll providers — would be both accurate and useful. SA payroll integration is a common tender requirement. The question is whether APPSolve has an established integration approach and which SA payroll systems are supported.

### Business Value

**High if reframed — medium if original framing retained (which it cannot be).**

Most South African organisations running Acumatica will have a separate payroll system (VIP Payroll, Sage Payroll, PaySpace, Pastel Payroll, or similar). A clear statement of how Acumatica integrates with these systems — including integration method, data flow (cost centre / GL journal), and supported vendors — is a credible tender differentiator and directly addresses a common evaluator question.

A document reframed as "Acumatica Payroll Integration" carries more business value than no document, provided it is accurate.

### Evidence Available

- No source content in Wave 1 (SITA v1.06 is BeBanking-only; Acumatica templates do not include SA payroll integration)
- APPSolve's BeBanking offering includes Payroll H2H (Oracle EBS and Fusion only) — but this is not Acumatica payroll
- The DRAFT file notes: *"APPSolve's Acumatica proposals reviewed do not include a standard Payroll module description"*

### Decision Required

BU lead must answer two questions before this file can be progressed or archived.

### Exact BU Lead Questions

> **Question 1:** "For Acumatica clients, what payroll system approach does APPSolve typically recommend or implement? For example: VIP Payroll, Sage Payroll, PaySpace, or another system?"

> **Question 2:** "How does the Acumatica implementation connect to the payroll system — is there a direct API integration, a flat-file/extract import, or a manual GL journal entry process? Is this integration included in APPSolve's standard Acumatica delivery scope?"

Expected answer options:
- **APPSolve has a standard payroll integration approach** → Author "Acumatica Payroll Integration" document from BU lead description; this is valuable Wave 2 content
- **APPSolve leaves payroll to the client / not in scope** → Archive W1S2-007; note the gap but do not author speculative content
- **APPSolve uses BeBanking Payroll H2H alongside Acumatica** → This is already documented in W1S3-004; W1S2-007 would note the dependency but not duplicate it

### Recommended Action

**Defer with condition.** Do not archive yet — unlike W1S2-008 (no evidence, no market), this file has a plausible path forward as a payroll integration document. But it cannot be authored without BU lead direction on which integrations APPSolve actually delivers.

If the BU lead confirms an integration approach, update the file title, description, and scope to "Acumatica Payroll Integration" and advance as Wave 2 authoring. If no integration is offered, archive.

### Reopen Criteria

- BU lead confirms APPSolve has a standard SA payroll integration approach for Acumatica clients, OR
- An Acumatica tender RFP specifically asks about payroll integration capability

---

## Summary

| File | Current status | Decision needed | Recommended next step |
|---|---|---|---|
| W1S2-006 Field Services | STRUCTURE ONLY — Candidate | Is Field Services an active APPSolve Acumatica offering? | Defer; BU lead Q&A first |
| W1S2-007 Payroll Integration | STRUCTURE ONLY — Candidate (scope reframe required) | What SA payroll integration does APPSolve deliver with Acumatica? | Defer with condition; Q&A before archiving or advancing |
| W1S2-008 Construction | **Archived 2026-06-10** | — | No further action unless reopened |

**Neither file is blocking Wave 2 Oracle extraction work.** The BU lead Q&A can be conducted at any time and does not require a dedicated AI session — it is a 10-minute conversation with Hein Blignaut that yields the inputs needed to advance or archive both files.

---

*Created 2026-06-10 by Claude (AI) on instruction from Hein Blignaut.*
