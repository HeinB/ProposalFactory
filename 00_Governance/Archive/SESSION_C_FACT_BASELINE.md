# Session C — BeBanking Confirmed Fact Baseline
**Established:** 2026-06-10
**Updated:** 2026-06-10 (BQ7 confirmed)
**Source:** BeBanking BU Lead responses to Session C review questions (BQ1–BQ13) and website alignment review (BQ-WEB-01–06)
**Authority:** BU Lead guidance supersedes SITA v1.06 (2017), historical proposals, website alignment report, and extraction assumptions.
**Status:** All 13 questions confirmed. Session C fully unblocked. Authoritative baseline for Session C review. Do not modify approved Session A content on the basis of this document.

---

## Status Summary

| Question | Status | Impact |
|---|---|---|
| SAP ERP support | Confirmed | High — adds a 4th ERP platform |
| BQ1 — Connectivity architecture | Confirmed | Critical — Connect Direct obsolete; API/SFTP model |
| BQ2 — Approval model | Confirmed | High — historical AP/PAY Level 1/2 obsolete |
| BQ3 — Cloud ERP support | Confirmed | Moderate — both on-premise and cloud supported |
| BQ4 — Banking integrations | Confirmed | Critical — 9 named banks including international |
| BQ5 — Acumatica integration | Confirmed | High — specific modules and scope confirmed |
| BQ6 — Oracle Fusion support | Confirmed | Confirmed |
| BQ7 — Module currency | **Confirmed 2026-06-10** | High — 2 modules retired; 2 modules added |
| BQ8 — AVS | Confirmed | Low — no change to existing content |
| BQ9 — Commercial model | Confirmed | High — historical licensing model obsolete |
| BQ10 — Monitoring and audit | Confirmed | Moderate — monitoring content gap resolved |
| BQ11 — Forex capability | Confirmed | Critical — W1S3-005 moves from STRUCTURE ONLY to MODERNISE |
| BQ12 — Exchange rate sources | Confirmed | Low — specific sources named |
| BQ13 — POPIA compliance | Confirmed | Moderate — POPIA confirmed, GDPR roadmap |

---

## Confirmed Fact Baseline

### F-C-01 — Supported ERP Platforms

BeBanking integrates with:

- **Oracle E-Business Suite** (Oracle EBS) — R11, R12
- **Oracle Fusion Applications** (Oracle Cloud ERP)
- **Acumatica** (via Acumatica Payments and Acumatica Cash Management modules)
- **SAP** — confirmed integration (see SAP note below)

Both **on-premise** and **cloud ERP deployments** are supported.

**SAP note:** SAP integration is confirmed by the BeBanking BU lead. The Session A removal (F10/D1) was correct based on corpus evidence at the time (zero references in 18,400 files, all from pre-2017 sources). The website reflects current product capability. This is a product evolution post-2017, not a corpus error. W1S1-005 is flagged for future enhancement review but Session A is not reopened.

### F-C-02 — Banking Integrations

BeBanking is **integrated with** the following banks (9 confirmed):

| Bank | Jurisdiction |
|---|---|
| ABSA | South Africa |
| Nedbank | South Africa |
| Nedbank | Namibia |
| FNB (First National Bank) | South Africa |
| Standard Bank | South Africa |
| Standard Bank | Namibia |
| Investec | South Africa |
| Citi Bank | United Kingdom |
| Santander Bank | Chile |

**Wording guidance:** Use "integrated with" — do not use "certified by." There is no formal bank certification programme.

**Geographic reach:** BeBanking is deployed across the **Common Monetary Area (CMA)** — South Africa, Namibia, Lesotho, and Eswatini — as well as internationally. Confirmed international integrations include Citi Bank United Kingdom and Santander Bank Chile. All Session C files should use international-ready framing. Remove "South African banking infrastructure" language where it appears.

### F-C-03 — Connectivity Architecture (replaces Connect Direct)

**Connect Direct is no longer used.**

Current architecture:
- **API-first:** APIs are the preferred communication method with both clients and banks.
- **SFTP fallback:** For banks that do not expose APIs, BeBanking provides an API layer that communicates with banks using SFTP.

All references to Connect Direct in Session C candidates must be replaced with the API / SFTP architecture description.

**Supersedes:** All SITA v1.06 (2017) references to Connect Direct and dedicated file transfer utilities. The **Secure File Transfer module** has been retired (see F-C-12) — the API layer now provides secure transmission natively.

### F-C-04 — Approval Framework (replaces AP/PAY Level 1/2 model)

**The historical AP Level 1 / AP Level 2 and PAY Level 1 / PAY Level 2 model is obsolete.**

Current model:
- Flexible approval framework
- Supports **first-responder wins** (first qualified approver completes the approval)
- Supports **voting-based approvals** (majority or consensus required)
- **Unlimited approval levels** — configurable per client
- **Configurable segregation-of-duty controls**
- Designed to meet client-specific governance requirements

