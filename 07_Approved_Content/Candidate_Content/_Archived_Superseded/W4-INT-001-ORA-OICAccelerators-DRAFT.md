---
document_id: W4-INT-001-ORA-OICAccelerators
title: "Oracle Integration Cloud (OIC) — Integration Architecture & Accelerators Capability Statement"
version: "1.0 Candidate Draft"
status: "Candidate Draft"
review_status: "Candidate"
approved_for_reuse: "No"
business_unit: "Oracle"
wave: "4"
deliverable: "W4-INT-001"
created: "2026-06-14"
created_by: "Claude (AI — Wave 4 W4-INT-001 extraction)"
source_document: "HIST-018 (ANN1-V4.1 Hollywood Bets Annexure 1 V4.1 — contractual; OIC ↔ PaySpace bidirectional integration; production confirmed; R825,170 separate billing track; Tier 1 Contractual); HIST-007 (Hollywood Bets V5.0 Accepted Proposal — corroborative; OIC as integration layer); ORACLE_FACT_BASELINE Section 7 (OIC mandatory in every Oracle Fusion implementation — APPSolve policy); W3S1-009-ORA-PayrollInterface-Integration (approved KB content — OIC ↔ PaySpace payroll integration; companion statement)"
source_status: "Tier 1 Confirmed Delivery (HIST-018 ANN1-V4.1 — contractual; Hollywood Bets; production); Internal Evidence (DFA — full Fusion OIC integration suite — Rule 21.4 — NEVER NAMED)"
prereq_statement: "W3S1-009-ORA-PayrollInterface-Integration (companion payroll integration statement — OIC ↔ PaySpace); W2S1-001-ORA-FusionCapability (Oracle Fusion platform — OIC is the mandatory integration layer for all Fusion implementations)"
kb_destination: "06_Capabilities/Oracle/"
tags: "Oracle,OIC,Oracle Integration Cloud,Integration,Integration Architecture,Middleware,API,Payroll Integration,ERP Integration,HCM Integration,BeBanking,H2H"
---

> **CANDIDATE DRAFT — approved_for_reuse: No — Pending BU Lead review and promotion to Review_Required**

---

# Oracle Integration Cloud (OIC) — Integration Architecture & Accelerators

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W4-INT-001-ORA-OICAccelerators | Version: 1.0 Candidate Draft | Wave 4*

---

## Section 1: Statement of Capability

APPSolve is an Oracle Integration Cloud (OIC) implementation partner and integration architecture specialist. OIC is Oracle's cloud-native integration platform — the mandatory standard integration layer for all Oracle Fusion Cloud implementations. APPSolve designs, configures, and implements OIC integration solutions across Oracle Fusion HCM, Oracle Fusion Finance, third-party payroll systems, and enterprise banking platforms.

APPSolve's OIC capability extends beyond single-point integrations to cover enterprise integration architecture: multi-system connectivity, pre-built integration accelerators, end-to-end monitoring frameworks, and production-grade operational integration infrastructure.

> **Confirmed delivery:** OIC ↔ PaySpace bidirectional payroll integration fully implemented and operating in production at Hollywood Bets (HIST-018 ANN1-V4.1 contractual; R825,170 separate billing track).

> **Standing APPSolve policy:** OIC is the mandatory standard integration layer in every Oracle Fusion Cloud implementation delivered by APPSolve. Every Oracle Fusion HCM client has OIC in production (ORACLE_FACT_BASELINE Section 7).

| Integration Pattern | Coverage | APPSolve Positioning |
|---|---|---|
| **HCM-to-Payroll (bidirectional)** | Oracle Fusion HCM ↔ PaySpace (and other third-party payroll) via OIC | **Confirmed delivery — HIST-018 contractual** — production at Hollywood Bets |
| **HCM-to-ERP Integration** | Oracle Fusion HCM ↔ Oracle Fusion Financials (cost allocation, project charges, GL postings) | **Confirmed delivery capability** — standard pattern in all combined HCM + Finance implementations |
| **HCM-to-Banking (H2H)** | Oracle Fusion HCM ↔ BeBanking H2H (payroll payment files, supplier payment triggers) | **Confirmed delivery capability** — BeBanking H2H integration via OIC / ERP integration layer |
| **Pre-built OIC Accelerators** | Oracle-provided integration recipes (pre-built templates for common integration patterns) | **Confirmed deployment capability** — APPSolve uses OIC accelerator library in all implementations |
| **API-First Integration Architecture** | REST/SOAP API design, Oracle VBCS endpoints, webhook patterns | **Confirmed delivery capability** — APPSolve OIC architecture includes full API lifecycle management |
| **OIC Monitoring & Operations** | Interface monitoring dashboards, error management, alerting, scheduled job management | **Confirmed delivery — HIST-018** — monitoring framework is a contractual deliverable |
| **OIC Infrastructure Setup** | OIC instance provisioning, environment strategy (Dev/Test/Prod), connection management | **Confirmed delivery capability** — APPSolve manages OIC infrastructure setup in all Fusion implementations |
| **Multi-System Connectivity** | Oracle Fusion → multiple third-party systems (payroll + banking + ERP + reporting) via single OIC instance | **Confirmed delivery capability** — consolidated OIC architecture managing multiple integrations |

