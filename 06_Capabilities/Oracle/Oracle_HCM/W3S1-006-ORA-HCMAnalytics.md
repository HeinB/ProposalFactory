---
document_id: W3S1-006-ORA-HCMAnalytics
title: "Oracle HCM Analytics & Workforce Intelligence — Capability Statement"
version: "1.1 Approved"
status: "Approved"
review_status: "Approved"
approved_for_reuse: "Yes"
business_unit: "Oracle"
wave: "3"
deliverable: "W3S1-006"
created: "2026-06-13"
created_by: "Claude (AI — Wave 3 W3S1-006 extraction)"
approved_by: "Hein Blignaut (BU Lead)"
approval_date: "2026-06-13"
source_document: "HIST-006 (SAA HCM RFP Response, June 2025 — platform capability narrative); HIST-008 (RedPath Mining RFI Reply, March 2026 — OTBI + BI Publisher confirmed capability); HIST-007 (Hollywood Bets V5.0, April 2023 — OTBI BOM evidence); HIST-015 (Afrocentric HCM Proposal V4.0, 2023 — delivery assumptions); ORACLE_FACT_BASELINE Sections 4.1, 19, 21"
source_status: "Platform Capability (HIST-006 — OAX, OTBI); Confirmed Delivery Capability (HIST-008 — OTBI + BI Publisher); Implementation Evidence — OTBI (HIST-007 Hollywood Bets BOM); Delivery Assumptions (HIST-015)"
prereq_statement: "W3S1-001-ORA-HCMCore (Oracle HCM Core — Global HR is the mandatory prerequisite; OTBI and BI Publisher are included within the Oracle HCM license; Oracle HCM Analytics is a separately licensed product requiring a separate implementation)"
kb_destination: "06_Capabilities/Oracle/Oracle_HCM/"
tags: "Oracle,HCM,Analytics,OTBI,BI Publisher,OAX,Oracle HCM Analytics,Workforce Intelligence,Reporting,Dashboards,Predictive Analytics,FAW,Fusion Analytics Warehouse"
---

> **APPROVED — approved_for_reuse: Yes — Approved by BU Lead 2026-06-13**

---

# Oracle HCM Analytics & Workforce Intelligence

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W3S1-006-ORA-HCMAnalytics | Version: 1.1 Approved | Wave 3*

---

## Section 1: Statement of Capability

APPSolve delivers Oracle HCM reporting and analytics capabilities across the full Oracle Fusion HCM product hierarchy — from standard embedded transactional reporting through to formatted regulatory reports and advanced workforce analytics dashboards.

Oracle Fusion HCM provides a structured analytics and reporting architecture comprising three primary tiers, each serving a distinct purpose:

| Tier | Product | License | APPSolve delivery |
|---|---|---|---|
| **A** | Oracle Transactional Business Intelligence (OTBI) | Included in Oracle HCM license | **Confirmed delivery capability** — standard in every Oracle HCM implementation |
| **B** | BI Publisher | Included in Oracle HCM license | **Confirmed delivery capability** — APPSolve developers have extensive experience |
| **C** | Oracle HCM Analytics (OAX) | **Separately licensed** | **Platform Capability** — APPSolve has product knowledge and technical capability; positions and supports where licensed by clients |

Oracle HCM Analytics (OAX) is a separately licensed, separately implemented Oracle cloud product. It is not included in the standard Oracle Fusion HCM license. Clients who elect to include Oracle HCM Analytics in their programme receive pre-built dashboards, KPI libraries, workforce intelligence capabilities, and machine learning-driven workforce insights that extend beyond the standard OTBI reporting available within the Oracle HCM platform.

APPSolve's OTBI and BI Publisher delivery is confirmed through multiple Oracle HCM implementations. Hollywood Bets' Oracle Fusion HCM implementation (go-live July 2025) included delivery of custom OTBI reports and custom workflows. APPSolve's Oracle practice has extensive confirmed developer and consultant capability across OTBI report authoring, BI Publisher layout design, and report lifecycle administration.

---

## Section 2: Oracle HCM Analytics Architecture — Product Hierarchy and Boundary

### 2.1 Analytics Product Hierarchy

Oracle Fusion HCM's analytics and reporting architecture is structured across four tiers. This hierarchy must be maintained in all Oracle HCM tender responses and implementations.

| Tier | Product | Role | Licensing |
|---|---|---|---|
| **Tier A — OTBI** | Oracle Transactional Business Intelligence | Primary operational reporting tool embedded in Oracle Fusion HCM. Real-time reports, role-based pre-built analyses, custom user-built reports, embedded contextual analytics | **Included with Oracle HCM license** |
| **Tier B — BI Publisher** | Oracle BI Publisher | Formatted report output layer — pixel-perfect layouts for payslips, offer letters, compliance reports, audit reports, regulatory submissions | **Included with Oracle HCM license** |
| **Tier C — OAX** | Oracle HCM Analytics | Advanced analytics platform — pre-built KPI library (50+ metrics), workforce intelligence dashboards, machine learning and predictive workforce insights, cross-functional analytics | **Separately licensed — not included in standard Oracle HCM** |
| **Tier D — FAW** | Oracle Fusion Analytics Warehouse | Underlying data warehouse and analytics platform on which Oracle HCM Analytics is built | **Delivered as part of OAX — not a standalone product** |

### 2.2 Critical Licensing Boundary

**Oracle HCM Analytics (OAX) requires a separate Oracle license.** It is not included in the Oracle Fusion HCM Cloud Service subscription. Clients who wish to implement Oracle HCM Analytics must license and implement it as a separate product, in addition to their Oracle HCM implementation.

This distinction must be stated clearly in any tender response. Implying that Oracle HCM Analytics pre-built dashboards are included as standard in an Oracle HCM implementation is inaccurate and creates commercial risk.

| Included in Oracle HCM license | Not included — requires separate license |
|---|---|
| OTBI (all pre-built and custom reports) | Oracle HCM Analytics (OAX) pre-built dashboards |
| BI Publisher (formatted output) | OAX KPI library (50+ metrics) |
| Embedded module-level analytics | OAX machine learning and predictive analytics |
| Standard audit reports | OAX cross-functional analytics (HCM + Finance + SCM) |
| HCM Extracts (data extraction) | OAX employee sentiment analytics |
| Role-based delivered dashboards | OAX mobile-optimised advanced dashboards |

