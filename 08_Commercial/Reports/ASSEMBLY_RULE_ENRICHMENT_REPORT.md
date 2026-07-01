---
document_id: ASSEMBLY-RULE-ENRICHMENT-REPORT-V1
title: "Assembly Rule Enrichment Report — PF2-002"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-002 — Assembly Rule Enrichment Engine"
approved_by: "PF2-002"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Work Package Report"
scope: "Documents the AREL expression enrichment applied to all 49 CAP and 13 ASP governed assets in the Knowledge Asset Registry."
---

# Assembly Rule Enrichment Report — PF2-002

**Work Package:** PF2-002  
**Date:** 2026-06-29  
**Status:** APPROVED  
**Platform Maturity:** L5.2 → **L5.3**

---

## 1. Objective

Populate deterministic, explainable, non-duplicate AREL V1.0 assembly expressions (`mandatory_if`, `optional_if`, `excluded_if`) for all 49 CAP and 13 ASP governed assets in the Knowledge Asset Registry.

**Pre-conditions confirmed:**

| Pre-condition | Status |
|---|---|
| Platform Maturity | L5.2 |
| Knowledge Platform v1.0 | COMPLETE — WP19D |
| Registry V1.0 CERTIFIED | BUILD-20260628-150801; 213 core + 1,136 ASM |
| RSE operational | rse.py v1.0; 17/17 PASS; 5 regression, 0 violations |
| AREL V1.0 FROZEN | WP19B; grammar; 20 context variables; 30 ARVAL rules |

---

## 2. Enrichment Summary

| Dimension | Count |
|---|---|
| CAP assets enriched | 49 / 49 |
| ASP assets enriched | 13 / 13 |
| Total governed assets enriched | 62 / 62 |
| Assets with mandatory_if populated | 56 |
| Assets with optional_if populated | 33 |
| Assets with excluded_if populated | 24 |
| Assets with `mandatory_if: TRUE` (unconditional) | 6 |
| Governance exclusions encoded (excluded_if) | 24 |
| AREL expression validation | 62 / 62 VALID |
| Syntax issues | 0 |
| Invalid variable references | 0 |
| Duplicate logic conflicts | 0 |
| Contradiction violations (excluded ∩ mandatory) | 0 |

---

## 3. Rule Design Principles

### 3.1 Selection Cascade

Rules follow the AREL V1.0 selection cascade:

1. `excluded_if` evaluates first — if TRUE → EXCLUDED (overrides all)
2. `mandatory_if` — if TRUE → MANDATORY
3. `optional_if` — if TRUE → OPTIONAL_SELECTED
4. Otherwise → DEFAULT_EXCLUDED

### 3.2 Corporate Block (Always Mandatory)

Six assets are unconditionally mandatory across all tender types:

| Asset | mandatory_if |
|---|---|
| W1S1-001 Company Overview | `TRUE` |
| W1S1-002 Company History | `TRUE` |
| W1S1-006 Awards & Recognition | `TRUE` |
| W1S1-007 Delivery Model | `TRUE` |
| W1S1-008 Geographic Presence | `TRUE` |
| W1S1-009 Key Differentiators | `TRUE` |

### 3.3 Platform-Based Selection

Platform-exclusive assets use `in [...]` list membership to exclude cross-platform contamination:

- W1S1-003 Oracle Partnership: `excluded_if: platform in ["Acumatica", "BeBanking"]`
- W1S1-004 Acumatica Partnership: `excluded_if: platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", ...]`
- W1S1-005 BeBanking Overview: `excluded_if: platform in ["Oracle HCM Cloud", ...]`

### 3.4 Module-Driven Mandatory Escalation

Oracle HCM Wave 3 assets use a two-tier pattern:
- `mandatory_if: platform == "Oracle HCM Cloud" and modules contains "<module>"` → MANDATORY when module in scope
- `optional_if: platform == "Oracle HCM Cloud"` → OPTIONAL when platform matches but module absent

This ensures HCM module assets are always reachable when the platform matches, regardless of exact module selection.

### 3.5 Governance Constraint GOV-010 — Mining Sector Only

**W3S1-005-ORA-WorkforceCompensation** and **HCM-COMPENSATION-ASSUMPTIONS-V1** encode the G-001 Mining restriction:

```
mandatory_if: platform == "Oracle HCM Cloud" and modules contains "Oracle Workforce Compensation" and industry == "Mining"
optional_if:  platform == "Oracle HCM Cloud" and industry == "Mining"
excluded_if:  not industry == "Mining"
```

