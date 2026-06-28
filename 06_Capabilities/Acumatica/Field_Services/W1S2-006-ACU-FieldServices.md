---
document_id: W1S2-006-ACU-FieldServices
title: "Acumatica Field Services Capability Statement"
version: "1.2 APPROVED"
source_document: "APPSolve_Interconnect_Proposal V2.0.docx"
source_path: "Parties/Customers/Interconnect Systems/RFP/ERP Implementation/1. Working/APPSolve_Interconnect_Proposal V2.0.docx"
source_secondary: "Acumatica_Interconnect Outlay.docx; APPSolve_Interconnect_Proposal V1.0.docx"
source_secondary_path: "Parties/Customers/Interconnect Systems/RFP/ERP Implementation/1. Working/; Parties/Customers/Interconnect Systems/RFP/Additional Appointments/"
source_contract: "Annexure 1_Interconnect_Acumatica Implementation_V2.0.docx"
source_contract_path: "Parties/Customers/Interconnect Systems/0. Contract/Annexure 1_Interconnect_Acumatica Implementation_V2.0.docx"
extraction_date: "2026-06-12"
extracted_by: "Claude (AI extraction)"
review_date: "2026-06-12"
reviewed_by: "Hein Blignaut"
source_status: "Approved"
approved_for_reuse: "Yes"
approved_by: "Hein Blignaut"
approval_date: "2026-06-12"
business_unit: "Acumatica"
review_status: "Approved"
kb_destination: "06_Capabilities/Acumatica/Field_Services/"
wave: "Wave 1 (Acumatica)"
bu_lead_decisions_open: "None"
bu_lead_decisions_closed: "D-W6-001; D-W6-002; D-W6-003; Section 2 Target Industries; Source basis; Sections 3–10; Interconnect referenceability (confirmed 2026-06-12)"
---

> **APPROVED — approved_for_reuse: Yes — Approved by Hein Blignaut, 2026-06-12**
> Version: 1.2 APPROVED | Extraction: 2026-06-12 | Review: 2026-06-12 | Approval: 2026-06-12
> Source: Interconnect Systems — Proposal V2.0 §3.9 (primary); Outlay.docx (corroborating); Annexure 1 (contractual); Proposal V1.0 (live-use confirmation)
> Interconnect Systems is referenceable for Acumatica Field Services — approved by Hein Blignaut 2026-06-12
> Superseded: `07_Approved_Content/Review_Required/Acumatica/W1S2-006-ACU-FieldServices.md`

---

# Acumatica Field Services Capability Statement

## Section 1 — Overview

APPSolve implements and supports the Acumatica Field Services Edition as part of its Acumatica Gold Partner delivery practice. The module connects field service operations directly with the Acumatica ERP back-office — enabling a single, integrated view of customer activities, service orders, technician resources, inventory, and financials across all operations.

The Acumatica Field Services Edition is designed for businesses that manage a workforce of field technicians who respond to customer service requests, perform on-site maintenance or repairs, and require real-time coordination between the office and the field. Acumatica integrates Field Services with CRM, sales, inventory, purchasing, accounting, and financial reporting — eliminating the disconnect between field operations and financial management.

APPSolve's Field Services implementation capability covers the full module scope: service order and work order management, technician scheduling and dispatch, mobile technician enablement, equipment and service history management, inventory and parts management, billing and financial integration, and CRM and customer service integration.

---

## Section 2 — Target Industries

> **Note:** This section contains one confirmed-client industry and two industries derived from Field Services operating requirements. Derived industries are clearly labelled. Pre-tender check PT-W6-001 applies: derived industry wording must remain limited and non-client-specific.

The Acumatica Field Services Edition is suited to businesses where field technicians are deployed to customer sites to deliver, install, service, repair, or maintain products and equipment.

**Technology products and systems distribution** *(confirmed — client implementation evidence)* — Companies that distribute and support technology systems, hardware, and equipment use Field Services to manage post-sale installation, maintenance, and support appointments. Service teams dispatch technicians to customer sites, track work orders against product records, and manage service contracts alongside sales and distribution operations.

**Service and maintenance contractors** *(derived — Field Services operating requirements)* — Businesses operating technician teams for recurring maintenance, repair, and inspection services use Field Services to schedule appointments, track equipment and asset history against customer records, manage parts and inventory in transit vehicles, and generate invoices directly from field completion.

