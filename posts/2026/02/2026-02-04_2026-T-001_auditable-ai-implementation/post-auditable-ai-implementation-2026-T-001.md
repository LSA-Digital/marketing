# How We Built Auditable AI: Separating Advisors from Research Agents

## Metadata
- **Post ID**: 2026-T-001
- **Audience**: tech
- **Product**: LSARS, HSRA
- **Themes**: AGENT_GUARDRAILS, COMMUNITY_TRANSPARENCY
- **Expert**: Mike, Keith
- **Depends On**: 2026-B-001
- **Dependency Name**: Trust Through Auditable AI
- **Relationship**: Advisor/research-agent split makes the audit trail inspectable
- **Assets**: zero-trust-boundary-diagram.png
- **CTA**: see artifacts at [lsadigital.com](https://lsadigital.com)

## Post

Compliance failures don't announce themselves. They show up later—as rework, delays, and decisions nobody wants to defend.

We built an AI workflow that's explicitly **auditable**, **bounded**, and **designed to escalate safely** when evidence is missing.

We applied this in LSARS permitting work—where trust and auditability aren't "nice to have," they're the whole game.

Key best-practice upgrades we made (high level):
- **Separate read-only answering from research/tool-calling** so common questions stay predictable, and edge cases escalate intentionally.
- **Route by data priority (highest-confidence first)** to reduce ungrounded claims and make provenance clearer.
- **Turn validation into readable artifacts** so reviewers can see what was used, what was calculated, and what changed.

Result: faster answers for common questions, controlled escalation for edge cases, and fewer "we can't ship this because we can't explain it" moments.
If you want the patterns and supporting artifacts, start at [lsadigital.com](https://lsadigital.com).

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/lsars
  - https://www.lsadigital.com/products/hra

## Post asset ideas

### Missing assets (add before publish)

- [ ] Architecture diagram — 3-tier priority routing (P1/P2/P3)
- [ ] Zero-trust boundary diagram (optional)
- [ ] Validation report with KaTeX formulas screenshot

### Asset guidelines

- LinkedIn image dimensions: 1200×627 px (1.91:1 ratio)
- Technical diagrams: keep labels readable at small sizes
- Use LSA Digital brand colors if available
