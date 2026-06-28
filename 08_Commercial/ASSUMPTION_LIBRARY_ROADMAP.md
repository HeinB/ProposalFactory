---
document_id: ASSUMPTION_LIBRARY_ROADMAP
title: "Commercial Assumptions Library — Roadmap"
version: "1.7"
created: "2026-06-15"
created_by: "WP11 — Commercial Assumptions Library"
last_updated: "2026-06-19"
last_updated_by: "WP16A — Library Reconciliation Baseline"
status: "Active"
---

# Commercial Assumptions Library — Roadmap

## Current State

As at 2026-06-19 (WP16A reconciliation baseline), the Commercial Assumptions Library contains thirteen documents (9 approved packs/overlays + 4 draft HCM module packs):

| Pack | File | Status | Assumptions | BU Review Items |
|---|---|---|---|---|
| HCM Base | `HCM/HCM_BASE_ASSUMPTIONS_V1.md` | **Approved — 2026-06-15** | 114 | 0 (closed) |
| HCM Recruiting (Pack 1) | `HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md` | **Draft** | 54 | 2 HIGH (BU-REC-005/006) + 2 LOW (BU-REC-001/007); MEDIUM resolved WP15F |
| HCM Learning (Pack 2) | `HCM/HCM_LEARNING_ASSUMPTIONS_V1.md` | **Draft** | 37 *(+6 pending authoring)* | 3 LOW (BU-LRN-001/003/005); MEDIUM resolved WP15F |
| HCM Talent Management (Pack 3) | `HCM/HCM_TALENT_ASSUMPTIONS_V1.md` | **Draft** | 31 *(+7 pending authoring)* | 3 LOW (BU-TLT-001/003/004); MEDIUM resolved WP15F |
| HCM Workforce Compensation (Pack 4) | `HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md` | **Draft** | 30 *(+10 pending authoring)* | 3 LOW (BU-COM-001/002/005); MEDIUM resolved WP15F |
| OIC Standalone (Pack 5) | `OIC/OIC_ASSUMPTIONS_V1.md` | **Approved — 2026-06-15** | 104 | 0 (closed) |
| Oracle ERP (Pack 6) | `ERP/ERP_ASSUMPTIONS_V1.md` | **Approved — 2026-06-15** | 123 | 0 (closed) |
| OCI Infrastructure (Pack 7) | `OCI/OCI_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-16** | 174 | 0 (all APPROVED; BU-OCI-007 WITHDRAWN) |
| Acumatica Base (Pack 8) | `Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-18 (WP15C)** | 152 | 0 (all 14 decisions resolved WP15C) |
| BeBanking Base (Pack 9) | `BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-18 (WP14F)** | 117 | 0 (all 10 decisions resolved WP14F) |
| Managed Services / AMS (Pack 10) | `AMS/AMS_ASSUMPTIONS_V1.md` | **Approved — 2026-06-15** | 84 | 0 (closed) |
| EBS AMS SLA Overlay | `AMS/EBS_AMS_SLA_OVERLAY_V1.md` | **Approved v1.0 — 2026-06-19 (WP15F)** | 53 | 0 (all 4 EBS-SLA decisions resolved WP15F) |
| EBS Dedicated Resource Model | `AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-19 (WP15F)** | 62 | 0 (all 5 EBS-DRM decisions resolved WP15F) |

> **WP16A Reconciliation Baseline — 2026-06-19:** All counts are body/register-authoritative (frontmatter corrected to match body where they diverged).

**Total assumptions (body-authoritative):** 1,135 | **Total approved:** 983 (HCM Base 114 + OIC 104 + ERP 123 + OCI 174 + Acumatica 152 + BeBanking 117 + AMS 84 + EBS SLA Overlay 53 + EBS DRM Overlay 62) | **Draft:** 152 (Recruiting 54 + Learning 37 + Talent 31 + Compensation 30; +23 pending authoring in HCM module packs)

