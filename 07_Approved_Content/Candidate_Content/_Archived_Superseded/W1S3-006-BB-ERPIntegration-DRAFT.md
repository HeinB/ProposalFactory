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

# BeBanking — ERP Integration

## Integration Philosophy

BeBanking is designed to extend and complement the ERP — not to replace it. All payment initiation, approval, and reconciliation processes take place within the ERP's native user interface and security model. BeBanking adds the bank connectivity and automation layer on top of existing ERP workflows.

## Oracle EBS Integration

BeBanking integrates natively with Oracle EBS R12 (and R11) across the following modules:

| ERP Module | BeBanking Integration Point |
|---|---|
| Accounts Payable (AP) | Supplier payment processing, approval workflow, remittance generation |
| Payroll (PAY) | Payroll payment processing, ACB file generation, approval workflow |
| Cash Management (CE) | Bank statement automation, reconciliation, connect direct connection |
| Accounts Receivable (AR) | Automated receipt creation and application from bank deposits |
| General Ledger (GL) | Exchange rate loading, cash management posting |

**Integration requirements for Oracle EBS:**
- AP, PAY, IBY (Payments), CE modules must be implemented and functioning
- Connect Direct or SFTP channel required between ERP application server and bank server
- SSH certificates required for automated server-to-server communication
- VPN access to client environment for implementation and ongoing support

## Acumatica Integration

BeBanking integrates with Acumatica's financial and banking modules.

**[UPDATE: Document the specific Acumatica module integration points — confirm with the BeBanking BU lead which Acumatica modules BeBanking integrates with, and what the Acumatica-specific workflow looks like. The SITA proposal only covers Oracle EBS.]**

## Technical Architecture (ERP-to-Bank)

```
ERP Application     BeBanking Layer     Banking Infrastructure
─────────────────   ─────────────────   ──────────────────────
AP/Payroll Module ─► File generation  ─► Connect Direct / SFTP ─► Bank H2H System
CE Module         ◄─ Response parsing ◄─ Bank response file     ◄─ Bank processing
AR Module         ◄─ Receipt creation ◄─ Bank statement file
```

The BeBanking layer sits between the ERP and the bank, handling format translation, approval orchestration, and file transfer — without requiring any changes to the ERP's core modules.

## Security Model

- All approvals managed through ERP responsibility assignments — no external portal
- Connect Direct and SSH certificates for encrypted file transmission
- Separate H2H profiles for supplier and payroll (data segregation)
- No payment file is generated without completing the full approval chain
- Full audit trail maintained within the ERP

---

**Review notes:** ERP integration details sourced from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement phases and Assumptions section. This is Oracle EBS-specific. MODERNISE rating applied: (1) Acumatica integration points must be documented separately, (2) confirm whether any new ERP platforms have been added since 2017, (3) the technical architecture diagram is a synthesis — verify the actual deployment model with the BeBanking technical team. The "IBY" (Oracle Internet Banking module) reference is Oracle-specific and should be removed or clarified when used in an Acumatica context.
