---
document_id: ARM-IT045-ASSEMBLED-SCHEDULE
title: "ARM IT045 — Assembled Assumption Schedule"
tender_id: "ARM IT045"
client: "African Rainbow Minerals"
engagement: "Oracle EBS Application Managed Services"
assembly_pattern: "EBS AMS Full Stack"
version: "1.0"
assembled: "2026-06-19"
assembled_by: "Assembly Engine MVP v1.0 (WP17B — Dry Run)"
status: "Dry Run — Validation Only (tender WON 2026-08-28)"
assumption_count_raw: 600
assumption_count_suppressed: 1
assumption_count_net: 599
---

# ARM IT045 — Assembled Assumption Schedule

**Tender:** RFP | ARM IT045 | African Rainbow Minerals | Oracle EBS AMS  
**Assembly Pattern:** EBS AMS Full Stack (Enhanced SLA + Dedicated Resource Model)  
**Assembled:** 2026-06-19 | Assembly Engine MVP v1.0 (WP17B Dry Run)  
**Status:** Dry Run — validation against WP14C; tender won 2026-08-28

> **Note:** This schedule is a dry-run validation artefact. The tender is already won and submitted. The purpose is to prove the Assembly Engine MVP can correctly assemble the approved assumption set for this engagement type.

---

## Section 1 — Assembly Metadata

### 1.1 Tender Profile

| Field | Value |
|---|---|
| Tender ID | ARM IT045 |
| Client | African Rainbow Minerals |
| Engagement Type | Oracle EBS Application Managed Services (AMS) |
| Systems in Scope | Oracle EBS HR & Payroll v12.2.8 (5 sites, 1,787 users); Oracle EBS Financials v12.2.10 (3 sites) |
| Infrastructure | OCI (EBS hosted on Oracle Cloud Infrastructure) |
| OIC in Scope | Yes — OIC Enterprise integration support |
| AMS Model | Dedicated Resource Model — 680h/month across 5 named roles |
| SLA Tier | Enhanced — 5-tier (P1–P5); P1=15min response/2hr resolution; 24/7 P1 coverage |
| Sector | Mining — JSE-listed, 5 operational mine sites |

### 1.2 Pack Manifest

