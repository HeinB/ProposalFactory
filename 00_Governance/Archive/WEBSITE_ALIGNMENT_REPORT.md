# Website Alignment Report
**Prepared:** 2026-06-10
**Prepared by:** Claude (AI analysis — requires human review)
**Purpose:** Validation and enrichment review against current APPSolve websites. Websites are not authoritative sources. Repository hierarchy applies: Approved Content > Validated Repository Evidence > Current Website Content > Historical Tender Content > AI-generated Content.
**Status:** For review only. No repository files have been modified.

---

## Sources Reviewed

| URL | Description | Content quality |
|---|---|---|
| https://appsolve.co.za | Corporate home page | Sparse — service lines, two client quotes, product names only |
| https://appsolvegroup.com | UK entity — Oracle specialists | Moderate — service lines, UK focus, headcount claim |
| https://oracle.appsolve.co.za | Oracle-specific site | Good — service lines, awards, capabilities |
| https://acumatica.appsolve.co.za | Acumatica-specific site | Good — modules, industries, integrations |
| https://bebanking.appsolve.co.za | BeBanking product site | High value — modules, banks, ERP platforms, stats |

---

## Critical Alert

> **WB-CRITICAL-001 — SAP listed as BeBanking ERP platform**
>
> bebanking.appsolve.co.za displays "Sage, Acumatica, Oracle, SAP" as ERP platform icons. This directly conflicts with the approved W1S1-005 (BeBanking Overview), which explicitly removed the SAP claim during Session A fact validation (Decision D1 / Fact F10). The SAP removal was based on zero corpus evidence across 18,400 files. The website now publicly asserts SAP integration. This finding must be reviewed by Hein Blignaut before Session C proceeds — it may represent a product capability added since 2017, or an unsupported marketing claim that needs to be corrected on the website.

---

## Findings by Classification

---

### CONFIRMED

Findings that align with approved repository content, validating existing claims.

