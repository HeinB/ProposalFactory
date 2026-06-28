---
document_id: ARM-IT045-FACTORY-GAP-REGISTER
title: "ARM IT045 — Factory Gap Register"
tender_id: "ARM IT045"
version: "1.0"
status: "WP18C Stage 7 Output"
created: "2026-06-25"
created_by: "WP18C — Proposal Factory Assembly Engine v1.0"
total_gaps: 14
sev1_blocking: 5
sev2_significant: 5
sev3_advisory: 4
sev4_enhancement: 0
---

# ARM IT045 — Factory Gap Register

**Stage 7 Output:** Gap analysis per PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md  
**Tender:** ARM IT045 | African Rainbow Minerals | Oracle EBS AMS  
**Gap detection date:** 2026-06-25  
**Total gaps:** 14  
**SEV-1 (Blocking):** 5 | **SEV-2 (Significant):** 5 | **SEV-3 (Advisory):** 4

---

## 1. Gap Summary

| Severity | Label | Count | Description |
|---|---|---|---|
| SEV-1 | BLOCKING | 5 | Factory cannot produce submission-ready output without resolution |
| SEV-2 | SIGNIFICANT | 5 | Output produced but content is AI-generated or incomplete; human review mandatory |
| SEV-3 | ADVISORY | 4 | Factory produces acceptable output; KB enrichment would improve quality |
| SEV-4 | ENHANCEMENT | 0 | Quality improvements only; no impact on submission readiness |
| **TOTAL** | | **14** | |

---

## 2. SEV-1 — Blocking Gaps

These gaps prevent the Factory from producing submission-ready content. They must be resolved before ARM IT045 (or any similar future tender) can be submitted.

---

### GAP-001 — People: Named Consultant Team Not Assembled

| Field | Value |
|---|---|
| **Gap ID** | GAP-001 |
| **Category** | G-CV (Consultant and CV) |
| **Severity** | SEV-1 — BLOCKING |
| **Sections Affected** | S-46 (Team Structure), S-47 (CVs), A-02 (CV Appendix) |
| **Description** | The AMS team structure requires named, dedicated consultants across 7 role positions. The Factory cannot select or name consultants — ADR-001 permanently requires CVs to be obtained from APPTime and named by the BU Lead. The People section is entirely empty. |
| **Root Cause** | Permanent governance constraint (ADR-001). BU Lead assignment is always required. |
| **Resolution** | BU Lead to: (1) confirm 7 named resources for ARM IT045 AMS team; (2) obtain CVs from APPTime for each. |
| **Resolution Owner** | BU Lead |
| **Resolution Effort** | 4–8 hours |
| **Factory Remediation** | N/A — permanent constraint. CONSULTANT_INDEX can accelerate role matching; CVs always APPTime. |
| **Recurrence** | Will apply to every tender. Not eliminatable by Factory improvements. |

---

### GAP-002 — Commercial: Pricing Section Empty

| Field | Value |
|---|---|
| **Gap ID** | GAP-002 |
| **Category** | G-COMM (Commercial) |
| **Severity** | SEV-1 — BLOCKING |
| **Sections Affected** | S-52 (Commercials / Pricing) |
| **Description** | The commercial pricing section is a PLACEHOLDER. The Factory does not have access to commercial rate structures, margin targets, or pricing models. The proposal cannot be submitted without a commercial offer. |
| **Root Cause** | Permanent governance constraint. Commercial data is not stored in the KB. No commercial rates in any KB file. This is by design — Commercial Director authority. |
| **Resolution** | Commercial Director to author the commercial section and pricing structure for ARM IT045. |
| **Resolution Owner** | Commercial Director |
| **Resolution Effort** | 2–4 hours |
| **Factory Remediation** | N/A — permanent constraint. A pricing section template (format only, no rates) could reduce effort from 4h to 2h if WP19 includes a commercial template. |
| **Recurrence** | Will apply to every tender. Not eliminatable. |

---

### GAP-003 — References: Unconfirmed + Letters Outstanding

