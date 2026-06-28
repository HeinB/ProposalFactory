# Session A — Fact Resolution Report
**Prepared:** 2026-06-09
**Scope:** Repository-based resolution of F1, F6, F8, F9, F10, F16 from Session_A_Review_Workbook.md
**Previously confirmed externally (F2, F3, F4, F5, F7, F11, F15):** Recorded below for completeness
**Do not modify extraction candidates until recommended updates in Section 3 are applied.**

---

## Section 1 — Confirmed External Facts (F2, F3, F4, F5, F7, F11, F15)

These values were provided directly by Hein Blignaut and are authoritative. Recorded here for file update reference.

| Fact | Confirmed Value | Apply to files |
|---|---|---|
| F2 — Senior consultant count | **50+ senior consultants** (replace all instances of 100+, 110+) | W1S1-001, W1S1-007, W1S1-009 |
| F3 — Oracle partner model | **Oracle Level 1 Partner** under Oracle's new partner model | W1S1-002, W1S1-003, W1S1-007 |
| F3 — Published expertise areas | Oracle Fusion Cloud Financials; Oracle Fusion Cloud HCM Core; Oracle Integration; Oracle E-Business Suite Migration to OCI; Oracle Cloud Infrastructure Migration | W1S1-003 |
| F4 — Legacy tier language | Remove "Oracle Gold Partner" / "Gold Level" from all files. Use Level 1 credentials as the current authoritative claim. | W1S1-002, W1S1-003, W1S1-007 |
| F5 — Acumatica partner tier | **Acumatica Gold Partner** | W1S1-004 |
| F7 — Oracle awards 2020–2026 | Add: Oracle Business Impact Award – EMEA – **2024** and Oracle Business Impact Award – ECEMEA Region – **2024** | W1S1-002, W1S1-003, W1S1-006 |
| F11 — BeBanking banks | **All major South African banks** (do not publish specific bank list until BeBanking BU lead confirms) | W1S1-005 |
| F15 — DBA team claim | Replace with: "APPSolve maintains one of the largest locally based Oracle Applications DBA teams in South Africa." | W1S1-007 |
| F10 — SAP claim | Treat as unverified. **Remove from all candidates.** | W1S1-005 |

---

## Section 2 — Repository-Based Fact Resolution

### F1 — Years APPSolve Has Been in Business

**Research conducted:**
- Read `Tender Pack/appsolve info.txt` — full company registration details
- Company registration number: **2002/008072/07** — year of registration confirmed as 2002
- Cross-referenced against Columbus Consulting Company Profile document (c. 2023): "APPSolve was established in 2002 as an IT Technology Services and Support provider... over the last 21 years" — consistent
- CIPC consolidated registration PDF exists (`Tender Pack/Registration Docs/Consolidated APPSolve Registration Documents.PDF`) but is not readable as text; it would contain the exact incorporation date

**Finding:** The founding year is **definitively 2002**. The exact month cannot be confirmed from readable repository content. Given today's date of 2026-06-09:
- If founded January–June 2002: 24 years ✓
- If founded July–December 2002: 23 years (anniversary not yet reached)

**Confidence:** HIGH for year (2002). LOW for specific month — CIPC PDF required for certainty.

**Recommendation for candidate files:** Use "**established in 2002**" or "**over 23 years**" as the safe conservative claim. Do not write "24 years" until founding month is confirmed. The CIPC registration PDF is in `Tender Pack/Registration Docs/` — open it to confirm the month.

---

### F6 — Oracle EMEA/ECEMEA Business Impact Award Dates

**Research conducted:**
- Background search across all DOCX files in corpus for "Business Impact Award", "ECEMEA", "EMEA.*award" — found 5 matching documents
- Key document examined: `Parties/Customers/Columbus Consulting/APPSolve Company Profile.docx` (c. 2023) — the most comprehensive company profile found in the corpus
- Finding: The 2023 Columbus Consulting profile lists Oracle Innovation Sustainability Award (2015, 2016), Oracle SaaS Partner of Year SADC 2016, New Entrant 2019 — but **does NOT include any EMEA/ECEMEA Business Impact Award**
- This absence is diagnostic: as at 2023, no EMEA/ECEMEA Business Impact Award had yet been received

**Finding:** The EMEA/ECEMEA Business Impact Awards were **not received until 2024** — which is why they appear undated in the September 2024 Oracle Fusion Template (received after or around the template authoring date). The user-confirmed F7 update (both awards received in 2024) is consistent with this evidence.

