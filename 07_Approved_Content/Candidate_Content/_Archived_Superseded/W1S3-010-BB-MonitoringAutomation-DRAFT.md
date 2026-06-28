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

# BeBanking — Monitoring and Automation

## Automated Banking Processes

BeBanking's core value proposition is the automation of high-volume, high-risk banking processes that would otherwise require manual intervention. The following processes can be fully automated once BeBanking is deployed and configured:

| Process | Automation Type | Manual Effort Eliminated |
|---|---|---|
| Bank statement import | Scheduled, automated via Connect Direct | Daily manual file download and upload |
| Exchange rate loading | Daily scheduled automation | Manual daily rate capture in ERP |
| Payment file transmission | Event-triggered (post-approval) | Manual file download, portal upload |
| Bank response processing | Automatic on file receipt from bank | Manual reconciliation of bank responses |
| Remittance advice delivery | Event-triggered (post-payment) | Manual sending of proof-of-payments |
| AR receipt creation | Event-triggered (on statement receipt) | Manual customer deposit identification and receipt creation |

## Scheduled and Event-Based Automation

BeBanking supports two automation modes:

**Scheduled Automation** — tasks run at predefined intervals:
- Bank statement imports — typically daily, automated end-to-end
- Exchange rate loads — daily, sourced directly from bank
- Database maintenance and file archiving within the banking server environment

**Event-Based Automation** — tasks triggered by ERP workflow events:
- Payment file generation triggered on approval completion
- Remittance advice generation triggered on payment file creation
- AR receipt creation triggered on bank statement import and customer match

## Automated Bank Statement Management

**Unbreakable Bank Statements** module provides:
- Fully automated bank statement import via Connect Direct
- Handling of non-standard bank statement numbering and transaction codes
- Single unique electronic bank statement per day — enables high-volume processing without errors from duplicate statement numbers
- Exception handling for out-of-spec bank formats, without requiring manual intervention for every occurrence

## Automated Receipt Creation and Application

For inbound cash management, BeBanking automates:
- Identification of customer or invoice numbers from bank deposit description text
- Auto-creation of AR receipts in Accounts Receivable
- Option to auto-apply identified receipts to oldest open invoices (FIFO) or to specific transactions
- Full reconciliation audit trail in Cash Management
- Unidentified deposits flagged for manual review rather than blocking the automated process

## Monitoring

**[UPDATE: Confirm whether BeBanking has active monitoring capabilities (alerts, dashboards, error notifications). The SITA 2017 proposal describes automation but does not describe a monitoring dashboard or alerting system. If monitoring capabilities exist beyond the standard ERP audit trail, document them here.]**

---

**Review notes:** Monitoring and automation content sourced from SITA BeBanking Proposal v1.06 (June 2017) — Appendix Product Module Summary sections on Unbreakable Bank Statements, Automated Exchange Rates, and Automated Receipt Creation. MODERNISE rating: (1) confirm whether a BeBanking monitoring dashboard or alerting system has been developed since 2017; (2) Acumatica's native Monitoring and Automation module (documented separately in W1S2-001) is a different product — cross-reference when presenting to Acumatica clients, (3) confirm whether the "Automated Exchange Rates" module sources rates from a bank feed or a third-party rate provider.
