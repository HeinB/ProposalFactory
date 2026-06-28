# Methodology Library Design
**Date:** 2026-06-05
**Purpose:** Define the target methodology library before authoring begins
**Status:** Design only — no documents authored yet
**Feeds into:** `08_Methodologies/` folder structure

> **Note on folder numbering:** The methodology folder is `08_Methodologies/`, not `05_Methodologies/`.
> `05_Certifications/` holds certifications. This document refers throughout to `08_Methodologies/`.

---

## Design Principles

Before defining documents, four principles govern this library:

1. **Write once, cite many.** Cross-BU documents are authored once and referenced from Oracle, Acumatica, and BeBanking tenders. They are never copy-pasted and edited per-BU — changes are made in one place.

2. **Structure for extraction.** Each methodology document is written in named sections. Tender responses pull individual sections ("our testing approach", "our cutover process") without needing the full document. Every section must stand alone.

3. **Separating framework from execution.** A methodology describes HOW. It does not describe a specific client's project. Evaluator credibility comes from the framework being thoughtful and structured; evidence of having done it comes from references.

4. **Authoring from evidence up.** Where historical proposals exist, extract and formalise what was done. Do not invent approach. Where no proposals exist, conduct SME workshops first, then author.

---

## Section 1: Cross-BU vs Business-Unit-Specific Decision

### 1.1 Shared Cross-BU Methodology Documents

The following methodologies apply regardless of which product is being implemented. The governance framework, the way data is migrated, the way testing is run, and the way go-live is managed do not fundamentally change between an Oracle EBS project and an Acumatica Manufacturing project.

Shared documents are stored in `08_Methodologies/Cross_BU/` and **cited by reference** from BU-specific documents. They are the backbone of the methodology library.

| Doc ID | Document | Rationale for Sharing |
|---|---|---|
| METH-X01 | APPSolve Project Management Framework | Governance, RACI, status reporting, escalation, change control are product-agnostic |
| METH-X02 | Data Migration Methodology | Extract-transform-validate-load approach is the same; only source system differs |
| METH-X03 | Change Management and Training Approach | Stakeholder analysis, communication, super-user model, knowledge transfer apply to all ERP and platform projects |
| METH-X04 | Testing Methodology | Test phases, defect management, sign-off criteria are universal |
| METH-X05 | Go-Live and Cutover Methodology | Cutover planning, parallel running, go/no-go criteria, hypercare apply to all implementations |
| METH-X06 | Quality Assurance Framework | Phase gate reviews, deliverable acceptance, quality metrics apply across all projects |
| METH-X07 | Risk Management Approach | Risk identification, rating, mitigation framework is product-agnostic |

### 1.2 Business-Unit-Specific Methodology Documents

These documents are BU-specific because the delivery process, tooling, vendor framework, or technical architecture differs materially between business units.

**Oracle-specific:** Oracle follows its own Oracle Unified Methodology (OUM) / Application Implementation Methodology (AIM) conventions. Oracle Cloud projects differ structurally from Oracle EBS projects (SaaS configuration vs on-premise customisation). OCI infrastructure delivery follows cloud-native patterns. OIC integration delivery has its own design patterns. These cannot be shared meaningfully with Acumatica or BeBanking.

**Acumatica-specific:** Acumatica uses SureStep — a structured 7-phase partner implementation methodology. This is distinct from Oracle's methodology. Manufacturing and Payroll implementations within Acumatica have configuration paths specific to those modules.

**BeBanking-specific:** BeBanking is a product, not a packaged ERP. The delivery methodology is about onboarding a client to a banking platform, establishing bank channels, and integrating with their ERP. This has no overlap with Oracle or Acumatica project delivery.

---

## Section 2: Recommended Folder Structure

```
08_Methodologies/
│
├── FOLDER_INDEX.md                          ← Master index: all 22 methodology documents
│
├── Cross_BU/                                ← 7 shared frameworks (product-agnostic)
│   ├── METH-X01_Project_Management.md
│   ├── METH-X02_Data_Migration.md
│   ├── METH-X03_Change_Management_Training.md
│   ├── METH-X04_Testing_Methodology.md
│   ├── METH-X05_Go_Live_Cutover.md
│   ├── METH-X06_Quality_Assurance.md
│   └── METH-X07_Risk_Management.md
│
├── Oracle/                                  ← 7 Oracle-specific methodologies
│   ├── METH-O01_EBS_Implementation.md
│   ├── METH-O02_EBS_Upgrade.md
│   ├── METH-O03_Cloud_Fusion_Implementation.md
│   ├── METH-O04_OCI_Infrastructure_Deployment.md
│   ├── METH-O05_OIC_Integration_Delivery.md
│   ├── METH-O06_Oracle_Managed_Services.md
│   └── METH-O07_APEX_Development.md
│
├── Acumatica/                               ← 4 Acumatica-specific methodologies
│   ├── METH-A01_SureStep_Implementation.md
│   ├── METH-A02_Manufacturing_Approach.md
│   ├── METH-A03_Payroll_Approach.md
│   └── METH-A04_Acumatica_Managed_Services.md
│
└── BeBanking/                               ← 4 BeBanking-specific methodologies
    ├── METH-B01_Client_Onboarding.md
    ├── METH-B02_ERP_Integration.md
    ├── METH-B03_Bank_Connectivity_Setup.md
    └── METH-B04_Support_Reconciliation_Model.md
```

**Total: 22 methodology documents across 4 folders.**

Each document is a sidecar-style markdown file combining structured YAML frontmatter (for AI retrieval) with the methodology body text (for human use and tender extraction). The METH sidecar template in `00_Governance/Templates/METH_template.md` applies to all 22 files.

---

## Section 3: Document Specifications

### Cross-BU Documents

---

#### METH-X01 — APPSolve Project Management Framework
**Doc ID:** METH-X01
**BU:** Cross
**Impact:** Critical
**Authoring source:** Extract from historical proposals + augment

**Purpose:**
Defines how APPSolve governs and manages any implementation or delivery project — regardless of product. Establishes the governance structure, meeting cadence, status reporting format, escalation matrix, change control process, and RACI assignment model. Answers evaluator questions: "How do you manage projects?", "How do we get visibility of progress?", "What happens when issues arise?", "How are scope changes handled?"

**Typical length:** 8–10 pages