**Equipment installation and commissioning** *(derived — Field Services operating requirements)* — Organisations managing multi-phase project-based installations alongside scheduled service appointments use Acumatica Field Services integrated with Project Accounting for unified project and service order billing.

---

## Section 3 — Field Service Operating Model

APPSolve configures the Acumatica Field Services module to support an end-to-end field service workflow: from service contract and order creation through technician assignment, field execution, and financial close.

**Service contract management.** APPSolve sets up Acumatica to manage contracts across sale, service, recurring maintenance, and repair scenarios. Service contracts define billing procedures and drive automated service order generation at configurable frequencies. Contract renewals are streamlined through built-in renewal workflows.

**Order creation and assignment.** Service orders are created from CRM cases, customer calls, or contract schedules. Orders are assigned to technicians through the Calendar Board, which provides a visual, drag-and-drop scheduling interface. Appointment templates accelerate order creation by defaulting service types and materials.

**Dispatch and execution.** Once assigned, technicians receive appointment details on their mobile device. They can access customer history, equipment records, and required materials before arriving on site. Progress updates, materials used, and field notes are captured in real time and are immediately visible in the back-office system.

**Financial close.** On appointment completion, invoices are generated based on actuals or estimations, in line with the billing rules configured per customer and service order type. All field costs — labour time, parts, and expenses — are reconciled against the service order and integrated with Acumatica Accounts Receivable and Accounts Payable.

APPSolve implements this operating model in accordance with its six-phase Acumatica implementation methodology: Mobilise → Analyse and Prepare → Plan and Design → Configure and Build → Validate and Test → Transition and Go-Live.

---

## Section 4 — Work Order and Scheduling Management

Effective technician scheduling and work order management are the operational core of the Acumatica Field Services Edition. APPSolve configures the scheduling engine, work order workflows, and calendar board for each client's operational model.

**Service contract and order generation.** Acumatica manages service contracts for sale, service, recurring maintenance, and repair scenarios. Billing procedures are defined on the contract and service orders are generated automatically at the configured frequency, reducing manual order entry.

**Appointment scheduling by availability, skill, and location.** Technicians are scheduled based on their availability, geographic location, skill qualifications, active licences, and designated service areas. Scheduling by these criteria reduces unnecessary travel, prevents unqualified technician assignments, and maximises appointment throughput.

**Calendar Board.** The Calendar Board provides a visual scheduling interface where appointments are created and assigned via drag-and-drop. Schedulers can view resource availability by day, week, or month and apply filters based on appointment requirements. Unscheduled service orders are visible alongside the calendar for efficient queue management.

**Appointment lifecycle management.** Appointments are managed from creation through completion. Technicians start and end appointments from the field, providing real-time status updates to the back-office. Multi-day appointments are supported, as are mid-appointment pauses for travel or break time.

**Resource scheduling by workload, location, and certification.** Resource scheduling ensures that the right technician is matched to the right appointment — considering current workload, proximity to the customer site, and any required certifications or specialisations. The system ensures technicians have the required equipment and inventory before departing.

**Route and GPS tracking.** Estimated routes and route statistics are visible per technician. Actual route history and real-time GPS location are tracked, providing office schedulers with visibility of field resource movements throughout the working day.

| Capability | Description |
|---|---|
| Service Contract Management | Manage sale, service, maintenance, and repair contracts; define billing procedures; auto-generate service orders at configurable frequencies |
| Calendar Board | Visual drag-and-drop scheduling; day/week/month view; filter by appointment requirements |
| Appointment Lifecycle | Create, assign, start, pause, and complete; single or multi-day; real-time status updates |
| Schedule by Availability | Technician scheduling by availability, location, skills, licences, and service areas |
| Resource Scheduling | Assign by workload, location, skill, and certification |
| Route Tracking | Visualise estimated route and statistics; track actual GPS route history |
| Route Optimisation | WorkWave Routing Engine integration — optional third-party add-on; confirm availability before including in tender scope (PT-W6-003) |

---

## Section 5 — Mobile / Technician Enablement

APPSolve implements the Acumatica Field Services mobile application as part of every Field Services deployment. The mobile application gives field technicians full access to their appointment schedule, customer history, equipment records, and field capture tools — without returning to the office.

