---
document_id: HCM-COMPENSATION-ASSUMPTIONS-V1
title: "Oracle Fusion Workforce Compensation — Assumptions, Exclusions, and Customer Responsibilities"
version: "1.1"
status: "Approved v1.0"
created: "2026-06-15"
created_by: "WP11 — Commercial Assumptions Library"
approved_by: "Oracle HCM BU Lead"
approved_date: "2026-06-19"
approved_for_reuse: true
lifecycle_status: APPROVED
category: "Commercial / Assumptions"
scope: "Oracle Fusion Workforce Compensation Cloud Service (B109620): merit cycles, bonus plans, manager worksheets, budget pools, total compensation statements. Extends HCM_BASE_ASSUMPTIONS_V1.md."
apply_with: "TENDER_ASSUMPTION_ASSEMBLY_RULES.md"
parent_pack: "HCM_BASE_ASSUMPTIONS_V1.md"
assumption_count: 30
oracle_part_number: "B109620"
kb_reference: "W3S1-005-ORA-WorkforceCompensation.md"
bu_lead_review_items: []
---

# Oracle Fusion Workforce Compensation — Assumptions V1.0

**Scope:** This document governs Oracle Fusion Workforce Compensation Cloud Service (B109620) implementations. It extends `HCM_BASE_ASSUMPTIONS_V1.md`. Oracle Workforce Compensation enables merit reviews, bonus cycles, manager compensation worksheets, budget pools, and total compensation statements. This is distinct from Oracle Fusion Global Payroll (which runs payroll calculations) and from Oracle Compensation and Benefits (benefits administration, included in HCM Base B85800).

**Load order:** HCM Base Assumptions (complete) → this pack (additive). For full HCM suite implementations, also load Talent Management pack where performance ratings feed into compensation decisions.

---

## 43. Compensation Framework Assumptions

**COM-FRM-001**  
APPSolve configures Oracle Workforce Compensation (WFC) to implement the client's compensation review process. The configuration scope covers: compensation plans, compensation components (merit, bonus, one-time payments), grade and salary range configuration, budget distribution, manager worksheets, approval workflows, and total compensation statements. The design of the compensation framework is agreed in the Scope and Design phase.

**COM-FRM-002**  
The client is responsible for providing all compensation structure data before WFC configuration commences. This includes: (a) salary grade structure (grades, steps, minimum/midpoint/maximum salary ranges per grade); (b) job-to-grade mapping; (c) compensation plan eligibility rules (which employees participate in each plan); (d) budget amounts and distribution model. APPSolve configures Oracle WFC based on this data; it does not design the client's compensation philosophy or grade structure.

**COM-FRM-003**  
The budget model (top-down or bottom-up) for the compensation cycle is confirmed in the Scope and Design phase. APPSolve configures the budget pool architecture as agreed. The default implementation is a single budget model. Where the client requires both top-down budget allocation and bottom-up budget tracking simultaneously, this is assessed as a scope addition.

**COM-FRM-004**  
Oracle Workforce Compensation is configured to reflect the client's compensation cycle timing (annual, semi-annual, or quarterly review periods). The cycle schedule is confirmed in the Scope and Design phase. Multiple concurrent compensation cycles (for example, a merit cycle for permanent staff and a separate review cycle for contractors) are assessed as a scope addition.

---

## 44. Merit and Incentive Plan Assumptions

**COM-PLN-001**  
A maximum of one (1) merit plan is configured in base scope. A merit plan governs the annual salary review cycle — defining eligible employees, salary increase guidelines, budget allocation, manager worksheet access, and approval routing. Each additional merit plan (for example, a separate merit plan for a business unit, employment category, or subsidiary with a different review cycle) constitutes a Change Request.

**COM-PLN-002**  
A maximum of one (1) short-term incentive (bonus) plan is configured in base scope. A bonus plan governs the discretionary or formulaic bonus award cycle. The plan design (eligible employees, target bonus percentages, payout calculation method, and approval routing) is confirmed in the Scope and Design phase. Each additional bonus plan constitutes a Change Request.

**COM-PLN-003**  
Oracle Workforce Compensation supports one-time payment awards (spot bonuses, recognition payments, retention payments) as a distinct plan type. APPSolve configures one-time payment capability where included in the agreed plan inventory. One-time payment plans are subject to the same plan count assumptions as merit and bonus plans.

**COM-PLN-004**  
Where Oracle Fusion Talent Management (B94925) is also in scope, Oracle WFC is configured to surface the employee's performance rating on the manager's compensation worksheet. This integration eliminates the need for the manager to switch between Talent Management and WFC during the compensation cycle. APPSolve configures this integration as part of the combined Talent + WFC implementation.