The library now covers Oracle HCM full-suite, OIC, Oracle ERP, OCI Infrastructure, AMS/Managed Services (including EBS overlay packs), Acumatica Base, and BeBanking Base. Nine packs/overlays Approved; four HCM module packs remain Draft (12 BU Lead decisions pending — 2 HIGH + 10 LOW).

---

## Prioritised Roadmap

### Pack 1 — HCM Recruiting Assumptions
**File:** `08_Commercial/Assumptions/HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | Very High — Recruiting proposals have the most complex scope boundary disputes: career site count, ATS migration, offer template complexity, onboarding integration, background check providers, Recruiting Booster activation |
| **Reuse frequency** | High — Oracle Fusion Recruiting Cloud is included in >80% of full HCM suite proposals and is increasingly sold as a standalone module in high-volume recruitment sectors |
| **Tender impact** | High — Recruiting scope disputes are common; assumptions on career site count, candidate journey, offer letters, job board integrations, and background check providers have caused project overruns |
| **Recommended priority** | **1 — CREATED 2026-06-15 (Draft — 2 HIGH + 2 LOW decisions remaining)** |

**Key assumptions to include:**
- Career site count (external, internal, agency portal) — default and overage
- ATS data migration (active vacancies only; historical application data excluded by default)
- Job board posting (LinkedIn, PNet direct integration vs manual posting)
- Candidate journey steps — default count and overage rule
- Offer letter template count
- Background check provider — vendor's responsibility to provide API
- Onboarding integration with Core HR Journeys
- Recruiting Booster — specific to B95763 BOM line
- Interview scheduling — calendar provider (Microsoft 365 assumed; Google Workspace requires assessment)
- Internal mobility portal — included vs. separate scope decision

---

### Pack 2 — HCM Learning Assumptions
**File:** `08_Commercial/Assumptions/HCM/HCM_LEARNING_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | High — Learning proposals frequently suffer from content ownership disputes, third-party LMS migration scope creep, SETA reporting expectation gaps, and eLearning authoring tool integration queries |
| **Reuse frequency** | High — Oracle Learning Cloud included in most full HCM suite deals; increasingly sold standalone for SETA-reporting organisations |
| **Tender impact** | High — SETA/WSP/ATR reporting expectations frequently misaligned; content migration scope (SCORM/video/PDF) underestimated |
| **Recommended priority** | **2 — CREATED 2026-06-15 (Draft — 3 LOW decisions remaining; MEDIUM resolved WP15F)** |

**Key assumptions to include:**
- Learning content ownership (client provides content in Oracle-supported formats)
- Supported content types (SCORM/AICC/PDF/video/assessment/web link)
- Historical learning completion migration — active employees, maximum years
- Third-party LMS integration — count limit; vendor API responsibility
- SETA/WSP/ATR — data extract approach; client submits statutory reports
- AI learning recommendations — platform capability vs. APPSolve configuration
- Learning community structure — count and complexity
- eLearning authoring tools (Articulate/Lectora/Captivate) — not in APPSolve scope
- Learning catalogue population — APPSolve provides framework; client populates
- Certification management — expiry tracking vs. recertification automation

---

