---
document_id: RISK-LIBRARY-STANDARD
title: "Risk Library Standard"
version: "1.0"
status: "Approved — WP18B"
created: "2026-06-25"
created_by: "WP18B — Methodology & Risk Library Foundation"
category: "Governance Standard"
scope: "Defines the governed structure, taxonomy, metadata standard, rating framework, and assembly rules for the APPSolve Risk Library. The Risk Library is a first-class Proposal Factory source for the Risk Register (S-50) and RAID Framework (S-37) proposal sections. This document is the authoritative standard for creating, approving, and maintaining all risk library content."
---

# Risk Library Standard

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18B — Methodology & Risk Library Foundation  
**Governs:** Risk Library — all risk register and RAID content

---

## 1. Purpose

The Risk Library enables the Proposal Factory to assemble a structured, credible Risk Register and RAID Framework for every proposal — without authoring risks from scratch for each tender.

A Risk Library entry is a pre-approved, categorised risk with a standard description, likelihood and impact rating, and mitigation approach. When the Proposal Factory assembles a proposal, it selects applicable risks from the Risk Library, adjusts them to the specific tender context, and inserts them into the Risk Register section (S-50) and RAID Framework section (S-37).

Without the Risk Library:
- Every Risk Register is authored from scratch — inconsistent, slow, unreviewable
- The Proposal Assembly Engine cannot assemble S-37 or S-50 deterministically
- Tender risk registers vary in quality between Bid Managers and tenders

With the Risk Library:
- Risk entries are pre-approved by the BU Lead and sourced from delivery experience
- The Proposal Factory selects risks by platform, engagement type, and risk category
- Human review focuses on customising mitigations, not identifying all risks
- Risk Registers are consistent, complete, and traceable

---

## 2. Risk Library Structure

### 2.1 Risk categories

The Risk Library is organised into 15 categories. Every risk entry belongs to exactly one category.

| Category Code | Category Name | Description | Typical proposal usage |
|---|---|---|---|
| RC-TECH | Technical Risk | Risks arising from the technology platform, its configuration, or platform-level events | Implementation, upgrade, and integration tenders |
| RC-COMM | Commercial Risk | Risks that affect the commercial structure, pricing accuracy, or contractual interpretation | All fixed-price tenders |
| RC-PROJ | Project Risk | Risks arising from project management, governance, or decision-making processes | All engagements |
| RC-RES | Resource Risk | Risks arising from the availability, capability, or continuity of project resources (both APPSolve and client) | All engagements |
| RC-INFRA | Infrastructure Risk | Risks arising from infrastructure environments (OCI, cloud hosting, network, hardware) | OCI and cloud tenders |
| RC-INT | Integration Risk | Risks arising from third-party system integrations, APIs, and data interfaces | Any engagement with integration in scope |
| RC-SEC | Security Risk | Risks arising from data security, access control, and compliance obligations | Any engagement with security or regulatory requirements |
| RC-DATA | Data Risk | Risks arising from data quality, completeness, migration, or governance | All implementation engagements |
| RC-MIG | Migration Risk | Risks specific to data migration execution, cutover migration, and production data load | All engagements with data migration in scope |
| RC-CUT | Cutover Risk | Risks specific to the go-live event, parallel run, and cutover execution window | All fixed-price implementation engagements |
| RC-OPS | Operational Risk | Risks arising after go-live, in steady-state operation or managed services | AMS, managed services, and support proposals |
| RC-CLIENT | Client Dependency Risk | Risks arising from the client's readiness, engagement, availability, or decisions | All engagements |
| RC-COMP | Compliance Risk | Risks arising from regulatory compliance, certification, or document validity | All proposals requiring compliance documentation |
| RC-CM | Change Management Risk | Risks arising from organisational change, user adoption, and business readiness | HCM and large ERP implementations |
| RC-3P | Third Party Risk | Risks arising from third-party vendors, bank dependencies, and partner obligations | OIC, BeBanking, and multi-vendor engagements |

### 2.2 Risk Library location

Risk library content is stored in risk register sections within methodology documents (Section 7.2 of METHODOLOGY_LIBRARY_STANDARD.md) and in the following dedicated register files:

