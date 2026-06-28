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

# BeBanking — Payroll Payments

## Overview

BeBanking's Payroll H2H module integrates directly with the ERP Payroll module to automate the processing and authorisation of payroll payments through a secure host-to-host connection with the organisation's bank.

Payroll payments are treated as a separate H2H profile from supplier payments, ensuring that payroll data remains protected and segregated from the AP function.

## How Payroll H2H Works

1. **Payroll Completion** — Once payroll processing is completed in the ERP (Oracle EBS Payroll module or equivalent), the payment batch is available for H2H approval
2. **Two-Level Approval** — Two independent approvers must authorise the payroll batch before any file is transmitted. Approver responsibilities are managed within the ERP application:
   - PAY Approval Level 1 (Initial Approvers)
   - PAY Approval Level 2 (Final Approvers)
3. **ACB File Translation** — Upon approval, BeBanking translates the ACB payroll file into the bank's required format
4. **Transmission** — Payroll file sent directly to the bank via secure channel
5. **Reconciliation** — Bank response reconciled back to ERP; summary cash management reconciliation completed

## Data Segregation and Security

- A **separate H2H profile** is created specifically for payroll to protect sensitive salary data
- Payroll approvers (PAY Level 1 and Level 2) are separate responsibility assignments from AP approvers
- Summary cash management reconciliation allows finance to confirm payroll bank entries without exposing individual salary details
- All approvals are managed within the ERP — approvers cannot see individual payroll data through the approval screen

## Benefits

- Eliminates manual payroll file creation, upload to internet banking, and manual reconciliation
- Reduces risk of payroll data exposure during the payment process
- Provides an auditable, two-level approval chain for every payroll run
- Approvers can authorise from any location and device — no VPN to internet banking portal required

---

**Review notes:** Payroll H2H capability sourced from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement Phase 4 and Appendix Product Module Summary. All SITA-specific references removed. The "ACB file" reference is specific to South African payroll format (Automated Clearing Bureau) — this is correct for SA. MODERNISE rating applied because: (1) Oracle EBS-specific — confirm Acumatica integration model, (2) payroll module naming may differ in Acumatica context, (3) confirm whether any changes to the two-level approval model have been made since 2017.
