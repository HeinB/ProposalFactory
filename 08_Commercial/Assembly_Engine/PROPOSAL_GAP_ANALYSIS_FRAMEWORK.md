---
document_id: PROPOSAL-GAP-ANALYSIS-FRAMEWORK
title: "Proposal Gap Analysis Framework — Gap Analysis Engine Design"
version: "1.0"
status: "Approved — WP18A"
created: "2026-06-25"
created_by: "WP18A — Proposal Factory Architecture"
category: "Architecture / Engine Design"
scope: "Defines the design of the Proposal Gap Analysis Engine (WP18C). When proposal assembly cannot complete automatically, the engine identifies exactly what is missing, classifies severity, identifies responsible owner, and provides remediation guidance. This document is the governing specification for WP18C."
---

# Proposal Gap Analysis Framework

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18A — Proposal Factory Architecture  
**Governs:** WP18C — Proposal Gap Analysis Engine  
**Position in pipeline:** PROPOSAL_ASSEMBLY_SEQUENCE.md Step 9

---

## 1. Purpose

The Gap Analysis Engine runs before proposal section assembly begins (Step 9 of the assembly sequence). Its role is to identify every gap that would prevent the factory from producing a complete, submission-ready proposal.

A gap is defined as any condition where the Proposal Factory cannot automatically produce a required proposal element from approved KB sources.

The engine does not stop assembly. It records and classifies gaps, inserts `[GAP]` markers into the assembled proposal at the affected section, and produces a Gap Register for BU Lead and Bid Manager action.

---

## 2. Gap Categories

| Category Code | Category Name | Description |
|---|---|---|
| G-CAP | Missing Capability | A required product capability has no approved KB asset covering it |
| G-ASS | Missing Assumption Pack | A required assumption pack does not exist or is not yet approved |
| G-METH | Missing Methodology | A required methodology document is absent from the Methodology Library |
| G-REF | Missing Reference | No qualifying reference letter exists for the required product / sector combination |
| G-CV | Missing CV | Required consultant has no current CV obtainable from APPTime |
| G-CASE | Missing Case Study | No case study for the required sector / solution exists in the KB |
| G-COMP | Missing Compliance | A required compliance document is absent, expired, or pending |
| G-COMM | Missing Commercial Decision | A required commercial decision has not been made (rate, discount, margin, pricing model) |
| G-CUST | Missing Customer Information | Required client-specific information has not been provided (entity count, user count, integration list, etc.) |
| G-REQ | Missing Compliance Response | The tender requires a specific compliance response (POPIA, ISO, sector cert) that APPSolve cannot provide |
| G-CERT | Missing Certification | A required partner or product certification is absent or expired |
| G-RISK | Missing Risk Information | A required risk register or RAID log cannot be produced (no Risk Library) |
| G-TENDER | Missing Tender Information | Tender document is incomplete — required information not stated in RFP |
| G-GOV | Governance Blocker | A governance restriction prevents including required content (e.g., AM approval pending, prohibited client) |

---

## 3. Gap Severity Classification

| Severity | Code | Meaning | Assembly Impact |
|---|---|---|---|
| Critical | SEV-1 | Gap prevents submission. Proposal cannot be submitted without resolution. | Assembly halts at affected section; BU Lead must resolve or accept exception |
| High | SEV-2 | Gap significantly weakens the proposal. Resolution strongly recommended before submission. | `[GAP-HIGH: description]` inserted; assembly continues |
| Medium | SEV-3 | Gap reduces completeness but does not prevent submission. | `[GAP-MED: description]` inserted; assembly continues |
| Low | SEV-4 | Minor omission; does not affect scoring or commercial protection. | `[GAP-LOW: description]` inserted; noted for future resolution |

---

## 4. Blocking vs Non-Blocking

| Classification | Definition | Engine Action |
|---|---|---|
| **Blocking** | Gap prevents a mandatory section from being assembled. Proposal cannot be submitted with this section absent. | Engine flags as BLOCKING; BU Lead must resolve or explicitly accept risk before assembly proceeds past this section. |
| **Non-blocking** | Gap produces an incomplete or weakened section but does not prevent submission. | Engine inserts `[GAP]` marker; assembly continues; gap registered for BU Lead awareness. |

**Blocking gap examples:**
- No assumption pack for a product type that is central to the engagement
- B-BBEE certificate expired and tender requires current certificate
- No reference letter for a product that the tender requires evidence for
- Commercial pricing section cannot be populated (CD decision outstanding)

**Non-blocking gap examples:**
- No case study for a secondary product in scope
- DR methodology absent but engagement does not specifically require DR design
- Consultant summary profiles not available from APPTime (CVs will follow)

---

## 5. Gap Register Format

