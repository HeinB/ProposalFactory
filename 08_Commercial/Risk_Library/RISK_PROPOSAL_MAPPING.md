---
document_id: RISK-PROPOSAL-MAPPING-V1
title: "Risk → Proposal Section and Pattern Mapping — V1.0"
version: "1.0"
status: "DRAFT — Pending BU Lead Review"
created: "2026-06-26"
created_by: "WP18B-EXT.1A — Enterprise Risk Library Normalisation"
approved_by: ""
approved_date: ""
approved_for_reuse: false
category: "Commercial / Risk Library / Governance"
scope: "Maps each canonical risk to the proposal sections and Proposal Patterns where it must appear. Supports the Proposal Factory assembly pipeline."
related_documents:
  - ENTERPRISE_RISK_REGISTER_V1.md
  - 08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md
  - RISK_LIBRARY_STANDARD.md
---

# Risk → Proposal Section and Pattern Mapping — V1.0

**Purpose:** This document maps each canonical risk entry to:
1. The proposal sections where the risk must appear (primary = mandatory output; secondary = supporting context)
2. The Proposal Patterns for which the risk is applicable

**Section reference:**
- **S-12** — Assumptions, Dependencies, and Exclusions
- **S-37** — RAID Framework
- **S-38** — Change Control Process (Implementation patterns only; excluded for P13/AMS per SI-001)
- **S-50** — Risk Register (primary risk output section)
- **S-71** — SLA Framework
- **S-72** — Incident Management Protocol
- **S-73** — AMS Change Request Management (Pattern 13 only; excluded for Implementation per SI-001)

**Pattern reference:**
- P1 = HCM Full Suite Single
- P2 = HCM Full Suite Phased
- P3 = HCM + Payroll Integration
- P4 = Recruiting Standalone
- P5 = Learning Standalone
- P6 = OIC Standalone
- P7 = ERP Multi-Module
- P8 = ERP Single Module
- P9 = EBS Implementation
- P10 = DBA / Managed Services
- P11 = Acumatica
- P12 = BeBanking
- P13 = AMS

**Combination Rule C-1 (from SI-001):** When Implementation + AMS in same tender, include both S-38 and S-73 with distinct scope labels.

---

## Section Mapping Rules

### S-50 — Risk Register (Primary Output)
All risks appear in S-50 when triggered. S-50 is the primary section for all 40 canonical risks.

### S-37 — RAID Framework
S-37 appears as secondary for all risks. The RAID Framework references the risk register and links risks to assumptions and issues.

### S-38 — Change Control Process
S-38 appears as secondary for risks that relate directly to scope change or post-sign-off changes:
- RC-PROJ-001 (design not signed off before build)
- RC-PROJ-004 (configuration milestone changed)
- RC-TECH-003 (absence rules complexity — scope addition trigger)
- RC-TECH-004 (T&L complexity — scope addition trigger)
- RC-TECH-011 (career site complexity — scope addition trigger)
- RC-INT-002 (integration scope underestimated — scope addition trigger)
- RC-INT-007 (bespoke payroll mapping — scope addition trigger)
- RC-COMM-003 (integration method commitment — scope change risk)
- RC-CLIENT-007 (cross-functional alignment — change authority needed)
- RC-PROJ-003 (org design late — change control boundary)

### S-71 — SLA Framework
S-71 appears as secondary for operational risks:
- RC-OPS-001 (first live operational cycle — SLA governs hypercare)

### S-72 — Incident Management
S-72 appears as secondary for post-go-live operational risks:
- RC-OPS-001 (first live operational cycle)

### S-73 — AMS Change Request Management
S-73 appears as secondary for AMS-applicable risks (Pattern 13 only):
- RC-TECH-001 (quarterly SaaS update — change request trigger)
- RC-TECH-010 (digital channel complexity — change request trigger)
- RC-TECH-012 (annual SA legislative change — change request trigger)
- RC-INT-004 (payroll API version change — change request trigger)
- RC-COMM-002 (Help Desk vs Service Cloud — scope boundary)
- RC-CLIENT-006 (knowledge base ownership — AMS scope boundary)
- RC-OPS-001 (operational cycle risk — also applicable in AMS)