**Mobile application (Android and iOS).** The Acumatica Field Services mobile app is available on both Android and iOS devices. Technicians use the app to manage their daily appointment schedule and capture all field activity from their mobile device.

**Appointment access and status management.** Technicians access their scheduled appointments from the mobile app, including appointment details, customer information, service history, and equipment records. They start and end appointments directly from the app, with status updates immediately visible to the back-office scheduler.

**GPS navigation.** The mobile app provides GPS navigation to the customer's location and supports real-time GPS location tracking. Office schedulers can monitor technician locations and actual route history.

**Field capture capabilities.**

| Capture type | Capability |
|---|---|
| Electronic signatures | Capture customer acceptance signatures on job completion |
| Credit card payments | Accept and process customer payments in the field |
| Expense receipts | Capture mobile expense receipts directly against the appointment |
| Voice dictation | Dictate field notes using voice-to-text |
| Image uploads | Upload photos and documents from the field against the appointment |

**Service history and equipment access.** Field technicians can view full service history and equipment information for the customer's assets from the mobile app before and during the appointment. This eliminates the need for technicians to call the office for background information.

**Real-time back-office synchronisation.** Status updates, materials used, and field notes captured on the mobile app are synchronised in real time with the Acumatica back-office, providing management with live visibility of appointment progress.

---

## Section 6 — Equipment, Asset and Service History

Acumatica Field Services maintains equipment and asset records linked to customer accounts, providing technicians and service managers with a complete history of service activity against each item in the field.

**Equipment records.** Customer equipment and assets are registered in Acumatica with user-configurable fields that capture the attributes relevant to each client's industry and service model — product type, serial number, installation date, and any other data points required for effective service management.

**Service history by equipment.** Every service appointment, work order, and repair event is recorded against the equipment record. Field technicians access this history on the mobile app before and during an appointment, enabling them to review prior service actions, recurring fault patterns, and previously used parts before arriving on site.

**Warranty management.** APPSolve configures warranty tracking within Acumatica to manage multidimensional service contracts — where different warranty periods apply to different components of the same system. Warranty terms are defined at the point of sale and are tracked through every field repair interaction. At service time, technicians and billing staff can identify which parts and labour are covered under warranty, preventing incorrect billing and protecting the client's customer relationships.

**User-defined fields.** Service contract and equipment forms support user-defined fields, allowing each client implementation to capture the specific attributes that matter for their field service operation — without requiring development.

**Integration with Fixed Assets.** Where clients also use the Acumatica Fixed Assets module, the equipment record is separate from the fixed asset register. Fixed Assets manages depreciation and accounting lifecycle; Field Services equipment records manage service history and maintenance tracking. APPSolve configures the relationship between these records as part of implementation scoping.

---

## Section 7 — Inventory, Parts and Procurement Integration

Parts and inventory availability is a critical dependency for effective field service delivery. Acumatica Field Services integrates with the Acumatica Inventory and Distribution modules to give technicians and office staff a unified view of parts in warehouses and in transit vehicles.

**Inventory visibility across warehouses and mobile vehicles.** Acumatica tracks inventory quantities and locations across fixed warehouses and mobile vehicle stock — enabling accurate parts availability checks at the time of appointment scheduling. Technicians can see the parts assigned to their vehicle and confirm availability before departure.

**Parts allocation to service orders.** Parts are allocated to service orders within Acumatica, linking inventory movements to specific customer appointments. This provides accurate costing at the order level and ensures that stock movements are reflected in the inventory system as parts are consumed in the field.

**Purchase orders from the field.** When a required part is not available in vehicle stock, technicians can initiate a purchase order from the field through the mobile application. Purchase orders created in the field flow directly into the Acumatica Procurement module for processing.

**Inventory replenishment.** Acumatica's inventory replenishment logic applies to field service vehicle stock. Replenishment orders are generated automatically when mobile vehicle inventory falls below defined thresholds, ensuring technicians are stocked for upcoming appointments without manual stock monitoring.

**AP Bill linkage to appointments.** Accounts Payable bills from suppliers are linked directly to the relevant field service appointments in Acumatica. This provides holistic expense management by appointment — giving service managers a complete view of the cost of each appointment, including parts, external services, and labour.

