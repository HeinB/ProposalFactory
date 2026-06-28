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

# BeBanking — Security

## Security Design Principles

BeBanking is designed with the following security principles as its foundation:

1. **Zero trust at the payment boundary** — no payment file reaches the bank without completing the full approval chain within the ERP
2. **Segregation of duties** — supplier and payroll approvers are separately defined and cannot cross-approve
3. **ERP-native access control** — all security is managed through ERP responsibility assignments, not external portals
4. **Encrypted transmission** — all bank communication via Connect Direct with SSH certificates
5. **Audit trail** — every approval, payment, and rejection is recorded within the ERP

## Access Control

- All BeBanking functions are accessed through ERP responsibility assignments
- Supplier approval responsibilities: AP Approval Level 1 and AP Approval Level 2
- Payroll approval responsibilities: PAY Approval Level 1 and PAY Approval Level 2
- Approvers cannot access bank system directly — they work only within the ERP
- Bank account attachment responsibilities are separate from approval responsibilities

## Supplier Bank Account Security

The Supplier Bank Account Approval module addresses supplier bank detail fraud risk:

- **Two-step approval** before any bank account is accepted for payment processing
- No payment will be processed against an unapproved bank account — enforced programmatically
- AVS (Account Verification Services) automatically validates bank account details against the bank's own records before approval is completed
- Bulk and individual approval modes support different operational environments

## Payment Approval Security

- Two independent approvers required before any payment file is generated
- Approvers can be based anywhere — mobile and remote approval supported
- Payment batches can be partially voided during approval without abandoning the full batch
- No payment reaches the bank without the full two-level approval cycle completing

## Transmission Security

- Dedicated banking server with Connect Direct connectivity **[UPDATE: confirm if Connect Direct still required or if SFTP is now the primary channel]**
- SSH certificates required for automated server communication
- Encrypted file transmission — bank files never pass through internet banking portals
- Server-to-server (host-to-host) architecture eliminates human handling of payment files during transmission

## Audit and Compliance

- Complete audit trail of all payment approvals maintained within the ERP
- Bank response data (accepted/rejected) returned and stored against payment records
- Rejection reasons captured for audit and resolution purposes
- Separation of duty for bank statement management (CE module) vs. payment initiation (AP/PAY)

---

**Review notes:** Security architecture sourced from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement (approval phases), Assumptions section, and Product Module Summary. MODERNISE rating applied: (1) confirm whether Connect Direct is still required or SFTP/API has replaced it; (2) confirm whether any MFA or additional security layers have been added since 2017; (3) POPIA compliance claims should be added if applicable to the banking data handled. The core approval architecture is unlikely to have changed but must be confirmed.
