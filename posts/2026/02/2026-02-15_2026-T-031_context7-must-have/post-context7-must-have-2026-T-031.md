# Stop Letting Models Guess. Force a Docs Lookup Step (CONTEXT7)

## Metadata
- **Post ID**: 2026-T-031
- **CTA**: see artifacts

## Post

This is a workflow rule we use in practice - for example, in this repo we enforce "CONTEXT7 FIRST" so agents look up authoritative docs instead of guessing.

Even strong models still do something expensive and unnecessary:

This is true even for today's most sophisticated models (e.g., Claude 4.6).

They try to solve problems they should look up.

This is why CONTEXT7 is non-optional in agentic development.

If a library/framework question has an authoritative answer, the agent should be forced to consult docs first.

**The workflow shift:**
- **Resolve the library:** find the right doc set.
- **Query the docs:** get the specific API behavior.
- **Then implement:** now you can code with confidence.

The critical design choice: **"look it up" is a tool, not a suggestion.**

It improves Agent-UX (AUX) because the agent has a reliable path to truth.

And it improves Human-UX (HUX) because developers spend less time cleaning up confident mistakes.

See our approach: https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Screenshot: a real Context7 lookup in a dev workflow
- [ ] Mini-checklist: "when an agent must consult docs"
- [ ] Example: before/after diff of guessing vs lookup-driven implementation
