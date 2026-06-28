---
source_document: "Session C Confirmed Fact Baseline — BU lead responses BQ7 (module confirmed), BQ11 (international and forex capability confirmed), BQ12 (exchange rate providers confirmed) — 2026-06-10. Partial extraction: APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx (Automated Exchange Rates module description only)."
source_path: "00_Governance/SESSION_C_FACT_BASELINE.md; Parties/Customers/SITA/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
authoring_basis: "AUTHOR from confirmed Session C fact baseline. NOT a direct extraction. Parliament FX Rates document recorded as future enhancement source only — does not block promotion."
extraction_date: "2026-06-10"
extracted_by: "Claude (AI authoring from confirmed Session C fact baseline — requires human review)"
remediation_date: "2026-06-10"
remediated_by: "Claude (AI — Session W1S3-005 review resolution)"
readiness: "MODERNISE"
approved_for_reuse: "No"
business_unit: "BeBanking"
review_status: "Review_Required"
reviewer: "Hein Blignaut (pending)"
---

> **REVIEW REQUIRED — Pending BU lead approval. Not approved for tender use.**
> Readiness: MODERNISE | Reviewer: Hein Blignaut

---

# BeBanking — International and Forex Payment Processing

## Overview

BeBanking International and Forex Payment Processing is BeBanking's module for cross-border and foreign currency payment automation. It extends the same Host-to-Host (H2H) architecture that governs domestic supplier and payroll payments to international payments — automating the full lifecycle from ERP initiation through configurable approval to transmission to integrated banking partners, without internet banking portals or manual file handling.

**This module is distinct from the Automated Exchange Rates module (module 6).** The Automated Exchange Rates module manages the daily loading of foreign exchange rates into the ERP — it is a rate data management capability. International and Forex Payment Processing (module 9) handles payment initiation, approval, and transmission of payment instructions to integrated banking partners. Both capabilities work together in a complete foreign currency payment workflow.

BeBanking's international payment capability covers the Common Monetary Area (South Africa, Namibia, Lesotho, Eswatini) and extends internationally through bank integrations in the United Kingdom and Chile.

---

## Business Problem

Organisations conducting cross-border business face operational challenges when managing international payments through conventional means:

- Payment initiation through internet banking portals bypasses ERP-native approval controls and creates segregation-of-duty gaps
- No consistent audit trail for forex payment authorisations when using internet banking channels
- Separate processes for domestic and international payments increase operational risk and training requirements
- Manual daily exchange rate capture delays ERP data currency and introduces keying errors
- Cross-border payments across multiple regions require multiple bank portals without an integrated solution
- AP teams manually handle payment files, creating security exposure and audit gaps

---

## International and Forex Payments Capability

The International and Forex Payment Processing module provides end-to-end cross-border payment automation:

| Capability | Description |
|---|---|
| Cross-border payment initiation | International payments initiated from within the ERP in the same workflow used for domestic payments — no separate process or portal |
| International payment processing | Payment instructions transmitted to integrated banking partners, who execute cross-border payments (including SWIFT transactions) through their own banking infrastructure |
| Configurable approval workflow | All forex payments subject to BeBanking's flexible approval framework before transmission: unlimited configurable levels, first-responder or voting-based authorisation, configurable segregation-of-duty controls |
| Bank-format file generation | Payment file generated in the format required by the receiving banking partner, automatically upon full approval completion |
| API-first transmission | Payment instructions transmitted to banking partners via API integration; SFTP over SSH used for banking partners without API endpoints |
| Bank response processing | Bank acceptance and rejection responses received and reconciled back to the originating payment batch in the ERP |
| Complete audit trail | Full record of all payment approvals, file generation, and transmission events maintained in the ERP |

---

## SWIFT and Cross-Border Payments

BeBanking transmits international payment instructions to integrated banking partners. Banking partners execute SWIFT and cross-border transactions through their own banking infrastructure. The payment lifecycle follows the same server-to-server architecture as domestic payments:

