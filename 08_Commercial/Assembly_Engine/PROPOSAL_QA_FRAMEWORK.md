---
document_id: PROPOSAL-QA-FRAMEWORK
title: "Proposal QA Framework — Proposal QA Engine Design"
version: "1.0"
status: "Approved — WP18A"
created: "2026-06-25"
created_by: "WP18A — Proposal Factory Architecture"
category: "Architecture / Engine Design"
scope: "Defines the design of the Proposal QA Engine (WP18D). Specifies all automated verification checks, the QA scorecard structure, scoring methodology, and the pass/fail thresholds that govern whether an assembled proposal can proceed to rendering."
---

# Proposal QA Framework

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18A — Proposal Factory Architecture  
**Governs:** WP18D — Proposal QA Engine  
**Position in pipeline:** PROPOSAL_ASSEMBLY_SEQUENCE.md Step 17

---

## 1. Purpose

The Proposal QA Engine is the final automated gate before BU Lead review and document rendering. It verifies that the assembled proposal:

1. Addresses every tender requirement
2. Contains every mandatory section
3. Has no duplicated content
4. Contains no contradictory statements
5. Uses correct assumption references
6. Uses correct capability references
7. Includes required certifications and compliance documents
8. Includes mandatory appendices
9. Scores above the minimum completeness threshold
10. Has an acceptable risk score
11. Passes readability checks
12. Has full assembly traceability

QA does not replace BU Lead review. It eliminates the manual verification checklist that a Bid Manager or BU Lead would otherwise have to perform item by item.

---

## 2. QA Check Categories

| Category | Code | Description |
|---|---|---|
| Requirements Coverage | QA-REQ | Has every tender requirement been addressed? |
| Structural Completeness | QA-STR | Are all mandatory sections present? |
| Content Integrity | QA-INT | No duplicated content; no contradictions; no prohibited content |
| Assembly Traceability | QA-TRC | All content traceable to approved KB sources |
| Assumption Quality | QA-ASS | Assumption schedule correct, complete, and properly referenced |
| Reference Quality | QA-REF | All references valid, approved, and appropriately cited |
| Compliance Completeness | QA-COMP | All required compliance documents present and current |
| Appendix Completeness | QA-APP | All mandatory appendices present and properly formatted |
| Commercial Protection | QA-COMM | Commercial section properly handled; no rate exposure |
| Governance | QA-GOV | All governance restrictions applied; no prohibited content |
| Readability | QA-READ | Word count, section length, formatting quality |
| Scoring Readiness | QA-SCORE | Proposal structure aligned with tender scoring criteria |

---

## 3. QA Checks — Requirements Coverage (QA-REQ)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-REQ-001 | Every mandatory requirement in the Requirement Matrix has been addressed in at least one proposal section | 100% mandatory requirements addressed | CRITICAL |
| QA-REQ-002 | Every addressed requirement is traceable to an approved KB source, an AI-generated section marked for review, or a `[GAP]` marker | All requirements have a disposition | HIGH |
| QA-REQ-003 | No proposal section claims to address a requirement that is not in the Requirement Matrix | Zero phantom requirements | MEDIUM |
| QA-REQ-004 | Requirements marked as scoring criteria have dedicated proposal content | All scored requirements have corresponding narrative | HIGH |
| QA-REQ-005 | Compliance requirements are each addressed in the Compliance section | 100% compliance requirements addressed | CRITICAL |

---

## 4. QA Checks — Structural Completeness (QA-STR)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-STR-001 | Company Overview section present | Yes | CRITICAL |
| QA-STR-002 | Proposed Solution section present | Yes | CRITICAL |
| QA-STR-003 | Understanding of Requirements section present | Yes | CRITICAL |
| QA-STR-004 | Implementation Methodology present (if fixed-price) | Yes | CRITICAL |
| QA-STR-005 | Project Plan present (if fixed-price) | Yes | HIGH |
| QA-STR-006 | Team Structure section present | Yes | HIGH |
| QA-STR-007 | Client References section present | Yes | HIGH |
| QA-STR-008 | Key Assumptions body section present (if fixed-price) | Yes | CRITICAL |
| QA-STR-009 | Scope Exclusions section present (if fixed-price) | Yes | HIGH |
| QA-STR-010 | Commercial / Pricing section present (even if placeholder) | Yes | CRITICAL |
| QA-STR-011 | Compliance section present | Yes | CRITICAL |
| QA-STR-012 | Complete Assumption Schedule (Appendix) present (if fixed-price) | Yes | CRITICAL |
| QA-STR-013 | All `[GAP]` markers have severity classification | Yes | HIGH |
| QA-STR-014 | All `[PLACEHOLDER]` markers have owner assigned | Yes | HIGH |