---

## Full Risk → Section → Pattern Mapping Table

| Risk ID | Risk Title | Primary Section | Secondary Sections | Patterns |
|---|---|---|---|---|
| RC-PROJ-001 | Module design not signed off before build | S-50 | S-37, S-38, S-12 | P1, P2, P3 |
| RC-PROJ-002 | Upstream phase not stable when dependent phase begins | S-50 | S-37, S-12 | P2 |
| RC-PROJ-003 | Organisational design decisions made late | S-50 | S-37, S-38, S-12 | P1, P2, P3 |
| RC-PROJ-004 | Configuration milestone changed after sign-off | S-50 | S-37, S-38, S-12 | P1, P2, P3, P7, P8, P9, P11 |
| RC-DATA-001 | Legacy HR data quality causes migration delays | S-50 | S-37, S-12 | P1, P2, P3 |
| RC-DATA-002 | Client content format incompatible with platform | S-50 | S-37, S-12 | P5, P1, P2 |
| RC-DATA-003 | HCM data quality produces invalid payroll input | S-50 | S-37, S-12 | P1, P2, P3 |
| RC-DATA-004 | Biometric enrolment data does not match HR records | S-50 | S-37, S-12 | P1, P2, P3 |
| RC-DATA-005 | Demand/scheduling data unavailable | S-50 | S-37, S-12 | P1, P2 |
| RC-INT-001 | Payroll integration timeline not aligned to HCM go-live | S-50 | S-37, S-12 | P1, P2, P3 |
| RC-INT-002 | Third-party integration scope underestimated | S-50 | S-37, S-38, S-12 | P1, P2, P3, P6, P7, P8, P11 |
| RC-INT-003 | Third-party API unavailable at integration build start | S-50 | S-37, S-12 | P3, P6, P7, P8, P9, P11 |
| RC-INT-004 | Payroll API version changes post-go-live | S-50 | S-37, S-12, S-73 | P3, P6, P13 |
| RC-INT-005 | Integration schedule not aligned to payroll cutoff | S-50 | S-37, S-12 | P1, P2, P3, P6 |
| RC-INT-006 | Integration field mapping errors produce incorrect data | S-50 | S-37, S-12 | P3, P6, P7, P8, P9, P11 |
| RC-INT-007 | Bespoke payroll mapping beyond standard patterns | S-50 | S-37, S-38, S-12 | P3, P11 |
| RC-TECH-001 | Quarterly SaaS update breaks configured functionality | S-50 | S-37, S-12, S-73 | P1, P2, P3, P4, P5, P6, P7, P8, P9, P13 |
| RC-TECH-002 | SETA/WSP/ATR extract complexity | S-50 | S-37, S-12 | P1, P2 |
| RC-TECH-003 | Absence rules complexity exceeds standard scope | S-50 | S-37, S-38, S-12 | P1, P2, P3 |
| RC-TECH-004 | Time and labour rules complexity exceeds estimate | S-50 | S-37, S-38, S-12 | P1, P2, P3 |
| RC-TECH-005 | BCEA overtime calculation requires additional config | S-50 | S-37, S-12 | P1, P2, P3 |
| RC-TECH-006 | OAX licensing not confirmed before commitment | S-50 | S-37, S-12 | P1, P2 |
| RC-TECH-007 | OAX data model not aligned to HCM configuration | S-50 | S-37, S-12 | P1, P2 |
| RC-TECH-008 | Oracle product licensing for dependent features not confirmed | S-50 | S-37, S-12 | P1, P2, P3, P7, P8, P9 |
| RC-TECH-009 | ODA scope added without separate license confirmation | S-50 | S-37, S-12 | P1, P2 |
| RC-TECH-010 | Digital channel complexity beyond standard configuration | S-50 | S-37, S-73, S-12 | P13 |
| RC-TECH-011 | Career site design complexity exceeds standard scope | S-50 | S-37, S-38, S-12 | P4, P1, P2 |
| RC-TECH-012 | Annual SA legislative change not reflected in integrations | S-50 | S-37, S-12, S-73 | P3, P6, P13 |
| RC-CLIENT-001 | Super-user availability insufficient during UAT | S-50 | S-37, S-12 | P1, P2, P3, P4, P5, P6, P7, P8, P9, P11 |
| RC-CLIENT-002 | Client prerequisite systems or accounts not available | S-50 | S-37, S-12 | P1, P2, P3, P7, P8, P9, P11 |
| RC-CLIENT-003 | Onboarding task and workflow ownership not defined | S-50 | S-37, S-12 | P1, P2, P4 |
| RC-CLIENT-004 | Learning catalog not ready at system go-live | S-50 | S-37, S-12 | P5, P1, P2 |
| RC-CLIENT-005 | Performance rating data unavailable for compensation cycle | S-50 | S-37, S-12 | P1, P2 |
| RC-CLIENT-006 | Knowledge base content ownership undefined | S-50 | S-37, S-73, S-12 | P13 |
| RC-CLIENT-007 | Cross-functional alignment on design frameworks | S-50 | S-37, S-38, S-12 | P1, P2, P3 |
| RC-COMM-001 | Analytics expectations misaligned with platform capability | S-50 | S-37, S-12 | P1, P2 |
| RC-COMM-002 | Oracle HR Help Desk conflated with Oracle Service Cloud | S-50 | S-37, S-73, S-12 | P13 |
| RC-COMM-003 | Integration method commitment in tender creates exposure | S-50 | S-37, S-38, S-12 | P3, P6, P11 |
| RC-OPS-001 | First live operational cycle high-stakes risk | S-50 | S-37, S-71, S-72, S-12 | P1, P2, P3, P4, P5, P7, P8, P9, P11, P13 |
| RC-COMP-001 | POPIA non-compliance in HR or payroll data handling | S-50 | S-37, S-12 | P1, P2, P3, P12, P13 |