| Field | Value |
|---|---|
| **Gap ID** | GAP-003 |
| **Category** | G-REF (Reference) |
| **Severity** | SEV-1 — BLOCKING |
| **Sections Affected** | S-67 (Client References), A-03 (Reference Letters) |
| **Description** | Four references selected (REF-ORA-008/-004/-005/-009). All 4 require AM approval before inclusion. Reference contact details are not in the draft. Signed reference letters are not confirmed as available in the KB directory. |
| **Root Cause** | AM approval workflow not automated. Reference letter status not tracked in KB. |
| **Resolution** | Account Manager to: (1) confirm approval for all 4 references; (2) insert reference contact details; (3) confirm signed letters available or obtain new letters. |
| **Resolution Owner** | Account Manager |
| **Resolution Effort** | 2–4 hours (approval) + variable (letter procurement — may require client contact) |
| **Factory Remediation** | Medium-term: AM approval workflow as part of Reference Selector (WP18B-EXT or WP19). Near-term: structured AM approval checklist in Reference Section template. |
| **Recurrence** | Will apply to every tender. Reference letters require fresh confirmation per tender. |

---

### GAP-004 — OCI Capability Narrative Missing

| Field | Value |
|---|---|
| **Gap ID** | GAP-004 |
| **Category** | G-CAP (Capability) |
| **Severity** | SEV-1 — BLOCKING (for OCI-scope tenders) |
| **Sections Affected** | S-22 (OCI Infrastructure) |
| **Description** | There is no standalone OCI capability narrative asset in the Capability Library. S-22 (OCI Infrastructure) is currently assembled from OCI assumption pack proxy content (AI-generated). This is adequate as a draft but not a governed, approved capability statement. For a tender like ARM IT045 where OCI is a core service component, this is a significant gap. |
| **Root Cause** | OCI capability narrative was not created as part of WP1–WP9 (Capability Library work packages). The OCI coverage in assumption packs covers scope/exclusions/dependencies but not a narrative capability statement. |
| **Resolution** | Author a standalone OCI capability narrative asset (similar to W2S1-002, W2S1-003, W2S1-004). Submit as WP18B-METH4 or as a separate quick-win work package. |
| **Resolution Owner** | BU Lead (Oracle Practice) |
| **Resolution Effort** | 4–8 hours (one writing session + BU review) |
| **Factory Remediation** | Once the OCI capability asset is approved and loaded into the Capability Library, S-22 changes from AI-GENERATE (L1) to DIRECT (L3). |
| **Recurrence** | Will affect all OCI-scope tenders until resolved. |

---

### GAP-005 — Mining Charter Compliance Coverage Absent

| Field | Value |
|---|---|
| **Gap ID** | GAP-005 |
| **Category** | G-COMP (Compliance) |
| **Severity** | SEV-1 — BLOCKING (for mining sector tenders with charter requirement) |
| **Sections Affected** | S-55 (Compliance Schedule) — conditional |
| **Description** | ARM IT045 is a JSE-listed mining group. Mining sector RFPs often require explicit Mining Charter compliance statements or social and labour plan (SLP) acknowledgement. No assumption pack covers Mining Charter and no compliance template addresses it. If ARM's RFP requires a Mining Charter compliance statement, the Factory has no source. |
| **Root Cause** | Mining Charter is sector-specific and not covered in any assumption pack or compliance template. |
| **Resolution** | BU Lead + AM to assess whether ARM IT045 RFP explicitly requires Mining Charter compliance. If required, author the response section. If not required for ARM IT045, create the Mining Charter compliance template for future mining sector tenders. |
| **Resolution Owner** | BU Lead |
| **Resolution Effort** | 2 hours (RFP assessment) + 4 hours (template if required) |
| **Factory Remediation** | Author a Mining Charter compliance statement template and add to the Compliance Library. Flag as required whenever tender is mining sector. |
| **Recurrence** | Will affect all mining sector tenders. |

---

## 3. SEV-2 — Significant Gaps

These gaps produce draft content but the content is AI-generated or requires significant human review before submission.

---

### GAP-006 — Risk Register: Risk Library Empty

| Field | Value |
|---|---|
| **Gap ID** | GAP-006 |
| **Category** | G-RISK (Risk) |
| **Severity** | SEV-2 — SIGNIFICANT |
| **Sections Affected** | S-50 (Risk Register), S-37 (RAID Framework) |
| **Description** | The Risk Library Standard was approved in WP18B (RISK_LIBRARY_STANDARD.md). However, no approved risk register entries exist in the Risk Library. The ARM IT045 Risk Register (S-50) was AI-generated (9 risks). These risks are plausible and well-structured but are not sourced from approved KB content. They must be reviewed and approved by BU Lead before submission. |
| **Root Cause** | Risk Library approved in WP18B but population deferred to WP18B-EXT quick win. |
| **Resolution (Short-term)** | BU Lead reviews and approves the 9 AI-generated risks in S-50 before ARM IT045 submission. |
| **Resolution (Long-term)** | Execute WP18B-EXT: extract 75–90 risk entries from existing capability asset risk registers and approve them via BU Lead. This permanently resolves the gap for all future tenders. |
| **Resolution Owner** | BU Lead |
| **Resolution Effort** | 2 hours (review + approval for ARM IT045); 4–6 hours AI session + 3 hours BU review (WP18B-EXT) |
| **Factory Remediation** | Once Risk Library populated, S-50 changes from AI-GENERATE (L1) to EXTRACT (L3). |
| **Recurrence** | Will affect all tenders until WP18B-EXT is completed. |