**Standard sections (all reusable across BUs):**
| Section | Content | Reusable? |
|---|---|---|
| Project Governance Structure | Steering committee, project board, workstream leads, project manager | Yes — structure |
| Roles and Responsibilities (RACI) | RACI template with typical APPSolve vs client roles | Yes — template |
| Meeting Cadence | Daily stand-up, weekly status, steering committee, design workshops | Yes |
| Status Reporting | Status report format, RAG indicators, KPI tracking | Yes |
| Change Control Process | Change request lifecycle, approval authority, impact assessment | Yes |
| Escalation Matrix | 3-tier escalation (workstream → PM → Director) | Yes |
| Issue and Action Log Management | How issues are tracked, owned, and resolved | Yes |
| Communication Plan | Stakeholder communication approach | Yes |

**Source material likely in existing proposals:**
- SARB template proposal: likely contains governance section (SARB public sector tenders require detailed governance)
- PPro 2024 proposal: likely contains project management section
- Mauritius Telecom HCM: may contain governance for an offshore/international engagement
- Estimated extraction yield: 50–70% of draft — significant editing needed to generalise

**Dependencies:** None. Can be authored first.

---

#### METH-X02 — Data Migration Methodology
**Doc ID:** METH-X02
**BU:** Cross
**Impact:** Critical
**Authoring source:** Extract from proposals + SME augmentation

**Purpose:**
Defines APPSolve's approach to migrating data from legacy systems into the target system. Covers the full lifecycle: data assessment, mapping, cleansing, trial migrations, validation, and cutover migration. Answers: "How do you ensure our data will be accurate in the new system?", "What happens if data quality is poor?", "How many trial runs do you do?"

This document is cited by all three BUs. The Oracle, Acumatica, and BeBanking-specific methodology documents reference it and note any product-specific variations (e.g., Acumatica data import tools, Oracle ADFdi templates, BeBanking payment file format mapping).

**Typical length:** 10–14 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Data Migration Philosophy | Clean-in, clean-out principle; client data ownership | Yes |
| Data Assessment Phase | Source system audit, data volume, quality scoring | Yes |
| Data Mapping | Source-to-target field mapping, transformation rules | Yes — structure |
| Data Cleansing Approach | Cleansing rules, client responsibility, tools | Yes |
| Trial Migration Runs | How many trial runs, what is validated each round | Yes |
| Data Validation Framework | Reconciliation reports, count/total checks, exception management | Yes |
| Cutover Migration | Final data freeze, migration execution, validation sign-off | Yes |
| Roles and Responsibilities | APPSolve vs client data ownership during migration | Yes |
| Data Migration Risk Management | Top migration risks and mitigations | Yes |

**BU-specific notes sections** (short additions at end, not full sections):
- Oracle: ADFdi, FBDI, Data Load templates; Oracle-specific validation queries
- Acumatica: Import scenarios, Acumatica data import templates, Excel import validation
- BeBanking: Payment file format mapping (ISO 20022, proprietary bank formats), bank account validation

**Source material likely in existing proposals:**
- Oracle EBS proposals (SARB, PPro) likely describe data migration — EBS projects are data-heavy
- Estimated extraction yield: 40–60% of a draft

---

#### METH-X03 — Change Management and Training Approach
**Doc ID:** METH-X03
**BU:** Cross
**Impact:** High
**Authoring source:** Partial extract; significant fresh authoring needed

**Purpose:**
Defines how APPSolve manages organisational change and delivers training during system implementations. Covers: stakeholder analysis, change impact assessment, communication planning, super-user identification and training, end-user training, and post-go-live knowledge transfer. Answers: "How do you manage user adoption?", "What training will our staff receive?", "How do you handle resistance to change?"

**Typical length:** 8–12 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Change Management Philosophy | People-first; change as a project workstream not an afterthought | Yes |
| Stakeholder Analysis | Identification, impact classification, engagement strategy | Yes — template |
| Change Impact Assessment | Role-by-role impact analysis approach | Yes |
| Communication Plan | Audience, message, channel, timing matrix | Yes — template |
| Super-User Model | Selection criteria, training programme, role during UAT and go-live | Yes |
| Training Needs Analysis | How training requirements are identified per role | Yes |
| Training Delivery Approach | Classroom, self-paced, train-the-trainer, role plays | Yes |
| Training Materials | What APPSolve produces (guides, job aids, videos) | Yes |
| Knowledge Transfer | How knowledge transfers to the client team at end of project | Yes |
| Post-Go-Live Adoption Support | Hypercare support for user adoption queries | Yes |

**Source material likely in existing proposals:**
- Mauritius Telecom HCM: HCM is change-heavy; likely to contain training and change management sections
- Estimated extraction yield: 30–50% — HCM proposals tend to address this; ERP finance proposals less so

---

#### METH-X04 — Testing Methodology
**Doc ID:** METH-X04
**BU:** Cross
**Impact:** Critical
**Authoring source:** Likely partial extraction from proposals; significant authoring needed

**Purpose:**
Defines APPSolve's structured approach to testing throughout the implementation lifecycle. Covers all test types: unit testing, system integration testing (SIT), user acceptance testing (UAT), regression testing, and performance testing. Answers: "How do you test the system before go-live?", "What is your defect management process?", "How do you handle UAT?", "When do you sign off that the system is ready?"

**Typical length:** 8–12 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Testing Philosophy | Quality at source; testing is continuous, not a phase | Yes |
| Test Types and Sequence | Unit → SIT → UAT → Regression → Performance | Yes |
| Test Planning | Test plan structure, entry/exit criteria per test type | Yes — template |
| Test Case Design | How test cases are written, who writes them | Yes |
| Unit Testing | Developer-level testing; APPSolve responsibility | Yes |
| System Integration Testing (SIT) | End-to-end process testing; cross-module flows | Yes |
| User Acceptance Testing (UAT) | Client-led; APPSolve facilitation and defect support | Yes |
| Defect Management | Severity classification (P1–P4), lifecycle, resolution SLAs | Yes |
| Regression Testing | When and how regression is run after fixes | Yes |
| Test Sign-Off Process | Criteria for proceeding to go-live; client sign-off | Yes |
| Testing Roles | APPSolve test lead, client UAT coordinator, business testers | Yes |