---

## Pattern-Centric View

This view lists, for each pattern, which risks are applicable. Use this view during assembly to confirm the minimum risk register for a given tender.

### P1 — HCM Full Suite Single
Applicable risks (patterns include P1):
RC-PROJ-001, RC-PROJ-003, RC-PROJ-004, RC-DATA-001, RC-DATA-002, RC-DATA-003, RC-DATA-004, RC-DATA-005, RC-INT-001, RC-INT-002, RC-INT-005, RC-TECH-001, RC-TECH-002, RC-TECH-003, RC-TECH-004, RC-TECH-005, RC-TECH-006, RC-TECH-007, RC-TECH-008, RC-TECH-009, RC-TECH-011, RC-CLIENT-001, RC-CLIENT-002, RC-CLIENT-003, RC-CLIENT-004, RC-CLIENT-005, RC-CLIENT-007, RC-COMM-001, RC-OPS-001, RC-COMP-001

Minimum risk register (RISK_LIBRARY_STANDARD Section 7.2): Include at minimum 1 from RC-PROJ, 1 from RC-DATA or RC-INT, 1 from RC-CLIENT.

### P2 — HCM Full Suite Phased
All P1 risks plus:
RC-PROJ-002 (phased delivery risk — mandatory for P2)

### P3 — HCM + Payroll Integration
Applicable risks:
RC-PROJ-001, RC-PROJ-003, RC-PROJ-004, RC-DATA-001, RC-DATA-003, RC-DATA-004, RC-INT-001, RC-INT-002, RC-INT-003, RC-INT-004, RC-INT-005, RC-INT-006, RC-INT-007, RC-TECH-001, RC-TECH-003, RC-TECH-004, RC-TECH-005, RC-TECH-008, RC-TECH-012, RC-CLIENT-001, RC-CLIENT-002, RC-CLIENT-007, RC-COMM-003, RC-OPS-001, RC-COMP-001