1. **Initiation** — International payment created within the ERP (Oracle EBS, Oracle Fusion Applications, or Acumatica) through the normal payments workflow
2. **Approval** — Payment batch submitted to BeBanking's configurable approval framework; no payment file is generated until the full configured approval chain is complete
3. **File generation** — BeBanking generates the payment file in the format required by the receiving banking partner, upon approval completion
4. **Transmission** — Payment instruction transmitted to the banking partner via API (primary channel) or SFTP (fallback channel); no internet banking portal access required
5. **Bank processing** — Banking partner processes the payment instruction through their own banking infrastructure and returns a response file
6. **Reconciliation** — Bank response matched back to the ERP; payment status (accepted or rejected) updated against the originating batch

Organisations can configure their approval framework to apply additional approval levels or higher approval thresholds for international or above-limit payments, to meet their international payment governance requirements.

---

## Common Monetary Area Support

BeBanking is deployed across the Common Monetary Area (CMA) — the monetary union linking South Africa, Namibia, Lesotho, and Eswatini under a shared monetary framework with currencies pegged to the South African Rand.

| Country | CMA status |
|---|---|
| South Africa | CMA member — BeBanking integrated banks: ABSA, FNB, Nedbank SA, Standard Bank SA, Investec |
| Namibia | CMA member — BeBanking integrated banks: Nedbank Namibia, Standard Bank Namibia |
| Lesotho | CMA member |
| Eswatini | CMA member |

CMA-region payments are processed through BeBanking's supported banking partners and the client's own banking arrangements. The CMA geographic scope means BeBanking is not a South Africa-only product. Organisations with operations across the CMA — such as South African organisations with Namibian subsidiaries — can manage regional payments through a single integrated solution.

**Beyond the CMA:** BeBanking's international bank integrations extend beyond the CMA to the United Kingdom (Citi Bank) and Chile (Santander Bank), enabling payment automation outside the African continent.

---

## ERP Integration

International and Forex Payment Processing is supported across BeBanking's confirmed ERP integrations:

| ERP Platform | Integration status | Integration notes |
|---|---|---|
| Oracle E-Business Suite (R11, R12) | Supported | Forex payments initiated from Oracle EBS Accounts Payable; integration with Cash Management (CE) for reconciliation |
| Oracle Fusion Applications | Supported | Forex payments initiated from Oracle Fusion Accounts Payable and payments workflows |
| Acumatica | Supported | Forex payments confirmed via Acumatica Payments and Cash Management modules |
| SAP | Supported | SAP integration confirmed — no module-level or workflow-level forex detail stated |

**Acumatica scope note:** Forex payments are a confirmed Acumatica integration capability through BeBanking, covering supplier-initiated international payments via Acumatica Payments and Cash Management. Payroll H2H payments remain Oracle EBS and Oracle Fusion Applications only — the Acumatica integration does not extend to payroll payment processing.

BeBanking's approval framework operates identically regardless of the ERP platform. Forex payment approvals for Acumatica-sourced transactions follow the same configurable workflow as Oracle-sourced transactions.

---

## Exchange Rate Management

BeBanking provides two distinct but complementary capabilities for foreign currency management. They are separate modules — one manages rate data; the other manages payment execution.

### Automated Exchange Rates (module 6) — Rate loading

The Automated Exchange Rates module automates the daily loading of foreign exchange rates into the ERP. This eliminates a manual daily process and ensures foreign currency transactions in the ERP are valued at the correct current rate.

| Feature | Description |
|---|---|
| Automated daily rate loading | Exchange rates loaded into the ERP automatically each day without user intervention |
| Multiple rate providers | Clients select their preferred rate provider from supported sources |
| Client-selectable providers | Organisations are not locked into a single source; provider can be changed without product customisation |
| Confirmed providers | FNB (First National Bank), Andisa, ExchangeRate-API |

The Automated Exchange Rates module is available independently of the International and Forex Payment Processing module — organisations that need only rate loading can subscribe to module 6 independently.

### International and Forex Payment Processing (module 9) — Payment execution

The payment processing module initiates, approves, and transmits international payment instructions to banking partners. Payments are processed at the exchange rate that has been loaded into the ERP — either through the Automated Exchange Rates module or through a manually entered rate.

