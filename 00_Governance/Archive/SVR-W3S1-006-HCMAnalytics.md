---
document_id: SVR-W3S1-006
title: "Source Validation Report — Oracle HCM Analytics & Workforce Intelligence"
version: "1.0"
status: "AUTHORISED — All 5 OI items CLOSED 2026-06-13"
created: "2026-06-13"
created_by: "Claude (AI — Wave 3 SVR)"
extraction_readiness: "AUTHORISED 2026-06-13 — All 5 OI items closed; extraction may proceed"
wave: "3"
deliverable: "W3S1-006"
---

> **SVR AUTHORISED 2026-06-13 — All 5 OI items closed. Extraction may proceed. Candidate Draft production authorised.**

---

# Source Validation Report: W3S1-006
## Oracle HCM Analytics & Workforce Intelligence

**Wave 3 | APPSolve Oracle Business Unit**
*Document ID: SVR-W3S1-006 | Version: 1.0 | Date: 2026-06-13*

---

## Section 1: Executive Summary

This Source Validation Report (SVR) covers the full corpus review and source classification for the W3S1-006 Oracle HCM Analytics & Workforce Intelligence capability statement. The corpus review was conducted against all Wave 3 sources — HIST-006, HIST-007, HIST-014, HIST-015, HIST-016, HIST-017 — and the ORACLE_FACT_BASELINE.

**Key finding: the analytics landscape across Oracle Fusion HCM comprises four distinct capability tiers that must be cleanly separated throughout the Candidate Draft. Conflating these tiers is the primary governance risk for this statement.**

| Tier | Product | Licensing | Implementation model |
|---|---|---|---|
| Tier A | OTBI — Oracle Transactional Business Intelligence | Included in Oracle HCM license | Standard component — configured in every HCM implementation |
| Tier B | BI Publisher | Included in Oracle HCM license | Standard component — used for formatted report output |
| Tier C | Oracle HCM Analytics (OAX) | **Separately licensed** | Separately implemented — requires dedicated project |
| Tier D | Fusion Analytics Warehouse (FAW) | Underpinning of OAX — not separately positioned | Delivered as part of OAX implementation |

**Implementation evidence summary:**
- OTBI: Confirmed in every Oracle HCM implementation APPSolve has delivered. Hollywood Bets BOM explicitly includes "10 Custom reports" (OTBI). RedPath Mining RFI (HIST-008) confirms "APPSolve developers have extensive experience in writing OTBI and BI Publisher reports."
- OAX: **Zero confirmed client implementations.** OAX capability is described in HIST-006 (SAA — not awarded) and HIST-014 (CCBA — not awarded, restricted). No referenceable client. No internal corroboration client. This is platform capability evidence only.
- Predictive/ML analytics: OAX-exclusive capability. Not available in OTBI. Must not be framed as APPSolve delivery capability without OAX implementation evidence.

**Extraction readiness: AUTHORISED 2026-06-13.** All 5 OI items closed by BU Lead. Extraction may proceed. See Section 10 for closed decisions.

---

## Section 2: Source Evidence Classification

### 2.1 Source Documents Reviewed

| Source ID | Document | Date | Analytics relevance | Classification |
|---|---|---|---|---|
| **HIST-006** | APPSolve SAA HCM RFP Response | June 2025 | **Primary — 73 analytics hits.** Dedicated OAX module section (paras 461–494). Comprehensive Analytics & Reporting section (paras 1182–1195). OTBI described as "primary reporting tool within Fusion HCM." OAX described as "specialized module." BI Publisher referenced (para 1127). FAW mentioned (para 1210). Predictive analytics tied to OAX (para 1191). Not awarded — platform capability source only. SAA never named. | Tier 2 — Platform Capability (not awarded) |
| **HIST-007** | Hollywood Bets Accepted Proposal V5.0 | April 2023 | **Low — 2 incidental hits.** BOM (paras 56–66) includes "10 Custom reports and 6 Custom Workflows" — OTBI standard. Para 576: "We recommend the acquisition of a third-party reporting tool" — advisory note implying standard OTBI alone may not satisfy all reporting needs. OAX absent from BOM. | Tier 1 — Implementation Evidence (OTBI only) |
| **HIST-008** | RedPath Mining RFI Reply | March 2026 | **Low — 2 targeted hits. High value for OTBI.** Para 204–205: "APPSolve developers have extensive experience in writing OTBI and BI Publisher reports. Also using Visual Builder Studio (VB Studio) for Oracle Redwood pages." Active implementation in progress. | Tier 2 — Platform Capability (pipeline; OTBI confirmed developer capability) |
| **HIST-015** | Afrocentric HCM Proposal V4.0 | 2023 | **Delivery assumptions — 7 hits.** Para 467: "standard delivered reports and dashboards will be used to satisfy reporting requirements." Para 502: same assumption for recruiting. Para 511: "Oracle Learning Cloud does not include any Learning Reports or Dashboards" — key standing caveat. No OAX reference. | Tier 3 — Delivery Methodology and Assumptions |
| **HIST-014** | CCBA Oracle HCM Solution V2.0 | May 2025 | **54 analytics hits — RESTRICTED.** Dedicated OAX section (paras 591–624) mirrors HIST-006. Additional Strategic Workforce Planning section (paras 626–663) not present in HIST-006. Not awarded. CCBA never named. **Extraction support use only.** | RESTRICTED — extraction support; CCBA never named |
| **HIST-016** | SABS ETS Oracle Fusion RFP Response | Dec 2025 | **Zero analytics hits.** Reference corroboration only — no analytics content. | No analytics evidence |
| **HIST-017** | SAA HCM Additional Information | June 2025 | **1 incidental hit.** Utilisation reporting reference only. Not relevant to analytics capability. | No analytics evidence |

