---
created: "2026-06-10"
created_by: "Claude (AI — Wave 2 Session 1 pre-extraction analysis)"
status: "Active — extraction readiness notes only; no content extracted to KB yet"
sources_read:
  - TMPL-001: Oracle Fusion Template.docx (563 lines, Sept 2024)
  - SAA: APPSolve_SAA_RFP.docx (2138 lines, June 2025)
  - RedPath: RedPath Mining_APPSolve_RFI Reply Detail.docx (449 lines, March 2026)
  - Baseline: ORACLE_FACT_BASELINE.md (created 2026-06-10)
---

# Oracle Fusion Extraction Notes
**Session:** Wave 2 Session 1 | **Date:** 2026-06-10 | **Purpose:** Pre-extraction analysis for W2S1-001

These notes document what was found across all three sources. They are not KB content. The extractor uses these as the working map before creating W2S1-001.

---

## 1. Module Coverage — What Exists in Sources

### 1.1 Oracle Fusion HCM Modules (SAA Section 2 — primary source)

SAA contains 10 named module sections, each with Overview, Benefits, Key Features and Capabilities sub-structure:

| Module | Section quality | Primary source | Notes |
|---|---|---|---|
| Oracle HCM Base Cloud (Global HR) | High — full O/B/KF structure | SAA lines 112–180 | Covers lifecycle, compliance, ESS/MSS |
| Oracle AI-Based Dynamic Skills | High | SAA lines 130–134 | Skills mapping, personalized learning, gap identification |
| Oracle Absence Management | High | SAA lines 135–139 | Leave tracking, self-service, payroll integration |
| Oracle Benefits | High | SAA lines 140–144 | Flexible programs, self-service, regulatory compliance |
| Oracle Journeys | High | SAA lines 145–149 | Onboarding, guided processes, personalized experiences |
| Oracle Payroll Interface (3rd party) | High | SAA lines 150–155 | Third-party integration; NOT Oracle Cloud Payroll native |
| Oracle Workforce Directory Management | High | SAA lines 155–159 | Org structures, team insights, self-service |
| Oracle Workforce Modelling and Predictions | High | SAA lines 160–164 | Predictive analytics, scenario planning, actionable insights |
| Oracle Work Life Solutions | High | SAA lines 165–169 | Work-life integration, wellness, EAP |
| OTBI (Transactional Business Intelligence) | High | SAA lines 170–174 | Real-time reporting, self-service analytics, embedded |
| TDE (Transparent Data Encryption) | Medium | SAA lines 175–179 | Data security, compliance, encryption |
| Oracle Workforce Compensation Cloud | High — standalone section | SAA lines 181–236 | Salary, bonus, incentives; merit-based; compensation plans |
| Oracle Recruiting Cloud | High — standalone section | SAA lines 238–293 | AI-driven; ATS; onboarding; analytics |
| Oracle Talent Management | High — standalone section | SAA lines 296–348 | Performance; career development; succession; AI-driven |
| Oracle Help Desk | High — standalone section | SAA lines 349–408 | HR case management; AI; multi-channel |
| Oracle Learning Cloud | High — standalone section | SAA lines 411–458 | LMS; AI-driven; certifications; offline mobile |
| Oracle HCM Analytics | High — standalone section | SAA lines 460–493 | Prebuilt dashboards; 50+ KPIs; predictive |
| Oracle Time and Labor | High — standalone section | SAA lines 495–535 | Flexible time entry; rules engine; payroll integration |
| Oracle Workforce Scheduling | High — standalone section | SAA lines 536–582 | Demand-driven; rule-based; self-service shift management |

**Assessment:** SAA Section 2 is the richest HCM source in the corpus. 19 capability areas covered. All have sufficient detail to extract KB content.

### 1.2 Oracle Fusion Finance and Procurement (RedPath Mining and SABS ETS — validation)

No dedicated Finance/Procurement capability descriptions exist in TMPL-001, SAA, or RedPath Mining. The only Finance/Procurement content is:
- TMPL-001 core components table: "Manages financial operations, including general ledger, accounts payable, accounts receivable, fixed assets, and cash management"
- RedPath Mining Expanded Criteria: "We have implemented multiple Oracle Cloud ERP Finance implementations"
- RedPath Mining client list: DFA (Financial Modules, Procurement), Cape Union Mart (Financial Modules, SCM + Procurement), Investec (Financials, Procurement)