**Rate accuracy note:** BeBanking loads exchange rates from client-selected providers. The accuracy and timeliness of exchange rates is the responsibility of the selected rate provider. BeBanking does not provide its own foreign exchange quoting service or guarantee the accuracy of rates from third-party providers.

---

## Banking Integration

BeBanking is integrated with nine banking partners across South Africa, the CMA region, the United Kingdom, and Chile. Payments can be processed through supported banking partners subject to the capabilities and international reach of the selected bank.

| Bank | Country | Notes |
|---|---|---|
| ABSA | South Africa | CMA — all standard BeBanking modules |
| FNB (First National Bank) | South Africa | CMA — also a supported exchange rate provider |
| Nedbank | South Africa | CMA |
| Nedbank | Namibia | CMA regional |
| Standard Bank | South Africa | CMA |
| Standard Bank | Namibia | CMA regional |
| Investec | South Africa | CMA |
| Citi Bank | United Kingdom | International banking partner |
| Santander Bank | Chile | International banking partner |

**Wording guidance:** BeBanking is "integrated with" these banks. There is no formal bank certification programme — do not use "certified by," "approved by," or "licensed by" in tender responses.

---

## Security and Compliance

### Transmission Security

| Control | Implementation |
|---|---|
| API-first architecture | All payment instructions transmitted via API integration; no internet banking portal access required at any stage |
| TLS encryption | All data in transit encrypted using TLS |
| SFTP over SSH | Secure fallback channel for banking partners without API endpoints |
| Server-to-server architecture | Payment instructions transmitted directly between BeBanking and banking partners — no manual handling at any stage |
| No human file handling | Eliminates the security exposure of manual payment file management during transmission |

### Approval Controls

| Control | Description |
|---|---|
| Zero-bypass approval | No payment instruction reaches the banking partner without completing the full configured approval chain — applicable to all payment types including forex |
| Configurable segregation of duties | Forex payment approvers can be defined separately from domestic AP approvers |
| Configurable approval levels | Organisations can require additional approval levels for cross-border or above-threshold payments to reflect their international payment governance requirements |
| ERP-native access control | All approval actions managed through ERP responsibility assignments — no external portal required |
| Location-independent approvals | Approvers can authorise from any location and any device |

### Compliance

| Area | Status | Wording for tender use |
|---|---|---|
| POPIA | **Confirmed — current** | "BeBanking is designed and operated in compliance with the Protection of Personal Information Act (POPIA)." |
| GDPR | **Roadmap — not current** | "GDPR compliance is on the BeBanking product roadmap." |

---

## Benefits

| Benefit | Description |
|---|---|
| Unified payment process | International payments follow the same ERP-initiated, approval-controlled workflow as domestic payments — no separate process, portal, or training |
| Eliminated manual handling | Forex payment instructions generated and transmitted automatically — no manual upload to bank portals, no manual file management |
| ERP-native audit trail | All forex payment approvals and transmission events recorded in the ERP; complete history available for audit and reporting |
| Reduced governance risk | Configurable segregation-of-duty controls and mandatory approval workflows apply to all forex payments, eliminating the governance gaps inherent in internet banking workflows |
| CMA and international reach | Single integrated solution for payments across South Africa, Namibia, Lesotho, Eswatini, the United Kingdom, and Chile |
| Multi-ERP support | Forex payment automation available for Oracle EBS, Oracle Fusion Applications, and Acumatica implementations from a single product |
| Automated rate management | Daily exchange rate loading automated from client-selected providers — eliminates a manual, recurring task prone to error and timing delay |

---

## Use Cases