| # | Finding | Website | Repository match | Notes |
|---|---|---|---|---|
| WB-C-001 | 2024 Oracle Business Impact Award — EMEA | oracle.appsolve.co.za | W1S1-003, W1S1-006 | Award confirmed on website. Note: website mentions EMEA only; repository records both EMEA and ECEMEA. See WB-MI-010 for ECEMEA. |
| WB-C-002 | Oracle partnership status | oracle.appsolve.co.za | W1S1-003 | Oracle partner status confirmed. Partner tier (Level 1) not stated on website but partnership confirmed. |
| WB-C-003 | Oracle Cloud Services — Financials, HCM, Integration | oracle.appsolve.co.za | W1S1-003 (5 expertise areas include Fusion Cloud Financials, Fusion Cloud HCM Core, Oracle Integration) | Three of the five OPN expertise areas confirmed on website. |
| WB-C-004 | Oracle EBS as a distinct service line | oracle.appsolve.co.za | W1S1-007 (Delivery Model), W1S1-003 (EBS Migration to OCI) | Website lists "Oracle E-Business Suite Services" separately from Cloud Services. |
| WB-C-005 | Oracle DBA capability | oracle.appsolve.co.za | W1S1-007 ("APPS DBA / Developer / Functional / BA / PM capability" matches W1S1-007's DBA team description) | Confirms the DBA capability is still publicly positioned. |
| WB-C-006 | Oracle Value-Added Reseller — License sales | oracle.appsolve.co.za | W1S1-003 (Oracle VAR) | "Oracle License & Cloud Subscription Sales" listed as a service line. Confirms VAR role. |
| WB-C-007 | Oracle OCI as a service area | oracle.appsolve.co.za | W1S1-003 (OCI Migration expertise area) | Website lists "Oracle OCI Administration & DevOps" and "Oracle Cloud Infrastructure Services." Confirms OCI capability. |
| WB-C-008 | Acumatica as a partner | appsolve.co.za, acumatica.appsolve.co.za | W1S1-004 | Acumatica prominently featured on both sites. |
| WB-C-009 | Acumatica Financial Management module | acumatica.appsolve.co.za | W1S2-001 | Confirmed as listed module. |
| WB-C-010 | Acumatica Distribution module | acumatica.appsolve.co.za | W1S2-002 | Confirmed as listed module. |
| WB-C-011 | Acumatica Manufacturing module | acumatica.appsolve.co.za | W1S2-004 | Confirmed as listed module. |
| WB-C-012 | Acumatica CRM module | acumatica.appsolve.co.za | W1S2-005 | Confirmed as listed module. |
| WB-C-013 | Acumatica Project Accounting module | acumatica.appsolve.co.za | W1S2-009 | Confirmed as listed module. |
| WB-C-014 | Acumatica Construction module | acumatica.appsolve.co.za | W1S2-008 | Confirmed as available module. Note: W1S2-008 is STRUCTURE ONLY (content gap) — website confirms the product exists and is sold. |
| WB-C-015 | Acumatica cloud + on-premises deployment | acumatica.appsolve.co.za | W1S1-004, W1S2 candidates | "Can run on servers in your private network or in the public cloud." Both deployment models confirmed. |
| WB-C-016 | BeBanking integrates with Acumatica | bebanking.appsolve.co.za, acumatica.appsolve.co.za | W1S1-005 (D1 decision) | BeBanking listed as an integrated product on the Acumatica site; Acumatica listed as supported ERP on BeBanking site. |
| WB-C-017 | BeBanking integrates with Oracle | bebanking.appsolve.co.za | W1S1-005 | Oracle listed as a supported ERP platform on BeBanking site. |
| WB-C-018 | BeBanking — Host-to-Host banking as core capability | bebanking.appsolve.co.za | W1S1-005, W1S3-002 | H2H banking confirmed as the primary BeBanking capability. |
| WB-C-019 | BeBanking — supplier payment automation | bebanking.appsolve.co.za | W1S1-005, W1S3-003 | Payment automation / supplier payments confirmed. |
| WB-C-020 | BeBanking — automated bank statement import | bebanking.appsolve.co.za | W1S3-010 | "Statement Ingestion" confirms W1S3-010's Unbreakable Bank Statements module. |
| WB-C-021 | BeBanking — receipt reconciliation | bebanking.appsolve.co.za | W1S3-010 | "Receipt Reconciliation" confirms W1S3-010's Automated Receipt Creation module. |
| WB-C-022 | BeBanking — role-based approvals and audit trails | bebanking.appsolve.co.za | W1S3-007 | Security & Fraud Prevention section confirms approval workflows and audit trails. |
| WB-C-023 | Standard Bank as a BeBanking banking partner | bebanking.appsolve.co.za | W1S3-002 (Standard Bank cited in 2017 SITA) | Confirmed as still a listed bank. See WB-NI-007 for the full 2026 bank list. |
| WB-C-024 | BeBanking — segregation of duties | bebanking.appsolve.co.za | W1S3-007 | Listed under Security & Fraud Prevention. |
| WB-C-025 | PaySpace as a partner | appsolve.co.za, acumatica.appsolve.co.za | Not in approved content (not a conflict — simply not documented) | PaySpace appears on both sites. Confirms integration exists. |
| WB-C-026 | BeBanking — managed services / support model | bebanking.appsolve.co.za | W1S1-007 (Managed Services service line) | Flexible Pricing & Scalability implies ongoing service model. |

---

### NEW INFORMATION

Findings not currently in the repository that add value or may warrant extraction.

| # | Finding | Website source | Detail | Recommended action | Confidence |
|---|---|---|---|---|---|
| WB-NI-001 | BeBanking transaction volume: R6 billion per month | bebanking.appsolve.co.za | "R6 billion transactions per month" stated as a headline statistic. If accurate, this is a powerful differentiator for BeBanking tenders. | Confirm with BU lead (BQ-WEB-01). If confirmed, add to W1S1-005 and W1S3-001. | Medium — unverified statistic |
| WB-NI-002 | BeBanking — Disaster Recovery module | bebanking.appsolve.co.za | Website lists "Disaster Recovery" as a named capability section with "Business continuity capabilities." This is not documented in W1S3-001's 9-module table or any other W1S3 file. | Add to Session C BU lead questions (BQ-WEB-02). If confirmed, W1S3 architecture/hosting files need a Disaster Recovery section. | Medium — website is current |
| WB-NI-003 | BeBanking — Sage ERP platform | bebanking.appsolve.co.za | "Sage" is listed alongside Acumatica, Oracle, and SAP as a supported ERP platform. Sage is not in the approved repository. | Confirm with BU lead (BQ-WEB-03). If confirmed, this expands the ERP compatibility claim in W1S1-005 and all W1S3 files. Do not update approved content until confirmed. | Medium — but see WB-PC-001 (SAP context makes this harder to assess without BU input) |
| WB-NI-004 | BeBanking — confirmed bank list for 2026 | bebanking.appsolve.co.za | Website lists: Standard Bank, FNB, African Bank, ABSA, Investec, Capitec, Nedbank (7 banks). This directly resolves Session C BQ4 (bank partner list). | Confirm with BU lead that this is the current 2026 list. If confirmed, replace "[UPDATE]" placeholder in W1S3-002 and update the W1S1-005 "all major South African banks" statement with an option to cite the specific list. | High — public website is a strong signal; BU confirmation still required |
| WB-NI-005 | BeBanking — Forex Payments as a distinct module | bebanking.appsolve.co.za | Website lists "Forex Payments" as a named module under Core Features. This is not just Automated Exchange Rates — the framing suggests active international payment processing. This directly addresses Session C BQ11. | Confirm scope with BU lead (BQ11 in Session C Workbook). If confirmed as SWIFT/international payments, W1S3-005 needs significant content expansion beyond current STRUCTURE ONLY placeholder. | High — public website claim; BU must confirm capability depth |
| WB-NI-006 | BeBanking — monitoring: "Live, accurate transaction data 24/7/365" | bebanking.appsolve.co.za | Website claims live 24/7 transaction visibility. This addresses Session C BQ10 (monitoring dashboard). Implies a monitoring capability beyond what was documented in the 2017 SITA source. | Confirm with BU lead. If confirmed, the [UPDATE] placeholder in W1S3-010's monitoring section can be completed. | Medium — general marketing claim; details needed |
| WB-NI-007 | Oracle APEX Development & Support as a service line | oracle.appsolve.co.za | Oracle APEX is listed as a distinct service offering. APEX is Oracle's low-code development platform. This is not mentioned in W1S1-003 (Oracle Partnership) or W1S1-007 (Delivery Model). | Wave 2 extraction: consider adding Oracle APEX to the Delivery Model / Technical Services section. Confirm with Oracle BU lead whether APEX engagements are active in the client base. | High — APEX is a growing Oracle capability; website is current |
| WB-NI-008 | Oracle Analytics / BI Publisher as named tools | oracle.appsolve.co.za | Oracle Analytics and BI Publisher listed. W1S1-007 references "OBIEE" — the legacy business intelligence tool that Oracle Analytics replaced. The website reflects the current tool name. | Recommend updating W1S1-007's Technical Skills list during next review cycle: replace OBIEE reference with "Oracle Analytics Cloud (OAC)" and retain BI Publisher. | Medium — current tool names |
| WB-NI-009 | Oracle — Health Checks & System Reviews as a named service | oracle.appsolve.co.za | "Health Checks & System Reviews" is listed as a distinct Oracle service line. This is not documented in the approved Delivery Model. | Wave 2 extraction: add Health Check service offering to Oracle capability content. High tender value — government and financial sector clients often request service scope descriptions. | High — named service with tender relevance |
| WB-NI-010 | Oracle — SCM listed in Oracle Cloud capabilities | oracle.appsolve.co.za | Website lists Oracle Cloud Services as covering "Financials, SCM, HCM, Integration." SCM (Supply Chain Management) is NOT one of the 5 approved OPN expertise areas. This suggests APPSolve may deliver SCM implementations beyond their published expertise certifications. | Confirm with Oracle BU lead: is SCM an active delivery area? If yes, consider whether to cite as a service offering vs. a registered expertise area (different claims). | Medium — may be a service area rather than certified expertise |
| WB-NI-011 | Acumatica — Service Management module | acumatica.appsolve.co.za | Website lists "Service Management" as a distinct module. W1S2-006 is STRUCTURE ONLY (Field Services — content gap). Service Management may be equivalent to or broader than Field Services. | Session B priority: review acumatica.appsolve.co.za Service Management page for content to fill W1S2-006. The website existence confirms the module is sold. | High — resolves a content gap |
| WB-NI-012 | Acumatica — Retail & eCommerce Management module | acumatica.appsolve.co.za | Website lists "Retail & eCommerce Management" as a module. This is not in the repository's Acumatica module list (W1S2 series does not include a Retail/eCommerce candidate). | Wave 2 action: create extraction candidate for Acumatica Retail & eCommerce. Source content from acumatica.appsolve.co.za and Acumatica partner portal. | Medium — website confirms it is sold; actual APPSolve implementation experience unknown |
| WB-NI-013 | Acumatica — Agriculture & Mining as an industry | acumatica.appsolve.co.za | "Agriculture & Mining" listed as an Acumatica industry. The approved W1S1-004 (Acumatica Partnership) lists industries as Financial Services, Professional Services, Manufacturing, Wholesale Distribution, FMCG, Government. Agriculture is not listed. Note: APPSolve has "APPSolve Agri" product. | Add to W1S1-004 at next review cycle. Confirm with BU lead. | Medium — consistent with APPSolve Agri product existence |
| WB-NI-014 | APPSolve Agri — new product not in repository | appsolve.co.za | "APPSolve Agri" described as a "cloud-based supply chain management system." Not mentioned anywhere in the approved repository. | Wave 2 extraction: add APPSolve Agri as a product. Relevant to Agriculture & Mining industry sectors. | High — distinct proprietary product; competitive differentiator in agriculture tenders |
| WB-NI-015 | APPTime — new product not in repository | appsolve.co.za | "APPTime" described as a "cloud-based back-office system for time capture, contract management, invoicing and much more." Not in repository. | Wave 2 extraction: add APPTime description to the product catalogue. May be relevant to professional services and managed services tenders. | Medium — relevance to tenders depends on use case |
| WB-NI-016 | Velixo listed as an Acumatica integration partner | acumatica.appsolve.co.za | "Velixo" listed as an integrated product alongside BeBanking and PaySpace. Velixo is a reporting tool for Acumatica (Excel-based). Not in the repository. | Flag for Wave 2. If APPSolve implements and supports Velixo, it should be mentioned in the Acumatica module/reporting section. | Low — complementary tool, not a core APPSolve product |
| WB-NI-017 | Acumatica — Dukathole Group as a named reference | acumatica.appsolve.co.za | "Dukathole Group success story" referenced on the Acumatica page. Not in the repository reference assets. | Chase Dukathole Group for a signed reference letter. Add to reference letter chase list alongside existing contacts. | High — named public reference on live website; testimonial/case study extraction priority |
| WB-NI-018 | Mazda Southern Africa as a named client | appsolve.co.za | Mazda Southern Africa (Raj Naidoo, IT Manager) listed with a testimonial. Not in the repository. | Add to reference letter chase list. The testimonial language ("highly skilled resources," "minimising our risks") can be used as a tender reference statement pending formal letter. | High — named client with a named contact publicly listed on the website |
| WB-NI-019 | ARM IT as a named client | appsolve.co.za | ARM IT (Jacobus Loubser) listed with a testimonial. Not in the repository. | Add to reference letter chase list. | Medium — ARM IT is likely a smaller engagement; confirm |
| WB-NI-020 | UK entity — appsolvegroup.com | appsolvegroup.com | appsolvegroup.com presents as a UK-based Oracle entity ("UK-based Oracle specialists delivering Oracle E-Business Suite and Oracle Fusion Cloud services globally"). This entity is not referenced in the approved Geographic Presence (W1S1-008) or any other approved file. This may represent a UK subsidiary, affiliate, or related brand. | Critical: Hein Blignaut to clarify the relationship between APPSolve (ZA) and appsolvegroup.com (UK) before any geography or headcount claims referencing the "group" are made in tenders. See also WB-PC-002. | High — structural finding with tender compliance implications |

---

### POTENTIAL CONFLICTS

Findings that may contradict or complicate approved repository content. Each requires BU lead review before any repository action is taken.

| # | Finding | Website source | Repository source | Conflict description | Recommended action | Confidence |
|---|---|---|---|---|---|---|
| WB-PC-001 | SAP listed as a BeBanking ERP platform | bebanking.appsolve.co.za | W1S1-005 (approved) — SAP removed during Session A, Decision D1 / Fact F10 | The Session A fact validation explicitly removed SAP from BeBanking's ERP list based on zero corpus evidence across 18,400 files. The live website now publicly lists SAP as a supported ERP. This is a direct conflict between approved repository content and the current website. | **Priority review.** Hein Blignaut to confirm: (a) Does BeBanking now support SAP? If yes, the approved W1S1-005 needs to be updated and the Session A decision revisited. (b) If no, the website should be corrected. Do not cite SAP in any tender response until resolved. | High — this is the most significant finding in this review |
| WB-PC-002 | "100+ Oracle professionals across the group" | appsolvegroup.com | Validated Fact Baseline: 50+ senior consultants (F2); confirmed by Hein Blignaut 2026-06-09 | appsolvegroup.com claims "100+ Oracle professionals across the group." The approved repository uses "50+ Senior Consultants." These may refer to different entities (SA entity vs. a combined group), or different counting methods (all Oracle professionals vs. senior consultants only), or the website may be overstating — exactly as the September 2024 templates were doing before correction. The relationship between appsolvegroup.com and appsolve.co.za must be established before this figure can be assessed. | Do not update any approved content until the relationship between the two entities is confirmed (see WB-NI-020). The 50+ figure remains the correct approved value for the SA entity. | High |
| WB-PC-003 | BeBanking module grouping differs from W1S3-001 | bebanking.appsolve.co.za | W1S3-001-BB-ProductOverview-DRAFT.md (9-module table) | The website groups BeBanking capabilities into 9 sections: Host-to-Host Banking, Payment Automation, Statement Ingestion, Receipt Reconciliation, Forex Payments, Security & Fraud Prevention, Data Security Protocols, Disaster Recovery, Access & Approvals. The W1S3-001 candidate uses a different 9-module taxonomy: Secure File Transfer, Unbreakable Bank Statements, AVS, Supplier Bank Account Approval, Supplier H2H Payments, Payroll H2H Payments, Automated Exchange Rates, Supplier PDF Remittances, Automated Receipt Creation. Several website modules have no direct match in W1S3-001 (Disaster Recovery, Data Security Protocols). AVS is in W1S3-001 but not visible in the website's grouping. | Resolve during Session C BU lead review. The BU lead should confirm which taxonomy should be used in tenders: the functional module names (W1S3-001 style) or the website's benefit-oriented groupings. W1S3-001 may need structural alignment with the current website presentation. | Medium — not a factual conflict; a presentation/taxonomy conflict |
| WB-PC-004 | Acumatica Construction module exists (website) vs. STRUCTURE ONLY (W1S2-008) | acumatica.appsolve.co.za | W1S2-008-ACU-Construction-DRAFT.md (STRUCTURE ONLY — gap) | W1S2-008 was marked STRUCTURE ONLY because "Construction Edition not found in reviewed templates." The Acumatica website now confirms it is offered. The content gap was a source document gap, not a product gap. | Session B action: source Construction content from the acumatica.appsolve.co.za page and/or from the Acumatica partner portal. Upgrade W1S2-008 from STRUCTURE ONLY to MODERNISE or DIRECT once content is sourced. | High — the product is confirmed; the content gap is addressable |
| WB-PC-005 | "12+ Years of Oracle E-Business Suite experience" | appsolvegroup.com | Validated Fact Baseline: company founded 2002 = 23+ years; Oracle partnership "over two decades" | The UK entity claims "12+ Years of Oracle EBS experience" — which appears inconsistent with the SA entity's 23-year history and "over two decades" Oracle partnership. This likely means the UK entity was established later than the SA entity (or only the UK team's tenure is counted). | Clarify with Hein Blignaut whether appsolvegroup.com is a newer entity than appsolve.co.za. Do not use the "12+ years" figure in any SA entity tender. The 23-year figure applies to APPSolve South Africa. | Medium — likely a different entity timeline |
| WB-PC-006 | 2024 ECEMEA Award not confirmed on website | oracle.appsolve.co.za | W1S1-003, W1S1-006 (both approved — EMEA and ECEMEA as two separate awards) | The website mentions "2024 Oracle Partner Awards – EMEA Business Impact Category" only. It does not mention the ECEMEA award. The approved repository records two separate 2024 awards (EMEA and ECEMEA). This is a website omission rather than a repository error, but it means the ECEMEA award cannot be validated from the website alone. | The approved repository content for the ECEMEA award was confirmed directly by Hein Blignaut (F7). The website omission does not override that confirmation. However, verify the ECEMEA award is still listed on the OPN portal at next annual review. | Low — website omission; repository confirmation stands |
| WB-PC-007 | Oracle Cloud SCM listed as a service but not an approved OPN expertise area | oracle.appsolve.co.za | W1S1-003 (5 OPN expertise areas: Fusion Cloud Financials, Fusion Cloud HCM Core, Oracle Integration, EBS Migration to OCI, OCI Migration — SCM not listed) | The website presents SCM alongside Financials, HCM, and Integration as Oracle Cloud services. The approved repository does not include SCM as an expertise area. If APPSolve cites SCM expertise in a tender and a client checks the OPN portal, they would not find a registered SCM expertise area. | Do not add SCM to the Oracle expertise areas without OPN portal verification. In tender responses, frame SCM as a service offering rather than a certified expertise area, unless OPN registration is confirmed. Add to Wave 2 review checklist. | Medium |

