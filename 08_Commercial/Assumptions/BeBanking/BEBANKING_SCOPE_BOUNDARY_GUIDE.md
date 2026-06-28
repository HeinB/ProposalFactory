---
title: BeBanking Base Assumption Pack — Scope Boundary Guide
version: v1.1-Draft
status: Draft — For internal use during proposal assembly
pack_code: BB
date: 2026-06-18
---

# BeBanking Scope Boundary Guide

**Purpose:** This guide provides standard responses to the most common scope-creep scenarios encountered in BeBanking proposals and implementations. Use this guide during proposal review, SOW drafting, and delivery planning to apply consistent boundary decisions.

**Reference:** All boundary decisions reference the applicable assumption in `BEBANKING_BASE_ASSUMPTIONS_V1.md`.

---

## Scope Boundary Scenarios

---

### SB-BB-001 — New Bank Onboarding After Go-Live

**Client request:** "After we go live with ABSA and FNB, we want to add Nedbank. Can that be included in the project?"

**Standard response:** New bank connectivity after go-live is not included in the initial BeBanking onboarding scope. Adding Nedbank requires a new bank onboarding engagement: bank registration, format specification work, connectivity testing, and UAT. This is a separately scoped and priced Change Request.

**Included in standard scope:** Initial onboarding for the banks confirmed in the SOW before project kick-off.

**Excluded:** Any bank added after the initial scope confirmation, regardless of whether the bank is on APPSolve's supported bank list.

**Escalation path:** BeBanking BU Lead approves bank addition scope and pricing. Commercial Director signs off CR above threshold. Refer to BU-BB-002 for standard new-bank charging model.

**Assumptions referenced:** BB-BNK-001, BB-BNK-003, BB-EXT-008, BB-SUP-006

---

### SB-BB-002 — Bank-Initiated Payment File Format Change

**Client request:** "Our bank has updated their EFT payment file specification. Can you update BeBanking?"

**Standard response:** Bank-initiated like-for-like format changes (field rename, field position adjustment, encoding change) are addressed by APPSolve as a support activity at no additional charge under the BeBanking support arrangement. Structural changes (new file type, new connectivity method, new payment channel) are assessed as Change Requests.

**Included:** Like-for-like format update to an existing payment file type that APPSolve already supports for that bank.

**Excluded:** New payment file types, new connectivity methods, new bank channels, or changes that require significant BeBanking reconfiguration.

**Escalation path:** Client logs support ticket. APPSolve assesses change scope. If CR, BeBanking BU Lead approves scope; CR follows commercial governance process.

**Assumptions referenced:** BB-BNK-008, BB-SUP-007

---

### SB-BB-003 — New Country Rollout

**Client request:** "We're expanding to Namibia. Can you extend our BeBanking to cover Nedbank Namibia?"

**Standard response:** Namibian banking connectivity is available but is separately scoped from South African banking implementations. Nedbank Namibia and Standard Bank Namibia require dedicated bank onboarding — the Namibian bank entities are distinct from their South African counterparts and have different file format specifications, connectivity requirements, and onboarding processes. This is a separately scoped engagement.

**Included:** SA banking connectivity as per the agreed SOW. Namibia is an optional add-on.

**Excluded:** Multi-country banking connectivity from the base South African BeBanking implementation.

**Escalation path:** BeBanking BU Lead confirms multi-country deployment model (refer to BU-BB-007). New bank onboarding SOW required. Commercial Director signs off.

**Assumptions referenced:** BB-GEN-002, BB-BNK-009, BB-EXT-008

---

### SB-BB-004 — Additional ERP Platform Integration

**Client request:** "We've just acquired a subsidiary that runs SAP. Can BeBanking integrate with both our Oracle ERP and their SAP environment?"

**Standard response:** BeBanking supports integration with SAP environments. The additional SAP integration is not included in the initial BeBanking onboarding scope, which was defined for a single ERP instance. An additional ERP integration requires a separate integration design, integration testing, and potentially a distinct BeBanking payment channel configuration. This is a separately scoped Change Request or a new SOW.

