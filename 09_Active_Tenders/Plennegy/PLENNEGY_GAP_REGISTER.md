---
document_id: PLENNEGY-GAP-REGISTER
title: "Plennegy — Gap Register"
version: "1.0"
created: "2026-06-30"
work_package: "PF2-006"
---

# Plennegy — Gap Register

**Tender:** PLENNEGY-HCM-001 — Oracle HCM Full Suite Implementation
**Date:** 2026-06-30

---

## A. Knowledge Gaps

| Code | Gap | Impact | Recommendation |
|---|---|---|---|
| KG-001 | Oracle Recruiting Booster — no KB asset | S-16 HCM Capability section cannot render Booster-specific content | Add to Wave 5 backlog; describe at high level using Oracle product documentation; flag as "Tier 3 — external source" |
| KG-002 | Oracle Touch Points — no KB asset | S-16 HCM Capability section cannot render Touch Points content | Add to Wave 5 backlog; brief mention only in current proposal |
| KG-003 | No Agribusiness/FMCG sector client reference | Reference coverage score reduced (~40–58% depending on Hollywood Bets approval) | Accept for this tender; no governed agribusiness reference exists |
| KG-004 | No Oracle Fusion HCM signed production reference | Strongest reference gap; Hollywood Bets is closest but unsigned | OAR-C01 resolution is highest priority reference action |

---

## B. Data Quality Issues

| Code | Issue | Impact | Recommendation |
|---|---|---|---|
| DQ-001 | S-36 Project Governance: EXTRACT method includes full W2S1-005 body | Proposal reviewer must manually extract project governance sub-sections from methodology | Lower priority; bid manager to curate S-36 from rendered content |

---

## C. Platform Defects (Fixed in PF2-006)

| Code | Defect | Fix Applied | Status |
|---|---|---|---|
| C-PSAE-001 | PSAE had no `--context` flag; production tenders could not be processed without source code modification | Added `--context YAML_FILE` flag to `proposal_section_engine.py` | FIXED |
| C-RENDERER-001 | S-49/S-51/A-01 `DIRECT` method silently dropped assumption packs 2–N when multiple packs selected | Changed assembly_method from `DIRECT` to `MERGE` for S-49, S-51, A-01 in PSAE SECTION_DEFS | FIXED |

---

## D. Tender-specific Requirements (Human Input Required)

| Code | Requirement | Section | Notes |
|---|---|---|---|
| TR-001 | Scope of Work — Inclusions | S-30 | Requires Plennegy-specific scope confirmed by AM and client |
| TR-002 | Scope of Work — Exclusions | S-31 | Requires confirmation of what is NOT in scope |
| TR-003 | Deliverables list | S-32 | Module-specific deliverables to be confirmed |
| TR-004 | Dependencies | S-33 | Client-side dependencies (data access, steering committee, payroll system access) |
| TR-005 | Executive Summary | S-13 | Win themes, Plennegy-specific context, sector acknowledgement |
| TR-006 | Understanding of Requirements | S-14 | Drawn from RFP/RFQ document; tender-specific |
| TR-007 | Proposed Solution Overview | S-15 | High-level solution narrative; Plennegy-specific |
| TR-008 | RAID Framework | S-37 | Plennegy-specific risks, assumptions, issues, dependencies |
| TR-009 | Change Control Framework | S-38 | Confirm change threshold with BU Lead |
| TR-010 | Cutover / Go-Live Plan | S-42 | Wave go-live dates pending OAR-C04 |
| TR-011 | Workforce Compensation excluded | — | G-001 applies; if Plennegy requests this, requires BU Lead governance decision |

---

## E. Human Commercial Decisions Required

| Code | Decision | Owner | OAR Reference | Status |
|---|---|---|---|---|
| HC-001 | Hollywood Bets AM approval for naming in proposal | Oracle BU Lead / AM | OAR-C01 | OPEN |
| HC-002 | Costing / commercial section complete | Commercial Director + BU Lead | OAR-C02 | OPEN |
| HC-003 | B-BBEE certificate renewal before submission | Finance Director | OAR-A01 | URGENT — expires 2026-07-31 |
| HC-004 | Confirm Plennegy parameters (LE count, headcount, payroll cycle, go-live date) | Account Manager | OAR-C04 | OPEN |
| HC-005 | Oracle awards wording verification | Oracle HCM BU Lead | OAR-C05 | OPEN |

---

*PLENNEGY_GAP_REGISTER v1.0 | PF2-006 | 2026-06-30*
