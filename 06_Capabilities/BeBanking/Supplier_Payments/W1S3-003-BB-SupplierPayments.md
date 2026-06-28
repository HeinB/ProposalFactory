---
source_document: "APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
source_path: "Parties/Customers/SITA/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
extraction_date: "2026-06-08"
extracted_by: "Claude (AI extraction — requires human review)"
remediation_date: "2026-06-10"
remediated_by: "Claude (AI remediation — requires human review)"
readiness: "MODERNISE"
approved_for_reuse: "Yes"
business_unit: "BeBanking"
review_status: "Approved"
reviewer: "Hein Blignaut"
approved_date: "2026-06-10"
approved_by: "Hein Blignaut"
---

# BeBanking — Supplier Payments

## Supplier Bank Account Approval

Before any supplier payment can be processed through H2H, the supplier's bank account details must be verified and approved. BeBanking's Supplier Bank Account Approval module provides:

- **Flexible Approval Framework** — supplier bank account changes require approval through a configurable workflow before the account is considered valid for payment. The number of approval levels, approval mode (first-responder or voting-based), and segregation-of-duty controls are configured per client.
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
- Once ERP payment processing is completed, the configured approval workflow is initiated before any payment file is generated
- Payment batches can be partially voided during approval without rebuilding the complete batch
- Payment file generated in bank-required format only upon full approval workflow completion
- Approval responsibilities managed within the ERP — no external portal login required

## Supplier PDF Remittances

When H2H payments are enabled, supplier remittance advices can be tightly integrated:

- PDF remittances generated automatically upon payment processing
- Includes actual bank response data — whether payment was ACCEPTED or REJECTED, and rejection reason if applicable
- Automated bursting and emailing to supplier email addresses on record
- Replaces manual sending of proof-of-payments with best-practice automated processing

---

**Remediation notes (2026-06-10):** Changes applied against SESSION_C_FACT_BASELINE.md (F-C-04).
- Supplier Bank Account Approval: "2-Level Approval Architecture" removed. Replaced with "Flexible Approval Framework" description — unlimited levels, configurable first-responder or voting-based, configurable SOD.
- Supplier H2H Payments and Approval: "two-level approval is initiated" replaced with "configured approval workflow is initiated"; "full two-level approval" replaced with "full approval workflow completion."
- AVS section: confirmed active (BQ8) — no content changes required.
- All remaining content confirmed accurate against current product baseline.

**Original source review notes:** Supplier payment capabilities sourced from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement Phase 2 (AVS + Account Approval), Phase 3 (Supplier H2H), and Appendix Product Module Summary. All SITA-specific references removed. Approval model updated (2-level → flexible framework per BQ2). AVS confirmed active (BQ8).