**Included:** Single ERP integration confirmed in the initial SOW.

**Excluded:** Integration with additional ERP platforms, additional ERP instances, or additional financial systems beyond the initial scope.

**Escalation path:** BeBanking BU Lead and ERP BU Lead jointly scope the additional integration. SOW addendum required. Note: SAP integration uses "SAP environments" framing only — no SAP module-level claims without explicit pre-sales confirmation.

**Assumptions referenced:** BB-INT-002, BB-INT-006, BB-SUP-006

---

### SB-BB-005 — Additional Approval Workflow Levels

**Client request:** "Our CFO needs to approve all payments above R500,000. Can we add a third approval level with value-based routing?"

**Standard response:** The standard BeBanking approval workflow is a two-level maker-checker model (creator + approver). Additional approval levels, value-based routing, or workflow branching beyond the standard two-level model are separately scoped configuration items. This is a Change Request.

**Included:** Two-level maker-checker (Payment Creator + Payment Authoriser). Email notification of pending approvals.

**Excluded:** Third or fourth approval levels, value-based approval tiering, role-based payment value limits, approval delegation rules.

**Escalation path:** BeBanking BU Lead approves configuration design for additional workflow. CR raised and approved before development begins.

**Assumptions referenced:** BB-PAY-003, BB-SUP-006

---

### SB-BB-006 — Additional Payment Types

**Client request:** "We'd like BeBanking to also process our debit orders for subscription billing."

**Standard response:** BeBanking does not support direct debit (debit order) processing. BeBanking is an EFT credit payment platform. Debit order processing requires a collections management system, which is outside BeBanking's scope. This cannot be added as a configuration item — it is a fundamental platform exclusion.

**Included:** EFT credit payments (supplier, payroll, intercompany, forex). Bank statement import.

**Excluded:** Debit orders, direct debits, mandate management, collections processing, NAEDO, DebiCheck.

**Escalation path:** If the client has a debit order requirement, escalate to BeBanking BU Lead to assess whether a separate product or partner solution is available. Do not commit BeBanking to debit order capability in any proposal.

**Assumptions referenced:** BB-PAY-001, BB-EXC-006

---

### SB-BB-007 — Historical Bank Statement Migration

**Client request:** "Can you load our last 3 years of bank statements from our previous banking system into BeBanking so we have a complete history?"

**Standard response:** Historical bank statement data migration is not included in the standard BeBanking onboarding. BeBanking captures bank statements from the go-live date forward. Loading historical statement data into BeBanking requires a separate data migration assessment — including statement format conversion, data volume assessment, and BeBanking import design — and is a separately scoped engagement.

**Included:** Bank statement import from go-live forward for in-scope banks.

**Excluded:** Historical statement migration from any prior period, legacy banking systems, or third-party statement formats.

**Escalation path:** BeBanking BU Lead assesses feasibility and effort for historical statement migration. If technically feasible, CR or separate SOW required. Note: BB-DAT-004 covers historical payment data migration exclusion; the same principle applies to bank statements.

**Assumptions referenced:** BB-DAT-004, BB-INT-008

---

### SB-BB-008 — Bank-Side Troubleshooting

**Client request:** "We submitted our payment batch but the bank is showing some payments as unprocessed. Can you fix this from your side?"

**Standard response:** BeBanking support covers the BeBanking application layer. Bank-side payment processing issues — rejections, unprocessed batches, bank system outages — are outside BeBanking's control. APPSolve can confirm that BeBanking successfully transmitted the payment file to the bank and provide the transmission acknowledgement as evidence. The client must liaise directly with their bank to investigate and resolve bank-side processing issues. APPSolve assists with diagnosis and escalation where within its capability.

**Included:** Confirming successful payment file transmission from BeBanking to the bank. Providing transmission logs and acknowledgement files. Escalating to the bank's technical team on the client's behalf where APPSolve has a technical support channel with the bank.

**Excluded:** Bank system investigation, bank payment processing errors, bank liquidity or credit limit issues, payment recall or reversal instruction (must go via client directly to their bank).

