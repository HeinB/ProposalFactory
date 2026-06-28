---
document_id: ASSEMBLY-RULES-ENGINE
title: "Assembly Rules Engine"
version: "1.0"
created: "2026-06-16"
created_by: "WP12 — Proposal Assembly Engine"
status: "Active"
---

# Assembly Rules Engine

**Purpose:** Deterministic IF/THEN rules that govern proposal assembly. Apply all rules before producing a proposal draft. Rules are hierarchical — BLOCK rules override all others.

**Rule types:**
- `INCLUDE` — add this asset to the assembly
- `EXCLUDE` — remove this asset or section
- `REQUIRE` — a gate that must be cleared before proceeding
- `FLAG` — not a blocker, but must be noted in the proposal or tracked in the action register
- `BLOCK` — stops submission until resolved

---

## A. Capability Inclusion Rules

### A1 — Oracle HCM

| Condition | Rule | Asset |
|---|---|---|
| IF Oracle HCM in scope (any module) | INCLUDE | W1S1-003, W2S1-005, W3S1-001 |
| IF Absence Management in scope | INCLUDE | W3S1-007 |
| IF Journeys / Onboarding in scope | INCLUDE | W4-HCM-002 |
| IF AI Skills / Dynamic Skills in scope | INCLUDE | W4-AI-002 |
| IF Recruiting Cloud in scope | INCLUDE | W3S1-003 |
| IF Learning Cloud in scope | INCLUDE | W3S1-004 |
| IF Talent Management in scope | INCLUDE | W3S1-002 |
| IF Workforce Compensation in scope AND sector = Mining | INCLUDE | W3S1-005 |
| IF Workforce Compensation in scope AND sector ≠ Mining | BLOCK | W3S1-005 — raise G-001 conflict to BU Lead |
| IF HR Help Desk in scope | INCLUDE | W3S1-008 (with Section 14.2 suppression — see Rule G4) |
| IF Payroll Interface in scope (PaySpace or other) | INCLUDE | W3S1-009 (with Section 13.2 suppression — see Rule G5) AND W4-INT-001 |
| IF Analytics / reporting is a primary stated requirement | INCLUDE | W3S1-006 |
| IF OIC integrations in scope (not covered by Payroll Interface) | INCLUDE | W4-INT-001 |

### A2 — Oracle ERP

| Condition | Rule | Asset |
|---|---|---|
| IF Oracle Fusion Financials in scope | INCLUDE | W4-ERP-001, W2S1-001, W2S1-005 |
| IF Oracle Fusion Procurement in scope | INCLUDE | W4-ERP-002, W2S1-001 |
| IF Oracle PPM in scope | INCLUDE | W4-ERP-003, W2S1-001 |
| IF Oracle EBS in scope | INCLUDE | W2S1-002, W2S1-005 |
| IF Oracle DBA in scope | INCLUDE | W2S1-003 |
| IF Oracle Managed Services (non-AMS) in scope | INCLUDE | W2S1-004 |

### A3 — Acumatica

| Condition | Rule | Asset |
|---|---|---|
| IF Acumatica in scope (any module) | INCLUDE | W1S1-004, W5-METH-001, W1S1-007 |
| IF Acumatica Financials in scope | INCLUDE | W1S2-001 |
| IF Acumatica Distribution in scope | INCLUDE | W1S2-002 |
| IF Acumatica Inventory in scope | INCLUDE | W1S2-003 |
| IF Acumatica Manufacturing in scope | INCLUDE | W1S2-004 |
| IF Acumatica CRM in scope | INCLUDE | W1S2-005 |
| IF Acumatica Field Services in scope | INCLUDE | W1S2-006 |
| IF Acumatica PaySpace integration in scope | INCLUDE | W1S2-007 |
| IF Acumatica Project Accounting in scope | INCLUDE | W1S2-009 |
| IF Acumatica AMS in scope | INCLUDE | W5-ACU-001 |

### A4 — BeBanking