---

### MARKETING LANGUAGE ONLY

Findings that are promotional framing with no factual claim content requiring repository action.

| # | Statement | Website | Notes |
|---|---|---|---|
| WB-ML-001 | "South Africa's Leading Acumatica ERP Partner: Sales, Implementation, and Support" | acumatica.appsolve.co.za | Superlative claim. Not attributable to a ranking or certification. Do not use verbatim in tenders. The approved W1S1-004 uses "Gold Partner" which is a certified tier — use that. |
| WB-ML-002 | "Automate 98% of your payment processes" | bebanking.appsolve.co.za | Statistic without a cited source or methodology. Do not use without BU confirmation of origin and measurement basis. |
| WB-ML-003 | "100% successful payments rate" | bebanking.appsolve.co.za | Zero-failure claim unlikely to be contractually accurate. Marketing language only. Do not use in tender responses. |
| WB-ML-004 | "We only do Oracle — no diluted, generalised IT consulting" | appsolvegroup.com | UK entity positioning language; does not apply to the SA entity. |
| WB-ML-005 | "Solving business problems making systems work" | appsolve.co.za | Tagline. No tender value. |
| WB-ML-006 | "Trusted by more than 6,500 companies worldwide" | acumatica.appsolve.co.za | Acumatica's global customer count — not APPSolve's client count. Do not attribute to APPSolve. |
| WB-ML-007 | "Two UK leaders personally oversee every engagement" | appsolvegroup.com | Specific to the UK entity. Do not apply to SA entity. |
| WB-ML-008 | "Lower per-transaction costs" | bebanking.appsolve.co.za | Comparative claim without reference point. Marketing language only. |