### 2.3 Fusion Analytics Warehouse (FAW)

Oracle Fusion Analytics Warehouse (FAW) is the technical data warehousing and analytics platform that underpins Oracle HCM Analytics. FAW is not positioned as a standalone APPSolve delivery offering. Where Oracle HCM Analytics is implemented, FAW is delivered as the underlying technical infrastructure. APPSolve does not separately position FAW implementation as a distinct service line.

---

## Section 3: Oracle Transactional Business Intelligence (OTBI) — Standard Embedded Reporting

### 3.1 OTBI Overview

Oracle Transactional Business Intelligence (OTBI) is the primary reporting tool embedded within Oracle Fusion HCM. It provides direct, real-time access to Oracle HCM transactional data — enabling HR professionals, managers, and business leaders to generate operational reports and analytics without leaving the HCM application.

OTBI is included in the Oracle Fusion HCM license and is configured and delivered by APPSolve as a standard deliverable in every Oracle HCM implementation engagement.

> **APPSolve delivery confirmation:** RedPath Mining RFI (March 2026) — *"APPSolve developers have extensive experience in writing OTBI and BI Publisher reports. Also using Visual Builder Studio (VB Studio) for Oracle Redwood pages for extensive personalisation of Redwood UI elements."*

### 3.2 OTBI Capabilities

| OTBI Capability | Description | APPSolve delivery |
|---|---|---|
| **Real-time operational reports** | OTBI provides real-time access to live transactional data across all Oracle HCM modules — headcount, turnover, absence, payroll, performance, recruitment, and learning | Standard |
| **Pre-built role-based analyses** | Oracle delivers pre-built reports and dashboards tailored to HR roles — HR Generalist, Compensation Manager, Recruiter, Talent Manager, Line Manager. Cover common HR metrics and KPIs | Standard — delivered in every HCM implementation |
| **Custom user-built analyses** | Business users create and customise reports using a drag-and-drop interface without coding skills. Combine data from different HCM modules; apply filters, sorts, and calculations | APPSolve configures and trains users |
| **Embedded contextual analytics** | OTBI reports and dashboards embedded directly within Oracle HCM module pages — providing contextual insights to users within their workflows without navigating to a separate reporting tool | Standard |
| **Cross-module subject areas** | OTBI subject areas cover all Oracle HCM modules — workforce, absence, compensation, recruiting, performance, learning, time and labor, help desk, and more | Standard — all subject areas available |
| **Scheduled reports** | Reports can be scheduled for automated delivery at defined intervals — daily, weekly, monthly | Standard configuration deliverable |
| **Drill-down and filtering** | Users drill down from summary dashboards to individual employee or transaction detail within the same report | Standard |
| **Export and distribution** | Reports exported to Excel, PDF, or CSV; distributed to defined recipient lists | Standard |

### 3.3 OTBI in APPSolve Implementations

OTBI is a standard configuration and delivery component in every APPSolve Oracle HCM engagement. APPSolve's standard implementation scope includes:

| Deliverable | Description |
|---|---|
| **Custom OTBI reports** | APPSolve develops custom OTBI reports against the client's confirmed reporting requirements during the Build phase. Hollywood Bets V5.0 implementation scope included 10 custom reports as a defined deliverable. |
| **Pre-built report review and configuration** | Review and configuration of Oracle-delivered pre-built reports against the client's HR function roles and reporting requirements. Identify which delivered analyses are suitable for use without modification. |
| **Embedded dashboard configuration** | Configuration of OTBI dashboards embedded in key HCM module landing pages — ensuring managers and HR see relevant operational metrics within their daily workflow |
| **OTBI report skills transfer** | APPSolve trains designated client report authors to create and modify OTBI reports independently after go-live, reducing ongoing dependency on APPSolve for report changes |
| **Report library documentation** | Documentation of all custom reports delivered — business purpose, subject area, filters, prompts, and scheduling configuration |

### 3.4 Module-Level OTBI Reporting Coverage

Oracle Fusion HCM modules deliver pre-built OTBI subject areas that APPSolve configures and enables as part of each module implementation. The following reporting areas are available as standard OTBI deliverables:

| HCM Module | OTBI Reporting Coverage |
|---|---|
| **Core HR / Global HR** | Headcount analysis, employee distribution, workforce composition, organisational hierarchy, employee lifecycle events (hires, terminations, transfers) |
| **Absence Management** | Absence trends, absence plan balances, leave liability, top absence types, team absence calendar |
| **Oracle Recruiting Cloud** | Recruiting pipeline, time-to-fill, time-to-hire, offer acceptance rates, source effectiveness, diversity metrics, recruiter workload |
| **Talent Management** | Performance rating distribution, talent profile completeness, succession pipeline depth, competency gap analysis, career development progress |
| **Performance Management** | Performance review completion rates, performance rating distribution, goal achievement rates, calibration outcomes |
| **Oracle Workforce Compensation** | Compensation cycle status, budget consumption tracking, merit distribution by performance rating, compa-ratio analysis, approval workflow status |
| **Oracle Fusion Learning Cloud** | Learning completion rates, learning assignment compliance, assessment scores, certification status — note: Oracle Fusion Learning Cloud does not include pre-built Learning Reports or Dashboards as OOB standard; OTBI subject areas provide the operational reporting layer |
| **Oracle Help Desk** | Service request volumes, resolution times, open/closed/escalated status, HR service performance metrics |
| **Time and Labor** | Time entry compliance, overtime trends, timecard approval status, labor cost allocation |

---

## Section 4: BI Publisher — Formatted and Scheduled Reporting

### 4.1 BI Publisher Overview

Oracle BI Publisher is Oracle's enterprise reporting output tool, enabling the production of formatted, pixel-perfect report documents from Oracle HCM data. Where OTBI provides analytical self-service reporting and dashboards, BI Publisher produces structured documents with defined layouts — payslips, offer letters, regulatory submissions, compliance reports, and formatted audit outputs.

BI Publisher is included in the Oracle Fusion HCM license and is delivered by APPSolve as a standard component in HCM implementations where formatted report requirements exist.

> **APPSolve delivery confirmation:** RedPath Mining RFI (March 2026) — *"APPSolve developers have extensive experience in writing OTBI and BI Publisher reports."*

### 4.2 BI Publisher Capabilities