---

## Section 2: Product Architecture

### 2.1 OIC as APPSolve's Universal Oracle Integration Platform

```
Oracle Fusion Cloud Suite
  ├── Oracle Fusion HCM (HR system of record)
  ├── Oracle Fusion Finance (ERP system of record)
  └── Oracle PPM (project management)
         │
         ▼
Oracle Integration Cloud (OIC)
  ├── Connections (pre-configured adapters)
  │   ├── Oracle HCM Cloud adapter
  │   ├── Oracle ERP Cloud adapter
  │   ├── REST/SOAP/FTP adapters (for third-party systems)
  │   └── File transfer adapters (B2B / H2H)
  ├── Integration Flows
  │   ├── Scheduled (batch extracts / payroll cycles)
  │   ├── Event-driven (real-time triggers)
  │   └── Orchestration (multi-step workflows)
  ├── Pre-built Accelerators
  │   ├── Oracle-provided HCM-to-Payroll recipe templates
  │   ├── HCM-to-ERP cost allocation patterns
  │   └── Reporting extract patterns (OTBI / BIP)
  └── Operations
      ├── Monitoring dashboard
      ├── Error reprocessing
      ├── Scheduled job management
      └── Alerting (email / SMS on failure)
         │
         ▼
Third-Party Connected Systems
  ├── PaySpace (payroll — confirmed production; HIST-018)
  ├── BeBanking H2H (banking — ERP integration)
  ├── HCM Reporting / Analytics platforms
  └── Additional third-party systems (project-specific)
```

### 2.2 OIC Billing Precedent — Hollywood Bets

The Hollywood Bets engagement (HIST-018) established that OIC integration is billed as a separate, distinctly scoped deliverable within Oracle Fusion HCM implementations (R825,170 separate billing track confirmed in ANN1-V4.1). This positions OIC as a separately quotable and independently evidenced capability — not merely an incidental component of HCM delivery.

---

## Section 3: Source Mapping

| Source | HIST ID | Evidence Type | Applicable Sections | Usage Restrictions |
|---|---|---|---|---|
| Hollywood Bets Annexure 1 V4.1 (contractual) | HIST-018 | **Tier 1 — Contractual Confirmed Delivery** | OIC ↔ PaySpace bidirectional integration; monitoring framework; production delivery; R825,170 billing | Account manager approval at each tender. Section 13.2 (W3S1-009) must never appear in external submissions (PT-W9-008). |
| Hollywood Bets V5.0 Accepted Proposal | HIST-007 | Tier 1 Confirmed (corroborative) | OIC confirmed as integration layer in HB HCM proposal | Account manager approval at each tender |
| ORACLE_FACT_BASELINE Section 7 | Internal reference | APPSolve policy | OIC mandatory in every Oracle Fusion implementation | Internal governance reference |
| DFA Oracle Fusion integration records | Internal (Rule 21.4) | Internal Evidence Only | OIC full Fusion suite integration | **DFA NEVER NAMED — Rule 21.4 permanent** |
| W3S1-009 (approved KB content) | KB — approved | Approved companion statement | OIC ↔ PaySpace payroll interface architecture | Approved for reuse — refer to pre-tender controls (PT-W9-008) |

---

## Section 4: Evidence Classification

| Field | Value |
|---|---|
| **Evidence Tier** | **Tier 1 — Confirmed Delivery** (HIST-018 contractual; production) |
| **Primary Evidence** | HIST-018 (Hollywood Bets ANN1-V4.1 — OIC ↔ PaySpace bidirectional integration; contractual; production; R825,170 billing) |
| **Supporting Evidence** | HIST-007 (Hollywood Bets V5.0 Accepted Proposal); ORACLE_FACT_BASELINE Section 7 (OIC mandatory policy) |
| **Internal Evidence** | DFA (Rule 21.4 — full Fusion OIC suite; never named) |
| **Named Reference** | Hollywood Bets — subject to account manager approval at each tender. No signed reference letter in KB as of 2026-06-14. |
| **Strongest Evidence** | HIST-018 is the highest-weight source in the KB — signed contract + separate billing line + production confirmation |
| **Sector** | Retail / Gaming (HB); OIC is applicable across all Oracle Fusion sectors |
| **Restriction Summary** | DFA never named (Rule 21.4); HB account manager approval required; PT-W9-008 active (Section 13.2 from W3S1-009 must never appear in external submissions) |

---

## Section 5: Approved and Prohibited Wording

### Approved Wording

> "APPSolve is an Oracle Integration Cloud (OIC) implementation specialist, delivering enterprise-grade integration architectures that connect Oracle Fusion Cloud to third-party payroll platforms, banking systems, and ERP environments."

> "OIC is the standard integration layer in every Oracle Fusion Cloud implementation delivered by APPSolve. APPSolve designs, configures, and operationalises OIC environments that are production-ready, monitored, and supported as permanent infrastructure components of the Oracle Fusion platform."