| Condition | Rule | Asset |
|---|---|---|
| IF BeBanking in scope (any service) | INCLUDE | W1S1-005, W1S3-001, W1S3-002, W1S3-008 |
| IF Supplier Payments in scope | INCLUDE | W1S3-003 |
| IF Payroll Payments in scope | INCLUDE | W1S3-004 |
| IF Forex in scope | INCLUDE | W1S3-005 |
| IF ERP Integration in scope | INCLUDE | W1S3-006 |
| IF Security architecture required | INCLUDE | W1S3-007 |
| IF Hosting model detail required | INCLUDE | W1S3-009 |
| IF Monitoring/automation detail required | INCLUDE | W1S3-010 |

### A5 — AMS and Cross-BU

| Condition | Rule | Asset |
|---|---|---|
| IF Oracle AMS in scope | INCLUDE | W2S1-004, AMS_ASSUMPTIONS_V1.md |
| IF Acumatica AMS in scope | INCLUDE | W5-ACU-001, AMS_ASSUMPTIONS_V1.md |
| IF multi-platform proposal (Oracle + Acumatica, or Oracle + BeBanking) | SWAP W2S1-005 → W5-METH-001 | Use platform-agnostic methodology |
| IF Oracle-only proposal AND W5-METH-001 was selected | SWAP W5-METH-001 → W2S1-005 | Use Oracle-specific methodology |

### A6 — Corporate Block

| Condition | Rule | Asset |
|---|---|---|
| ALL proposals | INCLUDE | W1S1-001, W1S1-007, W1S1-008, W1S1-009 |

---

## B. Assumption Pack Inclusion Rules

| Condition | Rule | Pack |
|---|---|---|
| IF Oracle HCM in scope | INCLUDE | HCM_BASE_ASSUMPTIONS_V1.md (Approved — mandatory) |
| IF Recruiting in scope | FLAG | HCM Recruiting pack is Draft (7 BU items pending) — note "subject to final approval" if referenced |
| IF Learning in scope | FLAG | HCM Learning pack is Draft (5 BU items pending) |
| IF Talent in scope | FLAG | HCM Talent pack is Draft (4 BU items pending) |
| IF Compensation in scope | FLAG | HCM Compensation pack is Draft (5 BU items pending) |
| IF OIC integrations in scope | INCLUDE | OIC_ASSUMPTIONS_V1.md (Approved) |
| IF Oracle ERP or EBS in scope | INCLUDE | ERP_ASSUMPTIONS_V1.md (Approved) |
| IF AMS in scope | INCLUDE | AMS_ASSUMPTIONS_V1.md (Approved) |
| IF Acumatica in scope | FLAG | Acumatica Base pack NOT YET CREATED — include flag in proposal: "Detailed Acumatica implementation assumptions to be provided as an addendum" |
| IF BeBanking in scope | FLAG | BeBanking pack NOT YET CREATED — same flag approach |
| NEVER include Draft packs | RULE | If a Draft pack is included, add footnote: "These assumptions are subject to BU Lead review and may be updated prior to contract execution" |

---

## C. Reference Selection Rules

### C1 — Inclusion

| Condition | Rule |
|---|---|
| IF Oracle proposal AND oracle_endorsement relevant | INCLUDE REF-ORA-007 (Oracle Corporation SA) — always safe; endorsement letter |
| IF HCM Learning in proposal | INCLUDE REF-ORA-006 Mr Price Group (Learning Cloud scope only — C-W3-002) |
| IF ERP Financials in proposal | CONSIDER REF-ORA-001 Investec; REF-ORA-002 NALA; REF-ORA-003 Cape Union Mart |
| IF EBS Finance + DBA in proposal | CONSIDER REF-ORA-004 Assore; REF-ORA-005 Adcock Ingram |
| IF EBS + OIC in proposal | CONSIDER REF-ORA-008 ARM |
| IF DBA / Managed Services in proposal | CONSIDER REF-ORA-009 MTN |
| IF BeBanking in proposal | CONSIDER REF-ORA-010 WITS |
| IF Acumatica Distribution in proposal | CONSIDER REF-ACU-001 Dunlop Srixon; REF-ACU-005 Interconnect |
| IF Acumatica Manufacturing in proposal | CONSIDER REF-ACU-003 Maxiflex; REF-ACU-004 At Source |

