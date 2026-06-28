> **SUPERSEDED — DO NOT USE FOR PLANNING**
> This document was built on 3 Tender Pack proposals and pre-dates discovery of the 18,400-file historical corpus. Gap ratings for Oracle methodology, Acumatica content, and BeBanking content are incorrect — extensive source material exists in the corpus. Retained for historical reference only.
> Current state: see `MIGRATION_ANALYSIS.md`, `EXTRACTION_PLAN.md`, and `00_Governance/KNOWLEDGE_BASE_STATUS.md`.

# Tender Knowledge Base — Content Gap Analysis
**Date:** 2026-06-05
**Scope:** Pre-migration assessment of content sufficiency by business unit
**Input:** `MIGRATION_ANALYSIS.md` (full Tender Pack inventory)
**Status:** Analysis only — no files migrated, no content authored

---

## How to Read This Document

Each content category is rated for each business unit:

| Rating | Meaning |
|---|---|
| **Strong** | Content exists, is current, and is substantially ready for tender use |
| **Partial** | Content exists but is outdated, incomplete, or not in tender-ready format |
| **Weak** | Minimal content exists; significant authoring required before use |
| **Missing** | No content exists; must be authored from scratch |

**Impact** indicates how heavily this gap affects tender outcomes:
- `Critical` — evaluators score this category heavily; absence likely causes a loss
- `High` — frequent requirement; absence forces last-minute rushed writing
- `Medium` — important but not always scored; gap manageable short-term
- `Low` — nice to have; absence rarely decisive

---

## Executive Summary

| Business Unit | Overall Readiness | Primary Risk |
|---|---|---|
| **Oracle** | Partial | Strong compliance and references; zero methodology content; no standard sections |
| **Acumatica** | Weak | Company profile and 5 references exist; no methodology, no standard responses, thin cert coverage |
| **BeBanking** | Missing | Essentially no tender-ready content exists for this BU |

**The single largest gap across all three business units is the complete absence of methodology documents.** Every tender evaluation scores methodology. Zero methodology content exists anywhere in the Tender Pack.

**BeBanking represents the highest risk exposure.** APPSolve appears to be actively selling BeBanking solutions, but the knowledge base would be built entirely from scratch. Any BeBanking tender submitted today draws on nothing structured.

---

## Section 1: Oracle Content Assessment

### 1.1 Capability Statements
**Rating: Partial | Impact: High**

**What exists:**
- `APPSolve Company Profile - Oracle 2025.pdf` — general company profile covering Oracle services
- `APPSolve Company Profile (International) 2024.pdf` — international-facing version
- `APPSolve Company Profile (SA) 2024.pdf` — SA-facing version
- DOCX editable version of the 2024 profile

**Gaps:**
- The company profiles are marketing documents, not structured capability statements. They do not follow the Tender KB `CAP` template format (verbatim-usable intro text, supporting evidence table, typical tender sections).
- No service-area-specific capability statements exist. Evaluators who ask "describe your capability to deliver Oracle EBS Managed Services" or "describe your Oracle Cloud HCM implementation experience" need a focused 1–2 page response, not a 20-page company profile.

**Missing service-area capability statements:**
| Service Area | Exists | Must Author |
|---|---|---|
| Oracle EBS Implementation | No | Yes |
| Oracle EBS Managed Support | No | Yes |
| Oracle Cloud Finance (Fusion) | No | Yes |
| Oracle Cloud HCM | No | Yes |
| Oracle Cloud SCM / Procurement | No | Yes |
| Oracle Cloud Projects | No | Yes |
| Oracle Integration Cloud (OIC) | No | Yes |
| Oracle APEX / Developer | No | Yes |
| OCI Infrastructure / Managed Services | No | Yes |

**Action required:** Author 9 service-area capability statements. Source material: company profile (broad claims), historical proposals (specific project descriptions), reference letters (outcome evidence).

---

### 1.2 Methodology Documents
**Rating: Missing | Impact: Critical**

**What exists:** Nothing.

**Gaps:**
There are no methodology documents of any kind in the Tender Pack — no delivery framework, no implementation playbook, no project management approach, no support model description. This is the most significant Oracle content gap.

