# Milestone Checkpoint — Session C Progress
**Date:** 2026-06-10
**Prepared by:** Claude (AI — requires human review)
**Milestone type:** Progress checkpoint at end of Session C Batch 1 remediation
**Related documents:** SESSION_C_FACT_BASELINE.md | SESSION_C_IMPACT_ANALYSIS.md | SESSION_C_APPROVAL_PLAN.md | SESSION_A_CLOSEOUT.md

---

## 1. Repository Statistics

### Extraction Pipeline — Wave 1 (28 registered candidates)

| Stage | Count | Files |
|---|---|---|
| Approved | **9** | W1S1-001 through W1S1-009 (Session A — all Cross-BU/Oracle/Acumatica/BeBanking profile files) |
| Review_Required | **3** | W1S3-003 (Supplier Payments), W1S3-004 (Payroll Payments), W1S3-007 (Security) |
| Candidate — not yet reviewed | **16** | W1S2-001 to W1S2-009 (Acumatica, 9 files); W1S3-001, 002, 005, 006, 008, 009, 010 (BeBanking, 7 files) |
| Archived (superseded DRAFTs) | **6** | W1S1-001, W1S1-004, W1S1-005, W1S1-007, W1S1-008, W1S1-009 Candidate DRAFTs in `_Archived_Superseded/` |
| **Total extraction candidates** | **28** | — |

### Broader Document Register

| Register type | Count | Notes |
|---|---|---|
| Approved KB extracts (extraction pipeline) | 9 | Wave 1, Session A |
| Active proposal templates (TMPL) | 3 | Oracle Fusion, Oracle EBS, Acumatica Sept 2025 |
| Historical tenders (HIST) | 5 | HIST-001 to HIST-005 |
| Compliance examples (COMP) | 2 | — |
| Reference letters (REF) | 3 | Example entries — active letters not yet migrated |
| Certification records (CERT) | 2 | Example entries |
| Methodology records (METH) | 1 | Example entry |
| **Total registered assets** | **25** | Excludes archived DRAFTs and governance files |

### By Business Unit — Extraction Pipeline

| Business Unit | Approved | Review_Required | Candidate | Total |
|---|---|---|---|---|
| Cross_BU | 6 | 0 | 0 | 6 |
| Oracle | 1 | 0 | 0 | 1 |
| Acumatica | 1 | 0 | 9 | 10 |
| BeBanking | 1 | 3 | 7 | 11 |
| **Total** | **9** | **3** | **16** | **28** |

---

## 2. Approved Content by Business Unit

All approved files located at `07_Approved_Content/Approved/Cross_BU/`. Approved by Hein Blignaut on 2026-06-09. All carry `approved_for_reuse: Yes`.

### Cross-BU (6 files)

| File | Type | Content covered | Restrictions |
|---|---|---|---|
| W1S1-001-CORP-CompanyOverview.md | CORP | Company intro; 23+ years; 50+ consultants; sub-Saharan + international; 18 industries | None |
| W1S1-002-CORP-CompanyHistory.md | CORP | Founder background; geographic expansion; Oracle partnership history; awards | None |
| W1S1-006-CORP-AwardsRecognition.md | CAP | 6 Oracle awards 2015–2024 (award table unrestricted); success story references | Success stories (Tiger Brands, USAID, UT Grain): URL verification required before citing |
| W1S1-007-CORP-DeliveryModel.md | CAP | 8 service lines; Oracle Level 1 Partner; DBA team; Monthly Recurring Invoice Model | None |
| W1S1-008-CORP-GeographicPresence.md | CORP | 5 sub-Saharan markets; 4 international countries; industries by geography | None |
| W1S1-009-CORP-KeyDifferentiators.md | CAP | 7 differentiators; Hybrid Support Model; Continuous Improvement Model; 3 costing models | None |

### Oracle (1 file)

| File | Type | Content covered | Restrictions |
|---|---|---|---|
| W1S1-003-ORA-OraclePartnership.md | CAP | Oracle Level 1 Partner; 5 expertise areas; Oracle VAR; 6 awards 2015–2024 | Annual revalidation: confirm Cloud Excellence Implementer and Linux Specialist status via OPN before each major tender cycle |

