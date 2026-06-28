# Gap Register — WP6 Content Gaps
**Work Package:** WP6 — Tender Simulation & Coverage Assessment | **Version:** 1.0 | **Created:** 2026-06-14
**Pilot:** AFROSAI-E Acumatica Proposal May 2026
**Scope:** Recurring content gaps that affect tender coverage. Excludes by-design gaps (CVs, pricing, project plans, compliance docs).

---

## How to Read This Register

**Frequency:** How many tender types this gap affects (per ANSWER_ASSEMBLY_FRAMEWORK.md recipes)
**Business impact:** Revenue/win-rate effect if gap persists
**Recommended asset:** Minimum content required to close gap

Gaps are ordered by **tender impact** (frequency × severity).

---

## Gap Register

### GAP-001 — Acumatica Post-Implementation Support Model

| Field | Detail |
|---|---|
| **Gap ID** | GAP-001 |
| **Description** | No approved Acumatica support model exists in the KB. Post-implementation support is a mandatory section in every ERP implementation proposal. AFROSAI-E required this section — it was authored from scratch. W2S1-004 covers Oracle managed services only and cannot be repurposed. |
| **Affected Tender Sections** | Section 6.1 (support model), 6.2 (SLAs), 6.3 (help desk / escalation) |
| **Frequency** | **Every Acumatica tender** — 100% of Acumatica proposals require post-implementation support |
| **Business impact** | **Critical.** Without this section, every Acumatica proposal requires 2-4 hours of from-scratch authoring. In competitive tenders, support capability is often a scored criterion. Weak or generic support sections reduce win probability. |
| **Tenders affected** | AFROSAI-E (confirmed gap); all future Acumatica tenders |
| **Recommended asset** | **W5-ACU-001 — Acumatica Support & Managed Services Model** |
| **Recommended content** | Tier model (Bronze/Silver/Gold), response times, help desk process, escalation path, monitoring approach, hypercare-to-steady-state transition, APPSolve Acumatica consultant bench. Evidence: existing Acumatica clients receiving support (Interconnect, HyDac, DSSSA, FuelU2, Maxiflex — not yet formalised in KB). |
| **Effort to create** | Medium — 1 day. BU Lead authorisation required. Evidence must come from confirmed support relationships (do not infer). |
| **Priority** | **1 — CRITICAL** |

---

### GAP-002 — Acumatica Implementation Methodology (De-branded / Platform-Agnostic)

| Field | Detail |
|---|---|
| **Gap ID** | GAP-002 |
| **Description** | W2S1-005 is a comprehensive Oracle implementation methodology (16 sections, OUM-based, Oracle Unified Method, FBDI, CSN, Oracle Guided Learning). For every Acumatica tender, consultants must de-brand this document — removing ~30 Oracle-specific references and replacing with Acumatica equivalents. The AFROSAI-E submission used a separate APPSolve Project Methodology PDF (Feb 2024) that predates the KB and is not approved for reuse. |
| **Affected Tender Sections** | Section 4.1 (methodology), 4.4 (data migration), 4.5 (testing), 4.6 (governance) |
| **Frequency** | **Every Acumatica tender** and **any non-Oracle tender requiring methodology** |
| **Business impact** | **High.** Each de-branding effort costs 2-3 hours per tender. The Feb 2024 Company Methodology PDF has not been reviewed for accuracy — using it in submissions risks stating outdated or inaccurate facts. |
| **Tenders affected** | AFROSAI-E (confirmed); HyDac (retrospective); all future Acumatica tenders |
| **Recommended asset** | **W5-METH-001 — APPSolve ERP Implementation Methodology (Platform-Agnostic)** |
| **Recommended content** | Extract and de-brand W2S1-005. Replace OUM with "APPSolve Delivery Framework"; replace Oracle-specific tools with generic equivalents; add Acumatica-specific phases (Acumatica SaaS setup, import scenarios, Acumatica University training); retain project governance, change management, and data migration principles unchanged. |
| **Effort to create** | Low-medium — 3-4 hours. No BU Lead authorisation for Wave 5 needed if derived from existing approved W2S1-005. |
| **Priority** | **2 — HIGH** |

---

### GAP-003 — Acumatica Reference Client Register (DSSSA, FuelU2, Maxiflex)

| Field | Detail |
|---|---|
| **Gap ID** | GAP-003 |
| **Description** | AFROSAI-E submitted 4 reference letters (Interconnect, DSSSA, FuelU2, Maxiflex). Only Interconnect (W1S2-006) is formally approved in the KB. DSSSA, FuelU2, and Maxiflex letters are physically present in the AFROSAI-E corpus but not registered in 04_References/Acumatica/. This is a registration gap, not a content gap — the letters exist. |
| **Affected Tender Sections** | Section 7.1 (reference letters), 7.2 (comparable implementations) |
| **Frequency** | **Every Acumatica tender** — references are mandatory in most ERP tenders |
| **Business impact** | **High.** Approved KB clients can be named with confidence. Unregistered clients require manual retrieval and BU Lead confirmation at each tender. With 3 additional registered references, Acumatica reference section goes from "1 confirmed client" to "4 confirmed clients" immediately. |
| **Tenders affected** | AFROSAI-E (letters were retrieved manually); all future Acumatica tenders |
| **Recommended asset** | Not a new capability statement — register existing letters: `04_References/Acumatica/DSSSA-Reference-Letter.pdf`, `FuelU2-Reference-Letter.pdf`, `Maxiflex-Reference-Letter.pdf` |
| **Effort to close** | **Very Low — 1-2 hours.** BU Lead confirms signed status, KB Operator registers in 04_References/Acumatica/ and updates DOCUMENT_REGISTER.csv. |
| **Priority** | **3 — HIGH** |

