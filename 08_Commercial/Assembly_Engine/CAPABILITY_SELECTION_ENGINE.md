---
document_id: CAPABILITY-SELECTION-ENGINE
title: "Capability Selection Engine — BOM-to-Asset Lookup and Governance Rules"
version: "1.0"
status: "Approved — WP18C.3"
created: "2026-06-25"
created_by: "WP18C.3 — Tender Intelligence Layer"
category: "Architecture / Intelligence Layer"
scope: "Defines the deterministic BOM-to-capability-asset lookup table for all 16 BOMs. For each BOM: required assets, optional assets, section assignments, and applicable governance restrictions. Replaces manual capability selection (Stages 4 in WP18C). Input: bom_triggers from Tender Profile. Output: capability_assets_required + capability_assets_optional + section assignments."
---

# Capability Selection Engine

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18C.3 — Tender Intelligence Layer  
**Input:** `bom_triggers[]` from Tender Profile Block G  
**Output:** `capability_assets_required[]`, `capability_assets_optional[]`, section assignments, governance restrictions per asset

---

## 1. Purpose

The Capability Selection Engine converts BOM triggers from the Tender Profile into a governed list of capability assets that the factory will assemble into the proposal. It replaces the manual Stage 4 process identified in WP18C.1 as fully rule-based (AO-001).

**Selection principle:** Only assets with `approved_for_reuse: Yes` (from MASTER_CAPABILITY_INDEX.md) may be selected. Assets marked RETIRED or ARCHIVED are automatically excluded. Governance restrictions are applied per asset, not per proposal.

---

## 2. Standard Corporate Block

The Standard Corporate Block is always included in every proposal, regardless of BOM triggers. It is not conditional.

| Asset ID | Section | Notes |
|---|---|---|
| W1S1-001 | S-03 — Company Overview | Validate: year counts current (2002 = 24+ years in 2026); headcount = "more than 50 Senior Consultants" ONLY — never "100+" or "110+"; no Nigeria/Uganda/Ghana/Bangladesh/Qatar |
| W1S1-007 | S-06 — Delivery Model | No governance restrictions |
| W1S1-008 | S-07 — Geographic Presence | No governance restrictions |
| W1S1-009 | S-08 — Key Differentiators | No governance restrictions |
| COMP-001 | S-59 / A-05 — B-BBEE Certificate | Expiry check: Level 3 expires 2026-07-31 — OAR-A01 ACTIVE |
| COMP-002 | S-55 — Compliance Schedule | Verify all compliance items current |
| COMP-004 | S-57 — Tax Clearance | Check expiry date |
| COMP-011 | S-58 — Directors' Resolution | Check currency |

**Enterprise additions** (include for tenders with contract value indicators suggesting corporate procurement):

| Asset ID | Section | Notes |
|---|---|---|
| COMP-006 | S-56 — Company Registration (CIPC) | Annually current |
| COMP-007 | S-60 — Public Liability Insurance | Expiry check |
| COMP-008 | S-60 — Professional Indemnity | Expiry check |
| COMP-009 | S-64 — ISO / Other Certifications | Include if held and RFP-relevant |

---

## 3. BOM Capability Lookup Table

### BOM 1 — Oracle HCM Full Suite

**Trigger condition:** `oracle_products` includes HCM AND `modules_in_scope` has ≥4 HCM modules

