# Data manifests beat implicit semantics

## Metadata
- **Post ID**: 2026-T-006
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **SME reviewer**: Mike Idengren
- **CTA**: see artifacts
- **Depends on**: 2026-B-007

## Post
If your model has to *guess* what a domain field means, you’ve already shipped ambiguity into a high-stakes workflow.

What we did: we documented the AI context fields with a **data manifest** so the system can use domain data correctly (and reviewers can tell what it used), instead of relying on “implicit semantics.”

Best-practice stance: the manifest is part of the product. Treat it like code.

Guardrails we follow:
- **Define fields like a contract** (what it is, units, allowed ranges, source-of-truth).
- **Version it** so changes are reviewable and regressions are explainable.
- **Make it reviewer-friendly** (human-readable summaries, not just raw JSON).

This is one of the simplest ways to increase answer quality *without* adding tool calls or “more prompt engineering.” You’re removing misinterpretation at the source.

If you want a concrete manifest template + rubric as an artifact, see `https://lsadigital.com`.

## Artifacts
- Local:
  - `./assets/README.md`
- Remote:
  - `https://lsadigital.com`

## Claim boundaries
- Stage: in progress
- What we can say safely:
  - We use a data manifest to define domain-specific context fields for AI workflows.
  - The goal is reduced misinterpretation and clearer provenance for reviewers.
- What we should NOT claim:
  - Quantified accuracy improvements without measured benchmarks.

## Notes (optional)
- Repost kit:
  - Business caption: Trust requires a trail. Data manifests make the trail legible.
  - Technical caption: If you can’t define your fields, your model can’t either—ship the manifest.
- UTM:
  - `utm_source=linkedin`
  - `utm_medium=organic`
  - `utm_campaign=feb_2026_human_ai`
  - `utm_content=data_manifest`