| Capability | Description |
|---|---|
| Inventory tracking | Track parts in warehouses and mobile vehicle stock |
| Parts allocation | Allocate stock items to service orders; consume inventory on completion |
| Field POs | Create purchase orders from the field via mobile app |
| Replenishment | Automated replenishment of mobile vehicle stock |
| AP Bill linkage | Link AP bills to field service appointments for cost analysis by appointment |

---

## Section 8 — Billing and Financial Integration

Acumatica Field Services integrates directly with Acumatica Financials, enabling invoices to be generated from completed field work without manual re-entry. APPSolve configures billing rules, invoice grouping, and contract billing models to match each client's commercial terms.

**Flexible billing rules.** Invoices can be generated based on estimations or actuals. Billing rules are configured by customer and by service order type — allowing different commercial models to operate within the same system. Supported billing models include:

- Fixed-rate billing: invoice at a set amount per period, regardless of actuals
- Time and material billing: invoice based on actual time and parts consumed
- Start-of-period contract billing: invoice in advance at the start of each contract period

**Invoice grouping.** Invoices are grouped by service order, billing period, or customer purchase order — matching the client's invoicing preferences and customer requirements.

**Project-integrated billing.** For multi-phase project engagements that include service appointments, billing can be routed through the Acumatica Project Accounting module. Project billing supports fixed-price, cost-plus, and capped project cost models. This allows a single client to have both scheduled service appointments and project-based work billed through a unified project record.

**Time capture for downstream integration.** Technician time entries captured against appointments are available for downstream integration with payroll systems. This is a time tracking capability — time entries feed into the client's payroll processing system; Acumatica Field Services does not perform payroll calculations.

**AP bill linkage.** Supplier bills related to field service appointments — including parts, specialist subcontractors, and other direct costs — are linked to the appointment record in Acumatica. This enables margin analysis by appointment and ensures all costs are captured before invoicing.

**Contract renewals.** Service contract renewal workflows are built into Acumatica, reducing the manual effort required to renew recurring maintenance contracts and ensuring billing continuity.

---

## Section 9 — CRM / Customer Service Integration

Acumatica Field Services operates as a native extension of the Acumatica CRM module, providing a unified view of customer sales history, support cases, service orders, and appointment activity in one system.

**CRM integration.** Field Services is fully integrated with Acumatica CRM. Service management staff and field technicians have access to the customer's complete activity history — including sales history, open and closed support cases, and prior appointment records — from the same interface used for service management.

**Opportunity to service order conversion.** CRM sales opportunities can be converted directly into service orders. This enables a smooth handover from the sales team to the service team, with all opportunity details — customer, product, scope, and pricing — carried forward into the service order without re-entry.

**Case to appointment workflow.** Customer support cases logged in CRM can be converted into service appointments. This closes the loop between customer complaint management and field service dispatch, ensuring no case is lost between CRM and the service scheduler.

**Customer portal.** Customers have access to a self-service portal where they can view invoices, service history, and appointment status online. This reduces incoming call volume and gives customers real-time visibility of their service account.

**Unified customer record.** All interactions — sales, support, and service — are visible on the single customer record in Acumatica. Service managers can see the full customer relationship context when managing service accounts, and sales staff can see outstanding service issues when engaging with customers.

| Capability | Description |
|---|---|
| CRM integration | Access sales history, support cases, and activity history from Field Services |
| Opportunity conversion | Convert CRM opportunities into service orders directly |
| Case to appointment | Create service appointments from CRM support cases |
| Customer portal | Customer self-service access to invoices, history, and appointment status |
| Unified customer record | Single customer view across sales, support, and field service |

---

## Section 10 — Benefits

APPSolve's clients that implement Acumatica Field Services gain the following business outcomes:

**Expedite assignments.** Service needs are captured quickly and matched to the right technician using customer information, product history, and available resources. Appointment templates default service types and materials at creation, reducing setup time. The time between call receipt and appointment assignment is measurably reduced through workflow automation and the visual Calendar Board.

**Gain control of remote field service activities.** Management has real-time visibility of all field commitments through GPS location tracking, appointment status updates, and live progress reporting. Materials used, field notes, and images are captured in the field and immediately visible in the back-office system — eliminating the daily lag between field activity and office awareness.

**Improve communications.** Technicians and customers are notified of appointment assignments, modifications, and confirmations through automated email, SMS, or push notification. Customers are kept informed without manual intervention from the service desk.

