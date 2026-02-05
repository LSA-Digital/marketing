# Graph neural networks for community “network effects”

## Metadata
- **Post ID**: 2026-T-013
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS, HRA
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **Expert**: Mike Idengren (and/or LSA Digital implementer)
- **CTA**: see artifacts
- **Depends on**: 2026-B-013

## Post
Most “community analytics” treat neighborhoods like independent rows in a table.

But communities behave like networks: commute flows, referral patterns, and mobility access create **spillover effects** that simple models miss.

We designed a graph-based approach to model how interventions propagate through connected places.

**How it works:**
- **Graph-first representation**: nodes (tracts, facilities, hubs) and edges (flows, travel time, access patterns).
- **Context as features**: SDOH, baseline risk, demographics, and infrastructure capacity become node/edge signals.
- **Intervention simulation**: estimate how changes in one place affect outcomes in connected places.

The critical design choice: **the graph is a reviewable artifact** (what’s a node/edge, where data came from, what assumptions were made).

**Result:** recommendations can account for “network-aware” impact instead of optimizing a single tract in isolation.

If you’re building decision systems for communities, you need network models—not just better charts. See the artifacts: https://lsadigital.com

## Artifacts
- Local:
  - `./assets/README.md`
- Remote:
  - `https://lsadigital.com`
