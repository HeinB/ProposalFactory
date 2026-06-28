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

# BeBanking — Host-to-Host Banking Core Capability

## What is Host-to-Host Banking?

Host-to-Host (H2H) banking establishes a direct, secure connection between an organisation's ERP system and the bank's processing infrastructure. This eliminates the manual intermediary steps of creating payment files, uploading them to internet banking portals, and manually reconciling the results.

With BeBanking H2H, the entire payment lifecycle — from invoice approval in the ERP through bank processing and confirmation — is automated, auditable, and controlled from within the ERP application.

## How BeBanking H2H Works

1. **Initiation** — Payments are created and approved within the ERP (Oracle EBS, Oracle Fusion Applications, or Acumatica) using existing financial workflows
2. **Configurable Approval Workflow** — Before any file is transmitted to the bank, the payment batch must be authorised through BeBanking's flexible approval framework: configurable number of levels, first-responder or voting-based authorisation, configurable segregation-of-duty controls
3. **File Generation** — Upon approval, BeBanking automatically generates the required payment file in the bank's prescribed format
4. **Transmission** — The file is transmitted directly to the bank via API integration (primary channel) or SFTP (for banks without API endpoints)
5. **Bank Response** — The bank processes the payment and returns a response file
6. **Reconciliation** — The response is automatically matched back to the original payment batch in the ERP, with accepted/rejected status per payment

## Supplier H2H Payments

- Integrates with the ERP Payments module (AP) — Oracle EBS, Oracle Fusion Applications, and Acumatica supported
- Once ERP processing is completed, the configured approval workflow is initiated
- Payments can be voided during the approval stage without rebuilding complete batches
- Payment file generated in bank-required format only upon full approval workflow completion
- Integrated with Supplier PDF Remittance delivery

## Payroll H2H Payments

- Integrates with the ERP Payroll module — Oracle EBS and Oracle Fusion Applications (see payroll scope note below)
- Configurable approval workflow with segregated approval responsibilities — payroll approvers are separate from AP approvers and cannot cross-approve
- A separate H2H profile is created for payroll to protect salary data from AP users
- ACB payroll file translated into bank-required format
- Summary cash management reconciliation enabled without exposing individual payroll detail

**Payroll scope note:** BeBanking Payroll H2H is supported from Oracle EBS and Oracle Fusion Applications payroll sources. Acumatica does not provide payroll functionality in the South African market.

## Security Architecture

- All approvals managed through ERP responsibilities — no external portal login required
- Approvers can authorise from any location, any device
- No payment is processed if linked to an unapproved bank account (integrated with Supplier Bank Account Approval and AVS)
- The full configured approval workflow cannot be bypassed — full audit trail maintained in ERP
- API-first integration — TLS-encrypted, server-to-server architecture; payment files never pass through internet banking portals

## Supported Banking Integrations

BeBanking is integrated with the following banks across South Africa, the CMA region, and internationally:

| Bank | Country |
|---|---|
| ABSA | South Africa |
| FNB (First National Bank) | South Africa |
| Nedbank | South Africa |
| Nedbank | Namibia |
| Standard Bank | South Africa |
| Standard Bank | Namibia |
| Investec | South Africa |
| Citi Bank | United Kingdom |
| Santander Bank | Chile |

---

**Remediation notes (2026-06-10):** Changes applied against BeBanking_CAPABILITY_MAP.md (§4, §5, §6).
- Step 2 (How H2H Works): "Two-Level Approval" replaced with configurable approval workflow — flexible framework, unlimited levels, first-responder or voting modes, configurable SOD (BQ2).
- Step 4 (How H2H Works): "Connect Direct or SFTP" replaced with "API integration (primary) or SFTP (for banks without API endpoints)" (BQ1).
- Step 1: Added Oracle Fusion Applications and Acumatica alongside Oracle EBS (BQ5, BQ6).
- Supplier H2H: Acumatica parity added; "two-level approval is initiated" → "configured approval workflow is initiated."
- Payroll H2H: PAY Approval Level 1 and Level 2 removed; replaced with flexible framework; payroll scope note added (Oracle EBS and Oracle Fusion only — Acumatica payroll exclusion per BQ5 clarification).
- Security Architecture: "Connect Direct and SSH certificates" removed; API-first / TLS description added (BQ1).
- "Two-level approval cannot be bypassed" replaced with framework-neutral language.
- Supported Banks: [UPDATE] placeholder removed and replaced with full confirmed 9-bank list (BQ4). Geographic framing added (CMA + international).

**Original source review notes:** Core H2H capability description synthesised from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement phases 3 and 4, and Appendix Product Module Summary. Architecture principles confirmed current; bank list, connectivity model, and approval framework updated to 2026 confirmed baseline.
