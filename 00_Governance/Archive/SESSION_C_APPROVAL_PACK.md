# Session C — BeBanking Approval Pack
**Prepared:** 2026-06-10 | **Reviewer:** Hein Blignaut (BeBanking BU lead)
**Purpose:** Consolidated review pack for all 9 BeBanking files in Review_Required. Approve this set before authoring W1S3-005.
**Total files:** 9 | **Estimated review time:** 2–3 hours

---

## 1. Executive Summary

All 9 files have been extracted from source documents, reviewed against confirmed BU lead answers (BQ1–BQ13), and remediated to remove obsolete content. The remediation work was substantial: the primary source (SITA 2017 proposal) described a 2017-era architecture (Connect Direct, Dedicated Banking Server, two-level approval, IBY module, Automated Receipt Creation) that no longer reflects the current product. Every one of those components has been removed and replaced with confirmed 2026 content.

**The result is 9 files that represent BeBanking's current capability** — not a 2017 proposal with some cosmetic updates.

### Source Documents

| Source | Version | Date | Files sourced from it |
|---|---|---|---|
| APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx | V5.1 | December 2024 | W1S3-001 only |
| APPSolve SITA Host-to-Host BEBanking Proposal v1.06.docx | v1.06 | June 2017 | W1S3-002, 003, 004, 006, 007, 008, 009, 010 |

The HyDac December 2024 document was the most current available; the SITA 2017 document had the most detailed product content. All SITA-sourced files required significant modernisation.

### What Was Removed Across the Set (Do Not Reinstate)

| Removed Item | Reason | BQ Reference |
|---|---|---|
| Connect Direct connectivity | Architecture retired; replaced with API | BQ1 |
| Dedicated Banking Server | Not required in API-first model | BQ1 |
| IBY (Oracle Internet Banking module) | EBS-specific legacy; not used in current architecture | BQ6 |
| AP Level 1 / AP Level 2 / PAY Level 1 / PAY Level 2 approval naming | Obsolete approval framework nomenclature | BQ2 |
| "Two-Level Approval" as a fixed product description | Approval levels are configurable, not fixed at two | BQ2 |
| Automated Receipt Creation module | Module retired | BQ7 |
| Secure File Transfer Utility module | Module retired | BQ7 |
| "24x7x365 standby" | Overstated; corrected to confirmed support model | BQ8/BQ10 |
| Service Option / Software Option licence models | Obsolete; replaced with subscription model | BQ9 |
| AR receipt creation rows in integration tables | Module retired | BQ7 |
| Single-source exchange rate description | Multi-provider model confirmed | BQ12 |

### What Was Added Across the Set (AI-Authored From Confirmed Baseline)

| Added Item | Confidence | BQ Reference |
|---|---|---|
| Oracle Fusion Applications integration (W1S3-002, 004, 006, 008) | High — confirmed by BQ6 | BQ6 |
| Acumatica integration detail (W1S3-002, 006, 008) | High — confirmed by BQ5 | BQ5 |
| SAP integration entry (W1S3-001, 006, 008) | Medium — confirmed in principle; detail pending | BU lead confirmation |
| Full 9-bank list (W1S3-002, 008) | High — confirmed by BQ4 | BQ4 |
| ABSA Proof of Payment Integration module (W1S3-001) | High — confirmed by BQ7 | BQ7 |
| International and Forex Payment Processing module (W1S3-001) | High — confirmed by BQ7/BQ11 | BQ7/BQ11 |
| POPIA compliance section (W1S3-007) | High — confirmed by BQ13 | BQ13 |
| GDPR roadmap note (W1S3-007) | High — future-state only per BQ13 | BQ13 |
| Monitoring capabilities table (W1S3-010) | Medium — AI-authored from BQ10 baseline | BQ10 |
| Exchange rate multi-provider statement (W1S3-010) | High — confirmed FNB/Andisa/ExchangeRate-API | BQ12 |
| Cloud ERP deployment model (W1S3-009) | High — confirmed by BQ5/BQ6 | BQ5/BQ6 |
| Subscription-only commercial model (W1S3-009) | High — confirmed by BQ9 | BQ9 |

### Overall Assessment

Five of the nine files are clean with no open questions and can be approved as-is. Two files have minor wording decisions for the BU lead. Two files require a BU lead decision on specific sentences before approval. No files require external verification.

---

## 2. File-by-File Approval Recommendation

