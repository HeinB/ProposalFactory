---
document_id: RISK-ASSUMPTION-CROSS-REFERENCE-V1
title: "Risk → Assumption Cross-Reference — V1.0"
version: "1.0"
status: "DRAFT — Pending BU Lead Review"
created: "2026-06-26"
created_by: "WP18B-EXT.1A — Enterprise Risk Library Normalisation"
approved_by: ""
approved_date: ""
approved_for_reuse: false
category: "Commercial / Risk Library / Governance"
scope: "Maps each canonical risk entry to the governed assumption IDs that bound the risk. Used for: (1) proposal RAID assembly — identify which assumptions are relevant to each risk; (2) assumption audit — identify which risks are unbounded by current assumption packs."
related_documents:
  - ENTERPRISE_RISK_REGISTER_V1.md
  - RISK_LIBRARY_STANDARD.md
  - 08_Commercial/Assumptions/HCM/HCM_BASE_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/OIC/OIC_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/AMS/AMS_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/ERP/ERP_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/HCM/HCM_LEARNING_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/HCM/HCM_TALENT_ASSUMPTIONS_V1.md
  - 08_Commercial/Assumptions/HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md
assumption_packs_covered: 12
---

# Risk → Assumption Cross-Reference — V1.0

**Purpose:** Each row maps a canonical risk to the governed assumption IDs that define the contractual boundary for that risk. When a risk is realised, these assumptions are the first reference point: has the client breached a boundary assumption?

**Governance:** Use governed IDs only. All IDs in this document are traceable to approved assumption packs. No free-text assumption descriptions are used.

**Pack coverage:**
- HCM Base: HCM-ENV / HCM-ORG / HCM-SEC / HCM-WFL / HCM-DAT / HCM-RPT / HCM-TST / HCM-TRN / HCM-CUT / HCM-HYP / HCM-CHG / HCM-3PT / HCM-CUS / HCM-GEN / HCM-JRN / HCM-EXC
- HCM Recruiting: REC-SIT / REC-REQ
- HCM Learning: LRN-CON / LRN-PLT / LRN-AI / LRN-SAT / LRN-3PT / LRN-DAT / LRN-TRN / LRN-EXC
- HCM Talent: TLT-PER / TLT-GOL / TLT-SUC / TLT-CAR
- HCM Compensation: COM-FRM / COM-PLN / COM-WKS / COM-WFL / COM-TCS / COM-DAT
- OIC: OIC-SCP / OIC-DES / OIC-END / OIC-SEC / OIC-CERT / OIC-MAP / OIC-TST / OIC-PERF / OIC-SUP / OIC-CUS / OIC-DEP / OIC-CON / OIC-EXC
- AMS: AMS-SCP / AMS-HRS / AMS-CHN / AMS-INC / AMS-SRQ / AMS-ENH / AMS-CR / AMS-DEF / AMS-SLA / AMS-REL / AMS-MON / AMS-CUS / AMS-EXC
- EBS-SLA: EBS-SLA-001 to EBS-SLA-035
- EBS-DRM: EBS-DRM-001 to EBS-DRM-020+
- ERP: ERP-GEN / ERP-GL / ERP-AP / ERP-AR / ERP-FA / ERP-SEC / ERP-WFL / ERP-TST / ERP-TRN / ERP-CUT / ERP-HYP / ERP-CUS / ERP-EXC
- Acumatica: ACU-GEN / ACU-ENV / ACU-CFG / ACU-FIN / ACU-INV / ACU-MFG / ACU-PRJ / ACU-PUR / ACU-CRM / ACU-ORG / ACU-INT / ACU-DAT / ACU-REP / ACU-SEC / ACU-WFL / ACU-TST / ACU-TRN / ACU-CUT / ACU-UAT / ACU-EXT / ACU-SUP / ACU-AMS / ACU-PAY / ACU-CUS / ACU-EXC
- BeBanking: BB-GEN / BB-BNK / BB-PAY / BB-PYR / BB-FX / BB-INT / BB-SEC / BB-DAT / BB-RPT

---

## Cross-Reference Table

