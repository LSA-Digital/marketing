# Graph neural networks for community “network effects”

## Metadata
- **Post ID**: 2026-T-013
- **Audience**: tech
- **Product**: LSARS, HSRA
- **Themes**: LOCATION_INTELLIGENCE, RISK_INVESTMENTS, SMART_MOBILITY
- **Expert**: Mike, Keith
- **Depends On**: —
- **Dependency Name**: —
- **Relationship**: No direct relationship, but leave this article as future placeholder after LSARS-532 Permit Location Optimizer has made some progress.
- **Assets**: —
- **CTA**: see artifacts

## Post
Neighborhoods can't be understood with a simple spreadsheet table.

Communities behave like networks: commute flows, referral patterns, and mobility access create **spillover effects** that simple models miss.

That matters in permitting: detours shift congestion to parallel streets, curb rules move parking demand block-to-block, and a new shuttle route changes access well beyond a single tract.

We designed a graph-based approach to model how interventions propagate through connected places.

**How it works:**
- **Graph-first representation**: nodes (tracts, facilities, hubs) and edges (flows, travel time, access patterns).
- **Context as features**: SDOH, baseline risk, demographics, and infrastructure capacity become node/edge signals.
- **Intervention simulation**: estimate how changes in one place affect outcomes in connected places.

The critical design choice: **the graph is a reviewable artifact** (what’s a node/edge, where data came from, what assumptions were made).

**Result:** recommendations can account for “network-aware” impact instead of optimizing a single tract in isolation.

If you’re building decision systems for communities, you need network models—not just better charts. See the artifacts: https://lsadigital.com

## Artifacts
- Remote:
  - `https://lsadigital.com`

## Post asset ideas

Add any supporting artifacts for this post here.

### Suggested assets
- Graph schema one-pager: node/edge types + feature fields + data sources
- Example “network effect” visualization (mock)
- Assumptions checklist (what the graph includes/excludes)

## Citations / Sources
- https://arxiv.org/abs/2101.11174 (Survey: graph neural networks applied to traffic forecasting and transportation networks)
