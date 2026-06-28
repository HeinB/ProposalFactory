---
document_id: W4-HCM-004-ORA-TimeLabour
title: "Oracle Time and Labour — Capability Statement"
version: "1.0 Candidate Draft"
status: "Retired"
review_status: "Retired"
approved_for_reuse: "No"
business_unit: "Oracle"
wave: "4"
deliverable: "W4-HCM-004"
created: "2026-06-14"
created_by: "Claude (AI — Wave 4 W4-HCM-004 extraction)"
source_document: "HIST-016 (SABS ETS RFP Response Dec 2025 — Mr Price Group confirmed as Oracle Fusion HCM + Time and Labour client); ORACLE_FACT_BASELINE Section 11 (Mr Price Group — Oracle Fusion HCM including T&L scope confirmed); HIST-006 (SAA RFP Section 2 — Time and Labour module listed — SAA NEVER NAMED Rule 21.1); HIST-015 (Afrocentric Health HCM Proposal V4.0 — Phase 4 Time and Labour — Afrocentric NOT NAMED externally); C-W3-002 (Mr Price governance: Learning Cloud = implementation; broader HCM estate = support only — T&L scope to be confirmed precisely)"
source_status: "Tier 1 Confirmed Delivery (Mr Price Group — Oracle Fusion HCM + T&L confirmed in SABS ETS); Tier 2 Platform Capability (HIST-006 — SAA internal only; HIST-015 — Afrocentric internal only)"
prereq_statement: "W3S1-007-ORA-WorkforceManagement (companion Workforce Management statement — W3S1-007 covers Absence Management as primary with T&L secondary; W4-HCM-004 positions T&L as the primary module for T&L-specific tenders); W3S1-001-ORA-HCMCore (Oracle HCM Core — mandatory foundation)"
kb_destination: "06_Capabilities/Oracle/Oracle_HCM/"
tags: "Oracle,HCM,Time and Labour,T&L,Timesheets,Shift Scheduling,Labour Compliance,Oracle Fusion HCM,Workforce,Labour Analytics"
---

> **RETIRED — BU Lead decision 2026-06-14**
>
> W4-HCM-004 retired by BU Lead decision. Existing Time & Labour capability content remains governed through W3S1-007 Oracle Workforce Management. No standalone Time & Labour capability statement will be maintained until production implementation evidence becomes available.
>
> **Reason:** Oracle Time & Labour work was performed at Mr Price Group (proof-of-concept); the initiative did not proceed into a production implementation and APPSolve is not currently supporting the client for T&L. OI-W4H4-001 resolved: Tier 3 PoC — not eligible for promotion as a standalone approved statement.

> **CRITICAL GOVERNANCE NOTE — C-W3-002:** Mr Price Group governance rule C-W3-002 is active for this statement. Mr Price scope: Oracle Fusion HCM **Learning Cloud = implementation confirmed**. Broader HCM estate (including T&L) = **support scope, not confirmed implementation**. BU Lead review must confirm whether the T&L reference for Mr Price Group is: (a) implementation (delivered T&L in scope with APPSolve as implementer), or (b) support (APPSolve supporting an existing T&L implementation). The evidence classification below reflects the SABS ETS confirmed T&L scope, but the implementation vs. support distinction must be confirmed before this statement is approved for external use.

---

# Oracle Time and Labour (Standalone)

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W4-HCM-004-ORA-TimeLabour | Version: 1.0 Candidate Draft | Wave 4*

---

## Section 1: Statement of Capability

APPSolve configures, implements, and supports Oracle Time and Labour (T&L) — Oracle's enterprise workforce time capture and labour management module within Oracle Fusion HCM. Oracle T&L enables organisations to capture, validate, and process employee time across shift-based, project-based, and standard hour environments, with full integration to payroll processing and labour analytics.

This statement positions Oracle T&L as a primary capability — distinct from W3S1-007 (Oracle Workforce Management) which covers Absence Management as its primary scope with T&L as a secondary element. W4-HCM-004 is the appropriate statement for tenders where Oracle T&L is the primary evaluation criterion.

> **Confirmed client scope:** Mr Price Group confirmed as an Oracle Fusion HCM + Time and Labour client (SABS ETS Dec 2025; ORACLE_FACT_BASELINE Section 11). BU Lead to confirm implementation vs. support scope distinction (C-W3-002 active).

