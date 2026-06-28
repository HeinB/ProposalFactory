# Session C — Approval Plan
**Prepared:** 2026-06-10
**Prepared by:** Claude (AI analysis — requires human review)
**Source:** SESSION_C_FACT_BASELINE.md | SESSION_C_IMPACT_ANALYSIS.md
**Status as at 2026-06-10:** **Session C is fully unblocked.** All 13 BU lead questions answered. 0 files blocked.

---

## Overall Readiness

| Metric | Value |
|---|---|
| Total files in scope | 10 |
| Files blocked | **0** |
| Files requiring authoring | 1 (W1S3-005) |
| Files requiring editing only | 9 |
| Files Approve-As-Is | 0 |
| Open items blocking approval | 0 |
| Estimated total editing effort | 10–14 hours |

**Session C is fully unblocked.** The last remaining question (BQ7 — module currency) was answered on 2026-06-10. No approvals are gated on any pending question. BQ-WEB items are enhancements only and do not block any file.

---

## Per-File Approval Plan

### W1S3-001 — Product Overview

| Attribute | Value |
|---|---|
| Current readiness | DIRECT |
| Can advance to Review_Required? | Yes — after module table edit |
| Expected approval outcome | Approve-With-Edits |
| Estimated effort | 30–45 min |
| Approval sequence | 5 |

**Remaining edits:**

1. Module table — remove Secure File Transfer (retired)
2. Module table — remove Automated Receipt Creation (retired)
3. Module table — add ABSA Proof of Payment Integration (with ABSA-specific note)
4. Module table — add International and Forex Payment Processing
5. ERP Compatibility — add Oracle Fusion Applications
6. ERP Compatibility — add SAP
7. Geographic framing — update to CMA / international where applicable

**Residual risk:** None — all facts confirmed.

**Notes:** File is December 2024 vintage. The module changes are the primary addition beyond previously planned edits. Module count remains 9. ABSA Proof of Payment must be clearly framed as bank-specific.

---

### W1S3-002 — Host-to-Host Banking Core Capability

| Attribute | Value |
|---|---|
| Current readiness | MODERNISE |
| Can advance to Review_Required? | Yes — after edits |
| Expected approval outcome | Approve-With-Edits |
| Estimated effort | 60–90 min |
| Approval sequence | 6 |

**Remaining edits:**

1. Replace all Connect Direct references with API / SFTP architecture description
2. Replace AP Level 1/2 and PAY Level 1/2 with flexible approval framework description throughout
3. Replace [UPDATE] bank list placeholder with confirmed 9-bank list; use "integrated with"
4. Expand Acumatica description to confirmed parity (Acumatica Payments + Cash Management; approval workflows in BeBanking)
5. Update geographic framing: CMA and international (remove "South African banks only")
6. Remove client reference parenthetical from Standard Bank citation

**Residual risk:** None.

---

### W1S3-003 — Supplier Payments

| Attribute | Value |
|---|---|
| Current readiness | MODERNISE |
| Can advance to Review_Required? | Yes — after single edit |
| Expected approval outcome | Approve-With-Edits (minimal) |
| Estimated effort | 15–30 min |
| Approval sequence | 2 |

**Remaining edits:**

1. Replace "AP Level 1" and "AP Level 2" with flexible approval framework description

**Residual risk:** None. AVS confirmed active. This is the simplest Session C file.

---

### W1S3-004 — Payroll Payments

| Attribute | Value |
|---|---|
| Current readiness | MODERNISE |
| Can advance to Review_Required? | Yes — after edits |
| Expected approval outcome | Approve-With-Edits |
| Estimated effort | 30–45 min |
| Approval sequence | 3 |

**Remaining edits:**

1. Replace "PAY Level 1" and "PAY Level 2" with flexible approval framework description
2. Replace "Oracle EBS Payroll module or equivalent" with confirmed language: BeBanking integrates with Acumatica Payments and Acumatica Cash Management for payroll processing; equivalent approval workflows across ERP platforms

**Residual risk:** None. ACB format retained as SA implementation detail.

---

### W1S3-005 — International and Forex Payment Processing

| Attribute | Value |
|---|---|
| Current readiness | ~~STRUCTURE ONLY~~ → **MODERNISE** |
| Can advance to Review_Required? | After authoring |
| Expected approval outcome | Approve-With-Edits (post-authoring) |
| Estimated effort | 90–120 min (authoring) |
| Approval sequence | 10 |

**Remaining work (authoring, not editing):**

The confirmed baseline (SESSION_C_FACT_BASELINE.md F-C-06, F-C-12) provides all facts. The content must be written from these facts.

1. Rename/retitle to align with confirmed module name: "International and Forex Payment Processing"
2. Author: Module overview — full international payment capability; SWIFT processing; end-to-end lifecycle
3. Author: Supported payment types — SWIFT outward payments; CMA-region payments; foreign currency payments
4. Author: Exchange rate management — multi-source: FNB, Andisa, ExchangeRate-API; client selects preferred source(s); distinguish from Automated Exchange Rates module
5. Author: Approval workflow section — flexible approval framework; configurable SOD for forex authorisation
6. Author: Bank connectivity — API-first; SFTP fallback; international integrations confirm cross-border capability (Citi Bank UK, Santander Chile)
7. Retain: Automated Exchange Rates section — confirm it describes the ERP rate loading function (separate from payment initiation)
8. Remove: STRUCTURE ONLY placeholder text

