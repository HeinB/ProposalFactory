---
document_id: CONSULTANT_MCP_READINESS
title: "Consultant MCP Readiness — APPTime Integration Design"
version: "1.0"
created: "2026-06-15"
created_by: "WP10 — Consultant Index Programme"
scope: "Design-only document for future APPTime-to-KB integration. No integration is built here. No MCP tools are used."
constraint: "ADR-001 — APPTime is the authoritative source for all CV and consultant data. This document defines what APPTime must expose and what the KB will consume."
---

# Consultant MCP Readiness — APPTime Integration Design

**Status:** Design document only. No integration built. Intended to guide APPTime development roadmap.  
**Audience:** APPTime Product Owner; IT; Tender Factory maintainer  
**Prerequisite:** APPTime must be operational and contain structured consultant records before this design can be implemented.

---

## 1. Purpose

The Tender Knowledge Base currently holds a static `CONSULTANT_INDEX.csv` populated from CVs and certification files discovered during WP10. This index will become stale as consultants join, leave, gain new certifications, or complete new projects.

The intended steady-state architecture (per ADR-001) is:
- **APPTime** holds the authoritative consultant record (CV text, full project history, availability, timesheets, certifications with expiry dates)
- **KB** holds a **Consultant Index Record** (metadata only) that is refreshed from APPTime
- **Tender Factory** reads the Consultant Index to assemble resource plans and skill matrices without re-reading CVs

This document defines what APPTime must expose (API surface), what the KB will consume (data objects), when refresh occurs (trigger model), how access is secured (security model), and what tender assembly use cases the integration serves.

---

## 2. APPTime Required Data Objects

The following fields in `CONSULTANT_INDEX.csv` must be maintained in APPTime as structured data. APPTime must expose these fields as discrete queryable fields — not as free-text blob or PDF attachment.

### 2.1 Consultant Master Record

| Field Name | Type | Description | Source in APPTime |
|---|---|---|---|
| `consultant_id` | String | Unique APPSolve identifier (e.g., CON-ORA-001) | APPTime auto-assigned |
| `name` | String | Full name | Personnel record |
| `employment_type` | Enum | Employee / Contractor / Associate | HR record |
| `business_unit` | Enum | Oracle / Acumatica / BeBanking / Cross-BU | HR record |
| `location` | String | City / Province | HR record |
| `role_title` | String | Current role title | HR record |
| `seniority` | Enum | Junior / Intermediate / Senior / Principal / Director | HR record |
| `years_experience` | Integer | Total years of ERP/relevant experience | Personnel record |
| `active_status` | Boolean | True = available for tender deployment | HR / Resource Mgr |
| `availability_date` | Date | Earliest availability for new project | Resource schedule |
| `daily_rate_band` | Enum | Band A / B / C / D (not exact figure) | Rate card |

### 2.2 Certification Records (linked to Consultant)

| Field Name | Type | Description |
|---|---|---|
| `cert_id` | String | Internal cert ID |
| `cert_name` | String | Full certification name (e.g., Oracle Fusion GL 2025 Certified Impl Professional) |
| `issuing_body` | String | Oracle / Acumatica / PMI / ISACA / TOGAF / other |
| `product_area` | Enum | Oracle ERP / Oracle HCM / OCI / OIC / APEX / Acumatica / Other |
| `issue_date` | Date | Date certification was awarded |
| `expiry_date` | Date | Expiry date (null = no expiry) |
| `cert_status` | Enum | Active / Expired / Renewal In Progress |
| `cert_document_path` | String | Path to certificate PDF in APPTime document store |

### 2.3 Skill Tags (linked to Consultant)

| Field Name | Type | Description |
|---|---|---|
| `skill_tag` | Enum | Controlled vocabulary from KB skill taxonomy (see §5) |
| `proficiency` | Enum | Awareness / Practitioner / Lead / Principal |
| `last_used_year` | Integer | Year of most recent project using this skill |
| `endorsed_by` | String | BU Lead who validated the skill tag |

### 2.4 Project History (linked to Consultant — metadata only)

