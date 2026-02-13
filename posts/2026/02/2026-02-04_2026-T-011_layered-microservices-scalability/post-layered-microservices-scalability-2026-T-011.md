# Layered microservices for regulatory-grade scalability

## Metadata
- **Post ID**: 2026-T-011
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS, HSRA
- **Theme**: AI technology
- **Audience**: technical
- **Status**: approved
- **Poster**: company page
- **Expert**: Mike Idengren (and/or LSA Digital implementer)
- **CTA**: see artifacts
- **Depends on**: 2026-B-011

## Post
If you can’t explain **which system produced which number**, you can’t scale trust—you only scale confusion.

For LSARS Permit Intelligence portal and Healh & Social Risk Assessment solutions, we built a layered, API-first microservice architecture so health-risk + community-impact workflows can scale *without* turning into an un-auditable monolith.

**How it works:**
- **Layered services**: each layer has a narrow API and a clear owner (parity → disease mapping → economic burden → reports → SDOH → conversational UX).
- **Isolation by contract**: services exchange explicit inputs/outputs, so validation happens at boundaries—not after the fact.
- **Composable “pipelines”**: higher layers build only on validated outputs from lower layers.

The critical design choice: **the conversational layer is downstream of parity + validation**, not a shortcut around it.

**Result:** you can add capabilities (like SDOH-driven commitments) while keeping the core calculations reviewable, testable, and stable.

If you’re building AI-enabled systems in regulated domains, “microservices” isn’t the point—**audit-friendly ownership is**. See the artifacts at https://lsadigital.com

## Artifacts
- Local:
  - `./assets/README.md`
- Remote:
  - `https://lsadigital.com`
