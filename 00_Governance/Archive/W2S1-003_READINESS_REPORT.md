---
created: "2026-06-11"
created_by: "Claude (AI — Wave 2 pre-extraction readiness analysis)"
status: "Active — pre-authoring gate document for W2S1-003"
purpose: "Source analysis, prohibited wording register, content map, and W2S1-004 reuse plan before authoring W2S1-003 Oracle DBA Executive Summary"
---

# W2S1-003 Pre-Extraction Readiness Report
## Oracle DBA Executive Summary
**Date:** 2026-06-11 | **Owner:** Hein Blignaut | **Status:** Awaiting BU Lead authorisation to proceed

> This report must be reviewed by the BU Lead before authoring of W2S1-003 begins.
> Do not proceed to extraction if any prohibited wording flags are unresolved.

---

## 1. Source Inventory

| ID | Document | Date | Type | Lines | Relevance |
|---|---|---|---|---|---|
| **MTN-2026** | APPSolve_MTN_DBA_RFP_RFX-1000004246_v1.0.docx | 05 April 2026 | Submitted RFP response | 1,495 | **PRIMARY — treatment as source of truth per instruction** |
| **MTN-SOW** | T1. DB_Scope_of_work_Feb2026.docx | February 2026 | MTN client document | 5,650 | Context only — confirms environment scale and requirements; not APPSolve content |
| **MTN-RFI** | APPSolve_MTN_DBA_RFI.docx | December 2024 (est.) | Pre-RFP RFI response | 602 | Superseded by MTN-2026; used only if RFP is silent |
| **HIST-002** | APPSolve Executive Summary.docx (MTN 2014) | July 2014 | Archive tender document | 95 | Secondary validation only — superseded for all technical content; 8-reason framework partially survives |
| **ORACLE_FACT_BASELINE** | 00_Governance/ORACLE_FACT_BASELINE.md | 2026-06-10 | Governance fact file | — | Mandatory cross-reference for all company and Oracle claims |

**Source decision:** MTN-2026 (April 2026, 1,495 lines) is the definitive primary source. It is recent, APPSolve-authored, submitted, and covers every DBA service domain in the W2S1-003 scope. HIST-002 adds negligible content given the depth of MTN-2026. The scope-of-work (MTN-SOW) provides environmental context only.

---

## 2. MTN Environment Context (from MTN-SOW)

| Parameter | Detail |
|---|---|
| Oracle databases | 300+ instances |
| MS SQL databases | 2,000+ instances |
| Environments | Dev, QA, UAT, Pre-Prod, Prod, DR |
| Oracle versions | 12c, 19c |
| MS SQL versions | 2012, 2014 (EOL), 2019 |
| Specialised tech | RAC, DataGuard, GoldenGate, EIS BI |
| Support model | 24/7 with after-hours standby |
| Monthly ticket volume | ~118 requests + 36 changes |
| Current team | 1 SDM, 3 Oracle DBAs, 2 SQL DBAs |
| Contract period | 36 months |

*Source: MTN-2026 lines 68–96; MTN-SOW confirms database inventory with lists from page 23 onwards*

---

## 3. Prohibited Wording Register — MTN-2026

All occurrences found by grep. Every occurrence is in the Company History / Company Profile sections (MTN-2026 lines 1187–1410). The technical DBA content sections (lines 47–1186) are clean.

| # | Line | Prohibited text | Correction |
|---|---|---|---|
| PW-001 | 1212 | "He has 19 years' experience in the IT industry" (Hein) | "~30 years of IT industry experience" |
| PW-002 | 1237 | "APPSolve has over the last 22 years acquired…" | "APPSolve has over more than two decades acquired…" or "over 23 years" |
| PW-003 | 1238 | "…Nigeria, Tanzania, Uganda, and Ghana" | Remove Nigeria, Uganda, Ghana. Approved: Botswana, Zambia, Mozambique, Namibia, Tanzania only |
| PW-004 | 1238 | "…Bangladesh…Qatar" | Remove Bangladesh, Qatar. Approved: USA, France, Abu Dhabi, Pakistan only |
| PW-005 | 1249 | "APPSolve employs more than 110 Senior Consultants" | "APPSolve employs 50+ Senior Consultants" |
| PW-006 | 1307 | "Our Gold Level partnership with Oracle" | "Our Level 1 partnership with Oracle" |
| PW-007 | 1313 | "APPSolve has the largest number of locally based Oracle Applications DBAs" | "APPSolve operates one of the largest locally-based Oracle Applications DBA teams in South Africa" |
| PW-008 | 1373 | "a team of over 100 senior resources" | "a team of 50+ senior resources" |
| PW-009 | 1407 | "Oracle Partner for the past 22 years" | "Oracle partner for over two decades" |

