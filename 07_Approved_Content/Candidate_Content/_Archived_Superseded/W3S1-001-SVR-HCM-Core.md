---
document_id: W3S1-001-SVR-HCM-Core
title: "Source Validation Report — W3S1-001 Oracle HCM Core Global HR and Employee Lifecycle"
version: "1.0"
created: "2026-06-12"
created_by: "Claude (AI — Wave 3 W3S1-001 source validation)"
status: "Source Validation — Awaiting BU Lead Review Before Extraction"
business_unit: "Oracle"
wave: "3"
deliverable: "W3S1-001"
purpose: "Pre-extraction source validation. Do not begin drafting until this report is reviewed."
---

# Source Validation Report — W3S1-001
## Oracle HCM Core — Global HR and Employee Lifecycle

**Date:** 2026-06-12 | **Wave:** 3 | **Deliverable:** W3S1-001  
**Status:** Source validation complete — BU lead review required before extraction begins

---

## 1. Source Summary

| HIST | Document | Tier | Usable for W3S1-001 | Notes |
|---|---|---|---|---|
| HIST-007 | Hollywood Bets V5.0 ACCEPTED proposal | Implementation Evidence | **Yes — primary** | Phase 3.3.1 directly maps to HCM Core scope. Go-live July 2025. 7,000 users. |
| HIST-015 | Afrocentric HCM Proposal V4.0 | Implementation Evidence | **Yes — primary** | Phase 3.3.1 directly maps. Full assumption set for SA deployments. |
| HIST-006 | SAA HCM RFP Response | Capability/Corroborating | **Yes — corroborating** | Section 2 HCM Base Cloud overview. Must not be used as implementation evidence. |
| HIST-017 | SAA Additional Information | Capability/Corroborating | **Conditional** | Not yet read — flag for secondary pass if more HCM Core detail needed. |
| HIST-016 | SABS ETS Response | Reference evidence | **Yes — client list** | Confirms Mr Price (T&L + HCM) and Hollywood Bets as HCM clients. |
| CCBA (HIST-014) | CCBA Oracle HCM Solution V2.0 | Restricted | **Limited** | May use for extraction support; must never name CCBA in output. |

---

## 2. Confirmed Bill of Materials — W3S1-001 Scope

Scope confirmed across HIST-007 and HIST-015. The following modules are in scope for W3S1-001 Oracle HCM Core:

### 2.1 Confirmed in Hollywood Bets ACCEPTED Proposal (HIST-007)

Source: BOM, Phase 3.3.1, Implementation Approach.

| Module / Capability | Source Quote / Evidence | Extraction Quality |
|---|---|---|
| **Fusion HCM Base Cloud Service** | HIST-007 BOM: "Fusion Human Capital Management Base Cloud Service" | H — direct BOM line |
| **Core HR foundations** | HIST-007 Phase 3.3.1: "This is the foundation for the rest of the project. It establishes the common structures used by all subsequent modules." | H — phase description |
| **Absence Management** | HIST-007 Phase 3.3.1: "critical, and most used functionality such as absence management" | H — implementation evidence |
| **Employee Self-Service** | HIST-007 Phase 3.3.1: "self-service access to maintain personal records" | H — implementation evidence |
| **OIC integration to 3rd party payroll** | HIST-007 BOM: "Integration to 3rd party payroll — Integration to be done Utilising Oracle Integration Cloud Service" | H — confirmed integration architecture |
| **OUM methodology** | HIST-007: "The Oracle Unified Methodology (OUM) will be adhered to within the scope of APPSolve's applications project engagement responsibility." | H — methodology basis |
| **Hyper-care support model** | HIST-007: "3 months of hyper care with a full complement of senior resources available to assist with use and design adjustments or bug fixes" | H — post-go-live model |
| **Data management approach** | HIST-007: "where there are significant volumes of data to be migrated, we assist with preparing the content (general cleaning and normalisation) and mapping content into templates" | M — delivery approach |
| **User interface / Look and Feel** | HIST-007: "we prefer that your marketing, brand ambassadors, intranet and web site designers help to develop an appropriate colour scheme and style" | M — optional delivery item |