**BU-specific additions** (short notes only):
- Oracle: Oracle test scripts, UPK/OTL for test documentation
- Acumatica: Acumatica test scenarios by module
- BeBanking: Payment cycle testing, bank parallel processing tests, reconciliation validation

**Source material likely in existing proposals:**
- Oracle proposals likely contain testing overview; level of detail varies
- Estimated extraction yield: 30–50%

---

#### METH-X05 — Go-Live and Cutover Methodology
**Doc ID:** METH-X05
**BU:** Cross
**Impact:** Critical
**Authoring source:** Partial extraction possible; significant authoring needed

**Purpose:**
Defines how APPSolve plans and executes system go-live events. Covers: cutover planning (weeks before), parallel running (where applicable), go/no-go assessment, the cutover execution weekend, and hypercare support post go-live. Answers: "How do you minimise go-live risk?", "What happens if go-live fails?", "What support do you provide in the first weeks after go-live?"

**Typical length:** 8–12 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Go-Live Planning Timeline | 8–4–2–1 week countdown activities | Yes |
| Cutover Plan Structure | Task list, owner, timing, dependencies | Yes — template |
| Parallel Running Approach | When it's required, how reconciliation works, duration | Yes |
| Go/No-Go Criteria | The conditions that must be met before proceeding | Yes — template |
| Go/No-Go Review Meeting | Who attends, decision authority, outcome actions | Yes |
| Cutover Execution | Sequence of events during the cutover window | Yes — template |
| Hypercare Support Model | First 4–8 weeks post go-live; dedicated support resources | Yes |
| Escalation During Cutover | Who can be called and when during cutover weekend | Yes |
| Post Go-Live Review | Lessons learned, performance review, stabilisation sign-off | Yes |

**BU-specific variations** (noted in BU-specific methodology docs):
- Oracle: Oracle-specific cutover tasks (concurrent programs, interface enablement, profile option changes)
- Acumatica: Acumatica specific cutover (user activation, custom reports, automation schedules)
- BeBanking: Bank channel cutover, parallel payment processing, first live payment supervision

**Source material likely in existing proposals:**
- Oracle proposals should address cutover; level of detail may be shallow
- Estimated extraction yield: 30–40%

---

#### METH-X06 — Quality Assurance Framework
**Doc ID:** METH-X06
**BU:** Cross
**Impact:** High
**Authoring source:** Must author from scratch

**Purpose:**
Defines how APPSolve assures quality across all project deliverables and phases. Covers: phase gate reviews, deliverable standards, peer review processes, internal QA checkpoints, client sign-off milestones, and quality metrics. Answers: "What internal quality controls do you have?", "How do we know deliverables meet standards?", "Who checks your work?"

**Typical length:** 6–8 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Quality Philosophy | Quality built in, not inspected in; APPSolve quality standards | Yes |
| Phase Gate Reviews | What is reviewed at end of each project phase | Yes |
| Deliverable Standards | What constitutes an acceptable deliverable | Yes — template |
| Peer Review Process | Internal review before client delivery | Yes |
| Client Sign-Off Process | How deliverables are formally accepted | Yes — template |
| Quality Metrics | On-time delivery, defect rate, UAT pass rate | Yes |
| Independent QA (if applicable) | When external QA review is appropriate | Yes |

**Source material:** Unlikely to exist in proposals. Must be authored from scratch with delivery team input.

---

#### METH-X07 — Risk Management Approach
**Doc ID:** METH-X07
**BU:** Cross
**Impact:** High
**Authoring source:** Partial extraction possible; augmentation needed

**Purpose:**
Defines how APPSolve identifies, assesses, plans for, and monitors project risks. Covers: risk identification workshops, risk register structure, likelihood/impact rating, risk owner assignment, mitigation strategies, and risk reporting. Answers: "How do you manage project risk?", "Can we see your risk register?", "How do you handle risks that materialise?"

**Typical length:** 6–8 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Risk Management Philosophy | Proactive identification; shared responsibility | Yes |
| Risk Identification | Workshops, risk prompt lists, ongoing identification | Yes |
| Risk Rating Framework | Likelihood × Impact matrix (3×3 or 5×5) | Yes — template |
| Risk Register Structure | Fields: ID, description, likelihood, impact, rating, owner, mitigation, due date | Yes — template |
| Risk Response Types | Accept, avoid, transfer, mitigate | Yes |
| Risk Reporting | How risks are reported in status meetings and steering committees | Yes |
| Top Project Risks by Category | Standard ERP top risks and mitigations | Partial — supplement per BU |

**BU-specific additions:** Top risk lists differ by BU (Oracle data migration risks ≠ Acumatica payroll compliance risks ≠ BeBanking bank connectivity risks). Each BU-specific methodology document includes a risk section with product-specific risks.

**Source material:** Likely fragments in Oracle proposals. Estimated extraction yield: 30–40%.

---

### Oracle-Specific Documents

---

#### METH-O01 — Oracle EBS Implementation Methodology
**Doc ID:** METH-O01
**BU:** Oracle
**Impact:** Critical
**Authoring source:** Strong — extract from all 3 historical proposals

**Purpose:**
APPSolve's structured approach to implementing Oracle E-Business Suite, from Inception through to Operate. Covers all standard Oracle AIM/OUM phases, EBS-specific workstreams (Financials, Projects, HR/Payroll, Procurement), configuration and customisation approach, and the Oracle-specific technical environment. Answers: "Describe your Oracle EBS implementation methodology", "How do you handle CEMLI development?", "How long does an EBS implementation take?"

**Typical length:** 14–18 pages

**Standard sections:**
| Section | Content | Reusable cross-project? |
|---|---|---|
| Methodology Overview | Oracle AIM/OUM heritage; APPSolve adaptation | Yes |
| Phase 1: Inception and Discovery | Project setup, current state analysis, business requirements | Yes |
| Phase 2: Solution Architecture | Solution design, CEMLI register, gap analysis | Yes |
| Phase 3: Build and Configure | Configuration workbooks, CEMLI development, data migration prep | Yes |
| Phase 4: System Integration Testing | SIT approach (references METH-X04) | Cite METH-X04 |
| Phase 5: User Acceptance Testing | UAT facilitation, client responsibilities | Cite METH-X04 |
| Phase 6: Go-Live and Cutover | EBS-specific cutover tasks | Cite METH-X05 + EBS specifics |
| Phase 7: Hypercare and Stabilisation | First 4–8 weeks post go-live | Cite METH-X05 |
| EBS CEMLI Framework | How customisations are classified, designed, developed | Yes |
| Oracle EBS Technical Environment | Database, middleware, concurrent processing, patching | Yes — technical audience |
| Project Governance | References METH-X01 | Cite METH-X01 |
| Data Migration | EBS-specific tools (ADFdi, FBDI); references METH-X02 | Cite METH-X02 + EBS tools |
| Testing | References METH-X04 with EBS-specific test scripts | Cite METH-X04 |
| EBS-Specific Risks | Data conversion, CEMLI complexity, interface failures | Yes — supplement METH-X07 |
| Key Deliverables per Phase | Deliverable list with owners | Yes |