**Accelerate decision-making.** Drilldown reports and dashboards provide service managers with access to historical data and forward-looking insights. Key performance metrics — including technician utilisation, appointment throughput, first-time fix rates, and service performance by region — are defined and tracked within the Acumatica reporting environment.

**Integrated financial management.** Because Field Services is native to Acumatica ERP, billing, inventory, purchasing, and payroll time data are all managed in the same system. There is no interface between a standalone FSM product and a separate ERP — all field costs and revenues are reflected in the general ledger in real time.

---

## Section 11 — Source Mapping / Assumptions / Risk Register

### 11.1 Source Mapping

| Section | Primary source | Paragraphs / location | Confidence |
|---|---|---|---|
| 1. Overview | Interconnect Proposal V2.0 §3.9 | Paras 714–718 | High |
| 2. Target Industries | V1.0 para 336 (distribution confirmed); V2.0 general context (derived) | Para 336 + scope context | Medium — limited; PT-W6-001 applies |
| 3. Field Service Operating Model | Proposal V2.0 §3.9 + §4 | Paras 719, 734, 741, 743 | High |
| 4. Work Order and Scheduling | Proposal V2.0 §3.9 | Paras 720, 741–745, 749, 751 | High |
| 5. Mobile / Technician Enablement | Proposal V2.0 §3.9 | Paras 721, 752–753 | High |
| 6. Equipment, Asset and Service History | Proposal V2.0 §3.9 | Paras 721, 756–757, 767 | High |
| 7. Inventory, Parts and Procurement | Proposal V2.0 §3.9 | Paras 721, 759, 761 | High |
| 8. Billing and Financial Integration | Proposal V2.0 §3.9 | Paras 746–747, 759–761 | High |
| 9. CRM / Customer Service Integration | Proposal V2.0 §3.9 | Paras 723, 758–759 | High |
| 10. Benefits | Proposal V2.0 §3.9 | Paras 729–732 | High |

**Corroborating source:** `Acumatica_Interconnect Outlay.docx` paragraphs 393–446 — all Field Services content confirmed independently.

**Live-use confirmation:** `APPSolve_Interconnect_Proposal V1.0.docx` (May 2024) para 62: *"Interconnect requires the implementation of an Additional Appointment extension to the Field Services Application already installed."*

**Contractual evidence:** `Annexure 1_Interconnect_Acumatica Implementation_V2.0.docx` para 228: *"Field Service Management, up to 1,000 appointments / month"* — R35,059.20/month, signed contractual line item.

---

### 11.2 Assumptions

| Assumption ID | Assumption | Basis | Status |
|---|---|---|---|
| A-W6-001 | Field Services was fully implemented and is live in production at the source client | Implementation completed 2023-07-31; V1.0 May 2024 confirms "already installed"; active support through May 2027; upgrade 25R1→25R2 April 2026 includes Field Services UAT | Confirmed |
| A-W6-002 | The source client is a technology products and distribution company | V1.0 para 336 ("long standing Distribution clients"); Advanced Distribution Edition is the licensed base product | Confirmed |
| A-W6-003 | Capabilities reflect standard Acumatica Field Services Edition, not a bespoke build | Feature set matches standard Acumatica Field Services product SKU | Confirmed |
| A-W6-004 | Appointment throughput (1,000 appointments/month) is a licensing capacity parameter | Acumatica licensing tier; actual throughput is client-operational-volume dependent | Confirmed |

---

### 11.3 Factual Risk Register

| Risk ID | Risk | Severity | Status |
|---|---|---|---|
| R-W6-001 | Source text is Acumatica product marketing copy | Medium | **Mitigated** — all content reframed as APPSolve implementation capability |
| R-W6-002 | Source client named in tender-facing content | High | **Mitigated** — client not named in sections 1–10; Interconnect referenceable per BU decision 2026-06-12 |
| R-W6-003 | WorkWave Routing Engine presented as standard Field Services | Low | **Mitigated** — flagged as optional third-party in §4; PT-W6-003 preserved |
| R-W6-004 | Section 2 limited source coverage | Medium | **Mitigated** — BU Lead confirmed limited wording acceptable 2026-06-12; derived industries labelled |
| R-W6-005 | Time capture read as payroll processing | Low | **Mitigated** — §8 explicitly states time tracking only; not payroll processing |
| R-W6-006 | Fixed Assets conflated with Field Services equipment | Low | **Mitigated** — §6 explicitly differentiates the two modules |

