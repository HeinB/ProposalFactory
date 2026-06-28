# Session C — BU Lead Response Impact Analysis
**Prepared:** 2026-06-10 | **Updated:** 2026-06-10 (BQ7 confirmed)
**Prepared by:** Claude (AI analysis — requires human review)
**Source:** SESSION_C_FACT_BASELINE.md (BU lead responses BQ1–BQ13 + BQ7 confirmed 2026-06-10)
**Purpose:** Document what changes in each W1S3 candidate file following BU lead confirmation. Identify what can proceed, what needs content work, and what readiness ratings have changed.
**Status:** Pre-approval analysis only. All 13 questions answered. No files blocked. No Session A content modified.

---

## Executive Summary

All 13 BU lead questions are now confirmed. Session C is **fully unblocked**.

- **1 file** elevated from STRUCTURE ONLY to MODERNISE (W1S3-005 — Forex Payments)
- **1 file** elevated from "Return to Candidate" to MODERNISE — actionable (W1S3-006 — ERP Integration)
- **9 files** MODERNISE with specific, bounded edits fully defined
- **9 files** can advance to Review_Required once edits are applied
- **1 file** requires content authoring before advancing (W1S3-005)
- **0 files** blocked

**BQ7 impact (confirmed 2026-06-10):**
- 2 modules confirmed retired: Secure File Transfer; Automated Receipt Creation
- 2 modules confirmed added: ABSA Proof of Payment Integration; International and Forex Payment Processing
- Net module count unchanged at 9
- Affects W1S3-001 (module table), W1S3-005 (module name), W1S3-008 (Secure File Transfer from architecture), W1S3-010 (Automated Receipt Creation from automation table)

**Biggest structural change:** Connect Direct → API/SFTP affects 6 files. This is a wholesale architecture replacement, not a minor update.

**Biggest content elevation:** W1S3-005 transforms from a structural placeholder to a substantive product capability file requiring new content authoring. Module name confirmed: "International and Forex Payment Processing."

**Key discovery from BQ4 + BQ7:** BeBanking is deployed across the CMA region (South Africa, Namibia, Lesotho, Eswatini) and internationally (UK, Chile). All Session C files should use CMA/international framing rather than South African banking framing.

---

## Readiness Rating Changes

| File | Previous rating | New rating | Change | Reason |
|---|---|---|---|---|
| W1S3-001 | DIRECT | DIRECT | No change | Dec 2024 source; module table edit required (BQ7) |
| W1S3-002 | MODERNISE | MODERNISE | No change | Edits fully defined and bounded |
| W1S3-003 | MODERNISE | MODERNISE | No change | Minor; all blockers resolved |
| W1S3-004 | MODERNISE | MODERNISE | No change | Acumatica payroll scope confirmed |
| **W1S3-005** | **STRUCTURE ONLY** | **MODERNISE** | **Elevated** | Full forex capability confirmed; module name confirmed; content to be written from baseline |
| W1S3-006 | MODERNISE (stalled) | MODERNISE (actionable) | Unblocked | Acumatica section has confirmed baseline; no longer "Return to Candidate" |
| W1S3-007 | MODERNISE | MODERNISE | No change | Edits defined |
| W1S3-008 | MODERNISE | MODERNISE | No change | Architecture rewrite scope confirmed; Secure File Transfer retired |
| W1S3-009 | MODERNISE | MODERNISE | No change | Commercial model rewrite defined |
| W1S3-010 | MODERNISE | MODERNISE | No change | Monitoring gap resolved; Automated Receipt Creation to be removed |

---

## Approval Readiness by File

| File | Can advance to Review_Required? | Remaining blockers |
|---|---|---|
| W1S3-001 | **Yes** | Module table update required (BQ7: 2 retired, 2 added); then advance |
| W1S3-002 | **Yes** | All blockers resolved |
| W1S3-003 | **Yes** | None |
| W1S3-004 | **Yes** | None |
| W1S3-005 | **Authoring required first** | Full file content must be written from confirmed baseline; no source document |
| W1S3-006 | **Yes — Acumatica section must be written** | Acumatica section requires new content (confirmed baseline available via BQ5) |
| W1S3-007 | **Yes** | None |
| W1S3-008 | **Yes — architecture rewrite required** | Connectivity architecture (API model) requires significant section rewrite; Secure File Transfer removal |
| W1S3-009 | **Yes — commercial section must be rewritten** | Commercial model complete rewrite required |
| W1S3-010 | **Yes** | Automated Receipt Creation must be removed from automation table |

