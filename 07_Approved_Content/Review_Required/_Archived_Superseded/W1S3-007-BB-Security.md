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

# BeBanking — Security

## Security Design Principles

BeBanking is designed with the following security principles as its foundation:

1. **Zero trust at the payment boundary** — no payment file reaches the bank without completing the full approval chain within the ERP
2. **Segregation of duties** — supplier and payroll approvers are separately defined and cannot cross-approve
3. **ERP-native access control** — all security is managed through ERP responsibility assignments, not external portals
4. **Encrypted transmission** — all communication between BeBanking and banking institutions uses TLS encryption via API integration; SFTP over SSH is used for banks that do not expose API endpoints
5. **Audit trail** — every approval, payment, and rejection is recorded within the ERP

## Access Control

- All BeBanking functions are accessed through ERP responsibility assignments
- Supplier payment approval responsibilities are configured per client within the flexible approval framework — unlimited approval levels, configurable for first-responder or voting-based authorisation
- Payroll approval responsibilities are separate from supplier approval responsibilities and are configured independently within the framework
- Approvers cannot access the bank system directly — they work only within the ERP
- Bank account attachment responsibilities are separate from approval responsibilities
- Segregation-of-duty controls are configurable to meet each client's governance requirements

## Supplier Bank Account Security

The Supplier Bank Account Approval module addresses supplier bank detail fraud risk:

- **Configurable approval levels** before any bank account is accepted for payment processing
- No payment will be processed against an unapproved bank account — enforced programmatically
- AVS (Account Verification Services) automatically validates bank account details against the bank's own records before approval is completed
- Bulk and individual approval modes support different operational environments

## Payment Approval Security

- Configurable approval workflow required before any payment file is generated — number of approval levels and authorisation model set per client
- Approvers can be based anywhere — mobile and remote approval supported
- Payment batches can be partially voided during approval without abandoning the full batch
- No payment reaches the bank without the full configured approval workflow completing

## Transmission Security

- API-first connectivity — BeBanking communicates with banks via API integration as the primary channel
- SFTP over SSH — for banks that do not expose API endpoints, BeBanking provides an API layer that communicates with the bank using SFTP; no dedicated banking server is required on the client side
- TLS encryption for all data in transit — payment files never pass through internet banking portals
- Server-to-server (host-to-host) architecture eliminates human handling of payment files during transmission

## Audit and Compliance

- Complete audit trail of all payment approvals maintained within the ERP
- Bank response data (accepted/rejected) returned and stored against payment records
- Rejection reasons captured for audit and resolution purposes
- Separation of duty for bank statement management (Cash Management module) vs. payment initiation (AP/Payroll)

## Compliance

### POPIA

BeBanking is designed and operated in compliance with the Protection of Personal Information Act (POPIA). Banking data, payroll data, and supplier bank account information processed through BeBanking is handled in accordance with POPIA requirements for lawful processing, data minimisation, and security safeguards.

### GDPR

GDPR compliance is on the BeBanking product roadmap. Clients operating in jurisdictions with GDPR obligations should note this as future-state capability.

---

**Remediation notes (2026-06-10):** Changes applied against SESSION_C_FACT_BASELINE.md (F-C-03, F-C-04, F-C-11).
- Security principle #4: Connect Direct / SSH certificates → TLS encryption via API; SFTP over SSH as fallback.
- Access Control: AP Approval Level 1/2 and PAY Approval Level 1/2 removed. Replaced with flexible approval framework — unlimited levels, first-responder or voting modes, configurable SOD.
- Supplier Bank Account Security: "Two-step approval" replaced with "configurable approval levels" — the number of levels is not fixed.
- Payment Approval Security: "Two independent approvers" replaced with configurable workflow language.
- Transmission Security: Connect Direct dedicated banking server [UPDATE placeholder] replaced with API-first / SFTP-over-SSH description.
- Compliance section added: POPIA confirmed (BQ13); GDPR roadmap noted (BQ13).
- Source review notes retained for traceability.

**Original source review notes:** Security architecture sourced from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement (approval phases), Assumptions section, and Product Module Summary. The core approval architecture is confirmed current. Connectivity model updated (Connect Direct obsolete). POPIA added. GDPR positioned as roadmap.
