# Session A — Formal Closeout
**Session:** Wave 1, Session A — Company Profile Master (W1S1-001 through W1S1-009)
**Closed:** 2026-06-09
**Approved by:** Hein Blignaut
**Prepared by:** Claude (AI extraction and analysis)

---

## Summary

| Metric | Value |
|---|---|
| Files in scope | 9 |
| Files approved | 9 |
| Files rejected | 0 |
| Files returned to Candidate | 0 |
| Factual corrections applied | 6 |
| Major risks removed | 5 |
| Approval decisions (D1–D6) | 6 |
| Candidate DRAFTs archived | 6 |

All 9 Session A files are now in `07_Approved_Content/Approved/Cross_BU/`. Six superseded Candidate DRAFT files (W1S1-001, 004, 005, 007, 008, 009) have been archived to `07_Approved_Content/Candidate_Content/_Archived_Superseded/`. Three Candidate DRAFT files (W1S1-002, 003, 006) were deleted upon direct promotion to Approved.

For detailed approval decisions and the validated fact baseline, see `00_Governance/APPROVAL_SUMMARY_WAVE1.md`.

---

## Assets Approved

| File | Type | Content | Primary Tender Use |
|---|---|---|---|
| W1S1-001 Company Overview | CORP | 23-year history; 50+ consultants; sub-Saharan + international; 18 industries | Generic company introduction for any tender |
| W1S1-002 Company History | CORP | Founder background; geographic expansion; Oracle partnership history; awards | Corporate narrative; about us; company background |
| W1S1-003 Oracle Partnership | CAP | Oracle Level 1 Partner; 5 expertise areas; VAR; 6 awards 2015–2024; Oracle Backed | Oracle tender credentials section |
| W1S1-004 Acumatica Partnership | CAP | Acumatica Gold Partner; VAR; industries | Acumatica tender credentials section |
| W1S1-005 BeBanking Overview | CAP | 7 capabilities; Oracle EBS/Fusion/Acumatica integration; all major SA banks | BeBanking product description in any tender |
| W1S1-006 Awards and Recognition | CAP | 6 Oracle awards 2015–2024 (award table unrestricted); success story references (URL verification required) | Awards section; credentials; company track record |
| W1S1-007 Delivery Model | CAP | 8 service lines; DBA team; MRI Model; Oracle Level 1 Partner | Delivery approach; service line descriptions |
| W1S1-008 Geographic Presence | CORP | 5 sub-Saharan markets; 4 international countries; industries by geography | Geographic footprint; market coverage |
| W1S1-009 Key Differentiators | CAP | 7 differentiators; Hybrid Support Model; CIM; 3 costing models | Why APPSolve; competitive differentiation |

---

## Key Factual Corrections Applied

Six factual errors or outdated claims were identified and corrected before any file was approved.

| # | Fact corrected | Template value | Confirmed value | Evidence |
|---|---|---|---|---|
| 1 | Headcount | "110+" and "over 100 Senior Consultants" | "50+ Senior Consultants" | Columbus Consulting 2023 company profile (F2); confirmed Hein Blignaut |
| 2 | Oracle partner tier | "Gold Level partnership" / "Gold Certified" | "Oracle Level 1 Partner" + 5 expertise areas | EXPIRED_APPSolve_OPN_202108.pdf; OPN portal (F3/F4) |
| 3 | Geography | Nigeria, Uganda, Bangladesh, Qatar, Ghana cited as active markets | Sub-Saharan: Botswana, Zambia, Mozambique, Namibia, Tanzania; International: USA, France, Abu Dhabi, Pakistan | 18,400-file corpus: zero client folders for excluded countries; 6+ folders for each confirmed market |
| 4 | SAP BeBanking | "SAP integration capability" extracted into W1S1-005 | No integration — claim removed entirely | Zero BeBanking corpus documents mention SAP; inference traced to Columbus Consulting JV agreement (F10) |
| 5 | Oracle awards | Undated "EMEA/ECEMEA Business Impact Award" | Oracle Business Impact Award 2024 — EMEA and ECEMEA (two separate awards) | Confirmed Hein Blignaut (F7); corroborated by absence from 2023 company profile |
| 6 | Founder bio superlative | "a significant force in the South African Oracle industry" | Removed — remaining sentence factually sufficient | Unverifiable promotional claim; no external evidence |

