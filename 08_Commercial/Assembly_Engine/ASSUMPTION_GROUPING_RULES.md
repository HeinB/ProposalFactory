---
document_id: ASSUMPTION-GROUPING-RULES
title: "Assumption Grouping Rules — Section Mapping and Organisation Standard"
version: "1.0"
status: "Approved"
created: "2026-06-22"
created_by: "WP17D-0 — Assumption Schedule Design Standard"
category: "Assembly Engine / Grouping Standard"
scope: "Defines how assembled assumptions are organised into client-facing sections. Provides the deterministic mapping table that the ASSUMPTION_EXTRACTOR uses to assign each assumption ID to its correct client-facing section."
---

# Assumption Grouping Rules — Section Mapping and Organisation Standard

**Version:** 1.0 | **Date:** 2026-06-22 | **Status:** Approved  
**Authority:** This is the authoritative grouping specification. The ASSUMPTION_EXTRACTOR must implement this standard in WP17D-1.  
**Companion documents:** `ASSUMPTION_SCHEDULE_STANDARD.md` | `ASSUMPTION_PUBLICATION_RULES.md`

---

## 1. Why Grouping Matters

### 1.1 Current state (WP17B/WP17C output)

The current Assembled Assumption Schedule groups assumptions **by source pack**:
- Pack 1: Oracle ERP Pack (123 assumptions)
- Pack 2: Oracle OCI Pack (174 assumptions)
- Pack 3: Oracle OIC Pack (104 assumptions)
- etc.

This grouping reflects internal Assembly Engine load order. It is not client-friendly because:
- Pack names are technical (clients do not know what "Oracle ERP Pack" means vs "Oracle OCI Pack")
- Client responsibilities are scattered across 6 packs (ERP-CUS, OIC-CUS, AMS-CUS, etc.)
- Exclusions are scattered across 6 packs (ERP-EXC, OIC-EXC, AMS-EXC, OCI-EXT, etc.)
- The SLA assumptions are split between AMS Pack and EBS SLA Overlay, confusing readers
- Section A (for an EBS AMS engagement) would show 174 infrastructure assumptions before reaching any service management content

### 1.2 Target state (WP17D output)

The WP17D client-facing schedule groups assumptions **by topic** using 8 standard sections (A through H), ordered to match how proposal evaluators read:

1. What is this engagement? (Section A — Engagement & Commercial)
2. How will it be delivered? (Section B — Project & Implementation)
3. What specific products are in scope? (Section C — Functional, per product)
4. What infrastructure is involved? (Section D — Infrastructure)
5. How is it supported post-go-live? (Section E — Service Management)
6. How is security handled? (Section F — Security & Compliance)
7. What must the client do? (Section G — Client Responsibilities)
8. What is explicitly excluded? (Section H — Explicit Exclusions)

---

## 2. The 8 Client-Facing Sections

### Section A — Engagement and Commercial Assumptions

**Purpose:** Sets the commercial context. Defines the engagement type, pricing model structure, and general commercial terms.

**Content:** General scope statements, engagement type definitions, commercial model structure, cost management assumptions from infrastructure packs.

**Client-facing heading:** `A. Engagement and Commercial Assumptions`

---

### Section B — Project and Implementation Assumptions

**Purpose:** Defines the implementation approach, methodology phases, testing scope, training model, cutover, and hypercare.

**Content:** Data migration methodology, testing approach and cycle count, training scope and delivery mode, cutover approach, hypercare period, infrastructure migration approach.

**Client-facing heading:** `B. Project and Implementation Assumptions`

---

### Section C — Application Functional Assumptions

**Purpose:** Defines what APPSolve will configure, build, and deliver for each product in scope.

**Content:** Per-product functional scope assumptions — which modules, which configurations, which processes are in scope.

**Client-facing heading:** `C. Application Functional Assumptions`

**Sub-sections (present only when the corresponding pack is loaded):**

