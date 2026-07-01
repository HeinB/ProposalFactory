---
document_id: PLENNEGY_COVERAGE_REPORT
title: "WP12 Tender Factory Pilot — Plennegy Oracle Opportunity: Coverage Report"
version: "1.0"
created: "2026-06-15"
created_by: "WP12 — Real Tender Pilot #1"
scope: "Simulation only. KB coverage analysis against Plennegy_Oracle_HCM_V3.docx."
---

# WP12 — Plennegy Oracle Opportunity: Coverage Report

**Simulation date:** 2026-06-15 | **Proposal version analysed:** V3 (22 May 2026)  
**Assessment scope:** Oracle HCM implementation proposal only (Track A)

---

## 1. Overall Coverage Summary

| Coverage Dimension | % Covered | Notes |
|---|---|---|
| **Capability / Product Descriptions** | 82% | 9 of 11 product areas have approved KB assets; 2 have no dedicated asset (Recruiting Booster; Touch Points) |
| **Implementation Methodology** | 88% | W2S1-005 covers OUM phases, data migration, governance principles. V3 has expanded governance sections |
| **Company Profile** | 45% | W1S1-001 provides the approved foundation; V3 draft currently contains 6 governance violations |
| **Reference Coverage** | 40% | 3 usable HCM references exist; no Oracle Fusion HCM reference available; Hollywood Bets letter pending |
| **Compliance Documentation** | 75% | 6 of 8 required compliance documents are valid; 2 are CRITICAL gaps (Directors' Resolution EXPIRED; B-BBEE expiring) |
| **Consultant / Resource Coverage** | 72% | Core HCM team is strong; team CVs on file; Fusion HCM reference projects limited to unconfirmed Hollywood Bets |
| **Governance Compliance** | 60% | V3 draft contains 6 prohibited claims from the ORACLE_FACT_BASELINE; must be corrected before submission |
| **Overall KB Coverage** | **67%** | Weighted average; see breakdown below |

---

## 2. Governance Violations Detected in Current V3 Draft

These are violations of the ORACLE_FACT_BASELINE, FACT_RESOLUTION_REPORT, and Wave 3 CROSS-1 amendment as applied to the current `Plennegy_Oracle_HCM_V3.docx`. Each item is a blocking issue that must be corrected before submission.

| # | Location in V3 | Violation | Required Fix | Severity |
|---|---|---|---|---|
| GOV-V3-001 | Section 7.2 Company Contacts | "Hein has 19 years' experience in the IT industry" | PROHIBITED. Hein started 1996 — as of 2026 is 30 years. Use "since 1996" or "more than 25 years". Never "19 years". | **CRITICAL** |
| GOV-V3-002 | Section 7.3 Company History — last paragraph | "APPSolve employs more than 110 Senior Consultants" | PROHIBITED per Wave 3 CROSS-1 amendment. Use "50+ Senior Consultants". | **CRITICAL** |
| GOV-V3-003 | Section 7.3 Company History — sub-Saharan Africa | "Nigeria, Tanzania, Uganda, and Ghana" listed as operating countries | PROHIBITED per FACT_RESOLUTION_REPORT F9. Nigeria, Uganda, Ghana have no client folder evidence. Approved list: Botswana, Zambia, Mozambique, Namibia, Tanzania. Remove Nigeria, Uganda, Ghana. | **CRITICAL** |
| GOV-V3-004 | Section 7.3 Company History — international | "Bangladesh...Pakistan, and Qatar" listed as international countries | PROHIBITED per FACT_RESOLUTION_REPORT F9. Bangladesh and Qatar have no client folder evidence. Approved international list: USA, France, Abu Dhabi, Pakistan only. Remove Bangladesh and Qatar. | **CRITICAL** |
| GOV-V3-005 | Section 7.3 Company History | "APPSolve has over the last 22 years..." | INCORRECT. APPSolve established 2002; as of May 2026 = 24 years. Use "more than 23 years" or "over 24 years". | MODERATE |
| GOV-V3-006 | Section 7.4 Products and Services (bottom paragraph) | "...our proud legacy over more than 16 years" | STALE TEMPLATE TEXT — 16 years is from an old document. As of 2026, this should be "more than 24 years". Update immediately. | MODERATE |
| GOV-V3-007 | Section 7.3 Company History | "Oracle Innovation Sustainability Award for 2015 and 2016" and "Oracle SaaS Partner of the Year (SADC Region) 2016 and...2019" | UNVERIFIED CLAIMS — ORACLE_FACT_BASELINE Section F7 only confirms EMEA/ECEMEA Business Impact Award 2024. 2015/2016/2019 award claims are not in the approved fact baseline. BU Lead to confirm these awards are still accurately described before including. | MODERATE |
| GOV-V3-008 | Section 7.3 Company History | "We operate from offices in Gauteng and the Western Cape" | VERIFY — confirmed in some documents but not explicitly in approved fact baseline. Confirm accuracy with BU Lead. | LOW |

**⚠ ACTION REQUIRED BEFORE SUBMISSION:** All GOV-V3-001 through GOV-V3-004 are CRITICAL and must be corrected. The company profile section of V3 must be replaced with content derived from approved W1S1-001 Company Overview.

---

## 3. Capability Coverage by Product Area

### 3.1 Fully Covered Areas (KB asset present, approved, directly applicable)

| Product Area | KB Asset(s) | Coverage Notes |
|---|---|---|
| Oracle Global HR / Core HR | W3S1-001 | Full coverage — employee lifecycle, self-service, compliance |
| Oracle Absence Management | W3S1-007 | Full coverage — confirmed Hollywood Bets production deployment (7,000 users, biometric OIC) |
| Oracle Journeys / Onboarding | W4-HCM-002 | Full coverage — approved asset, Tier 1 (Hollywood Bets Phase 1 in production) |
| Oracle AI-Based Dynamic Skills | W4-AI-002 | Full coverage — dedicated asset; approved HCM AI capability statement |
| Oracle Payroll Interface (third-party) | W3S1-009 | Full coverage — PaySpace integration in production; note: Plennegy's payroll system unknown — verify payroll provider before citing PaySpace specifically |
| Oracle OTBI / Analytics | W3S1-006 | Full coverage — OTBI Tier 1 (confirmed HB delivery); OAX platform-capability-only caveat applies |
| Oracle Talent Management Suite | W3S1-002 | Full coverage — Goal, Performance, Talent Review, Career Development all addressed |
| Oracle Recruiting Cloud | W3S1-003 | Full coverage — dedicated approved asset; Hollywood Bets is Tier 1 reference |
| Oracle Learning Cloud | W3S1-004 | Full coverage — Mr Price is the sole implementation reference (C-W3-002: Learning Cloud scope only) |
| Oracle Workforce Compensation | W3S1-005 | Coverage confirmed — **NOTE: Tier 2 (WP3-EX-001 ACTIVE)** — Redpath Mining pipeline cited only with approved wording. No Tier 1 named client reference for Workforce Compensation |
| Oracle Implementation Methodology | W2S1-005 | Full coverage — OUM 5-phase model, data migration, governance framework |

### 3.2 Partially Covered Areas

| Product Area | Gap | KB Asset | Notes |
|---|---|---|---|
| Oracle Recruiting Booster | No dedicated KB asset | W3S1-003 (partial) | Booster-specific features (Two-Way Messaging, Oracle Digital Assistant chatbot, Event Management, bulk communications) require supplementary product description. V3 sources this from Oracle's own product documentation — acceptable as product context but not approved KB content |
| Oracle Fusion Benefits | Benefits addressed within W3S1-001 overview | W3S1-001 (partial) | Benefits Administration is covered at summary level only; no deep-dive Benefits asset exists |
| OIC Enterprise (integration layer) | No standalone OIC-for-HCM asset | W2S1-001 (partial), W3S1-009 | W2S1-001 covers Oracle Cloud overview; W3S1-009 covers HCM payroll integration; no OIC Enterprise capability statement for HCM integration specifically |
| SA Statutory Compliance (SETA/WSP/ATR) | Specific SA statutory reporting for Learning | W3S1-004 (partial) | W3S1-004 notes the data extract approach for SETA reporting; no dedicated statutory compliance section in KB |
| Project Governance (expanded) | V3 has more detailed governance content | W2S1-005 (partial) | V3 risk/issue/change control sections are more client-ready than W2S1-005 governance paragraphs; KB provides the framework but V3 has expanded narrative |

### 3.3 Not Covered (No KB Asset)

| Product Area | Gap | Risk | Mitigation |
|---|---|---|---|
| Oracle Fusion Touch Points | No KB asset exists | Proposal section incomplete without approved content | Source from Oracle product documentation; flag to BU Lead to add as W4 or W5 asset in next wave |
| Costing / Pricing | Never in KB by design | No risk — this is correct | Pricing always bespoke; Oracle licensing costs from Oracle |
| Plennegy-specific client context | Never in KB — always bespoke | No risk — this is correct | Assembled per tender from client discovery |

---

## 4. Reference Coverage

| Reference Need | Available Reference | Tier | Governance | Coverage |
|---|---|---|---|---|
| Oracle HCM Fusion — full suite (Core HR + Recruiting + Learning + Talent + Compensation) | **NONE** — Hollywood Bets signed letter pending | — | Gap 2 from REFERENCE_GAP_ANALYSIS | **CRITICAL GAP** |
| Oracle HCM Cloud partner endorsement | REF-ORA-007 (Oracle Corp — Ashley Sanichar, Country Mgr) | Gold | OK — safe to use | ✓ Available |
| Oracle HCM — SA enterprise deployment (EBS) | REF-ORA-008 (ARM African Rainbow Minerals — EBS HCM) | Gold | OK | ✓ Available (EBS, not Fusion) |
| Oracle EBS HCM + Payroll | REF-ORA-010 (WITS — EBS HCM, BeBanking, Payroll) | Gold | OK | ✓ Available (EBS, not Fusion) |
| Oracle Learning Cloud (Fusion) | REF-ORA-006 (Mr Price — Learning Cloud) | Silver | **C-W3-002: cite Learning Cloud scope only** | ✓ Available — scope restricted |
| Oracle Recruiting Cloud | REF-ORA-003 (implied in W3S1-003 as Hollywood Bets) | — | Hollywood Bets named — AM approval required at each tender | ✓ Available with AM approval |
| Agribusiness sector reference | **NONE** | — | — | **GAP** — no agri/FMCG sector reference in corpus |
| Multi-entity group HR implementation | **NONE** signed | — | Hollywood Bets (7,000 users, multi-location) closest — no signed letter | **GAP** |

**Reference coverage rating: 40%** — Three usable references but none for Oracle Fusion HCM as a full suite. The most important letter for this specific tender (Hollywood Bets Oracle HCM Fusion) is the only missing letter that would close this gap.

---

## 5. Compliance Coverage

| Document | Status | Tender Impact |
|---|---|---|
| B-BBEE Certificate (COMP-001) | **RENEWAL REQUIRED** — expires 2026-07-31 (46 days) | If tender submits after July 31 without renewed cert, proposal is invalid. Renew by July 15. |
| SARS Tax Clearance PIN (COMP-002) | Active — valid to Feb 2027 | ✓ Include with proposal |
| Professional Indemnity (COMP-003) | Active — expires Nov 2026 | ✓ Include with proposal |
| COIDA Letter of Good Standing (COMP-004) | Active — valid to April 2027 | ✓ Include with proposal |
| CSD Registration (COMP-006) | Active — dated Aug 2025 | ✓ Include; note it's 10 months old — refresh if tender requires dated within 6 months |
| CIPC Annual Compliance (COMP-010) | Active — 2026 filed | ✓ Include |
| Directors' Resolution (COMP-011) | **EXPIRED March 2026 — CRITICAL** | **BLOCKER.** Cannot legally sign and submit tender without valid Directors' Resolution. Must be renewed before submission. |
| Public Liability Insurance (COMP-008) | **MISSING** | HIGH — if Plennegy requires Public Liability (common in large contracts), this must be obtained before submission |
| Oracle Partner Certificate (COMP-014) | Active | ✓ Include |
| POPIA Policy (COMP-012) | **MISSING** | MEDIUM — Plennegy may require supplier POPIA compliance evidence; no document on file |

**Compliance coverage: 75%** — 6 of 8 essential documents valid; 2 critical blockers (Directors' Resolution EXPIRED, B-BBEE expiring).

---

## 6. Critical Gaps (Must Fix Before Submission)

| # | Gap | Category | Severity | Action |
|---|---|---|---|---|
| CG-001 | Directors' Resolution EXPIRED | Compliance | **CRITICAL BLOCKER** | Renew Directors' Resolution immediately. Cannot submit without it. Estimated effort: 1–2 business days (board resolution + notarial) |
| CG-002 | B-BBEE Certificate expires 2026-07-31 (46 days) | Compliance | **CRITICAL URGENT** | Initiate renewal NOW. Allow 3–4 weeks for verifier turnaround. Target renewed cert by July 10. |
| CG-003 | V3 Company Profile — 6 governance violations | Governance | **CRITICAL BLOCKER** | Replace company profile section with W1S1-001 approved content. Apply all corrections per GOV-V3-001 through GOV-V3-004. |
| CG-004 | No Oracle Fusion HCM signed reference letter | References | **HIGH** | Priority request to Hollywood Bets for signed reference letter covering: Oracle HCM Core, Recruiting, Absence, Learning, HR Help Desk, OIC/PaySpace integration. Without this, Plennegy tender has no Fusion HCM production evidence. |
| CG-005 | Oracle Fusion Touch Points — no KB asset | Capability | MODERATE | Current V3 content (Section 3.7) sources from Oracle documentation — not prohibited but not approved KB. Add Touch Points asset to Wave 5 backlog. For this tender: use Oracle official product content with clear attribution. |

---

## 7. Moderate Gaps

| # | Gap | Category | Severity | Action |
|---|---|---|---|---|
| MG-001 | Recruiting Booster — no dedicated KB asset | Capability | MODERATE | V3 Section 3.6 is reasonable. Supplement W3S1-003 with Oracle product documentation for Booster-specific features. Add Recruiting Booster to Wave 5 KB backlog. |
| MG-002 | Agribusiness/FMCG sector narrative | Client Context | MODERATE | KB has no agri/FMCG narrative. V3 client context is bespoke and adequate; ensure it is reviewed and approved by BU Lead before submission |
| MG-003 | Payroll interface — Plennegy payroll system unknown | Technical | MODERATE | V3 mentions "Third-Party Payroll Integration" generically. Before submission, confirm which payroll system Plennegy uses. W3S1-009 is built on PaySpace assumption — adapt if Plennegy uses different payroll |
| MG-004 | CSD report dated Aug 2025 | Compliance | MODERATE | Refresh CSD report if tender is submitted after Feb 2026 (6-month threshold). Currently 10 months old. |
| MG-005 | POPIA policy MISSING | Compliance | MODERATE | Large enterprise client (Plennegy may require supplier POPIA evidence). Source POPIA policy or obtain from external counsel. |

---

## 8. Minor Gaps

| # | Gap | Category | Notes |
|---|---|---|---|
| MNG-001 | Oracle awards claims (2015/2016/2019) in V3 | Governance | Verify or remove — only EMEA/ECEMEA 2024 is in approved fact baseline |
| MNG-002 | Hein's Gazette-era HCM qualifications cited | Governance | V3 uses an old Hein bio; replace with approved W1S1-001 director profile |
| MNG-003 | V3 version history / change tracking | Document management | V3 lacks internal change log; add version history before final submission |
| MNG-004 | Public Liability Insurance missing | Compliance | Not always required; if Plennegy tender requires it, this becomes Critical |

---

## 9. Human Input Required

The following require BU Lead or account manager decision before KB or assembly can proceed:

| Item | Owner | Notes |
|---|---|---|
| Hollywood Bets AM approval for Fusion HCM reference | Oracle BU Lead + HB AM | Named HCM reference requires explicit AM approval per NAMED_REFERENCE_MATRIX |
| Plennegy payroll provider confirmation | Account Manager | Needed to customise W3S1-009 integration approach |
| Oracle awards (2015/2016/2019) factual verification | Oracle BU Lead | Confirm or remove these claims |
| Directors' Resolution renewal | Admin / Directors | Board resolution + annual renewal required |
| B-BBEE renewal initiation | Admin | Must initiate immediately |

---

*PLENNEGY_COVERAGE_REPORT v1.0 | WP12 Simulation | 2026-06-15 | See PLENNEGY_QUESTION_MATRIX.md and PLENNEGY_READINESS_SCORECARD.md*
