# Answer Assembly Framework
**Work Package:** WP5 — Tender Response Factory | **Version:** 1.0 | **Created:** 2026-06-14
**Purpose:** Shows how to combine approved KB assets into a complete tender response for each tender type. Each recipe specifies which assets to use, in what order, and which governance checks to apply.

---

## How to Use This Framework

**Step 1 — Identify the tender type** from the list below
**Step 2 — Follow the assembly recipe** for that type
**Step 3 — Run all governance checks** listed for each asset used
**Step 4 — Apply section exclusions** (Section 14.2 W3S1-008; Section 13.2 W3S1-009)
**Step 5 — Fill mandatory gaps** with bespoke content (marked ✍️ in recipes)
**Step 6 — BU Lead review** before submission (named references, governance exceptions)

> **Always-on rule:** Do not use `approved_for_reuse: No` content in any tender response. All named reference restrictions (Rule 21.4 DFA, Rule 21.1 SAA, HIST-014 CCBA) apply at all times regardless of tender type.

---

## Recipe 1 — Oracle HCM Full Implementation Tender

**When to use:** Tender requires full Oracle Fusion HCM implementation (Core HR + multiple modules)

**Typical tender sections and asset mapping:**

| Tender Section | Primary Assets | Notes |
|---|---|---|
| **Executive Summary** | W1S1-001 + W1S1-009 | Extract: company overview paragraph + differentiators relevant to HCM |
| **About APPSolve** | W1S1-001, W1S1-002, W1S1-008 | Company overview, history, geographic presence |
| **Oracle Partnership** | W1S1-003 | Level 1 Partner; 5 expertise areas; awards |
| **Oracle HCM Core Capability** | W3S1-001 | Full HCM Core statement — adapt intro paragraph to tender context |
| **Module-Specific Capability** | W3S1-002 through W3S1-009 (select relevant modules) | Pick modules matching tender requirements |
| **New Modules (Wave 4)** | W4-HCM-002 (Journeys), W4-AI-002 (AI Skills) if required | Include only if tender asks for Journeys or AI |
| **Payroll Integration** | W3S1-009 + W4-INT-001 | OIC ↔ PaySpace architecture; include only if payroll integration required |
| **Implementation Methodology** | W2S1-005 | Full 6-phase methodology; Oracle HCM context |
| **Change Management** | W2S1-005 (embedded) + W3S1-001 (user adoption) | Extract change management sections; no standalone statement available |
| **Training** | W2S1-005 (train-the-trainer) + W3S1-004 (if LMS requested) | W3S1-004 only if client asks about Oracle Learning Cloud as training tool |
| **Key Personnel** | ✍️ From APPTime (ADR-001) | Must source CVs from APPTime; not in KB |
| **Reference Clients** | W3S1-001 (Hollywood Bets — AM approval) | AM approval required before naming HB; Mr Price for Learning Cloud (W3S1-004) |
| **Support Model** | W2S1-004 | Oracle HCM support model; adapt SLAs per tender spec |
| **Awards / Credentials** | W1S1-006 | Oracle awards; success stories (URL verify before use) |

**Governance checklist before submission:**
- [ ] HB account manager approval for named reference
- [ ] W3S1-008 Section 14.2 EXCLUDED (internal only — PT-W8-007)
- [ ] W3S1-009 Section 13.2 EXCLUDED (internal only — PT-W9-008)
- [ ] Oracle HR Help Desk not described as Oracle Fusion Service / Oracle Service Cloud
- [ ] DFA not named anywhere
- [ ] SAA not named anywhere
- [ ] CCBA not named anywhere
- [ ] BEE Level 3 confirmed (cert expires 2026-07-31)
- [ ] OPN certification current (W1S1-003 annual check)

**Coverage rating: ~85%** — Gap areas: Standalone change management; Standalone testing; Key personnel CVs (by design)

---

## Recipe 2 — Oracle HCM Analytics / Reporting Tender

**When to use:** Tender specifically focuses on HCM data, reporting, workforce intelligence