### C2 — Suppression (apply before finalising reference list)

| Condition | Rule |
|---|---|
| IF Hollywood Bets selected AND AM_approval_confirmed = FALSE | BLOCK — replace with "a leading gaming and financial services company" or omit; add OAR-C01 to action register |
| IF Hollywood Bets selected AND AM_approval_confirmed = TRUE | INCLUDE — with signed letter attached |
| IF KPMG selected | BLOCK — AM-W4E3-001 ACTIVE: KPMG must NOT be named until signed reference letter registered |
| IF DFA selected | SUPPRESS — Rule 21.4: NEVER include DFA in any external submission |
| IF CCBA selected | SUPPRESS — NEVER include CCBA in external submissions |
| IF Redpath selected AND go_live_confirmed = FALSE | SUPPRESS — Rule 21.5: not referenceable until go-live |
| IF Mr Price selected AND module ≠ Learning_Cloud | SUPPRESS — C-W3-002: restrict to Learning Cloud context only |
| IF any unsigned reference template selected | SUPPRESS — only signed, registered letters may be included |
| IF ARM selected for HCM Fusion context | FLAG — ARM reference is EBS HCM only, not Fusion HCM; ensure scope description matches |
| IF WITS selected for Fusion HCM context | FLAG — WITS is EBS + BeBanking, not Fusion HCM |

### C3 — AM Approval Gate

| Condition | Rule |
|---|---|
| ANY named client reference in Oracle Oracle BU | REQUIRE AM approval confirmation at submission time — not just at proposal preparation time |

---

## D. Consultant Selection Rules

| Rule | Detail |
|---|---|
| D1 — Skill matching | Use CONSULTANT_INDEX.csv to identify candidates by product and role tag |
| D2 — ADR-001 (hardcoded) | NEVER write CV text from KB records. AI must not generate or compose consultant CVs. |
| D3 — CV source | All CVs must be obtained from APPTime; referenced by consultant ID from index |
| D4 — Named consultants | NEVER name specific consultants in a proposal without BU Lead confirmation |
| D5 — PM selection | For PM role: check CON-XBU-* category (Cross-BU PMs) in CONSULTANT_INDEX.csv |
| D6 — OIC selection | For OIC role: check "OIC" skill tag or Oracle BU consultants with integration experience |
| D7 — No guarantee | Proposal language must state: "APPSolve will assign the most suitable available consultant" — no named consultant guarantee without explicit BU approval |

---

## E. Compliance Document Rules