---

## Alignment Against Repository Assets

### Approved Content — Alignment Summary

| Approved file | Status | Key findings |
|---|---|---|
| W1S1-001 Company Overview | Broadly confirmed | No new material found on corporate home page. APPSolve Agri and APPTime not in repository (WB-NI-014, WB-NI-015). |
| W1S1-002 Company History | Not addressed | No history content found on any website page reviewed. |
| W1S1-003 Oracle Partnership | Confirmed with gaps | EMEA award confirmed. ECEMEA not on website (WB-PC-006). Oracle APEX, Health Checks, SCM are on website but not in approved file (WB-NI-007, WB-NI-009, WB-NI-010, WB-PC-007). OAC/Analytics should update OBIEE reference (WB-NI-008). |
| W1S1-004 Acumatica Partnership | Confirmed with additions | Module list confirmed. Agriculture industry missing from approved file (WB-NI-013). Construction confirmed as available (WB-C-014). "South Africa's Leading" is marketing language (WB-ML-001). |
| W1S1-005 BeBanking Overview | **CRITICAL CONFLICT** | SAP on website (WB-PC-001). Sage on website (WB-NI-003). Bank list now available (WB-NI-004). R6bn statistic (WB-NI-001). ERP compatibility needs BU review. |
| W1S1-006 Awards and Recognition | Confirmed | EMEA award confirmed. ECEMEA website omission noted (WB-PC-006). |
| W1S1-007 Delivery Model | Confirmed with gaps | Oracle APEX, Health Checks, OAC not in Delivery Model. OBIEE reference should be updated (WB-NI-008). APPSolve Agri and APPTime as custom development examples (WB-NI-014, WB-NI-015). |
| W1S1-008 Geographic Presence | **New finding** | UK entity (appsolvegroup.com) not referenced in approved geography (WB-NI-020). Must be resolved before geographic claims in tenders. |
| W1S1-009 Key Differentiators | Not addressed | No conflicting content found. R6bn BeBanking stat could enrich this file if confirmed (WB-NI-001). |

