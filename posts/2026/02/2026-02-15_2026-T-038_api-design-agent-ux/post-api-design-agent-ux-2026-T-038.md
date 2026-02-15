# Design APIs for Agent-UX (AUX), Not Just Human-UX (HUX)

## Metadata
- **Post ID**: 2026-T-038
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

We've had to build AUX-first tool surfaces ourselves - for example, EPMS uses an MCP/tool layer so agents can reliably read/write artifacts and workflows without fragile glue code.

An API can be usable by a human developer...

And still be unusable by an agent.

That's why we talk about Agent-UX (AUX).

**AUX-first API design choices that remove agent failure modes:**
- **Idempotency:** retries shouldn't create duplicate side effects.
- **Schema contracts:** strict inputs/outputs; no "stringly typed" chaos.
- **Error messages that teach recovery:** "what happened" + "what to do next."
- **Deterministic pagination and filtering:** agents need predictable iteration.
- **Correlation IDs:** traces that connect intent -> tool call -> outcome.

The critical design choice: **agents will do exactly what your API allows, not what you meant.** AUX is how you encode intent into contracts.

Good AUX improves Human-UX (HUX) too:

Less time debugging.

More time shipping.

https://lsadigital.com

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/epms

## Post asset ideas
- [ ] Example: one endpoint rewritten for idempotency + clearer errors
- [ ] One-page AUX checklist for API/tool surfaces
- [ ] Diagram: correlation ID from UI intent to tool traces