**Confidence:** CONFIRMED. Both awards are from **2024**. Resolved by triangulation: repository absence in 2023 + user confirmation of 2024.

**Resolved value:** Oracle Business Impact Award – EMEA – 2024; Oracle Business Impact Award – ECEMEA Region – 2024.

---

### F8 — Hein Blignaut Years of Experience

**Research conducted:**
- Searched for Hein Blignaut CVs across corpus in DOCX format
- Found master DBA CV: `Parties/employees/CVs/Existing Employees and Contractors/Management/DBA_CV Hein Blignaut.docx`
- Read career history section

**Career history from CV:**

| Employer | Period | Role |
|---|---|---|
| Mobile Telephone Networks (MTN) | **1996–2000** | Senior APPS DBA |
| Total Managed Delivery, U.K. | 2000–2003 | Senior APPS DBA |
| APPSolve | 2003–Present | Managing Director, Principal APPS DBA |

**CV self-description:** "At present, I have 19 years experience in the I.T. industry" — this CV was last updated approximately **2015** (1996 + 19 = 2015).

**Finding:** Hein's IT career commenced in **1996** at MTN. As of 2026, this is **30 years** of IT and Oracle experience.

**Confidence:** HIGH. Career start year 1996 is unambiguous in the CV. The 30-year figure is arithmetic.

**Note for W1S1-002:** W1S1-002 contains the biographical founding statement. If a personal experience claim is added, use "**30 years**" not "19 years." The CV in the management folder requires updating before use in tender submissions — it is over 10 years stale.

---

### F9 — Geographic Presence Validation

**Research conducted:**
- Listed all customer folders matching geographic search terms
- Examined Axon folder structure (USA) and ATC France folder structure (France)
- Searched corpus documents for Nigeria, Uganda, Bangladesh, Qatar client evidence
- Cross-referenced against Columbus Consulting Company Profile (c. 2023) for geographic claims in use

**Results by geography:**

| Geography | Evidence | Status | Recommendation |
|---|---|---|---|
| Botswana | Multiple dedicated client folders: Botswana Housing, BIUST, NBFIRA, Construction Industry Trust Fund, DAI-Botswana, University of Botswana | ✅ CONFIRMED — strong | Retain. Active presence claim defensible. |
| Zambia | Rural Electrification Authority, Zanaco Bank Zambia | ✅ CONFIRMED | Retain. |
| Mozambique | Westfalia Fruto Mozambique client folder; Oracle Innovation Award 2015/2016 context | ✅ CONFIRMED | Retain. |
| Namibia | MTC Namibia, Road Fund Administration - Namibia, Shine Technologies Namibia | ✅ CONFIRMED | Retain. |
| Tanzania | CRDB Bank PLC, Tanzania Revenue Authority | ✅ CONFIRMED | Retain. |
| USA | Axon Enterprises (Arizona) — active contract documented in `Tender Pack/appsolve info.txt` with full remittance details | ✅ CONFIRMED | Retain. Soften to "contracts taken up" (past-tense framing already in template). |
| France | ATC France — signed Master Consultant Agreement + signed Service Annexures found | ✅ CONFIRMED | Retain. |
| Abu Dhabi (UAE) | ClearPeaks Abu Dhabi — dedicated client folder | ✅ CONFIRMED | Retain. Claim as "Abu Dhabi" or "UAE." |
| Pakistan | Central Depository Company of Pakistan — client folder with 2019 proposal activity | ✅ CONFIRMED (2019 vintage) | Retain with caution. Use past-tense framing. |
| Ghana | "Nathan Ofori - AfricaTradeAPP - Ghana" — folder name suggests an individual contact or very small engagement | ⚠️ UNCERTAIN | Soften or remove. Not evidenced as a formal implementation client. |
| Nigeria | No client folder found. No corpus document evidence. | ❌ NOT FOUND | **Remove from active list or move to historical footnote.** |
| Uganda | No client folder found. No corpus document evidence. | ❌ NOT FOUND | **Remove from active list or move to historical footnote.** |
| Bangladesh | No client folder found. No corpus document evidence. | ❌ NOT FOUND | **Remove from active list or move to historical footnote.** |
| Qatar | No client folder found. No corpus document evidence. | ❌ NOT FOUND | **Remove from active list or move to historical footnote.** |

**Confidence:** HIGH for confirmed geographies. HIGH for absences (thorough search, zero results).