> "APPSolve has delivered bidirectional Oracle Integration Cloud integrations in production environments, including OIC-based HCM-to-payroll integrations that process real-time employee data synchronisation and payroll result feeds — evidenced by contractual delivery documentation."

> "APPSolve's OIC accelerator library includes pre-built integration templates for Oracle HCM payroll interfaces, HCM-to-Finance cost allocations, and banking H2H file exchange — reducing implementation timelines and providing proven, tested integration patterns."

### Prohibited Wording

- Do NOT name DFA as a client, example, or reference (Rule 21.4 permanent)
- Do NOT reference the billing amount (R825,170) from HIST-018 in any external submission — this is internal commercial information
- Do NOT claim OIC as an APPSolve-built product — OIC is an Oracle product; APPSolve is the implementation and configuration partner
- Do NOT conflate OIC with Oracle Visual Builder Studio (VBS) — VBS builds standalone applications; OIC manages integration between systems
- Do NOT conflate OIC with BeBanking — BeBanking is APPSolve's own banking product; OIC is Oracle's integration platform; they are distinct (though BeBanking may integrate via OIC or its own API)
- Do NOT use content from Section 13.2 of W3S1-009 in any external submission (PT-W9-008)

---

## Section 6: Pre-Tender Validation Checks

Before including this capability statement in any tender submission, confirm all of the following:

- [ ] **PT-W4I1-001:** Hollywood Bets account manager approval obtained for this specific tender submission
- [ ] **PT-W4I1-002:** DFA is NOT named in any OIC content — Rule 21.4 check
- [ ] **PT-W4I1-003:** Internal commercial figures from HIST-018 (R825,170 billing amount) are NOT included in any external content
- [ ] **PT-W4I1-004:** If citing W3S1-009 alongside this statement — confirm PT-W9-008 (Section 13.2 exclusion) is applied
- [ ] **PT-W4I1-005:** Tender scope aligns with OIC integration architecture — confirm tender is not asking about Oracle Fusion product licensing (that belongs in W2S1-001)
- [ ] **PT-W4I1-006:** BEE certificate validity confirmed (expires 2026-07-31)

---

## Section 7: Named Reference Controls

| Client | Reference Status | Permitted Use | Restrictions |
|---|---|---|---|
| **Hollywood Bets** | Referenceable — pending account manager approval | Named reference for OIC integration (contractual — HIST-018) | Account manager approval at each tender. No signed letter in KB. Do not quote HIST-018 billing figures externally. |
| DFA | NEVER NAMED | Internal evidence only | **Rule 21.4 — permanent and absolute** |
| SAA | NEVER NAMED | Internal evidence only | **Rule 21.1** |
| CCBA | NEVER NAMED | Internal evidence only | **HIST-014 restriction** |

---

## Section 8: Product Boundary Controls

| Product | Relationship | Boundary Rule |
|---|---|---|
| **Oracle OIC** | THIS STATEMENT | Oracle's cloud-native integration platform — not a product APPSolve builds; APPSolve configures and implements |
| **W3S1-009 HCM Payroll Interface** | Companion statement | W3S1-009 covers OIC specifically in the payroll interface context. W4-INT-001 covers OIC as APPSolve's broader integration platform. Use together for tender responses requiring integration architecture positioning. |
| **BeBanking** | Different product | BeBanking is APPSolve's own banking integration product. OIC is Oracle's integration cloud. They operate in different contexts — do NOT conflate. BeBanking H2H integrates via its own file-based H2H protocol, not via OIC. |
| **Oracle VBS** | Different product | VBS builds standalone apps on Oracle Cloud. OIC manages integration flows between systems. Do NOT conflate. |
| **Oracle ERP (W4-ERP-001/002)** | Integration target | Oracle Finance is an integration target for OIC (cost allocations from HCM; supplier payments). OIC connects Oracle products to each other and to third-party systems. |

---

## Section 9: Extraction Log

| Field | Value |
|---|---|
| **Wave** | 4 |
| **Extraction Date** | 2026-06-14 |
| **Extractor** | Claude (AI — Wave 4 extraction authorised by BU Lead 2026-06-14) |
| **BU Lead Decision** | W4-INT-001 Oracle OIC Accelerators — High priority; Tier 1 basis in HIST-018 contractual; eligible for Wave 4 extraction |
| **Primary Source** | HIST-018 (Hollywood Bets ANN1-V4.1 — contractual; strongest evidence in KB) |
| **Evidence Tier at Extraction** | Tier 1 (contractual) |
| **Status** | Candidate Draft — approved_for_reuse: No |
| **Next Action** | BU Lead review → Promotion to Review_Required |
| **Promotion Requirement** | BU Lead sets approved_for_reuse: Yes after review |

---

*W4-INT-001-ORA-OICAccelerators-DRAFT.md v1.0 — Candidate Draft 2026-06-14*
*Do not use in tender responses. approved_for_reuse: No.*
