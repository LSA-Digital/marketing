# Unit Tests Aren't Enough When Correctness Is the Whole Point

## Metadata
- **Post ID**: 2026-T-003
- **Audience**: tech
- **Product**: LSARS, HSRA
- **Themes**: REGULATORY_ALIGNMENT
- **Expert**: Mike, Keith
- **Depends On**: 2026-B-004
- **Dependency Name**: Regulatory Alignment Isn't One-Size-Fits-All
- **Relationship**: Gold-standard parity validation underpins credible EPA/OEHHA alignment
- **Assets**: —
- **CTA**: see artifacts

## Post

If your system produces numbers that regulators will scrutinize, "tests pass" isn't good enough. You need parity checks against an authoritative reference implementation—and regression artifacts that humans can actually review.

We built continuous validation against a gold standard into LSARS health risk calculations.

Here's what that looks like in practice:

- **Reference implementation parity**: Every calculation is compared against the authoritative regulatory tool (HARP2) across hundreds of pollutants, validated to multiple significant figures.

- **Regression artifacts, not just green checks**: Validation generates reports with the actual formulas, intermediate values, and source citations—so reviewers can see *why* the numbers match, not just that they do.

- **Continuous, not one-time**: Parity checks run automatically as data and code evolve, catching drift before it becomes a compliance problem.

The result: confidence at scale. When the underlying health data updates, when the calculation logic changes, when new pollutants are added—the system proves it still matches the gold standard, every time.

In domains where correctness is the whole point, validation has to be more than a checkbox. It has to be evidence.

See how we approach regulatory-grade validation: https://lsadigital.com

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/hra

## Post asset ideas

### Missing assets to add

- [ ] **Validation report example** — Sample report showing formulas, intermediate values, citations
- [ ] **Parity test output screenshot** — Example of HARP2 comparison results
- [ ] **Regression test dashboard** — Showing continuous validation status