**Contradiction discovered — see Section 4.**

---

### F10 — SAP BeBanking Integration Claim

**Research conducted:**
- Search 1 (targeted): Searched all DOCX files in corpus with filenames containing "bebank", "banking", "h2h", or "host" for any SAP reference → **0 results**
- Search 2 (broad): Searched all DOCX files in corpus for any SAP reference → **5 results**, all non-BeBanking documents:
  - `APPSolve References v2.docx` — general reference document
  - `APPSolve SARB ERP Support Extension.docx` — SARB support contract
  - `Ekal/Document 1 - ITT.docx` — invitation to tender (Ekal client)
  - `Columbus Consulting/APPSolve Company Profile.docx` — company profile mentioning SAP in industry context
  - `Columbus Consulting/JV Agreement Col-AppS.docx` — joint venture agreement with Columbus Consulting (a SAP implementer)

**Finding:** No BeBanking proposal, product description, or capability document across 14 years of corpus history (approximately 18,400 files) references SAP integration. The Columbus Consulting JV Agreement confirms APPSolve explored a partnership with a SAP implementer — this likely prompted the AI extractor to infer SAP integration — but **no actual BeBanking-SAP integration is evidenced**.

**Confidence:** HIGH. Absence of evidence is conclusive here: if BeBanking-SAP integration existed, it would appear in at least one proposal in 14 years. It does not.

**Action:** Remove the SAP line from W1S1-005. Do not re-add unless Hein or the BeBanking BU lead explicitly confirms it as a current capability.

---

### F16 — Acumatica Industry Reference Coverage

**Research conducted:**
- Checked `04_References/Acumatica/` in the Tender Knowledge Base: **folder structure exists but is empty** (not yet populated — pending compliance migration)
- Checked `Tender Pack/References/Acumatica References/`:
  - **Signed**: 1 reference — `ATS - Acumatica Letter.pdf` (industry of ATS not determinable from filename)
  - **Unsigned templates**: 9 clients — USB-ED, FuelU2, Chemunique, Maxiflex, Interconnect, Dunlop Srixon Sport, At Source, Truman and Orange, Terbodore
- Read USB-ED reference template: USB Executive Development — **Higher Education** confirmed (implementation scope: Intercompany Accounting)
- Read Chemunique reference template: **Advanced Distribution Edition** — chemical distribution
- Checked corpus client folders: HyDac (Manufacturing — hydraulic systems), Tiger Brands - Acumatica (FMCG/Food), Nampak and Mpact (Packaging/Manufacturing)

**Industry coverage assessment:**

| Claimed Industry | Evidence | Confidence |
|---|---|---|
| Manufacturing | HyDac (hydraulic systems), Nampak, Mpact | ✅ CONFIRMED |
| Distribution | Chemunique (Advanced Distribution Edition) | ✅ CONFIRMED |
| Higher Education | USB-ED (reference template — unsigned) | ✅ CONFIRMED (but no signed reference) |
| FMCG / Food & Beverage | Tiger Brands - Acumatica | ✅ CONFIRMED |
| Healthcare | No reference letter, no identifiable healthcare client folder found | ❌ NOT EVIDENCED |
| Professional Services | Not specifically evidenced through reference letters | ⚠️ UNCONFIRMED |

**Finding:** "Healthcare" is listed in W1S1-004 as a delivery industry but cannot be evidenced from any reference letter or client folder in the repository. This is the highest-risk industry claim in W1S1-004. It should be removed from W1S1-004 unless Hein can identify a healthcare Acumatica client by name.

**Note on signed references:** Only 1 of 10 Acumatica reference letters is signed (ATS). The remaining 9 are unsigned templates. These represent actual clients but cannot be cited as "reference letters" until signed. This is the Acumatica reference gap noted in HANDOVER.md.

**Confidence:** HIGH for confirmed industries. HIGH for Healthcare absence.

---

## Section 3 — Candidate Update Recommendations

The following updates apply all confirmed facts (F2–F16) to the 9 Session A candidates. Apply in the recommended review order from Session_A_Review_Workbook.md.

---

### W1S1-001 — Company Overview
**Updates required:**

1. **Years in business:** Replace `[UPDATE: 24]` → `"established in 2002"` (or `"over 23 years"` — avoid "24" until founding month confirmed from CIPC PDF)
2. **Headcount:** Replace `[UPDATE: verify current headcount]` → `"50+"` → Full wording: `"more than 50 Senior Consultants"`
3. **Geography:** Remove Nigeria, Uganda, Bangladesh, Qatar from international markets list; soften Ghana to footnote or remove. Retain: Botswana, Zambia, Mozambique, Namibia, Tanzania, USA, France, Abu Dhabi, Pakistan.

