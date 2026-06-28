# Tender Pack Migration Analysis
**Date:** 2026-06-05
**Source:** `../Tender Pack/` (628 files total)
**Status:** READ-ONLY ANALYSIS — no files modified, copied, or moved
**Produced by:** AI assistant (Claude) — human review required before migration

---

## Executive Summary

| Metric | Count |
|---|---|
| Total files in Tender Pack | 628 |
| System / ignore (.DS_Store, inventory .txt) | 6 |
| Backup copies (bkp/, Old/, Archive/ subfolders) | ~185 |
| Unsigned DOCX templates (internal working docs) | ~50 |
| Operational / non-tender files | ~12 |
| Third-party company docs (QSE partners) | 5 |
| **Recommended for primary migration** | **~155** |
| **Pending human content review before deciding** | **~35** |
| **OCR candidates (likely scanned PDFs)** | **~28** |

**Critical alerts identified:**
- BEE certificate (Level 3) expires **2026-07-31** — 56 days from today. Initiate renewal.
- Workers Comp letter 20250430 is already **expired**. Current letters exist for 2026 and 2027.
- Supplier Portal Logins spreadsheet contains credentials — **exclude from KB entirely**.
- The 2026 Tax Clearance PIN (20260305) — confirm validity period with SARS.

---

## Section 1: Document Classification by Source Folder

### 1.1 Bank Letter/
**Summary:** 14 files. 1 current, 13 archived.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| APPSolve Bank Letter 2026-05-22.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | **Current** |
| All other Bank Letters (2021–2025) | CORP | Corporate | Skip — superseded | — | Historical |

---

### 1.2 BEE/
**Summary:** 10 files. 1 current + .zip duplicate, 8 archived.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| BEE Level 3 Certificate (expires 2026-07-31).pdf | COMP | Corporate | `01_Compliance/BEE/` | No | **Current — EXPIRING SOON (56 days)** |
| Same file as .zip | — | — | Skip — duplicate format | — | Duplicate |
| 8 older BEE certificates | COMP | Corporate | Skip — superseded | — | Historical |

---

### 1.3 Certifications - Oracle and Other/
**Summary:** Largest folder (~200 files). Multiple sub-groups — see below.

#### 1.3.1 Acumatica/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Wanda van der Merwe - Acumatica Payroll.pdf | CERT | Acumatica | `05_Certifications/Acumatica/` | No | Current |
| Wanda van der Merwe - Acumatica [2nd module].pdf | CERT | Acumatica | `05_Certifications/Acumatica/` | No | Current |

#### 1.3.2 Certs/EMC/
4 old EMC/storage certifications. Expired, scanned, not relevant to Oracle/Acumatica/BeBanking.
**Action:** `99_Archive/` — do not use in tender responses.

#### 1.3.3 Consultant Certifications/Cloud/ — MASTER ORACLE CLOUD CERT SET
~40 individual Oracle Cloud consultant certifications, organised by module. These are the **authoritative originals**.

| Module Group | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Cloud/Developer/ (3–5 certs) | CERT | Oracle | `05_Certifications/Oracle/Cloud/Developer/` | No | Current |
| Cloud/Finance/ (5–8 certs) | CERT | Oracle | `05_Certifications/Oracle/Cloud/Finance/` | No | Current |
| Cloud/HCM/ (5–8 certs) | CERT | Oracle | `05_Certifications/Oracle/Cloud/HCM/` | No | Current |
| Cloud/OCI/ (3–5 certs) | CERT | Oracle | `05_Certifications/Oracle/Cloud/OCI/` | No | Current |
| Cloud/OIC/ (2–3 certs) | CERT | Oracle | `05_Certifications/Oracle/Cloud/OIC/` | No | Current |
| Cloud/Procurement/ (2–3 certs) | CERT | Oracle | `05_Certifications/Oracle/Cloud/Procurement/` | No | Current |
| Cloud/Projects/ (2–3 certs) | CERT | Oracle | `05_Certifications/Oracle/Cloud/Projects/` | No | Current |
| Cloud/SCM/ (2–3 certs) | CERT | Oracle | `05_Certifications/Oracle/Cloud/SCM/` | No | Current |

**Migrate these as the primary certification set. Do not use Legal Aid Tender/ or Oracle Certificates 2024/ as the source.**

#### 1.3.4 Consultant Certifications/EBS/ — MASTER EBS CERT SET
~15 Oracle EBS certifications by role.

| Module Group | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| EBS/DBA/ | CERT | Oracle | `05_Certifications/Oracle/EBS/DBA/` | No | Current |
| EBS/Developer/ | CERT | Oracle | `05_Certifications/Oracle/EBS/Developer/` | No | Current |
| EBS/Financials/ | CERT | Oracle | `05_Certifications/Oracle/EBS/Financials/` | No | Current |
| EBS/Projects/ | CERT | Oracle | `05_Certifications/Oracle/EBS/Projects/` | No | Current |

#### 1.3.5 Legal Aid Tender/
~22 certs assembled for a specific Legal Aid tender. Duplicates of Consultant Certifications/ files.
**Action:** Skip entirely — all originals exist in the master set above.

#### 1.3.6 Oracle Certificates 2024/
~16 certs assembled as another tender-specific collection. Duplicates of Consultant Certifications/.
**Action:** Skip entirely — use master set above.

#### 1.3.7 Oracle Partner/ — HIGH VALUE
Current Oracle Partner status certificates.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Oracle Partner 2026.pdf | CERT | Oracle | `05_Certifications/Oracle/Partner/` | No | **Current** |
| EBS Sell Expertise 2026.pdf | CERT | Oracle | `05_Certifications/Oracle/Partner/` | No | **Current** |
| [Additional Sell Expertise 2026 files] | CERT | Oracle | `05_Certifications/Oracle/Partner/` | No | **Current** |
| Service Expertise 2026.pdf | CERT | Oracle | `05_Certifications/Oracle/Partner/` | No | **Current** |
| EBS_OCI_expertise 2025.pdf | CERT | Oracle | `05_Certifications/Oracle/Partner/` | No | Current |

#### 1.3.8 Oracle Partner/Old/
Historical partner certificates by year (2011, 2014, 2019–2025).
**Action:** `99_Archive/Oracle_Partner_History/` — proof of tenure, not for tender use.