**Verdict:** 9 prohibited occurrences. All are in the company profile section (lines 1187–1410). The technical DBA content (lines 47–1186) is free of prohibited wording. Corrections are straightforward. W2S1-003 must not extract the company history/profile section verbatim — it must be constructed from approved W1S1 files.

---

## 4. DBA Content Coverage Assessment

Assessment of each W2S1-003 scope domain against MTN-2026 content.

| Domain | MTN-2026 Coverage | Key Lines | Depth |
|---|---|---|---|
| DBA overview / service definition | Executive Summary + Scope Understanding | 47–149 | FULL |
| Core DBA services (install, config, decommission) | Scope section 2.3.1 | 100–106 | FULL |
| Monitoring (proactive, multi-layer) | Q20 — 3-layer monitoring framework | 670–723 | FULL |
| Performance tuning (query, index, wait events) | Q16, Q20 | 579–599, 697–711 | FULL |
| Patching / upgrades (N-1 strategy) | Q9, Q27 | 447–452, 1013–1021 | FULL |
| Backup / recovery | Q17 (DR/BCM section), SOPs | 601–613, 725–749 | FULL |
| Disaster Recovery (DataGuard, RAC, GoldenGate) | Q17, Q15 | 601–613, 573–577 | FULL |
| Capacity planning / demand management | Q14 | 543–571 | FULL |
| Security (POPIA, RBAC, Guardium, audit) | Q18 | 615–627 | FULL |
| Operational governance (ITIL, CMDB, SLA) | Q8, Q13, Q19 | 435–541, 629–668 | FULL |
| Segregation of duties | Q28 | 1040–1167 | FULL |
| Oracle tool competencies | Q26 — tool-by-tool response with reference clients | 926–990 | FULL |
| ETL / integration services | Q6, Q11 | 419–480 | FULL |
| Migration capability | Q5, Q11 | 352–480 | FULL |
| 24x7 support model | Q23 | 832–872 | FULL |
| Continuous Service Improvement | Q12 | 482–497 | FULL |
| Service Delivery Management | Q13 | 499–541 | FULL |
| OEM vendor engagement | Q7 | 427–431 | FULL |
| Project management / BAU | Q10 | 453–459 | FULL |
| Reference clients (DBA managed services) | Q1, Q3, Q26 | 155–174, 345–347 | GOOD |
| Team profiles / certifications | Q2 | 175–218 | GOOD |

**Overall coverage rating: EXCELLENT.** All 21 domains covered with specific, detailed, APPSolve-authored content.

---

## 5. Oracle Tool Competency Evidence (from MTN-2026 Q26, lines 926–990)

| Tool | Evidence | Reference Clients |
|---|---|---|
| Oracle APEX | 15+ years, multiple sites | Investec, Adcock Ingram, American Tower, MTN Group |
| Oracle R | 15+ years | South African Reserve Bank |
| Oracle Heterogeneous Services | 20+ years | Adcock Ingram, Mr Price, Investec, KPMG, American Tower |
| Oracle GoldenGate | 20+ years, multiple sites | FNB, South African Reserve Bank, Assore, Technology Management Network Services |
| Oracle Enterprise Manager (OEM) | 20+ years, multiple sites | KPMG, Adcock Ingram, SA Reserve Bank, African Rainbow Minerals |
| Oracle RAC | Multiple sites | SA Reserve Bank, Adcock Ingram, Cell C |
| Oracle DBFS | DBFS Content Store, Secure File Store, DBFS Client | Not named |
| Oracle DataGuard | Multiple sites | SA Reserve Bank, Adcock Ingram, KPMG, FNB, Harmony, African Rainbow Minerals |

*Source: MTN-2026 lines 926–990*

---

## 6. DBA Managed Services Reference Clients (from MTN-2026)

Reference clients confirmed for Oracle DBA managed services (Q1 and Q3 responses):

