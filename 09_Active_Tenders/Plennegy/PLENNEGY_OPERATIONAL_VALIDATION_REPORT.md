---
document_id: PLENNEGY-OPERATIONAL-VALIDATION-REPORT
title: "PF2-006 — Operational Validation Report: Plennegy Oracle HCM Full Suite"
version: "1.0"
status: "COMPLETE"
created: "2026-06-30"
work_package: "PF2-006"
platform_maturity_before: "L5.6"
platform_maturity_after: "L5.7"
---

# PF2-006 — Operational Validation Report: Plennegy Oracle HCM Full Suite

**Date:** 2026-06-30
**Tender:** PLENNEGY-HCM-001 — Plennegy Oracle HCM Full Suite Implementation
**BOM:** TENDER_BOM_LIBRARY.md BOM 1 (Oracle HCM Full Suite); Pattern P1

---

## 1. Executive Summary

The first live operational validation of the Proposal Factory was executed against the Plennegy Oracle HCM Full Suite tender. The complete pipeline (PSAE → Renderer) executed successfully in under 1 second of compute time, producing an 11,066-line governed proposal draft with:

- **2 Platform Defects discovered and fixed** (C-PSAE-001, C-RENDERER-001)
- **RENDERED=21 / PLACEHOLDER=18 / AI-DRAFT=3 / NOT_FOUND=0**
- **5 assumption packs** fully rendered in assumption schedule
- **All governance rules correctly applied** (G-001 Workforce Compensation excluded for Agribusiness)
- **6/6 regression tests PASS** after all fixes

**Overall Operational Readiness Score: 71/100** (see Section 9)

---

## 2. BOM Analysis and Tender Classification

### 2.1 BOM Source Selection

The `09_Active_Tenders/Plennegy/` folder was empty on session start. BOM information was located in:
1. `99_Archive/Plennegy/PLENNEGY_ASSEMBLY_TEST.md` — primary BOM (WP12, 2026-06-16)
2. `99_Archive/Plennegy/PLENNEGY_READINESS_SCORECARD.md` — readiness baseline
3. `08_Commercial/Assembly_Engine/TENDER_BOM_LIBRARY.md` — BOM 1 (Oracle HCM Full Suite)

**Selection rationale:** PLENNEGY_ASSEMBLY_TEST.md is the authoritative BOM document produced by the WP12 assembly test. It pre-identifies all assets, assumption packs, references, and governance restrictions. BOM 1 (Oracle HCM Full Suite) was confirmed as the correct BOM.

### 2.2 Engagement Classification

| Parameter | Value | Governance Impact |
|---|---|---|
| Client | Plennegy Pty Ltd | — |
| Sector | Agribusiness / Agricultural Holdings | G-001 applies: Compensation EXCLUDED |
| Platform | Oracle HCM Cloud | Oracle Partnership section mandatory |
| Engagement type | Implementation | AMS sections excluded |
| Pattern | P1 | Standard implementation ordering |
| Modules | 9 (7 governable + 2 KB gaps) | See §3 |
| OIC integration | Yes (payroll_integration=true) | OIC pack OPTIONAL_SELECTED |
| AMS | Not in scope | — |

---

## 3. Asset Selection Results

### 3.1 Capability Asset Selection

