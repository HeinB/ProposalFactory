---
source_document: "APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
source_path: "Parties/Customers/SITA/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx"
extraction_date: "2026-06-08"
extracted_by: "Claude (AI extraction — requires human review)"
readiness: "MODERNISE"
approved_for_reuse: "No"
business_unit: "BeBanking"
review_status: "Candidate"
---

> **DRAFT — NOT APPROVED FOR TENDER USE**
> Readiness: MODERNISE | Review required by: Hein Blignaut

---

# BeBanking — Hosting and Deployment Model

## Deployment Options

BeBanking is deployed on client infrastructure (on-premises or client-managed cloud), operating alongside the ERP application. The banking server is a separate component from the ERP application server.

**[UPDATE: Confirm whether APPSolve now offers a hosted/managed BeBanking deployment option. The 2017 SITA model was fully on-premises. Acumatica being cloud-native may require a different deployment architecture — confirm with the BeBanking BU lead.]**

## On-Premises / Client-Hosted Deployment

### Banking Server

A dedicated banking server is deployed to host the BeBanking file transfer components:

- Physically or virtually separate from the ERP application server
- Hosts the Connect Direct software and SSH certificate store
- Accessible from the ERP application server over the internal network
- Accessible to APPSolve consultants via VPN for implementation and ongoing support

### Server Requirements

- VPN access enabled for APPSolve implementation and support
- Connect Direct connectivity configured to the bank's H2H system
- SSH certificates implemented for server-to-server communication
- Sufficient network bandwidth for remote support

## Support Model Post-Deployment

After go-live, BeBanking support is provided by APPSolve remotely:

- VPN access to client environment is the primary support mechanism
- APPSolve's Hybrid Support Model applies — on-site support available when required (see W1S1-009 Key Differentiators)
- 24x7x365 standby available through APPSolve's Remote Support Centre

## Licensing Model

BeBanking is offered under two engagement models:

| Model | Structure | Typical Use |
|---|---|---|
| **Service Option** | Once-off installation fee + monthly usage fee per module | Clients preferring OPEX model |
| **Software Option** | Once-off license + installation fee + annual support fee | Clients preferring capital purchase |

**[UPDATE: Confirm current pricing model names and structure — the two-option model (Service vs. Software) was current in 2017. Verify whether this structure is still offered or has been replaced.]**

---

**Review notes:** Hosting and deployment model sourced from SITA BeBanking Proposal v1.06 (June 2017) — Proposed Engagement, Cost Proposal sections. MODERNISE rating: (1) the 2017 model is entirely on-premises; Acumatica cloud-native deployments may require different banking server hosting, (2) confirm current licensing structure, (3) confirm VPN is still the primary support channel or whether API/cloud alternatives exist. The two-option licensing model was confirmed in SITA v1.06; specific pricing figures were NOT extracted (commercially sensitive and 2017 rates).
