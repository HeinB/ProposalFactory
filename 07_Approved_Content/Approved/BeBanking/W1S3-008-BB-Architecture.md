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
kb_destination: "06_Capabilities/BeBanking/Architecture/"
---

# BeBanking — Technical Architecture

## Architecture Overview

BeBanking uses an API-first, server-to-server integration architecture. The system connects an organisation's ERP directly to the bank's H2H processing infrastructure without requiring a dedicated banking server on the client side, internet banking portals, or manual file handling.

The architecture has two integration boundaries:
1. **ERP-side:** BeBanking integrates with the ERP's financial modules to initiate payments, receive bank responses, and post reconciliation data
2. **Bank-side:** BeBanking connects to each bank's H2H infrastructure via API (primary) or SFTP (fallback)

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                         ERP System                                │
│                                                                   │
│  AP Module ──┐                              ┌── CE Module         │
│  PAY Module ─┤                              ├── GL Module         │
│              └──── BeBanking Integration ───┘                     │
│                         Layer                                     │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             │  API / SFTP (TLS encrypted)
                             │
              ┌──────────────▼───────────────┐
              │       BeBanking API Layer     │
              │      (Integration Engine)     │
              └──────────────┬───────────────┘
                             │
                             │  API (primary) / SFTP over SSH (fallback)
                             │
              ┌──────────────▼───────────────┐
              │     Bank H2H Systems          │
              │     (9 supported banks)       │
              │  ABSA | FNB | Nedbank SA/NA   │
              │  Standard SA/NA | Investec    │
              │  Citi UK | Santander Chile    │
              └───────────────────────────────┘
```

**Notes on the diagram:**
- The BeBanking Integration Layer is deployed within or adjacent to the ERP environment
- The BeBanking API Layer manages secure, encrypted communication with bank H2H endpoints
- No dedicated banking server is required — the API Layer replaces the role of the former dedicated server
- Deployment supports on-premises ERP (Oracle EBS, SAP) and cloud ERP (Oracle Fusion, Acumatica)

---

## Component Architecture

### BeBanking Integration Layer (ERP-side)

The ERP-side layer handles all interaction with ERP modules:

| Function | Description |
|---|---|
| Payment file generation | Constructs bank-format payment files from ERP AP/Payroll payment batches |
| Approval workflow engine | Manages the configurable approval workflow; enforces SOD controls; audit trail |
| Bank statement import | Receives bank statement data from the API Layer; posts to CE/Cash Management |
| Exchange rate loading | Posts daily exchange rates to GL/CE from the configured rate provider |
| Bank response processing | Receives accepted/rejected payment results; posts to AP/PAY for reconciliation |
| Remittance generation | Generates PDF remittance advices and delivers by email on payment confirmation |

### BeBanking API Layer (bank-side)

The bank-facing layer handles all communication with bank H2H systems:

| Function | Description |
|---|---|
| API connectivity | Manages REST/HTTPS connections to bank API endpoints; TLS encrypted |
| SFTP connectivity | Manages SFTP over SSH for banks that do not expose API endpoints |
| Payment file transmission | Delivers payment files to the bank's H2H processing infrastructure |
| Bank response retrieval | Retrieves payment response files from the bank |
| Bank statement retrieval | Retrieves daily bank statement files from the bank |
| Multi-bank routing | Manages concurrent connections to multiple bank institutions |

---

## ERP Integration Points

| Function | ERP Module | Direction | Notes |
|---|---|---|---|
| Supplier payment file generation | AP | ERP → BeBanking | Includes void processing and remittance |
| Payroll file generation | PAY | ERP → BeBanking | ACB format; Oracle EBS and Oracle Fusion only — see payroll scope note |
| Bank statement import | CE | BeBanking → ERP | Daily reconciliation; Unbreakable Bank Statements |
| Exchange rate loading | GL / CE | BeBanking → ERP | FNB, Andisa, or ExchangeRate-API (client choice) |
| Bank response processing | AP / PAY | BeBanking → ERP | Accepted/rejected reconciliation per payment |

**Payroll scope note:** Payroll H2H is supported from Oracle EBS and Oracle Fusion Applications payroll modules. Acumatica does not provide payroll functionality in the South African market.

---

## Deployment Requirements

| Requirement | Specification |
|---|---|
| BeBanking Integration Layer | Application server; deployed on-premises (for EBS/SAP) or as cloud-hosted instance (for Oracle Fusion, Acumatica) |
| Network: ERP connectivity | Standard LAN/WAN connectivity to ERP application server |
| Network: Bank connectivity | Outbound HTTPS (API) or SFTP/SSH to bank H2H endpoints — standard internet or leased-line connectivity |
| Dedicated banking server | **Not required** — the API Layer handles all bank connectivity; no on-premises bank server is needed |
| Internet banking portal | Not used — all payment transmission is server-to-server |
| Firewall requirements | Outbound HTTPS (port 443) to bank API endpoints; outbound SFTP (port 22) for SFTP-connected banks |

### Cloud ERP Deployment
For organisations running Oracle Fusion Applications or Acumatica, the BeBanking Integration Layer can be deployed as a cloud-hosted instance. This eliminates on-premises middleware requirements entirely and aligns with cloud-native ERP deployment models.

---

## Security Architecture

| Principle | Implementation |
|---|---|
| Encrypted transmission | TLS for all API connections; SSH for SFTP connections |
| Server-to-server architecture | Payment files never pass through internet banking portals or email |
| Approval-gated transmission | No payment file is transmitted unless the full configured approval workflow is complete |
| ERP-native access control | All user permissions managed through ERP responsibilities — no external portal |
| Segregation of duties | AP approvers and Payroll approvers are independently defined; mutual exclusion enforced |
| Audit trail | Complete, immutable audit trail for all approvals, transmissions, and bank responses within the ERP |
| Bank account integrity | No payment transmitted to an unapproved bank account (enforced by Supplier Bank Account Approval and AVS modules) |

---

**Remediation notes (2026-06-10):** Changes applied against BeBanking_CAPABILITY_MAP.md (§5, §6).
- Connect Direct removed throughout — replaced with API/SFTP per F-C-01 (BQ1). Connect Direct is retired.
- "Dedicated Bank Server (APPSolve-managed)" removed from architecture diagram and deployment requirements — not required in API-first model (BQ1).
- Secure File Transfer Utility component section removed entirely — module retired (BQ7).
- IBY (Oracle Internet Banking) reference removed from ERP requirements — not required in current architecture (see W1S3-006).
- "Automated Receipt Creation" row removed from ERP Integration Points table — module retired (BQ7).
- Architecture diagram redrawn to reflect API Layer replacing Dedicated Bank Server; bank list from confirmed 9-bank baseline (BQ4).
- Cloud ERP deployment note added for Oracle Fusion and Acumatica (BQ5, BQ6).
- Payroll scope note added to ERP Integration Points table.

**Original source review notes:** Architecture content from SITA BeBanking Proposal v1.06 (2017) — Section 4 (H2H Technology Architecture) and Appendix diagram. The 2017 architecture used Connect Direct with a Dedicated Banking Server. Both are retired in the current product. Secure File Transfer Utility described as a module component in 2017 — module was retired per BQ7. The rewritten architecture reflects the API-first model confirmed by BQ1 (2026-06-10).