All approval workflow descriptions in Session C candidates must be updated to reflect this framework.

### F-C-05 — Acumatica Integration Scope

BeBanking integrates with:
- **Acumatica Payments** module
- **Acumatica Cash Management** module

Supported capabilities through Acumatica:
- Local payments
- Forex payments
- Bank statement processing

**Approval workflows** are managed in BeBanking and provide equivalent functionality regardless of the ERP platform. The approval framework (F-C-04) applies to Acumatica-sourced transactions identically to Oracle-sourced transactions.

**Important — payroll scope:** Acumatica does not provide payroll functionality in the South African market. BeBanking Payroll H2H is supported from Oracle EBS and Oracle Fusion Applications payroll sources only. Do not apply F-C-05 capabilities to payroll processing.

### F-C-06 — Forex Capability

**BeBanking is confirmed as a full forex payment capability.** (Resolves W1S3-005 structural gap.)

Confirmed capabilities:
- **International payments** — full cross-border payment processing
- **SWIFT / foreign payment processing** — confirmed
- **Forex exchange rate management** — automated rate loading

Exchange rate sources (client choice — multiple sources supported):
- First National Bank (FNB)
- Andisa
- ExchangeRate-API

**Confirmed module name:** "International and Forex Payment Processing" (see F-C-12).

**Wording guidance:** Do not imply a single mandatory rate provider. Position as "supported sources include…" or "clients can choose from multiple rate providers."

**Supersedes:** The W1S3-005 SITA v1.06 "partial gap" classification. W1S3-005 readiness is elevated from STRUCTURE ONLY to MODERNISE.

### F-C-07 — Oracle Integration Scope

BeBanking integrates with:
- **Oracle E-Business Suite** (R11, R12) — deep integration including AP, Payroll, Cash Management (CE), AR
- **Oracle Fusion Applications** — confirmed integration

### F-C-08 — AVS (Account Verification Services)

AVS remains an active BeBanking module. Available across all supported banks. Integrated with banking account verification services.

No changes to the AVS description from what was extracted in W1S3-003.

### F-C-09 — Commercial / Licensing Model (replaces Service Option / Software Option)

**The historical Service Option / Software Option two-model licensing structure is obsolete.**

Current model:
- **Monthly subscription**
- **Annual subscription**

There is no once-off licence model. There is no once-off implementation ownership model.

All commercial references in W1S3-009 (and any other Session C file citing the commercial model) must be updated.

### F-C-10 — Monitoring and Audit Capabilities

BeBanking provides:
- **Payment approval reporting** — approval status and workflow visibility
- **Transaction-level audit reporting** — full transaction history and audit trail
- **Bank account maintenance approval reporting** — audit trail for banking detail changes
- **Operational monitoring and audit visibility** — operational oversight across banking workflows

This confirms and resolves the [UPDATE] monitoring placeholder in W1S3-010.

### F-C-11 — POPIA and GDPR Compliance

- **POPIA:** BeBanking is POPIA compliant. Confirmed for use in South African tender compliance sections.
- **GDPR:** Future roadmap capability. Must be positioned as "roadmap / future-state" — do not represent as current.

**Wording guidance for POPIA:** "BeBanking is designed and operated in compliance with the Protection of Personal Information Act (POPIA)."
**Wording guidance for GDPR:** "GDPR compliance is on the BeBanking product roadmap."

### F-C-12 — Confirmed Module Portfolio (BQ7 — confirmed 2026-06-10)

#### Current modules (9 — confirmed as at June 2026)

| # | Module | Status |
|---|---|---|
| 1 | Unbreakable Bank Statements | Current |
| 2 | Integrated Account Verification Services (AVS) | Current |
| 3 | Supplier Bank Account Approval | Current |
| 4 | Supplier H2H Payments and Approval | Current |
| 5 | Payroll H2H Payments and Approval | Current |
| 6 | Automated Exchange Rates | Current |
| 7 | Supplier PDF Remittances | Current |
| 8 | ABSA Proof of Payment Integration | Current — **new; not in W1S3-001** |
| 9 | International and Forex Payment Processing | Current — **new; replaces partial gap in W1S3-005** |

#### Retired modules (no longer offered)

| Module | Status | Impact |
|---|---|---|
| Secure File Transfer | **Retired** | Remove from W1S3-001 module table; remove from W1S3-008 architecture; API layer now provides secure transmission |
| Automated Receipt Creation | **Retired** | Remove from W1S3-001 module table; remove from W1S3-010 automation table |

#### Key positioning notes

