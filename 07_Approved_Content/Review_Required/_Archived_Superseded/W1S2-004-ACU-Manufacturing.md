---
source_document: "APPSolve_HyDac_Proposal_20241211_V5.1.docx"
source_path: "Parties/Customers/HyDac/RFP/Acumatica Implementation/1. Working/APPSolve_HyDac_Proposal_20241211_V5.1.docx"
extraction_date: "2026-06-08"
extracted_by: "Claude (AI extraction — requires human review)"
readiness: "DIRECT"
approved_for_reuse: "No"
business_unit: "Acumatica"
review_status: "Review_Required"
remediation_date: "2026-06-10"
remediated_by: "Claude (AI — Session B Part 1)"
reviewer: "Hein Blignaut (pending)"
---

> **REVIEW REQUIRED — Pending BU lead approval. Not approved for tender use.**
> Readiness: DIRECT | Reviewer: Hein Blignaut

---

# Acumatica Manufacturing Edition

*Source: HyDac V5.1 (December 2024) — manufacturing-specific sections not present in Sept 2025 template.*

## Prime Manufacturing Edition — Overview

Acumatica Prime Manufacturing Edition is a comprehensive ERP solution designed specifically for manufacturing businesses. It offers a wide range of features to help manufacturers manage and streamline their operations, improve productivity, and enhance decision-making.

**Benefits:**
- **Scalability:** Supports businesses as they grow, from small manufacturers to large enterprises
- **Flexibility:** Customisable workflows and processes tailored to specific manufacturing needs
- **Cloud-Based:** Accessible from anywhere, with cloud-hosted services providing real-time data and collaboration
- **User-Friendly Interface:** Modern, intuitive design that simplifies navigation and use
- **Mobile Access:** Native mobile apps allow shop floor workers and management to access the system from tablets and smartphones

## Manufacturing Platform — Core Components

| Capability | Description |
|---|---|
| Advanced Inventory | Advanced warehouse and materials management for the manufacturing floor — multi-bin and multi-location tracking, directed put-away, barcode scanning support, and real-time visibility of materials and components across production. |
| Bill of Materials and Routing | Multi-level, dimensional, rules-based system with non-hierarchical feature selections and configuration evaluation on quotes, sales orders, and production orders with real-time price and cost rollup. |
| Production Management | Manage and monitor shop floor schedule and work centre capacity (finite and infinite). Includes what-if planning capability, capable-to-promise, and ability to schedule employee and/or machine resources. |
| Material Requirements Planning (MRP) | Demand-driven production planning calculating material and capacity requirements from sales orders, forecasts, and inventory levels. Generates automatic replenishment recommendations with supply and demand balancing across planning horizons. Exception-based alerts identify potential shortages before they impact production. |
| Estimating | Create cost estimates for new or existing items from materials, labour, and overhead. Convert estimates directly to bills of materials, production orders, or sales quotes. Maintain revision history and cost comparisons across estimate versions. |
| Order Management | Manage sales activities, streamline procurement processes, and automate order fulfilment for internal or external clients. |
| Advanced Planning and Scheduling | Meet customer demands by setting accurate and reliable delivery dates based on availability of resources. |
| Warehouse Management System (WMS) | Streamline distribution processes with advanced warehouse operations in receiving, inventory management, and order fulfilment. Barcode scanners and mobile devices supported. |
| Advanced Financials | Augment base financials with GL consolidation, sub-accounts, and automatic revenue recognition. |

## Manufacturing Foundation

Manufacturing Foundation provides the core manufacturing capabilities:

- BOM (Bill of Materials) and Routing management
- Production scheduling and control
- Shop floor management and monitoring
- Work centre capacity management (finite and infinite)
- Capable-to-promise and what-if planning

## Discrete Manufacturing

Discrete Manufacturing supports complex manufacturing processes:

- Production order management for discrete items
- Actual cost tracking against budget
- Scrap and rework management
- Quality hold and inspection integration
- Post-production cost roll-up

## Material Requirements Planning (MRP)

- Demand-driven production planning
- Automatic replenishment recommendations
- Supply and demand balancing across multiple planning horizons
- Integration with sales orders, production orders, and purchase orders
- Exception-based planning alerts

## Estimating

- Estimate creation from scratch or from existing items/BOMs
- Conversion of estimates to production orders, sales quotes, or BOMs
- Cost rollup for materials, labour, and overhead
- Revision history and comparison

## Engineering Change Control (ECC)

- Formal engineering change request and approval workflow
- Engineering Change Order (ECO) management with full approvals
- Engineering Change Notice (ECN) tracking
- Impact analysis before changes are committed
- Full audit trail from request to implementation

---

**Remediation notes (2026-06-10 — Session B Part 1):** Three table row descriptions in the Manufacturing Platform — Core Components table were corrected. The DRAFT contained a cascade content mismatch where descriptions had shifted one row out of position:

- **Advanced Inventory row:** Original description was Estimating content (*"Create estimates for new or existing items and convert them into bills of materials, production orders, and/or other estimates"*). Replaced with correct Advanced Inventory content: advanced warehouse and materials management for the manufacturing floor.
- **MRP row:** Original description was Project Accounting content (*"Manufacture to a project and track all associated costs at the project task level..."*). Replaced with correct MRP content drawn from the standalone MRP section of the same DRAFT (demand-driven production planning, replenishment recommendations, exception-based alerts). Note: the displaced project-tied manufacturing costs content is correctly covered in W1S2-009 (Project Accounting), Manufacturing Integration row.
- **Estimating row:** Original description was Engineering Change Control (ECC) content (*"Automate, control, and organise all change requests, plans, and actual changes to a bill of materials..."*). Replaced with correct Estimating content drawn from the standalone Estimating section of the same DRAFT.

All standalone sections (Manufacturing Foundation, Discrete Manufacturing, MRP, Estimating, ECC) were correct in the DRAFT — no changes applied to those sections.

**Reviewer note:** This file is the only KB source for Acumatica Manufacturing content — not present in the September 2025 template. HyDac V5.1 (won, December 2024) is the sole source.