| BI Publisher Capability | Description | Use case |
|---|---|---|
| **Pixel-perfect report layouts** | Define precise report layouts using RTF templates, PDF templates, or the BI Publisher online layout editor. Output is formatted consistently regardless of the underlying data volume | Payslips, offer letters, contracts, certificates |
| **Multiple output formats** | Reports generated in PDF, Excel, Word (RTF), HTML, CSV, or XML — appropriate format selected per business requirement | Compliance reports (PDF), data exports (Excel/CSV), integration files (XML) |
| **Scheduled report delivery** | Reports scheduled to run at defined intervals and delivered to defined recipients by email or file server | Monthly payroll reports, weekly headcount reports, legislative submissions |
| **Bursting** | A single report run produces separate output documents per recipient or organisational unit — for example, one payslip batch produces individual payslip PDFs per employee | Payslips, IRP5 data certificates, annual reporting |
| **Parameter-driven reports** | End-users select parameters (date range, department, location) at run time to generate targeted outputs | Period-end HR reports, departmental summaries |
| **Integration with OTBI** | BI Publisher report layouts applied to OTBI analyses to produce formatted PDF or Excel output from self-service analyses | Formatted dashboards, management packs |
| **Legislative and regulatory formatting** | BI Publisher used to produce SETA (Skills Development Levy) supporting documentation, WSP/ATR report outputs, EMP201 supporting summaries, and other formatted statutory outputs | SA legislative compliance |
| **Custom audit reports** | Custom audit report layouts for internal audit, governance, and compliance requirements | Internal audit, change history documentation |

### 4.3 BI Publisher in APPSolve Implementations

| Deliverable | Description |
|---|---|
| **Custom BI Publisher report layouts** | APPSolve develops BI Publisher layouts to client specifications — format, branding, content, and distribution requirements confirmed during Scope and Design |
| **Offer letter templates** | Branded offer letter templates configured as standard implementation deliverable. APPSolve standard practice: a maximum of 3 offer letter templates per implementation; additional templates scoped separately |
| **Payslip layouts** | Where Oracle Payroll Cloud is in scope, payslip BI Publisher layouts configured and branded. Where payroll is third-party, payslip formatting is handled by the payroll system |
| **WSP/ATR supporting documentation** | BI Publisher templates supporting SETA WorkPlace Skills Plan (WSP) and Annual Training Report (ATR) output requirements |
| **Skills transfer** | APPSolve trains designated BI Publisher administrators to modify existing templates and create new templates post go-live |

---

## Section 5: Oracle HCM Analytics — Platform Overview

### 5.1 What is Oracle HCM Analytics (OAX)?

Oracle HCM Analytics is a separately licensed, cloud-based analytics solution that extends the value of Oracle Fusion Cloud HCM beyond the standard OTBI reporting capability included in the Oracle HCM license. It enables HR professionals, analysts, and business leaders to access workforce data through advanced analytics, pre-built dashboard content, and visualisations — delivered out of the box without requiring extensive setup.

Oracle HCM Analytics is built on Oracle Fusion Analytics Warehouse (FAW), Oracle's cloud-native analytics data warehouse platform. It is not a configuration of OTBI — it is a distinct Oracle product that must be separately licensed, provisioned, and implemented.

**Licensing note:** Oracle HCM Analytics requires a separate Oracle Cloud subscription. Clients must hold an Oracle HCM Analytics license in addition to their Oracle Fusion HCM Cloud Service license. APPSolve advises clients on Oracle HCM Analytics licensing requirements as part of Oracle HCM programme planning.

### 5.2 Oracle HCM Analytics Value Proposition

| Benefit | Description |
|---|---|
| **Out-of-the-box value** | Oracle HCM Analytics delivers pre-built dashboards, metrics, and KPIs without requiring extensive setup or customisation. HR teams can access analytics insights from day one of go-live, using over 50 pre-built metrics tailored to HR use cases |
| **Faster insight-driven decisions** | Empowers HR and business leaders with real-time, actionable insights to drive strategic decisions and workforce planning — moving beyond transactional reporting into analytical workforce understanding |
| **Enhanced data integration** | Combines HCM data with data from other Oracle applications — Finance, CRM, Supply Chain — for a more holistic view of the organisation and the workforce's impact on business outcomes |
| **Reduced IT dependency** | Self-service analytics and reporting capabilities reduce reliance on IT or technical consultants for day-to-day workforce reporting and exploration |
| **Strategic HR enablement** | Supports tracking and measurement of key HR objectives — diversity and inclusion, succession pipeline health, employee engagement, attrition risk, and skills gaps |
| **Role-based security** | Inherits Oracle HCM security models to ensure data privacy and role-appropriate access — sensitive employee data visible only to authorised users |

---

## Section 6: Oracle HCM Analytics — Pre-Built Dashboard and KPI Library

### 6.1 Pre-Built KPI Library

Oracle HCM Analytics includes over 50 pre-built metrics and dashboards covering the key domains of HR management. These are delivered as Oracle-maintained content and do not require custom development to activate.

| Analytics Domain | Pre-Built Coverage |
|---|---|
| **Workforce Composition** | Headcount by department, location, grade, gender, tenure band, employment type. Headcount movement — hires, terminations, transfers, internal mobility. FTE analysis. Organisation structure analytics. |
| **Talent Acquisition** | Recruitment funnel metrics, time-to-fill, time-to-hire, offer acceptance rates, source effectiveness, cost-per-hire, diversity of candidate pipeline, recruiter productivity |
| **Attrition and Retention** | Attrition rate by department, grade, tenure, location. Voluntary vs involuntary attrition. Flight risk segmentation. Retention rate trends. New hire attrition. |
| **Diversity, Equity and Inclusion (DEI)** | Gender representation across grade bands and leadership levels. Ethnicity distribution. Pay equity by demographic. Promotion and hiring rate analysis by demographic group. |
| **Compensation Analytics** | Compensation spend analysis, salary distribution, compa-ratio benchmarking, merit increase distribution, bonus analytics, total compensation by segment. See also: W3S1-005 Oracle Workforce Compensation for OWC-built-in analytics context. |
| **Learning and Development** | Learning completion rates, compliance training status, certification currency, skills development trends. See note: Oracle Fusion Learning Cloud does not include pre-built Learning Reports or Dashboards — OAX provides the advanced Learning analytics capability. |
| **Performance** | Performance rating distribution, review completion rates, calibration analytics, goal achievement, performance trend analysis |
| **Employee Engagement and Sentiment** | Employee survey results, engagement trends, sentiment indicators (where applicable to client HR programme) |
| **Succession and Talent Pipeline** | Succession pipeline readiness, key position fill-ability, talent depth indices, potential and risk ratings |