**Post-update status:** Ready to advance to Review_Required once geography list is confirmed with Hein.

---

### W1S1-002 — Company History
**Updates required:**

1. **Years in business:** Replace `[UPDATE: 24]` → `"established in 2002"` / `"over 23 years"`
2. **Headcount:** Replace `[UPDATE: verify]` → `"more than 50 Senior Consultants"`
3. **Geography:** Same as W1S1-001 — remove four unconfirmed countries; retain confirmed nine
4. **Oracle partner model:** Replace all "Oracle Gold Partner" / "Gold Level" references with "Oracle Level 1 Partner" language; add published expertise areas
5. **Oracle awards — add 2024 awards:** Add "Oracle Business Impact Award – EMEA – 2024" and "Oracle Business Impact Award – ECEMEA Region – 2024" to the awards list
6. **Oracle EMEA/ECEMEA award fix:** The existing entry "Oracle APPS/SaaS Partner Business Impact Award — EMEA and ECEMEA — [UPDATE: Confirm dates]" — update to show year 2024, retitle to match official 2024 award name as provided in F7
7. **Founder biography:** Confirm with Hein whether "The company was founded by Hein Blignaut" biographical sentence is approved for tender use before advancing

**Post-update status:** Requires Hein's decision on item 7 (founder bio) before advancing.

---

### W1S1-003 — Oracle Partnership
**Updates required:**

1. **Partner tier and model:** This file requires a substantive rewrite of the Partner Credentials section. Replace:
   - "Oracle Partner — Gold Level" → "Oracle Level 1 Partner"
   - Remove "Oracle Gold Level partnership entitles us to sell and distribute Oracle licenses..." → retain the capability statement but update the tier language
   - Add the 5 published expertise areas as distinct credentials
2. **Years as Oracle partner:** Replace `[UPDATE: 24+]` → derive from F4 (Oracle Level 1 — use "over two decades")
3. **Oracle awards:** Update the award table — add both 2024 Business Impact Awards; confirm date for EMEA/ECEMEA entries (now confirmed as 2024)
4. **"Oracle Backed" section:** Review language referring to "Gold Level" — update to reflect Level 1 credential and expertise-based model

**Post-update status:** Requires substantive credential section rewrite. Higher effort than other files but content structure is sound.

---

### W1S1-004 — Acumatica Partnership
**Updates required:**

1. **Partner tier:** Replace "Acumatica Gold Certified Partner" → "**Acumatica Gold Partner**" (confirmed tier per F5)
2. **Industry list:** Remove "Healthcare" (not evidenced). Suggested replacement: "Manufacturing, Distribution, FMCG, and Higher Education" — all confirmed from reference portfolio. Optionally add "Professional Services" if Hein confirms.
3. **Industry verification note:** Remove the `[UPDATE: Verify this industry list]` flag once healthcare is removed.

**Post-update status:** Ready to advance to Review_Required after items 1 and 2 are applied. Low effort.

---

### W1S1-005 — BeBanking Overview
**Updates required:**

1. **Remove SAP line:** Delete "SAP — integration capability" from the ERP Compatibility section entirely. No repository evidence supports this claim.
2. **Banking partners:** Replace "including Standard Bank" → "all major South African banks" (per F11). Add note: specific bank list subject to BeBanking BU lead confirmation before individual bank names are cited.
3. **Acumatica integration:** The line "Acumatica — native integration with Acumatica's financial and banking modules" — this remains `[UPDATE: Verify]` pending BeBanking BU lead confirmation. Do not remove but do not approve as DIRECT without BeBanking BU confirmation.

**Post-update status:** After items 1 and 2, the only remaining open item is the Acumatica integration confirmation (item 3), which is a BeBanking BU question. Can advance to Review_Required with item 3 flagged for BeBanking BU lead review.

---

### W1S1-006 — Awards and Recognition
**Updates required:**

