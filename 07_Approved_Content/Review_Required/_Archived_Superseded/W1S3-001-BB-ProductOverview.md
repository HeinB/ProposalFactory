---
source_document: "APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx"
source_path: "Parties/Customers/HyDac/RFP/Acumatica Implementation/1. Working/APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx"
extraction_date: "2026-06-08"
extracted_by: "Claude (AI extraction — requires human review)"
remediation_date: "2026-06-10"
remediated_by: "Claude (AI remediation — requires human review)"
readiness: "DIRECT"
approved_for_reuse: "No"
business_unit: "BeBanking"
review_status: "Review_Required"
reviewer: "Hein Blignaut"
---

> **REVIEW REQUIRED — NOT APPROVED FOR TENDER USE**
> Readiness: DIRECT | Promoted to Review_Required: 2026-06-10 | Reviewer: Hein Blignaut

---

# BeBanking — Product Overview

## What is BeBanking?

APPSolve's **BeBanking** (Business Efficient Banking) enables organisations to access the most secure and efficient banking processes seamlessly from their ERP (Enterprise Resource Planning) applications.

BeBanking enables H2H (Host to Host) technology that automates and controls sensitive banking processes. This enables organisations to have complete end-to-end visibility of the payment process and process large volumes of data effortlessly.

Your business will be able to control access to information, avoid manual checks, and transact securely and with confidence. Approvers can at any time, from any location and any device, authorise payments originating directly from your ERP.

BeBanking is deployed across South Africa, the Common Monetary Area (Namibia, Lesotho, Eswatini), and internationally — with banking integrations in the United Kingdom and Chile.

## The Problem BeBanking Solves

Many organisations operate with manually segregated banking processes that create significant risk:

- Manual bank statement uploads or capturing
- Manual statement reconciliation for payments initiated from ERP
- Unverified supplier banking details creating fraud risk
- No automated audit trail for payment approvals
- Manual reconciliation of payroll against bank responses

BeBanking resolves these issues by automating the full payment lifecycle — from initiation in the ERP through bank processing and back.

## Product Module Portfolio

BeBanking is a suite of banking automation modules that can be implemented in phases:

| Module | Purpose |
|---|---|
| Unbreakable Bank Statements | Automated bank statement import and reconciliation |
| Integrated Account Verification Services (AVS) | Real-time verification of supplier bank account details against the bank's own records |
| Supplier Bank Account Approval | Configurable approval workflow for supplier banking detail changes before the account is valid for payment |
| Supplier H2H Payments and Approval | Host-to-host supplier payment processing with configurable approval workflow |
| Payroll H2H Payments and Approval | Host-to-host payroll payment processing with segregated approvals |
| Automated Exchange Rates | Daily automated loading of foreign exchange rates from client-selected provider |
| Supplier PDF Remittances | Automated remittance advice generation and email delivery |
| ABSA Proof of Payment Integration | Automated retrieval and archiving of ABSA proof-of-payment documents (ABSA clients) |
| International and Forex Payment Processing | SWIFT and foreign currency payment processing with multi-source exchange rate management |

## ERP Compatibility

BeBanking integrates with:
- **Oracle EBS** (R11, R12) — deep integration with AP, Payroll, Cash Management (CE), and GL modules
- **Oracle Fusion Applications** — Oracle Cloud ERP; both on-premises and cloud deployment supported
- **Acumatica** — Acumatica Payments and Acumatica Cash Management modules; local payments, forex payments, and bank statement processing
- **SAP** — confirmed integration

**Note on Acumatica payroll:** Acumatica does not provide payroll functionality in the South African market. BeBanking Payroll H2H is supported from Oracle EBS and Oracle Fusion Applications payroll sources only.

---

**Remediation notes (2026-06-10):** Changes applied against BeBanking_CAPABILITY_MAP.md (§2, §3).
- Module table: Removed Secure File Transfer (retired per BQ7); Removed Automated Receipt Creation (retired per BQ7); Added ABSA Proof of Payment Integration (new module per BQ7); Added International and Forex Payment Processing (new module per BQ7, confirmed by BQ11).
- Module description update: "Supplier Bank Account Approval" — "2-level approval workflow" replaced with "configurable approval workflow" per F-C-04.
- ERP Compatibility: Added Oracle Fusion Applications (BQ6); Added SAP (BU lead confirmed); updated Acumatica description with confirmed scope (BQ5); added payroll exclusion note.
- Geographic framing: Added CMA and international context to intro.

**Original source review notes:** Product overview synthesised from the BeBanking H2H section of HyDac V5.1 Template BeBanking (December 2024) and SITA BeBanking Proposal v1.06 (June 2017). December 2024 source is the most current available. Module composition now confirmed by BU lead (BQ7). ERP compatibility confirmed by BU lead (BQ5, BQ6, BU confirmation of SAP).