| Risk ID | Risk Title | Primary Pack(s) | Governing Assumption IDs |
|---|---|---|---|
| RC-PROJ-001 | Module design not signed off before build | HCM Base | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008 |
| RC-PROJ-002 | Upstream phase not stable when dependent phase begins | HCM Base | HCM-CUT-001, HCM-CUT-002, HCM-CUT-003, HCM-CUT-004, HCM-CUT-005, HCM-CUT-006, HCM-CUT-007, HCM-CUT-008, HCM-ORG-001 |
| RC-PROJ-003 | Organisational design decisions made late | HCM Base | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008 |
| RC-PROJ-004 | Configuration milestone changed after sign-off | HCM Base / ERP | HCM-ORG-001, ERP-GEN-001, ERP-GEN-002 |
| RC-DATA-001 | Legacy HR data quality causes migration delays | HCM Base | HCM-DAT-001, HCM-DAT-002, HCM-DAT-003, HCM-DAT-004, HCM-DAT-005, HCM-DAT-006, HCM-DAT-007, HCM-DAT-008, HCM-DAT-009 |
| RC-DATA-002 | Client content format incompatible with platform | HCM Learning | LRN-DAT-001, LRN-DAT-002, LRN-DAT-003, LRN-DAT-004 |
| RC-DATA-003 | HCM data quality produces invalid payroll input | HCM Base / OIC | HCM-DAT-001, HCM-DAT-002, HCM-DAT-003, HCM-DAT-004, HCM-DAT-005, OIC-MAP-001, OIC-MAP-002, OIC-MAP-003 |
| RC-DATA-004 | Biometric enrolment data does not match HR records | HCM Base | HCM-DAT-001, HCM-DAT-002 |
| RC-DATA-005 | Demand/scheduling data unavailable | HCM Base | HCM-DAT-001 |
| RC-INT-001 | Payroll integration timeline not aligned to HCM go-live | HCM Base / OIC | HCM-3PT-001, HCM-3PT-002, HCM-3PT-003, HCM-3PT-004, HCM-3PT-005, HCM-3PT-006, OIC-DES-001, OIC-DES-002, OIC-DES-003, OIC-END-001, OIC-END-002 |
| RC-INT-002 | Third-party integration scope underestimated | OIC / HCM Base | OIC-DES-001, OIC-DES-002, OIC-DES-003, OIC-DES-004, OIC-DES-005, OIC-SCP-001, OIC-SCP-002, HCM-3PT-001, HCM-3PT-002 |
| RC-INT-003 | Third-party API unavailable at integration build start | OIC | OIC-END-001, OIC-END-002, OIC-END-003, OIC-END-004, OIC-END-005, OIC-END-006, OIC-DES-001 |
| RC-INT-004 | Payroll API version changes post-go-live | OIC / AMS | OIC-DES-001, OIC-DES-002, AMS-REL-001 |
| RC-INT-005 | Integration schedule not aligned to payroll cutoff | OIC / HCM Base | OIC-DES-001, OIC-DES-002, OIC-DES-003, HCM-3PT-001, HCM-3PT-002, HCM-CUT-001, HCM-CUT-002, HCM-CUT-003 |
| RC-INT-006 | Integration field mapping errors produce incorrect data | OIC | OIC-MAP-001, OIC-MAP-002, OIC-MAP-003, OIC-MAP-004, OIC-MAP-005, OIC-MAP-006, OIC-TST-001, OIC-TST-002, OIC-TST-003 |
| RC-INT-007 | Bespoke payroll mapping beyond standard patterns | OIC / Acumatica | OIC-MAP-001, OIC-MAP-002, OIC-MAP-003, ACU-INT-001 |
| RC-TECH-001 | Quarterly SaaS update breaks configured functionality | HCM Base / AMS | HCM-ENV-004, AMS-REL-001 |
| RC-TECH-002 | SETA/WSP/ATR extract complexity | HCM Base | HCM-RPT-001, HCM-RPT-002, HCM-RPT-003, HCM-RPT-004, HCM-RPT-005, HCM-RPT-006 |
| RC-TECH-003 | Absence rules complexity exceeds standard scope | HCM Base | HCM-WFL-001, HCM-WFL-002, HCM-WFL-003, HCM-WFL-004, HCM-WFL-005, HCM-WFL-006 |
| RC-TECH-004 | Time and labour rules complexity exceeds estimate | HCM Base | HCM-WFL-001, HCM-WFL-002 |
| RC-TECH-005 | BCEA overtime calculation requires additional config | HCM Base | HCM-WFL-001 |
| RC-TECH-006 | OAX licensing not confirmed before commitment | HCM Base | HCM-RPT-003 |
| RC-TECH-007 | OAX data model not aligned to HCM configuration | HCM Base | HCM-RPT-003 |
| RC-TECH-008 | Oracle product licensing for dependent features not confirmed | HCM Base / ERP | HCM-RPT-003, ERP-GEN-001, ERP-GEN-002 |
| RC-TECH-009 | ODA scope added without separate license confirmation | HCM Base | HCM-RPT-003 |
| RC-TECH-010 | Digital channel complexity beyond standard configuration | AMS | AMS-CHN-001, AMS-CHN-002, AMS-CHN-003, AMS-CHN-004 |
| RC-TECH-011 | Career site design complexity exceeds standard scope | HCM Recruiting | REC-SIT-001, REC-SIT-002, REC-SIT-003, REC-SIT-004, REC-SIT-005 |
| RC-TECH-012 | Annual SA legislative change not reflected in integrations | OIC / AMS | OIC-DES-001, AMS-REL-001 |
| RC-CLIENT-001 | Super-user availability insufficient during UAT | HCM Base / ERP | HCM-TST-001, HCM-TST-002, HCM-TST-003, HCM-TST-004, HCM-TST-005, HCM-TST-006, HCM-TST-007, HCM-TST-008, ERP-TST-001, ERP-TST-002, ERP-TST-003, ERP-TST-004, ERP-TST-005, ERP-TST-006 |
| RC-CLIENT-002 | Client prerequisite systems or accounts not available | HCM Base / ERP | HCM-CUS-001, HCM-CUS-002, HCM-CUS-003, HCM-CUS-004, HCM-CUS-005, ERP-CUS-001, ERP-CUS-002, ERP-CUS-003 |
| RC-CLIENT-003 | Onboarding task and workflow ownership not defined | HCM Base / HCM Recruiting | HCM-CUS-001, HCM-CUS-002, HCM-CUS-003, HCM-CUS-004 |
| RC-CLIENT-004 | Learning catalog not ready at system go-live | HCM Learning | LRN-CON-001, LRN-CON-002, LRN-CON-003, LRN-CON-004, LRN-CON-005, LRN-DAT-001, LRN-DAT-002, LRN-DAT-003, LRN-DAT-004 |
| RC-CLIENT-005 | Performance rating data unavailable for compensation cycle | HCM Talent / HCM Compensation | TLT-PER-001, TLT-PER-002, TLT-PER-003, TLT-PER-004, TLT-PER-005, TLT-PER-006, COM-DAT-001 |
| RC-CLIENT-006 | Knowledge base content ownership undefined | AMS | AMS-CHN-001, AMS-CHN-002, AMS-CHN-003, AMS-CHN-004 |
| RC-CLIENT-007 | Cross-functional alignment on design frameworks | HCM Base | HCM-ORG-001, HCM-ORG-002, HCM-ORG-003, HCM-ORG-004, HCM-ORG-005, HCM-ORG-006, HCM-ORG-007, HCM-ORG-008, HCM-CHG-001, HCM-CHG-002, HCM-CHG-003, HCM-CHG-004 |
| RC-COMM-001 | Analytics expectations misaligned with platform capability | HCM Base | HCM-RPT-003 |
| RC-COMM-002 | Oracle HR Help Desk conflated with Oracle Service Cloud | AMS | AMS-CHN-001, AMS-CHN-002 |
| RC-COMM-003 | Integration method commitment in tender creates exposure | OIC / Acumatica | ACU-INT-001, OIC-DES-001 |
| RC-OPS-001 | First live operational cycle high-stakes risk | HCM Base / AMS / ERP | HCM-CUT-001, HCM-CUT-002, HCM-CUT-003, HCM-CUT-004, HCM-CUT-005, HCM-CUT-006, HCM-CUT-007, HCM-CUT-008, HCM-HYP-001, HCM-HYP-002, HCM-HYP-003, HCM-HYP-004, HCM-HYP-005, AMS-SLA-001, AMS-SLA-002, AMS-SLA-005, ERP-CUT-001, ERP-CUT-002, ERP-CUT-003, ERP-CUT-004, ERP-CUT-005, ERP-HYP-001, ERP-HYP-002, ERP-HYP-003, ERP-HYP-004 |
| RC-COMP-001 | POPIA non-compliance in HR or payroll data handling | HCM Base / OIC / BeBanking | OIC-SEC-001, OIC-SEC-002, OIC-SEC-003, OIC-SEC-004, OIC-SEC-005, OIC-SEC-006, BB-DAT-006, HCM-SEC-001, HCM-SEC-002, HCM-SEC-003, HCM-SEC-004, HCM-SEC-005, HCM-SEC-006, HCM-SEC-007, HCM-SEC-008 |