---

## Major Risks Removed

Five risks were removed from the approved content.

**1. Oracle Gold Partner claim**
Citing an expired Oracle Gold Membership (expired August 2021) in 2024–2026 tender responses is a verifiable misrepresentation. An evaluator or competitor can check the OPN portal. The claim had gone uncorrected for 3+ years across templates. Removed from all 9 files and replaced with confirmed Oracle Level 1 Partner language.

**2. Headcount overstatement**
A 2× overstatement of company size. September 2024 templates stated "110+" and "over 100 Senior Consultants" against a confirmed value of 50+. Overstating company size in a formal tender is a material misrepresentation that could be challenged. Corrected uniformly.

**3. Geography inflation**
Active operations claimed in Nigeria, Uganda, Bangladesh, and Qatar over multiple template generations, with zero client folder evidence across 18,400 files. If an evaluator requested client references for any of these markets, the claim could not be substantiated. All four removed.

**4. Unconfirmed SAP integration**
A capability claim with zero source document evidence. The inference was plausible (APPSolve had a JV partner who was a SAP partner) but factually incorrect. If cited in a BeBanking tender against a SAP shop, the claim could be tested and found false. Removed entirely.

**5. Promotional superlative in founder bio**
"a significant force in the South African Oracle industry" — an unverifiable self-assessment. In a formal tender context it reads as puffery and could undermine credibility with technically sophisticated evaluators. Removed.

---

## Lessons Learned

### L1 — Stale templates are the primary risk vector

The September 2024 Oracle Fusion template contained three critical errors that had gone uncorrected for years: Gold Partner claim (~3 years stale), headcount inflation (2×), and four unsubstantiated geographies. The template continued to be reused without triggering a review. The Tender KB exists specifically to prevent this.

**Implication for future sessions:** Template vintage must be noted at extraction. Any fact that relies on external status (partner tier, certifications, headcount, awards) must be re-validated at each major approval cycle.

### L2 — AI extractors can make plausible-but-wrong inferences

The SAP claim was added by the AI extractor from context inference (JV partner agreement). The inference was logical but the fact was wrong. This is a category of error invisible to readability checks.

**Implication for future sessions:** No capability claim should be approved solely because the extractor included it. Every capability claim must have a confirmed source document. "The extractor found it" is not sufficient.

### L3 — Separating facts from framing enables faster approval

Distinguishing between verifiable facts (headcount, partner tier, geography) and framing language (superlatives, promotional claims) made the review more efficient. Facts required evidence; framing required editorial judgment. Mixing the two would have slowed every decision.

**Implication for future sessions:** Review workbooks should maintain two lanes: "Fact — evidence required" and "Framing — editorial decision."

### L4 — URL-dependent content is not a binary blocker

W1S1-006 (Awards and Recognition) was initially treated as blocked pending URL verification for three success story references. The solution — separating the award table (confirmed, unrestricted) from success story references (URL verification required but not a file-level blocker) — was correct and efficient.

**Implication for future sessions:** Separate confirmed-unrestricted content from URL-dependent content at extraction time. URL verification of secondary content should not block approval of primary content in the same file.

### L5 — Annual review notes should be written at approval time

W1S1-003 required an OPN revalidation note for two credentials. Writing the note at approval time — when the evidence gap is fresh — is more reliable than expecting a future reviewer to rediscover the need.

**Implication for future sessions:** Every file citing time-sensitive credentials, certifications, or partner tiers must include an explicit annual review note at approval time.