### Session C BeBanking Candidates — Alignment Summary

| W1S3 file | Impact | Key findings |
|---|---|---|
| W1S3-001 Product Overview | **High** | Module taxonomy conflict (WB-PC-003). Disaster Recovery not in W1S3-001 (WB-NI-002). Bank list now available (WB-NI-004). SAP and Sage ERP platforms conflict (WB-PC-001, WB-NI-003). |
| W1S3-002 H2H Core | **High** | BQ4 resolved — full bank list on website (WB-NI-004). Standard Bank confirmed (WB-C-023). Channel (Connect Direct vs. SFTP) still not addressed by website. |
| W1S3-003 Supplier Payments | Moderate | Payment automation and approval workflows confirmed on website. AVS not visible in website taxonomy (WB-PC-003 context). |
| W1S3-004 Payroll Payments | Low | Payroll H2H payments confirmed as part of payment automation on website. No additional detail available. |
| W1S3-005 Forex Payments | **Critical** | "Forex Payments" is a named module on the website — this strongly suggests BQ11 answer is YES (full forex capability, not just exchange rates). BU confirmation still required. W1S3-005 may be substantially below scope if the website claim is accurate (WB-NI-005). |
| W1S3-006 ERP Integration | **High** | SAP and Sage conflict (WB-PC-001, WB-NI-003) means ERP integration scope is unclear. Acumatica integration confirmed. Oracle integration confirmed. |
| W1S3-007 Security | Confirmed | Role-based approvals, audit trails, segregation of duties all confirmed on website. "Data Security Protocols" on website may enrich W1S3-007 content. |
| W1S3-008 Architecture | Low | No new architectural content on website. Disaster Recovery noted (WB-NI-002). |
| W1S3-009 Hosting Model | Moderate | "Flexible Pricing & Scalability" confirms a flexible model exists. Deployment model not specified on website. Cloud deployment question (BQ3) still not resolved. |
| W1S3-010 Monitoring | Moderate | "Live, accurate transaction data 24/7/365" suggests monitoring dashboard may exist (WB-NI-006). Confirms some level of BQ10 answer. |

