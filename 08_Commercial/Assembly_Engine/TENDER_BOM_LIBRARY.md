---
document_id: TENDER-BOM-LIBRARY
title: "Tender Bill of Materials Library"
version: "1.1"
created: "2026-06-16"
created_by: "WP12 — Proposal Assembly Engine"
updated: "2026-06-26"
updated_by: "WP18C.2 — Section Library Consolidation"
status: "Updated — KI-001 stale pack statuses corrected (HCM module packs Approved v1.0; Acumatica Base Approved v1.0; BeBanking Base Approved v1.0; EBS overlay packs added to BOM 16)"
---

# Tender Bill of Materials Library

**Purpose:** Defines the reusable Bill of Materials for each standard tender type. Use this to assemble the complete set of assets required for any proposal.

**How to use:**
1. Identify the product type(s) in scope.
2. Load all Required assets for each product type.
3. Review Optional assets against the specific scope.
4. Check MASTER_CAPABILITY_INDEX.md for per-asset governance restrictions.
5. Apply governance suppression rules before final assembly.

**Asset authority:** `06_Capabilities/MASTER_CAPABILITY_INDEX.md` (v1.2)
**Assumption authority:** `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md`

---

## Standard Corporate Block (All Proposals)

Include in every proposal regardless of product type:

| Asset ID | Name | Notes |
|---|---|---|
| W1S1-001 | Company Overview | "more than 50 Senior Consultants" only — never 100+ or 110+ |
| W1S1-007 | Delivery Model | 8 service lines; 3 costing models |
| W1S1-008 | Geographic Presence | Approved sub-Saharan + international markets only |
| W1S1-009 | Key Differentiators | 7 differentiators; Continuous Improvement Model |
| COMP-001 | B-BBEE Certificate | Level 3 — EXPIRES 2026-07-31; check at submission |
| COMP-002 | Tax Clearance PIN | Valid to 2027-02-23 |
| COMP-004 | CIPC Registration | Full pack: COR14.3 + Disclosure + Cor39 + Beneficiary Ownership |
| COMP-011 | Directors' Resolution | Renewed 2026-06-15; valid to June 2027 |

Enterprise/financial services additions: COMP-006 (Bank Letter — < 3 months old), COMP-007 (PI Insurance), COMP-008 (PL Insurance — obtained 2026-06-15), COMP-009 (COIDA).
Public sector additions: COMP-003 (VAT), COMP-005 (CSD — refresh if > 12 months), COMP-010 (EE Certificate).

---

## BOM 1 — Oracle HCM Full Suite

**Scope:** Core HR + 4 or more of: Recruiting, Learning, Talent, Compensation, Absence, Journeys, AI Skills, Payroll Interface.

### Required Capability Assets

| Asset | Name |
|---|---|
| W1S1-003 | Oracle Partnership Statement |
| W2S1-005 | Oracle Implementation Methodology |
| W3S1-001 | HCM Core — Global HR |
| W3S1-007 | Oracle Workforce Management (Absence Management) |
| W4-HCM-002 | Oracle Journeys |
| W4-AI-002 | Oracle AI Skills |

### Optional (include per modules in scope)

| Asset | Include When |
|---|---|
| W3S1-002 | Talent Management in scope |
| W3S1-003 | Recruiting Cloud in scope |
| W3S1-004 | Learning Cloud in scope |
| W3S1-005 | Workforce Compensation in scope — **Mining sector only (G-001)** |
| W3S1-006 | Analytics / reporting emphasis |
| W3S1-008 | HR Help Desk in scope |
| W3S1-009 | Payroll integration (PaySpace) — **exclude Section 13.2 externally** |
| W4-INT-001 | OIC integrations confirmed in scope |

### Required Assumption Packs

| Pack | Status | When |
|---|---|---|
| HCM Base | **Approved v1.1 (WP16D)** | Always — mandatory |
| HCM Recruiting | **Approved v1.0 (WP16C 2026-06-19)** | Recruiting in scope |
| HCM Learning | **Approved v1.0 (WP16C 2026-06-19)** | Learning in scope |
| HCM Talent | **Approved v1.0 (WP16C 2026-06-19)** | Talent in scope |
| HCM Compensation | **Approved v1.0 (WP16C 2026-06-19)** | Compensation in scope — Mining sector only (G-001) |
| OIC Integration | **Approved** | OIC integrations in scope |
| AMS | **Approved** | Post-implementation support in scope |