**Escalation path:** Client logs support ticket. APPSolve provides transmission evidence. Client escalates to their bank relationship manager or technical team. If the issue is determined to be a BeBanking software fault, APPSolve accepts P1 incident and resolves.

**Assumptions referenced:** BB-SUP-002, BB-PAY-005, BB-EXT-004

---

### SB-BB-009 — User Provisioning Requests

**Client request:** "Can you add three new users to BeBanking for our new AP team members?"

**Standard response:** Routine user provisioning and deprovisioning is the client's operational responsibility. The client's designated BeBanking System Administrator adds, modifies, and removes user accounts. This is not a BeBanking support request. APPSolve does not manage routine user administration post-go-live.

**Included:** Initial user account setup during onboarding. Emergency access restoration where the client's System Administrator role is unavailable.

**Excluded:** Routine user additions, modifications, and deactivations post-go-live.

**Escalation path:** Client's BeBanking System Administrator adds the users directly in BeBanking. If the Administrator is unavailable or locked out, the client logs an emergency support request and APPSolve provides temporary access restoration.

**Assumptions referenced:** BB-SEC-002, BB-SUP-005

---

### SB-BB-010 — Client-Requested Security Review or Penetration Test

**Client request:** "Our internal audit team needs a penetration test report for BeBanking as part of our annual IT security audit."

**Standard response:** BeBanking conducts periodic platform-level security reviews. A dedicated penetration test or security audit specific to the client's BeBanking environment requires coordination between APPSolve, the client's security team, and potentially the client's bank, and is a separately scoped engagement. A client-requested penetration test is not included in the standard BeBanking subscription.

**Included:** APPSolve's own periodic security review programme. Provision of the BeBanking Security Architecture document confirming encryption standards and access controls.

**Excluded:** Client-specific penetration testing, client-commissioned security audits, bespoke security assessment reports, vulnerability scanning of the client's BeBanking instance.

**Escalation path:** BeBanking BU Lead reviews the security assessment request and determines scope. Engage APPSolve's security review capability or an accredited external assessor as appropriate. Separately scoped SOW required.

**Assumptions referenced:** BB-SEC-006, BB-EXT-007

---

### SB-BB-011 — Production Support Requests Outside SLA Hours

**Client request:** "Our month-end payment run failed at 8 PM on Friday. We need immediate help."

**Standard response:** BeBanking P1 incidents (Production environment down; no payment processing possible) receive out-of-hours response under the standard BeBanking support arrangement. If the after-hours issue is classified as P1, APPSolve's BeBanking support team responds within the P1 SLA (1 hour). P2–P4 incidents outside business hours are queued and addressed the next business day.

**Included:** P1 out-of-hours response. P2–P4 queued to next business day under standard support.

**Excluded:** After-hours response to P2–P4 issues under standard support. 24×7 all-priority support is not part of the standard BeBanking arrangement — any such requirement must be separately negotiated.

**Escalation path:** Client logs P1 ticket via the BeBanking emergency support channel. APPSolve BeBanking on-call team responds within P1 SLA. If the incident is classified below P1 on assessment, the client is notified and the ticket is addressed next business day.

**Assumptions referenced:** BB-SUP-001, BB-SUP-004

---

### SB-BB-012 — Disaster Recovery Testing by Client

**Client request:** "We need to do a DR failover test as part of our business continuity programme. Can you schedule this for us?"

**Standard response:** BeBanking includes DR capability and APPSolve conducts internal DR tests on a scheduled basis. Client-initiated DR rehearsals — where the client participates in or witnesses a DR failover test — are separately scoped. Client-initiated DR testing is not included in the standard BeBanking subscription.

**Included:** APPSolve's own internal DR testing programme. DR capability as specified in the subscription agreement (RTO/RPO commitments).

**Excluded:** Client-initiated DR rehearsals, on-demand DR failover tests, client-witnessed DR exercises, DR testing that simulates specific client disaster scenarios.