| Field Name | Type | Description |
|---|---|---|
| `project_ref` | String | Internal project reference (links to APPTime project record) |
| `client_name` | String | Client name (subject to Named Reference Governance Policy) |
| `project_role` | String | Consultant's role on the project |
| `product_deployed` | Enum | From KB product taxonomy |
| `project_start` | Date | Project start month/year |
| `project_end` | Date | Project end month/year (null = ongoing) |
| `named_reference_allowed` | Boolean | Per NAMED_REFERENCE_MATRIX.md |

> **Note:** No project narrative text (what we did, outcomes, challenges) is stored in the KB. Project narrative lives in APPTime and in KB Capability Statements only. The `project_ref` field links back to APPTime for retrieval when needed.

---

## 3. Required API Endpoints

APPTime must expose the following REST API endpoints to support KB refresh. All endpoints require authentication (see §6).

### 3.1 Consultant Endpoints

| Method | Endpoint | Description | Returns |
|---|---|---|---|
| `GET` | `/api/v1/consultants` | List all active consultants | Array of Consultant Master Records |
| `GET` | `/api/v1/consultants/{id}` | Single consultant record | Consultant Master + certs + skills |
| `GET` | `/api/v1/consultants?bu={unit}` | Filter by business unit | Filtered consultant list |
| `GET` | `/api/v1/consultants?available=true` | Filter by current availability | Consultants available for project deployment |
| `GET` | `/api/v1/consultants?skill={tag}` | Filter by skill tag | Consultants with that skill at Practitioner+ level |

### 3.2 Certification Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/certifications` | All certifications across all consultants |
| `GET` | `/api/v1/certifications?expiring_before={date}` | Certifications expiring before given date |
| `GET` | `/api/v1/certifications?product={area}` | Certifications by product area |
| `GET` | `/api/v1/consultants/{id}/certifications` | All certifications for one consultant |

### 3.3 Project History Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/consultants/{id}/projects` | Project history for consultant (metadata only) |
| `GET` | `/api/v1/projects?product={area}` | Projects by product area (cross-consultant) |