---

## Section 3: Product Architecture and Capability Boundary Analysis

### 3.1 Oracle Transactional Business Intelligence (OTBI) — Tier A

**Source authority:** HIST-006 paras 171–175, 1184–1188; HIST-008 paras 204–205; HIST-007 BOM (10 custom reports); ORACLE_FACT_BASELINE Section 4.1

**Product description from HIST-006 paras 1184–1188:**
> "Oracle Transactional Business Intelligence (OTBI): This is the primary reporting tool within Fusion HCM itself. OTBI provides real-time access to transactional data, allowing users to create reports on current HR operations (e.g., headcount, turnover, absence, payroll). Oracle delivers numerous pre-built reports and dashboards tailored to different HR roles (e.g., HR Generalist, Compensation Manager, Recruiter). Users can create their own custom reports and analyses using a drag-and-drop interface, without requiring technical skills. OTBI reports and dashboards can be embedded directly within HCM pages, providing contextual insights to users within their workflows."

**Capability boundary — OTBI includes:**
- Real-time operational reports on live HCM transactional data
- Pre-built role-based reports and dashboards (delivered by Oracle)
- Custom user-built analyses (drag-and-drop; no coding required)
- Embedded analytics within HCM module pages
- Headcount, turnover, absence, payroll, recruitment pipeline, performance distribution reporting
- Custom formatted reports via BI Publisher (see Section 3.2)
- Custom audit reports (HIST-006 para 1127)

**OTBI does NOT include:**
- ML/predictive workforce analytics — OAX only
- Cross-functional analytics (HCM + Finance + SCM combined) — OAX only
- Pre-built 50+ KPI library covering DEI, attrition trends, talent acquisition analytics — OAX only

**APPSolve delivery evidence:**
- Hollywood Bets V5.0 BOM (April 2023): "10 Custom reports and 6 Custom Workflows" — OTBI confirmed in scope
- RedPath Mining RFI (March 2026): "APPSolve developers have extensive experience in writing OTBI and BI Publisher reports. Also using Visual Builder Studio (VB Studio) for Oracle Redwood pages"
- Every Oracle HCM implementation includes OTBI — standard component
- **APPSolve delivery claim for OTBI is confirmed and referenceable via Hollywood Bets**

### 3.2 BI Publisher — Tier B

**Source authority:** HIST-006 para 1127, 1210; HIST-008 paras 204–205

**Product description:** BI Publisher is Oracle's report layout and output tool, enabling formatted report generation (PDF, Excel, RTF, HTML). Used alongside OTBI for producing structured, formatted report documents such as payslips, offer letters, audit reports, and compliance reports.

**Key quote from HIST-006 para 1127:**
> "Organizations can build custom audit reports using Oracle's reporting tools (e.g., BI Publisher, OTBI) to meet specific internal or regulatory requirements."

**Key quote from HIST-006 para 1210:** "Customizing OTBI, BI Publisher, and FAW reports."

**APPSolve delivery evidence:**
- RedPath Mining RFI (March 2026): "APPSolve developers have extensive experience in writing OTBI and BI Publisher reports"
- **BI Publisher delivery claim is confirmed**

### 3.3 Oracle HCM Analytics (OAX) — Tier C

**Source authority:** HIST-006 paras 461–494, 1189–1195; HIST-014 CCBA paras 591–624 (restricted — support only)

**Product description from HIST-006 para 1189:**
> "Oracle HCM Analytics is a specialized module designed to deliver deep insights across the full spectrum of human capital management functions."

**Dedicated OAX section (HIST-006 paras 461–494) — full capability inventory:**

| OAX Capability | Source paragraph | Description |
|---|---|---|
| Product overview | 463 | "Prebuilt, cloud-based analytics solution that extends the value of Oracle Fusion Cloud HCM. Delivers out-of-the-box dashboards and KPIs tailored for HR use cases such as workforce composition, talent acquisition, diversity, and employee retention." |
| Faster insight-driven decisions | 466 | "Empowers HR and business leaders with real-time, actionable insights to drive strategic decisions and workforce planning." |
| Out-of-the-box value | 469 | "Delivers prebuilt dashboards, metrics, and KPIs without needing extensive setup or customization." |
| Enhanced data integration | 471 | "Combines HCM data with data from other sources (e.g., Finance, CRM) for a more holistic view." |
| Self-service analytics | 473 | "Reduces reliance on IT through user-friendly self-service analytics and reporting capabilities." |
| Strategic HR initiatives | 475 | "Helps track key HR objectives such as diversity and inclusion, succession planning, and employee engagement." |
| Prebuilt Dashboards & KPIs | 482 | "Over 50 prebuilt metrics and dashboards covering headcount, compensation, turnover, DEI, and recruitment." |
| Role-Based Access & Security | 485 | "Inherits security models from Oracle HCM to ensure data privacy and role-appropriate access." |
| Self-Service Data Exploration | 488 | "Allows users to drill down, filter, and customize reports without needing technical expertise." |
| Machine Learning & Predictive Analytics | 491 | "Supports trend analysis and predictive modelling to identify potential workforce risks or opportunities." |
| Cross-Functional Analytics | 494 | "Enables linking HCM data with data from Oracle ERP, SCM, or CX for cross-domain insights." |

**HIST-006 paras 1189–1195 — additional OAX details:**