| Status | Asset ID | Section(s) | Governance / Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 — Oracle Partnership | OPN Level 1 ONLY — Gold Partner EXPIRED 2021 (GOV-006) |
| Required | W2S1-005 | S-34 — Implementation Methodology | EXCLUDED for AMS (Pattern 13) |
| Required | W3S1-001 | S-16 — Oracle Fusion HCM Capability | Core HCM foundation capability |
| Required | W3S1-007 | S-16 + S-48 — HCM Core plus brief profiles | Section 14.2 content NEVER in external submissions |
| Required | W4-HCM-002 | S-16 — Journeys / Onboarding | — |
| Required | W4-AI-002 | S-16 — AI Skills / Dynamic Skills Cloud | Do NOT conflate with ODA or Oracle Grow |
| Optional | W3S1-002 | S-16 — Talent Management | Include if Talent in scope |
| Optional | W3S1-003 | S-16 — Oracle Recruiting Cloud | Include if Recruiting in scope; DFA Taleo = internal only (Rule 21.4) |
| Optional | W3S1-004 | S-16 — Oracle Learning Cloud | Include if Learning in scope |
| Optional | W3S1-005 | S-16 — Oracle Workforce Compensation | **G-001: Mining sector ONLY** — exclude if industry ≠ Mining |
| Optional | W3S1-006 | S-16 — HCM Analytics | Include if analytics/reporting emphasis |
| Optional | W3S1-008 | S-16 — (content as applicable) | Section 14.2 NEVER in external submissions; **W1S2-008 ARCHIVED — never use** |
| Optional | W3S1-009 | S-19 — Oracle OIC / Integration | Section 13.2 NEVER in external submissions; HIST-018 billing NEVER external |
| **DESELECTED** | W4-HCM-004 | — | **RETIRED — NEVER select** (automatic deselection) |

### BOM 2 — Oracle HCM Base

**Trigger condition:** Oracle HCM with ≤3 modules OR HCM base only

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | GOV-006 |
| Required | W2S1-005 | S-34 | EXCLUDED for AMS |
| Required | W3S1-001 | S-16 | — |
| Required | W3S1-007 | S-16 | Section 14.2 never external |
| Required | W4-HCM-002 | S-16 | — |
| Optional | W4-AI-002 | S-16 | If AI Skills in scope |
| Optional | W3S1-006 | S-16 | If analytics emphasis |

### BOM 3 — Oracle Recruiting Cloud

**Trigger condition:** Recruiting module explicitly in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W3S1-003 | S-16 | DFA Taleo: internal only (Rule 21.4); Redpath Recruiting: Rule 21.5 |
| Optional | W4-HCM-002 | S-16 | If Journeys/Onboarding also in scope |

### BOM 4 — Oracle Learning Cloud

**Trigger condition:** Learning Cloud explicitly in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W3S1-004 | S-16 | — |
| Optional | W3S1-006 | S-16 | If SETA/analytics emphasis |
| Reference note | REF-ORA-006 | S-67 | Mr Price = Learning Cloud scope ONLY (C-W3-002) — never claim broader HCM |

### BOM 5 — Oracle Talent Management

**Trigger condition:** Talent / Performance management in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W3S1-002 | S-16 | — |
| Optional | W3S1-006 | S-16 | If 9-box analytics emphasis |

### BOM 6 — Oracle Workforce Compensation

**Trigger condition:** Compensation / salary review cycle in scope — **Mining sector ONLY**

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W3S1-005 | S-16 | **G-001 PERMANENT: Mining sector ONLY. Retail attribution PROHIBITED. No Tier 1 client.** Auto-deselect if `industry ≠ Mining` |

**Deselection trigger:** If `client_profile.industry ≠ Mining` AND BOM-6 is triggered → auto-deselect W3S1-005; log deselection reason G-001 in capability selection output.

### BOM 7 — Oracle Journeys / Onboarding

**Trigger condition:** Journeys or onboarding module in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W4-HCM-002 | S-16 | — |
| Required | W3S1-001 | S-16 | Core HCM context |

### BOM 8 — Oracle AI Skills

**Trigger condition:** AI Skills / Dynamic Skills Cloud in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W4-AI-002 | S-16 | Do NOT conflate with ODA or Oracle Grow — AI Skills = Dynamic Skills Cloud only |
| Required | W3S1-002 | S-16 | Talent foundation context |

### BOM 9 — Oracle OIC Integration

**Trigger condition:** OIC / Oracle Integration Cloud in scope (standalone or as part of HCM/ERP)

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W4-INT-001 | S-19 | HIST-018 billing (R825,170) MUST NEVER appear in external submissions |
| Required | W2S1-001 | S-17 | Oracle Fusion context (if applicable) |
| Optional | W3S1-009 | S-19 | Only if HCM ↔ payroll integration; Section 13.2 NEVER in external submissions |

### BOM 10 — Oracle Fusion Financials

