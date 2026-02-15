# Prompt and Agent Config Are Production Infrastructure. Roll Them Out Like Code.

## Metadata
- **Post ID**: 2026-T-036
- **CTA**: see artifacts

## Post

Most teams treat prompts and agent config like notes.

Then they "tweak" something on Friday.

And Monday is a postmortem.

In production, agent behavior is a release surface.

So we treat prompt/config changes like infrastructure:

**How we do it:**
- **Version everything:** prompts, tool permissions, routing rules, escalation thresholds.
- **Review changes:** diffs, approvals, and explicit intent.
- **Canary rollout:** ship to a small slice first.
- **Break-glass rollback:** one switch to revert behavior.

The critical design choice: **behavior must be repeatable.** If you can't reproduce what the agent did yesterday, you can't operate it today.

That's how you keep Vibe Engineering speed while still being safe at CI/CD tempo.

https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Example: a config diff with an approval comment
- [ ] Diagram: canary rollout + rollback flow for agent behavior
- [ ] Checklist: what must be true before a prompt/config change hits CI/CD