| OAX Capability | Source paragraph | Description |
|---|---|---|
| Pre-built HR Analytics domains | 1190 | "Workforce Composition, Talent Acquisition, Diversity & Inclusion, Attrition, Learning, Employee Sentiment — based on industry best practices." |
| Predictive & AI-Driven Insights | 1191 | "Leveraging embedded machine learning, HCM Analytics can forecast workforce trends, identify high-risk employees, and suggest proactive actions to improve employee engagement and retention." |
| Self-Service Data Exploration | 1192 | "HR teams, business leaders, and analysts can explore data through intuitive visualizations, customize reports, and create their own dashboards without relying heavily on IT." |
| Unified Workforce View | 1193 | "Can integrate data from Oracle ERP, SCM, and CX as well as external sources, offering a consolidated view of workforce impact on broader business outcomes." |
| Security-Aware Access | 1194 | "Built with Oracle's security model, HCM Analytics respects role-based permissions." |
| Mobile-Optimized Dashboards | 1195 | "Key insights and dashboards are accessible via mobile devices." |

**Salary cost planning context (HIST-006 paras 885–889):**
OAX is explicitly positioned as the analytics layer for compensation cost planning:
> "Provides pre-built analytics and dashboards specifically for payroll and compensation costing. Allows drill-down from high-level KPIs to employee-level cost details. Analyse historical payroll and compensation data to identify patterns and trends."

**APPSolve delivery evidence for OAX:**
- **NONE CONFIRMED.** No client has been identified with confirmed OAX implementation by APPSolve.
- HIST-006 (SAA) and HIST-014 (CCBA) describe OAX as platform capability in unawarded proposals
- Hollywood Bets: OAX absent from BOM (paras 56–66)
- Mr Price: No analytics implementation confirmed
- DFA: No OAX in confirmed scope (Rule 21.4 — internal only regardless)
- Redpath Mining: Active scope (Core HR, Absence, Recruiting, Compensation, Talent) — OAX absent
- **This is the primary blocking open item: OI-W6-001**

### 3.4 Fusion Analytics Warehouse (FAW) — Tier D

**Source authority:** HIST-006 para 1210 (single reference)

**Evidence:** FAW appears once: "Customizing OTBI, BI Publisher, and FAW reports."

**Assessment:** FAW is the technical underpinning of Oracle HCM Analytics (OAX). It is the data warehouse and analytics platform on which OAX pre-built content is delivered. FAW is not a separately marketed or separately implemented product in the context of HCM analytics. It is delivered as the technical layer of an OAX implementation.

**Extraction guidance:** Do not position FAW as a separately deliverable product. Reference FAW in the technical architecture context only — as the underlying platform for Oracle HCM Analytics delivery.

### 3.5 Predictive Analytics / AI-Driven Workforce Insights

**Source authority:** HIST-006 paras 163, 491, 974, 1191; HIST-014 CCBA paras 619–621, 654–656

**Evidence summary:**
- HIST-006 para 163 (general HCM overview): "Predictive Analytics: Leverages data analytics and AI to predict workforce trends, such as turnover, hiring needs, and skills gaps."
- HIST-006 para 491 (OAX section): "Machine Learning & Predictive Analytics: Supports trend analysis and predictive modelling to identify potential workforce risks or opportunities."
- HIST-006 para 1191 (OAX description): "Leveraging embedded machine learning, HCM Analytics can forecast workforce trends, identify high-risk employees, and suggest proactive actions."
- HIST-006 para 974: "Predictive Analytics: The system leverages historical data (e.g., attrition rates, hiring trends, productivity metrics) to forecast future headcount requirements by department, job role, and skill set." — in the Workforce Planning section.

**Product attribution:**
- ML/Predictive analytics capabilities are **OAX-exclusive** — they are not delivered through OTBI
- Cannot be framed as APPSolve delivery capability without OAX implementation evidence
- Can be framed as platform capability: "Oracle HCM Analytics provides embedded machine learning capabilities that..."
- **This is blocking open item OI-W6-002**

### 3.6 HCM Extracts

**Source authority:** HIST-006 paras 859–863, 1166; HIST-015 para 509

**Assessment:** HCM Extracts are a **data extraction and integration tool**, not an analytics product. They extract data from Oracle HCM in configurable formats (flat files, XML, CSV) for external systems (payroll providers, data warehouses, SETA reporting tools).

**Relevant capability:**
- Configurable data extract definitions
- Scheduled incremental extracts
- Multiple output formats
- Legislative reporting support (SETA, ATR, WSP) via data extract (HIST-015 para 509)
- Payroll outbound integration

**Governance note:** HCM Extracts are standard functionality included in every Oracle HCM implementation. They are not part of the analytics product boundary. Include in the W3S1-006 document as supporting data infrastructure context, not as an analytics capability.

### 3.7 Strategic Workforce Planning (CCBA source — restricted)

**Source authority:** HIST-014 CCBA paras 626–663 (RESTRICTED — extraction support only)

**Evidence:** HIST-014 CCBA contains a dedicated "Enterprise Performance Management – Strategic Workforce Planning" section (paras 626–663) that is not present in HIST-006. This describes a separate Oracle product for long-range workforce planning, scenario modelling, and headcount/cost alignment.

**Product assessment:** This appears to be **Oracle Fusion Cloud Strategic Workforce Planning**, part of the Oracle Fusion Cloud EPM (Enterprise Performance Management) suite. It is distinct from OAX and from Oracle HCM Analytics. It is a separately licensed, separately implemented product.

**Governance constraint:** CCBA is restricted — extraction support use only. CCBA must never be named. However, the content may be used to establish whether Strategic Workforce Planning is within scope for W3S1-006.

**Advisory open item: OI-W6-003** — BU Lead to confirm whether Strategic Workforce Planning should be included in W3S1-006 or scoped to a separate statement.

---

## Section 4: Per-Source Coverage Analysis

### 4.1 HIST-006 SAA HCM RFP Response — Detailed Coverage Map

