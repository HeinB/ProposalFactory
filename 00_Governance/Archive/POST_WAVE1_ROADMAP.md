---
created: "2026-06-10"
created_by: "Claude (AI — consolidation planning)"
status: "Active"
---

# Post-Wave 1 Roadmap
**Date:** 2026-06-10 | **Owner:** Hein Blignaut | **Status:** Wave 1 complete — entering Oracle gap closure phase

---

## Context

Wave 1 is complete. 25 files are approved across Cross-BU, BeBanking, and Acumatica. The repository is operational for BeBanking and Acumatica tenders. **Oracle capability content has not yet been extracted.** An Oracle tender response today would have a partnership statement, awards table, company overview, and delivery model — but no product capability statements and no methodology documents. This is the primary gap.

The work below addresses that gap plus the remaining consolidation actions.

---

## Immediate Actions (Before Any Wave 2 Extraction)

These do not require new content and should be completed first.

| Action | Effort | Urgency | Notes |
|---|---|---|---|
| **BEE certificate renewal** | External — initiate with accredited agency | **CRITICAL** — deadline 2026-07-31 (~51 days) | Cannot cite BEE in tenders after expiry |
| **Copy 25 approved files to KB destinations** | 30–45 min | High — completes pipeline | See `APPROVED_CONTENT_PLACEMENT_PLAN.md` |
| **BU lead Q&A — W1S2-006 and W1S2-007** | 10-min conversation | Medium — unblocks Acumatica candidates | See `WAVE2_CANDIDATE_DECISIONS.md` |

---

## Content Priority Ranking

### 1. Oracle Fusion Capability Statement

**Source:** TMPL-001 — `Parties/Customers/0. Proposal Templates/Oracle Fusion/Oracle Fusion Template.docx`
**Section to extract:** "Oracle Fusion Information" — the Fusion-specific product capability section

**Estimated effort:** 1–1.5 hours
- Read and assess Oracle Fusion Information section (~30 min)
- Extract and structure into BU-lead-reviewed KB format (~30 min)
- Self-review and promote to Review_Required (~15 min)
- BU lead review and approval (separate session or quick review)

**Source availability:** Confirmed. Template exists at the path above. It was used as a source for W1S1-001 to W1S1-003, so the file is accessible and readable.

**Business value:** CRITICAL
The most significant content gap in the repository. Without a Fusion capability statement, any Oracle Cloud tender response must be improvised from general company profile content. A confirmed, approved Fusion capability statement unlocks APPSolve's ability to respond to Oracle Cloud tenders with specific, citeable content for: Financial Management, HCM, SCM, CRM, Procurement, Oracle Integration Cloud, and Cloud infrastructure.

**Tender impact:** HIGH — Oracle Cloud (Fusion) is a common RFP category. Competitors will have detailed product capability matrices; APPSolve without this document is at a structural disadvantage.

**Recommended sequence:** Extract first among Wave 2 items.

**Coverage target:** `06_Capabilities/Oracle/Oracle_ERP/`

---

### 2. Oracle EBS Capability Overview

**Source:** TMPL-002 — `Parties/Customers/0. Proposal Templates/Oracle EBS Template.docx`
**Section to extract:** "Oracle EBS Information" — the EBS-specific product capability section

**Estimated effort:** 45 min–1 hour
- Read and assess Oracle EBS Information section (~20 min)
- Extract and structure (~20 min)
- Self-review, promote to Review_Required (~10 min)

**Source availability:** Confirmed. Oracle EBS Template exists at the Proposal Templates path. Note: exact filename not confirmed — verify at `Parties/Customers/0. Proposal Templates/Oracle Fusion/` or similar path.

**Business value:** HIGH
Oracle EBS (R11/R12) remains a significant part of APPSolve's delivery portfolio. Many South African organisations still run EBS and are upgrading or maintaining. A capability overview enables responses to EBS implementation, upgrade, and migration tenders.

**Tender impact:** HIGH for EBS-specific tenders. Moderate for cloud migration tenders (where EBS experience is cited as context for cloud migration capability).

**Recommended sequence:** Extract immediately after Oracle Fusion (Priority 1).

**Coverage target:** `06_Capabilities/Oracle/Oracle_EBS/`

---

### 3. Oracle DBA Executive Summary

**Source:** HIST-002 — `Parties/Customers/MTN/RFP/[year]/APPSolve Tender - Volume 2/APPSolve Executive Summary.docx`
**Section to extract:** Full executive summary document — won engagement

**Estimated effort:** 30–45 min
- Read and assess executive summary (~15 min)
- Extract and modernise (update company stats, partner tier, years in business) (~20 min)
- Self-review, promote to Review_Required (~10 min)

**Source availability:** Confirmed. HIST-002 is registered in DOCUMENT_REGISTER.csv. The MTN 2014 engagement was won. Executive summary from a won engagement is high-value source material.

**Business value:** HIGH
APPSolve has one of the largest locally based Oracle Applications DBA teams in South Africa. This claim is validated and approved but has no supporting narrative document. A standalone Oracle DBA executive summary enables DBA managed services proposals to be built around a compelling, pre-approved positioning document.