### Validated Fact Baseline — Alignment Summary

| Fact | Baseline value | Website finding | Status |
|---|---|---|---|
| 50+ senior consultants | 50+ (F2, confirmed) | appsolvegroup.com claims "100+ Oracle professionals across the group" | **Review required** — different entity may explain difference (WB-PC-002) |
| Oracle Level 1 Partner | Confirmed (F3/F4) | Website confirms Oracle partnership; tier not stated on site | Baseline stands — website does not contradict |
| Oracle expertise areas (5) | Fusion Cloud Financials, Fusion Cloud HCM Core, Oracle Integration, EBS Migration to OCI, OCI Migration | Website confirms 3 of 5 directly; SCM is on website but not in expertise list (WB-PC-007) | Broadly confirmed; SCM to be investigated |
| Acumatica Gold Partner | Confirmed (F5) | Website says "South Africa's Leading Acumatica ERP Partner" — marketing language, not a tier claim | Baseline stands; partner tier not contradicted |
| Oracle Business Impact Awards 2024 (EMEA and ECEMEA) | Confirmed (F7) | Website confirms EMEA; ECEMEA not mentioned | EMEA confirmed; ECEMEA: baseline confirmation stands |
| Hein Blignaut 30 years IT experience | 30 years as of 2026 (started 1996) | No leadership names or bio on any website reviewed | Not addressed |
| Geography corrections | Sub-Saharan: BW/ZM/MZ/NA/TZ; International: USA/FR/AE/PK | UK entity not in approved geography (WB-NI-020, WB-PC-002 context) | **New finding** — UK entity must be investigated |
| BeBanking ERP: Oracle EBS, Oracle Fusion, Acumatica | Confirmed (D1) | Website adds SAP and Sage (WB-PC-001, WB-NI-003) | **Critical conflict** — requires immediate BU review |