**COM-PLN-005**  
Compensation guidelines — the matrix or table that defines recommended salary increase ranges by performance rating and compa-ratio band — are configured in Oracle WFC based on rules provided by the client. The client provides the complete compensation guidelines matrix before worksheet configuration commences. APPSolve configures the matrix; it does not define the client's compensation guidelines.

---

## 45. Manager Worksheet Assumptions

**COM-WKS-001**  
Oracle Workforce Compensation manager worksheets provide managers with a structured view of their team's compensation data, enabling them to allocate salary increases and bonuses within their assigned budget. APPSolve configures manager worksheets as part of the standard WFC implementation. Worksheet fields, column visibility, and manager instructions are agreed in the Scope and Design phase.

**COM-WKS-002**  
The columns displayed on the manager worksheet (for example: current salary, proposed salary, increase amount, increase percentage, compa-ratio, performance rating, and budget remaining) are configured based on the client's requirements, confirmed in the Scope and Design phase. Column count does not in itself constitute a scope addition; however, calculated columns requiring custom formula logic are assessed per complexity.

**COM-WKS-003**  
Read-only higher-level manager access to team worksheets (second-level manager visibility) is a standard WFC feature. APPSolve configures manager hierarchy access as part of the standard implementation. The client provides confirmation of the management hierarchy structure in Oracle HCM before worksheet configuration commences.

---

## 46. Compensation Approval Workflow Assumptions

**COM-WFL-001**  
A maximum of one (1) approval workflow is configured per compensation plan in base scope. The approval workflow defines the approval routing for completed manager worksheets (for example: manager → HR Business Partner → HR Director → approved). Additional approval workflows per plan or conditional approval routing based on increase thresholds constitute a Change Request. HCM Base assumption HCM-WFL-001 applies.

**COM-WFL-002**  
Oracle Workforce Compensation approval workflow notifications (worksheet assignment notifications, approval notifications, deadline reminders, and approval confirmation notifications) are configured using Oracle's standard notification framework. Custom HTML-branded email templates are not included in base scope. HCM Base assumption HCM-WFL-004 applies.

---

## 47. Total Compensation Statement Assumptions

**COM-TCS-001**  
Oracle Workforce Compensation includes the ability to generate Total Compensation Statements for employees. APPSolve configures a standard Oracle BI Publisher-based Total Compensation Statement template as part of the WFC implementation. The standard template includes compensation components configured in Oracle WFC and Oracle Benefits (where applicable). Custom-branded TCS templates with significant layout changes or additional data sources are assessed as a scope addition.

**COM-TCS-002**  
Total Compensation Statements reflect compensation data from Oracle WFC and Oracle Benefits (if included in scope). Data from third-party benefit providers, external pension fund valuations, long-term incentive (LTI) platforms, or payroll systems (for example, medical aid contributions, provident fund employer contributions) is only included in the TCS where it is loaded into Oracle HCM through a structured data feed or data migration. Third-party compensation data integration is assessed separately.

**COM-TCS-003**  
Oracle Total Compensation Statements are generated and published to employees via Oracle HCM self-service. APPSolve configures the statement publishing rules (which employees receive statements, and when they become visible in self-service). The client's HR Compensation team is responsible for reviewing statements before publication; APPSolve configures the statement; it does not review statement accuracy on behalf of the client.

---

## 48. Compensation Data and Reporting Assumptions

**COM-DAT-001**  
Compensation history migration is not performed as a standalone WFC deliverable. Employee current salary data is migrated as part of the HCM Base employee data migration (HCM-DAT-001 through HCM-DAT-004 apply). Historical salary change history (for example, every salary increase or grade change over the past 5 years) is not included in the base data migration scope. Historical compensation data required for reporting purposes is assessed separately.

**COM-DAT-002**  
Salary grade and salary range data (minimum, midpoint, maximum per grade) is loaded into Oracle WFC based on data provided by the client in APPSolve's required template format. The client is responsible for the accuracy and completeness of grade and salary range data. APPSolve loads the data and confirms it is correctly reflected in Oracle WFC.

**COM-DAT-003**  
Third-party salary benchmarking data (Remchannel, Mercer, Korn Ferry, 21st Century, or equivalent) is not loaded into Oracle WFC as part of this implementation. Where the client wishes to use external market data to inform salary ranges, the client must provide grade-to-market data mapping, and APPSolve will assess whether it can be configured as a salary range input in Oracle WFC.

**COM-DAT-004**  
Oracle Transaction Business Intelligence (OTBI) provides standard compensation reporting capability. APPSolve configures up to the agreed number of custom OTBI reports for compensation analytics during the implementation (subject to HCM Base reporting scope, HCM-REP-001 through HCM-REP-003). Where pay equity analysis reporting is required, APPSolve provides guidance on available OTBI subject areas; the design of a pay equity reporting framework is assessed per complexity.

---

## 49. Compensation Training Assumptions