---

### GAP-007 — Executive Summary: AI-Generated Only

| Field | Value |
|---|---|
| **Gap ID** | GAP-007 |
| **Category** | G-ASS (Assembly/Content) |
| **Severity** | SEV-2 — SIGNIFICANT |
| **Sections Affected** | S-13 (Executive Summary) |
| **Description** | The Executive Summary is AI-generated using tender context and KB assets. The draft is substantive but must be personalised to the specific relationship (ARM is an existing client), reviewed for tone and commercial sensitivity, and approved by the BU Lead and Account Manager. |
| **Root Cause** | Executive Summary is inherently tender-specific and relationship-dependent. Cannot be fully deterministic. This is expected maturity L1→L4 (AI-assisted, not fully automated). |
| **Resolution** | BU Lead + AM review and rewrite as needed. ARM IT045 has a strong relationship angle (previous work, named references) that should be foregrounded. |
| **Resolution Owner** | BU Lead + Account Manager |
| **Resolution Effort** | 1–2 hours |
| **Factory Remediation** | Maturity L1→L4 is the target for Executive Summary. L5 is not achievable (always relationship-specific). The Factory's AI draft reduces effort from 3–4h to 1–2h. |
| **Recurrence** | Permanent — every tender needs a personalised Executive Summary. |

---

### GAP-008 — Understanding of Requirements: No Requirement Extraction Engine

| Field | Value |
|---|---|
| **Gap ID** | GAP-008 |
| **Category** | G-REQ (Requirement) |
| **Severity** | SEV-2 — SIGNIFICANT |
| **Sections Affected** | S-14 (Understanding of Requirements) |
| **Description** | The Understanding of Requirements section was AI-generated from tender context. A formal Requirement Extraction Engine (Pipeline Stage 2) does not yet exist. Requirements have not been formally extracted from the ARM IT045 RFP and mapped to APPSolve's capability. The AI draft is adequate for a review starting point but needs BU Lead validation. |
| **Root Cause** | Pipeline Stage 2 (Requirement Extraction) is a future work package — not yet built. This is a known Factory architecture gap. |
| **Resolution (Short-term)** | BU Lead and AM read the ARM IT045 RFP and validate/correct the AI-drafted Understanding section. |
| **Resolution (Long-term)** | Build Requirement Extraction Engine (Pipeline Stage 2 — future WP). |
| **Resolution Owner** | BU Lead + AM (short-term) |
| **Resolution Effort** | 1–2 hours (review); 2–4 weeks (Requirement Extraction Engine — future) |
| **Factory Remediation** | Stage 2 (Requirement Extraction) is a future pipeline investment. Expected WP19 or WP20 scope. |
| **Recurrence** | Permanent until Stage 2 is built. |

---

### GAP-009 — B-BBEE Certificate Expiry Risk

| Field | Value |
|---|---|
| **Gap ID** | GAP-009 |
| **Category** | G-COMP (Compliance) |
| **Severity** | SEV-2 — SIGNIFICANT |
| **Sections Affected** | S-12, S-59, A-05 |
| **Description** | APPSolve's B-BBEE Level 3 certificate expires 2026-07-31. ARM IT045 was won 28 August 2025 — this is a historical reference tender used as an MVP test. However, for any future tender submitted after 2026-07-31, the certificate will be expired. This affects competitive positioning (BEE Level 3 is a common minimum requirement for government-adjacent and JSE-listed clients). |
| **Root Cause** | Certificate expiry is a business operations matter, not a Factory architecture gap. The Factory correctly flags the expiry; the resolution is outside the Factory. |
| **Resolution** | BU Lead to: (1) confirm B-BBEE renewal is in progress and expected date; (2) update COMPLIANCE_REGISTER.csv when renewed. The Proposal Factory will automatically reflect the updated status. |
| **Resolution Owner** | BU Lead (business operations) |
| **Resolution Effort** | External — depends on verification agency timeline. Factory effort: 15 minutes to update COMPLIANCE_REGISTER.csv. |
| **Factory Remediation** | The Factory correctly identifies this flag. Long-term: automated compliance expiry alerting (WP19 or WP20) to proactively flag certificates approaching expiry. |
| **Recurrence** | Every tender after 2026-07-31 until renewed. |