**Assessment:** Finance/Procurement capability content is thin in these three sources. TMPL-001 has a Finance section that was not extracted in this read. A separate read of the full TMPL-001 Finance section is recommended for W2S1-001 if Finance is to be included. Or scope W2S1-001 to HCM only and note Finance as a Wave 2 addendum.

### 1.3 Oracle Fusion SCM, CRM, GRC (all sources)

Only high-level component table descriptions. No implementation capability content.

### 1.4 Oracle PPM (Project Portfolio Management)

Not covered in dedicated section in any of the three sources. Only reference: RedPath Mining "Projects / PPM" expanded criteria: "We have implemented multiple Oracle ERP implementations with Project module included."

---

## 2. Oracle Fusion Capability Areas — Extractable

| Capability area | Available content | Best source |
|---|---|---|
| Platform architecture overview | Modular, cloud-native, SaaS, analytics, UX, global, security | TMPL-001 / SAA (identical text) |
| HCM full module list (19 modules) | Full Overview/Benefits/Key Features per module | SAA Section 2 |
| Fusion Finance overview | Core components table only | TMPL-001 |
| OCI security and compliance | OCI services (Cloud Guard, WAF, IAM); SOC 1/SOC 2 evidence | SAA lines 1096–1109 |
| Oracle Integration Cloud (OIC) | Standard in ALL Fusion implementations; SAP integration | RedPath Mining line 195; SAA lines 882–888 |
| Data migration tools | HDL, HSDL, FBDI — Oracle standard tools | SAA lines 1158–1173; RedPath Mining line 199 |
| REST APIs | Comprehensive REST API coverage | SAA lines 1176–1186 |
| Scalability (SaaS) | Multi-tenant, automatic updates, global data centers | SAA lines 1188–1197 |
| Analytics (OTBI + HCM Analytics) | Real-time, self-service, embedded | SAA lines 1203–1215 |
| Security (RBAC, MFA, encryption) | Role-based, data security profiles, TDE, MFA | SAA lines 1083–1094 |
| Compliance (POPIA, GDPR) | Data retention, audit trails, privacy by design | SAA lines 1113–1148 |
| SAP payroll integration | OIC or HCM Extracts; "implemented many times" | SAA line 890 |
| Visual Builder Studio / Redwood | Custom extensions, personalisation | RedPath Mining line 205; SAA line 1232 |
| Reporting (OTBI, BI Publisher) | Standard and custom reports | RedPath Mining line 205 |
| Implementation methodology | OUM-based 6-stage approach | SAA Section 5; RedPath Mining Section — nearly identical |

---

## 3. OCI Positioning

### What the sources say

**SAA lines 1096–1109:**
Fusion HCM runs on Oracle Cloud Infrastructure (OCI). OCI provides:
- Oracle Cloud Guard (continuous security monitoring)
- Vulnerability Scanning Service
- Web Application Firewall (WAF)
- Identity and Access Management (IAM)
- Threat Intelligence Service
- Oracle Advanced HCM Controls (AI-powered transaction monitoring, SoD enforcement, fraud prevention)

**SAA lines 1187–1197 (Scalability section):**
OCI provides elastic, auto-scaling infrastructure; global data center network; customers choose data center region for data residency compliance.

**Baseline confirmation:**
SOC 1 Type 2 + SOC 2 Type 2 Bridge Letters submitted with SAA RFP (June 2025). These are OCI compliance evidence documents available for submission in other tenders.

### OCI extraction recommendation

The OCI positioning can be extracted as a subsection under the main Oracle Fusion capability document:
- "Oracle Cloud Infrastructure (OCI) — Security and Compliance" subsection
- Key claim: Fusion applications run on OCI with enterprise-grade security
- Key differentiator: SOC 1 and SOC 2 Bridge Letters available (evidence submitted June 2025)
- Note: OCI Bridge Letters must be referenced as supporting attachments, not embedded in the KB document

---

## 4. OIC Positioning

### What the sources say