**Escalation path:** BeBanking BU Lead reviews client DR testing request and scope. Separately scoped SOW required for client-participated DR testing. APPSolve's internal DR RTO/RPO commitments are confirmed in the subscription agreement; the BeBanking BU Lead can provide this detail during proposal negotiations.

**Assumptions referenced:** BB-ENV-004, BB-ENV-005 *(Note: BB-ENV-006 was removed from the pack per WP14D BU Lead Master Review; DR capability is not explicitly asserted in an assumption but remains a platform feature confirmed in the subscription agreement)*

---

### SB-BB-013 — SARB Regulatory Reporting Support

**Client request:** "Can BeBanking help us prepare our SARB BoP monthly returns based on the forex payments we've processed?"

**Standard response:** BeBanking does not prepare or submit SARB regulatory filings. Regulatory reporting — including SARB Balance of Payments returns, SARS EFT payment declarations, and NPA reporting — is the client's legal and regulatory responsibility. BeBanking provides the underlying forex payment data through its standard reporting pack; the client's finance team or tax advisors use this data to prepare regulatory submissions.

**Included:** Standard BeBanking reports providing forex payment data (payment amounts, currencies, beneficiary references, transaction dates). See BB-RPT-001.

**Excluded:** SARB BoP form preparation, SARB submission, SARS reporting, regulatory compliance advice of any kind.

**Escalation path:** Client's finance team or appointed advisors use BeBanking forex payment reports for regulatory filing purposes. APPSolve does not provide regulatory compliance services.

**Assumptions referenced:** BB-FX-003, BB-FX-006, BB-EXT-006 *(Note: BB-RPT-005 was removed from the pack per WP14D BU Lead Master Review; regulatory reporting exclusion is covered by BB-EXT-006)*

---

### SB-BB-014 — Additional Forex Currency or Country

**Client request:** "We've started buying from a supplier in Japan. Can BeBanking process Japanese Yen payments?"

**Standard response:** BeBanking supports the foreign currencies enabled by the client's bank forex agreement. If JPY is enabled by the client's forex bank (Citi Bank UK, ABSA, Nedbank, or FNB), adding JPY payments may be a configuration change. If JPY is not currently enabled, the client must first arrange JPY capability with their forex bank; once confirmed, APPSolve assesses any BeBanking configuration changes required. Currency additions post-go-live may trigger a Change Request.

**Included:** Forex payments in currencies supported by the client's existing bank forex agreement.

**Excluded:** Forex payments in currencies not yet enabled by the client's bank; establishing new currency facilities with the bank (client responsibility); currencies not supported by APPSolve's supported forex banking partners.

**Escalation path:** Client confirms JPY facility with their bank. Client notifies APPSolve. APPSolve assesses BeBanking configuration requirement. If a CR is required, BeBanking BU Lead approves scope.

**Assumptions referenced:** BB-FX-004, BB-FX-002, BB-SUP-006

---

### SB-BB-015 — Custom Remittance Advice or Payment Notification

**Client request:** "We want BeBanking to send a branded PDF remittance with our company logo, payment reference and itemised invoice lines to our suppliers."

**Standard response:** The standard BeBanking remittance advice is a plain text or standard HTML email containing the payment amount, beneficiary reference, and payment date. Custom branded PDF remittance advice, itemised invoice line detail on remittances, or delivery through a supplier portal are not included in the standard BeBanking implementation and are separately scoped.

**Included:** Standard email remittance advice to beneficiary email addresses from the client's ERP. Payment amount, reference, and date included.

**Excluded:** Branded PDF remittance advice, custom HTML templates, itemised invoice line detail, SMS delivery, supplier portal delivery.

**Escalation path:** BeBanking BU Lead and Commercial Director scope the custom remittance requirement. CR or separate deliverable SOW required.

**Assumptions referenced:** BB-PAY-006

---

*BeBanking Base Assumption Pack — Scope Boundary Guide v1.1-Draft | WP11J | WP14D 2026-06-18*  
*15 boundary scenarios (SB-BB-001 through SB-BB-015)*
