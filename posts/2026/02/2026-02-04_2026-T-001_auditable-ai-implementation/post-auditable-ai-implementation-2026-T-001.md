# How We Built Auditable AI: Separating Advisors from Research Agents

## Metadata
- **Post ID**: 2026-T-001
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS, HRA
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Publish target**: 2026-02-10 (Mon)
- **Poster**: company page
- **SME reviewer**: Mike Idengren
- **CTA**: see artifacts at [lsadigital.com](https://lsadigital.com)
- **Depends on**: 2026-B-001 (auditable-ai-trust)

## Post

Compliance failures don’t announce themselves. They show up later—as rework, delays, and decisions nobody wants to defend.

We built an AI workflow that’s explicitly **auditable**, **bounded**, and **designed to escalate safely** when evidence is missing.

We applied this in LSARS permitting work—where trust and auditability aren’t “nice to have,” they’re the whole game.

Key best-practice upgrades we made (high level):
- **Separate read-only answering from research/tool-calling** so common questions stay predictable, and edge cases escalate intentionally.
- **Route by data priority (highest-confidence first)** to reduce ungrounded claims and make provenance clearer.
- **Turn validation into readable artifacts** so reviewers can see what was used, what was calculated, and what changed.

Result: faster answers for common questions, controlled escalation for edge cases, and fewer “we can’t ship this because we can’t explain it” moments.
If you want the patterns and supporting artifacts, start at [lsadigital.com](https://lsadigital.com).

## Artifacts
- Local:
  - `./assets/README.md` (placeholder for architecture diagram)
- Remote:
  - https://www.lsadigital.com/products/lsars
  - https://www.lsadigital.com/products/hra

## Claim boundaries
- Stage: in progress
- What we can say safely:
  - Priority-based routing and controlled escalation to research when governed context is insufficient
  - Primary advisor is read-only; tool-calling is gated
  - Validation generates readable artifacts (not just pass/fail)
- What we should NOT claim:
  - Specific latency/cost numbers without measurement
  - "Zero hallucination" or absolute guarantees
  - Production deployment status beyond "in progress"

## Notes (optional)
- Repost kit:
  - Business caption: "Trust in AI comes from architecture, not promises. Here's how we separated answering from research in LSARS."
  - Technical caption: "Auditable AI needs bounded workflows, governed context, and readable validation artifacts. Here’s the pattern we used."
  - Partner voice caption: "When regulatory-grade trust matters, here's how Human-AI systems should be built."
- Question prompt: "What's your approach to preventing hallucinations in domain-specific AI? Priority routing, guardrails, or something else?"
- UTM:
  - `utm_source=linkedin`
  - `utm_medium=organic`
  - `utm_campaign=feb_2026_human_ai`
  - `utm_content=auditable-ai-implementation`