### 3.4 Availability / Resource Scheduling

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/resources/available?from={date}&to={date}` | Consultants available in date range |
| `GET` | `/api/v1/resources/available?skill={tag}&from={date}` | Available consultants with specific skill in date range |

---

## 4. Refresh Strategy

### 4.1 Recommended: Event-Driven Refresh

Preferred approach for keeping CONSULTANT_INDEX current without manual intervention:

| Event | Trigger | KB Action |
|---|---|---|
| New consultant hired | APPTime HR record created | KB creates new Consultant Index Record (skeleton; BU Lead to validate tags) |
| Consultant status changed to inactive | APPTime HR status updated | KB sets `active_status = false`; removes from skill matrix |
| Certification added | APPTime cert record created | KB updates consultant cert fields |
| Certification expired | APPTime cert expiry date passed | KB sets cert_status = Expired; flags in CV_GAP_ANALYSIS |
| Project completed | APPTime project record closed | KB adds project metadata to consultant record |
| Availability changes | APPTime resource schedule updated | KB updates `availability_date` |

**Implementation note:** APPTime must support webhooks or an event queue (e.g., Azure Service Bus, internal queue) for the KB to subscribe to these events. If APPTime cannot support webhooks, fall back to scheduled refresh (§4.2).

### 4.2 Fallback: Scheduled Batch Refresh

If event-driven is not feasible in the APPTime release roadmap, implement nightly batch:

- **Time:** 01:00 SAST nightly
- **Process:** KB polling script calls `GET /api/v1/consultants` with `modified_since={last_run_timestamp}`
- **Delta detection:** Compare returned records against current CONSULTANT_INDEX.csv; update changed records; flag new records for BU Lead validation
- **Frequency:** Nightly for cert expiry monitoring; weekly for skill tag refresh

### 4.3 Manual Override

BU Leads must be able to override APPTime-sourced data at the KB level in cases where:
- APPTime record is incomplete or pending update
- Tender requires a specific framing of skills not captured in the structured tag
- A consultant's availability for a specific tender differs from the general schedule

Manual overrides are recorded in a `_manual_override` flag field and reviewed quarterly to determine if APPTime needs updating.

---

## 5. KB Skill Taxonomy (Controlled Vocabulary for Skill Tags)

APPTime must use this controlled vocabulary when tagging consultant skills. This vocabulary maps directly to CONSULTANT_SKILL_MATRIX.md product coverage areas.

### Oracle Practice Tags
`ORA-EBS-FINANCE` · `ORA-EBS-HCM` · `ORA-EBS-DBA` · `ORA-EBS-TECHNICAL` · `ORA-EBS-PROJECTS` · `ORA-EBS-PROCUREMENT` · `ORA-EBS-SCM`  
`ORA-FUSION-GL` · `ORA-FUSION-AP` · `ORA-FUSION-AR` · `ORA-FUSION-FA` · `ORA-FUSION-ACCOUNTING-HUB` · `ORA-FUSION-PPM` · `ORA-FUSION-PROCUREMENT` · `ORA-FUSION-SCM` · `ORA-FUSION-INVENTORY` · `ORA-FUSION-WMS`  
`ORA-HCM-CORE-HR` · `ORA-HCM-PAYROLL-FUSION` · `ORA-HCM-PAYROLL-EBS` · `ORA-HCM-RECRUITING` · `ORA-HCM-LEARNING` · `ORA-HCM-TALENT` · `ORA-HCM-ABSENCE` · `ORA-HCM-TL` · `ORA-HCM-COMPENSATION` · `ORA-HCM-HR-HELP-DESK`  
`ORA-OCI-ARCHITECTURE` · `ORA-OCI-COMPUTE` · `ORA-OCI-DATABASE-MIGRATION` · `ORA-OCI-SECURITY` · `ORA-OCI-ODA` · `ORA-OCI-AI`  
`ORA-OIC-DESIGN` · `ORA-OIC-EBS-INTEGRATION` · `ORA-OIC-FUSION-INTEGRATION`  
`ORA-APEX-DEVELOPMENT` · `ORA-APEX-ADB` · `ORA-ANALYTICS-OAC` · `ORA-ANALYTICS-OBIEE`  
`ORA-SOLUTION-ARCHITECT` · `ORA-PROJECT-MANAGEMENT`

### Acumatica Tags
`ACU-FINANCE` · `ACU-DISTRIBUTION` · `ACU-MANUFACTURING` · `ACU-RETAIL` · `ACU-CUSTOMER-SUCCESS` · `ACU-TECHNICAL` · `ACU-ECOMMERCE`

### BeBanking Tags
`BBNK-H2H-INTEGRATION` · `BBNK-PAYMENT-PROCESSING` · `BBNK-IMPLEMENTATION`

### Cross-BU Tags
`XBU-PROGRAMME-MANAGEMENT` · `XBU-PROJECT-MANAGEMENT` · `XBU-BUSINESS-ANALYSIS` · `XBU-TESTING-QA` · `XBU-TEST-AUTOMATION` · `XBU-SOLUTION-ARCHITECTURE` · `XBU-ENTERPRISE-ARCHITECTURE` · `XBU-CYBERSECURITY` · `XBU-CLOUD-INFRASTRUCTURE` · `XBU-JAVA-DEVELOPMENT` · `XBU-DEVOPS`

---

## 6. Security Model

### 6.1 Access Control

| Consumer | Access Level | Scope |
|---|---|---|
| KB Tender Factory (automated) | Read-only API key | All fields except `daily_rate_band` |
| BU Lead (human) | Read + validate-tag permission | Own BU consultants only |
| Director (Hein Blignaut) | Full read | All records |
| External (tender portal) | None | No direct APPTime access; KB outputs only |

### 6.2 Data Classification

| Data Element | Classification | Handling |
|---|---|---|
| Consultant name + role | Internal | Included in tender documents (with consent) |
| Daily rate band | Confidential | Never exposed in KB; accessed by Director/Finance only via APPTime |
| Certification details | Internal | Included in tender CVs |
| Availability date | Internal | KB reads for resource planning; not published in tenders |
| Project history (named clients) | Confidential until reference approved | Governed by NAMED_REFERENCE_MATRIX.md |

### 6.3 API Authentication

Recommended: OAuth 2.0 Client Credentials flow with short-lived tokens (1-hour TTL). KB refresh scripts hold client credentials in secure vault (not in code or KB files). If APPTime uses a simpler model (API key), store the key in environment variable on the KB server — never committed to the KB repository.

---

## 7. Tender Assembly Use Cases

These are the end-state scenarios the APPTime–KB integration must serve. Each use case maps to a query on the APPTime API surface defined in §3.

### UC-1 — Named Resource Plan (Most Common)

**Trigger:** Tender requires named CV list for specific roles (PM, Functional Lead, Technical Lead, DBA)  
**Query sequence:**
1. `GET /api/v1/resources/available?from={project_start}&to={project_end}`
2. Filter by required `skill_tag` for each role
3. For each matched consultant: retrieve cert list, project history metadata, active status
4. Generate resource plan table; attach CV PDFs from Rate Card path
5. BU Lead validates and approves before submission

### UC-2 — Competency Matrix for RFP

**Trigger:** Tender asks for a matrix of skills/certifications across the delivery team  
**Query sequence:**
1. `GET /api/v1/consultants?bu={oracle|acumatica|bebanking}`
2. For each consultant: retrieve skill tags and certifications
3. Render skill matrix (analogous to CONSULTANT_SKILL_MATRIX.md) with current live data

### UC-3 — Certification Count for Partner Evidence

**Trigger:** Tender asks "How many of your consultants are Oracle/Acumatica certified?"  
**Query sequence:**
1. `GET /api/v1/certifications?product={area}&status=Active`
2. Aggregate count by product area and certification level
3. Output: "APPSolve holds X active Oracle Cloud certifications across Y consultants"

### UC-4 — Expiring Certifications Alert (Preventive)

**Trigger:** Monthly compliance check to avoid KB data becoming stale  
**Query sequence:**
1. `GET /api/v1/certifications?expiring_before={today+90days}`
2. Generate renewal alert list; assign to BU Lead for action
3. Update KB COMPLIANCE_REGISTER.csv cert entries (future: COMP-017+ Oracle cert expiry tracking)

### UC-5 — SPOF Detection

**Trigger:** Before submitting a large tender, confirm no SPOF in proposed team  
**Query sequence:**
1. For each skill tag in the proposed resource plan: `GET /api/v1/consultants?skill={tag}&available=true`
2. If count < 2 for a critical role → flag as SPOF
3. Output SPOF warning to BU Lead before submission

---

## 8. Implementation Roadmap

This integration should be implemented in phases aligned to APPTime development capacity.

| Phase | Deliverable | Prerequisites | Target |
|---|---|---|---|
| **Phase 0 (Now)** | Static CONSULTANT_INDEX.csv | Complete — WP10 delivers this | 2026-06-15 |
| **Phase 1** | APPTime structured fields built | APPTime dev roadmap item approved | Q3 2026 |
| **Phase 2** | Manual export from APPTime → CSV import | APPTime exports to CSV/Excel | Q4 2026 |
| **Phase 3** | Scheduled batch API refresh | APPTime REST API available | Q1 2027 |
| **Phase 4** | Event-driven refresh + SPOF UC | APPTime webhooks / event queue | Q2 2027 |
| **Phase 5** | Full tender assembly automation | All prior phases stable | Q3 2027 |

**Immediate action (Phase 0→1):** APPSolve IT to review this document with APPTime Product Owner and add Phase 1 fields to APPTime development backlog. Priority fields: `active_status`, `availability_date`, `cert_expiry_date`, `skill_tags`.

---

*CONSULTANT_MCP_READINESS v1.0 | Design document only | No MCP tools used | No APPTime integration built | APPSolve IT to implement per roadmap above | Created 2026-06-15*