### W1S3-001 — BeBanking Product Overview

**Source:** HyDac V5.1 December 2024 (DIRECT)
**Recommendation:** Approve — subject to confirming SAP entry wording (see Section 4, Decision D1)

**What BU lead should verify:**
- Module portfolio table (9 modules listed) — confirm count and names are correct
- ERP compatibility list — confirm Oracle EBS, Oracle Fusion, Acumatica, SAP entries are all appropriate for tender use
- SAP entry reads "confirmed integration" — confirm this minimal claim is acceptable (see D1)
- Acumatica payroll exclusion note — confirm wording is correct
- Geographic framing in the intro (South Africa, CMA, UK, Chile) — confirm this is accurate

**Risk level:** Low. Source is December 2024. Module list confirmed by BQ7. Main decision is the SAP entry wording.

---

### W1S3-002 — Host-to-Host Banking Core Capability

**Source:** SITA v1.06 2017 (MODERNISE)
**Recommendation:** Approve as-is

**What BU lead should verify:**
- "How BeBanking H2H Works" steps 1–6 — confirm the process description is accurate end-to-end
- Approval framework description (Step 2) — "configurable number of levels, first-responder or voting-based authorisation, configurable segregation-of-duty controls" — confirm this accurately describes the product
- Bank list (9 banks) — confirm this is the correct and complete current list
- Payroll scope note at the end of the Payroll H2H section — confirm wording

**Risk level:** Low. All facts confirmed by BQ1 (connectivity), BQ2 (approval framework), BQ4 (bank list), BQ5 (Acumatica), BQ6 (Oracle Fusion).

**Governance note on approval:** When this file is approved, update `AI_CONTEXT.md` — the banking partners statement currently reads "Do not list specific bank names unless confirmed by the BU lead." BQ4 has now confirmed the full 9-bank list. The AI_CONTEXT.md banking partner rule is outdated and should be revised to reflect the confirmed bank list.

---

### W1S3-003 — Supplier Payments

**Source:** SITA v1.06 2017 (MODERNISE)
**Recommendation:** Approve as-is

**What BU lead should verify:**
- Supplier Bank Account Approval section — confirm the approval framework description is accurate
- AVS section — confirm AVS is still an active module and the description is current
- Supplier H2H Payments and Approval section — confirm the void-during-approval capability is correct
- Supplier PDF Remittances section — confirm this accurately describes the remittance delivery process

**Risk level:** Low. All content from confirmed baseline. No open questions.

---

### W1S3-004 — Payroll Payments

**Source:** SITA v1.06 2017 (MODERNISE)
**Recommendation:** Approve as-is

**What BU lead should verify:**
- Step 1 — "Supported ERP platforms for payroll H2H include Oracle EBS and Oracle Fusion Applications" — confirm this is the complete list (no other payroll ERP sources)
- ACB file reference — confirm ACB (Automated Clearing Bureau) is still the correct South African payroll file format
- Data Segregation section — confirm separate H2H profile description is accurate
- Benefits section — confirm all four bullet points are accurate

**Risk level:** Low. Acumatica payroll exclusion is correctly applied. Oracle EBS and Oracle Fusion confirmed as payroll sources.

---

### W1S3-006 — ERP Integration

**Source:** SITA v1.06 2017 (MODERNISE — with AI-authored Fusion, Acumatica, and SAP sections)
**Recommendation:** Approve — subject to confirming SAP section wording (see Section 4, Decision D2)

**What BU lead should verify:**
- **Oracle EBS section** — integration table (AP, PAY, CE, GL modules); integration notes. Confirm IBY exclusion note is correctly stated: "There is no Oracle Internet Banking (IBY) module dependency in the current architecture."
- **Oracle Fusion section** — entirely AI-authored from BQ6 baseline. Read in full. Integration table (Fusion Payables, Fusion Payroll, Fusion Cash Management, Fusion GL). Confirm Oracle Fusion integration notes are accurate.
- **Acumatica section** — AI-authored from BQ5 baseline. Integration table (Acumatica Payments, Acumatica Cash Management). Confirm "Local payments (ZAR domestic EFT and ACH)" is correct — specifically confirm ACH (Automated Clearing House) is the correct terminology for Acumatica/SA context or whether EFT only is more accurate.
- **SAP section** — two sentences; confirm wording (see Decision D2)
- Connectivity requirements table at the bottom — confirm all rows are accurate