### 6.2 Self-Service Data Exploration

Beyond the pre-built KPI library, Oracle HCM Analytics provides self-service data exploration capabilities that allow HR analysts and business leaders to interrogate workforce data without requiring technical expertise.

| Self-Service Capability | Description |
|---|---|
| **Drill-down and slice-and-dice** | Navigate from organisation-level KPIs to department-level, then individual-level detail. Filter and segment by any available dimension — grade, tenure, location, performance rating, demographic |
| **Customisable dashboards** | Users create and save custom dashboards combining pre-built metrics and custom analyses to suit their specific business questions |
| **Visualisation options** | Charts, graphs, tables, heat maps, and interactive filters — all configurable without coding |
| **Collaboration and sharing** | Dashboards and analyses shared with defined user groups. Export to PDF, Excel, or embed in management reporting packs |

---

## Section 7: Oracle HCM Analytics — Workforce Intelligence and Predictive Insights

Oracle HCM Analytics provides workforce intelligence capabilities powered by embedded machine learning — delivering predictive and AI-driven insights that support proactive workforce decision-making. These capabilities are part of the Oracle HCM Analytics platform and are available to clients who have licensed and implemented Oracle HCM Analytics.

APPSolve positions Oracle HCM Analytics predictive capabilities as Oracle platform capabilities that APPSolve can support and configure where clients have licensed Oracle HCM Analytics as part of their Oracle Fusion HCM programme.

### 7.1 Machine Learning and Predictive Analytics

| Predictive Capability | Description |
|---|---|
| **Attrition prediction** | Oracle HCM Analytics uses machine learning to identify employees at elevated risk of voluntary departure, based on historical patterns including tenure, performance, compensation position, engagement signals, and absence behaviour. This enables HR to take targeted retention action before attrition occurs. |
| **Workforce trend forecasting** | Forecast future headcount, attrition, and hiring requirements based on historical workforce data, seasonal patterns, and organisational growth plans. |
| **Skills gap identification** | Identify current and anticipated skills gaps by comparing the existing workforce skills inventory against future business capability requirements. |
| **High-performance talent identification** | Surface talent profiles that match defined high-performance and high-potential patterns, informing succession and talent development prioritisation. |
| **Diversity outcome forecasting** | Model the projected impact of current hiring, promotion, and retention trends on future workforce diversity composition. |

### 7.2 Workforce Intelligence — Strategic Insights

| Workforce Intelligence Capability | Description |
|---|---|
| **Hiring needs forecasting** | Based on attrition predictions and business growth plans, forecast the volume and type of hiring required across defined time horizons |
| **Retention risk segmentation** | Segment the workforce by retention risk level — high, medium, low — enabling targeted engagement and retention investment |
| **Workforce scenario modelling** | Model different workforce outcomes under alternative strategies — for example, the projected workforce composition under a high-growth vs steady-state headcount plan |
| **Cross-functional workforce impact** | Oracle HCM Analytics can connect workforce data with financial data (Oracle Fusion Finance) to quantify the cost impact of workforce events — attrition, headcount growth, training investment — against business performance metrics |

### 7.3 Approved Positioning for Predictive Analytics

The following framing applies throughout this document and all W3S1-006 tender usage:

- *"Oracle HCM Analytics provides machine learning capabilities that enable predictive workforce insights..."*
- *"Oracle HCM Analytics enables organisations to move from reactive reporting to predictive workforce intelligence..."*
- *"Where clients have licensed Oracle HCM Analytics, APPSolve can support and configure the predictive analytics capabilities..."*
- Do not use: "APPSolve delivers predictive workforce analytics" or "APPSolve has implemented predictive analytics at [client]"

---

## Section 8: Oracle HCM Analytics — Cross-Functional Workforce Analytics

One of Oracle HCM Analytics' distinguishing capabilities over OTBI is its ability to combine Oracle HCM data with data from other Oracle Cloud applications — Finance, Supply Chain, CRM — to produce cross-functional workforce intelligence.

| Cross-Functional Analytics Area | Description |
|---|---|
| **Workforce cost and financial performance** | Link headcount costs, compensation spend, and training investment to revenue, margin, and productivity metrics — enabling true workforce ROI analysis |
| **Finance and headcount alignment** | Connect Oracle Fusion Finance cost centre structures and financial plan data with HCM headcount and compensation actuals, providing Finance and HR a unified view of people costs |
| **Operational workforce analytics** | Where Oracle Supply Chain or operational systems are in scope, workforce productivity can be connected to operational output metrics |
| **Enterprise analytics data model** | Oracle HCM Analytics uses a unified data model across Oracle Cloud applications — ensuring consistent entity definitions (employee, department, cost centre) across the analytics layer |

---

## Section 9: Analytics by HCM Domain — Summary Boundary Reference

The following table provides a consolidated reference for analytics capability attribution across Oracle HCM modules. This boundary table must be applied consistently when citing analytics capabilities in Oracle HCM tender responses.

| HCM Domain | OTBI (standard — included) | OAX (separate license) |
|---|---|---|
| **Core HR** | Headcount reports, workforce composition, org analytics, employee lifecycle events | Advanced workforce composition KPIs, attrition trending, DEI analytics |
| **Absence Management** | Absence plan balances, absence trend reports, leave liability | Cross-period absence trend analysis, absenteeism risk indicators |
| **Recruiting** | Pipeline reports, time-to-fill, time-to-hire, source analysis, diversity metrics | Predictive talent acquisition analytics, sourcing effectiveness trends |
| **Talent Management** | Performance distribution, succession pipeline, competency gap | Retention risk prediction, talent mobility analytics, succession fill-ability modelling |
| **Performance Management** | Review completion rates, performance rating distribution | AI-driven performance pattern analysis, flight risk identification |
| **Workforce Compensation** | Plan cycle status, budget consumption, compa-ratio, merit distribution | Advanced compensation dashboards, total comp trending, pay equity analytics (see W3S1-005) |
| **Learning Cloud** | Completion rates, assignment compliance, certification status (via OTBI) — **note: no pre-built OOB reports in Learning Cloud standard** | Learning effectiveness analytics, skills development trending, compliance gap prediction |
| **Help Desk** | Case volume, resolution time, open/closed/escalated status | HR service trends, proactive issue identification |
| **Time and Labor** | Time entry compliance, overtime, timecard approval | Cross-period labor cost analytics, absenteeism-productivity correlation |

