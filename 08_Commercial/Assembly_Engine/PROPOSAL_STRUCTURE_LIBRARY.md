---
document_id: PROPOSAL-STRUCTURE-LIBRARY
title: "Proposal Structure Library"
version: "1.0"
created: "2026-06-16"
created_by: "WP12 — Proposal Assembly Engine"
status: "Active"
---

# Proposal Structure Library

**Purpose:** Defines the standard section structure for each proposal type. For each section: content source, generation method, required human inputs, and governance checks.

**Generation methods:**
- **AUTO** — Content drawn directly from approved KB asset; minimal modification needed
- **HYBRID** — Approved KB asset is the foundation; customise for this client/tender
- **MANUAL** — Must be written specific to this engagement; no KB asset covers this section
- **PLACEHOLDER** — Section required but depends on commercial or client data not yet available

---

## Structure 1 — Oracle HCM Proposal

Standard for: HCM Full Suite, HCM Base, module-specific HCM tenders.

| # | Section | Source Asset(s) | Method | Human Input Required | Governance Checks |
|---|---|---|---|---|---|
| 1 | Cover Page / Title | Tender template | MANUAL | Client name, tender reference, date, APPSolve contact | None |
| 2 | Table of Contents | Auto-generated from DOCX headings | AUTO | Word TOC generation after all sections confirmed | None |
| 3 | Executive Summary | W1S1-001 + client-specific context | HYBRID | Client context; scope summary; commercial value proposition | No prohibited claims; no invented references; no unapproved headcounts |
| 4 | Company Profile | W1S1-001, W1S1-002, W1S1-006 | AUTO | Verify year counts are current (2002 = 24+ years as of 2026) | **CROSS-1**: 50+ consultants only. Remove Nigeria/Uganda/Ghana/Bangladesh/Qatar. No "19 years" — Hein career = since 1996. Remove 110+ headcount. |
| 5 | Oracle Partnership | W1S1-003 | AUTO | Annual OPN revalidation check | Level 1 only — NEVER cite Gold Partner. |
| 6 | Awards and Recognition | W1S1-006 | AUTO | Verify award claims with BU Lead; W1S1-001 award table | Award table: unrestricted. Success story URLs (Tiger Brands, USAID, UT Grain): pending verification — omit until confirmed. |
| 7 | Delivery Model | W1S1-007 | AUTO | None | 8 service lines. Monthly Recurring Invoice Model. 3 costing models. |
| 8 | Geographic Presence | W1S1-008 | AUTO | None | Use approved sub-Saharan list only (BW, ZM, MZ, NA, TZ). International: USA, France, Abu Dhabi, Pakistan only. |
| 9 | Understanding of Requirements | RFP/tender document + W3S1-001 for context | MANUAL | Read RFP; map client requirements to HCM modules; note gaps where no KB asset exists | Confirm scope matches approved assets only; flag missing asset gaps |
| 10 | Proposed Solution Overview | W3S1-001 + selected module assets (BOM 1) | HYBRID | Map approved assets to solution sections per tender scope | Module-specific restrictions (G-001, C-W3-002, OI-W4-001); never invent capabilities |
| 10a | HCM Core / Global HR | W3S1-001 | AUTO | Confirm employee count, LE count | None |
| 10b | Absence Management | W3S1-007 | AUTO | Confirm absence types in scope | None |
| 10c | Oracle Journeys / Onboarding | W4-HCM-002 | AUTO | Confirm Journey types in scope | None |
| 10d | Oracle AI Skills | W4-AI-002 | AUTO | Confirm AI Skills module in BOM | Do NOT conflate with ODA or Oracle Grow |
| 10e | Recruiting Cloud | W3S1-003 | AUTO | Confirm career site count; ATS migration scope | DFA Taleo: internal only. Redpath Recruiting: Rule 21.5. |
| 10f | Learning Cloud | W3S1-004 | HYBRID | Confirm content ownership; SETA reporting scope | Mr Price = Learning Cloud only (C-W3-002) |
| 10g | Talent Management | W3S1-002 | AUTO | Confirm performance template count; succession scope | DFA: Rule 21.4. Redpath: Rule 21.5. |
| 10h | Workforce Compensation | W3S1-005 | HYBRID | Confirm plan count; approval depth; sector | **G-001: Mining sector only** — Retail prohibited |
| 10i | HR Help Desk | W3S1-008 | AUTO | Confirm Help Desk modules: ER, KB, Chatbot | **Section 14.2 MUST NOT appear externally (PT-W8-007)** |
| 10j | Payroll Interface (OIC) | W3S1-009 | HYBRID | Confirm payroll system (PaySpace assumed); parallel run status | **Section 13.2 MUST NOT appear externally (PT-W9-008)**. Parallel run INCLUDED by default (HCM-CUT-005). |
| 10k | OIC Accelerators | W4-INT-001 | HYBRID | Confirm integration list; confirm OIC tier | HIST-018 billing (R825,170) MUST NOT appear externally |
| 11 | Implementation Methodology | W2S1-005 | HYBRID | Tailor phases; confirm client-specific milestones and go-live target | D-W5-003 (OPN revalidation), D-W5-004 (BEE), D-W5-005 (named client check), D-W5-006 (awards — BU confirm) |
| 12 | Project Plan | PROJECT_PLAN_TEMPLATES.md Pattern 1 | HYBRID | Confirm go-live date; set week offsets; confirm resource availability | Week-based only — convert to calendar dates only in final submission |
| 13 | Project Governance | W2S1-005 Sections 11–12 | HYBRID | RAID structure; escalation model; steering committee cadence | Standard governance — no client-specific claims without BU approval |
| 14 | Proposed Team | CONSULTANT_INDEX.csv skill match → APPTime CVs | MANUAL | BU Lead selects team; obtain current CVs from APPTime for selected consultants | ADR-001: NEVER write CV text from KB records. Use index for skill matching only. |
| 15 | Client References | REFERENCE_MASTER.csv → approved letters | HYBRID | Check AM approval for each named client; match sector/product | AM approval required at each submission. DFA/CCBA/Redpath exclusions. No unsigned templates. |
| 16 | Commercial Assumptions | HCM Base + module packs per scope | AUTO | Select assumption packs; include as appendix | Use only Approved packs. Flag Draft packs as "pending final approval" if referenced. |
| 17 | Scope — Inclusions | RFP + assumption packs + W2S1-005 | MANUAL | Define what is in scope for this specific engagement | Map to approved assumption pack inclusion language |
| 18 | Scope — Exclusions | Assumption packs + W3S1 per module | HYBRID | Confirm exclusions with BU Lead | Use approved assumption pack exclusion language verbatim |
| 19 | Compliance Attachments | COMPLIANCE_REGISTER.csv | AUTO | Verify expiry dates at submission time; refresh any expired documents | COMP-001 B-BBEE expires 2026-07-31. COMP-011 valid to 2027-06-15. COMP-006 Bank Letter < 3 months old. |
| 20 | Commercials / Pricing | WP11F Commercial Framework | PLACEHOLDER | **[COMMERCIAL INPUT REQUIRED]** — BU Lead + Commercial Director | NEVER generate prices without Commercial Director authorisation. Apply COMMERCIAL_GOVERNANCE.md sign-off sequence. |
| App A | Commercial Assumptions Pack | HCM_BASE_ASSUMPTIONS_V1.md | AUTO | None | Include only Approved version — never Draft |
| App B | OIC Assumptions | OIC_ASSUMPTIONS_V1.md | AUTO | Include only if OIC integrations in scope | |
| App C | AMS Assumptions | AMS_ASSUMPTIONS_V1.md | AUTO | Include only if post-implementation support in scope | |
| App D | Consultant CVs | APPTime-generated CVs | MANUAL | Obtain from APPTime after BU Lead selects team | |

