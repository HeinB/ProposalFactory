# Automation Readiness Scorecard — WP6
**Work Package:** WP6 — Tender Simulation & Coverage Assessment | **Version:** 1.0 | **Created:** 2026-06-14
**Pilot basis:** AFROSAI-E Acumatica Proposal May 2026 + 47-asset KB assessment
**Purpose:** Score the current KB across five dimensions to establish an automation readiness baseline and identify where investment will deliver the greatest return.

---

## Scoring Method

Each dimension scored 0-100 based on observable evidence from the KB and the AFROSAI-E pilot simulation. Scores reflect the current state (2026-06-14). The dimension weight reflects its relative importance to automating tender response generation.

| Dimension | Weight | Score | Weighted |
|---|---|---|---|
| 1. Content Coverage | 35% | 68 | 23.8 |
| 2. Evidence Quality | 25% | 82 | 20.5 |
| 3. Reference Coverage | 15% | 44 | 6.6 |
| 4. Governance Maturity | 15% | 91 | 13.7 |
| 5. Automation Readiness | 10% | 38 | 3.8 |
| **OVERALL** | **100%** | | **68.4** |

**Overall Automation Readiness Score: 68 / 100**

---

## Dimension 1 — Content Coverage (Score: 68/100)

**What it measures:** Does the KB have approved assets that address the question types encountered in real tenders?

### Evidence

| Tender Type | Coverage | Score |
|---|---|---|
| BeBanking / H2H | ~95% narrative | 95 |
| Oracle EBS / DBA | ~90% narrative | 90 |
| Oracle HCM | ~85% narrative | 85 |
| Oracle ERP (Fusion) | ~75% narrative | 75 |
| Acumatica ERP | ~56% narrative (AFROSAI-E pilot) | 56 |
| Mixed Multi-Platform | ~75% narrative | 75 |

**Weighted average across 6 tender types (by estimated pipeline volume):**
Assuming pipeline split: Acumatica 40%, Oracle HCM 25%, Oracle ERP 15%, Oracle EBS/DBA 10%, BeBanking 5%, Mixed 5%:
- Weighted: (56×0.4) + (85×0.25) + (75×0.15) + (90×0.10) + (95×0.05) + (75×0.05) = 22.4 + 21.25 + 11.25 + 9 + 4.75 + 3.75 = **72.4%**

**Score: 68** — Adjusted slightly below the weighted average because Acumatica (largest pipeline share) has the most material gap (support model).

### Breakdown by gap type

| Gap type | Count | Impact on score |
|---|---|---|
| Content does not exist (C-GAP) | 6 gaps identified | -15 points |
| Content exists but needs de-branding (B-class) | ~11 questions | -8 points |
| Content exists and is directly usable (A-class) | 8 fully answerable | Baseline |

### What would move this score

| Action | Score improvement |
|---|---|
| Author W5-ACU-001 (support model) | +8 points |
| De-brand W2S1-005 into platform-agnostic methodology | +4 points |
| Author Acumatica security statement | +2 points |
| Register Oracle reference letters (Oracle ERP coverage) | +2 points |
| **Total achievable at 80% coverage target** | **+16 → Score: 84** |

---

## Dimension 2 — Evidence Quality (Score: 82/100)

**What it measures:** Are the claims in approved KB assets supported by confirmed Tier 1 or Tier 2 evidence? How defensible is the content in a scored or audited procurement?

### Evidence

**Tier distribution across 47 approved assets:**

| Evidence Tier | Definition | Assets | % |
|---|---|---|---|
| Tier 1 (Confirmed Delivery) | Client accepted delivery; in production | ~30 | 64% |
| Tier 1A (Rule 21.4 — internal confirmation only) | Delivery confirmed; client cannot be named | ~3 | 6% |
| Tier 2 (Active Implementation / Platform Capability) | Delivery in progress or platform-level evidence | ~10 | 21% |
| Tier 2 with active exception (WP3-EX) | Formally registered Tier 2 exception | 2 | 4% |
| PoC / Proof of Concept | Only PoC evidence | 1 (retired W4-HCM-004) | N/A |
| Not yet confirmed (AM exceptions) | Tier 1 evidence but letters pending | 3 | 6% |

**Strengths:**
- 70% of assets are Tier 1 confirmed delivery (strongest evidence tier)
- All assets have been through formal BU Lead approval (not just AI extraction)
- Evidence claims have been verified — AI-introduced hallucinations identified and corrected (W1S2-004 table corrections; W1S2-009 intercompany row removed)
- Source documents are registered in DOCUMENT_REGISTER.csv with HIST identifiers