#### 1.3.9 Previous Certificates/
~100 historical individual consultant certs. Many likely scanned (OCR needed). Mix of still-current and expired certs.
**Action:** Cross-reference against current Consultant Certifications/ master set. If a consultant still appears in Rate Card/ CVs AND has a cert here that is their latest version → migrate. If superseded by a newer cert in the master set, or if the consultant is no longer active → `99_Archive/`.
**Estimate:** ~20 may still be current/unique; ~80 are superseded or for former staff.

---

### 1.4 Company Info/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| appsolve info.txt | CORP | Corporate | Skip — low-value text snippet | No | Historical |

---

### 1.5 Company Profile/ — HIGH VALUE
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| 2025/APPSolve Company Profile - Acumatica 2025.pdf | CAP | Acumatica | `06_Capabilities/Acumatica/` | No | **Current** |
| 2025/APPSolve Company Profile - Oracle 2025.pdf | CAP | Oracle | `06_Capabilities/Oracle/` | No | **Current** |
| 2024/APPSolve Company Profile (International) 2024.pdf | CAP | Cross | `06_Capabilities/Cross/` | No | Current |
| 2024/APPSolve Company Profile (SA) 2024.pdf | CAP | Corporate | `06_Capabilities/Cross/` | No | Current |
| 2024/[DOCX editable version].docx | CAP | Cross | `06_Capabilities/Cross/` | No | Current — editable master |
| 2024/[PPTX presentation version].pptx | CAP | Cross | `06_Capabilities/Cross/` | No | Current — pitch version |
| 2024/APPSolve Company Profile Oracle 2024.pdf | CAP | Oracle | Skip — superseded by 2025 | — | Superseded |
| 2020/[Any 2020 profiles] | CAP | Corporate | `99_Archive/` | Maybe | Historical |

---

### 1.6 Company Stamp/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Appsolve stamp.jpg | CORP | Corporate | `01_Compliance/Corporate/` | No | Current |
| Appsolve stamp.docx | CORP | Corporate | `01_Compliance/Corporate/` | No | Current |

---

### 1.7 CSD Report/
**Summary:** 9 files. 2 current (2025-08-02), 7 archived.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| APPSolve CSD Detail 2025-08-02.pdf | COMP | Corporate | `01_Compliance/CSD/` | No | **Current** |
| APPSolve CSD Summary 2025-08-02.pdf | COMP | Corporate | `01_Compliance/CSD/` | No | **Current** |
| 7 older CSD reports | COMP | Corporate | Skip — superseded | — | Historical |

---

### 1.8 Employment Equity Cert/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Employment Equity Certificate 2025.pdf | COMP | Corporate | `01_Compliance/Employment-Equity/` | No | **Current** |

---

### 1.9 Financial Statements/
**Summary:** 8 signed AFS files 2018–2025.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| AFS 2025 signed.pdf | CORP | Corporate | `01_Compliance/Financial-Statements/` | No | **Current** |
| AFS 2024 signed.pdf | CORP | Corporate | `01_Compliance/Financial-Statements/` | No | **Current** |
| AFS 2023 signed.pdf | CORP | Corporate | `01_Compliance/Financial-Statements/` | No | Current |
| AFS 2022 signed.pdf | CORP | Corporate | `01_Compliance/Financial-Statements/` | Maybe | Current |
| AFS 2018–2021 signed | CORP | Corporate | `99_Archive/Financial-Statements/` | **Yes — likely scanned** | Historical |

---

### 1.10 ID Documents/
**Summary:** 6 director ID copies.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| 6 × director ID documents | CORP | Corporate | `01_Compliance/Corporate/` | No | Current |

---

### 1.11 Insurance/
**Summary:** 3 files. 1 current (2026), 1 soon-to-expire (2025), 1 archived.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| PI Certificate expires 2026-11-14.pdf | COMP | Corporate | `01_Compliance/Insurance/` | No | **Current** |
| PI Certificate expires 2025-11-14.pdf | COMP | Corporate | Skip — expired Nov 2025 | — | **Expired** |
| [Archived PI cert] | COMP | Corporate | Skip — superseded | — | Historical |

---

### 1.12 Municipal and Lease Information/
Lease agreement, addendum, and 6 water/electricity account files (2020).
**Action:** Skip entirely. Property/utility documents are rarely required for tenders. If proof of address is needed, use the current municipal account files in `Utility Bill/` instead.

---

### 1.13 Org Chart/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| APPSolve Organogram Detail 202405_v1_bbbee.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | **Current (2024-05)** |
| APPSolve Organogram Detail 202202_v2.pdf | CORP | Corporate | `99_Archive/` | No | Historical |
| Rate Card - Feb21.xlsx | — | Cross | `13_Quote_Generator/Rate_Cards/` | No | Historical rate card |

---

### 1.14 QSE/ (Joint Venture Partner Documents)
Documents for Imbasa SA and Intecon — external JV partner companies.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Imbasa/CSD Reg Summary_ImbasaSA.pdf | CORP | Corporate | `99_Archive/QSE-Partners/` | No | Third-party |
| Intecon/corporate-profile.pdf | CORP | Corporate | `99_Archive/QSE-Partners/` | No | Third-party |
| Intecon/CSD Feb 2021.pdf | CORP | Corporate | `99_Archive/QSE-Partners/` | No | Third-party |
| Intecon/INTECON BEE.pdf | CORP | Corporate | `99_Archive/QSE-Partners/` | No | Third-party |
| Intecon/OPNmember_certificate.pdf | CERT | Corporate | `99_Archive/QSE-Partners/` | No | Third-party |

**Do not cite these as APPSolve credentials.** Context only for joint bid scenarios.

---

### 1.15 Rate Card/
This folder serves as both the CV library and rate card repository.

#### Individual CVs (root level) — 42 consultant PDFs

> **⛔ MIGRATION CANCELLED — Architecture Decision ADR-001 (2026-06-10)**
>
> The planned migration of all consultant CV PDFs from this folder to `03_CVs/[BU]/` in the Knowledge Base has been cancelled.
>
> **Decision:** APPTime is the authoritative source for consultant CV content. Full CV documents are not maintained in the Knowledge Base. The KB stores Consultant Index Records (metadata: skill tags, certifications, availability flag, APPTime reference) only.
>
> **Action:** Do not migrate any CV PDFs from this folder to the Knowledge Base. These files remain read-only in the Tender Pack as historical records. Consultant Index Records will be created separately from APPTime — see `00_Governance/CONSULTANT_INDEX_PROGRAMME.md` and `00_Governance/ADR-001-CV_SOURCE_OF_TRUTH.md`.
>
> **The table below is preserved as historical inventory only. All "KB Destination" values in this table are void.**

