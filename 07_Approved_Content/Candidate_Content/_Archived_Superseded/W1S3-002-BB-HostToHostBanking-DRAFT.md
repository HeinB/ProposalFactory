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
> Items requiring update before use are marked **[UPDATE]**.

---

# BeBanking — Host-to-Host Banking Core Capability

## What is Host-to-Host Banking?

Host-to-Host (H2H) banking establishes a direct, secure connection between an organisation's ERP system and the bank's processing infrastructure. This eliminates the manual intermediary steps of creating payment files, uploading them to internet banking portals, and manually reconciling the results.

With BeBanking H2H, the entire payment lifecycle — from invoice approval in the ERP through bank processing and confirmation — is automated, auditable, and controlled from within the ERP application.

## How BeBanking H2H Works

1. **Initiation** — Payments are created and approved within the ERP (Oracle EBS or Acumatica) using existing financial workflows
2. **Two-Level Approval** — Before any file is transmitted to the bank, two independent approvers must authorise the payment batch from within the ERP
3. **File Generation** — Upon approval, BeBanking automatically generates the required payment file in the bank's prescribed format
4. **Transmission** — The file is transmitted directly to the bank via a secure Connect Direct or SFTP channel
5. **Bank Response** — The bank processes the payment and returns a response file
6. **Reconciliation** — The response is automatically matched back to the original payment batch in the ERP, with accepted/rejected status per payment

## Supplier H2H Payments

- Integrates with the ERP Payments module (AP)
- Once ERP processing is completed, two-level approval is initiated
- Payments can be voided during the approval stage without rebuilding complete batches
- Payment file generated in bank-required format only upon full approval
- Integrated with Supplier PDF Remittance delivery

## Payroll H2H Payments

- Integrates with the ERP Payroll module
- Two-level approval with segregated approval responsibilities (PAY Approval Level 1 and Level 2)
- A separate H2H profile is created for payroll to protect salary data from AP users
- ACB payroll file translated into bank-required format
- Summary cash management reconciliation enabled without exposing payroll detail

## Security Architecture

- All approvals managed through ERP responsibilities — no external portal login required
- Approvers can authorise from any location, any device
- No payment is processed if linked to an unapproved bank account (integrated with Supplier Bank Account Approval)
- Two-level approval cannot be bypassed — full audit trail maintained
- Connect Direct and SSH certificates ensure encrypted server-to-server communication

## Supported Banks

**[UPDATE: Confirm full list of certified BeBanking banking partners for 2026]**
- Standard Bank — confirmed integration (used in multiple implementations)
- **[UPDATE: List other banks now supported — Nedbank, ABSA, FNB, Capitec?]**

---

**Review notes:** Core H2H capability description synthesised from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement phases 3 and 4, and Appendix Product Module Summary. The 2017 source is Oracle EBS-specific. The principles (two-level approval, file generation, connect direct) are architecture-level and should be current. MODERNISE rating applied because: (1) bank partner list needs updating for 2026, (2) Acumatica integration not described in SITA doc, (3) any new capabilities added post-2017 are missing. Primary review action: confirm current bank partnerships and whether the two-level approval architecture still applies in the Acumatica integration.