```
08_Commercial/
├── RISK_LIBRARY_STANDARD.md          ← This document (governance)
└── Risk_Library/                     ← (target folder — to be created)
    ├── RISK_INDEX.md                  ← Master index of all approved risk entries
    ├── RC-TECH_Technical_Risks.md
    ├── RC-COMM_Commercial_Risks.md
    ├── RC-PROJ_Project_Risks.md
    ├── RC-RES_Resource_Risks.md
    ├── RC-INFRA_Infrastructure_Risks.md
    ├── RC-INT_Integration_Risks.md
    ├── RC-SEC_Security_Risks.md
    ├── RC-DATA_Data_Risks.md
    ├── RC-MIG_Migration_Risks.md
    ├── RC-CUT_Cutover_Risks.md
    ├── RC-OPS_Operational_Risks.md
    ├── RC-CLIENT_Client_Dependency_Risks.md
    ├── RC-COMP_Compliance_Risks.md
    ├── RC-CM_Change_Management_Risks.md
    └── RC-3P_Third_Party_Risks.md
```

**Note:** The `08_Commercial/Risk_Library/` directory does not yet exist. Creating this directory is an action for WP18B implementation. Until the directory is created, interim risk content may be documented as sections within methodology documents (per METHODOLOGY_LIBRARY_STANDARD.md Section 7.2).

---

## 3. Risk Entry Schema

Every risk entry in the Risk Library uses the following standard format:

### 3.1 Risk Entry template

```markdown
---
risk_id: [RC-CATEGORY-NNN]
category: [RC-TECH / RC-COMM / RC-PROJ / RC-RES / RC-INFRA / RC-INT / RC-SEC / RC-DATA / RC-MIG / RC-CUT / RC-OPS / RC-CLIENT / RC-COMP / RC-CM / RC-3P]
title: "[Short risk title — 10 words or fewer]"
platforms: [All / Oracle / Acumatica / BeBanking / list specific platforms]
engagement_types: [All / Implementation / Upgrade / AMS / Integration / all applicable types]
version: "1.0"
approved_for_reuse: Yes
approved_by: "[BU Lead name]"
approval_date: "[YYYY-MM-DD]"
source: "[Source document or evidence — KB asset, capability asset, or SME session]"
---

**Risk:** [Full risk description — what could go wrong and why it matters]

**Likelihood:** [Low / Medium / High]  
**Impact:** [Low / Medium / High]  
**Rating:** [LOW / MEDIUM / HIGH / CRITICAL] — see rating matrix Section 4

**Owner:** [APPSolve PM / BU Lead / Client / Shared]

**Standard mitigation:** [Standard mitigation approach applicable in most engagements]

**Customisation guidance:** [How to adjust the mitigation for specific tender contexts]

**Assembly trigger:** [What condition triggers this risk being included in a proposal Risk Register]

**Related assumptions:** [Assumption IDs if this risk is related to specific assumption pack assumptions]
```

### 3.2 Risk ID format

Risk IDs follow the format `RC-[CATEGORY]-[NNN]` where NNN is a sequential number within the category:

- `RC-TECH-001`, `RC-TECH-002`, etc.
- `RC-COMM-001`, `RC-COMM-002`, etc.
- First entry per category starts at 001

Risk IDs are permanent. Once assigned, a risk ID is never reused even if the entry is retired.

---

## 4. Risk Rating Framework

### 4.1 Likelihood × Impact matrix

The Risk Library uses a 3×3 Likelihood × Impact matrix:

| | **Low Impact** | **Medium Impact** | **High Impact** |
|---|---|---|---|
| **Low Likelihood** | LOW | LOW | MEDIUM |
| **Medium Likelihood** | LOW | MEDIUM | HIGH |
| **High Likelihood** | MEDIUM | HIGH | CRITICAL |

### 4.2 Rating definitions

| Likelihood | Definition |
|---|---|
| Low | Unlikely to occur in a typical engagement of this type |
| Medium | May occur; seen in some engagements of this type |
| High | Commonly occurs in engagements of this type; plan for it |

| Impact | Definition |
|---|---|
| Low | Minor disruption; recoverable within normal project tolerance |
| Medium | Significant disruption; may require change request or timeline adjustment |
| High | Material impact on project delivery, commercial outcome, or client relationship |

| Rating | Proposal treatment |
|---|---|
| LOW | Include in Risk Register; standard mitigation; no additional narrative required |
| MEDIUM | Include in Risk Register; customised mitigation recommended; BU Lead awareness |
| HIGH | Include in Risk Register prominently; specific mitigation required; flag to BU Lead |
| CRITICAL | Requires dedicated treatment in proposal Risk Register; blocking issues escalated immediately |

### 4.3 Consistency with other frameworks

