---
created: "2026-06-10"
created_by: "Claude (AI — consolidation planning)"
status: "Draft — awaiting BU lead review before execution"
---

# Approved Content Placement Plan
**Date:** 2026-06-10 | **Purpose:** Map all 25 approved assets from staging (`07_Approved_Content/Approved/`) to their final KB destination folders

Do not move files until this plan is reviewed and approved by Hein Blignaut.

---

## Important: Actual Folder Structure

The actual KB folder numbering differs from the reference in `AI_CONTEXT.md`. The filesystem structure is:

```
00_Governance/
01_Compliance/         ← BEE, CIPC, Tax, Insurance, etc.
02_Corporate/          ← Company_Profile, Company_Info, Org_Chart, Bank_Letters
03_People/             ← Consultant Index Records, CVs (APPTime-sourced)
04_References/         ← Oracle, Acumatica, BeBanking, Managed_Services
05_Methodologies/      ← Implementation, Support, Managed_Services, Project_Management, etc.
06_Capabilities/       ← Oracle, Acumatica, BeBanking (with subfolders)
07_Approved_Content/   ← PIPELINE STAGING — not a final destination
08_Historical_Tenders/ ← Submitted tenders (read-only reference)
09_Active_Tenders/     ← Current RFP responses
...
99_Archive/
```

**AI_CONTEXT.md references `08_Methodologies/` and `09_Executive_Summaries/` — these folders do not exist.** The correct methodologies folder is `05_Methodologies/`. There is no Executive_Summaries folder; this should be created under `02_Corporate/` or as a new top-level folder when Wave 2 executive summary files are produced.

**Action required:** Update `AI_CONTEXT.md` Repository Structure Reference section to reflect the actual folder numbering.

---

## Placement Map — All 25 Approved Files

### Destination Key

| Code | Folder | Purpose |
|---|---|---|
| CORP | `02_Corporate/Company_Profile/` | Company overview, history, geographic profile, awards |
| CORP-INFO | `02_Corporate/Company_Info/` | Awards, recognition, general corporate info |
| CAP-ORA | `06_Capabilities/Oracle/Oracle_ERP/` | Oracle partnership and general Oracle capability |
| CAP-ACU-ERP | `06_Capabilities/Acumatica/ERP/` | Acumatica core modules and partnership |
| CAP-ACU-DIST | `06_Capabilities/Acumatica/Distribution/` | Distribution and Inventory modules |
| CAP-ACU-MFG | `06_Capabilities/Acumatica/Manufacturing/` | Manufacturing module |
| CAP-BB-OVW | `06_Capabilities/BeBanking/Product_Overview/` | BeBanking product overview |
| CAP-BB-BNK | `06_Capabilities/BeBanking/Banking/` | H2H banking, monitoring/automation |
| CAP-BB-SUP | `06_Capabilities/BeBanking/Supplier_Payments/` | Supplier payments |
| CAP-BB-PAY | `06_Capabilities/BeBanking/Payroll/` | Payroll payments |
| CAP-BB-FX | `06_Capabilities/BeBanking/Forex/` | International and forex payments |
| CAP-BB-INT | `06_Capabilities/BeBanking/Integrations/` | ERP integration detail |
| CAP-BB-SEC | `06_Capabilities/BeBanking/Security/` | Security |
| CAP-BB-ARC | `06_Capabilities/BeBanking/Architecture/` | Architecture |
| CAP-BB-HST | `06_Capabilities/BeBanking/OCI_Hosting/` | Hosting model |
| METH | `05_Methodologies/` | Delivery model (see note) |

---

### Cross-BU / Company Profile Files (W1S1)

| # | File | Content | Destination | Subfolder note | Priority |
|---|---|---|---|---|---|
| 1 | W1S1-001-CORP-CompanyOverview.md | Company introduction, 23-year history, 50+ consultants, industries | `02_Corporate/Company_Profile/` | Directly in folder — usable in any tender | **High** |
| 2 | W1S1-002-CORP-CompanyHistory.md | Founder background, Oracle history, geographic expansion, awards | `02_Corporate/Company_Profile/` | Companion to W1S1-001 | High |
| 3 | W1S1-003-ORA-OraclePartnership.md | Oracle Level 1 Partner, 5 expertise areas, VAR, 6 awards | `06_Capabilities/Oracle/Oracle_ERP/` | Oracle partnership statement; supplements Oracle capability files | **High** |
| 4 | W1S1-004-ACU-AcumaticaPartnership.md | Acumatica Gold Partner, VAR, 5 industries | `06_Capabilities/Acumatica/ERP/` | Acumatica partnership statement; supplements module capability files | **High** |
| 5 | W1S1-005-BB-BeBankingOverview.md | BeBanking product, 7 capabilities, ERP compatibility | `06_Capabilities/BeBanking/Product_Overview/` | Highest-use BeBanking intro document | **High** |
| 6 | W1S1-006-CORP-AwardsRecognition.md | 6 Oracle awards 2015–2024; success stories (URL verification pending) | `02_Corporate/Company_Info/` | — | Medium |
| 7 | W1S1-007-CORP-DeliveryModel.md | 8 service lines, MRI Model, DBA team, senior-only delivery | `05_Methodologies/` | ⚠️ No direct subfolder match — recommend creating `05_Methodologies/Delivery_Model/` or place directly in root of `05_Methodologies/` | High |
| 8 | W1S1-008-CORP-GeographicPresence.md | Sub-Saharan Africa (5 markets), international (4 countries) | `02_Corporate/Company_Profile/` | — | High |
| 9 | W1S1-009-CORP-KeyDifferentiators.md | 7 differentiators, Hybrid Support Model, CIM, 3 costing models | `02_Corporate/Company_Profile/` | Cross-BU; useful in all tenders alongside overview | High |