| Tender Section | Primary Assets | Notes |
|---|---|---|
| **Executive Summary** | W1S1-001 + W1S1-009 | — |
| **About APPSolve** | W1S1-001, W1S1-002 | — |
| **Oracle Partnership** | W1S1-003 | — |
| **HCM Core** | W3S1-001 | Brief foundation — HCM platform context |
| **Analytics Capability** | W3S1-006 | Full HCM Analytics statement — OTBI Tier 1; BI Publisher Tier 1; OAX Platform Capability Only |
| **AI Skills (if relevant)** | W4-AI-002 | If tender asks about AI-driven workforce insights |
| **Implementation** | W2S1-005 | Abbreviated — focus on Validate and Evolve phases |
| **Reference Clients** | W3S1-006 (HB OTBI) | HB reference for OTBI/BI Publisher; AM approval required |

**Key restriction:** OAX (Oracle Analytics Cloud) is Platform Capability Only — never claim an OAX implementation in W3S1-006. Strategic Workforce Planning is entirely excluded.

---

## Recipe 3 — Oracle ERP Tender (Fusion Finance + Procurement)

**When to use:** Oracle Fusion Cloud ERP tender requiring Finance and/or Procurement modules

| Tender Section | Primary Assets | Notes |
|---|---|---|
| **Executive Summary** | W1S1-001 + W1S1-009 | — |
| **About APPSolve** | W1S1-001, W1S1-002, W1S1-008 | — |
| **Oracle Partnership** | W1S1-003 | — |
| **Oracle Fusion Platform Overview** | W2S1-001 | High-level Fusion platform credential |
| **Oracle Fusion Financials** | W4-ERP-001 | Full Finance statement; use anonymous client framing until letters registered |
| **Oracle Fusion Procurement** | W4-ERP-002 | If Procurement is in scope; same anonymous framing |
| **Oracle PPM** | W4-ERP-003 | Only if Project Accounting / PPM is in scope |
| **OIC Integration** | W4-INT-001 | If integration to third-party systems is required |
| **Multi-Country Experience** | W4-ERP-001 (Investec multi-country); W2S1-001 (NALA 8 countries) | Use anonymous framing ("multi-country environments in Sub-Saharan Africa, Europe, and North America") until letters registered |
| **Implementation Methodology** | W2S1-005 | Full methodology |
| **Support Model** | W2S1-004 | Oracle ERP support |
| **Reference Clients** | W2S1-002 (ARM, Assore, Adcock, Harmony, Investec for EBS); W4-ERP-001/002 (pending letter registration for Fusion) | Register SABS corpus letters to unlock Fusion Finance named references |

**Anonymous reference wording (use until letters registered):**
> "APPSolve has delivered Oracle Fusion Financials across multi-country environments in Sub-Saharan Africa, Europe, and North America, including multi-entity financial management across multiple legal entities with localised tax and statutory reporting."

**Governance checklist:**
- [ ] AM-W4E1-001 check: Named clients Investec/NALA/CUM — letters confirmed and registered?
- [ ] AM-W4E2-001 check: Cape Union Mart scope confirmed as Oracle Finance/Procurement (not Acumatica/PaySpace)?
- [ ] AM-W4E3-001 check: KPMG letter confirmed and registered before naming?
- [ ] DFA not named anywhere (Rule 21.4)
- [ ] HIST-018 billing figure (R825,170) not appearing anywhere

**Coverage rating: ~75%** — Gap areas: Named references blocked (use anonymous framing); No Oracle SCM statement; Key personnel from APPTime

---

## Recipe 4 — Oracle EBS Tender

**When to use:** Oracle EBS (E-Business Suite) implementation, upgrade, or managed services

