---
document_id: W1S2-007-ACU-PayrollIntegration
title: "Acumatica PaySpace Payroll Integration Capability Statement"
version: "1.2 APPROVED"
source_document: "BU Lead Decisions D-W7-001 through D-W7-004 (Hein Blignaut, 2026-06-12)"
source_path: ""
source_status: "Approved"
extraction_date: "2026-06-12"
extracted_by: "Claude (AI authoring from BU Lead decisions)"
approved_for_reuse: "Yes"
lifecycle_status: APPROVED
approved_by: "Hein Blignaut"
approval_date: "2026-06-12"
business_unit: "Acumatica"
review_status: "Approved"
kb_destination: "06_Capabilities/Acumatica/Payroll_Integration/"
source_type: "BU Lead Decision"
authoring_note: "No corpus source document exists for PaySpace integration (confirmed by full corpus search 2026-06-12). Content authored from confirmed BU Lead decisions D-W7-001 through D-W7-004. BU Lead refinements applied and approved 2026-06-12."
---

> **APPROVED — approved_for_reuse: Yes — Approved by Hein Blignaut, 2026-06-12**
> Source: BU Lead Decisions D-W7-001 through D-W7-004 (Hein Blignaut, 2026-06-12) — no corpus source document
> Governance note: APPSolve does not implement native Acumatica Payroll in South Africa. Integration scope only. PaySpace is the payroll system of record.
> Review_Required file: `07_Approved_Content/Review_Required/Acumatica/W1S2-007-ACU-PayrollIntegration.md` (SUPERSEDED)
> KB copy: `06_Capabilities/Acumatica/Payroll_Integration/W1S2-007-ACU-PayrollIntegration.md`

---

## BU Lead Review Record

| Review Item | BU Lead Decision | Date |
|---|---|---|
| Section 1 — SA Payroll Integration Context | Add explicit statements: Acumatica not used for statutory payroll calculations in SA; PAYE/UIF/SDL/IRP5/EMP501 compliance processing = PaySpace responsibility; document describes integration capability, not payroll processing capability. APPLIED. | 2026-06-12 |
| Section 2 — APPSolve Payroll Integration Approach | Expand APPSolve's role to explicitly include: integration design, data mapping, validation and reconciliation, testing and deployment support. APPLIED. | 2026-06-12 |
| Section 4 — Integration Architecture and Data Flows | Architecture presented as Acumatica ↔ Integration Layer ↔ PaySpace. Do not imply direct API always used. APPLIED — data flow updated to bidirectional notation; intro wording revised. | 2026-06-12 |
| Section 5 — Payroll Journal and Financial Reconciliation | Retain and emphasise: "The journal integration method is determined during solution design and may use API integration, automated imports, or controlled manual processes depending on client requirements." Do not imply single mandatory pattern. APPLIED. | 2026-06-12 |
| Section 6 — SA Compliance Responsibilities | Include explicit 5-responsibility matrix: Payroll calculations / PAYE+UIF+SDL compliance / IRP5+EMP501 submissions = PaySpace; Financial posting and reporting / Cost centre allocation and reconciliation = Acumatica. APPLIED. | 2026-06-12 |
| Section 8 — Governance Register | Add R-W7-005: payroll integrations are client-specific; bespoke mapping, validation and reconciliation may be required. Mitigation: confirm during solution design and discovery. APPLIED. | 2026-06-12 |
| D-W7-001 through D-W7-004 | All four BU Lead decisions confirmed CLOSED. Wording confirmed as accurate. | 2026-06-12 |
| Final approval | Approved for reuse. approved_for_reuse: Yes. approved_by: Hein Blignaut. approval_date: 2026-06-12. | 2026-06-12 |

---

# Acumatica PaySpace Payroll Integration Capability Statement

---

## 1. South African Payroll Integration Context

