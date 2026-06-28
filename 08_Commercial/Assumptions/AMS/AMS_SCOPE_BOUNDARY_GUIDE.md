---
document_id: AMS-SCOPE-BOUNDARY-GUIDE
title: "APPSolve AMS — Scope Boundary Guide"
version: "1.0"
created: "2026-06-15"
created_by: "WP11E — AMS / Managed Services Assumptions Pack"
status: "Draft — Pending BU Lead Review"
applies_to: "All APPSolve AMS agreements (Oracle, Acumatica, BeBanking)"
companion_to: "AMS_ASSUMPTIONS_V1.md"
---

# APPSolve AMS — Scope Boundary Guide

This document defines scope boundaries for APPSolve Application Managed Services (AMS) agreements. It is the companion document to `AMS_ASSUMPTIONS_V1.md`. Where the assumptions state what APPSolve does and does not do, this guide explains what the boundary looks like in practice — with examples of what is IN scope and OUT of scope, and how to handle common disputes.

**Authority:** Where a client request does not clearly fall into IN or OUT of scope, escalate to the AMS Account Manager before committing. Do not make ad hoc scope decisions without escalation.

---

## How to Use This Guide

1. When a client request arrives, check it against the boundary tables below.
2. **IN SCOPE** = handle as incident, service request, or within monthly hours allocation.
3. **OUT OF SCOPE** = communicate clearly to the client, log the request, and raise a CR or refer to a project engagement.
4. **ASSESS** = escalate to AMS Account Manager before proceeding.
5. Document every out-of-scope communication in the monthly report.

---

## 1. Core AMS Boundary: Support vs Project

This is the most important boundary in AMS. The distinction determines whether work is done within the monthly AMS fee or separately invoiced as a project.

| Characteristic | AMS Support | Project Work |
|---|---|---|
| System already exists and configured | Yes | No — new configuration |
| Restoring or adjusting existing functionality | Yes | No — creating new functionality |
| Work completable within monthly hours | Yes | No — requires separate estimate |
| Repeatable and recurring | Often | No — one-time delivery event |
| Requires Scope and Design document | No | Yes |
| Requires formal project management | No | Yes |
| Covered by AMS SLA | Yes | No — project timeline |
| Requires formal acceptance / UAT sign-off | Depends on complexity | Yes |

**Rule of thumb:** If you need to design something new, write a Scope and Design document, run a testing cycle, and get a formal sign-off from the client's leadership — it's a project, not AMS.

---

## 2. Oracle Fusion HCM AMS Boundaries

| IN SCOPE (AMS standard) | OUT OF SCOPE (project or excluded) | ASSESS CASE BY CASE |
|---|---|---|
| Adjusting an existing workflow approval limit | Designing a new approval workflow type | Restructuring an existing approval hierarchy (e.g., adding a new approval level) |
| Assigning a new Oracle role to an existing user | Creating new custom Oracle roles | Adding a new duty role to an existing custom role |
| Adding a new HCM organisation (department, location, job, grade) | Implementing a new Oracle HCM module (e.g., adding Learning where it was never implemented) | Adding a new legal employer or business unit |
| Updating an existing OTBI report (filter or column change) | Developing a new OTBI report | Adding a new subject area to an existing OTBI report |
| Resolving an integration error in an existing OIC integration | Building a new OIC integration | Modifying an existing integration to add a new data field (scope depends on effort) |
| Updating a user's absence plan eligibility | Designing a new absence type | Adding a new absence reason (usually SR-level config) |
| Processing a bulk load request using an existing HDL template | Developing a new HDL template for a new data object | Adding a new column to an existing HDL template |
| Year-end compensation cycle support (existing Workforce Compensation setup) | Redesigning the compensation plan structure | Adding a new merit plan to an existing compensation cycle |
| Updating performance review ratings scale | Redesigning the performance review template | Adding a new performance section to an existing template |
| Payroll interface error investigation | Redesigning the payroll interface | Adding a new data field to the payroll extract |

---

## 3. Oracle Fusion ERP AMS Boundaries

