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

# BeBanking — Supplier Payments

## Supplier Bank Account Approval

Before any supplier payment can be processed through H2H, the supplier's bank account details must be verified and approved. BeBanking's Supplier Bank Account Approval module provides:

- **2-Level Approval Architecture** — supplier bank account changes require two separate approvers before the account is considered valid for payment
- **Parallel Processing** — supplier invoice and payment processing can continue while bank account approval runs in parallel
- **Individual and Bulk Approval** — approve single accounts or run bulk approval for efficiency
- **Payment Integration** — no payment will be processed if it is linked to a bank account that has not been fully approved
- **AVS Integration** — bank account approval triggers Automated Account Verification Services (AVS) check against the bank's database before approval is completed

## Integrated Account Verification Services (AVS)

Using master data directly from the ERP source ensures data quality. By enabling AVS host-to-host processing, actual data in the ERP is verified with no risk of manual mistakes.

- Batch processing reduces time spent on AVS
- Automated batch selection criteria ensure only relevant data is targeted for verification
- Verification confirms account number, account holder identity, and bank routing

## Supplier H2H Payments and Approval

- Integrates directly with the ERP Payments module (AP)
- Once ERP payment processing is completed, two-level approval is initiated before any payment file is generated
- Payment batches can be partially voided during approval without rebuilding the complete batch
- Payment file generated in bank-required format only upon full approval
- Approval responsibilities managed within the ERP — no external portal login required

## Supplier PDF Remittances

When H2H payments are enabled, supplier remittance advices can be tightly integrated:

- PDF remittances generated automatically upon payment processing
- Includes actual bank response data — whether payment was ACCEPTED or REJECTED, and rejection reason if applicable
- Automated bursting and emailing to supplier email addresses on record
- Replaces manual sending of proof-of-payments with best-practice automated processing

---

**Review notes:** Supplier payment capabilities sourced from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement Phase 2 (AVS + Account Approval), Phase 3 (Supplier H2H), and Appendix Product Module Summary. All SITA-specific references removed (Desmond Somthunzi, Standard Bank QA system references, SITA-specific assumptions). MODERNISE rating applied: bank-specific references updated to generic. Confirm whether the 2-level approval architecture is still the current BeBanking model — no changes expected but verify.