**Source material:**
- `APPSolve SARB XxxxXxxx - PRxxxx.NEW 2022.docx` — SARB is an EBS client; this proposal likely contains the fullest EBS methodology description
- `APPSolve_PPro_Proposal_20240712_V2.0.docx` — 2024 proposal, likely Oracle Cloud or EBS
- **Estimated extraction yield: 60–75%** — this is the most available source material in the KB

---

#### METH-O02 — Oracle EBS Upgrade Methodology
**Doc ID:** METH-O02
**BU:** Oracle
**Impact:** Medium
**Authoring source:** Limited — may need SME input

**Purpose:**
Defines APPSolve's approach to Oracle EBS version upgrades (e.g., 12.1.3 to 12.2.x). Distinct from fresh implementation: an upgrade must coexist with a live system, carry forward all CEMLIs, preserve data, and manage functional delta changes. Answers: "Have you done EBS upgrades?", "How do you manage CEMLI compatibility?", "How do you test an upgrade without disrupting production?"

**Typical length:** 10–14 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Upgrade vs Reimplementation Decision | When to upgrade vs when to start fresh | Yes |
| Pre-Upgrade Assessment | Technical health check, CEMLI inventory, customisation impact analysis | Yes |
| Upgrade Approach | Technical upgrade path, online patching (12.2.x) | Technical — stable |
| CEMLI Remediation | How CEMLIs are assessed, fixed, tested post-upgrade | Yes |
| Functional Delta Analysis | What changed between versions, what client needs to know | Yes — structure |
| Parallel Environment Strategy | Running upgrade in parallel with production | Yes |
| Testing Strategy | Regression focus (most configurations already tested in production) | Cite METH-X04 |
| Cutover | Similar to implementation but faster — less data migration | Cite METH-X05 |
| EBS 12.2 Online Patching | Specific to 12.2.x — edition-based redefinition | Technical — stable |

**Source material:** Unlikely to be in the 3 proposals (which are likely new implementations). Requires input from EBS technical team and architect.
**Estimated extraction yield: 10–20%**

---

#### METH-O03 — Oracle Cloud (Fusion) Implementation Methodology
**Doc ID:** METH-O03
**BU:** Oracle
**Impact:** Critical
**Authoring source:** Extract from Mauritius Telecom HCM + augment

**Purpose:**
APPSolve's delivery methodology for Oracle Cloud SaaS applications (Oracle Fusion Finance, HCM, SCM, Procurement, Projects). Fundamentally different from EBS: configuration-first, limited customisation, Oracle-managed infrastructure, quarterly update cycles, and standardised integration patterns. Answers: "How do you implement Oracle Cloud?", "How do you manage Oracle quarterly updates?", "How is Oracle Cloud implementation different from EBS?"

**Typical length:** 14–18 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Oracle Cloud vs EBS — Key Differences | SaaS model, no CEMLIs, quarterly updates, OCI hosting | Yes |
| APPSolve Cloud Methodology Overview | Configured for SaaS — accelerated phases | Yes |
| Phase 1: Initiate and Plan | Project setup, environment provisioning, team onboarding | Yes |
| Phase 2: Analyse and Design | Business process mapping, configuration workbooks, extension decisions | Yes |
| Phase 3: Build and Configure | Tenant configuration, sandbox, OTBI reports, integrations | Yes |
| Phase 4: Test | SIT → UAT (cite METH-X04); Cloud-specific test approach | Yes |
| Phase 5: Deploy | Production configuration, data migration, user provisioning | Cite METH-X02 |
| Phase 6: Go-Live and Hypercare | Oracle Cloud cutover tasks; hypercare plan | Cite METH-X05 |
| Oracle Quarterly Update Management | How APPSolve manages update cycles for live clients | Yes — unique to Cloud |
| Oracle Cloud Extensions | When to use OIC, APEX, or REST APIs instead of CEMLI | Yes |
| Oracle Cloud Integration Approach | Pre-built adapters, OIC, REST APIs — overview | References METH-O05 |
| Environment Strategy | Development, Test, UAT, Production environment management | Yes |
| Oracle Cloud Governance | Oracle SR process, MOS, cloud support during implementation | Yes |
| Data Migration | Oracle FBDI, OTBI, HDL (HCM) — references METH-X02 | Cite METH-X02 + tools |

**Source material:**
- `APPSolve Mauritius Telecom - HCM Proposal V3.0.docx` — Oracle Cloud HCM; likely richest source for Cloud methodology
- ETS Tender proposals likely include Cloud Finance or HCM content
- **Estimated extraction yield: 50–65%**

---

#### METH-O04 — OCI Infrastructure Deployment Methodology
**Doc ID:** METH-O04
**BU:** Oracle
**Impact:** Medium
**Authoring source:** Must author from scratch with OCI specialist

**Purpose:**
Defines how APPSolve designs and deploys Oracle Cloud Infrastructure tenancies — landing zone design, network topology, security baseline, compute and storage provisioning, OCI governance setup, and managed services handover. Answers: "How do you design an OCI environment?", "What is your OCI security baseline?", "How do you manage OCI post-deployment?"

**Typical length:** 10–14 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| OCI Architecture Patterns | Common patterns: lift-and-shift, cloud-native, hybrid | Yes |
| Landing Zone Design | Compartments, VCN, IAM, tenancy setup | Technical — stable |
| Network Topology | VCN, subnets, security lists, load balancers, FastConnect | Technical — stable |
| Security Baseline | CIS OCI benchmark; key controls | Technical — stable |
| Compute and Storage | Shapes, flexible instances, block and object storage sizing | Yes |
| OCI Governance | Tagging strategy, quotas, budget alerts, audit logging | Yes |
| OCI Tools | Terraform for IaC, OCI CLI, OCI DevOps | Yes |
| Managed Services for OCI | Ongoing monitoring, patching, cost optimisation (references METH-O06) | Cite METH-O06 |
| DR and Backup | RPO/RTO approach, cross-region backup, DR testing | Yes |