| Framework | Rating scale used | Mapping |
|---|---|---|
| PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md | SEV-1 to SEV-4 | CRITICAL = SEV-1; HIGH = SEV-2; MEDIUM = SEV-3; LOW = SEV-4 |
| PROPOSAL_QA_FRAMEWORK.md | CRITICAL / HIGH / MEDIUM / LOW | Direct match |
| GOVERNANCE_RISK_REGISTER.md | HIGH / MEDIUM / LOW | Direct match to this standard |
| W3S1 capability risk registers | Informal Likelihood × Impact | Mapped at extraction time |

---

## 5. Risk Library Population — Initial Extraction

### 5.1 Source mapping

The Risk Library is not authored from scratch. Risk entries are extracted and formalised from existing KB content. The following sources provide the initial population:

| Source | Category codes | Estimated entries |
|---|---|---|
| W3S1-001 (HCM Core) Risk Register | RC-PROJ, RC-DATA, RC-INT, RC-TECH, RC-RES | 5 entries |
| W3S1-002 (Talent Mgmt) Risk Register | RC-PROJ, RC-CLIENT, RC-TECH | 5 entries |
| W3S1-003 (Recruiting Cloud) Risk Register | RC-TECH, RC-PROJ | ~5 entries |
| W3S1-004 (Learning Cloud) Risk Register | RC-TECH, RC-PROJ | ~5 entries |
| W3S1-005 (Compensation) Risk Register | RC-PROJ, RC-COMM | ~5 entries |
| W3S1-006 (Analytics) Risk Register | RC-TECH, RC-PROJ | ~5 entries |
| W3S1-007 (Workforce Mgmt) Risk Register | RC-TECH, RC-PROJ | ~5 entries |
| W3S1-008 (Help Desk) Risk Register | RC-PROJ, RC-TECH | ~5 entries |
| W3S1-009 (Payroll Interface) Risk Register | RC-INT, RC-TECH | ~5 entries |
| W1S2-007 (Acumatica Payroll) Risk Register | RC-INT, RC-COMM | 2 entries (R-W7-004, R-W7-005) |
| W2S1-005 Section 10.1 | RC-PROJ, RC-RES | ~4 entries |
| OIC_GAP_REPORT.md | RC-COMM, RC-INT | ~10 entries |
| BeBanking assumption BB-EXT-003 | RC-3P, RC-INT | 1 entry |
| OIC-CON-004 | RC-INT, RC-3P | 1 entry |
| ERP-GEN-008 | RC-PROJ, RC-CLIENT | 1 entry |
| HCM Assumption (Project Sponsor) | RC-CLIENT | 1 entry |
| SME sessions (Acumatica, BeBanking, Security) | RC-SEC, RC-TECH (Acumatica), RC-3P (BeBanking) | ~15 entries |

**Estimated initial Risk Library population: 75–90 entries across 15 categories**

### 5.2 Extraction rules

When extracting a risk from a capability asset risk register into the Risk Library:

1. **Generalise the risk description.** Remove product-specific phrasing unless the risk is genuinely platform-specific. "Oracle quarterly release introduces breaking changes" → `RC-TECH-NNN` (Oracle platform) or generalised to "SaaS platform quarterly update introduces breaking changes to configured functionality" (Cross-BU).

2. **Assign the correct category.** Use the 15-category taxonomy, not the source document's classification.

3. **Set the assembly trigger.** Every risk entry must specify what tender condition triggers its inclusion. Example: "Trigger: Oracle Cloud Fusion in BOM."

4. **Link related assumptions.** Where the risk is related to an assumption pack assumption (e.g., ERP-GEN-008 for legal entity design), record the assumption ID.

5. **Verify the mitigation is actionable.** Mitigations must describe what APPSolve does, not what the client should do.

6. **BU Lead review required.** Every extracted risk entry requires BU Lead approval before `approved_for_reuse: Yes` is set. The extraction process does not auto-approve.

---

## 6. RAID Log Standard

The Risk Library also governs the RAID Log structure used in every APPSolve project (as listed in DELIVERY_PATTERN_LIBRARY.md and PROJECT_PLAN_TEMPLATES.md).

### 6.1 RAID components

| Component | Definition | Source of content |
|---|---|---|
| **R — Risks** | Events that may occur and negatively affect delivery | Risk Library (this document) |
| **A — Assumptions** | Conditions assumed to be true for the engagement to proceed as planned | Assumption Library (13 packs) — the definitive source |
| **I — Issues** | Events that have already occurred and must be managed | Project-specific; raised by PM; tracked in issues log |
| **D — Dependencies** | External conditions or actions that the project depends on | DEP sections in assumption packs + project-specific dependencies |