### Reference Assets

| Ref | Client | Applicable modules | Restriction |
|---|---|---|---|
| REF-ORA-007 | Oracle Corporation SA | All Oracle — always include | Partner endorsement — not a client reference |
| Hollywood Bets | NOT registered | Full HCM suite; Recruiting; Absence; HR Help Desk; OIC | **AM approval required before naming — no signed letter** |
| REF-ORA-006 | Mr Price Group | Learning Cloud only | **C-W3-002: Learning Cloud scope restriction** |
| REF-ORA-008 | ARM | EBS HCM history (not Fusion) | AM approval required |
| REF-ORA-010 | WITS | EBS + BeBanking — not Fusion HCM | AM approval required |

### Consultant Categories
HCM Principal Functional Consultant (lead); Senior HCM Module Specialists (per module); OIC Integration Consultant (if integrations); Project Manager; Programme Manager (large engagements).

### Commercial Components
Bottom-up estimate (ESTIMATION_GUIDE.md); Effort multipliers (EFFORT_MULTIPLIERS.md); HCM Base assumption pack in appendix; Module packs where approved; `[COMMERCIAL INPUT REQUIRED]` for pricing.

### Governance Restrictions
- DFA: NEVER named (Rule 21.4)
- CCBA: NEVER named
- Redpath: NOT referenceable until go-live + BU Lead waiver (Rule 21.5)
- Hollywood Bets: AM approval required at each submission
- W3S1-008: Section 14.2 MUST NOT appear externally (PT-W8-007)
- W3S1-009: Section 13.2 MUST NOT appear externally (PT-W9-008)
- W3S1-005 Compensation: Mining sector only (G-001) — Retail attribution prohibited
- T&L: No standalone statement; governed through W3S1-007 only

---

## BOM 2 — Oracle HCM Base (Core HR)

**Scope:** Core HR, Absence Management, Benefits, Journeys only.

| Category | Assets |
|---|---|
| Required capability | W1S1-003, W2S1-005, W3S1-001, W3S1-007, W4-HCM-002 |
| Optional | W4-AI-002, W3S1-006 |
| Assumption packs | HCM Base (Approved) |
| References | REF-ORA-007; Hollywood Bets (AM approval) |
| Governance | Same as BOM 1; DFA Rule 21.4; Redpath Rule 21.5 |

---

## BOM 3 — Oracle Recruiting Cloud

| Category | Assets |
|---|---|
| Required | W1S1-003, W3S1-003, W2S1-005, W3S1-001 |
| Optional | W4-HCM-002 (Journeys/Onboarding) |
| Assumption packs | HCM Base (Approved v1.1); HCM Recruiting (**Approved v1.0 — WP16C 2026-06-19**) |
| References | REF-ORA-007; Hollywood Bets Phase 3 (AM approval required) |
| Restrictions | DFA Taleo = internal only (Rule 21.4). Redpath Recruiting = Rule 21.5. |

---

## BOM 4 — Oracle Learning Cloud

| Category | Assets |
|---|---|
| Required | W1S1-003, W3S1-004, W2S1-005 |
| Optional | W3S1-006 (SETA/analytics emphasis) |
| Assumption packs | HCM Base (Approved v1.1); HCM Learning (**Approved v1.0 — WP16C 2026-06-19**) |
| References | REF-ORA-007; REF-ORA-006 Mr Price — Learning Cloud scope only (C-W3-002) |
| Restrictions | Mr Price = Learning Cloud implementation only — no broader HCM claim |

---

## BOM 5 — Oracle Talent Management

| Category | Assets |
|---|---|
| Required | W1S1-003, W3S1-002, W2S1-005 |
| Optional | W3S1-006 (9-box analytics) |
| Assumption packs | HCM Base (Approved v1.1); HCM Talent (**Approved v1.0 — WP16C 2026-06-19**) |
| References | REF-ORA-007; Hollywood Bets Phase 4 (AM approval required) |
| Restrictions | DFA: Rule 21.4. Redpath: Rule 21.5. |

