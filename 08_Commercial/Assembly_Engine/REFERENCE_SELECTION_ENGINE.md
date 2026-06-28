---
document_id: REFERENCE-SELECTION-ENGINE
title: "Reference Selection Engine — Scoring Matrix and Governance Rules"
version: "1.0"
status: "Approved — WP18C.3"
created: "2026-06-25"
created_by: "WP18C.3 — Tender Intelligence Layer"
category: "Architecture / Intelligence Layer"
scope: "Defines the deterministic reference selection algorithm for all 16 approved reference letters. Scoring: 7 dimensions / 10-point maximum. Exclusion rules: 12 governance restrictions. AM approval workflow. Input: Tender Profile (platform, industry, engagement_type, modules_in_scope, country). Output: reference_pool (scored, ranked, AM-approval-status)."
---

# Reference Selection Engine

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18C.3 — Tender Intelligence Layer  
**Input:** Tender Profile Blocks B, C, D (client profile, platform, scope)  
**Output:** `reference_pool[]` — scored and ranked list with AM approval status per reference

---

## 1. Purpose

The Reference Selection Engine converts the Tender Profile into a governed, ranked list of eligible reference letters. It replaces the manual Stage 5 reference selection identified in WP18C.1 as fully rule-based (AO-003).

**Governing principle:** Only signed letters held in `04_References/` may be cited in any proposal. AM approval is required at each tender before a reference is confirmed for inclusion. No reference may be used that is not in the approved reference inventory below.

**Exclusion rule takes precedence over scoring.** A reference with the highest score is still excluded if any exclusion rule applies.

---

## 2. Reference Inventory

The complete approved reference pool as at 2026-06-25. Source of truth is REFERENCE_MASTER.csv; this table summarises scoring-relevant attributes.

| Ref ID | Client | Products | Platform | Engagement Type | Industry | Country | Size | Special Restrictions |
|---|---|---|---|---|---|---|---|---|
| REF-ORA-001 | Investec | Fusion Financials, Procurement | Oracle-Fusion | Implementation | Financial-Services | ZA | Enterprise | AM approval required |
| REF-ORA-002 | NALA | Oracle ERP (Fusion) | Oracle-Fusion | Implementation | Other | ZA | Mid-market | AM approval required |
| REF-ORA-003 | Cape Union Mart | Fusion Financials + Procurement | Oracle-Fusion | Implementation | Retail | ZA | Enterprise | Scope confirmed: Finance + Procurement only |
| REF-ORA-004 | Assore | Oracle EBS Finance + HRMS | Oracle-EBS | Implementation | Mining | ZA | Enterprise | AM approval required |
| REF-ORA-005 | Adcock Ingram | Oracle EBS Finance + HRMS | Oracle-EBS | Implementation | Manufacturing | ZA | Enterprise | AM approval required |
| REF-ORA-006 | Mr Price Group | Oracle Learning Cloud | Oracle-Fusion | Implementation | Retail | ZA | Enterprise | **C-W3-002: Learning Cloud scope ONLY — never claim broader HCM** |
| REF-ORA-007 | Oracle Corporation SA | All Oracle products | Cross-platform | Partner reference | Technology | ZA | Enterprise | Always eligible; standard letter |
| REF-ORA-008 | ARM (African Rainbow Minerals) | Oracle EBS + OIC + AMS | Oracle-EBS + OIC | AMS | Mining | ZA | Enterprise | AM approval required |
| REF-ORA-009 | MTN | Oracle EBS DBA | Oracle-EBS | DBA/Managed | Telecommunications | ZA | Enterprise | AM approval required |
| REF-ORA-010 | WITS | Oracle EBS + BeBanking | Oracle-EBS + BeBanking | Implementation | Education | ZA | Enterprise | AM approval required |
| REF-ACU-001 | Dunlop | Acumatica Distribution | Acumatica | Implementation | Distribution/Manufacturing | ZA | Mid-market | AM approval required |
| REF-ACU-003 | Maxiflex | Acumatica Manufacturing | Acumatica | Implementation | Manufacturing | ZA | Mid-market | AM approval required |
| REF-ACU-004 | At Source | Acumatica Manufacturing + WMS | Acumatica | Implementation | Manufacturing | ZA | SME | AM approval required |
| REF-ACU-005 | Interconnect | Acumatica Distribution + CRM + PA | Acumatica | Implementation | Distribution | ZA | SME | AM approval required |
| REF-HB-001 | Hollywood Bets | Oracle HCM (multiple phases) | Oracle-Fusion | Implementation | Entertainment/Gaming | ZA | Enterprise | **AM approval required at EACH tender — no standing approval** |
| REF-ORA-011 | (Reserved) | — | — | — | — | — | — | — |