---

## Priority Analysis

### Top 10 Findings by Business Value

| Rank | Finding | Classification | Business value | Urgency |
|---|---|---|---|---|
| 1 | SAP listed as BeBanking ERP — direct conflict with approved W1S1-005 | Potential Conflict (WB-PC-001) | **Critical** — live website contradicts approved content; any tender using W1S1-005 is out of alignment with the public website if SAP exists | Immediate |
| 2 | BeBanking bank list confirmed: Standard Bank, FNB, African Bank, ABSA, Investec, Capitec, Nedbank | New Information (WB-NI-004) | **High** — resolves BQ4; enables W1S3-002 to advance; removes a Session C blocker | Session C (before review) |
| 3 | BeBanking Forex Payments confirmed as a named module | New Information (WB-NI-005) | **High** — strongly suggests BQ11 (forex scope) = YES; W1S3-005 may need full redraft not just scope definition | Session C (before review) |
| 4 | R6 billion transactions per month | New Information (WB-NI-001) | **High** — powerful tender differentiator if confirmed; immediately usable in BeBanking competitive sections | BU confirm then W1S1-005 |
| 5 | UK entity (appsolvegroup.com) — geography and headcount implications | New Information / Potential Conflict (WB-NI-020, WB-PC-002) | **High** — geographic presence claim in approved W1S1-008 does not include UK; headcount "100+" on group site needs explanation | Immediate |
| 6 | Acumatica Construction module confirmed on website — W1S2-008 is STRUCTURE ONLY | Potential Conflict (WB-PC-004) | **High** — Session B gap can be addressed using website content; unblocks a candidate | Session B |
| 7 | Oracle APEX Development & Support — not in repository | New Information (WB-NI-007) | **High** — growing Oracle capability; relevant to any tender asking for custom development or Oracle low-code | Wave 2 |
| 8 | Acumatica Service Management module — may resolve W1S2-006 (Field Services STRUCTURE ONLY) | New Information (WB-NI-011) | **High** — Session B gap; website presence confirms the module is offered | Session B |
| 9 | APPSolve Agri — proprietary product not in repository | New Information (WB-NI-014) | **High** — agriculture sector tenders; competitive differentiator; new product area entirely missing from KB | Wave 2 |
| 10 | BeBanking module taxonomy mismatch with W1S3-001 | Potential Conflict (WB-PC-003) | **Medium-High** — Session C files should use the current product taxonomy; may affect how all 10 W1S3 files are structured | Session C (BU alignment) |

---

### Items for Session C Consideration

These findings should be reviewed with the BeBanking BU lead before Session C approval decisions are finalised.

| Finding | Session C implication |
|---|---|
| WB-PC-001 — SAP as supported ERP | If confirmed: W1S3-001 and W1S3-006 must include SAP integration sections. If denied: the website must be corrected before any BeBanking tender response is issued. Either way, this must be resolved before Session C approvals. |
| WB-NI-003 — Sage as supported ERP | Same as above. Add Sage to BQ5 scope if confirmed. |
| WB-NI-004 — Full bank list | Add the 7-bank list as the definitive answer to BQ4. Ask BU lead to confirm this is the current 2026 list and whether it can be named in tenders. |
| WB-NI-005 — Forex Payments as a module | Revise BQ11 framing: present website evidence to BU lead and ask for confirmation of full SWIFT/forex capability. This changes W1S3-005 from "cannot advance" to "advance pending BU confirmation + full redraft." |
| WB-NI-006 — Live monitoring 24/7 | Add to BQ10 context: present website claim to BU lead and ask for the monitoring tool or dashboard name. |
| WB-NI-002 — Disaster Recovery module | Add as a new BU lead question (BQ-WEB-02): is Disaster Recovery a configurable module or a hosting-level service? Which W1S3 file should it appear in? |
| WB-PC-003 — Module taxonomy mismatch | Ask BU lead to confirm preferred taxonomy for tenders: functional module names (W1S3-001 style) or website benefit groupings. |
| WB-NI-001 — R6bn transactions/month | Ask BU lead to confirm statistic and authorise for tender use. If authorised, add to W1S1-005 and W1S3-001. |

**New BU lead questions to add to the Session C Workbook:**