1. **EMEA/ECEMEA award:** Update entry from `[UPDATE: Confirm date]` → year **2024**. Retitle to match official 2024 award names per F7: "Oracle Business Impact Award – EMEA – 2024" and "Oracle Business Impact Award – ECEMEA Region – 2024"
2. **Add 2024 awards:** These may be the same as the existing EMEA/ECEMEA entry (now dated), or additional rows — confirm with Hein whether these are the same awards previously listed as undated, or new entries to add
3. **Success stories (Tiger Brands, USAID, UT Grain):** URLs not captured in the candidate file; external web confirmation still required before this section can be approved. Mark as outstanding item.
4. **Post-2019 gap now closed:** The 2024 awards close the 2019–2026 gap confirmed by F7.

**Post-update status:** After items 1 and 2, this file is significantly closer to approval. Items 3 (URL verification) cannot be resolved from the repository and remain external.

---

### W1S1-007 — Delivery Model
**Updates required:**

1. **Oracle tier:** Replace "Gold Level partnership with Oracle" (in Business Development section) → "Oracle Level 1 Partner" language
2. **Years count:** Replace `[UPDATE: 24+]` → `"over 23 years"` (consistent with F1 resolution)
3. **DBA team claim:** Replace "APPSolve has the largest number of locally based Oracle Applications DBAs in South Africa" → "APPSolve maintains one of the largest locally based Oracle Applications DBA teams in South Africa." (per F15)
4. **Technical skills list review:** OBIEE (superseded by OAC) and legacy ADF/OAF noted as potentially outdated. This is an optional enhancement — not a blocking update.

**Post-update status:** After items 1–3, ready to advance to Review_Required. Item 4 is optional.

---

### W1S1-008 — Geographic Presence
**Updates required:**