### Acumatica (1 file)

| File | Type | Content covered | Restrictions |
|---|---|---|---|
| W1S1-004-ACU-AcumaticaPartnership.md | CAP | Acumatica Gold Partner; Acumatica VAR; delivery experience; industry footprint (Manufacturing, Distribution, FMCG, Professional Services, Higher Education) | None |

### BeBanking (1 file)

| File | Type | Content covered | Restrictions |
|---|---|---|---|
| W1S1-005-BB-BeBankingOverview.md | CAP | BeBanking product description; 7 capabilities; Oracle EBS/Fusion/Acumatica integration; all major SA banks | Bank list: "all major South African banks" — do not replace with specific bank names unless confirmed for that tender |

---

## 3. Major Decisions Made Since Project Inception

### D-STRAT-001 — Extraction-First Strategy
**Date:** 2026-06-08 | **Decision:** The original plan (authoring capability statements from scratch using the Tender Pack as source) was replaced after discovery of the full historical tender corpus. APPSolve's 315-client, 18,400-file, 2012–2026 corpus is the primary IP source. Content is extracted, modernised, and approved — not authored from scratch. Authoring from scratch is reserved for confirmed gaps with no source material.

**Standing rule:** `CONTENT_GAP_ANALYSIS.md` (built on 3 Tender Pack proposals) is unreliable — do not use until revised post-Wave 3. The TMPL document type was introduced as a 9th document type to represent active reusable proposal templates.

### D-STRAT-002 — Read-Only Source Repository Rule
**Date:** 2026-06-08 | **Decision:** All files under `Parties/Customers/` and `Tender Pack/` are permanently read-only. No file may be moved, copied, renamed, or modified. Content is extracted by reading — not by copying or moving files. Every extracted file must record `source_path` pointing to the original.

### D-STRAT-003 — Three-Stage Approved Content Pipeline
**Date:** 2026-06-08 | **Decision:** All content passes through three mandatory stages before it can be cited in a tender: Candidate_Content/ → Review_Required/ → Approved/. `approved_for_reuse: Yes` may only be set by the BU lead reviewer — never by the extractor or AI. No shortcuts. No direct path from source to KB.

### D-FACT-001 — Oracle Level 1 Partner Correction
**Date:** 2026-06-09 | **Decision:** September 2024 proposal templates stated "Gold Level partnership" and "Gold Certified." Oracle Gold Membership expired August 2021 (evidenced by `EXPIRED_APPSolve_OPN_202108.pdf`). Corrected across all Session A files to "Oracle Level 1 Partner" with 5 published expertise areas. Annual OPN revalidation required.

**Permanent rule:** Do not cite "Gold Partner" or "Gold Level" for Oracle. Confirmed designation is Oracle Level 1 Partner.

### D-FACT-002 — Headcount Correction (110+ → 50+)
**Date:** 2026-06-09 | **Decision:** September 2024 templates stated "110+" and "over 100 Senior Consultants." The 2023 Columbus Consulting company profile stated "50+ Senior Consultants." Confirmed by Hein Blignaut as 50+. Corrected across all Session A files.

**Permanent rule:** Use "more than 50 Senior Consultants." Do not use 100+ or 110+.

### D-FACT-003 — Geography Correction
**Date:** 2026-06-09 | **Decision:** Nigeria, Uganda, Bangladesh, Qatar, and Ghana were cited as active markets across multiple template generations. Zero client folder evidence found for any of these five countries across 18,400 files. All five removed from all approved content.

**Permanent rule:** Sub-Saharan presence: Botswana, Zambia, Mozambique, Namibia, Tanzania. International: USA, France, Abu Dhabi, Pakistan. Do not cite Nigeria, Uganda, Bangladesh, Qatar, or Ghana.

### D-FACT-004 — BeBanking SAP (Session A removal → Session C BU confirmation)
**Date (removal):** 2026-06-09 | **Date (confirmed):** 2026-06-10 | **Decision:** Session A correctly removed the SAP integration claim from W1S1-005 — zero BeBanking corpus references across 18,400 files. The claim was an inference from a Columbus Consulting JV agreement. Session C BU lead confirmation (2026-06-10) established that SAP integration is a current product capability — a product evolution post-2017, not a Session A error.