### Pack 3 — HCM Talent Management Assumptions
**File:** `08_Commercial/Assumptions/HCM/HCM_TALENT_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | Medium-High — Talent Management scope is often initially under-appreciated; succession and talent review configuration is more complex than clients expect |
| **Reuse frequency** | Medium-High — Typically sold as part of full HCM suite; less frequently sold standalone |
| **Tender impact** | Medium — Performance template complexity and succession plan depth are common scope creep vectors |
| **Recommended priority** | **3 — CREATED 2026-06-15 (Draft — 3 LOW decisions remaining; MEDIUM resolved WP15F)** |

**Key assumptions to include:**
- Performance review template count and complexity
- Rating model — single vs. multi-dimension (performance + potential)
- 9-box grid calibration — standard Oracle or custom configuration
- Goal cascade source — client provides corporate goals before configuration
- Career path content — client defines career paths; APPSolve configures framework
- Succession pool depth — count of succession plans in scope
- Talent profile completeness — client responsible for competency and skill data
- AI skills integration — Dynamic Skills feeds Talent Profiles (HCM Base licence)
- HR Review meeting facilitation — not in APPSolve scope

---

### Pack 4 — HCM Workforce Compensation Assumptions
**File:** `08_Commercial/Assumptions/HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | High — Compensation scope disputes are disproportionately costly: budget modelling complexity, approval workflow depth, and pay equity analysis expectations frequently exceed initial estimates |
| **Reuse frequency** | Medium — Sold as part of full HCM suite; sometimes sold standalone for merit cycle management |
| **Tender impact** | High — Compensation plan count, budget pool configuration, and approval routing complexity are consistent overrun sources |
| **Recommended priority** | **4 — CREATED 2026-06-15 (Draft — 3 LOW decisions remaining; MEDIUM resolved WP15F)** |

**Key assumptions to include:**
- Compensation plan count (merit plans, bonus plans, one-time payments) — default and overage
- Budget pool model — top-down vs. bottom-up; single vs. multi-level
- Approval workflow depth for compensation decisions
- Total compensation statement design — standard Oracle template vs. custom
- Salary range configuration — client provides grade/range data before configuration
- Pay equity analysis — platform analytics only; not a compliance audit
- Compensation history migration — excluded by default
- Third-party benchmarking tool integration (Mercer, Hay, Remchannel) — not in base scope
- Variable pay (commission, incentive) — assessed separately; complex commission schemes are not in standard Compensation Cloud scope

---

### Pack 5 — OIC Integration Assumptions
**File:** `08_Commercial/Assumptions/OIC/OIC_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | Very High — OIC integration is present in almost every Oracle HCM and ERP proposal; integration scope disputes are among the highest-risk commercial issues in delivery |
| **Reuse frequency** | Very High — OIC Enterprise is a BOM line item in nearly every Oracle proposal (HCM payroll interface; ERP bank integration; BeBanking H2H; third-party systems) |
| **Tender impact** | Very High — Integration estimate accuracy and scope boundary are the single most common source of project overruns in the Oracle practice |
| **Recommended priority** | **5 — APPROVED — 2026-06-15 (WP11C-A — all 7 BU decisions closed)** |

**Key assumptions to include:**
- Integration count and definition of an "integration" (one directional flow = one integration)
- Message capacity (OIC message tier — 1M vs. 2M — and what constitutes a message)
- Third-party vendor API responsibility
- Integration design vs. build vs. test ownership (APPSolve vs. client vs. vendor)
- Error handling and monitoring framework — standard OIC monitoring dashboard
- OIC version — Enterprise (standard and on-premises adapters) vs. Standard
- API-first vs. file-based integration preference — confirmed in Scope and Design
- Non-production OIC tenant for testing vs. production
- OIC accelerators — confirmed reusable patterns (see W4-INT-001)
- Scheduler/trigger ownership post-go-live

---

### Pack 6 — Oracle ERP Assumptions
**File:** `08_Commercial/Assumptions/ERP/ERP_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | Very High — Oracle Fusion ERP (Financials, Procurement, PPM) proposals involve the largest commercial values and the highest scope risk |
| **Reuse frequency** | High — Growing Oracle ERP pipeline (NALA, CUM, Investec, Plennegy ERP track) |
| **Tender impact** | Very High — ERP scope disputes involve multi-entity configuration, chart of accounts complexity, bank reconciliation, and multi-currency — consistently under-scoped areas |
| **Recommended priority** | **6 — APPROVED — 2026-06-15 (WP11D-A — all 8 BU-ERP decisions closed)** |