Typical tender sections that need methodology content:
- "Describe your implementation methodology"
- "How do you manage project risks?"
- "Describe your change management approach"
- "What is your testing methodology?"
- "How do you manage go-live and cutover?"
- "Describe your post-go-live support model"

**Missing methodology documents:**
| Methodology | Source Material Available | Must Author |
|---|---|---|
| Oracle EBS Implementation Methodology | Partial (historical proposals contain fragments) | Reconstruct + augment |
| Oracle Cloud (Fusion) Implementation Methodology | Partial (proposal fragments) | Reconstruct + augment |
| Oracle Managed Services / Support Methodology | Nothing | Author from scratch |
| OCI Infrastructure Deployment Methodology | Nothing | Author from scratch |
| OIC Integration Delivery Methodology | Nothing | Author from scratch |
| APPSolve Project Management Framework | Nothing | Author from scratch |
| Data Migration Methodology | Nothing | Author from scratch |
| Testing and UAT Methodology | Nothing | Author from scratch |
| Change Management Approach | Nothing | Author from scratch |

**Extractable from existing sources:** The 3 historical proposals (`Mauritius Telecom HCM`, `SARB template`, `PPro 2024`) likely contain methodology sections. These should be read and deconstructed before authoring begins — they may provide 30–50% of a draft methodology for Cloud and EBS.

**Action required:** Read and extract methodology content from 3 historical proposals, then author structured methodology documents for all 9 areas above.

---

### 1.3 Reference Library
**Rating: Partial | Impact: High**

**What exists (strong):**
- 7 signed Oracle support reference letters (Adcock Ingram, ARM, Assore, Cape Union Mart, MTN, Nala, WITS) — all current
- 9 root-level signed reference PDFs (Harmony 2024, Investec 2023, Mr Price 2024, Stellenbosch University 2025, MTN 202507, Oracle SA endorsement ×2)
- Oracle Recruiting Cloud references for Hollywoodbets and Mr Price (DOCX, unsigned)

**Gaps:**
- **No structured sidecar data exists** for any reference. The KB requires sidecar files with: project scope, services rendered, project value band, outcomes, approved quotable text, contact name. All of this must be authored for each reference — it cannot be derived from filename alone.
- **Sector coverage is narrow.** Current signed references are dominated by JSE-listed corporate and financial services. Government/public sector references are missing. Government tenders often require public sector experience specifically.
- **ORC references are unsigned DOCX.** Hollywoodbets and Mr Price Oracle Recruiting Cloud references have no signed PDF. These cannot be cited in tenders until signed.
- **No implementation project references.** The support references describe ongoing managed support relationships. Evaluators asking for "references where you implemented an Oracle system" need different evidence — implementation references. The proposals suggest implementation work was done, but no implementation-specific reference letters are in the active set.
- **No BeBanking-context Oracle references.** Historical BankServ and FNB letters (archive) may cover Oracle EBS + payment integration but are scanned, outdated, and unverified.

**Missing:**
| Gap | Impact |
|---|---|
| Sidecar metadata for all ~16 Oracle references | High — AI cannot use references without structured data |
| Government/public sector references | High — needed for public procurement tenders |
| Oracle implementation references (not just support) | High — evaluators distinguish implementation from support |
| Signed ORC references (Hollywoodbets, Mr Price) | Medium |
| Oracle APEX / Developer references | Medium |
| OCI / cloud infrastructure references | Medium |

---

### 1.4 Executive Summaries
**Rating: Missing | Impact: High**

**What exists:** Nothing designed for this purpose.

**Gaps:**
Every tender response opens with an executive summary. Currently there is no pre-written, reusable executive summary for any Oracle service area. The company profiles contain some executive-style language but are not formatted for insertion into a tender response.

**Missing:**
| Executive Summary | Must Author |
|---|---|
| APPSolve Oracle Practice — General | Yes |
| Oracle EBS Managed Support positioning | Yes |
| Oracle Cloud (Fusion) implementation positioning | Yes |
| OCI / Infrastructure positioning | Yes |
| Why APPSolve for government Oracle tenders | Yes |

