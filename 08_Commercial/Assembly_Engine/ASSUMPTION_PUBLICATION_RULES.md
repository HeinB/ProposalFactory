---
document_id: ASSUMPTION-PUBLICATION-RULES
title: "Assumption Publication Rules — Classification and External Publication Standard"
version: "1.0"
status: "Approved"
created: "2026-06-22"
created_by: "WP17D-0 — Assumption Schedule Design Standard"
category: "Assembly Engine / Publication Standard"
scope: "Defines which assumptions are published in client-facing proposals, which are conditional, and which remain internal. Defines the assumption type classification model."
---

# Assumption Publication Rules — Classification and External Publication Standard

**Version:** 1.0 | **Date:** 2026-06-22 | **Status:** Approved  
**Authority:** This document governs all decisions about external publication of assembled assumptions.  
**Companion documents:** `ASSUMPTION_SCHEDULE_STANDARD.md` | `ASSUMPTION_GROUPING_RULES.md`

---

## 1. Guiding Principle

The APPSolve Assumption Library was designed from inception as a **commercial protection mechanism**. All assumptions in approved packs are authored for client-facing use. They define the boundaries of scope, responsibility, and commercial commitments.

The publication decision is therefore not "what can we share?" but "what must we share to protect commercial position?" The default is **publish all assembled net assumptions**.

No assumption in any approved pack contains confidential commercial rates, margin information, or personnel costs. Sensitive commercial data is held in the Commercial Director authority schedule (WP11F) and never enters the assumption packs.

---

## 2. Assumption Type Classification Model

This model classifies assumptions by their commercial purpose. The classification is used for:
- Determining publication status
- Informing grouping decisions (see ASSUMPTION_GROUPING_RULES.md)
- Communicating assumption function to BU Lead

### 2.1 Classification table

| Type | Code | Definition | Typical ID suffixes |
|------|------|-----------|-------------------|
| **Scope Assumption** | SCOPE | Defines what is included in the engagement scope. Establishes the perimeter of deliverables. | GEN, SCP |
| **Exclusion Statement** | EXCL | Explicitly names items that are out of scope. Prevents scope creep and misaligned expectations. | EXC, EXT |
| **Client Responsibility** | CLIENT | Defines what the client must provide, decide, or execute. Creates enforceable client obligations. | CUS, CON, DEP |
| **Technical Assumption** | TECH | Defines the technical approach, architecture, configuration scope, and tool selection. Protects against rework claims if the environment differs from stated assumptions. | GL, AP, AR, FA, CM, PRO, PPM, REP, INT, WFL, LZ, IAM, NET, CMP, STO, DB, MW, BKP, DR, MON, OPS, MIG, SCP, DES, END, MAP, CERT, PERF, CERT |
| **Service Assumption** | SERVICE | Defines the service delivery model: SLA tiers, response/resolution targets, support channels, hours of coverage, resource model, incident classification, change request process. | SLA, PRI, HRS, CHN, INC, SRQ, ENH, CR, DEF, REL, PAT, REP, MON |
| **Commercial Assumption** | COMM | Defines commercial model aspects: rate structure type (fixed / time-and-materials), billing cycle, CR threshold, engagement prerequisites. Never contains actual rates or monetary thresholds. | GEN (commercial sub-set), CR (commercial items) |
| **Governance Assumption** | GOV | Defines compliance, regulatory, and partner-status assumptions. Includes POPIA obligations, data residency, partner tier statements, and certification scope. | SEC (governance sub-set), GOV, POPIA |

### 2.2 Type assignment by ID pattern

The classification is inferred from the source assumption ID. The following lookup rules apply in priority order:

| Priority | ID pattern | Assigned type |
|----------|-----------|--------------|
| 1 | Section code = EXC or EXT | EXCL |
| 2 | Section code = CUS, CON, or DEP | CLIENT |
| 3 | Section code = SEC or GOV | GOV |
| 4 | Section code = SLA, PRI, HRS, CHN, INC, SRQ, ENH, CR (AMS/EBS pack) | SERVICE |
| 5 | Section code = GEN, SCP | SCOPE |
| 6 | All remaining | TECH |