**Source material:** Unlikely in any current proposals. Requires OCI architect / technical lead SME input.
**Estimated extraction yield: 0–10%**

---

#### METH-O05 — Oracle Integration Cloud (OIC) Delivery Methodology
**Doc ID:** METH-O05
**BU:** Oracle
**Impact:** Medium-High
**Authoring source:** Must author — limited source material

**Purpose:**
Defines APPSolve's approach to designing and delivering Oracle Integration Cloud integrations. Covers: integration assessment and pattern selection, adapter configuration, mapping design, error handling, monitoring and alerting, versioning, and deployment to production. Answers: "How do you design Oracle integrations?", "How do you handle integration errors?", "How are integrations monitored post go-live?"

**Typical length:** 10–14 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| OIC in the Oracle Architecture | Where OIC fits: Oracle Cloud, EBS, third-party | Yes |
| Integration Assessment | Identifying integration requirements, pattern selection | Yes |
| OIC Design Patterns | App-to-app, pub-sub, API-led, scheduled | Yes |
| Adapter Configuration | Oracle, REST, SOAP, FTP, DB adapters | Technical — stable |
| Mapping and Transformation | XSLT, expression language, data normalization | Technical |
| Error Handling Framework | Global error handling, notifications, retry logic | Yes |
| Integration Testing | Unit test, end-to-end test, monitoring check | Cite METH-X04 |
| OIC Monitoring and Alerting | Instance monitoring, SLA tracking, alert configuration | Yes |
| Deployment to Production | OIC package export/import, environment promotion | Yes |
| Versioning and Change Management | How integration versions are managed | Yes |

**Source material:** May have fragments in Oracle Cloud proposals where integrations were described. Dedicated OIC content unlikely.
**Estimated extraction yield: 15–25%**

---

#### METH-O06 — Oracle Managed Services Methodology
**Doc ID:** METH-O06
**BU:** Oracle
**Impact:** Critical
**Authoring source:** Must author from scratch with service delivery team

**Purpose:**
Defines how APPSolve delivers ongoing Oracle application management and support services (AMS) for both Oracle EBS and Oracle Cloud clients. Covers: incident management, service levels, SLA structure, service desk operation, application management, patch management, enhancement pipeline management, and service review governance. Answers: "How does your managed support service work?", "What are your SLAs?", "What do we get for our monthly retainer?", "How are enhancement requests handled?"

This is the most commercially important methodology document for Oracle — most of APPSolve's reference clients appear to be on managed support retainers.

**Typical length:** 12–18 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Managed Services Overview | What is included; scope definition; what is excluded | Yes |
| Incident Management | P1–P4 classification, response SLAs, resolution SLAs | Yes — SLA table |
| Service Desk | How incidents are logged, owned, tracked | Yes |
| Application Management | Monthly application health checks, user management, configuration changes | Yes |
| Oracle Patch Management | EBS: CPU/PSU patches; Cloud: quarterly update management | Oracle-specific |
| Enhancement Management | How enhancement requests flow from request to delivery | Yes |
| Proactive Monitoring | System health monitoring, scheduled jobs, interfaces | Yes |
| Monthly Service Review | Governance meeting: SLA performance, capacity, upcoming changes | Yes |
| Escalation Matrix | Escalation path within APPSolve and to Oracle | Yes |
| SLA Schedule | Full SLA table (the key commercial attachment) | Yes — template |
| On/Off-Shore Support | How support is delivered; time zones; coverage model | Yes |
| Transition-In Methodology | How APPSolve takes over support from a previous vendor | Yes — unique |

**Source material:** Brief description may exist in company profiles. The support reference letters (Adcock, ARM, Assore, etc.) can inform what services are described. But a formal methodology document does not exist.
**Estimated extraction yield: 5–15% (from company profile snippets)**

---

#### METH-O07 — Oracle APEX Development Methodology
**Doc ID:** METH-O07
**BU:** Oracle
**Impact:** Low-Medium
**Authoring source:** Must author from scratch with APEX practice lead

**Purpose:**
Defines APPSolve's approach to developing and delivering Oracle APEX applications. Covers: requirements discovery for APEX builds, application design, development sprints, code review, OCI deployment, UAT, and handover. Positioned for organisations wanting low-code Oracle extensions or standalone APEX applications.

**Typical length:** 8–10 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| APEX in APPSolve's Oracle Practice | Where APEX fits: extensions, portals, reporting | Yes |
| Discovery and Requirements | APEX-specific requirements: data sources, user roles, UI needs | Yes |
| Application Architecture | APEX workspace, multi-page app design, REST integrations | Technical |
| Agile Delivery Approach | Sprint structure, demo-and-iterate, acceptance per sprint | Yes |
| Development Standards | Naming conventions, page design standards, security | Technical |
| Code Review Process | Internal review, security review | Cite METH-X06 |
| OCI Deployment | APEX on OCI: workspace export, production deployment | Technical |
| UAT and Acceptance | User testing, issue resolution (cite METH-X04) | Cite METH-X04 |
| Handover and Documentation | How the application is handed over to client admin | Yes |

**Source material:** None. Requires APEX practice lead input.

---

### Acumatica-Specific Documents

---

#### METH-A01 — Acumatica SureStep Implementation Methodology
**Doc ID:** METH-A01
**BU:** Acumatica
**Impact:** Critical
**Authoring source:** Must author from scratch — no existing material

**Purpose:**
APPSolve's adapted version of Acumatica's SureStep partner implementation methodology. Covers all seven SureStep phases with APPSolve-specific activities, deliverables, and responsibilities. The primary methodology document for any Acumatica implementation tender. Answers: "How do you implement Acumatica?", "What methodology do you follow?", "How long does Acumatica take to implement?", "What do we need to do as the client?"