**Total approved references: 15 confirmed + 1 reserved. Reference pool = 15 usable letters.**

> Note: REF-ACU-002 is not assigned. If encountered in existing documents, treat as unregistered — do not use until registered in REFERENCE_MASTER.csv with signed letter confirmed.

---

## 3. Exclusion Rules (Applied Before Scoring)

Exclusion rules take absolute precedence over scoring. A reference matching any exclusion rule is removed from the pool entirely.

| Rule ID | Rule | References Affected |
|---|---|---|
| EX-001 | Only signed letters held in `04_References/` — unsigned or missing letters are automatically excluded | All references — verify against `04_References/` before selection |
| EX-002 | DFA (Dimension Data Financial Advisors): never named externally (Rule 21.4 PERMANENT) | Any reference that reveals DFA as client |
| EX-003 | CCBA: never named externally | Any reference citing CCBA |
| EX-004 | SAA (South African Airways): never named as client | Any reference citing SAA |
| EX-005 | Redpath Mining: not referenceable (Rule 21.5 PERMANENT) | Any reference citing Redpath |
| EX-006 | Hollywood Bets: AM approval required at each tender — no standing approval | REF-HB-001: remove from pool until AM approval confirmed for this tender |
| EX-007 | Vintage rule: references older than 5 years must be flagged | Flag any reference where engagement go-live > 5 years before tender submission date; include but mark VINTAGE-FLAG |
| EX-008 | Scope restriction: Mr Price (REF-ORA-006) = Learning Cloud scope only | If tender does not include Learning Cloud → exclude REF-ORA-006 entirely |
| EX-009 | KPMG: not named (AM-W4E3-001 ACTIVE) | Any reference citing KPMG as client — hold until signed letter registered |
| EX-010 | Platform mismatch: if `primary_platform = Acumatica` — Oracle references score near-zero but may be included for company credibility (REF-ORA-007 always eligible) | Oracle-specific references excluded from BOM 14 pool |
| EX-011 | Platform mismatch: if `primary_platform = BeBanking` — references must relate to BeBanking or Oracle EBS | Only REF-ORA-010 (WITS — EBS + BeBanking) and REF-ORA-007 eligible |
| EX-012 | AM approval status: any reference where AM approval has not been obtained for this specific tender must be marked PENDING and cannot be confirmed in the proposal | All references — check approval status per tender |

---

## 4. Scoring Matrix

After exclusion rules are applied, remaining references are scored on 7 dimensions (maximum 10 points).

| Dimension | Max Points | Scoring Logic |
|---|---|---|
| **Product Match** | 3 | 3 = exact same product(s) as tender scope; 2 = same product family (e.g. EBS vs Fusion ERP); 1 = same Oracle platform broadly; 0 = different platform |
| **Platform Match** | 2 | 2 = exact platform (e.g. both Oracle EBS); 1 = related platform (e.g. Fusion ERP and EBS = related); 0 = different platform |
| **Engagement Architecture** | 2 | 2 = same engagement type (e.g. both AMS; both implementation); 1 = related (e.g. AMS reference for implementation tender — shows ongoing relationship); 0 = unrelated |
| **Industry / Sector** | 1 | 1 = exact industry match; 0 = different industry |
| **Country** | 1 | 1 = same country (ZA to ZA = 1); 0 = different country |
| **Customer Size** | 1 | 1 = same size tier (Enterprise/Mid-market/SME); 0 = different tier |
| **Scope Overlap** | 0–1 composite | Partial: awarded as a fraction of 1 point based on how many tender scope elements the reference covers |

**Total maximum: 10 points**

**Scoring tie-breaker:** If two references have the same score, prefer the one with the more recent engagement completion date.

**VINTAGE-FLAG adjustment:** If a reference is flagged for age (EX-007), reduce the score by 1 point to reflect reduced relevance. Still include in pool but mark VINTAGE-FLAG.

---

## 5. Reference Scoring Examples

### Example A: ARM IT045 (Oracle EBS AMS — Mining — ZA)