---

## Per-File Impact Analysis

---

### W1S3-001 — Product Overview

**Previous status:** Approve with edit — SAP and Oracle Fusion confirmed; BQ7 (module currency) was pending

**BQ7 impact:** Module table in W1S3-001 must be updated. The file was sourced from December 2024 — most current in corpus — but the module composition has changed.

**Confirmed changes required:**

| Change | Source | Action |
|---|---|---|
| Remove Secure File Transfer from module table | BQ7 — retired | Delete row |
| Remove Automated Receipt Creation from module table | BQ7 — retired | Delete row |
| Add ABSA Proof of Payment Integration | BQ7 — new module | Add row: "ABSA Proof of Payment Integration — ABSA-specific proof of payment document retrieval and archiving" |
| Add International and Forex Payment Processing | BQ7 — new module | Add row: "International and Forex Payment Processing — SWIFT and foreign currency payment processing with multi-source exchange rate management" |
| Add SAP to ERP Compatibility | SAP confirmed (F-C-01) | Edit ERP Compatibility section |
| Add Oracle Fusion to ERP Compatibility | BQ6 confirmed | Already flagged; confirmed |
| CMA and international framing | BQ7 + BQ4 | Update geographic framing where relevant |

**Risk removed:** Module table now matches the confirmed 2026 product. Citing retired modules (Secure File Transfer, Automated Receipt Creation) in a tender could cause confusion if a prospect asks about capabilities that no longer exist.

**Note on ABSA Proof of Payment:** This module is bank-specific. The description should indicate it is available to ABSA-integrated clients, not universally.

**Note on module count:** Both the old and new tables have 9 modules. The count is unchanged; the composition has changed.

**Can proceed:** Yes — module table update is well-defined. All other edits are confirmed.

**Rating:** DIRECT — unchanged.

---

### W1S3-002 — Host-to-Host Banking Core Capability

**Previous status:** All blockers resolved. BQ7 did not add new edits to this file.

**Confirmed changes required:**

| Change | Source | Old content | New content |
|---|---|---|---|
| Connectivity | BQ1 (F-C-03) | "Connect Direct" throughout | "API-based connectivity; SFTP for banks without API endpoints" |
| Approval model | BQ2 (F-C-04) | AP Level 1/2 and PAY Level 1/2 | Flexible approval framework — unlimited levels, first-responder and voting modes, configurable SOD |
| Bank list | BQ4 (F-C-02) | "[UPDATE] — Standard Bank only confirmed" | Full 9-bank list with "integrated with" wording |
| Acumatica workflow | BQ5 (F-C-05) | "Oracle EBS or Acumatica" at step 1 only | Full Acumatica parity confirmed |
| Geographic framing | BQ4 + BQ7 | "South African banks" | CMA and international framing |
| Parenthetical client reference | Style | "(used in multiple implementations)" | Remove |

**Risks removed:** Stale connectivity, incomplete bank list, Oracle-only workflow description.

**Can proceed:** Yes.

**Rating:** MODERNISE — unchanged.

---

### W1S3-003 — Supplier Payments

**Previous status:** All blockers resolved. BQ7 did not add new edits.

**Confirmed changes required:**

| Change | Source | Action |
|---|---|---|
| Approval model | BQ2 (F-C-04) | Replace "AP Level 1" and "AP Level 2" with flexible approval framework description |
| AVS | BQ8 (F-C-08) | Confirmed active — no change needed |

**Risks removed:** Stale approval model language.

**Can proceed:** Yes. This is the simplest W1S3 file.

**Rating:** MODERNISE — unchanged.

---

### W1S3-004 — Payroll Payments

**Previous status:** All blockers resolved. BQ7 did not add new edits.

**Confirmed changes required:**

| Change | Source | Action |
|---|---|---|
| Approval model | BQ2 (F-C-04) | Replace "PAY Level 1" and "PAY Level 2" with flexible approval framework |
| ERP payroll scope correction | BQ5 clarification (F-C-05) | Replace "Oracle EBS Payroll module or equivalent" with: Oracle EBS and Oracle Fusion Applications. Note: Acumatica does not provide payroll functionality in South Africa. Remove any Acumatica payroll references from this file. |