| Sub-section | Client heading | Triggered by |
|-------------|---------------|--------------|
| C.1 | Oracle ERP (Financials and ERP) | ERP Pack |
| C.2 | Oracle HCM | HCM Base Pack (+ module packs: Recruiting, Learning, Talent, Compensation) |
| C.3 | Oracle Integration Cloud | OIC Pack |
| C.4 | Acumatica ERP | Acumatica Base Pack |
| C.5 | BeBanking | BeBanking Base Pack |

---

### Section D — Infrastructure Assumptions

**Purpose:** Defines Oracle Cloud Infrastructure scope, configuration approach, and operational model.

**Content:** OCI Landing Zone, IAM, networking, compute, storage, database, middleware, backup, disaster recovery, monitoring, operations, performance.

**Client-facing heading:** `D. Infrastructure Assumptions`

**Activation:** Present only when OCI Pack is loaded. Omit entirely if OCI not in scope.

---

### Section E — Service Management and Support Assumptions

**Purpose:** Defines the managed services operating model, SLA structure, resource model, and support processes.

**Content:** Support scope, operating hours, SLA tiers and targets, incident/service request/enhancement/change request classification and process, dedicated resource model, patching, reporting.

**Client-facing heading:** `E. Service Management and Support Assumptions`

**Activation:** Present only when AMS Pack is loaded. Omit entirely if managed services not in scope.

**Note on overlays:** EBS SLA Overlay and EBS DRM Overlay assumptions are placed in Section E alongside the active AMS Pack assumptions. The distinction between packs is invisible in the client document. Suppressed AMS assumptions (replaced by overlay equivalents) are absent.

---

### Section F — Security and Compliance Assumptions

**Purpose:** Defines security approach, data handling, compliance obligations, and regulatory posture.

**Content:** Role-based access control model, POPIA obligations, data residency, audit trail, encryption, identity management, penetration testing scope.

**Client-facing heading:** `F. Security and Compliance Assumptions`

---

### Section G — Client Responsibilities

**Purpose:** Defines what the client must provide, decide, and execute. Creates enforceable obligations.

**Content:** All customer responsibility assumptions from all loaded packs (CUS, CON, DEP sections). Consolidated from all sources into a single section.

**Client-facing heading:** `G. Client Responsibilities`

**Critical rule:** Client responsibilities from ALL packs are pulled out of their source sections and consolidated here. A client responsibility from the OIC pack does NOT appear in Section C.3 — it appears only in Section G.

---

### Section H — Explicit Exclusions

**Purpose:** Names items that are explicitly NOT included in scope. Provides the primary defence against scope creep claims.

**Content:** All exclusion assumptions from all loaded packs (EXC, EXT sections). Consolidated from all sources into a single section.

**Client-facing heading:** `H. Explicit Exclusions`

**Critical rule:** Exclusions from ALL packs are pulled out of their source sections and consolidated here. An exclusion from the ERP pack does NOT appear in Section C.1 — it appears only in Section H.

---

## 3. Deterministic Mapping Rules

The following rules determine which section each assumption is assigned to. Rules are evaluated in priority order — the first matching rule wins.

### 3.1 Universal rules (apply regardless of source pack)

| Priority | Match condition | Assigned section |
|----------|----------------|-----------------|
| **P1 — Highest** | Section code = `CUS`, `CON`, or `DEP` | **G — Client Responsibilities** |
| **P2** | Section code = `EXC` or `EXT` | **H — Explicit Exclusions** |
| **P3** | Section code = `GEN` | **A — Engagement and Commercial** |
| **P4** | Section code = `SEC` | **F — Security and Compliance** |

### 3.2 Pack-specific rules (apply after P1–P4 match fails)