South African payroll is governed by a distinct statutory framework that imposes precise calculation, withholding, and reporting obligations on every employer. These obligations include Pay-As-You-Earn (PAYE) income tax withholding under the Income Tax Act, Unemployment Insurance Fund (UIF) contributions under the Unemployment Insurance Act, and Skills Development Levy (SDL) contributions under the Skills Development Levies Act. Monthly submission of the EMP201 return to SARS is mandatory, the annual EMP501 reconciliation must balance against all monthly submissions, and IRP5 employee tax certificates must be issued to all employees at tax year-end.

These compliance requirements are locally specific and subject to frequent SARS regulatory changes.

**Scope clarification:** This document describes APPSolve's **payroll integration capability**, not payroll processing capability. Acumatica is not used for statutory payroll calculations in South Africa. PAYE, UIF, SDL, IRP5, and EMP501 compliance processing remains the responsibility of PaySpace as the payroll system of record. APPSolve's role is to connect Acumatica with PaySpace so that payroll financial data flows accurately into the Acumatica general ledger.

South African Acumatica implementations are therefore designed around a two-system model: Acumatica serves as the ERP and financial system of record — covering financials, distribution, manufacturing, project accounting, and operations — while PaySpace manages all payroll processing, statutory calculations, and SARS submissions.

APPSolve's confirmed integration partner for Acumatica payroll integration is **PaySpace** — a cloud-native South African payroll and human resource management platform built for SARS legislative compliance. The integration between Acumatica and PaySpace ensures that payroll financial data is accurately reflected in Acumatica's general ledger, enabling complete financial reporting, cost allocation, and audit-ready period-end close.

> **Note on scope:** This capability statement is distinct from BeBanking's Host-to-Host (H2H) payroll payment capability, which transmits payment files from Oracle ERP systems to banking institutions. BeBanking H2H payroll is a separate product serving a separate function. Acumatica–PaySpace integration addresses the transfer of payroll journals into the Acumatica financial ledger only.

---

## 2. APPSolve Payroll Integration Approach

APPSolve positions the Acumatica–PaySpace integration as a deliberate architectural design: PaySpace is the payroll system of record, responsible for all payroll processing, statutory compliance, and SARS submissions. Acumatica is the financial system of record, responsible for the general ledger, financial reporting, cost centre management, and management accounts.

The integration transfers payroll journal data from PaySpace into Acumatica following each payroll run, ensuring that:

- Gross salaries, employer contributions, and statutory deductions are reflected in the Acumatica general ledger
- Payroll costs are allocated to the correct cost centres, project codes, and natural accounts
- Month-end financial close is supported with accurate payroll expense recognition
- Payroll-related provisions and accruals can be traced to verifiable journal entries

**APPSolve's implementation scope covers four core activities:**

| Activity | Description |
|---|---|
| **Integration design** | Scoping the integration architecture, selecting the appropriate integration pattern, and designing the data flow between PaySpace and Acumatica based on the client's technical environment and requirements |
| **Data mapping** | Mapping PaySpace payroll categories, cost centres, and employee groupings to Acumatica GL accounts, financial dimensions, and sub-accounts |
| **Validation and reconciliation** | Configuring validation rules and reconciliation checks to confirm that payroll journal totals in Acumatica match PaySpace payroll run outputs; resolving variances before period-end close |
| **Testing and deployment support** | Conducting integration testing across payroll scenarios prior to go-live; providing deployment support during initial live payroll runs to confirm end-to-end accuracy |

The integration method — API-based, middleware-facilitated, or controlled manual data exchange — is selected during the solution design phase based on the client's technical environment, PaySpace configuration, and transaction volume requirements. No single method is pre-committed before a solution design engagement.

This approach provides clients with the operational flexibility to choose an integration pattern appropriate to their environment while maintaining the financial accuracy and compliance assurance that statutory South African payroll obligations require.

---

## 3. PaySpace Integration Overview

PaySpace is a cloud-native South African payroll and HR management platform designed for SARS legislative compliance. It supports PAYE calculation and withholding, UIF contributions, SDL levies, EMP201 monthly submissions, EMP501 annual reconciliation, and IRP5 certificate generation. PaySpace is the sole confirmed integration target for APPSolve's Acumatica payroll integration capability.