Note: A small sub-set of GEN assumptions address commercial model structure (COMM type). These are a sub-classification of SCOPE for grouping purposes and are not separated in the client document.

---

## 3. Publication Status per Type

### 3.1 Summary table

| Type | Publication Status | Rationale |
|------|--------------------|-----------|
| SCOPE | **PUBLISH** — always | Defines what the client is buying. Must be explicit. |
| EXCL | **PUBLISH** — always | Exclusions are the primary commercial protection against scope creep. Non-publication would remove this protection entirely. |
| CLIENT | **PUBLISH** — always | Client must know their obligations. Non-publication invalidates the obligation — clients cannot be held to responsibilities they did not receive in writing. |
| TECH | **PUBLISH** — always | Technical assumptions define the conditions under which the price is valid. If the environment differs, APPSolve must be able to demonstrate the assumption was stated. |
| SERVICE | **PUBLISH** — always | SLA, resource model, and support assumptions define the measurable commitments. Clients evaluate these. Non-publication removes enforceability. |
| COMM | **PUBLISH** — always | Commercial model structure (billing, CR thresholds, rate types) must be visible. *Actual rate amounts are never in assumptions — they are in the Commercial Director authority schedule.* |
| GOV | **PUBLISH** — always | Compliance and partner status assumptions are verifiable facts. Non-publication creates misrepresentation risk. |

### 3.2 Publication verdict

**All assumption types in all approved packs are published in the client-facing schedule.**

There are no internal-only individual assumptions. The internal/external distinction applies to **documents**, not individual assumptions:

| Document | Audience |
|----------|----------|
| Client-facing Assumption Schedule | Client — published as part of proposal |
| Assembly Audit Report | Internal — not shared with client |
| Pack source files | Internal — authoritative library source |
| Suppression log | Internal — contained in Audit Report |

---

## 4. Suppressed Assumptions — Publication Rule

Suppressed assumptions follow a strict rule regardless of their type:

| Status | Publication rule |
|--------|-----------------|
| Active (not suppressed) | **PUBLISH** in client schedule |
| Suppressed (replaced by overlay) | **DO NOT PUBLISH** — ever |
| Replacement assumption (overlay) | **PUBLISH** in client schedule |

When a suppression fires (e.g., S2 replaces AMS-SLA-001 with EBS-SLA-002), the client sees only EBS-SLA-002. AMS-SLA-001 is completely absent from the client document. No notation, no reference, no strikethrough.

---

## 5. Rate and Commercial Sensitivity Rules

### 5.1 What is never in assumptions

The following data never enters any assumption pack. If discovered in a draft assumption, the BU Lead must edit the assumption to remove it before pack approval:

- Actual hourly or daily rates (e.g., "R2,500/hour")
- Monetary thresholds (e.g., "CR threshold: R50,000")
- Margin floors or markup percentages
- Discount authorities or approval thresholds
- Specific personnel costs

### 5.2 Why this matters

If rates were in assumption packs:
- Every competitor who receives the proposal would see APPSolve's rate card
- B-BBEE and public tender regulations may require rate transparency, which conflicts with confidentiality
- Governance becomes complex (rate changes would require assumption pack versions)

### 5.3 What assumptions DO state about commercial matters

Assumptions state **structure and model**, not amounts:

| Acceptable | Not acceptable |
|-----------|---------------|
| "Service credits are calculated as a percentage of the monthly retainer fee" | "Service credits are 5% of the R150,000/month retainer" |
| "Change Requests above the agreed threshold are priced on a time-and-materials basis" | "Change Requests above R20,000 are T&M" |
| "Resource hours are allocated on a named-role monthly model" | "The SDM is billed at R800/hour for 40h/month" |

---

## 6. Conditional Publication Scenarios

### 6.1 Optional overlay packs

