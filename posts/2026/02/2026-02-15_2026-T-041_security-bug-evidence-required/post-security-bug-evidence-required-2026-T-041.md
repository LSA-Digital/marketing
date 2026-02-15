# A Security Bug Isn't Fixed Until the Evidence Ships

## Metadata
- **Post ID**: 2026-T-041
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

This is one of the simplest automated compliance rules we practice:

Any security bug requires documentation that shows it was fixed.

Not vibes.

Evidence.

For example, we require Jira ticket analysis so the fix is reviewable and auditable later.

**What we expect in a "security fix" ticket:**
- **Impact + scope:** what was at risk, and what wasn't.
- **Root cause:** what allowed the bug to exist.
- **Fix summary:** what changed and why it closes the hole.
- **Verification evidence:** tests, reproduction steps, or screenshots/logs showing the fix works.
- **Deployment note:** where/when it was deployed (deployment is not the same as release).

The critical design choice: **compliance isn't a separate deliverable.** It's the byproduct of disciplined engineering artifacts.

That's how you keep Vibe Engineering fast without creating security debt.

https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Jira ticket template for security issues (impact, root cause, evidence)
- [ ] Example: a redacted "before/after" reproduction checklist
- [ ] Diagram: drift alert -> ticket -> fix -> evidence -> close loop
