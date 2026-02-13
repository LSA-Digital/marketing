# Route questions by data priority (highest-confidence first)

## Metadata

- **Post ID**: 2026-T-005
- **CTA**: see artifacts
- **Depends on**: 2026-B-006

## Post

The fastest way to lose trust in an AI system is to give a nonsense answer (hallucinate).

For the LSARS Health & Social Risk Assessment (HSRA) + Permitting solution, "all permitting is local", and frequently, local information is more important than generic national information.  We implemented **data-priority routing** so the AI Agents answer questions from the highest-confidence, domain-appropriate sources first, and only expands scope when it has to.

When review capacity is the constraint, the system has to reduce rework—not add another portal. Priority routing creates a shared evidence trail: fewer nonsense answers, clearer provenance, and fewer “which version is true?” loops.

The lesson: “One model + one prompt” is not an effective agentic architecture. For questions that need to draw from vairous complex data sets, agents need guardrails (and sometimes, hard rules).

Key Guardrails we follow:

- **Authoritative-first**: prefer vetted, domain-specific sources over broad web context.
- **Transparency**: make it obvious which tier the answer came from and why.
- **Escalation is gated**: only invoke broader research when the high-confidence tiers don’t cover the question, and assign AI agent scope & permissions accordingly.

**Result**: fewer rework loops and answers that can be reviewed and defended—especially when the outcome affects real-world decisions. (Cost and latency improve too, but that’s secondary.)

If you want the pattern (and a concrete routing rubric) as an artifact, see `https://lsadigital.com`.

## Artifacts
- Remote:
  - `https://lsadigital.com`

## Post asset ideas

No assets have been created for this post yet.

If we want a concrete artifact for engineers, capture one of these:
- 1-page “routing rubric” (source tiers + when to escalate)
- Diagram: Tier 1 (authoritative) → Tier 2 (domain) → Tier 3 (research), with provenance annotations
- Redacted example: same question answered at two tiers, showing why tier choice matters