| Priority | Pack | Section codes | Assigned section |
|----------|------|--------------|-----------------|
| **P5** | OCI | `CST` | A — Engagement and Commercial |
| **P6** | OCI | `SUP` | E — Service Management |
| **P7** | OCI | All remaining | D — Infrastructure |
| **P8** | AMS | All remaining | E — Service Management |
| **P9** | EBS-SLA | All | E — Service Management |
| **P10** | EBS-DRM | All | E — Service Management |
| **P11** | ERP | `DAT`, `TST`, `TRN`, `CUT`, `HYP`, `INT` | B — Project and Implementation |
| **P12** | ERP | All remaining | C.1 — Oracle ERP |
| **P13** | HCM | `TST`, `TRN`, `CUT` | B — Project and Implementation |
| **P14** | HCM | All remaining | C.2 — Oracle HCM |
| **P15** | REC, LRN, TLT, COM | `TST`, `TRN`, `CUT` | B — Project and Implementation |
| **P16** | REC | All remaining | C.2 — Oracle HCM (sub-section: Recruiting) |
| **P17** | LRN | All remaining | C.2 — Oracle HCM (sub-section: Learning) |
| **P18** | TLT | All remaining | C.2 — Oracle HCM (sub-section: Talent Management) |
| **P19** | COM | All remaining | C.2 — Oracle HCM (sub-section: Workforce Compensation) |
| **P20** | OIC | `TST`, `CUT` | B — Project and Implementation |
| **P21** | OIC | All remaining | C.3 — Oracle Integration Cloud |
| **P22** | ACU | All remaining | C.4 — Acumatica ERP |
| **P23** | BB | All remaining | C.5 — BeBanking |

### 3.3 Mapping logic (algorithmic specification for WP17D-1)

```
function assignSection(assumptionID):
  pack = extractPackPrefix(assumptionID)        # e.g., "ERP", "OCI", "AMS", "HCM", "REC"
  sectionCode = extractSectionCode(assumptionID) # e.g., "GEN", "GL", "CUS", "EXC"

  # P1 — Universal: Client Responsibilities
  if sectionCode IN ["CUS", "CON", "DEP"]:
    return "G"

  # P2 — Universal: Explicit Exclusions
  if sectionCode IN ["EXC", "EXT"]:
    return "H"

  # P3 — Universal: General → Engagement & Commercial
  if sectionCode = "GEN":
    return "A"

  # P4 — Universal: Security → Security & Compliance
  if sectionCode = "SEC":
    return "F"

  # P5 — OCI Cost Management → Engagement & Commercial
  if pack = "OCI" AND sectionCode = "CST":
    return "A"

  # P6 — OCI Support → Service Management
  if pack = "OCI" AND sectionCode = "SUP":
    return "E"

  # P7 — OCI remainder → Infrastructure
  if pack = "OCI":
    return "D"

  # P8 — AMS remainder → Service Management
  if pack = "AMS":
    return "E"

  # P9/P10 — EBS Overlays → Service Management
  if pack IN ["EBS-SLA", "EBS-DRM"]:
    return "E"

  # P11 — ERP delivery sections → Project & Implementation
  if pack = "ERP" AND sectionCode IN ["DAT", "TST", "TRN", "CUT", "HYP", "INT"]:
    return "B"

  # P12 — ERP remainder → Oracle ERP functional
  if pack = "ERP":
    return "C.1"

  # P13 — HCM delivery sections → Project & Implementation
  if pack = "HCM" AND sectionCode IN ["TST", "TRN", "CUT"]:
    return "B"

  # P14 — HCM remainder → Oracle HCM functional
  if pack = "HCM":
    return "C.2"

  # P15 — HCM module delivery sections → Project & Implementation
  if pack IN ["REC", "LRN", "TLT", "COM"] AND sectionCode IN ["TST", "TRN", "CUT"]:
    return "B"

  # P16-P19 — HCM modules → Oracle HCM functional (sub-sectioned by module)
  if pack = "REC": return "C.2-REC"
  if pack = "LRN": return "C.2-LRN"
  if pack = "TLT": return "C.2-TLT"
  if pack = "COM": return "C.2-COM"

  # P20 — OIC delivery sections → Project & Implementation
  if pack = "OIC" AND sectionCode IN ["TST", "CUT"]:
    return "B"

  # P21 — OIC remainder → Oracle Integration Cloud functional
  if pack = "OIC":
    return "C.3"

  # P22 — Acumatica → Acumatica ERP functional
  if pack = "ACU":
    return "C.4"

  # P23 — BeBanking → BeBanking functional
  if pack = "BB":
    return "C.5"

  # Fallback — should not occur if all packs are handled above
  return "UNCLASSIFIED"
```