| IN SCOPE (AMS standard) | OUT OF SCOPE (project or excluded) | ASSESS CASE BY CASE |
|---|---|---|
| Adding a new GL account to an existing COA value set | Redesigning the Chart of Accounts (adding or removing segments) | Adding a new segment value set |
| Updating an approval limit in the purchase order approval workflow | Adding a new approval workflow type (e.g., new Capex workflow where none existed) | Adding a new approval group to an existing workflow |
| Adding a new supplier to Oracle AP using FBDI | Migrating a new entity's full supplier master (bulk migration = project) | Bulk loading 50+ suppliers as a batch SR |
| Updating payment terms on an existing supplier | Configuring a new payment method type | Setting up a new bank account for an existing supplier |
| Investigating a failed bank reconciliation | Designing a new bank statement reconciliation rule | Updating an existing reconciliation rule |
| Adding a new GL period to the accounting calendar | Changing the financial year structure | Adding a new secondary ledger period |
| Updating an existing FRS report column | Developing a new FRS financial statement | Adding a new row set to an existing FRS report |
| Investigating an oracle.acm.oracle.com error | Applying an Oracle patch (EBS on-premises) | Raising an Oracle SR for a platform defect |
| Adding a user and assigning standard ERP roles | Creating a new custom ERP role | Cloning an existing role and modifying duties |
| Resolving an AP invoice hold | Redesigning the AP invoice hold rules | Updating existing invoice matching tolerances |

---

## 4. Acumatica AMS Boundaries

| IN SCOPE (AMS standard) | OUT OF SCOPE (project or excluded) | ASSESS CASE BY CASE |
|---|---|---|
| Adjusting an existing approval map | Designing a new Acumatica approval map from scratch | Adding a new step to an existing approval map |
| Adding a new Acumatica user and assigning standard roles | Designing new custom Acumatica security roles | Modifying an existing custom role's permissions |
| Adding a new chart of accounts code segment value | Restructuring the Acumatica chart of accounts | Adding a new subaccount segment |
| Adjusting an existing Acumatica report using Report Designer | Developing a new Acumatica generic inquiry or report | Adding a new column to an existing report |
| Investigating a Acumatica error message | Developing a new Acumatica customisation | Investigating a Acumatica SDK or customisation conflict |
| Adding a new customer or vendor to Acumatica | Migrating a new entity's full customer or vendor master | Bulk loading 100+ customers from a newly acquired entity |
| Updating existing Acumatica email notification templates | Developing new Acumatica Push notifications | Adding a new event trigger to an existing notification |
| PaySpace integration error investigation (AMS scope) | Redesigning the Acumatica-PaySpace integration | Modifying the PaySpace integration mapping for a new payroll element |

---

## 5. OIC Integration AMS Boundaries