**Key assumptions to include:**
- Chart of accounts — client designs; APPSolve configures
- Legal entity count and configuration effort
- Multi-currency — functional currency per LE; translation vs. revaluation
- Bank account configuration — client provides bank details; number of accounts
- Subledger accounting (SLA) — standard vs. custom accounting rules
- Fixed assets — asset register migration; impairment testing not included
- IFRS 16 lease accounting — assessed separately if required
- Intercompany transactions — volume and complexity assessment
- Period-end close automation — standard Oracle vs. custom scripting
- AP invoice automation (OCR) — separately licensed; not in base ERP

---

### Pack 7 — OCI Infrastructure Assumptions
**File:** `08_Commercial/Assumptions/OCI/OCI_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | Medium — OCI is growing as APPSolve hosts middleware, DBA environments, and custom applications on OCI |
| **Reuse frequency** | Medium — OCI is not a standalone BOM item in most Oracle HCM proposals; more relevant for OCI-hosted middleware, DBA services, and BeBanking hosting |
| **Tender impact** | Medium — OCI infrastructure scope disputes are less frequent but higher impact when they occur (cloud networking, security zones, tenancy design) |
| **Recommended priority** | **7 — APPROVED v1.0 — 2026-06-16 (WP11H-A — all 15 BU decisions closed; 174 assumptions)** |

---

### Pack 8 — Acumatica Base Assumptions
**File:** `08_Commercial/Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | High — Acumatica has a growing implementation portfolio; Acumatica-specific assumptions (cloud vs. SaaS hosting, PaySpace integration, customisation, ERP data migration) are not covered by Oracle assumptions |
| **Reuse frequency** | High — Every Acumatica proposal needs a base assumptions pack |
| **Tender impact** | High — Acumatica customisation scope, PaySpace integration, and data migration from legacy ERP (Pastel/SAGE) are frequent overrun sources |
| **Recommended priority** | **8 — APPROVED v1.0 — 2026-06-18 (WP15C — all 14 BU-ACU decisions resolved)** |

**Key assumptions to include:**
- Acumatica cloud SaaS model (no on-premises deployment)
- Acumatica version compatibility — customisations constrained to Acumatica Low-Code/No-Code approach
- PaySpace integration — client must use PaySpace; other payroll providers assessed separately
- ERP data migration (Pastel, SAGE, QuickBooks) — client extracts; APPSolve validates
- Acumatica licence model — per concurrent user vs. per transaction module
- Customisation approach — Acumatica framework only; no direct database modification
- Multi-branch / multi-entity configuration
- Period-end close and reporting

---

