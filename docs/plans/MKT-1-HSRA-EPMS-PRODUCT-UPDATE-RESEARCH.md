# MKT-1: HSRA EPMS Product Update and Research Package

**Last Updated:** 2026-03-09
**Jira Ticket:** [MKT-1](https://lsadigital.atlassian.net/browse/MKT-1)
**Type:** Story
**Status:** Research package and EPMS entity enrichment completed; checklist save-path remains blocked by EPMS bug(s)

---

## Overview

Update the EPMS product record for **Health and Social Risk Assessment (HSRA)** with as much grounded information as possible from the current LSARS HRA codebase, internal product/strategy documents, the HSRA deck, and HPR Life Circumstances Intelligence (LCI) source material. The output should support both EPMS product-matrix population and a set of markdown research artifacts that explain what the product does, where it fits in the market, and how LSA Digital can sell both software licensing and premium configuration/consulting services.

This work is product-management research and packaging, not application implementation. The goal is to turn existing technical and domain knowledge into an auditable product narrative, buyer map, competitive context, and commercialization package.

---

## Scope

### In Scope

- Analyze the current HSRA/HRA product from the adjacent codebase in `../lsars-hra`
- Extract product capabilities, workflows, outputs, and proof points from internal documentation and source files
- Analyze the HSRA deck in `docs/inputs/HSRA/HSRA-pophealthmap.ai-deck-2026Mar9.pdf`
- Analyze HPR LCI source material in `docs/inputs/HPR/LCI-GQM.html` and `docs/inputs/HPR/LCI-data-model-master.xlsx`
- Define the EPMS section-by-section content population plan for HSRA
- Produce a markdown research summary explaining what HSRA does today
- Produce one or more markdown research files covering license, premium data, configuration, and consulting opportunity
- Expand target audience and business-case analysis, with Tennessee as the anchor example
- Expand competitive landscape analysis
- Expand market analysis across commercial, research, local, state, and federal buyers
- Put special focus on the other 49 states and current rural health funding demand signals
- Recommend where separate deep-research workstreams should be split out for efficiency

### Out of Scope

- Editing production application code in `../lsars-hra`
- Directly updating the EPMS HSRA product record in this ticket unless separately requested
- Final design/polish of marketing web pages or outbound collateral
- Purchasing or ingesting new proprietary datasets
- Legal claims, pricing approval, or regulatory claims beyond cited sources

---

## Research Inputs and Evidence Sources

### Primary Internal Sources

- `../lsars-hra/README.md`
- `../lsars-hra/docs/architecture.md`
- `../lsars-hra/docs/LSARS_HRA_API_DOCUMENTATION.md`
- `../lsars-hra/docs/LSARS-283-PopHRAGoals.md`
- `../lsars-hra/docs/plans/LSARS-506-STATE-FIRST-EVIDENCE-CARDS.md`
- `../lsars-hra/docs/plans/LSARS-509-TN-DATA-SOURCE-EXPANSION.md`
- `../lsars-hra/docs/research/state_first_TN/TN_health_data_gap_analysis_LSARS_HRA_2026-01-27.md`
- `../lsars-hra/docs/state_first/TN_PILOT_DATA_STRATEGY.md`
- `../lsars-hra/docs/investor/03_Traction_Pilots/Pilot_OnePager_TN_Health.md`
- `../lsars-hra/docs/investor/research/Research_Health_Equity_Pilots.md`
- `../lsars-hra/apps/backend/prompts/data_manifest.md`
- `../lsars-hra/apps/backend/prompts/state_first_guidance_TN.md`
- `../lsars-hra/apps/backend/services/sdoh_service.py`
- `../lsars-hra/apps/backend/report/sdoh_data.py`

### Marketing / Positioning Sources

- `lsaProductExpertAlignment.md`
- `videos/scripts/LSARS HSRA+PI explainer.SCRIPT.md`
- `docs/inputs/HSRA/HSRA-pophealthmap.ai-deck-2026Mar9.pdf`

### Premium Data / HPR Sources

- `docs/inputs/HPR/LCI-GQM.html`
- `docs/inputs/HPR/LCI-data-model-master.xlsx`

### External Market / Demand Research

- Competitor and market-context briefing collected 2026-03-09 (session research; to be normalized into `docs/research/hsra/hsra-competitive-landscape-2026.md`)
- `docs/research/market/hsra-demand-signals-rural-health-2026.md`
- Public program sources identified in those briefings, including CMS, HRSA, PHAB, NACCHO, ASTHO, EPA, CDC, and state health/environmental agencies

---

## Working Thesis

HSRA is best positioned as a **health-and-social risk decision platform** that combines environmental exposure burden, cancer and non-cancer risk, social vulnerability, tract/county prioritization, and state-specific public-health evidence into an auditable workflow for resource allocation, policy analysis, public-health planning, and community-facing decision support. Its commercial upside is strongest when sold as a combination of:

- core software/license access,
- premium data enrichment (including Human Performance Resources, LLC data where licensed), and
- high-value configuration/consulting for state-specific deployment, buyer-specific question framing, and intervention planning.

---

## Concrete Deliverables

### Product Planning Deliverables

- EPMS HSRA section population plan with mapped evidence by section
- Product matrix/source traceability table showing which source informs which EPMS section
- Gap log identifying what is known, what is inferable, and what still needs expert confirmation

### Markdown Research Deliverables

- `docs/research/hsra/hsra-product-summary-2026.md`
- `docs/research/hsra/hsra-license-and-services-opportunity-2026.md`
- `docs/research/hsra/hsra-competitive-landscape-2026.md`
- `docs/research/hsra/hsra-government-market-analysis-2026.md`
- `docs/research/hsra/hsra-source-map-and-evidence-register-2026.md`

### EPMS Update Deliverables

- Drafted content for: Product Idea, Industry Targets, Market Segments, Goals Problems, Customer Questions, Value Props, Key Metrics Deltas User Roles, Competitive Landscape, Sales Marketing Roadmap, Market Model Inputs, and Sources
- `docs/research/hsra/hsra-epms-section-draft-2026.md` - named EPMS-ready draft artifact for checklist population and review

---

## Phase Plan

### Phase 1: Source Map and Capability Extraction

- confirm product naming and boundaries
- extract current-state functionality from codebase/docs
- separate implemented capability from positioning language

### Phase 2: Premium Data and Buyer Question Framing

- extract HPR goal/question/data-level structure
- define public-data mode vs premium-data mode
- map buyer questions to current HSRA and premium HSRA answers

### Phase 3: Research Artifact Drafting

- write product summary markdown
- write license and services opportunity markdown
- write competitive landscape markdown
- write government market analysis markdown

### Phase 4: EPMS Packaging

- convert research outputs into EPMS-ready section drafts
- prepare source register and gap log
- define upload/ingestion plan for research markdown artifacts

---

## User Impact and Artifact Map

| Layer | Audience / User | What They Need | Planned Artifact |
|---|---|---|---|
| Product record | EPMS product owner | Complete HSRA section content with traceable sources | EPMS section population plan |
| Internal strategy | LSA Digital leadership / SMEs | Shared product narrative and packaging logic | Product summary markdown |
| Sales / GTM | Business development / partner-facing leads | License + services framing and buyer packaging | License and services opportunity markdown |
| Market intelligence | Product strategy / GTM | Category competitors, gaps, and differentiation | Competitive landscape markdown |
| Public-sector targeting | State/local/federal outreach | Buyer personas, programs, funding signals, and state replication logic | Government market analysis markdown |
| Auditability | Writers, reviewers, approvers | What each claim is based on | Source map and evidence register |

---

## Acceptance Criteria

- [x] **AC-1:** The plan identifies the exact internal sources that will be used to describe HSRA functionality, methodologies, outputs, and proof points.
- [x] **AC-2:** The plan includes a section-by-section mapping from EPMS HSRA checklist sections to evidence sources and expected content outputs.
- [x] **AC-3:** The plan explicitly covers Tennessee as the anchor business case, including county/tract analysis of pollution, cancer, and social health factors.
- [x] **AC-4:** The plan explicitly covers the premium HPR data option and distinguishes public-data-only HSRA from premium-data-enhanced HSRA.
- [x] **AC-5:** The plan includes a dedicated workstream for a markdown product-summary document describing what HSRA does today.
- [x] **AC-6:** The plan includes a dedicated workstream for one or more commercialization research markdown files describing license, configuration, and consulting opportunity.
- [x] **AC-7:** The plan includes a competitive-landscape workstream covering enterprise PHM, SDOH/social-care, CHNA, EJ/GIS, rural-health analytics, and adjacent commercial HRA categories.
- [x] **AC-8:** The plan includes a government market-analysis workstream with special attention to the other 49 states, rural health improvement funding, and state/local/federal buyer personas.
- [x] **AC-9:** The plan includes a recommended split for any deep-research subprojects that are better handled as separate research passes.
- [x] **AC-10:** The plan defines a fixed citation and traceability format for every markdown deliverable, including a sources section and explicit source-to-claim mapping.
- [x] **AC-11:** A new EPMS-project bug ticket documents the MCP save-path failures, exact error messages, and reproduction context. (`EPMS-182`)
- [x] **AC-12:** All intended HSRA research markdown is uploaded to EPMS using `epms.save_research` only.
- [x] **AC-13:** A 10-minute overall HSRA research summary document exists and is uploaded to EPMS.
- [x] **AC-14:** The HSRA document set includes Mermaid diagrams where they materially improve architecture, roadmap, or process comprehension.
- [x] **AC-15:** EPMS entity-based enrichment is completed for the highest-value entity paths using `entity_crud` only.

---

## Request-to-Deliverable Traceability

| User Request Element | Planned Deliverable |
|---|---|
| Analyze `../lsars-hra` codebase | Source map, capability extraction, EPMS section notes |
| Analyze HSRA deck PDF | Product summary, positioning notes, EPMS product idea |
| Analyze HPR GQM/workbook | Premium-data packaging, customer questions, market-model inputs |
| Describe target audience and business case | Product summary, license/services doc, government market analysis |
| Include Tennessee pilot framing | Product summary and government market analysis |
| Cover premium HPR option | License/services doc and premium-data packaging section |
| Cover competitors / existing solutions | Competitive landscape markdown |
| Expand market analysis for other 49 states | Government market analysis markdown |
| Consider splitting work into deep-research components | Recommended deep-research split section |

---

## EPMS Section Mapping Plan

| EPMS Section | Planned Content Source | Notes |
|---|---|---|
| Definitions | `../lsars-hra/docs/terms.md`, API/docs | Establish HRA/HSRA, OEHHA, EPA, SDOH, CRS, HEM |
| Product Name | Existing EPMS product name | Confirm HSRA naming consistency vs HRA/LSARS framing |
| Product Family | `lsaProductExpertAlignment.md`, LSARS product materials | Likely LSARS / public-health / decision-support family |
| Product Idea | README, architecture, HSRA deck, explainer script | Core description of product and why it exists |
| Industry Targets | pilot docs, competitor/demand research | State health, local health, Medicaid, hospitals, research, employers |
| Market Segments | competitor/demand research, TN pilot docs | Segment by public-sector, providers, research, commercial |
| Goals Problems | HPR GQM, TN pilot docs, LSARS-283 | Tie buyer pain to analytics/output capability |
| Customer Questions | HPR GQM, state-first guidance, TN gap analysis | Use as buyer-question framework |
| Value Props | README, investor docs, market research | Auditable prioritization, integrated risk, tract-level insight |
| Key Metrics Deltas User Roles | pilot docs, HPR GQM, LSARS outputs | Metrics by buyer persona and intended change |
| Competitive Landscape | external market briefing | Category-by-category competitive analysis |
| Financial Model | license + services research | Likely software + premium data + consulting bundle |
| Sales Marketing Roadmap | commercialization workstream | Tennessee-first then replicate across states |
| Red Team Devils Advocate | explicit skepticism section | Methodology, procurement friction, data licensing, implementation burden |
| Market Model Inputs | source map + data inventory | Public data stack, HPR premium data, state-specific datasets |
| Sources | source register | All internal and external citations |
| Market Segment | synthesized segmentation | Final segmentation output for EPMS |

---

## Workstreams

### Workstream 1: Product Evidence Extraction

Goal: extract a defensible description of what HSRA does from codebase and internal docs.

Key topics:

- dual EPA/OEHHA methodology
- HARP2 parity and auditability
- tract/county/state workflows
- SDOH overlays and compounded risk scoring
- report bundles, HEM outputs, ranked tracts, state-first evidence cards
- Tennessee pilot relevance and public-health use cases

### Workstream 2: HPR / Premium Data Packaging

Goal: explain how public-data HSRA differs from premium-data HSRA enhanced with HPR LCI assets.

Key topics:

- 8 strategic goals and 29 questions from LCI GQM
- individual / household / neighborhood data levels
- what premium HPR data adds beyond public data
- how HPR improves segmentation, outreach, intervention design, and buyer-specific answerability

### Workstream 3: Product Summary Markdown

Goal: write a concise, source-backed markdown document describing what HSRA is, how it works, who it serves, and what outputs it produces.

Required sections:

- what the product does
- data sources and methods
- outputs and decision objects
- target users
- Tennessee pilot example
- public-data mode vs premium-data mode

### Workstream 4: License and Services Opportunity Markdown

Goal: define how HSRA can be sold as software plus configuration/consulting.

Required sections:

- software/license value
- premium-data upsell model
- configuration and implementation services
- state-specific onboarding and data-integration services
- expert interpretation / strategy services where appropriate
- procurement-friendly packaging options

### Workstream 5: Competitive Landscape

Goal: place HSRA against adjacent alternatives without overstating uniqueness.

Required comparison categories:

- enterprise population health analytics
- SDOH/social care networks
- CHNA/community health needs tools
- environmental justice / GIS / risk mapping tools
- rural-health planning analytics
- employer/commercial HRA vendors

### Workstream 6: Government and Public-Sector Market Analysis

Goal: build a buyer map for local/state/federal demand, especially beyond Tennessee.

Required buyer/persona groups:

- state Medicaid agencies
- state health departments
- state rural health offices
- local health departments
- nonprofit hospital community-benefit teams
- environmental justice / environmental health agencies
- cancer control programs
- federally funded rural-health and public-health grant applicants

Required emphasis:

- why other states should care now
- rural health transformation and funding pressure
- tract/county questions agencies need answered
- how HSRA fits grant justification, prioritization, and reporting

---

## Recommended Deep-Research Split

These pieces are likely best handled as separate deep-research tasks so the final outputs are stronger and easier to verify:

1. **Competitive landscape deep research**
2. **50-state government demand and procurement signals**
3. **HPR premium-data differentiation and packaging**
4. **Tennessee pilot business case and replicability narrative**

The base plan and source map should be completed first, then the deeper research passes can enrich the final markdown artifacts and EPMS content.

### When To Do Deep Research

Deep research should happen **after** the following local work is complete:

1. the internal source inventory is built,
2. HSRA current-state capabilities are extracted from `../lsars-hra`,
3. the HSRA deck and HPR inputs are summarized, and
4. the exact unanswered external questions are written down.

That sequence matters because deep research is most useful when it is answering **specific external market questions**, not trying to rediscover what our own codebase and internal docs already say.

### How To Do Deep Research

Use ChatGPT web Deep Research as a **targeted external research pass**, not as the primary author of the whole package.

Recommended workflow:

1. complete local source-map work in this repo first,
2. create one focused deep-research brief per topic,
3. ask for source-linked findings with explicit citations and buyer/program detail,
4. export or save the resulting report,
5. write a local markdown version under `docs/research/hsra/` or `docs/research/market/`, and
6. merge only the supported findings back into EPMS drafts and research documents.

### Best Topics For ChatGPT Web Deep Research

- cross-state demand signals and procurement patterns,
- competitor category mapping and representative vendors,
- federal/state rural-health program funding and compliance drivers,
- public evidence for Tennessee-relevant replication patterns,
- premium-data commercialization patterns where external analogs are useful.

### Topics That Should Stay Local First

- what HSRA currently does,
- which outputs are already implemented,
- what the Tennessee pilot framing already says internally,
- how HPR GQM maps to our product packaging,
- how EPMS sections should be populated from our evidence base.

### Output Contract For Each Deep-Research Pass

Each deep-research pass should come back with:

- a short research question,
- key findings,
- source links,
- buyer/program implications,
- claims that are strong enough to cite directly,
- open questions or weakly supported areas that still need validation.

### Practical Execution Rule

Do **not** block plan execution waiting for all deep-research tasks.

Instead:

- finish the source map and product-summary draft first,
- launch deep research for the externally heavy sections in parallel,
- then use those outputs to strengthen the competitive, government-market, and commercialization markdown files.

---

## Implementation Todo List

- [x] **Task 1: Build source inventory and evidence register**
  - What to do: enumerate all internal and external sources, capture what each source can prove, and identify gaps.
  - Must not do: do not blur internal claims with uncited external claims.
  - Output: `docs/research/hsra/hsra-source-map-and-evidence-register-2026.md`

- [x] **Task 2: Extract product capabilities from codebase and docs**
  - What to do: summarize real capabilities, workflows, outputs, and proof points from `../lsars-hra`.
  - Must not do: do not infer features not supported by code or docs.
  - Output: capability summary section in source map + EPMS draft notes.

- [x] **Task 3: Analyze HSRA deck and explainer materials**
  - What to do: convert visual/product-positioning material into explicit product narrative inputs.
  - Must not do: do not treat visual positioning as proof of implemented capability unless corroborated.
  - Output: product idea, target users, and positioning notes.

- [x] **Task 4: Analyze HPR GQM and workbook**
  - What to do: extract goals, questions, data levels, and premium-data differentiation for packaging.
  - Must not do: do not imply HPR data is included in current public-data HSRA by default.
  - Output: premium-data option framing and market-model inputs.

- [x] **Task 5: Draft HSRA product summary markdown**
  - What to do: write a concise explanation of what HSRA does and how buyers use it.
  - Must not do: do not turn it into sales fluff; keep it evidence-backed.
  - Output: `docs/research/hsra/hsra-product-summary-2026.md`

- [x] **Task 6: Draft license and services opportunity markdown**
  - What to do: define software, premium-data, configuration, and consulting revenue motions.
  - Must not do: do not invent pricing or legal terms.
  - Output: `docs/research/hsra/hsra-license-and-services-opportunity-2026.md`

- [x] **Task 7: Draft competitive landscape markdown**
  - What to do: compare HSRA with adjacent categories and vendors.
  - Must not do: do not claim direct feature parity without evidence.
  - Output: `docs/research/hsra/hsra-competitive-landscape-2026.md`

- [x] **Task 8: Draft government market analysis markdown**
  - What to do: build the public-sector buyer map with Tennessee anchor and 49-state expansion logic.
  - Must not do: do not rely on vague "government interest" language without program or policy grounding.
  - Output: `docs/research/hsra/hsra-government-market-analysis-2026.md`

- [x] **Task 9: Draft EPMS section population sheet**
  - What to do: map draft content into EPMS checklist sections for HSRA.
  - Must not do: do not update EPMS directly until content is reviewed.
  - Output: `docs/research/hsra/hsra-epms-section-draft-2026.md`

- [x] **Task 10: Final review and upload plan**
  - What to do: verify every markdown artifact has citations and define which artifacts should be uploaded/ingested.
  - Must not do: do not leave unsupported claims in final research docs.
  - Output: upload-ready package and next-step checklist.

- [x] **Task 11: File EPMS MCP bug ticket**
  - What to do: create a new bug in the EPMS Jira project covering broken section-save and generic research-save paths.
  - Must not do: do not leave the errors only in local notes or comments.
  - Output: `EPMS-182` linked from this plan and MKT-1.

- [x] **Task 12: Create 10-minute summary document**
  - What to do: write a concise executive research summary that synthesizes the package for a fast reader.
  - Must not do: do not duplicate every underlying doc verbatim.
  - Output: `docs/research/hsra/hsra-overall-research-summary-2026.md`

- [x] **Task 13: Add Mermaid diagrams where helpful**
  - What to do: enrich the summary and/or core HSRA docs with architecture, process, roadmap, or evidence-flow diagrams.
  - Must not do: do not add decorative diagrams without explanatory value.
  - Output: Mermaid-enhanced docs.

- [x] **Task 14: Upload all intended research via EPMS save_research**
  - What to do: attach the local HSRA markdown package to EPMS using `epms.save_research` only.
  - Must not do: do not use `epms.save` for research markdown uploads.
  - Output: EPMS research inventory with the intended HSRA files attached.

- [x] **Task 15: Complete EPMS entity-based enrichment**
  - What to do: populate stakeholder, persona, jtbd, metric, risk, pilot, capability, marketing, and other high-value entities from the local package.
  - Must not do: do not push unsupported claims into entities.
  - Output: enriched EPMS entity graph for HSRA.

---

## Test Matrix

| Deliverable / A/C | Verification Method | Evidence of Completion |
|---|---|---|
| AC-1 / AC-2 | Manual source audit | Every EPMS section maps to cited sources |
| AC-3 | Manual content review | Tennessee pilot business case references documented sources |
| AC-4 | Manual content review | Public-data vs premium-data distinction is explicit |
| AC-5 | Markdown QA review | Product summary exists and cites internal sources |
| AC-6 | Markdown QA review | License/services doc exists and avoids unsupported pricing/legal claims |
| AC-7 | Market research QA review | Competitive categories and representative vendors are cited |
| AC-8 | Program/policy QA review | Government market analysis cites real program demand signals |
| AC-9 | Plan review | Deep-research split documented with rationale |
| AC-10 | Final package review | Every research artifact includes source section and traceability |

---

## Status Updates

| Date | Status | Update |
|---|---|---|
| 2026-03-09 | Planning | Created initial Jira-backed work plan for HSRA EPMS product update and research packaging. |
| 2026-03-09 | Drafted | Created HSRA source map, product summary, license/services opportunity, competitive landscape, government market analysis, and EPMS section draft under `docs/research/hsra/`. |
| 2026-03-09 | Reviewed | Tightened claim hygiene after Oracle review, marked EPMS-safe vs SME-review content, and posted the artifact package back to `MKT-1`. |
| 2026-03-09 | EPMS Pass 1 Partial | Merged ChatGPT Deep Research into the local HSRA package, uploaded 5 research records into EPMS, created 5 customer-question entities, and drafted several safe sections. Section-save endpoints still show an EPMS backend template-generation bug for some saves. |
| 2026-03-09 | Extended | Added follow-up work for EPMS bug filing, save-research-only uploads, overall summary creation, Mermaid enrichment, and full entity-based enrichment. |
| 2026-03-09 | Enriched | Added the overall summary and Mermaid diagrams, uploaded additional HSRA research via `epms.save_research`, created capability/stakeholder/persona/JTBD/metric/risk/pilot/marketing entities, and filed `EPMS-182` for MCP/save-path and schema issues. |

---

## Risks and Open Questions

- HSRA vs HRA naming may need explicit normalization across EPMS, product pages, and technical docs.
- Some product-positioning language in deck/script may exceed what is directly implemented today and must be checked against source evidence.
- Premium HPR data packaging must clearly distinguish licensed external data from current internal/public-data capabilities.
- Competitive claims must remain category-aware and evidence-backed, especially where adjacent tools cover only parts of the problem.
- State-level expansion logic should prioritize funded, policy-driven demand signals over generic market-size claims.
- EPMS section-save operations are currently partially blocked by backend errors referencing missing template assets (`/app/assets/templates/EPMS_TEMPLATE.json`) and a broken generic research-save wrapper.
- `epms.save` should not be used for research markdown uploads; use `epms.save_research` for research and `entity_crud` for entity-based enrichment.
- Some EPMS entity fields enforce backend length limits (for example, a metric create path failed with `value too long for type character varying(100)`) that are not exposed in the published schema; this is now tracked in `EPMS-182`.

---

## Suggested Next Phase After Planning

Execute the workstreams in this order:

1. Source map and capability extraction
2. Product summary markdown
3. License/services opportunity markdown
4. Competitive landscape markdown
5. Government market analysis markdown
6. EPMS section population draft

---

## Ownership and Execution Model

### OpenCode / local repo work

Owner: OpenCode

- maintain the canonical plan in `docs/plans/`
- read and synthesize local evidence from `../lsars-hra`, the HSRA deck, HPR files, and local research docs
- draft and revise the markdown artifacts under `docs/research/hsra/`
- enforce claim hygiene: implemented vs configurable vs premium vs positioning
- convert approved research into EPMS-ready draft language

### ChatGPT web Deep Research

Owner: User runs in ChatGPT web UI; OpenCode prepares prompts and merges outputs

- run the externally heavy research passes that depend on broad web synthesis
- save/export the deep-research results
- return the exported findings to the repo workflow so they can be converted into local markdown files

Best-fit topics:

- competitor deep research
- 50-state demand and procurement signals
- rural-health funding/program analysis
- Tennessee replication/public evidence analysis

### SME / business review

Owner: Product / domain SME(s)

- review any EPMS draft section marked `Needs SME review`
- approve product-family, product-idea, value-prop, and market-segment language
- confirm where HSRA stops and broader LSARS solution positioning begins
- validate premium HPR packaging claims before they are treated as approved messaging

### EPMS update step

Owner: OpenCode via EPMS MCP tools

- use `docs/research/hsra/hsra-epms-section-draft-2026.md` as the MCP update source
- upload/save research markdown into EPMS with `epms.save_research` instead of manual copy/paste
- enrich the product through entity-based MCP paths using `entity_crud`
- hold `Needs SME review` checklist sections until approved or until the section-save backend is repaired
- verify saved EPMS state with fetch/bundle tools before closing the work

### EPMS MCP Execution Phase

This happens in **two passes**, both owned by OpenCode.

#### Pass 1: Safe-content EPMS write pass

When it happens:

- after the local markdown package exists,
- after claim hygiene is complete,
- before waiting on SME review for flagged sections.

Actions:

1. call `epms.research_widget` if the EPMS session needs initialization
2. call `epms.get_product_bundle` and/or `epms.get_product_clusters` to refresh current product state
3. call `epms.save_research` to push the local research markdown into EPMS-backed research records
4. call `epms.entity_crud` to populate safe entity-based data paths
5. call `epms.fetch` or `epms.get_product_bundle` again to verify the saved content

#### Pass 2: SME-reviewed EPMS write pass

When it happens:

- after product/domain SMEs review sections marked `Needs SME review`
- after any deep-research outputs are merged into the local docs, if those outputs materially change the language

Actions:

1. update the local markdown artifacts first
2. call `epms.entity_crud` for reviewed entity-based changes
3. call `epms.save_research` for any revised research markdown that should replace or supplement earlier uploads
4. call `epms.approve_section` only for checklist sections once the checklist save path is healthy and the content is ready
5. call `epms.get_product_bundle` to verify the final saved/approved state

#### EPMS Write Rule

Do not treat the local markdown files as the final destination. They are the staging layer. The actual execution step is the EPMS MCP write pass.

Additional rule: do **not** use `epms.save` for research markdown uploads.

### Recommended practical sequence

1. OpenCode drafts and tightens the local markdown package
2. User runs ChatGPT web Deep Research for the external-heavy topics
3. OpenCode merges those results into the local markdown files
4. OpenCode performs EPMS MCP Pass 1 for `Safe to paste` sections and research uploads
5. SME reviews the flagged sections
6. OpenCode performs EPMS MCP Pass 2 for reviewed sections and approvals
7. OpenCode verifies final EPMS saved state with EPMS fetch/bundle tools