| Asset | Name | AREL Result | Notes |
|---|---|---|---|
| W1S1-001 | Company Overview | MANDATORY | Corporate block |
| W1S1-002 | Company History | MANDATORY | Corporate block |
| W1S1-003 | Oracle Partnership | MANDATORY | Oracle platform |
| W1S1-006 | Awards and Recognition | MANDATORY | Corporate block |
| W1S1-007 | Delivery Model | MANDATORY | Corporate block |
| W1S1-008 | Geographic Presence | MANDATORY | Corporate block |
| W1S1-009 | Key Differentiators | MANDATORY | Corporate block |
| W2S1-001 | Oracle Fusion Capability | OPTIONAL_SELECTED | ERP Fusion driver |
| W2S1-005 | Oracle Implementation Methodology | MANDATORY | Oracle Implementation |
| W3S1-001 | HCM Core | MANDATORY | Platform=Oracle HCM Cloud |
| W3S1-002 | Talent Management | MANDATORY | Module in scope |
| W3S1-003 | Recruiting Cloud | MANDATORY | Module in scope |
| W3S1-004 | Learning Cloud | MANDATORY | Module in scope |
| **W3S1-005** | **Workforce Compensation** | **EXCLUDED** | **G-001: industry ≠ Mining** |
| W3S1-006 | HCM Analytics | OPTIONAL_SELECTED | Oracle HCM platform |
| W3S1-007 | Workforce Management (Absence) | MANDATORY | Platform=Oracle HCM Cloud |
| W3S1-008 | HR Help Desk | OPTIONAL_SELECTED | Not in primary scope |
| W3S1-009 | Payroll Interface (OIC ↔ PaySpace) | MANDATORY | payroll_integration=true |
| W4-AI-002 | Oracle AI Skills | MANDATORY | Module in scope |
| W4-HCM-002 | Oracle Journeys | MANDATORY | Platform=Oracle HCM Cloud |
| W4-INT-001 | OIC Accelerators | OPTIONAL_SELECTED | integration_scope=true |

**G-001 applied correctly:** W3S1-005 excluded because `industry == "Agribusiness"` — not Mining. This is the correct governance outcome.

### 3.2 Assumption Pack Selection

| Pack | AREL Result | Rendered In |
|---|---|---|
| HCM-BASE-ASSUMPTIONS-V1 | MANDATORY | S-49, S-51, A-01 |
| HCM-RECRUITING-ASSUMPTIONS-V1 | MANDATORY | S-49, S-51, A-01 |
| HCM-LEARNING-ASSUMPTIONS-V1 | MANDATORY | S-49, S-51, A-01 |
| HCM-TALENT-ASSUMPTIONS-V1 | MANDATORY | S-49, S-51, A-01 |
| HCM-COMPENSATION-ASSUMPTIONS-V1 | EXCLUDED (G-001) | — |
| OIC-ASSUMPTIONS-V1 | OPTIONAL_SELECTED | S-49, S-51, A-01 |
| AMS-ASSUMPTIONS-V1 | EXCLUDED (not AMS) | — |

**5 assumption packs rendered** (HCM Base + Recruiting + Learning + Talent + OIC)

---

## 4. Platform Defects Discovered and Fixed

### C-PSAE-001: No `--context` flag for production tender input

**Discovery:** PSAE had no CLI mechanism to process a tender from a YAML context file. The `--manifest` flag only worked for hardcoded `REGRESSION_CONTEXTS`. This blocked all production use — any real tender required either modifying source code or embedding tender logic in `REGRESSION_CONTEXTS`.

**Fix:** Added `--context YAML_FILE` flag to `proposal_section_engine.py` CLI. Loads `tender_context:` wrapper from YAML, normalises `pattern` → `tender_pattern`, calls `build_section_manifest()`, writes manifest to `Proposals/[TENDER_ID]/`. Generalises to all future tenders.

**Parallel:** The KVE already had `--context` for assembly mode. PSAE now has parity.

**Impact:** All future production tenders can be processed by creating a `tender_context_[TENDER].yaml` file. No source code modification required.

### C-RENDERER-001: S-49/S-51/A-01 `DIRECT` method silently drops assumption packs 2–N

**Discovery:** S-49 (Key Assumptions), S-51 (Commercial Assumptions), and A-01 (Assumption Schedule) were defined with `assembly_method: DIRECT` in the PSAE SECTION_DEFS. The renderer's `_render_direct()` uses only `source_assets[0]`. For the Plennegy context, 5 packs were selected as source assets — but only HCM-BASE was rendered. The other 4 packs (Recruiting, Learning, Talent, OIC) were silently dropped.

