# Vibe Coding Without Tickets Becomes Institutional Memory Loss

## Metadata
- **Post ID**: 2026-T-023
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

"Move fast" dies the moment nobody can answer:

What changed?

Why?

And how do we know it works?

This is the balance point we push hard on:

Even in 60% vibe / 40% engineering mode, every user story should have a Jira ticket and a lightweight plan doc.

Not because we love process.

Because it keeps speed sustainable.

**How we run it:**
- **A ticket per story:** small enough to ship, big enough to track.
- **A plan doc per ticket:** the detailed source of truth (assumptions, approach, acceptance checks).
- **Evidence hooks:** for UI work, require proof artifacts (e.g., Playwright screenshots) so "done" means "verified."
- **Sync loop:** Jira stays high-level; the repo plan stays detailed; commits link back to both.

We also automate the boring parts with Claude/OpenCode commands and simple hooks:

- Plan docs are stored locally as markdown and reference Jira ticket numbers.
- Jira carries high-level context + status updates.
- The repo plan carries the details an agent needs to move fast and still hit acceptance checks.

The critical design choice: **vibe coding is allowed to be fast, not allowed to be untraceable.**

If you're building agentic workflows and want speed that doesn't collapse into rework, your system needs tickets, plans, and evidence as first-class artifacts.

https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Screenshot: a minimal plan doc template (scope, acceptance checks, test matrix)
- [ ] Example: a UI ticket requiring Playwright screenshot evidence
- [ ] Diagram: Jira (high-level) <-> repo plan (detailed) <-> commits (traceability)