### Acumatica Module Files (W1S2)

| # | File | Content | Destination | Subfolder note | Priority |
|---|---|---|---|---|---|
| 10 | W1S2-001-ACU-Financials.md | GL, AR, AP, Cash, Multi-Currency, Tax, IFRS 15, Fixed Assets — 10 rows | `06_Capabilities/Acumatica/ERP/` | Core financials; highest-use Acumatica file | **High** |
| 11 | W1S2-002-ACU-Distribution.md | Order Management, Procurement, Sales, Financial Integration — 4 rows | `06_Capabilities/Acumatica/Distribution/` | — | High |
| 12 | W1S2-003-ACU-Inventory.md | FIFO/WAC/Standard costing, Lot/Serial Tracking, Multi-Location — 7 rows | `06_Capabilities/Acumatica/Distribution/` | Inventory is logically paired with Distribution | High |
| 13 | W1S2-004-ACU-Manufacturing.md | Manufacturing Platform 9 rows + MRP + Estimating + ECC — sole KB source | `06_Capabilities/Acumatica/Manufacturing/` | — | High |
| 14 | W1S2-005-ACU-CRM.md | Contact/Account, Sales Pipeline, Quote, Case, Portal, Outlook — 8 rows | `06_Capabilities/Acumatica/ERP/` | ⚠️ No CRM subfolder exists — place in ERP/ or create `06_Capabilities/Acumatica/CRM/` | Medium |
| 15 | W1S2-009-ACU-ProjectAccounting.md | Budget, WIP, Revenue Recognition, Billing, Change Orders, Mfg Integration — 8 rows | `06_Capabilities/Acumatica/ERP/` | ⚠️ No Project Accounting subfolder — place in ERP/ or create `06_Capabilities/Acumatica/Project_Accounting/` | Medium |

### BeBanking H2H Capability Files (W1S3)

| # | File | Content | Destination | Priority |
|---|---|---|---|---|
| 16 | W1S3-001-BB-ProductOverview.md | 9-module portfolio, ERP compatibility, geographic deployment | `06_Capabilities/BeBanking/Product_Overview/` | **High** |
| 17 | W1S3-002-BB-HostToHostBanking.md | H2H process 6 steps, 9-bank list, configurable approval, API-first | `06_Capabilities/BeBanking/Banking/` | **High** |
| 18 | W1S3-003-BB-SupplierPayments.md | Bank Account Approval, AVS, H2H Payments, PDF Remittances | `06_Capabilities/BeBanking/Supplier_Payments/` | **High** |
| 19 | W1S3-004-BB-PayrollPayments.md | Payroll H2H, ACB file, Oracle EBS and Fusion only | `06_Capabilities/BeBanking/Payroll/` | **High** |
| 20 | W1S3-005-BB-InternationalAndForexPayments.md | Module 9: AP-initiated SWIFT, CMA + UK + Chile, module 6 separate | `06_Capabilities/BeBanking/Forex/` | **High** |
| 21 | W1S3-006-BB-ERPIntegration.md | Oracle EBS/Fusion, Acumatica, SAP integration tables | `06_Capabilities/BeBanking/Integrations/` | High |
| 22 | W1S3-007-BB-Security.md | POPIA, GDPR roadmap, API/TLS, access control | `06_Capabilities/BeBanking/Security/` | High |
| 23 | W1S3-008-BB-Architecture.md | API-first diagram, component architecture, deployment | `06_Capabilities/BeBanking/Architecture/` | Medium |
| 24 | W1S3-009-BB-HostingModel.md | On-premises + cloud, subscription-only, support model | `06_Capabilities/BeBanking/OCI_Hosting/` | Medium |
| 25 | W1S3-010-BB-MonitoringAutomation.md | 5 automated processes, bank statements, exchange rate automation | `06_Capabilities/BeBanking/Banking/` | Medium |

---

## Empty Destination Folders (will remain empty after this copy)

All `06_Capabilities` subfolders without a planned file assignment:

| Folder | Status | Comment |
|---|---|---|
| `06_Capabilities/Acumatica/Integration/` | Empty — no Wave 1 content | Will receive content after BeBanking/Acumatica integration detail is documented (future wave) |
| `06_Capabilities/Acumatica/Managed_Services/` | Empty — no Wave 1 content | Will receive content after managed services methodology is extracted |
| `06_Capabilities/Acumatica/Payroll/` | Empty — no Wave 1 content | Will receive content if W1S2-007 is advanced as Acumatica Payroll Integration |
| `06_Capabilities/BeBanking/Client_References/` | Empty — no Wave 1 content | Will receive content when BeBanking reference letters are obtained |
| `06_Capabilities/Oracle/Oracle_APEX/` | Empty — no Wave 1 content | Wave 3+ extraction |
| `06_Capabilities/Oracle/Oracle_DR/` | Empty — no Wave 1 content | Wave 3+ extraction |
| `06_Capabilities/Oracle/Oracle_Database/` | Empty — no Wave 1 content | Wave 3+ extraction |
| `06_Capabilities/Oracle/Oracle_EBS/` | Empty — Wave 2 target | Will receive Oracle EBS capability statement (TMPL-002 extraction) |
| `06_Capabilities/Oracle/Oracle_HCM/` | Empty — no Wave 1 content | Wave 3+ extraction |
| `06_Capabilities/Oracle/Oracle_Managed_Services/` | Empty — no Wave 1 content | Wave 2/3 extraction (DBA managed services) |
| `06_Capabilities/Oracle/Oracle_OCI/` | Empty — no Wave 1 content | Wave 3+ extraction |
| `06_Capabilities/Oracle/Oracle_OIC/` | Empty — no Wave 1 content | Wave 3+ extraction |
| `06_Capabilities/Oracle/Oracle_Security/` | Empty — no Wave 1 content | Wave 3+ extraction |

Note: `06_Capabilities/Oracle/Oracle_ERP/` will receive W1S1-003 (Oracle Partnership) as the first Oracle capability file.

---

## Missing Folders — Need to be Created

| Missing folder | Purpose | When needed |
|---|---|---|
| `05_Methodologies/Delivery_Model/` | For W1S1-007 Delivery Model | Before copying W1S1-007 |
| `06_Capabilities/Acumatica/CRM/` *(optional)* | For W1S2-005 CRM | Could place in ERP/ instead — BU lead preference |
| `06_Capabilities/Acumatica/Project_Accounting/` *(optional)* | For W1S2-009 Project Accounting | Could place in ERP/ instead — BU lead preference |
| Executive Summaries folder | For Wave 2 Oracle DBA Executive Summary | Before Wave 2 copy — suggest `02_Corporate/Executive_Summaries/` |

---

## Copy Sequence Recommendation

Copy in this order to validate the process before committing to all 25 files:

**Batch 1 — High confidence, clear destinations (10 files)**
W1S3-001, W1S3-002, W1S3-003, W1S3-004, W1S3-005, W1S3-006, W1S3-007 (BeBanking — perfect folder match)
W1S1-001, W1S1-002, W1S1-008 (Corporate profile)

**Batch 2 — Clear destinations, BU-specific (8 files)**
W1S1-003 (Oracle ERP), W1S1-004 (Acumatica ERP), W1S1-005 (BeBanking overview), W1S1-006, W1S1-009
W1S2-001 (Acumatica Financials), W1S2-002 (Distribution), W1S2-004 (Manufacturing)

**Batch 3 — Create missing subfolders first (5 files)**
W1S1-007 (needs Delivery_Model subfolder), W1S3-008, W1S3-009, W1S3-010
W1S2-003 (Inventory → Distribution folder)

**Batch 4 — BU lead preference on subfolder (2 files)**
W1S2-005 (CRM — ERP/ or new CRM/)
W1S2-009 (Project Accounting — ERP/ or new Project_Accounting/)

---

## Dependencies

| Dependency | Required before | Notes |
|---|---|---|
| Create `05_Methodologies/Delivery_Model/` | Copying W1S1-007 | Simple mkdir |
| BU lead decision on CRM and Project Accounting subfolder | Copying W1S2-005, W1S2-009 | Low-stakes; ERP/ is acceptable default if no preference |
| Executive Summaries folder decision | Wave 2 copy | Decide folder structure before Oracle DBA Executive Summary is produced |

---

## Notes on Copying Approach

- **Copy, do not move.** Files in `07_Approved_Content/Approved/` are the master pipeline copies. The destination folders receive copies for operational use. Both locations should exist post-copy.
- Files are Markdown (`.md`) — no conversion needed.
- The `approved_for_reuse: Yes` metadata in each file is the authority for use; destination folder is for retrieval and organisation.
- After copying, update `EXTRACTION_LOG.csv` `kb_path` column for each file with the final destination path.

---

*Prepared 2026-06-10 by Claude (AI) on instruction from Hein Blignaut. Review and approve before executing any file copies.*
