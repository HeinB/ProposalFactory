---
document_id: OIC_APPROVAL_CHANGE_LOG
title: "OIC Assumptions — BU Lead Approval Change Log"
version: "1.0"
created: "2026-06-15"
tracks: "OIC_ASSUMPTIONS_V1.md"
---

# OIC Assumptions — BU Lead Approval Change Log

This log records the seven BU Lead decisions applied during WP11C-A that promoted `OIC_ASSUMPTIONS_V1.md` from Draft to Approved v1.0 on 2026-06-15.

---

## Change Summary

| Change # | Assumption ID | Change Type | BU Decision | Summary |
|---|---|---|---|---|
| CL-OIC-001 | OIC-SCP-002 | Modified | BU-OIC-001 | Integration definition confirmed: one directional flow = one integration |
| CL-OIC-002 | OIC-SCP-005 | Modified | BU-OIC-002 | 1 Production + 1 non-production OIC environment; APPSolve does not license |
| CL-OIC-003 | OIC-MON-002 | Modified | BU-OIC-003 | Error notifications: customer mailbox + APPSolve during hypercare only |
| CL-OIC-004 | OIC-SUP-002 | Modified | BU-OIC-004 | OIC hypercare concurrent with primary project hypercare; 4-week default |
| CL-OIC-005 | OIC-CON-006 | Modified | BU-OIC-005 | Simple/Standard/Complex tier definitions confirmed |
| CL-OIC-006 | OIC-DES-007 | Modified | BU-OIC-006 | No automatic accelerator discounts; per-integration assessment required |
| CL-OIC-007 | OIC-DES-005 | Modified | BU-OIC-007 | SFTP standard fallback confirmed; subject to customer security approval |
| CL-OIC-008 | Frontmatter | Updated | All 7 decisions | Status: Draft → Approved; approved_by/date set; bu_lead_decisions_applied recorded |
| CL-OIC-009 | OIC_ASSUMPTION_REGISTER.csv | Updated | All 7 decisions | All 101 rows: Status Draft → Active; 7 BU-OIC pending labels removed |
| CL-OIC-010 | OIC_IMPLEMENTATION_PATTERNS.md | Updated | BU-OIC-005 / BU-OIC-006 | Section 6 confirmed tier definitions; Section 7 accelerator disclaimer updated |

---

## Detailed Change Records

### CL-OIC-001 — OIC-SCP-002 (BU-OIC-001)

**Change type:** Modified  
**Before:** "One integration is defined as one directional data flow... An integration that also returns an acknowledgement or response from System B to System A is a second integration." — the wording "also returns" was ambiguous and could be read as a subordinate action of the same integration.  
**After:** Explicit statement: "An integration that returns data from System B to System A is a second, separate integration — two integrations must therefore be scoped, estimated, and priced where a bidirectional flow is required." Added the word "priced" to make the commercial implication explicit.  
**Commercial reason:** The most common OIC scope dispute: client describes a bidirectional flow as "one integration" and disputes the line item count when the estimate shows two. The new wording makes it unambiguous that A→B and B→A are two separately priced items.  
**Risk mitigated:** Client disputes that a PaySpace↔HCM bidirectional flow should cost the same as a single-direction flow; expects two-for-one pricing.

---

### CL-OIC-002 — OIC-SCP-005 (BU-OIC-002)

**Change type:** Modified  
**Before:** "Oracle OIC Enterprise (B91110) includes access to a non-production OIC environment as part of the standard subscription." — generic and not specific to APPSolve's assumption.  
**After:** "APPSolve assumes one (1) Production OIC environment and one (1) standard non-production OIC environment, where these are included in the customer's Oracle OIC licence. APPSolve does not provide, procure, or license Oracle OIC environments."  
**Commercial reason:** Makes explicit that APPSolve is not providing the OIC licence (a recurring client misunderstanding), and specifies exactly which environments are assumed (1 Production + 1 non-production). Additional environments must be separately licensed by the client.  
**Risk mitigated:** Client assumes APPSolve provides the OIC platform; client expects DEV + TEST + UAT + PROD environments under the standard scope.

---

### CL-OIC-003 — OIC-MON-002 (BU-OIC-003)

**Change type:** Modified  
**Before:** "The recipients of error notification emails are confirmed during the Scope and Design phase (typically: client's integration operations team and APPSolve's support contact during hypercare)."  
**After:** Two specific recipients defined: (1) customer nominated support mailbox (permanent); (2) APPSolve support mailbox during hypercare only. Explicit statement that APPSolve's mailbox is removed from notification configuration after hypercare.  
**Commercial reason:** APPSolve receiving error notifications indefinitely after hypercare creates an implied ongoing support obligation with no commercial basis. Removing APPSolve from error notifications post-hypercare protects against the client assuming APPSolve is monitoring and responding to errors without an AMS contract.  
**Risk mitigated:** Client assumes APPSolve is monitoring integrations 12 months post-go-live because they're still receiving error alert emails; escalates an integration failure expecting APPSolve to respond under the original contract.

---

### CL-OIC-004 — OIC-SUP-002 (BU-OIC-004)

