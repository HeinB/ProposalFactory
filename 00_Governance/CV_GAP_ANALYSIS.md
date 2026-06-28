---
document_id: CV_GAP_ANALYSIS
title: "CV Gap Analysis"
version: "1.0"
created: "2026-06-15"
created_by: "WP10 — Consultant Index Programme"
scope: "Missing CVs, expired certifications, single points of failure, and coverage deficits in the consultant corpus"
constraint: "ADR-001 — observations are metadata-level only; no CV narrative content"
---

# CV Gap Analysis

**Assessment date:** 2026-06-15 | **Consultants assessed:** 60 (CONSULTANT_INDEX.csv)  
**Source materials:** Rate Card CVs; Certifications folder; CONSULTANT_SKILL_MATRIX.md

---

## Executive Summary

The consultant corpus is strong in Oracle EBS and Fusion Finance. Key gaps are: (1) 10+ certification holders with no CV on file; (2) Acumatica BU team is largely absent from CONSULTANT_INDEX; (3) BeBanking BU team not registered; (4) three programme managers are contractor/associate (fragile PM bench); (5) Fusion Payroll has a single-person dependency; and (6) certification dates in the EBS folder suggest several certificates are 5–15 years old.

---

## Gap Category 1 — Consultants With Certifications But No CV

These individuals appear only in `Tender Pack/Certifications - Oracle and Other/` — no `_cv.pdf` found in Rate Card root or any named subfolder.

| Consultant | ID | Known Certifications | Action Required |
|---|---|---|---|
| Jordan Kroll | CON-ORA-023 | Oracle Global HR Cloud 2023 | Submit CV + role profile to APPTime/tender folder |
| Gaëlle Pelé | CON-ORA-024 | Oracle Financial Cloud Payables 2023 | Submit CV + role profile |
| Taz Mafukidze | CON-ORA-025 | Oracle Financial Cloud Payables 2024 | Submit CV + role profile |
| AK Sarangi | CON-ORA-026 | Procurement; Inventory; WMS; PPM Cloud (4 certs) | Submit CV + role profile — significant SCM bench depth hidden behind missing CV |
| Johan Kruger | CON-ORA-027 | OCI AI Foundations 2025; Oracle Fusion AI Agent Studio 2025 | Submit CV + role profile — AI specialisation is emerging tender differentiator |
| Sam Vilakazi | CON-ORA-028 | OCI AI Foundations; Foundations Associate 2025 | Submit CV + role profile |
| Mpho Tsotetsi | CON-ORA-029 | Oracle APEX Cloud Developer Professional 2024 | Submit CV + role profile |
| Mpho Mabaso | CON-ORA-031 | Oracle OCP 10g DBA | Submit CV; verify if still active |
| Ridwaan (surname unknown) | CON-ORA-032 | OCP8; OCP9i DBA | Surname required before CV can be registered; verify if still active |
| Cindy — surname TBC | CON-ORA-022 | Oracle Financial Cloud Payables (AP eCertificate) | Surname required; confirm identity |
| Wanda van der Merwe | CON-ORA-030 | Oracle GL + AR 2020; Acumatica CS10; F105 | CV exists in Acumatica BU folder — locate and register in CONSULTANT_INDEX |

**Priority:** HIGH — AK Sarangi (4 SCM certs), Jordan Kroll (HCM), Johan Kruger (AI) represent hidden capability that cannot be marketed until CVs are on file.

---

## Gap Category 2 — Acumatica BU Team Not Registered

The Acumatica practice has 5 active signed reference letters and multiple proposals in HIST — but the Acumatica BU delivery team is not represented in CONSULTANT_INDEX beyond Gavin Sadler (dual Oracle/Acumatica) and Wanda van der Merwe.

| Expected Role | Status | Action |
|---|---|---|
| Acumatica BU Lead (Technical) | Not registered | BU Lead to submit CV and team roster |
| Acumatica Functional Consultant(s) | Not registered | BU Lead to submit CVs |
| BeBanking Product Specialist | Not registered | BU Lead to submit CV |
| Acumatica Project Manager | Not registered | PM CV required for tender resource plans |