| Para range | Content | Analytics tier | Usable for extraction |
|---|---|---|---|
| 87 | "Advanced Analytics: Oracle Fusion includes embedded analytics and BI tools. Real-time insights and predictive analytics." | OAX platform overview | Yes — platform capability |
| 121 | "Real-time insights: Provides analytics and reporting capabilities for informed decision-making." | General OTBI/OAX | Yes — as general framing |
| 163 | "Predictive Analytics: Leverages data analytics and AI to predict workforce trends, turnover, hiring needs, skills gaps." | OAX predictive (subject to OI-W6-002) | Conditional — pending framing decision |
| 171–175 | OTBI section: real-time data reporting, self-service analytics, embedded analytics | OTBI | Yes — confirmed standard capability |
| 188 | Compensation analytics — data-driven decisions, real-time analytics | OTBI/compensation module | Yes — OWC context (W3S1-005 boundary applies) |
| 228–231 | Compensation Analytics & Reporting — real-time dashboards, comparative analytics, pay equity | OTBI compensation embedded | Yes — platform capability |
| 253 | "Provides real-time analytics on recruiting performance and candidate pipelines" | OTBI recruiting | Yes |
| 281 | "Centralized dashboard for recruiters and hiring managers" | OTBI recruiting | Yes |
| 287–289 | Advanced Recruiting Analytics — real-time dashboards, hiring performance, diversity metrics, time-to-fill | OTBI recruiting | Yes |
| 312 | Performance/retention analytics — real-time | OTBI performance | Yes |
| 341–343 | Advanced Talent Analytics — dashboards for workforce trends, retention risks, performance tracking | OTBI/OAX boundary | Conservative: OTBI unless OAX confirmed |
| 400–402 | HR Analytics & Reporting — real-time dashboards for HR service performance | OTBI Help Desk | Yes |
| 452–454 | Learning Analytics & Progress Tracking — dashboards, learning effectiveness | OTBI (but per HIST-015 para 511: no OOB Learning reports in Learning Cloud — OAX covers this gap) | Qualified — apply Learning caveat |
| 461–494 | **Dedicated OAX section** — full product description, 5 benefits, 5 features | OAX — separately licensed | Yes — platform capability; subject to OI-W6-001 framing |
| 874 | "Salary cost planning... often augmented by HCM Analytics" | OAX compensation analytics | Yes — confirms OAX augments compensation planning |
| 885–889 | OAX pre-built dashboards for payroll and compensation costing, drill-down, historical analysis, variance analysis | OAX | Yes — platform capability |
| 1125–1128 | Audit reports — BI Publisher + OTBI for custom audit reports | OTBI + BI Publisher | Yes |
| 1166 | HCM Extracts for data exchange to downstream systems and reporting tools | HCM Extracts | Yes — data infrastructure |
| 1182–1195 | **Comprehensive Analytics & Reporting section** — OTBI (1184–1188), OAX (1189–1195) | Both OTBI and OAX — clearly distinguished | Yes — this is the clearest product boundary articulation in the corpus |
| 1210 | "Customizing OTBI, BI Publisher, and FAW reports" | FAW mentioned — context of report customization | Yes — FAW as technical context |

### 4.2 HIST-007 Hollywood Bets V5.0

| Para | Content | Assessment |
|---|---|---|
| 56–66 | BOM: "10 Custom reports and 6 Custom Workflows" | OTBI — confirmed implementation deliverable |
| 576 | "We recommend the acquisition of a third-party reporting tool" | Advisory; implies OTBI standard may not fully satisfy all reporting needs — supports OAX as value-add |
| 638 | SETA/WSP/ATR reporting via Oracle + Moodle integration | HCM Extracts / OTBI context |

**Conclusion:** Hollywood Bets confirms OTBI as standard implementation deliverable. OAX explicitly absent from BOM.

### 4.3 HIST-008 RedPath Mining RFI (March 2026)

| Para | Content | Assessment |
|---|---|---|
| 204–205 | "APPSolve developers have extensive experience in writing OTBI and BI Publisher reports. Also using Visual Builder Studio (VB Studio) for Oracle Redwood pages." | **Strongest confirmed developer capability claim for OTBI + BIP** |

**Conclusion:** HIST-008 provides the most direct confirmed capability claim for OTBI and BI Publisher. Active implementation in progress. Approved for use in delivery capability framing.

### 4.4 HIST-015 Afrocentric HCM Proposal V4.0

| Para | Content | Assessment |
|---|---|---|
| 467 | "Standard delivered reports and dashboards will be used to satisfy reporting requirements" | Delivery assumption — standard OTBI/delivered reports |
| 502 | Same assumption for recruiting | Delivery assumption |
| 509 | SETA/ATR/WSP via "data extract that can be manipulated" | HCM Extracts for legislative reporting |
| 511 | **"Oracle Learning Cloud does not include any Learning Reports or Dashboards."** | Critical caveat — applies to W3S1-006 analytics scope |

**Conclusion:** HIST-015 supports delivery methodology framing. The para 511 caveat must be applied in W3S1-006: Learning module analytics require OAX for pre-built dashboards; Learning Cloud built-in reporting is absent.

### 4.5 HIST-014 CCBA (Restricted — extraction support only)

| Para range | Content | Assessment |
|---|---|---|
| 591–624 | Mirrors HIST-006 OAX section (largely parallel content) | Supports HIST-006 platform capability claims — confirms content currency |
| 626–663 | **Strategic Workforce Planning** — scenario modelling, headcount/cost planning, skills gap analysis, predictive analytics for long-range workforce | Distinct product scope — separate Oracle offering; subject to OI-W6-003 |

**Governance confirmation:** CCBA content may be used to validate HIST-006 claims and verify content accuracy. CCBA may not be cited. CCBA must never be named.

---