### L6 — Client-specific language can be removed without losing value

D2 (MTN removed from W1S1-008) showed that client names in generic capability sections add compliance risk without adding tender value. "Tier 1 telecommunications operators" is equally compelling and risk-free.

**Implication for future sessions:** At extraction, every client name in a generic capability section should be flagged for review. Default to genericisation unless the specific client reference adds unique evidential value.

### L7 — The two-track validation model worked

Splitting fact validation into two tracks — AI corpus-based research (geography search, SAP corpus search) and human confirmation (awards, partner tier, headcount) — was efficient and reliable.

**Implication for future sessions:** Use the same model. Prepare a "Hein to confirm" list for external facts at the start of each session so confirmations can be batched.

### L8 — Session A revealed the full cost of template drift

Three separate errors (Gold Partner, headcount, geography) had accumulated in templates used across dozens of real tenders between 2021 and 2024. The KB approval process is now the control point for all future tender content. The first session's primary value was corrective; future sessions' value will be preventive.

**Implication for future sessions:** Every new extraction from a template source should begin with a "drift audit" — how old is this content, and which facts could have changed since it was last verified?

---

## Recommended Review Standards for Future Sessions

Eight review standards derived from Session A experience. Apply to Sessions B, C, and all subsequent review cycles.

### Standard 1 — Source document currency check
Every extracted file must state the source document vintage in its metadata. If the source is more than 2 years old, apply MODERNISE readiness regardless of content stability. If more than 5 years old, apply a "Significant MODERNISE" flag and require BU lead confirmation before the file advances to Review_Required.

### Standard 2 — External claim verification protocol
The following claim types require confirmed external sources before approval — template reuse alone is not sufficient:
- Partner tier (Oracle, Acumatica, Microsoft, SAP, etc.)
- Certifications and awards (year, level, region)
- Headcount and team size
- Geographic operations (must have client folder evidence or direct confirmation)
- Capability claims (must have source proposal, live client evidence, or BU lead confirmation)

### Standard 3 — Client-specific language checklist
Before any file advances from Candidate to Review_Required, check for:
- Named clients (review disclosure obligations; default to generic description)
- Named individuals (check if public-facing or internal-only contact)
- Named projects or tenders (remove unless used as a confirmed public reference)
- Named competitors (remove)
- Pricing (never extract — commercially sensitive)

### Standard 4 — Framing and superlative audit
Flag any sentence containing: "unique", "only", "largest", "best", "leading", "significant force", "industry-leading", "world-class". Each must be either:
(a) Supported by a cited source; or
(b) Softened to a defensible formulation ("distinctive", "among the largest", "recognised")

### Standard 5 — Approved content consistency check
Before approving a new file, verify it does not contradict any existing approved file. Check against:
- The Validated Fact Baseline (`FACT_RESOLUTION_REPORT.md`)
- All previously approved files in the same content area
- ERP integration claims — must align with W1S1-005 (Oracle EBS, Oracle Fusion Applications, Acumatica)

### Standard 6 — BU lead confirmation scope
Define the BU lead's required sign-offs at the start of each session. For BeBanking sessions: BU lead must confirm bank partnerships, product currency, Acumatica integration model, and hosting model before any file citing these facts advances. Do not approve files containing unconfirmed BU-specific content.

### Standard 7 — URL-dependent content separation
At extraction time, separate confirmed-and-standing content (partnerships, awards, capabilities) from URL-dependent content (case studies, success stories, published references). Use distinct section headers so each section can be independently approved.

### Standard 8 — Annual review note placement
Every file citing time-sensitive credentials must include an annual review note in the file's Review notes section, specifying: what needs re-checking, where to check it, and what change would require re-approval.

---

*This closeout record supplements `00_Governance/APPROVAL_SUMMARY_WAVE1.md` (approval decisions D1–D6 and fact baseline) and `00_Governance/FACT_RESOLUTION_REPORT.md` (full fact validation record).*