**Source material:** Company profiles, Oracle Partner certificate positioning, reference letter outcomes. Authoring effort: medium — factual claims exist; tender-ready prose must be written.

---

### 1.5 Standard Tender Responses
**Rating: Weak | Impact: High**

**What exists:**
- 3 historical proposal DOCX files containing reusable section content
- SBD/MBD government form templates (blank — not pre-filled)

**Gaps:**
The 3 proposals are complete documents, not deconstructed into reusable standard sections. To build a standard response library, these proposals must be read, good sections extracted, and converted into structured reusable blocks tagged by topic.

**Estimated reusable content from existing proposals:** 40–60% of an Oracle Cloud or EBS tender, with significant editing required.

**Standard sections that must be authored or extracted:**
| Section | Source | Status |
|---|---|---|
| Company Background and History | Company profiles + proposals | Extract + reformat |
| Oracle Partnership and Credentials | Partner certs + company profile | Extract + update |
| Staffing and Resource Approach | CVs + proposals | Extract + reformat |
| Project Management Approach | Proposals (if present) | Extract + augment |
| Quality Assurance Approach | Unknown — likely missing | Author from scratch |
| Risk Management Framework | Unknown — likely missing | Author from scratch |
| Support and Maintenance Model | Company profile (partial) | Author from scratch |
| BEE / Transformation Commitment | BEE cert + company profile | Extract + structure |
| Pricing Approach / Rate Card Narrative | Rate cards exist (raw Excel) | Author narrative |
| References Summary Section | Reference letters exist | Author structured summary |

---

## Section 2: Acumatica Content Assessment

### 2.1 Capability Statements
**Rating: Weak | Impact: High**

**What exists:**
- `APPSolve Company Profile - Acumatica 2025.pdf` — general Acumatica company profile

**Gaps:**
Same structural problem as Oracle: a marketing profile exists but no service-area-specific, tender-ready capability statements. Acumatica tenders frequently ask for module-specific capability (e.g., "describe your Manufacturing ERP experience" or "how do you deliver Acumatica Payroll?").

**Missing service-area capability statements:**
| Service Area | Exists | Must Author |
|---|---|---|
| Acumatica Manufacturing | No | Yes |
| Acumatica Distribution / Inventory | No | Yes |
| Acumatica Payroll | No | Yes |
| Acumatica Finance | No | Yes |
| Acumatica Field Service | No | Yes |
| Acumatica CRM | No | Yes |
| Acumatica Support / Managed Services | No | Yes |
| Acumatica Reporting / BI | No | Yes |

**Note on Gold Partner status:** The Acumatica Gold Partner certificate was referenced in the KB example data. If this certificate exists in the Tender Pack (not clearly identified in inventory as a standalone cert), its positioning must be included in all Acumatica capability statements.

---

### 2.2 Methodology Documents
**Rating: Missing | Impact: Critical**

**What exists:** Nothing.

**Gaps:**
No Acumatica implementation methodology exists anywhere in the Tender Pack. Acumatica uses a structured SureStep implementation methodology — APPSolve should have an adapted version. No evidence of this in the inventory.

**Missing:**
| Methodology | Source Material | Must Author |
|---|---|---|
| Acumatica Implementation Methodology (SureStep) | Nothing | Author from scratch |
| Data Migration Methodology (Acumatica context) | Nothing | Author from scratch |
| Go-Live and Cutover Approach | Nothing | Author from scratch |
| Acumatica Support Model | Nothing | Author from scratch |
| Manufacturing ERP Delivery Approach | Nothing | Author from scratch |
| Payroll Implementation Approach | Nothing | Author from scratch |
| Training and Enablement Approach | Nothing | Author from scratch |

**Action required:** This content must be authored entirely from scratch. Recommended approach: workshop with Acumatica delivery team to extract tacit methodology knowledge, then document.

---

### 2.3 Reference Library
**Rating: Weak | Impact: Critical**

**What exists:**
- 5 signed reference letters: ATS, DSSSA, FuelU2, Interconnect Systems, Maxiflex