---

## Structure 2 — Oracle ERP Proposal

Standard for: Oracle Fusion Financials, Procurement, PPM (single or combined).

| # | Section | Source | Method | Notes |
|---|---|---|---|---|
| 1–5 | Corporate + Oracle Partnership | W1S1-001/002/003/006/007 | AUTO | Same governance checks as HCM |
| 6 | Understanding of Requirements | RFP + W4-ERP-001/002/003 context | MANUAL | Map RFP to ERP modules; confirm LE count, COA, multi-currency |
| 7 | Oracle Fusion ERP Capability | W2S1-001 + W4-ERP-001/002/003 | HYBRID | Select modules per scope; confirm integration points |
| 8 | Data Migration | ERP_ASSUMPTIONS_V1.md (DAT section) | HYBRID | Confirm migration objects; confirm 2 mock + final standard; opening balance only default |
| 9 | OIC Integration | W4-INT-001 + OIC_ASSUMPTIONS_V1.md | HYBRID | Confirm integration count; OIC tier; error handling model |
| 10 | Implementation Methodology | W2S1-005 | HYBRID | ERP-specific phases; data migration milestones |
| 11 | Project Plan | PROJECT_PLAN_TEMPLATES.md Pattern 3 | HYBRID | Confirm go-live; week-based |
| 12 | Project Governance | W2S1-005 Sections 11–12 | HYBRID | Standard |
| 13 | Proposed Team | CONSULTANT_INDEX.csv → APPTime | MANUAL | ERP Finance Principal, Senior Finance, OIC, PM |
| 14 | Client References | REFERENCE_MASTER.csv | HYBRID | ERP refs: Investec (REF-ORA-001), NALA (REF-ORA-002), Cape Union Mart (REF-ORA-003), ARM (REF-ORA-008) |
| 15 | Commercial Assumptions | ERP_ASSUMPTIONS_V1.md + OIC_ASSUMPTIONS_V1.md | AUTO | ERP pack mandatory; OIC pack if integrations |
| 16 | Scope Inclusions / Exclusions | ERP assumption packs | HYBRID | Use ERP-INC/ERP-EXC language from ERP pack |
| 17 | Compliance + Commercials | COMPLIANCE_REGISTER.csv + WP11F | AUTO + PLACEHOLDER | Standard compliance; [COMMERCIAL INPUT REQUIRED] |