## Section 5: Implementation Evidence Assessment

### 5.1 Client Reference Classification — Analytics

| Client | OTBI status | OAX status | Referenceable | Governance rule |
|---|---|---|---|---|
| **Hollywood Bets** | Confirmed — 10 custom reports in BOM (implemented 2023, live July 2025) | ABSENT from BOM | **YES — for OTBI/standard reporting** | Tier 1 referenceable |
| **Mr Price Group** | Assumed standard (HCM implementation) | Not confirmed | Support reference only (broader HCM) | Rule 21.2 — implementation vs support distinction |
| **DFA** | Assumed standard (full Oracle HCM suite) | Not confirmed | NOT referenceable — Rule 21.4 | DFA never named |
| **Redpath Mining** | Active implementation (assumed standard) | Not in scope | NOT referenceable — pipeline only | Rule 21.5 — active, not live |
| **KPMG** | Taleo (not Fusion HCM) | N/A | Internal only (source evidence) | No Fusion HCM analytics evidence |
| **SAA** | Platform capability source only | Proposed (not awarded) | Never named | SAA not awarded — Rule 21.1 context |
| **CCBA** | Platform capability source only | Proposed (not awarded) | PROHIBITED | CCBA never named |

### 5.2 Analytics Evidence Quality Assessment

| Evidence type | Quality | Source | Reusable for extraction |
|---|---|---|---|
| OTBI developer capability | **HIGH** | RedPath Mining RFI para 204–205 (March 2026) | Yes — most current confirmed claim |
| OTBI implementation deliverable | **HIGH** | HB V5.0 BOM para 56–66 (April 2023, live July 2025) | Yes — confirmed Tier 1 reference |
| OAX platform capability (overview) | **HIGH — volume, detail** | HIST-006 paras 461–494, 1189–1195 | Yes — as platform capability (reframed; SAA not named) |
| OAX implementation evidence | **NONE** | No source | NOT AVAILABLE — blocks OI-W6-001 |
| BI Publisher developer capability | **HIGH** | RedPath Mining RFI para 204–205 | Yes |
| Predictive/ML analytics | **Platform capability only** | HIST-006 paras 491, 1191 | Conditional on OI-W6-002 framing decision |
| HCM Extracts | **HIGH** | HIST-006 paras 859–863; HIST-015 para 509 | Yes — standard tool |
| Strategic Workforce Planning | **RESTRICTED** | HIST-014 CCBA only | Advisory — pending OI-W6-003 |

---

## Section 6: Product Boundary — OTBI vs OAX

The following table establishes the authoritative capability boundary for use in the Candidate Draft. This boundary is derived from HIST-006 paras 1184–1195 and must be applied consistently across all sections.

| Capability | Belongs to | Evidence | Notes |
|---|---|---|---|
| Real-time transactional reports | OTBI | HIST-006 para 1185 | Standard HCM — no extra license |
| Pre-built role-based dashboards | OTBI | HIST-006 para 1186 | Included with HCM license |
| Custom drag-and-drop user reports | OTBI | HIST-006 para 1187 | No coding required |
| Embedded analytics in HCM pages | OTBI | HIST-006 para 1188 | Contextual insights within workflows |
| Formatted report output (PDF, Excel) | BI Publisher | HIST-006 para 1127 | Formatted report layouts |
| Custom audit reports | OTBI + BI Publisher | HIST-006 para 1127 | Both tools used |
| Report customization (OTBI, BIP, FAW) | OTBI / BI Publisher / FAW | HIST-006 para 1210 | FAW is technical layer of OAX |
| 50+ pre-built KPIs | OAX | HIST-006 para 482 | **Separate license** |
| DEI / diversity analytics | OAX | HIST-006 para 482 | **OAX only** |
| Attrition analytics | OAX | HIST-006 para 482 | **OAX only** |
| Workforce composition analytics | OAX | HIST-006 paras 463, 1190 | **OAX only** |
| Employee sentiment analytics | OAX | HIST-006 para 1190 | **OAX only** |
| Machine learning / predictive analytics | OAX | HIST-006 paras 491, 1191 | **OAX only — not in OTBI** |
| Attrition forecasting / high-risk employee identification | OAX | HIST-006 para 1191 | **OAX only** |
| Cross-functional analytics (HCM + Finance + SCM) | OAX | HIST-006 paras 494, 1193 | **OAX only** |
| Mobile-optimized analytics dashboards | OAX | HIST-006 para 1195 | OAX specific |
| Salary cost planning dashboards | OAX | HIST-006 para 886 | OAX augments Compensation module |
| Drill-down to employee-level cost detail | OAX | HIST-006 para 887 | **OAX capability** |
| Historical payroll trend analysis | OAX | HIST-006 para 888 | OAX compensation analytics |
| HCM data extracts (payroll, SETA) | HCM Extracts | HIST-006 paras 859–863 | Standard — not analytics |
| Strategic workforce planning (scenario modelling) | Separate EPM product | HIST-014 CCBA only | Pending OI-W6-003 |

---

## Section 7: Analytics Claims in Previous Wave 3 Statements — Consistency Check

The following module-level analytics claims were made in approved or candidate Wave 3 statements. The W3S1-006 Candidate Draft must be consistent with these.

