# Back-Calculations Drift. Source Data Doesn't.

## Metadata
- **Post ID**: 2026-T-007
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS, HRA
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **SME reviewer**: Mike Idengren
- **CTA**: see artifacts
- **Depends on**: 2026-B-008

## Post

Every team that's inherited a calculation system knows the pattern: intermediate values that don't trace back to source documents, formulas that were "optimized" into shortcuts, and nobody quite remembers why the constants are what they are.

We built LSARS health risk calculations from authoritative source data—not from reverse-engineering existing outputs.

Here's what source-data-first engineering looks like:

- **Single source of truth**: Every calculation traces directly to CARB/OEHHA regulatory tables—the same files regulators use. No intermediate transformations, no "we derived it from X."

- **Tested functions, not duplicated logic**: Instead of copying formulas across modules, each calculation is a function tested against the authoritative reference implementation. When the source data updates, the system updates.

- **Auditability by design**: Because we never shortcut the chain from source to output, every number can be traced back to its regulatory origin. Auditors don't have to trust our math—they can verify it.

The result: regulatory-grade consistency that survives code changes, data updates, and team turnover. When California updates their health reference values, we don't "adjust" our system—we re-run against the new source and prove parity again.

Shortcut math is technical debt with regulatory consequences. Source-data-first is how you build systems that stay correct.

See how we approach regulatory-grade calculation architecture: https://lsadigital.com

## Artifacts
- Local:
  - `./assets/` (placeholder for: data lineage diagram, source data → calculation flow)
- Remote:
  - https://www.lsadigital.com/products/hra