### 2.2 Confirmed in Afrocentric HCM Proposal V4.0 (HIST-015)

Source: Phase 3.3.1, General Assumptions, Specific Assumptions.

| Module / Capability | Source Quote / Evidence | Extraction Quality |
|---|---|---|
| **Core HR foundation** | HIST-015 Phase 3.3.1: "This is the foundation for the rest of the project. It establishes the common structures used by all subsequent modules." | H — mirrors HB; independent confirmation |
| **Absence Management** | HIST-015 Phase 3.3.1: "most used functionality such as absence management" | H — confirmed in scope |
| **Self-Service** | HIST-015 Phase 3.3.1: "self-service access to maintain personal records" | H — confirmed |
| **SA-specific deployment model** | HIST-015 Specific Assumptions: "Only South African operations have been included in the deployment of all listed modules." | H — SA delivery model |
| **Shared services model** | HIST-015: "AFROCENTRIC will be utilising a central shared services model for all HR Related activities" | H — delivery pattern |
| **Active employees only** | HIST-015: "We only migrate records for active employees." | H — data migration scope rule |
| **Legislative fields** | HIST-015: "Only legislative required fields will be defined." | H — configuration approach |
| **Data templates** | HIST-015: "Data for migration will be prepared and owned by the client. APPSolve to provide the templates for data only." | H — RACI pattern |
| **Time and Labor integration** | HIST-015 Phase 3.3.4: "The only integrations in scope would be for a time logging/access control solution and a Payroll solution." | M — T&L-specific note |
| **Critical care post go-live** | HIST-015: "We advise after each phase a critical care period. This should be allocated about 280 hours per phase." | M — support model |

### 2.3 Corroborating Evidence — SAA HCM RFP (HIST-006)

**Rule:** SAA is not implementation evidence. Use for product capability context only. Reframe all Oracle product claims as APPSolve delivery capability.

| Module | SAA Section 2 Description | Extraction Use |
|---|---|---|
| **HCM Base Cloud** | "Oracle Fusion Human Capital Management (HCM) is a comprehensive suite of cloud-based applications designed to help organizations manage their workforce effectively. Oracle Cloud HCM supports multi-country, multi-currency, and multi-language operations." | Corroborating platform description. Reframe: APPSolve configures and implements the Oracle Fusion HCM platform... |
| **Multi-country support** | SAA Section 2: "supports multi-country, multi-currency, and multi-language operations, making it ideal for businesses expanding into new markets" | Use as platform benefit claim. |
| **Quarterly updates** | SAA Section 2: "benefits from regular, automatic updates that include new features, enhancements, and compliance with changing regulations" | Use as platform benefit — SaaS model advantage. |
| **AI-Based Skills** | ORACLE_FACT_BASELINE Section 4.1: confirmed in SAA Section 2 | Corroborating — no independent implementation proof. Flag as platform capability. |
| **Workforce Directory / Modelling** | ORACLE_FACT_BASELINE Section 4.1: confirmed in SAA Section 2 | Corroborating — no independent implementation proof. Flag as platform capability. |
| **Work Life** | ORACLE_FACT_BASELINE Section 4.1: confirmed in SAA Section 2 | Corroborating — no independent implementation proof. Flag as platform capability. |
| **Benefits** | ORACLE_FACT_BASELINE Section 4.1: confirmed in SAA Section 2 | Corroborating — no independent implementation proof. Flag as platform capability. |
| **Journeys** | ORACLE_FACT_BASELINE Section 4.1: confirmed in SAA Section 2 | Corroborating — no independent implementation proof. Flag as platform capability. |

---

## 3. Claim Classification Matrix

Every claim in the extracted document must be classifiable as one of:

| Class | Definition | Approved phrase pattern |
|---|---|---|
| **Implemented** | Confirmed in HIST-007 (HB accepted, go-live July 2025) or HIST-015 (Afrocentric proposal) | "APPSolve has implemented...", "APPSolve configures and deploys..." |
| **Platform capability** | Confirmed in SAA/CCBA proposals (corroborating) but not in an ACCEPTED proposal or go-live | "Oracle Fusion HCM enables...", "APPSolve configures the platform to..." |
| **Standard methodology** | Delivery approach confirmed across multiple proposals (HB and Afrocentric) | "APPSolve's standard implementation approach includes..." |

**Rule (F-W3-001 closed):** All Oracle HCM modules are confirmed as implemented by APPSolve. Claim Class = Implemented for all modules. However: corroborating-only modules (AI-Based Skills, Workforce Directory/Modelling, Work Life, Benefits, Journeys) may be described as implemented but the drafting must not cite a specific client for these — use generic "enterprise clients."

---

## 4. Governance Corrections — Source Documents Contain Outdated Facts

The following outdated facts appear in HIST-015 (Afrocentric V4.0) and must NOT be extracted. Replace with approved values from ORACLE_FACT_BASELINE.

| Source claim | Correction | Rule |
|---|---|---|
| "80 Senior Consultants" (HIST-015 line 18) | "50+ Senior Consultants" | ORACLE_FACT_BASELINE Section 13 |
| "APPSolve has been an Oracle Gold Partner for the past 13 years" (HIST-015 line 73) | "Oracle Level 1 Partner" | ORACLE_FACT_BASELINE Section 1 |
| "21 years" (HIST-015 line 12 implied) | "over 23 years" | ORACLE_FACT_BASELINE Section 13 |
| "sub-Sahara African market including... Nigeria... Uganda" + Bangladesh, Qatar (HIST-015 line 13) | Remove Nigeria, Uganda, Bangladesh, Qatar | F9 correction — no client folder evidence |
| "24x7x365" | "24x7 monitoring with after-hours support" | ORACLE_FACT_BASELINE Section 10 |
| "Oracle Unified Methodology (OUM)" (HIST-007) | Approved — retain as is | W2S1-005 confirms OUM basis |

---

## 5. Proposed Document Structure — W3S1-001