**Note on ACB:** ACB format is the South African Automated Clearing Bureau payroll file format. This applies to Oracle EBS and Oracle Fusion payroll implementations only. Acumatica does not provide payroll functionality in South Africa and does not generate ACB payroll files.

**Can proceed:** Yes.

**Rating:** MODERNISE — unchanged.

---

### W1S3-005 — Forex Payments / International and Forex Payment Processing

**Previous status:** STRUCTURE ONLY → MODERNISE (elevated when BQ11 confirmed)

**BQ7 impact:** The confirmed module name is "International and Forex Payment Processing." The file title and content should align with this name. Automated Exchange Rates remains a separate module — W1S3-005 covers the international/SWIFT payment capability, not the exchange rate loading functionality (which sits in W1S3-010).

**⚑ READINESS ELEVATED: STRUCTURE ONLY → MODERNISE**

**Confirmed module name:** International and Forex Payment Processing

**Recommend retitling candidate file to:** `W1S3-005-BB-InternationalForexPayments-DRAFT.md`

**What was in the file:** Automated Exchange Rates section (confirmed) + STRUCTURE ONLY placeholder (forex processing unconfirmed).

**Revised content to be authored:**

| Section | Content required | Source |
|---|---|---|
| Module overview | "International and Forex Payment Processing" — full international payment capability; SWIFT processing; end-to-end payment lifecycle | F-C-06, F-C-12 |
| Supported payment types | SWIFT outward payments; foreign currency payments; CMA region payments | BU baseline |
| Exchange rate management | Multi-source rate loading; FNB, Andisa, ExchangeRate-API; client selects preferred source(s) | F-C-06 |
| Approval workflow | Flexible approval framework applies; configurable SOD controls for forex authorisation | F-C-04 |
| Bank connectivity | API-first; SFTP fallback; international integrations (Citi Bank UK, Santander Chile) confirm cross-border capability | F-C-03, F-C-02 |
| Note on Automated Exchange Rates | Distinguish from the separate "Automated Exchange Rates" module — this module handles payment initiation; the other handles ERP rate loading | F-C-12 |

**Risks removed:** Capability scope unknown → confirmed; file unadvanceable → authoring path defined.

**Can proceed:** Content authoring required before advancing to Review_Required.

**Rating:** STRUCTURE ONLY → **MODERNISE**.

---

### W1S3-006 — ERP Integration

**Previous status:** Unblocked. BQ7 did not add new edits beyond Secure File Transfer retirement.

**BQ7 impact:** Any reference to "Secure File Transfer Utility" as an ERP integration component must be removed. The API layer replaces it.

**Confirmed changes required:**

| Change | Source | Action |
|---|---|---|
| Connectivity | BQ1 (F-C-03) | Replace all Connect Direct references with API/SFTP |
| Remove Secure File Transfer component | BQ7 (F-C-12) | Remove "Secure File Transfer Utility" from any integration diagrams or component lists |
| Acumatica section | BQ5 (F-C-05) | Write from confirmed baseline: Acumatica Payments + Cash Management; local, forex, bank statement processing; BeBanking manages approvals |
| Oracle Fusion | BQ6 (F-C-07) | Add Oracle Fusion Applications to Oracle integration section |
| SAP | SAP confirmed (F-C-01) | Brief SAP compatibility statement pending BQ-WEB-04 detail |
| IBY module | Prior recommendation | Remove or footnote — Oracle Fusion does not use IBY |

**Split consideration:** If SAP integration architecture is materially different, consider splitting into W1S3-006a (Oracle + Acumatica) and W1S3-006b (SAP). Raise with BU lead when BQ-WEB-04 is answered.

**Can proceed:** Yes.

**Rating:** MODERNISE — unchanged (but fully unblocked).

---

### W1S3-007 — Security

**Previous status:** All blockers resolved. BQ7 did not add new edits.

**Confirmed changes required:**

| Change | Source | Action |
|---|---|---|
| Connect Direct | BQ1 (F-C-03) | Replace "Dedicated banking server with Connect Direct connectivity" with API-based description |
| Approval model | BQ2 (F-C-04) | Update any Level 1/2 references to flexible approval framework |
| POPIA | BQ13 (F-C-11) | Add POPIA compliance statement |
| GDPR | BQ13 (F-C-11) | Add as roadmap: "GDPR compliance is on the BeBanking product roadmap" |