**Trigger condition:** Oracle Fusion Financials (GL, AP, AR, Fixed Assets, Cash Management) in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W4-ERP-001 | S-17 | — |
| Required | W2S1-001 | S-17 | Oracle Fusion ERP foundation |
| Required | W2S1-005 | S-34 | EXCLUDED for AMS |
| Optional | W4-INT-001 | S-19 | If OIC bank integration in scope |
| Optional | W4-ERP-002 | S-17 | If Procurement also in scope |

### BOM 11 — Oracle Fusion Procurement

**Trigger condition:** Oracle Fusion Procurement (Purchasing, Sourcing, Supplier Portal) in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W4-ERP-002 | S-17 | — |
| Required | W2S1-001 | S-17 | — |
| Required | W2S1-005 | S-34 | EXCLUDED for AMS |
| Optional | W4-ERP-001 | S-17 | If Financials also in scope |

### BOM 12 — Oracle PPM

**Trigger condition:** Oracle Project Portfolio Management in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | — |
| Required | W4-ERP-003 | S-17 | — |
| Required | W2S1-001 | S-17 | — |
| Reference note | — | S-67 | **AM-W4E3-001 ACTIVE — KPMG must NOT be named; use anonymous reference only until signed letter registered** |

### BOM 13 — Oracle EBS

**Trigger condition:** Oracle E-Business Suite implementation or AMS

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-003 | S-09 | GOV-006 |
| Required | W2S1-002 | S-18 | **Vintage content 2012–2014 — flag for modernisation** before submission; verify statistics |
| Required | W2S1-005 | S-34 | EXCLUDED for AMS (Pattern 13) |
| Optional | W2S1-003 | S-20 — Oracle DBA Capability | Include if DBA scope in tender; verify stats |
| Optional | W4-INT-001 | S-19 | If OIC migration or integration in scope |

### BOM 14 — Acumatica ERP

**Trigger condition:** Acumatica ERP in scope (any modules)

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-004 | S-10 — Acumatica Partnership | Verify certificate currency |
| Required | W5-METH-001 | S-34 — Platform-agnostic Methodology | — |
| Required | W1S1-007 | S-06 | Already in Standard Corporate Block |
| Module-conditional | W1S2-001 | S-23 — Acumatica Financials | If Acumatica-Financials in scope |
| Module-conditional | W1S2-002 | S-24 — Acumatica Distribution | If Acumatica-Distribution in scope |
| Module-conditional | W1S2-003 | S-27 — Inventory Management | If Inventory in scope |
| Module-conditional | W1S2-004 | S-25 — Acumatica Manufacturing | If Acumatica-Manufacturing in scope; HyDac sole KB source |
| Module-conditional | W1S2-005 | S-26 — Acumatica CRM | If CRM in scope |
| Module-conditional | W1S2-006 | S-27 — Field Services | If Field Services in scope |
| Module-conditional | W1S2-007 | S-27 — PaySpace Integration | If PaySpace integration in scope |
| Module-conditional | W1S2-009 | S-27 — Project Accounting | If PA in scope |
| Optional | W5-ACU-001 | S-28 — Acumatica Managed Services | If AMS in scope for Acumatica |
| Assumption pack | — | — | Acumatica Base pack: **Approved v1.0 (WP15C 2026-06-18) — 152 assumptions** — `08_Commercial/Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` |
| Compliance gap | COMP-016 | S-63 | Acumatica Partner Certificate MISSING — flag OAR-E03 |
| **DESELECTED** | W1S2-008 | — | **ARCHIVED — NEVER select** |

### BOM 15 — BeBanking