---

### GAP-010 — EBS Capability Asset Vintage (W2S1-002)

| Field | Value |
|---|---|
| **Gap ID** | GAP-010 |
| **Category** | G-CAP (Capability) |
| **Severity** | SEV-2 — SIGNIFICANT |
| **Sections Affected** | S-18 (Oracle EBS Capability) |
| **Description** | W2S1-002 (Oracle EBS Capability Statement) is flagged as potentially vintage — reference data (client names, headcount, version coverage) may need modernisation. The CONTENT_SOURCE_MATRIX.md flags W2S1-002 as requiring periodic refresh. For a critical tender like ARM IT045, the BU Lead should validate current client list and version claims before inclusion. |
| **Root Cause** | KB asset maintenance cadence — W2S1-002 was approved but may not have been refreshed since initial authoring. |
| **Resolution** | BU Lead to review W2S1-002 for currency; update client list, version claims, and any statistics before the next Oracle EBS tender submission. |
| **Resolution Owner** | BU Lead |
| **Resolution Effort** | 2–3 hours (review and update) |
| **Factory Remediation** | Periodic review of W2S1-002 (and all W2-series assets) to be added to the Capability Library maintenance calendar. |
| **Recurrence** | Annual review cycle recommended. |

---

## 4. SEV-3 — Advisory Gaps

These gaps do not prevent submission but represent opportunities to improve Factory output quality.

---

### GAP-011 — Team Structure: CONSULTANT_INDEX Integration Limited

| Field | Value |
|---|---|
| **Gap ID** | GAP-011 |
| **Category** | G-CV |
| **Severity** | SEV-3 — ADVISORY |
| **Sections Affected** | S-46 (Team Structure) |
| **Description** | The Factory produced a team structure template with role definitions and hour allocations from the EBS-DRM Overlay. However, it cannot pre-populate names from CONSULTANT_INDEX.csv because CONSULTANT_INDEX does not currently have AMS role matching metadata (which consultants are qualified for which AMS roles). Adding role-matching metadata to CONSULTANT_INDEX.csv would allow the Factory to suggest named resource candidates for BU Lead confirmation. |
| **Root Cause** | CONSULTANT_INDEX.csv does not have structured role/capability tagging sufficient for AMS role matching. |
| **Resolution** | Add AMS role classification metadata to CONSULTANT_INDEX.csv. Factory can then suggest candidates; BU Lead confirms. |
| **Resolution Owner** | BU Lead (HR/Resource Management) |
| **Resolution Effort** | 2–4 hours (metadata addition to CONSULTANT_INDEX) |
| **Factory Remediation** | Enriched CONSULTANT_INDEX enables L2→L3 for team structure assembly. |

---

### GAP-012 — OCI DBA Stats Verification (W2S1-003)

| Field | Value |
|---|---|
| **Gap ID** | GAP-012 |
| **Category** | G-CAP |
| **Severity** | SEV-3 — ADVISORY |
| **Sections Affected** | S-20 (Oracle DBA Capability) |
| **Description** | W2S1-003 (Oracle DBA Executive Summary) contains team size claims ("one of the largest locally-based Oracle DBA teams in South Africa"). These claims should be verified by the BU Lead before submission to ensure they remain accurate. |
| **Root Cause** | Headcount and comparative claims age quickly and should be verified periodically. |
| **Resolution** | BU Lead to verify DBA team size claim and update W2S1-003 if needed. |
| **Resolution Owner** | BU Lead |
| **Resolution Effort** | 30 minutes |

---

### GAP-013 — Security Architecture: No Standalone Security Methodology Asset

