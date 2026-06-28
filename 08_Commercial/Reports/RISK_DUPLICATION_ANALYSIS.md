---
title: "WP18B-EXT.1 — Risk Duplication Analysis"
status: "COMPLETE"
version: "1.0"
created: "2026-06-26"
created_by: "WP18B-EXT.1 — Risk Library Foundation"
---

# WP18B-EXT.1 — Risk Duplication Analysis

**Work Package:** WP18B-EXT.1 — Risk Library Foundation — Phase 1  
**Status:** COMPLETE  
**Date:** 2026-06-26  

This document records the full duplication analysis performed during WP18B-EXT.1. It shows which source risks were merged, which were kept separate, and the justification for each decision.

---

## Summary

| Total source risks audited | 51 |
|---|---|
| Duplication groups identified | 8 |
| Source risks absorbed into canonical risks | 9 |
| Source risks kept as independent canonical risks | 42 |
| Canonical risks produced | 40 |
| **Net reduction from deduplication** | **11 (22% fewer canonical entries than source risks)** |

---

## Duplication Groups

### DG-001 — Design Sign-Off Before Build (RC-PROJ-001)

**Source risks merged:**

| Source ID | Asset | Title | Original L × I |
|-----------|-------|-------|----------------|
| R-W2-001 | W3S1-002 | Talent profile architecture not agreed before config | High × High |
| R-W3-005-001 | W3S1-005 | Compensation plan design not complete before build | Medium × High |

**Canonical risk:** RC-PROJ-001 — Module design not signed off before build begins  
**Canonical L × I:** Medium × High → **HIGH**

**Merge justification:** Both source risks share the same root cause (design decisions not finalised before Oracle HCM configuration begins), the same mitigation pattern (formal design gate with written sign-off before build), and the same assembly trigger (any Oracle HCM module with a design-then-build phase). The High × High rating on R-W2-001 reflects a specific Talent Management scenario where the risk materialized at High probability; the canonical risk is rated at Medium × High to represent the general case across all HCM modules.

**Why not kept separate:** Talent profile architecture and compensation plan design are both instances of the same governance gap (no mandatory design sign-off gate). Separate canonical entries would create redundancy in the assembly engine and confuse risk register reviewers. The customisation guidance in RC-PROJ-001 allows BU Leads to elevate Likelihood to High when the specific module's design risk warrants it.

---

### DG-002 — Phase Dependency Not Managed (RC-PROJ-002)

**Source risks merged:**

| Source ID | Asset | Title | Original L × I |
|-----------|-------|-------|----------------|
| R-W2-003 | W3S1-002 | HCM Core not stable when Talent Management phase begins | Medium × High |
| R-W3-003-003 | W3S1-003 | Job profiles in Core HR not ready when Recruiting begins | Medium × High |

**Canonical risk:** RC-PROJ-002 — Upstream phase not stable when dependent module phase begins  
**Canonical L × I:** Medium × High → **HIGH**

**Merge justification:** Identical root cause (programme management failure to enforce a stability gate between dependent Oracle HCM implementation phases), identical Likelihood and Impact, and identical mitigation (define phase stability gates; no downstream phase starts until upstream milestone confirmed). The specific module pair (HCM Core → Talent; HCM Core → Recruiting) is an instance of a pattern, not a distinct risk.

**Why not kept separate:** Creating individual canonical risks for every Oracle HCM module-pair dependency would produce an unmanageable registry. The canonical risk is expressed at the pattern level; the assembly trigger and customisation guidance address which specific dependencies are in scope for a given tender.

---

### DG-003 — SETA/Legislative Reporting Complexity (RC-TECH-002)

**Source risks merged:**

| Source ID | Asset | Title | Original L × I |
|-----------|-------|-------|----------------|
| R-W3-004-004 | W3S1-004 | SETA/WSP/ATR extract complexity (Learning Cloud) | Medium × Medium |
| R-W3-006-004 | W3S1-006 | SETA legislative extract complexity (Analytics) | Medium × Medium |

**Canonical risk:** RC-TECH-002 — SETA/WSP/ATR reporting extract complexity  
**Canonical L × I:** Medium × Medium → **MEDIUM**

**Merge justification:** Both source risks describe the same SA-legislative reporting requirement (SETA/WSP/ATR extract) appearing in two different module contexts (OLC and OAX). The technical risk — that the standard Oracle extract is insufficient for the client's SETA reporting needs — is identical. The mitigation (requirements confirmation in Scope and Design, standard template review, scoping of bespoke configuration) is identical.