**Weaknesses:**
- W4-ERP-001/002/003: Tier 1 evidence exists but letters not registered → effective usability = Tier 2 until letters registered
- W3S1-005 (Workforce Compensation): WP3-EX-001 active — no referenceable client (Redpath Mining in pipeline)
- W1S2-007 (Acumatica PaySpace): WP3-EX-003 active — no reference clients

**Score: 82** — High because the majority of assets have strong Tier 1 evidence and a rigorous approval process. Adjusted down 18 points for the 3 ERP assets with pending letters and 2 active Tier 2 exceptions.

### What would move this score

| Action | Score improvement |
|---|---|
| Register Oracle reference letters (converts 3 AM exceptions to fully usable) | +5 points |
| Redpath Mining go-live + upgrade W3S1-005 to Tier 1 | +3 points |
| First Acumatica PaySpace live integration + reference (WP3-EX-003) | +2 points |
| **Score after reference letter registration** | **+5 → Score: 87** |

---

## Dimension 3 — Reference Coverage (Score: 44/100)

**What it measures:** Can the KB support named, referenceable clients in external submissions across all major tender types?

### Evidence

**Reference status by product area:**

| Product Area | Referenceable Clients (approved in KB) | Restrictions Active |
|---|---|---|
| Oracle HCM | Hollywood Bets (AM approval per tender); Mr Price Learning Cloud; Afrocentric (Tier 1 — not named externally) | Yes — AM approval required |
| Oracle EBS | ARM, Assore, Adcock Ingram, Harmony Gold, Investec | 0 — strongest reference set |
| Oracle ERP (Fusion) | None yet (Investec/NALA/CUM — letters pending) | AM-W4E1-001, AM-W4E2-001, AM-W4E3-001 all ACTIVE |
| Oracle Integration / OIC | Hollywood Bets (AM approval per tender) | Yes — AM approval required |
| Acumatica | Interconnect Systems only | DSSSA/FuelU2/Maxiflex letters not registered |
| BeBanking | SITA (explicit); HyDac (implicit from sources) | No formal letter registered in KB |

**Score: 44** — Oracle EBS reference set is strong (score: 80+). Oracle HCM has references but requires per-tender AM approval (score: 60). Oracle ERP Fusion has zero usable named references currently (score: 10). Acumatica has 1 confirmed client (score: 30). BeBanking references are weak despite strong capability (score: 35).

**This is the lowest-scoring dimension and represents the biggest single gap relative to effort required to close it.**

### What would move this score

| Action | Score improvement |
|---|---|
| Register Oracle ERP reference letters (Investec, NALA, CUM, KPMG) | +18 points |
| Register Acumatica reference letters (DSSSA, FuelU2, Maxiflex) | +8 points |
| Register BeBanking reference letters (SITA formal, HyDac) | +4 points |
| **Score after all registrations** | **+30 → Score: 74** |
| **Effort required** | **Very Low — 1-2 days total** |

**Reference letter registration is the highest-return, lowest-effort action available. It lifts the lowest-scoring dimension by 30 points for minimal effort.**

---

## Dimension 4 — Governance Maturity (Score: 91/100)

**What it measures:** Does the KB have clear rules, restrictions, and checkpoints that prevent governance failures in tender submissions?

### Evidence

**Governance framework elements present:**

| Element | Status |
|---|---|
| Formal approval process (BU Lead only; `approved_for_reuse: Yes` by BU Lead) | ✅ Fully operational |
| 20+ named governance rules (Rule 21.1, 21.4, 21.5; CROSS-1; etc.) | ✅ Documented in ORACLE_FACT_BASELINE + capability files |
| Active restriction register (AM-W4E1 through AM-W4E3; WP3-EX-001/003) | ✅ Formally registered |
| Section exclusion rules (14.2, 13.2, DFA, SAA, CCBA) | ✅ Embedded in each affected asset + governance checklist |
| Evidence tier classification (Tier 1, 1A, 2; Rule 21.5 pipeline) | ✅ Applied to all assets |
| Source registration requirement (Rule 6 — HIST identifiers) | ✅ Applied across KB |
| DOCUMENT_REGISTER.csv | ✅ Present |
| EXTRACTION_LOG.csv | ✅ 51 rows — complete |
| MASTER_CAPABILITY_INDEX.md | ✅ v1.1 — 47 assets |
| Standard Governance Checkpoint (ANSWER_ASSEMBLY_FRAMEWORK.md) | ✅ Written and ready for use |
| CV sourcing architecture (ADR-001) | ✅ Formally decided |

**Governance gaps identified:**
- ORACLE_FACT_BASELINE Section 4.3 KPMG source docs not yet registered as HIST assets (AM-W4E3-002 open)
- No automated governance scan (only manual checklist — Phase 3 of TENDER_AUTOMATION_ROADMAP)
- Compliance document register (Tax, BEE, CSD) not yet formal (GAP noted in WP6)