---

### GAP-004 — Oracle ERP Reference Letters (Investec, NALA, Cape Union Mart, KPMG)

| Field | Detail |
|---|---|
| **Gap ID** | GAP-004 |
| **Description** | W4-ERP-001 (Fusion Finance), W4-ERP-002 (Fusion Procurement), and W4-ERP-003 (PPM) are approved but subject to active restrictions (AM-W4E1-001, AM-W4E2-001, AM-W4E3-001) preventing named client references. Investec, NALA, and Cape Union Mart letters exist in SABS ETS corpus. KPMG letter not found — requires separate approach. |
| **Affected Tender Sections** | Section 7 (references) in Oracle ERP tenders |
| **Frequency** | Every Oracle ERP (Finance, Procurement, PPM) tender — affects 3 of 47 approved assets |
| **Business impact** | **High.** Without named references, Oracle ERP tenders must use anonymous framing ("a South African financial services group") which is weaker in scored RFPs. Named clients with letters are often required for compliance checklist tenders. |
| **Tenders affected** | Any Oracle Fusion Finance or Procurement or PPM tender |
| **Recommended asset** | Register SABS ETS letters in 04_References/Oracle/: Investec (2023-09), NALA, Cape Union Mart. Confirm CUM scope. Register Assore + Adcock Ingram while at it. |
| **Effort to close** | **Very Low — 2-3 hours.** BU Lead confirms scope + signs off. KB Operator registers. DFA letter in same folder must NEVER be registered — Rule 21.4. |
| **Priority** | **4 — HIGH** |

---

### GAP-005 — Acumatica Security, Data Governance, and POPIA Compliance Statement

| Field | Detail |
|---|---|
| **Gap ID** | GAP-005 |
| **Description** | No Acumatica security and data governance statement exists in the KB. W1S3-007 (BeBanking Security) covers BeBanking-specific security only. Public sector tenders (especially inter-governmental organisations like AFROSAI-E) routinely require statements on: data security, access control, audit logging, POPIA compliance, international data residency, disaster recovery, and role-based access. |
| **Affected Tender Sections** | Section 3.8 (security/access control) |
| **Frequency** | Most public sector and financial services Acumatica tenders (estimated 60-70% of Acumatica pipeline) |
| **Business impact** | **Medium-High.** Security is increasingly a scored criterion in public sector tenders. AFROSAI-E as an inter-governmental body with multi-country data would have this as a compliance requirement. Without a statement, section must be authored from scratch or Acumatica's own marketing material repurposed. |
| **Recommended asset** | **W5-ACU-002 — Acumatica Security and Data Governance** |
| **Recommended content** | Role-based access control (RBAC), audit trail, TLS encryption, SOC 1/SOC 2 compliance (Acumatica is SOC 2 Type II certified), data residency (AWS/Azure regions), POPIA compliance posture, multi-factor authentication, disaster recovery (cloud-native). Most content derivable from Acumatica's published security documentation — not from internal corpus. |
| **Effort to create** | Medium — 1 day. Requires BU Lead authorisation for Wave 5 if new asset. |
| **Priority** | **5 — MEDIUM-HIGH** |

---

### GAP-006 — Standalone Change Management / OCM Statement (Platform-Agnostic)

| Field | Detail |
|---|---|
| **Gap ID** | GAP-006 |
| **Description** | Change management and user adoption are consistently required in ERP proposals but no standalone OCM statement exists. The content is embedded in W2S1-005 (Oracle methodology, Deploy phase) and not extractable without de-branding from Oracle. AFROSAI-E Section 5.3 (user adoption) had no KB content to draw from. |
| **Affected Tender Sections** | Section 5.1 (change management), 5.3 (user adoption) |
| **Frequency** | All ERP tenders across all product lines (Oracle + Acumatica) — estimated 80%+ |
| **Business impact** | **Medium.** OCM sections rarely eliminate a bid but can positively differentiate. Current workaround: extract and adapt from W2S1-005 (1-2 hours per tender). Standalone statement would reduce this to <30 minutes. |
| **Recommended asset** | **W5-OCM-001 — APPSolve Change Management & User Adoption Framework (Platform-Agnostic)** |
| **Recommended content** | APPSolve OCM approach (stakeholder mapping, impact assessment, communication plan, training approach, adoption measurement, hypercare). Generic enough for Oracle and Acumatica. Evidence: Hollywood Bets adoption success; Interconnect change management; RedPath Mining (subject to Rule 21.5). |
| **Effort to create** | Low-medium — half day. Derivable from W2S1-005 with de-branding + expansion. |
| **Priority** | **6 — MEDIUM** |