- **Secure File Transfer** must not be cited as a current capability. The API-first architecture (F-C-03) provides secure transmission natively. Do not describe the retired module as simply "renamed."
- **Automated Receipt Creation** must not be cited as a current capability. Remove from all session C files.
- **ABSA Proof of Payment Integration** is a bank-specific module — note in tender content that this integration is available for ABSA clients. Do not imply it applies to all banks.
- **International and Forex Payment Processing** is the confirmed module name for the forex capability confirmed in BQ11. Use this name consistently. Note: this is separate from **Automated Exchange Rates** (module #6) — they are distinct capabilities. Automated Exchange Rates = loading FX rates into the ERP; International and Forex Payment Processing = initiating and transmitting international payments.
- **Module count:** The product remains a 9-module suite as documented in W1S3-001. The composition has changed; the count has not.

---

## Resolved Contradictions

The BU lead responses resolved the following contradictions that existed between repository content and the current product:

| Contradiction | Repository position (pre-BU) | Confirmed resolution |
|---|---|---|
| SAP ERP support | Removed in Session A (F10/D1) — no corpus evidence | **Confirmed current capability.** Session A removal was correct at the time. Product evolved post-2017. Flag W1S1-005 for future enhancement. |
| Connect Direct connectivity | Referenced as current architecture in SITA v1.06 | **Obsolete.** API-first model; SFTP where no bank API exists. All references to be updated. |
| AP Level 1/2 / PAY Level 1/2 approval model | Described as current in SITA v1.06 | **Obsolete.** Flexible approval framework with unlimited levels, voting, first-responder options. |
| Service Option / Software Option licensing | Described as current in W1S3-009 | **Obsolete.** Monthly and annual subscription only. |
| "South African banks" framing | Approved W1S1-005 says "all major South African banks" | **Resolved.** Bank list confirmed: 9 banks across South Africa, Namibia, UK, and Chile. CMA positioning confirmed. W1S1-005 flagged for future enhancement (Session A not reopened). |
| Forex capability as a gap | W1S3-005 classified as STRUCTURE ONLY — SWIFT unconfirmed | **Confirmed full capability.** International payments, SWIFT processing, forex exchange rates all confirmed. W1S3-005 elevated to MODERNISE. Module named "International and Forex Payment Processing." |
| Commercial model | Service Option / Software Option (once-off + recurring) | **Obsolete.** Subscription-only model (monthly or annual). |
| Module portfolio (BQ7) | W1S3-001 December 2024 list assumed current — unconfirmed | **Resolved.** 2 modules retired (Secure File Transfer, Automated Receipt Creation); 2 modules added (ABSA Proof of Payment Integration, International and Forex Payment Processing). Net module count unchanged at 9. |

---

## Open Items

| # | Question | Status | Affects |
|---|---|---|---|
| BQ-WEB-01 | R6 billion transactions/month statistic — authorised for tender use? | Pending | W1S1-005 (future), W1S3-001 |
| BQ-WEB-02 | Is Disaster Recovery a named BeBanking module or a hosting-level feature? | Pending | W1S3-008, W1S3-009 |
| BQ-WEB-03 | Sage ERP integration scope | Pending | W1S1-005 (future), W1S3-001, W1S3-006 |
| BQ-WEB-04 | SAP integration architecture and scope details | Pending | W1S3-006 |
| CORP-01 | Corporate relationship between appsolve.co.za and appsolvegroup.com | Pending | HANDOVER.md, W1S1-008 future review |

**Note:** None of the open items block Session C approvals. BQ-WEB-04 affects the SAP section of W1S3-006 only — the file can be approved with a brief SAP compatibility statement pending full detail. All other items are enhancements or future-review items.

---

## Positioning Notes for Session C Content

Derived from the confirmed baseline. Apply when editing Session C candidates.

**1. CMA and international product, not South African only.** BeBanking is deployed across the Common Monetary Area (South Africa, Namibia, Lesotho, Eswatini) and internationally (UK, Chile). Frame as "banking automation for ERP-connected organisations across South Africa, the CMA region, and internationally."

**2. ERP-agnostic approval framework.** The flexible approval framework (F-C-04) operates identically across Oracle EBS, Oracle Fusion, Acumatica, and SAP. This is a differentiator — a single BeBanking implementation serves a mixed ERP estate.

**3. API-first architecture.** The move from Connect Direct to APIs is not just a technology update — it positions BeBanking as a modern, open-integration product. Secure File Transfer as a standalone module is retired; secure transmission is now inherent in the API layer.

**4. Subscription-only commercial model.** This simplifies the commercial conversation and aligns with cloud-era buying patterns. All once-off pricing references must be removed.

**5. POPIA compliance is a tender-ready claim.** For South African government and financial sector tenders, POPIA compliance is a frequent requirement. This claim can be stated directly.

**6. Forex is a named, full product capability.** Module name: "International and Forex Payment Processing." Not just exchange rate loading (that is the separate "Automated Exchange Rates" module). Position as a standalone international payments capability.

**7. ABSA Proof of Payment Integration is bank-specific.** Do not present it as a universal feature. Frame as: "Available for ABSA clients" or "ABSA-specific integration."

---

*This baseline establishes the authoritative BeBanking product facts for Session C review. For Session A approved content, see `00_Governance/APPROVAL_SUMMARY_WAVE1.md` and `07_Approved_Content/Approved/Cross_BU/`. Session A content is not modified by this document.*