---

## 4. Section Ordering Within Each Section

Within each client-facing section, assumptions are ordered as follows:

### 4.1 Section A (Engagement & Commercial)

Order: GEN assumptions from each loaded pack, in pack load order (ERP → OCI → OIC → AMS → HCM → ACU → BB). OCI-CST assumptions follow OCI-GEN assumptions.

### 4.2 Section B (Project & Implementation)

Order: By delivery phase:
1. Planning and design assumptions (INT where applicable)
2. Data migration (DAT, MIG)
3. Testing (TST)
4. Training (TRN)
5. Cutover (CUT)
6. Hypercare (HYP)

Within each phase, ERP assumptions before HCM before OIC.

### 4.3 Section C — Sub-sections

Sub-sections are presented in this order when applicable:

1. C.1 — Oracle ERP
2. C.2 — Oracle HCM (Base → Recruiting → Learning → Talent → Compensation)
3. C.3 — Oracle Integration Cloud
4. C.4 — Acumatica ERP
5. C.5 — BeBanking

Within each sub-section, assumptions are presented in source pack section order (GL before AP before AR, etc.) to maintain the structured flow familiar to functional reviewers.

### 4.4 Section D (Infrastructure)

Order: OCI Pack natural section order: LZ → IAM → NET → SEC (if any — but SEC goes to F) → CMP → STO → DB → MW → INT → BKP → DR → MON → OPS → MIG → PER.

### 4.5 Section E (Service Management)

Order:
1. AMS scope and hours (SCP, HRS)
2. Support channels (CHN)
3. Incident management (INC)
4. Service requests (SRQ)
5. Enhancements (ENH)
6. Change requests (CR)
7. Defect management (DEF)
8. SLA and priority classification — EBS-SLA-* assumptions (when loaded) replace AMS-SLA and AMS-PRI; EBS-SLA assumptions appear in this position
9. Dedicated Resource Model (EBS-DRM-* assumptions, when loaded)
10. Release and patching (REL, PAT)
11. Monitoring and reporting (MON, REP)
12. OCI Support assumptions (OCI-SUP)
13. OIC Support assumptions (OIC-SUP)

### 4.6 Section F (Security & Compliance)

Order: ERP-SEC → OCI-SEC → OIC-SEC → HCM-SEC → AMS-SEC → ACU-SEC → BB-SEC (present only if applicable). Governance assumptions follow security assumptions.

### 4.7 Section G (Client Responsibilities)

Order: By source pack in load order. All ERP-CUS before OCI-CUS before OIC-CUS, etc.

**Sub-headings within Section G are optional.** If the engagement spans multiple products, sub-headings by product area improve readability:
- G.1 — ERP Client Responsibilities
- G.2 — HCM Client Responsibilities
- G.3 — OIC Client Responsibilities (including OIC-DEP and OIC-CON)
- G.4 — Infrastructure (OCI) Client Responsibilities
- G.5 — Managed Services Client Responsibilities
- G.6 — Acumatica Client Responsibilities
- G.7 — BeBanking Client Responsibilities

For single-product engagements, sub-headings are not required.

### 4.8 Section H (Explicit Exclusions)

Order: By source pack in load order. All ERP-EXC before OCI-EXT before OIC-EXC before AMS-EXC, etc.