**Tender impact:** DIRECT for Oracle DBA/managed services tenders. Useful as supporting evidence in any Oracle tender where DBA capability is evaluated.

**Recommended sequence:** Third extraction after Priority 1 and 2.

**Coverage target:** `02_Corporate/Executive_Summaries/` (new folder — create before copying) or `05_Methodologies/Managed_Services/`

---

### 4. BeBanking Implementation Methodology

**Source:** HIST-004 — `Parties/Customers/Mpact/RFP/2019/` (Mpact BeBanking implementation proposal)
**Section to extract:** Implementation methodology / delivery phases section

**Estimated effort:** 1–1.5 hours
- Read and assess methodology sections (~30 min)
- Extract phases, workstreams, and timelines; modernise to current product version (~30–45 min)
- Self-review, promote to Review_Required (~15 min)

**Source availability:** Confirmed. HIST-004 is registered as the most complete BeBanking methodology document in the corpus. Mpact 2019 is a high-fidelity real engagement.

**Business value:** HIGH
BeBanking tenders often require a project implementation plan or methodology section. Without this, the BeBanking response relies on the generic Delivery Model (W1S1-007). A BeBanking-specific methodology with phases (discovery, configuration, bank testing, UAT, go-live) and timelines is a significant differentiator.

**Tender impact:** HIGH for BeBanking implementation tenders. Moderate for H2H integration assessments.

**Recommended sequence:** Extract in parallel with or after Priority 3. Can be done independently of Oracle work.

**Coverage target:** `05_Methodologies/Implementation/` (within a BeBanking sub-path if available, or at implementation level)

---

### 5. Reference Letter Programme

**This is not an extraction task — it is a client outreach activity.**

**Current state:** Zero signed Oracle reference letters in the KB. One Acumatica reference letter (ATS — signed). Nine Acumatica reference letter templates are unsigned. BeBanking reference letters: unknown status.

**Estimated effort:** Per letter — one email or call per client contact; actual letter return depends on client responsiveness (days to weeks)

**Source availability:** `04_References/Oracle/` — empty. `04_References/Acumatica/` — 1 signed. Templates in Tender Pack.

**Business value:** VERY HIGH for tenders that require client references
Most competitive tenders require at least two or three verifiable client references. Without signed letters, APPSolve can only offer names — not verification. This is a material weakness in any evaluated tender.

**Tender impact:** Can cause disqualification in formal RFPs that require submitted reference letters with original signatures or contact names.

**Priority targets:**
- Oracle: ATC, Old Mutual, Truworths — contact BU lead to initiate
- Acumatica: 9 unsigned templates outstanding — identify contact person at each client
- BeBanking: Confirm status with BeBanking BU lead

**Recommended approach:** Raise with BU leads as a separate work item. Does not require an AI session — requires human client outreach. Assign a deadline tied to the next expected tender submission.

---

## Recommended Wave 2 Sequence

| Step | Activity | Type | Effort | Start |
|---|---|---|---|---|
| 0a | BEE certificate renewal — initiate | External | — | **Now** |
| 0b | Copy 25 files to KB destinations | Admin | 45 min | Next session |
| 0c | BU lead Q&A (W1S2-006, 007) | Conversation | 10 min | Anytime |
| 1 | Oracle Fusion Capability Statement (TMPL-001) | Extraction | 1.5 hr | Session after 0b |
| 2 | Oracle EBS Capability Overview (TMPL-002) | Extraction | 1 hr | Same session as #1 |
| 3 | Oracle DBA Executive Summary (HIST-002) | Extraction | 45 min | Same session or next |
| 4 | BeBanking Implementation Methodology (HIST-004) | Extraction | 1.5 hr | Parallel with or after #3 |
| 5 | Reference letter chase — Oracle (ATC, Old Mutual, Truworths) | Outreach | Variable | Initiate now; external |
| 6 | W1S2-006/007 authoring (if BU lead confirms) | Authoring | 1–2 hr each | After step 0c decision |

Total estimated AI session time for steps 1–4: approximately 4–5 hours across two sessions.

---

## Wave 3 Preview (Not Yet Planned)

Items that will be valuable after Wave 2 is complete:

| Item | Source | Notes |
|---|---|---|
| Oracle DBA Technical Solution | HIST-002 MTN 2014 Section 2.1 | Detailed DBA methodology — deeper than the exec summary |
| BeBanking Delivery Phases | HIST-004 Mpact 2019 | Sub-section of methodology — delivery phase detail |
| BeBanking Support Model | HIST-003 SITA Exec Summary | Support model sub-sections |
| Oracle Cloud methodology | Historical corpus Oracle Cloud tenders | Search for post-2020 Oracle Cloud won engagements |
| Acumatica implementation methodology | Historical corpus Acumatica tenders | HIST-005 + any other Acumatica won proposals |
| Standard RFP responses | Across corpus | Common questions: BEE, company registration, insurance, pricing model |
| Case studies | Across corpus | Oracle: MTN, Transnet. Acumatica: HyDac. BeBanking: Mpact, SITA |
| CONTENT_GAP_ANALYSIS.md revision | — | Revise post-Wave 3 when more gaps are closed |

---

*Prepared 2026-06-10 by Claude (AI) on instruction from Hein Blignaut.*
