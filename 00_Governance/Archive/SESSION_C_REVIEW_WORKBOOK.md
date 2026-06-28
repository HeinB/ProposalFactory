# Session C — BeBanking Core Review Workbook
**Session:** Wave 1, Session C — BeBanking H2H Capability (W1S3-001 through W1S3-010)
**Prepared:** 2026-06-09 | **Updated:** 2026-06-10 (BU lead responses received)
**Prepared by:** Claude (AI pre-review)
**Review standard applied:** Session A standard + BeBanking BU lead gate (see SESSION_A_CLOSEOUT.md Standard 6)
**Status:** All 13 questions resolved. BQ7 confirmed 2026-06-10. Session C fully unblocked. All files ready for editing and Review_Required advancement.

See also: `SESSION_C_FACT_BASELINE.md` (full baseline) | `SESSION_C_IMPACT_ANALYSIS.md` (per-file changes)

---

## Scope

| File | Title | Source | Vintage | Readiness |
|---|---|---|---|---|
| W1S3-001 | Product Overview | HyDac V5.1 Template BeBanking | December 2024 | DIRECT |
| W1S3-002 | Host-to-Host Banking Core | SITA BeBanking Proposal v1.06 | June 2017 | MODERNISE |
| W1S3-003 | Supplier Payments | SITA BeBanking Proposal v1.06 | June 2017 | MODERNISE |
| W1S3-004 | Payroll Payments | SITA BeBanking Proposal v1.06 | June 2017 | MODERNISE |
| W1S3-005 | Forex Payments | SITA BeBanking Proposal v1.06 | June 2017 | ~~STRUCTURE ONLY~~ → **MODERNISE** |
| W1S3-006 | ERP Integration | SITA BeBanking Proposal v1.06 | June 2017 | MODERNISE |
| W1S3-007 | Security | SITA BeBanking Proposal v1.06 | June 2017 | MODERNISE |
| W1S3-008 | Technical Architecture | SITA BeBanking Proposal v1.06 | June 2017 | MODERNISE |
| W1S3-009 | Hosting and Deployment Model | SITA BeBanking Proposal v1.06 | June 2017 | MODERNISE |
| W1S3-010 | Monitoring and Automation | SITA BeBanking Proposal v1.06 | June 2017 | MODERNISE |

**Critical note on source material:** W1S3-001 is sourced from December 2024. W1S3-002 through W1S3-010 are sourced from SITA v1.06 (June 2017). BU lead responses now supersede SITA v1.06 assumptions throughout. The 2017 connectivity model (Connect Direct), approval model (AP/PAY Level 1/2), and commercial model (Service Option / Software Option) are all confirmed obsolete.

**Consistency anchor:** The approved file W1S1-005 (BeBanking Product Overview, Session A) states: Oracle EBS, Oracle Fusion Applications, and Acumatica as supported ERPs; "all major South African banks." Session C files will add SAP to ERP platforms (BU confirmed) and the specific 9-bank list including international banks. W1S1-005 is flagged for future enhancement but is not modified (Session A is closed).

---

## Consolidated BU Lead Questions

BU lead responses received 2026-06-10. Authoritative baseline documented in `SESSION_C_FACT_BASELINE.md`.

### Architecture

| # | Question | Affects files | Priority | BU Answer |
|---|---|---|---|---|
| BQ1 | Is Connect Direct still the primary bank connectivity channel, or has SFTP or API replaced it? | W1S3-002, 006, 007, 008, 010 | High | **CONFIRMED — Connect Direct is obsolete.** Current architecture: API-first. SFTP for banks without API endpoints (via BeBanking API layer). Update all architecture and integration documents. |
| BQ2 | Is the two-level approval architecture (AP Level 1/Level 2; PAY Level 1/Level 2) still current? | W1S3-002, 003, 004, 007 | High | **CONFIRMED — historical model is obsolete.** Current: Flexible approval framework. Supports first-responder wins and voting-based approvals. Unlimited approval levels. Configurable segregation-of-duty controls. Client-specific governance requirements. |
| BQ3 | Does BeBanking support cloud-hosted ERP deployments? | W1S3-008, 009 | High | **CONFIRMED.** Supports both on-premise and cloud ERP deployments. Oracle EBS, Oracle Fusion Applications, and Acumatica all supported on both deployment models. |

