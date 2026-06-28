# BeBanking — Authoritative Capability Map
**Version:** 1.0
**Established:** 2026-06-10
**Maintained by:** APPSolve BeBanking Business Unit
**Prepared by:** Claude (AI — requires BU lead review and confirmation)
**Authority:** BU lead responses BQ1–BQ13 (confirmed 2026-06-10); source: SITA BeBanking Proposal v1.06 (2017); website validation (bebanking.appsolve.co.za, appsolve.co.za)
**Status:** Reference document — authoritative baseline for tender content, extraction, remediation, website validation, and AI retrieval

---

## 1. Product Overview

### What is BeBanking?

BeBanking (Business Efficient Banking) is APPSolve's proprietary Host-to-Host (H2H) banking integration product. It connects ERP systems directly to banks, automating the full payment lifecycle — from payment initiation inside the ERP through approval, bank transmission, and reconciliation — without requiring manual intervention or internet banking portals.

BeBanking is a middleware product: it does not replace the ERP or the bank's systems, but provides the automation layer between them.

### Target Customers

| Customer type | Description |
|---|---|
| ERP-connected organisations | Businesses running Oracle EBS, Oracle Fusion Applications, Acumatica, or SAP that process significant payment volumes through accounts payable, payroll, or treasury |
| Multi-bank organisations | Organisations banking with more than one institution, requiring a single integrated payment and statement platform |
| High-governance environments | Public sector, financial services, and listed companies requiring auditable, segregated payment approval workflows |
| CMA-region and international businesses | South Africa, Namibia, Lesotho, Eswatini; international presence through UK and Chile bank integrations |

### Primary Business Problems Solved

| Problem | BeBanking solution |
|---|---|
| Manual bank statement upload and reconciliation | Unbreakable Bank Statements — automated import and ERP reconciliation |
| Unverified supplier banking details | AVS + Supplier Bank Account Approval — automated verification and configurable approval |
| Manual payment file generation and portal upload | Supplier H2H Payments — automated file generation and direct bank transmission |
| Manual payroll submission to bank | Payroll H2H Payments — automated payroll file transmission with segregated approvals |
| Manual remittance advice sending | Supplier PDF Remittances — automated PDF generation and email delivery |
| Manual daily exchange rate capture | Automated Exchange Rates — daily rate loading from confirmed providers |
| No proof-of-payment document retrieval (ABSA clients) | ABSA Proof of Payment Integration — automated retrieval and archiving |
| No international payment automation | International and Forex Payment Processing — SWIFT and forex payment processing |

### Supported Deployment Models

| Model | Status | Notes |
|---|---|---|
| On-premises ERP | Supported | Oracle EBS on-premises; traditional deployment |
| Cloud ERP | Supported | Oracle Fusion Applications; Acumatica (cloud-native); BeBanking supports both |
| Hybrid ERP | Supported | Mixed on-premises and cloud ERP estate in the same organisation |

---

## 2. Current Module Portfolio

### Active Modules — Confirmed June 2026

| # | Module | Description | Notes |
|---|---|---|---|
| 1 | Unbreakable Bank Statements | Automated daily bank statement import and ERP reconciliation. Handles non-standard bank statement numbering and transaction codes. | All supported banks |
| 2 | Integrated Account Verification Services (AVS) | Real-time verification of supplier bank account details against the bank's own records before any account is approved for payment. | All supported banks |
| 3 | Supplier Bank Account Approval | Configurable approval workflow for supplier banking detail changes before the account is valid for payment. Configurable levels, modes (first-responder or voting), and SOD controls. | All supported banks |
| 4 | Supplier H2H Payments and Approval | Full supplier payment lifecycle: ERP initiation → configurable approval workflow → bank-format file generation → API or SFTP transmission → bank response reconciliation. | All supported banks |
| 5 | Payroll H2H Payments and Approval | Payroll payment lifecycle with segregated approvals and separate H2H profile from supplier payments. Protects salary data from AP users. Oracle EBS and Oracle Fusion Applications payroll sources only — see payroll scope note. | Oracle EBS, Oracle Fusion only (see §3) |
| 6 | Automated Exchange Rates | Daily automated loading of foreign exchange rates into the ERP from a client-selected rate provider. | Rate sources: FNB, Andisa, ExchangeRate-API |
| 7 | Supplier PDF Remittances | Automated PDF remittance advice generation and email delivery on payment processing. Includes actual bank response (ACCEPTED/REJECTED). | All supported banks |
| 8 | ABSA Proof of Payment Integration | Automated retrieval and archiving of ABSA proof-of-payment documents. | **ABSA clients only** |
| 9 | International and Forex Payment Processing | SWIFT and foreign currency payment processing. International bank integrations (Citi Bank UK, Santander Chile). Exchange rate management from multiple sources. | Full forex capability confirmed — see §7 |