**Risk level:** Medium. Most AI-authored new sections in the set. BU lead should read this file carefully.

---

### W1S3-007 — Security

**Source:** SITA v1.06 2017 (MODERNISE)
**Recommendation:** Approve as-is

**What BU lead should verify:**
- Five security design principles — confirm all five are accurate
- Access control section — confirm approval framework description is correct
- Supplier Bank Account Security section — confirm AVS integration description
- Transmission Security section — confirm API-first / SFTP-over-SSH description is accurate
- **POPIA section** — confirm the POPIA statement is accurate and appropriate for tender use
- **GDPR section** — confirm "GDPR compliance is on the BeBanking product roadmap. Clients operating in jurisdictions with GDPR obligations should note this as future-state capability." This is the correct framing per BQ13 — but confirm this is still the current position.

**Risk level:** Low. All changes from confirmed baseline. POPIA/GDPR framing confirmed by BQ13.

---

### W1S3-008 — Technical Architecture

**Source:** SITA v1.06 2017 (MODERNISE — significant rewrite; architecture diagram redrawn)
**Recommendation:** Approve — after verifying architecture diagram accuracy

**What BU lead should verify:**
- **Architecture diagram** — the three-tier diagram (ERP System → BeBanking API Layer → Bank H2H Systems) has been redrawn from scratch. Confirm this accurately represents how BeBanking actually works.
- Notes on the diagram: "The BeBanking Integration Layer is deployed within or adjacent to the ERP environment" and "No dedicated banking server is required" — confirm both are correct.
- "Deployment supports on-premises ERP (Oracle EBS, SAP) and cloud ERP (Oracle Fusion, Acumatica)" — confirm SAP in this list is accurate given D1/D2 SAP decisions.
- Component architecture tables (Integration Layer functions; API Layer functions) — read in full and confirm each row is accurate.
- Deployment requirements table — specifically "BeBanking Integration Layer: Application server; deployed on-premises (for EBS/SAP) or as cloud-hosted instance (for Oracle Fusion, Acumatica)" — confirm this is accurate.
- Security architecture table — confirm all seven rows are correct.

**Risk level:** Medium. The architecture diagram was redrawn from the 2017 source based on the confirmed API-first model. BU lead should verify the diagram represents the actual product architecture before this file is used in a technical tender section.

---

### W1S3-009 — Hosting Model and Commercial Terms

**Source:** SITA v1.06 2017 (MODERNISE — commercial model completely rewritten)
**Recommendation:** Approve — subject to confirming two wording items (see Section 4, Decisions D3 and D4)

**What BU lead should verify:**
- **Hosting Overview paragraph** — contains "Connect Direct licences" in a historical comparison context (see Decision D3)
- Deployment architecture tables (on-premises and cloud) — confirm all responsibility assignments are correct
- **Support model table** — 6 rows; read each. Confirm "Bank connectivity monitoring: 24x7 monitoring capability with after-hours support services" is accurate.
- **Commercial Model** — Monthly and Annual subscription per module. Confirm this is correct.
- Commercial Model Notes bullet: "There is no software licence ownership, no once-off implementation fee for the product component, and no perpetual licence" — see Decision D4.

**Risk level:** Medium. Commercial terms section was completely rewritten because the 2017 Service Option/Software Option models are obsolete. The BU lead should confirm the subscription model description is accurate before this is used in a commercial tender section.

---

### W1S3-010 — Monitoring and Automation

**Source:** SITA v1.06 2017 (MODERNISE)
**Recommendation:** Approve as-is