### Pack 9 — BeBanking Assumptions
**File:** `08_Commercial/Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | High — BeBanking proposals involve complex banking partner dependencies, file format requirements, and bank testing schedules that must be commercially governed |
| **Reuse frequency** | Medium — BeBanking is sold alongside Oracle and Acumatica ERP |
| **Tender impact** | High — Bank testing (UAT with bank) is a long-lead-time activity outside APPSolve's control; assumptions governing bank readiness protect delivery timelines |
| **Recommended priority** | **9 — APPROVED v1.0 — 2026-06-18 (WP14F — all 10 BU-BB decisions resolved; 117 approved assumptions)** |

**Key assumptions to include:**
- Supported banks — confirmed integration list (ABSA, FNB, Nedbank SA, Nedbank Namibia, Standard Bank SA, Standard Bank Namibia, Investec, Citi Bank UK, Santander Chile)
- Bank testing schedule — bank's own UAT timeline is outside APPSolve's control
- ERP source system — Oracle EBS or Oracle Fusion only; Acumatica scope-specific
- Payment file formats — client confirms file format before design commences
- SWIFT — indirect model only; no direct SWIFT membership
- Fx payments — spot vs. forward contract; hedging not in scope
- BeBanking hosting on OCI — client account or APPSolve-managed

---

### Pack 10 — Managed Services / AMS Assumptions
**File:** `08_Commercial/Assumptions/AMS/AMS_ASSUMPTIONS_V1.md`

| Dimension | Assessment |
|---|---|
| **Value** | Very High — AMS agreements are APPSolve's highest-margin recurring revenue; commercial protection of AMS scope boundaries (what is a bug vs. enhancement; SLA scope; change request thresholds) is critical |
| **Reuse frequency** | Very High — Almost every implementation transitions to AMS; AMS assumptions apply across Oracle, Acumatica, and BeBanking |
| **Tender impact** | Very High — AMS scope creep (changes treated as bugs; enhancements absorbed into support hours) is the primary AMS margin risk |
| **Recommended priority** | **10 — APPROVED — 2026-06-15 (WP11E-A — all 7 BU-AMS decisions closed)** |

**Key assumptions to include:**
- Scope of AMS (configuration support only; no new development)
- Bug vs. enhancement definition (critical — must be unambiguous)
- Included support hours per month and overage mechanism
- SLA tiers (P1–P4 response and resolution targets)
- Oracle quarterly release management (assessment, testing, activation)
- Excluded: new module implementation; new integration development; data migration; new report development
- Change Request threshold — minimum effort that triggers a CR vs. absorbed into support
- Named support consultant (best-efforts availability; not guaranteed)
- Monthly reporting obligation

---

### Overlays — EBS AMS Overlay Packs
**Files:** `08_Commercial/Assumptions/AMS/EBS_AMS_SLA_OVERLAY_V1.md` | `08_Commercial/Assumptions/AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md`

These packs supplement (not replace) the AMS Base pack for EBS AMS engagements. Both approved WP15F (2026-06-19).

| Overlay | Assumptions | Sections | Approved |
|---|---|---|---|
| EBS AMS SLA Overlay | 53 | EBS-SLA: P1–P4 tiers; client-configurable SLAs; resolution on-request; fixed premium; service credits | 2026-06-19 (WP15F) |
| EBS Dedicated Resource Model | 62 | EBS-DRM: per-engagement hours; rollover to month N+1; 3-BD illness / 10-BD leave; 30-CD notice; runbook standard | 2026-06-19 (WP15F) |

---

## Roadmap Summary

| Pack | Priority | Owner | Status |
|---|---|---|---|
| HCM Recruiting | 1 | Oracle BU Lead | **Draft — 2 HIGH (BU-REC-005/006) + 2 LOW remaining** |
| HCM Learning | 2 | Oracle BU Lead | **Draft — 3 LOW remaining (BU-LRN-001/003/005)** |
| HCM Talent Management | 3 | Oracle BU Lead | **Draft — 3 LOW remaining (BU-TLT-001/003/004)** |
| HCM Workforce Compensation | 4 | Oracle BU Lead | **Draft — 3 LOW remaining (BU-COM-001/002/005)** |
| OIC Integration | 5 | Oracle BU Lead | **APPROVED — 2026-06-15 (104 assumptions; all 7 BU decisions closed)** |
| Oracle ERP | 6 | Oracle BU Lead | **APPROVED — 2026-06-15 (123 assumptions; all 8 BU decisions closed)** |
| OCI Infrastructure | 7 | Oracle BU Lead / OCI Architect | **APPROVED v1.0 — 2026-06-16 (174 assumptions; 14 decisions applied, 1 withdrawn)** |
| Acumatica Base | 8 | Acumatica BU Lead | **APPROVED v1.0 — 2026-06-18 (WP15C; 152 assumptions; all 14 BU-ACU decisions resolved)** |
| BeBanking | 9 | BeBanking BU Lead | **APPROVED v1.0 — 2026-06-18 (WP14F; 117 assumptions; all 10 BU-BB decisions resolved)** |
| Managed Services / AMS | 10 | Oracle BU Lead (primary) | **APPROVED — 2026-06-15 (84 assumptions; all 7 BU-AMS decisions closed)** |
| EBS AMS SLA Overlay | Overlay | Oracle BU Lead | **APPROVED v1.0 — 2026-06-19 (WP15F; 53 assumptions; all 4 EBS-SLA decisions resolved)** |
| EBS DRM Overlay | Overlay | Oracle BU Lead | **APPROVED v1.0 — 2026-06-19 (WP15F; 62 assumptions; all 5 EBS-DRM decisions resolved)** |

**Outstanding decisions:** 12 total — 2 HIGH (BU-REC-005, BU-REC-006) + 10 LOW (BU-REC-001/007, BU-LRN-001/003/005, BU-TLT-001/003/004, BU-COM-001/002/005)

---

## When Each Pack Unblocks Revenue

| Pack | Tender Types Unblocked |
|---|---|
| HCM Base (current) | Oracle Fusion Core HR, Absence, Benefits, Journeys, Payroll Interface proposals |
| + Recruiting | Full HCM suite proposals with Recruiting Cloud; standalone Recruiting tenders |
| + Learning | Full HCM suite proposals; standalone Oracle Learning Cloud tenders |
| + Talent | Full HCM suite proposals; standalone Talent Management tenders |
| + Compensation | Full HCM suite proposals; standalone Compensation Cloud tenders |
| + OIC | Any Oracle proposal with integrations (effectively all Oracle proposals) |
| + ERP | Oracle Fusion Financials, Procurement, PPM proposals |
| + OCI | Any proposal including OCI migration, EBS on OCI, OCI hosting, BeBanking OCI, Managed OCI services |
| + Acumatica | All Acumatica implementation proposals |
| + BeBanking | All BeBanking implementation proposals; cross-sell with Oracle/Acumatica |
| + AMS (Base + EBS Overlays) | All post-implementation managed services proposals across all BUs; EBS AMS commercial governance |

**Current coverage gap:** The 4 HCM module packs are the only remaining Draft artefacts. Full HCM suite proposals (Recruiting, Learning, Talent, Compensation) ship with HCM Base protection; the gaps are module-specific scope boundaries. 2 HIGH decisions (BU-REC-005/006) are the priority — they affect career site and ATS scope in Recruiting proposals. 10 LOW decisions can be resolved in a single BU Lead session.

---

---

## Commercial Framework (WP11F-A) — Completed 2026-06-16

The Commercial Framework is a separate but companion system to the Assumption Library. 5 framework documents were drafted in WP11F and approved by BU Lead in WP11F-A (2026-06-16):

| Document | Status | CD Items |
|---|---|---|
| RATE_CARD_FRAMEWORK.md | **Approved v1.0** | BU-RC-004, BU-RC-008 |
| ESTIMATION_GUIDE.md | **Approved v1.0** | None |
| CR_PRICING_MODEL.md | **Approved v1.0** | BU-CR-003 |
| EFFORT_MULTIPLIERS.md | **Approved v1.0** | BU-EM-006 |
| COMMERCIAL_GOVERNANCE.md | **Approved v1.0** | BU-GOV-001, BU-GOV-003 |

**6 Commercial Director items outstanding.** These items (monetary thresholds, margin floors, AMS rate policy) are maintained in the Commercial Director's authority schedule. Change logs: `RATE_CARD_CHANGE_LOG.md`, `ESTIMATION_CHANGE_LOG.md`, `CR_PRICING_CHANGE_LOG.md`, `EFFORT_MULTIPLIER_CHANGE_LOG.md`, `COMMERCIAL_GOVERNANCE_CHANGE_LOG.md`.

---

---

## OCI Infrastructure Pack (WP11H + WP11H-A) — APPROVED 2026-06-16

Four deliverables created in WP11H and approved via BU Lead review in WP11H-A (2026-06-16):

| File | Status | Content |
|---|---|---|
| `OCI/OCI_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-16** | 174 assumptions; Sections 101–119 |
| `OCI/OCI_ASSUMPTION_REGISTER.csv` | **Approved** | 174 rows; all status = Approved |
| `OCI/OCI_GAP_REPORT.md` | **Approved v1.0** | 12 gaps (1 CRITICAL resolved; 5 HIGH resolved; 3 MEDIUM resolved; 3 MEDIUM remain as future research) |
| `OCI/OCI_SCOPE_BOUNDARY_GUIDE.md` | **Approved v1.0** | 12 scope creep scenarios; quick-reference In/Out table |

