# Proposal Section Assembly Report — PF2-003

**Generated:** 2026-06-30 07:01 UTC  
**Engine:** PSAE v1.0  
**Scenarios:** 6  

---

## Summary

| Tender | Pattern | Platform | Eng Type | Mandatory | Optional | Excluded | Seq | Errors | Warnings |
|---|---|---|---|---|---|---|---|---|---|
| ARM-IT045 | P13 | Oracle EBS | AMS | 43 | 2 | 21 | 45 | PASS | 1 |
| REG-HCM-P3-MINING | P3 | Oracle HCM Cloud | Implementation | 41 | 1 | 18 | 42 | PASS | 0 |
| REG-OIC-P7 | P7 | Oracle Integration Cloud | Implementation | 41 | 0 | 18 | 41 | PASS | 0 |
| REG-ERP-P7-FULLSUITE | P7 | Oracle ERP Cloud | Implementation | 42 | 1 | 18 | 43 | PASS | 0 |
| REG-ACU-P11 | P11 | Acumatica | Implementation | 41 | 3 | 13 | 44 | PASS | 0 |
| REG-BEB-P12 | P12 | BeBanking | Implementation | 40 | 0 | 18 | 40 | PASS | 0 |

---

## ARM-IT045

**Platform:** Oracle EBS  **Pattern:** P13  **Engagement:** AMS  **Industry:** Mining

### Included Sections (assembly order)

| Order | Section | Status | Method | Assets | Human |
|---|---|---|---|---|---|
| 1 | S-01 Cover Page / Transmittal | MANDATORY | TEMPLATE | — | Yes |
| 2 | S-02 Table of Contents | MANDATORY | TEMPLATE | — | Yes |
| 3 | S-03 Company Overview | MANDATORY | DIRECT | W1S1-001 | No |
| 4 | S-04 Company History | MANDATORY | DIRECT | W1S1-002 | No |
| 5 | S-05 Awards and Recognition | MANDATORY | DIRECT | W1S1-006 | Yes |
| 6 | S-06 Delivery Model | MANDATORY | DIRECT | W1S1-007 | No |
| 7 | S-07 Geographic Presence | MANDATORY | DIRECT | W1S1-008 | No |
| 8 | S-08 Key Differentiators | MANDATORY | DIRECT | W1S1-009 | No |
| 9 | S-09 Oracle Partnership | MANDATORY | DIRECT | W1S1-003 | Yes |
| 10 | S-12 B-BBEE Compliance Statement | MANDATORY | DIRECT | — | Yes |
| 11 | S-13 Executive Summary | MANDATORY | AI-GENERATE | W1S1-001 | Yes |
| 12 | S-14 Understanding of Requirements | MANDATORY | AI-GENERATE | — | Yes |
| 13 | S-15 Proposed Solution Overview | MANDATORY | MERGE | — | Yes |
| 14 | S-18 Oracle EBS Capability | MANDATORY | DIRECT | W2S1-002 | Yes |
| 15 | S-19 Oracle OIC / Integration Capability | OPTIONAL_SELECTED | DIRECT | W4-INT-001-ORA-OICAccelerators | No |
| 16 | S-20 Oracle DBA Capability | OPTIONAL_SELECTED | DIRECT | W2S1-003 | Yes |
| 17 | S-21 Oracle Managed Services Capability | MANDATORY | DIRECT | W2S1-004 | No |
| 18 | S-30 Scope of Work — Inclusions | MANDATORY | EXTRACT | — | Yes |
| 19 | S-31 Scope of Work — Exclusions | MANDATORY | EXTRACT | — | Yes |
| 20 | S-32 Deliverables | MANDATORY | EXTRACT | — | Yes |
| 21 | S-33 Dependencies | MANDATORY | EXTRACT | — | Yes |
| 22 | S-36 Project Governance | MANDATORY | EXTRACT | — | No |
| 23 | S-37 RAID Framework | MANDATORY | MERGE | — | Yes |
| 24 | S-74 Resource Model (AMS) | MANDATORY | EXTRACT | AMS-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1, EBS-DRM-ASSUMPTIONS-V1 | No |
| 25 | S-70 Support Model | MANDATORY | MERGE | W2S1-004, AMS-ASSUMPTIONS-V1 | No |
| 26 | S-71 SLA Framework | MANDATORY | EXTRACT | AMS-ASSUMPTIONS-V1, EBS-AMS-SLA-OVERLAY-V1 | No |
| 27 | S-72 Incident Management | MANDATORY | EXTRACT | AMS-ASSUMPTIONS-V1 | No |
| 28 | S-73 Change Request Process | MANDATORY | EXTRACT | AMS-ASSUMPTIONS-V1 | No |
| 29 | S-75 Release Management | MANDATORY | EXTRACT | AMS-ASSUMPTIONS-V1 | No |
| 30 | S-76 Monitoring and Reporting | MANDATORY | EXTRACT | AMS-ASSUMPTIONS-V1 | No |
| 31 | S-49 Key Assumptions (Body Section) | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1 | Yes |
| 32 | S-50 Risk Register | MANDATORY | AI-GENERATE | — | Yes |
| 33 | S-51 Commercial Assumptions | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1 | Yes |
| 34 | S-52 Commercials / Pricing | MANDATORY | PLACEHOLDER | — | Yes |
| 35 | S-55 Compliance Schedule | MANDATORY | EXTRACT | — | Yes |
| 36 | S-56 Company Registration | MANDATORY | DIRECT | — | Yes |
| 37 | S-57 Tax Clearance | MANDATORY | DIRECT | — | Yes |
| 38 | S-58 Directors' Resolution | MANDATORY | DIRECT | — | Yes |
| 39 | S-59 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |
| 40 | S-60 Public Liability Insurance | MANDATORY | DIRECT | — | Yes |
| 41 | S-62 Oracle OPN Certificate | MANDATORY | DIRECT | W1S1-003 | Yes |
| 42 | S-67 Client References | MANDATORY | TEMPLATE | — | Yes |
| 43 | A-01 Complete Assumption Schedule | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1 | Yes |
| 44 | A-04 Certifications and Compliance | MANDATORY | DIRECT | — | Yes |
| 45 | A-05 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |

### Warnings

- GOV-EBS-001: S-18 Oracle EBS content is vintage 2012–2014; review and modernise before submission

### Governance Flags

- GOV-BBEE-001: B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); verify renewal before submission after that date
- GOV-ADR-001: CVs (S-47, S-48, A-02) from APPTime only — never from KB records

---

## REG-HCM-P3-MINING

**Platform:** Oracle HCM Cloud  **Pattern:** P3  **Engagement:** Implementation  **Industry:** Mining

### Included Sections (assembly order)

| Order | Section | Status | Method | Assets | Human |
|---|---|---|---|---|---|
| 1 | S-01 Cover Page / Transmittal | MANDATORY | TEMPLATE | — | Yes |
| 2 | S-02 Table of Contents | MANDATORY | TEMPLATE | — | Yes |
| 3 | S-03 Company Overview | MANDATORY | DIRECT | W1S1-001 | No |
| 4 | S-04 Company History | MANDATORY | DIRECT | W1S1-002 | No |
| 5 | S-05 Awards and Recognition | MANDATORY | DIRECT | W1S1-006 | Yes |
| 6 | S-06 Delivery Model | MANDATORY | DIRECT | W1S1-007 | No |
| 7 | S-07 Geographic Presence | MANDATORY | DIRECT | W1S1-008 | No |
| 8 | S-08 Key Differentiators | MANDATORY | DIRECT | W1S1-009 | No |
| 9 | S-09 Oracle Partnership | MANDATORY | DIRECT | W1S1-003 | Yes |
| 10 | S-12 B-BBEE Compliance Statement | MANDATORY | DIRECT | — | Yes |
| 11 | S-13 Executive Summary | MANDATORY | AI-GENERATE | W1S1-001 | Yes |
| 12 | S-14 Understanding of Requirements | MANDATORY | AI-GENERATE | — | Yes |
| 13 | S-15 Proposed Solution Overview | MANDATORY | MERGE | — | Yes |
| 14 | S-16 Oracle Fusion HCM Capability | MANDATORY | MERGE | W3S1-001-ORA-HCMCore, W3S1-002-ORA-TalentMgmt, W3S1-003-ORA-RecruitingCloud… | No |
| 15 | S-17 Oracle Fusion ERP Capability | OPTIONAL_SELECTED | MERGE | W2S1-001 | No |
| 16 | S-19 Oracle OIC / Integration Capability | MANDATORY | DIRECT | W3S1-009-ORA-PayrollInterface-Integration, W4-INT-001-ORA-OICAccelerators | No |
| 17 | S-30 Scope of Work — Inclusions | MANDATORY | EXTRACT | — | Yes |
| 18 | S-31 Scope of Work — Exclusions | MANDATORY | EXTRACT | — | Yes |
| 19 | S-32 Deliverables | MANDATORY | EXTRACT | — | Yes |
| 20 | S-33 Dependencies | MANDATORY | EXTRACT | — | Yes |
| 21 | S-34 Implementation Methodology | MANDATORY | DIRECT | W2S1-005-ORA-ImplementationMethodology | Yes |
| 22 | S-35 Project Plan / Timeline | MANDATORY | TEMPLATE | — | Yes |
| 23 | S-36 Project Governance | MANDATORY | EXTRACT | W2S1-005-ORA-ImplementationMethodology | No |
| 24 | S-37 RAID Framework | MANDATORY | MERGE | — | Yes |
| 25 | S-38 Change Control Framework | MANDATORY | DIRECT | — | No |
| 26 | S-42 Cutover / Go-Live Plan | MANDATORY | EXTRACT | — | Yes |
| 27 | S-46 Team Structure | MANDATORY | TEMPLATE | — | Yes |
| 28 | S-49 Key Assumptions (Body Section) | MANDATORY | MERGE | HCM-BASE-ASSUMPTIONS-V1, HCM-RECRUITING-ASSUMPTIONS-V1, HCM-LEARNING-ASSUMPTIONS-V1… | Yes |
| 29 | S-50 Risk Register | MANDATORY | AI-GENERATE | — | Yes |
| 30 | S-51 Commercial Assumptions | MANDATORY | MERGE | HCM-BASE-ASSUMPTIONS-V1, HCM-RECRUITING-ASSUMPTIONS-V1, HCM-LEARNING-ASSUMPTIONS-V1… | Yes |
| 31 | S-52 Commercials / Pricing | MANDATORY | PLACEHOLDER | — | Yes |
| 32 | S-55 Compliance Schedule | MANDATORY | EXTRACT | — | Yes |
| 33 | S-56 Company Registration | MANDATORY | DIRECT | — | Yes |
| 34 | S-57 Tax Clearance | MANDATORY | DIRECT | — | Yes |
| 35 | S-58 Directors' Resolution | MANDATORY | DIRECT | — | Yes |
| 36 | S-59 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |
| 37 | S-60 Public Liability Insurance | MANDATORY | DIRECT | — | Yes |
| 38 | S-62 Oracle OPN Certificate | MANDATORY | DIRECT | W1S1-003 | Yes |
| 39 | S-67 Client References | MANDATORY | TEMPLATE | — | Yes |
| 40 | A-01 Complete Assumption Schedule | MANDATORY | MERGE | HCM-BASE-ASSUMPTIONS-V1, HCM-RECRUITING-ASSUMPTIONS-V1, HCM-LEARNING-ASSUMPTIONS-V1… | Yes |
| 41 | A-04 Certifications and Compliance | MANDATORY | DIRECT | — | Yes |
| 42 | A-05 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |

### Governance Flags

- GOV-BBEE-001: B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); verify renewal before submission after that date
- GOV-ADR-001: CVs (S-47, S-48, A-02) from APPTime only — never from KB records

---

## REG-OIC-P7

**Platform:** Oracle Integration Cloud  **Pattern:** P7  **Engagement:** Implementation  **Industry:** Financial-Services

### Included Sections (assembly order)

| Order | Section | Status | Method | Assets | Human |
|---|---|---|---|---|---|
| 1 | S-01 Cover Page / Transmittal | MANDATORY | TEMPLATE | — | Yes |
| 2 | S-02 Table of Contents | MANDATORY | TEMPLATE | — | Yes |
| 3 | S-03 Company Overview | MANDATORY | DIRECT | W1S1-001 | No |
| 4 | S-04 Company History | MANDATORY | DIRECT | W1S1-002 | No |
| 5 | S-05 Awards and Recognition | MANDATORY | DIRECT | W1S1-006 | Yes |
| 6 | S-06 Delivery Model | MANDATORY | DIRECT | W1S1-007 | No |
| 7 | S-07 Geographic Presence | MANDATORY | DIRECT | W1S1-008 | No |
| 8 | S-08 Key Differentiators | MANDATORY | DIRECT | W1S1-009 | No |
| 9 | S-09 Oracle Partnership | MANDATORY | DIRECT | W1S1-003 | Yes |
| 10 | S-12 B-BBEE Compliance Statement | MANDATORY | DIRECT | — | Yes |
| 11 | S-13 Executive Summary | MANDATORY | AI-GENERATE | W1S1-001 | Yes |
| 12 | S-14 Understanding of Requirements | MANDATORY | AI-GENERATE | — | Yes |
| 13 | S-15 Proposed Solution Overview | MANDATORY | MERGE | — | Yes |
| 14 | S-17 Oracle Fusion ERP Capability | MANDATORY | MERGE | W2S1-001 | No |
| 15 | S-19 Oracle OIC / Integration Capability | MANDATORY | DIRECT | W4-INT-001-ORA-OICAccelerators | No |
| 16 | S-30 Scope of Work — Inclusions | MANDATORY | EXTRACT | — | Yes |
| 17 | S-31 Scope of Work — Exclusions | MANDATORY | EXTRACT | — | Yes |
| 18 | S-32 Deliverables | MANDATORY | EXTRACT | — | Yes |
| 19 | S-33 Dependencies | MANDATORY | EXTRACT | — | Yes |
| 20 | S-34 Implementation Methodology | MANDATORY | DIRECT | W2S1-005-ORA-ImplementationMethodology | Yes |
| 21 | S-35 Project Plan / Timeline | MANDATORY | TEMPLATE | — | Yes |
| 22 | S-36 Project Governance | MANDATORY | EXTRACT | W2S1-005-ORA-ImplementationMethodology | No |
| 23 | S-37 RAID Framework | MANDATORY | MERGE | — | Yes |
| 24 | S-38 Change Control Framework | MANDATORY | DIRECT | — | No |
| 25 | S-42 Cutover / Go-Live Plan | MANDATORY | EXTRACT | — | Yes |
| 26 | S-46 Team Structure | MANDATORY | TEMPLATE | — | Yes |
| 27 | S-49 Key Assumptions (Body Section) | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1 | Yes |
| 28 | S-50 Risk Register | MANDATORY | AI-GENERATE | — | Yes |
| 29 | S-51 Commercial Assumptions | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1 | Yes |
| 30 | S-52 Commercials / Pricing | MANDATORY | PLACEHOLDER | — | Yes |
| 31 | S-55 Compliance Schedule | MANDATORY | EXTRACT | — | Yes |
| 32 | S-56 Company Registration | MANDATORY | DIRECT | — | Yes |
| 33 | S-57 Tax Clearance | MANDATORY | DIRECT | — | Yes |
| 34 | S-58 Directors' Resolution | MANDATORY | DIRECT | — | Yes |
| 35 | S-59 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |
| 36 | S-60 Public Liability Insurance | MANDATORY | DIRECT | — | Yes |
| 37 | S-62 Oracle OPN Certificate | MANDATORY | DIRECT | W1S1-003 | Yes |
| 38 | S-67 Client References | MANDATORY | TEMPLATE | — | Yes |
| 39 | A-01 Complete Assumption Schedule | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1 | Yes |
| 40 | A-04 Certifications and Compliance | MANDATORY | DIRECT | — | Yes |
| 41 | A-05 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |

### Governance Flags

- GOV-BBEE-001: B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); verify renewal before submission after that date
- GOV-ADR-001: CVs (S-47, S-48, A-02) from APPTime only — never from KB records

---

## REG-ERP-P7-FULLSUITE

**Platform:** Oracle ERP Cloud  **Pattern:** P7  **Engagement:** Implementation  **Industry:** Manufacturing

### Included Sections (assembly order)

| Order | Section | Status | Method | Assets | Human |
|---|---|---|---|---|---|
| 1 | S-01 Cover Page / Transmittal | MANDATORY | TEMPLATE | — | Yes |
| 2 | S-02 Table of Contents | MANDATORY | TEMPLATE | — | Yes |
| 3 | S-03 Company Overview | MANDATORY | DIRECT | W1S1-001 | No |
| 4 | S-04 Company History | MANDATORY | DIRECT | W1S1-002 | No |
| 5 | S-05 Awards and Recognition | MANDATORY | DIRECT | W1S1-006 | Yes |
| 6 | S-06 Delivery Model | MANDATORY | DIRECT | W1S1-007 | No |
| 7 | S-07 Geographic Presence | MANDATORY | DIRECT | W1S1-008 | No |
| 8 | S-08 Key Differentiators | MANDATORY | DIRECT | W1S1-009 | No |
| 9 | S-09 Oracle Partnership | MANDATORY | DIRECT | W1S1-003 | Yes |
| 10 | S-12 B-BBEE Compliance Statement | MANDATORY | DIRECT | — | Yes |
| 11 | S-13 Executive Summary | MANDATORY | AI-GENERATE | W1S1-001 | Yes |
| 12 | S-14 Understanding of Requirements | MANDATORY | AI-GENERATE | — | Yes |
| 13 | S-15 Proposed Solution Overview | MANDATORY | MERGE | — | Yes |
| 14 | S-17 Oracle Fusion ERP Capability | MANDATORY | MERGE | W2S1-001, W4-ERP-001-ORA-FusionFinancials, W4-ERP-002-ORA-FusionProcurement… | No |
| 15 | S-19 Oracle OIC / Integration Capability | OPTIONAL_SELECTED | DIRECT | W4-INT-001-ORA-OICAccelerators | No |
| 16 | S-22 OCI Infrastructure | MANDATORY | AI-GENERATE | OCI-ASSUMPTIONS-V1 | Yes |
| 17 | S-30 Scope of Work — Inclusions | MANDATORY | EXTRACT | — | Yes |
| 18 | S-31 Scope of Work — Exclusions | MANDATORY | EXTRACT | — | Yes |
| 19 | S-32 Deliverables | MANDATORY | EXTRACT | — | Yes |
| 20 | S-33 Dependencies | MANDATORY | EXTRACT | — | Yes |
| 21 | S-34 Implementation Methodology | MANDATORY | DIRECT | W2S1-005-ORA-ImplementationMethodology | Yes |
| 22 | S-35 Project Plan / Timeline | MANDATORY | TEMPLATE | — | Yes |
| 23 | S-36 Project Governance | MANDATORY | EXTRACT | W2S1-005-ORA-ImplementationMethodology | No |
| 24 | S-37 RAID Framework | MANDATORY | MERGE | — | Yes |
| 25 | S-38 Change Control Framework | MANDATORY | DIRECT | — | No |
| 26 | S-42 Cutover / Go-Live Plan | MANDATORY | EXTRACT | — | Yes |
| 27 | S-45 Security Architecture | MANDATORY | EXTRACT | OCI-ASSUMPTIONS-V1 | Yes |
| 28 | S-46 Team Structure | MANDATORY | TEMPLATE | — | Yes |
| 29 | S-49 Key Assumptions (Body Section) | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, OCI-ASSUMPTIONS-V1 | Yes |
| 30 | S-50 Risk Register | MANDATORY | AI-GENERATE | — | Yes |
| 31 | S-51 Commercial Assumptions | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, OCI-ASSUMPTIONS-V1 | Yes |
| 32 | S-52 Commercials / Pricing | MANDATORY | PLACEHOLDER | — | Yes |
| 33 | S-55 Compliance Schedule | MANDATORY | EXTRACT | — | Yes |
| 34 | S-56 Company Registration | MANDATORY | DIRECT | — | Yes |
| 35 | S-57 Tax Clearance | MANDATORY | DIRECT | — | Yes |
| 36 | S-58 Directors' Resolution | MANDATORY | DIRECT | — | Yes |
| 37 | S-59 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |
| 38 | S-60 Public Liability Insurance | MANDATORY | DIRECT | — | Yes |
| 39 | S-62 Oracle OPN Certificate | MANDATORY | DIRECT | W1S1-003 | Yes |
| 40 | S-67 Client References | MANDATORY | TEMPLATE | — | Yes |
| 41 | A-01 Complete Assumption Schedule | MANDATORY | MERGE | OIC-ASSUMPTIONS-V1, ERP-ASSUMPTIONS-V1, OCI-ASSUMPTIONS-V1 | Yes |
| 42 | A-04 Certifications and Compliance | MANDATORY | DIRECT | — | Yes |
| 43 | A-05 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |

### Governance Flags

- GOV-BBEE-001: B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); verify renewal before submission after that date
- GOV-ADR-001: CVs (S-47, S-48, A-02) from APPTime only — never from KB records

---

## REG-ACU-P11

**Platform:** Acumatica  **Pattern:** P11  **Engagement:** Implementation  **Industry:** Distribution

### Included Sections (assembly order)

| Order | Section | Status | Method | Assets | Human |
|---|---|---|---|---|---|
| 1 | S-01 Cover Page / Transmittal | MANDATORY | TEMPLATE | — | Yes |
| 2 | S-02 Table of Contents | MANDATORY | TEMPLATE | — | Yes |
| 3 | S-03 Company Overview | MANDATORY | DIRECT | W1S1-001 | No |
| 4 | S-04 Company History | MANDATORY | DIRECT | W1S1-002 | No |
| 5 | S-05 Awards and Recognition | MANDATORY | DIRECT | W1S1-006 | Yes |
| 6 | S-06 Delivery Model | MANDATORY | DIRECT | W1S1-007 | No |
| 7 | S-07 Geographic Presence | MANDATORY | DIRECT | W1S1-008 | No |
| 8 | S-08 Key Differentiators | MANDATORY | DIRECT | W1S1-009 | No |
| 9 | S-10 Acumatica Partnership | MANDATORY | DIRECT | W1S1-004 | Yes |
| 10 | S-12 B-BBEE Compliance Statement | MANDATORY | DIRECT | — | Yes |
| 11 | S-13 Executive Summary | MANDATORY | AI-GENERATE | W1S1-001 | Yes |
| 12 | S-14 Understanding of Requirements | MANDATORY | AI-GENERATE | — | Yes |
| 13 | S-15 Proposed Solution Overview | MANDATORY | MERGE | — | Yes |
| 14 | S-23 Acumatica Financials | MANDATORY | DIRECT | W1S2-001 | No |
| 15 | S-24 Acumatica Distribution | OPTIONAL_SELECTED | DIRECT | W1S2-002 | No |
| 16 | S-25 Acumatica Manufacturing | OPTIONAL_SELECTED | DIRECT | W1S2-004 | No |
| 17 | S-26 Acumatica CRM | OPTIONAL_SELECTED | DIRECT | W1S2-005 | No |
| 18 | S-27 Acumatica Other Modules | MANDATORY | DIRECT | W1S2-003, W1S2-006-ACU-FieldServices, W1S2-007-ACU-PayrollIntegration… | No |
| 19 | S-30 Scope of Work — Inclusions | MANDATORY | EXTRACT | — | Yes |
| 20 | S-31 Scope of Work — Exclusions | MANDATORY | EXTRACT | — | Yes |
| 21 | S-32 Deliverables | MANDATORY | EXTRACT | — | Yes |
| 22 | S-33 Dependencies | MANDATORY | EXTRACT | — | Yes |
| 23 | S-34 Implementation Methodology | MANDATORY | DIRECT | W5-METH-001-ERP-ImplementationMethodology | Yes |
| 24 | S-35 Project Plan / Timeline | MANDATORY | TEMPLATE | — | Yes |
| 25 | S-36 Project Governance | MANDATORY | EXTRACT | W5-METH-001-ERP-ImplementationMethodology | No |
| 26 | S-37 RAID Framework | MANDATORY | MERGE | — | Yes |
| 27 | S-38 Change Control Framework | MANDATORY | DIRECT | — | No |
| 28 | S-42 Cutover / Go-Live Plan | MANDATORY | EXTRACT | — | Yes |
| 29 | S-46 Team Structure | MANDATORY | TEMPLATE | — | Yes |
| 30 | S-49 Key Assumptions (Body Section) | MANDATORY | MERGE | ACU-BASE-ASSUMPTIONS-V1 | Yes |
| 31 | S-50 Risk Register | MANDATORY | AI-GENERATE | — | Yes |
| 32 | S-51 Commercial Assumptions | MANDATORY | MERGE | ACU-BASE-ASSUMPTIONS-V1 | Yes |
| 33 | S-52 Commercials / Pricing | MANDATORY | PLACEHOLDER | — | Yes |
| 34 | S-55 Compliance Schedule | MANDATORY | EXTRACT | — | Yes |
| 35 | S-56 Company Registration | MANDATORY | DIRECT | — | Yes |
| 36 | S-57 Tax Clearance | MANDATORY | DIRECT | — | Yes |
| 37 | S-58 Directors' Resolution | MANDATORY | DIRECT | — | Yes |
| 38 | S-59 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |
| 39 | S-60 Public Liability Insurance | MANDATORY | DIRECT | — | Yes |
| 40 | S-63 Acumatica Partner Certificate | MANDATORY | DIRECT | W1S1-004 | Yes |
| 41 | S-67 Client References | MANDATORY | TEMPLATE | — | Yes |
| 42 | A-01 Complete Assumption Schedule | MANDATORY | MERGE | ACU-BASE-ASSUMPTIONS-V1 | Yes |
| 43 | A-04 Certifications and Compliance | MANDATORY | DIRECT | — | Yes |
| 44 | A-05 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |

### Governance Flags

- GOV-BBEE-001: B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); verify renewal before submission after that date
- GOV-ADR-001: CVs (S-47, S-48, A-02) from APPTime only — never from KB records

---

## REG-BEB-P12

**Platform:** BeBanking  **Pattern:** P12  **Engagement:** Implementation  **Industry:** Banking

### Included Sections (assembly order)

| Order | Section | Status | Method | Assets | Human |
|---|---|---|---|---|---|
| 1 | S-01 Cover Page / Transmittal | MANDATORY | TEMPLATE | — | Yes |
| 2 | S-02 Table of Contents | MANDATORY | TEMPLATE | — | Yes |
| 3 | S-03 Company Overview | MANDATORY | DIRECT | W1S1-001 | No |
| 4 | S-04 Company History | MANDATORY | DIRECT | W1S1-002 | No |
| 5 | S-05 Awards and Recognition | MANDATORY | DIRECT | W1S1-006 | Yes |
| 6 | S-06 Delivery Model | MANDATORY | DIRECT | W1S1-007 | No |
| 7 | S-07 Geographic Presence | MANDATORY | DIRECT | W1S1-008 | No |
| 8 | S-08 Key Differentiators | MANDATORY | DIRECT | W1S1-009 | No |
| 9 | S-11 BeBanking Product Overview | MANDATORY | DIRECT | W1S1-005 | No |
| 10 | S-12 B-BBEE Compliance Statement | MANDATORY | DIRECT | — | Yes |
| 11 | S-13 Executive Summary | MANDATORY | AI-GENERATE | W1S1-001 | Yes |
| 12 | S-14 Understanding of Requirements | MANDATORY | AI-GENERATE | — | Yes |
| 13 | S-15 Proposed Solution Overview | MANDATORY | MERGE | — | Yes |
| 14 | S-29 BeBanking H2H Banking | MANDATORY | MERGE | W1S1-005, W1S3-001, W1S3-002… | No |
| 15 | S-30 Scope of Work — Inclusions | MANDATORY | EXTRACT | — | Yes |
| 16 | S-31 Scope of Work — Exclusions | MANDATORY | EXTRACT | — | Yes |
| 17 | S-32 Deliverables | MANDATORY | EXTRACT | — | Yes |
| 18 | S-33 Dependencies | MANDATORY | EXTRACT | — | Yes |
| 19 | S-34 Implementation Methodology | MANDATORY | DIRECT | W5-METH-001-ERP-ImplementationMethodology | Yes |
| 20 | S-35 Project Plan / Timeline | MANDATORY | TEMPLATE | — | Yes |
| 21 | S-36 Project Governance | MANDATORY | EXTRACT | W5-METH-001-ERP-ImplementationMethodology | No |
| 22 | S-37 RAID Framework | MANDATORY | MERGE | — | Yes |
| 23 | S-38 Change Control Framework | MANDATORY | DIRECT | — | No |
| 24 | S-42 Cutover / Go-Live Plan | MANDATORY | EXTRACT | — | Yes |
| 25 | S-45 Security Architecture | MANDATORY | EXTRACT | W1S3-007 | Yes |
| 26 | S-46 Team Structure | MANDATORY | TEMPLATE | — | Yes |
| 27 | S-49 Key Assumptions (Body Section) | MANDATORY | MERGE | BEBANKING-BASE-ASSUMPTIONS-V1 | Yes |
| 28 | S-50 Risk Register | MANDATORY | AI-GENERATE | — | Yes |
| 29 | S-51 Commercial Assumptions | MANDATORY | MERGE | BEBANKING-BASE-ASSUMPTIONS-V1 | Yes |
| 30 | S-52 Commercials / Pricing | MANDATORY | PLACEHOLDER | — | Yes |
| 31 | S-55 Compliance Schedule | MANDATORY | EXTRACT | — | Yes |
| 32 | S-56 Company Registration | MANDATORY | DIRECT | — | Yes |
| 33 | S-57 Tax Clearance | MANDATORY | DIRECT | — | Yes |
| 34 | S-58 Directors' Resolution | MANDATORY | DIRECT | — | Yes |
| 35 | S-59 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |
| 36 | S-60 Public Liability Insurance | MANDATORY | DIRECT | — | Yes |
| 37 | S-67 Client References | MANDATORY | TEMPLATE | — | Yes |
| 38 | A-01 Complete Assumption Schedule | MANDATORY | MERGE | BEBANKING-BASE-ASSUMPTIONS-V1 | Yes |
| 39 | A-04 Certifications and Compliance | MANDATORY | DIRECT | — | Yes |
| 40 | A-05 B-BBEE Certificate | MANDATORY | DIRECT | — | Yes |

### Governance Flags

- GOV-BBEE-001: B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); verify renewal before submission after that date
- GOV-ADR-001: CVs (S-47, S-48, A-02) from APPTime only — never from KB records

---