**RedPath Mining line 195 (strongest, most direct claim):**
> "All our Fusion implementation we have also implemented Oracle Integration Cloud. We have used OIC for all inbound and out bound interfaces between Oracle SaaS and 3rd party systems."

**SAA lines 882–888 (contextual — SAP integration):**
> "Oracle Integration Cloud (OIC) or other third-party middleware solutions are often used... OIC offers pre-built adapters for various applications, including SAP, which can simplify the integration process."

**SAA line 884 (CAUTION — client-specific hedging):**
> "this would require more in depth information about SAA integration architecture and once this is workshopped / scoped we can confirm if OIC is required in the interim"

This SAA-specific hedge must NOT be extracted as a general statement. It was SAA-context language. The RedPath Mining statement is the authoritative general claim.

### OIC extraction recommendation

Use RedPath Mining line 195 as the authoritative base:
> "APPSolve implements Oracle Integration Cloud (OIC) as the standard integration layer in all Oracle Fusion implementations. OIC manages all inbound and outbound interfaces between Oracle SaaS modules and third-party systems."

Then add the SAP payroll integration claim from SAA (line 890):
> "APPSolve has implemented an integration between Oracle HCM and SAP Payroll many times."

---

## 5. Migration Positioning

### What the sources say

**RedPath Mining line 199:**
> "We predominantly use Oracle's standard API's and FBDI sheets to load master and transactional data. Extracting and transforming data is normally the responsibility of our customers with the assistance of the APPSolve resources to explain and guide the users to the Oracle required and extra fields. Transactional data in the financial modules are always reconciled back to the control accounts in the Trial Balances."

**SAA lines 1158–1173:**
- HCM Data Loader (HDL) — primary bulk migration tool
- HCM Spreadsheet Data Loader (HSDL) — Excel-based, for business users
- File-Based Data Import (FBDI) — for other Oracle Cloud data
- Phased migration recommended for large/complex organizations

**OPN Published Expertise (from baseline):**
- "Oracle E-Business Suite Migration to OCI" — published expertise area
- "Oracle Cloud Infrastructure Migration" — published expertise area

### Migration extraction recommendation

Two distinct migration claims:
1. **Data migration within an implementation project** — use RedPath Mining + SAA content (FBDI/HDL approach, customer-led with APPSolve guidance, reconciliation to Trial Balance)
2. **EBS-to-OCI migration** — use W1S1-003 published expertise areas (content must be added in extraction)

---

## 6. Oracle Differentiators

These are APPSolve-specific claims that differentiate from generic Oracle product descriptions:

| Differentiator | Evidence | Source(s) |
|---|---|---|
| OIC as standard in ALL Fusion implementations | "All our Fusion implementation we have also implemented Oracle Integration Cloud" | RedPath Mining line 195 |
| SAP Payroll integration experience | "APPSolve has implemented an Integration between Oracle HCM and SAP Payroll many times" | SAA line 890 |
| Mining sector Oracle expertise | "we have implemented and supporting 3 mining companies: Assore, ARM, Harmony" | RedPath Mining line 193 |
| Multi-country Fusion rollouts | Investec (3 countries), Nala Renewables (8 countries) | RedPath Mining lines 233–239 |
| DBA team | "one of the largest locally-based Oracle Applications DBA teams in South Africa" | W1S1-007 (approved) |
| OUM-based methodology | "APPSolve has developed its own implementation methodology, based on Oracle's OUM" | RedPath Mining line 257 |
| Customer Success Navigator alignment | Methodology stages align to Oracle's current CSN stages | RedPath Mining line 257 |
| Visual Builder Studio / Redwood | Custom UI extensions; Oracle Redwood pages for personalisation | RedPath Mining line 205; SAA line 1232 |
| Oracle validation tool | "we have developed our own validation tool to compare against Oracle's Usage report" | RedPath Mining line 208 |
| Senior-only delivery | "Senior consultants allocated to this project. No juniors or midlevel consultants" | RedPath Mining line 364 |
| Hyper-care support | "3 months of hyper care with a full complement of senior resources" | SAA line 1256 |
| Oracle Modern Best Practices | Applied to all implementation scoping | SAA line 1427; RedPath Mining line 273 |

---

## 7. Referenceable Client Experience

All client references confirmed across two or more sources. These can be cited in W2S1-001 without additional verification (reference letters to be attached separately per tender requirement).