Each gap identified by the engine is recorded in the Gap Register using this format:

```
GAP-[TENDER_ID]-[NNN]

Category:        [G-CAP / G-ASS / G-METH / G-REF / G-CV / G-CASE / G-COMP / G-COMM / 
                  G-CUST / G-REQ / G-CERT / G-RISK / G-TENDER / G-GOV]
Severity:        [SEV-1 / SEV-2 / SEV-3 / SEV-4]
Blocking:        [Yes / No]
Affected Section: [Section ID from PROPOSAL_SECTION_LIBRARY.md]
Description:     [What is missing and why]
Impact:          [What the proposal cannot include or say as a result]
Responsible Owner: [Bid Manager / BU Lead / Commercial Director / AM / Finance Director / Company Secretary / BU Lead + AM]
Suggested Remediation: [What action resolves the gap]
Deadline:        [Date by which resolution is required to meet submission deadline]
Status:          [Open / In Progress / Resolved / Accepted (risk accepted by BU Lead)]
```

---

## 6. Gap Detection Rules — By Category

### 6.1 Capability Gaps (G-CAP)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-CAP-001 | Tender BOM triggers a product for which no approved capability asset exists | SEV-2 | No |
| GD-CAP-002 | Tender requires OCI standalone narrative and no narrative asset exists | SEV-3 | No |
| GD-CAP-003 | Tender requires a capability that has been archived (W4-HCM-004 T&L) | SEV-2 | Yes if T&L is core to tender |
| GD-CAP-004 | Tender requires Compensation capability but client is NOT mining sector | SEV-1 | Yes |
| GD-CAP-005 | Tender requires an Acumatica module not covered by any approved asset | SEV-2 | No |

### 6.2 Assumption Pack Gaps (G-ASS)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-ASS-001 | BOM triggers a product type with no approved assumption pack | SEV-1 | Yes |
| GD-ASS-002 | Assumption pack exists but is in Draft status | SEV-1 | Yes |
| GD-ASS-003 | AMS engagement does not have KT/onboarding pack (GAP-007) | SEV-3 | No |
| GD-ASS-004 | Mining sector engagement has no Mining Charter assumption pack (GAP-005) | SEV-2 | No |

### 6.3 Methodology Gaps (G-METH)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-METH-001 | Tender requires DR plan and `05_Methodologies/Disaster_Recovery/` is empty | SEV-2 | No |
| GD-METH-002 | Tender requires security design document and no security methodology exists | SEV-2 | No |
| GD-METH-003 | Tender requires formal testing methodology and `05_Methodologies/Testing/` is empty | SEV-3 | No |
| GD-METH-004 | Tender requires project management methodology and `05_Methodologies/Project_Management/` is empty | SEV-3 | No |
| GD-METH-005 | AMS engagement and `05_Methodologies/Managed_Services/` is empty | SEV-3 | No |

### 6.4 Reference Gaps (G-REF)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-REF-001 | Tender requires reference letters and fewer than 2 qualifying letters exist | SEV-2 | No |
| GD-REF-002 | Required reference letter exists but AM approval has not been obtained | SEV-1 | Yes |
| GD-REF-003 | Tender specifies a sector for which no matching reference exists | SEV-2 | No |
| GD-REF-004 | AM-W4E3-001 active — KPMG cannot be named; KPMG reference unavailable | SEV-2 | No |
| GD-REF-005 | Harmony Gold reference unreadable (OAR-B03) | SEV-3 | No |

### 6.5 CV Gaps (G-CV)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-CV-001 | Required consultant is not marked `available_for_tenders: Yes` in CONSULTANT_INDEX | SEV-2 | No |
| GD-CV-002 | Required role has no matching consultant in CONSULTANT_INDEX (skill not covered) | SEV-2 | No |
| GD-CV-003 | Consultant CV not yet obtained from APPTime | SEV-2 | No (placeholder inserted) |

### 6.6 Compliance Gaps (G-COMP)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-COMP-001 | B-BBEE certificate expires before submission date | SEV-1 | Yes |
| GD-COMP-002 | Tax Clearance expires before submission date | SEV-1 | Yes |
| GD-COMP-003 | Directors' Resolution expires before submission date | SEV-1 | Yes |
| GD-COMP-004 | Acumatica Partner Certificate not obtained (OAR-E03) | SEV-2 | No (for Acumatica tenders) |
| GD-COMP-005 | POPIA Policy not available (OAR-E01) | SEV-2 | No |
| GD-COMP-006 | PAIA Manual not available (OAR-E02) | SEV-2 | No |
| GD-COMP-007 | Required ISO certification not held | SEV-2 | No |
| GD-COMP-008 | OPN Level 1 annual revalidation not current | SEV-1 | Yes (Oracle tenders) |
| GD-COMP-009 | Public Liability Insurance expiry not confirmed | SEV-2 | No |