**Note on module 9:** The candidate file W1S3-005 for this module is in the authoring phase. Content is confirmed from BQ7 and BQ11 but the file has not yet been promoted to Review_Required.

### Discontinued Modules

| Module | Status | Reason | Replacement |
|---|---|---|---|
| Secure File Transfer | **Retired** | API-first architecture provides secure transmission natively. No dedicated file transfer component required. | API layer (see §5) |
| Automated Receipt Creation | **Retired** | Module discontinued. AR receipt creation from bank deposits no longer part of BeBanking's core offering. | No direct replacement |

**Important:** Do not cite Secure File Transfer or Automated Receipt Creation in tender content or product descriptions. These modules no longer exist.

---

## 3. ERP Compatibility Matrix

### Oracle E-Business Suite (Oracle EBS)

| Item | Detail |
|---|---|
| Status | **Supported** |
| Versions | R11, R12 |
| Deployment | On-premises |

**Supported ERP modules:**

| Oracle EBS Module | BeBanking Integration |
|---|---|
| Accounts Payable (AP) | Supplier payment processing, approval workflow, remittance generation |
| Payroll (PAY) | Payroll payment processing, ACB file generation, approval workflow |
| Cash Management (CE) | Bank statement import, reconciliation, bank response processing |
| General Ledger (GL) | Exchange rate loading, cash management posting |

**Notes:** Deep, native integration across all modules listed. Oracle EBS is the original and most mature BeBanking integration platform.

### Oracle Fusion Applications

| Item | Detail |
|---|---|
| Status | **Supported** |
| Deployment | Cloud (Oracle Cloud ERP) |

**Notes:** Oracle Fusion is confirmed. IBY (Internet Banking module) is Oracle EBS-specific and does not apply to Oracle Fusion. Fusion integration does not use the IBY module — do not reference IBY when describing Fusion integration.

### Acumatica

| Item | Detail |
|---|---|
| Status | **Supported** |
| Supported modules | Acumatica Payments; Acumatica Cash Management |
| Deployment | Cloud (Acumatica SaaS) |

**Confirmed Acumatica capabilities through BeBanking:**
- Local payments
- Forex payments
- Bank statement processing

**⚑ PAYROLL EXCLUSION — PERMANENT RULE:**
Acumatica does **not** provide payroll functionality in the South African market. BeBanking Payroll H2H (module 5) is supported from Oracle EBS and Oracle Fusion Applications payroll sources only. Do not imply Acumatica payroll integration, payroll payment generation, or payroll workflows in any BeBanking content. This applies regardless of whether an Acumatica ERP integration is described elsewhere in the same document.

### SAP

| Item | Detail |
|---|---|
| Status | **Supported — confirmed by BU lead 2026-06-10** |
| Architecture detail | Pending BQ-WEB-04 |
| Deployment | On-premises and cloud |

**Notes:** SAP integration is confirmed as a current BeBanking capability. This is a product evolution post-2017 — the 2017 SITA proposal did not reference SAP, and Session A correctly removed the claim based on zero corpus evidence at the time. Full integration architecture and supported SAP module detail is pending BQ-WEB-04 response. Until then, use: "BeBanking is compatible with SAP" without specifying module-level detail.

**Important note on W1S1-005:** The approved Session A file W1S1-005 does not mention SAP — this was correct at the time (no corpus evidence in 2017 source). W1S1-005 is not reopened. SAP compatibility appears in Session C content only (W1S3-001, W1S3-006).

### Sage

| Item | Detail |
|---|---|
| Status | **Pending confirmation — BQ-WEB-03** |

**Notes:** Sage integration was referenced on the BeBanking website. BQ-WEB-03 has been raised with the BU lead to confirm scope and supported modules. Until BQ-WEB-03 is answered, do not cite Sage integration in tender content. Use "additional ERP platforms on request" if needed.

---

