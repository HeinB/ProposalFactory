---
created: "2026-06-10"
created_by: "Claude (AI — Wave 2 gap analysis)"
status: "Active — current state assessment; reflects approved content as of 2026-06-10"
---

# Oracle Tender Readiness Assessment
**Date:** 2026-06-10 | **Owner:** Hein Blignaut | **Purpose:** Compare current approved Oracle content against a typical Oracle RFP; classify coverage as Covered / Partially Covered / Missing

This is a snapshot assessment based on the 25 approved Wave 1 files and current KB state. It is a planning tool, not a tender submission checklist.

**Updated 2026-06-10 (Phase B):** Three additional confirmed source documents identified after initial assessment — SAA HCM RFP Response (June 2025), Hollywood Bets Accepted Proposal V5.0 (April 2023), RedPath Mining RFI Reply (March 2026). These sources materially improve the extractable content available for Sections 3, 4, and 7. Updated coverage and Wave 2 plan now reflects 5 deliverables (expanded from 3). See revised tables at the end of this document.

---

## Assessment Method

A typical Oracle RFP — whether for implementation, managed services, or support — evaluates vendors across 8 standard sections. This assessment compares the approved Wave 1 content inventory against each section and rates coverage as:

- **Covered** — Approved content exists that directly addresses this section; citeable without gap
- **Partially Covered** — Some approved content exists but does not fully address the section; gap is noted
- **Missing** — No approved content; must flag the gap at tender time; source documents exist for future extraction

---

## Section-by-Section Coverage Assessment

### 1. Company Profile and History

**Coverage:** Covered

| Approved file | What it provides |
|---|---|
| W1S1-001 Company Overview | Company description, consultants, industries, geography |
| W1S1-002 Company History | Founded 2002; Oracle DBA origins; 23-year history; expansion narrative |
| W1S1-008 Geographic Presence | Sub-Saharan Africa (5 markets); international (4 markets) |
| W1S1-009 Key Differentiators | 7 differentiators; senior-only delivery; MRI model; 3 costing models |

**Assessment:** Strong. All four cross-BU files are approved and comprehensive. No gap for standard company profile questions.

**Residual risk:** CIPC registration and BEE certificate must be verified at tender time (BEE expires 2026-07-31 — renewal in progress).

---

### 2. Oracle Partnership and Accreditation

**Coverage:** Covered

| Approved file | What it provides |
|---|---|
| W1S1-003 Oracle Partnership Statement | Oracle Level 1 Partner; 5 expertise areas; VAR authorisation; 6 awards 2015–2024 |
| W1S1-007 Delivery Model | Oracle Level 1 Partner reference; 8 service lines including Oracle services |

**Assessment:** Covered for partnership tier and authorisation. Oracle Level 1 Partner is confirmed and approved. Six awards table is approved.

**Critical rule — must apply at every Oracle tender:**
> Oracle Gold Partner status EXPIRED August 2021. Cite "Oracle Level 1 Partner" only. Never "Gold Partner" or "Gold Level."

**Gap remaining:**
- Cloud Excellence Implementer designation: approved in W1S1-003 but flagged for annual OPN revalidation. Confirm current status before including in any tender.
- Linux Specialist designation: same annual revalidation flag.

---

### 3. Oracle Implementation Capability

**Coverage:** Partially Covered

| Approved file | What it provides |
|---|---|
| W1S1-007 Delivery Model | Service lines include Oracle ERP implementation; methodology model referenced |
| W1S1-003 Oracle Partnership Statement | Implementation authorisation implied through partnership tier and expertise areas |

**What is missing:**
- **Oracle Fusion capability statement** — no approved product-level capability description for Oracle Cloud / Fusion. This is the most significant Oracle content gap. Sources available: TMPL-001 (structural authority) + SAA Section 2 (June 2025, richest HCM content) + RedPath Mining RFI (confirms OIC standard and client list).
- **Oracle EBS capability statement** — no approved module-level capability description for Oracle EBS R12. Source available: TMPL-002.
- **Oracle implementation methodology** — W1S1-007 covers the general delivery model but there is no Oracle-specific phased implementation methodology. Sources now confirmed: Hollywood Bets V5.0 (accepted proposal, Phase structure) + RedPath Mining RFI (OUM-based methodology) + SAA Section 5.

**Phase B source update:** SAA HCM RFP (June 2025) contains 15+ HCM modules with detailed Overview / Benefits / Key Features tables — this is now the primary HCM extraction source, richer than TMPL-001 for HCM. Hollywood Bets V5.0 confirms a 7-module Fusion HCM implementation with full phase structure. RedPath Mining RFI confirms OIC as standard in every Fusion implementation.

