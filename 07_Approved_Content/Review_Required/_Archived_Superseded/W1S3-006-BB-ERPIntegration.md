---
source_document: "APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
source_path: "Parties/Customers/SITA/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
extraction_date: "2026-06-08"
extracted_by: "Claude (AI extraction — requires human review)"
remediation_date: "2026-06-10"
remediated_by: "Claude (AI remediation — requires human review)"
readiness: "MODERNISE"
approved_for_reuse: "No"
business_unit: "BeBanking"
review_status: "Review_Required"
reviewer: "Hein Blignaut"
---

> **REVIEW REQUIRED — NOT APPROVED FOR TENDER USE**
> Readiness: MODERNISE | Promoted to Review_Required: 2026-06-10 | Reviewer: Hein Blignaut

---

# BeBanking — ERP Integration

## Overview

BeBanking integrates natively with multiple ERP platforms. In each case, BeBanking sits alongside the ERP as a specialised banking middleware layer — it does not replace ERP modules but augments them with H2H banking automation. Integration is bidirectional: the ERP pushes payment instructions to BeBanking; BeBanking returns bank responses and bank statement data to the ERP.

All ERP connectivity uses API-based integration or SFTP over SSH. No dedicated banking server is required on the client side.

---

## Oracle E-Business Suite (Oracle EBS)

### Supported Versions
Oracle EBS R11 and R12 (on-premises deployments).

### Integration Architecture
BeBanking communicates with Oracle EBS via standard Oracle API interfaces. There is no Oracle Internet Banking (IBY) module dependency in the current architecture — BeBanking provides its own ERP-side integration layer that interfaces directly with AP, Payroll, Cash Management, and General Ledger.

### Supported Oracle EBS Modules

| Oracle EBS Module | Integration Type | Direction | Purpose |
|---|---|---|---|
| Accounts Payable (AP) | Payment processing | ERP → BeBanking | Supplier payment file generation, void processing, remittance delivery |
| Payroll (PAY) | Payroll processing | ERP → BeBanking | Payroll ACB file generation and H2H transmission |
| Cash Management (CE) | Bank statement reconciliation | BeBanking → ERP | Daily bank statement import; bank response auto-matching |
| General Ledger (GL) | Exchange rates | BeBanking → ERP | Daily automated foreign exchange rate loading |

### Oracle EBS Integration Notes
- Deep AP integration includes payment void and reversal processing with automatic remittance recall
- Payroll ACB file format is supported from Oracle EBS PAY module; payroll approvers are segregated from AP approvers via separate H2H profiles
- Bank statement import handles non-standard statement numbering and transaction codes (Unbreakable Bank Statements)
- Exchange rate loading supports FNB, Andisa, and ExchangeRate-API as sources (client choice)

---

## Oracle Fusion Applications

### Supported Versions
Oracle Cloud ERP (Oracle Fusion Applications) — current cloud release.

### Integration Architecture
Oracle Fusion integration uses the same BeBanking middleware layer. The Oracle Internet Banking (IBY) module is EBS-specific and does not apply to Oracle Fusion integration — do not reference IBY when describing Fusion integration.

### Supported Oracle Fusion Modules

| Oracle Fusion Module | Integration Type | Direction | Purpose |
|---|---|---|---|
| Oracle Fusion Payables | Payment processing | ERP → BeBanking | Supplier payment file generation, approval, remittance delivery |
| Oracle Fusion Payroll | Payroll processing | ERP → BeBanking | Payroll H2H file generation and transmission |
| Oracle Fusion Cash Management | Bank statement reconciliation | BeBanking → ERP | Daily bank statement import; bank response matching |
| Oracle Fusion General Ledger | Exchange rates | BeBanking → ERP | Daily automated foreign exchange rate loading |

### Oracle Fusion Integration Notes
- Cloud ERP deployment is supported; no on-premises infrastructure required for Fusion integration
- Payroll H2H from Oracle Fusion Payroll is fully supported — Oracle Fusion is a confirmed payroll source for BeBanking Payroll H2H

---

## Acumatica

### Supported Versions
Acumatica (cloud-native ERP, current release).

### Integration Architecture
BeBanking integrates with Acumatica via the Acumatica Payments and Acumatica Cash Management modules using REST API integration. This is a cloud-to-cloud integration model.

### Supported Acumatica Modules

| Acumatica Module | Integration Type | Direction | Purpose |
|---|---|---|---|
| Acumatica Payments | Payment processing | ERP → BeBanking | Local and foreign currency supplier payment file generation and H2H transmission |
| Acumatica Cash Management | Bank statement reconciliation | BeBanking → ERP | Bank statement import and reconciliation |

### Confirmed Acumatica Capabilities Through BeBanking
- Local payments (ZAR domestic EFT and ACH)
- Foreign currency payments (forex H2H through International and Forex Payment Processing module)
- Bank statement processing and reconciliation

### Acumatica Payroll Exclusion
Acumatica does not provide payroll functionality in the South African market. BeBanking Payroll H2H is not available from an Acumatica payroll source. Do not describe or imply Acumatica payroll workflows, ACB file generation from Acumatica, or payroll H2H transmission from Acumatica in any content.

---

## SAP

BeBanking is compatible with SAP ERP. Integration follows the same BeBanking middleware model — payment files generated from SAP AP and transmitted via the BeBanking H2H layer. Detailed SAP module and version support is available from the BeBanking BU lead.

---

## Integration Connectivity Requirements

| Requirement | Specification |
|---|---|
| Bank connectivity — primary | API integration (REST/HTTPS, TLS encrypted) |
| Bank connectivity — fallback | SFTP over SSH (for banks without API endpoints) |
| ERP connectivity | Standard ERP API interfaces |
| Dedicated banking server | Not required — API-first architecture eliminates on-premises bank connectivity hardware |
| Internet banking portal | Not used — all transmission is server-to-server |

---

**Remediation notes (2026-06-10):** Changes applied against BeBanking_CAPABILITY_MAP.md (§3, §5).
- IBY (Oracle Internet Banking) reference removed from Oracle EBS section — IBY is an EBS-specific legacy module not required in the current architecture; explicitly excluded from Fusion section.
- Connect Direct removed throughout — replaced with API/SFTP per F-C-01 (BQ1).
- Secure File Transfer Utility removed from architecture and requirements — module retired (BQ7).
- Automated Receipt Creation removed from ERP integration table — module retired (BQ7); "Receipt auto-creation / BeBanking → AR" row is gone.
- Oracle Fusion section added from scratch — confirmed by BQ6.
- Acumatica section: placeholder replaced with confirmed integration detail (BQ5). Acumatica payroll exclusion added per L-C-001 rule.
- SAP section added — confirmed by BU lead 2026-06-10.

**Original source review notes:** ERP integration content from SITA BeBanking Proposal v1.06 (2017) — Section 4 (H2H Technology) and Module Architecture sections. Oracle EBS was the sole ERP at the time. Oracle Fusion, Acumatica, and SAP sections authored from confirmed baseline (BQ5, BQ6, BU confirmation of SAP). Connect Direct and IBY references were 2017-era components; both retired.