| # | New question | Affects |
|---|---|---|
| BQ-WEB-01 | Confirm the "R6 billion transactions per month" statistic — is it current, how is it measured, and is it authorised for tender use? | W1S1-005, W1S3-001 |
| BQ-WEB-02 | Is Disaster Recovery a named BeBanking module or a hosting-level feature? What does it cover? Which W1S3 file should it appear in? | W1S3-008, W1S3-009 |
| BQ-WEB-03 | Does BeBanking support Sage ERP? If yes, when was this added? What is the integration scope? | W1S1-005, W1S3-001, W1S3-006 |
| BQ-WEB-04 | The website lists SAP as a supported ERP — is this current? (See WB-CRITICAL-001.) What is the SAP integration model? | W1S1-005, W1S3-001, W1S3-006 |
| BQ-WEB-05 | Confirm the 2026 bank list (Standard Bank, FNB, African Bank, ABSA, Investec, Capitec, Nedbank) as the definitive current list for tender use. | W1S1-005, W1S3-002 |
| BQ-WEB-06 | The website lists "Forex Payments" as a named module — does BeBanking support full SWIFT/international payment processing, or is this limited to Automated Exchange Rates loading? | W1S3-005 |

---

### Items for Wave 2 Extraction

| Finding | Wave 2 action |
|---|---|
| WB-NI-007 — Oracle APEX | Extract Oracle APEX capability statement. Source: oracle.appsolve.co.za APEX page + any APEX client proposals in corpus. |
| WB-NI-009 — Oracle Health Checks | Extract Oracle Health Check & System Review service description. Source: oracle.appsolve.co.za + relevant HIST files. |
| WB-NI-012 — Acumatica Retail & eCommerce | Create extraction candidate for Acumatica Retail & eCommerce module. Source: acumatica.appsolve.co.za + Acumatica partner portal. |
| WB-NI-014 — APPSolve Agri | Create extraction candidate for APPSolve Agri. Source: appsolve.co.za product page (fetch further pages) + any Agri client proposals in corpus. |
| WB-NI-015 — APPTime | Create extraction candidate for APPTime product description. Source: appsolve.co.za. |
| WB-NI-008 — Oracle Analytics (replaces OBIEE) | Update W1S1-007 Technical Skills list — replace OBIEE with Oracle Analytics Cloud. Minor edit, not a new extraction. |
| WB-NI-010 — Oracle SCM | Verify with BU lead whether OPN has SCM expertise registered. If yes, update W1S1-003. If no, note as a service offering only. |
| WB-NI-020 — UK entity relationship | Determine the corporate relationship between appsolve.co.za and appsolvegroup.com. Update W1S1-008 Geographic Presence if UK operations are confirmed. |

---

### Items That Should Trigger Repository Corrections

These findings require action on approved content or the validated fact baseline.

| Finding | Correction required | Priority |
|---|---|---|
| WB-PC-001 — SAP on BeBanking website | If BU confirms SAP is a real integration: update W1S1-005 ERP Compatibility and all W1S3 files. If BU confirms SAP is NOT supported: website must be corrected; no repository change needed. | **Immediate** |
| WB-NI-003 — Sage on BeBanking website | If BU confirms Sage is a real integration: update W1S1-005 ERP Compatibility and W1S3-001 ERP Compatibility. | **Session C — BU confirmation first** |
| WB-NI-004 — Bank list | If BU confirms: update W1S1-005 "all major South African banks" to name specific banks (or add as a supplementary list). Replace W1S3-002 [UPDATE] placeholder. | Session C |
| WB-PC-002 — UK entity / headcount | If UK entity is a separate company: no repository change needed; retain 50+ for SA entity. If UK entity is part of the same APPSolve group and headcount should reflect this: update fact baseline and all references to headcount. | After WB-NI-020 is resolved |
| WB-NI-013 — Agriculture & Mining industry for Acumatica | Add Agriculture & Mining to the Acumatica industry list in W1S1-004 at next review cycle. | Low — next review cycle |
| WB-NI-008 — OBIEE → Oracle Analytics | Update W1S1-007 Technical Skills list to replace OBIEE with Oracle Analytics Cloud. | Low — next review cycle |

---

## Additional BU Lead Questions Added by This Review

The following questions should be added to `00_Governance/SESSION_C_REVIEW_WORKBOOK.md` before the BeBanking BU lead meeting:

> BQ-WEB-01 through BQ-WEB-06 as listed in the Session C section above.

The following question applies to Hein Blignaut directly (not BeBanking BU):

> **CORP-01:** What is the corporate relationship between appsolve.co.za and appsolvegroup.com? Is appsolvegroup.com a separate UK entity, a subsidiary, or a different brand operated by the same principals? This affects geographic presence, headcount claims, and group capability statements in tenders.

---

*No repository files were modified as part of this review.*
*All findings classified as Potential Conflict or New Information require BU lead or Hein Blignaut confirmation before any approved content is updated.*
*Repository hierarchy: Approved Content > Validated Repository Evidence > Current Website Content.*