**Tender impact:** Without Fusion or EBS capability statements, an Oracle implementation RFP response must rely on the generic company overview. Wave 2 (5 deliverables) closes this gap completely.

---

### 4. Oracle Managed Services and DBA Capability

**Coverage:** Partially Covered

| Approved file | What it provides |
|---|---|
| W1S1-007 Delivery Model | "One of the largest locally-based Oracle Applications DBA teams in South Africa" (approved claim) |
| W1S1-009 Key Differentiators | Hybrid Support Model; 24x7 monitoring; senior-only delivery; after-hours support |

**Update 2026-06-11 — W2S1-003 APPROVED; W2S1-004 CANDIDATE created:**

| File | Status | What it provides |
|---|---|---|
| W2S1-003 Oracle DBA Executive Summary | **APPROVED 2026-06-11** | 12 sections: executive overview, DBA service scope, Oracle DB administration, performance monitoring, backup/recovery/DR, patching/lifecycle, security, Oracle tool competency, 24x7 support, large-scale estate experience, differentiators, review notes. 8 Oracle DBA reference clients (DFA excluded per BU Lead). Hybrid Support Model, CIM, Monthly Recurring Invoice Model. **Approved_for_reuse: Yes** |
| W2S1-004 Oracle Managed Services Support Model | **APPROVED 2026-06-11** | 15 sections: ITIL framework, CSI model, service delivery management, capacity/demand, performance management, monitoring framework, CMDB governance, release/deployment, segregation of duties, documentation standards (backup SOP, monthly report TOC), migration/ETL capability, 24x7 support structure. All 7 assumptions resolved. **Approved_for_reuse: Yes** |

**Tender impact:** W2S1-003 and W2S1-004 together provide a complete Oracle DBA managed services response capability. Section 4 (Managed Services / DBA) is now fully Covered.

---

### 5. Oracle Cloud Services (OCI, Fusion Cloud)

**Coverage:** Missing

| Approved file | What it provides |
|---|---|
| W1S1-003 Oracle Partnership | Oracle Level 1 Partner — implicitly covers cloud but no explicit OCI claim |
| W1S1-007 Delivery Model | Cloud advisory listed as service line |

**What is missing:**
- No approved Oracle Cloud / OCI / Fusion Cloud capability statement exists
- No approved Oracle Cloud implementation methodology
- No approved Oracle Cloud migration capability description
- Cloud Excellence Implementer designation is claimed in W1S1-003 but not supported by a detailed cloud capability document

**Source available:** TMPL-001 Oracle Fusion Template (covers Fusion/Cloud component table). This is the Wave 2 Priority 1 extraction.

---

### 6. Oracle Upgrades and Migrations

**Coverage:** Partially Covered

| Approved file | What it provides |
|---|---|
| W1S1-007 Delivery Model | Upgrades and migrations listed as a service line |
| W1S1-009 Key Differentiators | Modernisation narrative implied |

**What is missing:**
- No approved upgrade/migration methodology document
- No specific R11-to-R12 or EBS-to-Cloud migration methodology approved
- No documented migration case studies in approved content

**Source available:** HIST-002 (MTN 2014 has transition methodology sections). Wave 3 target.

---

### 7. Oracle Support Services

**Coverage:** Partially Covered

| Approved file | What it provides |
|---|---|
| W1S1-007 Delivery Model | Support services listed as a service line; Hybrid Support Model described |
| W1S1-009 Key Differentiators | Hybrid Support Model; 24x7 monitoring; after-hours support; CIM 4-stage model |

**What is missing:**
- No Oracle-specific support tier document (P1/P2/P3/P4 response targets)
- No Oracle AMS (Application Managed Services) capability statement
- No support governance model document

**Update 2026-06-11:** W2S1-004 Oracle Managed Services Support Model created as CANDIDATE. Primary source: MTN 2026 DBA RFP (RFX-1000004246, April 2026) — superseded ATNS EBS 2025 as planned source. Sections 9–13 of W2S1-004 specifically address support services: ITIL service management, CSI model, service delivery management (governance cadence, reporting framework), 24x7 support structure. BU Lead review required before tender use.

---

### 8. Oracle Client References

**Coverage:** Missing (from KB perspective) — Partially available from corpus

| KB location | Status |
|---|---|
| `04_References/Oracle/` | **Empty** — no signed Oracle reference letters in the KB |

**Corpus discovery (not in KB):**
Multiple Oracle reference letters exist in tender submission folders across the corpus. See `ORACLE_REFERENCE_GAP_REPORT.md` for the full inventory.

**Tender impact:** Most evaluated RFPs require two to three verifiable client references. Without signed letters registered in the KB, APPSolve must locate letters from corpus submission folders at each tender. Letters are present; they just need to be registered and confirmed as usable.