**Impact:** Any Acumatica tender requiring a named resource plan cannot be assembled from CONSULTANT_INDEX.  
**Action:** Acumatica BU Lead: submit all team CVs to `Tender Pack/Rate Card/` and rate cards; notify APPTime administrator to create records.

---

## Gap Category 3 — BeBanking BU Team Not Registered

BeBanking has client references (WITS, HyDac) and HIST proposal records but zero named BeBanking consultants in CONSULTANT_INDEX outside of Carin Webb (integration architect via OIC).

| Expected Role | Status | Action |
|---|---|---|
| BeBanking Product Lead | Not registered | Submit CV |
| BeBanking Implementation Consultant | Not registered | Submit CV |

**Impact:** BeBanking tenders cannot display a consultant bench. Carin Webb's OIC/integration coverage is referenced but she is not a BeBanking product consultant.  
**Action:** BeBanking BU Lead: register team by end July 2026.

---

## Gap Category 4 — Expired or Aged Certifications

The following certifications are 5+ years old and may no longer be presented as current evidence of Oracle competency. Oracle certification validity varies by type; many Cloud certifications expire after 1–2 years.

| Consultant | Certification | Year | Age | Status Concern |
|---|---|---|---|---|
| Ian de Koker | Oracle Global HR Cloud 2017 | 2017 | 9 years | EXPIRED — Oracle HCM Cloud versions have changed materially since 2017 |
| Ian de Koker | Oracle Global HR Cloud 2020 | 2020 | 6 years | Likely expired — verify Oracle validity window |
| Ian de Koker | Oracle Recruiting Cloud 2020 | 2020 | 6 years | Likely expired |
| Jono O'Donoghue | OCI Developer 2022 | 2022 | 4 years | Check Oracle OCI renewal requirement |
| Jono O'Donoghue | OIC App Integration 2022 | 2022 | 4 years | Check Oracle OIC renewal requirement |
| Michael Palombo | Oracle HCM Cloud 2019 | 2019 | 7 years | EXPIRED — major HCM Cloud versions since 2019 |
| Riaan du Plessis | OCI Developer 2021 | 2021 | 5 years | Check Oracle OCI renewal requirement |
| Riaan du Plessis | OIC Integration 2021 | 2021 | 5 years | Check Oracle OIC renewal requirement |
| Andre Pelser | OCP DBA; OCP Developer R2; OCP Internet Developer | Pre-2010 | 15+ years | EBS credentials; mark as historical |
| Ridwaan | OCP8; OCP9i DBA | Pre-2005 | 20+ years | Historical only — Oracle 8i/9i retired |
| Mpho Mabaso | OCP 10g DBA | Pre-2010 | 15+ years | Historical only — Oracle 10g retired |
| Wanda van der Merwe | Oracle GL + AR 2020 | 2020 | 6 years | Check Oracle renewal status |
| Daan van der Merwe | Oracle Enterprise Manager CIS 2013 | 2013 | 13 years | Historical only |
| Rahul Dave | Oracle Fusion PPM 2014 | 2014 | 12 years | Historical — product has evolved significantly |
| Rahul Dave | EBS R12 Projects 2016 | 2016 | 10 years | Historical |

**Action:** Oracle BU Lead to audit the certifications folder and identify consultants due for renewal. Priority: Ian de Koker (HCM 2017), Michael Palombo (HCM 2019), Jono O'Donoghue (OCI/OIC 2022), Riaan du Plessis (OCI/OIC 2021).  
**Note:** EBS-era DBAs (Ridwaan, Mpho Mabaso, Andre Pelser) hold historical certifications relevant to EBS support but should not be presented as Cloud-certified.

---

## Gap Category 5 — Consultants Without Identifiable Reference Projects

These consultants appear in CONSULTANT_INDEX but have no link to a named project or reference client that can be cited in a tender. They have functional roles but no reference traceability.

| Consultant | ID | Concern |
|---|---|---|
| Mahlatse Khoza | CON-ORA-017 | Junior DBA — no external reference project; internal support only |
| Marlene Mostert | CON-XBU-004 | PM profile; clients not identified from available CV data |
| Naeem Essop | CON-XBU-005 | SAP background with no Oracle reference projects — limits deployment on Oracle tenders |
| Werner van Niekerk | CON-XBU-007 | SAP primary background; no Oracle reference projects |
| Associates (17 total) | CON-ASC-001 to 017 | All have roles but no named project references linked to APPSolve engagements |