**Typical length:** 14–18 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Acumatica SureStep Overview | The 7-phase framework; why APPSolve uses it | Yes |
| Phase 1: Initiation | Project kick-off, environment setup, team onboarding | Yes |
| Phase 2: Analysis | Current state assessment, business process mapping, gap analysis | Yes |
| Phase 3: Design | Solution design, Acumatica configuration plan, integration design | Yes |
| Phase 4: Development | Configuration, customisation, import scenarios, report development | Yes |
| Phase 5: Testing | SIT and UAT (cite METH-X04); Acumatica test scenarios | Cite METH-X04 |
| Phase 6: Deployment | Data migration (cite METH-X02), go-live (cite METH-X05) | Cite both |
| Phase 7: Post Go-Live | Hypercare, stabilisation, transition to support | Yes |
| Acumatica Configuration Approach | How configuration is documented (workbooks) | Yes |
| Acumatica Customisation Framework | When to customise vs configure; customisation standards | Yes |
| Acumatica Integration Approach | Import scenarios, REST APIs, Acumatica marketplace | Yes |
| Client Responsibilities | What the client must provide and do during each phase | Yes |
| Acumatica-Specific Risks | License activation, import scenario complexity, customisation conflicts | Supplement METH-X07 |

**Source material:** None. Must workshop with Acumatica delivery team. Acumatica publishes SureStep guidance for partners — APPSolve's partner portal may have reference material.
**Estimated extraction yield: 0%**

---

#### METH-A02 — Acumatica Manufacturing Implementation Approach
**Doc ID:** METH-A02
**BU:** Acumatica
**Impact:** High
**Authoring source:** Must author from scratch

**Purpose:**
Supplement to METH-A01 covering Manufacturing-specific implementation considerations within Acumatica. Covers: BOM and routing setup, production order workflow, MRP/MPS configuration, shop floor data capture, inventory costing methods, and integration with distribution. Answers: "Do you have experience implementing Acumatica Manufacturing?", "How do you set up MRP?", "How do you handle complex BOM structures?"

**Typical length:** 8–12 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Manufacturing Module Overview | What Acumatica Manufacturing covers; where it fits | Yes |
| Bill of Materials (BOM) Setup Approach | BOM structure, revision management, phantom assemblies | Manufacturing-specific |
| Routing and Work Centre Configuration | Work centres, operations, routing setup | Manufacturing-specific |
| Production Order Workflow | Order types, release process, actual vs estimated | Manufacturing-specific |
| MRP / MPS Configuration | Demand planning, supply planning, MRP exceptions | Manufacturing-specific |
| Inventory Costing Configuration | Standard, average, FIFO — decision guidance | Yes |
| Shop Floor Considerations | Data capture, labour tracking | Manufacturing-specific |
| Manufacturing–Distribution Integration | How manufacturing feeds distribution; inventory movement | Yes |
| Pre-Requisites and Client Readiness | What the client must have defined before configuration starts | Yes |

**Source material:** None. Requires Acumatica Manufacturing specialist input. ATS and Maxiflex references (if reviewed) may provide project context clues.
**Estimated extraction yield: 0%**

---

#### METH-A03 — Acumatica Payroll Implementation Approach
**Doc ID:** METH-A03
**BU:** Acumatica
**Impact:** High
**Authoring source:** Must author from scratch

**Purpose:**
Supplement to METH-A01 covering Payroll-specific implementation in Acumatica. South Africa-specific regulatory compliance is central: SARS PAYE, UIF, SDL, Skills Levy, IRP5/IT3 generation, COIDA. Answers: "Can you implement Acumatica Payroll for a South African company?", "How do you handle SARS compliance?", "What is your parallel payroll run approach?"

**Typical length:** 8–12 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| SA Payroll Legislation Scope | PAYE, UIF, SDL, Skills Levy, COIDA — which are handled | SA-specific |
| Pay Structure Configuration | Pay codes, deduction codes, leave types, benefit structures | Yes |
| SARS Integration | IRP5/IT3 generation, EMP201/501 submission approach | SA-specific |
| Leave Management | Leave types, accrual rules, negative leave | Yes |
| Payroll Parallel Run Approach | How many parallel runs, what is reconciled, sign-off criteria | Yes |
| Integration with HR (if applicable) | Acumatica HR or third-party HRIS integration | Yes |
| Payroll Reporting | Standard payroll reports, custom report requirements | Yes |
| Post Go-Live Payroll Support | Payroll-specific hypercare: first live payroll, SARS submission | Yes |

**Source material:** None. Requires Acumatica Payroll specialist input.
**Estimated extraction yield: 0%**

---

#### METH-A04 — Acumatica Managed Services Methodology
**Doc ID:** METH-A04
**BU:** Acumatica
**Impact:** Medium
**Authoring source:** Partially inherit from METH-O06 structure; Acumatica-specific additions needed

**Purpose:**
How APPSolve delivers ongoing managed support and application management for Acumatica clients post go-live. Similar structure to METH-O06 but with Acumatica-specific content: Acumatica push update management, marketplace app support, customisation versioning, and Acumatica-specific incident categories.

**Typical length:** 10–14 pages

**Standard sections:**
| Section | Content | Reusable from METH-O06? |
|---|---|---|
| Managed Services Overview | Scope, inclusions, exclusions | Adapt from METH-O06 |
| Incident Management + SLA Table | P1–P4 with Acumatica-specific examples | Largely reuse METH-O06 |
| Acumatica Push Update Management | How APPSolve manages Acumatica's automatic updates | Acumatica-specific |
| Customisation Version Management | How customisations are versioned and maintained across updates | Acumatica-specific |
| Marketplace App Support | Which marketplace apps APPSolve can support | Acumatica-specific |
| Enhancement Management | As per METH-O06 | Reuse METH-O06 |
| Monthly Service Review | As per METH-O06 | Reuse METH-O06 |

**Source material:** Structure largely inherited from METH-O06 once that is written.
**Estimated extraction yield: 60% once METH-O06 is complete (structural reuse)**

---

### BeBanking-Specific Documents

---

#### METH-B01 — BeBanking Client Onboarding Methodology
**Doc ID:** METH-B01
**BU:** BeBanking
**Impact:** Critical
**Authoring source:** Must author from scratch — requires product SME briefing first

**Purpose:**
End-to-end methodology for onboarding a new corporate client onto the BeBanking platform. Covers: requirements gathering, bank connectivity setup, platform configuration, testing (including parallel payment processing), go-live, and post go-live support. This is the primary methodology document for any BeBanking tender. Answers: "How does the BeBanking implementation work?", "How long does it take?", "What do we need to do as the client?", "How is the first live payment managed?"