---

## Summary Coverage Table (Updated — Phase B, 2026-06-10)

| RFP Section | Coverage | Gap Severity | Wave 2 Action |
|---|---|---|---|
| 1. Company Profile | **Covered** | None | None — use approved files |
| 2. Oracle Partnership | **Covered** | Low — annual OPN revalidation | Revalidate Cloud Excellence annually |
| 3. Implementation Capability | **Covered (EBS + Fusion + Methodology)** | None — W2S1-001 APPROVED (2026-06-11); W2S1-002 APPROVED (2026-06-12); W2S1-005 APPROVED (2026-06-12) | W2S1-001 (Fusion — APPROVED 2026-06-11; pre-tender checks A-001 A-002 A-004 open); W2S1-002 (EBS — APPROVED 2026-06-12; 5 referenceable clients; pre-tender checks: FR-EBS-012 OPN cert; SARB separate BU approval; register reference letters); W2S1-005 (Methodology — APPROVED 2026-06-12; 16 sections + Section 17 Approval Record; standing pre-tender checks D-W5-003 through D-W5-006) |
| 4. Managed Services / DBA | **Covered** | None | W2S1-003 (DBA Exec Summary — APPROVED 2026-06-11); W2S1-004 (Support Model — APPROVED 2026-06-11) |
| 5. Oracle Cloud / OCI | **Missing** | **CRITICAL** — no cloud capability doc | W2S1-001 (Fusion covers OCI/cloud); OCI SOC Bridge Letters available |
| 6. Upgrades / Migrations | **Partially Covered** | Medium — service line listed only | Wave 3 — full methodology |
| 7. Support Services | **Partially Covered** | Medium — framework in W1S1-007/009 | W2S1-004 (Managed Services + Support Model — ATNS 2025) |
| 8. Client References | **Missing (KB)** | **HIGH** — letters exist but not registered | Register corpus letters (see Ref Gap Report); new: MTN July 2025 + Stellenbosch 2025 added |

---

## Current Oracle Tender Response Capability (Before Wave 2)

**What an Oracle tender can use today:**
- Strong company profile and history (4 approved files)
- Confirmed partnership tier and awards table (W1S1-003)
- Delivery model with Oracle service lines (W1S1-007)
- Key differentiators and DBA team claim (W1S1-009)

**What an Oracle tender cannot yet use:**
- Any Oracle product capability statement (Fusion, EBS, Cloud, HCM, DBA)
- Oracle-specific implementation methodology
- Oracle-specific SLA or governance framework
- A registered signed Oracle client reference

**Conclusion:** APPSolve can currently respond to Oracle tenders at the company credibility level but cannot populate product capability sections without using unverified source material or fabricated content. Wave 2 (5 documents, approximately 7–8 hours extraction across 3 sessions) moves the capability coverage from Partially Covered to substantially Covered for all evaluated RFP sections.

---

## Coverage After Completing Wave 2 (5 Deliverables — Updated Phase B)

If all five Wave 2 documents are extracted and approved:

| RFP Section | Coverage After Wave 2 | Delivering document(s) |
|---|---|---|
| 1. Company Profile | Covered | Unchanged — use approved W1S1 files |
| 2. Oracle Partnership | Covered | Unchanged — W1S1-003 |
| 3. Implementation Capability | **Covered** | W2S1-001 (Fusion — all confirmed HCM/Finance modules), W2S1-002 (EBS — module overview), W2S1-005 (Methodology) |
| 4. Managed Services / DBA | **Covered** | W2S1-003 (DBA Exec Summary), W2S1-004 (Support Model + SLA framework) |
| 5. Oracle Cloud / OCI | **Covered** | W2S1-001 (Fusion covers OCI); OCI SOC Bridge Letters available as supporting docs |
| 6. Upgrades / Migrations | Partially Covered | Wave 3 — EBS-to-OCI migration methodology (confirmed expertise area, not yet in KB) |
| 7. Support Services | **Mostly Covered** | W2S1-004 (Managed Services Support Model — APPROVED 2026-06-11; Sections 4, 13 address support governance and 24x7 model) |
| 8. Client References | Missing → **Partially Covered** | Register corpus letters (see Reference Gap Report). Letters exist for Harmony 2024, Assore 2023, Investec 2023, Mr Price 2024 (Fusion), Oracle Corp 2024, ARM R12.2. New letters: MTN July 2025, Stellenbosch University 2025 (found in RedPath Mining folder). |

---

*Prepared 2026-06-10 by Claude (AI) — initial gap analysis. Updated same date (Phase B) to reflect SAA HCM, Hollywood Bets V5.0, and RedPath Mining RFI confirmed sources. No extraction work performed. Based on approved content as of this date.*
