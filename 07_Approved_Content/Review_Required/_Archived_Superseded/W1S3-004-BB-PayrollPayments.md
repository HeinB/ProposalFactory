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

# BeBanking — Payroll Payments

## Overview

BeBanking's Payroll H2H module integrates directly with the ERP Payroll module to automate the processing and authorisation of payroll payments through a secure host-to-host connection with the organisation's bank.

Payroll payments are treated as a separate H2H profile from supplier payments, ensuring that payroll data remains protected and segregated from the AP function.

## How Payroll H2H Works

1. **Payroll Completion** — Once payroll processing is completed in the ERP, the payment batch is available for H2H approval. Supported ERP platforms for payroll H2H include Oracle EBS and Oracle Fusion Applications.
2. **Configurable Approval Workflow** — The payroll batch must be authorised through a configured approval workflow before any file is transmitted. Approval is managed within BeBanking's flexible approval framework:
   - Configurable number of approval levels per client
   - First-responder or voting-based authorisation mode
   - Segregation-of-duty controls to separate payroll approvers from AP approvers
3. **ACB File Translation** — Upon approval, BeBanking translates the ACB payroll file into the bank's required format
4. **Transmission** — Payroll file sent directly to the bank via secure channel (API or SFTP)
5. **Reconciliation** — Bank response reconciled back to ERP; summary cash management reconciliation completed

## Data Segregation and Security

- A **separate H2H profile** is created specifically for payroll to protect sensitive salary data
- Payroll approver responsibilities are separate from supplier (AP) approver responsibilities and are configured independently within the flexible approval framework
- Summary cash management reconciliation allows finance to confirm payroll bank entries without exposing individual salary details
- All approvals are managed within the ERP — approvers cannot see individual payroll data through the approval screen

## Benefits

- Eliminates manual payroll file creation, upload to internet banking, and manual reconciliation
- Reduces risk of payroll data exposure during the payment process
- Provides an auditable, configurable approval chain for every payroll run
- Approvers can authorise from any location and device — no VPN to internet banking portal required

---

**Remediation notes (2026-06-10):** Changes applied against SESSION_C_FACT_BASELINE.md (F-C-03, F-C-04).
- Overview: ERP platform scope corrected — Oracle EBS and Oracle Fusion Applications only. Acumatica does not provide payroll functionality in South Africa. Paragraph incorrectly introducing Acumatica removed (corrected 2026-06-10).
- How Payroll H2H Works Step 1: "Oracle EBS Payroll module or equivalent" → explicit list of supported payroll ERP platforms (Oracle EBS, Oracle Fusion Applications only).
- How Payroll H2H Works Step 2: "Two-Level Approval" with PAY Approval Level 1 / PAY Approval Level 2 replaced with flexible approval framework description — configurable levels, first-responder or voting modes, SOD controls.
- Step 4 Transmission: Added "(API or SFTP)" per F-C-03.
- Data Segregation: "PAY Level 1 and Level 2" references removed; replaced with flexible framework language.
- Benefits: "two-level approval chain" replaced with "configurable approval chain."
- ACB file reference retained — correct for South African payroll format (Automated Clearing Bureau). Applies to Oracle EBS and Oracle Fusion payroll implementations only.

**Original source review notes:** Payroll H2H capability sourced from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement Phase 4 and Appendix Product Module Summary. All SITA-specific references removed. Approval model updated (PAY Level 1/2 → flexible framework per BQ2). Acumatica payroll references removed — Acumatica does not provide payroll functionality in South Africa (BQ5 clarification). ACB format confirmed appropriate for SA context.