**Typical length:** 10–14 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| BeBanking Platform Overview | What BeBanking does; core components | Yes |
| Client Readiness Assessment | What must be in place before onboarding starts | Yes |
| Phase 1: Requirements and Design | Payment types, bank relationships, ERP integration requirements, file formats | Yes |
| Phase 2: Bank Connectivity Setup | Which banks, channel type, bank-side setup (client's bank contact) | Yes — structure |
| Phase 3: Platform Configuration | Payment templates, approval workflows, user roles, notification rules | Yes |
| Phase 4: ERP Integration Setup | Payment file export from ERP; reconciliation import | References METH-B02 |
| Phase 5: Testing | Payment cycle testing, parallel processing, reconciliation validation | Yes |
| Phase 6: Go-Live | First live payment supervision, cutover from legacy | Yes |
| Phase 7: Post Go-Live Support | Reconciliation support, payment failure resolution, user queries | References METH-B04 |
| Client Responsibilities | Bank mandates, ERP readiness, staff availability | Yes |
| Typical Timeline | Realistic duration by complexity tier | Yes |

**Source material:** None from Tender Pack. Must be authored by BeBanking product owner or delivery lead.
**Estimated extraction yield: 0%**

---

#### METH-B02 — BeBanking ERP Integration Methodology
**Doc ID:** METH-B02
**BU:** BeBanking
**Impact:** High
**Authoring source:** Must author from scratch; Tiger/SAA DOCX files may provide clues

**Purpose:**
Defines how BeBanking is integrated with a client's ERP system (Oracle EBS, Oracle Cloud, SAP, Acumatica, or other). Covers: payment file format mapping, ERP configuration to generate payment files, BeBanking import configuration, reconciliation file format, and the integration testing approach. Answers: "How does BeBanking connect to our Oracle/SAP/Acumatica system?", "What file formats are supported?", "How does reconciliation work?"

**Typical length:** 10–14 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Integration Architecture Options | File-based vs API; push vs pull; supported formats | Yes |
| ERP Payment File Configuration | How the ERP is configured to generate BeBanking-compatible payment files | Per-ERP — split by subsection |
| Payment File Format Specification | Structure of standard BeBanking payment file | Yes |
| BeBanking Import Configuration | How BeBanking ingests the payment file from the ERP | Yes |
| Reconciliation File | Structure of return file from BeBanking back to ERP | Yes |
| ERP Reconciliation Import | How the ERP processes the return reconciliation | Per-ERP |
| Integration Testing Approach | Test scenarios, parallel run, reconciliation validation | Yes |
| Error Handling | What happens when a payment file has errors | Yes |
| ERP-Specific Subsections | Oracle EBS, Oracle Cloud, SAP, Acumatica integration notes | Per-ERP |

**Source material:** `Tiger Reference Letter BeBanking SAP.docx` and `SAA Tiger Reference Letter SAP Integration.docx` may describe the integration context — review before authoring. Otherwise, must workshop with BeBanking technical team.
**Estimated extraction yield: 5–15% (if Tiger/SAA DOCX files contain integration details)**

---

#### METH-B03 — BeBanking Bank Connectivity Setup
**Doc ID:** METH-B03
**BU:** BeBanking
**Impact:** Medium
**Authoring source:** Must author from scratch with BeBanking technical team

**Purpose:**
Defines the technical process for establishing bank channel connectivity between BeBanking and South African banks. Covers: supported channel types (SFTP, API, host-to-host), bank-by-bank setup requirements, bank-side mandate and configuration, connectivity testing, and go-live. This document is often required in tenders from financial institutions or from large corporate clients with complex banking relationships.

**Typical length:** 8–12 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| Supported Bank Channel Types | SFTP, direct API, host-to-host — when each is used | Yes |
| Supported Banks | Which South African banks BeBanking is connected to | Yes |
| Bank Mandate Requirements | What the client must set up with their bank | Yes |
| Bank-Side Configuration | What each bank needs to configure on their side | Bank-specific |
| BeBanking-Side Configuration | Connectivity settings within BeBanking | Yes |
| Connectivity Testing | How the channel is tested before go-live | Yes |
| Bank Connectivity Troubleshooting | Common issues and resolution approach | Yes |
| Ongoing Connectivity Monitoring | How bank channel health is monitored | References METH-B04 |

**Source material:** None from Tender Pack. Requires BeBanking technical team input.
**Estimated extraction yield: 0%**

---

#### METH-B04 — BeBanking Support and Reconciliation Model
**Doc ID:** METH-B04
**BU:** BeBanking
**Impact:** High
**Authoring source:** Partially inherit from METH-O06 structure; BeBanking-specific additions

**Purpose:**
Defines how APPSolve supports BeBanking clients post go-live. Covers: payment failure management (which has urgency and financial impact), reconciliation support, bank query management, user support, SLA definitions, and the escalation chain to banks. Fundamentally different from Oracle/Acumatica support because payment failures have immediate financial consequences.

**Typical length:** 10–14 pages

**Standard sections:**
| Section | Content | Reusable? |
|---|---|---|
| BeBanking Support Model Overview | Scope, what is included, 24-hour considerations for payment failures | Unique — payment urgency |
| Payment Failure Management | Classification, immediate response, resolution, re-submission | BeBanking-specific |
| Incident SLAs | P1 = payment failure; faster SLAs than standard software support | Unique to BeBanking |
| Reconciliation Support | How APPSolve assists with reconciliation exceptions | BeBanking-specific |
| Bank Query Management | How APPSolve escalates to the bank on the client's behalf | BeBanking-specific |
| User Support | How end-user queries are handled | Adapt from METH-O06 |
| Reporting and Service Reviews | Monthly payment statistics, exceptions, SLA performance | Adapt from METH-O06 |
| Escalation Matrix | APPSolve escalation + bank escalation | Unique to BeBanking |

**Source material:** Structure partially from METH-O06. BeBanking-specific content requires product/support team input.

---

## Section 4: Priority Ranking — Documents to Author First

Ranked by: frequency required in tenders × evaluator scoring weight × BU pipeline urgency.

| Rank | Doc ID | Document | BU | Rationale |
|---|---|---|---|---|
| **1** | METH-X01 | Project Management Framework | Cross | Required in every tender; high evaluator score; 50–70% extractable from proposals |
| **2** | METH-O01 | Oracle EBS Implementation Methodology | Oracle | Most common Oracle tender; 60–75% extractable; source material is richest |
| **3** | METH-O03 | Oracle Cloud (Fusion) Implementation Methodology | Oracle | Growing demand; HCM proposal as source; 50–65% extractable |
| **4** | METH-X04 | Testing Methodology | Cross | Required in almost every implementation tender; cited by 6+ other documents |
| **5** | METH-X02 | Data Migration Methodology | Cross | Required in every implementation tender; cited by Oracle, Acumatica, BeBanking methodology docs |
| **6** | METH-O06 | Oracle Managed Services Methodology | Oracle | Most commercially important for Oracle retainers; 7 support references need a methodology to back them |
| **7** | METH-A01 | Acumatica SureStep Implementation Methodology | Acumatica | Every Acumatica tender; currently zero content; high urgency |
| **8** | METH-X05 | Go-Live and Cutover Methodology | Cross | Required in every implementation tender; cited by all BU-specific documents |
| **9** | METH-X03 | Change Management and Training Approach | Cross | Frequently scored; sources in HCM proposals |
| **10** | METH-B01 | BeBanking Client Onboarding Methodology | BeBanking | Critical for BeBanking tenders; currently zero content; requires SME first |
| **11** | METH-X07 | Risk Management Approach | Cross | Required in most tenders; moderate effort |
| **12** | METH-O05 | OIC Integration Delivery Methodology | Oracle | Integration tenders growing; OIC skills already certified |
| **13** | METH-X06 | Quality Assurance Framework | Cross | Frequently asked but lower scoring weight; author from scratch |
| **14** | METH-A02 | Acumatica Manufacturing Approach | Acumatica | High demand in manufacturing sector tenders |
| **15** | METH-B02 | BeBanking ERP Integration Methodology | BeBanking | Needed for any ERP + BeBanking tender |
| **16** | METH-A03 | Acumatica Payroll Approach | Acumatica | Payroll tenders are common in SA ERP market |
| **17** | METH-B04 | BeBanking Support and Reconciliation Model | BeBanking | Needed for BeBanking managed service proposals |
| **18** | METH-O04 | OCI Infrastructure Deployment Methodology | Oracle | Infrastructure tenders; requires specialist input |
| **19** | METH-A04 | Acumatica Managed Services Methodology | Acumatica | Largely inherits from METH-O06 once that is done |
| **20** | METH-B03 | BeBanking Bank Connectivity Setup | BeBanking | Technical; lower tender frequency |
| **21** | METH-O02 | Oracle EBS Upgrade Methodology | Oracle | Less frequent; author when upgrade pipeline grows |
| **22** | METH-O07 | Oracle APEX Development Methodology | Oracle | Niche; author when APEX pipeline develops |

---

## Section 5: Authoring Prerequisites by Document

| Document | SME Input Required | Before Authoring: |
|---|---|---|
| METH-X01 | Delivery Director / PM lead | Read 2 Oracle proposals for governance sections |
| METH-X02 | Oracle EBS lead + Acumatica lead | Read Oracle proposals for data migration sections |
| METH-X03 | HCM / change management lead | Read Mauritius Telecom HCM proposal |
| METH-X04 | Any senior consultant | Read Oracle proposals for test sections |
| METH-X05 | Any senior consultant | Read Oracle proposals for cutover sections |
| METH-X06 | Delivery Director | No proposals — direct authoring |
| METH-X07 | Delivery Director | Read Oracle proposals for risk sections |
| METH-O01 | Oracle EBS lead | Read all 3 Oracle proposals — full extraction first |
| METH-O02 | Oracle EBS technical architect | No extraction needed; fresh SME session |
| METH-O03 | Oracle Cloud lead | Read Mauritius Telecom HCM proposal in full |
| METH-O04 | OCI architect | No extraction; SME session with OCI specialist |
| METH-O05 | OIC developer / architect | Limited extraction; SME session |
| METH-O06 | Service delivery manager | Read reference letter content for what services are described |
| METH-O07 | APEX developer lead | No extraction; APEX lead to drive content |
| METH-A01 | Acumatica delivery lead | Mandatory workshop before authoring |
| METH-A02 | Acumatica Manufacturing specialist | Mandatory workshop; review ATS + Maxiflex references |
| METH-A03 | Acumatica Payroll specialist | Mandatory workshop |
| METH-A04 | Acumatica delivery lead | Write METH-O06 first; then adapt |
| METH-B01 | BeBanking product owner | Mandatory SME briefing — zero source material |
| METH-B02 | BeBanking technical lead | Review Tiger/SAA DOCX files first |
| METH-B03 | BeBanking technical lead | Mandatory technical team session |
| METH-B04 | BeBanking support lead | Write METH-O06 first; then adapt |

---

## Section 6: Summary

| Category | Documents | Fully Extractable | Partial Extraction | Fresh Authoring |
|---|---|---|---|---|
| Cross-BU | 7 | 0 | 6 (from Oracle proposals) | 1 (METH-X06) |
| Oracle | 7 | 0 | 4 (METH-O01, O03 richest) | 3 (O02, O04, O07) |
| Acumatica | 4 | 0 | 0 | 4 (all from scratch) |
| BeBanking | 4 | 0 | 0 | 4 (all from scratch) |
| **Total** | **22** | **0** | **10** | **12** |

**No methodology document can be fully extracted from existing material.** The best case is 60–75% extraction (METH-O01 from Oracle EBS proposals), which still requires significant editing, generalising, and gap-filling. Twelve documents must be authored entirely from scratch and require SME input sessions before a single word is written.

**The correct sequence:**
1. Read and annotate the 3 historical Oracle proposals — extract all methodology fragments first.
2. Author Cross-BU documents (X01–X07) using extracted material as the base.
3. Author Oracle BU documents (O01, O03 first) using remaining extracted content.
4. Conduct Acumatica SME workshop — then author A01–A04.
5. Conduct BeBanking SME briefing — then author B01–B04.
6. Author remaining Oracle documents (O02, O04, O05, O06, O07) in parallel with other work.

---

*End of Methodology Library Design.*
*Next step: Human review and sign-off → create folder structure → begin Phase 1 authoring.*
