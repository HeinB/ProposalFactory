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

# BeBanking — Monitoring and Automation

## Overview

BeBanking automates the repetitive operational tasks in the banking lifecycle. Once configured, the system runs scheduled and event-driven processes without manual intervention. APPSolve monitors the BeBanking environment and the bank connectivity layer to ensure daily processes complete reliably.

---

## Automated Processes

| Process | Trigger | Channel | Frequency | ERP Destination |
|---|---|---|---|---|
| Bank statement import | Scheduled — daily | API or SFTP | Daily | CE / Cash Management |
| Payment response matching | Event-driven — bank response received | Bank H2H | Per payment batch | AP / Payroll |
| Supplier PDF remittance delivery | Event-driven — payment confirmed | Email (SMTP) | Per payment batch | AP |
| Exchange rate loading | Scheduled — daily | FNB / Andisa / ExchangeRate-API (client choice) | Daily | GL / CE |
| Payment approval notifications | Event-driven — batch awaiting approval | Email | Per approval request | Workflow |

**Note on table changes:** The Automated Receipt Creation process has been removed from this table. The Automated Receipt Creation module has been retired and is no longer part of the BeBanking module portfolio. Do not reference AR receipt creation as a BeBanking-automated process.

---

## Automated Bank Statement Management

BeBanking's Unbreakable Bank Statements module provides automated, daily bank statement management:

- **Automated retrieval:** Bank statements are retrieved automatically each business day via API or SFTP — no manual download or portal login required
- **Non-standard handling:** BeBanking is engineered to handle non-standard bank statement structures, including banks that use non-sequential statement numbers or non-standard transaction codes
- **ERP reconciliation:** Retrieved statements are automatically imported into the ERP Cash Management (CE) module; transactions are matched against outstanding ERP records
- **Exception management:** Unmatched transactions are flagged for review within the ERP; APPSolve monitors for statement retrieval failures and resolves before business start
- **Audit trail:** Complete statement import history maintained within the ERP

---

## Exchange Rate Automation

BeBanking automates daily foreign exchange rate loading into the ERP:

- **Multi-provider support:** Clients select their preferred rate provider — supported providers are FNB, Andisa, and ExchangeRate-API
- **Automated daily load:** Rates are loaded automatically once per business day, eliminating manual treasury data entry
- **ERP integration:** Rates post directly to GL and CE; available immediately for payment processing and reporting
- **No manual intervention:** The full rate retrieval and ERP posting process is unattended

---

## Monitoring and Operational Oversight

### APPSolve Operational Monitoring

APPSolve provides ongoing monitoring of the BeBanking environment:

| Monitoring area | Description |
|---|---|
| Bank connectivity | Continuous monitoring of API and SFTP connections to all integrated banks |
| Bank statement retrieval | Daily confirmation that all bank statement imports completed successfully before client business hours |
| Payment transmission | Real-time monitoring of payment file delivery and bank response receipt |
| Exchange rate loading | Daily confirmation of rate loading to ERP |
| Integration layer health | Application health monitoring for the BeBanking Integration Layer |

*Monitoring capabilities confirmed against current product functionality (BQ10, 2026-06-10 — Hein Blignaut).*

### Client-Side Audit and Reporting

Clients have direct access to the following within the ERP:

| Report / View | Description |
|---|---|
| Payment approval status | Current approval workflow status for all payment batches — which level, who has approved, what is pending |
| Payment transmission log | Full transmission history — file sent, bank response received, timestamp, accepted/rejected counts |
| Bank statement import log | Import history — date, bank, statement period, transaction count, match status |
| Bank account maintenance audit | Full change history for supplier banking details — who changed, when approved, approval chain |
| Transaction-level audit | Complete immutable audit record for every transaction processed through BeBanking |

*Audit and reporting capabilities confirmed against current product functionality (BQ10, 2026-06-10 — Hein Blignaut).*

---

**Remediation notes (2026-06-10):** Changes applied against BeBanking_CAPABILITY_MAP.md (§2, §5, §7).
- Automated Receipt Creation row removed from automation table — module retired per BQ7. Previous automation table had 6 processes; now 5.
- Bank statement import row updated: "via Connect Direct" replaced with "API or SFTP" per F-C-01 (BQ1).
- Exchange rate loading row updated: "sourced directly from bank" replaced with confirmed multi-provider statement: "FNB / Andisa / ExchangeRate-API (client choice)" per BQ12.
- Monitoring section: [UPDATE] placeholder replaced with confirmed monitoring and audit capabilities from BQ10.
- "Automated Receipt Creation and Application" section removed — entire section described a retired module; removed in its entirety.
- "Automated Bank Statement Management" section: "Connect Direct" removed; replaced with "API or SFTP."

**Original source review notes:** Monitoring and automation content from SITA BeBanking Proposal v1.06 (2017) — Section 4 (Automation Capabilities) and Appendix. Core automation concepts (bank statements, payment response matching, exchange rates, remittances) remain valid. Automated Receipt Creation was a legitimate module in 2017 — retired per BQ7. Connect Direct was the 2017 transmission channel — retired per BQ1. Exchange rate single-bank sourcing was 2017 practice — multi-provider model confirmed per BQ12. Monitoring and audit section authored from confirmed BQ8/BQ10 baseline.