**BU Lead decisions — all resolved 2026-06-16:**

| Decision | Item | Outcome |
|---|---|---|
| BU-OCI-001 | OCI tenancy provisioning service scope | Billable pre-engagement activity |
| BU-OCI-002 | FastConnect vs IPSec VPN threshold | Recommend FastConnect: >100 Mbps / >100 users / sub-second OIC / DR RTO <2h |
| BU-OCI-003 | Oracle DB licensing default | BYOL default; licence position confirmed at pre-sales discovery |
| BU-OCI-004 | Pilot Light DR pricing status | Always separately priced; never included by default |
| BU-OCI-005 | OCI DBA AMS scope boundary | OCI AMS = infra DBA; ERP/HCM AMS = application DBA |
| BU-OCI-006 | EBS on OCI addendum pack | ERP Pack + OCI Pack sufficient; no addendum needed |
| **BU-OCI-007** | **BeBanking OCI hosting cost responsibility** | **WITHDRAWN — concept does not exist in APPSolve's operating model** |
| BU-OCI-008 | OCI cost estimate disclaimer language | Mandatory approved wording applied to OCI-CST-002 |
| BU-OCI-009 | Non-production environment count | 2 environments: Dev/Test combined + UAT separate |
| BU-OCI-010 | OCI patching cadence in AMS | Quarterly standard; monthly premium; critical within 30 days |
| NEW-OCI-011 | Data Guard default for production VM DB | Default included; single-instance requires written risk acceptance |
| NEW-OCI-012 | 30-day migration performance warranty | 30-day warranty post sign-off; requires baseline; app-level excluded |
| NEW-OCI-013 | EBS OS choice at design sign-off | Oracle Linux or RHEL; confirmed at design sign-off |
| NEW-OCI-014 | Regulated-industry security escalation | Flagged at pre-sales; OCI Security Addendum discussion |
| NEW-OCI-015 | Production DB backup retention | Production: 30 days; non-production: 7 days |

