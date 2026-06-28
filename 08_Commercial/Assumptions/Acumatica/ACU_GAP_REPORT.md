---
document_id: ACU-GAP-REPORT-V1
title: "APPSolve Acumatica Base Assumption Pack — Gap Report"
version: "1.2-Approved"
status: "Closed — All decisions resolved WP15C 2026-06-18"
created: "2026-06-16"
last_updated: "2026-06-18"
created_by: "WP11I — Acumatica Base Assumption Pack"
updated_by: "WP15C — Acumatica Final Decision Application and Promotion"
pack_code: ACU
related_pack: ACU-BASE-ASSUMPTIONS-V1
total_gaps: 14
bu_decisions_required: 14
bu_decisions_resolved: 14
bu_decisions_outstanding: 0
---

# Acumatica Base Assumption Pack — Gap Report

**Pack:** ACU | **Status:** CLOSED — All 14 decisions resolved WP15C 2026-06-18 | **Total Gaps:** 14 | **BU Decisions Required:** 14 | **BU Decisions Resolved:** 14 | **Outstanding:** 0

This gap report documents assumptions in the Acumatica Base pack that require BU Lead decisions before the pack can be used in client-facing proposals. It also documents research gaps where commercial, legal, or technical positions need further confirmation before the assumption wording is locked down.

---

## Gap Summary

| Severity | Count | Description |
|---|---|---|
| CRITICAL | 1 | Must be resolved before any Acumatica proposal is issued |
| HIGH | 4 | Should be resolved before first Acumatica proposal; workarounds exist |
| MEDIUM | 5 | Resolve before scaled Acumatica delivery; acceptable to defer for a single pilot proposal |
| RESEARCH | 4 | Factual/legal/commercial items requiring confirmation — not BU decisions |
| **Total** | **14** | |

---

## CRITICAL Gaps

### GAP-ACU-C01: APPSolve's Acumatica Partnership Tier Not Confirmed

**Severity:** CRITICAL
**Assumption affected:** ACU-GEN-009
**BU Decision:** BU-ACU-009

APPSolve's current Acumatica partner tier is not confirmed in the knowledge base. Assumption ACU-GEN-009 explicitly states that APPSolve is NOT a "Gold Certified" partner, but the actual tier (Authorised, Silver, Gold, or VAR-only) is unconfirmed. This is a CRITICAL gap because:

1. Every Acumatica proposal citing APPSolve's credentials must accurately reflect the partnership tier.
2. Claiming an incorrect tier (either too high or too low) is a compliance and credibility risk.
3. The partner tier affects which Acumatica modules APPSolve is authorised to implement.

**Resolution required:** BU Lead to confirm APPSolve's current Acumatica partner tier and the approved description to use in proposals.

**Risk if unresolved:** APPSolve issues proposals citing incorrect partner credentials — reputational and contractual risk.

---

## HIGH Gaps

### GAP-ACU-H01: PaySpace Integration Method Not Standardised

**Severity:** HIGH
**Assumption affected:** ACU-PAY-001, ACU-PAY-004
**BU Decision:** BU-ACU-001

The Acumatica-PaySpace integration is a core feature of APPSolve's Acumatica offering. However, the standard integration method has not been defined. Four options exist:

- **(a) Native API integration** — real-time or scheduled; requires PaySpace to expose an Acumatica-compatible REST API endpoint
- **(b) Custom middleware** — higher effort; more flexible
- **(c) Automated file-based** — scheduled export from PaySpace + scheduled import to Acumatica
- **(d) Manual file-based** — lowest effort; highest operational risk; not sustainable for regular payroll runs

Without a standard approach, different Acumatica proposals will price this integration differently, creating inconsistency and margin risk.

**Resolution required:** BU-ACU-001 — BU Lead to confirm the standard Acumatica-PaySpace integration method.

**Risk if unresolved:** Inconsistent scoping and pricing of the PaySpace integration; potential under-pricing of implementation effort.

---

### GAP-ACU-H02: Hypercare Duration Not Standardised

**Severity:** HIGH
**Assumption affected:** ACU-CUT-005
**BU Decision:** BU-ACU-008

The standard hypercare period after Acumatica go-live is not defined. The AMS pack (for Oracle) uses a defined hypercare period. Acumatica requires its own standard because:

- Acumatica implementations range from single-module (simple, short hypercare) to full-suite (complex, longer hypercare)
- The hypercare period directly affects the cost of delivery and the handover to AMS
- Without a standard, each proposal will define hypercare differently, creating client expectation inconsistencies

**Resolution required:** BU-ACU-008 — BU Lead to confirm the standard Acumatica hypercare duration.

**Risk if unresolved:** Over- or under-scoped hypercare in proposals; cost overrun or client expectation gap.

---

### GAP-ACU-H03: Integration Tier Definitions for Acumatica Not Confirmed

**Severity:** HIGH
**Assumption affected:** ACU-INT-001
**BU Decision:** BU-ACU-002