**Standing resolution:** Session A approved content (W1S1-005) states Oracle EBS, Oracle Fusion Applications, and Acumatica — this remains correct for Session A purposes and is not reopened. SAP is reflected in Session C content (W1S3-001, W1S3-006) and flagged in W1S1-005 for future enhancement. Use "integrated with" — do not describe as "certified by."

### D-FACT-005 — Acumatica Payroll Clarification
**Date:** 2026-06-10 | **Decision:** An AI inference error introduced Acumatica payroll language into W1S3-004 during Session C Batch 1 remediation. Corrected and a permanent rule established.

**Permanent rule:** Acumatica does not provide payroll functionality in the South African market. BeBanking Payroll H2H is supported from Oracle EBS and Oracle Fusion Applications payroll sources only. Do not imply Acumatica payroll integration, payroll payment generation, or payroll workflows in any BeBanking content. Support for an ERP platform does not imply support for every module within that ERP.

### D-PROD-001 — BeBanking API-First Architecture (Connect Direct obsolete)
**Date:** 2026-06-10 (BQ1 confirmed) | **Decision:** Connect Direct is no longer used. Current architecture: API-first (preferred); SFTP over SSH for banks without API endpoints. Secure File Transfer as a standalone module has been retired — the API layer now provides secure transmission natively. All Session C files must reflect the API/SFTP model.

### D-PROD-002 — Flexible Approval Framework (AP/PAY Level 1/2 obsolete)
**Date:** 2026-06-10 (BQ2 confirmed) | **Decision:** The AP Level 1 / AP Level 2 / PAY Level 1 / PAY Level 2 approval model is obsolete. Current model: flexible approval framework — unlimited levels, first-responder wins or voting-based, configurable segregation-of-duty controls per client.

### D-PROD-003 — BeBanking Module Portfolio Update (BQ7)
**Date:** 2026-06-10 | **Decision:** The December 2024 module list in W1S3-001 had two retired modules and two new modules.

| Change | Module |
|---|---|
| Retired | Secure File Transfer |
| Retired | Automated Receipt Creation |
| Added | ABSA Proof of Payment Integration (ABSA-specific) |
| Added | International and Forex Payment Processing |

Net module count: 9 (unchanged).

### D-PROD-004 — BeBanking Commercial Model (Subscription Only)
**Date:** 2026-06-10 (BQ9 confirmed) | **Decision:** The historical Service Option / Software Option two-model licensing structure is obsolete. Current model: Monthly subscription and Annual subscription only. No once-off licence. All W1S3-009 commercial content must be rewritten.

### D-PROD-005 — BeBanking CMA and International Positioning
**Date:** 2026-06-10 (BQ4 + BQ7 confirmed) | **Decision:** BeBanking is deployed across the Common Monetary Area (South Africa, Namibia, Lesotho, Eswatini) and internationally (Citi Bank UK, Santander Bank Chile). Remove "South African banking infrastructure" framing from all Session C content. Use CMA and international framing.

---

## 4. Lessons Learned Register

### Session A Lessons (closed 2026-06-09)

**L1 — Stale templates are the primary risk vector**
September 2024 templates contained three critical errors uncorrected for years: Gold Partner claim, headcount inflation, and unsubstantiated geographies. Template vintage must be noted at extraction. Facts relying on external status (partner tier, certifications, headcount, awards) must be re-validated at each major approval cycle.

**L2 — AI extractors can make plausible-but-wrong inferences**
The SAP claim was added by inference from context (JV partner agreement). Logical inference is not sufficient — every capability claim must have a confirmed source document. "The extractor found it" is not sufficient.

**L3 — Separating facts from framing enables faster approval**
Distinguishing verifiable facts (headcount, partner tier, geography) from framing language (superlatives, promotional claims) makes review more efficient. Review workbooks should maintain two lanes: "Fact — evidence required" and "Framing — editorial decision."

**L4 — URL-dependent content is not a binary blocker**
Separating confirmed-standing content (award table) from URL-dependent content (success story references) in W1S1-006 allowed the award table to be approved unrestricted while success stories remain pending verification. Apply at extraction time.