**Why hidden in regression:** The ARM-IT045 regression (EBS AMS) has only one ASP pack selected (AMS-ASSUMPTIONS-V1) for S-49/S-51/A-01 → DIRECT with one asset worked correctly. All other regression tenders were not observed to fail because their assumption audit output was not scrutinised at the per-asset level.

**Fix:** Changed `assembly_method` from `"DIRECT"` to `"MERGE"` for S-49, S-51, and A-01 in PSAE SECTION_DEFS. `MERGE` iterates all `source_assets` and concatenates them in selection order. **Verified:** All 5 packs now appear in Plennegy S-49, S-51, A-01. All 6 regression tests continue to PASS.

**Impact:** Every multi-pack HCM tender (Recruiting + Learning + Talent + OIC combinations) now renders complete assumption schedules. This is a high-impact fix — without it, 4 of 5 packs were silently omitted from every assumption section.

---

## 5. Issues Classified (Non-Platform-Defect)

| Code | Issue | Type | Description |
|---|---|---|---|
| KG-001 | Oracle Recruiting Booster | A. Knowledge Gap | No KB asset; describe at high level using Oracle documentation only |
| KG-002 | Oracle Touch Points | A. Knowledge Gap | No KB asset; brief mention only; Wave 5 backlog |
| KG-003 | No Agribusiness sector reference | A. Knowledge Gap | No client reference in KB for Agribusiness/FMCG sector |
| KG-004 | No Oracle Fusion HCM signed reference | A. Knowledge Gap | Hollywood Bets is closest but no signed letter |
| HC-001 | OAR-C01 — Hollywood Bets AM approval | E. Human Commercial Decision | Must resolve before naming HB in submission |
| HC-002 | OAR-C02 — Costing section | E. Human Commercial Decision | Commercial Director authority; rendered as PLACEHOLDER |
| HC-003 | OAR-A01 — B-BBEE certificate renewal | E. Human Commercial Decision | Expires 2026-07-31; URGENT |
| HC-004 | OAR-C04 — Client parameters | E. Human Commercial Decision | Entity count, payroll cycle, go-live date from AM |
| TR-001 | S-30–S-33 Scope sections PLACEHOLDER | D. Tender-specific Requirement | Scope inclusions/exclusions/deliverables/dependencies are always bespoke |
| TR-002 | S-13 Executive Summary AI-DRAFT | D. Tender-specific Requirement | Win themes and client-specific context always bespoke |
| TR-003 | W3S1-005 excluded by G-001 | D. Tender-specific Requirement | Agribusiness ≠ Mining; governance correctly applied; accept score impact |
| DQ-001 | S-36 Project Governance: full W2S1-005 body included | B. Data Quality Issue | EXTRACT method doesn't sub-section; full methodology included; manual curation required |

---

## 6. Proposal Completeness Assessment

### 6.1 Section Coverage (42 sections in assembly sequence)

| Status | Count | % |
|---|---|---|
| RENDERED | 21 | 50% |
| PLACEHOLDER | 18 | 43% |
| AI-DRAFT | 3 | 7% |
| NOT_FOUND | 0 | 0% |

### 6.2 Placeholder Decomposition

| Category | Count | Explanation |
|---|---|---|
| Bespoke scope sections | 4 | S-30/31/32/33 — always human-authored |
| Compliance documents | 6 | S-55–S-60 — physical documents, not KB content |
| Commercial / pricing | 2 | S-52 + S-37 — Commercial Director authority |
| Cover + template sections | 3 | S-01, S-35, S-46 — tender-specific fields |
| Bespoke content | 3 | S-12, S-15, S-38, A-04, A-05 |

**Assessment:** All PLACEHOLDER sections are correctly classified — they represent genuinely bespoke or physically-supplied content that is not automatable from the KB. 0 placeholders are caused by missing KB content.

### 6.3 Capability Coverage