**The Assumption component is fully governed by the Assumption Library.** The Risk component is governed by this Risk Library Standard. The Issues and Dependencies components are project-specific and tracked by the Project Manager.

### 6.2 RAID log template

Each APPSolve project RAID log follows this structure:

```markdown
# RAID Log — [CLIENT] [PROJECT NAME]
**Version:** [N] | **Date:** [YYYY-MM-DD] | **Owner:** Project Manager

## RISKS

| Risk ID | Risk | Likelihood | Impact | Rating | Owner | Mitigation | Status |
|---|---|---|---|---|---|---|---|
| [RL-R-NNN] | [Description] | [L/M/H] | [L/M/H] | [LOW/MED/HIGH/CRIT] | [PM/BU Lead/Client] | [Mitigation] | [Open/Monitoring/Closed] |

## ASSUMPTIONS

[Assembled from Assumption Library — refer to [TENDER_ID]_ASSUMPTION_SCHEDULE.md for full schedule]
[Summary of key assumptions only — by section: Client Responsibilities, Dependencies, Exclusions]

## ISSUES

| Issue ID | Issue | Raised Date | Owner | Action | Due Date | Status |
|---|---|---|---|---|---|---|
| [RL-I-NNN] | [Description] | [date] | [Owner] | [Action] | [date] | [Open/Resolved] |

## DEPENDENCIES

| Dep ID | Dependency | Owner | Required by | Status |
|---|---|---|---|---|
| [RL-D-NNN] | [Description] | [Client/3rd Party/APPSolve] | [date] | [Outstanding/Met] |
```

### 6.3 RAID log IDs

RAID log IDs are project-specific (not global KB IDs):
- Risks: `RL-R-001`, `RL-R-002`, etc.
- Issues: `RL-I-001`, `RL-I-002`, etc.
- Dependencies: `RL-D-001`, `RL-D-002`, etc.
- Assumptions: referenced from the Assumption Schedule (no RAID-specific ID needed)

---

## 7. Proposal Risk Register Assembly Rules

When the Proposal Factory assembles the Risk Register section (S-50) for a proposal, it follows these rules:

### 7.1 Selection criteria

| Trigger | Risks selected |
|---|---|
| Platform = Oracle Cloud | Include RC-TECH risks with platform: Oracle; include RC-INT risks with Oracle integration scope |
| Platform = Oracle EBS | Include RC-TECH risks with platform: Oracle EBS |
| Platform = Acumatica | Include RC-TECH risks with platform: Acumatica |
| Engagement type = Implementation | Include RC-PROJ, RC-DATA, RC-MIG, RC-CUT risks |
| Engagement type = AMS / Managed Services | Include RC-OPS, RC-RES risks |
| Integration in BOM | Include RC-INT risks |
| BeBanking in BOM | Include RC-3P risks with platform: BeBanking |
| Fixed-price engagement | Include RC-COMM risks |
| Large engagement (>500 users / >3 modules) | Include RC-CM risks |
| Any engagement | Include RC-CLIENT, RC-RES risks (always applicable) |

### 7.2 Minimum Risk Register requirements

Every proposal Risk Register must contain:
- Minimum 5 risks (or all applicable risks if fewer than 5 are applicable)
- At least 1 risk from each of: RC-PROJ, RC-DATA or RC-INT, RC-CLIENT
- All CRITICAL and HIGH rated risks applicable to the engagement type

### 7.3 Risk Register format in proposal

The proposal Risk Register (Section S-50) uses this standard table format:

```markdown
## Risk Register

APPSolve proactively identifies and manages project risks from the Mobilize phase. The following risks are applicable to this engagement. The full RAID log is maintained throughout the project and available to the client at all times.

| Risk ID | Risk | Likelihood | Impact | APPSolve Mitigation |
|---|---|---|---|---|
| [RC-CAT-NNN] | [Risk description — adjusted for this tender context] | [L/M/H] | [L/M/H] | [Mitigation — adjusted for this engagement] |
```

### 7.4 Governance restrictions on Risk Register content

- Risk descriptions must not quote commercial rates, margins, or pricing
- Risk descriptions must not name restricted clients (DFA, CCBA, SAA, Redpath)
- Risk descriptions must not disclose internal governance decisions or approval thresholds
- Risk descriptions must not contradict assumption pack language (e.g., do not describe a risk as managed by APPSolve when the corresponding assumption assigns client responsibility)

