---
document_id: ASSEMBLY-RULE-COVERAGE-REPORT-V1
title: "Assembly Rule Coverage Report — PF2-002"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-002 — Assembly Rule Enrichment Engine"
---

# Assembly Rule Coverage Report

**Work Package:** PF2-002  
**Generated:** 2026-06-29  
**Engine:** ARE v1.0  

---

## 1. Coverage Summary

| Dimension | Count |
|---|---|
| Total governed assets | 62 |
| CAP assets | 49 |
| ASP assets | 13 |
| Assets with mandatory_if | 55 |
| Assets with optional_if | 35 |
| Assets with excluded_if | 15 |
| Assets TRUE (unconditionally mandatory) | 6 |
| Assets with governance exclusion (excluded_if) | 15 |
| Regression scenarios | 6 |
| Regression violations | 0 |

---

## 2. CAP Rule Detail

| Asset ID | Title | mandatory_if | optional_if | excluded_if |
|---|---|---|---|---|
| `W1S1-001` | Company Overview | `TRUE` | `—` | `—` |
| `W1S1-002` | Company History | `TRUE` | `—` | `—` |
| `W1S1-006` | Awards & Recognition | `TRUE` | `—` | `—` |
| `W1S1-007` | Delivery Model | `TRUE` | `—` | `—` |
| `W1S1-008` | Geographic Presence | `TRUE` | `—` | `—` |
| `W1S1-009` | Key Differentiators | `TRUE` | `—` | `—` |
| `W1S1-003` | Oracle Partnership | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle…` | `—` | `platform in ["Acumatica", "BeBanking"]` |
| `W1S1-004` | Acumatica Partnership | `platform == "Acumatica"` | `—` | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle…` |
| `W1S1-005` | BeBanking Overview | `platform == "BeBanking"` | `—` | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle…` |
| `W1S2-001` | Acumatica Financials | `platform == "Acumatica" and modules contains "Acumatica Fina…` | `platform == "Acumatica"` | `—` |
| `W1S2-002` | Acumatica Distribution | `platform == "Acumatica" and modules contains "Acumatica Dist…` | `platform == "Acumatica"` | `—` |
| `W1S2-003` | Acumatica Inventory | `—` | `platform == "Acumatica"` | `—` |
| `W1S2-004` | Acumatica Manufacturing | `platform == "Acumatica" and modules contains "Acumatica Manu…` | `platform == "Acumatica"` | `—` |
| `W1S2-005` | Acumatica CRM | `platform == "Acumatica" and modules contains "Acumatica CRM"` | `platform == "Acumatica"` | `—` |
| `W1S2-006-ACU-FieldServices` | Field Services | `—` | `platform == "Acumatica"` | `—` |
| `W1S2-007-ACU-PayrollIntegration` | PaySpace Integration | `platform == "Acumatica" and payroll_integration == true` | `platform == "Acumatica"` | `—` |
| `W1S2-009` | Project Accounting | `platform == "Acumatica" and modules contains "Acumatica Proj…` | `platform == "Acumatica"` | `—` |
| `W1S3-001` | BB Product Overview | `platform == "BeBanking"` | `—` | `—` |
| `W1S3-002` | BB H2H Banking | `platform == "BeBanking"` | `—` | `—` |
| `W1S3-003` | BB Supplier Payments | `platform == "BeBanking" and modules contains "BeBanking Supp…` | `platform == "BeBanking"` | `—` |
| `W1S3-004` | BB Payroll Payments | `platform == "BeBanking" and modules contains "BeBanking Payr…` | `platform == "BeBanking"` | `—` |
| `W1S3-005` | BB Forex | `platform == "BeBanking" and modules contains "BeBanking Fore…` | `platform == "BeBanking"` | `—` |
| `W1S3-006` | BB ERP Integration | `platform == "BeBanking" and integration_scope == true` | `platform == "BeBanking"` | `—` |
| `W1S3-007` | BB Security | `platform == "BeBanking" and security_in_scope == true` | `platform == "BeBanking"` | `—` |
| `W1S3-008` | BB Architecture | `platform == "BeBanking"` | `—` | `—` |
| `W1S3-009` | BB Hosting | `—` | `platform == "BeBanking"` | `—` |
| `W1S3-010` | BB Monitoring | `—` | `platform == "BeBanking"` | `—` |
| `W2S1-001` | Oracle Fusion Cloud | `platform in ["Oracle ERP Cloud", "Oracle Integration Cloud"]` | `platform == "Oracle HCM Cloud" and integration_scope == true` | `—` |
| `W2S1-002` | Oracle EBS | `platform == "Oracle EBS"` | `—` | `—` |
| `W2S1-003` | Oracle DBA | `—` | `platform == "Oracle EBS"` | `—` |
| `W2S1-004` | Oracle Managed Services | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle…` | `—` | `platform in ["Acumatica", "BeBanking"]` |
| `W2S1-005-ORA-ImplementationMethodology` | Oracle Methodology | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle…` | `—` | `engagement_type == "AMS"` |
| `W3S1-001-ORA-HCMCore` | HCM Core | `platform == "Oracle HCM Cloud"` | `—` | `—` |
| `W3S1-002-ORA-TalentMgmt` | Talent Mgmt | `platform == "Oracle HCM Cloud" and modules contains "Oracle …` | `platform == "Oracle HCM Cloud"` | `—` |
| `W3S1-003-ORA-RecruitingCloud` | Recruiting | `platform == "Oracle HCM Cloud" and modules contains "Oracle …` | `platform == "Oracle HCM Cloud"` | `—` |
| `W3S1-004-ORA-LearningCloud` | Learning | `platform == "Oracle HCM Cloud" and modules contains "Oracle …` | `platform == "Oracle HCM Cloud"` | `—` |
| `W3S1-005-ORA-WorkforceCompensation` | Compensation (G-001) | `platform == "Oracle HCM Cloud" and modules contains "Oracle …` | `platform == "Oracle HCM Cloud" and industry == "Mining"` | `not industry == "Mining"` |
| `W3S1-006-ORA-HCMAnalytics` | HCM Analytics | `—` | `platform == "Oracle HCM Cloud"` | `—` |
| `W3S1-007-ORA-WorkforceManagement` | Workforce Mgmt | `platform == "Oracle HCM Cloud"` | `—` | `—` |
| `W3S1-008-ORA-HelpDesk-HRServiceDelivery` | Help Desk | `—` | `platform == "Oracle HCM Cloud"` | `—` |
| `W3S1-009-ORA-PayrollInterface-Integration` | Payroll Interface | `platform == "Oracle HCM Cloud" and payroll_integration == tr…` | `platform == "Oracle HCM Cloud" and integration_scope == true` | `—` |
| `W4-AI-002-ORA-AISkills` | AI Skills | `platform == "Oracle HCM Cloud" and modules contains "Oracle …` | `platform == "Oracle HCM Cloud"` | `—` |
| `W4-ERP-001-ORA-FusionFinancials` | Fusion Financials | `platform == "Oracle ERP Cloud" and modules contains "Oracle …` | `platform == "Oracle ERP Cloud"` | `—` |
| `W4-ERP-002-ORA-FusionProcurement` | Fusion Procurement | `platform == "Oracle ERP Cloud" and modules contains "Oracle …` | `platform == "Oracle ERP Cloud"` | `—` |
| `W4-ERP-003-ORA-PPM` | PPM | `platform == "Oracle ERP Cloud" and modules contains "Oracle …` | `platform == "Oracle ERP Cloud"` | `—` |
| `W4-HCM-002-ORA-Journeys` | Journeys | `platform == "Oracle HCM Cloud"` | `—` | `—` |
| `W4-INT-001-ORA-OICAccelerators` | OIC Accelerators | `platform == "Oracle Integration Cloud"` | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle…` | `—` |
| `W5-ACU-001-ACU-SupportManagedServices` | Acumatica AMS | `platform == "Acumatica" and engagement_type == "AMS"` | `platform == "Acumatica" and support_scope == true` | `—` |
| `W5-METH-001-ERP-ImplementationMethodology` | ERP Methodology | `platform in ["Acumatica", "BeBanking"] and engagement_type =…` | `—` | `engagement_type == "AMS"` |

## 3. ASP Rule Detail

| Asset ID | mandatory_if | optional_if | excluded_if |
|---|---|---|---|
| `HCM-BASE-ASSUMPTIONS-V1` | `platform == "Oracle HCM Cloud"` | `—` | `platform in ["Oracle ERP Cloud", "Oracle EBS", "Oracle …` |
| `HCM-RECRUITING-ASSUMPTIONS-V1` | `platform == "Oracle HCM Cloud" and modules contains "Or…` | `platform == "Oracle HCM Cloud"` | `—` |
| `HCM-LEARNING-ASSUMPTIONS-V1` | `platform == "Oracle HCM Cloud" and modules contains "Or…` | `platform == "Oracle HCM Cloud"` | `—` |
| `HCM-TALENT-ASSUMPTIONS-V1` | `platform == "Oracle HCM Cloud" and modules contains "Or…` | `platform == "Oracle HCM Cloud"` | `—` |
| `HCM-COMPENSATION-ASSUMPTIONS-V1` | `platform == "Oracle HCM Cloud" and modules contains "Or…` | `platform == "Oracle HCM Cloud" and industry == "Mining"` | `not industry == "Mining"` |
| `OIC-ASSUMPTIONS-V1` | `platform == "Oracle Integration Cloud"` | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "O…` | `—` |
| `ERP-ASSUMPTIONS-V1` | `platform == "Oracle ERP Cloud"` | `—` | `platform in ["Oracle HCM Cloud", "Oracle EBS", "Oracle …` |
| `OCI-ASSUMPTIONS-V1` | `oci_in_scope == true` | `—` | `—` |
| `AMS-ASSUMPTIONS-V1` | `engagement_type == "AMS"` | `—` | `engagement_type == "Implementation"` |
| `EBS-AMS-SLA-OVERLAY-V1` | `platform == "Oracle EBS" and engagement_type == "AMS"` | `—` | `not platform == "Oracle EBS"` |
| `EBS-DRM-ASSUMPTIONS-V1` | `platform == "Oracle EBS" and engagement_type == "AMS"` | `—` | `not platform == "Oracle EBS"` |
| `ACU-BASE-ASSUMPTIONS-V1` | `platform == "Acumatica"` | `—` | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "O…` |
| `BEBANKING-BASE-ASSUMPTIONS-V1` | `platform == "BeBanking"` | `—` | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "O…` |

## 4. Regression Results

| Scenario | Platform | Eng | Pattern | Mandatory | Optional | Excluded | Default | Violations |
|---|---|---|---|---|---|---|---|---|
| ARM-IT045-EBS-AMS | Oracle EBS | AMS | P13 | 12 | 3 | 8 | 39 | 0 |
| REG-HCM-P3-MINING | Oracle HCM Cloud | Implementation | P3 | 15 | 12 | 8 | 27 | 0 |
| REG-OIC-P7 | Oracle Integration Cloud | Implementation | P7 | 11 | 0 | 11 | 40 | 0 |
| REG-ERP-P7-FULLSUITE | Oracle ERP Cloud | Implementation | P7 | 14 | 0 | 10 | 38 | 0 |
| REG-ACU-P11 | Acumatica | Implementation | P11 | 11 | 6 | 11 | 34 | 0 |
| REG-BEB-P12 | BeBanking | Implementation | P12 | 16 | 3 | 11 | 32 | 0 |

## 5. Regression Detail

### ARM-IT045-EBS-AMS

**Platform:** Oracle EBS | **Engagement:** AMS | **Pattern:** P13

**Mandatory (12):** AMS-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1, EBS-DRM-ASSUMPTIONS-V1, W1S1-001, W1S1-002, W1S1-003, W1S1-006, W1S1-007, W1S1-008, W1S1-009, W2S1-002, W2S1-004
**Optional (3):** OIC-ASSUMPTIONS-V1, W2S1-003, W4-INT-001-ORA-OICAccelerators
**Excluded (8):** ACU-BASE-ASSUMPTIONS-V1, BEBANKING-BASE-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, HCM-BASE-ASSUMPTIONS-V1, W1S1-004, W1S1-005, W2S1-005-ORA-ImplementationMethodology, W5-METH-001-ERP-ImplementationMethodology
**Violations:** None

### REG-HCM-P3-MINING

**Platform:** Oracle HCM Cloud | **Engagement:** Implementation | **Pattern:** P3

**Mandatory (15):** HCM-BASE-ASSUMPTIONS-V1, HCM-COMPENSATION-ASSUMPTIONS-V1, W1S1-001, W1S1-002, W1S1-003, W1S1-006, W1S1-007, W1S1-008, W1S1-009, W2S1-005-ORA-ImplementationMethodology, W3S1-001-ORA-HCMCore, W3S1-005-ORA-WorkforceCompensation, W3S1-007-ORA-WorkforceManagement, W3S1-009-ORA-PayrollInterface-Integration, W4-HCM-002-ORA-Journeys
**Optional (12):** HCM-LEARNING-ASSUMPTIONS-V1, HCM-RECRUITING-ASSUMPTIONS-V1, HCM-TALENT-ASSUMPTIONS-V1, OIC-ASSUMPTIONS-V1, W2S1-001, W3S1-002-ORA-TalentMgmt, W3S1-003-ORA-RecruitingCloud, W3S1-004-ORA-LearningCloud, W3S1-006-ORA-HCMAnalytics, W3S1-008-ORA-HelpDesk-HRServiceDelivery, W4-AI-002-ORA-AISkills, W4-INT-001-ORA-OICAccelerators
**Excluded (8):** ACU-BASE-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1, BEBANKING-BASE-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1, EBS-DRM-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, W1S1-004, W1S1-005
**Violations:** None

### REG-OIC-P7

**Platform:** Oracle Integration Cloud | **Engagement:** Implementation | **Pattern:** P7

**Mandatory (11):** OIC-ASSUMPTIONS-V1, W1S1-001, W1S1-002, W1S1-003, W1S1-006, W1S1-007, W1S1-008, W1S1-009, W2S1-001, W2S1-005-ORA-ImplementationMethodology, W4-INT-001-ORA-OICAccelerators
**Optional (0):** —
**Excluded (11):** ACU-BASE-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1, BEBANKING-BASE-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1, EBS-DRM-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, HCM-BASE-ASSUMPTIONS-V1, HCM-COMPENSATION-ASSUMPTIONS-V1, W1S1-004, W1S1-005, W3S1-005-ORA-WorkforceCompensation
**Violations:** None

### REG-ERP-P7-FULLSUITE

**Platform:** Oracle ERP Cloud | **Engagement:** Implementation | **Pattern:** P7

**Mandatory (14):** ERP-ASSUMPTIONS-V1, OCI-ASSUMPTIONS-V1, W1S1-001, W1S1-002, W1S1-003, W1S1-006, W1S1-007, W1S1-008, W1S1-009, W2S1-001, W2S1-005-ORA-ImplementationMethodology, W4-ERP-001-ORA-FusionFinancials, W4-ERP-002-ORA-FusionProcurement, W4-ERP-003-ORA-PPM
**Optional (0):** —
**Excluded (10):** ACU-BASE-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1, BEBANKING-BASE-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1, EBS-DRM-ASSUMPTIONS-V1, HCM-BASE-ASSUMPTIONS-V1, HCM-COMPENSATION-ASSUMPTIONS-V1, W1S1-004, W1S1-005, W3S1-005-ORA-WorkforceCompensation
**Violations:** None

### REG-ACU-P11

**Platform:** Acumatica | **Engagement:** Implementation | **Pattern:** P11

**Mandatory (11):** ACU-BASE-ASSUMPTIONS-V1, W1S1-001, W1S1-002, W1S1-004, W1S1-006, W1S1-007, W1S1-008, W1S1-009, W1S2-001, W1S2-009, W5-METH-001-ERP-ImplementationMethodology
**Optional (6):** W1S2-002, W1S2-003, W1S2-004, W1S2-005, W1S2-006-ACU-FieldServices, W1S2-007-ACU-PayrollIntegration
**Excluded (11):** AMS-ASSUMPTIONS-V1, BEBANKING-BASE-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1, EBS-DRM-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, HCM-BASE-ASSUMPTIONS-V1, HCM-COMPENSATION-ASSUMPTIONS-V1, W1S1-003, W1S1-005, W2S1-004, W3S1-005-ORA-WorkforceCompensation
**Violations:** None

### REG-BEB-P12

**Platform:** BeBanking | **Engagement:** Implementation | **Pattern:** P12

**Mandatory (16):** BEBANKING-BASE-ASSUMPTIONS-V1, W1S1-001, W1S1-002, W1S1-005, W1S1-006, W1S1-007, W1S1-008, W1S1-009, W1S3-001, W1S3-002, W1S3-003, W1S3-004, W1S3-006, W1S3-007, W1S3-008, W5-METH-001-ERP-ImplementationMethodology
**Optional (3):** W1S3-005, W1S3-009, W1S3-010
**Excluded (11):** ACU-BASE-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1, EBS-DRM-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, HCM-BASE-ASSUMPTIONS-V1, HCM-COMPENSATION-ASSUMPTIONS-V1, W1S1-003, W1S1-004, W2S1-004, W3S1-005-ORA-WorkforceCompensation
**Violations:** None

## 6. Governance Constraints Encoded

| Constraint | Asset | Rule |
|---|---|---|
| GOV-010 Mining Only | W3S1-005, HCM-COMPENSATION | `excluded_if: not industry == "Mining"` |
| AMS Exclusion | W2S1-005, W5-METH-001 | `excluded_if: engagement_type == "AMS"` |
| Platform Exclusion | W1S1-003, W1S1-004, W1S1-005 | Platform `in` list exclusion |
| EBS-Only Overlays | EBS-AMS-SLA, EBS-DRM | `excluded_if: not platform == "Oracle EBS"` |
| Oracle-Only Managed Services | W2S1-004 | `excluded_if: platform in [Acumatica, BeBanking]` |

---

*ASSEMBLY_RULE_COVERAGE_REPORT.md v1.0 | PF2-002 | 2026-06-29*