## 4. Banking Integration Matrix

BeBanking is **integrated with** the following banks. Do not use the term "bank certified" — there is no formal bank certification programme.

| Bank | Country | Integration Status | Notes |
|---|---|---|---|
| ABSA | South Africa | Integrated | All standard BeBanking modules + ABSA Proof of Payment Integration (ABSA-specific) |
| FNB (First National Bank) | South Africa | Integrated | Also a supported exchange rate provider |
| Nedbank | South Africa | Integrated | — |
| Nedbank | Namibia | Integrated | Confirms CMA regional deployment |
| Standard Bank | South Africa | Integrated | — |
| Standard Bank | Namibia | Integrated | Confirms CMA regional deployment |
| Investec | South Africa | Integrated | — |
| Citi Bank | United Kingdom | Integrated | Confirms international deployment capability |
| Santander Bank | Chile | Integrated | Confirms international deployment capability |

**Geographic scope derived from bank integrations:** South Africa, Namibia (CMA), United Kingdom, Chile. Full CMA deployment confirmed: South Africa, Namibia, Lesotho, Eswatini.

**Wording guidance:** Use "BeBanking is integrated with [bank name]" — do not use "certified by," "approved by," or "licensed by" in relation to banks.

---

## 5. Connectivity Architecture

### Current Architecture (as at 2026)

| Component | Description |
|---|---|
| **API-first** | APIs are the primary method of communication between BeBanking and banking institutions. This is the preferred channel. |
| **SFTP over SSH** | For banks that do not expose API endpoints, BeBanking provides an API layer that communicates with the bank via SFTP. The client does not need to manage SFTP connections — BeBanking handles the translation. |
| **TLS encryption** | All data in transit is encrypted using TLS. Payment files never pass through internet banking portals. |
| **Server-to-server** | Host-to-host architecture — payment files are transmitted directly between BeBanking and the bank's processing systems without human handling. |

### Historical Architecture (retired — do not cite)

| Component | Status | Note |
|---|---|---|
| Connect Direct | **Retired** | Connect Direct is no longer used. No references to Connect Direct should appear in current product descriptions, tender content, or capability statements. |
| Dedicated Banking Server | **No longer required** | The API-first model does not require a separate dedicated banking server on the client side. |
| Secure File Transfer utility | **Retired** (module retired) | The Secure File Transfer module is discontinued. Secure transmission is now inherent in the API layer. |

**Key message for tender responses:** BeBanking uses a modern, API-first integration architecture. This eliminates the need for dedicated banking server hardware and Connect Direct licensing on the client side, reducing infrastructure complexity while improving security.

---

## 6. Approval Framework

### Current Model: Flexible Approval Framework

BeBanking's approval framework is fully configurable per client. There are no fixed approval levels — the framework supports any combination of the following:

| Capability | Description |
|---|---|
| **Unlimited approval levels** | No limit on the number of approval levels configured per client. 2 levels, 5 levels, 10 levels — all supported. |
| **First-responder mode** | Any qualified approver in a level can complete the approval. First approver to act proceeds the workflow. |
| **Voting mode** | All (or a quorum of) approvers in a level must authorise before the workflow proceeds. |
| **Configurable SOD** | Segregation-of-duty controls are configurable — supplier (AP) approvers, payroll approvers, bank account maintenance approvers, and treasury approvers can all be separately defined and mutually exclusive. |
| **ERP-native** | All approvals are managed through ERP responsibility assignments. No external portal login is required. |
| **Location-independent** | Approvers can authorise from any location and any device. No VPN to internet banking is required. |

### Historical Model (obsolete — do not cite)

The following approval model described in SITA BeBanking Proposal v1.06 (2017) is obsolete and must not appear in current tender content:

| Legacy term | Current status |
|---|---|
| AP Approval Level 1 | Obsolete — historical example, not a product constraint |
| AP Approval Level 2 | Obsolete — historical example, not a product constraint |
| PAY Approval Level 1 | Obsolete — historical example, not a product constraint |
| PAY Approval Level 2 | Obsolete — historical example, not a product constraint |

**Context:** The legacy two-level model was an implementation example from the 2017 SITA proposal. The current product supports unlimited levels. The "Level 1 / Level 2" terminology described a specific client configuration, not a product limitation.

---

## 7. International Capability

### Geographic Scope

