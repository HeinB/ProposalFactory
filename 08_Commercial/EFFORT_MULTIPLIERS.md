---
document_id: EFFORT-MULTIPLIERS
title: "APPSolve Effort Multipliers — Adjustment Factors for Implementation Estimates"
version: "1.0"
created: "2026-06-15"
created_by: "WP11F — Tender Commercial Framework"
status: "Approved — 2026-06-16"
approved_by: "Hein Blignaut (BU Lead)"
approval_ref: "WP11F-A"
applies_to: "All Oracle, Acumatica, and BeBanking implementation proposals and SOWs"
companion_docs:
  - "ESTIMATION_GUIDE.md"
  - "RATE_CARD_FRAMEWORK.md"
  - "CR_PRICING_MODEL.md"
  - "COMMERCIAL_GOVERNANCE.md"
---

# APPSolve Effort Multipliers

## 1. Purpose

Effort multipliers are adjustment factors applied to base effort estimates to account for specific engagement conditions that increase (or in limited cases, decrease) the effort required beyond the baseline. They translate engagement-specific risk and complexity into the commercial estimate.

**How multipliers work:**
```
Adjusted effort = Base effort × Multiplier
```

Where multiple multipliers apply, they are applied sequentially (or compounded, per Section 2.2).

**Multipliers do not change the daily rate.** They change the effort estimate. This preserves rate card integrity: the client sees the same daily rate regardless of engagement complexity, but the total fee reflects the correct effort.

---

## 2. Multiplier Application Rules

### 2.1 General Rules

1. Apply multipliers to the affected phase or workstream, not to the total project estimate — where a multiplier affects only one phase (e.g., data migration multiplier applies to Deploy phase only), apply it to that phase.
2. Document every multiplier applied in the commercial justification file (internal use, not shared with client).
3. Where a multiplier cannot be justified with a specific engagement condition, do not apply it.
4. Multipliers are reviewed and confirmed by the Functional Lead and BU Lead before the estimate is submitted.

### 2.2 Compounding vs. Additive

| Method | When to use | Formula |
|---|---|---|
| Additive | Multipliers affect different phases or workstreams independently | Adjusted effort = Sum of (Phase base × Phase multiplier) |
| Compounded | Multiple multipliers affect the same phase simultaneously and are interdependent | Adjusted effort = Base effort × M1 × M2 |
| Capped compound | Compounding would produce an unrealistically high estimate | Apply a cap multiplier defined by the BU Lead and Commercial Director |

The default method is **additive per phase**. Compounding is used only where explicitly justified.

---

## 3. Multiplier Categories

### 3.1 Scope Complexity Multipliers

These multipliers adjust for the inherent complexity of what is being built. They are derived from the C1–C4 complexity classification (ESTIMATION_GUIDE.md Section 4).

| Condition | Multiplier Range | Notes |
|---|---|---|
| C1 — Simple | 0.8–1.0 | May reduce base effort if the engagement is unusually well-scoped |
| C2 — Standard | 1.0 | Base estimate is C2 by default |
| C3 — Complex | 1.2–1.4 | Apply to affected module/workstream |
| C4 — Highly Complex | 1.5–1.8 | Apply to affected module/workstream; BU Lead sign-off required |

### 3.2 Legal Entity and Organisational Multipliers

These multipliers apply when the number of legal entities, operating units, or business units exceeds the base assumption.

| Condition | Multiplier | Application |
|---|---|---|
| 1 LE — base | 1.0 | No adjustment |
| 2–3 LE (same jurisdiction, same COA) | 1.1–1.2 | Apply to GL and Org setup phases |
| 2–3 LE (different jurisdictions or different COA) | 1.3–1.5 | Apply to GL, AP, FA, and Org phases |
| 4–6 LE | 1.5–1.8 | Full ERP cross-entity effort — BU Lead review required |
| 7+ LE | Assessed separately | Treat as programme, not project — BU Lead + Commercial Director to agree programme delivery model before submission |
| Multi-country (3+ countries) | +0.2–0.3 on base LE multiplier | Language, currency, statutory requirements add overhead |

### 3.3 Data Migration Multipliers

These multipliers apply to the data migration workstream effort.

| Condition | Multiplier | Notes |
|---|---|---|
| Opening balance only, clean data, client has prepared extract | 1.0 | Base assumption per ERP-DAT-006 |
| Opening balance, data cleaning required | 1.2–1.3 | Client data quality issues add reconciliation effort |
| Multiple data objects (AP + GL + FA + suppliers) | 1.1 per additional data object beyond base | Applied to total data migration effort |
| Historical data (where exceptionally approved) | 1.5–2.5 | Only with explicit commercial justification; rare |
| Large volume (>100,000 records per object) | 1.2–1.5 | Batch process design and validation adds effort |
| Third migration cycle (beyond two mock + final) | +0.5 per additional cycle | Per ERP-DAT-006 change control principle |

### 3.4 Integration Multipliers

These multipliers apply to OIC integration effort per integration.