**Trigger condition:** BeBanking H2H platform in scope

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required | W1S1-005 | S-11 — BeBanking Product Overview | — |
| Required | W1S3-001 | S-29 — BeBanking H2H | Core H2H banking capability |
| Required | W1S3-002 | S-29 | — |
| Required | W1S3-008 | S-29 — Architecture | — |
| Module-conditional | W1S3-003 | S-29 | If Supplier Payments in scope |
| Module-conditional | W1S3-004 | S-29 | If Payroll Payments in scope; Oracle EBS/Fusion payroll SOR only — no Acumatica payroll |
| Module-conditional | W1S3-005 | S-29 | If Forex in scope |
| Module-conditional | W1S3-006 | S-29 | If ERP Integration in scope |
| Module-conditional | W1S3-007 | S-29 | If Security architecture required |
| Module-conditional | W1S3-009 | S-29 | If Hosting in scope |
| Module-conditional | W1S3-010 | S-29 | If Monitoring in scope |
| Assumption pack | — | — | BeBanking Base pack: **Approved v1.0 (WP14F 2026-06-18) — 117 assumptions** — `08_Commercial/Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` |
| Restriction | — | — | SAP = environments only. SWIFT = bank-intermediated only. Payroll H2H = Oracle EBS/Fusion sources only |

### BOM 16 — AMS / Managed Services

**Trigger condition:** `engagement_type = AMS` or `support_scope = YES`

| Status | Asset ID | Section(s) | Notes |
|---|---|---|---|
| Required (Oracle AMS) | W2S1-004 | S-21, S-70–76 | Use for Oracle (EBS, Fusion) AMS engagements |
| Required (Acumatica AMS) | W5-ACU-001 | S-28, S-70–76 | Use for Acumatica AMS engagements |
| Commercial | — | S-73 | AMS CRs always T&M — never fixed price; CR threshold = 2 hours |
| Restriction | — | — | Named consultant not guaranteed — do not commit named resources; 24x7/proactive monitoring excluded unless contracted |

---

## 4. Capability Selection Output Format

The engine produces a `[TENDER_ID]_CAPABILITY_SELECTION.md` file with the following structure per selected asset:

```yaml
capability_selection:
  tender_id: ""
  total_required: 0
  total_optional: 0
  standard_corporate_block: [W1S1-001, W1S1-007, W1S1-008, W1S1-009, COMP-001, COMP-002, COMP-004, COMP-011]

  selected_assets:
    - asset_id: ""
      status: "Required / Optional"
      source_bom: ""
      section_assignment: []
      governance_restrictions: []
      human_review_required: true/false
      review_reason: ""

  deselected_assets:
    - asset_id: ""
      deselection_reason: ""
      rule_applied: ""
```

---

## 5. Governance Deselection Rules

These rules are applied automatically during capability selection. Any asset matching a deselection rule is removed from the selection list and logged.

| Rule | Asset(s) | Condition | Action |
|---|---|---|---|
| RETIRED | W4-HCM-004 | Always | Auto-deselect; log "RETIRED — never use" |
| ARCHIVED | W1S2-008 | Always | Auto-deselect; log "ARCHIVED — never use" |
| G-001 Mining Only | W3S1-005 | `industry ≠ Mining` | Deselect; log "G-001: Compensation asset restricted to Mining sector" |
| GOV-006 Gold Partner | W1S1-003 | Always | Include but flag: language must say "Level 1 Partner" — Gold Partner language never permitted |
| Rule 21.4 DFA | W3S1-003 (Recruiting) | DFA as client or reference | Ensure DFA Taleo content is internal only; redact for external |
| Rule 21.5 Redpath | Any asset mentioning Redpath | Always | Auto-exclude Redpath Mining from any asset content in external submission |
| C-W3-002 Mr Price | REF-ORA-006 (Learning) | BOM ≠ BOM-4 (Learning) | Exclude if not Learning Cloud scope; never claim broader HCM |
| Section 13.2 | W3S1-009 | Always | Include asset but flag: Section 13.2 content NEVER in external submissions |
| HIST-018 | W4-INT-001 | Always | Include asset but flag: billing amounts (R825,170) NEVER in external submissions |
| Section 14.2 | W3S1-007/008 | Always | Include asset but flag: Section 14.2 content NEVER in external submissions |
| AM-W4E3-001 | BOM 12 references | Always | KPMG not named; use anonymous reference |

---

## 6. Human Review Triggers

The following assets require human review before the assembled section is approved for submission:

| Asset | Section | Review Required For |
|---|---|---|
| W1S1-001 | S-03 | Validate year counts (current from 2002); headcount language; no unsupported geographies |
| W2S1-002 | S-18 | Vintage content 2012–2014 — modernise statistics and examples before critical tender submissions |
| W2S1-003 | S-20 | Verify DBA stats are current |
| W1S1-003 | S-09 | OPN revalidation — confirm Level 1 status current; no Gold Partner language |
| W1S1-004 | S-10 | Acumatica partner certificate currency |
| W4-ERP-003 | S-17 (PPM) | Confirm anonymous reference only — KPMG AM-W4E3-001 active |
| COMP-001 | S-59 | B-BBEE expiry 2026-07-31 — OAR-A01 — confirm renewal before submission |
| Any OCI content | S-22 | OCI capability asset absent (GAP-004) — AI-GENERATE required; human review mandatory |

---

## 7. Examples

### Example 1: ARM IT045 (Oracle EBS AMS)

**BOM triggers:** BOM-13, BOM-16  
**Standard Corporate Block:** always included

**Required assets:**
- W1S1-001 (S-03), W1S1-007 (S-06), W1S1-008 (S-07), W1S1-009 (S-08) — Corporate Block
- W1S1-003 (S-09) — Oracle Partnership
- W2S1-002 (S-18) — Oracle EBS Capability [flag: vintage content]
- W2S1-004 (S-21/S-70–76) — Oracle Managed Services
- COMP-001/002/004/011 — Compliance Block

**Deselected:**
- W2S1-005: EXCLUDED (AMS — Pattern 13; S-34 not in scope)
- W4-HCM-004: RETIRED

**Optional assets (BU Lead selects):**
- W2S1-003 (S-20) — Oracle DBA Capability (include if DBA scope confirmed)
- W4-INT-001 (S-19) — OIC Integration (include for OIC scope)

---

### Example 2: Oracle Fusion HCM Full Suite (Mining sector)

**BOM triggers:** BOM-1, BOM-6 (Compensation — Mining), BOM-9 (if OIC)

**Required assets:**
- Standard Corporate Block
- W1S1-003 (S-09)
- W2S1-005 (S-34)
- W3S1-001 (S-16)
- W3S1-007 (S-16/S-48)
- W4-HCM-002 (S-16)
- W4-AI-002 (S-16)
- W3S1-005 (S-16) — Compensation [G-001 CONFIRMED — Mining sector only]

**Optional:** W3S1-002/003/004/006 per module scope

---

### Example 3: Acumatica ERP (Manufacturing + Distribution)

**BOM triggers:** BOM-14 (Acumatica)

**Required assets:**
- Standard Corporate Block
- W1S1-004 (S-10) — Acumatica Partnership [verify certificate]
- W5-METH-001 (S-34)
- W1S2-004 (S-25) — Manufacturing
- W1S2-002 (S-24) — Distribution

**Assumption pack:** Acumatica Base — Approved v1.0 (WP15C 2026-06-18) — 152 assumptions

**Gap to flag:**
- COMP-016 Acumatica Partner Certificate MISSING (OAR-E03)

---

### Example 4: BeBanking H2H (Supplier + Payroll Payments)

**BOM triggers:** BOM-15 (BeBanking) + BOM-13 if Oracle EBS is payroll SOR

**Required assets:**
- Standard Corporate Block
- W1S1-005 (S-11) — BeBanking Product Overview
- W1S3-001, W1S3-002, W1S3-008 (S-29) — Core H2H capability
- W1S3-003 (S-29) — Supplier Payments
- W1S3-004 (S-29) — Payroll Payments [Oracle EBS/Fusion SOR only]

**Restriction to apply:** Payroll H2H requires Oracle EBS or Oracle Fusion as payroll SOR. If client uses Acumatica for payroll → not supported. Raise as gap.

**Assumption pack:** BeBanking Base — Approved v1.0 (WP14F 2026-06-18) — 117 assumptions

---

*CAPABILITY_SELECTION_ENGINE.md v1.0 | WP18C.3 — Tender Intelligence Layer | 2026-06-25*  
*Companion: TENDER_BOM_LIBRARY.md | MASTER_CAPABILITY_INDEX.md | PROPOSAL_PATTERN_ENGINE.md*
