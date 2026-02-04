# Route questions by data priority (highest-confidence first)

## Metadata
- **Post ID**: 2026-T-005
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **SME reviewer**: Mike Idengren
- **CTA**: see artifacts
- **Depends on**: 2026-B-006

## Post
The fastest way to lose trust in an AI system is to answer from the wrong source—confidently.

What we did: we implemented **data-priority routing** so the system answers from the highest-confidence, domain-appropriate sources first, and only expands scope when it has to.

Best-practice stance: “One model + one prompt” is not an architecture. In high-stakes workflows, routing is the architecture.

Guardrails we follow:
- **Authoritative-first**: prefer vetted, domain-specific sources over broad web context.
- **Provenance always**: make it obvious which tier the answer came from and why.
- **Escalation is gated**: only invoke broader research when the high-confidence tiers don’t cover the question.

This reduces cost and latency, but more importantly: it produces answers that can be reviewed and defended—especially when the outcome affects real-world decisions.

If you want the pattern (and a concrete routing rubric) as an artifact, see `https://lsadigital.com`.

## Artifacts
- Local:
  - `./assets/README.md`
- Remote:
  - `https://lsadigital.com`

## Claim boundaries
- Stage: in progress
- What we can say safely:
  - We implemented a data-priority routing pattern to answer from highest-confidence sources first.
  - The design goal is lower latency/cost and clearer provenance for reviewers.
- What we should NOT claim:
  - Specific accuracy, cost, or latency improvements without measured benchmarks.

## Notes (optional)
- Repost kit:
  - Business caption: Faster review happens when the evidence trail is shared.
  - Technical caption: Routing is the architecture—authoritative-first, provenance, gated escalation.
- UTM:
  - `utm_source=linkedin`
  - `utm_medium=organic`
  - `utm_campaign=feb_2026_human_ai`
  - `utm_content=data_priority_routing`