| Statement | Analytics claim | Classification | Consistency requirement |
|---|---|---|---|
| W3S1-004 (Learning Cloud) | "Oracle Fusion Learning Cloud does not include pre-built Learning Reports or Dashboards as part of the standard implementation scope." Advanced analytics = OAX. | OAX boundary applied | W3S1-006 must confirm this. OAX covers the Learning analytics gap. |
| W3S1-005 (Workforce Compensation) | Section 9.1: OWC built-in analytics (plan cycle tracking, budget consumption, approval status, pay equity monitoring). Section 9.2: OAX advanced compensation dashboards (separate product). Cross-reference to W3S1-006. | OAX boundary applied | W3S1-006 must be the definitive OAX document that W3S1-004 and W3S1-005 cross-reference. |
| W3S1-001 (HCM Core) | "OTBI (Oracle Transactional Business Intelligence)" listed as confirmed module in ORACLE_FACT_BASELINE Section 4.1 (SAA Section 2). | OTBI standard | W3S1-006 must include OTBI consistently with W3S1-001. |

**Cross-reference requirement:** W3S1-006 is the definitive analytics capability statement. W3S1-004 and W3S1-005 both cross-reference W3S1-006 for advanced analytics. The W3S1-006 Candidate Draft must explicitly address the analytics gaps left open by W3S1-004 (no Learning OOB reports) and W3S1-005 (OWC plan tracking vs OAX dashboards) and confirm how OAX addresses these.

---

## Section 8: Governance Risks

| Risk ID | Risk | Likelihood | Impact | Severity | Mitigation |
|---|---|---|---|---|---|
| **R-W6-001** | **OTBI vs OAX conflation** — HIST-006 uses "dashboards" and "analytics" in every module section without product attribution. If extracted without attribution, the draft will incorrectly imply OAX capability within standard OTBI. | **HIGH** | **HIGH** | CRITICAL | Apply Section 6 product boundary table consistently throughout extraction. Every analytics claim must be attributed to OTBI or OAX explicitly. |
| **R-W6-002** | **No OAX implementation evidence** — OAX is described in unawarded proposals only. No client confirmation of OAX implementation by APPSolve. If OAX is presented as delivery capability, it is unsupported. | **CONFIRMED** | HIGH | BLOCKING | Pending OI-W6-001. If no client confirmed, all OAX content must be framed as "platform capability APPSolve configures and implements" — same model as Learning Cloud analytics in W3S1-004. |
| **R-W6-003** | **Predictive analytics/AI overstatement** — Predictive workforce analytics (attrition forecasting, high-risk employee identification, ML-driven insights) are OAX-exclusive. If framed as standard APPSolve delivery capability, the claim is unsupported. | HIGH | HIGH | BLOCKING | Pending OI-W6-002. Must be framed as platform capability pending BU Lead decision. |
| **R-W6-004** | **FAW overstated as standalone product** — FAW is the technical underpinning of OAX, not a separately marketed offering. If positioned as a standalone deliverable, it misrepresents the product. | LOW | MEDIUM | ADVISORY | Frame FAW as technical architecture context only (underlying platform for OAX). Never present as standalone product. |
| **R-W6-005** | **"Workforce Intelligence" as product name** — "Workforce Intelligence" is not a distinct Oracle product. Using it as a product name could cause confusion with Oracle's historical "Oracle Workforce Intelligence" product suite (separate EBS-era tool). | LOW | MEDIUM | ADVISORY | Frame "Workforce Intelligence" as a capability descriptor, not a product name. Document title may use it descriptively but content must not imply it is a distinct Oracle product. |
| **R-W6-006** | **Strategic Workforce Planning scope creep** — HIST-014 CCBA describes a Strategic Workforce Planning product (EPM suite). If included in W3S1-006 without BU Lead confirmation, scope exceeds HCM Analytics. | MEDIUM | MEDIUM | ADVISORY | Pending OI-W6-003. Do not include Strategic Workforce Planning in extraction until BU Lead confirms scope. |
| **R-W6-007** | **Module-level "advanced analytics" claims in prior statements** — W3S1-004 (Learning) and W3S1-005 (Compensation) both reference OAX cross-reference to W3S1-006. If W3S1-006 OAX content is weaker than implied, the cross-references appear unsupported. | MEDIUM | LOW | LOW | W3S1-006 must be a comprehensive OAX reference document that substantiates the cross-references in W3S1-004 and W3S1-005. |
| **R-W6-008** | **CCBA content mirroring HIST-006** — HIST-014 CCBA analytics content largely mirrors HIST-006 (likely same source material). If both are used independently, extraction may introduce undetected duplication. | LOW | LOW | LOW | HIST-006 is the primary platform capability source. HIST-014 CCBA is used for support and validation only — not as a separate evidence stream. |

---

## Section 9: Proposed Document Structure

Subject to BU Lead decisions (OI-W6-001 through OI-W6-005), the following 15-section structure is proposed:

| Section | Content | Primary source | Notes |
|---|---|---|---|
| 1 | Statement of Capability | ORACLE_FACT_BASELINE; HIST-008 | OTBI confirmed; OAX framing subject to OI-W6-001 |
| 2 | Oracle HCM Analytics Architecture — Product Overview | HIST-006 paras 1182–1195 | OTBI vs OAX boundary; FAW technical architecture |
| 3 | OTBI — Standard Embedded Reporting | HIST-006 paras 1184–1188; HIST-008 paras 204–205 | Confirmed delivery capability |
| 4 | BI Publisher — Formatted Report Output | HIST-006 para 1127; HIST-008 para 205 | Confirmed delivery capability |
| 5 | Oracle HCM Analytics (OAX) — Product Overview and Value | HIST-006 paras 461–494 | Platform capability; subject to OI-W6-001 |
| 6 | OAX — Prebuilt Dashboards and KPI Library | HIST-006 paras 480–494 | Platform capability — 50+ KPIs |
| 7 | OAX — Machine Learning and Predictive Workforce Insights | HIST-006 paras 491, 1191 | Subject to OI-W6-002 framing |
| 8 | OAX — Cross-Functional Workforce Analytics | HIST-006 paras 492–494, 1193 | Platform capability |
| 9 | Analytics by HCM Domain | HIST-006 (module analytics sections) | Apply OTBI/OAX boundary per Section 6 boundary table |
| 10 | HCM Extracts — Data Infrastructure for Analytics | HIST-006 paras 859–863; HIST-015 para 509 | Standard tool |
| 11 | APPSolve Delivery Capability | HIST-008 paras 204–205; HIST-007 BOM | Confirmed OTBI + BIP; OAX pending OI-W6-001 |
| 12 | Implementation References | ORACLE_FACT_BASELINE Section 19; HIST-007 | HB = OTBI reference; OAX = pending |
| 13 | Implementation Approach | ORACLE_FACT_BASELINE Section 17 | OUM phases |
| 14 | Risk Register | SVR risk analysis | 5–6 risks |
| 15 | Assumptions Register | HIST-015 para 467; delivery context | 6–8 assumptions |
| 17 | Approval Record | — | Standard |
| App A | Source Mapping | — | Standard |
| App B | Governance Self-Review | — | Standard |
| App C | Extraction Return Report | — | Standard |

