---
document_id: ERP_APPROVAL_CHANGE_LOG
title: "Oracle ERP Assumptions — BU Lead Approval Change Log"
version: "1.0"
created: "2026-06-15"
tracks: "ERP_ASSUMPTIONS_V1.md"
---

# Oracle ERP Assumptions — BU Lead Approval Change Log

This log records the eight BU Lead decisions applied during WP11D-A that promoted `ERP_ASSUMPTIONS_V1.md` from Draft to Approved v1.0 on 2026-06-15.

---

## Change Summary

| Change # | Assumption ID | Change Type | BU Decision | Summary |
|---|---|---|---|---|
| CL-ERP-001 | ERP-GL-001 | Modified | BU-ERP-001 | Secondary ledgers explicitly excluded from base scope; separately scoped and priced |
| CL-ERP-002 | ERP-GL-006 | Modified | BU-ERP-002 | Intercompany accounting excluded from base GL scope; basic balancing segment may be included |
| CL-ERP-003 | ERP-AP-003 | Modified | BU-ERP-003 | Three-way match confirmed as APPSolve default; two-way match conditions tightened |
| CL-ERP-004 | ERP-FA-002 | Modified | BU-ERP-004 | Opening balance only confirmed; current asset register required from customer |
| CL-ERP-005 | ERP-CUT-005 | Modified | BU-ERP-005 | Parallel running excluded; short controlled validation period may be included if explicitly stated |
| CL-ERP-006 | ERP-INT-005 / ERP-EXC-003 | Modified | BU-ERP-006 | SARS eFiling excluded unless custom integration scoped; OTBI tax extracts may be included |
| CL-ERP-007 | ERP-DAT-006 | Modified | BU-ERP-007 | Two mock migrations plus final confirmed as standard; additional cycles require change control |
| CL-ERP-008 | ERP-SEC-006 | Modified | BU-ERP-008 | SSO excluded by default; Azure AD/Entra ID SSO may be included as explicitly listed item |
| CL-ERP-009 | Frontmatter | Updated | All 8 decisions | Status: Draft → Approved; approved_by/date set; bu_lead_decisions_applied recorded |
| CL-ERP-010 | ERP_ASSUMPTION_REGISTER.csv | Updated | All 8 decisions | All 128 rows: Status Draft → Active; 8 BU-ERP pending labels removed |

---

## Detailed Change Records

### CL-ERP-001 — ERP-GL-001 (BU-ERP-001)

**Change type:** Modified  
**Before:** "Secondary ledgers... require additional design and configuration effort and are assessed as a scope addition unless explicitly in the agreed design." — ambiguous; the qualifier "unless explicitly in the agreed design" left the door open for clients to argue that their secondary ledger was implicitly in scope if the design happened to mention it.  
**After:** Secondary ledgers are "excluded from base scope unless explicitly listed in the proposal and SOW." Where required, their effort "is separately assessed and priced."  
**Commercial reason:** Secondary ledgers (used for IFRS vs local GAAP, reporting currency, or management vs statutory accounting) are materially more complex than a primary ledger — they require separate accounting rules, separate chart of account mapping, separate reconciliation, and separate FRS reporting. Including them in base scope without explicit pricing has caused project overruns. The new wording makes it contract-level explicit: if it's not named in the SOW, it's not in scope.  
**Risk mitigated:** Client with a holding company structure expects local GAAP secondary ledger and IFRS primary ledger in base scope; secondary ledger is configured and tested without a CR; margin eroded.

---

### CL-ERP-002 — ERP-GL-006 (BU-ERP-002)

**Change type:** Modified  
**Before:** "Standard intercompany accounting... is included in the standard GL scope where the client has multiple legal entities in scope." — this created an obligation to deliver intercompany accounting for any multi-entity client.  
**After:** "Intercompany accounting is excluded from base GL scope unless explicitly listed in the proposal." Basic balancing segment design may be included (Oracle requires a primary balancing segment to be set up in the COA — this is always done and costs negligible effort). Full intercompany scope "requires a separately scoped and priced engagement."  
**Commercial reason:** Intercompany accounting in Oracle ERP involves intercompany accounting rules, intercompany invoicing (Oracle Fusion Intercompany), intercompany reconciliation workflows, multi-lateral netting, and consolidation eliminations. This is a significant standalone sub-project for a multi-entity client. Treating it as a base GL inclusion creates scope commitments that are not priced.  
**Risk mitigated:** A client with three legal entities and intercompany transactions claims that intercompany accounting is in scope under "standard GL" and refuses a CR; APPSolve absorbs intercompany implementation effort.