**Why not kept separate:** The SETA extract requirement exists independently of the Oracle module delivering it. Whether OLC or OAX is used to generate the extract, the risk is the same: the standard configuration may not match the SETA format. A single canonical risk with an assembly trigger referencing "SA SETA reporting requirement" is more useful to a Bid Manager than two separate risks distinguishable only by module.

---

### DG-004 — Third-Party Integration Scope Underestimated (RC-INT-002)

**Source risks merged:**

| Source ID | Asset | Title | Original L × I |
|-----------|-------|-------|----------------|
| R-W3-003-005 | W3S1-003 | Background check and assessment integrations underestimated | Medium × Medium |
| R-W3-004-005 | W3S1-004 | Content provider integration underestimated | Low × Medium |

**Canonical risk:** RC-INT-002 — Third-party system integration scope underestimated at tender stage  
**Canonical L × I:** Medium × Medium → **MEDIUM**

**Merge justification:** Both source risks describe the same commercial and technical failure mode: APPSolve scopes a third-party integration at a fixed effort without reviewing the vendor's API documentation, and discovers during build that the integration is more complex than assumed. The root cause (tendering without API review) and the mitigation (scope as T&M; require API documentation before Scope and Design) are identical. The specific third party (background screening vs. content provider) is an instance of the risk, not a distinct risk.

**Why not kept separate:** A canonical risk at the "third-party integration scope underestimated" pattern level is more reusable across all Oracle module implementations than module-specific instances. The assembly trigger references "any unvalidated third-party integration in scope" to cover all instances.

---

### DG-005 — Analytics Expectations Misaligned (RC-COMM-001)

**Source risks merged:**

| Source ID | Asset | Title | Original L × I |
|-----------|-------|-------|----------------|
| R-W3-004-002 | W3S1-004 | Analytics expectations misaligned — OLC vs OAX | Medium × Medium |
| R-W3-005-003 | W3S1-005 | Analytics expectations exceed OWC built-in capability | Medium × Medium |
| R-W3-006-003 | W3S1-006 | OTBI/OAX conflation in tender response creates expectation gap | Medium × High |

**Canonical risk:** RC-COMM-001 — Analytics expectations misaligned with platform capability in scope  
**Canonical L × I:** Medium × High → **HIGH**

**Merge justification:** All three source risks describe the same commercial failure mode: the client believes they are receiving OAX-level analytics capability when the scope includes only OTBI or built-in module reporting. The root cause (analytics product boundary not clearly communicated), mitigation (explicit product boundary statement in proposal and charter), and assembly trigger (any proposal where analytics is a stated requirement) are identical across all three.

The Impact is elevated to High (from one of the three sources) because the canonical risk must reflect the potential consequence — a mid-project scope dispute about analytics capability is commercially high-impact regardless of which specific module created the expectation.

**Why not kept separate:** These three risks are not different risks in different contexts — they are three instances of the same client-communication failure about Oracle analytics capability. A single canonical risk is more useful to the Risk Selection Engine and produces a cleaner proposal risk register.

---

### DG-006 — Payroll Integration Cutoff Misalignment (RC-INT-005)

**Source risks merged:**

| Source ID | Asset | Title | Original L × I |
|-----------|-------|-------|----------------|
| R-W9-003 | W3S1-009 | Payroll cut-off misalignment in OIC integration schedule | Low × High |
| R-W3-005-005 | W3S1-005 | Compensation approval close-down not aligned to payroll calendar | Medium × High |

**Canonical risk:** RC-INT-005 — Integration extraction schedule not aligned to payroll processing cutoff  
**Canonical L × I:** Medium × High → **HIGH**

**Merge justification:** Both source risks describe the same integration design failure: the timing of HCM data extraction (whether by OIC integration or manual compensation approval cutoff) is not aligned to the payroll system's processing calendar. The consequence is the same — payroll transactions from the current period are missed in the current cycle. The mitigation (design extraction schedule in Scope and Design against the payroll calendar; test in UAT with live payroll cycle dates) is identical.

**Canonical Likelihood elevated:** R-W9-003 rates this Low (OIC integration timing is usually configurable) while R-W3-005-005 rates it Medium (compensation approval timing depends on client process discipline). The canonical risk uses Medium to represent the general case where process and system alignment must both be achieved.

**Why not kept separate:** Both risks are manifestations of the same integration design requirement: HCM data must be extracted within the payroll processing window. Whether the extraction is triggered by an OIC schedule or by a compensation manager's approval action, the risk and the mitigation are the same.

---

### DG-007 — POPIA Compliance (RC-COMP-001)

**Source risks merged:**