Tender profile: Oracle-EBS, AMS engagement, Mining, ZA, Enterprise

| Ref ID | Client | Product (3) | Platform (2) | Architecture (2) | Industry (1) | Country (1) | Size (1) | Scope (1) | Total | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| REF-ORA-008 | ARM | 3 — EBS exact match; OIC exact match; AMS exact | 2 — Oracle-EBS | 2 — AMS = AMS | 1 — Mining | 1 — ZA | 1 — Enterprise | 1 — EBS+OIC+AMS | **10/10** | #1 — perfect score; is the tender client — note: may be sensitive to use; AM approval required |
| REF-ORA-004 | Assore | 3 — EBS exact match | 2 — Oracle-EBS | 1 — Implementation (close) | 1 — Mining | 1 — ZA | 1 — Enterprise | 0.5 — EBS match; no AMS | **9.5/10** | #2 |
| REF-ORA-005 | Adcock Ingram | 3 — EBS exact match | 2 — Oracle-EBS | 1 — Implementation | 0 — Manufacturing | 1 — ZA | 1 — Enterprise | 0.5 | **8.5/10** | #3 |
| REF-ORA-009 | MTN | 2 — EBS DBA match | 2 — Oracle-EBS | 1 — DBA/Managed (related) | 0 — Telecom | 1 — ZA | 1 — Enterprise | 0.5 | **7.5/10** | #4 |
| REF-ORA-007 | Oracle Corp SA | 1 — Oracle broadly | 2 — Oracle | 0 | 0 | 1 — ZA | 1 — Enterprise | 0.5 | **5.5/10** | Eligible but lower relevance |
| REF-ORA-001 | Investec | 0 — Fusion Financials; wrong product | 0 — Oracle-Fusion | 1 — Implementation | 0 | 1 | 1 | 0 | **3/10** | Low score; different platform |
| REF-HB-001 | Hollywood Bets | 0 | 0 — Oracle Fusion | 1 | 0 | 1 | 1 | 0 | **3/10** | EXCLUDED per EX-006 pending AM approval |
| REF-ACU-* | Acumatica refs | 0 | 0 | 0 | 0 | 1 | varies | 0 | **1/10** | EXCLUDED EX-010 (platform mismatch) |
| REF-ORA-006 | Mr Price | 0 | 0 | 0 | 0 | 1 | 1 | 0 | **2/10** | EXCLUDED EX-008 (Learning only) |