**Document ID:** W3S1-001-ORA-HCM-Core  
**File name:** `W3S1-001-ORA-HCMCore.md`  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`

### Proposed Sections

| Section | Content | Primary Source |
|---|---|---|
| **Section 1 — Overview** | APPSolve as Oracle Level 1 Partner; HCM practice overview; number of HCM go-lives; platform approach | HIST-007, HIST-015, ORACLE_FACT_BASELINE |
| **Section 2 — Oracle Fusion HCM Platform** | Platform architecture; SaaS model; multi-country capability; quarterly release cadence; OIC standard integration | HIST-006 (reframed), ORACLE_FACT_BASELINE Section 7 |
| **Section 3 — Core HR and Organisational Management** | Global HR foundation; organisational structures; position management; workforce directory; workforce modelling; hire-to-retire lifecycle | HIST-007 Phase 3.3.1, HIST-015 Phase 3.3.1, HIST-006 reframed |
| **Section 4 — Absence Management** | Leave types; absence rules; legislative compliance; integration with Time and Labor and Payroll | HIST-007 Phase 3.3.1, HIST-015 Phase 3.3.1 + Phase 3.3.4 note |
| **Section 5 — Employee Self-Service and Journeys** | Self-service portal; journeys; onboarding; life events; mobile access | HIST-007 Phase 3.3.1, HIST-006 reframed |
| **Section 6 — AI-Based Skills and Workforce Capability** | Skills management; workforce modelling; work life; benefits; AI-driven people insights | HIST-006 reframed; ORACLE_FACT_BASELINE Section 4.1 |
| **Section 7 — APPSolve Delivery Capability** | Go-live evidence; implementation team structure; reference clients (Hollywood Bets confirmed); multi-industry experience | HIST-007 (HB — go-live July 2025, 7,000 users), HIST-015 |
| **Section 8 — Implementation Approach** | OUM-based phases; Journey Prep through Support; hyper-care; data migration RACI; SA deployment model | HIST-007, HIST-015 (identical methodology) |
| **Section 9 — Integration Architecture** | OIC as standard integration layer; payroll system integration (SAP Payroll, PaySpace); biometric integration; HR system integration | HIST-007 BOM + Annexure 1, ORACLE_FACT_BASELINE Section 7 |
| **Section 10 — Risk Register** | Standard HCM core risks | New — governed by Wave 3 risk register rules |
| **Section 11 — Assumptions** | SA-first deployment; shared services model; active-only migration; standard reports | HIST-015 Specific Assumptions |
| **Section 17 — Approval Record and Pre-Tender Checks** | Standard governance section | Template from W2S1-005 |

---

## 6. Decision Register — W3S1-001

All Wave 3 BU lead decisions (F-W3-001 through F-W3-005) are CLOSED. No blocking decisions pending for W3S1-001.

| Decision ID | Decision | Status | Impact on W3S1-001 |
|---|---|---|---|
| F-W3-001 | APPSolve has implemented all Oracle HCM modules | CLOSED | All modules may be described as implemented. Use generic client framing for modules without a named reference. |
| F-W3-002 | Hollywood Bets confirmed and referenceable | CLOSED | Hollywood Bets may be named as a go-live HCM reference. Approved scope: Fusion HCM Base Cloud, Recruiting, Talent Management, Goal Management, Performance Management, Talent Review and Succession, Career Development. Go-live July 2025. 7,000 users. |
| F-W3-003 | SAA not awarded — capability evidence only | CLOSED | SAA must not be cited as a client or reference. SAA source content used for platform capability descriptions only. |
| F-W3-004 | CCBA source-only | CLOSED | CCBA content may be used for extraction support. CCBA must never appear in the approved document. |
| F-W3-005 | Reference letters in Tender Pack and Reference folders may be registered | CLOSED | Register applicable reference letters to `04_References/Oracle/` as part of Wave 3 governance. |

**Module-level decisions for W3S1-001 (from F-W3-001):**

| Module | Confirmed Implemented | Named Client Evidence | Notes |
|---|---|---|---|
| Global HR / Core HCM | Yes | Hollywood Bets (go-live Jul 2025) | Primary implementation reference |
| Absence Management | Yes | Hollywood Bets Phase 1 | Named reference available |
| Employee Self-Service | Yes | Hollywood Bets Phase 3.3.1 | Named reference available |
| AI-Based Skills | Yes (F-W3-001) | No named client in corpus | Use "enterprise clients" framing |
| Workforce Directory / Modelling | Yes (F-W3-001) | No named client in corpus | Use "enterprise clients" framing |
| Work Life | Yes (F-W3-001) | No named client in corpus | Use "enterprise clients" framing |
| Benefits Management | Yes (F-W3-001) | No named client in corpus | Use "enterprise clients" framing |
| Journeys / Onboarding | Yes (F-W3-001) | Hollywood Bets Annexure 1 (WSP/ATR — Journeys concept implicit) | Use HB for general self-service; Journeys framing from SAA |

---

## 7. Risk Register — W3S1-001

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-W3S1-001-01 | SAA source contains Oracle product-marketing language — risk of extracting Oracle feature descriptions as APPSolve delivery claims | High | High | Every paragraph from HIST-006 must be reframed to APPSolve delivery capability before extraction. Apply: "APPSolve implements/configures X" not "Oracle Fusion HCM does X." |
| R-W3S1-001-02 | Afrocentric outdated company stats (80 consultants, Gold Partner) — risk of importing prohibited facts | High | Medium | Corrections documented in Section 4 above. Apply all corrections before extraction. Do not source company profile content from HIST-015. |
| R-W3S1-001-03 | Modules without named client references (AI-Based Skills, Work Life, Benefits, Journeys, Workforce Directory/Modelling) — risk of overstating implementation evidence | Medium | Medium | Use "APPSolve has implemented [module] for enterprise clients across multiple industries" — no named client. |
| R-W3S1-001-04 | Hollywood Bets contact confirmation not yet in KB — reference not formally registered | Low | High | Pre-tender check: confirm HB account manager approval before citing HB in any live tender. Register as standing check PT-W1-001. |
| R-W3S1-001-05 | Afrocentric document is a fixed-price proposal for a single client — scope assumptions may be too narrow if reused verbatim | Medium | Low | Extract the methodology and platform capability — not the client-specific scope assumptions. Generalise SA delivery model from HIST-015. |

---

## 8. Assumptions Register — W3S1-001

The following assumptions are drawn from HIST-015 (Afrocentric) and are suitable for reuse as standard APPSolve delivery assumptions for Oracle HCM Core:

| Assumption ID | Assumption | Source |
|---|---|---|
| A-W1-001 | Implementation scope covers South Africa as the primary rollout jurisdiction; multi-country extensions are scoped separately. | HIST-015 |
| A-W1-002 | Client will adopt a central shared services model for HR activities in scope. | HIST-015 |
| A-W1-003 | Data migration is limited to active employees. Historical records are excluded unless separately scoped. | HIST-015 |
| A-W1-004 | Standard Oracle-delivered reports and dashboards will satisfy the client's initial reporting requirements. Custom reports are out of scope unless separately agreed. | HIST-015 |
| A-W1-005 | Integration to payroll is in scope; all other third-party integrations are out of scope unless separately agreed. | HIST-015 |
| A-W1-006 | Data preparation, extraction, cleaning, and formatting is the client's responsibility. APPSolve provides templates and data governance frameworks. | HIST-015 |
| A-W1-007 | Train-the-trainer delivery only; end-user training is the client's responsibility post knowledge transfer. | HIST-015 |
| A-W1-008 | Standard functionality will be used throughout. Customisation or development is out of scope unless separately agreed. | HIST-007, HIST-015 |

---

## 9. Extraction Readiness Assessment

| Check | Result |
|---|---|
| Primary implementation evidence identified (HIST-007, HIST-015) | ✅ Ready |
| Corroborating evidence identified (HIST-006) | ✅ Ready |
| Governance corrections documented (Section 4) | ✅ Ready |
| Claim classification matrix established (Section 3) | ✅ Ready |
| Proposed structure approved | ⚠️ Pending BU lead review |
| Decision register complete | ✅ All decisions CLOSED |
| Risk register complete | ✅ 5 risks documented |
| Assumptions register complete | ✅ 8 assumptions documented |
| ORACLE_FACT_BASELINE reviewed | ✅ Corrections applied in Section 4 |
| CCBA restriction noted | ✅ Source-only; never named in output |
| SAA restriction noted | ✅ Capability evidence only; not implementation proof |
| Pre-tender checks identified | ✅ HB reference confirmation (PT-W1-001) |

**Extraction status: READY pending BU lead review of proposed structure (Section 5).**

---

## 10. Source File Locations

| HIST | Full path |
|---|---|
| HIST-007 | `Parties/Customers/Hollywood Bets/RFP/HCM and Payroll Implementation/Accepted proposal/APPSolve_HollywoodBets_Oracle Implementation 3rd part_V5.0.docx` |
| HIST-015 | `Parties/Customers/Afrocentric Health/RFP/HCM 2023/APPSolve Afrocentric - HCM Proposal V4.0.docx` |
| HIST-006 | `Parties/Customers/South African Airways/HCM/1.Working/APPSolve_SAA_RFP.docx` |
| HIST-016 | `Parties/Customers/SABS/RFP/ETS - Oracle Fusion/APPSolve_SABS_RFP_Response.docx` |

---

*Source Validation Report prepared 2026-06-12 by Claude (AI) — no capability content extracted.*  
*Extraction begins only after BU lead confirms proposed structure in Section 5.*
