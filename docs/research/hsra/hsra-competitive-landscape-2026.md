# HSRA Competitive Landscape

**Last Updated:** 2026-03-09

## Summary

HSRA does not sit in a single clean software category. Its nearest alternatives are spread across population-health analytics, SDOH/social-care platforms, CHNA tools, environmental-justice/GIS tools, rural-health planning tools, and employer/wellness HRA products. The most defensible positioning is not that HSRA replaces every category; it is that HSRA integrates parts of several categories into a tract/county-level decision-support workflow.

## Evidence Standard For This Note

This document uses category-level synthesis, not a feature-by-feature competitive teardown. Vendor references should be read as representative examples of adjacent categories unless a directly cited vendor source proves a narrower claim.

## Competitive Categories

| Category | Representative Solutions | What They Commonly Do Well | What They Commonly Do Not Integrate End-to-End | HSRA Angle |
|---|---|---|---|---|
| Enterprise population health analytics | Arcadia, Innovaccer Government, Oracle Health | Clinical/claims aggregation, risk stratification, care management analytics | Pollution burden and public-health tract-level environmental risk fusion | HSRA is stronger where environmental exposure and public-health prioritization must live in the same workflow |
| SDOH / social-care platforms | Unite Us, findhelp, Socially Determined | Social-needs screening, referral workflows, social-risk datasets | Permit/public-health HRA methodology, pollutant-driven risk analysis, HARP2-style credibility | HSRA is stronger when environmental burden and health-risk methodology matter |
| CHNA / community health planning tools | Community Commons, SparkMap, other CHNA consulting/data platforms | Community assessment workflows, public data packaging, board/community reporting | Integrated pollution + HRA + SDOH tract-level risk engine | HSRA is stronger as a more analytical, auditable prioritization engine |
| EJ / GIS mapping tools | Esri-based solutions, state EnviroScreen tools, public EJ maps | Mapping, geography, environmental and demographic overlays | Health-risk methodology plus report outputs and intervention/prioritization framing | HSRA is stronger when the buyer needs health-risk logic and not just mapping |
| Rural-health planning tools | HRSA rural mapping/reference tools, grant-support tools | Rural designation, shortage areas, public program planning support | Integrated pollution + cancer + SDOH decision objects | HSRA is stronger as a root-cause and prioritization layer |
| Employer/commercial HRA tools | Sharecare, Wellsource, CoreHealth | Wellness assessments, engagement, employer population baselines | Environmental exposure burden and public-sector geography logic | HSRA is stronger when public health, environmental burden, and community-level analysis are required |

## External Research Additions

The Deep Research pass strengthens the category framing with a few safer, more specific observations:

- `Arcadia` and `Innovaccer Government` publicly emphasize clinical/program analytics, interoperability, oversight, and care-management-oriented population health rather than a single workflow joining environmental burden, formal air-toxics risk logic, and tract-level resource allocation.
- `Unite Us`, `findhelp`, and `Socially Determined` reinforce the distinction between social-care orchestration and social-risk analytics on one side, versus pollutant-burden and HRA methodology on the other.
- `Community Commons` and `SparkMap` strengthen the CHNA/community-assessment comparison because they clearly support assessment, downloadable reporting, and indicator access, but not a unified environmental-burden-plus-health-risk engine in their public descriptions.
- `Esri` and state EJ tools show that tract-based burden ranking and prioritization are normal public-sector patterns, but the public materials still support a mapping/prioritization analog more than an end-to-end HSRA-equivalent product.

## Where HSRA Looks Strong (`Category-level synthesis`)

- It can combine environmental burden, HRA methodology, and SDOH overlays in one narrative.
- It has a strong auditability story because of the HARP2-parity and source-data-first technical foundation.
- It has a clearer Tennessee/public-health allocation story than generic enterprise PHM tools.
- It has a natural upsell path into premium data and configuration services.
- External research also supports a cleaner integration-gap claim: the closest alternatives are adjacent categories rather than one-for-one substitutes.

## Where HSRA Needs Careful Framing (`Claim hygiene`)

- It should not be sold as a full care-management operating system in the way enterprise PHM vendors are.
- It should not be sold as a closed-loop social-referral network unless such workflow capabilities are separately evidenced.
- It should not be described as a turnkey CHNA replacement without proving reporting/workflow fit for hospital compliance teams.
- It should not overclaim GIS breadth versus full geospatial platform vendors.

## Recommended Differentiation Language (`EPMS-safe framing`)

Preferred language:

- integrated health-and-social risk prioritization
- tract/county-level environmental burden plus SDOH
- auditable resource-allocation support
- public-health and policy-facing decision infrastructure
- configurable public-data plus premium-data packaging

Avoid language such as:

- no competitor can do this
- full replacement for enterprise PHM suites
- complete social-care platform
- turnkey statewide transformation without configuration

## Practical Positioning Takeaway

HSRA is best presented as a bridge product:

- deeper environmental-health methodology than generic PHM tools,
- more decision-ready than static public-data portals,
- more public-health and tract-level than typical employer HRA tools,
- more analytically grounded than broad narrative-only CHNA packaging.

## Source-to-Claim Map

| Claim | Sources |
|---|---|
| HSRA combines HRA methodology with SDOH and prioritization outputs | `../lsars-hra/README.md`, `../lsars-hra/docs/LSARS_HRA_API_DOCUMENTATION.md`, `../lsars-hra/apps/backend/report/sdoh_data.py` |
| Competitive categories should be treated as adjacent, not one-for-one | Official vendor and public sources listed below |
| HSRA is strongest as an integrated decision-support layer | `../lsars-hra/README.md`, `docs/research/market/hsra-demand-signals-rural-health-2026.md`, `../lsars-hra/docs/investor/03_Traction_Pilots/Pilot_OnePager_TN_Health.md` |
| Public evidence supports an integration opportunity more than a claim that no competitor can do any similar task | `docs/research/hsra/chatgpt-deep-research-result-2026.md` |

## Sources

- `../lsars-hra/README.md`
- `../lsars-hra/docs/LSARS_HRA_API_DOCUMENTATION.md`
- `../lsars-hra/apps/backend/report/sdoh_data.py`
- `../lsars-hra/docs/investor/03_Traction_Pilots/Pilot_OnePager_TN_Health.md`
- `docs/research/market/hsra-demand-signals-rural-health-2026.md`
- `docs/research/hsra/chatgpt-deep-research-result-2026.md`
- https://www.arcadia.io
- https://innovaccer.com/solutions/government
- https://uniteus.com/products/closed-loop-referral-system/
- https://company.findhelp.com/products/
- https://www.sociallydetermined.com
- https://www.lightbeamhealth.com
- https://www.persivia.com
- https://www.communitycommons.org
- https://sparkmap.org
- https://www.esri.com
- https://oehha.ca.gov/calenviroscreen/sb535
- https://www.ruralhealthinfo.org
- https://www.sharecare.com
- https://www.wellsource.com