**Action:** For each tender that requires named reference projects per consultant, PM and BU Leads to supply project names. This data belongs in APPTime and should be pulled from APPTime at tender assembly time.

---

## Gap Category 6 — Single Points of Failure (Confirmed)

| SPOF Area | Consultant(s) | Risk Level | Mitigation |
|---|---|---|---|
| Oracle Fusion Payroll | Annatjie Theron only | CRITICAL | Second Fusion Payroll consultant required urgently; training programme for Debbie Blignaut |
| BeBanking OIC Integration | Carin Webb only | HIGH | Cross-train Riaan du Plessis on BeBanking H2H integration pattern |
| OCI Principal Architecture | Jono O'Donoghue primary | HIGH | Francois Terblanche growing into OCI; Johan Kruger AI track; Hein Blignaut has OCI Architect cert |
| Oracle SCM/PPM (Fusion) | AK Sarangi (contractor — no CV on file) | HIGH | Get AK Sarangi CV registered; confirm availability and engagement model |
| APEX Principal Lead | Shaun Cronje + Rahul Dave | MEDIUM | Two APEX principals; Mpho Tsotetsi growing; adequate for current pipeline |
| Programme Management (permanent) | Marlene Mostert only (employee) | MEDIUM | Niel du Toit (associate) provides PM depth; review if additional PM hire needed at >3 concurrent programmes |
| Testing / QA Lead | Sega Phoshoko (associate) | MEDIUM | All test leads are associates; no permanent QA capacity |

---

## Gap Category 7 — Missing Skills Profiles / Domains

Skill domains referenced in tenders where no consultant is registered in CONSULTANT_INDEX:

| Missing Domain | Tender Relevance | Notes |
|---|---|---|
| Oracle EPM (PBCS/EPBCS/FCCS) | Large ERP + FP&A tenders | Kiran built custom IFRS16 EPBCS solution — but not an EPM specialist; no dedicated EPM consultant registered |
| Oracle Analytics Cloud (OAC/OBIEE) | Analytics/BI tender coverage | Daan van der Merwe (OBIEE — EBS era); Rahul Dave (OAC); not a deep bench |
| Oracle Digital Assistant (ODA) | Emerging / AI-adjacent tenders | Johan Kruger (AI Studio cert) is entry-level; no ODA implementation experience cited |
| Acumatica Retail / eCommerce | Retail sector Acumatica tenders | Current Acumatica references are distribution/manufacturing only |
| Oracle Cloud Payroll (Fusion) | Major HCM tenders | Annatjie Theron only; gap confirmed in REFERENCE_GAP_ANALYSIS Gap 4 |
| SAP-to-Oracle Migration | ERP replacement tenders | SAP-background PMs (Naeem, Werner) can advise; but no migration architect |

---

## Priority Action Plan

| Priority | Action | Owner | Target Date |
|---|---|---|---|
| 1 | Obtain CVs for AK Sarangi, Jordan Kroll, Johan Kruger, Mpho Tsotetsi | BU Leads | July 2026 |
| 2 | Acumatica BU Lead submits full team roster and CVs | Acumatica BU Lead | July 2026 |
| 3 | BeBanking BU Lead submits team roster | BeBanking BU Lead | July 2026 |
| 4 | Audit certifications — confirm renewal status for 2022 and older Oracle Cloud certs | Oracle BU Lead | July 2026 |
| 5 | Identify second Oracle Fusion Payroll consultant | Oracle BU Lead | August 2026 |
| 6 | Cross-train Riaan du Plessis on BeBanking H2H integration pattern | Carin Webb | September 2026 |
| 7 | Resolve unknown surnames (Ridwaan, Cindy-AP) | HR / Admin | July 2026 |
| 8 | Register all associate project histories in APPTime | APPTime Admin | Ongoing |

---

*CV_GAP_ANALYSIS v1.0 | Assessment date: 2026-06-15 | See CONSULTANT_INDEX.csv and CONSULTANT_SKILL_MATRIX.md for full detail*