| Use case | Description |
|---|---|
| International supplier payments | Overseas suppliers paid through BeBanking's integrated banking partners using the same AP approval workflow as domestic suppliers — no separate internet banking session required |
| CMA regional payments | Organisations with subsidiaries or operations in Namibia, Lesotho, or Eswatini process regional payments through BeBanking's integrated banking partners and the client's own banking arrangements |
| International AP payment batches | AP-initiated payments to international suppliers processed through BeBanking's configurable approval workflow — payment instructions transmitted to integrated banking partners without portal access; accepted and rejected payment status reconciled back to the ERP |
| Multi-ERP organisations | Organisations running Oracle EBS, Oracle Fusion, or Acumatica initiate forex payments from within their ERP without accessing a bank portal |
| Multi-bank forex management | Organisations using different banking partners for domestic and international payments (e.g., Nedbank SA for ZAR, Citi Bank UK for international) manage all payments through a single BeBanking integration |
| Daily rate automation | Finance teams automate the daily exchange rate loading process — rates available in the ERP from opening of business, with no manual intervention |

---

## Limitations and Assumptions

| Item | Detail |
|---|---|
| SWIFT transmission model | BeBanking transmits payment instructions to integrated banking partners. Banking partners execute SWIFT and cross-border transactions through their own banking infrastructure. BeBanking does not claim direct SWIFT network membership. |
| International payment reach | Payments can be processed through supported banking partners subject to the capabilities and international reach of the selected bank. Confirm specific payment corridors with the relevant banking partner. |
| Exchange rate accuracy | BeBanking loads exchange rates from client-selected providers (FNB, Andisa, ExchangeRate-API). Rate accuracy and timeliness are the responsibility of the selected provider. BeBanking provides no rate guarantee and does not provide its own exchange rate quoting service. |
| Acumatica scope — forex only | Acumatica forex payments are confirmed as a supplier/AP-initiated capability via Acumatica Payments and Cash Management. Payroll H2H payments are Oracle EBS and Oracle Fusion Applications only — this module does not extend Acumatica payroll capabilities. |
| Parliament FX Rates document | The APPSolve BeBanking Parliament FX Rates document (Parties/Customers/Parliament/APPSolve BeBanking Parliament FX Rates.docx) is recorded as a future enhancement source. Review of this document may yield additional forex detail in a future file version. It does not affect the accuracy of the current content, which is drawn from the confirmed Session C fact baseline. |
| No payment volume claims | No statements are made about payment processing volumes, transaction throughput, or processing SLAs. |

---

**Remediation notes (2026-06-10 — Session W1S3-005 review resolution):**

Six review findings resolved by BU lead decisions:

**Decision 1 — SWIFT model:** All references to "SWIFT payment processing" as a BeBanking-direct capability replaced with the confirmed indirect model: BeBanking transmits payment instructions to integrated banking partners; banking partners execute SWIFT transactions through their own infrastructure. Updated in: capability table, SWIFT section intro and step 5, use cases, limitations. BeBanking does not claim direct SWIFT network membership.

**Decision 2 — CMA support:** Removed the banking integration column from the CMA table for Lesotho and Eswatini (previously showed "Via CMA banking relationships" which implied a named integration). Replaced with statement that CMA processing occurs through supported banking partners and client banking arrangements. Lesotho and Eswatini remain listed as CMA members.

**Decision 3 — SAP:** SAP ERP table row updated. Removed "specific forex workflow and module detail pending BQ-WEB-04 confirmation." SAP now appears as "Supported — no module-level or workflow-level forex detail stated." SAP Limitations row removed (no longer applicable).

**Decision 4 — Treasury use case:** Treasury-initiated cross-border payments use case replaced with "International AP payment batches" — AP-initiated international supplier payments through BeBanking's configurable approval workflow. Reference to "treasury governance policies" in the approval controls section replaced with "international payment governance requirements."

**Decision 5 — International reach wording:** "Geographic reach of individual payments depends on the receiving bank's own international payment network" and "confirms BeBanking's ability to initiate and transmit international payments beyond the African continent" replaced with the confirmed wording: "Payments can be processed through supported banking partners subject to the capabilities and international reach of the selected bank."

**Decision 6 — Parliament FX document:** Limitations row updated. Parliament document recorded as a future enhancement source only. Promotion is not blocked by this document.

**Original authoring basis:** SESSION_C_FACT_BASELINE.md BQ7, BQ11, BQ12; BeBanking_CAPABILITY_MAP.md §7; Automated Exchange Rates description from SITA v1.06.