| Region | Countries | Basis |
|---|---|---|
| Common Monetary Area (CMA) | South Africa, Namibia, Lesotho, Eswatini | Confirmed BU lead 2026-06-10 |
| International — banking integrations | United Kingdom (Citi Bank), Chile (Santander Bank) | Confirmed BQ4 2026-06-10 |

**Positioning guidance:** BeBanking is not a South Africa-only product. Frame as "banking automation for ERP-connected organisations across South Africa, the CMA region, and internationally."

### SWIFT and Forex Payment Processing

| Capability | Status | Notes |
|---|---|---|
| International payments (SWIFT outward) | Confirmed — full capability | Via module: International and Forex Payment Processing |
| Foreign currency payments | Confirmed | SWIFT processing; cross-border payment lifecycle |
| CMA-region payments | Confirmed | All CMA bank integrations supported |
| Forex exchange rate management | Confirmed | Automated rate loading via module 6 (Automated Exchange Rates) |

**Note on module distinction:** "Automated Exchange Rates" (module 6) and "International and Forex Payment Processing" (module 9) are distinct capabilities:
- **Automated Exchange Rates** — loads foreign exchange rates from a provider into the ERP. This is ERP data management, not payment initiation.
- **International and Forex Payment Processing** — initiates, approves, and transmits SWIFT and foreign currency payments to banks. This is payment execution.

### Exchange Rate Providers

BeBanking supports multiple exchange rate sources. The client selects their preferred provider(s):

| Provider | Notes |
|---|---|
| FNB (First National Bank) | Also a BeBanking-integrated bank — dual role as rate provider and banking partner |
| Andisa | Third-party rate provider |
| ExchangeRate-API | Third-party rate API |

**Wording guidance:** Do not imply a single mandatory rate provider. Use: "BeBanking supports multiple exchange rate sources including FNB, Andisa, and ExchangeRate-API — clients select their preferred provider."

---

## 8. Compliance and Security

### POPIA Compliance

**Status: Confirmed**

BeBanking is designed and operated in compliance with the Protection of Personal Information Act (POPIA). Banking data, payroll data, and supplier bank account information processed through BeBanking is handled in accordance with POPIA requirements for lawful processing, data minimisation, and security safeguards.

**Tender use:** This claim can be stated directly in South African government and financial sector tenders.

### GDPR

**Status: Roadmap / future-state**

GDPR compliance is on the BeBanking product roadmap. Must be positioned as future-state only — do not represent as a current capability.

**Approved wording:** "GDPR compliance is on the BeBanking product roadmap."

### Audit Trail and Reporting

BeBanking maintains complete audit trails across all banking operations:

| Audit capability | Description |
|---|---|
| Payment approval reporting | Full approval status and workflow visibility for all payment batches |
| Transaction-level audit reporting | Complete history of every transaction processed through BeBanking |
| Bank account maintenance approval reporting | Audit trail for all supplier banking detail changes and approval decisions |
| Operational monitoring and audit visibility | Operational oversight across all banking workflows |

### Security Principles

| Principle | Implementation |
|---|---|
| Zero trust at payment boundary | No payment file reaches the bank without completing the full configured approval chain |
| Segregation of duties | Supplier approvers, payroll approvers, and bank account approvers are separately defined and mutually exclusive |
| ERP-native access control | All security managed through ERP responsibility assignments — no external portal |
| Encrypted transmission | TLS encryption for all data in transit; API channel; SFTP over SSH as fallback |
| No human handling of payment files | Server-to-server architecture eliminates manual file handling during transmission |

---

## 9. Commercial Model

### Current Model (confirmed BQ9 — 2026-06-10)

| Option | Structure |
|---|---|
| Monthly subscription | Per module, per month — OPEX model |
| Annual subscription | Per module, per year — OPEX model |

**No once-off licence model.** There is no Software Option, no once-off implementation ownership, and no perpetual licence. All commercial engagements are subscription-based.

### Historical Model (obsolete — do not cite)

| Legacy option | Status |
|---|---|
| Service Option (once-off install + monthly fee) | **Obsolete** |
| Software Option (once-off licence + annual support) | **Obsolete** |

---

## 10. Source References