When `industry` is absent from context: `industry == "Mining"` → false → `not false` → TRUE → EXCLUDED.
This is intentional and correct — the asset is excluded when industry is unknown or non-Mining.

### 3.6 Engagement Type Rules

- **AMS packs:** `mandatory_if: engagement_type == "AMS"` / `excluded_if: engagement_type == "Implementation"`
- **Implementation methodology:** `mandatory_if: ... and engagement_type == "Implementation"` / `excluded_if: engagement_type == "AMS"`
- **Oracle Managed Services (W2S1-004):** `mandatory_if: ... and engagement_type == "AMS"` — Oracle platforms only; `excluded_if: platform in ["Acumatica", "BeBanking"]`

### 3.7 EBS-Specific Overlays

EBS-only assets use `excluded_if: not platform == "Oracle EBS"` to ensure they are excluded for all non-EBS platforms:

- EBS-AMS-SLA-OVERLAY-V1: `mandatory_if: platform == "Oracle EBS" and engagement_type == "AMS"`
- EBS-DRM-ASSUMPTIONS-V1: `mandatory_if: platform == "Oracle EBS" and engagement_type == "AMS"`

---

## 4. CAP Rule Assignments by Category

### 4.1 Corporate Block (W1S1 — always mandatory)

| Asset | Rule Pattern |
|---|---|
| W1S1-001 through 009 | TRUE (6 assets) or platform-based exclusion (3 partnership statements) |

### 4.2 Acumatica Module Assets (W1S2)

Eight Acumatica assets use `platform == "Acumatica"` as the base condition:
- Mandatory when specific module confirmed in context
- Optional for all other Acumatica engagements
- No explicit excluded_if (DEFAULT_EXCLUDED for non-Acumatica platforms)

### 4.3 BeBanking Assets (W1S3)

Ten BeBanking assets use `platform == "BeBanking"` as base condition:
- W1S3-001, W1S3-002, W1S3-008: always mandatory for BeBanking
- W1S3-003–005: mandatory when specific payment module in scope
- W1S3-006: mandatory when `integration_scope == true`
- W1S3-007: mandatory when `security_in_scope == true`
- W1S3-009, W1S3-010: always optional for BeBanking

### 4.4 Oracle Platform Capability (W2S1)

| Asset | Mandatory When | Optional When |
|---|---|---|
| W2S1-001 Fusion Cloud | ERP Cloud or OIC | HCM Cloud + integration_scope |
| W2S1-002 Oracle EBS | EBS platform | — |
| W2S1-003 Oracle DBA | — | EBS platform |
| W2S1-004 Managed Services | Any Oracle AMS | — (excluded for Acumatica/BeBanking) |
| W2S1-005 Oracle Methodology | Any Oracle Implementation | — (excluded for AMS) |

### 4.5 Oracle HCM Wave 3 (W3S1)

| Asset | Mandatory When | Optional When | Excluded When |
|---|---|---|---|
| W3S1-001 HCM Core | Oracle HCM Cloud | — | — |
| W3S1-002 Talent Mgmt | HCM + Oracle Talent Mgmt module | HCM Cloud | — |
| W3S1-003 Recruiting | HCM + Oracle Recruiting Cloud | HCM Cloud | — |
| W3S1-004 Learning | HCM + Oracle Learning Cloud | HCM Cloud | — |
| W3S1-005 Compensation | HCM + Compensation + Mining | HCM + Mining | `not industry == "Mining"` |
| W3S1-006 Analytics | — | HCM Cloud | — |
| W3S1-007 Workforce Mgmt | HCM Cloud | — | — |
| W3S1-008 Help Desk | — | HCM Cloud | — |
| W3S1-009 Payroll Interface | HCM + payroll_integration | HCM + integration_scope | — |

### 4.6 Oracle Wave 4 (W4)

| Asset | Mandatory When | Optional When |
|---|---|---|
| W4-AI-002 AI Skills | HCM + Oracle AI Skills module | HCM Cloud |
| W4-ERP-001 Fusion Financials | ERP + Oracle Fusion Financials | ERP Cloud |
| W4-ERP-002 Fusion Procurement | ERP + Oracle Fusion Procurement | ERP Cloud |
| W4-ERP-003 PPM | ERP + Oracle PPM | ERP Cloud |
| W4-HCM-002 Journeys | HCM Cloud | — | — |
| W4-INT-001 OIC Accelerators | Oracle Integration Cloud | Oracle HCM/ERP/EBS + integration_scope |

### 4.7 Cross-Platform Wave 5 (W5)