The integration scope between Acumatica and PaySpace covers:

| Integration Scope Item | Description |
|---|---|
| **Payroll journals** | Periodic payroll run data transferred from PaySpace to the Acumatica general ledger |
| **Cost centre mapping** | Alignment of PaySpace cost centres to Acumatica financial dimensions and sub-accounts |
| **GL account mapping** | Mapping of payroll expense categories to Acumatica chart of accounts |
| **Payroll reconciliation** | Verification that PaySpace payroll totals match Acumatica GL postings |
| **Period allocation** | Payroll costs allocated to the correct financial period in Acumatica |

The integration does not extend to payroll system configuration, statutory compliance settings, SARS submissions, or PaySpace administration — these remain the responsibility of the client's payroll team operating within the PaySpace platform.

APPSolve does not extend this integration scope to other payroll platforms without additional confirmed evidence. If a tender prospect uses a payroll system other than PaySpace, APPSolve will confirm the integration approach separately before committing to a capability claim in a tender response.

---

## 4. Integration Architecture and Data Flows

APPSolve implements three integration patterns for Acumatica–PaySpace connectivity, mediated through an integration layer that sits between the two systems. The appropriate pattern is selected during solution design based on the client environment, data volume, internal control requirements, and technical capability.

The integration is architecturally framed as:

```
Acumatica ↔ Integration Layer ↔ PaySpace
```

This bidirectional design reflects that the integration layer manages data exchange between both systems — retrieving payroll journal data from PaySpace and posting validated entries to Acumatica — regardless of which specific integration pattern is used.

### 4.1 API-Based Integration

Where PaySpace provides API access and the client's technical environment supports it, APPSolve configures an API-based connection between the two systems via the integration layer. This pattern:

- Retrieves payroll journal data from PaySpace via its API following each payroll run finalisation
- Posts journal entries to Acumatica through the integration layer, eliminating manual data transfer steps
- Provides a fully auditable integration log from PaySpace payroll run to Acumatica GL posting

### 4.2 Middleware-Facilitated Integration

Where direct API connectivity is not available, or where the client's architecture requires a controlled intermediary, APPSolve implements a custom middleware integration layer. This pattern:

- Receives structured payroll export data from PaySpace
- Applies transformation and validation rules against Acumatica's GL structure, account mapping, and dimension requirements
- Posts the validated journal to Acumatica through its import or API endpoint
- Maintains an audit trail of data transformation, validation results, and posting events

### 4.3 Controlled Manual Data Exchange

Where automated integration is not appropriate — typically for lower payroll volumes, transitional environments, or where internal controls require human review before GL posting — APPSolve implements a controlled manual data exchange process via the integration layer. This pattern:

- Defines a structured payroll export template from PaySpace with required fields and format
- Applies pre-import validation rules to the exported data before it enters Acumatica
- Uses Acumatica's standard journal import to post the validated payroll data
- Includes a documented review and sign-off step before each posting is finalised

### 4.4 Data Flow

All three integration patterns follow the same logical architecture:

```
PaySpace                          Acumatica
(payroll system of record)        (financial system of record)
         │                               ▲
         ▼                               │
    Integration Layer ─────────────────►│
  (API / middleware /                    │
   controlled manual)         Payroll journal posted
                              (accounts, cost centres, dimensions)
                                         │
                                         ▼
                               Financial Reporting
                     (P&L, cost centre reports, management accounts)
```

The integration layer mediates all data exchange between PaySpace and Acumatica. The specific mechanism — API, middleware, or controlled manual — is determined during solution design based on client requirements. No single method is assumed or pre-committed.

---

## 5. Payroll Journal and Financial Reconciliation

The transfer of payroll journal data and subsequent reconciliation between PaySpace and Acumatica is the core functional output of the integration.

> **The journal integration method is determined during solution design and may use API integration, automated imports, or controlled manual processes depending on client requirements.** No single method is mandatory. Each implementation uses one primary approach, selected based on the client's technical environment, transaction volume, internal control requirements, and preference.

