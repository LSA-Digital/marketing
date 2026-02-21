# Ensemble uncertainty quantification: bounds you can explain

## Metadata
- **Post ID**: 2026-T-012
- **Audience**: tech
- **Product**: LSARS, HSRA
- **Themes**: LOCATION_INTELLIGENCE, COMMUNITY_TRANSPARENCY
- **Expert**: Mike
- **Depends On**: 2026-B-012
- **Dependency Name**: Permit approvals shouldn't be surprises. Bound the date.
- **Relationship**: Produces explainable date bounds plus uncertainty drivers for planning
- **Assets**: —
- **CTA**: see artifacts

## Post
Don't just calculate a statistical “confidence interval” and call it done.

If you can’t answer **what the uncertainty means** and **what’s driving it**, you’re not shipping confidence—you’re shipping ambiguity.

For LSARS Permit Intelligence, we designed an uncertainty-quantification approach that produces *bounds + drivers* that humans can review.

**How it works:**
- **Multiple lenses**: ensembles (e.g., Monte Carlo + sensitivity analysis + Bayesian structures) to estimate variance instead of hiding it.
- **Driver attribution**: identify which inputs/factors contribute most to the spread (so teams can reduce uncertainty deliberately).
- **Decision-friendly outputs**: intervals and scenarios that map to “what changes the date / risk” instead of raw model internals.

The critical design choice: **uncertainty outputs must be explainable artifacts**, not opaque numbers.

**Result:** reviewers get bounded, defensible estimates—and engineers get a roadmap for where to invest in better data.

If you’re building high-stakes AI, don’t ship “confidence.” Ship bounds, drivers, and reviewable evidence.

## Post asset ideas

Add any supporting artifacts for this post here.

### Suggested assets
- Example “bounds + drivers” report section (mock)
- Sensitivity chart: top contributors to uncertainty
- Short design note: how uncertainty artifacts are generated and reviewed