### 6.7 Commercial Gaps (G-COMM)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-COMM-001 | Commercial pricing section not populated by Commercial Director | SEV-1 | Yes |
| GD-COMM-002 | Fixed-price proposal without commercial file (estimate + multiplier + rate card) | SEV-1 | Yes |
| GD-COMM-003 | CD decisions outstanding that affect the engagement type (BU-RC-004/008, BU-CR-003, BU-EM-006) | SEV-2 | No |
| GD-COMM-004 | Margin floor or discount approval required but not yet obtained | SEV-1 | Yes |

### 6.8 Customer Information Gaps (G-CUST)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-CUST-001 | Entity count / Legal Entity count not provided | SEV-2 | No |
| GD-CUST-002 | User count / named user count not confirmed | SEV-3 | No |
| GD-CUST-003 | Integration list not provided for OIC in scope | SEV-2 | No |
| GD-CUST-004 | Go-live date not confirmed | SEV-3 | No |
| GD-CUST-005 | ERP source system(s) not identified for migration | SEV-2 | No |
| GD-CUST-006 | Payroll system not confirmed (defaults to PaySpace per HCM-PAY) | SEV-3 | No |
| GD-CUST-007 | Banking partners not confirmed (BeBanking) | SEV-2 | No |

### 6.9 Governance Blockers (G-GOV)

| Rule | Trigger | Severity | Blocking |
|---|---|---|---|
| GD-GOV-001 | Hollywood Bets reference required and AM approval not obtained | SEV-1 | Yes |
| GD-GOV-002 | Tender subject to Redpath Mining restriction (Rule 21.5) | SEV-1 | Yes |
| GD-GOV-003 | KPMG reference required (AM-W4E3-001 active) | SEV-2 | No |
| GD-GOV-004 | Fixed-price engagement without all required commercial governance approvals | SEV-1 | Yes |
| GD-GOV-005 | BEE certificate expires before tender submission date | SEV-1 | Yes (links to GD-COMP-001) |

---

## 7. Gap Register Output Format

The engine produces `[TENDER_ID]_GAP_REGISTER.md` in `09_Active_Tenders/[TENDER_ID]/`.

### 7.1 Summary section

```
GAP REGISTER — [TENDER_ID]
Generated: [date]
Total gaps: [N]
  SEV-1 (Critical): [N]
  SEV-2 (High): [N]
  SEV-3 (Medium): [N]
  SEV-4 (Low): [N]
Blocking gaps: [N]
Assembly status: [PROCEED / HALT — blocking gaps unresolved]
```

### 7.2 Blocking gaps summary

All SEV-1 and blocking gaps listed first, with owner and deadline.

### 7.3 Full gap register

All gaps in tabular format per Section 5.

---

## 8. Gap Remediation Guidance — Standard Responses

| Gap Category | Standard Remediation |
|---|---|
| G-CAP | Author new capability asset using KB extraction workflow; or scope that capability out of the proposal |
| G-ASS | Author new assumption pack through full governance workflow; or flag engagement as outside current capability scope |
| G-METH | Author methodology document into appropriate `05_Methodologies/` subfolder |
| G-REF | Obtain signed reference letter from client; register in REFERENCE_MASTER.csv; or source from alternate client with AM approval |
| G-CV | Obtain from APPTime; BU Lead to confirm consultant availability |
| G-CASE | Extract case study from historical tender corpus; BU Lead approval required before external use |
| G-COMP | Obtain/renew document; register in COMPLIANCE_REGISTER.csv |
| G-COMM | Commercial Director to populate pricing; BU Lead to obtain required approvals |
| G-CUST | Bid Manager to request client information via pre-bid clarification |
| G-GOV | Obtain approval or exclude restricted content; BU Lead escalation |
| G-CERT | Obtain certification; register in COMPLIANCE_REGISTER.csv |
| G-RISK | Use AI-generated risk register with mandatory human review until Risk Library is built |

---

## 9. Gap Analysis Engine — Interim Operation

Until WP18C is built, the Gap Analysis is performed manually by the Bid Manager using:
1. This framework as the checklist
2. ASSEMBLY_READINESS_MATRIX.md as the capability readiness reference
3. COMPLIANCE_REGISTER.csv for compliance gap detection
4. REFERENCE_MASTER.csv for reference gap detection
5. CONSULTANT_INDEX.csv for CV availability

The Bid Manager produces a manual Gap Register in the same format as Section 7 above, and presents it to BU Lead before assembly begins.

---

*PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md v1.0 | WP18A — Proposal Factory Architecture | 2026-06-25*  
*Design specification for WP18C — Proposal Gap Analysis Engine.*