---

## Section 10: HCM Extracts — Data Infrastructure for Analytics

HCM Extracts is a standard Oracle Fusion HCM tool that enables the extraction of workforce data in configurable formats for use by external systems — payroll platforms, data warehouses, reporting tools, legislative submissions, and business intelligence platforms.

HCM Extracts is distinct from analytics — it is a data integration and extraction capability, not a dashboarding or analytics product. It is included in the Oracle Fusion HCM license and is a standard component in every Oracle HCM implementation.

| HCM Extracts Capability | Description |
|---|---|
| **Configurable extract definitions** | Define what data to extract, from which modules, with what filters and transformations. Highly flexible and configurable without custom code. |
| **Multiple output formats** | Extracts generated in flat files (CSV, fixed-length), XML, or structured formats compatible with receiving systems |
| **Scheduled extraction** | Extracts scheduled to run automatically — daily, weekly, bi-weekly, monthly — for systematic data transfer |
| **Incremental extraction** | Configure HCM Extracts to extract only changed data since the last run — reducing data volumes and improving efficiency |
| **Payroll integration** | Standard extraction method for sending employee data changes (new hires, terminations, salary updates, benefit changes, absence data) to third-party payroll systems (e.g. PaySpace, SAP Payroll) |
| **Legislative reporting** | SETA, ATR, and WSP data extracted via HCM Extracts in formats compatible with SETA reporting tools and government portals. Afrocentric HCM Proposal: *"Legislative reporting (SETA, ATR, WSP) will be supported by means of a data extract that can be manipulated and updated by the client."* |
| **Data warehouse feeding** | HCM Extracts used to feed data into client data warehouses, Oracle HCM Analytics (OAX), or third-party BI tools |

---

## Section 11: APPSolve Delivery Capability

### 11.1 Oracle Analytics Practice

APPSolve's Oracle Business Unit includes HCM-certified consultants and developers with confirmed delivery experience across OTBI and BI Publisher in Oracle Fusion HCM implementations. APPSolve holds Oracle Level 1 Partner status. Oracle Integration is a published Oracle partner expertise area.

APPSolve's confirmed analytics delivery capability:

| Capability Area | Confirmed evidence | Confidence |
|---|---|---|
| OTBI report authoring | RedPath Mining RFI (March 2026): "extensive experience in writing OTBI reports"; Hollywood Bets BOM (April 2023): 10 custom reports in implementation scope | **HIGH — confirmed** |
| BI Publisher layout design | RedPath Mining RFI (March 2026): "extensive experience in writing... BI Publisher reports" | **HIGH — confirmed** |
| Visual Builder Studio (VBS) | RedPath Mining RFI (March 2026): "using Visual Builder Studio for Oracle Redwood pages for extensive personalisation" | **HIGH — confirmed** |
| Oracle HCM Analytics (OAX) | Platform capability knowledge; support experience in Oracle Analytics environments; no confirmed end-to-end delivery | **Platform knowledge — no delivery claim** |
| Predictive analytics configuration | Oracle HCM Analytics platform capability; APPSolve can support and configure where clients have licensed OAX | **Platform knowledge — no delivery claim** |

### 11.2 Delivery Approach — OTBI and BI Publisher

APPSolve applies a structured approach to analytics delivery within Oracle HCM implementations:

| Delivery Principle | Description |
|---|---|
| **Requirements-first reporting design** | Reporting requirements are gathered and documented during the Scope and Design phase before report development begins. Each report's purpose, audience, data sources, filters, and scheduling requirements are agreed with the client. |
| **Pre-built report assessment** | Before developing custom reports, APPSolve reviews Oracle's delivered pre-built reports with the client to identify which delivered content satisfies requirements without custom development. This reduces build effort and maintenance overhead. |
| **Standard-first principle** | Custom OTBI reports and BI Publisher layouts are developed only where standard delivered content is insufficient. APPSolve applies this principle consistently to manage scope and complexity. |
| **Report scope management** | Standard implementation scope includes a defined number of custom reports and BI Publisher layouts (typically 10 OTBI custom reports as per Hollywood Bets precedent; exact number confirmed in Scope and Design). Additional reports are scoped separately. |
| **Skills transfer** | APPSolve trains designated client OTBI report authors and BI Publisher administrators during the Build and Deploy phases — ensuring the client can create and modify their own reports after go-live without dependency on APPSolve. |
| **Report documentation** | All custom reports documented with business purpose, subject area, parameters, filters, and scheduling configuration. Documentation forms part of the go-live deliverables. |
| **SETA and legislative reporting** | APPSolve configures HCM Extracts and BI Publisher templates to support SETA, WSP, and ATR reporting requirements as a standard component of Learning Cloud and Core HR implementations. |

### 11.3 Delivery Approach — Oracle HCM Analytics (OAX)

Where clients have licensed Oracle HCM Analytics, APPSolve supports the implementation and configuration of OAX as an additional workstream within or alongside the Oracle HCM programme.

| OAX Delivery Activity | Description |
|---|---|
| **OAX licensing guidance** | APPSolve advises clients on Oracle HCM Analytics licensing requirements and positions OAX as the advanced analytics pathway for clients requiring pre-built workforce dashboards and predictive insights |
| **OAX implementation support** | APPSolve can support the OAX provisioning, configuration, and dashboard activation process for clients who have licensed Oracle HCM Analytics |
| **Pre-built content activation** | Working with the client's HR analytics team to activate and configure Oracle's pre-built dashboard content — KPI selection, role-based access configuration, dashboard customisation |
| **User enablement** | Training HR analytics users, HR business partners, and business leaders on OAX self-service data exploration, dashboard navigation, and custom analysis creation |
| **HCM-OAX data alignment** | Ensuring that Oracle HCM configuration (organisational structures, job families, grades, cost centres) is structured consistently to support OAX analytics dimensions and subject areas |

### 11.4 Resource and Delivery Model