---

## BOM 6 — Oracle Workforce Compensation

| Category | Assets |
|---|---|
| Required | W1S1-003, W3S1-005, W2S1-005 |
| Assumption packs | HCM Base (Approved v1.1); HCM Compensation (**Approved v1.0 — WP16C 2026-06-19**) |
| References | REF-ORA-007 only — no Tier 1 referenceable client (evidence gap) |
| Restrictions | **G-001: Mining sector ONLY. Retail attribution PROHIBITED. No Tier 1 client.** DFA: Rule 21.4. |

---

## BOM 7 — Oracle Journeys / Onboarding

| Category | Assets |
|---|---|
| Required | W1S1-003, W4-HCM-002, W3S1-001 |
| Assumption packs | HCM Base (Approved) |
| References | REF-ORA-007; Hollywood Bets Phase 1 (AM approval required) |

---

## BOM 8 — Oracle AI Skills

| Category | Assets |
|---|---|
| Required | W1S1-003, W4-AI-002, W3S1-002 |
| Assumption packs | HCM Base (Approved) |
| References | REF-ORA-007; Hollywood Bets Phase 4 (AM approval required) |
| Restrictions | Do NOT conflate with ODA or Oracle Grow. AI Skills = Dynamic Skills Cloud only. |

---

## BOM 9 — Oracle OIC Integration

| Category | Assets |
|---|---|
| Required | W1S1-003, W4-INT-001, W2S1-001 |
| Optional | W3S1-009 (if HCM ↔ payroll integration) |
| Assumption packs | OIC Integration (Approved) |
| References | REF-ORA-007; REF-ORA-008 ARM (OIC scope); Hollywood Bets OIC (AM required) |
| Restrictions | HIST-018 billing (R825,170) MUST NEVER appear in external submissions. W3S1-009 Section 13.2 NEVER external. |

---

## BOM 10 — Oracle Fusion Financials

| Category | Assets |
|---|---|
| Required | W1S1-003, W4-ERP-001, W2S1-001, W2S1-005 |
| Optional | W4-INT-001 (OIC bank integration), W4-ERP-002 (Procurement) |
| Assumption packs | Oracle ERP (Approved); OIC (if bank integration); AMS (if support) |
| References | REF-ORA-007; REF-ORA-001 Investec; REF-ORA-002 NALA; REF-ORA-003 Cape Union Mart (Finance + Procurement confirmed D2) |
| Restrictions | DFA: Rule 21.4. AM approval required for all named clients. |

---

## BOM 11 — Oracle Fusion Procurement

| Category | Assets |
|---|---|
| Required | W1S1-003, W4-ERP-002, W2S1-001, W2S1-005 |
| Optional | W4-ERP-001 (Financials — often paired) |
| Assumption packs | Oracle ERP (Approved); OIC (if supplier integration) |
| References | REF-ORA-001 Investec; REF-ORA-003 Cape Union Mart (scope confirmed: Finance + Procurement) |

---

## BOM 12 — Oracle PPM

| Category | Assets |
|---|---|
| Required | W1S1-003, W4-ERP-003, W2S1-001 |
| Assumption packs | Oracle ERP (Approved) |
| References | REF-ORA-007 only — **KPMG BLOCKED: AM-W4E3-001 ACTIVE** — use anonymous until signed letter obtained |
| Restrictions | AM-W4E3-001 ACTIVE — KPMG must NOT be named in any submission until signed letter registered. |

---

## BOM 13 — Oracle EBS

| Category | Assets |
|---|---|
| Required | W1S1-003, W2S1-002, W2S1-005 |
| Optional | W2S1-003 (DBA — if DBA scope); W4-INT-001 (OIC migration) |
| Assumption packs | Oracle ERP (Approved — covers EBS GL/AP/AR/FA) |
| References | REF-ORA-004 Assore; REF-ORA-005 Adcock Ingram; REF-ORA-008 ARM; REF-ORA-009 MTN (DBA) |
| Restrictions | Oracle Gold Partner EXPIRED 2021 — NEVER cite. Level 1 only. |