---

### CL-ERP-003 — ERP-AP-003 (BU-ERP-003)

**Change type:** Modified  
**Before:** "Three-way match... is the default matching approach... Where goods receipt processing (Oracle Receiving) is not in scope, two-way match... is used." — already directionally correct; refined to add the second condition under which two-way match may be used (client explicitly confirms their process does not use goods receipts).  
**After:** Three-way match is the default where both Procurement AND Receiving are in BOM scope. Two-way match only where: (a) Oracle Receiving is not in the BOM; OR (b) client explicitly confirms their purchasing process does not use GRN confirmation. The matching approach is documented in the AP configuration design.  
**Commercial reason:** Three-way match is the correct control environment for most clients; it also protects APPSolve because three-way match requires proper Receiving setup and generates less post-go-live AP query volume. Two-way match is only appropriate where the client genuinely does not use goods receipts (e.g., services-only businesses). Documenting the decision in the configuration design creates an audit trail.  
**Risk mitigated:** Client bypasses Oracle Receiving to save time; AP invoices are paid without goods receipt confirmation; client disputes invoice payment control failure and implicates APPSolve's configuration.

---

### CL-ERP-004 — ERP-FA-002 (BU-ERP-004)

**Change type:** Modified  
**Before:** Opening balance migration described but did not explicitly require the client to provide a current, reconciled asset register; did not state that migration cannot proceed without it.  
**After:** Added: "The client is required to provide the current, reconciled asset register (including cost, accumulated depreciation, and NBV per asset) before migration commences. Migration cannot proceed without a client-approved asset register."  
**Commercial reason:** The most common FA migration delay is the client providing an unreconciled, incomplete, or internally disputed asset register. If migration proceeds with a bad register, the FA book in Oracle will never reconcile to the client's trial balance. Making the client's asset register a formal prerequisite — explicitly stated as a blocker for migration to commence — creates a contractual dependency that protects the project timeline.  
**Risk mitigated:** APPSolve loads the asset register provided by the client; post-go-live the client disputes the FA balance because their own register was incorrect; they expect APPSolve to reload without a CR.

---

### CL-ERP-005 — ERP-CUT-005 (BU-ERP-005)

**Change type:** Modified  
**Before:** Parallel running excluded. Where client requires it, assessed as scope addition. — no nuance between a short validation check and a full parallel close cycle.  
**After:** Three tiers defined:
1. Excluded by default (no mention in proposal = not in scope)
2. Short controlled validation period (5–10 business days, trial balance / opening balance verification only) — may be included where explicitly stated in the proposal scope section
3. Full parallel financial close cycles — excluded unless separately scoped and priced  
**Commercial reason:** The BU Lead's decision reflects a practical position: some clients need a few days to validate opening balances against their legacy system before fully cutting over. This is a legitimate, low-effort activity that can be included if explicitly named. A full parallel close (running all month-end journals, reconciliations, and reports in both systems) is an entirely different magnitude of work and must always be separately priced.  
**Risk mitigated:** Client interprets "validation period" as a full parallel month-end close; APPSolve must support dual-system operations for a full month without a CR.

---

### CL-ERP-006 — ERP-INT-005 / ERP-EXC-003 (BU-ERP-006)

**Change type:** Modified  
**Before:** SARS eFiling excluded. — simple exclusion with no nuance about what IS includable.  
**After:** Two-part clarification:
1. SARS eFiling integration is "not an APPSolve standard ERP capability" — confirms APPSolve has no product or partner for automated eFiling
2. Tax reporting data extracts via OTBI — OTBI VAT reports or GL tax reports to support the client's manual eFiling process — "may be included in scope where explicitly listed in the proposal"  
**Commercial reason:** Clients frequently ask about SARS integration. The clear answer is: no automated eFiling integration. However, OTBI-based tax reports to support manual eFiling are standard Oracle ERP output and can be included in the OTBI report list. Making this explicit prevents the exclusion from being read as "APPSolve will not help you with tax reporting at all."  
**Risk mitigated:** Client reads "SARS eFiling excluded" as meaning no tax reporting; then at go-live asks why there's no VAT report in Oracle; claims it was excluded by APPSolve.