**High-value outcome:** POPIA confirmation makes this file directly usable in government and financial sector tenders.

**Can proceed:** Yes.

**Rating:** MODERNISE — unchanged.

---

### W1S3-008 — Technical Architecture

**Previous status:** All blockers resolved. BQ7 adds Secure File Transfer retirement impact.

**BQ7 impact:** "Secure File Transfer" was the component that described the dedicated banking server's file transfer mechanism. With the module retired and the API layer now standard, this component should be removed and replaced with the API layer description.

**Confirmed changes required:**

| Change | Source | Action |
|---|---|---|
| Connectivity architecture | BQ1 (F-C-03) | **Major rewrite.** Connect Direct / dedicated banking server → BeBanking API integration layer; SFTP where bank has no API |
| Architecture diagram | BQ1 + BQ7 | Update ASCII diagram: "Connect Direct" → "API / SFTP Layer"; "Standard Bank" → "Bank H2H System"; remove "Secure File Transfer Utility" component |
| Cloud ERP | BQ3 (F-C-01) | Add cloud ERP deployment topology |
| ERP table | F-C-01, F-C-12 | Add SAP and Oracle Fusion; remove IBY; remove Secure File Transfer Utility as a listed component |
| CMA/international framing | BQ4 + BQ7 | Reflect CMA reach and international bank integrations |

**Note on Appendix 5.2:** The SITA v1.06 PDF process flow diagram is now doubly irrelevant — the architecture has fundamentally changed. A new API-model process flow would have substantially higher value.

**Can proceed:** Yes.

**Rating:** MODERNISE — unchanged.

---

### W1S3-009 — Hosting and Deployment Model

**Previous status:** All blockers resolved. BQ7 did not add new edits to this file.

**Confirmed changes required:**

| Change | Source | Action |
|---|---|---|
| Commercial model | BQ9 (F-C-09) | **Complete rewrite.** Remove Service Option / Software Option. Replace: Monthly subscription; Annual subscription. No once-off licence. |
| Cloud deployment | BQ3 (F-C-01) | Add: BeBanking supports both on-premise and cloud ERP configurations |
| 24x7x365 | D3-equivalent | Apply: "24x7 monitoring capability with after-hours support services" |

**Can proceed:** Yes.

**Rating:** MODERNISE — unchanged.

---

### W1S3-010 — Monitoring and Automation

**Previous status:** All blockers resolved. BQ7 adds Automated Receipt Creation retirement impact.

**BQ7 impact:** "Automated Receipt Creation" was listed as one of the 6 processes in the automation table. It is retired. Remove it — the automation table reduces from 6 processes to 5 processes.

**Confirmed changes required:**

| Change | Source | Action |
|---|---|---|
| Remove Automated Receipt Creation row | BQ7 (F-C-12) | Delete row from the 6-process automation table. Automation table becomes 5 processes. |
| Connect Direct in automation table | BQ1 (F-C-03) | Update bank statement import row: API / SFTP |
| Monitoring section | BQ10 (F-C-10) | **Complete the [UPDATE] placeholder:** Payment approval reporting; transaction-level audit reporting; bank account maintenance approval reporting; operational monitoring and audit visibility |
| Exchange rate source | BQ12 (F-C-06) | "Supported sources include FNB, Andisa, and ExchangeRate-API — clients select their preferred source" |

**Risk removed:** Citing a retired module in the automation table corrected; monitoring gap resolved.

**Can proceed:** Yes.

**Rating:** MODERNISE — unchanged.

---

## Cross-File Changes Required

| Change | Files affected | Description |
|---|---|---|
| Connect Direct → API/SFTP | W1S3-002, 006, 007, 008, 010 | All references to Connect Direct must be replaced (F-C-03) |
| AP/PAY Level 1/2 → flexible approval framework | W1S3-002, 003, 004, 007 | All historical approval level references updated (F-C-04) |
| CMA/international framing | W1S3-001, 002, 006, 008 | Remove "South African banking" framing; add CMA and international scope |
| SAP added to ERP platforms | W1S3-001, 006 | ERP compatibility lists updated (F-C-01) |
| Oracle Fusion confirmed | W1S3-001, 006 | Oracle Fusion Applications in all ERP lists |
| **Secure File Transfer — remove** | **W1S3-001, 006, 008** | **Retired module; remove from module table, component lists, architecture** |
| **Automated Receipt Creation — remove** | **W1S3-001, 010** | **Retired module; remove from module table and automation table** |
| **ABSA Proof of Payment — add** | **W1S3-001** | **New module; add to module table in W1S3-001** |
| **International and Forex Payment Processing — add** | **W1S3-001** | **New/renamed module; add to module table; use as confirmed name in W1S3-005** |