**Score: 91** — Best-performing dimension. The governance framework is comprehensive, documented, and enforced. Adjusted down 9 points for three open items (KPMG Rule 6, no automated scan, no compliance document register).

---

## Dimension 5 — Automation Readiness (Score: 38/100)

**What it measures:** How close is the current KB to enabling an AI assistant to generate first-draft tender responses with minimal human input?

### Evidence

| Automation requirement | Current state |
|---|---|
| All KB assets in machine-readable format (Markdown) | ✅ Yes — all 47 assets in .md |
| Assets structured with consistent frontmatter | ✅ Yes — YAML frontmatter on all assets |
| Assembly framework documented | ✅ Yes — ANSWER_ASSEMBLY_FRAMEWORK.md (8 recipes) |
| Question-to-asset mapping documented | ✅ Yes — TENDER_QUESTION_TAXONOMY.md (~80 patterns) |
| AI prompting framework | ❌ No — not yet built |
| Automated governance check | ❌ No — manual checklist only |
| Reference letter register integration | ❌ No — 04_References/ is empty (letters not registered) |
| Platform-agnostic methodology available | ❌ No — W2S1-005 is Oracle-specific |
| Acumatica support model | ❌ No — GAP-001 |
| Compliance document register | ❌ No |
| Tender Briefing Template | ❌ No |
| AI input interface / pipeline | ❌ No |

**Score: 38** — The KB is structured for human use and has good asset coverage, but the AI-enablement layer does not yet exist. The assembly framework and question taxonomy are the right foundations. The missing elements are the prompt library, reference integration, and Acumatica gaps.

**This score is expected at Phase 1 of the TENDER_AUTOMATION_ROADMAP — it reflects "structured for AI" not "running on AI."**

### What would move this score

| Action | Score improvement |
|---|---|
| Register reference letters (04_References/ populated) | +8 points |
| De-brand W2S1-005 into platform-agnostic methodology | +6 points |
| Build prompt library (Phase 2 TENDER_AUTOMATION_ROADMAP) | +12 points |
| Author W5-ACU-001 support model | +6 points |
| Implement Tender Briefing Template | +5 points |
| **Score at Phase 2 completion** | **+37 → Score: 75** |

---

## Overall Scorecard Summary

| Dimension | Weight | Current | Target (80% auto) | Target (90% auto) |
|---|---|---|---|---|
| 1. Content Coverage | 35% | 68 | 82 | 91 |
| 2. Evidence Quality | 25% | 82 | 87 | 92 |
| 3. Reference Coverage | 15% | 44 | 74 | 82 |
| 4. Governance Maturity | 15% | 91 | 93 | 96 |
| 5. Automation Readiness | 10% | 38 | 72 | 88 |
| **OVERALL** | | **68** | **80** | **90** |

---

## Roadmap to 80% Score

The following actions, in priority order, close the 68 → 80 gap (+12 points):

| # | Action | Dimension | Points gained | Effort |
|---|---|---|---|---|
| 1 | Register Oracle ERP reference letters | Ref Coverage, Content | +5 | Very Low |
| 2 | Register Acumatica reference letters | Ref Coverage | +3 | Very Low |
| 3 | De-brand W2S1-005 (platform-agnostic methodology) | Content, Automation | +2 | Low |
| 4 | Author W5-ACU-001 Acumatica support model | Content, Automation | +2 | Medium |
| **Total** | | | **+12** | |

**Conclusion: 80% automation readiness is achievable within 2-4 weeks with the actions above.**

---

## Roadmap to 90% Score

Reaching 90% requires completing all Phase 2 TENDER_AUTOMATION_ROADMAP actions:

| # | Action | Dimension | Points gained | Effort |
|---|---|---|---|---|
| All 80% actions | (above) | Multiple | +12 | 2-4 weeks |
| 5 | Build AI prompt library | Automation | +8 | Medium |
| 6 | Author Acumatica security statement | Content | +2 | Low |
| 7 | Author platform-agnostic OCM statement | Content | +1 | Low |
| 8 | Author Acumatica cloud hosting statement | Content | +1 | Low |
| 9 | Implement Tender Briefing Template | Automation | +3 | Low |
| 10 | Register BeBanking reference letters | Ref Coverage | +2 | Low |
| 11 | Wave 5 targeted extraction (1-2 assets) | Content, Evidence | +1 | Medium |
| **Total** | | | **+22 → 90** | |

**Conclusion: 90% automation readiness requires completing Phases 1 and 2 of the TENDER_AUTOMATION_ROADMAP (approximately Q3 2026).**

---

*AUTOMATION_READINESS_SCORECARD.md v1.0 — WP6 2026-06-14. Overall score: 68/100. 80% achievable in 2-4 weeks with reference registration + 2 content items. 90% achievable by Q3 2026 with Phase 2 automation layer.*
