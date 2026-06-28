---
source_document: "APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
source_path: "Parties/Customers/SITA/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
extraction_date: "2026-06-08"
extracted_by: "Claude (AI extraction — requires human review)"
remediation_date: "2026-06-10"
remediated_by: "Claude (AI remediation — requires human review)"
readiness: "MODERNISE"
approved_for_reuse: "Yes"
lifecycle_status: APPROVED
business_unit: "BeBanking"
review_status: "Approved"
reviewer: "Hein Blignaut"
approved_date: "2026-06-10"
approved_by: "Hein Blignaut"
kb_destination: "06_Capabilities/BeBanking/OCI_Hosting/"
---

# BeBanking — Hosting Model and Commercial Terms

## Hosting Overview

BeBanking operates as a managed banking middleware service. APPSolve manages the BeBanking application layer, banking integrations, and ongoing bank H2H connectivity on behalf of clients. Clients do not need to procure banking software, manage Connect Direct licences, or maintain dedicated banking infrastructure.

The hosting model supports both on-premises ERP deployments (Oracle EBS, SAP) and cloud ERP deployments (Oracle Fusion Applications, Acumatica).

---

## Deployment Architecture

### On-Premises ERP Deployment (Oracle EBS, SAP)

| Component | Responsibility | Notes |
|---|---|---|
| BeBanking Integration Layer | APPSolve-hosted or client-hosted application server | Deployed in the client's network for proximity to ERP |
| ERP integration | Client ERP environment | BeBanking integrates via ERP APIs — no dedicated banking server hardware required |
| Bank connectivity | Outbound API / SFTP over SSH | Standard internet or leased-line connectivity; no bank-specific hardware required |
| Banking credentials and certificates | APPSolve-managed | APPSolve manages the bank H2H onboarding, credentials, and maintenance |

### Cloud ERP Deployment (Oracle Fusion, Acumatica)

| Component | Responsibility | Notes |
|---|---|---|
| BeBanking Integration Layer | APPSolve cloud-hosted instance | Cloud-to-cloud architecture; no on-premises BeBanking component required |
| ERP integration | Cloud ERP environment (Oracle Fusion / Acumatica) | API-based integration |
| Bank connectivity | Outbound API / SFTP | Standard cloud outbound connectivity |
| Banking credentials and certificates | APPSolve-managed | Same managed model as on-premises |

---

## Support Model

APPSolve provides a managed H2H banking service for BeBanking clients:

| Support area | Description |
|---|---|
| Bank connectivity monitoring | 24x7 monitoring capability with after-hours support services |
| Banking integration maintenance | APPSolve manages all bank-side changes — bank format updates, new bank onboarding, bank credential renewals |
| Bank statement delivery | Daily automated bank statement retrieval — failures are monitored and resolved before business start |
| H2H profile management | APPSolve manages client H2H profiles with each bank; clients do not interact with bank H2H operations teams directly |
| ERP integration support | Application support for BeBanking integration layer; ERP module compatibility maintained per ERP version upgrade |
| Upgrade management | BeBanking module updates delivered by APPSolve; no client downtime required for BeBanking updates |

*Support model confirmed against current operational capability (BQ8, BQ10, 2026-06-10 — Hein Blignaut).*

---

## Commercial Model — Licensing

BeBanking is available under a subscription-only commercial model. There is no once-off licence option.

| Option | Structure | Notes |
|---|---|---|
| **Monthly subscription** | Per module, per month | OPEX model — payable monthly |
| **Annual subscription** | Per module, per year | OPEX model — payable annually; typically includes a discount vs monthly |

### Commercial Model Notes

- All BeBanking modules are priced individually — clients subscribe only to the modules they use
- Modules can be added incrementally as the client's banking automation scope expands
- There is no software licence ownership, no once-off implementation fee for the product component, and no perpetual licence

---

**Remediation notes (2026-06-10):** Changes applied against BeBanking_CAPABILITY_MAP.md (§5, §9).
- Connect Direct hosting references removed throughout — replaced with API-first architecture description (BQ1). Previous content described the BeBanking hosting model around hosting Connect Direct software and SSH certificate stores on a dedicated banking server.
- "Dedicated Banking Server" section removed — not required in current architecture (BQ1, see W1S3-008).
- "24x7x365 standby" corrected to "24x7 monitoring capability with after-hours support services" (BQ8 / BQ10 confirmed service model).
- Cloud ERP deployment section added — Oracle Fusion and Acumatica cloud deployment model added (BQ5, BQ6).
- Licensing Model section completely rewritten: Service Option and Software Option (obsolete once-off/licence models) replaced with Monthly subscription and Annual subscription only (BQ9 — subscription-only model confirmed).
- [UPDATE] placeholder for licensing confirmation removed — replaced with confirmed subscription model.

**Original source review notes:** Hosting model and commercial terms from SITA BeBanking Proposal v1.06 (2017) — Section 5 (Commercial and Support Terms). The 2017 proposal described a dedicated banking server hosted by APPSolve running Connect Direct. Commercial model offered Service Option (once-off + monthly) and Software Option (once-off licence + annual support). Both the infrastructure model and the commercial model have been superseded. All replacements sourced from BU lead confirmation (BQ1, BQ8, BQ9, BQ10) 2026-06-10.