**Gaps:**
- **5 signed references is thin.** Oracle has ~16. Acumatica tenders asking for 3+ references can be satisfied, but there is no redundancy and no sector diversity. If a tender requires sector-specific references (e.g., "manufacturing clients" or "clients with >200 employees"), the options are very limited.
- **13 unsigned templates outstanding.** The 13 DOCX templates (At Source, Chemunique, Dukathole, etc.) represent clients who have not yet signed. Until signed, these cannot be cited.
- **No sidecar metadata.** As with Oracle, no structured reference data exists — project scope, outcomes, value band, approved quotable text must all be authored for each of the 5 signed letters.
- **Sector coverage:** All 5 references appear to be SME clients. No enterprise-scale Acumatica implementation reference visible.
- **No module-specific tagging.** Without reading the letters, it is unknown which Acumatica modules each reference relates to. A tender asking for "Acumatica Manufacturing references" cannot be answered without this.

**Missing:**
| Gap | Impact |
|---|---|
| Sidecar metadata for all 5 Acumatica references | Critical — cannot use in AI retrieval without structure |
| At least 3 additional signed references | High — thin coverage, no redundancy |
| Enterprise-scale Acumatica reference | High — missing entirely |
| Module-tagged reference library | High — needed for module-specific tender questions |
| References with quantified business outcomes | Medium — most letters likely describe services, not measurable results |

---

### 2.4 Executive Summaries
**Rating: Missing | Impact: High**

**What exists:** Nothing.

**Missing:**
| Executive Summary | Must Author |
|---|---|
| APPSolve Acumatica Practice — General | Yes |
| Acumatica Gold Partner positioning | Yes |
| Manufacturing ERP positioning | Yes |
| Why APPSolve for SME / mid-market ERP | Yes |

---

### 2.5 Standard Tender Responses
**Rating: Missing | Impact: Critical**

**What exists:** Nothing. No historical Acumatica tender proposals were found in the Tender Pack.

**Gaps:**
This is the most exposed gap in the entire KB. Oracle has 3 historical proposals to draw from. Acumatica has zero. Every section of every Acumatica tender must be written from scratch with no prior content to extract from.

**All sections must be authored from scratch:**
| Section | Status |
|---|---|
| Company Background (Acumatica context) | Author from scratch |
| Acumatica Partnership and Credentials | Author from scratch |
| Implementation Approach | Author from scratch |
| Staffing and Team Composition | Author from scratch |
| Module-Specific Responses (Manufacturing, Payroll, etc.) | Author from scratch |
| Support and Maintenance | Author from scratch |
| Training Approach | Author from scratch |
| Pricing Narrative | Author from scratch |
| References Section | Author from scratch |

**Priority action:** Source at least 1–2 previously submitted Acumatica tender responses (even non-KB copies) to use as extraction source before authoring begins. Check if any were submitted outside the Tender Pack folder.

---

## Section 3: BeBanking Content Assessment

### 3.1 Capability Statements
**Rating: Missing | Impact: Critical**

**What exists:** Nothing. There is no BeBanking-specific document of any kind in the current Tender Pack, other than two historical archive reference letters (BankServ, FNB EBS) and two uninvestigated DOCX templates (Tiger, SAA).

**Gaps:**
BeBanking is described in `AI_CONTEXT.md` as covering: host-to-host banking, supplier payments, payroll payments, forex payments, and ERP integration (SAP, Oracle, Acumatica). None of these service areas have any capability statement content.

**All BeBanking capability statements must be authored from scratch:**
| Service Area | Exists | Must Author |
|---|---|---|
| BeBanking Platform Overview | No | Yes |
| Host-to-Host Banking Integration | No | Yes |
| Supplier Payment Automation | No | Yes |
| Payroll Payment Processing | No | Yes |
| Forex Payment Management | No | Yes |
| ERP Integration (Oracle / SAP / Acumatica) | No | Yes |
| Banking Regulatory Compliance (SARB, NPS) | No | Yes |
| Security and Fraud Controls | No | Yes |

---

### 3.2 Methodology Documents
**Rating: Missing | Impact: Critical**

**What exists:** Nothing.