---

## Structure 3 — Oracle EBS Proposal

| # | Section | Source | Method | Notes |
|---|---|---|---|---|
| 1–5 | Corporate + Partnership | W1S1-001/002/003/006/007 | AUTO | Same governance; Level 1 only |
| 6 | Oracle EBS Capability | W2S1-002 (EBS Capability) | HYBRID | 2012 vintage — modernise stats and references for critical tenders |
| 7 | DBA / Managed Services | W2S1-003 + W2S1-004 | HYBRID | MTN 2014 DBA content — modernise for critical tenders; verify statistics |
| 8 | Methodology | W2S1-005 | HYBRID | OUM-based |
| 9 | Project Plan | PROJECT_PLAN_TEMPLATES.md Pattern 3 | HYBRID | |
| 10 | References | REF-ORA-004 Assore; REF-ORA-005 Adcock Ingram; REF-ORA-008 ARM; REF-ORA-009 MTN | HYBRID | Match by sector/scope; AM approval |
| 11 | ERP Assumptions + Commercials | ERP_ASSUMPTIONS_V1.md | AUTO + PLACEHOLDER | |

---

## Structure 4 — Oracle OIC Proposal

| # | Section | Source | Method | Notes |
|---|---|---|---|---|
| 1–5 | Corporate + Partnership | W1S1-001/002/003/007 | AUTO | |
| 6 | OIC Capability | W4-INT-001 + W2S1-001 | HYBRID | HIST-018 billing NEVER external |
| 7 | Integration Architecture | W4-INT-001 | AUTO | |
| 8 | Payroll Interface (if HCM) | W3S1-009 | HYBRID | Section 13.2 NEVER external (PT-W9-008) |
| 9 | Methodology | W5-METH-001 Appendix C (OCI/OIC) | HYBRID | |
| 10 | OIC Assumptions | OIC_ASSUMPTIONS_V1.md | AUTO | |
| 11 | References | REF-ORA-008 ARM (OIC scope); Hollywood Bets OIC (AM required) | HYBRID | |
| 12 | Compliance + Commercials | Standard | AUTO + PLACEHOLDER | |

---

## Structure 5 — Acumatica ERP Proposal