| Asset | Mandatory When | Optional When | Excluded When |
|---|---|---|---|
| W5-ACU-001 Acumatica AMS | Acumatica + AMS | Acumatica + support_scope | — |
| W5-METH-001 ERP Methodology | Acumatica/BeBanking + Implementation | — | AMS engagements |

---

## 5. ASP Rule Assignments

| Asset Pack | Mandatory When | Excluded When |
|---|---|---|
| HCM-BASE-ASSUMPTIONS-V1 | Oracle HCM Cloud | Non-HCM platforms |
| HCM-RECRUITING-ASSUMPTIONS-V1 | HCM + Recruiting module | — |
| HCM-LEARNING-ASSUMPTIONS-V1 | HCM + Learning module | — |
| HCM-TALENT-ASSUMPTIONS-V1 | HCM + Talent module | — |
| HCM-COMPENSATION-ASSUMPTIONS-V1 | HCM + Compensation + Mining | `not industry == "Mining"` |
| OIC-ASSUMPTIONS-V1 | Oracle Integration Cloud | — |
| ERP-ASSUMPTIONS-V1 | Oracle ERP Cloud | Non-ERP platforms |
| OCI-ASSUMPTIONS-V1 | `oci_in_scope == true` | — |
| AMS-ASSUMPTIONS-V1 | `engagement_type == "AMS"` | Implementation engagements |
| EBS-AMS-SLA-OVERLAY-V1 | Oracle EBS + AMS | `not platform == "Oracle EBS"` |
| EBS-DRM-ASSUMPTIONS-V1 | Oracle EBS + AMS | `not platform == "Oracle EBS"` |
| ACU-BASE-ASSUMPTIONS-V1 | Acumatica | Non-Acumatica platforms |
| BEBANKING-BASE-ASSUMPTIONS-V1 | BeBanking | Non-BeBanking platforms |

---

## 6. Regression Results

| Scenario | Platform | Pattern | Mandatory | Optional | Excluded | Default | Violations |
|---|---|---|---|---|---|---|---|
| ARM-IT045-EBS-AMS | Oracle EBS | P13 | 12 | 3 | 8 | 39 | 0 |
| REG-HCM-P3-MINING | Oracle HCM Cloud | P3 | 15 | 12 | 8 | 27 | 0 |
| REG-OIC-P7 | Oracle Integration Cloud | P7 | 11 | 0 | 11 | 40 | 0 |
| REG-ERP-P7-FULLSUITE | Oracle ERP Cloud | P7 | 14 | 0 | 10 | 38 | 0 |
| REG-ACU-P11 | Acumatica | P11 | 11 | 6 | 11 | 34 | 0 |
| REG-BEB-P12 | BeBanking | P12 | 16 | 3 | 11 | 32 | 0 |

**All 6 scenarios: 0 validation violations. Deterministic across repeated execution.**

---

## 7. Data Quality Observations

| Observation | Impact | Resolution |
|---|---|---|
| Existing regression contexts lack `industry` field | W3S1-005/HCM-COMPENSATION evaluate to EXCLUDED (null → safe) | ARE regression uses ARE-internal contexts with `industry` populated |
| Some contexts use non-canonical module names ("Acumatica Financial Management" vs "Acumatica Financials") | Module-triggered mandatory falls back to optional_if | Acceptable; note in TIL normalization requirements |
| `client_sector: "Mining"` in P3 context is non-canonical | `client_sector` != `industry`; separate AREL variables | Use `industry: "Mining"` for GOV-010 compliance |
| OCI-ASSUMPTIONS-V1 activates only when `oci_in_scope: true` | OCI pack remains DEFAULT_EXCLUDED for most contexts | Correct behavior — OCI is a narrow in-scope activation |

---

## 8. Governance Constraints Encoded

| Constraint | Assets | Expression |
|---|---|---|
| G-001 Mining Only (GOV-010) | W3S1-005, HCM-COMPENSATION | `excluded_if: not industry == "Mining"` |
| AMS/Implementation mutual exclusion | W2S1-005, W5-METH-001, AMS-ASSUMPTIONS | excluded_if per engagement type |
| EBS Overlay isolation | EBS-AMS-SLA, EBS-DRM | `excluded_if: not platform == "Oracle EBS"` |
| Oracle-only Managed Services | W2S1-004 | `excluded_if: platform in ["Acumatica", "BeBanking"]` |
| Partnership statement exclusion | W1S1-003/004/005 | Bidirectional platform exclusion |

---

## 9. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-002 | Initial enrichment — 49 CAP + 13 ASP |