**Missing:**
| Methodology | Must Author |
|---|---|
| BeBanking Onboarding / Integration Methodology | Yes |
| Bank Connectivity Setup Methodology | Yes |
| ERP Integration Delivery Methodology | Yes |
| Testing and Parallel Run Approach | Yes |
| Go-Live and Cutover Approach | Yes |
| Ongoing Reconciliation and Support Model | Yes |

**Note:** The BeBanking delivery methodology is likely highly specific to how the product works and how banks and clients integrate with it. This content can only be authored by subject matter experts who understand the BeBanking platform.

---

### 3.3 Reference Library
**Rating: Missing | Impact: Critical**

**What exists:**
- `BankServ APPSolve Reference Letter.pdf` — archive, scanned, historical (~2017–2019)
- `FNB Client Reference.pdf` — archive, scanned, historical (~2017–2019). Also `FNB_EBS_REFERENCE2017.pdf` — this is an Oracle EBS reference, not a BeBanking reference.
- `Tiger Reference Letter BeBanking SAP.docx` — template only, unsigned, uninvestigated
- `SAA Tiger Reference Letter SAP Integration.docx` — template only, unsigned, uninvestigated

**Gaps:**
- The two archive references (BankServ, FNB) are 7–8 years old, likely scanned, and unverified. Their usability in a 2026 tender is questionable. A client from 2018 cannot be assumed to still endorse APPSolve.
- No current signed BeBanking reference letters exist.
- Tiger and SAA templates are uninvestigated — it is unknown whether these projects were completed, whether the clients are willing to sign, or what the scope was.
- The reference library for BeBanking is effectively empty for practical tender use.

**Missing:**
| Gap | Impact |
|---|---|
| At least 3 current signed BeBanking references | Critical |
| References that name specific banking functionality (host-to-host, payroll, forex) | Critical |
| References from banking sector clients | Critical |
| References from corporate clients using BeBanking for supplier payments | High |

**Immediate action required:** Identify current active BeBanking clients who can provide reference letters. The Tiger and SAA DOCX templates should be investigated — if the work was done, these clients should be asked to sign.

---

### 3.4 Executive Summaries
**Rating: Missing | Impact: Critical**

**What exists:** Nothing.

**Missing:**
| Executive Summary | Must Author |
|---|---|
| BeBanking Platform — What It Is | Yes |
| Why APPSolve / BeBanking for Corporate Treasury | Yes |
| Why APPSolve / BeBanking for Banking Sector | Yes |
| BeBanking + ERP Integration Value Proposition | Yes |

**Note:** BeBanking executive summaries will require input from product management / business owners who understand the competitive positioning. This is not something that can be inferred from the existing document inventory.

---

### 3.5 Standard Tender Responses
**Rating: Missing | Impact: Critical**

**What exists:** Nothing.

All BeBanking tender response content must be authored from scratch. This is the most underdeveloped BU in the knowledge base.

---

## Section 4: Cross-BU Gaps

These gaps affect all three business units and every tender APPSolve submits.

| Gap | Impact | Notes |
|---|---|---|
| **APPSolve Company Background — standard section** | Critical | No pre-written, reusable "About APPSolve" section suitable for tender insertion exists. Company profiles serve this role but are not structured as extract-and-paste tender sections. |
| **BEE / Transformation Commitment section** | Critical | Required in every government tender. Must include current Level, BBBEE certificate reference, employment equity data, skills development commitments. No pre-written section exists. |
| **POPIA / Data Protection Compliance statement** | High | Tenders increasingly require POPIA compliance statements. Nothing exists. |
| **Project Management Approach — standard section** | High | Generic project governance, RACI, escalation framework, status reporting approach. Fragments may be in historical proposals but no standalone document. |
| **Staffing and Resourcing Approach — standard section** | High | How APPSolve assembles project teams, manages subcontractors, ensures continuity. Not documented. |
| **Quality Assurance Framework** | High | QA approach, defect management, acceptance criteria. Not documented anywhere. |
| **Training and Enablement Approach** | Medium | Applies across Oracle, Acumatica, BeBanking. Not documented. |
| **APPSolve References Summary Table** | High | A structured table of all references by BU, client, sector, scope — ready to insert into a tender response. Does not exist; must be assembled and maintained. |
| **Testimonial / Quote Bank** | Medium | Approved verbatim quotes extracted from signed reference letters for use in proposals. Does not exist. |
| **Pricing Approach / Commercial Narrative** | High | How APPSolve structures and presents pricing. Raw rate cards exist but no narrative or guidance document. |
| **Approved CV Format / Shell** | Medium | CV template used in tenders for a consistent look. `AF Resources CV.xlsx` suggests a format exists but it is not in the KB. |
| **Subcontractor / Partner Management section** | Medium | How APPSolve manages JV partners (Imbasa, Intecon). QSE partner docs exist in Tender Pack but no narrative. |