The AMS pack defines Simple/Standard/Complex integration tiers for Oracle integrations. These tiers need to be confirmed for Acumatica context — particularly because:

- Acumatica's native REST API and Import Scenarios make some integrations inherently simpler than Oracle equivalents
- The BeBanking integration has unique complexity that may warrant its own tier
- PaySpace integration complexity varies by method

Without tier definitions, estimating integration effort in proposals requires individual assessment each time, which is slow and inconsistent.

**Resolution required:** BU-ACU-002 — BU Lead to confirm whether Oracle AMS tiers apply, or Acumatica-specific tiers should be defined.

---

### GAP-ACU-H04: Acumatica ISV Products APPSolve Actively Supports

**Severity:** HIGH
**Assumption affected:** ACU-EXT-003
**BU Decision:** BU-ACU-004

The Acumatica Marketplace contains ISV add-on products. Clients frequently ask whether specific ISV products (e.g., Velixo for Excel reporting, Procore integration for construction, specific local payroll or HR ISVs) are within APPSolve's delivery scope.

Without a confirmed list, APPSolve risks:
1. Committing to ISV support for products where APPSolve has no competency
2. Declining to support ISVs that are well within APPSolve's capability

**Resolution required:** BU-ACU-004 — BU Lead to confirm and publish the list of Acumatica ISV products APPSolve actively supports.

---

## MEDIUM Gaps

### GAP-ACU-M01: BI Connector Configuration Status

**Severity:** MEDIUM
**Assumption affected:** ACU-REP-004
**BU Decision:** BU-ACU-003

Power BI is a common client request for Acumatica reporting. Acumatica exposes an OData feed that Power BI can connect to. The question is whether configuring this OData connection is:
- A standard Acumatica implementation task (included in base scope)
- Always separately scoped
- Included only for clients with existing Power BI licences

**Resolution required:** BU-ACU-003.

---

### GAP-ACU-M02: Standard Report Set Not Defined Per Module

**Severity:** MEDIUM
**Assumption affected:** ACU-REP-001
**BU Decision:** BU-ACU-006

"Standard Acumatica report library" is referenced but the exact set of reports included per module is not enumerated. Without a report list, "standard reports" can be interpreted broadly by clients. A curated list would clarify the boundary and make the scope defensible.

**Resolution required:** BU-ACU-006 — BU Lead to determine whether to enumerate a curated report set or rely on Acumatica's standard library.

---

### GAP-ACU-M03: Training Delivery Default

**Severity:** MEDIUM
**Assumption affected:** ACU-TRN-002
**BU Decision:** BU-ACU-007

The assumption states virtual facilitated training as the standard. This needs BU Lead confirmation given:
- South African clients often request on-site training, particularly for go-live
- On-site incurs travel costs that must be captured in proposals
- Hybrid approaches (virtual for configuration training, on-site for go-live support) may be preferred

**Resolution required:** BU-ACU-007.

---

### GAP-ACU-M04: Parallel Run Standard Position

**Severity:** MEDIUM
**Assumption affected:** ACU-CUT-002
**BU Decision:** BU-ACU-005

The assumption excludes parallel run by default. However, some Acumatica clients (particularly those migrating from legacy DOS-based systems or spreadsheet-based operations) may consider parallel run essential for financial audit purposes.

The BU needs to decide whether to: explicitly exclude parallel run in all proposals (requiring the client to add it as a scope item), or offer a limited parallel run as a standard option.

**Resolution required:** BU-ACU-005.

---

### GAP-ACU-M05: Historical Data Migration Default Position

**Severity:** MEDIUM
**Assumption affected:** ACU-DAT-005, ACU-EXC-005
**BU Decision:** BU-ACU-010

Opening balances only vs. historical transaction migration is a significant scoping decision. Some clients expect historical transaction migration as standard (expecting to be able to query history in Acumatica). The effort delta between opening-balance-only and 12-month history migration can be substantial.

**Resolution required:** BU-ACU-010 — BU Lead to confirm the default position (opening balances only) and whether any standard history migration period should be offered.

---

## RESEARCH Gaps

### GAP-ACU-R01: PaySpace API Availability for Acumatica Integration

**Severity:** RESEARCH
**Assumption affected:** ACU-PAY-004

It is not confirmed whether PaySpace exposes a REST API that supports automated integration with Acumatica for payroll GL journal posting. This is a factual question requiring confirmation from PaySpace's technical documentation or direct API assessment. The answer determines which integration method (ACU-PAY-004 option a, b, c, or d) is the most viable default.

**Action required:** Technical assessment of PaySpace API capabilities for GL journal posting to Acumatica.

---

### GAP-ACU-R02: Acumatica OData Feed — Column-Level Access

**Severity:** RESEARCH
**Assumption affected:** ACU-REP-004

Acumatica's OData feed exposes Generic Inquiry results as OData endpoints. However, the specific columns, refresh rates, and access controls (particularly for multi-entity tenants with branch-level security) have not been validated. Power BI connectivity relies on this being available and performant.