**L5 — Annual review notes should be written at approval time**
Write annual revalidation notes at the moment evidence gaps are identified — not retroactively. Every file citing time-sensitive credentials must include an explicit annual review note specifying what to check, where, and what change requires re-approval.

**L6 — Client-specific language can be removed without losing value**
Client names in generic capability sections add compliance risk without adding tender value. Default to genericisation (e.g. "Tier 1 telecommunications operators" instead of "MTN") unless a specific name adds unique evidential value.

**L7 — The two-track validation model worked**
AI corpus-based research (geography search, SAP corpus search) combined with human confirmation (awards, partner tier, headcount) is efficient and reliable. Prepare a "Hein to confirm" list at the start of each session to batch confirmations.

**L8 — Session A revealed the full cost of template drift**
Three separate errors had accumulated in templates used across dozens of real tenders between 2021 and 2024. Every new extraction from a template source should begin with a "drift audit" — how old is this content, and which facts could have changed?

### Session C Lessons (in progress)

**L-C-001 — Do not infer functional capability from ERP integration scope (2026-06-10)**
During Session C Batch 1 remediation of W1S3-004, the AI inferred that BeBanking supports Acumatica payroll because BeBanking integrates with Acumatica (confirmed for local payments, forex, bank statements). This inference was incorrect — Acumatica does not provide payroll functionality in South Africa. The error was caught by the BU reviewer before any file was approved.

**Root cause:** BQ5 (Acumatica integration scope) was applied too broadly, without explicit confirmation of payroll-specific capability. ERP integration scope was conflated with full ERP module support.

**Permanent rule established:** Functional capability requires explicit evidence. Support for an ERP platform does not imply support for every module within that ERP. Encode known module exclusions explicitly rather than inferring from integration scope.

**Encoded in:** AI_CONTEXT.md, PROJECT.md, memory/project_context.md, SESSION_C_FACT_BASELINE.md (F-C-05 clarifying note).

---

## 5. Current Approved Fact Baseline

Facts confirmed through external confirmation by Hein Blignaut and corpus research across 18,400 files (2026-06-09) and BeBanking BU lead responses (2026-06-10). Safe for tender use in the contexts noted.

### Corporate / Cross-BU

| Fact | Confirmed value | Use in tenders |
|---|---|---|
| Founded | 2002 — "over 23 years" or "established in 2002" | Any |
| Headcount | "more than 50 Senior Consultants, each with 10+ years' experience" | Any |
| Sub-Saharan presence | Active and recent client engagements in Botswana, Zambia, Mozambique, Namibia, Tanzania | Any |
| International delivery | USA, France, Abu Dhabi, Pakistan | Any |
| Do not cite | Nigeria, Uganda, Bangladesh, Qatar, Ghana | — |
| DBA team | "one of the largest locally based Oracle Applications DBA teams in South Africa" | Oracle tenders |
| Founder IT career | Started at MTN in 1996 — approximately 30 years' IT experience as of 2026 | Corporate narrative |
| Industries served | 18 industries (from W1S1-001) | Any |

### Oracle

| Fact | Confirmed value | Use in tenders |
|---|---|---|
| Partner tier | Oracle Level 1 Partner | Oracle tenders |
| Oracle Gold | Expired August 2021 — do not cite | — |
| Expertise (5 areas) | Fusion Cloud Financials; Fusion Cloud HCM Core; Oracle Integration; EBS Migration to OCI; OCI Migration | Oracle Cloud tenders |
| Reseller status | Authorised Oracle Value-Added Reseller | Oracle tenders |
| Awards | Business Impact Award EMEA 2024; Business Impact Award ECEMEA 2024 | Any |
| Full awards list | 6 Oracle awards 2015–2024 (W1S1-006) | Any |
| Annual revalidation | Check Cloud Excellence Implementer and Linux Specialist via OPN before each major cycle | — |

### Acumatica

| Fact | Confirmed value | Use in tenders |
|---|---|---|
| Partner tier | Acumatica Gold Partner | Acumatica tenders |
| Do not cite | "Gold Certified" | — |
| Reseller status | Authorised Acumatica Value-Added Reseller | Acumatica tenders |
| Industries | Manufacturing, Distribution, FMCG, Professional Services, Higher Education | Acumatica tenders |
| Payroll (SA market) | **Acumatica does not provide payroll functionality in South Africa** | Critical — do not claim |

