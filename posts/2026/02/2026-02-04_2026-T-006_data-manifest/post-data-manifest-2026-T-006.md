# Data manifests beat implicit semantics

## Metadata
- **Post ID**: 2026-T-006
- **CTA**: see artifacts
- **Depends on**: 2026-B-007

## Post
AI agents are not good at guessing what you mean.  In a ChatGPT back-and-forth dialog, you can just correct it.  In an autonomous production system, the AI agents have to go by guardrails and rules.

For our partners' LSARS Permitting + Community Health & Social Risk Assessment (HSRA) solution, we documented the AI context fields with a **data manifest** so the system can use domain data correctly (and reviewers can tell what it used), instead of relying on “implicit semantics.”

The manifest is part of the product. Treat it like code.

Guardrails we follow:
- **Define fields like a contract** (what it is, units, allowed ranges, source-of-truth).
- **Version it** so changes are reviewable and regressions are explainable.
- **Make it reviewer-friendly** (human-readable summaries, not just raw JSON).

This is one of the simplest ways to increase answer quality *without* adding tool calls or “more prompt engineering.” You’re removing misinterpretation at the source.

If you want a concrete manifest template + rubric as an artifact, see `https://lsadigital.com`.

## Artifacts
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

## Post asset ideas

No assets have been created for this post yet.

Good artifacts for engineers:
- A 1-page data manifest template (field name, meaning, units, source, constraints, examples)
- “Before/after” example: same prompt with/without manifest (showing why implicit semantics fails)
- Diagram: domain dataset → manifest → model context → provenance in answer