### Banking and Integration

| # | Question | Affects files | Priority | BU Answer |
|---|---|---|---|---|
| BQ4 | What is the current full list of banking integrations? | W1S3-001, 002 | Critical | **CONFIRMED — 9 integrations.** ABSA; Nedbank South Africa; Nedbank Namibia; FNB; Standard Bank South Africa; Standard Bank Namibia; Investec; Citi Bank United Kingdom; Santander Bank Chile. **Use "integrated with" — not "certified by."** No formal bank certification programme. |
| BQ5 | Acumatica integration: which specific modules and approval workflow? | W1S3-001, 002, 004, 006 | Critical | **CONFIRMED.** Integrates with Acumatica Payments and Acumatica Cash Management. Supports local payments, forex payments, bank statement processing. Approval workflows managed in BeBanking — equivalent functionality regardless of ERP platform. |
| BQ6 | Does BeBanking integrate with Oracle Fusion Applications? | W1S3-001, 006 | Critical | **CONFIRMED.** Integrates with Oracle E-Business Suite and Oracle Fusion Applications. |

### Product and Capability

| # | Question | Affects files | Priority | BU Answer |
|---|---|---|---|---|
| BQ7 | Is the 9-module portfolio in W1S3-001 still the complete current product? | W1S3-001, 010 | High | **CONFIRMED 2026-06-10.** Current modules (9): Unbreakable Bank Statements; Integrated AVS; Supplier Bank Account Approval; Supplier H2H Payments and Approval; Payroll H2H Payments and Approval; Automated Exchange Rates; Supplier PDF Remittances; **ABSA Proof of Payment Integration (new)**; **International and Forex Payment Processing (new)**. Retired: Secure File Transfer; Automated Receipt Creation. Net count unchanged at 9. |
| BQ8 | Is AVS still an active BeBanking module? | W1S3-003 | Medium | **CONFIRMED.** AVS remains active. Available across all supported banks. Integrated with banking account verification services. |
| BQ9 | Is the Service Option / Software Option licensing structure still current? | W1S3-009 | Medium | **CONFIRMED — historical model is obsolete.** Current model: Monthly subscription and Annual subscription only. No once-off licence. No once-off implementation ownership. |
| BQ10 | Does BeBanking include a monitoring dashboard or alerting capability? | W1S3-010 | Medium | **CONFIRMED.** BeBanking provides: payment approval reporting; transaction-level audit reporting; bank account maintenance approval reporting; operational monitoring and audit visibility. |

### Capability Scope

| # | Question | Affects files | Priority | BU Answer |
|---|---|---|---|---|
| BQ11 | Does BeBanking support full international/SWIFT payment processing? | W1S3-005 | Critical | **CONFIRMED — full capability.** Supports international payments, SWIFT / foreign payment processing, and forex exchange rates. Treat Forex Payments as a full product capability. W1S3-005 elevated from STRUCTURE ONLY to MODERNISE. |
| BQ12 | Are exchange rates sourced from a bank feed or third-party provider? | W1S3-005, 010 | Low | **CONFIRMED — client choice.** Supported sources: FNB, Andisa, ExchangeRate-API. Clients select preferred source(s). Do not imply a single mandatory provider. |

### Compliance

| # | Question | Affects files | Priority | BU Answer |
|---|---|---|---|---|
| BQ13 | Should POPIA compliance claims be added to BeBanking security documentation? | W1S3-007 | Medium | **CONFIRMED.** BeBanking is POPIA compliant. Add to security documentation. GDPR compliance is on the roadmap — position as future-state only. |

### SAP — Resolved Contradiction (from Website Alignment Review)