| Condition | Rule |
|---|---|
| IF any proposal | INCLUDE COMP-001, COMP-002, COMP-004, COMP-011 |
| IF enterprise or financial services tender | ADD COMP-006 (Bank Letter), COMP-007 (PI Insurance), COMP-008 (PL Insurance), COMP-009 (COIDA) |
| IF public sector tender | ADD COMP-003 (VAT), COMP-005 (CSD), COMP-010 (EE Certificate) |
| IF COMP-001 (B-BBEE) expiry date < submission_date | BLOCK submission — cannot submit with expired B-BBEE; register as OAR-A01 |
| IF COMP-001 expiry date < 30 days from submission | FLAG — urgent renewal required |
| IF COMP-002 (Tax Clearance) expired | REFRESH — obtain new PIN from SARS |
| IF COMP-006 (Bank Letter) age > 3 months at submission | REFRESH — request new letter from bank |
| IF Acumatica proposal | FLAG — COMP-016 (Acumatica Partner Certificate) MISSING; note in compliance section |
| IF COMP-011 (Directors' Resolution) expiry < submission_date | BLOCK — obtain renewed resolution; current valid to June 2027 |

---

## F. Commercial Placeholder Rules

| Condition | Rule |
|---|---|
| ALL proposals — commercial section | INSERT "[COMMERCIAL INPUT REQUIRED — BU Lead and Commercial Director to complete before submission]" |
| IF AMS proposal — CR billing | Note: "Change Requests are billed on a time-and-materials basis. A CR order above 2 hours requires a signed SOW before work begins." |
| IF ERP proposal — data migration | Note: "The commercial estimate includes 2 data migration mock runs and 1 final migration. Additional mock runs are charged as CRs." |
| NEVER generate price estimates | RULE — AI/assembler must never compute or suggest specific Rand values without Commercial Director sign-off |
| NEVER apply RATE_CARD_FRAMEWORK rates | RULE — rate card is confidential; rates are inserted by Commercial Director only |

---

## G. Governance Suppression Rules

| Code | Rule |
|---|---|
| G1 | IF proposal includes W3S1-008 → strip Section 14.2 before external distribution (PT-W8-007) |
| G2 | IF proposal includes W3S1-009 → strip Section 13.2 before external distribution (PT-W9-008) |
| G3 | IF proposal includes W4-INT-001 → scan for HIST-018 billing amounts (R825,170 or any client billing figure) and remove |
| G4 | IF "Oracle Gold Partner" or "Gold Certified" appears in any section → replace with "Oracle Partner Network" |
| G5 | IF headcount > 50 in any statement → correct to "more than 50 Senior Consultants" |
| G6 | IF "110+" or "100+" or any number > 50 used as a headcount → correct |
| G7 | IF "19 years" (Hein career) appears → correct to "since 1996" or "more than 29 years" |
| G8 | IF approved country list violated (Nigeria, Uganda, Ghana, Bangladesh, Qatar in geographic reach) → remove |
| G9 | IF competitor product named positively → remove |
| G10 | IF any unapproved client name appears (DFA, CCBA, Redpath without waiver, Hollywood Bets without AM approval, KPMG) → BLOCK or anonymise |
| G11 | IF "22 years" company age → correct to "24+ years" (founded 2002; current year 2026) |
| G12 | IF W3S1-005 (Compensation) included AND sector ≠ Mining → BLOCK (G-001 violation) |

---

## H. Duplicate Removal Rules

| Condition | Rule |
|---|---|
| IF W2S1-005 AND W5-METH-001 both in assembly | Keep one only: Oracle-only proposal → keep W2S1-005; multi-platform → keep W5-METH-001 |
| IF W3S1-007 selected AND standalone T&L statement found | Remove standalone T&L; W3S1-007 governs (W4-HCM-004 is retired) |
| IF same company referenced via two different letters | Use most recent signed letter only |
| IF W3S1-001 AND W3S1-009 both included AND Payroll Interface IS the primary scope | Ensure payroll interface section does not duplicate HCM Core employee management content |

---

## I. Conflict Escalation Matrix

| Conflict | Action | Escalation |
|---|---|---|
| G-001 violation (Compensation + non-Mining) | BLOCK assembly; raise to BU Lead | Oracle HCM BU Lead must approve before including W3S1-005 |
| PT-W8-007 violation (Section 14.2 in external doc) | Strip section; note in review log | None — auto-fix; inform BU Lead |
| PT-W9-008 violation (Section 13.2 in external doc) | Strip section | Auto-fix; inform BU Lead |
| C-W3-002 violation (Mr Price in non-Learning context) | Remove Mr Price reference | Auto-fix |
| AM-W4E3-001 violation (KPMG named) | BLOCK | Account Manager must obtain signed letter first |
| Rule 21.4 violation (DFA named) | SUPPRESS | Auto-fix; document in governance log |
| Rule 21.5 violation (Redpath named before go-live) | SUPPRESS | Confirm go-live status with BU Lead |
| Hollywood Bets without AM approval | BLOCK or anonymise | OAR-C01 must be resolved |

---

*ASSEMBLY_RULES_ENGINE v1.0 | WP12 — Proposal Assembly Engine | 2026-06-16*
*Companion: TENDER_BOM_LIBRARY.md | PROPOSAL_STRUCTURE_LIBRARY.md | ASSEMBLY_READINESS_MATRIX.md*