| Condition | Multiplier | Notes |
|---|---|---|
| Simple (C1) integration | 0.9 | Well-documented, pre-built adapter, prior APPSolve experience |
| Standard (C2) integration | 1.0 | Base estimate |
| Complex (C3) integration | 1.3–1.5 | Custom transformation; limited vendor cooperation |
| Highly complex (C4) integration | 1.6–2.0 | Multi-direction; high volume; new vendor |
| New vendor (no prior APPSolve integration) | +0.2 on base | Vendor API discovery and testing overhead |
| Real-time (sub-second) integration | +0.3 on base | Performance design and testing overhead |
| Error reprocessing / recovery design | +0.2 on base | Applies where error handling is complex |
| Bi-directional integration (A→B and B→A) | Count as 2 integrations per OIC-SCP-002 | Not a multiplier — count correctly in the first place |

### 3.5 Client Readiness Multipliers

These multipliers adjust for the client's ability to participate effectively in the implementation. Poor client readiness increases APPSolve effort (more clarification cycles, more rework, more delays absorbed by APPSolve team).

**Application rule:** Client readiness multipliers are NOT applied by default. They are only applied when a specific client readiness risk factor has been identified (e.g., from the Estimation Input Model risk flags), discussed with the BU Lead, and documented in the commercial justification file. Do not apply these multipliers as a routine risk buffer.

| Condition | Multiplier | Assessment criteria |
|---|---|---|
| High client readiness | 0.9–1.0 | Experienced internal ERP team; documented requirements; data already clean; fast decision-making |
| Standard client readiness | 1.0 | Typical client engagement — some delays, some rework expected |
| Low readiness — limited internal ERP team | 1.1–1.2 | Heavy reliance on APPSolve for user decisions; slow sign-off |
| Low readiness — first ERP implementation | 1.2–1.3 | No internal ERP experience; extensive knowledge transfer required |
| Very low readiness — poor data quality | 1.1–1.5 (data workstream only) | Data cleansing is client's responsibility; but APPSolve absorbs iteration cycles |
| Slow decision-making (client governance) | 1.1–1.2 | Multiple approval layers for every design decision; design cycles take longer |

**Important:** Client readiness multipliers should be discussed with the BU Lead and Commercial Director before applying — do not apply unilaterally. They may be sensitive in client-facing contexts.

### 3.6 Timeline Multipliers

These multipliers apply when the client requires a compressed delivery timeline.

| Condition | Multiplier | Rationale |
|---|---|---|
| Standard timeline (per methodology norms) | 1.0 | No adjustment |
| Compressed by 10–20% | 1.1–1.15 | Parallel workstreams; overtime risk; additional PM overhead |
| Compressed by 20–35% | 1.2–1.3 | Significant parallel working; higher risk of rework |
| Compressed by >35% (aggressive fast-track) | 1.4–1.6 | Multi-team parallel delivery; very high risk; requires Commercial Director approval |

Timeline compression multipliers apply to the total implementation effort. They reflect the efficiency loss of parallel working, the additional management overhead, and the risk of rework from insufficient design time.

### 3.7 Geography and Travel Multipliers

| Condition | Multiplier / Supplement | Notes |
|---|---|---|
| Remote delivery (standard) | 1.0 | No adjustment — remote-first is APPSolve standard |
| Hybrid (key workshops on-site; rest remote) | 1.05–1.1 | Travel time is not billable effort; on-site day rate supplemented separately |
| Fully on-site delivery (client requirement) | 1.1–1.15 | On-site overhead; less efficient than remote configuration |
| Multi-country engagement (2+ countries) | 1.1–1.2 per additional country | Time zone overhead; multi-language documentation; additional PM effort |

Travel costs (flights, accommodation, car hire) are quoted separately at cost. They are not included in the effort estimate.

### 3.8 Resource Availability Multipliers

| Condition | Multiplier | Notes |
|---|---|---|
| Named resource confirmed and available | 1.0 | No adjustment |
| Sub-optimal resource (less experienced than ideal for scope) | 1.1–1.2 | Mentoring overhead; quality review time |
| SPOF resource risk (see CONSULTANT_SKILL_MATRIX.md) | Assessed case-by-case | BU Lead to confirm succession plan before applying |
| Team split across BUs | 1.05–1.1 | Coordination overhead for cross-BU engagements |

---

## 4. Combined Multiplier Examples

### 4.1 Example: Oracle Fusion ERP — 3 LE, Moderate Complexity

| Factor | Multiplier | Applied to |
|---|---|---|
| C3 complexity (ERP Financials) | 1.3 | Financials workstream |
| 3 LE, different COA structures | 1.4 | GL and organisation setup |
| Data migration (opening balance, multiple objects) | 1.2 | Data migration workstream |
| 2 OIC integrations (C2 standard) | 1.0 | OIC workstream |
| Standard client readiness | 1.0 | All phases |
| Standard timeline | 1.0 | All phases |
| **Standard contingency** | **+15%** | Total after multipliers |