---

## Section 10: Open Items Register

### OI-W6-001 — [CLOSED 2026-06-13] OAX Implementation Evidence

**Status:** CLOSED — BU Lead decision 2026-06-13

**BU Lead decision:**
APPSolve has not implemented Oracle HCM Analytics (OAX) as a delivery partner for any confirmed referenceable client.

APPSolve has participated in Oracle Analytics environments as a technical specialist and support partner on the client side at SARB, including support and maintenance activities. SARB must not be used as implementation evidence or as a named client reference.

**Resulting position:**
- Oracle HCM Analytics (OAX) is **Platform Capability Only**
- No implementation claims are permitted
- No referenceable client evidence exists
- APPSolve may be positioned as having product knowledge, support experience, and technical capability in Oracle Analytics environments
- SARB: never named, never referenced as implementation evidence

**Impact on Candidate Draft:** Outcome A applied. All OAX sections framed as platform capability. No implementation reference. SARB explicitly excluded.

---

### OI-W6-002 — [CLOSED 2026-06-13] Predictive Analytics / AI Workforce Insights — Framing Decision

**Status:** CLOSED — BU Lead decision 2026-06-13

**BU Lead decision:**
Predictive workforce analytics, workforce intelligence, attrition prediction, workforce risk indicators, AI-driven workforce insights, and related machine learning capabilities are Oracle HCM Analytics platform capabilities. No confirmed APPSolve client implementation evidence exists.

**Resulting position:**
- Platform Capability Only
- Do not present as confirmed APPSolve-delivered functionality
- Present as Oracle HCM Analytics capabilities that APPSolve can support and configure where licensed and implemented by clients

**Impact on Candidate Draft:** Outcome A applied. Predictive/ML sections framed as Oracle HCM Analytics platform capabilities, not as APPSolve delivery claims.

---

### OI-W6-003 — [CLOSED 2026-06-13] Strategic Workforce Planning — Scope Inclusion

**Status:** CLOSED — BU Lead decision 2026-06-13

**BU Lead decision:** Exclude Strategic Workforce Planning entirely from W3S1-006. Rationale: separate product domain; introduces unnecessary product-boundary risk; outside approved scope for this statement.

**Impact on Candidate Draft:** Strategic Workforce Planning section removed from document structure. No reference to Oracle Fusion Cloud Strategic Workforce Planning or Oracle EPM in this statement.

---

### OI-W6-004 — [CLOSED 2026-06-13] BI Publisher — Inclusion and Framing

**Status:** CLOSED — BU Lead decision 2026-06-13

**BU Lead decision:** Retain BI Publisher as a dedicated section separate from OTBI. Rationale: confirmed capability evidence exists; different use case and audience from OTBI; avoids OTBI / BI Publisher conflation.

**Impact on Candidate Draft:** Section 4 (BI Publisher) as a standalone section. Covers pixel-perfect formatting, scheduled reporting, regulatory/compliance reporting use cases. Confirmed delivery capability from HIST-008.

---

### OI-W6-005 — [CLOSED 2026-06-13] Document Title Confirmation

**Status:** CLOSED — BU Lead decision 2026-06-13

**BU Lead decision:** Approved title: **Oracle HCM Analytics & Workforce Intelligence**. Governance note: "Workforce Intelligence" is a capability descriptor and not a separate licensable Oracle product.

**Impact on Candidate Draft:** Title confirmed. Document ID: W3S1-006-ORA-HCMAnalytics.

---

## Section 11: Extraction Readiness Assessment

| Check | Status | Notes |
|---|---|---|
| Source evidence sufficient for OTBI | ✅ SUFFICIENT | HIST-006, HIST-007 (BOM), HIST-008 (HIST-008 confirmed capability) |
| Source evidence sufficient for BI Publisher | ✅ SUFFICIENT | HIST-008 confirmed capability |
| Source evidence sufficient for OAX platform capability | ✅ SUFFICIENT | HIST-006 paras 461–494, 1189–1195 — comprehensive |
| Source evidence sufficient for OAX implementation reference | ✅ RESOLVED | OI-W6-001 CLOSED — Platform Capability Only; SARB excluded |
| Predictive analytics framing confirmed | ✅ RESOLVED | OI-W6-002 CLOSED — Platform Capability Only |
| Strategic Workforce Planning scope confirmed | ✅ RESOLVED | OI-W6-003 CLOSED — EXCLUDED |
| BI Publisher section scope confirmed | ✅ RESOLVED | OI-W6-004 CLOSED — Dedicated section confirmed |
| Document title confirmed | ✅ RESOLVED | OI-W6-005 CLOSED — "Oracle HCM Analytics & Workforce Intelligence" approved |
| Standing Wave 3 governance rules applied | ✅ PASS | Rules 21.1–21.5 verified — all consistent |
| CCBA prohibition confirmed | ✅ PASS | CCBA never named; content used for extraction support only |
| SAA prohibition confirmed | ✅ PASS | SAA never named; platform capability source reframed |
| ORACLE_FACT_BASELINE current | ✅ CURRENT | Updated 2026-06-13 (OI-W5-003 DFA Compensation) |