### P4 — Recruiting Standalone
Applicable risks:
RC-TECH-001, RC-TECH-011, RC-CLIENT-001, RC-CLIENT-003, RC-OPS-001

### P5 — Learning Standalone
Applicable risks:
RC-DATA-002, RC-TECH-001, RC-CLIENT-001, RC-CLIENT-004, RC-OPS-001

### P6 — OIC Standalone
Applicable risks:
RC-INT-002, RC-INT-003, RC-INT-004, RC-INT-005, RC-INT-006, RC-TECH-001, RC-TECH-012, RC-CLIENT-001, RC-COMM-003, RC-OPS-001

### P7 — ERP Multi-Module
Applicable risks:
RC-PROJ-004, RC-INT-002, RC-INT-003, RC-INT-006, RC-TECH-001, RC-TECH-008, RC-CLIENT-001, RC-CLIENT-002, RC-OPS-001

### P8 — ERP Single Module
Same as P7 (subset of P7 risks applicable depending on module).

### P9 — EBS Implementation
Applicable risks:
RC-PROJ-004, RC-INT-003, RC-INT-006, RC-TECH-001, RC-TECH-008, RC-CLIENT-001, RC-CLIENT-002, RC-OPS-001

### P10 — DBA / Managed Services
No canonical risks applicable at this time. P10 is excluded from RC-OPS-001 (DBA engagements do not have a go-live). Risk coverage for P10 is a WP18B-EXT.2 gap item.

### P11 — Acumatica
Applicable risks:
RC-PROJ-004, RC-INT-002, RC-INT-003, RC-INT-006, RC-INT-007, RC-TECH-001, RC-CLIENT-001, RC-CLIENT-002, RC-COMM-003, RC-OPS-001

### P12 — BeBanking
Applicable risks:
RC-COMP-001

Note: BeBanking-specific risks (BB-INT, BB-PAY, BB-SEC) are not yet in the canonical risk register. This is a coverage gap for WP18B-EXT.2.

### P13 — AMS
Applicable risks:
RC-INT-004, RC-TECH-001, RC-TECH-010, RC-TECH-012, RC-CLIENT-006, RC-COMM-002, RC-OPS-001, RC-COMP-001

AMS minimum risk register: At minimum include RC-OPS-001, RC-TECH-001, and one RC-CLIENT or RC-COMM risk.

---

## S-50 Assembly Priority Order

Within S-50, risks should appear in this order (by assembly_priority, then by rating):

1. CRITICAL-rated risks with assembly_priority = Critical
2. HIGH-rated risks with assembly_priority = Critical
3. CRITICAL-rated risks with assembly_priority = High
4. HIGH-rated risks with assembly_priority = High
5. MEDIUM-rated risks with assembly_priority = Standard (alphabetically by RC-ID)
6. LOW-rated risks (alphabetically by RC-ID)

**CRITICAL + assembly_priority = Critical (must lead every applicable register):**
- RC-OPS-001
- RC-PROJ-003 (V1.0 recalculated)
- RC-DATA-001 (V1.0 recalculated)
- RC-DATA-003 (V1.0 recalculated)
- RC-DATA-004 (V1.0 recalculated)
- RC-TECH-003 (V1.0 recalculated)
- RC-TECH-006
- RC-TECH-008
- RC-TECH-012 (V1.0 recalculated)
- RC-CLIENT-004 (V1.0 recalculated)
- RC-CLIENT-007 (V1.0 recalculated)
- RC-COMM-001 (V1.0 recalculated)
- RC-COMM-002

Note: Several risks were recalculated from HIGH to CRITICAL in V1.0 based on observed frequency and impact on live projects. BU Lead should review these rating elevations during WP18B-EXT.2.