---

## 5. QA Checks — Content Integrity (QA-INT)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-INT-001 | No section duplicates another section (same heading appears twice) | Zero duplicate headings | HIGH |
| QA-INT-002 | No verbatim paragraph appears in more than one section | Zero verbatim paragraph duplication | MEDIUM |
| QA-INT-003 | No contradictory statements between Scope Inclusions and Scope Exclusions | Zero contradictions | CRITICAL |
| QA-INT-004 | No contradictory statements between Methodology and Project Plan | Zero contradictions | HIGH |
| QA-INT-005 | No contradictory statements between Assumptions and Proposed Solution | Zero contradictions | HIGH |
| QA-INT-006 | No prohibited client names (DFA, CCBA, SAA) appear anywhere in the document | Zero prohibited names | CRITICAL |
| QA-INT-007 | No expired Oracle Gold Partner claim | "Gold Partner" absent | CRITICAL |
| QA-INT-008 | No unapproved geography claims | Only approved geos | HIGH |
| QA-INT-009 | Headcount expressed as "more than 50 Senior Consultants" only | Correct phrasing | HIGH |
| QA-INT-010 | Section 14.2 (W3S1-008) absent from external document | Absent | CRITICAL |
| QA-INT-011 | Section 13.2 (W3S1-009) absent from external document | Absent | CRITICAL |
| QA-INT-012 | HIST-018 billing figure (R825,170) absent | Absent | CRITICAL |
| QA-INT-013 | No actual rate card values or margin thresholds | Absent | CRITICAL |
| QA-INT-014 | No BEE Level cited if certificate expired | Absent or valid cert confirmed | CRITICAL |
| QA-INT-015 | W4-HCM-004 (T&L) not cited as standalone capability | Absent | HIGH |
| QA-INT-016 | BeBanking SAP claim uses "integrates with SAP environments" only | Correct phrasing | HIGH |

---

## 6. QA Checks — Assembly Traceability (QA-TRC)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-TRC-001 | Every capability claim traces to an asset in MASTER_CAPABILITY_INDEX | 100% traceable | HIGH |
| QA-TRC-002 | Every assumption reference traces to an ID in the Assembly Audit Report | 100% traceable | CRITICAL |
| QA-TRC-003 | Assembly Audit Report produced and filed | Yes | HIGH |
| QA-TRC-004 | Capability Selection List filed for this tender | Yes | HIGH |
| QA-TRC-005 | Reference Selection List filed | Yes | HIGH |
| QA-TRC-006 | Methodology Selection filed | Yes | MEDIUM |
| QA-TRC-007 | Gap Register filed (even if zero gaps) | Yes | HIGH |

---

## 7. QA Checks — Assumption Quality (QA-ASS)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-ASS-001 | Assumption Schedule count in body section (KEY_ASSUMPTIONS) matches Assembly Engine output | Exact match | CRITICAL |
| QA-ASS-002 | Assumption Schedule count in appendix (ASSUMPTION_SCHEDULE) matches Assembly Engine output | Exact match | CRITICAL |
| QA-ASS-003 | Numbering in body and appendix are consistent — same assumption has same number | 100% consistent | CRITICAL |
| QA-ASS-004 | All suppressed assumptions absent from both outputs | 6 known suppressions absent (ARM IT045 pattern) | CRITICAL |
| QA-ASS-005 | All -EXC- and -EXT- assumptions present in body Section 4 (Explicit Exclusions) | 100% present | CRITICAL |
| QA-ASS-006 | All -CUS-, -CON-, -DEP- assumptions present in body Section 3 (Client Responsibilities) | 100% present | CRITICAL |
| QA-ASS-007 | Standard commercial preamble present in appendix | Yes | HIGH |
| QA-ASS-008 | Legal linkage statement present in body section | Yes | HIGH |
| QA-ASS-009 | All Ref IDs in `*(Ref: PACK-SECTION-NNN)*` format | 100% | HIGH |
| QA-ASS-010 | No pack names or internal metadata in client-facing outputs | Absent | HIGH |