APPSolve implements one of three reconciliation approaches per implementation:

### 5.1 API-Based Journal Integration

Payroll journal data is retrieved from PaySpace via API and posted to Acumatica through the integration layer. Journal entries are generated at the natural account and cost centre level, providing full payroll cost visibility within Acumatica financial reports. Post-posting reconciliation compares PaySpace payroll run totals against Acumatica GL balances to confirm completeness and accuracy.

### 5.2 Automated GL Import

Payroll data is exported from PaySpace in a structured format (typically CSV or compatible structured file) and imported into Acumatica using its standard import routines. APPSolve configures the field mapping between PaySpace export fields and Acumatica GL accounts and financial dimensions. The import process is scheduled to run following payroll finalisation, reducing manual effort and data transfer risk.

### 5.3 Manual Journal Import

A documented, controlled process in which payroll data is exported from PaySpace by the client's payroll administrator, reviewed and signed off, and then imported into Acumatica by the finance team using a pre-defined journal template. APPSolve defines the journal template, account mapping rules, and the sign-off procedure that must be completed before each import. This method is appropriate for lower payroll volumes or environments where internal controls require pre-posting human review.

---

## 6. South African Compliance Responsibilities

The Acumatica–PaySpace integration model assigns compliance responsibilities clearly between the two platforms. This delineation is a fundamental design principle of the two-system model.

**Responsibility matrix:**

| Responsibility | System |
|---|---|
| Payroll calculations | PaySpace |
| PAYE / UIF / SDL compliance | PaySpace |
| IRP5 / EMP501 submissions | PaySpace |
| Financial posting and reporting | Acumatica |
| Cost centre allocation and reconciliation | Acumatica |

**Expanded detail:**

| Compliance Responsibility | System | Notes |
|---|---|---|
| PAYE calculation and income tax withholding | PaySpace | Income Tax Act obligation |
| UIF contributions (employer and employee) | PaySpace | Unemployment Insurance Act obligation |
| SDL levy calculation | PaySpace | Skills Development Levies Act obligation |
| EMP201 monthly submission to SARS | PaySpace | Monthly payroll tax return |
| EMP501 annual reconciliation submission | PaySpace | Annual payroll tax reconciliation |
| IRP5 employee tax certificate generation | PaySpace | Issued to employees at tax year-end |
| Payroll calculation accuracy | PaySpace | Gross pay, net pay, deductions, contributions |
| Payroll journal posting to general ledger | Acumatica | Via the integration layer |
| Cost centre allocation of payroll expenses | Acumatica | Mapped during APPSolve integration design |
| Financial period recognition of payroll costs | Acumatica | Period-end close |
| P&L reporting of salary and wage costs | Acumatica | Management accounts and statutory financials |
| Payroll expense accruals and provisions | Acumatica | Leave provisions, bonus accruals |
| Cost centre reconciliation | Acumatica | Payroll cost vs GL balance |

APPSolve's implementation scope covers the configuration and maintenance of the integration layer, and the setup of GL account mapping, cost centre mapping, and financial dimension alignment within Acumatica.

Statutory payroll compliance — PAYE, UIF, SDL, EMP201, EMP501, and IRP5 — remains the sole responsibility of the client's payroll team, operating through the PaySpace platform. APPSolve does not advise on payroll tax compliance, provide statutory tax calculations, or represent PaySpace's compliance certifications.

---

## 7. Benefits

The Acumatica–PaySpace integration model, as implemented by APPSolve, delivers the following benefits:

| Benefit | Description |
|---|---|
| **Financial completeness** | Payroll costs are fully and accurately reflected in Acumatica's general ledger, supporting complete financial reporting and audit readiness at period end. |
| **Statutory compliance assurance** | PaySpace manages all South African statutory payroll obligations; Acumatica reflects the financial outcome. Compliance responsibilities are clearly delineated between the two systems. |
| **Flexible integration architecture** | Three integration patterns — API-based, middleware-facilitated, and controlled manual — accommodate different client technical environments, volumes, and internal control requirements. |
| **Cost centre and project visibility** | Payroll costs are allocated to the correct cost centres, natural accounts, and project codes in Acumatica, enabling management reporting at departmental and project level. |
| **Reduced manual reconciliation effort** | Automated integration patterns eliminate manual re-entry of payroll data, reducing the risk of data errors and the reconciliation burden on finance teams. |
| **Audit trail integrity** | All three integration methods produce a traceable audit trail from the PaySpace payroll run to the Acumatica GL posting, supporting internal audit and external financial review. |
| **Month-end efficiency** | Payroll journals are available in Acumatica promptly after payroll finalisation, supporting timely financial period close without waiting for manual data transfer. |
| **Scalable design** | The integration architecture scales from manual controlled processes for smaller organisations to API-based automation for higher-volume environments, without requiring a redesign as the client grows. |

---

## 8. Source Mapping and Governance Register

### 8.1 Source Basis

No corpus source document exists for Acumatica–PaySpace payroll integration within APPSolve's historical tender corpus. This was confirmed by a full corpus search conducted on 2026-06-12, covering all client proposal documents in `Parties/Customers/` using both keyword grep and Python DOCX extraction against terms including "PaySpace", "payroll integration", "payroll API", "payroll journal", and "payroll system". Zero relevant documents were identified.

This document is authored from BU Lead decisions (D-W7-001 through D-W7-004, confirmed by Hein Blignaut, 2026-06-12) under the KB's confirmed authoring-from-scratch protocol: *"Content authoring from scratch is appropriate only where no source document exists."*

All content in Sections 1 through 7 is based on the confirmed BU Lead decisions listed in Section 8.2, supplemented by general knowledge of South African payroll statutory requirements (PAYE, UIF, SDL, EMP201, EMP501, IRP5). No product marketing claims have been extracted from PaySpace or Acumatica published materials. All integration capability claims are framed as APPSolve implementation capability, not Acumatica or PaySpace product features.

### 8.2 BU Lead Decision Register

| Decision ID | Decision | Wording confirmed | Confirmed by | Date |
|---|---|---|---|---|
| D-W7-001 | APPSolve does not implement Acumatica native Payroll in South Africa. PaySpace is the integration target. Scope is payroll integration capability only — not native payroll processing. | Yes | Hein Blignaut | 2026-06-12 |
| D-W7-002 | Confirmed payroll platform: PaySpace only. No other payroll platforms may be listed or claimed without additional confirmed evidence and a separate BU Lead decision. | Yes | Hein Blignaut | 2026-06-12 |
| D-W7-003 | Confirmed integration methods: API integration, custom middleware, controlled manual integration processes. | Yes | Hein Blignaut | 2026-06-12 |
| D-W7-004 | Supported journal integration methods: API-based integration, automated GL import, manual journal import. Method selected per client requirements during solution design. | Yes | Hein Blignaut | 2026-06-12 |

### 8.3 Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-W7-001 | No corpus evidence exists. Content is authored from BU Lead decisions, not extracted from a confirmed client engagement. Content accuracy depends on BU Lead decision quality. | Low — decisions confirmed and approved by BU Lead | High — incorrect claims in tender | BU Lead approved 2026-06-12. Pre-tender check PT-W7-001 must be completed before citing in any tender. |
| R-W7-002 | PaySpace only — D-W7-002 prohibits listing other platforms. If tender requires a different payroll system, this document cannot be cited. | Medium — many SA clients use other payroll systems | Medium — tender response gap | PT-W7-001 must confirm client payroll system before use. |
| R-W7-003 | No named reference clients. No corpus evidence exists; no client can be cited as a PaySpace integration reference without a separate BU Lead decision. | Medium — tender evaluators often request references | Medium — reduced credibility | PT-W7-002 must be completed; do not cite reference clients without BU Lead confirmation. |
| R-W7-004 | Integration method commitment risk. If a tender response is read as committing to a specific integration method, APPSolve may be held to it contractually. | Low — document wording is deliberately non-prescriptive | High — contractual exposure | Use qualifying wording from Section 2 and Section 5 note. PT-W7-003 governs. |
| R-W7-005 | Payroll integrations are client-specific and may require bespoke mapping, validation, and reconciliation rules beyond the standard patterns described in this document. | Medium — every client has a unique chart of accounts, cost centre structure, and payroll setup | Medium — integration scope underestimation | Confirm integration scope, mapping requirements, and reconciliation approach during solution design and discovery. Do not commit to a fixed integration effort without a scoping exercise. |