**No sub-headings required.** Exclusions are listed as a flat numbered list. The source is implied by the Ref ID.

---

## 5. Grouping for Known Assembly Patterns

### 5.1 EBS AMS Full Stack (T1 — ARM IT045 type)

| Section | Sources | Count (ARM IT045) |
|---------|---------|------------------|
| A — Engagement & Commercial | ERP-GEN, OCI-GEN, OIC-GEN, AMS-GEN, OCI-CST | ~24 |
| B — Project & Implementation | ERP-DAT, ERP-TST, ERP-TRN, ERP-CUT, ERP-HYP, ERP-INT, OCI-MIG, OIC-TST, OIC-CUT | ~30 |
| C.1 — Oracle ERP | ERP functional sections (GL, AP, AR, FA, CM, PRO, PPM, REP, WFL) | ~68 |
| C.3 — Oracle Integration | OIC functional sections (SCP, DES, END, MAP, CERT, PERF, MON, DEP\*) | ~55 |
| D — Infrastructure | OCI pack (LZ, IAM, NET, CMP, STO, DB, MW, INT, BKP, DR, MON, OPS, PER, SUP\*) | ~152 |
| E — Service Management | AMS active + EBS-SLA-* + EBS-DRM-* (OCI-SUP, OIC-SUP) | ~175 |
| F — Security & Compliance | ERP-SEC, OCI-SEC, OIC-SEC | ~22 |
| G — Client Responsibilities | ERP-CUS, OIC-CUS, OIC-CON, OIC-DEP, AMS-CUS | ~40 |
| H — Explicit Exclusions | ERP-EXC, OCI-EXT, OIC-EXC, AMS-EXC | ~39 |

*OIC-DEP and OIC-CON → Group G (Client Responsibilities) by rule P1*
*OCI-SUP → Group E (Service Management) by rule P6*

**Total: 594 net assumptions (after 6 suppressions)**

### 5.2 HCM Full Suite (T2)

| Section | Sources | Count |
|---------|---------|-------|
| A — Engagement & Commercial | HCM-GEN | ~5 |
| B — Project & Implementation | HCM-TST, HCM-TRN, HCM-CUT + module equivalents | ~20 |
| C.2 — Oracle HCM | HCM functional sections + REC + LRN + TLT + COM | ~210 |
| F — Security & Compliance | HCM-SEC + module SEC sections | ~8 |
| G — Client Responsibilities | All -CUS sections across 5 packs | ~17 |
| H — Explicit Exclusions | All -EXC sections across 5 packs | ~41 |

**Total: 267 net assumptions (0 suppressions)**

### 5.3 OIC Standalone (T3)

| Section | Sources | Count |
|---------|---------|-------|
| A — Engagement & Commercial | OIC-GEN | ~3 |
| B — Project & Implementation | OIC-TST, OIC-CUT | ~10 |
| C.3 — Oracle Integration | OIC functional (SCP, DES, END, CERT, MAP, PERF, MON, SUP) | ~50 |
| F — Security & Compliance | OIC-SEC | ~6 |
| G — Client Responsibilities | OIC-CUS, OIC-DEP, OIC-CON | ~24 |
| H — Explicit Exclusions | OIC-EXC | ~15 |

**Total: 104 net assumptions**

### 5.4 BeBanking + OIC + AMS (T4)

| Section | Sources | Count |
|---------|---------|-------|
| A — Engagement & Commercial | BB-GEN, OIC-GEN, AMS-GEN | ~10 |
| B — Project & Implementation | OIC-TST, OIC-CUT | ~10 |
| C.3 — Oracle Integration | OIC functional | ~45 |
| C.5 — BeBanking | BB functional sections | ~80 |
| E — Service Management | AMS active | ~70 |
| F — Security & Compliance | BB-SEC, OIC-SEC, AMS-SEC | ~15 |
| G — Client Responsibilities | BB-CUS, OIC-CUS, OIC-DEP, OIC-CON, AMS-CUS | ~45 |
| H — Explicit Exclusions | BB-EXC, OIC-EXC, AMS-EXC | ~30 |