| Consultant | Type | BU | KB Destination (VOID — ADR-001) | OCR | Status |
|---|---|---|---|---|---|
| Arno Rautenbach | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Avinth Rabbipal (0625) | CV | Oracle | `03_CVs/Oracle/` | No | **Current (Jun 2025)** |
| Biju Jacob | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Carin Webb | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Carol Grosvenor | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Charles Patsanza (0625) | CV | Oracle | `03_CVs/Oracle/` | No | **Current (Jun 2025)** |
| Cindy Pedlar | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Colin Heuer | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Cornelius Jordaan (0625) | CV | Oracle | `03_CVs/Oracle/` | No | **Current (Jun 2025)** |
| Daan van der Merwe | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Debbie Blignaut | CV | Cross | `03_CVs/Oracle/` | No | Current |
| Errol Genis | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Esna Pretorius | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Fiona Carrim (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Francois Terblanche | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Gavin Sadler | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Ian de Koker | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Jono O'Donoghue | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Katlego Shiane (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Kgomotso Moepi (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Kirankumar Doradla | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Krivahn Doss (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Lucia Van Wyk | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Mahlatse Khoza | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Marcus Veeraragaloo (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Marlene Mostert | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Morongwa Modiba (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Mthokozisi Sithole (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Naeem Essop | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Niel du Toit (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Nkululeko Mashego (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Obakeng Modukanele (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Rahul Dave | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Seef Muller | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Sega Phoshoko (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Shaun Cronje | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Sternly Simon | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Thato Miyen (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Themba Tambekwayo (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Tim Kriel | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| Tshabo Monethi (0625) | CV | Pending review | `03_CVs/` | No | **Current (Jun 2025)** |
| Werner van Niekerk | CV | Oracle | `03_CVs/Oracle/` | No | Current |
| AF Resources CV.xlsx | — | — | Skip — formatting sheet | — | — |

**Note on BU "Pending review":** Consultants with only 0625-dated CVs and no visible certifications in the inventory need content review to determine correct BU sub-folder (Oracle/Acumatica/BeBanking/Cross). These may include BeBanking payment specialists or Acumatica consultants.

#### Rate Card/Rate Cards/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| 2022 Rate Card.csv | — | Cross | `13_Quote_Generator/Rate_Cards/` | No | Historical |
| Rate Card Jan 2020.xlsx | — | Cross | `13_Quote_Generator/Rate_Cards/` | No | Historical |
| Book.xlsx | — | Cross | `13_Quote_Generator/Rate_Cards/` | No | Historical — unclear purpose |

#### Rate Card/ETS Tender/ — Tender-specific package
CVs and certs assembled for the ETS tender. **All are duplicates** of root-level CVs and Consultant Certifications/ master set.

| File | KB Action |
|---|---|
| Rates Spreadsheet ETS.xlsx | `13_Quote_Generator/Historical_Quotes/` — historical pricing reference |
| 8 × consultant CVs (Annatjie Theron, Daan, Esna, Francois, Gavin, Ian, Michael, Riaan, Tshepho, Wietse) | Skip — duplicates of root Rate Card/ CVs |
| ~15 × individual certs | Skip — duplicates of Consultant Certifications/ master set |

---

### 1.16 References/ — HIGHEST VALUE FOLDER

#### 1.16.1 Oracle Reference to Include in all Proposals/ (curated top references)

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| AppSolve_Reference Letter_02092024.pdf | REF | Oracle | `04_References/Oracle/` | No | **Current — Oracle SA endorsement** |
| Reference 2024 Oracle Letter.pdf | REF | Oracle | `04_References/Oracle/` | No | Current — check if same as above |
| ORC References/Hollywoodbets Reference.docx | REF | Oracle | `04_References/Oracle/` | No | Current — ORC implementation |
| ORC References/Mr Price Reference.docx | REF | Oracle | `04_References/Oracle/` | No | Current — ORC implementation |

#### Updated Support References/0.Signed/ — 7 SIGNED ORACLE REFERENCE LETTERS (PRIORITY)

| File | Client | Type | BU | KB Destination | OCR |
|---|---|---|---|---|---|
| Adcock Ingram_Reference Letter.pdf | Adcock Ingram | REF | Oracle | `04_References/Oracle/` | No |
| ARM_Reference letter.pdf | ARM | REF | Oracle | `04_References/Oracle/` | No |
| Assore_Reference Letter.pdf | Assore | REF | Oracle | `04_References/Oracle/` | No |
| Cape Union Mart_Reference Letter.pdf | Cape Union Mart | REF | Oracle | `04_References/Oracle/` | No |
| MTN_Reference Letter.pdf | MTN | REF | Oracle | `04_References/Oracle/` | No |
| Nala_Reference Letter.pdf | Nala | REF | Oracle | `04_References/Oracle/` | No |
| WITS_Reference Letter.pdf | Wits University | REF | Oracle | `04_References/Oracle/` | No |

**These 7 signed letters are the highest-value content in the Tender Pack. Migrate first.**

#### Updated Support References/ (unsigned DOCX — internal working docs)

| File | KB Action | Reason |
|---|---|---|
| Adcock Reference 202507.docx | Skip | Use signed PDF |
| ARM Reference 202507.docx | Skip | Use signed PDF |
| Assore Reference 202507.docx | Skip | Use signed PDF |
| ATC Reference 202507.docx | **Pending** | No signed version found — may be outstanding |
| Cape Union Mart Reference 202507.docx | Skip | Use signed PDF |
| Investec Reference 202507.docx | **Pending** | Check against `Reference 2023 09 Investec Letter.pdf` |
| MTN Reference 202507.docx | Skip | Use signed PDF |
| Nala Reference 202507.docx | Skip | Use signed PDF |
| Old Mutual Reference 202507.docx | **Pending** | No signed version found — may be outstanding |
| Truworths Reference 202507.docx | **Pending** | No signed version found — may be outstanding |
| Stellenbosch University Reference 202507.docx | Skip | Check against `Reference 2025 Stellenbosch University.pdf` |
| Wits Reference 202507 (3 variants).docx | Skip | Use signed PDF |
| emails/ (.msg files — 5) | Skip | Email evidence, not primary reference documents |

**Action:** Chase ATC, Old Mutual, and Truworths for signed reference letters. These appear to be outstanding.

#### 1.16.2 Acumatica References/Signed/ — 5 SIGNED ACUMATICA REFERENCE LETTERS (PRIORITY)

| File | Client | Type | BU | KB Destination | OCR |
|---|---|---|---|---|---|
| ATS - Acumatica Letter.pdf | ATS | REF | Acumatica | `04_References/Acumatica/` | No |
| DSSSA - Referrence Letter.pdf | DSSSA | REF | Acumatica | `04_References/Acumatica/` | No |
| FuelU2 letter 22 09 2025.pdf | FuelU2 | REF | Acumatica | `04_References/Acumatica/` | No |
| Interconnect Systems Reference Letter.pdf | Interconnect Systems | REF | Acumatica | `04_References/Acumatica/` | No |
| Maxiflex Reference Letter.pdf | Maxiflex | REF | Acumatica | `04_References/Acumatica/` | No |

#### Acumatica References/Templates/ (13 unsigned DOCX)
| File | KB Action |
|---|---|
| At Source, Chemunique, Dukathole, Dunlop Srixon, FuelU2, Interconnect, Linebooker, Maxiflex, Milpark, Prommac, Terbodore, Truman and Orange, USB-ED | Skip — internal templates; signed versions needed |

**Action:** The 13 unsigned template DOCX files represent 8 additional Acumatica clients without signed references. These are outstanding. Prioritise chasing: At Source, Chemunique, Dukathole, Dunlop Srixon, Linebooker, Milpark, Prommac, Terbodore, Truman and Orange, USB-ED.

#### 1.16.3 References/Archive/ — Historical Oracle References (2017–2020)
These have been superseded for most clients by the Updated Support References/ 2025 versions. However, some clients in the Archive are NOT in the current active set and may be relevant for BeBanking positioning.

| File | Client | BU | KB Destination | OCR | Note |
|---|---|---|---|---|---|
| 1 Adcock Ingram APPSolve Reference 1.pdf | Adcock Ingram | Oracle | `99_Archive/References/` | Maybe | Superseded by 2025 |
| 1 Adcock Ingram APPSolve Reference 2.pdf | Adcock Ingram | Oracle | `99_Archive/References/` | Maybe | Superseded |
| 2 ARM IM Appsolve Reference.pdf | ARM | Oracle | `99_Archive/References/` | Maybe | Superseded |
| 3 Harmony APPSolve Reference.pdf | Harmony | Oracle | `99_Archive/References/` | Maybe | Has current 2024 version |
| 3. SARB Client Reference Letter.pdf | SARB | Oracle | `99_Archive/References/` | Maybe | Unique — SARB not in current active set |
| 4 MTN APPSolve Reference Letter.pdf | MTN | Oracle | `99_Archive/References/` | Maybe | Superseded |
| 5 WITS Reference Letter APPSolve.pdf | Wits | Oracle | `99_Archive/References/` | Maybe | Superseded |
| 6 SARB Client Reference Feb 2018.pdf | SARB | Oracle | `99_Archive/References/` | Maybe | Unique |
| 7 Blue Strata APPSolve Reference.pdf | Blue Strata | Oracle | `99_Archive/References/` | Maybe | Unique |
| 8 BankServ APPSolve Reference Letter.pdf | BankServ | **BeBanking** | `04_References/BeBanking/` | Maybe | Unique — BeBanking context |
| 9 FNB Client Reference.pdf | FNB | **BeBanking** | `04_References/BeBanking/` | Maybe | Unique — BeBanking context |
| fastjet reference letter 2019.pdf | Fastjet | Oracle | `99_Archive/References/` | Maybe | Unique — aviation sector |
| FNB_EBS_REFERENCE2017.pdf | FNB | Oracle | `99_Archive/References/` | Maybe | Unique — EBS context |
| NHLS_Main_Reference.pdf | NHLS | Oracle | `99_Archive/References/` | Maybe | Unique — health sector |
| WITS Reference Letter_Appsolve1.pdf | Wits | Oracle | `99_Archive/References/` | Maybe | Superseded |
| TCTA/ subfolder (9 files) | Various | Oracle | `99_Archive/TCTA-Tender/` | Maybe | Tender-specific package |

**Note on BeBanking references:** BankServ and FNB references (EBS context) may contain BeBanking-relevant content about payment integration. Flag for BeBanking capability review before archiving.

#### 1.16.4 References/ Root Level — Current Signed PDFs

| File | Client | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|---|
| NALA Reference Letter Appsolve.pdf | Nala | REF | Oracle | `04_References/Oracle/` | No | Current |
| Reference 2023 Adcock Ingram Letter.pdf | Adcock Ingram | REF | Oracle | `04_References/Oracle/` | No | Current |
| Reference 2023 Assore Reference Letter.pdf | Assore | REF | Oracle | `04_References/Oracle/` | No | Current |
| Reference 202507 MTN Reference Letter.pdf | MTN | REF | Oracle | `04_References/Oracle/` | No | **Current (Jul 2025)** |
| Reference 2023 09 Investec Letter.pdf | Investec | REF | Oracle | `04_References/Oracle/` | No | Current |
| Reference 2024 Harmony Letter.pdf | Harmony | REF | Oracle | `04_References/Oracle/` | No | Current |
| Reference 2024 Mr Price.pdf | Mr Price | REF | Oracle | `04_References/Oracle/` | No | Current |
| Reference 2024 Oracle Letter.pdf | Oracle SA | REF | Oracle | `04_References/Oracle/` | No | Current |
| Reference 2025 Stellenbosch University.pdf | Stellenbosch University | REF | Oracle | `04_References/Oracle/` | No | **Current (2025)** |

#### 1.16.5 References/Template/ (Blank DOCX templates)
Internal reference letter templates — APPSolve-authored blanks for clients to sign. 18 DOCX files.
**Action:** Skip for migration — these are working source documents, not the signed references.
**Exception:** `Tiger Reference Letter BeBanking SAP.docx` and `SAA Tiger Reference Letter SAP Integration.docx` — these name Tiger and SAA as clients for BeBanking/SAP integration. Flag for follow-up: are signed versions of these available?

---

### 1.17 Registration Docs/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| BeneficiaryOwnershipDisclosure certificate 20251007.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | **Current** |
| Consolidated APPSolve Registration Documents.PDF | CORP | Corporate | `01_Compliance/Corporate/` | **YES — scanned** | **Current** |
| Cor 39.pdf | CORP | Corporate | `01_Compliance/Corporate/` | Maybe | Current |
| Disclosure Certificate 2026.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | **Current** |
| Disclosure Certificate 2026 CM_no_COR14.3.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | Current variant |
| Disclosure Certificate 2025.pdf | CORP | Corporate | Skip — superseded | — | Historical |
| Disclosure Certificate 2023a.pdf | CORP | Corporate | `99_Archive/` | — | Historical |

---

### 1.18 Resolution/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| 20250301 Resolution signatures.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | **Current** |
| 20250301 Resolution signatures.docx | — | — | Skip — keep PDF | — | Source file |
| Old/ (8 historical resolutions 2020–2024) | CORP | Corporate | `99_Archive/` | — | Historical |

---

### 1.19 SBD4 Declaration of Interest/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| SBD 4 DECLARATION OF INTEREST 20240515.pdf | COMP | Corporate | `01_Compliance/Declarations/` | No | **Current** |
| SBD 4 DECLARATION OF INTEREST.docx | COMP | Corporate | `01_Compliance/Declarations/` | No | Editable template |
| SBD 4 DECLARATION OF INTEREST.pdf | — | — | Skip — undated, superseded | — | — |

---

### 1.20 Shareholding/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Appsolve Shareholding confirmation 11 04 2024.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | **Current** |
| Diagram_Appsolve 202404.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | **Current** |
| Ownership summary.xlsx | CORP | Corporate | `01_Compliance/Corporate/` | No | Current |
| shareholding summary 20240414.xlsx | CORP | Corporate | `01_Compliance/Corporate/` | No | Current |
| Ordinary Shares/ (cert nos 26–33, 6 files) | CORP | Corporate | `01_Compliance/Corporate/` | Maybe | **Current** |
| Ordinary Shares/Certified Ordinary shares/ (6 files) | CORP | Corporate | Skip — duplicates | — | Duplicate |
| Ordinary Shares/bkp/ and Shareholding/bkp/ | — | — | Skip | — | Backup copies |

---

### 1.21 Supplier Portal Logins/
**EXCLUDE ENTIRELY.** Contains iSupplier portal credentials (usernames/passwords). Operational/sensitive data, not a tender document. Do not copy to the Knowledge Base.

---

### 1.22 Tax Cert SARS/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Tax Clearance APPSolve_PIN 20260305.pdf | COMP | Corporate | `01_Compliance/Tax/` | No | **Current** |
| Tax Clearance APPSolve_PIN 20270223.pdf | COMP | Corporate | `01_Compliance/Tax/` | No | **Future (expires ~2027-02-23)** |
| bkp/ (5 older tax certs 2022–2025) | COMP | Corporate | Skip — superseded | — | Historical |

---

### 1.23 Template Proposals/ — HIGH VALUE HIST
These are actual proposal documents with reusable structure, methodology descriptions, and pricing approaches.

| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| APPSolve Mauritius Telecom - HCM Proposal V3.0.docx | HIST | Oracle | `09_Active_Tenders/Submitted/Historical/` | No | Historical — HCM proposal |
| APPSolve SARB XxxxXxxx - PRxxxx.NEW 2022.docx | HIST | Oracle | `09_Active_Tenders/Submitted/Historical/` | No | Historical — template structure |
| APPSolve_PPro_Proposal_20240712_V2.0.docx | HIST | Oracle | `09_Active_Tenders/Submitted/Historical/` | No | Historical — 2024 proposal |

**Note:** Create `09_Active_Tenders/Submitted/Historical/` sub-folder if it does not exist.

---

### 1.24 Tender Tracker/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Tender Tracker.xlsx | — | Cross | Skip — operational tool | No | Current |
| MBD Forms/MBD FORMS 2018-19.doc | COMP | Corporate | `99_Archive/` | — | Historical |
| SBD Forms/SBD 1.doc | COMP | Corporate | `01_Compliance/Declarations/` | No | Standard form template |
| SBD Forms/SBD 4.doc | COMP | Corporate | `01_Compliance/Declarations/` | No | Standard form template |
| SBD Forms/SBD 6.1.docx | COMP | Corporate | `01_Compliance/Declarations/` | No | Standard form template |
| SBD Forms/SBD 8.doc | COMP | Corporate | `01_Compliance/Declarations/` | No | Standard form template |
| SBD Forms/SBD 9.doc | COMP | Corporate | `01_Compliance/Declarations/` | No | Standard form template |

---

### 1.25 Utility Bill/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Andre Municipal account.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | Current — proof of address |
| Hein Municipal account.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | Current — proof of address |
| Jeaenette Municipal account.pdf | CORP | Corporate | `01_Compliance/Corporate/` | No | Current — proof of address |
| September 2020.pdf | CORP | Corporate | Skip — outdated | — | Historical |

---

### 1.26 VAT Registration/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| Vat Registration appsolve.pdf | COMP | Corporate | `01_Compliance/Tax/` | **Maybe — likely old SARS letter** | Current (no expiry) |

---

### 1.27 Workmans Comp/
| File | Type | BU | KB Destination | OCR | Status |
|---|---|---|---|---|---|
| WComp Letter of goodstanding 20260430.pdf | COMP | Corporate | `01_Compliance/Workers-Comp/` | No | **Current (expires 2026-04-30)** |
| WComp Letter of goodstanding 20270430.pdf | COMP | Corporate | `01_Compliance/Workers-Comp/` | No | **Future (expires 2027-04-30)** |
| 20250528 LOGS.pdf | — | — | Pending — identify content | — | Unknown |
| WComp Letter of goodstanding 20250430.pdf | COMP | Corporate | Skip — **EXPIRED** | — | Expired |
| bkp/ (5 historical letters 2021–2023) | COMP | Corporate | Skip — superseded | — | Historical |

---

## Section 2: Likely Duplicates Register

These groups contain the same underlying document in multiple copies, versions, or formats. **Migrate only the primary recommended version.**

| Duplicate Group | Files | Recommended Primary | Skip |
|---|---|---|---|
| **Oracle Cloud Certs** | `Consultant Certifications/Cloud/` vs `Legal Aid Tender/` vs `Oracle Certificates 2024/` | `Consultant Certifications/Cloud/` | Legal Aid Tender/ and Oracle Certificates 2024/ |
| **ETS Tender CVs** | `Rate Card/ETS Tender/[Name]/[Name]_cv.pdf` vs `Rate Card/[Name]_cv.pdf` | Root-level Rate Card/ CVs | ETS Tender/ copies |
| **ETS Tender Certs** | `Rate Card/ETS Tender/[Name]/eCertificate*.pdf` vs `Consultant Certifications/Cloud/` | `Consultant Certifications/Cloud/` | ETS Tender/ copies |
| **Oracle Partner Certs (annual)** | `Oracle Partner/Old/` (2011–2025) vs `Oracle Partner/` (2026) | `Oracle Partner/` (2026 current) | `Oracle Partner/Old/` → 99_Archive/ |
| **Adcock Ingram References** | Archive 2018 (×2) vs 2023 root vs Updated Support 2025 signed | Updated Support/0.Signed/ 2025 version | Archive and 2023 |
| **MTN References** | Archive 2018 vs 2025 root PDF vs Updated Support 2025 signed | Updated Support/0.Signed/ and `Reference 202507 MTN.pdf` | Archive 2018 |
| **WITS References** | Archive (×2) vs 2025 signed PDF vs template DOCX variants | Updated Support/0.Signed/ current signed | All others |
| **ARM References** | Archive 2018 vs Updated Support 2025 signed | Updated Support/0.Signed/ | Archive 2018 |
| **Assore References** | 2023 root PDF vs Updated Support 2025 signed | Updated Support/0.Signed/ | 2023 root |
| **Daan van der Merwe CV** | `Rate Card/Daan van der Merwe_cv.pdf` vs `Rate Card/ETS Tender/Daan Van Der Merwe/Daan van der Merwe_cv.pdf` | Root Rate Card/ version | ETS Tender/ copy |
| **Esna Pretorius CV** | Root Rate Card/ vs ETS Tender/ version | Root Rate Card/ (check which is newer) | ETS Tender/ copy |
| **Francois Terblanche CV** | Root Rate Card/ vs ETS Tender/ | Root Rate Card/ | ETS Tender/ copy |
| **Gavin Sadler CV** | Root Rate Card/ `Gavin Sadler_cv (3).pdf` vs ETS Tender/ | Root (version 3) | ETS Tender/ copy |
| **Ian de Koker CV** | Root `Ian de Koker_cv (2).pdf` vs ETS Tender/ | Root (version 2) | ETS Tender/ copy |
| **BEE Certificate** | Current PDF vs .zip file | PDF | .zip |
| **Bank Letters** | 14 total — 1 current | 2026-05-22 version | All 2021–2025 |
| **CSD Reports** | 9 total — 2 current | 2025-08-02 Detail + Summary | All older |
| **Tax Clearance** | bkp/ 2022–2025 vs current 2026 + future 2027 | 2026 + 2027 current | All bkp/ |
| **Workers Comp** | bkp/ 2021–2023 + expired 2025 vs current 2026 + future 2027 | 2026 + 2027 | All bkp/ + expired 2025 |
| **Disclosure Certificates** | 2023a + 2025 + 2026 + 2026 variant | 2026 and 2026 CM variant | 2023a + 2025 |
| **Resolution** | DOCX source + multiple PDF versions by year | 2025-03-01 PDF | All Old/ + DOCX |
| **Ordinary Share Certificates** | Current in Ordinary Shares/ vs Certified copies subfolder vs bkp | Ordinary Shares/ (cert nos 26–33) | Certified copies subfolder + bkp |
| **Company Profile** | 2020 + 2024 versions + 2025 versions | 2025 Oracle + 2025 Acumatica + 2024 International + 2024 DOCX | 2024 Oracle PDF + 2020 |
| **Supplier Portal Logins** | 3 copies (current + Old/ duplicates) | Exclude entirely | All |
| **Rate Cards** | Feb 2021 vs Jan 2020 vs 2022 | Use all 3 in 13_Quote_Generator/ for historical reference | None (all historical) |
| **SARB References** | 2 SARB references in Archive (SRT8 and Feb 2018) | Both unique — move to 99_Archive/ with notes | — |
| **WITS Reference Template DOCX** | `Template/WITS Reference Letter.docx` vs `Template/Wits Reference 202507.docx` vs 2 additional variants | Skip all — use signed PDFs | All 4 DOCX variants |

---

## Section 3: OCR Candidates

The following files are likely scanned PDFs requiring OCR before content is machine-readable. Prioritise OCR for high-value documents needed for tender responses.

**Priority 1 — High value, OCR needed before migration:**

| File | Reason OCR Suspected | KB Destination Post-OCR |
|---|---|---|
| `Registration Docs/Consolidated APPSolve Registration Documents.PDF` | All-caps .PDF extension, compiled registration bundle — typically scanned | `01_Compliance/Corporate/` |
| `References/Archive/` signed PDFs (2017–2020 era) | Physical letter + signature, era before digital signing | `99_Archive/References/` |
| `References/Archive/TCTA/` PDFs | Same era | `99_Archive/TCTA-Tender/` |
| `Certifications/Previous Certificates/` (older certs) | Pre-digital era certifications | Vary by cert validity |
| `Certifications/Certs/EMC/` (4 files) | Old EMC storage certs, 2000s era | `99_Archive/` |
| `VAT Registration/Vat Registration appsolve.pdf` | Original SARS letter, likely scanned | `01_Compliance/Tax/` |

**Priority 2 — Corporate, moderately useful:**

| File | Reason OCR Suspected | KB Destination Post-OCR |
|---|---|---|
| `Registration Docs/Cor 39.pdf` | CIPC registration doc, often scanned | `01_Compliance/Corporate/` |
| `Financial Statements/AFS 2018.pdf` | Signed AFS, pre-2021 likely scanned | `99_Archive/` |
| `Financial Statements/AFS 2019.pdf` | Same | `99_Archive/` |
| `Financial Statements/AFS 2020.pdf` | Same | `99_Archive/` |
| `Financial Statements/AFS 2021.pdf` | Signed AFS, transition era | `99_Archive/` |
| `Shareholding/Ordinary Shares/*.pdf` (share certificates) | Physical certificates, typically scanned | `01_Compliance/Corporate/` |
| `Org Chart/APPSolve Organogram Detail 202202_v2.pdf` | Possibly exported from Visio as image PDF | `99_Archive/` |
| `Company Profile/2020/*.pdf` | Older marketing PDF, may be image-based | `99_Archive/` |

**Priority 3 — Archive, low urgency:**

| File | Reason |
|---|---|
| Older BEE certificates (pre-2023) in `BEE/` | Physical BEE audit letters often scanned |
| `Tender Tracker/MBD Forms/MBD FORMS 2018-19.doc` | Old government forms |
| `References/Template/WITS Reference Letter_Appsolve1.pdf` | Scanned copy in template folder |
| `References/Archive/NHLS_Main_Reference.pdf` | Old reference, likely scanned |

**Total OCR candidates: ~28 files**

To process: copy to `12_OCR_Working/Needs_OCR/`, run OCR, save output to `12_OCR_Working/OCR_Complete/`, then migrate.

---

## Section 4: High-Value Priority Documents

Migrate these first. They are the most frequently required, highest-impact documents for tender responses.

### Tier 1 — Migrate Immediately (Compliance baseline — needed for every tender)

| Priority | File | Source Folder | KB Destination |
|---|---|---|---|
| 1 | Tax Clearance APPSolve_PIN 20260305.pdf | Tax Cert SARS/ | `01_Compliance/Tax/` |
| 2 | Tax Clearance APPSolve_PIN 20270223.pdf | Tax Cert SARS/ | `01_Compliance/Tax/` |
| 3 | BEE Level 3 Certificate (expires 2026-07-31).pdf | BEE/ | `01_Compliance/BEE/` |
| 4 | APPSolve CSD Detail 2025-08-02.pdf | CSD Report/ | `01_Compliance/CSD/` |
| 5 | APPSolve CSD Summary 2025-08-02.pdf | CSD Report/ | `01_Compliance/CSD/` |
| 6 | WComp Letter of goodstanding 20260430.pdf | Workmans Comp/ | `01_Compliance/Workers-Comp/` |
| 7 | WComp Letter of goodstanding 20270430.pdf | Workmans Comp/ | `01_Compliance/Workers-Comp/` |
| 8 | PI Certificate expires 2026-11-14.pdf | Insurance/ | `01_Compliance/Insurance/` |
| 9 | APPSolve Bank Letter 2026-05-22.pdf | Bank Letter/ | `01_Compliance/Corporate/` |
| 10 | SBD 4 DECLARATION OF INTEREST 20240515.pdf | SBD4 Declaration/ | `01_Compliance/Declarations/` |
| 11 | 20250301 Resolution signatures.pdf | Resolution/ | `01_Compliance/Corporate/` |
| 12 | Disclosure Certificate 2026.pdf | Registration Docs/ | `01_Compliance/Corporate/` |
| 13 | Employment Equity Certificate 2025.pdf | Employment Equity Cert/ | `01_Compliance/Employment-Equity/` |
| 14 | Vat Registration appsolve.pdf | VAT Registration/ | `01_Compliance/Tax/` |

### Tier 2 — Migrate First Week (Core capability and reference content)

| Priority | File | Source Folder | KB Destination |
|---|---|---|---|
| 15 | 7 × Signed Oracle reference letters (Adcock, ARM, Assore, Cape Union Mart, MTN, Nala, WITS) | References/0. Oracle.../Updated Support/0.Signed/ | `04_References/Oracle/` |
| 16 | 5 × Signed Acumatica reference letters (ATS, DSSSA, FuelU2, Interconnect, Maxiflex) | References/Acumatica References/Signed/ | `04_References/Acumatica/` |
| 17 | Root-level signed Oracle references (9 files — MTN 202507, Stellenbosch 2025, Investec 2023, Harmony 2024, Mr Price 2024, etc.) | References/ | `04_References/Oracle/` |
| 18 | Oracle Partner 2026.pdf + all 2026 expertise certs | Certifications/Oracle Partner/ | `05_Certifications/Oracle/Partner/` |
| 19 | APPSolve Company Profile - Oracle 2025.pdf | Company Profile/2025/ | `06_Capabilities/Oracle/` |
| 20 | APPSolve Company Profile - Acumatica 2025.pdf | Company Profile/2025/ | `06_Capabilities/Acumatica/` |
| 21 | APPSolve Company Profile (International) 2024.pdf | Company Profile/2024/ | `06_Capabilities/Cross/` |

### Tier 3 — Migrate Month 1 (Supporting credentials and personnel)

| Priority | Content Group | Action |
|---|---|---|
| 22 | All ~40 Consultant Certifications/Cloud/ Oracle Cloud certs | `05_Certifications/Oracle/Cloud/[module]/` |
| 23 | All ~15 Consultant Certifications/EBS/ Oracle EBS certs | `05_Certifications/Oracle/EBS/[role]/` |
| 24 | 2 Acumatica certs (Wanda van der Merwe) | `05_Certifications/Acumatica/` |
| 25 | ~~All ~42 consultant CVs in Rate Card/ root~~ | ~~`03_CVs/[BU after content review]/`~~ — **⛔ CANCELLED by ADR-001 (2026-06-10).** CV documents are not migrated to the KB. APPTime is authoritative. Consultant Index Records created separately — see CONSULTANT_INDEX_PROGRAMME.md. |
| 26 | 3 historical proposals in Template Proposals/ | `09_Active_Tenders/Submitted/Historical/` |
| 27 | Oracle endorsement letters (AppSolve_Reference Letter_02092024.pdf, Reference 2024 Oracle Letter.pdf) | `04_References/Oracle/` |
| 28 | ORC References (Hollywoodbets, Mr Price) | `04_References/Oracle/` |
| 29 | AFS 2025 + AFS 2024 | `01_Compliance/Financial-Statements/` |
| 30 | Organogram 202405_v1_bbbee.pdf | `01_Compliance/Corporate/` |

---

## Section 5: Outstanding Reference Letters (Action Required)

Based on the unsigned DOCX templates found, the following reference letters appear to be outstanding (template exists, no signed PDF found):

### Oracle / Support clients
| Client | Template Location | Action |
|---|---|---|
| ATC | `Updated Support References/ATC Reference 202507.docx` | Chase client for signature |
| Old Mutual | `Updated Support References/Old Mutual Reference 202507.docx` | Chase client for signature |
| Truworths | `Updated Support References/Truworths Reference 202507.docx` | Chase client for signature |

### Acumatica clients
| Client | Template Location | Action |
|---|---|---|
| At Source | `Acumatica References/Templates/At Source_Acumatica_Reference.docx` | Chase client |
| Chemunique | Templates/ | Chase client |
| Dukathole | Templates/ | Chase client |
| Dunlop Srixon Sport | Templates/ | Chase client |
| Linebooker | Templates/ | Chase client |
| Milpark | Templates/ | Chase client |
| Prommac | Templates/ | Chase client |
| Terbodore | Templates/ | Chase client |
| Truman and Orange | Templates/ | Chase client |
| USB-ED | Templates/ | Chase client |

### BeBanking clients (potential)
| Client | Template Location | Action |
|---|---|---|
| Tiger Brands (BeBanking SAP) | `References/Template/Tiger Reference Letter BeBanking SAP.docx` | Investigate — is a signed version available? |
| SAA (SAP Integration) | `References/Template/SAA Tiger Reference Letter SAP Integration.docx` | Investigate |

---

## Section 6: Files to Exclude from KB

These files should **not** be migrated to the Knowledge Base for the reasons stated.

| File / Group | Reason |
|---|---|
| All `.DS_Store` files (~5) | macOS system metadata |
| `tender_pack_files.txt` | This inventory file — not a document |
| `Supplier Portal Logins/` (all 3 files) | Contains credentials — security risk |
| `Municipal and Lease Information/` (all files) | Property/utility documents, minimal tender relevance |
| `QSE/Imbasa/` and `QSE/Intecon/` | Third-party company documents — not APPSolve credentials |
| All `bkp/` subfolders | Backup copies superseded by current versions |
| All `Old/` subfolders | Historical, superseded |
| `References/Archive/` | Historical — move to `99_Archive/`, not active `04_References/` |
| `Rate Card/ETS Tender/` CVs + certs | Duplicates of master sets |
| `Certifications/Legal Aid Tender/` | Duplicate of master set |
| `Certifications/Oracle Certificates 2024/` | Duplicate of master set |
| Unsigned reference letter DOCX templates (both Oracle and Acumatica `Templates/` folders) | Working documents — not final signed references |
| `References/Template/` (blank templates) | Internal working docs — not signed references |
| `References/Updated Support References/emails/` (.msg files) | Email correspondence — not primary documents |
| `Company Info/appsolve info.txt` | Minimal content |
| `Tender Tracker/Tender Tracker.xlsx` | Operational tool, not a KB document |
| `Rate Card/AF Resources CV.xlsx` | CV formatting template |
| `Org Chart/Rate Card - Feb21.xlsx` | Historical — use 13_Quote_Generator/ |
| Insurance PI Certificate expires 2025-11-14.pdf | Expired Nov 2025 |
| WComp Letter of goodstanding 20250430.pdf | Expired Apr 2025 |
| Utility Bill/September 2020.pdf | Outdated |
| `Shareholding/Ordinary Shares/Certified Ordinary shares/` | Duplicate of current share certs |
| SBD 4 DECLARATION OF INTEREST.pdf (undated) | Use dated 20240515 version |
| `References/Template/KPMG Reference Letter-Surface1.docx` | Duplicate of KPMG template |
| `Company Profile/2024/APPSolve Company Profile Oracle 2024.pdf` | Superseded by 2025 version |

---

## Migration Readiness Summary

| Folder | Current Docs Ready | Needs OCR First | Pending Review | Skip/Archive |
|---|---|---|---|---|
| 01_Compliance/Tax/ | 3 | 1 (VAT Reg) | — | 5 (bkp) |
| 01_Compliance/BEE/ | 1 (expiring) | — | — | 9 (old) |
| 01_Compliance/CSD/ | 2 | — | — | 7 (old) |
| 01_Compliance/Insurance/ | 1 | — | — | 2 (expired/old) |
| 01_Compliance/Workers-Comp/ | 2 | — | 1 (LOGS.pdf) | 6 (expired/bkp) |
| 01_Compliance/Corporate/ | ~15 | 2 | — | ~20 (bkp/old) |
| 01_Compliance/Declarations/ | 6 | — | — | 2 (old) |
| 01_Compliance/Financial-Statements/ | 2–4 | 4 (2018–2021) | — | — |
| 03_CVs/ | **0 — CANCELLED (ADR-001 2026-06-10)** | — | — | CV documents not migrated to KB. `03_People/Resource_Profiles/` receives Consultant Index Records (metadata only) instead. See CONSULTANT_INDEX_PROGRAMME.md. |
| 04_References/Oracle/ | ~20 | ~12 (Archive) | 3 (outstanding) | ~30 (templates/dupes) |
| 04_References/Acumatica/ | 5 | — | 10 (outstanding) | 13 (unsigned) |
| 04_References/BeBanking/ | 2 (BankServ, FNB) | 2 (old) | 2 (Tiger, SAA) | — |
| 05_Certifications/Oracle/ | ~55 | ~20 (Previous Certs) | ~20 (review needed) | ~38 (dupes) |
| 05_Certifications/Acumatica/ | 2 | — | — | — |
| 06_Capabilities/ | ~6 | — | — | 1 (2020 profile) |
| 09_Active_Tenders/ | 3 (proposals) | — | — | — |
| 13_Quote_Generator/ | 4 (rate cards) | — | — | — |
| 99_Archive/ | — | — | — | ~185 |

---

*End of Migration Analysis. No files were copied, moved, renamed, or modified during this analysis.*
*Next step: Human review of this report → confirm Tier 1 migration list → begin OCR on identified candidates → copy Tier 1 compliance docs.*