**Residual risk:** None factual — all content can be authored from the confirmed baseline. Effort is authoring, not research.

---

### W1S3-006 — ERP Integration

| Attribute | Value |
|---|---|
| Current readiness | MODERNISE (previously stalled — fully unblocked) |
| Can advance to Review_Required? | Yes — after edits + Acumatica section |
| Expected approval outcome | Approve-With-Edits |
| Estimated effort | 90–120 min |
| Approval sequence | 9 |

**Remaining edits:**

1. Replace all Connect Direct references with API / SFTP
2. Remove "Secure File Transfer Utility" from any component lists or diagrams
3. Remove or footnote IBY module reference (Oracle Fusion does not use IBY)
4. Add Oracle Fusion Applications to Oracle integration section
5. Write Acumatica integration section from confirmed baseline: Acumatica Payments + Acumatica Cash Management; local payments, forex payments, bank statement processing; BeBanking manages all approval workflows
6. Add brief SAP compatibility statement pending BQ-WEB-04 detail

**Residual risk:** SAP integration depth (BQ-WEB-04) is pending — the SAP section should state "SAP-compatible" only until full architecture detail is confirmed. This does not block approval.

**Split consideration:** If BQ-WEB-04 reveals that SAP integration architecture is substantially different, consider splitting into two files at review: W1S3-006a (Oracle + Acumatica) and W1S3-006b (SAP).

---

### W1S3-007 — Security

| Attribute | Value |
|---|---|
| Current readiness | MODERNISE |
| Can advance to Review_Required? | Yes — after edits |
| Expected approval outcome | Approve-With-Edits |
| Estimated effort | 30–45 min |
| Approval sequence | 1 |

**Remaining edits:**

1. Replace "Dedicated banking server with Connect Direct connectivity" with API-based architecture description
2. Update any AP Level 1/2 or PAY Level 1/2 references in security context to flexible approval framework
3. Add POPIA compliance section: "BeBanking is designed and operated in compliance with the Protection of Personal Information Act (POPIA)"
4. Add GDPR as roadmap: "GDPR compliance is on the BeBanking product roadmap"

**Residual risk:** None.

**High-value note:** POPIA confirmation makes this file immediately usable in government and financial sector tenders. Recommended as first file to approve.

---

### W1S3-008 — Technical Architecture

| Attribute | Value |
|---|---|
| Current readiness | MODERNISE |
| Can advance to Review_Required? | Yes — after rewrite |
| Expected approval outcome | Approve-With-Edits |
| Estimated effort | 90–120 min |
| Approval sequence | 8 |

**Remaining edits:**

1. Rewrite connectivity section: replace dedicated banking server / Connect Direct with BeBanking API integration layer; SFTP for banks without API
2. Remove "Secure File Transfer Utility" from architecture diagram and component descriptions
3. Update ASCII architecture diagram: "Connect Direct" → "API / SFTP Layer"; "Standard Bank" → "Bank H2H System"; remove Secure File Transfer Utility component
4. Add cloud ERP deployment topology: BeBanking supports both on-premise and cloud ERP configurations
5. Update ERP integration points table: add SAP, Oracle Fusion; remove IBY; remove Secure File Transfer Utility as component
6. Update geographic framing: CMA and international bank integration scope (Namibia, UK, Chile)

**Residual risk:** None factual. Complexity is editorial — the architecture facts are fully confirmed.

**Note:** SITA v1.06 Appendix 5.2 process flow diagram is now doubly irrelevant (architecture has fundamentally changed). A new API-model process flow diagram would be high-value for future Wave 2.

---

### W1S3-009 — Hosting and Deployment Model

| Attribute | Value |
|---|---|
| Current readiness | MODERNISE |
| Can advance to Review_Required? | Yes — after commercial rewrite |
| Expected approval outcome | Approve-With-Edits |
| Estimated effort | 45–60 min |
| Approval sequence | 4 |

**Remaining edits:**

1. Complete rewrite of the commercial/licensing section: remove Service Option / Software Option model; replace with Monthly subscription and Annual subscription; remove all once-off licence references
2. Add cloud ERP deployment section: BeBanking supports both on-premise ERP and cloud ERP client configurations
3. Apply D3-equivalent fix: "24x7x365 standby" → "24x7 monitoring capability with after-hours support services"

**Residual risk:** None.

---

### W1S3-010 — Monitoring and Automation

| Attribute | Value |
|---|---|
| Current readiness | MODERNISE |
| Can advance to Review_Required? | Yes — after edits |
| Expected approval outcome | Approve-With-Edits |
| Estimated effort | 45–60 min |
| Approval sequence | 7 |

**Remaining edits:**