| Capability Area | Coverage | APPSolve Positioning |
|---|---|---|
| **Time Entry & Timesheets** | Employee timesheet entry — daily, weekly, period-based; mobile time capture; manager approval workflows | **Confirmed delivery capability** — Oracle T&L timesheet configuration within HCM |
| **Shift Scheduling** | Shift pattern management, work schedules, rotation patterns, shift differentials | **Confirmed delivery capability** — shift-based workforce environment configuration |
| **T&L Rules Engine** | Overtime rules, premium pay triggers, rounding rules, gap fill rules, legislative compliance rules | **Confirmed delivery capability** — T&L rules engine configuration for SA and international environments |
| **Labour Cost Distribution** | Time entry → labour cost allocation to GL cost centres, departments, projects | **Confirmed delivery capability** — integrated cost allocation within Oracle ERP suite |
| **Payroll Integration** | Oracle T&L hours → OIC → PaySpace (third-party payroll); or Oracle T&L → Oracle Payroll (native) | **Confirmed delivery capability** — T&L hours feed payroll processing (OIC integration where PaySpace is payroll system of record) |
| **Absence & T&L Coordination** | T&L co-ordination with Oracle Absence Management (W3S1-007) — absence hours deducted from T&L; holiday entitlement tracking | **Confirmed delivery capability** — native integration within Oracle HCM module suite |
| **Labour Analytics** | Time entry analytics, overtime trend analysis, labour utilisation reporting (OTBI dashboards) | **Confirmed delivery capability** — OTBI-based labour analytics within Oracle HCM Analytics framework |
| **Legislative Compliance** | BCEA compliance (South African Basic Conditions of Employment Act) — overtime caps, rest periods, Sunday pay | **Confirmed delivery capability** — SA T&L legislative compliance configuration |

---

## Section 2: Product Architecture

### 2.1 Oracle Time and Labour — Time Capture to Payroll Flow

```
Time Entry Sources
  ├── Employee timesheet (Oracle HCM Self-Service / Journeys)
  ├── Shift clock-in/clock-out (biometric / badge integration via OIC)
  ├── Manager timesheet entry (on behalf of employee)
  └── Project time entry (linked to Oracle PPM — if applicable)
         │
         ▼
Oracle T&L Processing Engine
  ├── T&L Rules Engine
  │   ├── Overtime calculation (BCEA-compliant)
  │   ├── Shift differential rules (night shift, weekend, public holiday)
  │   ├── Absence deduction coordination (W3S1-007)
  │   └── Rounding and gap-fill rules
  ├── Approval Workflow
  │   ├── Manager approval
  │   └── HR exception review
  └── Time Period Close
      ├── Payroll-ready extract
      └── Labour cost distribution to GL
         │
         ▼
Integration (OIC)
  ├── T&L hours → PaySpace (third-party payroll via OIC — HIST-018 pattern)
  └── Labour costs → Oracle GL (cost centre allocation)
         │
         ▼
Reporting & Analytics
  ├── OTBI: Overtime trends, shift utilisation, labour cost by department
  └── Manager dashboards: Team time compliance, pending approvals
```

### 2.2 Distinction from W3S1-007 (Workforce Management)

| Aspect | W3S1-007 Oracle Workforce Management | W4-HCM-004 Oracle Time and Labour |
|---|---|---|
| **Primary Module** | Oracle Absence Management | Oracle Time and Labour |
| **Use Case** | Leave management, leave entitlements, absence tracking | Time capture, timesheets, shift scheduling, labour compliance |
| **Primary Evidence** | Hollywood Bets Absence Management Phase 3.3.1 | Mr Price Group Oracle Fusion HCM + T&L |
| **When to Use** | Tender requires absence management / leave as primary | Tender requires timesheet management / shift scheduling / T&L compliance as primary |
| **Overlap** | T&L and Absence Management share scheduling data — they are complementary | T&L and Absence Management are often deployed together |

---

## Section 3: Source Mapping