### BeBanking — Session A Baseline (from W1S1-005)

| Fact | Confirmed value | Notes |
|---|---|---|
| ERP integration | Oracle EBS (R11/R12), Oracle Fusion Applications, Acumatica | W1S1-005 approved |
| Banking partners | "all major South African banks" | Use this phrase; do not list specific banks in Session A content |
| Core capabilities (7) | Supplier H2H Payments; Payroll H2H; AVS; Automated Bank Statements; Automated Exchange Rates; Supplier PDF Remittances; Monitoring and Automation | W1S1-005 approved |
| SAP (W1S1-005) | Not cited — Session A removed due to zero corpus evidence | W1S1-005 NOT reopened |

### BeBanking — Session C Baseline (BU lead confirmed 2026-06-10, pending full approval)

*These facts are confirmed by BU lead but not yet in Approved content. Use to inform Session C edits — do not cite from Candidate or Review_Required files in tenders.*

| Fact | Confirmed value |
|---|---|
| SAP | Confirmed current integration capability (product evolution post-2017) |
| Banking integrations (9) | ABSA, Nedbank SA, Nedbank Namibia, FNB, Standard Bank SA, Standard Bank Namibia, Investec, Citi Bank UK, Santander Bank Chile — use "integrated with" |
| Connectivity | API-first; SFTP over SSH for banks without API endpoints; Connect Direct obsolete |
| Approval framework | Flexible — unlimited levels, first-responder or voting-based, configurable SOD; AP/PAY Level 1/2 obsolete |
| Acumatica scope | Payments, Cash Management; local payments, forex payments, bank statements — **not payroll** |
| Forex capability | Full — SWIFT processing, international payments, exchange rate management |
| Module name | "International and Forex Payment Processing" (confirmed module name) |
| Current modules (9) | Unbreakable Bank Statements; AVS; Supplier Bank Account Approval; Supplier H2H Payments and Approval; Payroll H2H Payments and Approval; Automated Exchange Rates; Supplier PDF Remittances; ABSA Proof of Payment Integration; International and Forex Payment Processing |
| Retired modules | Secure File Transfer; Automated Receipt Creation |
| Commercial model | Monthly subscription or Annual subscription — no once-off licence |
| POPIA | BeBanking is POPIA compliant |
| GDPR | Roadmap / future-state only |
| Geographic scope | CMA (South Africa, Namibia, Lesotho, Eswatini) and international |

---

## 6. Outstanding Risks

### Approval Pipeline Risks

| Risk | Files affected | Severity | Path to resolution |
|---|---|---|---|
| W1S3-003, 004, 007 in Review_Required — not yet approved | Cannot cite these files in tenders | Low — files are ready for BU review | Hein Blignaut reviews three files in `Review_Required/BeBanking/` |
| W1S3-005 requires content authoring | Forex/International Payments file has no approved source text | Medium — authoring well-defined | Author from SESSION_C_FACT_BASELINE.md F-C-06, F-C-12 |
| Session C Batch 2–4 not yet remediated | W1S3-001, 002, 006, 008, 009, 010 still in Candidate | Medium — all edits defined in approval plan | Complete remaining remediation batches per SESSION_C_APPROVAL_PLAN.md |

### URL Verification Risk

| Item | File | Severity | Path to resolution |
|---|---|---|---|
| Tiger Brands success story URL | W1S1-006 | Medium — applies to success story section only; award table is unrestricted | Verify published URL before citing in live tenders |
| USAID Southern Africa success story URL | W1S1-006 | Medium — same as above | Verify published URL |
| UT Grain success story URL | W1S1-006 | Medium — same as above | Verify published URL |

**Note:** These do not block tender use of W1S1-006 for the award table or general awards narrative. They only restrict citing the specific success story references.

### Compliance Deadline Risk

| Item | Deadline | Days remaining | Severity | Action |
|---|---|---|---|---|
| BEE certificate renewal | 2026-07-31 | ~51 days | **High — hard deadline** | Initiate renewal process immediately. Cannot cite BEE certificate in tenders after expiry. |

