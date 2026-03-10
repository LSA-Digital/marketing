# HSRA EPMS Section Draft

**Last Updated:** 2026-03-09

## Usage Labels

- `Safe to paste`: supported by current source map and suitable for EPMS draft entry
- `Needs SME review`: strategically useful, but should be reviewed before being treated as approved product language

## Definitions (`Safe to paste`)

- **HSRA / HRA:** Health and Social Risk Assessment built on the LSARS HRA engine for tract/county-level environmental and social-risk analysis.
- **EPA method:** Population screening approach using EPA-style IUR-based calculations.
- **OEHHA method:** Age-weighted CA-OEHHA-aligned approach suitable for more detailed health-risk reporting.
- **SDOH:** Social Determinants of Health overlays used to identify vulnerability and prioritization context.

## Product Name (`Safe to paste`)

Health and Social Risk Assessment (HSRA)

## Product Family (`Needs SME review`)

LSARS / public-health and risk-decision support

## Product Idea (`Needs SME review`)

HSRA combines environmental health risk analysis, social vulnerability overlays, and tract/county-level prioritization outputs into an auditable product for public-health planning, resource allocation, environmental-justice analysis, and related decision support.

## Industry Targets (`Needs SME review`)

- state health agencies
- local health departments
- Medicaid and rural-health programs
- nonprofit hospitals and community-benefit teams
- environmental-justice and environmental-health programs
- public-health researchers and policy teams
- selected employer/payer or wellness-oriented buyers when premium data is relevant

External support note:

- strongest current public-sector demand signals are county/community-level rural transformation, CHNA/CHA assessment cycles, and state EJ / health-equity prioritization contexts

## Market Segments (`Needs SME review`)

### Public-Sector Core

- state health departments
- local health departments
- state rural-health offices
- public-health grant programs
- Medicaid / rural-health transformation initiatives with county/community metric requirements

### Provider / Community Health

- nonprofit hospitals
- community health planning teams
- cancer-control and screening programs
- nonprofit hospital CHNA and implementation-strategy work

### Adjacent Commercial

- employers and payers seeking richer population segmentation
- consulting-led deployments where HPR premium data adds actionability

## Goals / Problems (`Needs SME review`)

- combine pollution burden, cancer/public-health burden context, and SDOH into one prioritization workflow
- move from surveillance to auditable resource allocation
- identify which tracts/counties should receive interventions first
- support state-first deployment using public data and configurable local inputs
- create a path to premium-data-enhanced segmentation and intervention design

## Customer Questions (`Safe to paste`)

- Which counties or tracts have the highest combined pollution, cancer, and social-risk burden?
- Where should mobile services, screenings, or interventions go first?
- Which communities have risk plus access barriers that make standard interventions less effective?
- How do we justify prioritization decisions to funders, boards, or the public?
- Which subpopulations need premium segmentation, outreach, or engagement design rather than basic public-data prioritization?

## Value Props (`Needs SME review`)

- auditable integration of environmental burden and SDOH
- tract/county-level prioritization rather than generic averages
- HARP2-parity credibility and source-data-first methodology foundation
- state-first deployment model for practical public-sector use
- expandable packaging: public-data baseline plus premium-data enhancement
- fits existing funding and reporting pressure better than a generic dashboard-only story

## Key Metrics / Deltas / User Roles (`Needs SME review`)

### Key Metrics

- risk burden by tract/county
- vulnerability and compounded-risk scores
- ranked priority zones
- screening or intervention targeting rates
- resource-allocation auditability

### Desired Deltas

- higher targeting precision
- better justification for resource allocation
- faster movement from assessment to action
- improved screening/intervention deployment in priority zones

### User Roles

- state health strategist
- public-health analyst / epidemiologist
- local health department leader
- hospital community-benefit leader
- program manager for rural-health or health-equity initiatives

## Competitive Landscape (`Needs SME review`)

HSRA sits between PHM analytics, CHNA tools, EJ/GIS tools, social-care platforms, and employer HRAs. Its strongest position is as an integrated environmental-health-plus-SDOH prioritization layer rather than a replacement for every workflow in those adjacent categories.

## Sales / Marketing Roadmap (`Needs SME review`)

1. Lead with Tennessee as the strongest concrete business case.
2. Use public-data HSRA as the base offer for public-sector buyers.
3. Target states and agencies with county/community-level reporting, RHT-style funding pressure, CHNA/CHA cycles, or EJ / health-equity prioritization needs.
4. Add premium HPR data and services where segmentation, outreach, or intervention design is needed.
5. Convert research outputs into buyer-specific one-pagers and outreach materials.

## Red Team / Devil's Advocate (`Safe to paste`)

- Is HSRA being over-positioned as broader LSARS strategy rather than the current product itself?
- Which claims are configuration-dependent rather than out-of-the-box?
- Does the buyer actually need premium data, or is public-data HSRA enough?
- Are we claiming workflow capabilities that belong to adjacent systems rather than HSRA?
- Do we have the right evidence to separate implemented capability from market vision?

## Market Model Inputs (`Safe to paste`)

- LSARS HRA engine outputs and report bundles
- EPA AirToxScreen, SVI, ACS, and state-specific public health datasets
- Tennessee state-first evidence-card approach
- HPR LCI premium data model for segmentation, communications, access, and intervention design
- public-sector funding and compliance signals from rural-health, CHA/CHIP, CHNA, and EJ contexts

## Source-to-Claim Map

| EPMS Area | Primary Sources |
|---|---|
| Product idea / value props | `../lsars-hra/README.md`, `docs/inputs/HSRA/HSRA-pophealthmap.ai-deck-2026Mar9.pdf` |
| Public-sector targets and Tennessee story | `../lsars-hra/docs/investor/03_Traction_Pilots/Pilot_OnePager_TN_Health.md`, `docs/research/market/hsra-demand-signals-rural-health-2026.md`, `docs/research/hsra/chatgpt-deep-research-result-2026.md` |
| Premium-data packaging | `docs/inputs/HPR/LCI-GQM.html`, `docs/inputs/HPR/LCI-data-model-master.xlsx` |
| Current outputs and methodology claims | `../lsars-hra/docs/LSARS_HRA_API_DOCUMENTATION.md`, `../lsars-hra/apps/backend/report/sdoh_data.py` |

## Sources

- `../lsars-hra/README.md`
- `../lsars-hra/docs/LSARS_HRA_API_DOCUMENTATION.md`
- `../lsars-hra/apps/backend/report/sdoh_data.py`
- `../lsars-hra/docs/investor/03_Traction_Pilots/Pilot_OnePager_TN_Health.md`
- `docs/inputs/HSRA/HSRA-pophealthmap.ai-deck-2026Mar9.pdf`
- `docs/inputs/HPR/LCI-GQM.html`
- `docs/inputs/HPR/LCI-data-model-master.xlsx`
- `docs/research/market/hsra-demand-signals-rural-health-2026.md`
- `docs/research/hsra/chatgpt-deep-research-result-2026.md`