---

### GAP-007 — Acumatica Cloud Hosting / SaaS Model Statement

| Field | Detail |
|---|---|
| **Gap ID** | GAP-007 |
| **Description** | Questions about cloud hosting, SaaS model, availability, and disaster recovery arise in most ERP tenders. No Acumatica hosting statement exists. W1S3-009 covers BeBanking hosting only. Acumatica's cloud-native model (hosted on AWS/Azure, 99.5%+ uptime SLA, no hardware required) is a key competitive differentiator against on-premise ERP alternatives. |
| **Affected Tender Sections** | Section 3.9 (cloud hosting/DR) |
| **Frequency** | Most Acumatica tenders — cloud deployment question is routine |
| **Business impact** | **Medium.** Content is available from Acumatica's public marketing and documentation. Current workaround: reference Acumatica's published SaaS facts (~30 minutes). A KB-approved statement eliminates the risk of overstating or misstating Acumatica's hosting terms. |
| **Recommended asset** | **W5-ACU-003 — Acumatica Cloud Hosting and SaaS Delivery Model** |
| **Recommended content** | Acumatica true-cloud model, AWS/Azure infrastructure, Acumatica SaaS uptime SLA, data backup, DR, no local hardware, subscription licensing, automatic upgrades. All from Acumatica public documentation — straightforward extraction. |
| **Effort to create** | Low — 2-3 hours. |
| **Priority** | **7 — MEDIUM** |

---

### GAP-008 — Acumatica Integration Capability Statement

| Field | Detail |
|---|---|
| **Gap ID** | GAP-008 |
| **Description** | Integration questions (with third-party systems, banking, payroll, document management) arise in most ERP tenders. W1S2-007 (PaySpace integration) and W4-INT-001 (Oracle OIC) do not cover Acumatica's general integration framework. Acumatica has a documented REST API framework and pre-built connectors (Salesforce, HubSpot, major banks) that could be described in a capability statement. |
| **Affected Tender Sections** | Section 3.7 (integration) |
| **Frequency** | ~60% of Acumatica tenders — integration questions most common in larger deals |
| **Business impact** | **Low-Medium.** Integration sections are usually not primary evaluation criteria. Current workaround: reference W1S2-007 (PaySpace integration as example) + describe Acumatica REST API framework from public documentation (~45 minutes). |
| **Recommended asset** | **W5-ACU-004 — Acumatica Integration Framework** |
| **Recommended content** | Acumatica REST API framework, OData endpoints, Acumatica webhooks, pre-built connectors (banking: BeBanking, PaySpace; document management: DocuSign; CRM: Salesforce). |
| **Effort to create** | Low — 2-3 hours. |
| **Priority** | **8 — LOW-MEDIUM** |

---

## Gap Summary Table

| Gap ID | Description | Frequency | Priority | Effort | Type |
|---|---|---|---|---|---|
| GAP-001 | Acumatica Support Model | Every Acumatica tender | **Critical** | Medium | New asset |
| GAP-002 | Platform-Agnostic Methodology | Every Acumatica tender | **High** | Low-medium | Adapt W2S1-005 |
| GAP-003 | Acumatica Reference Letters (DSSSA/FuelU2/Maxiflex) | Every Acumatica tender | **High** | Very Low | Registration only |
| GAP-004 | Oracle ERP Reference Letters (Investec/NALA/CUM/KPMG) | Every Oracle ERP tender | **High** | Very Low | Registration only |
| GAP-005 | Acumatica Security/Data Governance | ~60-70% Acumatica tenders | **Medium-High** | Medium | New asset |
| GAP-006 | Standalone OCM / Change Management | ~80% all ERP tenders | **Medium** | Low-medium | Adapt W2S1-005 |
| GAP-007 | Acumatica Cloud Hosting / SaaS | Most Acumatica tenders | **Medium** | Low | New asset |
| GAP-008 | Acumatica Integration Framework | ~60% Acumatica tenders | **Low-Medium** | Low | New asset |

---

## Quick Wins (Close Immediately Without Wave 5 Authorisation)

**GAP-003 and GAP-004 can be closed in 1-2 days with zero capability extraction work:**
- GAP-003: BU Lead confirms DSSSA/FuelU2/Maxiflex letters signed → KB Operator registers in 04_References/Acumatica/
- GAP-004: BU Lead confirms Oracle letters (Investec/NALA/CUM) signed + CUM scope → KB Operator registers in 04_References/Oracle/

**GAP-002 can be closed without Wave 5 authorisation** — it is a de-branding of the already-approved W2S1-005, not new extraction.

---

*GAP_REGISTER.md v1.0 — WP6 2026-06-14. 8 gaps identified. 2 registrations (GAP-003, GAP-004) can be closed immediately. 1 adaptation (GAP-002) can be done without Wave 5 authorisation. 4 new assets (GAP-001, GAP-005, GAP-007, GAP-008) require Wave 5 authorisation.*