### Reference Letter Gaps

| Gap | Impact | Path to resolution |
|---|---|---|
| Oracle reference letters — ATC, Old Mutual, Truworths | Cannot cite specific Oracle client references | Chase clients for signed letters |
| Acumatica reference letters — 10 clients with unsigned templates | Cannot cite specific Acumatica client references | Chase outstanding signatures |

### Session C Open BU Questions (non-blocking)

| Item | Description | Files affected |
|---|---|---|
| BQ-WEB-01 | "R6 billion transactions/month" statistic — authorised for tender use? | W1S3-001 |
| BQ-WEB-02 | Disaster Recovery — named module or hosting-level feature? | W1S3-008, W1S3-009 |
| BQ-WEB-03 | Sage ERP integration scope | W1S3-001, W1S3-006 |
| BQ-WEB-04 | SAP integration architecture detail | W1S3-006 (SAP section only) |
| CORP-01 | Corporate relationship between appsolve.co.za and appsolvegroup.com | Future corporate review |

**None of the above block any Session C approval.** They are enhancement questions for a future BU lead touchpoint.

---

## 7. Recommended Next Sequence

Ranked by business value — activities that unlock the most tender response capability fastest.

| Rank | Activity | Business value | Effort | Unlocks |
|---|---|---|---|---|
| 1 | **Hein Blignaut reviews W1S3-003, 004, 007** (Review_Required) | Immediate — these are ready for sign-off | 30–60 min human review | First three BeBanking H2H capability files in Approved pool |
| 2 | **Renew BEE certificate** | Hard deadline 2026-07-31 (~51 days). Cannot wait. | External action — initiate now | Continued compliance eligibility for all tenders |
| 3 | **Session C Batch 2** — W1S3-009 (Hosting), W1S3-001 (Product Overview), W1S3-002 (H2H Core) | Completes core BeBanking product narrative | 3–4 hours AI remediation | BeBanking commercial model, product overview, and H2H architecture |
| 4 | **Session C Batch 3** — W1S3-010 (Monitoring), W1S3-008 (Architecture), W1S3-006 (ERP Integration) | Technical depth content | 4–5 hours AI remediation | Full technical BeBanking stack |
| 5 | **Session C Batch 4** — W1S3-005 (International and Forex Payment Processing) | Content authoring — sole file requiring authoring | 90–120 min AI authoring | International payments capability statement |
| 6 | **Copy Session A approved files to KB destinations** | Completes Session A pipeline to final KB folders | 30 min | Proper KB taxonomy — files accessible in `06_Capabilities/` etc. |
| 7 | **Session B — Acumatica module library review** (W1S2-001 through W1S2-009) | 6 of 9 files are DIRECT — fast review cycle | 2–4 hours | Full Acumatica module coverage for module-specific tenders |
| 8 | **Wave 2 extraction — Oracle DBA Executive Summary** | Single high-value extraction from HIST-002 MTN 2014 | 30 min | Standalone Oracle DBA managed services positioning document |
| 9 | **Wave 2 extraction — Oracle Fusion Capability Statement** | Bridges critical Oracle Cloud content gap (C1) | 1 hour | Oracle Cloud tender responses |
| 10 | **URL verification — W1S1-006 success stories** | Tiger Brands, USAID, UT Grain — verify before live use | 30 min | Unlocks success story references for tender citation |
| 11 | **Reference letter chase** — Oracle (ATC, Old Mutual, Truworths); Acumatica (10 unsigned) | Strong tender differentiator; no letters currently in KB | External action | Verifiable client references for tenders |
| 12 | **BU lead touchpoint — BQ-WEB items** | Enhancement confirmations (R6bn stat, SAP architecture, Sage, DR scope) | 30 min meeting | Enriches Session C content; non-blocking |

---

*This milestone document is a point-in-time snapshot as at 2026-06-10. For current pipeline status, see `HANDOVER.md` and `00_Governance/KNOWLEDGE_BASE_STATUS.md`. For Session C detail, see `SESSION_C_APPROVAL_PLAN.md` and `SESSION_C_FACT_BASELINE.md`.*