### 8.4 Assumptions

| Assumption ID | Assumption | Impact if incorrect |
|---|---|---|
| A-W7-001 | The tender prospect uses PaySpace as their payroll system of record. | This capability statement does not apply. Integration approach must be confirmed separately before any tender claim is made. |
| A-W7-002 | The integration method is selected during solution design based on the client's environment. No specific method is pre-committed in this document. | If a tender response is interpreted as committing to a specific method, a qualifying statement must be added explicitly. |
| A-W7-003 | PaySpace provides sufficient API or structured export capability to support the selected integration pattern. | If PaySpace does not support the required integration mechanism, a client-specific workaround must be scoped and costed before quoting. |

### 8.5 Pre-Tender Checks

The following checks must be completed before this document is cited in any tender response.

| Check ID | Check | Action required |
|---|---|---|
| PT-W7-001 | **Client payroll system** | Confirm the prospect uses PaySpace as their payroll system of record. If not, do not cite this document without a separate BU Lead decision authorising scope extension. |
| PT-W7-002 | **Reference clients** | This document contains no named reference clients. Before claiming a referenceable PaySpace integration engagement in a tender, confirm with BU Lead that evidence exists and that the client is referenceable. |
| PT-W7-003 | **Integration method commitment** | Do not commit to a specific integration method (API / middleware / manual) in a tender response without including the qualifying statement that the final method is confirmed during solution design. |
| PT-W7-004 | **PaySpace product currency** | Confirm that the PaySpace integration approach documented in this capability statement is consistent with the current PaySpace product offering and API availability at the time of tender submission. |

---

## 17. Approval Record

### 17.1 Approval Record

| Field | Value |
|---|---|
| Document ID | W1S2-007-ACU-PayrollIntegration |
| Version | 1.2 APPROVED |
| Approved by | Hein Blignaut |
| Approval date | 2026-06-12 |
| approved_for_reuse | Yes |
| Source type | BU Lead Decision (D-W7-001 through D-W7-004) |
| Corpus source | None — confirmed by full search 2026-06-12 |
| KB destination | `06_Capabilities/Acumatica/Payroll_Integration/` |
| Authoring basis | BU Lead decisions only — authoring-from-scratch protocol |
| Standing governance note | APPSolve does not implement native Acumatica Payroll in South Africa. Integration scope only. PaySpace is the payroll system of record and owns all statutory payroll compliance. Acumatica is the financial system of record. Integration method is client-specific and confirmed during solution design. No reference clients approved. |

### 17.2 Pre-Tender Checks (Standing)

The following checks must be completed each time this document is cited in a tender response.

| Check ID | Check | Action required |
|---|---|---|
| PT-W7-001 | **Client payroll system** | Confirm the prospect uses PaySpace as their payroll system of record. If not, do not cite this document without a separate BU Lead decision authorising scope extension. |
| PT-W7-002 | **Reference clients** | This document contains no named reference clients. Before claiming a referenceable PaySpace integration engagement, confirm with BU Lead that evidence exists and that the client is referenceable. |
| PT-W7-003 | **Integration method commitment** | Do not commit to a specific integration method (API / middleware / manual / automated import) in a tender response without including the qualifying statement that the final method is confirmed during solution design. |
| PT-W7-004 | **PaySpace product currency** | Confirm that the PaySpace integration approach documented in this capability statement is consistent with the current PaySpace product offering and API availability at the time of tender submission. |

---

*Approved by: Hein Blignaut | Approval date: 2026-06-12 | Acumatica Wave 1 Payroll Integration Deliverable — approved_for_reuse: Yes*