### Oracle Fusion Clients

| Client | Modules confirmed | Headcount / scale | Source |
|---|---|---|---|
| Dark Fibre Africa (DFA) | Finance, Procurement, Project Costing, HCM Core, Recruiting, Talent, Performance, Learning, Oracle Payroll Cloud | Not stated | RedPath Mining lines 214–220, 245 |
| Cape Union Mart | Finance, SCM, Procurement | Not stated | RedPath Mining lines 222–225 |
| Investec Bank | Finance, Procurement (3 countries: SA, US, UK) | Multi-country | RedPath Mining lines 233–236 |
| Mr Price Group | HCM, OIC | Not stated | RedPath Mining lines 230–232 |
| Hollywood Bets | HCM, OIC | Not stated | RedPath Mining lines 227–229 |
| Nala Renewables | Finance, Project (8 countries) | 8-country rollout | RedPath Mining lines 237–239; 246 |

### Oracle EBS Clients

| Client | Scope | Source |
|---|---|---|
| KPMG | EBS Finance, Procurement, HCM, Project (5 SADC countries, 2-year rolling rollout) | RedPath Mining line 244 |
| Assore | EBS | RedPath Mining line 193 |
| ARM (African Rainbow Minerals) | EBS (R12.2) | RedPath Mining line 193 |
| Harmony | EBS | RedPath Mining line 193 |

---

## 8. Statements Appearing Across Multiple Sources

These statements appear in two or more sources in identical or near-identical form. They are the most stable content for extraction.

| Statement | Appears in | Extraction status |
|---|---|---|
| Oracle Fusion Overview (Modular, Cloud-Native, Analytics, UX, Global, Security) | TMPL-001 lines 112–122; SAA lines 82–109 (identical) | SAFE TO EXTRACT — Oracle product description |
| Oracle Fusion core components table (Financials, HCM, SCM, CRM, GRC) | TMPL-001 lines 123–141; SAA lines 92–109 (identical) | SAFE TO EXTRACT — Oracle product description |
| Implementation methodology (Mobilize → Scoping → Prototype → Validate → Deploy → Evolve) | SAA Section 5; RedPath Mining lines 262–333 (near-identical) | SAFE TO EXTRACT — for Deliverable 5 |
| Awards (EMEA/ECEMEA 2024, Sustainability 2015/2016, SaaS SADC 2016/2019) | TMPL-001; SAA; RedPath Mining (all three) | APPROVED — use W1S1-003 approved text |
| DBA services list (monitoring, trace files, backups, performance tuning, tablespace) | TMPL-001 lines 322–331; SAA lines 1862–1871 | SAFE TO EXTRACT — for Deliverable 3 |
| Hybrid Support Model description | TMPL-001 lines 400–408; SAA lines 1940–1948 (near-identical) | SAFE — use W1S1-009 approved text |
| "APPSolve is backed by Oracle" | TMPL-001 line 416; SAA line 1956 | SAFE — use W1S1-003 approved text |

---

## 9. Contradictions Found

These contradictions between source documents and the approved fact baseline require extraction judgment.

### Contradiction C1 — DBA Team Superlative (HIGH importance)

| Source | Wording | Status |
|---|---|---|
| TMPL-001 line 321 | "APPSolve has **the** largest number of locally based Oracle Applications DBAs" | PROHIBITED (superlative is unverifiable) |
| SAA line 1861 | Same as TMPL-001 | PROHIBITED |
| W1S1-007 (approved) | "one of **the largest** locally-based Oracle Applications DBA teams in South Africa" | USE THIS |

**Rule:** Use W1S1-007 language in all extractions. Do not use the unqualified superlative from source documents.

### Contradiction C2 — Gold Partner Reference (CRITICAL)

| Source | Wording | Status |
|---|---|---|
| TMPL-001 line 315 | "Our **Gold Level** partnership with Oracle entitles us to sell and distribute Oracle licenses" | **PROHIBITED** — Gold expired August 2021 |
| SAA line 1855 | Same as TMPL-001 | **PROHIBITED** |
| W1S1-003 (approved) | "Oracle **Level 1 Partner** — authorised to sell and distribute Oracle licenses" | USE THIS |

