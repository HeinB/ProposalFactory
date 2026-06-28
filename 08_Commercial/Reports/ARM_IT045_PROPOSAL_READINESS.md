---
document_id: ARM-IT045-PROPOSAL-READINESS
title: "ARM IT045 — Proposal Readiness Dashboard"
tender_id: "ARM IT045"
version: "1.0"
status: "WP18C Stage 5 Output"
created: "2026-06-25"
created_by: "WP18C — Proposal Factory Assembly Engine v1.0"
overall_readiness_pct: 67
qa_score: 72
submission_ready: false
blocking_gaps: 5
---

# ARM IT045 — Proposal Readiness Dashboard

**Stage 5 Output:** Machine-readable readiness assessment  
**Tender:** ARM IT045 | African Rainbow Minerals | Oracle EBS AMS  
**Assessment date:** 2026-06-25  
**Overall readiness:** 67% — NOT READY FOR SUBMISSION  
**QA score:** 72/100 (threshold: 75 — BELOW THRESHOLD)  
**Blocking items:** 5 (resolve before submission)

---

## 1. Overall Readiness Summary

```
PROPOSAL READINESS: ARM IT045
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall:          ████████████████████░░░░░░░░░░  67%
QA Score:         72/100  [THRESHOLD: 75]  ⚠ BELOW THRESHOLD
Submission:       ✗ NOT READY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 2. Readiness by Category

| Category | Sections | Ready | Partial | Gap | Readiness % | Status |
|---|---|---|---|---|---|---|
| Corporate and Partnership | 10 | 8 | 2 | 0 | 80% | AMBER |
| Understanding and Solution | 8 | 4 | 3 | 1 | 50% | AMBER |
| Scope and Governance | 7 | 5 | 2 | 0 | 71% | AMBER |
| People | 2 | 0 | 0 | 2 | 0% | **RED** |
| Commercial and Governance | 4 | 2 | 0 | 2 | 50% | **RED** |
| Compliance | 7 | 5 | 2 | 0 | 71% | AMBER |
| References | 2 | 0 | 2 | 0 | 0% | **RED** |
| AMS Support Sections | 7 | 6 | 1 | 0 | 86% | GREEN |
| Appendices | 5 | 1 | 2 | 2 | 20% | **RED** |
| **TOTAL** | **52** | **31** | **14** | **7** | **60%** | **RED** |

*(Note: Cover page + TOC counted separately; total section count including those = 57)*

---

## 3. Category Detail

### 3.1 Corporate and Partnership — 80% READY

```
S-01 Cover Page          ●● PARTIAL   Insert submission date + contact
S-02 Table of Contents   ●●●● READY
S-03 Company Overview    ●●●● READY   W1S1-001 DIRECT
S-04 Company History     ●●●● READY   W1S1-002 DIRECT
S-05 Awards              ●● PARTIAL   Extract award table from W1S1-006
S-06 Delivery Model      ●●●● READY   W1S1-007 DIRECT
S-07 Geographic Presence ●●●● READY   W1S1-008 DIRECT
S-08 Key Differentiators ●●●● READY   W1S1-009 DIRECT
S-09 Oracle Partnership  ●●●● READY   W1S1-003 DIRECT [BU: confirm OPN]
S-12 B-BBEE Statement    ●● PARTIAL   ⚠ Certificate expires 2026-07-31
```

### 3.2 Understanding and Solution — 50% AMBER

```
S-13 Executive Summary   ●● PARTIAL   AI-GENERATED — BU LEAD REVIEW REQUIRED
S-14 Understanding       ●● PARTIAL   AI-GENERATED — BU LEAD REVIEW REQUIRED
S-15 Proposed Solution   ●●●● READY   MERGE (W2S1-002 + W2S1-004 + W4-INT-001)
S-18 Oracle EBS          ●● PARTIAL   W2S1-002 vintage — verify stats
S-19 Oracle OIC          ●●●● READY   W4-INT-001 DIRECT
S-20 Oracle DBA          ●● PARTIAL   W2S1-003 — verify team size claims
S-21 Oracle MS           ●●●● READY   W2S1-004 EXTRACT
S-22 OCI Infrastructure  ○ GAP        No KB narrative asset — AI-generated proxy
```

### 3.3 Scope and Governance — 71% AMBER

```
S-30 Scope Inclusions    ●●●● READY   EXTRACT from 6 packs
S-31 Scope Exclusions    ●●●● READY   EXTRACT from 6 packs Section H
S-33 Dependencies        ●●●● READY   EXTRACT from 6 packs Section G
S-36 Project Governance  ●●●● READY   W2S1-005 EXTRACT
S-37 RAID Framework      ●● PARTIAL   Standard defined; no Risk Library entries
S-38 Change Control      ●●●● READY   AMS pack EXTRACT
S-45 Security Arch.      ●● PARTIAL   OCI pack proxy — validate against ARM's posture
```

### 3.4 People — 0% RED

```
S-46 Team Structure      ○ GAP        [PLACEHOLDER] BU Lead must confirm team
S-47 CVs                 ○ GAP        [PLACEHOLDER] APPTime only (ADR-001)
```

### 3.5 Commercial and Governance — 50% RED

```
S-49 Key Assumptions     ●●●● READY   WP17D-1 COMPLETE — 175 body assumptions
S-50 Risk Register       ○ GAP        AI-GENERATED — Risk Library empty; BU APPROVAL REQUIRED
S-51 Comm. Assumptions   ●●●● READY   WP17D-1 COMPLETE — 594 assumptions (appendix)
S-52 Commercials         ○ GAP        [PLACEHOLDER] Commercial Director required
```

### 3.6 Compliance — 71% AMBER

```
S-55 Compliance Schedule ●● PARTIAL   B-BBEE flag; all others current
S-56 Company Reg.        ●●●● READY   DIRECT
S-57 Tax Clearance       ●●●● READY   Valid 2027-02-23 DIRECT
S-58 Directors' Res.     ●●●● READY   Renewed 2026-06-15 DIRECT
S-59 B-BBEE Cert.        ●● PARTIAL   ⚠ EXPIRES 2026-07-31 FLAG
S-60 Public Liability    ●●●● READY   Renewed 2026-06-15 DIRECT
S-62 Oracle OPN Cert.    ●●●● READY   Level 1 DIRECT [confirm annual]
```

### 3.7 References — 0% RED

```
S-67 Client References   ●● PARTIAL   4 refs selected; AM approval pending; contacts missing
S-69 Reference Letters   ○ GAP        Letters not yet confirmed in KB directory
```

### 3.8 AMS Support Sections — 86% GREEN

```
S-70 Support Model       ●●●● READY   W2S1-004 + AMS MERGE
S-71 SLA Framework       ●●●● READY   EBS-SLA Overlay EXTRACT
S-72 Incident Mgmt       ●●●● READY   AMS pack EXTRACT
S-73 Change Request      ●●●● READY   AMS pack EXTRACT
S-74 Resource Model      ●● PARTIAL   Hours total confirmed; role split pending BU Lead
S-75 Release Mgmt        ●●●● READY   AMS pack EXTRACT
S-76 Monitoring          ●●●● READY   AMS pack EXTRACT
```

### 3.9 Appendices — 20% RED

```
A-01 Assumption Schedule ●●●● READY   WP17D-1 COMPLETE — ARM_IT045_ASSUMPTION_SCHEDULE_V1.md
A-02 CVs                 ○ GAP        [PLACEHOLDER] APPTime (ADR-001)
A-03 Reference Letters   ○ GAP        Physical letters required — AM to obtain
A-04 Certifications      ●● PARTIAL   Package required; all documents exist in KB
A-05 B-BBEE Certificate  ●● PARTIAL   ⚠ EXPIRES 2026-07-31 FLAG
```

---

## 4. Blocking Items (Must Resolve Before Submission)

These items will prevent proposal submission until resolved:

| # | Item | Section | Owner | Severity | Impact |
|---|---|---|---|---|---|
| **B1** | Named AMS team — resource confirmation | S-46, A-02 | BU Lead | BLOCKING | People section entirely empty without this |
| **B2** | Commercial pricing section | S-52 | Commercial Director | BLOCKING | Proposal has no price — client cannot evaluate |
| **B3** | Reference letters and AM approval for all 4 refs | S-67, A-03 | Account Manager | BLOCKING | Unconfirmed references create legal/relationship risk |
| **B4** | B-BBEE certificate renewal confirmation | S-12, S-59, A-05 | BU Lead | BLOCKING | Submission after 2026-07-31 with expired cert may disqualify |
| **B5** | Risk Register BU Lead approval (AI-generated content) | S-50 | BU Lead | BLOCKING | AI-generated risk register not approved for submission |

---

## 5. Non-Blocking Items (Resolve to Maximise QA Score)

| # | Item | Section | Owner | Priority | Impact on QA |
|---|---|---|---|---|---|
| N1 | Executive Summary personalisation | S-13 | BU Lead + AM | HIGH | +3 QA points |
| N2 | Understanding of Requirements review | S-14 | BU Lead + AM | HIGH | +2 QA points |
| N3 | OCI narrative (AI-generated) — write proper KB asset | S-22 | BU Lead | HIGH | +2 QA points; permanent KB value |
| N4 | EBS Capability modernisation (W2S1-002 vintage) | S-18 | BU Lead | MED | +1 QA point |
| N5 | Oracle DBA stats verification (W2S1-003) | S-20 | BU Lead | MED | +1 QA point |
| N6 | Awards and Recognition table extraction | S-05 | Bid Manager | LOW | +0.5 QA points |
| N7 | Cover page finalisation | S-01 | Bid Manager | LOW | Minor |
| N8 | Security architecture validation against ARM actual | S-45 | BU Lead | MED | Risk reduction |

---

## 6. Readiness Trajectory

| Action Batch | Owner | Actions | Projected QA After |
|---|---|---|---|
| Baseline (current) | — | — | 72/100 |
| Batch 1: Block resolve (B1–B5) | BU Lead + AM + Commercial | B1, B2, B3, B4, B5 | ~79/100 (SUBMITTABLE) |
| Batch 2: Non-block polish (N1–N8) | BU Lead + Bid Manager | N1–N8 | ~86/100 |
| Full governance sign-off | BU Lead | All items complete | ~88/100 |

**Minimum required:** Complete Batch 1 → QA score ≥ 75, no CRITICAL failures → SUBMITTABLE

---

## 7. Factory Automation Assessment

| Assembly Method | Sections | % of Total |
|---|---|---|
| DIRECT (fully deterministic — approved KB asset) | 22 | 38.6% |
| EXTRACT (deterministic — from approved source) | 19 | 33.3% |
| MERGE (deterministic — from multiple approved sources) | 3 | 5.3% |
| AI-GENERATE (AI-drafted; human review mandatory) | 8 | 14.0% |
| TEMPLATE (structure from standard; content from BU) | 3 | 5.3% |
| PLACEHOLDER (no automation; fully manual) | 2 | 3.5% |
| **Deterministic automation** (DIRECT + EXTRACT + MERGE) | **44** | **77.2%** |
| **Human-authored** (AI-GENERATE + TEMPLATE + PLACEHOLDER) | **13** | **22.8%** |

**Automation rate: 77.2% deterministic assembly**  
*(This means 44 of 57 sections were assembled from approved KB assets without AI generation or manual authoring. The 22.8% human-authored content represents AI-drafts needing review (14%), templates needing completion (5.3%), and permanent placeholders (3.5%).)*

---

## 8. Governance Flags Active

| Flag | Category | Section | Severity | Detail |
|---|---|---|---|---|
| FLAG-001 | Compliance | S-12, S-59, A-05 | CRITICAL | B-BBEE Level 3 certificate expires 2026-07-31 |
| FLAG-002 | Content | S-13, S-14, S-22, S-50 | HIGH | AI-generated content requires BU Lead approval before submission |
| FLAG-003 | People | S-46, S-47, A-02 | CRITICAL | CV/team section empty — APPTime sourcing required |
| FLAG-004 | Commercial | S-52 | CRITICAL | Pricing section empty — Commercial Director input required |
| FLAG-005 | References | S-67, A-03 | CRITICAL | Reference letters and AM approvals outstanding |
| FLAG-006 | OCI Gap | S-22 | HIGH | No standalone OCI capability narrative KB asset exists |
| FLAG-007 | Risk Library | S-50, S-37 | HIGH | Risk Library standard defined but not populated; Risk Register is AI-draft only |

---

*ARM_IT045_PROPOSAL_READINESS.md v1.0 | WP18C — Proposal Factory Assembly Engine v1.0 | 2026-06-25*  
*Stage 5 output. Overall readiness: 67%. QA: 72/100. Status: NOT READY FOR SUBMISSION. 5 blocking items outstanding.*