### 4.2 Example: Oracle HCM — Fast-Track, 1 LE, No Integrations

| Factor | Multiplier | Applied to |
|---|---|---|
| C2 complexity (Core HR + Recruiting) | 1.0 | Base estimate |
| 1 LE, standard COA | 1.0 | No adjustment |
| No data migration beyond employee master | 1.0 | No adjustment |
| Timeline compressed 25% | 1.25 | Total implementation effort |
| Standard contingency | +10% | Total after multipliers |

### 4.3 Example: AMS — Elevated Complexity CR

| Factor | Multiplier | Notes |
|---|---|---|
| New OIC integration (C3) | 1.4 | Applied to integration development effort |
| Client in multi-country environment | 1.1 | Additional testing required across entities |
| Timeline compression (urgent business need) | 1.15 | Applied to full CR effort |
| Fixed-price CR risk allowance | +8% | Internal risk buffer on fixed-price |

---

## 5. Multiplier Governance

| Action | Owner |
|---|---|
| Applying multipliers ≤ 1.3 to any workstream | Functional Lead (document and justify) |
| Applying multipliers > 1.3 to any workstream | Functional Lead + BU Lead sign-off |
| Applying multipliers > 1.5 to any workstream | Commercial Director sign-off required |
| Applying client readiness multipliers | BU Lead review before applying (client sensitivity) |
| Reviewing multiplier calibration annually | BU Leads + Commercial Director |

**Written justification:** Any multiplier above 1.3 applied to any workstream must be documented in the commercial justification file with a specific explanation of the risk condition that warranted the uplift. "General project risk" is not an acceptable justification — the specific driver must be named.

---

## 6. What Multipliers Do NOT Cover

The following are separate from multipliers and must be accounted for independently:

| Item | How to handle |
|---|---|
| Travel costs | Quote separately at cost |
| Third-party software licensing | Quote separately per licence schedule |
| Third-party vendor delay (bank testing, API delays) | Risk register; T&M billing if delay causes additional APPSolve effort |
| Scope creep beyond agreed scope | Change request; do not absorb into base estimate |
| Oracle quarterly update regressions (AMS) | AMS incident management; not a multiplier |
| BeBanking bank testing phase | Bank-controlled testing is excluded from the multiplier model entirely. Bank testing scope is binary (in or out) and separately scoped or billed by milestone |

---

## 7. Decision Record

*WP11F-A — Commercial Framework Approval | 2026-06-16 | BU Lead: Hein Blignaut*

| Decision ID | Item | Decision | Applied |
|---|---|---|---|
| BU-EM-001 | Complexity multiplier ranges (0.8–1.8) | **APPROVED** — Ranges confirmed as calibrated correctly against delivered Oracle HCM projects (Hollywood Bets); ERP-specific range re-calibration may follow ERP BU Lead validation of ESTIMATION_GUIDE indicators | Section 3.1 confirmed |
| BU-EM-002 | LE multiplier tiers | **APPROVED** — LE multiplier table confirmed as correct; 7+ LE requires programme delivery model agreed by BU Lead + Commercial Director before submission | Section 3.2 updated |
| BU-EM-003 | Client readiness multipliers (routine vs explicit) | **APPROVED** — NOT applied by default; only applied when specific risk factor identified, discussed with BU Lead, and documented in commercial justification file | Section 3.5 updated |
| BU-EM-004 | Timeline compression model | **APPROVED** — Compression multiplier table (1.0 to 1.6) confirmed as consistent with delivered fast-track experience | Section 3.6 confirmed |
| BU-EM-005 | Written justification >1.3 | **APPROVED** — Written justification required in commercial file for any multiplier above 1.3; specific risk driver must be named | Section 5 updated |
| BU-EM-006 | Maximum compound multiplier cap | **DEFERRED TO COMMERCIAL DIRECTOR** — Maximum compound multiplier cap for any single engagement to be defined by BU Lead + Commercial Director; intersects with margin floor policy | CD decision item — no change applied |
| BU-EM-007 | Multipliers >1.5 and CD sign-off alignment | **APPROVED** — Confirmed aligned with Section 5 governance and COMMERCIAL_GOVERNANCE.md Section 4.1 (C4 fixed-price = RED flag) | Section 5 confirmed |
| BU-EM-008 | BeBanking bank testing exclusion | **APPROVED** — Bank testing phase excluded from multiplier model entirely; binary in/out scoping; separately billed | Section 6 updated |

**Commercial Director items outstanding: BU-EM-006**

---

*EFFORT_MULTIPLIERS v1.0 | WP11F — Tender Commercial Framework | 2026-06-15 → Approved 2026-06-16 | BU Lead: Hein Blignaut*  
*Companion: ESTIMATION_GUIDE.md · RATE_CARD_FRAMEWORK.md · CR_PRICING_MODEL.md · COMMERCIAL_GOVERNANCE.md*  
*Internal use only — do not share multiplier values or structure with clients*