**What BU lead should verify:**
- **Automated Processes table** (5 processes) — confirm count and descriptions. Specifically: bank statement import, payment response matching, supplier PDF remittance, exchange rate loading, payment approval notifications.
- Exchange rate loading row: "FNB / Andisa / ExchangeRate-API (client choice)" — confirm this is the correct current list of supported providers.
- **Automated Bank Statement Management section** — confirm the "Unbreakable Bank Statements" description is current and accurate.
- **Exchange Rate Automation section** — read the "Wording note" at the bottom of this section and confirm: do you want this note retained in the final approved file (it's an internal reminder not to misstate the exchange rate sources), or should it be removed when approving?
- **Monitoring table** — 5 rows; AI-authored from BQ10 baseline. Read each row and confirm the monitoring descriptions are accurate.
- **Client-Side Audit and Reporting table** — 5 rows; confirm all five report types exist in the current product.

**Risk level:** Low-medium. The monitoring and audit reporting sections are AI-authored from BQ10 baseline and are the most detailed new content in this file. BU lead should read these sections more carefully than the automation table.

---

## 3. Remaining Factual Risks

The following risks apply across the file set. They are ranked by potential impact.

### R1 — SAP Integration Claims (High — cross-cutting)

**Affects:** W1S3-001, W1S3-006, W1S3-008, W1S3-009 (implicitly)

SAP is stated as a confirmed ERP integration. This is correct — the BU lead confirmed SAP integration during Session C (2026-06-10). However, BQ-WEB-04 (SAP detail verification from BeBanking website) is still open, and no SAP-specific tender documentation has been produced.

**Current treatment:** W1S3-001 has a minimal entry ("SAP — confirmed integration"); W1S3-006 has two sentences with a deliberate deflection ("Detailed SAP module and version support is available from the BeBanking BU lead"); W1S3-008 mentions SAP only in the deployment notes diagram caption.

**Risk:** If a client asks for SAP integration specifics and the product cannot deliver what was implied, this creates a delivery risk. The current minimal treatment reduces this risk — but BU lead should explicitly confirm what SAP claims are defensible.

**Resolution:** See Decision D1 and D2.

---

### R2 — Acumatica "ACH" Terminology in W1S3-006 (Low-Medium)

**Affects:** W1S3-006 only

The Acumatica confirmed capabilities section reads: "Local payments (ZAR domestic EFT and ACH)."

ACH (Automated Clearing House) is a US payment network term. In South Africa, the equivalent is the SASWITCH / SARB National Payment System, and payment file formats are typically EFT/ACB. ACH may cause confusion or appear incorrect to a South African treasury auditor.

**Possible issue:** The Acumatica ERP platform may use "ACH" in its module naming (this is an Acumatica product convention), in which case the term is technically correct as a product reference. But in a South African tender context, this may need clarification.

**Resolution:** BU lead to confirm: does BeBanking's Acumatica integration use ACH terminology, or should this read "ZAR domestic EFT"? See Decision D5.

---

### R3 — Monitoring Section AI-Authorship (Low-Medium)

**Affects:** W1S3-010 primarily; W1S3-009 support model table

The monitoring table in W1S3-010 and the support model table in W1S3-009 were authored by AI from BQ10 confirmed baseline. They were not extracted from a source document. The content is based on BU lead answers, not historical proposal text.

**Risk:** If the BU lead's BQ10 answer was summarised or interpreted differently from the actual operational monitoring capability, the tables may overstate or incorrectly describe the monitoring service.

**Resolution:** BU lead should read both tables against their operational knowledge and correct any inaccuracies before approving W1S3-009 and W1S3-010.

---

### R4 — GDPR Roadmap Statement Accuracy (Low)

**Affects:** W1S3-007 only

GDPR compliance is described as "on the BeBanking product roadmap." This was confirmed per BQ13. However, if any GDPR-related development has progressed since the BQ13 answer was given, the "future-state" framing may be outdated.

**Resolution:** BU lead to confirm the GDPR roadmap statement is still the correct position. If GDPR compliance has progressed, the wording should be updated before approval.

---

### R5 — AI_CONTEXT.md Banking Partner Rule (Low — governance)

**Affects:** Not a content risk in W1S3-002; a governance risk for future AI sessions

`AI_CONTEXT.md` currently states: "Banking partners: Supports connectivity with all major South African banks. Do not list specific bank names unless confirmed by the BeBanking BU lead."

BQ4 (confirmed 2026-06-10) provides the full 9-bank list, which is now correctly included in W1S3-002. However, AI_CONTEXT.md has not been updated to reflect this. A future AI session reading AI_CONTEXT.md in isolation could incorrectly refuse to list specific banks even when the full bank list is in an approved file.

**Resolution:** When W1S3-002 is approved, update `AI_CONTEXT.md` — replace the "Do not list specific bank names" line with the confirmed 9-bank list. This is a governance action on approval, not a blocker for approval itself.

---

## 4. Remaining BU Lead Decisions

The following decisions are required. Each is labelled with a decision ID for easy reference when communicating back to the extractor.

---

### D1 — SAP Entry Wording in W1S3-001

**File:** W1S3-001 — Product Overview
**Current wording:**
```
| SAP | confirmed integration |
```
(in the ERP Compatibility table)

**Decision required:** Is this level of detail — "confirmed integration" with no module or version specifics — appropriate for a tender document, or does it need more or less detail?

**Option A — Keep as-is.** "Confirmed integration" is a minimal, defensible claim. It does not overstate the integration. Clients who ask for more detail are redirected to the BU lead. Approve without changes.

**Option B — Add one sentence.** If the BU lead can confirm a minimum SAP capability statement (e.g., "SAP ERP and SAP S/4HANA — payment file generation and H2H transmission via the BeBanking API layer"), replace the minimal entry with that.

**Option C — Remove SAP from this file.** If there is any possibility that the SAP integration is not yet production-ready or not yet customer-facing, removing it from the product overview reduces risk. SAP can be added back when BQ-WEB-04 is resolved.

**Recommendation:** Option A if the BU lead is confident the SAP integration is deployed and client-facing. Option C if the integration is still in development or not yet sold as a product offering.

---

### D2 — SAP Section Wording in W1S3-006

**File:** W1S3-006 — ERP Integration
**Current wording:**

> BeBanking is compatible with SAP ERP. Integration follows the same BeBanking middleware model — payment files generated from SAP AP and transmitted via the BeBanking H2H layer. Detailed SAP module and version support is available from the BeBanking BU lead.

**Decision required:** Is the deflection sentence — "Detailed SAP module and version support is available from the BeBanking BU lead" — appropriate for a tender document, or does it signal a gap that a procurement team would penalise?

**Option A — Keep as-is.** The deflection is honest. It does not overstate the integration. In a tender evaluation, the panel might note that the detail is available on request, which is defensible.

**Option B — Replace deflection with minimum detail.** If the BU lead can supply the minimum SAP facts (e.g., supported SAP version, which SAP modules integrate), replace the deflection sentence with that.

**Option C — Remove SAP section from W1S3-006.** If the SAP section would create more questions than it answers in a tender context, remove it from this file. The SAP entry in W1S3-001 would still be present if Decision D1 keeps it.

**Recommendation:** Decide D1 first. D2 should be consistent with D1.

---

### D3 — "Connect Direct Licences" in W1S3-009

**File:** W1S3-009 — Hosting Model and Commercial Terms
**Location:** Hosting Overview, first paragraph
**Current wording:**

> Clients do not need to procure banking software, manage Connect Direct licences, or maintain dedicated banking infrastructure.

**Decision required:** This sentence is technically accurate — clients do not need to manage these things. However, "Connect Direct licences" introduces a retired product name into a tender document. A client unfamiliar with Connect Direct might find the reference confusing.

**Option A — Keep as-is.** The sentence is true and positions BeBanking as removing infrastructure burden. The mention of Connect Direct is historical context, not a claim.

**Option B — Remove the Connect Direct reference.** Replace with:

> Clients do not need to procure banking software, manage bank connectivity infrastructure, or maintain dedicated banking hardware.

This is cleaner for a modern tender document and removes retired terminology.

**Recommendation:** Option B. The sentence is forward-looking in purpose; the Connect Direct reference is a legacy artefact that adds no value to a prospect who has never encountered Connect Direct.

---

### D4 — Commercial Model Notes Wording in W1S3-009

**File:** W1S3-009 — Hosting Model and Commercial Terms
**Location:** Commercial Model Notes, third bullet
**Current wording:**

> There is no software licence ownership, no once-off implementation fee for the product component, and no perpetual licence

**Decision required:** The phrase "no once-off implementation fee for the product component" is intended to mean there is no once-off BeBanking software fee (because it is subscription-only). However, it could be misread as "APPSolve does not charge an implementation fee" — which would be incorrect (APPSolve charges professional services fees for the implementation project).

**Option A — Keep as-is.** "For the product component" is the qualifying phrase that distinguishes the product subscription from implementation services. Accept the current wording.

**Option B — Rewrite for clarity:**

> There is no software licence fee, no perpetual licence, and no once-off product purchase. BeBanking is priced on a module subscription basis only. Professional services fees for implementation are separate and quoted per project.

**Recommendation:** Option B if there is any risk of misinterpretation. Option A if the BU lead is comfortable with the "product component" qualifier.

---

### D5 — "ACH" Terminology in W1S3-006 Acumatica Section

**File:** W1S3-006 — ERP Integration
**Location:** Acumatica — Confirmed Capabilities, first bullet
**Current wording:**

> Local payments (ZAR domestic EFT and ACH)

**Decision required:** Is "ACH" the correct term in the Acumatica context, or should this read "ZAR domestic EFT" only?

**Background:** ACH is a US payment network term. In South Africa, domestic EFT payments are processed through the SARB-managed interbank payment systems; ACH as a term may appear in Acumatica's module naming (Acumatica is a US-origin product). If BeBanking's Acumatica integration processes both EFT and ACH-format transactions, both terms are correct. If Acumatica SA deployments use EFT only, "ACH" should be removed.

**Option A — Keep "ZAR domestic EFT and ACH."** Acumatica uses ACH terminology for its payment processing module and the integration supports this.

**Option B — Change to "ZAR domestic EFT."** Remove ACH from the description; EFT covers domestic payments in the South African context.

**Recommendation:** BU lead to confirm based on technical knowledge of the Acumatica Payments module integration. If uncertain, use Option B (EFT only) — it is less specific but not incorrect.

---

### D6 — Wording Note in W1S3-010 (Retain or Remove)

**File:** W1S3-010 — Monitoring and Automation
**Location:** Exchange Rate Automation section, final line
**Current wording:**

> **Wording note:** Do not describe exchange rates as "sourced directly from the bank" — this implies the bank is the only provider. Use "sourced from client-selected rate provider (FNB, Andisa, or ExchangeRate-API)."

**Decision required:** This note is an internal extractor reminder, not tender content. It should be removed from the approved version of this file. But the BU lead should confirm before it is removed: is the multi-provider statement (FNB, Andisa, ExchangeRate-API) correct and complete?

**Resolution:** This note must be removed before or at approval. It is not appropriate for a client-facing document. It should be replaced with nothing (the preceding Exchange Rate Automation section already contains the correct wording). If the BU lead confirms the provider list is current and complete, remove the note. If the provider list needs updating, update it first, then remove the note.

---

## 5. Exact Wording Recommendations

### For D3 (W1S3-009) — Replace the Connect Direct sentence

**Replace:**
> Clients do not need to procure banking software, manage Connect Direct licences, or maintain dedicated banking infrastructure.

**With:**
> Clients do not need to procure banking software, manage bank connectivity infrastructure, or maintain dedicated banking hardware.

---

### For D4 Option B (W1S3-009) — Clarify commercial model notes

**Replace:**
> There is no software licence ownership, no once-off implementation fee for the product component, and no perpetual licence

**With:**
> There is no software licence fee, no perpetual licence, and no once-off product purchase. BeBanking is priced on a module subscription basis only. Professional services fees for implementation are separate and quoted per project.

---

### For D6 (W1S3-010) — Remove wording note

**Remove entirely** (the two-line wording note at the end of the Exchange Rate Automation section). The section above it already contains correct wording. No replacement needed.

---

### For AI_CONTEXT.md banking partner update (on W1S3-002 approval)

**Replace** (in AI_CONTEXT.md, BeBanking section, banking partners line):
> **Banking partners:** Supports connectivity with all major South African banks. Do not list specific bank names unless confirmed by the BeBanking BU lead.

**With:**
> **Banking partners (confirmed BQ4, 2026-06-10):** ABSA, FNB (First National Bank), Nedbank (South Africa), Nedbank (Namibia), Standard Bank (South Africa), Standard Bank (Namibia), Investec (South Africa), Citi Bank (United Kingdom), Santander Bank (Chile). Nine banking integrations total across South Africa, CMA region, and international.

---

## 6. Which Files Can Be Approved Immediately

These files have no open decisions. BU lead reads the file in full, spot-checks against the source notes, confirms content is accurate, and sets `approved_for_reuse: Yes`.

| File | Key thing to read carefully | Time estimate |
|---|---|---|
| W1S3-002 — H2H Core | Bank list (9 banks); approval framework description | 15 min |
| W1S3-003 — Supplier Payments | AVS and remittance sections | 10 min |
| W1S3-004 — Payroll Payments | ACB reference; payroll scope note | 10 min |
| W1S3-007 — Security | POPIA section; GDPR roadmap statement | 15 min |
| W1S3-010 — Monitoring | Monitoring table (AI-authored); exchange rate providers | 15 min |

**Total estimated time: 65 minutes**

---

## 7. Which Files Require Edits Before Approval

These files require one or more decisions from Section 4 to be resolved, and may require a minor edit, before `approved_for_reuse: Yes` can be set.

| File | Required decisions | Edit required if... |
|---|---|---|
| W1S3-001 — Product Overview | D1 (SAP entry wording) | BU lead chooses Option B or C for D1 |
| W1S3-006 — ERP Integration | D2 (SAP section), D5 (ACH terminology) | BU lead chooses Option B or C for D2, or Option B for D5 |
| W1S3-009 — Hosting + Commercial | D3 (Connect Direct mention), D4 (commercial notes) | If BU lead accepts D3 Option B or D4 Option B (recommended) |

Additionally:
- W1S3-010 requires D6 resolution (remove the internal wording note) before approval regardless of other decisions.

---

## 8. Which Files Require External Verification

**None.** All facts in these files are sourced from:
- BU lead confirmed answers (BQ1–BQ13, 2026-06-10)
- December 2024 HyDac proposal (current source)
- Internal product knowledge

The only external verification items are the open BQ-WEB questions (BQ-WEB-03 Sage, BQ-WEB-04 SAP detail) — but these do not block approval of what is currently written. If BQ-WEB-03 resolves to Sage being a confirmed ERP integration, a new file would need to be created or these files updated. If BQ-WEB-04 provides more SAP detail, W1S3-001, W1S3-006 could be enriched.

Neither outcome blocks the current approval round.

---

## 9. Recommended Approval Sequence

Approve in this order to build confidence progressively from cleanest to most complex.

| Order | File | Why this position | Estimated time |
|---|---|---|---|
| 1 | W1S3-003 — Supplier Payments | Cleanest file in the set; no open decisions; core commercial capability | 10 min |
| 2 | W1S3-004 — Payroll Payments | Clean; contains the critical Acumatica payroll exclusion rule — confirm it is correctly stated | 10 min |
| 3 | W1S3-007 — Security | Clean; confirm POPIA statement before moving to more complex files | 15 min |
| 4 | W1S3-002 — H2H Core | Core capability file; confirm bank list and approval framework; triggers AI_CONTEXT.md banking partner update | 15 min |
| 5 | W1S3-010 — Monitoring | Mostly clean; resolve D6 (remove wording note); verify AI-authored monitoring table | 15 min |
| 6 | W1S3-001 — Product Overview | Module portfolio overview; resolve D1 (SAP entry) | 15 min |
| 7 | W1S3-008 — Architecture | Architecture diagram verification; most visual file; review after context established from earlier files | 20 min |
| 8 | W1S3-006 — ERP Integration | Most AI-authored content; resolve D2 (SAP section) and D5 (ACH); read Oracle Fusion and Acumatica sections carefully | 25 min |
| 9 | W1S3-009 — Hosting + Commercial | Commercial terms last; resolve D3 (Connect Direct) and D4 (commercial notes); confirm subscription model | 20 min |

**Total estimated review time: ~2.5 hours**

---

## Approval Actions Checklist (For the BU Lead)

For each file, when approving:

- [ ] Read file in full
- [ ] Confirm no client-specific language remains
- [ ] Confirm all capability claims are accurate and current
- [ ] Confirm any AI-authored sections (Oracle Fusion, Acumatica, SAP sections in W1S3-006; monitoring tables in W1S3-010) are factually correct
- [ ] Resolve any open decisions for that file (Section 4)
- [ ] If edits are needed: provide the edit instruction; extractor applies edit; re-read before approving
- [ ] Set `approved_for_reuse: Yes` in the file's metadata block
- [ ] Change `review_status` from `Review_Required` to `Approved`
- [ ] Remove the `REVIEW REQUIRED — NOT APPROVED FOR TENDER USE` banner
- [ ] Update EXTRACTION_LOG.csv: set review_status = Approved, approved = Yes, reviewer name and date
- [ ] Update DOCUMENT_REGISTER.csv: approved_for_reuse = Yes, kb_path = destination path
- [ ] Copy file to KB destination: `07_Approved_Content/Approved/BeBanking/`
- [ ] Update AI_CONTEXT.md "Approved Content Available" section to list the newly approved file
- [ ] When W1S3-002 is approved: also update AI_CONTEXT.md banking partner rule

---

*This pack was prepared by AI (Claude) on 2026-06-10. All capability claims and wording recommendations are based on BU lead–confirmed answers (BQ1–BQ13) from the Session C fact baseline session. The approval decision rests with Hein Blignaut as BeBanking BU lead. No content in this pack constitutes approval of any file.*