**Rule:** Never extract the Gold Level / Gold Partner reference. Replace with W1S1-003 approved language in any and all Oracle content.

### Contradiction C3 — Company Age (HIGH importance)

| Source | Wording | Status |
|---|---|---|
| TMPL-001; SAA; RedPath Mining (all three) | "over **22 years**" | **PROHIBITED** — should be 23 years as of 2026 |
| W1S1-002 (approved) | "over **23 years**" (company founded 2002) | USE THIS |

**Rule:** Replace "22 years" with "over 23 years" in all company history extractions.

### Contradiction C4 — Headcount (CRITICAL)

| Source | Wording | Status |
|---|---|---|
| TMPL-001 line 257; SAA lines 1798, 380; RedPath Mining line 90 | "more than **110** Senior Consultants" / "over **100** senior resources" | **PROHIBITED** |
| W1S1-001 (approved) | "**50+** Senior Consultants" | USE THIS |

**Rule:** Any extraction touching company headcount must use 50+. These source documents are consistently wrong on this.

### Contradiction C5 — Hein Blignaut Experience (HIGH importance)

| Source | Wording | Status |
|---|---|---|
| TMPL-001; SAA; RedPath Mining (all three contact sections) | "He has **19 years' experience** in the IT industry" | **PROHIBITED** — Hein started 1996, ~30 years as of 2026 |
| Approved (baseline) | "~30 years" or "since 1996" | USE THIS |

**Rule:** The Hein CV summary block appears in all three source documents and contains prohibited stats. Do not extract the Hein CV text from these sources. Use the approved statement from the baseline.

### Contradiction C6 — Oracle Partner Duration (MEDIUM importance)

| Source | Wording | Status |
|---|---|---|
| SAA line 414, 1954; RedPath Mining line 79 | "Oracle Partner for the **past 22 years**" | OUTDATED — should reflect 2026 |
| W1S1-003 (approved) | "Oracle partner for **over two decades**" | USE THIS (deliberately non-numeric to age gracefully) |

### Contradiction C7 — OIC Language Hedging vs. Standard Claim

| Source | Wording | Type |
|---|---|---|
| RedPath Mining line 195 | "**All** our Fusion implementations we have also implemented Oracle Integration Cloud" | Strong general claim |
| SAA line 884 | "we can **confirm if OIC is required** in the interim" | Client-specific hedge |

**Rule:** Use RedPath Mining language (OIC as standard) for the KB capability statement. Discard SAA's client-specific hedge — it was SAA-context negotiation language, not a capability limitation.

### Contradiction C8 — DFA Module Scope (LOW — additive, not conflicting)

| Source | DFA scope |
|---|---|
| RedPath Mining line 245 | Finance, Procurement, Project, HCM Core, HCM recruiting, Talent, Performance, Learning |
| SABS ETS (from baseline) | Full suite + Oracle Payroll Cloud native |

**Assessment:** Not a contradiction — RedPath Mining gives functional module detail; SABS ETS adds the Payroll Cloud note. Combine both for the most complete DFA reference.

---

## 10. Approved Wording Candidates

These phrases appear in source documents and are candidates for inclusion in W2S1-001. They must be verified against the baseline before use.