| Capability Area | Status | Asset |
|---|---|---|
| Corporate / Company Profile | RENDERED | W1S1-001/002/006/007/008/009 |
| Oracle Partnership | RENDERED | W1S1-003 |
| Implementation Methodology | RENDERED | W2S1-005 |
| HCM Core + Absence | RENDERED | W3S1-001, W3S1-007 |
| Talent Management | RENDERED | W3S1-002 |
| Recruiting Cloud | RENDERED | W3S1-003 |
| Learning Cloud | RENDERED | W3S1-004 |
| AI Skills | RENDERED | W4-AI-002 |
| Journeys / Onboarding | RENDERED | W4-HCM-002 |
| Payroll Interface (OIC) | RENDERED | W3S1-009 |
| Workforce Compensation | EXCLUDED — G-001 | W3S1-005 (Agribusiness ≠ Mining) |
| Recruiting Booster | KNOWLEDGE GAP | No KB asset |
| Touch Points | KNOWLEDGE GAP | No KB asset |

**Coverage: 9/11 capability areas covered (82%).** The 2 uncovered areas (Recruiting Booster, Touch Points) were pre-identified as Wave 5 backlog items in WP12.

### 6.4 Assumption Coverage

**5/7 applicable packs fully rendered** (HCM Base + Recruiting + Learning + Talent + OIC).
Compensation excluded by governance (G-001). AMS excluded (not AMS engagement).

### 6.5 Risk Coverage

Risk register section (S-50) is `AI-DRAFT` — requires human authoring. The Enterprise Risk Register (WP18B-EXT.2) provides the risk library. 40 approved risks available.

---

## 7. Execution Metrics

| Metric | Value |
|---|---|
| Pipeline execution time | < 1 second total |
| PSAE execution | 0.53s |
| Renderer execution | 0.22s |
| Rendered proposal size | 11,066 lines |
| Sections in assembly sequence | 42 |
| Mandatory sections | 41 |
| Optional sections | 1 |
| Excluded sections | 40 (18 explicit + 22 default) |
| NOT_FOUND assets | 0 |
| Platform defects discovered | 2 |
| Platform defects fixed | 2 |
| Regression suite after fixes | 6/6 PASS |
| Governance violations | 0 |

---

## 8. Deterministic Behaviour Verification

The platform is fully deterministic. Running PSAE + Renderer twice in sequence produces byte-identical output except for the `generated_at` timestamp in the manifest header. All section selections, asset lookups, and render methods are deterministic given the same tender context. This was confirmed by running the full pipeline twice.

---

## 9. Operational Readiness Score

| Dimension | Score | Notes |
|---|---|---|
| Capability coverage | 17/20 | 82% — 9/11 areas; 2 Wave 5 gaps |
| Assumption coverage | 18/20 | 5/7 applicable packs; governance correctly excludes 2 |
| Pipeline correctness | 20/20 | 0 NOT_FOUND; 0 governance violations; deterministic |
| Platform defects | 14/20 | 2 defects found and fixed (C-PSAE-001, C-RENDERER-001) |
| Human action burden | 9/20 | 5 open human actions (OAR-C01/C02/A01/C04/C05); normal for a live tender |
| **TOTAL** | **78/100** | **CONDITIONALLY READY** |

**Score interpretation:** 78/100 reflects a platform that works correctly but surfaces 5 human blockers before submission. These blockers (costing, BEE renewal, client parameters, AM approval) are correct outcomes — they represent genuine human decisions, not platform failures.

---

## 10. Recommendations

| Priority | Recommendation | Type |
|---|---|---|
| 1 | OAR-A01: B-BBEE renewal by 2026-07-31 | Human — URGENT |
| 2 | OAR-C01: Hollywood Bets AM approval | Human |
| 3 | OAR-C02: Initiate costing input with Commercial Director | Human |
| 4 | Add Oracle Recruiting Booster KB asset | Knowledge Gap (Wave 5) |
| 5 | Add Oracle Touch Points KB asset | Knowledge Gap (Wave 5) |
| 6 | Add `--context` pattern to KVE regression documentation | Platform improvement |

---

*PF2-006 Operational Validation Report v1.0 | 2026-06-30*
*Proposal Factory Platform Maturity L5.6 → L5.7*