---

## 8. Risk Library Approval Workflow

| Stage | Who | What |
|---|---|---|
| Extract / Draft | AI (with source citation) | Extract from KB source or draft from SME session notes |
| BU Lead Review | BU Lead | Review risk description, likelihood, impact, mitigation for accuracy |
| Approve | BU Lead | Set `approved_for_reuse: Yes`; assign Risk ID |
| Index | AI | Add to RISK_INDEX.md and category file |

**Gate rule:** No risk entry may be used in a proposal Risk Register until `approved_for_reuse: Yes` is set. During the interim period before the Risk Library is populated, the Proposal Factory falls back to AI-generated risk content with mandatory BU Lead review (per PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md G-RISK remediation).

---

## 9. Risk Library Maintenance

### 9.1 Annual review

All risk entries are reviewed annually by the BU Lead (or at major platform version changes):
- Is the risk still applicable?
- Is the likelihood / impact rating still accurate?
- Is the standard mitigation still best practice?
- Has the risk materialised on a project? If so, update the description with the outcome.

### 9.2 Version control

When a risk entry is updated:
- Increment the version number in the entry
- Record the change reason in a change log field
- The old version is archived (not deleted)

### 9.3 New risk entries

New risk entries may be proposed by:
- Project Managers (from active project RAID logs)
- Bid Managers (from tender responses where new risks were identified)
- BU Leads (from delivery experience or sector knowledge)

All new entries follow the approval workflow in Section 8.

---

## 10. Integration with Proposal Factory

The Risk Library integrates with the Proposal Factory at two pipeline stages:

**Stage 9 — Gap Analysis:**
- If no Risk Library exists or applicable risks cannot be retrieved: G-RISK gap flagged (SEV-3, non-blocking)
- If Risk Library populated but specific category missing: G-RISK gap flagged with relevant category

**Stage 13 — Assemble Delivery Sections:**
- RAID Framework (S-37): RAID log structure assembled using Risk Library taxonomy + Assumption Schedule (for A component)
- Risk Register (S-50): assembled from Risk Library entries selected by BOM trigger conditions

**Source hierarchy for risk assembly:**
1. `approved_for_reuse: Yes` Risk Library entries → DIRECT EXTRACT (deterministic)
2. Risk Register sections from methodology documents (METH-X07, BU-specific) → EXTRACT
3. AI-generated risks using Risk Library taxonomy → AI-GENERATE with mandatory BU Lead review

---

## 11. Relationship to Methodology Library

The Risk Library and Methodology Library are complementary:

| Methodology Library | Risk Library |
|---|---|
| Defines HOW APPSolve delivers | Defines what COULD GO WRONG and how APPSolve manages it |
| Produces methodology sections (S-34 to S-43) | Produces risk sections (S-37 RAID, S-50 Risk Register) |
| Section structure built from delivery phases | Risk entries categorised by risk type |
| METH-X07 (Risk Management Approach) describes the process | Risk Library entries are the content of that process |

The Risk Management Approach document (METH-X07, when authored) describes the framework APPSolve uses to manage risks. The Risk Library is the content of that framework — the actual risk entries that populate the RAID log and Risk Register.

---

## 12. Current State Summary

| Item | Status |
|---|---|
| Risk Library Standard (this document) | APPROVED — WP18B |
| Risk Library folder (`08_Commercial/Risk_Library/`) | NOT YET CREATED — action item |
| RISK_INDEX.md | NOT YET CREATED — action item |
| Category files (15 files) | NOT YET CREATED — action item |
| Initial risk entry extraction | NOT YET DONE — WP18B+ work |
| BU Lead approval of extracted entries | NOT YET DONE — requires extraction first |
| Assembly Engine integration (S-37, S-50) | NOT YET BUILT — WP18C+ |

**Interim operation:** Until the Risk Library is populated and approved, the Proposal Factory inserts a G-RISK gap marker in the Risk Register section and the Bid Manager produces the Risk Register manually using this Standard as a framework (categories, rating matrix, RAID structure).

---

*RISK_LIBRARY_STANDARD.md v1.0 | WP18B — Methodology & Risk Library Foundation | 2026-06-25*  
*Governing standard for the Risk Library. 15 categories. 3×3 rating matrix. 75–90 initial entries extractable from existing KB. Feeds S-37 (RAID Framework) and S-50 (Risk Register).*