| Client | Service type | Platform | Notes |
|---|---|---|---|
| MTN | Long-standing DBA managed service since 2002 | Oracle | Database monitoring, performance, backup/recovery, security, patching, upgrades, migrations, cloud support — lines 231–240 |
| Cell C | DBA and application support | Oracle | Lines 242–262 |
| Dark Fibre Africa (DFA) | Database and application managed services | Oracle | Lines 264–275; includes cloud DB support |
| African Rainbow Minerals (ARM) | O/S, database and application managed services | Oracle | Currently active — line 347 |
| SA Reserve Bank | Enterprise architecture, DBA, application support | Oracle | Currently active — line 347 |
| KPMG Africa | O/S and database support | Oracle | Currently active — line 347 |
| Expert Buying Group | Full DBA managed service | Microsoft | Lines 276–288 |
| Truman & Orange | Full DBA managed service | Microsoft | Lines 289–301 |
| NeuCoat | Full DBA managed service | Microsoft | Lines 302–314 |
| Adcock Ingram | DBA support (reference tool evidence) | Oracle | Multiple tool competency refs |
| Investec | DBA support (reference tool evidence) | Oracle | Multiple tool competency refs |
| FNB | GoldenGate, DataGuard | Oracle | Tool competency ref |

**Telecom sector:** MTN, Cell C, Virgin Mobile (lines 242–262) — all Oracle DBA managed services. Strong telecom DBA reference base.

---

## 7. Service Model Highlights (sourced from MTN-2026)

| Capability | Description | Lines |
|---|---|---|
| Hybrid Support Model | Unique blended on-site / remote model; Remote Support Centre for 24x7 monitoring; cost-effective | 1393–1405 |
| 24x7 Support Structure | Primary On-Call DBA (L2/L3), Secondary Escalation (L3/SME), Service Delivery Lead; <15 min response SLA | 840–872 |
| Continuous Improvement Model | 4 stages: Analyse → Plan → Implement → Measure; 3 pillars: People, Processes, Technology | 1377–1392 |
| Monthly Recurring Invoice Model | Flexible and predictable costing; capacity transfer between months | 1402–1406 |
| N-1 Patching | Continuous OEM monitoring → non-prod validation → CAB-approved after-hours deployment | 447–452 |
| ITIL Alignment | Incident (B-55), Problem (B-137), Event (B-151), Change (B-163) — all named MTN-aligned processes | 436–445 |
| Design Assurance Methodology | Architectural review to prevent recurrence; OEM engagement to drive patch fixes | 427–431 |
| Customer Success Manager | C-level sponsor at no cost; monthly strategic alignment with MTN | 541 |

---

## 8. HIST-002 (2014) vs. MTN-2026 Comparison

| Content area | HIST-002 (2014) | MTN-2026 (April 2026) | Verdict |
|---|---|---|---|
| 8-reason framework structure | ✓ Present (origin) | ✓ Evolved version present | MTN-2026 supersedes in all areas except historical framing |
| Hybrid Support Model | ✓ Originated here | ✓ Expanded and current | MTN-2026 is authoritative |
| CIM (Continuous Improvement Model) | ✓ Originated here | ✓ Expanded with 4-stage + 3-pillar detail | MTN-2026 is authoritative |
| Monthly Recurring Invoice Model | ✓ Present | ✓ Present (identical concept, updated language) | MTN-2026 language is current |
| Team capabilities | 3 Oracle APPS DBAs named | 6 named consultants with certs | MTN-2026 is authoritative |
| Oracle partner status | "Gold partner for the past 10 years" — PROHIBITED | Level 1 Partner used in technical sections (prohibited wording in profile section) | MTN-2026 technical sections are cleaner; both need correction |
| Technical depth | Minimal (8-point executive summary only) | Full 28-question response | MTN-2026 far superior |

**HIST-002 verdict:** HIST-002 has zero unique content for W2S1-003 beyond confirming the origination of the Hybrid Support Model and CIM concepts, which are more fully articulated in MTN-2026. HIST-002 should be treated as validation context only. Do not extract any content directly from HIST-002.

---

## 9. W2S1-004 Managed Services Reuse Map

To avoid duplicate extraction effort, the following content blocks from MTN-2026 are better suited to W2S1-004 Oracle Managed Services Support Model than to W2S1-003 Oracle DBA Executive Summary. Mark each block for W2S1-004 and do not duplicate in W2S1-003.