---

## Coverage Analysis

### By Risk Category

| Category | Risks | Assumptions Referenced | Coverage Status |
|---|---|---|---|
| RC-PROJ | 4 | HCM-ORG-001 to -008, HCM-CUT-001 to -008, ERP-GEN-001, ERP-GEN-002 | Full |
| RC-DATA | 5 | HCM-DAT-001 to -009, LRN-DAT-001 to -004, OIC-MAP-001 to -003 | Full |
| RC-INT | 7 | HCM-3PT-001 to -006, OIC-DES-001 to -005, OIC-END-001 to -006, OIC-MAP-001 to -006, OIC-SCP-001 to -002, OIC-TST-001 to -003, AMS-REL-001, ACU-INT-001 | Full |
| RC-TECH | 12 | HCM-ENV-004, HCM-RPT-001 to -006, HCM-WFL-001 to -006, AMS-CHN-001 to -004, AMS-REL-001, REC-SIT-001 to -005, ERP-GEN-001, OIC-DES-001 | Full |
| RC-CLIENT | 7 | HCM-TST-001 to -008, HCM-CUS-001 to -005, HCM-CHG-001 to -004, HCM-ORG-001 to -008, ERP-TST-001 to -006, ERP-CUS-001 to -003, LRN-CON-001 to -005, LRN-DAT-001 to -004, TLT-PER-001 to -006, COM-DAT-001, AMS-CHN-001 to -004 | Full |
| RC-COMM | 3 | HCM-RPT-003, AMS-CHN-001 to -002, ACU-INT-001, OIC-DES-001 | Full |
| RC-OPS | 1 | HCM-CUT-001 to -008, HCM-HYP-001 to -005, AMS-SLA-001, AMS-SLA-002, AMS-SLA-005, ERP-CUT-001 to -005, ERP-HYP-001 to -004 | Full |
| RC-COMP | 1 | HCM-SEC-001 to -008, OIC-SEC-001 to -006, BB-DAT-006 | Full |