**Action required:** Technical validation of Acumatica OData feed capabilities for Power BI connectivity.

---

### GAP-ACU-R03: Acumatica South Africa Regulatory Compliance — POPIA

**Severity:** RESEARCH
**Assumption affected:** ACU-FIN-009, ACU-CUS-002

Acumatica's data residency position for South African clients (whether client data is hosted in South Africa or offshore) has not been confirmed for POPIA compliance purposes. This is relevant for Acumatica SaaS tenants where regulated personal data (customer records, employee data) is stored in Acumatica.

**Action required:** Confirm Acumatica's data residency options for South African SaaS tenants and POPIA compliance position.

---

### GAP-ACU-R04: Acumatica BEE Reporting Module Availability

**Severity:** RESEARCH
**Assumption affected:** ACU-REP-005

South African B-BBEE reporting is a common client requirement. It is not confirmed whether Acumatica has a native B-BBEE scorecard reporting module or whether this is an ISV product. If it is an ISV product, it is relevant to BU-ACU-004 (ISV support list).

**Action required:** Confirm whether Acumatica offers native B-BBEE reporting or whether this is covered by a Marketplace ISV.

---

## BU Decision Summary

| Decision ID | Item | Severity | Status |
|---|---|---|---|
| BU-ACU-001 | Acumatica-PaySpace standard integration method | HIGH | **RESOLVED WP15C 2026-06-18** — Method confirmed at pre-sales per PaySpace licence tier |
| BU-ACU-002 | Acumatica integration tier definitions | HIGH | **RESOLVED WP15C 2026-06-18** — AMS Pack tiers adopted (Simple/Standard/Complex) |
| BU-ACU-003 | BI connector configuration scope | MEDIUM | **RESOLVED WP15C 2026-06-18** — Always separately scoped; never in standard scope |
| BU-ACU-004 | Acumatica ISV products APPSolve supports | HIGH | **RESOLVED WP15C 2026-06-18** — APPSolve maintains published ISV Support List |
| BU-ACU-005 | Parallel run default position | MEDIUM | **RESOLVED WP15C 2026-06-18** — Excluded by default; SOW explicit inclusion required |
| BU-ACU-006 | Standard report set definition per module | MEDIUM | **RESOLVED WP15C 2026-06-18** — All factory Acumatica reports for modules in scope |
| BU-ACU-007 | Training delivery format default | MEDIUM | **RESOLVED WP15C 2026-06-18** — Virtual facilitated as standard; on-site at additional cost |
| BU-ACU-008 | Hypercare duration standard | HIGH | **RESOLVED WP15C 2026-06-18** — 4-week standard (consistent with BeBanking + Oracle) |
| BU-ACU-009 | Acumatica partner tier in proposals | CRITICAL | **RESOLVED WP14G 2026-06-18** — Acumatica Gold Partner confirmed; never cite Gold Certified |
| BU-ACU-010 | Historical data migration default | MEDIUM | **RESOLVED WP15C 2026-06-18** — Opening balances and open items only; history separately scoped |
| BU-ACU-011 | Non-PaySpace payroll integration standard position | HIGH | **RESOLVED WP15C 2026-06-18** — PaySpace standard; non-PaySpace assessed as custom at pre-sales |
| BU-ACU-012 | POPIA data residency disclosure approach in proposals | HIGH | **RESOLVED WP15C 2026-06-18** — Mandatory in all Acumatica proposals |
| BU-ACU-014 | APPSolve Project Manager inclusion default | MEDIUM | **RESOLVED WP15C 2026-06-18** — PM included for 3+ modules or multi-BU scope |
| BU-ACU-015 | Consolidated financial reporting default for multi-entity | MEDIUM | **RESOLVED WP15C 2026-06-18** — Always separately scoped |

---

## WP11I-A Remediation Note

Four additional BU decisions (BU-ACU-011, BU-ACU-012, BU-ACU-014, BU-ACU-015) were added during the WP11I-A Pre-Approval Validation and Remediation pass (2026-06-16). BU-ACU-013 (Velixo partnership status) was proposed but rejected — Velixo partnership status is a factual business relationship confirmation, not a governance decision. Seventeen new assumptions were added to the pack across four new sections/section extensions (ACU-GEN, ACU-CFG, ACU-DAT, ACU-FIN, ACU-ORG, ACU-PAY, ACU-INT, ACU-TRN, ACU-SUP, and new ACU-SEC). The pack assumption count is now confirmed at 152 (correcting a count error in WP11I where 135 assumptions were created but reported as 152 — remediation closes the actual gap to 152). Section range extended to 120–139.

---

*Acumatica Base Gap Report v1.2-Approved | WP11I-A Remediation Applied 2026-06-16 | WP15C All decisions resolved 2026-06-18*
*14 gaps originally identified | 14 BU decisions resolved | 0 outstanding | Pack promoted to Approved v1.0 WP15C 2026-06-18*