**Selected pool for ARM IT045:** REF-ORA-008 (#1), REF-ORA-004 (#2), REF-ORA-005 (#3), REF-ORA-009 (#4)

**Note on REF-ORA-008:** This reference is ARM themselves. BU Lead must confirm whether ARM is comfortable with their own reference letter being cited back to them. This is common practice but must be confirmed with the Account Manager.

---

### Example B: Oracle Fusion HCM Full Suite — Retail — ZA

| Ref ID | Client | Product (3) | Platform (2) | Architecture (2) | Industry (1) | Country (1) | Size (1) | Scope (1) | Total |
|---|---|---|---|---|---|---|---|---|---|
| REF-HB-001 | Hollywood Bets | 3 — HCM multi-phase | 2 — Oracle-Fusion | 2 — Implementation | 0 — Entertainment | 1 — ZA | 1 | 1 | **10/10 pending AM** |
| REF-ORA-006 | Mr Price | 2 — HCM (Learning) | 2 — Oracle-Fusion | 2 — Implementation | 1 — Retail | 1 — ZA | 1 | 0.5 | **9.5/10 — Learning scope only** |
| REF-ORA-007 | Oracle Corp SA | 1 — Oracle broadly | 2 | 0 | 0 | 1 | 1 | 0.5 | **5.5/10** |

**Selected pool:** REF-HB-001 (pending AM approval), REF-ORA-006 (Learning scope flag — C-W3-002), REF-ORA-007

---

### Example C: Acumatica ERP — Manufacturing — ZA

| Ref ID | Client | Score | Notes |
|---|---|---|---|
| REF-ACU-003 | Maxiflex | 10/10 | Acumatica Manufacturing exact match |
| REF-ACU-004 | At Source | 9/10 | Manufacturing + WMS; SME size |
| REF-ACU-001 | Dunlop | 7/10 | Distribution scope; right platform |
| REF-ORA-007 | Oracle Corp SA | 2/10 | Platform mismatch; company credibility only |
| All Oracle refs | — | ≤3/10 | EXCLUDED per EX-010 (platform mismatch) |

---

## 6. Selection Algorithm

### Step RS-01 — Apply Exclusion Rules
Filter the full reference inventory against all 12 exclusion rules. Output: eligible pool (may include PENDING references pending AM approval).

### Step RS-02 — Score Eligible References
Apply the 7-dimension scoring matrix to each eligible reference. Record per-dimension scores and total.

### Step RS-03 — Rank and Select
Sort by total score (descending). Apply vintage flag adjustments (−1 point). Select top-ranked references:
- Minimum selection: 2 references
- Standard selection: 3–4 references
- Maximum selection without BU Lead approval: 5 references

If the pool has fewer than 2 eligible references after exclusions → flag as SEV-1 gap (GAP-003 level: References unconfirmed).

### Step RS-04 — Apply Quantity Rule
If RFP specifies a reference count requirement (from `reference_requirements` field):
- Match the required count
- If required count exceeds available eligible pool → flag as gap

### Step RS-05 — Record AM Approval Status
For each selected reference, record approval status:
- CONFIRMED: AM has explicitly approved use of this letter for this tender
- PENDING: Eligible but AM approval not yet obtained
- EXCLUDED: Removed by exclusion rule

No reference may be marked CONFIRMED in the proposal without explicit AM approval. PENDING references appear as `[REFERENCE PENDING AM APPROVAL — [Client Name]]` in the draft.

### Step RS-06 — Output Reference Pool
Produce the `reference_pool[]` array for the Tender Profile:

```yaml
reference_pool:
  - ref_id: "REF-ORA-008"
    client: "African Rainbow Minerals"
    score: 10
    rank: 1
    am_approval_status: "PENDING"
    am_approval_note: "Confirm ARM comfortable with own reference cited"
    vintage_flag: false
    scope_restriction: null
  - ref_id: "REF-ORA-004"
    client: "Assore"
    score: 9.5
    rank: 2
    am_approval_status: "PENDING"
    am_approval_note: ""
    vintage_flag: false
    scope_restriction: null
```

---

## 7. AM Approval Workflow

### Rule: No Standing Approval

AM approval for a reference letter is granted per-tender. Approval at the previous tender does not carry forward. The Account Manager must confirm, before each proposal is finalised, that:
1. The client has not withdrawn permission to be cited
2. The letter content is still accurate and the client relationship is current
3. Any sensitivity concerns (active disputes, competitive dynamics) are resolved

### Workflow Steps

| Step | Action | Owner | Timing |
|---|---|---|---|
| 1 | Tender Profile produced; reference_pool with PENDING status | Factory (automated) | Stage 0 / TIL |
| 2 | BU Lead sends reference request to Account Manager | BU Lead | Before proposal assembly begins |
| 3 | Account Manager confirms approval or denies for each reference | Account Manager | Before proposal draft complete |
| 4 | Reference pool updated with CONFIRMED or EXCLUDED status | BU Lead | Before S-67 assembly |
| 5 | If EXCLUDED after draft written: replace with next-ranked eligible reference | BU Lead | Before QA |
| 6 | Final confirmed list recorded in proposal assembly report | Factory | Stage 7 |

### Escalation Triggers

| Condition | Escalation |
|---|---|
| Hollywood Bets required and AM not reachable | Do not include; use next-ranked reference |
| Fewer than 2 references confirmed | SEV-1 blocker — B3 on readiness dashboard |
| RFP minimum reference count not met | Flag in Gap Register; discuss with BU Lead |
| Vintage-flagged reference is only available option | Use with contemporary framing; note in assembly report |

---

## 8. Cross-BU Reference Rules

When a tender spans multiple platforms (e.g. Oracle EBS + BeBanking):
- Select references relevant to each platform component
- Oracle references score against the Oracle scope; Acumatica/BeBanking references score against their scope
- REF-ORA-010 (WITS — EBS + BeBanking) is the only reference covering both — prioritise for cross-BU tenders

---

*REFERENCE_SELECTION_ENGINE.md v1.0 | WP18C.3 — Tender Intelligence Layer | 2026-06-25*  
*Companion: REFERENCE_MASTER.csv | 04_References/ | PROPOSAL_FACTORY_ARCHITECTURE.md*