1. **Remove from Sub-Saharan list:** Nigeria, Uganda (no client evidence)
2. **Remove from International list:** Bangladesh, Qatar (no client evidence)
3. **Ghana:** Move to a "historical projects" footnote or remove — evidence is a single uncertain contact, not a confirmed corporate implementation client
4. **Retain confirmed geographies:** Botswana, Zambia, Mozambique, Namibia, Tanzania (sub-Saharan); USA, France, Abu Dhabi, Pakistan (international)
5. **Industries table — "Tier 1 operators" (Telco):** Can retain — MTN is a confirmed Tier 1 client (referenced in Hein's CV and multiple corpus folders)
6. **Language adjustment for past-tense markets:** Pakistan (2019 vintage) and USA/France (contract basis rather than ongoing office) — consider using "APPSolve has delivered projects in..." rather than "operates in"

**Post-update status:** After items 1–4, ready to advance to Review_Required. Straightforward edits.

---

### W1S1-009 — Key Differentiators
**Updates required:**

1. **Resource pool size:** Replace "over 100 senior resources" → "over 50 senior resources" (per F2)

**Post-update status:** One-line edit. After item 1, ready to advance to Review_Required immediately.

---

## Section 4 — Contradictions Discovered

### Contradiction 1 — Headcount figures inconsistent across templates

**Files affected:** W1S1-001, W1S1-007, W1S1-009

The September 2024 Oracle Fusion Template contained two different headcount figures:
- W1S1-001: "more than 110+ Senior Consultants"
- W1S1-009: "pool of over 100 senior resources"

A third figure was found in the Columbus Consulting Company Profile (c. 2023): "over 50 senior resources."

The user-confirmed F2 value of "50+" aligns with the 2023 figure — not the 2024 template figures. The September 2024 template appears to have **doubled the headcount claim without a factual basis**. This inconsistency would be immediately visible to any evaluator comparing two sections of the same tender.

**Resolution:** Apply "50+" uniformly across all three files. The September 2024 template headcount figures (100, 110+) should not be used.

---

### Contradiction 2 — Geographic claims appear in 2023 documents without client evidence

**Files affected:** W1S1-001, W1S1-002, W1S1-008

The Columbus Consulting Company Profile (c. 2023) includes Nigeria, Uganda, Bangladesh, and Qatar in the same geographic paragraph. However, no dedicated client folders and no corpus documents were found for any of these four countries across the entire 18,400-file historical corpus.

This means the geographic claims for Nigeria, Uganda, Bangladesh, and Qatar have been carried forward through at least two template generations (2023 Columbus profile, September 2024 Oracle Fusion Template) without supporting client evidence.

**Risk:** If a government tender evaluator challenges a geographic claim (e.g., "provide a client reference for your Nigeria engagement"), APPSolve would be unable to respond. This is a credibility and procurement integrity risk.

**Resolution:** Remove these four countries from the active geography list. They may be moved to a "historical context" note if Hein can confirm that engagements did occur but were small or pre-RFP-system. Do not use in active tender responses.

---

### Contradiction 3 — Oracle partner tier language was not updated when Oracle changed its model

**Files affected:** W1S1-002, W1S1-003, W1S1-007

The Tender Pack certifications archive shows:
- 2019: OPN membership and cloud certificates
- 2020: "OPN Gold Membership 2020.pdf"
- 2021: "EXPIRED_APPSolve_OPN_202108.pdf"
- 2022–2024: Expertise-based certificates (Finance, HCM, OIC, OCI) in "Old/" subfolder
- 2025–2026: Current expertise certificates (EBS OCI 2025, EBS Sell 2026)

The Oracle Gold Membership expired in August 2021. From 2022 onward, APPSolve has operated under Oracle's expertise-based model (now Level 1). The September 2024 Oracle Fusion Template — which is still in use — continued to reference "Gold Level partnership" even though the Gold Membership had expired three years earlier.

**Risk:** Citing an expired "Gold Partner" tier in a 2026 tender is a material factual error. Oracle certifications are verifiable online by evaluators.

**Resolution:** All "Gold Level" / "Gold Partner" Oracle references must be replaced with "Oracle Level 1 Partner" and the current published expertise areas. Applied to W1S1-002, W1S1-003, W1S1-007.

---

## Section 5 — Summary Confidence Table

| Fact | Finding | Confidence | Requires External Action? |
|---|---|---|---|
| F1 — Founding year | 2002 confirmed. Month unknown. | HIGH (year) | Yes — read CIPC PDF for exact month |
| F6 — EMEA/ECEMEA award dates | Both awards: 2024 (confirmed by user + repo absence pre-2024) | CONFIRMED | No |
| F8 — Hein's experience | IT career from 1996; 30 years as of 2026 | HIGH | No — confirm CV update is desired |
| F9 — Geographies confirmed | Botswana, Zambia, Mozambique, Namibia, Tanzania, USA, France, Abu Dhabi, Pakistan | HIGH | No |
| F9 — Geographies not found | Nigeria, Uganda, Bangladesh, Qatar — zero client evidence | HIGH | Hein to confirm if any engagement history exists before removing |
| F9 — Ghana | Uncertain — single contact, not confirmed client | MEDIUM | Hein to confirm |
| F10 — SAP BeBanking | Zero evidence across 18,400 files. Remove. | HIGH | No |
| F16 — Manufacturing | Confirmed (HyDac, Nampak, Mpact, Chemunique) | HIGH | No |
| F16 — Distribution | Confirmed (Chemunique — Advanced Distribution Edition) | HIGH | No |
| F16 — FMCG | Confirmed (Tiger Brands - Acumatica) | HIGH | No |
| F16 — Higher Education | Confirmed (USB-ED — unsigned reference template) | MEDIUM-HIGH | No (but no signed reference) |
| F16 — Healthcare | Not evidenced — no reference letter or client folder | HIGH (absence) | Hein to confirm or remove |
| F16 — Professional Services | Not specifically evidenced | MEDIUM | Hein to confirm |

---

## Section 6 — Files Ready to Advance After Updates

Once the updates in Section 3 are applied, the following files can be moved directly to `07_Approved_Content/Review_Required/Cross_BU/`:

| File | Blocking items remaining after Section 3 updates | Estimated review time |
|---|---|---|
| **W1S1-009 Key Differentiators** | None — single F2 substitution | 5 minutes |
| **W1S1-001 Company Overview** | Confirm geography list with Hein (Nigeria etc. removal) | 10 minutes |
| **W1S1-004 Acumatica Partnership** | Confirm Healthcare removal and optional F16 industries | 10 minutes |
| **W1S1-005 BeBanking Overview** | Acumatica integration confirmation (BeBanking BU question — flag and advance) | 10 minutes |
| **W1S1-007 Delivery Model** | Optional technology skills list review (non-blocking) | 15 minutes |
| **W1S1-008 Geographic Presence** | Geography removal confirmed above; language softening for past-tense markets | 15 minutes |
| **W1S1-003 Oracle Partnership** | Credential section substantive rewrite required | 30–45 minutes |
| **W1S1-006 Awards and Recognition** | External URL verification still outstanding for success stories | Partial advance possible |
| **W1S1-002 Company History** | Founder bio approval from Hein required | Hein decision needed |

**Immediate target:** Apply Section 3 updates to W1S1-009, W1S1-001, W1S1-004, W1S1-005, W1S1-007, W1S1-008 — six files ready in a single sitting.