When overlay packs (EBS SLA Overlay, EBS DRM Overlay) are loaded:

| Scenario | What is published |
|----------|-----------------|
| AMS engagement without EBS SLA or DRM Overlay | AMS Pack assumptions (including AMS-SLA-001, AMS-PRI-001/002/003) |
| AMS engagement with EBS SLA Overlay loaded | AMS-SLA-001 and AMS-PRI-001/002/003 suppressed; EBS-SLA-* assumptions published instead |
| AMS engagement with EBS DRM Overlay loaded | AMS-SLA-005 suppressed; EBS-DRM-* assumptions published instead |
| AMS engagement with both EBS overlays | Both overlay packs published; all suppressed AMS assumptions absent |

### 6.2 Pattern-excluded packs

When a pack is excluded from an engagement (not triggered):

| Scenario | What is published |
|----------|-----------------|
| EBS AMS engagement (HCM Base excluded) | No HCM assumptions appear; ERP Pack covers EBS scope |
| HCM-only engagement (AMS not triggered) | No AMS assumptions appear |
| Acumatica standalone (Oracle packs not triggered) | No Oracle assumptions appear |

Pack exclusions are always reflected correctly in the client schedule — the client only sees assumptions relevant to their engagement.

---

## 7. Special Publication Categories

### 7.1 Journey assumptions (Rule JRN-1)

HCM-JRN-001 is automatically included whenever HCM Base loads. It is published as a standard SCOPE assumption in Section C.2 (Oracle HCM Functional). No special treatment required.

### 7.2 Exclusion assumptions (-EXC- and -EXT- sections)

All exclusion assumptions are **mandatory to publish**. They form the critical commercial boundary that prevents scope creep. Even if the content seems obvious ("custom RICEW objects not in scope"), the assumption must appear in the client document.

Under the grouping rules, all exclusion assumptions from all packs are consolidated into Section H — Explicit Exclusions, regardless of source pack.

### 7.3 Customer responsibilities (-CUS-, -CON-, -DEP- sections)

All client responsibility assumptions are **mandatory to publish**. They create legal and commercial obligations on the client. Under the grouping rules, they are consolidated into Section G — Client Responsibilities.

### 7.4 Governance assumptions (POPIA, partner status, sector compliance)

Where assumptions state compliance positions (e.g., POPIA data processing obligations, partner tier status, BEE positioning), these are published. They are also subject to the governance restrictions in HANDOVER.md:

- **BEE level**: Do not cite Level 3 BEE in submissions after 2026-07-31 unless renewal certificate confirmed
- **Oracle partner tier**: Level 1 Partner only — never "Gold Partner"
- **Acumatica partner tier**: "Gold Partner" — never "Gold Certified"

These governance restrictions apply to assumption text — if the assumption pack contains a phrase that violates a governance restriction, the pack must be corrected before the assumption is published in any submission.

---

## 8. Assumptions the Engine Cannot Generate

The following types of assumptions do not exist in the current library and require manual handling if relevant to an engagement:

| Gap | Affected engagements | Action |
|-----|---------------------|--------|
| Mining Charter / B-BBEE compliance | Mining sector AMS | Manual assumption authoring; no pack yet |
| Knowledge Transfer programme (KT) | All AMS engagements | GAP-007 — manual authoring for AMS; no pack yet |
| Multi-site / mine-site access | Multi-site EBS AMS | GAP-009 — manual authoring for mining; no pack yet |
| BeBanking KT programme | BeBanking + AMS | No BeBanking KT assumptions; manual authoring |

These gaps are tracked in the Assembly Audit Report per engagement. Manually authored assumptions for these gaps must be reviewed and approved by BU Lead before publication. They do not receive a standard Assumption ID until the gap is formally closed by a new pack.

---

*ASSUMPTION_PUBLICATION_RULES.md v1.0 | WP17D-0 Design Standard | 2026-06-22*  
*Approved for WP17D-1 implementation. All assembled net assumptions are published. No internal-only individual assumptions exist in approved packs.*
