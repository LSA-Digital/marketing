# Graph neural networks for community “network effects”

## Metadata
- **Post ID**: 2026-T-013
- **CTA**: see artifacts

## Post
Neighborhoods can't be understood with a simple spreadsheet table.

Communities behave like networks: commute flows, referral patterns, and mobility access create **spillover effects** that simple models miss.

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