| Section | Source document(s) | Website confirmation | BU lead confirmation |
|---|---|---|---|
| Product overview | SITA BeBanking Proposal v1.06 (2017); HyDac V5.1 Template BeBanking (Dec 2024) | bebanking.appsolve.co.za, appsolve.co.za | BQ1–BQ13 confirmed 2026-06-10 |
| Module portfolio (current) | HyDac V5.1 (Dec 2024) for original list | bebanking.appsolve.co.za/modules | BQ7 confirmed 2026-06-10 |
| Module portfolio (retired) | — | Not on website | BQ7 confirmed retired 2026-06-10 |
| Oracle EBS compatibility | SITA v1.06 (2017) — primary source | appsolve.co.za | BQ6 confirmed |
| Oracle Fusion compatibility | Not in 2017 source | appsolve.co.za/bebanking | BQ6 confirmed 2026-06-10 |
| Acumatica compatibility (scope) | Not in 2017 source | appsolve.co.za/bebanking | BQ5 confirmed 2026-06-10 |
| Acumatica payroll exclusion | — | Not claimed on website | BQ5 clarification confirmed 2026-06-10 |
| SAP compatibility | Not in 2017 source (zero corpus evidence) | bebanking.appsolve.co.za | BU lead confirmed 2026-06-10 |
| Sage compatibility | Not in 2017 source | bebanking.appsolve.co.za (website reference) | **Pending BQ-WEB-03** |
| Banking integration list (9 banks) | SITA v1.06 partial (Standard Bank only); websites list more | bebanking.appsolve.co.za/banks | BQ4 confirmed 9 banks 2026-06-10 |
| Connectivity architecture (API/SFTP) | Not in 2017 source | Not explicitly stated | BQ1 confirmed 2026-06-10 |
| Connect Direct retirement | — | — | BQ1 confirmed retired 2026-06-10 |
| Approval framework (flexible) | SITA v1.06 (2-level example only) | — | BQ2 confirmed 2026-06-10 |
| Forex / international | SITA v1.06 partial | bebanking.appsolve.co.za | BQ7 (module confirmed), BQ11 (capability confirmed) 2026-06-10 |
| CMA geographic scope | — | Not explicitly stated | BQ7 confirmed 2026-06-10 |
| Exchange rate providers | Not in 2017 source | — | BQ12 confirmed 2026-06-10 |
| POPIA compliance | Not in 2017 source | — | BQ13 confirmed 2026-06-10 |
| GDPR (roadmap only) | — | — | BQ13 confirmed roadmap 2026-06-10 |
| Commercial model (subscription) | SITA v1.06 (Service/Software Options) | — | BQ9 confirmed subscription-only 2026-06-10 |
| Monitoring and audit capabilities | SITA v1.06 partial | — | BQ10 confirmed 2026-06-10 |

---

## Appendix — Quick Reference: What to Say / What Not to Say

| Topic | Correct wording | Do not say |
|---|---|---|
| Bank relationships | "BeBanking is integrated with [bank name]" | "certified by," "approved by," "licensed by" |
| Connectivity | "API-first integration; SFTP fallback for banks without API endpoints" | "Connect Direct" (retired) |
| Approval levels | "configurable approval workflow with unlimited levels" | "AP Level 1/Level 2" or "PAY Level 1/Level 2" as product constraints |
| Acumatica payroll | Do not mention | "Acumatica payroll," "payroll from Acumatica" |
| Forex module name | "International and Forex Payment Processing" | "forex module," "FX module" (use the confirmed module name) |
| Exchange rates | "clients select from supported rate providers including FNB, Andisa, and ExchangeRate-API" | Single mandatory provider; "the bank" as the only source |
| Geographic scope | "South Africa, the CMA region, and internationally" | "South African banking solution" (too limiting) |
| SAP (until BQ-WEB-04) | "BeBanking is compatible with SAP" | Specific SAP module detail |
| Sage (until BQ-WEB-03) | "additional ERP platforms on request" | "Sage integration" |
| GDPR | "GDPR compliance is on the BeBanking product roadmap" | "GDPR compliant" (not current) |
| Licensing | "monthly or annual subscription" | "once-off licence," "Service Option," "Software Option" |

---

*This capability map is the authoritative reference for BeBanking product content. All Session C candidates (W1S3-001 through W1S3-010) are being remediated against this map. For the full Session C governance trail, see SESSION_C_FACT_BASELINE.md, SESSION_C_IMPACT_ANALYSIS.md, and SESSION_C_APPROVAL_PLAN.md.*
