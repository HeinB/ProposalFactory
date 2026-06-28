---
document_id: ACU-SCOPE-BOUNDARY-GUIDE-V1
title: "APPSolve Acumatica Base Assumption Pack — Scope Boundary Guide"
version: "1.0-Approved"
status: "Approved v1.0 — WP15C 2026-06-18"
created: "2026-06-16"
created_by: "WP11I — Acumatica Base Assumption Pack"
pack_code: ACU
related_pack: ACU-BASE-ASSUMPTIONS-V1
scenario_count: 14
---

# Acumatica Base Assumption Pack — Scope Boundary Guide

**Pack:** ACU | **Scenarios:** 14 | **Status:** Approved v1.0 — WP15C 2026-06-18

This guide addresses the most common scope boundary disputes in Acumatica implementations. Each scenario shows where the line falls between APPSolve's scope and the client's scope (or a separately priced item), and provides the standard response for project managers and BAs when the issue arises.

---

## How to Use This Guide

Each scenario follows this format:

- **The situation:** What the client requests or expects
- **APPSolve's position:** In scope / Out of scope / Separately scoped
- **Rationale:** Which assumption applies and why
- **Standard response:** The language to use with the client

---

## Scenario 1: "Can Acumatica replicate exactly how our old system worked?"

**Situation:** The client expects Acumatica to be configured to replicate the exact workflows, screen layouts, and data structures of their legacy system (Pastel, SAGE, QuickBooks, or custom-built).

**APPSolve's position:** Out of scope as described. Legacy system replication is not the objective of an Acumatica implementation.

**Rationale:** ACU-GEN-006. Business process design adapts to Acumatica's standard workflows. Acumatica is the target system — the legacy system is not the design reference.

**Standard response:** "Our Acumatica implementation configures the system using Acumatica's standard business processes as the design framework. Where Acumatica's standard process differs from your current process, we facilitate a process design workshop to find the best fit within Acumatica. We do not reverse-engineer Acumatica to replicate your legacy system's behaviour — that approach produces poor quality implementations that are difficult to maintain and upgrade. Where your current process is genuinely Acumatica-incompatible, we document this as a gap and assess whether customisation is justified."

---

## Scenario 2: "We need Acumatica to handle payroll."

**Situation:** The client asks APPSolve to implement payroll processing within Acumatica, including PAYE calculations, payslip generation, and SARS submissions.

**APPSolve's position:** Out of scope. Acumatica does not have a South African payroll module. This is PaySpace's scope.

**Rationale:** ACU-PAY-001, ACU-EXC-002.

**Standard response:** "Acumatica does not include a South African payroll module. South African payroll — PAYE, UIF, SDL, IRP5s, EMP501 — is managed in PaySpace, which we integrate with Acumatica. The integration posts payroll journals from PaySpace into Acumatica's General Ledger so your financial accounts reflect payroll costs accurately. Payroll processing, payslip generation, and SARS submissions remain in PaySpace. If you do not have a PaySpace subscription, we can refer you to a PaySpace implementation partner."

---

## Scenario 3: "We want to bring in our data from the last 10 years."

**Situation:** The client expects APPSolve to migrate their full transaction history (invoices, journals, stock movements) from the legacy system into Acumatica going back 5–10 years.

**APPSolve's position:** Out of scope for the standard implementation. Historical transaction migration is a separately scoped and separately priced activity.

**Rationale:** ACU-DAT-005, ACU-EXC-005.

**Standard response:** "Our standard Acumatica implementation migrates opening balances — your financial position as at the agreed go-live date — and active master data (customers, suppliers, items). Historical transaction migration is not included because it is a significant additional effort: the data volume is large, the mapping complexity is high, and legacy data quality issues compound during migration. If you need historical transactions in Acumatica, we scope this as a separate project. We also recommend considering whether a read-only archive of your legacy data (retained in the legacy system or a separate archive tool) meets your actual query needs at lower cost."

---

## Scenario 4: "Can you also configure our e-commerce store to sync with Acumatica?"

**Situation:** The client has a Shopify, WooCommerce, or Magento store and expects Acumatica to sync inventory, orders, and customer data with the e-commerce platform.

**APPSolve's position:** Separately scoped. E-commerce integration is not part of the standard Acumatica base implementation.

**Rationale:** ACU-INT-004, ACU-INT-001.

**Standard response:** "E-commerce integration with Acumatica is a separately scoped integration item. The scope includes: product/inventory sync, order feed, fulfilment status updates, and customer master sync. The complexity depends on your e-commerce platform and the volume and frequency of data exchange. We scope this integration separately after understanding the specific platform, data volumes, and sync requirements. Acumatica has standard connectors for some e-commerce platforms which simplify the integration — we'll assess which applies to your platform during pre-sales."

---

## Scenario 5: "We want customised screens that look like our current system."