---

## Risks Removed — Complete Record

| Risk | Previous status | Resolved by |
|---|---|---|
| Connect Direct cited as current architecture | Would have caused credibility failure with technical evaluators | BQ1 — API/SFTP confirmed |
| AP/PAY Level 1/2 described as current | Would have conflicted with client's actual governance setup | BQ2 — flexible framework confirmed |
| Bank list incomplete — only Standard Bank | Would have undermined credibility for multi-bank clients | BQ4 — 9-bank list confirmed |
| Acumatica integration undocumented | Acumatica tenders could not be supported by W1S3 content | BQ5 — integration scope confirmed |
| Forex capability unknown — STRUCTURE ONLY | BeBanking's international payments story was entirely missing | BQ11 — full forex capability confirmed |
| Commercial model obsolete — once-off licence | Would have caused confusion in commercial negotiations | BQ9 — subscription model confirmed |
| POPIA not mentioned in security documentation | Missing from compliance-critical sections | BQ13 — POPIA confirmed |
| AVS currency unknown | Core supplier verification unconfirmed | BQ8 — confirmed active |
| Module list unconfirmed (BQ7) | Could have cited retired modules (Secure File Transfer, Automated Receipt Creation) in live tenders | BQ7 — module list confirmed; 2 retired, 2 added |

---

## Remaining Open Items

| Item | Description | Files affected | Path to resolution |
|---|---|---|---|
| BQ-WEB-04 | SAP integration architecture and scope | W1S3-006 | Re-raise with BU lead. Add brief SAP statement to W1S3-006 pending full detail. Does not block approval. |
| BQ-WEB-02 | Disaster Recovery module scope | W1S3-008, W1S3-009 | Re-raise with BU lead. Does not block current approvals. |
| BQ-WEB-01 | R6 billion transactions/month statistic | W1S1-005 (future), W1S3-001 | Re-raise. Enhancement only — does not block. |
| BQ-WEB-03 | Sage ERP integration scope | W1S1-005 (future), W1S3-001, W1S3-006 | Re-raise. Enhancement only — does not block. |
| CORP-01 | appsolvegroup.com relationship | HANDOVER.md (future) | Hein Blignaut to confirm. Not Session C scope. |

**None of the remaining open items block any Session C approval.**

---

## Recommended Approval Sequence (final)

| Order | File | Edits required | Complexity | Notes |
|---|---|---|---|---|
| 1 | W1S3-007 Security | POPIA add; Connect Direct; approval model | Low | High tender value; standalone compliance value |
| 2 | W1S3-003 Supplier Payments | Approval model only | Very low | Simplest file |
| 3 | W1S3-004 Payroll Payments | Approval model; Acumatica payroll | Low | |
| 4 | W1S3-009 Hosting Model | Commercial rewrite; cloud; 24x7 fix | Low-Medium | Commercial section is a clean rewrite |
| 5 | W1S3-001 Product Overview | Module table (2 retired, 2 added); SAP; Oracle Fusion | Medium | Module changes add to previous edits |
| 6 | W1S3-002 H2H Core | Connectivity; approval model; bank list; Acumatica | Medium | Multiple targeted edits throughout |
| 7 | W1S3-010 Monitoring | Remove Automated Receipt Creation; complete monitoring section; connectivity | Medium | Module retirement adds to previous edits |
| 8 | W1S3-008 Architecture | API architecture rewrite; remove Secure File Transfer; diagram; cloud | High | Most structurally intensive edit |
| 9 | W1S3-006 ERP Integration | Acumatica section write; remove Secure File Transfer; SAP statement; connectivity | High | Acumatica section requires authoring |
| 10 | W1S3-005 Forex / International Payments | Full content authoring from confirmed baseline | High (authoring) | Only file requiring new content; do last |
