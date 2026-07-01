# Section Traceability Report — PF2-003

**Generated:** 2026-06-30 07:01 UTC  
**Engine:** PSAE v1.0  

---

## Purpose

For every proposal section, this report answers:
- **Why it exists** — which rule selected it and what assets contributed
- **Why it does not exist** — which exclusion rule removed it
- **Which assets contributed** — CAP/ASP traceability back to registry
- **Which SI rules applied** — section integrity constraints

---
## ARM-IT045 — Oracle EBS AMS

### Full Section Traceability

| Section | Status | Rationale | Source Assets | SI Rules |
|---|---|---|---|---|
| S-01 Cover Page / Transmittal | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-02 Table of Contents | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-03 Company Overview | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-04 Company History | MANDATORY | M-ALL — mandatory in all proposals | W1S1-002 | — |
| S-05 Awards and Recognition | MANDATORY | M-ALL — mandatory in all proposals | W1S1-006 | — |
| S-06 Delivery Model | MANDATORY | M-ALL — mandatory in all proposals | W1S1-007 | — |
| S-07 Geographic Presence | MANDATORY | M-ALL — mandatory in all proposals | W1S1-008 | — |
| S-08 Key Differentiators | MANDATORY | OPT — driver assets selected: ['W1S1-009'] | W1S1-009 | — |
| S-09 Oracle Partnership | MANDATORY | COND-ORA — platform=Oracle EBS; drivers: ['W1S1-003'] | W1S1-003 | — |
| S-10 Acumatica Partnership | EXCLUDED | EXCLUDED — S-10 requires Acumatica platform | — | — |
| S-11 BeBanking Product Overview | EXCLUDED | EXCLUDED — S-11 requires BeBanking platform | — | — |
| S-12 B-BBEE Compliance Statement | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-13 Executive Summary | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-14 Understanding of Requirements | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-15 Proposed Solution Overview | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-16 Oracle Fusion HCM Capability | DEFAULT_EXCLUDED | COND-HCM — no driver assets selected | — | — |
| S-17 Oracle Fusion ERP Capability | DEFAULT_EXCLUDED | COND-ERP — no driver assets selected | — | — |
| S-18 Oracle EBS Capability | MANDATORY | COND-EBS — drivers: ['W2S1-002'] | W2S1-002 | — |
| S-19 Oracle OIC / Integration Capability | OPTIONAL_SELECTED | COND-OIC — drivers: ['W4-INT-001-ORA-OICAccelerators'] | W4-INT-001-ORA-OICAccelerators | — |
| S-20 Oracle DBA Capability | OPTIONAL_SELECTED | COND-DBA — drivers: ['W2S1-003'] | W2S1-003 | — |
| S-21 Oracle Managed Services Capability | MANDATORY | COND-AMS — AMS engagement; drivers: ['W2S1-004'] | W2S1-004 | — |
| S-22 OCI Infrastructure | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-23 Acumatica Financials | EXCLUDED | EXCLUDED — S-23 requires Acumatica platform | — | — |
| S-24 Acumatica Distribution | EXCLUDED | EXCLUDED — S-24 requires Acumatica platform | — | — |
| S-25 Acumatica Manufacturing | EXCLUDED | EXCLUDED — S-25 requires Acumatica platform | — | — |
| S-26 Acumatica CRM | EXCLUDED | EXCLUDED — S-26 requires Acumatica platform | — | — |
| S-27 Acumatica Other Modules | EXCLUDED | EXCLUDED — S-27 requires Acumatica platform | — | — |
| S-28 Acumatica Managed Services | EXCLUDED | EXCLUDED — S-28 requires Acumatica AMS | — | — |
| S-29 BeBanking H2H Banking | EXCLUDED | EXCLUDED — S-29 requires BeBanking platform | — | — |
| S-30 Scope of Work — Inclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-31 Scope of Work — Exclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-32 Deliverables | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-33 Dependencies | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-34 Implementation Methodology | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-34 | — | SI-001 |
| S-35 Project Plan / Timeline | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-35 | — | SI-001 |
| S-36 Project Governance | MANDATORY | M-ALL — methodology asset selected or AMS; project governance mandatory | — | — |
| S-37 RAID Framework | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-38 Change Control Framework | EXCLUDED | EXCLUDED — AMS Pattern 13 exclusion; SI-001 applies | — | SI-001 |
| S-39 Testing Strategy | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-39 | — | — |
| S-40 Data Migration | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-40 | — | — |
| S-41 Training Plan | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-41 | — | — |
| S-42 Cutover / Go-Live Plan | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-42 | — | — |
| S-43 Hypercare / Post-Go-Live Transition | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-43 | — | — |
| S-44 Disaster Recovery | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-45 Security Architecture | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-46 Team Structure | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-46 | — | — |
| S-47 Named Consultant CVs | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-47 | — | ADR-001 |
| S-48 Consultant Profiles (Summary) | EXCLUDED | EXCLUDED — AMS Pattern 13 excludes S-48 | — | ADR-001 |
| S-49 Key Assumptions (Body Section) | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1 | SI-006 |
| S-50 Risk Register | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-51 Commercial Assumptions | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1 | — |
| S-52 Commercials / Pricing | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-006 |
| S-53 Rate Card Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-54 Estimation Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-55 Compliance Schedule | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-56 Company Registration | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-57 Tax Clearance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-58 Directors' Resolution | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-59 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| S-60 Public Liability Insurance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-61 Professional Indemnity | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-62 Oracle OPN Certificate | MANDATORY | COND-ORA — platform=Oracle EBS; drivers: ['W1S1-003'] | W1S1-003 | — |
| S-63 Acumatica Partner Certificate | EXCLUDED | EXCLUDED — S-63 requires Acumatica platform | — | — |
| S-64 ISO / Other Certifications | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-65 POPIA Policy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-66 PAIA Manual | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-67 Client References | MANDATORY | M-ALL — mandatory in all proposals | — | SI-005 |
| S-68 Case Studies | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-69 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | SI-005 |
| S-70 Support Model | MANDATORY | COND-AMS — AMS engagement; drivers: ['AMS-ASSUMPTIONS-V1', 'W2S1-004'] | W2S1-004, AMS-ASSUMPTIONS-V1 | SI-001 |
| S-71 SLA Framework | MANDATORY | COND-AMS — AMS engagement; drivers: ['AMS-ASSUMPTIONS-V1', 'EBS-AMS-SLA-OVERLAY-V1'] | AMS-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1 | SI-001, SI-007 |
| S-72 Incident Management | MANDATORY | COND-AMS — AMS engagement; drivers: ['AMS-ASSUMPTIONS-V1'] | AMS-ASSUMPTIONS-V1 | SI-001, SI-007 |
| S-73 Change Request Process | MANDATORY | COND-AMS — AMS engagement; drivers: ['AMS-ASSUMPTIONS-V1'] | AMS-ASSUMPTIONS-V1 | SI-001 |
| S-74 Resource Model (AMS) | MANDATORY | COND-AMS — AMS engagement; drivers: ['AMS-ASSUMPTIONS-V1', 'EBS-DRM-ASSUMPTIONS-V1'] | AMS-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1, EBS-DRM-ASSUMPTIONS-V1 | SI-001 |
| S-75 Release Management | MANDATORY | COND-AMS — AMS engagement; drivers: ['AMS-ASSUMPTIONS-V1'] | AMS-ASSUMPTIONS-V1 | SI-001 |
| S-76 Monitoring and Reporting | MANDATORY | COND-AMS — AMS engagement; drivers: ['AMS-ASSUMPTIONS-V1'] | AMS-ASSUMPTIONS-V1 | SI-001 |
| A-01 Complete Assumption Schedule | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1 | — |
| A-02 Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| A-03 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| A-04 Certifications and Compliance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| A-05 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| A-06 Company Registration | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |

---

## REG-HCM-P3-MINING — Oracle HCM Cloud Implementation

### Full Section Traceability

| Section | Status | Rationale | Source Assets | SI Rules |
|---|---|---|---|---|
| S-01 Cover Page / Transmittal | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-02 Table of Contents | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-03 Company Overview | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-04 Company History | MANDATORY | M-ALL — mandatory in all proposals | W1S1-002 | — |
| S-05 Awards and Recognition | MANDATORY | M-ALL — mandatory in all proposals | W1S1-006 | — |
| S-06 Delivery Model | MANDATORY | M-ALL — mandatory in all proposals | W1S1-007 | — |
| S-07 Geographic Presence | MANDATORY | M-ALL — mandatory in all proposals | W1S1-008 | — |
| S-08 Key Differentiators | MANDATORY | OPT — driver assets selected: ['W1S1-009'] | W1S1-009 | — |
| S-09 Oracle Partnership | MANDATORY | COND-ORA — platform=Oracle HCM Cloud; drivers: ['W1S1-003'] | W1S1-003 | — |
| S-10 Acumatica Partnership | EXCLUDED | EXCLUDED — S-10 requires Acumatica platform | — | — |
| S-11 BeBanking Product Overview | EXCLUDED | EXCLUDED — S-11 requires BeBanking platform | — | — |
| S-12 B-BBEE Compliance Statement | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-13 Executive Summary | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-14 Understanding of Requirements | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-15 Proposed Solution Overview | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-16 Oracle Fusion HCM Capability | MANDATORY | COND-HCM — drivers: ['W3S1-001-ORA-HCMCore', 'W3S1-002-ORA-TalentMgmt', 'W3S1-003-ORA-RecruitingCloud', 'W3S1-004-ORA-LearningCloud', 'W3S1-005-ORA-WorkforceCompensation', 'W3S1-006-ORA-HCMAnalytics', 'W3S1-007-ORA-WorkforceManagement', 'W3S1-009-ORA-PayrollInterface-Integration', 'W4-AI-002-ORA-AISkills', 'W4-HCM-002-ORA-Journeys'] | W3S1-001-ORA-HCMCore, W3S1-002-ORA-TalentMgmt, W3S1-003-ORA-RecruitingCloud, W3S1-004-ORA-LearningCloud, W3S1-005-ORA-WorkforceCompensation, W3S1-006-ORA-HCMAnalytics, W3S1-007-ORA-WorkforceManagement, W4-AI-002-ORA-AISkills, W4-HCM-002-ORA-Journeys | — |
| S-17 Oracle Fusion ERP Capability | OPTIONAL_SELECTED | COND-ERP — drivers: ['W2S1-001'] | W2S1-001 | — |
| S-18 Oracle EBS Capability | DEFAULT_EXCLUDED | COND-EBS — no driver assets selected | — | — |
| S-19 Oracle OIC / Integration Capability | MANDATORY | COND-OIC — drivers: ['W4-INT-001-ORA-OICAccelerators', 'W3S1-009-ORA-PayrollInterface-Integration'] | W3S1-009-ORA-PayrollInterface-Integration, W4-INT-001-ORA-OICAccelerators | — |
| S-20 Oracle DBA Capability | DEFAULT_EXCLUDED | COND-DBA — no driver assets selected | — | — |
| S-21 Oracle Managed Services Capability | EXCLUDED | EXCLUDED — S-21 applies to AMS only | — | — |
| S-22 OCI Infrastructure | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-23 Acumatica Financials | EXCLUDED | EXCLUDED — S-23 requires Acumatica platform | — | — |
| S-24 Acumatica Distribution | EXCLUDED | EXCLUDED — S-24 requires Acumatica platform | — | — |
| S-25 Acumatica Manufacturing | EXCLUDED | EXCLUDED — S-25 requires Acumatica platform | — | — |
| S-26 Acumatica CRM | EXCLUDED | EXCLUDED — S-26 requires Acumatica platform | — | — |
| S-27 Acumatica Other Modules | EXCLUDED | EXCLUDED — S-27 requires Acumatica platform | — | — |
| S-28 Acumatica Managed Services | EXCLUDED | EXCLUDED — S-28 requires Acumatica AMS | — | — |
| S-29 BeBanking H2H Banking | EXCLUDED | EXCLUDED — S-29 requires BeBanking platform | — | — |
| S-30 Scope of Work — Inclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-31 Scope of Work — Exclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-32 Deliverables | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-33 Dependencies | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-34 Implementation Methodology | MANDATORY | M-ALL — mandatory in all proposals | W2S1-005-ORA-ImplementationMethodology | SI-001 |
| S-35 Project Plan / Timeline | MANDATORY | M-ALL — mandatory in all proposals | — | SI-001 |
| S-36 Project Governance | MANDATORY | M-ALL — governance mandatory in all proposals | W2S1-005-ORA-ImplementationMethodology | — |
| S-37 RAID Framework | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-38 Change Control Framework | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-001 |
| S-39 Testing Strategy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-40 Data Migration | DEFAULT_EXCLUDED | COND-MIG — no driver assets selected | — | — |
| S-41 Training Plan | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-42 Cutover / Go-Live Plan | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-43 Hypercare / Post-Go-Live Transition | DEFAULT_EXCLUDED | COND-POST-GOLIVE — no driver assets selected | — | — |
| S-44 Disaster Recovery | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-45 Security Architecture | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-46 Team Structure | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-47 Named Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-48 Consultant Profiles (Summary) | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-49 Key Assumptions (Body Section) | MANDATORY | M-FIXED — mandatory in all proposals | HCM-BASE-ASSUMPTIONS-V1, HCM-RECRUITING-ASSUMPTIONS-V1, HCM-LEARNING-ASSUMPTIONS-V1, HCM-TALENT-ASSUMPTIONS-V1, HCM-COMPENSATION-ASSUMPTIONS-V1, OIC-ASSUMPTIONS-V1 | SI-006 |
| S-50 Risk Register | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-51 Commercial Assumptions | MANDATORY | M-FIXED — mandatory in all proposals | HCM-BASE-ASSUMPTIONS-V1, HCM-RECRUITING-ASSUMPTIONS-V1, HCM-LEARNING-ASSUMPTIONS-V1, HCM-TALENT-ASSUMPTIONS-V1, HCM-COMPENSATION-ASSUMPTIONS-V1, OIC-ASSUMPTIONS-V1 | — |
| S-52 Commercials / Pricing | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-006 |
| S-53 Rate Card Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-54 Estimation Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-55 Compliance Schedule | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-56 Company Registration | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-57 Tax Clearance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-58 Directors' Resolution | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-59 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| S-60 Public Liability Insurance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-61 Professional Indemnity | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-62 Oracle OPN Certificate | MANDATORY | COND-ORA — platform=Oracle HCM Cloud; drivers: ['W1S1-003'] | W1S1-003 | — |
| S-63 Acumatica Partner Certificate | EXCLUDED | EXCLUDED — S-63 requires Acumatica platform | — | — |
| S-64 ISO / Other Certifications | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-65 POPIA Policy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-66 PAIA Manual | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-67 Client References | MANDATORY | M-ALL — mandatory in all proposals | — | SI-005 |
| S-68 Case Studies | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-69 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | SI-005 |
| S-70 Support Model | EXCLUDED | EXCLUDED — S-70 applies to AMS engagements only | — | SI-001 |
| S-71 SLA Framework | EXCLUDED | EXCLUDED — S-71 applies to AMS engagements only | — | SI-001, SI-007 |
| S-72 Incident Management | EXCLUDED | EXCLUDED — S-72 applies to AMS engagements only | — | SI-001, SI-007 |
| S-73 Change Request Process | EXCLUDED | EXCLUDED — S-73 applies to AMS engagements only | — | SI-001 |
| S-74 Resource Model (AMS) | EXCLUDED | EXCLUDED — S-74 applies to AMS engagements only | — | SI-001 |
| S-75 Release Management | EXCLUDED | EXCLUDED — S-75 applies to AMS engagements only | — | SI-001 |
| S-76 Monitoring and Reporting | EXCLUDED | EXCLUDED — S-76 applies to AMS engagements only | — | SI-001 |
| A-01 Complete Assumption Schedule | MANDATORY | M-FIXED — mandatory in all proposals | HCM-BASE-ASSUMPTIONS-V1, HCM-RECRUITING-ASSUMPTIONS-V1, HCM-LEARNING-ASSUMPTIONS-V1, HCM-TALENT-ASSUMPTIONS-V1, HCM-COMPENSATION-ASSUMPTIONS-V1, OIC-ASSUMPTIONS-V1 | — |
| A-02 Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| A-03 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| A-04 Certifications and Compliance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| A-05 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| A-06 Company Registration | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |

---

## REG-OIC-P7 — Oracle Integration Cloud Implementation

### Full Section Traceability

| Section | Status | Rationale | Source Assets | SI Rules |
|---|---|---|---|---|
| S-01 Cover Page / Transmittal | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-02 Table of Contents | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-03 Company Overview | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-04 Company History | MANDATORY | M-ALL — mandatory in all proposals | W1S1-002 | — |
| S-05 Awards and Recognition | MANDATORY | M-ALL — mandatory in all proposals | W1S1-006 | — |
| S-06 Delivery Model | MANDATORY | M-ALL — mandatory in all proposals | W1S1-007 | — |
| S-07 Geographic Presence | MANDATORY | M-ALL — mandatory in all proposals | W1S1-008 | — |
| S-08 Key Differentiators | MANDATORY | OPT — driver assets selected: ['W1S1-009'] | W1S1-009 | — |
| S-09 Oracle Partnership | MANDATORY | COND-ORA — platform=Oracle Integration Cloud; drivers: ['W1S1-003'] | W1S1-003 | — |
| S-10 Acumatica Partnership | EXCLUDED | EXCLUDED — S-10 requires Acumatica platform | — | — |
| S-11 BeBanking Product Overview | EXCLUDED | EXCLUDED — S-11 requires BeBanking platform | — | — |
| S-12 B-BBEE Compliance Statement | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-13 Executive Summary | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-14 Understanding of Requirements | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-15 Proposed Solution Overview | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-16 Oracle Fusion HCM Capability | DEFAULT_EXCLUDED | COND-HCM — no driver assets selected | — | — |
| S-17 Oracle Fusion ERP Capability | MANDATORY | COND-ERP — drivers: ['W2S1-001'] | W2S1-001 | — |
| S-18 Oracle EBS Capability | DEFAULT_EXCLUDED | COND-EBS — no driver assets selected | — | — |
| S-19 Oracle OIC / Integration Capability | MANDATORY | COND-OIC — drivers: ['W4-INT-001-ORA-OICAccelerators'] | W4-INT-001-ORA-OICAccelerators | — |
| S-20 Oracle DBA Capability | DEFAULT_EXCLUDED | COND-DBA — no driver assets selected | — | — |
| S-21 Oracle Managed Services Capability | EXCLUDED | EXCLUDED — S-21 applies to AMS only | — | — |
| S-22 OCI Infrastructure | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-23 Acumatica Financials | EXCLUDED | EXCLUDED — S-23 requires Acumatica platform | — | — |
| S-24 Acumatica Distribution | EXCLUDED | EXCLUDED — S-24 requires Acumatica platform | — | — |
| S-25 Acumatica Manufacturing | EXCLUDED | EXCLUDED — S-25 requires Acumatica platform | — | — |
| S-26 Acumatica CRM | EXCLUDED | EXCLUDED — S-26 requires Acumatica platform | — | — |
| S-27 Acumatica Other Modules | EXCLUDED | EXCLUDED — S-27 requires Acumatica platform | — | — |
| S-28 Acumatica Managed Services | EXCLUDED | EXCLUDED — S-28 requires Acumatica AMS | — | — |
| S-29 BeBanking H2H Banking | EXCLUDED | EXCLUDED — S-29 requires BeBanking platform | — | — |
| S-30 Scope of Work — Inclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-31 Scope of Work — Exclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-32 Deliverables | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-33 Dependencies | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-34 Implementation Methodology | MANDATORY | M-ALL — mandatory in all proposals | W2S1-005-ORA-ImplementationMethodology | SI-001 |
| S-35 Project Plan / Timeline | MANDATORY | M-ALL — mandatory in all proposals | — | SI-001 |
| S-36 Project Governance | MANDATORY | M-ALL — governance mandatory in all proposals | W2S1-005-ORA-ImplementationMethodology | — |
| S-37 RAID Framework | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-38 Change Control Framework | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-001 |
| S-39 Testing Strategy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-40 Data Migration | DEFAULT_EXCLUDED | COND-MIG — no driver assets selected | — | — |
| S-41 Training Plan | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-42 Cutover / Go-Live Plan | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-43 Hypercare / Post-Go-Live Transition | DEFAULT_EXCLUDED | COND-POST-GOLIVE — no driver assets selected | — | — |
| S-44 Disaster Recovery | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-45 Security Architecture | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-46 Team Structure | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-47 Named Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-48 Consultant Profiles (Summary) | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-49 Key Assumptions (Body Section) | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1 | SI-006 |
| S-50 Risk Register | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-51 Commercial Assumptions | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1 | — |
| S-52 Commercials / Pricing | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-006 |
| S-53 Rate Card Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-54 Estimation Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-55 Compliance Schedule | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-56 Company Registration | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-57 Tax Clearance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-58 Directors' Resolution | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-59 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| S-60 Public Liability Insurance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-61 Professional Indemnity | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-62 Oracle OPN Certificate | MANDATORY | COND-ORA — platform=Oracle Integration Cloud; drivers: ['W1S1-003'] | W1S1-003 | — |
| S-63 Acumatica Partner Certificate | EXCLUDED | EXCLUDED — S-63 requires Acumatica platform | — | — |
| S-64 ISO / Other Certifications | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-65 POPIA Policy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-66 PAIA Manual | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-67 Client References | MANDATORY | M-ALL — mandatory in all proposals | — | SI-005 |
| S-68 Case Studies | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-69 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | SI-005 |
| S-70 Support Model | EXCLUDED | EXCLUDED — S-70 applies to AMS engagements only | — | SI-001 |
| S-71 SLA Framework | EXCLUDED | EXCLUDED — S-71 applies to AMS engagements only | — | SI-001, SI-007 |
| S-72 Incident Management | EXCLUDED | EXCLUDED — S-72 applies to AMS engagements only | — | SI-001, SI-007 |
| S-73 Change Request Process | EXCLUDED | EXCLUDED — S-73 applies to AMS engagements only | — | SI-001 |
| S-74 Resource Model (AMS) | EXCLUDED | EXCLUDED — S-74 applies to AMS engagements only | — | SI-001 |
| S-75 Release Management | EXCLUDED | EXCLUDED — S-75 applies to AMS engagements only | — | SI-001 |
| S-76 Monitoring and Reporting | EXCLUDED | EXCLUDED — S-76 applies to AMS engagements only | — | SI-001 |
| A-01 Complete Assumption Schedule | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1 | — |
| A-02 Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| A-03 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| A-04 Certifications and Compliance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| A-05 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| A-06 Company Registration | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |

---

## REG-ERP-P7-FULLSUITE — Oracle ERP Cloud Implementation

### Full Section Traceability

| Section | Status | Rationale | Source Assets | SI Rules |
|---|---|---|---|---|
| S-01 Cover Page / Transmittal | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-02 Table of Contents | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-03 Company Overview | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-04 Company History | MANDATORY | M-ALL — mandatory in all proposals | W1S1-002 | — |
| S-05 Awards and Recognition | MANDATORY | M-ALL — mandatory in all proposals | W1S1-006 | — |
| S-06 Delivery Model | MANDATORY | M-ALL — mandatory in all proposals | W1S1-007 | — |
| S-07 Geographic Presence | MANDATORY | M-ALL — mandatory in all proposals | W1S1-008 | — |
| S-08 Key Differentiators | MANDATORY | OPT — driver assets selected: ['W1S1-009'] | W1S1-009 | — |
| S-09 Oracle Partnership | MANDATORY | COND-ORA — platform=Oracle ERP Cloud; drivers: ['W1S1-003'] | W1S1-003 | — |
| S-10 Acumatica Partnership | EXCLUDED | EXCLUDED — S-10 requires Acumatica platform | — | — |
| S-11 BeBanking Product Overview | EXCLUDED | EXCLUDED — S-11 requires BeBanking platform | — | — |
| S-12 B-BBEE Compliance Statement | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-13 Executive Summary | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-14 Understanding of Requirements | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-15 Proposed Solution Overview | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-16 Oracle Fusion HCM Capability | DEFAULT_EXCLUDED | COND-HCM — no driver assets selected | — | — |
| S-17 Oracle Fusion ERP Capability | MANDATORY | COND-ERP — drivers: ['W2S1-001', 'W4-ERP-001-ORA-FusionFinancials', 'W4-ERP-002-ORA-FusionProcurement', 'W4-ERP-003-ORA-PPM'] | W2S1-001, W4-ERP-001-ORA-FusionFinancials, W4-ERP-002-ORA-FusionProcurement, W4-ERP-003-ORA-PPM | — |
| S-18 Oracle EBS Capability | DEFAULT_EXCLUDED | COND-EBS — no driver assets selected | — | — |
| S-19 Oracle OIC / Integration Capability | OPTIONAL_SELECTED | COND-OIC — drivers: ['W4-INT-001-ORA-OICAccelerators'] | W4-INT-001-ORA-OICAccelerators | — |
| S-20 Oracle DBA Capability | DEFAULT_EXCLUDED | COND-DBA — no driver assets selected | — | — |
| S-21 Oracle Managed Services Capability | EXCLUDED | EXCLUDED — S-21 applies to AMS only | — | — |
| S-22 OCI Infrastructure | MANDATORY | COND-OCI — drivers: ['OCI-ASSUMPTIONS-V1'] | OCI-ASSUMPTIONS-V1 | — |
| S-23 Acumatica Financials | EXCLUDED | EXCLUDED — S-23 requires Acumatica platform | — | — |
| S-24 Acumatica Distribution | EXCLUDED | EXCLUDED — S-24 requires Acumatica platform | — | — |
| S-25 Acumatica Manufacturing | EXCLUDED | EXCLUDED — S-25 requires Acumatica platform | — | — |
| S-26 Acumatica CRM | EXCLUDED | EXCLUDED — S-26 requires Acumatica platform | — | — |
| S-27 Acumatica Other Modules | EXCLUDED | EXCLUDED — S-27 requires Acumatica platform | — | — |
| S-28 Acumatica Managed Services | EXCLUDED | EXCLUDED — S-28 requires Acumatica AMS | — | — |
| S-29 BeBanking H2H Banking | EXCLUDED | EXCLUDED — S-29 requires BeBanking platform | — | — |
| S-30 Scope of Work — Inclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-31 Scope of Work — Exclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-32 Deliverables | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-33 Dependencies | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-34 Implementation Methodology | MANDATORY | M-ALL — mandatory in all proposals | W2S1-005-ORA-ImplementationMethodology | SI-001 |
| S-35 Project Plan / Timeline | MANDATORY | M-ALL — mandatory in all proposals | — | SI-001 |
| S-36 Project Governance | MANDATORY | M-ALL — governance mandatory in all proposals | W2S1-005-ORA-ImplementationMethodology | — |
| S-37 RAID Framework | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-38 Change Control Framework | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-001 |
| S-39 Testing Strategy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-40 Data Migration | DEFAULT_EXCLUDED | COND-MIG — no driver assets selected | — | — |
| S-41 Training Plan | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-42 Cutover / Go-Live Plan | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-43 Hypercare / Post-Go-Live Transition | DEFAULT_EXCLUDED | COND-POST-GOLIVE — no driver assets selected | — | — |
| S-44 Disaster Recovery | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-45 Security Architecture | MANDATORY | COND-OCI — drivers: ['OCI-ASSUMPTIONS-V1'] | OCI-ASSUMPTIONS-V1 | — |
| S-46 Team Structure | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-47 Named Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-48 Consultant Profiles (Summary) | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-49 Key Assumptions (Body Section) | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, OCI-ASSUMPTIONS-V1 | SI-006 |
| S-50 Risk Register | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-51 Commercial Assumptions | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, OCI-ASSUMPTIONS-V1 | — |
| S-52 Commercials / Pricing | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-006 |
| S-53 Rate Card Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-54 Estimation Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-55 Compliance Schedule | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-56 Company Registration | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-57 Tax Clearance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-58 Directors' Resolution | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-59 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| S-60 Public Liability Insurance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-61 Professional Indemnity | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-62 Oracle OPN Certificate | MANDATORY | COND-ORA — platform=Oracle ERP Cloud; drivers: ['W1S1-003'] | W1S1-003 | — |
| S-63 Acumatica Partner Certificate | EXCLUDED | EXCLUDED — S-63 requires Acumatica platform | — | — |
| S-64 ISO / Other Certifications | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-65 POPIA Policy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-66 PAIA Manual | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-67 Client References | MANDATORY | M-ALL — mandatory in all proposals | — | SI-005 |
| S-68 Case Studies | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-69 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | SI-005 |
| S-70 Support Model | EXCLUDED | EXCLUDED — S-70 applies to AMS engagements only | — | SI-001 |
| S-71 SLA Framework | EXCLUDED | EXCLUDED — S-71 applies to AMS engagements only | — | SI-001, SI-007 |
| S-72 Incident Management | EXCLUDED | EXCLUDED — S-72 applies to AMS engagements only | — | SI-001, SI-007 |
| S-73 Change Request Process | EXCLUDED | EXCLUDED — S-73 applies to AMS engagements only | — | SI-001 |
| S-74 Resource Model (AMS) | EXCLUDED | EXCLUDED — S-74 applies to AMS engagements only | — | SI-001 |
| S-75 Release Management | EXCLUDED | EXCLUDED — S-75 applies to AMS engagements only | — | SI-001 |
| S-76 Monitoring and Reporting | EXCLUDED | EXCLUDED — S-76 applies to AMS engagements only | — | SI-001 |
| A-01 Complete Assumption Schedule | MANDATORY | M-FIXED — mandatory in all proposals | OIC-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, OCI-ASSUMPTIONS-V1 | — |
| A-02 Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| A-03 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| A-04 Certifications and Compliance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| A-05 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| A-06 Company Registration | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |

---

## REG-ACU-P11 — Acumatica Implementation

### Full Section Traceability

| Section | Status | Rationale | Source Assets | SI Rules |
|---|---|---|---|---|
| S-01 Cover Page / Transmittal | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-02 Table of Contents | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-03 Company Overview | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-04 Company History | MANDATORY | M-ALL — mandatory in all proposals | W1S1-002 | — |
| S-05 Awards and Recognition | MANDATORY | M-ALL — mandatory in all proposals | W1S1-006 | — |
| S-06 Delivery Model | MANDATORY | M-ALL — mandatory in all proposals | W1S1-007 | — |
| S-07 Geographic Presence | MANDATORY | M-ALL — mandatory in all proposals | W1S1-008 | — |
| S-08 Key Differentiators | MANDATORY | OPT — driver assets selected: ['W1S1-009'] | W1S1-009 | — |
| S-09 Oracle Partnership | EXCLUDED | EXCLUDED — S-09 requires Oracle platform; platform=Acumatica | — | — |
| S-10 Acumatica Partnership | MANDATORY | COND-ACU — platform=Acumatica; drivers: ['W1S1-004'] | W1S1-004 | — |
| S-11 BeBanking Product Overview | EXCLUDED | EXCLUDED — S-11 requires BeBanking platform | — | — |
| S-12 B-BBEE Compliance Statement | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-13 Executive Summary | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-14 Understanding of Requirements | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-15 Proposed Solution Overview | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-16 Oracle Fusion HCM Capability | DEFAULT_EXCLUDED | COND-HCM — no driver assets selected | — | — |
| S-17 Oracle Fusion ERP Capability | DEFAULT_EXCLUDED | COND-ERP — no driver assets selected | — | — |
| S-18 Oracle EBS Capability | DEFAULT_EXCLUDED | COND-EBS — no driver assets selected | — | — |
| S-19 Oracle OIC / Integration Capability | DEFAULT_EXCLUDED | COND-OIC — no driver assets selected | — | — |
| S-20 Oracle DBA Capability | DEFAULT_EXCLUDED | COND-DBA — no driver assets selected | — | — |
| S-21 Oracle Managed Services Capability | EXCLUDED | EXCLUDED — S-21 applies to AMS only | — | — |
| S-22 OCI Infrastructure | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-23 Acumatica Financials | MANDATORY | COND-ACU — platform=Acumatica; drivers: ['W1S2-001'] | W1S2-001 | — |
| S-24 Acumatica Distribution | OPTIONAL_SELECTED | COND-ACU — platform=Acumatica; drivers: ['W1S2-002'] | W1S2-002 | — |
| S-25 Acumatica Manufacturing | OPTIONAL_SELECTED | COND-ACU — platform=Acumatica; drivers: ['W1S2-004'] | W1S2-004 | — |
| S-26 Acumatica CRM | OPTIONAL_SELECTED | COND-ACU — platform=Acumatica; drivers: ['W1S2-005'] | W1S2-005 | — |
| S-27 Acumatica Other Modules | MANDATORY | COND-ACU — platform=Acumatica; drivers: ['W1S2-003', 'W1S2-006-ACU-FieldServices', 'W1S2-007-ACU-PayrollIntegration', 'W1S2-009'] | W1S2-003, W1S2-006-ACU-FieldServices, W1S2-007-ACU-PayrollIntegration, W1S2-009 | — |
| S-28 Acumatica Managed Services | EXCLUDED | EXCLUDED — S-28 requires Acumatica AMS | — | — |
| S-29 BeBanking H2H Banking | EXCLUDED | EXCLUDED — S-29 requires BeBanking platform | — | — |
| S-30 Scope of Work — Inclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-31 Scope of Work — Exclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-32 Deliverables | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-33 Dependencies | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-34 Implementation Methodology | MANDATORY | M-ALL — mandatory in all proposals | W5-METH-001-ERP-ImplementationMethodology | SI-001 |
| S-35 Project Plan / Timeline | MANDATORY | M-ALL — mandatory in all proposals | — | SI-001 |
| S-36 Project Governance | MANDATORY | M-ALL — governance mandatory in all proposals | W5-METH-001-ERP-ImplementationMethodology | — |
| S-37 RAID Framework | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-38 Change Control Framework | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-001 |
| S-39 Testing Strategy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-40 Data Migration | DEFAULT_EXCLUDED | COND-MIG — no driver assets selected | — | — |
| S-41 Training Plan | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-42 Cutover / Go-Live Plan | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-43 Hypercare / Post-Go-Live Transition | DEFAULT_EXCLUDED | COND-POST-GOLIVE — no driver assets selected | — | — |
| S-44 Disaster Recovery | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-45 Security Architecture | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-46 Team Structure | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-47 Named Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-48 Consultant Profiles (Summary) | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-49 Key Assumptions (Body Section) | MANDATORY | M-FIXED — mandatory in all proposals | ACU-BASE-ASSUMPTIONS-V1 | SI-006 |
| S-50 Risk Register | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-51 Commercial Assumptions | MANDATORY | M-FIXED — mandatory in all proposals | ACU-BASE-ASSUMPTIONS-V1 | — |
| S-52 Commercials / Pricing | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-006 |
| S-53 Rate Card Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-54 Estimation Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-55 Compliance Schedule | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-56 Company Registration | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-57 Tax Clearance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-58 Directors' Resolution | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-59 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| S-60 Public Liability Insurance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-61 Professional Indemnity | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-62 Oracle OPN Certificate | EXCLUDED | EXCLUDED — S-62 requires Oracle platform; platform=Acumatica | — | — |
| S-63 Acumatica Partner Certificate | MANDATORY | COND-ACU — platform=Acumatica; drivers: ['W1S1-004'] | W1S1-004 | — |
| S-64 ISO / Other Certifications | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-65 POPIA Policy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-66 PAIA Manual | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-67 Client References | MANDATORY | M-ALL — mandatory in all proposals | — | SI-005 |
| S-68 Case Studies | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-69 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | SI-005 |
| S-70 Support Model | EXCLUDED | EXCLUDED — S-70 applies to AMS engagements only | — | SI-001 |
| S-71 SLA Framework | EXCLUDED | EXCLUDED — S-71 applies to AMS engagements only | — | SI-001, SI-007 |
| S-72 Incident Management | EXCLUDED | EXCLUDED — S-72 applies to AMS engagements only | — | SI-001, SI-007 |
| S-73 Change Request Process | EXCLUDED | EXCLUDED — S-73 applies to AMS engagements only | — | SI-001 |
| S-74 Resource Model (AMS) | EXCLUDED | EXCLUDED — S-74 applies to AMS engagements only | — | SI-001 |
| S-75 Release Management | EXCLUDED | EXCLUDED — S-75 applies to AMS engagements only | — | SI-001 |
| S-76 Monitoring and Reporting | EXCLUDED | EXCLUDED — S-76 applies to AMS engagements only | — | SI-001 |
| A-01 Complete Assumption Schedule | MANDATORY | M-FIXED — mandatory in all proposals | ACU-BASE-ASSUMPTIONS-V1 | — |
| A-02 Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| A-03 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| A-04 Certifications and Compliance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| A-05 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| A-06 Company Registration | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |

---

## REG-BEB-P12 — BeBanking Implementation

### Full Section Traceability

| Section | Status | Rationale | Source Assets | SI Rules |
|---|---|---|---|---|
| S-01 Cover Page / Transmittal | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-02 Table of Contents | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-03 Company Overview | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-04 Company History | MANDATORY | M-ALL — mandatory in all proposals | W1S1-002 | — |
| S-05 Awards and Recognition | MANDATORY | M-ALL — mandatory in all proposals | W1S1-006 | — |
| S-06 Delivery Model | MANDATORY | M-ALL — mandatory in all proposals | W1S1-007 | — |
| S-07 Geographic Presence | MANDATORY | M-ALL — mandatory in all proposals | W1S1-008 | — |
| S-08 Key Differentiators | MANDATORY | OPT — driver assets selected: ['W1S1-009'] | W1S1-009 | — |
| S-09 Oracle Partnership | EXCLUDED | EXCLUDED — S-09 requires Oracle platform; platform=BeBanking | — | — |
| S-10 Acumatica Partnership | EXCLUDED | EXCLUDED — S-10 requires Acumatica platform | — | — |
| S-11 BeBanking Product Overview | MANDATORY | COND-BB — platform=BeBanking; drivers: ['W1S1-005'] | W1S1-005 | — |
| S-12 B-BBEE Compliance Statement | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-13 Executive Summary | MANDATORY | M-ALL — mandatory in all proposals | W1S1-001 | — |
| S-14 Understanding of Requirements | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-15 Proposed Solution Overview | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-16 Oracle Fusion HCM Capability | DEFAULT_EXCLUDED | COND-HCM — no driver assets selected | — | — |
| S-17 Oracle Fusion ERP Capability | DEFAULT_EXCLUDED | COND-ERP — no driver assets selected | — | — |
| S-18 Oracle EBS Capability | DEFAULT_EXCLUDED | COND-EBS — no driver assets selected | — | — |
| S-19 Oracle OIC / Integration Capability | DEFAULT_EXCLUDED | COND-OIC — no driver assets selected | — | — |
| S-20 Oracle DBA Capability | DEFAULT_EXCLUDED | COND-DBA — no driver assets selected | — | — |
| S-21 Oracle Managed Services Capability | EXCLUDED | EXCLUDED — S-21 applies to AMS only | — | — |
| S-22 OCI Infrastructure | DEFAULT_EXCLUDED | COND-OCI — no driver assets selected | — | — |
| S-23 Acumatica Financials | EXCLUDED | EXCLUDED — S-23 requires Acumatica platform | — | — |
| S-24 Acumatica Distribution | EXCLUDED | EXCLUDED — S-24 requires Acumatica platform | — | — |
| S-25 Acumatica Manufacturing | EXCLUDED | EXCLUDED — S-25 requires Acumatica platform | — | — |
| S-26 Acumatica CRM | EXCLUDED | EXCLUDED — S-26 requires Acumatica platform | — | — |
| S-27 Acumatica Other Modules | EXCLUDED | EXCLUDED — S-27 requires Acumatica platform | — | — |
| S-28 Acumatica Managed Services | EXCLUDED | EXCLUDED — S-28 requires Acumatica AMS | — | — |
| S-29 BeBanking H2H Banking | MANDATORY | COND-BB — platform=BeBanking; drivers: ['W1S3-001', 'W1S3-002', 'W1S3-003', 'W1S3-004', 'W1S3-005', 'W1S3-006', 'W1S3-007', 'W1S3-008', 'W1S3-009', 'W1S3-010'] | W1S1-005, W1S3-001, W1S3-002, W1S3-003, W1S3-004, W1S3-005, W1S3-006, W1S3-007, W1S3-008, W1S3-009, W1S3-010 | — |
| S-30 Scope of Work — Inclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-31 Scope of Work — Exclusions | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-32 Deliverables | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-33 Dependencies | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-34 Implementation Methodology | MANDATORY | M-ALL — mandatory in all proposals | W5-METH-001-ERP-ImplementationMethodology | SI-001 |
| S-35 Project Plan / Timeline | MANDATORY | M-ALL — mandatory in all proposals | — | SI-001 |
| S-36 Project Governance | MANDATORY | M-ALL — governance mandatory in all proposals | W5-METH-001-ERP-ImplementationMethodology | — |
| S-37 RAID Framework | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-38 Change Control Framework | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-001 |
| S-39 Testing Strategy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-40 Data Migration | DEFAULT_EXCLUDED | COND-MIG — no driver assets selected | — | — |
| S-41 Training Plan | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-42 Cutover / Go-Live Plan | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-43 Hypercare / Post-Go-Live Transition | DEFAULT_EXCLUDED | COND-POST-GOLIVE — no driver assets selected | — | — |
| S-44 Disaster Recovery | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-45 Security Architecture | MANDATORY | COND-OCI — drivers: ['W1S3-007'] | W1S3-007 | — |
| S-46 Team Structure | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-47 Named Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-48 Consultant Profiles (Summary) | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| S-49 Key Assumptions (Body Section) | MANDATORY | M-FIXED — mandatory in all proposals | BEBANKING-BASE-ASSUMPTIONS-V1 | SI-006 |
| S-50 Risk Register | MANDATORY | M-FIXED — mandatory in all proposals | — | — |
| S-51 Commercial Assumptions | MANDATORY | M-FIXED — mandatory in all proposals | BEBANKING-BASE-ASSUMPTIONS-V1 | — |
| S-52 Commercials / Pricing | MANDATORY | M-FIXED — mandatory in all proposals | — | SI-006 |
| S-53 Rate Card Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-54 Estimation Basis | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-55 Compliance Schedule | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-56 Company Registration | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-57 Tax Clearance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-58 Directors' Resolution | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-59 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| S-60 Public Liability Insurance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| S-61 Professional Indemnity | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-62 Oracle OPN Certificate | EXCLUDED | EXCLUDED — S-62 requires Oracle platform; platform=BeBanking | — | — |
| S-63 Acumatica Partner Certificate | EXCLUDED | EXCLUDED — S-63 requires Acumatica platform | — | — |
| S-64 ISO / Other Certifications | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-65 POPIA Policy | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-66 PAIA Manual | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-67 Client References | MANDATORY | M-ALL — mandatory in all proposals | — | SI-005 |
| S-68 Case Studies | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| S-69 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | SI-005 |
| S-70 Support Model | EXCLUDED | EXCLUDED — S-70 applies to AMS engagements only | — | SI-001 |
| S-71 SLA Framework | EXCLUDED | EXCLUDED — S-71 applies to AMS engagements only | — | SI-001, SI-007 |
| S-72 Incident Management | EXCLUDED | EXCLUDED — S-72 applies to AMS engagements only | — | SI-001, SI-007 |
| S-73 Change Request Process | EXCLUDED | EXCLUDED — S-73 applies to AMS engagements only | — | SI-001 |
| S-74 Resource Model (AMS) | EXCLUDED | EXCLUDED — S-74 applies to AMS engagements only | — | SI-001 |
| S-75 Release Management | EXCLUDED | EXCLUDED — S-75 applies to AMS engagements only | — | SI-001 |
| S-76 Monitoring and Reporting | EXCLUDED | EXCLUDED — S-76 applies to AMS engagements only | — | SI-001 |
| A-01 Complete Assumption Schedule | MANDATORY | M-FIXED — mandatory in all proposals | BEBANKING-BASE-ASSUMPTIONS-V1 | — |
| A-02 Consultant CVs | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | ADR-001 |
| A-03 Reference Letters | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |
| A-04 Certifications and Compliance | MANDATORY | M-ALL — mandatory in all proposals | — | — |
| A-05 B-BBEE Certificate | MANDATORY | M-SA — mandatory in all proposals | — | — |
| A-06 Company Registration | DEFAULT_EXCLUDED | OPT — no condition triggered; not in scope | — | — |

---