| IN SCOPE (AMS standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| Investigating and resolving an error in an existing OIC integration | Building a new OIC integration | Modifying an existing integration to add a new source field or target mapping |
| Resubmitting failed messages from the OIC error console | Rebuilding a deprecated integration from scratch | Updating an OIC connection when a third-party changes their endpoint URL |
| Monitoring OIC error console (where contracted) | Proactive integration performance monitoring | Reviewing OIC activity logs for audit purposes |
| Updating SFTP credentials when a third party rotates credentials | Migrating an integration from one OIC instance to another | Testing an integration after Oracle quarterly update |
| Investigating OIC connectivity loss | Replacing an OIC adapter (e.g., swapping FTP adapter for REST adapter) | Updating an OIC integration for a new version of a third-party API |

---

## 6. BeBanking AMS Boundaries

| IN SCOPE (AMS standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| Investigating a BeBanking payment file error in OIC | Building a new BeBanking integration for a new bank | Adding a new bank to an existing BeBanking integration |
| Investigating an MT940 bank statement import failure | Redesigning the bank statement import process | Updating the MT940 format mapping for a bank format change |
| Escalating a BeBanking platform issue to BeBanking | Managing BeBanking's H2H portal or bank connectivity | Testing after BeBanking releases a new format version |
| Advising on BeBanking payment file field mapping | Re-mapping the payment file for a new payment type | Adding a new payment category to the existing payment file |

---

## 7. Common AMS Scope Disputes — How to Handle

### "The system used to do X and now it doesn't — you need to fix it."
**First question:** Was X in the original implementation scope? Check the Scope and Design document.  
- If YES: this is a defect — fix it under AMS incident management, no charge.  
- If NO: this is either (a) the client's expectation of functionality that was never configured (enhancement) or (b) a client-requested change that was made without APPSolve involvement (configuration drift — SR, billed against allocation).  
- If UNSURE: escalate to AMS Account Manager; check the implementation project documentation.

### "We just acquired a new company — can you add them to Oracle?"
**Answer:** Adding a new legal entity, new ledger, new operating unit, or new business unit is a project — it requires a Scope and Design document, configuration, data migration, testing, and go-live. This is not AMS work. Raise a project enquiry and provide a separate estimate.  
**Exception:** Adding a new department, location, or cost centre under an existing legal entity is a service request.

### "We need a new report."
**Answer:** Developing a new OTBI report, FRS report, or Acumatica report is out of AMS scope. Adjusting an existing report (adding a filter, changing a column, updating a prompt) is a service request within the monthly hours allocation.

### "Can you add a new module?"
**Answer:** Implementing a new Oracle Fusion module (e.g., adding Oracle Compensation where only Core HR was implemented) is a project. AMS covers the modules that are currently live and in the agreed AMS scope. New module scoping requires a project estimate.

### "Oracle just released their quarterly update and something broke."
**Answer:** Oracle quarterly update regressions are AMS incidents — APPSolve investigates and resolves within the standard SLA at no additional charge. If the issue turns out to be an Oracle bug (not a client config issue), APPSolve logs an Oracle SR and manages resolution.  
**Note:** Systematic regression testing before each quarterly update to prevent regressions is NOT included in standard AMS — this must be separately contracted (see AMS-REL-003).

### "Why isn't this a defect? You configured it."
**Answer:** A defect means the system does not behave per the agreed configuration design documented during the implementation. If the client changed a requirement after the design was agreed (even verbally), the system is working as it was designed — and the new requirement is an enhancement. Always refer back to the Scope and Design document and the implementation test sign-off as the evidence of what was agreed.

### "We want our reports to be in the new company colour scheme."
**Answer:** Custom UI branding and report template reformatting are out of AMS scope. Standard Oracle and Acumatica report formatting applies. Custom branded report templates (company letterhead on invoices, branded FRS report headers) are a separately scoped design activity.

### "We need you to train our new finance team."
**Answer:** End-user training is excluded from AMS (AMS-EXC-006). APPSolve can provide quick reference cards and job aids for specific how-to queries within the monthly hours. Formal training delivery requires a separate training engagement.

---

## 8. Escalation Guide

When a boundary dispute arises:

| Scenario | First step | Second step |
|---|---|---|
| Client argues a request is in scope; APPSolve disagrees | Log the dispute; refer to AMS_ASSUMPTIONS_V1.md relevant assumption | AMS Account Manager reviews within 1 business day and provides written response |
| Request is ambiguous; cannot classify as IN/OUT | Escalate to AMS Account Manager with request description | AMS Account Manager and client designated contact agree classification within 2 business days |
| Client is dissatisfied with classification | AMS Account Manager responds formally in writing | If unresolved, escalate to Commercial Director for final determination |
| Change is operationally urgent (client system impacted) | Start investigation as if IN scope; classify in parallel | If classified as OUT of scope, provide cost estimate before completing the work |

---

*AMS_SCOPE_BOUNDARY_GUIDE v1.0 | WP11E — AMS / Managed Services Assumptions Pack | 2026-06-15*  
*Companion to AMS_ASSUMPTIONS_V1.md | Draft — validate against first two AMS agreements before promoting to Approved*  
*Questions: AMS Account Manager | Escalation: Commercial Director*