| Tender Section | Primary Assets | Notes |
|---|---|---|
| **Executive Summary** | W1S1-001 + W1S1-009 | — |
| **About APPSolve** | W1S1-001, W1S1-002 | — |
| **Oracle Partnership** | W1S1-003 | — |
| **Oracle EBS Capability** | W2S1-002 | Full EBS statement; ARM R12.2 Tier 1A primary reference |
| **Reference Clients** | W2S1-002 (ARM, Assore, Adcock Ingram, Harmony, Investec — all referenceable) | Strongest named reference set in KB |
| **DBA Capability** | W2S1-003 | DBA Executive Summary — managed services context |
| **Support Model** | W2S1-004 | Oracle managed services model |
| **Implementation Methodology** | W2S1-005 | EBS implementation context |

**Pre-tender checks (from W2S1-002):**
- [ ] OPN cert verification for OCI Published Expertise (FR-EBS-012)
- [ ] SARB: separate explicit BU Lead approval required before any external citation
- [ ] MTN: source-evidence-only (not a reference client for EBS)
- [ ] ATNS: source-evidence-only (award unconfirmed, tender re-issued)
- [ ] Manufacturing: EXCLUDED from EBS capability (BU-EBS-003)

**Coverage rating: ~90%** — Strongest-coverage recipe; EBS reference set is the most complete named set in KB

---

## Recipe 5 — Oracle DBA / Managed Services Tender

**When to use:** Oracle database managed services, DBA support, Oracle environment management

| Tender Section | Primary Assets | Notes |
|---|---|---|
| **Executive Summary** | W1S1-001 + W1S1-009 | — |
| **About APPSolve** | W1S1-001, W1S1-002 | One of the largest locally based Oracle Applications DBA teams in SA |
| **Oracle Partnership** | W1S1-003 | — |
| **DBA Executive Summary** | W2S1-003 | Primary DBA statement; 12 sections |
| **Support Model** | W2S1-004 | 15-section managed services model; reuse map W2S1-003 B-001 through Q23 blocks |
| **Delivery Model** | W1S1-007 | Hybrid model; 24x7 monitoring with after-hours support |