---

## 8. QA Checks — Reference Quality (QA-REF)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-REF-001 | All cited references are in REFERENCE_MASTER.csv | 100% registered | CRITICAL |
| QA-REF-002 | AM approval recorded for all named clients | Yes | CRITICAL |
| QA-REF-003 | No archived/excluded references cited (DFA, CCBA, SAA, Redpath) | Zero prohibited citations | CRITICAL |
| QA-REF-004 | Reference letters are signed PDFs in `04_References/` | All present | HIGH |
| QA-REF-005 | Reference letters cited are relevant to the proposal platform / sector | Relevance confirmed | MEDIUM |

---

## 9. QA Checks — Compliance Completeness (QA-COMP)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-COMP-001 | B-BBEE certificate present and valid at submission date | Valid | CRITICAL |
| QA-COMP-002 | Tax Clearance valid at submission date | Valid (current to 2027-02-23) | CRITICAL |
| QA-COMP-003 | Directors' Resolution valid at submission date | Valid (renewed 2026-06-15) | CRITICAL |
| QA-COMP-004 | Public Liability Insurance valid at submission date | Valid | HIGH |
| QA-COMP-005 | Oracle OPN certificate present (if Oracle tender) | Present | HIGH |
| QA-COMP-006 | Acumatica Partner Certificate present (if Acumatica tender) | Present (or gap flagged) | HIGH |
| QA-COMP-007 | All compliance items in COMPLIANCE_REGISTER.csv checked against submission date | All checked | HIGH |

---

## 10. QA Checks — Appendix Completeness (QA-APP)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-APP-001 | Complete Assumption Schedule appendix present (if fixed-price) | Yes | CRITICAL |
| QA-APP-002 | CV appendix placeholder present with APPTime instruction | Yes | HIGH |
| QA-APP-003 | All referenced compliance documents attached as appendices | Yes | HIGH |
| QA-APP-004 | B-BBEE certificate attached | Yes | CRITICAL |
| QA-APP-005 | Appendices in correct sequence (per PROPOSAL_STRUCTURE_LIBRARY.md) | Yes | MEDIUM |

---

## 11. QA Checks — Commercial Protection (QA-COMM)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-COMM-001 | Pricing section is `[PLACEHOLDER — COMMERCIAL INPUT REQUIRED]` or populated by CD | Yes | CRITICAL |
| QA-COMM-002 | No rate card values appear in any client-facing section | Absent | CRITICAL |
| QA-COMM-003 | No margin floor or discount figures appear | Absent | CRITICAL |
| QA-COMM-004 | Fixed-price engagement has complete commercial file in `08_Commercial/` | Present | CRITICAL |
| QA-COMM-005 | AMS pricing statement consistent with AMS assumption pack language | Consistent | HIGH |

---

## 12. QA Checks — Readability (QA-READ)

| Check ID | Check | Pass Condition | Severity |
|---|---|---|---|
| QA-READ-001 | Executive Summary ≤ 2 pages | ≤ 1,500 words | MEDIUM |
| QA-READ-002 | Total proposal body (excl. appendices) ≤ 100 pages | ≤ 75,000 words | LOW |
| QA-READ-003 | All sections have headings | Yes | MEDIUM |
| QA-READ-004 | No section heading is a duplicate | Yes | HIGH |
| QA-READ-005 | Tender ID and client name correctly referenced throughout | Yes | MEDIUM |
| QA-READ-006 | No raw internal document IDs (e.g., W1S1-001) visible in client-facing sections | Absent | HIGH |
| QA-READ-007 | No AI-generated content markers (`[AI-GENERATED]`) left in final document | Absent | HIGH |
| QA-READ-008 | Version number present in document header | Yes | LOW |

---

## 13. QA Scorecard

The QA scorecard aggregates check results into a total score and sub-scores per category.

### 13.1 Scoring method