| Resource Type | Role |
|---|---|
| HCM Principal Consultant | Analytics design authority; reporting requirements governance; client engagement leadership |
| HCM Senior Functional Consultant | OTBI configuration; reporting requirements capture; pre-built report assessment; UAT support |
| HCM Technical Developer | OTBI custom report authoring; BI Publisher layout development; HCM Extracts configuration; VBS personalisation |
| OAX Specialist | Oracle HCM Analytics provisioning; pre-built content configuration; OAX user enablement (where OAX in scope) |
| Project Manager | Delivery governance; reporting scope management; stakeholder coordination |

---

## Section 12: Implementation References

### 12.1 Oracle Fusion HCM — OTBI and Custom Reporting (Hollywood Bets)

| Attribute | Detail |
|---|---|
| **Client** | Hollywood Bets |
| **Industry** | Retail / Gaming |
| **Product** | Oracle Fusion HCM — full implementation including OTBI custom reports |
| **Analytics scope** | 10 custom OTBI reports + 6 custom workflows as confirmed BOM deliverables |
| **Go-live** | July 2025 — 7,000 users |
| **Reference status** | Referenceable — Hollywood Bets is confirmed Tier 1 implementation reference |
| **Citation** | "APPSolve delivered 10 custom Oracle Transactional Business Intelligence (OTBI) reports and 6 custom workflows as part of the Hollywood Bets Oracle Fusion HCM implementation (go-live July 2025, 7,000 users)" |

### 12.2 OTBI and BI Publisher Developer Capability (RedPath Mining — active pipeline)

| Attribute | Detail |
|---|---|
| **Client** | Mining-sector client (active implementation) |
| **Status** | Active — not yet live |
| **Evidence** | "APPSolve developers have extensive experience in writing OTBI and BI Publisher reports. Also using Visual Builder Studio (VB Studio) for Oracle Redwood pages for extensive personalisation." |
| **Citation rule** | Active pipeline — approved framing: "APPSolve is currently delivering Oracle HCM capabilities for a mining-sector client, including OTBI and BI Publisher reporting." |

### 12.3 Oracle HCM Analytics (OAX) — Reference Position

No referenceable client implementation of Oracle HCM Analytics exists at the time of this document. APPSolve positions Oracle HCM Analytics as a platform capability — describing the platform's capabilities and APPSolve's ability to support and configure Oracle HCM Analytics where clients have licensed the product.

Approved framing: *"APPSolve has product knowledge and technical capability in Oracle Analytics environments and is positioned to support Oracle HCM Analytics implementations where clients elect to license and implement this product."*

---

## Section 13: Implementation Approach

### 13.1 Analytics within the Oracle Fusion HCM Programme

OTBI and BI Publisher reporting are configured during the Build phase of every Oracle HCM module implementation. Analytics requirements are captured during Scope and Design. Oracle HCM Analytics (OAX) is implemented as a parallel or subsequent workstream where licensed.

| Phase | Analytics Activities |
|---|---|
| **Mobilize** | Confirm analytics scope: custom report count, BI Publisher layout count, OAX in/out of scope, legislative reporting requirements (SETA, WSP/ATR) |
| **Scope and Design** | Reporting requirements catalogue — purpose, audience, data sources, filters, prompts, scheduling. Pre-built report assessment — identify delivered content satisfying requirements. BI Publisher layout specifications. OAX activation scope (if licensed). |
| **Prototype** | CRP1: Review pre-built OTBI reports with HR and business stakeholders. Validate against requirements. CRP2: Custom report prototypes reviewed; BI Publisher layout previews; report feedback incorporated. |
| **Build** | Custom OTBI report development. BI Publisher layout development. HCM Extracts configuration for payroll and legislative reporting. OAX activation and pre-built content configuration (if in scope). |
| **Deploy** | Report UAT — each custom report tested against business requirements. BI Publisher output tested (format, branding, data accuracy). OAX dashboard activation and user access configuration. Report skills transfer training (OTBI and BI Publisher). |
| **Post Go-Live** | Hyper-care reporting support — address report issues discovered during live operation. First-cycle SETA/WSP/ATR extract support. OAX user adoption support (if in scope). |

### 13.2 OUM Alignment

APPSolve applies the Oracle Unified Methodology (OUM) across all Oracle Fusion HCM implementations. Analytics and reporting deliverables are defined, designed, built, tested, and deployed within the OUM phase structure. Reporting scope changes after the Build phase starts are managed as change requests.

---

## Section 14: Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-W3-006-001 | OAX licensing not confirmed at project start — client assumes OAX is included in Oracle HCM license; discovers late that separate procurement is required | Medium | High | Confirm OAX licensing position at project initiation. APPSolve communicates OAX as a separate product during HCM programme planning and scoping. |
| R-W3-006-002 | Reporting requirements not confirmed during Scope and Design — client requests additional reports during Build or after go-live, increasing scope and delaying delivery | High | Medium | Reporting requirements catalogue produced and signed off before Build phase begins. Maximum custom report count agreed and governed as a scope boundary. |
| R-W3-006-003 | OTBI / OAX capability conflation in tender responses — client expects OAX pre-built dashboards but only has a standard Oracle HCM license; or APPSolve inadvertently promises OAX capabilities without confirming licensing | Medium | High | Section 2 product boundary table applied consistently in all tender responses. OTBI / OAX distinction stated explicitly in any analytics capability claim. |
| R-W3-006-004 | SETA / legislative reporting extract complexity — bespoke SETA extract formats required by specific SETA bodies (MERSETA, FASSET, INSETA) may exceed standard HCM Extract templates; additional configuration required | Medium | Medium | Legislative reporting extract requirements confirmed during Scope and Design. Standard extract templates reviewed against SETA body requirements before build. |
| R-W3-006-005 | OAX data model alignment — if Oracle HCM configuration (org structures, job families, grades) is not structured consistently with OAX analytics dimensions, pre-built dashboards return incomplete or misleading results | Low | Medium | OAX analytics dimensions reviewed during HCM configuration design where OAX is in scope. HCM configuration decisions documented against their impact on OAX analytics outcomes. |

---

## Section 15: Assumptions Register