---

---

## Acumatica Base Pack (WP11I + WP11I-A + WP15C) — APPROVED v1.0 2026-06-18

Four deliverables created in WP11I (2026-06-16) and remediated via WP11I-A Pre-Approval Validation (2026-06-16). Promoted to Approved v1.0 in WP15C (2026-06-18) after all 14 BU-ACU decisions resolved.

| File | Status | Content |
|---|---|---|
| `Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-18 (WP15C)** | 152 assumptions; Sections 120–139 (Section 139 ACU-SEC added in WP11I-A) |
| `Acumatica/ACU_ASSUMPTION_REGISTER.csv` | **Approved** | 152 rows; all status = Approved |
| `Acumatica/ACU_GAP_REPORT.md` | **Approved v1.1** | 14 gaps (1 CRITICAL, 4 HIGH, 5 MEDIUM, 4 RESEARCH) |
| `Acumatica/ACU_SCOPE_BOUNDARY_GUIDE.md` | **Approved** | 14 scope creep scenarios |
| `Acumatica/WP11I_A_REMEDIATION_REPORT.md` | **Complete** | WP11I-A validation findings + remediation decisions |

**BU Lead decisions — all resolved WP15C (2026-06-18):** BU-ACU-001–015 (excl. BU-ACU-013). All decisions applied to pack body. Pack promoted Approved v1.0.

---

## BeBanking Base Pack (WP11J + WP14D/E/F) — APPROVED v1.0 2026-06-18

Five deliverables created in WP11J (2026-06-16). Promoted to Approved v1.0 in WP14F (2026-06-18) after all 10 BU-BB decisions resolved. 5 assumptions deleted (WP14D/E), leaving 117 approved assumptions.

| File | Status | Content |
|---|---|---|
| `BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-18 (WP14F)** | 117 assumptions; Sections 140–153 (5 deleted WP14D/E) |
| `BeBanking/BEBANKING_ASSUMPTION_REGISTER.csv` | **Approved** | 117 rows; all status = Approved |
| `BeBanking/BEBANKING_GAP_REPORT.md` | **Approved** | 12 gaps (2 CRITICAL, 4 HIGH, 3 MEDIUM, 3 RESEARCH) |
| `BeBanking/BEBANKING_SCOPE_BOUNDARY_GUIDE.md` | **Approved** | 15 scope creep scenarios |

