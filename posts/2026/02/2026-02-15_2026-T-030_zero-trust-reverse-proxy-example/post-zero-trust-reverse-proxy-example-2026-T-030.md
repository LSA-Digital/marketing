# Stop Blaming Vibe Coding for Security Failures -- Practice Zero Trust Security Principles

## Metadata
- **Post ID**: 2026-T-030
- **CTA**: see artifacts

## Post

This is based on security architecture we've actually implemented in production-grade systems - for example, using an identity-aware reverse proxy pattern so internal services don't reinvent (or misconfigure) auth.

Most "zero trust" implementations fail for one boring reason:

They still rely on perfect configuration.

And perfect configuration doesn't exist.

Zero trust is bigger than any single pattern.

But one pattern we use a lot is an identity-aware reverse proxy (Google calls this an **Identity-Aware Proxy**): it enforces policy *before* requests ever reach internal services.

**How this pattern works:**
- **One ingress:** all traffic enters through a single HTTPS entry point.
- **Auth at the edge:** internal services do not implement authentication logic.
- **Policy by route:** the proxy enforces which identities can hit which tool/API surfaces.
- **No accidental exposure:** developers can't "just open a port" and bypass controls.

Other zero trust patterns exist too, and they often stack:

- **Policy Enforcement Points (PEPs) inside the perimeter:** enforce authorization closer to the workload/tool boundary (not only at ingress).
- **Service-level policy:** apply identity and policy checks per service/tool surface, with audit logs.

This matters even more for agentic systems.

Tool-using agents create more calls, more surfaces, and more ways to misconfigure a boundary.

The critical design choice: **security should be enforced by architecture, not by hoping every service got it right.**

See how we think about production-grade security: https://lsadigital.com

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/lsars
  - https://lsars.com/

## Post asset ideas
- [ ] Traffic flow diagram: ingress -> reverse proxy -> internal services
- [ ] Example policy: route-level authorization for tool surfaces
- [ ] Diagram: why internal services don't know how to authenticate
