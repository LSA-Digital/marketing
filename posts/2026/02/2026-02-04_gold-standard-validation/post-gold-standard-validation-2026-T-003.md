# Unit Tests Aren't Enough When Correctness Is the Whole Point

## Metadata
- **Post ID**: 2026-T-003
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS, HRA
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **SME reviewer**: Mike Idengren
- **CTA**: see artifacts
- **Depends on**: 2026-B-004

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
- Local:
  - `./assets/` (placeholder for: validation report example, parity test output screenshot)
- Remote:
  - https://www.lsadigital.com/products/hra

## Claim boundaries
- Stage: deployed
- What we can say safely:
  - LSARS validates against HARP2 as the gold standard
  - Validation covers hundreds of pollutants
  - Parity is checked to multiple significant figures
  - Validation generates human-readable reports with formulas and citations
  - Checks run continuously as code/data evolve
- What we should NOT claim:
  - Exact number of pollutants without citing product page
  - Specific significant figure count without verification
  - That this replaces regulatory certification

## Notes
- Repost kit:
  - Business caption: "When regulators scrutinize your calculations, 'tests pass' isn't enough. Here's how LSARS builds confidence through continuous gold-standard validation."
  - Technical caption: "Parity checks against HARP2, validation reports with actual formulas, continuous regression testing. Correctness as evidence, not just assertions."
  - Partner voice caption: "Regulatory-grade systems need regulatory-grade validation. This is what that looks like in practice."
- Question prompt: "How do you validate correctness in systems where the numbers really matter?"
- UTM:
  - `utm_source=linkedin`
  - `utm_medium=organic`
  - `utm_campaign=feb_2026_human_ai`
  - `utm_content=gold-standard-validation`