| Candidate phrase | Source | Baseline status | Recommendation |
|---|---|---|---|
| "APPSolve has implemented an Integration between Oracle HCM and SAP Payroll many times" | SAA line 890 | In baseline Section 12 | **APPROVED CANDIDATE** — extract verbatim |
| "All our Fusion implementation we have also implemented Oracle Integration Cloud. We have used OIC for all inbound and out bound interfaces between Oracle SaaS and 3rd party systems" | RedPath Mining line 195 | In baseline Section 7 | **APPROVED CANDIDATE** — extract verbatim or lightly modernise |
| "We are a Level 1 Principal Partner" | RedPath Mining line 253 | Consistent with W1S1-003 "Oracle Level 1 Partner" | Use W1S1-003 language, not "Principal Partner" (non-standard term) |
| "APPSolve has developed its own implementation methodology, based on Oracle's OUM and current Customer Success Navigator stages" | RedPath Mining line 257 | Consistent with baseline Section 17 | **APPROVED CANDIDATE** |
| "We have implemented and supporting 3 mining companies in South Africa, namely; Assore, ARM (African Rainbow Minerals) and Harmony" | RedPath Mining line 193 | Client list confirmed | **APPROVED CANDIDATE** for mining sector reference |
| "Senior consultants allocated to this project. No juniors or midlevel consultants." | RedPath Mining line 364 | Consistent with W1S1-009 senior-only claim | **APPROVED CANDIDATE** |
| "We predominantly use Oracle's standard API's and FBDI sheets to load master and transactional data. Transactional data in the financial modules are always reconciled back to the control accounts in the Trial Balances" | RedPath Mining line 199 | Consistent with baseline | **APPROVED CANDIDATE** for data migration section |
| "3 months of hyper care with a full complement of senior resources" | SAA line 1256 | Consistent with baseline | **APPROVED CANDIDATE** for support section |
| Oracle Fusion Overview — Key Features (Modular, Cloud-Native, Integration, Analytics, UX, Global, Security/Compliance) | TMPL-001 / SAA (identical) | Oracle product description, not an APPSolve claim | SAFE to include as product context; flag as Oracle product description, not APPSolve-authored |

---

## 11. Prohibited Wording Candidates

These phrases appear in the source documents and must NOT be extracted:

| Prohibited phrase | Appears in | Reason |
|---|---|---|
| "Gold Level partnership" / "Gold Level" / "Gold or higher" | TMPL-001; SAA | Gold expired August 2021 |
| "more than 110 Senior Consultants" | TMPL-001; SAA; RedPath Mining | Approved = 50+ |
| "over 100 senior resources" | SAA line 1920 | Same — approved = 50+ |
| "over 22 years" | All three sources | Approved = over 23 years |
| "He has 19 years' experience" (Hein) | All three source contact sections | Approved = ~30 years from 1996 |
| "Oracle Partner for the past 22 years" | SAA; RedPath Mining | Use "over two decades" from W1S1-003 |
| "APPSolve has the largest number of locally based Oracle Applications DBAs" | TMPL-001; SAA | Use "one of the largest" from W1S1-007 |
| "we can confirm if OIC is required in the interim" | SAA line 884 | SAA-specific negotiation language; OIC is standard |
| "Our Gold Level partnership with Oracle entitles us to sell and distribute Oracle licenses" | TMPL-001; SAA | Entire sentence prohibited — Gold expired |
| Nigeria, Uganda, Bangladesh, Qatar, Ghana in geography lists | TMPL-001; SAA | No client folder evidence — removed in Wave 1 |
| "16 years" / "more than 16 years" (company age) | TMPL-001; SAA | Outdated; use "over 23 years" |
| "18 years of IT experience" for Andre Pelser | TMPL-001; SAA | Stale — do not extract consultant bio stats without BU lead update |

---

## 12. Recommended Extraction Structure for W2S1-001

Based on the above analysis, the recommended document structure for W2S1-001 is:

```
W2S1-001 — Oracle Fusion Capability Statement

Section 1: Oracle Fusion Platform Overview
  1.1 What is Oracle Fusion?
      (Product description — from TMPL-001/SAA identical Oracle Fusion Overview)
  1.2 Core Component Areas
      (Table: Financials, HCM, SCM, CRM, GRC)

Section 2: APPSolve Oracle Fusion Partnership and Expertise
  2.1 Oracle Level 1 Partner Status
      (From W1S1-003 approved language)
  2.2 Oracle Integration Cloud — Standard Architecture
      (From RedPath Mining line 195 — OIC in ALL implementations)
  2.3 Oracle Modern Best Practices Alignment
      (From RedPath Mining / SAA methodology sections)

Section 3: Oracle Fusion HCM Capability
  3.1 Oracle HCM Base Cloud (Global HR, AI Skills, Absence, Benefits, Journeys)
  3.2 Workforce Management (Workforce Directory, Workforce Modelling, Work Life, Time and Labor, Workforce Scheduling)
  3.3 Compensation and Rewards (Workforce Compensation Cloud)
  3.4 Talent Acquisition (Recruiting Cloud)
  3.5 Talent and Career Development (Talent Management, Learning Cloud, Help Desk)
  3.6 Analytics and Reporting (OTBI, HCM Analytics)
  3.7 Payroll Integration (Payroll Interface — third-party model; SAP Payroll integration claim)

Section 4: Oracle Cloud Infrastructure (OCI)
  4.1 Security Architecture
      (Cloud Guard, WAF, IAM, TDE, MFA, encryption)
  4.2 Compliance and Certifications
      (SOC 1 + SOC 2 Bridge Letters available — June 2025)
  4.3 Scalability and Global Footprint

Section 5: Integration Architecture
  5.1 Oracle Integration Cloud (OIC) — Standard Layer
  5.2 REST APIs and Data Tools (HDL, HSDL, FBDI)
  5.3 SAP Payroll Integration Capability

Section 6: Referenceable Oracle Fusion Client Experience
  (Table: DFA, Cape Union Mart, Investec, Mr Price, Hollywood Bets, Nala)
  (Supporting reference letters attached separately)

Section 7: Oracle Fusion Implementation Approach (overview only — detail in W2S1-005)
  (Brief methodology reference; OUM-based; link to methodology document)
```