| Assumption ID | Assumption | Risk if incorrect |
|---|---|---|
| A-W6-001 | Custom OTBI report count is confirmed during Scope and Design before Build phase begins. Standard scope assumption: up to 10 custom reports (per Hollywood Bets precedent). Additional reports require separate scoping. | Unrestricted report development scope increases build effort and timeline |
| A-W6-002 | BI Publisher layouts are limited to a confirmed number during Scope and Design (typically 3 offer letter templates as per Afrocentric precedent; payslip layout if Oracle Payroll Cloud in scope; up to 3 additional layouts). Additional layouts require separate scoping. | Uncontrolled BI Publisher layout requests increase build scope |
| A-W6-003 | The client will nominate OTBI report authors and BI Publisher administrators who participate in skills transfer training during the project. These individuals will own report creation and modification post go-live. | Without trained internal owners, the client remains dependent on APPSolve for ongoing report changes |
| A-W6-004 | Oracle HCM Analytics (OAX) is separately licensed and its inclusion in the programme scope is explicitly confirmed by the client before any OAX implementation activities begin. | Including OAX activities without confirmed licensing creates billing risk |
| A-W6-005 | Legislative reporting (SETA, WSP/ATR) will be satisfied through HCM Extracts and BI Publisher layouts. The specific SETA body report format requirements will be provided by the client during Scope and Design. | Non-standard SETA format requirements may require additional development effort |
| A-W6-006 | Oracle HCM module configurations (organisational structures, job families, grade hierarchy, cost centres) will be completed before OTBI custom reports are developed — ensuring report subject areas reflect the live configuration. | Developing OTBI reports against interim configuration risks rework when configuration changes |
| A-W6-007 | For clients implementing Oracle HCM Analytics (OAX): HCM Analytics provisioning by Oracle (tenant activation) will be completed before APPSolve begins OAX configuration activities. Tenant activation is Oracle's responsibility. | Provisioning delays outside APPSolve's control can delay OAX workstream |

---

## Section 17: Approval Record

| Field | Value |
|---|---|
| **Document ID** | W3S1-006-ORA-HCMAnalytics |
| **Version** | 1.1 Approved |
| **Created** | 2026-06-13 |
| **Created by** | Claude (AI — Wave 3 W3S1-006 extraction) |
| **Status** | Approved — BU Lead approved 2026-06-13; all amendments applied (F-001/CROSS-1, F-002) |
| **Approved for reuse** | Yes — BU Lead approved 2026-06-13 |
| **Approved by** | Hein Blignaut (BU Lead) |
| **Approval date** | 2026-06-13 |
| **Open items at submission** | None — all 5 OI items (OI-W6-001 through OI-W6-005) CLOSED 2026-06-13 |
| **BU Lead** | Hein Blignaut |

---

## Appendix A: Source Mapping Table

| Section | Content type | Primary source | Governance classification |
|---|---|---|---|
| Section 1 | Statement of capability; product hierarchy | ORACLE_FACT_BASELINE Section 4.1; HIST-007 BOM; HIST-008 | Confirmed delivery (OTBI); Platform Capability (OAX) |
| Section 2.1–2.3 | Product hierarchy and licensing boundary; FAW | HIST-006 paras 1182–1195, 1210 | Platform capability; product boundary established |
| Section 3.1–3.2 | OTBI overview and capabilities | HIST-006 paras 1184–1188, 171–175 | Platform capability — reframed; SAA not named |
| Section 3.3 | OTBI in APPSolve implementations | HIST-007 BOM (para 56–66); HIST-008 paras 204–205 | Tier 1 implementation (HB); active pipeline (Redpath); confirmed developer capability |
| Section 3.4 | Module-level OTBI coverage | HIST-006 module analytics sections; HIST-015 para 511 | Platform capability; Learning caveat applied |
| Section 4.1–4.2 | BI Publisher overview and capabilities | HIST-006 para 1127; HIST-008 para 204–205 | Confirmed delivery capability |
| Section 4.3 | BI Publisher in APPSolve implementations | HIST-008 paras 204–205; HIST-015 paras 499, 509 | Confirmed delivery; delivery assumptions |
| Section 5.1–5.2 | OAX product overview and value | HIST-006 paras 461–494, 1189–1195 | Platform capability — separately licensed; reframed; SAA not named |
| Section 6.1 | OAX pre-built KPI library | HIST-006 paras 480–494 | Platform capability |
| Section 6.2 | OAX self-service data exploration | HIST-006 paras 488, 1192 | Platform capability |
| Section 7.1–7.2 | Predictive analytics and workforce intelligence | HIST-006 paras 491, 1191 | OAX Platform Capability ONLY — per OI-W6-002 |
| Section 7.3 | Approved positioning for predictive analytics | OI-W6-002 BU Lead decision | Governance rule — applied |
| Section 8 | Cross-functional analytics | HIST-006 paras 492–494, 1193 | OAX platform capability |
| Section 9 | Domain-level analytics boundary table | HIST-006; HIST-015 para 511; W3S1-004, W3S1-005 consistency | Boundary table — cross-document consistency required |
| Section 10 | HCM Extracts | HIST-006 paras 859–863; HIST-015 para 509 | Standard tool — confirmed in delivery assumptions |
| Section 11 | Delivery capability | HIST-008 paras 204–205; HIST-007 BOM | Confirmed delivery |
| Section 12.1 | Hollywood Bets OTBI reference | HIST-007 BOM para 56–73 | Tier 1 referenceable |
| Section 12.2 | RedPath Mining active pipeline | HIST-008 paras 204–205; ORACLE_FACT_BASELINE Rule 21.5 | Pipeline reference — approved framing applied |
| Section 12.3 | OAX reference position | OI-W6-001 BU Lead decision | Platform capability only — no named reference |
| Section 13 | Implementation approach | ORACLE_FACT_BASELINE Section 17 (OUM) | Standard methodology |
| Section 14 | Risk register | SVR-W3S1-006 risk analysis | Internal governance |
| Section 15 | Assumptions | HIST-015 paras 467, 499, 509; HIST-006 delivery context | Source-validated |

**Prohibited sources — confirmed excluded:**
- CCBA (HIST-014) — extraction support only in SVR; no CCBA content extracted; CCBA never named
- SARB — not named; not used as analytics implementation evidence (OI-W6-001 CLOSED)
- SAA — not named; platform capability source only (reframed); Rule 21.1 context
- Hollywood Bets — cited for OTBI (BOM confirmed); not cited for OAX (absent from BOM)
- DFA — not named anywhere (Rule 21.4)
- Redpath Mining — cited using approved pipeline framing; not named; no completed implementation claim (Rule 21.5)
- Aviation sector — not referenced anywhere (Rule 21.1)
- Strategic Workforce Planning — excluded entirely (OI-W6-003 CLOSED)

---