---

### CL-ERP-007 — ERP-DAT-006 (BU-ERP-007)

**Change type:** Modified  
**Before:** "Two data migration cycles are standard: (1) Mock Migration... (2) Final Migration." — the draft said two cycles but ambiguously described them as "Mock" and "Final" with only one mock.  
**After:** Explicitly named as: Mock Migration 1 + Mock Migration 2 + Final Migration = 3 total events, 2 mock cycles. This is the standard base scope. Additional cycles beyond 2 mocks require change control.  
**Commercial reason:** The BU Lead confirmed that two mock cycles is the standard (not one). This is important because mock cycles are a significant time and resource investment — the client's data team must extract, correct, and re-provide data between each mock. Naming two mocks as the standard gives both APPSolve and the client a clear expectation of how many data correction cycles are included before the final production load.  
**Risk mitigated:** APPSolve scopes one mock migration; client data quality requires three correction cycles; two additional mock loads must be done without a CR.

---

### CL-ERP-008 — ERP-SEC-006 (BU-ERP-008)

**Change type:** Modified  
**Before:** SSO "assessed as a separately scoped item" — left open whether it could be included or not.  
**After:** SSO is "excluded by default unless explicitly scoped." Azure AD / Entra ID SSO with Oracle Fusion may be included "as a separately listed configuration activity" where the client's licensing supports it. Other IdPs (Okta, Ping, Google, ADFS) assessed per environment. Client IT must provide federation metadata and co-ordinate certificates.  
**Commercial reason:** Azure AD + Oracle Fusion SAML 2.0 SSO is a well-understood, relatively contained configuration task that can reasonably be included in a proposal where both conditions are met: (a) client uses Azure AD/Entra ID; (b) Oracle Fusion licensing supports SAML 2.0 federation. Making this includable — but requiring explicit listing — allows APPSolve to price it as a separate line item rather than embedding it as a hidden assumption. Other IdPs are less predictable and should always be assessed.  
**Risk mitigated:** Client expects SSO to work on day 1 without it being priced or designed; Oracle ERP goes live without SSO; client demands it immediately post-go-live under the original contract.

---

### CL-ERP-009 — Frontmatter

**Change type:** Updated  
- `status`: Draft — Pending BU Lead Approval → **Approved**  
- `approved_by`: blank → **BU Lead — Oracle Practice**  
- `approved_date`: blank → **2026-06-15**  
- `approved_for_reuse`: false → **true**  
- `bu_lead_review_items`: removed (all 8 items closed)  
- `bu_lead_decisions_applied`: added (all 8 decisions recorded with affected assumptions)

---

### CL-ERP-010 — ERP_ASSUMPTION_REGISTER.csv

**Change type:** Updated  
All 128 rows: Status column updated from `Draft` / `Draft (BU-ERP-XXX pending)` → `Active`  
8 rows with BU-ERP pending labels: labels removed and status set to Active  
Register now reflects the approved state of the full ERP pack.

---

## Impact Assessment — Existing Proposals

No proposals were issued using ERP assumptions while in Draft status (ERP pack was created and approved in the same cycle). No retroactive proposal updates required.

**Future proposals:** All Oracle ERP proposals issued after 2026-06-15 must use this Approved pack. Key commercial defaults now active:
- Secondary ledgers excluded from base scope unless named in SOW (ERP-GL-001)
- Intercompany accounting excluded from base GL scope; basic balancing segment only (ERP-GL-006)
- Three-way match is the APPSolve default for PO-based invoices (ERP-AP-003)
- Fixed asset migration = opening balance only; current asset register required from customer (ERP-FA-002)
- Parallel running excluded; short validation period only if explicitly in proposal (ERP-CUT-005)
- SARS eFiling integration excluded; OTBI tax extracts may be included if listed (ERP-INT-005, ERP-EXC-003)
- Two mock migrations plus final migration is the base scope (ERP-DAT-006)
- SSO excluded by default; Azure AD included only as explicitly listed item (ERP-SEC-006)

---

*ERP_APPROVAL_CHANGE_LOG v1.0 | WP11D-A — Oracle ERP Assumptions Approval | 2026-06-15*  
*10 changes applied | 8 BU decisions closed | ERP pack promoted to Approved*