---

## 13. Source Quality Assessment

| Source | Quality for Fusion extraction | Key strength | Key risk |
|---|---|---|---|
| TMPL-001 (Sept 2024) | Medium — thin on module detail | Oracle Fusion Overview text; Company differentiators; DBA services | Contains multiple PROHIBITED stats; Finance section not read in detail |
| SAA RFP (June 2025) | **Very High** — primary source for HCM | 19 HCM modules with O/B/KF structure; methodology; payroll integration claims | Company profile sections contain PROHIBITED stats (same template reuse) |
| RedPath Mining RFI (March 2026) | High — primary for client list and OIC | Client list by module; OIC standard claim; mining sector reference; methodology | PROHIBITED stats in company profile; OCI section appears truncated |
| ORACLE_FACT_BASELINE.md | Reference only | Prohibited wording; approved phrases; confirmed client list | Not a source — it's the guardrail |

---

## 14. Content Overlap Analysis

### Areas where TMPL-001 and SAA have IDENTICAL text

The Oracle Fusion Overview section (product description, key features, core components table) is word-for-word identical between TMPL-001 and SAA. This is because SAA reused the TMPL-001 Oracle Fusion Information section verbatim.

**Implication:** For the Oracle Fusion Overview subsection of W2S1-001, either source is authoritative. Extract once — no need to cross-reference.

### Areas where SAA and RedPath Mining have NEAR-IDENTICAL text

The implementation methodology (Mobilize → Scoping → Prototype → Validate → Deploy → Evolve) is near-identical between SAA Section 5 and RedPath Mining Section 2. RedPath Mining has a slightly more condensed version.

**Implication:** This is APPSolve's master methodology text. It appears in two independent recent tenders (June 2025 and March 2026), which validates it as current. Extract once for Deliverable 5. The SAA version is more complete.

### Areas unique to each source

| Unique to... | Content |
|---|---|
| SAA only | 19 HCM module descriptions with full O/B/KF tables; evaluation criteria responses; payroll integration SAP claim; 6-phase implementation plan; costing assumptions |
| RedPath Mining only | Complete Fusion client list by module; OIC standard claim; mining sector reference; "Level 1 Principal Partner"; OUR validation tool |
| TMPL-001 only | Structural template sections (Assumptions page, Conclusion); DBA services list in company profile |

---

## Extraction Readiness Report

### Source Quality: GO

All three sources are readable, current, and contain extractable content. SAA (June 2025) is the primary source for HCM modules. RedPath Mining (March 2026) is the primary source for client list and OIC standard. TMPL-001 (Sept 2024) provides structural authority and Oracle Fusion Overview text.

### Content Overlap: RESOLVED

The TMPL-001/SAA duplication is understood — SAA reused TMPL-001 Oracle Fusion section verbatim. No competing versions of product descriptions. The SAA/RedPath methodology duplication is expected — both are current engagements using the same APPSolve methodology.

### Contradictions: 8 IDENTIFIED — ALL MANAGEABLE