---

## BOM 14 — Acumatica ERP

| Category | Assets |
|---|---|
| Required | W1S1-004, W5-METH-001, W1S1-007 |
| Modules (per scope) | W1S2-001 Financials; W1S2-002 Distribution; W1S2-003 Inventory; W1S2-004 Manufacturing; W1S2-005 CRM; W1S2-006 Field Services; W1S2-009 Project Accounting |
| Optional | W1S2-007 PaySpace Integration; W5-ACU-001 (AMS) |
| Assumption packs | Acumatica Base — **Approved v1.0 (WP15C 2026-06-18) — 152 assumptions; Sections 120–139; approved_for_reuse: Yes** |
| References | REF-ACU-001 Dunlop (Distribution); REF-ACU-003 Maxiflex (Manufacturing); REF-ACU-004 At Source (Manufacturing+WMS); REF-ACU-005 Interconnect (Distribution+CRM+PA) |
| Compliance gap | COMP-016 Acumatica Partner Certificate MISSING — flag in proposal |
| Restrictions | No SA payroll functionality — PaySpace is SOR. Manufacturing = HyDac sole KB source. |

---

## BOM 15 — BeBanking

| Category | Assets |
|---|---|
| Required | W1S1-005, W1S3-001, W1S3-002, W1S3-008 (Architecture) |
| Modules (per scope) | W1S3-003 Supplier Payments; W1S3-004 Payroll Payments; W1S3-005 Forex; W1S3-006 ERP Integration; W1S3-007 Security; W1S3-009 Hosting; W1S3-010 Monitoring |
| Assumption packs | BeBanking Base — **Approved v1.0 (WP14F 2026-06-18) — 117 assumptions; Sections 140–153; approved_for_reuse: Yes** |
| References | REF-ORA-010 WITS (Oracle EBS + BeBanking cross-BU reference) |
| Restrictions | SAP = environments only. SWIFT = bank-intermediated only. Payroll H2H = Oracle EBS/Fusion sources only (no Acumatica payroll). |

---

## BOM 16 — AMS / Managed Services

| Category | Assets |
|---|---|
| Required | W2S1-004 (Oracle AMS) or W5-ACU-001 (Acumatica AMS) — match to product |
| Assumption packs | AMS Base (Approved) — **mandatory for all AMS** |
| EBS Overlay packs | **EBS SLA Overlay — Approved v1.0 (WP15F 2026-06-19) — 53 assumptions** — include when Oracle EBS AMS with non-standard SLA commitments. Overlays (does not replace) AMS Base. **EBS DRM Overlay — Approved v1.0 (WP15F 2026-06-19) — 62 assumptions** — include when Oracle EBS AMS with dedicated/named resource model. Overlays AMS Base. Suppression rules S1–S4 apply when both overlays loaded (see RULE_PROCESSOR.md). |
| References | Oracle AMS: REF-ORA-001, 002, 004, 005, 008, 009, 010. Acumatica AMS: REF-ACU-003, 005. |
| Commercial | Retainer-based or allocated-hours model; CRs separate at T&M; [COMMERCIAL INPUT REQUIRED] |
| Key restrictions | AMS CRs always T&M — never fixed-price. CR threshold = 2 hours. Named consultant not guaranteed. 24x7/proactive monitoring excluded unless contracted. Change control governed by S-73 (not S-38) in AMS proposals. |

---

*TENDER_BOM_LIBRARY v1.1 | WP12 — Proposal Assembly Engine | Updated WP18C.2 2026-06-26*  
*Companion: ASSEMBLY_RULES_ENGINE.md | PROPOSAL_STRUCTURE_LIBRARY.md | MASTER_CAPABILITY_INDEX.md*  
*v1.1 (KI-001 fix): HCM module packs (Recruiting/Learning/Talent/Compensation) status corrected Draft → Approved v1.0 (WP16C 2026-06-19); Acumatica Base status corrected to Approved v1.0 (WP15C); BeBanking Base status corrected to Approved v1.0 (WP14F); EBS SLA and EBS DRM overlay packs added to BOM 16.*