**BU Lead decisions — all resolved WP14F (2026-06-18):** BU-BB-001–010. All decisions applied to pack body. Pack promoted Approved v1.0.

---

## EBS AMS Overlay Packs (WP15D + WP15F) — APPROVED v1.0 2026-06-19

Two overlay packs created in WP15D (2026-06-18) and promoted to Approved v1.0 in WP15F (2026-06-19) after all BU decisions resolved via email governance.

These packs are **additive overlays** to the AMS Base pack — they supplement, not replace, AMS base assumptions. Apply AMS Base first, then the relevant EBS overlay(s) for EBS AMS engagements.

| File | Status | Content |
|---|---|---|
| `AMS/EBS_AMS_SLA_OVERLAY_V1.md` | **Approved v1.0 — 2026-06-19 (WP15F)** | 53 assumptions; EBS-SLA sections: SLA tiers, client-configurable SLAs, resolution tracking, service premium, service credits |
| `AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-19 (WP15F)** | 62 assumptions; EBS-DRM sections: resource model, hours allocation, rollover, absence cover, notice period, runbook |

**EBS SLA Overlay — decisions resolved WP15F:**

| Decision | Item | Resolution |
|---|---|---|
| EBS-SLA-BU-001 | SLA tier structure | Recommended — P1 client-configurable within SLA envelope |
| EBS-SLA-BU-002 | Resolution SLA tracking | Option B — resolution SLAs on-request only; response SLAs always tracked |
| EBS-SLA-BU-003 | SLA premium model | Recommended — fixed monthly premium; no per-ticket surcharge |
| EBS-SLA-BU-004 | Service credits | Option C — negotiate per engagement; no standard credit table |

**EBS DRM Overlay — decisions resolved WP15F:**

| Decision | Item | Resolution |
|---|---|---|
| EBS-DRM-BU-001 | Resource hours model | Recommended — per-engagement hours; ARM IT045 reference architecture applies |
| EBS-DRM-BU-002 | Unused hours rollover | Rollover approved — unused hours expire end of month N+1 |
| EBS-DRM-BU-003 | Absence cover standard | Recommended — 3-BD illness / 10-BD leave standard |
| EBS-DRM-BU-004 | Notice period | 30 calendar days; all 6-week/30-BD references replaced |
| EBS-DRM-BU-005 | Runbook deliverable | Recommended — runbook standard deliverable in all EBS AMS DRM |

---

*ASSUMPTION_LIBRARY_ROADMAP v1.7 | Updated: WP16A — Library Reconciliation Baseline (all counts corrected to body/register-authoritative; Acumatica/BeBanking/EBS overlay packs updated to Approved v1.0; 9 approved packs/overlays; totals 1,060→1,135; approved 613→983; 12 BU decisions remaining) | 2026-06-19*
*Prior update: WP14A — Governance Baseline Correction Pass (eleven documents; OCI count 164→174; totals 1,050→1,060 / 603→613; BeBanking filename corrected) | 2026-06-16*
*Review trigger: Oracle BU Lead resolves 2 HIGH HCM decisions (BU-REC-005/006); then 10 LOW HCM decisions in single session*