| # | Item | Affects files | Resolution |
|---|---|---|---|
| WB-PC-001 | Does BeBanking support SAP integration? | W1S3-001, 006, and W1S1-005 future flag | **CONFIRMED.** SAP integration is supported. Session A removal (F10/D1) was correct based on 2017 corpus evidence. Website reflects current product capability. Record as resolved contradiction. Add SAP to ERP platforms. Flag W1S1-005 for future enhancement — do not reopen Session A. |

### Additional Website Alignment Questions (BQ-WEB)

| # | Question | Affects files | Status |
|---|---|---|---|
| BQ-WEB-01 | Confirm "R6 billion transactions per month" statistic for tender use | W1S1-005 (future), W1S3-001 | Pending |
| BQ-WEB-02 | Is Disaster Recovery a named module or hosting feature? | W1S3-008, W1S3-009 | Pending |
| BQ-WEB-03 | Confirm Sage ERP integration scope | W1S1-005 (future), W1S3-001, W1S3-006 | Pending |
| BQ-WEB-04 | SAP integration architecture and scope details | W1S3-006 | Pending |
| BQ-WEB-05 | Confirm 9-bank list is the definitive 2026 list for tender use | W1S1-005, W1S3-002 | Covered by BQ4 — confirmed |
| BQ-WEB-06 | Confirm full SWIFT/forex capability scope | W1S3-005 | Covered by BQ11 — confirmed |

---

## Per-File Pre-Review (Updated)

---

### W1S3-001 — Product Overview
**Source:** HyDac V5.1 (December 2024) | **Readiness:** DIRECT | **BU gate:** All 13 questions resolved

**Confirmed edits:**

| Edit | Change |
|---|---|
| Module table — remove | Secure File Transfer (retired per BQ7) |
| Module table — remove | Automated Receipt Creation (retired per BQ7) |
| Module table — add | ABSA Proof of Payment Integration (new; ABSA-specific — note bank-specific scope) |
| Module table — add | International and Forex Payment Processing (new; use confirmed module name) |
| ERP Compatibility | Add Oracle Fusion Applications (BQ6 confirmed); Add SAP (BU confirmed) |
| Bank reference | Option to add the specific 9-bank list if preferred over generic language |
| Geographic framing | Update to CMA / international where applicable |

**Client-specific language:** None detected.

**Preliminary recommendation:** **Approve with edit.** Can advance to Review_Required.

**Rating:** DIRECT — unchanged.

---

### W1S3-002 — Host-to-Host Banking Core Capability
**Source:** SITA v1.06 (June 2017) | **Readiness:** MODERNISE

**Confirmed edits:**

| Edit | Change |
|---|---|
| Connectivity throughout | Replace all "Connect Direct" references: "API integration; SFTP for banks without API endpoints" |
| Approval model | Replace AP Level 1/2 and PAY Level 1/2 with flexible approval framework (unlimited levels, first-responder wins, voting, configurable SOD) |
| Bank list | Replace "[UPDATE]" placeholder: ABSA, Nedbank South Africa, Nedbank Namibia, FNB, Standard Bank South Africa, Standard Bank Namibia, Investec, Citi Bank United Kingdom, Santander Bank Chile. Use "integrated with." |
| Acumatica | Expand from single mention to confirmed parity: BeBanking manages approval workflows regardless of ERP; Acumatica Payments and Cash Management modules |
| International framing | Remove "South African banks only" framing; reflect Namibia, UK, and Chile integrations |
| "Standard Bank (used in multiple implementations)" | Remove parenthetical |

**Preliminary recommendation:** **Approve with edits.** All blockers resolved. Can advance to Review_Required.

**Rating:** MODERNISE — unchanged.

---

### W1S3-003 — Supplier Payments
**Source:** SITA v1.06 (June 2017) | **Readiness:** MODERNISE

**Confirmed edits:**

| Edit | Change |
|---|---|
| Approval model | Replace "AP Level 1" and "AP Level 2" with flexible approval framework description |
| AVS | Confirmed active and accurate — no content change needed |

**Preliminary recommendation:** **Approve with minor edit.** Simplest W1S3 file. Can advance to Review_Required.

