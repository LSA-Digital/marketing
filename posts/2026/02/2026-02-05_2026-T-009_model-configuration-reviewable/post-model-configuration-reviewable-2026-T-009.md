# Model Selection Is a Product Decision. Treat It Like Configuration.

## Metadata
- **Post ID**: 2026-T-009
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS, HRA
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **SME reviewer**: Mike Idengren
- **CTA**: see artifacts
- **Depends on**: 2026-B-009

## Post

Your team picked Claude for the advisor flow, GPT-4 for research, and a custom fine-tune for extraction. Six months later, nobody remembers why—or how to change it safely.

**Model selection isn't a one-time decision. It's configuration that needs ownership, traceability, and the ability to change without breaking production.**

We built LSARS with explicit model configuration as a first-class concern:
- **Separate environment variables** for each model role (advisor, research, extraction)
- **Clear ownership** of which model does what—and why
- **Safe swap paths** for testing new models without touching production flows

Why this matters:

- **Audit readiness**: When someone asks "what model generated this output?"—you can answer
- **Operational control**: You can upgrade, downgrade, or replace models deliberately, not accidentally
- **Cost visibility**: Different models at different price points, assigned to appropriate tasks

Implicit model selection—where it's buried in code or spread across config files—creates drift. You end up with different models in dev vs. prod, or the wrong model handling sensitive tasks, and nobody knows until it breaks.

**Make model configuration explicit. Treat it like any other infrastructure decision: documented, versioned, and reviewable.**

https://lsadigital.com

## Artifacts
- Local:
  - `./assets/README.md`
- Remote:
  - https://www.lsadigital.com/products/lsars
  - https://lsadigital.com