---

## Section 5: Gap Priority Rankings

Ranked by impact on tender win rate and authoring urgency.

| Rank | Gap | BU | Impact | Authoring Effort | Source Material Available |
|---|---|---|---|---|---|
| 1 | Methodology documents — all service areas | All | Critical | High | Partial (Oracle proposals only) |
| 2 | BeBanking — all content (entire BU) | BeBanking | Critical | Very High | None |
| 3 | Acumatica standard tender responses | Acumatica | Critical | High | None |
| 4 | Oracle standard tender responses | Oracle | Critical | Medium | 3 historical proposals |
| 5 | Executive summaries — all BUs | All | High | Medium | Company profiles |
| 6 | Reference sidecar metadata — Oracle | Oracle | High | Medium | 16 signed reference PDFs |
| 7 | Acumatica capability statements (module-level) | Acumatica | High | Medium | Company profile |
| 8 | BeBanking current signed references | BeBanking | Critical | High (chase clients) | 2 archive letters |
| 9 | Oracle capability statements (service-level) | Oracle | High | Medium | Company profile + proposals |
| 10 | Reference sidecar metadata — Acumatica | Acumatica | High | Low-Medium | 5 signed reference PDFs |
| 11 | Acumatica reference library expansion | Acumatica | High | High (chase clients) | 13 unsigned templates |
| 12 | BEE / Transformation standard section | Cross | Critical | Low | BEE cert + company profile |
| 13 | Company Background standard section | Cross | High | Low | Company profiles |
| 14 | Project Management Approach | Cross | High | Medium | Proposal fragments |
| 15 | Acumatica methodology documents | Acumatica | Critical | High | None |
| 16 | Oracle implementation references | Oracle | High | High (chase clients) | None signed |
| 17 | ORC references — get signed | Oracle | Medium | Low (chase 2 clients) | Hollywoodbets + Mr Price DOCX |
| 18 | POPIA compliance statement | Cross | High | Low | None |
| 19 | Quality Assurance Framework | Cross | High | Medium | None |
| 20 | Testimonial / Quote Bank | Cross | Medium | Medium | 16+ signed reference PDFs |

---

## Section 6: Recommended Authoring Sequence

### Phase 1 — Immediate (before first tender submission)
Items that can be authored quickly using existing material as source:

1. **Company Background standard section** — draw from company profiles (1 day)
2. **BEE / Transformation standard section** — draw from BEE cert + company profile (half day)
3. **Oracle references sidecar metadata** — read each of the 16 signed reference PDFs and fill in the structured fields (2–3 days)
4. **Acumatica references sidecar metadata** — read 5 signed reference PDFs (half day)
5. **References summary table** — compile from sidecars once done (1 day)

### Phase 2 — Short-term (within 4 weeks)
Items requiring extraction from existing proposals + focused authoring:

6. **Read and deconstruct 3 Oracle historical proposals** — extract reusable sections, methodology fragments, capability statements (2 days reading + analysis)
7. **Oracle EBS and Cloud capability statements** (6 priority service areas) — draw from proposals + company profile (3–4 days)
8. **Oracle executive summaries** — 4 versions (2 days)
9. **Oracle standard tender sections** — Project Management, Staffing, Support Model, QA (3–4 days)
10. **Oracle methodology — EBS and Cloud** — reconstruct from proposal fragments + augment (3–4 days)

