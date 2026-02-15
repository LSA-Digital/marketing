# "Just Use an API Key" Doesn't Work for Agents. Draw JWT Boundaries.

## Metadata
- **Post ID**: 2026-T-019
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

Example from work we've shipped: in MEDICODA, we proved architecture and scalability with secure JWT boundaries and multiple EHR integrations.

The moment a tool-using agent touches regulated data, identity stops being a detail.

If your auth story is "just use an API key," you're building a demo.

In MEDICODA, we proved architecture and scalability with secure JWT boundaries and multiple EHR integrations.

**How it works (the parts that matter):**
- **Scoped JWTs:** tokens represent *who/what* is acting, with explicit scopes for *what* they can do.
- **Short-lived credentials:** minimize blast radius; rotate aggressively.
- **EHR isolation:** integrations don't share trust by accident; each boundary is intentional.
- **Audit-ready trails:** every tool call can be traced back to an identity and permission set.

The critical design choice: **agents should not be "special."** They should authenticate like any other actor, with stricter boundaries because they're automated.

That's Vibe Engineering in practice: you can explore quickly, but once the workflow touches real systems, the dial moves toward engineering and the receipts show up in auth, isolation, and audit logs.

https://lsadigital.com

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/medicoda

## Post asset ideas
- [ ] Diagram: JWT scopes and tool permissions for an agent vs a human user
- [ ] Example: token lifecycle (issue, rotate, revoke) for agent tools
- [ ] Checklist: "what must be true before an agent can touch EHR APIs"