| Content block | Lines | Recommended file | Reason |
|---|---|---|---|
| ITIL detail (Incident/Problem/Change/Event Management — full Q8 response) | 435–445 | W2S1-004 | Managed Services process detail; too granular for exec summary |
| SLA meeting cadence table (daily/weekly/monthly/quarterly) | 500–517 | W2S1-004 | Governance model detail |
| SLA and operational reporting table (5 report types) | 519–537 | W2S1-004 | Reporting framework |
| CSI closed-loop model (Measure/Analyse/Improve/Review) | 484–497 | W2S1-004 | CSI framework |
| Capacity Management approach (full Q14 response) | 543–571 | W2S1-004 | Capacity and demand management |
| 24x7 support model structure (full Q23 response with table) | 832–872 | W2S1-004 | Support model specification |
| Segregation of duties framework (full Q28 response) | 1040–1167 | W2S1-004 | Governance / security controls |
| CMDB governance model (full Q19 response) | 629–668 | W2S1-004 | Configuration management |
| Performance management detail (Q16) | 579–599 | Shared — summarise in W2S1-003; full detail in W2S1-004 |  |
| Monitoring framework detail (Q20 — 3-layer model with tables) | 670–723 | Shared — mention in W2S1-003; full detail in W2S1-004 | |
| ETL and migration factory detail (Q5, Q6, Q11) | 352–480 | W2S1-004 | Advanced technical content; too operational for exec summary |
| Backup SOP structure (Q21 — TOC only) | 725–749 | W2S1-004 | Documentation standards |
| Monthly report TOC (Q22) | 784–828 | W2S1-004 | Reporting standards |
| DR/BCM detail (full Q17 response) | 601–613 | Shared — headline in W2S1-003; full detail in W2S1-004 | |
| Deployment framework (Q27) | 993–1037 | W2S1-004 | Release management |

**Content appropriate for W2S1-003 Executive Summary only:**

| Content block | Lines | Notes |
|---|---|---|
| Executive Summary narrative | 47–55 | Core value proposition — with prohibited wording corrections applied |
| Scope understanding (2 pages) | 62–149 | Service scope context |
| DBA team names and certifications | 175–218 | Team credibility |
| Reference client managed services table | 220–330 | Delivery evidence |
| Oracle tool competencies table | 926–990 | DBA differentiators |
| Hybrid Support Model headline | 1393–1401 | Differentiator — headline only |
| CIM (Continuous Improvement Model) headline | 1377–1392 | Differentiator — 4-stage / 3-pillar summary |
| Monthly Recurring Invoice Model | 1402–1406 | Commercial differentiator |
| Key success factors | 145–149 | Strategic framing |

---

## 10. Factual Risk Register (Pre-Extraction)

| ID | Risk | Severity | Resolution |
|---|---|---|---|
| FR-A | Prohibited wording in company profile (PW-001 to PW-009) | CRITICAL | Do not extract company profile from MTN-2026. Construct company profile from approved W1S1 files only. |
| FR-B | "APPSolve has the largest number of locally based Oracle Applications DBAs" (line 1313) — absolute superlative | HIGH | Correct to "one of the largest locally-based Oracle Applications DBA teams in South Africa" per ORACLE_FACT_BASELINE.md Section 9 |
| FR-C | Team resource profiles in W2S1-003 — named consultants | MEDIUM | Do not include individual consultant names or detailed CVs in KB capability statement. Reference team depth generically. Named consultants live in APPTime only (ADR-001). |
| FR-D | DFA reference (lines 264–275) — DBA managed services client | MEDIUM | DFA appears as a reference in this MTN-2026 DBA proposal, including "cloud DB support". However, W2S1-001 established that DFA is NOT available for reference without BU Lead authorisation. Confirm DBA reference status for DFA with BU Lead before including in W2S1-003. |
| FR-E | MTN relationship since 2002 claim (lines 231, 33) | LOW | Confirmed: Hein established APPSolve in 2002. MTN is the origin client. Claim is accurate. Use with approved wording. |
| FR-F | "Reduced capacity-related incidents by over 40%" (line 563) | MEDIUM | Specific metric from unnamed enterprise engagement. Cannot verify. Flag as [UNVERIFIED] if used; or omit. |
| FR-G | "Managed environments exceeding 1000+ databases" (line 562) | MEDIUM | Implied to be MTN. Given MTN has 300+ Oracle + 2000+ SQL = 2300+ total, this is plausible but should be confirmed before stating as a reusable KB claim. Flag for BU Lead. |

---

## 11. ORACLE_FACT_BASELINE Cross-Reference