### Phase 3 — Medium-term (within 8 weeks)
Items requiring SME input and fresh authoring:

11. **Acumatica capability statements** — workshop with Acumatica practice lead (1 day workshop + 3 days authoring)
12. **Acumatica methodology documents** — workshop with Acumatica delivery team (1 day workshop + 3–4 days authoring)
13. **Acumatica executive summaries** — 4 versions (1–2 days)
14. **Acumatica standard tender responses** — all sections (5–6 days)
15. **OCI and OIC methodology documents** (Oracle) — workshop with Oracle technical lead (3 days)
16. **Chase outstanding reference letters** — 3 Oracle + 10 Acumatica + 2 BeBanking investigation (ongoing)

### Phase 4 — Strategic priority (within 12 weeks)
BeBanking requires dedicated effort from subject matter experts:

17. **BeBanking product briefing** — interview BeBanking product owner / sales lead (1 day)
18. **BeBanking capability statements** — all 8 service areas (4–5 days authoring)
19. **BeBanking executive summaries** (3–4 days)
20. **BeBanking methodology documents** — onboarding, integration, support (3–4 days)
21. **BeBanking standard tender responses** (4–5 days)
22. **BeBanking reference letters** — identify and engage 3+ active clients (ongoing)

---

## Section 7: Content That Must Be Authored vs Extracted

| Content Item | Source | Action |
|---|---|---|
| Oracle EBS methodology fragments | Historical proposals (Mauritius Telecom, SARB, PPro) | Read → extract → structure → augment |
| Oracle Cloud methodology fragments | Same proposals | Read → extract → structure → augment |
| Company background text | Company profiles (2024/2025) | Extract → reformat for tender insertion |
| Oracle service descriptions | Company profiles | Extract → expand into service-area capability statements |
| BEE commitment statement | BEE cert + company profile | Draft → verify against cert data |
| Oracle reference project details | Signed reference PDFs | Read → populate sidecar structured fields |
| Acumatica reference project details | 5 signed Acumatica PDFs | Read → populate sidecar structured fields |
| Oracle partner credentials | Oracle Partner 2026 certs | Extract claims → verify → include in capability statements |
| Testimonial quotes | All signed reference PDFs | Read → identify quotable sentences → seek approval |
| Approved CV format | `AF Resources CV.xlsx` | Investigate → adopt as KB standard |
| All BeBanking content | None | Author from scratch with SME input |
| Acumatica all standard sections | None | Author from scratch with SME input |
| All methodology detail | None (beyond proposal fragments) | Author from scratch with delivery team input |
| Executive summaries | Company profiles + proposals | Draft → review with leadership |
| POPIA compliance statement | None | Author from scratch with legal input |
| QA framework | None | Author from scratch with delivery team input |

---

## Section 8: Authoring Effort Summary

| Effort Level | Content Items | Estimated Days |
|---|---|---|
| **Extract and reformat** (existing source material, light effort) | Company background, BEE statement, Oracle reference sidecars, references summary table | 5–7 days |
| **Extract and augment** (proposals exist; heavy editing and structuring needed) | Oracle methodology (EBS, Cloud), Oracle standard sections, Oracle capability statements | 10–15 days |
| **Author from scratch with source material** (company profiles, cert data) | Executive summaries (all BUs), Acumatica capability statements | 8–12 days |
| **Author from scratch with SME input required** | Acumatica methodology, Acumatica standard responses, Oracle OCI/OIC methodology, POPIA statement, QA framework | 15–20 days |
| **Author from scratch with product briefing required** | All BeBanking content | 15–20 days |
| **Chase and obtain from clients** | 3 Oracle outstanding refs, 10 Acumatica outstanding refs, 2 BeBanking potential refs | Ongoing |

**Total estimated authoring effort: 53–74 working days** (one person, full-time equivalent).
In practice, this would be distributed over 3–6 months alongside active tender work.

---

*End of Content Gap Analysis.*
*Next step: Review and prioritise. Confirm Phase 1 items for immediate authoring.*
*This document should be updated as content is authored and gaps are closed.*