**Situation:** The client requests extensive Acumatica screen customisation to match the look and feel of their legacy system, including rebranded colour schemes, custom navigation menus, and screen layouts that mirror legacy screens.

**APPSolve's position:** Largely out of scope. Functional screen customisation (adding a missing field, reordering a lookup) is separately scoped. Aesthetic rebranding and layout replication to match the legacy system is not a supported use case.

**Rationale:** ACU-CFG-006, ACU-GEN-006.

**Standard response:** "Acumatica's screen customisation framework allows us to add fields, hide irrelevant fields, reorder columns, and relabel items where there is a genuine functional business need. What we do not do is redesign Acumatica screens to aesthetically match your previous system — that approach creates maintenance headaches with every Acumatica upgrade and does not produce a better implementation outcome. If you have specific screens where a field or layout change is operationally important, we capture those during Scope & Design, individually assess each one, and include the agreed set in the SOW. Customisations outside the agreed set are Change Requests."

---

## Scenario 6: "We'll handle our own testing — just give us the system."

**Situation:** The client wants to bypass the formal UAT process, claiming their team will test independently and just needs access to the configured system.

**APPSolve's position:** APPSolve requires a formal UAT process and written UAT sign-off before go-live proceeds. Informal self-testing without a sign-off milestone is not accepted as the basis for production migration.

**Rationale:** ACU-UAT-001, ACU-UAT-005.

**Standard response:** "We provide a UAT framework, test scenarios, and a defect log tool to make your testing efficient. Your team executes the testing — we support, not execute. What we do require is a formal UAT sign-off from your project sponsor before we proceed to production migration. This protects you: it creates a clear acceptance milestone, documents known issues (and their agreed disposition), and gives your project sponsor accountability for confirming readiness. We've seen implementations where informal testing missed issues that were caught during our UAT process. The sign-off step takes 30 minutes — it's worth it."

---

## Scenario 7: "We need Acumatica online by next month."

**Situation:** The client has an aggressive timeline that compresses the standard Acumatica implementation methodology below what is operationally feasible.

**APPSolve's position:** APPSolve does not commit to timelines that compromise delivery quality or skip mandatory milestones (data migration sign-off, UAT sign-off, go-live runbook approval). A realistic minimum timeline is confirmed during pre-sales based on scope.

**Rationale:** ACU-GEN-007, ACU-CUT-001.

**Standard response:** "We design our implementation timelines to match the scope you've confirmed. For a base Acumatica financial implementation with limited modules, our minimum realistic timeline is [X weeks — confirmed at pre-sales]. Compressing this further risks: insufficient UAT time (leading to go-live defects), insufficient data migration validation (leading to incorrect opening balances), and undertrained users. We will not commit to a timeline that we know is not achievable — that outcome is worse for you than taking the time to get it right. If there is a genuine external deadline (regulatory, audit, financial year), we work backwards from it and identify what scope is achievable by that date vs. what phases in later."

---

## Scenario 8: "We want to go live without running a test environment first."

**Situation:** The client wants to configure and test directly in the Production environment to save time, skipping the non-Production environment phase.

**APPSolve's position:** Not permitted. All configuration must be completed and validated in the non-Production environment before Production is touched.

**Rationale:** ACU-ENV-004.

**Standard response:** "We never configure Acumatica directly in a Production environment. Acumatica's cloud SaaS architecture provides a non-Production tenant at no significant additional cost. Skipping this step means any configuration error, data migration issue, or test defect occurs directly in your live financial system. Beyond the immediate risk, it also means your go-live is effectively a first attempt — with no rehearsal migration, no UAT cycle, and no clean go-live baseline. Acumatica's non-Production environment is your safety net. We use it and we require it."

---

## Scenario 9: "Can't you just fix that after we go live?"

**Situation:** During UAT, the client identifies a configuration gap but wants to go live anyway and fix it post go-live.

**APPSolve's position:** Depends on the nature of the issue. Cosmetic or non-blocking issues may be deferred. Business process-critical issues (incorrect tax configuration, broken approval workflows, inaccurate GL mapping) block go-live.

**Rationale:** ACU-UAT-005, ACU-CUT-001.

**Standard response:** "We assess each open UAT item against two criteria: can users operate the business process without this item, and is the financial data at risk? For non-blocking items (a report that's not aligned, a dashboard that's missing, a convenience feature), we can document them, agree a post-go-live resolution plan, and allow go-live to proceed with written acknowledgement from your project sponsor. For items that affect financial accuracy, workflow operation, or core business processes, we do not proceed to go-live until they are resolved — because fixing incorrect data in a live Production environment is significantly more costly and risky than the delay."

---

## Scenario 10: "We want APPSolve to also support our PaySpace configuration."