| Fact required for W2S1-003 | Baseline value | Aligned in MTN-2026 |
|---|---|---|
| Oracle partner tier | Level 1 Partner | Technical sections: not stated explicitly in those sections; profile section says "Gold Level" (PROHIBITED) — must correct |
| DBA team claim | "one of the largest locally-based Oracle Applications DBA teams in South Africa" | Line 1313 uses absolute "largest" — correction required |
| Consultant headcount | 50+ Senior Consultants | Line 1249: "110" (PROHIBITED); line 1373: "100" (PROHIBITED) — must correct |
| Hein Blignaut experience | ~30 years | Line 1212: "19 years" (PROHIBITED) — must correct |
| Oracle partner tenure | "over two decades" | Line 1407: "22 years" (PROHIBITED) — must correct |
| Awards | EMEA + ECEMEA 2024 Business Impact; 2015/2016 Innovation; 2016/2019 SaaS | Lines 1240–1244 include pre-2024 awards (correct) but omit 2024 Business Impact awards (from W1S1-003). Must add EMEA + ECEMEA 2024 during extraction. |

---

## 12. Readiness Recommendation

**Status: READY TO AUTHOR — with corrections**

| Dimension | Status | Notes |
|---|---|---|
| Source availability | ✓ READY | MTN-2026 April 2026 is recent, comprehensive, and APPSolve-authored |
| DBA scope coverage | ✓ READY | All 21 scope domains covered in detail |
| Prohibited wording | ⚠ REQUIRES CORRECTION | 9 occurrences in company profile section; all correctable from approved W1S1 files |
| HIST-002 cross-reference | ✓ COMPLETE | HIST-002 confirmed as superseded; zero unique content for W2S1-003 |
| DFA reference flag | ⚠ BU LEAD DECISION | DFA appears as DBA managed services client; DFA is NOT available for reference (per W2S1-001). BU Lead must confirm whether DBA reference status differs from Fusion reference status. |
| 40% reduction claim | ⚠ FLAG | Specific metric; unverified; flag or omit |
| 1000+ databases claim | ⚠ FLAG | Plausible but unverified; flag or omit |
| W2S1-004 reuse map | ✓ COMPLETE | 15 content blocks identified and pre-assigned to W2S1-004 |
| Company profile sourcing | ✓ CLEAR | Company profile for W2S1-003 must come from W1S1-001, W1S1-002, W1S1-003, W1S1-007, W1S1-009 — NOT from MTN-2026 company profile section |

**Pre-authoring action required from BU Lead:**
1. Confirm DFA DBA reference status — may use in W2S1-003 or not?
2. Confirm "40% reduction in capacity incidents" stat — use or omit?
3. Confirm "1000+ databases managed" claim — confirm as MTN and approve or omit?
4. No other blockers.

**If BU Lead approves, authoring of W2S1-003 may proceed immediately.**

---

## 13. Proposed W2S1-003 Structure

Recommended section structure for the Oracle DBA Executive Summary:

| Section | Content source | Length |
|---|---|---|
| 1. Executive Statement | MTN-2026 lines 47–55 (corrected); W1S1-001 company claims | ~200 words |
| 2. APPSolve DBA Partnership Background | W1S1-003 (partner status); W1S1-007 (DBA team claim); MTN-2026 relationship framing | ~150 words |
| 3. DBA Service Capability Overview | MTN-2026 lines 100–121 (scope categories); W1S1-009 (24x7, hybrid) | ~300 words |
| 4. Oracle Tool Competencies | MTN-2026 lines 926–990 (tool evidence table + reference clients) | Table format |
| 5. Service Delivery Model Highlights | CIM (4-stage/3-pillar); Hybrid Support Model; Monthly Recurring Invoice (headline only) | ~200 words |
| 6. Referenceable Managed Services Clients | MTN-2026 lines 220–330 (client table — Oracle clients only; DFA subject to BU Lead) | Table format |
| 7. Key Differentiators | MTN-2026 lines 145–149 + 427–431 (Design Assurance); W1S1-009 | ~150 words |
| Extraction documentation | Source map, assumptions, factual risks, quality assessment, recommendation | Internal only |

**Estimated KB content quality post-extraction:** STRONG — primary source is rich, current, and directly applicable.

---

*Prepared: 2026-06-11 — Wave 2 Session 1 pre-extraction analysis*
*Prepared by: AI (Claude Sonnet 4.6) — readiness gate only; BU Lead must approve before authoring proceeds*
*Sources read: MTN-2026 (1,495 lines), MTN-SOW (5,650 lines, context only), MTN-RFI (602 lines), HIST-002 (95 lines), ORACLE_FACT_BASELINE.md*
*Next action: BU Lead reviews this report → confirms DFA flag (FR-D), stat flags (FR-F, FR-G) → authorises authoring of W2S1-003*