1. Remove Automated Receipt Creation row from the 6-process automation table (retired module); table becomes 5 processes
2. Update bank statement import row: replace Connect Direct / Secure File Transfer reference with API / SFTP
3. Complete the monitoring section [UPDATE] placeholder: Payment approval reporting; transaction-level audit reporting; bank account maintenance approval reporting; operational monitoring and audit visibility
4. Update exchange rate source: "Supported sources include FNB, Andisa, and ExchangeRate-API — clients select their preferred source(s)"

**Residual risk:** None.

---

## Final Summary

### Files Ready for Immediate Review_Required Promotion
*(edits are minimal — single or two-point changes; can be edited and promoted in one session)*

| File | Edits | Estimated time |
|---|---|---|
| W1S3-003 Supplier Payments | Approval model only (1 edit) | 15–30 min |
| W1S3-004 Payroll Payments | Approval model + Acumatica payroll (2 edits) | 30–45 min |
| W1S3-007 Security | POPIA + GDPR + Connect Direct + approval model (4 targeted additions) | 30–45 min |

### Files Requiring Editing First
*(substantive edits required across multiple sections; advance after edits complete)*

| File | Primary edit scope | Estimated time |
|---|---|---|
| W1S3-001 Product Overview | Module table (4 changes) + ERP compatibility | 30–45 min |
| W1S3-002 H2H Core | Connectivity + approval model + bank list + Acumatica | 60–90 min |
| W1S3-009 Hosting Model | Commercial model rewrite + cloud + 24x7 | 45–60 min |
| W1S3-010 Monitoring | Module removal + monitoring section + connectivity | 45–60 min |
| W1S3-008 Architecture | Architecture rewrite + diagram + module removals | 90–120 min |
| W1S3-006 ERP Integration | Acumatica section write + module/connectivity edits | 90–120 min |

### Files Requiring Authoring First
*(new content must be written from confirmed baseline before advancing)*

| File | Work required | Estimated time |
|---|---|---|
| W1S3-005 International and Forex Payment Processing | Full content authoring from confirmed baseline | 90–120 min |

### Files Blocked

**None.** All 13 BU lead questions are answered. Session C is fully unblocked.

### Files Expected to be Approve-As-Is

**None.** Every file requires at least one substantive edit (minimum: approval model update). No file can be promoted without at least one confirmed change.

### Files Expected to be Approve-With-Edits

**All 10 files** are expected to be approved with edits. The scope of edits ranges from a single approval model paragraph (W1S3-003) to a full content authoring (W1S3-005).

---

## Approval Sequence — Consolidated

| Order | File | Category | Effort | Rationale |
|---|---|---|---|---|
| 1 | W1S3-007 Security | Edit | 30–45 min | POPIA; highest standalone tender value; fewest dependencies |
| 2 | W1S3-003 Supplier Payments | Edit | 15–30 min | Simplest file; single edit |
| 3 | W1S3-004 Payroll Payments | Edit | 30–45 min | Two edits; all facts confirmed |
| 4 | W1S3-009 Hosting Model | Edit | 45–60 min | Commercial rewrite is clean and well-defined |
| 5 | W1S3-001 Product Overview | Edit | 30–45 min | Module table is the new element; then straightforward |
| 6 | W1S3-002 H2H Core | Edit | 60–90 min | Multiple edits; all facts confirmed |
| 7 | W1S3-010 Monitoring | Edit | 45–60 min | Module removal + monitoring completion |
| 8 | W1S3-008 Architecture | Edit | 90–120 min | Most architecturally intensive; all facts confirmed |
| 9 | W1S3-006 ERP Integration | Edit + author | 90–120 min | Acumatica section needs authoring; SAP statement |
| 10 | W1S3-005 Forex / Intl Payments | Author | 90–120 min | Full content authoring; do last to allow other files to establish patterns |

**Total estimated effort:** 10–14 hours across all 10 files.

---

## Pending Items (non-blocking)

The following items remain open but do not block any Session C approval. Raise with BU lead in the next available session.

| Item | Description | Affects | Notes |
|---|---|---|---|
| BQ-WEB-04 | SAP integration architecture detail | W1S3-006 (SAP section) | Brief compatibility statement added pending full detail |
| BQ-WEB-02 | Disaster Recovery module vs. hosting feature | W1S3-008, W1S3-009 | Enhancement — not a current gap |
| BQ-WEB-01 | R6 billion transactions/month for tender use | W1S1-005 future, W1S3-001 | High-value statistic if confirmed |
| BQ-WEB-03 | Sage ERP integration scope | W1S1-005 future, W1S3-001, W1S3-006 | Would add a 5th ERP platform if confirmed |
| CORP-01 | appsolvegroup.com corporate relationship | HANDOVER.md, W1S1-008 | Corporate question; not Session C scope |

---

*See `SESSION_C_FACT_BASELINE.md` for the authoritative product baseline.*
*See `SESSION_C_IMPACT_ANALYSIS.md` for per-file change detail.*
*See `SESSION_C_REVIEW_WORKBOOK.md` for BU lead question log.*