| Source ID | Asset | Title | Original L × I |
|-----------|-------|-------|----------------|
| R-W8-007 | W3S1-008 | POPIA data handling in ER cases | Low × High |
| R-W9-005 | W3S1-009 | POPIA non-compliance in payroll data transmission | Low × High |

**Canonical risk:** RC-COMP-001 — POPIA non-compliance in HR or payroll data handling  
**Canonical L × I:** Low × High → **MEDIUM**

**Merge justification:** Both source risks are POPIA compliance risks with identical Likelihood (Low — POPIA controls are achievable with standard implementation practice) and Impact (High — POPIA non-compliance carries regulatory consequences). The root cause (personal information processed without adequate access controls, data minimisation, or purpose limitation) and mitigation (POPIA-aligned access controls; data field scope limits; retention period configuration; UAT compliance testing) are structurally the same across both contexts.

**Why not kept separate:** Creating separate canonical POPIA risks for every Oracle module that processes personal data would produce 10+ near-identical entries (Help Desk ER cases, payroll data, performance reviews, medical data, learning completion records...). A single canonical risk with a comprehensive assembly trigger and customisation guidance is more manageable and produces cleaner proposal risk registers. Module-specific POPIA details belong in the customisation guidance, not in separate canonical entries.

---

### DG-008 — Analytics Licensing Not Confirmed (RC-TECH-006 vs RC-TECH-008 boundary)

This is not a merge — it is a deliberate **split** to ensure clarity.

**Decision:** Two separate canonical risks are created:

| Canonical Risk | Scope |
|----------------|-------|
| RC-TECH-006 | OAX-specific — Oracle Analytics for HCM (OAX) licence not confirmed |
| RC-TECH-008 | General — Any Oracle dependent product licence not confirmed (covers Help Desk, ODA, OAX together) |

**Why kept separate:** R-W3-006-001 (OAX licensing) and R-W8-002 (Help Desk licensing) are instances of the same general risk (Oracle product licensing not confirmed). However:
- RC-TECH-008 (general licensing) is the primary canonical risk for proposal assembly — it covers all Oracle licence prerequisites in one risk entry
- RC-TECH-006 (OAX-specific) is retained because OAX is commonly scoped into HCM proposals with an assumption of OAX-in-HCM-licence that is factually incorrect, making it a high-frequency standalone risk

Including OAX-specific licensing detail in RC-TECH-008 only would cause it to be omitted from the risk register when an analytics-focused proposal includes RC-TECH-008 generically but doesn't trigger the OAX-specific check. Keeping both canonical risks ensures the OAX licensing gap is explicitly surfaced in analytics proposals.

---

## Risks Considered for Merging But Kept Separate

The following pairs were evaluated for merging and deliberately kept as separate canonical risks:

| Source Risk 1 | Source Risk 2 | Reason Kept Separate |
|---------------|---------------|---------------------|
| RC-TECH-003 (Absence rules) | RC-TECH-004 (T&L rules) | Different Oracle WFM feature areas; different design documentation requirements; different estimation impact path |
| RC-DATA-001 (Legacy HR data quality) | RC-DATA-003 (HCM data quality → payroll) | Different risk event (migration failure vs integration failure); different phase (pre-go-live vs ongoing); different owner |
| RC-INT-001 (Payroll integration timeline) | RC-INT-007 (Bespoke payroll mapping) | Different root cause (programme management vs technical scoping); different engagement type trigger |
| RC-TECH-006 (OAX licensing) | RC-COMM-001 (Analytics expectations) | Different risk type (technical — wrong licence) vs commercial (wrong expectation); different owner (Bid Manager vs Technical Lead) |
| RC-PROJ-001 (Design sign-off) | RC-CLIENT-007 (Cross-functional alignment) | RC-PROJ-001 is an APPSolve process risk (we don't have a sign-off gate); RC-CLIENT-007 is a client dependency risk (stakeholder alignment fails) — different owners and different mitigations |

---

## Notes on Near-Duplicates Not Merged

### R-W2-005 (Calibration not tested in UAT)
Directionally covered by RC-CLIENT-001 (super-user UAT availability). Not created as a separate canonical risk because calibration UAT coverage is a specific instance of insufficient UAT execution — the root cause (super-user availability) is the same. The customisation guidance in RC-CLIENT-001 covers this case.

### R-W3-006-002 (Reporting requirements not confirmed in Scope and Design)
Directionally covered by RC-CLIENT-007 (cross-functional alignment on design frameworks). Reporting requirements confirmation is a subset of the broader design framework sign-off. Not created as a separate canonical risk to avoid overpopulating the reporting-specific risk space; included in RC-CLIENT-007 scope.

### R-W8-003 (ER case process complexity)
Directionally adjacent to RC-TECH-008 (product licensing) and RC-PROJ-001 (design sign-off). The ER case process complexity is a technical configuration risk specific to Help Desk implementations. Rather than create a standalone canonical entry, it is captured in the customisation guidance for RC-TECH-008. If the BU Lead determines during WP18B-EXT.2 review that ER case complexity is a standalone risk of sufficient frequency, it should be extracted as RC-TECH-008a or a new RC-TECH-013.

---

## Traceability Matrix

The following matrix confirms every source risk maps to exactly one canonical risk (or disposition):

| Source Risk | Canonical Risk | Disposition |
|-------------|---------------|-------------|
| R-W1-001 | RC-PROJ-003 | Independent |
| R-W1-002 | RC-DATA-001 | Independent |
| R-W1-003 | RC-INT-001 | Independent |
| R-W1-004 | RC-TECH-001 | Independent |
| R-W1-005 | RC-CLIENT-001 | Independent |
| R-W2-001 | RC-PROJ-001 | Merged (DG-001) |
| R-W2-002 | RC-CLIENT-007 | Independent |
| R-W2-003 | RC-PROJ-002 | Merged (DG-002) |
| R-W2-004 | RC-PROJ-004 | Independent |
| R-W2-005 | RC-CLIENT-001 | Scope note (not separate canonical) |
| R-W3-003-001 | RC-TECH-011 | Independent |
| R-W3-003-002 | RC-CLIENT-002 | Independent |
| R-W3-003-003 | RC-PROJ-002 | Merged (DG-002) |
| R-W3-003-004 | RC-CLIENT-003 | Independent |
| R-W3-003-005 | RC-INT-002 | Merged (DG-004) |
| R-W3-004-001 | RC-CLIENT-004 | Independent |
| R-W3-004-002 | RC-COMM-001 | Merged (DG-005) |
| R-W3-004-003 | RC-DATA-002 | Independent |
| R-W3-004-004 | RC-TECH-002 | Merged (DG-003) |
| R-W3-004-005 | RC-INT-002 | Merged (DG-004) |
| R-W3-005-001 | RC-PROJ-001 | Merged (DG-001) |
| R-W3-005-002 | RC-CLIENT-005 | Independent |
| R-W3-005-003 | RC-COMM-001 | Merged (DG-005) |
| R-W3-005-004 | RC-OPS-001 | Independent |
| R-W3-005-005 | RC-INT-005 | Merged (DG-006) |
| R-W3-006-001 | RC-TECH-006 | Independent (see DG-008 note) |
| R-W3-006-002 | RC-CLIENT-007 | Scope note (not separate canonical) |
| R-W3-006-003 | RC-COMM-001 | Merged (DG-005) |
| R-W3-006-004 | RC-TECH-002 | Merged (DG-003) |
| R-W3-006-005 | RC-TECH-007 | Independent |
| R-W3-007-001 | RC-TECH-003 | Independent (see near-duplicate note) |
| R-W3-007-002 | RC-TECH-004 | Independent (see near-duplicate note) |
| R-W3-007-003 | RC-INT-003 | Independent |
| R-W3-007-004 | RC-DATA-004 | Independent |
| R-W3-007-005 | RC-TECH-005 | Independent |
| R-W3-007-006 | RC-DATA-005 | Independent |
| R-W8-001 | RC-COMM-002 | Independent |
| R-W8-002 | RC-TECH-008 | Independent (see DG-008 note) |
| R-W8-003 | RC-TECH-008 | Scope note (not separate canonical) |
| R-W8-004 | RC-CLIENT-006 | Independent |
| R-W8-005 | RC-TECH-010 | Independent |
| R-W8-006 | RC-TECH-009 | Independent |
| R-W8-007 | RC-COMP-001 | Merged (DG-007) |
| R-W9-001 | RC-INT-004 | Independent |
| R-W9-002 | RC-DATA-003 | Independent |
| R-W9-003 | RC-INT-005 | Merged (DG-006) |
| R-W9-004 | RC-INT-006 | Independent |
| R-W9-005 | RC-COMP-001 | Merged (DG-007) |
| R-W9-006 | RC-TECH-012 | Independent |
| R-W7-004 | RC-COMM-003 | Independent |
| R-W7-005 | RC-INT-007 | Independent |

**Validation:** All 51 source risks accounted for. All 40 canonical risks have at least one source risk. No source risk is unaccounted for.

---

*WP18B-EXT.1 Risk Duplication Analysis v1.0 — 2026-06-26*