**Change type:** Modified  
**Before:** "Where OIC is delivered as part of the same project as Oracle HCM or Oracle ERP, OIC hypercare runs concurrently with the primary module's hypercare period."  
**After:** Explicit confirmation that one single four-week hypercare period covers both primary modules and OIC integrations. Added: "OIC hypercare does not extend beyond the four-week default unless separately contracted."  
**Commercial reason:** Prevents the argument that OIC deserves a separate (additional) hypercare period on top of HCM hypercare. The concurrent model means the total hypercare cost is one period, not two.  
**Risk mitigated:** Client argues that OIC hypercare should start after HCM hypercare ends, effectively doubling the hypercare obligation.

---

### CL-OIC-005 — OIC-CON-006 (BU-OIC-005)

**Change type:** Modified  
**Before:** Draft tier model with "To be confirmed" effort indicators and a "BU Lead to confirm tier definitions" note.  
**After:** Confirmed tier definitions:
- **Simple:** One source, one target; standard adapter; limited mapping; no orchestration; standard auth; well-documented API with sandbox.
- **Standard:** One source, one target; moderate mapping; code-set lookups; conditional logic; standard error handling.
- **Complex:** Multi-step orchestration; multiple objects; complex transformations; high-volume or near-real-time; non-standard adapter; complex auth; no vendor sandbox.  
**Commercial reason:** Without confirmed tier definitions, each bid manager applies different criteria, leading to inconsistent pricing across proposals. The tier model is now the single authoritative basis for all OIC estimates.  
**Risk mitigated:** Two bid managers price the same integration type differently; APPSolve presents inconsistent pricing to the same client across proposals.

---

### CL-OIC-006 — OIC-DES-007 (BU-OIC-006)

**Change type:** Modified  
**Before:** Implied that accelerator reuse produced an effort discount — "Applicable accelerators and their effort reduction assumptions are identified..."  
**After:** "Accelerator applicability is assessed per integration during the estimation phase — no automatic effort discount is applied. Where an accelerator is confirmed applicable, the actual effort reduction is documented explicitly in the project estimate."  
**Commercial reason:** Automatic accelerator discounts create two problems: (a) the discount is applied even when the accelerator requires significant adaptation; (b) clients ask for the discount percentage as a negotiating tool. Per-integration assessment produces a more defensible and accurate estimate.  
**Risk mitigated:** Bid manager applies a blanket 30% discount for "having an accelerator" on every integration; actual build effort is higher because the accelerator only covers 40% of the design.

---

### CL-OIC-007 — OIC-DES-005 (BU-OIC-007)

**Change type:** Modified  
**Before:** "SFTP file-based integration is the default fallback mechanism."  
**After:** "SFTP file-based integration is the standard fallback mechanism, subject to the customer's IT security approval of the SFTP connectivity approach." Added: "Where the client's security policy does not permit SFTP-based integration, the integration approach requires assessment before it can be included in scope."  
**Commercial reason:** SFTP is increasingly restricted by corporate security policies (especially in financial services and government). Confirming SFTP as the default while acknowledging the security approval dependency protects APPSolve from scope disputes when SFTP is blocked.  
**Risk mitigated:** APPSolve designs and builds an SFTP integration; client's IT security team rejects SFTP during SIT setup; APPSolve must redesign at its own cost.

---

### CL-OIC-008 — Frontmatter

**Change type:** Updated  
- `status`: Draft — Pending BU Lead Approval → **Approved**  
- `approved_by`: blank → **BU Lead — Oracle Practice**  
- `approved_date`: blank → **2026-06-15**  
- `approved_for_reuse`: false → **true**  
- `bu_lead_review_items`: removed (all 7 items closed)  
- `bu_lead_decisions_applied`: added (all 7 decisions recorded with affected assumptions)

---

### CL-OIC-009 — OIC_ASSUMPTION_REGISTER.csv

**Change type:** Updated  
All 101 rows: Status column updated from `Draft` / `Draft (BU-OIC-XXX pending)` → `Active`  
7 rows with BU-OIC pending labels: labels removed and status set to Active  
Register now reflects the approved state of the full OIC pack.

---

### CL-OIC-010 — OIC_IMPLEMENTATION_PATTERNS.md

**Change type:** Updated  
Section 6: "Pending BU-OIC-005" heading removed; confirmed tier definitions applied; draft effort indicator column replaced with effort rate card reference (GAP-OIC-002 pending Delivery Lead).  
Section 7: "Pending BU-OIC-006" heading replaced; explicit statement added that no automatic accelerator discount applies; per-integration assessment requirement added.

---

## Impact Assessment — Existing Proposals

No proposals were issued using OIC assumptions while in Draft status (OIC pack was created and approved in the same cycle). No retroactive proposal updates required.

**Future proposals:** All OIC proposals issued after 2026-06-15 must use this Approved pack. Key commercial defaults now active:
- Bidirectional integrations always priced as two line items (OIC-SCP-002)
- APPSolve does not provide OIC licensing (OIC-SCP-005)  
- APPSolve error notification removed post-hypercare unless AMS (OIC-MON-002)
- Hypercare is concurrent with primary module — one 4-week period (OIC-SUP-002)
- All integrations classified as Simple / Standard / Complex (OIC-CON-006)
- No automatic accelerator discounts (OIC-DES-007)
- SFTP requires customer security approval (OIC-DES-005)

---

*OIC_APPROVAL_CHANGE_LOG v1.0 | WP11C-A — OIC Approval | 2026-06-15*  
*10 changes applied | 7 BU decisions closed | OIC pack promoted to Approved*