**COM-TRN-001**  
APPSolve delivers train-the-trainer (TTT) training for Oracle Workforce Compensation across three user populations: (1) **Compensation Administrator** — plan administration, budget management, cycle management, compensation statement publishing, OTBI compensation reporting, and Oracle WFC system administration; (2) **HR Business Partners / HR Managers** — review of manager worksheets, compensation cycle oversight, approval management; (3) **Managers** — compensation worksheet navigation, salary increase and bonus allocation, budget tracking, and approval submission.

**COM-TRN-002**  
Employee training for Total Compensation Statement self-service access is included in the standard HCM employee self-service training (HCM Base assumption HCM-TRN-002). No separate training session is delivered for the employee TCS view.

---

## 50. Compensation Exclusions

**COM-EXC-001**  
**Oracle Fusion Global Payroll:** Oracle Fusion Global Payroll (which calculates gross-to-net payroll, manages statutory deductions, and produces payslips) is a separate Oracle product and is not part of Oracle Workforce Compensation Cloud Service (B109620). APPSolve implements payroll interface outputs to the client's payroll provider as part of HCM Base (HCM-3PT-006). HCM Base assumption HCM-EXC-001 applies.

**COM-EXC-002**  
**Oracle Incentive Compensation (Variable Pay / Commission Management):** Oracle Fusion Incentive Compensation (B92085) is a distinct Oracle Cloud product for managing commission plans and incentive compensation for sales and variable-pay workforces. It is not part of Oracle Workforce Compensation Cloud Service (B109620). Where the client requires commission management, Oracle Incentive Compensation is assessed and priced as a separate engagement.

**COM-EXC-003**  
**Long-Term Incentive (LTI) and Equity Plan Administration:** Administration of long-term incentive programmes (restricted share units, performance shares, share options, share appreciation rights) is excluded from Oracle Workforce Compensation scope. LTI administration requires a dedicated equity management platform (Certent, Carta, Morgan Stanley Equity Edge, or equivalent). Integration between an equity management platform and Oracle HCM is assessed as a separately scoped OIC integration.

**COM-EXC-004**  
**Third-Party Salary Benchmarking Integration:** Loading, updating, and maintaining third-party salary benchmarking data (Remchannel, Mercer, Korn Ferry, 21st Century, or equivalent) within Oracle WFC as a live integration is excluded from base scope. Where the client wants to reference market data ranges in Oracle WFC, this is assessed as a scope addition, subject to the data provider's API or file export capability.

**COM-EXC-005**  
**Pay Equity Compliance Audit:** APPSolve configures Oracle WFC to support the data required for pay equity analysis. Conducting a formal pay equity compliance audit, presenting pay equity analysis results to HR leadership, or producing legal opinions on pay equity compliance under the Employment Equity Act is excluded from APPSolve's scope. These activities are the client's and their employment law advisers' responsibility.

**COM-EXC-006**  
**IFRS 2 (Share-Based Payment) Accounting:** Calculation and reporting of IFRS 2 share-based payment expenses, fair value adjustments, and disclosure requirements for financial statements is excluded from Oracle Workforce Compensation scope. IFRS 2 accounting is the client's finance and external auditor's responsibility, supported by specialist equity accounting tools.

**COM-EXC-007**  
**Retroactive Compensation Adjustments:** Processing retroactive salary increases (back-paying employees from a prior effective date based on a cycle that was completed late) is not a standard WFC feature. Where retroactive compensation adjustments are required, the approach is assessed during the Scope and Design phase, as it may require manual payroll interface adjustments outside Oracle WFC.

---

## Approval Record

All BU Lead review items confirmed. Status: **Approved v1.0 — 2026-06-19 (WP16C)**.

| Decision ID | Item | Confirmed Position | Resolved |
|---|---|---|---|
| BU-COM-001 | Merit plan count | One (1) merit plan in base scope | WP16C 2026-06-19 |
| BU-COM-002 | Bonus plan count | One (1) short-term incentive (bonus) plan in base scope | WP16C 2026-06-19 |
| BU-COM-003 | Compensation history migration | Zero standalone history migration; current salary migrated via HCM Base | WP15F 2026-06-19 |
| BU-COM-004 | Total Compensation Statement | Standard Oracle BI Publisher TCS template in base WFC scope | WP15F 2026-06-19 |
| BU-COM-005 | Pay equity reporting | OTBI guidance on subject areas; no standard pay equity extract in base scope | WP16C 2026-06-19 |

---

*HCM_COMPENSATION_ASSUMPTIONS_V1.1 | WP11 — Commercial Assumptions Library | 2026-06-15 | **Approved v1.0 — 2026-06-19 (WP16C)***  
*30 assumptions / exclusions / responsibilities across Sections 43–50 (+10 pending authoring — BAU v1.2 additions; sections defined, wording TBD)*  
*Parent pack: HCM_BASE_ASSUMPTIONS_V1.md | Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md*