**Rating:** MODERNISE — unchanged.

---

### W1S3-004 — Payroll Payments
**Source:** SITA v1.06 (June 2017) | **Readiness:** MODERNISE

**Confirmed edits:**

| Edit | Change |
|---|---|
| Approval model | Replace "PAY Level 1" and "PAY Level 2" with flexible approval framework |
| ERP payroll scope | Replace "Oracle EBS Payroll module or equivalent" with: Oracle EBS and Oracle Fusion Applications. Acumatica does not provide payroll functionality in South Africa — remove any Acumatica payroll references. |

**Note:** ACB format is the South African payroll file format (Automated Clearing Bureau). Applies to Oracle EBS and Oracle Fusion payroll implementations only. BQ5 clarification: Acumatica does not provide payroll functionality in South Africa. Retain ACB reference; no Acumatica payroll references should appear in this file.

**Preliminary recommendation:** **Approve with edits.** Can advance to Review_Required.

**Rating:** MODERNISE — unchanged.

---

### W1S3-005 — International and Forex Payment Processing
**Source:** SITA v1.06 (June 2017) | **Readiness:** ~~STRUCTURE ONLY~~ → **MODERNISE**

**⚑ Critical elevation. This file was previously blocked. BQ11 confirms full forex capability. BQ7 confirms module name.**

**Confirmed module name (BQ7):** "International and Forex Payment Processing"
**Recommended file retitle to:** `W1S3-005-BB-InternationalForexPayments-DRAFT.md`

**What was in the file:** Automated Exchange Rates section (confirmed) + STRUCTURE ONLY placeholder (forex processing unconfirmed).

**Content to be authored from confirmed baseline:**