**Total: 305 net assumptions**

### 5.5 Acumatica Standalone (T5)

| Section | Sources | Count |
|---------|---------|-------|
| A — Engagement & Commercial | ACU-GEN | ~8 |
| B — Project & Implementation | ACU delivery sections | ~20 |
| C.4 — Acumatica ERP | ACU functional (FIN, DIS, MAN, CRM, PRJ, PAY, INT, etc.) | ~90 |
| F — Security & Compliance | ACU-SEC | ~8 |
| G — Client Responsibilities | ACU-CUS | ~14 |
| H — Explicit Exclusions | ACU-EXC | ~12 |

**Total: 152 net assumptions**

*Note: Exact section counts in patterns 5.2–5.5 are indicative. The authoritative counts are produced by WP17D-1 after full text extraction from source packs. The mapping rules in Section 3 are definitive — section counts are derived, not fixed.*

---

## 6. Section Count Tolerance

When WP17D-1 assembles the document, the total of all section counts must equal the net assumption count from the Assembly Audit Report:

```
sum(A + B + C.1 + C.2 + C.3 + C.4 + C.5 + D + E + F + G + H) = net_assumption_count
```

If the total does not match, the ASSUMPTION_EXTRACTOR has either:
- Classified an assumption into multiple sections (error)
- Omitted an assumption (error)
- Included a suppressed assumption (error)

The WP17D-1 implementation must include this count balance check as a mandatory pre-output validation step.

---

## 7. Implementation Notes for WP17D-1

### 7.1 Parsing assumption IDs

To extract the pack prefix and section code from an assumption ID:

- Format: `[PACK]-[SECTION]-[NNN]`
- Example: `ERP-GL-001` → pack = `ERP`, section = `GL`, number = `001`
- Example: `EBS-SLA-001` → pack = `EBS-SLA`, section (is the full middle part)
- Example: `EBS-DRM-001` → pack = `EBS-DRM`
- Example: `HCM-CUS-001` → pack = `HCM`, section = `CUS`

For EBS overlay packs, the pack identifier includes the hyphen: `EBS-SLA` and `EBS-DRM`. The ASSUMPTION_EXTRACTOR must recognise these as distinct packs, not as EBS pack with section "SLA" or "DRM".

### 7.2 Reading full assumption text

For each assembled assumption ID, the ASSUMPTION_EXTRACTOR must:
1. Know which source pack file the ID belongs to
2. Read the full assumption text entry from that file
3. The text entry format in source packs is: `**[ID]** — [Full assumption text]`
4. Extract the text after the ` — ` separator

This requires reading each source pack file during assembly. The PACK_LOADER registry confirms the file path per pack.

### 7.3 Verification required before WP17D-1 implementation

The mapping rules in Section 3 are based on known pack section codes. The following should be verified against the actual pack files before WP17D-1 implementation:

| Pack | Verify |
|------|--------|
| HCM Base | Confirm all section code two-letter abbreviations (ENV, ORG, PER, EMP, etc.) |
| HCM Recruiting | Confirm section codes (SIT, REQ, BOO, etc.) |
| HCM Learning | Confirm section codes |
| HCM Talent | Confirm section codes |
| HCM Compensation | Confirm section codes |
| ACU Base | Confirm section codes (FIN, DIS, MAN, CRM, PRJ, PAY, GOV, etc.) |
| BeBanking Base | Confirm section codes (H2H, PAY, ACC, REC, etc.) |

The ERP, OCI, OIC, AMS, EBS-SLA, and EBS-DRM section codes are confirmed from WP17B dry-run validation.

---

*ASSUMPTION_GROUPING_RULES.md v1.0 | WP17D-0 Design Standard | 2026-06-22*  
*Approved for WP17D-1 implementation. This document is the authoritative section mapping specification.*