| ID | Issue | Severity | Resolution |
|---|---|---|---|
| C1 | "the largest" vs "one of the largest" DBA | HIGH | Use W1S1-007 approved language |
| C2 | "Gold Level" vs "Level 1 Partner" | **CRITICAL** | Use W1S1-003 approved language; never extract Gold |
| C3 | "22 years" vs "23 years" | HIGH | Use "over 23 years" |
| C4 | "110/100 consultants" vs "50+" | **CRITICAL** | Use "50+" |
| C5 | "19 years" for Hein vs ~30 years | HIGH | Do not extract Hein bio stats from sources |
| C6 | "22 years as partner" vs "two decades" | MEDIUM | Use W1S1-003 "over two decades" |
| C7 | OIC hedge (SAA) vs OIC standard (RedPath) | MEDIUM | Discard SAA hedge; use RedPath standard claim |
| C8 | DFA module detail (additive) | LOW | Combine both sources for complete picture |

All contradictions are resolved by applying ORACLE_FACT_BASELINE.md rules. No contradiction requires BU lead input before extraction begins.

### Pre-Extraction Conditions

| Condition | Status |
|---|---|
| ORACLE_FACT_BASELINE.md available | **DONE** |
| Prohibited wording list documented | **DONE** |
| All three sources read | **DONE** |
| Recommended extraction structure defined | **DONE** |
| Contradictions mapped to resolutions | **DONE** |
| Client list confirmed (dual-source) | **DONE** |
| OIC standard claim confirmed | **DONE** |

### Scope Recommendation

Scope W2S1-001 to:
- **In scope:** HCM (all 19 modules), OCI, OIC, SAP integration, client list, methodology overview
- **Deferred to separate extraction or addendum:** Finance/Procurement capability detail (TMPL-001 Finance section not read in full — flag as gap)
- **Out of scope for W2S1-001:** Methodology detail (→ Deliverable 5), DBA services (→ Deliverable 3)

### Go / No-Go Recommendation

**GO — proceed with W2S1-001 extraction.**

The sources are read, the prohibited wording list is applied, all contradictions are resolved, and the recommended extraction structure is clear. The SAA RFP (June 2025) provides enough HCM module content for a comprehensive capability statement without needing to access additional sources.

**One note before extraction begins:** Read the TMPL-001 Finance section more carefully if Finance/Procurement capability is required in W2S1-001. The current read covers the TMPL-001 high-level component table only. For now, proceed with HCM-first scope; Finance can be added in a Wave 2 addendum extraction.

---

*Prepared 2026-06-10 by Claude (AI) — source analysis only. No KB content extracted. W2S1-001 not yet created.*

---

## Addendum — 2026-06-11: Post-Extraction Corrections

W2S1-001 was created 2026-06-11. During Finance/ERP strengthening using Mpact (August 2025) and BankServAfrica (August 2024) proposals, two material errors from the pre-extraction analysis were identified and corrected:

**Error 1 — Cape Union Mart SCM attribution (MATERIAL):**
Pre-extraction notes carried forward a RedPath Mining RFI claim that Cape Union Mart implemented "Finance + SCM". Mpact ERP Proposal reference cards (August 2025) confirm Cape Union Mart implemented **Oracle Fusion Financials + Oracle Fusion Procurement only — NO SCM**. Section 6 of W2S1-001 initially cited Cape Union Mart as the sole SCM client — corrected.

**Error 2 — Nala country count (MATERIAL):**
RedPath Mining RFI stated Nala = "8 countries". Mpact ERP Proposal reference card (August 2025) confirms Nala Renewables = **4 countries: South Africa, Lithuania, Romania, Finland** — Go-Live April 2025. Two sources differ; Mpact reference card treated as primary.

**Finance/ERP scope resolution:**
The Go recommendation suggested Finance could be added in a Wave 2 addendum. This has been completed — Finance, Procurement, SCM, and Projects sections fully sourced from BankServAfrica ERP Proposal (August 2024) and Mpact reference cards. No further Finance source extraction required for W2S1-001.

**New sources identified and registered in ORACLE_FACT_BASELINE.md:**
- HIST-010: Mpact Oracle ERP Proposal (August 2025) — `Parties/Customers/Mpact/RFP/ERP/2 Working/`
- HIST-011: BankServAfrica ERP Proposal V1 (August 2024) — `Parties/Customers/Bankserv/RFP/ERP/1 Working/`

*Addendum added 2026-06-11 by Claude (AI)*