### Assumption Packs Referenced

| Pack | IDs Referenced | Note |
|---|---|---|
| HCM Base | HCM-ORG, HCM-DAT, HCM-RPT, HCM-TST, HCM-CUT, HCM-HYP, HCM-CHG, HCM-3PT, HCM-CUS, HCM-SEC, HCM-WFL, HCM-ENV | Primary pack — referenced by 37 of 40 risks |
| OIC | OIC-DES, OIC-END, OIC-MAP, OIC-SCP, OIC-TST, OIC-SEC | Referenced by all RC-INT and RC-COMP (OIC context) |
| AMS | AMS-REL, AMS-CHN, AMS-SLA | Referenced by AMS-applicable risks |
| ERP | ERP-GEN, ERP-TST, ERP-CUT, ERP-HYP, ERP-CUS | Referenced by cross-platform risks |
| HCM Recruiting | REC-SIT | Referenced by RC-TECH-011 only |
| HCM Learning | LRN-CON, LRN-DAT | Referenced by RC-DATA-002 and RC-CLIENT-004 |
| HCM Talent | TLT-PER | Referenced by RC-CLIENT-005 only |
| HCM Compensation | COM-DAT | Referenced by RC-CLIENT-005 only |
| Acumatica | ACU-INT | Referenced by RC-INT-007 and RC-COMM-003 |
| BeBanking | BB-DAT | Referenced by RC-COMP-001 only |
| EBS-SLA | — | Not directly referenced (EBS risks subsumed into ERP category) |
| EBS-DRM | — | Not directly referenced (EBS risks subsumed into ERP category) |

### Assumption Coverage Gaps

The following categories have no canonical risks (and therefore no assumption cross-references) because no source risks were extracted during the audit:

| Category | Status |
|---|---|
| RC-RES — Resource Risk | No source risks found in 49-asset audit. Assumption packs: none applicable. |
| RC-INFRA — Infrastructure Risk | No source risks found. OCI Pack exists but OCI risks not extracted. |
| RC-CM — Change Management Risk | No source risks found. HCM-CHG pack exists as secondary reference only. |
| RC-MIG — Migration Risk | No source risks found. Migration risk embedded in RC-DATA entries. |
| RC-CUT — Cutover Risk | No source risks found. Cutover risk embedded in RC-OPS-001. |
| RC-3P — Third Party Risk | No source risks found. Third-party risk embedded in RC-INT entries. |
| RC-SEC — Security Risk | No source risks found. Security references embedded in RC-COMP-001. |

**Recommendation:** These coverage gaps should be addressed in WP18B-EXT.2 (BU Lead review) or WP18B-EXT.3 (gap-fill exercise). The absence of source risks does not mean these categories have no applicable risks — it means APPSolve's 49-asset library had not explicitly articulated them.