| Field | Value |
|---|---|
| **Gap ID** | GAP-013 |
| **Category** | G-METH (Methodology) |
| **Severity** | SEV-3 — ADVISORY |
| **Sections Affected** | S-45 (Security Architecture) |
| **Description** | The Security Architecture section was assembled from OCI assumption pack SEC sections. This provides an adequate framework but is a proxy — there is no approved standalone Security Methodology asset in the Methodology Library. A dedicated Security Architecture methodology asset (similar to the DR methodology that was also flagged absent) would significantly improve the quality and comprehensiveness of S-45. |
| **Root Cause** | Security Methodology asset is in scope for WP18B-METH4 but not yet authored. |
| **Resolution** | Author Security Architecture methodology asset as part of WP18B-METH4. |
| **Resolution Owner** | BU Lead |
| **Resolution Effort** | 4–8 hours (WP18B-METH4 scope) |
| **Factory Remediation** | S-45 changes from AI-assisted proxy to EXTRACT once methodology asset exists. |

---

### GAP-014 — Case Study Library Absent

| Field | Value |
|---|---|
| **Gap ID** | GAP-014 |
| **Category** | G-CASE (Case Study) |
| **Severity** | SEV-3 — ADVISORY |
| **Sections Affected** | S-68 (Case Studies) — omitted for ARM IT045 |
| **Description** | Section S-68 (Case Studies) was omitted from the ARM IT045 proposal because no structured case study library exists in the KB. Case studies are a high-value proposal section for capability demonstration. REF-ORA-008 (ARM) and REF-ORA-009 (MTN) are the strongest candidates for EBS AMS case studies. |
| **Root Cause** | Case Study Library was identified as a high-effort gap in WP18A Automation Maturity Model (P10 in priority matrix). Not yet built. |
| **Resolution** | Build Case Study Library (structured case study assets for approved references). Estimated effort: 2–3 days AI session + BU review per case study. |
| **Resolution Owner** | BU Lead |
| **Resolution Effort** | High — full WP required |
| **Factory Remediation** | Case Study Library is a future roadmap item (WP18A Priority P10). Not blocking for ARM IT045. |

---

## 5. Gap Summary by Category

| Gap Category | SEV-1 | SEV-2 | SEV-3 | Total |
|---|---|---|---|---|
| G-CAP (Capability) | 1 (GAP-004) | 1 (GAP-010) | 1 (GAP-012) | 3 |
| G-COMM (Commercial) | 1 (GAP-002) | 0 | 0 | 1 |
| G-COMP (Compliance) | 1 (GAP-005) | 1 (GAP-009) | 0 | 2 |
| G-CV (Consultant/CV) | 1 (GAP-001) | 0 | 1 (GAP-011) | 2 |
| G-REF (Reference) | 1 (GAP-003) | 0 | 0 | 1 |
| G-REQ (Requirement) | 0 | 1 (GAP-008) | 0 | 1 |
| G-RISK (Risk) | 0 | 1 (GAP-006) | 0 | 1 |
| G-ASS (Assembly/Content) | 0 | 1 (GAP-007) | 0 | 1 |
| G-METH (Methodology) | 0 | 0 | 1 (GAP-013) | 1 |
| G-CASE (Case Study) | 0 | 0 | 1 (GAP-014) | 1 |
| **TOTAL** | **5** | **5** | **4** | **14** |

---

## 6. Factory Improvement Roadmap (Gap-Driven)

| Priority | Gap(s) | Action | Work Package | Effort | Maturity Gain |
|---|---|---|---|---|---|
| P1 | GAP-004 | Author OCI capability narrative asset | WP18B-METH4 or quick win | 4–8h | S-22: AI-GENERATE → DIRECT |
| P2 | GAP-006 | Populate Risk Library (WP18B-EXT) | WP18B-EXT | 8–12h AI + 3h BU | S-50: AI-GENERATE → EXTRACT |
| P3 | GAP-013 | Author Security Methodology asset | WP18B-METH4 | 4–8h | S-45: proxy → EXTRACT |
| P4 | GAP-011 | Enrich CONSULTANT_INDEX with AMS role metadata | Quick win | 2–4h | S-46: TEMPLATE → semi-automated |
| P5 | GAP-014 | Build Case Study Library | Future WP | High | S-68: absent → EXTRACT |
| P6 | GAP-003 | Build AM approval workflow in Reference Selector | WP19 or beyond | Medium | S-67: manual → governed workflow |
| P7 | GAP-008 | Build Requirement Extraction Engine | Future WP (Stage 2) | Very high | S-14: AI-GENERATE → L4 |

---

*ARM_IT045_FACTORY_GAP_REGISTER.md v1.0 | WP18C — Proposal Factory Assembly Engine v1.0 | 2026-06-25*  
*Stage 7 output. 14 gaps detected: 5 SEV-1 (blocking), 5 SEV-2 (significant), 4 SEV-3 (advisory). Factory improvement roadmap: 7 items.*