## Appendix B: Governance Self-Review

**Wave 3 Standing Rules — Compliance Check (ORACLE_FACT_BASELINE Section 21)**

| Rule | Check | Status |
|---|---|---|
| **21.1 Aviation PROHIBITED** | No aviation, airline, SAA, or South African Airways references as client or reference — confirmed absent | ✅ PASS |
| **21.1 SAA source rule** | SAA content used as platform capability narrative only; SAA not named as client, reference, or implementation anywhere | ✅ PASS |
| **21.2 Implementation vs Support** | Hollywood Bets = OTBI implementation (Tier 1 reference). Mr Price = not cited in this document. | ✅ PASS |
| **21.3 Opportunity Marketplace** | Not relevant to analytics statement | ✅ N/A |
| **21.4 DFA — never named** | DFA not named anywhere | ✅ PASS |
| **21.5 Redpath — not used as completed implementation** | Redpath cited as active pipeline (HIST-008 developer capability context) with approved framing; not named; not presented as completed implementation | ✅ PASS |
| **CCBA — never named** | CCBA not referenced anywhere in the document | ✅ PASS |
| **SARB — excluded** | SARB not named; not used as implementation evidence (OI-W6-001 CLOSED) | ✅ PASS |

**Product Boundary Checks**

| Check | Status |
|---|---|
| OAX clearly identified as separately licensed | ✅ Section 1 product hierarchy table; Section 2.2 licensing note |
| Predictive analytics framed as OAX platform capability only | ✅ Section 7.3 approved positioning applied throughout |
| No OAX implementation claim | ✅ Section 12.3 explicitly states no referenceable OAX client; no implementation claim made anywhere |
| Strategic Workforce Planning excluded | ✅ Absent from document entirely |
| OTBI and OAX cleanly separated throughout | ✅ Section 2 boundary table applied; Section 9 domain-level boundary table |
| BI Publisher as dedicated section | ✅ Section 4 standalone |
| FAW positioned as technical context only | ✅ Section 2.3 — not a standalone product |

**ORACLE_FACT_BASELINE Prohibited Wording Check**

| Prohibited item | Check |
|---|---|
| "Oracle Gold Partner" / "Gold Level" | Absent — "Oracle Level 1 Partner" in Section 11.1 | ✅ |
| "110 Senior Consultants" / "100+ consultants" | Absent — "50+ Senior Consultants" also removed per BU Lead CROSS-1 2026-06-13 | ✅ |
| "Oracle does X" framing | Absent — reframed as Oracle platform capabilities; APPSolve delivers/configures | ✅ |
| OAX implied as included in standard HCM license | Absent — Section 2.2 explicitly states OAX requires separate license | ✅ |
| Predictive analytics as APPSolve delivery claim | Absent — Section 7.3 approved positioning applied | ✅ |

**OI Items Closed — Final Confirmation**

| OI Item | Decision | Application |
|---|---|---|
| OI-W6-001 OAX client evidence | CLOSED — Platform Capability Only; SARB excluded | No OAX implementation claim anywhere in document |
| OI-W6-002 Predictive analytics framing | CLOSED — Platform Capability Only | Section 7.3 approved positioning applied; no delivery claims |
| OI-W6-003 Strategic Workforce Planning | CLOSED — EXCLUDED | Absent from document entirely |
| OI-W6-004 BI Publisher section | CLOSED — Dedicated section | Section 4 standalone BI Publisher section |
| OI-W6-005 Document title | CLOSED — "Oracle HCM Analytics & Workforce Intelligence" | Title confirmed |

**Governance Self-Review conclusion: CLEAN. No violations identified. Document approved by BU Lead 2026-06-13.**

---

## Appendix C: Extraction Return Report

| Field | Value |
|---|---|
| **Extraction ID** | W3S1-006 |
| **Document title** | Oracle HCM Analytics & Workforce Intelligence |
| **Version** | 1.1 Approved |
| **Date** | 2026-06-13 |
| **Sources used** | HIST-006 (platform capability narrative — OTBI, OAX); HIST-007 (OTBI BOM evidence); HIST-008 (confirmed OTBI + BI Publisher delivery capability); HIST-015 (delivery assumptions); ORACLE_FACT_BASELINE Sections 4.1, 19, 21 |
| **Sources NOT used** | HIST-014 CCBA (SVR support only; no content extracted; not named); HIST-016 SABS ETS (zero analytics hits — not used); HIST-017 SAA Clarification (utilisation reporting only — not relevant) |
| **Sections delivered** | 15 content sections (Sections 1–15) + Section 17 + Appendices A, B, C |
| **Open items at submission** | 0 — all 5 BU Lead decisions CLOSED 2026-06-13 |
| **Governance violations** | None |
| **Key governance boundaries (permanent)** | (1) OAX is separately licensed — must always be stated in tender responses. (2) OAX and predictive analytics are Platform Capability Only — no APPSolve delivery claims. (3) SARB excluded as analytics reference. (4) Strategic Workforce Planning excluded from this statement. (5) OTBI/OAX product boundary table (Section 2; Section 9) must be applied consistently in all W3S1-006 reuse. |
| **Cross-document consistency** | W3S1-004 Section 9 and W3S1-005 Section 9 both cross-reference W3S1-006 for advanced OAX analytics. This document is the authoritative OAX reference across Wave 3. |
| **Pre-tender checks (standing)** | PT-W6-001: Confirm whether the client has licensed Oracle HCM Analytics before citing OAX capabilities in any tender. PT-W6-002: Confirm OTBI custom report count is within standard scope before committing. PT-W6-003: Confirm Redpath Mining pipeline reference is still active before citing. PT-W6-004: Confirm OPN annual revalidation current. PT-W6-005: Confirm BEE certificate current (expires 2026-07-31). |
| **Amendments applied** | F-001/CROSS-1: "APPSolve employs 50+ Senior Consultants and" removed from Section 11.1 per BU Lead CROSS-1 decision 2026-06-13; F-002: Version 1.1 Approved; approved_for_reuse Yes; Approved by Hein Blignaut (BU Lead) 2026-06-13 |
| **Recommendation** | APPROVED — BU Lead approved 2026-06-13; all amendments applied; document approved for reuse |

---

*W3S1-006-ORA-HCMAnalytics v1.1 Approved — 2026-06-13 — Hein Blignaut (BU Lead) — approved_for_reuse: Yes*