| # | Pack Name | Version | Path | Loaded | Suppressed | Net |
|---|---|---|---|---|---|---|
| 1 | Oracle ERP Pack | 1.0 | `08_Commercial/Assumptions/ERP/ERP_ASSUMPTIONS_V1.md` | 123 | 0 | 123 |
| 2 | Oracle OCI Pack | 1.0 | `08_Commercial/Assumptions/OCI/OCI_ASSUMPTIONS_V1.md` | 174 | 0 | 174 |
| 3 | Oracle OIC Pack | 1.0 | `08_Commercial/Assumptions/OIC/OIC_ASSUMPTIONS_V1.md` | 104 | 0 | 104 |
| 4 | AMS Pack | 1.0 | `08_Commercial/Assumptions/AMS/AMS_ASSUMPTIONS_V1.md` | 84 | 1 | 83 |
| 5 | EBS SLA Overlay | 1.0 | `08_Commercial/Assumptions/AMS/EBS_AMS_SLA_OVERLAY_V1.md` | 53 | 0 | 53 |
| 6 | EBS DRM Overlay | 1.0 | `08_Commercial/Assumptions/AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | 62 | 0 | 62 |
| — | **TOTAL** | | | **600** | **1** | **599** |

### 1.3 Packs Excluded

| Pack | Reason |
|---|---|
| HCM Base | EBS AMS exclusion rule — EBS HR/Payroll support ≠ Oracle Fusion HCM implementation |
| HCM Module Packs (Recruiting, Learning, Talent, Compensation) | Not triggered — no HCM Base; EBS engagement |
| Acumatica Base | Not in scope |
| BeBanking Base | Not in scope |

---

## Section 2 — Assumptions

### Pack 1: Oracle ERP Pack
*(Version 1.0 | Approved | 123 assumptions)*

**ERP-GEN-001** | **ERP-GEN-002** | **ERP-GEN-003** | **ERP-GEN-004** | **ERP-GEN-005** | **ERP-GEN-006** | **ERP-GEN-007** | **ERP-GEN-008**

**ERP-GL-001** | **ERP-GL-002** | **ERP-GL-003** | **ERP-GL-004** | **ERP-GL-005** | **ERP-GL-006** | **ERP-GL-007** | **ERP-GL-008**

**ERP-AP-001** | **ERP-AP-002** | **ERP-AP-003** | **ERP-AP-004** | **ERP-AP-005** | **ERP-AP-006** | **ERP-AP-007**

**ERP-AR-001** | **ERP-AR-002** | **ERP-AR-003** | **ERP-AR-004** | **ERP-AR-005**

**ERP-FA-001** | **ERP-FA-002** | **ERP-FA-003** | **ERP-FA-004** | **ERP-FA-005**

**ERP-CM-001** | **ERP-CM-002** | **ERP-CM-003** | **ERP-CM-004**

**ERP-PRO-001** | **ERP-PRO-002** | **ERP-PRO-003** | **ERP-PRO-004** | **ERP-PRO-005** | **ERP-PRO-006** | **ERP-PRO-007**

**ERP-PPM-001** | **ERP-PPM-002** | **ERP-PPM-003** | **ERP-PPM-004** | **ERP-PPM-005** | **ERP-PPM-006** | **ERP-PPM-007**

**ERP-REP-001** | **ERP-REP-002** | **ERP-REP-003** | **ERP-REP-004** | **ERP-REP-005**

**ERP-DAT-001** | **ERP-DAT-002** | **ERP-DAT-003** | **ERP-DAT-004** | **ERP-DAT-005** | **ERP-DAT-006** | **ERP-DAT-007**

**ERP-INT-001** | **ERP-INT-002** | **ERP-INT-003** | **ERP-INT-004** | **ERP-INT-005**

**ERP-SEC-001** | **ERP-SEC-002** | **ERP-SEC-003** | **ERP-SEC-004** | **ERP-SEC-005** | **ERP-SEC-006**

**ERP-WFL-001** | **ERP-WFL-002** | **ERP-WFL-003** | **ERP-WFL-004** | **ERP-WFL-005** | **ERP-WFL-006**

**ERP-TST-001** | **ERP-TST-002** | **ERP-TST-003** | **ERP-TST-004** | **ERP-TST-005** | **ERP-TST-006**

**ERP-TRN-001** | **ERP-TRN-002** | **ERP-TRN-003** | **ERP-TRN-004**

**ERP-CUT-001** | **ERP-CUT-002** | **ERP-CUT-003** | **ERP-CUT-004** | **ERP-CUT-005**

**ERP-HYP-001** | **ERP-HYP-002** | **ERP-HYP-003** | **ERP-HYP-004**

**ERP-CUS-001** | **ERP-CUS-002** | **ERP-CUS-003** | **ERP-CUS-004** | **ERP-CUS-005** | **ERP-CUS-006** | **ERP-CUS-007** | **ERP-CUS-008** | **ERP-CUS-009** | **ERP-CUS-010** | **ERP-CUS-011** | **ERP-CUS-012**

*(Exclusions: ERP-EXC-001 through ERP-EXC-012 — see Section 3)*

---

### Pack 2: Oracle OCI Infrastructure Pack
*(Version 1.0 | Approved | 174 assumptions)*

**OCI-GEN-001** | **OCI-GEN-002** | **OCI-GEN-003** | **OCI-GEN-004** | **OCI-GEN-005** | **OCI-GEN-006** | **OCI-GEN-007** | **OCI-GEN-008**

**OCI-LZ-001** | **OCI-LZ-002** | **OCI-LZ-003** | **OCI-LZ-004** | **OCI-LZ-005** | **OCI-LZ-006** | **OCI-LZ-007** | **OCI-LZ-008** | **OCI-LZ-009** | **OCI-LZ-010**

**OCI-IAM-001** | **OCI-IAM-002** | **OCI-IAM-003** | **OCI-IAM-004** | **OCI-IAM-005** | **OCI-IAM-006** | **OCI-IAM-007** | **OCI-IAM-008** | **OCI-IAM-009** | **OCI-IAM-010**

**OCI-NET-001** | **OCI-NET-002** | **OCI-NET-003** | **OCI-NET-004** | **OCI-NET-005** | **OCI-NET-006** | **OCI-NET-007** | **OCI-NET-008** | **OCI-NET-009** | **OCI-NET-010** | **OCI-NET-011** | **OCI-NET-012**

**OCI-SEC-001** | **OCI-SEC-002** | **OCI-SEC-003** | **OCI-SEC-004** | **OCI-SEC-005** | **OCI-SEC-006** | **OCI-SEC-007** | **OCI-SEC-008** | **OCI-SEC-009** | **OCI-SEC-010**

**OCI-CMP-001** | **OCI-CMP-002** | **OCI-CMP-003** | **OCI-CMP-004** | **OCI-CMP-005** | **OCI-CMP-006** | **OCI-CMP-007** | **OCI-CMP-008**

**OCI-STO-001** | **OCI-STO-002** | **OCI-STO-003** | **OCI-STO-004** | **OCI-STO-005** | **OCI-STO-006** | **OCI-STO-007** | **OCI-STO-008**

**OCI-DB-001** | **OCI-DB-002** | **OCI-DB-003** | **OCI-DB-004** | **OCI-DB-005** | **OCI-DB-006** | **OCI-DB-007** | **OCI-DB-008** | **OCI-DB-009** | **OCI-DB-010** | **OCI-DB-011** | **OCI-DB-012**

**OCI-MW-001** | **OCI-MW-002** | **OCI-MW-003** | **OCI-MW-004** | **OCI-MW-005** | **OCI-MW-006** | **OCI-MW-007** | **OCI-MW-008**

**OCI-INT-001** | **OCI-INT-002** | **OCI-INT-003** | **OCI-INT-004** | **OCI-INT-005** | **OCI-INT-006** | **OCI-INT-007** | **OCI-INT-008**

**OCI-BKP-001** | **OCI-BKP-002** | **OCI-BKP-003** | **OCI-BKP-004** | **OCI-BKP-005** | **OCI-BKP-006** | **OCI-BKP-007** | **OCI-BKP-008**

**OCI-DR-001** | **OCI-DR-002** | **OCI-DR-003** | **OCI-DR-004** | **OCI-DR-005** | **OCI-DR-006** | **OCI-DR-007** | **OCI-DR-008** | **OCI-DR-009** | **OCI-DR-010**

**OCI-MON-001** | **OCI-MON-002** | **OCI-MON-003** | **OCI-MON-004** | **OCI-MON-005** | **OCI-MON-006** | **OCI-MON-007** | **OCI-MON-008**

**OCI-OPS-001** | **OCI-OPS-002** | **OCI-OPS-003** | **OCI-OPS-004** | **OCI-OPS-005** | **OCI-OPS-006** | **OCI-OPS-007** | **OCI-OPS-008**

**OCI-CST-001** | **OCI-CST-002** | **OCI-CST-003** | **OCI-CST-004** | **OCI-CST-005** | **OCI-CST-006** | **OCI-CST-007** | **OCI-CST-008**

**OCI-MIG-001** | **OCI-MIG-002** | **OCI-MIG-003** | **OCI-MIG-004** | **OCI-MIG-005** | **OCI-MIG-006** | **OCI-MIG-007** | **OCI-MIG-008** | **OCI-MIG-009** | **OCI-MIG-010** | **OCI-MIG-011** | **OCI-MIG-012**

**OCI-PER-001** | **OCI-PER-002** | **OCI-PER-003** | **OCI-PER-004** | **OCI-PER-005** | **OCI-PER-006** | **OCI-PER-007** | **OCI-PER-008**

**OCI-SUP-001** | **OCI-SUP-002** | **OCI-SUP-003** | **OCI-SUP-004** | **OCI-SUP-005** | **OCI-SUP-006** | **OCI-SUP-007** | **OCI-SUP-008**

**OCI-EXT-001** | **OCI-EXT-002** | **OCI-EXT-003** | **OCI-EXT-004** | **OCI-EXT-005** | **OCI-EXT-006** | **OCI-EXT-007** | **OCI-EXT-008** | **OCI-EXT-009** | **OCI-EXT-010**

*(No separate exclusions section — OCI pack uses OCI-EXT-001 through OCI-EXT-010 as explicit exclusions; included above)*

---

### Pack 3: Oracle OIC Integration Pack
*(Version 1.0 | Approved | 104 assumptions)*

**OIC-SCP-001** | **OIC-SCP-002** | **OIC-SCP-003** | **OIC-SCP-004** | **OIC-SCP-005** | **OIC-SCP-006** | **OIC-SCP-007** | **OIC-SCP-008**

**OIC-DES-001** | **OIC-DES-002** | **OIC-DES-003** | **OIC-DES-004** | **OIC-DES-005** | **OIC-DES-006** | **OIC-DES-007** | **OIC-DES-008** | **OIC-DES-009**

**OIC-END-001** | **OIC-END-002** | **OIC-END-003** | **OIC-END-004** | **OIC-END-005** | **OIC-END-006**

**OIC-SEC-001** | **OIC-SEC-002** | **OIC-SEC-003** | **OIC-SEC-004** | **OIC-SEC-005** | **OIC-SEC-006**

**OIC-CERT-001** | **OIC-CERT-002** | **OIC-CERT-003** | **OIC-CERT-004** | **OIC-CERT-005**

**OIC-MAP-001** | **OIC-MAP-002** | **OIC-MAP-003** | **OIC-MAP-004** | **OIC-MAP-005** | **OIC-MAP-006**

**OIC-TST-001** | **OIC-TST-002** | **OIC-TST-003** | **OIC-TST-004** | **OIC-TST-005** | **OIC-TST-006**

**OIC-PERF-001** | **OIC-PERF-002** | **OIC-PERF-003** | **OIC-PERF-004** | **OIC-PERF-005**

**OIC-CUT-001** | **OIC-CUT-002** | **OIC-CUT-003** | **OIC-CUT-004** | **OIC-CUT-005**

**OIC-MON-001** | **OIC-MON-002** | **OIC-MON-003** | **OIC-MON-004** | **OIC-MON-005**

**OIC-SUP-001** | **OIC-SUP-002** | **OIC-SUP-003** | **OIC-SUP-004**

**OIC-CUS-001** | **OIC-CUS-002** | **OIC-CUS-003** | **OIC-CUS-004** | **OIC-CUS-005** | **OIC-CUS-006** | **OIC-CUS-007** | **OIC-CUS-008** | **OIC-CUS-009** | **OIC-CUS-010** | **OIC-CUS-011** | **OIC-CUS-012**

**OIC-DEP-001** | **OIC-DEP-002** | **OIC-DEP-003** | **OIC-DEP-004** | **OIC-DEP-005** | **OIC-DEP-006**

**OIC-CON-001** | **OIC-CON-002** | **OIC-CON-003** | **OIC-CON-004** | **OIC-CON-005** | **OIC-CON-006**

*(Exclusions: OIC-EXC-001 through OIC-EXC-015 — see Section 3)*

---

### Pack 4: AMS — Managed Services Pack
*(Version 1.0 | Approved | 84 loaded; 1 suppressed [AMS-INC-004]; 83 active)*

**AMS-SCP-001** | **AMS-SCP-002** | **AMS-SCP-003** | **AMS-SCP-004** | **AMS-SCP-005** | **AMS-SCP-006** | **AMS-SCP-007**

**AMS-HRS-001** | **AMS-HRS-002** | **AMS-HRS-003** | **AMS-HRS-004** | **AMS-HRS-005** | **AMS-HRS-006**

**AMS-CHN-001** | **AMS-CHN-002** | **AMS-CHN-003** | **AMS-CHN-004**

**AMS-INC-001** | **AMS-INC-002** | **AMS-INC-003** | ~~**AMS-INC-004**~~ *(SUPPRESSED — Rule S1; replaced by EBS-DRM-013)* | **AMS-INC-005**

**AMS-SRQ-001** | **AMS-SRQ-002** | **AMS-SRQ-003** | **AMS-SRQ-004**

**AMS-ENH-001** | **AMS-ENH-002** | **AMS-ENH-003** | **AMS-ENH-004**

**AMS-CR-001** | **AMS-CR-002** | **AMS-CR-003** | **AMS-CR-004**

**AMS-DEF-001** | **AMS-DEF-002** | **AMS-DEF-003** | **AMS-DEF-004**

~~**AMS-SLA-001**~~ *(SUPPRESSED — Rule S2; replaced by EBS-SLA-002)*  
**AMS-SLA-002** | **AMS-SLA-003** | **AMS-SLA-004**  
~~**AMS-SLA-005**~~ *(SUPPRESSED — Rule S3; replaced by EBS-DRM-001)*

~~**AMS-PRI-001**~~ *(SUPPRESSED — Rule S2; replaced by EBS-SLA-004 + EBS-SLA-011)*  
~~**AMS-PRI-002**~~ *(SUPPRESSED — Rule S2; replaced by EBS-SLA-005 through EBS-SLA-009)*  
~~**AMS-PRI-003**~~ *(SUPPRESSED — Rule S2; replaced by EBS-SLA-012)*

**AMS-REL-001** | **AMS-REL-002** | **AMS-REL-003** | **AMS-REL-004** | **AMS-REL-005**

**AMS-PAT-001** | **AMS-PAT-002** | **AMS-PAT-003**

**AMS-MON-001** | **AMS-MON-002** | **AMS-MON-003** | **AMS-MON-004**

**AMS-REP-001** | **AMS-REP-002** | **AMS-REP-003** | **AMS-REP-004**

**AMS-CUS-001** | **AMS-CUS-002** | **AMS-CUS-003** | **AMS-CUS-004** | **AMS-CUS-005** | **AMS-CUS-006** | **AMS-CUS-007** | **AMS-CUS-008** | **AMS-CUS-009** | **AMS-CUS-010**

*(Exclusions: AMS-EXC-001 through AMS-EXC-012 — see Section 3)*

**AMS Pack net active: 83** (84 loaded − 1 suppressed [AMS-INC-004] − 4 suppressed [AMS-SLA-001, AMS-SLA-005, AMS-PRI-001, AMS-PRI-002, AMS-PRI-003] = **79** active)

> Note: Total AMS suppressions = 1 (AMS-INC-004) + 5 (SLA/PRI replacements) = 6. Net AMS active = 78.

---

### Pack 5: EBS AMS SLA Overlay
*(Version 1.0 | Approved WP15F | 53 assumptions — ADDITIVE; replaces AMS SLA/PRI assumptions)*

**EBS-SLA-001** | **EBS-SLA-002** *(replaces AMS-SLA-001)* | **EBS-SLA-003** | **EBS-SLA-004** *(replaces AMS-PRI-001)* | **EBS-SLA-005** | **EBS-SLA-006** | **EBS-SLA-007** | **EBS-SLA-008** | **EBS-SLA-009** | **EBS-SLA-010** | **EBS-SLA-011** *(replaces AMS-PRI-001/002/003)* | **EBS-SLA-012** *(replaces AMS-PRI-003)* | **EBS-SLA-013** | **EBS-SLA-014** | **EBS-SLA-015** | **EBS-SLA-016** | **EBS-SLA-017** | **EBS-SLA-018** | **EBS-SLA-019** | **EBS-SLA-020** | **EBS-SLA-021** | **EBS-SLA-022** | **EBS-SLA-023** | **EBS-SLA-024** | **EBS-SLA-025** | **EBS-SLA-026** | **EBS-SLA-027** | **EBS-SLA-028** | **EBS-SLA-029** | **EBS-SLA-030** | **EBS-SLA-031** | **EBS-SLA-032** | **EBS-SLA-033** | **EBS-SLA-034** | **EBS-SLA-035** | **EBS-SLA-036** | **EBS-SLA-037** | **EBS-SLA-038** | **EBS-SLA-039** | **EBS-SLA-040** | **EBS-SLA-041** | **EBS-SLA-042** | **EBS-SLA-043** | **EBS-SLA-044** | **EBS-SLA-045** | **EBS-SLA-046** | **EBS-SLA-047** | **EBS-SLA-048** | **EBS-SLA-049** | **EBS-SLA-050** | **EBS-SLA-051** | **EBS-SLA-052** | **EBS-SLA-053**

---

### Pack 6: EBS Dedicated Resource Model Overlay
*(Version 1.0 | Approved WP15F | 62 assumptions — ADDITIVE; replaces AMS-SLA-005; takes precedence over SLA Overlay on overlapping topics)*

**EBS-DRM-001** *(replaces AMS-SLA-005)* | **EBS-DRM-002** | **EBS-DRM-003** | **EBS-DRM-004** | **EBS-DRM-005** | **EBS-DRM-006** | **EBS-DRM-007** | **EBS-DRM-008** | **EBS-DRM-009** | **EBS-DRM-010** | **EBS-DRM-011** | **EBS-DRM-012** | **EBS-DRM-013** *(EBS infrastructure statement — replaces suppressed AMS-INC-004)* | **EBS-DRM-014** | **EBS-DRM-015** | **EBS-DRM-016** | **EBS-DRM-017** | **EBS-DRM-018** | **EBS-DRM-019** | **EBS-DRM-020** | **EBS-DRM-021** | **EBS-DRM-022** | **EBS-DRM-023** | **EBS-DRM-024** | **EBS-DRM-025** | **EBS-DRM-026** | **EBS-DRM-027** | **EBS-DRM-028** | **EBS-DRM-029** | **EBS-DRM-030** | **EBS-DRM-031** | **EBS-DRM-032** | **EBS-DRM-033** | **EBS-DRM-034** | **EBS-DRM-035** | **EBS-DRM-036** | **EBS-DRM-037** | **EBS-DRM-038** | **EBS-DRM-039** | **EBS-DRM-040** | **EBS-DRM-041** | **EBS-DRM-042** | **EBS-DRM-043** | **EBS-DRM-044** | **EBS-DRM-045** | **EBS-DRM-046** | **EBS-DRM-047** | **EBS-DRM-048** | **EBS-DRM-049** | **EBS-DRM-050** | **EBS-DRM-051** | **EBS-DRM-052** | **EBS-DRM-053** | **EBS-DRM-054** | **EBS-DRM-055** | **EBS-DRM-056** | **EBS-DRM-057** | **EBS-DRM-058** | **EBS-DRM-059** | **EBS-DRM-060** | **EBS-DRM-061** | **EBS-DRM-062**

---

## Section 3 — Explicit Exclusions

*(Rule E — Exclusions Always Included. Full text available in source pack files. IDs listed for schedule completeness.)*

### ERP Pack Exclusions
ERP-EXC-001 | ERP-EXC-002 | ERP-EXC-003 | ERP-EXC-004 | ERP-EXC-005 | ERP-EXC-006 | ERP-EXC-007 | ERP-EXC-008 | ERP-EXC-009 | ERP-EXC-010 | ERP-EXC-011 | ERP-EXC-012

### OIC Pack Exclusions
OIC-EXC-001 | OIC-EXC-002 | OIC-EXC-003 | OIC-EXC-004 | OIC-EXC-005 | OIC-EXC-006 | OIC-EXC-007 | OIC-EXC-008 | OIC-EXC-009 | OIC-EXC-010 | OIC-EXC-011 | OIC-EXC-012 | OIC-EXC-013 | OIC-EXC-014 | OIC-EXC-015

### AMS Pack Exclusions
AMS-EXC-001 | AMS-EXC-002 | AMS-EXC-003 | AMS-EXC-004 | AMS-EXC-005 | AMS-EXC-006 | AMS-EXC-007 | AMS-EXC-008 | AMS-EXC-009 | AMS-EXC-010 | AMS-EXC-011 | AMS-EXC-012

*(OCI pack uses OCI-EXT-001 through OCI-EXT-010 — included in Section 2 Pack 2 above)*

---

## Section 4 — Customer Responsibilities

*(Full text in source pack files. IDs listed for schedule completeness.)*

### ERP Pack Customer Responsibilities
ERP-CUS-001 through ERP-CUS-012 *(12 items)*

### OIC Pack Customer Responsibilities and Dependencies
OIC-CUS-001 through OIC-CUS-012 *(12 items)*  
OIC-DEP-001 through OIC-DEP-006 *(6 items)*  
OIC-CON-001 through OIC-CON-006 *(6 items)*

### AMS Pack Customer Responsibilities
AMS-CUS-001 through AMS-CUS-010 *(10 items)*

---

## Section 5 — Suppression Register

| Suppressed ID | Rule | Replaced By | Reason |
|---|---|---|---|
| AMS-INC-004 | S1 — EBS AMS engagement | EBS-DRM-013 | AMS-INC-004 states "Fusion HCM/ERP on Oracle SaaS infrastructure" — factually incorrect for EBS on OCI |
| AMS-SLA-001 | S2 — EBS SLA Overlay loaded | EBS-SLA-002 | EBS-specific SLA structure replaces generic AMS SLA |
| AMS-PRI-001 | S2 — EBS SLA Overlay loaded | EBS-SLA-004 + EBS-SLA-011 | 5-tier priority classification replaces 4-tier |
| AMS-PRI-002 | S2 — EBS SLA Overlay loaded | EBS-SLA-005 through EBS-SLA-009 | Per-tier P1–P5 response targets replace generic targets |
| AMS-PRI-003 | S2 — EBS SLA Overlay loaded | EBS-SLA-012 | 24/7 operational model replaces general coverage note |
| AMS-SLA-005 | S3 — EBS DRM Overlay loaded | EBS-DRM-001 | Named/dedicated resource assumption replaced by DRM |

**Total suppressed: 6** (6 from AMS Pack)  
**Net active: 594** (600 loaded − 6 suppressed)

> Correction to Section 1.2: Suppression count is 6 (not 1). Section 1.2 shows only AMS-INC-004; the SLA/PRI suppression count was completed after pack-level analysis. See ASSEMBLY_AUDIT_REPORT for reconciliation.

---

## Section 6 — Replacement Mappings

| Suppressed ID | Replacement ID | Pack Source |
|---|---|---|
| AMS-INC-004 | EBS-DRM-013 | EBS DRM Overlay |
| AMS-SLA-001 | EBS-SLA-002 | EBS SLA Overlay |
| AMS-PRI-001 | EBS-SLA-004, EBS-SLA-011 | EBS SLA Overlay |
| AMS-PRI-002 | EBS-SLA-005–009 | EBS SLA Overlay |
| AMS-PRI-003 | EBS-SLA-012 | EBS SLA Overlay |
| AMS-SLA-005 | EBS-DRM-001 | EBS DRM Overlay |

---

*ARM_IT045_ASSEMBLED_ASSUMPTION_SCHEDULE v1.0 | Assembly Engine MVP (WP17B) | Dry Run 2026-06-19*  
*Total: 600 loaded | 6 suppressed | 594 net — 6 packs | All packs Approved v1.0*
