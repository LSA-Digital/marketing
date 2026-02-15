# Safe Sandbox Tips for Vibe Engineering

## Metadata
- **Post ID**: 2026-T-028
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

We use these rules because we've built real systems where mistakes are expensive - for example, LSARS/HSRA-style workflows with sensitive data and tight security boundaries.

The fastest way to kill Vibe Engineering is a single incident:

"The agent touched prod."

Continuous Exploration (CE) should be fast.

It should also be contained.

**Safe sandbox rules we use (practical, not theoretical):**
- **No prod creds in CE:** if it needs prod access, it's not CE anymore.
- **Read-only by default:** agents start with observation, not mutation.
- **Explicit tool allowlists:** the agent can only call tools that are safe for the current dial setting.
- **Fake data and fixtures:** test with representative shapes, not real records.
- **Kill switches:** one command to disable a tool surface when something goes sideways.

The critical design choice: **sandboxing isn't "security later."** It's what keeps exploration possible.

Move fast. But make sure the blast radius is tiny.

https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Checklist: CE sandbox requirements vs CI/CD requirements
- [ ] Diagram: tool allowlist by dial setting (80/20 -> 20/80)
- [ ] Example: a "break glass" policy for emergency tool shutdown
