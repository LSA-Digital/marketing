# The Agent Security Threat Model: Boundaries Beat Policies

## Metadata
- **Post ID**: 2026-T-034
- **CTA**: see artifacts

## Post

Prompt injection isn't a "prompt" problem.

It's a boundary problem.

Tool-using agents add new attack surfaces:

Inputs that try to hijack goals.

Tools that can mutate state.

And credentials that can become a skeleton key.

So we treat agent security as an architecture discipline.

**The boundaries that matter:**
- **Tool authorization:** least privilege by default; escalation for risky actions.
- **Identity:** scoped, short-lived credentials (not shared API keys).
- **Network egress control:** agents shouldn't have arbitrary outbound access.
- **Audit logs:** every action traceable to an identity + policy decision.

The critical design choice: **enforce controls by design, not by policy docs nobody reads.**

That's how you can keep Vibe Engineering fast while still being safe at CI/CD speed.

https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] One-page threat model: prompt injection -> tool misuse -> data exfil
- [ ] Diagram: tool authorization layer + escalation queue
- [ ] Example: least-privilege token scopes for an agent
