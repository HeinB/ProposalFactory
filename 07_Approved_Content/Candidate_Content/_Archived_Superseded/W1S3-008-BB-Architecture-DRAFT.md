---
source_document: "APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
source_path: "Parties/Customers/SITA/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
extraction_date: "2026-06-08"
extracted_by: "Claude (AI extraction — requires human review)"
readiness: "MODERNISE"
approved_for_reuse: "No"
business_unit: "BeBanking"
review_status: "Candidate"
---

> **DRAFT — NOT APPROVED FOR TENDER USE**
> Readiness: MODERNISE | Review required by: Hein Blignaut

---

# BeBanking — Technical Architecture

## Note on Diagrams

The SITA BeBanking Proposal v1.06 includes a section titled "Host to Host Process Flow" (Appendix 5.2). This section heading was found in the document structure but the content is likely a diagram — the XML parser extracted no text from this section, which typically indicates image-only content.

**[UPDATE: Open SITA BeBanking Proposal v1.06 PDF directly and review Appendix 5.2 to extract or describe the process flow diagram. This is important content for architecture documentation.]**

## Architectural Overview

BeBanking operates as a middleware layer between the ERP application and the bank's host systems:

```
┌─────────────────────────────────────────────────────────────┐
│                         ERP System                           │
│   AP Module ──┐                         ┌── CE Module        │
│   PAY Module ─┤                         ├── AR Module        │
│               └──── BeBanking Layer ────┘                    │
└───────────────────────────┬─────────────────────────────────┘
                            │ Connect Direct / SFTP
                            │ SSH Certificates
                ┌───────────▼────────────┐
                │  Dedicated Bank Server │
                │  (APPSolve-managed)    │
                └───────────┬────────────┘
                            │ H2H Banking Channel
                ┌───────────▼────────────┐
                │   Bank H2H System      │
                │   (Standard Bank, etc.)│
                └────────────────────────┘
```

## Component Architecture

### Dedicated Banking Server

A separate banking server is deployed to handle all file transfer operations between the ERP and the bank:

- Hosts the Connect Direct software and SSH key pairs
- Provides a predefined and access-controlled file transfer directory
- Monitored and maintained separately from the ERP application server
- All file transfer access is logged and controlled from within the ERP

### Secure File Transfer Utility

The Secure File Transfer (SFT) utility is BeBanking's file management component:

- Manages file transfer between client and server, and server to server
- Files are available and secured in a predefined directory
- Access is monitored and controlled from within Oracle EBS or Acumatica
- Can be used for non-banking file transfer requirements (general server-to-server automation)

### ERP Integration Points

| Integration | Module | Type |
|---|---|---|
| Payment file generation | AP → BeBanking | Export |
| Payroll file generation | PAY → BeBanking | Export |
| Bank statement import | BeBanking → CE | Import |
| Bank response processing | BeBanking → AP/PAY | Import |
| Receipt auto-creation | BeBanking → AR | Import |
| Exchange rate loading | BeBanking → GL/CE | Import |

## Deployment Requirements

- Dedicated banking server accessible from the ERP application server
- Connect Direct connectivity to the bank's H2H system **[UPDATE: confirm whether Connect Direct or SFTP is the current channel]**
- SSH certificates configured between the banking server and the bank
- VPN access for APPSolve implementation and support resources
- ERP modules AP, PAY, IBY (Oracle) or equivalent (Acumatica) must be implemented and functioning

---

**Review notes:** Architecture description synthesised from the Proposed Engagement section and Assumptions in SITA BeBanking v1.06 (June 2017). The process flow diagram in Appendix 5.2 was not extractable from XML — the PDF version should be opened to recover this diagram, which would be valuable for tender submissions. The architecture described is Oracle EBS-specific. MODERNISE rating: (1) Acumatica architecture needs separate documentation, (2) confirm whether Connect Direct is still the primary channel or has been replaced by SFTP/API, (3) cloud-hosted ERP considerations may change the banking server deployment model.
