# Fine-tuning for regulatory language—without giving up auditability

## Metadata
- **Post ID**: 2026-T-014
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **Expert**: Keith Mangold + Mike Idengren (and/or LSA Digital implementer)
- **CTA**: see artifacts
- **Depends on**: 2026-B-014

## Post
If your model can write regulatory-sounding text, that’s not the win.

The win is: **it can cite the right sources, extract the right clauses, and stay reviewable under pressure.**

We designed a domain-specific fine-tuning approach for regulatory and permitting language that keeps auditability as a first-class constraint.

**How it works:**
- **Curated corpus**: guidance, standards, permitting docs, and agreement templates—kept versioned and attributable.
- **Task-focused outputs**: extraction, citation generation, and plain-language summaries (each with different guardrails).
- **Quality control loops**: expert verification + hallucination detection + citation accuracy checks.

The critical design choice: **fine-tuning never replaces provenance**—outputs must still attach citations and traceable inputs.

**Result:** better domain fit *and* fewer ungrounded claims, because the system is trained and evaluated against what reviewers actually care about.

If you’re building AI for regulated text, optimize for reviewability—not fluency. See the artifacts: https://lsadigital.com

## Artifacts
- Local:
  - `./assets/README.md`
- Remote:
  - `https://lsadigital.com`