| # | Section | Source | Method | Notes |
|---|---|---|---|---|
| 1–2 | Corporate | W1S1-001/002 | AUTO | |
| 3 | Acumatica Partnership | W1S1-004 | AUTO | Gold Partner — no "Gold Certified". Annual revalidation. |
| 4 | Module Capabilities | W1S2-001 to 009 per scope | HYBRID | Include only BOM 14 modules in scope |
| 5 | Methodology | W5-METH-001 Appendix B (Acumatica) | HYBRID | |
| 6 | Project Plan | PROJECT_PLAN_TEMPLATES.md Pattern 5 | HYBRID | |
| 7 | References | REF-ACU-001 to 005 per sector | HYBRID | Match industry to engagement; AM approval |
| 8 | Assumptions | Acumatica Base pack — NOT YET CREATED | PLACEHOLDER | Flag gap; use ESTIMATION_GUIDE.md language as interim |
| 9 | Compliance | Standard + COMP-016 (missing — flag) | AUTO | Flag Acumatica Partner Certificate gap |
| 10 | Commercials | WP11F framework | PLACEHOLDER | [COMMERCIAL INPUT REQUIRED] |

---

## Structure 6 — BeBanking Proposal

| # | Section | Source | Method | Notes |
|---|---|---|---|---|
| 1–2 | Corporate | W1S1-001/002 | AUTO | |
| 3 | BeBanking Product Overview | W1S1-005 + W1S3-001 | AUTO | SAP rule; SWIFT rule |
| 4 | H2H Banking | W1S3-002 | AUTO | |
| 5 | Service Modules | W1S3-003/004/005/006/007 per scope | HYBRID | Confirm which banking services are required |
| 6 | ERP Integration | W1S3-006 | HYBRID | Confirm ERP in scope; SAP = environments only; Acumatica payroll rule |
| 7 | Security Architecture | W1S3-007/008 | AUTO | |
| 8 | Hosting Model | W1S3-009 | AUTO | |
| 9 | References | REF-ORA-010 WITS (Oracle + BeBanking) | HYBRID | AM approval |
| 10 | Assumptions | BeBanking pack — NOT YET CREATED | PLACEHOLDER | Flag gap |
| 11 | Compliance + Commercials | Standard | AUTO + PLACEHOLDER | |

---

## Structure 7 — AMS Proposal

| # | Section | Source | Method | Notes |
|---|---|---|---|---|
| 1–3 | Corporate + Partnership | W1S1-001/002 + BU partnership asset | AUTO | |
| 4 | AMS Support Model | W2S1-004 (Oracle) or W5-ACU-001 (Acumatica) | HYBRID | Match to product in scope |
| 5 | SLA Framework | AMS_ASSUMPTIONS_V1.md (SLA/PRI sections) | AUTO | P1=1h; P2=4h; P3=1day; P4=3days. 08:00–17:00 SAST. Response ≠ resolution. |
| 6 | CR Process | AMS_ASSUMPTIONS_V1.md (CR section) | AUTO | 2-hour CR threshold. CR_PRICING_MODEL.md for detail. |
| 7 | Release Management | AMS_ASSUMPTIONS_V1.md (REL section) | AUTO | Oracle quarterly release advisory included. Regression testing = excluded unless contracted. |
| 8 | Monitoring | AMS_ASSUMPTIONS_V1.md (MON section) | AUTO | Standard = mailbox monitoring only. Proactive monitoring = separate scope. |
| 9 | Project Plan | PROJECT_PLAN_TEMPLATES.md Pattern 7 | HYBRID | AMS onboarding timeline |
| 10 | Proposed Team | CONSULTANT_INDEX.csv → APPTime | MANUAL | |
| 11 | Client References | REFERENCE_MASTER.csv | HYBRID | Oracle AMS: REF-ORA-001/002/004/005/008/009/010. Acumatica AMS: REF-ACU-003/005. AM approval. |
| 12 | AMS Assumptions Pack | AMS_ASSUMPTIONS_V1.md | AUTO | Full pack in appendix — Approved version only |
| 13 | Exclusions | AMS_ASSUMPTIONS_V1.md exclusion language | AUTO | New module implementation; new integration development; data migration; new report development — all excluded |
| 14 | Commercials | WP11F framework + AMS pricing | PLACEHOLDER | AMS CRs always T&M. [COMMERCIAL INPUT REQUIRED] |

---

*PROPOSAL_STRUCTURE_LIBRARY v1.0 | WP12 — Proposal Assembly Engine | 2026-06-16*
*Companion: TENDER_BOM_LIBRARY.md | ASSEMBLY_RULES_ENGINE.md | PROJECT_PLAN_TEMPLATES.md*