**Overall extraction readiness: AUTHORISED 2026-06-13**

All 5 open items closed by BU Lead. Extraction authorised. Candidate Draft production may begin. Key constraints confirmed: OAX = Platform Capability Only; predictive/ML = Platform Capability Only; SARB excluded; Strategic Workforce Planning excluded; BI Publisher = dedicated section; title confirmed.

---

## Section 12: Standing Governance Confirmations

**Wave 3 Standing Rules — ORACLE_FACT_BASELINE Section 21:**

| Rule | Check |
|---|---|
| **21.1 Aviation PROHIBITED** | SAA not named in any context. SAA content extracted and reframed as platform capability. | PASS |
| **21.2 Implementation vs Support** | Hollywood Bets = OTBI implementation reference. Mr Price = support reference only. Distinction maintained. | PASS |
| **21.3 Opportunity Marketplace** | Not relevant to analytics statement. | N/A |
| **21.4 DFA — never named** | DFA not named anywhere. Internal corroboration potential noted — pending OI-W6-001. | PASS |
| **21.5 Redpath — not used as completed implementation** | Active scope noted; not confirmed for OAX; will not be cited as completed implementation. | PASS |
| **CCBA PROHIBITED** | CCBA used for extraction support only. Never cited, never named, never referenced. | PASS |
| **OIC mandatory** | OAX is a cloud analytics product — OIC integration context less relevant to analytics than to transactional HCM modules. HCM Extracts integration (data to analytics layer) is standard. | APPLIED |
| **Prohibited wording** | No Gold Partner, 110+ consultants, 22 years, Level 2 BEE — confirmed absent from all planned extraction | PASS |

---

## Appendix: Source-Specific Analytics Paragraph Index

### HIST-006 SAA — Analytics-Specific Paragraphs (prioritised)

| Para | Keyword | Content summary |
|---|---|---|
| 87 | Advanced Analytics overview | Embedded analytics + BI tools; real-time insights + predictive analytics |
| 171 | OTBI heading | — |
| 173 | Real-Time Data Reporting (OTBI) | On-demand analytics; real-time reports from live data |
| 174 | Self-Service Analytics (OTBI) | Create/customize reports, visualizations, dashboards without technical skills |
| 175 | Embedded Analytics (OTBI) | Analytics embedded in HR processes for contextual decisions |
| 461 | HCM Analytics heading | — |
| 463 | OAX overview | Prebuilt cloud analytics solution; out-of-the-box dashboards; workforce composition, talent, DEI, retention |
| 469 | OAX prebuilt value | "Delivers prebuilt dashboards, metrics, and KPIs without needing extensive setup" |
| 471–473 | OAX data integration; efficiency | Combines HCM with Finance/CRM; reduces IT reliance |
| 480 | OAX Prebuilt Dashboards heading | — |
| 482 | OAX 50+ KPIs | "Over 50 prebuilt metrics covering headcount, compensation, turnover, DEI, recruitment" |
| 489 | OAX ML & Predictive heading | — |
| 491 | OAX Predictive Analytics | "Trend analysis and predictive modelling to identify potential workforce risks or opportunities" |
| 492 | OAX Cross-Functional heading | — |
| 494 | OAX Cross-Functional detail | "Enables linking HCM data with Oracle ERP, SCM, or CX for cross-domain insights" |
| 885–889 | OAX — Salary Cost Planning context | Pre-built dashboards for payroll costing; drill-down; historical analysis; variance analysis |
| 1125–1128 | Audit Reports — BI Publisher + OTBI | "Custom audit reports using BI Publisher, OTBI" |
| 1182–1183 | Analytics & Reporting section intro | "Comprehensive suite of analytics and reporting tools" |
| 1184–1188 | OTBI comprehensive description | "Primary reporting tool"; real-time operational; pre-built dashboards; custom; embedded |
| 1189–1195 | OAX comprehensive description | "Specialized module"; pre-built HR analytics; predictive & AI; self-service; unified view; security; mobile |
| 1210 | OTBI, BI Publisher, FAW mentioned | "Customizing OTBI, BI Publisher, and FAW reports" |

### HIST-008 RedPath Mining — Analytics

| Para | Content |
|---|---|
| 204–205 | "APPSolve developers have extensive experience in writing OTBI and BI Publisher reports. Also using Visual Builder Studio (VB Studio) for Oracle Redwood pages." |

### HIST-015 Afrocentric — Reporting Assumptions

| Para | Content |
|---|---|
| 467 | "Standard delivered reports and dashboards will be used to satisfy reporting requirements." |
| 502 | Same assumption — recruiting |
| 509 | SETA/ATR/WSP via data extract |
| 511 | **"Oracle Learning Cloud does not include any Learning Reports or Dashboards."** |

---

*SVR prepared 2026-06-13 by Claude (AI — Wave 3 W3S1-006 SVR).*
*Updated 2026-06-13 — All 5 OI items closed by BU Lead Hein Blignaut. Extraction authorised.*
*Standing Wave 3 governance rules ORACLE_FACT_BASELINE Section 21 confirmed — all pass.*
*Additional governance: SARB excluded (OI-W6-001); Strategic Workforce Planning excluded (OI-W6-003); OAX + predictive analytics = Platform Capability Only throughout.*