**Key restrictions (from W2S1-003):**
- No MTN-specific metrics
- No fixed SLA commitments (W2S1-004)
- No commercial commitments
- Section 7.4 POPIA framing: client-obligation-facing (not APPSolve's own POPIA obligations)
- No "at no cost" (A-007 closed)

**Coverage rating: ~90%** — DBA + managed services is the most mature support coverage in KB

---

## Recipe 6 — Acumatica ERP Tender

**When to use:** Acumatica ERP implementation — any module combination

| Tender Section | Primary Assets | Notes |
|---|---|---|
| **Executive Summary** | W1S1-001 + W1S1-009 | — |
| **About APPSolve** | W1S1-001, W1S1-002, W1S1-008 | — |
| **Acumatica Partnership** | W1S1-004 | Gold Partner; VAR; industries |
| **Acumatica Product Capability** | W1S2-001 through W1S2-009 (select modules per tender scope) | Match modules to tender requirements |
| **BeBanking Integration** | W1S3-006 (ERP Integration) | If H2H banking integration is in scope |
| **PaySpace Integration** | W1S2-007 | If payroll integration (Acumatica ↔ PaySpace) is in scope |
| **Implementation Methodology** | W2S1-005 (adapted) + W1S1-007 | W2S1-005 must be de-branded from Oracle-specific language (OUM, CSN references) for Acumatica use |
| **Key Personnel** | ✍️ From APPTime (ADR-001) | — |
| **Reference Clients** | W1S2-006 (Interconnect — confirmed); DSSSA/FuelU2/Maxiflex (letters in AFROSAI-E corpus — register to unlock) | Contact BU Lead to confirm which references can be cited |
| **Support Model** | ✍️ Must be authored | CRITICAL GAP — no Acumatica support statement exists |
| **Change Management** | W2S1-005 (embedded) | — |
| **Training** | W2S1-005 (train-the-trainer) | — |

**Critical gap management for Acumatica support model:**
When a tender requires post-implementation support details for Acumatica, use the following bridging approach until a dedicated Acumatica support statement is authored:
> "APPSolve provides post-implementation support for Acumatica ERP through our Hybrid Support Model, combining dedicated account management with a tiered support framework. Our support services are tailored to each client's requirements in terms of response times, coverage hours, and escalation procedures."

**Coverage rating: ~65%** — Gap areas: Acumatica support model (critical); Acumatica methodology de-branding required; Limited named reference clients

---

## Recipe 7 — BeBanking / H2H Banking Tender

**When to use:** Host-to-host banking, EFT payment automation, BeBanking product tender

| Tender Section | Primary Assets | Notes |
|---|---|---|
| **Executive Summary** | W1S1-001 + W1S1-009 | — |
| **About APPSolve** | W1S1-001, W1S1-002 | — |
| **BeBanking Overview** | W1S1-005, W1S3-001 | Product overview; module list; ERP compatibility |
| **H2H Banking Capability** | W1S3-002 | Core H2H statement |
| **Payment Modules** | W1S3-003, W1S3-004, W1S3-005 | Select by payment type required |
| **ERP Integration** | W1S3-006 | Which ERP the client uses |
| **Security** | W1S3-007 | Security approach; POPIA |
| **Architecture** | W1S3-008 | Technical architecture |
| **Hosting** | W1S3-009 | SaaS model; OCI |
| **Monitoring** | W1S3-010 | Operational monitoring |

**Governance notes:** Acumatica payroll H2H is NOT supported through BeBanking (W1S3-004 covers Oracle EBS/Fusion payroll only). SAP = "BeBanking integrates with SAP environments" only — no module claims.

**Coverage rating: ~95%** — Most complete recipe in KB; BeBanking is comprehensively documented

---

## Recipe 8 — Mixed / Multi-Platform Tender

**When to use:** Tender requires Oracle + Acumatica + BeBanking coverage simultaneously (e.g., group-level tender)

| Section | Assets |
|---|---|
| Corporate | W1S1-001, W1S1-002, W1S1-006, W1S1-007, W1S1-008, W1S1-009 |
| Oracle Partnership | W1S1-003 |
| Acumatica Partnership | W1S1-004 |
| BeBanking Overview | W1S1-005 |
| Oracle Capability | W2S1-001, W2S1-002, W3S1-001–009, W4 as relevant |
| Acumatica Capability | W1S2-001–009 as relevant |
| BeBanking Capability | W1S3-001–010 as relevant |
| Methodology | W2S1-005 (Oracle); ✍️ Acumatica methodology |
| Support | W2S1-004 (Oracle); ✍️ Acumatica support |

**Coverage rating: ~75%** — Oracle and BeBanking strong; Acumatica support gap still applies

---

## Standard Governance Checkpoint (All Recipes)

Run before every tender submission:

| Check | Rule |
|---|---|
| DFA not named anywhere | Rule 21.4 — permanent |
| SAA not named anywhere | Rule 21.1 — aviation prohibited |
| CCBA not named anywhere | HIST-014 |
| Redpath Mining: pipeline framing only, never named | Rule 21.5 |
| Hollywood Bets: AM approval obtained | Required per tender |
| Mr Price: Learning Cloud scope only (W3S1-004) | C-W3-002 |
| Mr Price T&L: PoC framing only if referenced at all | OI-W7-001 |
| W3S1-008 Section 14.2: EXCLUDED from submission | PT-W8-007 |
| W3S1-009 Section 13.2: EXCLUDED from submission | PT-W9-008 |
| Oracle HR Help Desk: never called Oracle Fusion Service / Oracle Service Cloud / Oracle B2C Service | Standing rule |
| HIST-018 billing figure (R825,170): never appears | Standing rule |
| BEE Level 3 confirmed current (expires 2026-07-31) | Pre-tender check |
| OPN certification current | W1S1-003 annual check |
| Acumatica Gold Partner status current | W1S1-004 annual check |
| 50+ Senior Consultants (not 100+ or 110+) | CROSS-1 applied — confirmed fact |

---

*ANSWER_ASSEMBLY_FRAMEWORK.md v1.0 — WP5 2026-06-14. All recipes subject to governance restrictions in TENDER_COMPONENT_LIBRARY.md and MASTER_CAPABILITY_INDEX.md.*