| Section | Content required |
|---|---|
| Forex payment processing overview | International payment capability; SWIFT processing; end-to-end payment lifecycle; approval workflows via flexible framework |
| Exchange rate management | Multi-source rate loading; FNB, Andisa, ExchangeRate-API; client selects preferred source(s) |
| Bank connectivity for forex | International bank integrations confirm cross-border capability: Citi Bank UK, Santander Bank Chile |
| Approval workflow for forex | Flexible approval framework applies; configurable SOD controls for forex authorisation |
| Distinction note | Clarify: this module = international payment initiation. Automated Exchange Rates (module #6) = ERP rate loading. These are distinct capabilities. |

**Preliminary recommendation:** **Authoring required — then advance to Review_Required.** The only file requiring new content authoring rather than editing.

**Rating:** STRUCTURE ONLY → **MODERNISE**.

---

### W1S3-006 — ERP Integration
**Source:** SITA v1.06 (June 2017) | **Readiness:** MODERNISE (previously stalled — now unblocked)

**Confirmed edits:**

| Edit | Change |
|---|---|
| Connectivity | Replace all Connect Direct references with API/SFTP |
| Remove Secure File Transfer Utility | Retired per BQ7 — remove from any component lists or diagrams |
| Acumatica section | Write from confirmed baseline: Acumatica Payments + Cash Management; local payments, forex payments, bank statement processing; BeBanking manages approval workflows |
| Oracle Fusion | Add Oracle Fusion Applications to Oracle integration section |
| SAP | Add brief SAP compatibility statement pending BQ-WEB-04 detail |
| IBY module | Remove or footnote — Oracle Fusion does not use IBY |

**Split consideration:** If SAP integration architecture proves materially different from Oracle EBS and Acumatica, consider splitting into W1S3-006a (Oracle + Acumatica) and W1S3-006b (SAP) at review. Raise with BU lead.

**Preliminary recommendation:** **Approve with edits + new Acumatica section.** Can advance to Review_Required.

**Rating:** MODERNISE — unchanged (but unblocked).

---

### W1S3-007 — Security
**Source:** SITA v1.06 (June 2017) | **Readiness:** MODERNISE

**Confirmed edits:**

| Edit | Change |
|---|---|
| Connect Direct | Replace "Dedicated banking server with Connect Direct connectivity" with API-based architecture statement |
| Approval model | Update any Level 1/2 references in security context to flexible approval framework |
| POPIA | Add: "BeBanking is designed and operated in compliance with the Protection of Personal Information Act (POPIA)" |
| GDPR | Add as roadmap: "GDPR compliance is on the BeBanking product roadmap" |

**High-value outcome:** POPIA confirmation makes this file directly usable in South African government and financial sector tenders.

**Preliminary recommendation:** **Approve with targeted edits.** Can advance to Review_Required.

**Rating:** MODERNISE — unchanged.

---

### W1S3-008 — Technical Architecture
**Source:** SITA v1.06 (June 2017) | **Readiness:** MODERNISE

**Confirmed edits:**

| Edit | Change |
|---|---|
| Connectivity architecture | **Significant rewrite.** "Dedicated banking server with Connect Direct" → BeBanking API integration layer; SFTP where bank does not expose APIs; BeBanking provides the translation layer |
| Architecture diagram | Update ASCII diagram: "Connect Direct" → "API / SFTP Layer"; "Standard Bank" → "Bank H2H System"; remove Secure File Transfer Utility component |
| Remove Secure File Transfer Utility | Retired per BQ7 — remove from component descriptions and architecture diagram |
| Cloud ERP | Add: BeBanking supports on-premise and cloud ERP configurations |
| ERP integration table | Add SAP and Oracle Fusion; remove IBY-specific reference; remove Secure File Transfer Utility as component |
| International framing | Reflect international bank integrations (Namibia, UK, Chile) |

**Note on Appendix 5.2:** The SITA v1.06 process flow diagram is now less relevant as the architecture has changed. A new diagram based on the API model would have higher value.

**Preliminary recommendation:** **Approve with significant section rewrite.** All facts confirmed. Can advance to Review_Required.

**Rating:** MODERNISE — unchanged.

---

### W1S3-009 — Hosting and Deployment Model
**Source:** SITA v1.06 (June 2017) | **Readiness:** MODERNISE

**Confirmed edits:**

| Edit | Change |
|---|---|
| Commercial model | **Complete rewrite.** Remove Service Option / Software Option. Replace: Monthly subscription; Annual subscription. No once-off licence. |
| Cloud deployment | Add: BeBanking supports both on-premise ERP and cloud ERP client configurations |
| 24x7x365 | Apply D3-equivalent fix: "24x7 monitoring capability with after-hours support services" |

**Preliminary recommendation:** **Approve with commercial rewrite.** Can advance to Review_Required.

**Rating:** MODERNISE — unchanged.

---

### W1S3-010 — Monitoring and Automation
**Source:** SITA v1.06 (June 2017) | **Readiness:** MODERNISE

**Confirmed edits:**

| Edit | Change |
|---|---|
| Remove Automated Receipt Creation | Retired per BQ7 — remove from the 6-process automation table; table becomes 5 processes |
| Connect Direct in automation table | Update bank statement import row: API / SFTP |
| Monitoring section | **Complete the [UPDATE] placeholder:** Payment approval reporting; transaction-level audit reporting; bank account maintenance approval reporting; operational monitoring and audit visibility |
| Exchange rate source | "Supported sources include FNB, Andisa, and ExchangeRate-API — clients select their preferred source" |

**Preliminary recommendation:** **Approve with targeted edits.** Monitoring gap resolved. Can advance to Review_Required.

**Rating:** MODERNISE — unchanged.

---

## Summary Assessment (Updated)

| File | Readiness | Status | Key edit | Can advance? |
|---|---|---|---|---|
| W1S3-001 Product Overview | DIRECT | Approve with edit | Module table: 2 retired, 2 added; SAP + Oracle Fusion add | Yes |
| W1S3-002 H2H Core | MODERNISE | Approve with edits | Connectivity; approval model; bank list; Acumatica | Yes |
| W1S3-003 Supplier Payments | MODERNISE | Approve with minor edit | Approval model only | Yes |
| W1S3-004 Payroll Payments | MODERNISE | Approve with edits | Approval model; Acumatica payroll | Yes |
| W1S3-005 Forex | **MODERNISE** (elevated) | Authoring required | New content: SWIFT/forex/exchange rates | Authoring first |
| W1S3-006 ERP Integration | MODERNISE (unblocked) | Approve with edits | Acumatica section; SAP statement; Oracle Fusion; connectivity | Yes |
| W1S3-007 Security | MODERNISE | Approve with edits | POPIA; Connect Direct; approval model | Yes |
| W1S3-008 Architecture | MODERNISE | Approve with significant rewrite | API architecture; cloud; diagram | Yes |
| W1S3-009 Hosting Model | MODERNISE | Approve with edits | Commercial rewrite; cloud; 24x7 fix | Yes |
| W1S3-010 Monitoring | MODERNISE | Approve with edits | Remove Automated Receipt Creation; complete monitoring section; connectivity | Yes |

**Files ready to advance (edit-only):** W1S3-001, 002, 003, 004, 006, 007, 008, 009, 010 — 9 files
**File requiring content authoring:** W1S3-005 — 1 file
**Files blocked:** None. All 13 BU lead questions are answered.

---

## Updated Approval Prerequisites

1. **All 13 BU lead questions are resolved.** No questions gate any file approval. BQ7 confirmed 2026-06-10.
2. **W1S3-005 requires content authoring** from `SESSION_C_FACT_BASELINE.md` F-C-06 and F-C-12 before advancing. Module name confirmed: "International and Forex Payment Processing."
3. **W1S3-006 SAP section** should be limited to a brief compatibility statement until BQ-WEB-04 is answered. Does not block approval.
4. **W1S1-005 future enhancement flag** must be recorded in governance — SAP is confirmed but Session A is closed.

---

## Suggested Approval Sequence (Updated)

| Order | File | Complexity | Notes |
|---|---|---|---|
| 1 | W1S3-007 Security | Low | POPIA + Connect Direct; high tender value |
| 2 | W1S3-003 Supplier Payments | Very low | Approval model only |
| 3 | W1S3-004 Payroll Payments | Low | Approval model + Acumatica |
| 4 | W1S3-009 Hosting Model | Low-Medium | Commercial rewrite + cloud + 24x7 fix |
| 5 | W1S3-001 Product Overview | Medium | Module table (4 changes) + SAP + Oracle Fusion |
| 6 | W1S3-002 H2H Core | Medium | Connectivity + approval model + bank list |
| 7 | W1S3-010 Monitoring | Medium | Module removal + monitoring section + connectivity |
| 8 | W1S3-008 Architecture | High | API architecture rewrite + diagram + module removals |
| 9 | W1S3-006 ERP Integration | High | Acumatica section write + SAP statement + module removals |
| 10 | W1S3-005 International and Forex Payments | High (authoring) | New content from confirmed baseline; module name confirmed |

---

## Pending Items for Re-escalation to BU Lead

*BQ7 is resolved. The following items are non-blocking enhancements only.*

| Item | Description | Files affected |
|---|---|---|
| BQ-WEB-04 | SAP integration architecture detail | W1S3-006 (SAP section only) |
| BQ-WEB-02 | Disaster Recovery module or hosting feature? | W1S3-008, W1S3-009 |
| BQ-WEB-01 | R6 billion transactions/month — authorised for tender use? | W1S1-005 (future), W1S3-001 |
| BQ-WEB-03 | Sage ERP integration scope | W1S1-005 (future), W1S3-001, W1S3-006 |
| CORP-01 | appsolvegroup.com corporate relationship | HANDOVER.md, W1S1-008 future |

---

*See `SESSION_C_FACT_BASELINE.md` for the full authoritative baseline.*
*See `SESSION_C_IMPACT_ANALYSIS.md` for per-file change detail and risk analysis.*
*See `SESSION_A_CLOSEOUT.md` for the 8 review standards applied to each file.*
*See `FACT_RESOLUTION_REPORT.md` for the Session A validated fact baseline.*