**Situation:** The client asks APPSolve to configure PaySpace (payroll structure, PAYE setup, leave policy configuration, employee master loading) as part of the Acumatica engagement.

**APPSolve's position:** Out of scope. PaySpace configuration is PaySpace's scope (or the client's PaySpace implementation partner's scope). APPSolve's scope is the Acumatica-PaySpace integration, not PaySpace itself.

**Rationale:** ACU-PAY-003.

**Standard response:** "PaySpace configuration — setting up payroll structures, leave types, employee records, tax codes, and company payroll policies — is managed by PaySpace or your designated PaySpace implementation partner. APPSolve's scope is connecting Acumatica to a configured, working PaySpace environment. If you need a PaySpace implementation partner, we can provide a referral. We need your PaySpace environment to be configured and running before we can design and test the Acumatica integration."

---

## Scenario 11: "We need the system to handle our BEE scorecard reporting."

**Situation:** The client requires Acumatica to produce B-BBEE scorecard reports or support BEE compliance tracking.

**APPSolve's position:** Standard Acumatica reporting does not include a dedicated B-BBEE scorecard module. This is assessed at pre-sales to determine whether an Acumatica Marketplace ISV or a custom GI/report approach meets the requirement.

**Rationale:** ACU-REP-001, GAP-ACU-R04.

**Standard response:** "B-BBEE reporting in Acumatica is not a standard module. We assess your B-BBEE reporting requirements during Scope & Design and determine the best approach: there are Acumatica Marketplace ISV products for BEE compliance tracking, and it may be possible to support BEE spend analysis through Generic Inquiries configured from Acumatica's supplier and procurement data. The right approach depends on the complexity of your BEE scorecard requirements. We confirm this during pre-sales and include it in the SOW if it's in scope."

---

## Scenario 12: "We'll do the data cleanup before go-live — we just need Acumatica to import whatever we give you."

**Situation:** The client commits to providing clean data but delivers data with significant quality issues (duplicates, incorrect formats, missing mandatory fields, referential integrity failures).

**APPSolve's position:** APPSolve validates the data against Acumatica's data model and returns quality issues to the client for correction. APPSolve does not cleanse, de-duplicate, or transform data beyond what is necessary for format compliance.

**Rationale:** ACU-DAT-003, ACU-CUS-004.

**Standard response:** "We run every client-provided dataset through our migration validation process, which checks format, referential integrity, and mandatory fields against Acumatica's data model. When we find issues, we return a defect log to your team for correction. We do not correct the data ourselves — your team knows which records are correct, which are duplicates, and what the right data should be. We revalidate after you correct the data. This cycle continues until the data passes validation. Data quality issues that are not resolved by the agreed data submission deadline delay the migration and the go-live date."

---

## Scenario 13: "We want separate Acumatica tenants for each of our five subsidiaries."

**Situation:** The client operates five subsidiary companies and wants each on a separate Acumatica tenant.

**APPSolve's position:** Five separate tenants is a major scope item. Each tenant requires its own implementation effort, licence, and ongoing maintenance. This is separately scoped and not assumed by default.

**Rationale:** ACU-GEN-008, ACU-ORG-001.

**Standard response:** "Acumatica supports multi-entity operations within a single tenant through its multi-company and multi-branch functionality, which is significantly more efficient to implement and maintain than five separate tenants. We recommend exploring the single-tenant multi-entity approach first — it consolidates intercompany transactions, shared master data, and group reporting under one implementation. Separate tenants are appropriate only where subsidiaries have fundamentally different configurations, different Acumatica licence tiers, or where there is a legal or security requirement for complete data segregation. If separate tenants are confirmed, each is scoped and priced independently."

---

## Scenario 14: "We need Acumatica to integrate with our customer's ERP system for automated order placement."

**Situation:** The client wants a B2B EDI-style integration between Acumatica and their major customer's procurement system (SAP, Oracle, or a custom ERP) for automated purchase order and invoice exchange.

**APPSolve's position:** Separately scoped. B2B ERP-to-ERP integration (EDI or direct API) is complex and is not a standard Acumatica base implementation item.

**Rationale:** ACU-EXT-009, ACU-INT-001.

**Standard response:** "ERP-to-ERP integration — whether via EDI standards like X12 or EDIFACT, or via direct API — requires individual scoping. The complexity depends on: the customer's ERP platform and API capabilities, the document types involved (PO, PO acknowledgement, ASN, invoice, payment advice), the transformation logic between your Acumatica data model and the customer's data model, and the error handling and reconciliation requirements. We assess this during pre-sales and scope it as a named integration item. In some cases, a managed EDI VAN (Value-Added Network) provider is the most practical solution — we evaluate this alongside direct API options."

---

*Acumatica Base Scope Boundary Guide v1.0-Draft | WP11I | 2026-06-16*
*14 scenarios | Status: Draft — Pending BU Lead Approval*