- CRITICAL check: 10 points each. FAIL = 0 points. PASS = 10 points.
- HIGH check: 5 points each. FAIL = 0 points. PASS = 5 points.
- MEDIUM check: 2 points each. FAIL = 0 points. PASS = 2 points.
- LOW check: 1 point each. FAIL = 0 points. PASS = 1 point.

### 13.2 Scorecard structure

| Category | CRITICAL | HIGH | MEDIUM | LOW | Max Score |
|---|---|---|---|---|---|
| QA-REQ Requirements Coverage | 2 | 2 | 1 | 0 | 30 |
| QA-STR Structural Completeness | 6 | 4 | 2 | 0 | 90 |
| QA-INT Content Integrity | 7 | 5 | 3 | 0 | 100 |
| QA-TRC Assembly Traceability | 2 | 4 | 1 | 0 | 50 |
| QA-ASS Assumption Quality | 8 | 2 | 0 | 0 | 90 |
| QA-REF Reference Quality | 3 | 2 | 1 | 0 | 50 |
| QA-COMP Compliance Completeness | 3 | 4 | 0 | 0 | 50 |
| QA-APP Appendix Completeness | 2 | 2 | 1 | 0 | 40 |
| QA-COMM Commercial Protection | 4 | 1 | 0 | 0 | 45 |
| QA-GOV (embedded in QA-INT) | — | — | — | — | — |
| QA-READ Readability | 0 | 2 | 3 | 3 | 19 |
| QA-SCORE Scoring Readiness | 0 | 1 | 0 | 0 | 5 |
| **TOTAL** | | | | | **~569** |

*Note: exact max score depends on total check count. Scoring formula normalises to 100.*

### 13.3 Normalised score and thresholds

```
Normalised Score = (Points Earned / Maximum Possible Points) × 100
```

| Score | Status | Action |
|---|---|---|
| 95–100 | **EXCELLENT** | Proceed to rendering |
| 85–94 | **GOOD** | Proceed to rendering; review findings |
| 75–84 | **ACCEPTABLE** | BU Lead review of all FAIL items before rendering |
| 60–74 | **REQUIRES REWORK** | Do not render; resolve FAIL items first |
| < 60 | **NOT SUBMISSION READY** | Halt; BU Lead must assess blocking issues |

**Minimum threshold to proceed to rendering: 75 (with no CRITICAL fails)**

**Any single CRITICAL fail blocks rendering regardless of overall score.**

---

## 14. QA Report Format

The engine produces `[TENDER_ID]_QA_REPORT.md` in `09_Active_Tenders/[TENDER_ID]/`:

```
QA REPORT — [TENDER_ID]
Date: [date]
Assembled by: [assembly method / operator]
QA Engine version: [version]

SUMMARY
━━━━━━━
Normalised Score: [N]/100
Status: [EXCELLENT / GOOD / ACCEPTABLE / REQUIRES REWORK / NOT SUBMISSION READY]
CRITICAL fails: [N]
HIGH fails: [N]
MEDIUM fails: [N]
LOW fails: [N]
Blocking issues: [N]

CRITICAL FINDINGS
━━━━━━━━━━━━━━━━
[List all CRITICAL fails with check ID, description, remediation required]

HIGH FINDINGS
━━━━━━━━━━━━━
[List all HIGH fails]

MEDIUM AND LOW FINDINGS
━━━━━━━━━━━━━━━━━━━━━━━
[Summary table]

DETAILED CHECK RESULTS
━━━━━━━━━━━━━━━━━━━━━━
[Full table: Check ID | Check | Result | Score | Notes]
```

---

## 15. QA Engine — Interim Operation

Until WP18D is built, QA is performed manually by the Bid Manager using this framework as a checklist. The Bid Manager:

1. Runs through each check in Sections 3–12 above
2. Records PASS / FAIL / N/A for each check
3. Calculates normalised score
4. Presents QA Report to BU Lead before submission
5. Resolves all CRITICAL failures before proceeding

The manual QA checklist uses the same check IDs and the same scoring method as the engine specification above, ensuring that when the engine is built (WP18D), the transition is seamless.

---

*PROPOSAL_QA_FRAMEWORK.md v1.0 | WP18A — Proposal Factory Architecture | 2026-06-25*  
*Design specification for WP18D — Proposal QA Engine. Minimum score to render: 75 / no CRITICAL fails.*