---

## Section 17 — Approval Record and Pre-Tender Checks

### 17.1 Approval Record

| Item | Detail |
|---|---|
| **Approved by** | Hein Blignaut |
| **Approval date** | 2026-06-12 |
| **approved_for_reuse** | Yes |
| **Extraction source** | Interconnect Systems — Proposal V2.0 §3.9; Outlay.docx; Annexure 1; Proposal V1.0 |
| **Pipeline path** | Candidate (2026-06-12) → Review_Required (2026-06-12) → Approved (2026-06-12) |
| **Interconnect referenceability** | **Approved** — Interconnect Systems is referenceable for Acumatica Field Services. Approved by Hein Blignaut 2026-06-12. Confirm contact and reference details before citing in a specific tender (PT-W6-002). |

**BU Lead decisions closed at approval:**

| Decision | Outcome |
|---|---|
| D-W6-001 — APPSolve Field Services capability | CONFIRMED |
| D-W6-002 — Interconnect as sufficient primary source | CONFIRMED |
| D-W6-003 — Partner portal brochure required | NOT NEEDED |
| Section 2 — Target Industries limited wording acceptable | CONFIRMED |
| Sections 3–10 — Factual content | CONFIRMED — no corrections |
| Interconnect Systems referenceability | **CONFIRMED — referenceable** |

---

### 17.2 Pre-Tender Checks

Apply the following checks before using this document in any tender response:

| Check ID | Item | Requirement |
|---|---|---|
| **PT-W6-001** | Target Industries — derived industry wording | Before citing W1S2-006 for an industry not listed in Section 2, obtain BU confirmation. Do not expand the industry list without a sourced client reference or explicit BU approval. |
| **PT-W6-002** | Interconnect Systems as reference client | **Interconnect Systems is approved as a referenceable Field Services client (Hein Blignaut, 2026-06-12).** Before naming Interconnect in a specific tender response, confirm current contact name, title, and contact details are correct. Do not include named reference contact information without verifying it is up to date. |
| **PT-W6-003** | WorkWave Routing Engine availability | WorkWave is an optional third-party integration. Before including route optimisation in any tender scope, confirm APPSolve can supply this capability to the specific client. |
| **PT-W6-004** | Acumatica Gold Partner status | Confirm Acumatica Gold Partner status is current at the time of each tender submission. |

---

## Appendix A — Extraction Notes

- **Extraction date:** 2026-06-12 | **Extracted by:** Claude (AI) — Sonnet 4.6
- **Reviewed and approved:** 2026-06-12 by Hein Blignaut
- **Pipeline:** Candidate → Review_Required → Approved — all stages completed 2026-06-12
- **Primary source:** `APPSolve_Interconnect_Proposal V2.0.docx` §3.9 (paras 714–767)
- **Corroborating source:** `Acumatica_Interconnect Outlay.docx` (paras 393–446)
- **Live-use confirmation:** `APPSolve_Interconnect_Proposal V1.0.docx` (May 2024) — Field Services already installed; appointment capacity extension
- **Contractual evidence:** Annexure 1 — "Field Service Management, up to 1,000 appointments / month"
- **KB destination:** `06_Capabilities/Acumatica/Field_Services/`

---

## Appendix B — Governance Self-Review

| Check | Result |
|---|---|
| All capability claims traceable to source paragraphs | PASS |
| No client names in sections 1–10 | PASS |
| No unsupported project-count or country-count claims | PASS |
| WorkWave flagged as optional third-party | PASS |
| Payroll governance: time capture as time tracking only | PASS |
| Section 2 derived industries clearly labelled | PASS |
| PT-W6-001 through PT-W6-004 current and accurate | PASS |
| PT-W6-002 updated: Interconnect referenceable per BU approval 2026-06-12 | PASS |
| Approved_for_reuse: Yes — set by BU Lead | PASS |
| Section 17 approval record complete | PASS |

---

*Approved by: Hein Blignaut | Approval date: 2026-06-12 | Acumatica Wave 1 Field Services Deliverable — approved_for_reuse: Yes*