| Source | HIST ID | Evidence Type | Applicable Sections | Usage Restrictions |
|---|---|---|---|---|
| SABS ETS RFP Response Dec 2025 | HIST-016 | Tier 1 Confirmed Scope | Mr Price Group confirmed as Oracle Fusion HCM + T&L client | **C-W3-002 active:** Confirm implementation vs. support scope for Mr Price T&L before naming in tender. Do NOT name SABS as client (HIST-016 restriction). |
| ORACLE_FACT_BASELINE Section 11 | Internal reference | Tier 1 Confirmed Scope | Mr Price Group — Fusion HCM including T&L scope | C-W3-002 active — Mr Price Learning Cloud = implementation; T&L scope type to confirm |
| Afrocentric Health HCM Proposal V4.0 | HIST-015 | Tier 2 Platform Capability (internal) | Phase 4 — Time and Labour module included | **Afrocentric NOT NAMED externally — HIST-015 restriction** |
| SAA Oracle Fusion HCM RFP | HIST-006 | Tier 2 Platform Capability (internal) | T&L module listed in Oracle HCM scope | **SAA NEVER NAMED — Rule 21.1 (Aviation PROHIBITED)** |

---

## Section 4: Evidence Classification

| Field | Value |
|---|---|
| **Evidence Tier** | **Tier 1 — Confirmed (subject to C-W3-002 scope confirmation)** |
| **Primary Evidence** | Mr Price Group — Oracle Fusion HCM + T&L confirmed (HIST-016; ORACLE_FACT_BASELINE Section 11) |
| **Corroborative Evidence** | HIST-015 (Afrocentric — internal only); HIST-006 (SAA — internal only) |
| **Named Reference** | Mr Price Group — **C-W3-002 active.** BU Lead must confirm: is the Mr Price T&L scope an APPSolve implementation or an APPSolve support engagement? If implementation: Tier 1 named reference approved. If support: Tier 1 named reference (T&L support, not full implementation). |
| **Sector** | Retail (Mr Price Group ~50,000 employees); applicable across shift-based workforce sectors |
| **Restriction Summary** | C-W3-002 active (Mr Price scope must be confirmed precisely); SAA never named (Rule 21.1); Afrocentric not named (HIST-015); CCBA never named (HIST-014); DFA never named (Rule 21.4) |

---

## Section 5: Approved and Prohibited Wording

### Approved Wording (pending C-W3-002 confirmation)

> "APPSolve configures and implements Oracle Time and Labour within Oracle Fusion HCM, enabling organisations to capture, validate, and process employee time across shift-based, project-based, and standard-hour environments, with full integration to payroll processing and labour cost reporting."

> "APPSolve delivers Oracle T&L implementations that are configured for South African legislative compliance — including BCEA overtime rules, shift differential pay triggers, and public holiday hour management."

> "Oracle Time and Labour, implemented by APPSolve, integrates natively with Oracle Absence Management and Oracle Payroll integration (OIC ↔ PaySpace) — enabling a seamless time-to-pay cycle within the Oracle Fusion HCM platform."

### Prohibited Wording

- Do NOT name SAA as a client or example (Rule 21.1)
- Do NOT name Afrocentric Health as a client or example (HIST-015 restriction)
- Do NOT name CCBA as a client or example (HIST-014)
- Do NOT name DFA as a client or example (Rule 21.4)
- **Do NOT describe Mr Price Group as a full Oracle HCM implementation client** — C-W3-002 is active: Mr Price = Learning Cloud implementation confirmed; T&L scope type (implementation vs. support) to be confirmed by BU Lead before use in tender
- Do NOT conflate Oracle T&L with Absence Management (W3S1-007) — different modules
- Do NOT conflate Oracle T&L with BeBanking Payroll H2H (W1S3-004) — T&L captures time; BeBanking executes payment

---

## Section 6: Pre-Tender Validation Checks

Before including this capability statement in any tender submission, confirm all of the following:

- [ ] **PT-W4H4-001:** C-W3-002 scope confirmed — BU Lead has confirmed whether Mr Price T&L scope is implementation or support. This must be confirmed before naming Mr Price in any T&L-specific tender context.
- [ ] **PT-W4H4-002:** If naming Mr Price as T&L reference — account manager approval obtained
- [ ] **PT-W4H4-003:** Mr Price Group signed reference letter confirmed and registered in `04_References/Oracle/` before naming in tender
- [ ] **PT-W4H4-004:** SAA is NOT named in any T&L content — Rule 21.1
- [ ] **PT-W4H4-005:** Afrocentric Health is NOT named in any T&L content — HIST-015 restriction
- [ ] **PT-W4H4-006:** Confirm tender T&L requirements align with Oracle T&L scope (not biometric hardware provision or standalone rostering systems — those are third-party integrations, not Oracle T&L itself)
- [ ] **PT-W4H4-007:** BEE certificate validity confirmed (expires 2026-07-31)

---

## Section 7: Named Reference Controls

| Client | Reference Status | Permitted Use | Restrictions |
|---|---|---|---|
| **Mr Price Group** | **C-W3-002 active — scope to confirm** | Oracle T&L client — scope type (implementation vs. support) must be confirmed by BU Lead before naming | C-W3-002: Learning Cloud = implementation confirmed. T&L = must confirm implementation vs. support. Do not name until BU Lead confirms scope type. |
| SAA | NEVER NAMED | Internal evidence only | **Rule 21.1 — Aviation PROHIBITED permanently** |
| Afrocentric Health | NOT NAMED | Internal methodology evidence only | **HIST-015 restriction** |
| CCBA | NEVER NAMED | Internal evidence only | **HIST-014 restriction** |
| DFA | NEVER NAMED | Internal evidence only | **Rule 21.4 — permanent** |
| Redpath Mining | NOT REFERENCEABLE | Active Pipeline | **Rule 21.5** |

---

## Section 8: Product Boundary Controls

| Product | Relationship | Boundary Rule |
|---|---|---|
| **Oracle Time and Labour** | THIS STATEMENT | Oracle HCM module for time capture, timesheets, shift scheduling, T&L rules |
| **Oracle Absence Management (W3S1-007)** | Related but distinct | W3S1-007 covers absence (leave) as primary. W4-HCM-004 covers T&L (timesheets/shifts) as primary. They share scheduling data but are separate modules. |
| **Oracle HCM Core (W3S1-001)** | Mandatory prerequisite | Oracle T&L operates within Oracle Fusion HCM. W3S1-001 is the mandatory foundation. |
| **Oracle OIC Integration (W4-INT-001)** | Integration layer | T&L hours feed payroll via OIC (same pattern as W3S1-009). OIC is the mandatory integration layer. |
| **BeBanking Payroll Payments (W1S3-004)** | Downstream payment | BeBanking executes the payroll payment that results from T&L-validated hours. Do NOT conflate time management with payment execution. |
| **Biometric hardware / rostering software** | Third-party integration | Oracle T&L captures and processes time — biometric clocking hardware integrates into Oracle T&L via OIC or direct adapters. The hardware is NOT Oracle T&L. APPSolve does not supply biometric hardware. |

---

## Section 9: Extraction Log

| Field | Value |
|---|---|
| **Wave** | 4 |
| **Extraction Date** | 2026-06-14 |
| **Extractor** | Claude (AI — Wave 4 extraction authorised by BU Lead 2026-06-14) |
| **BU Lead Decision** | W4-HCM-004 Oracle Time and Labour (Standalone) — High priority; Mr Price T&L confirmed in scope; eligible for Wave 4 extraction |
| **Primary Source** | HIST-016 (SABS ETS — Mr Price confirmed T&L); ORACLE_FACT_BASELINE Section 11 |
| **Evidence Tier at Extraction** | Tier 1 (Mr Price Group — subject to C-W3-002 scope confirmation) |
| **Open Item** | **OI-W4H4-001 (BU Lead action):** Confirm whether Mr Price T&L scope is implementation or support (C-W3-002). This is a pre-promotion required item. |
| **Status** | **RETIRED — BU Lead decision 2026-06-14** |
| **Next Action** | Not applicable. W4-HCM-004 retired by BU Lead 2026-06-14. Time & Labour capability content governed through W3S1-007 Oracle Workforce Management. Do not use this file in any tender. |
| **Promotion Requirement** | N/A — Retired. No standalone T&L capability statement will be maintained until production implementation evidence becomes available. |
| **Retirement Note** | W4-HCM-004 retired by BU Lead decision. Existing Time & Labour capability content remains governed through W3S1-007 Oracle Workforce Management. No standalone Time & Labour capability statement will be maintained until production implementation evidence becomes available. |

---

*W4-HCM-004-ORA-TimeLabour-DRAFT.md v1.0 — RETIRED 2026-06-14 by Hein Blignaut (BU Lead). Do not use in tender responses. approved_for_reuse: No.*
