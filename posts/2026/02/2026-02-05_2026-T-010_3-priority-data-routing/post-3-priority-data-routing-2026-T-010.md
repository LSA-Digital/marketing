# 3-Priority Data Routing: Answer from the Best Source First

## Metadata
- **Post ID**: 2026-T-010
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS, HSRA
- **Theme**: AI technology
- **Audience**: technical
- **Status**: approved
- **Poster**: company page
- **Expert**: Mike Idengren
- **CTA**: see artifacts
- **Depends on**: 2026-B-010

## Post

Most AI systems treat every question the same: throw it at the LLM and hope for the best. That's why they hallucinate on domain questions and burn tokens on answers that were already in the database.

We built a 3-priority routing architecture that answers from the most authoritative source first, and only escalates when necessary.

That matters because “where to invest” can’t come from generic model prose. It has to come from authoritative tract-level HSRA + SDOH evidence, so commitments are targeted, measurable, and defensible.

**How it works:**

- **P1 (Evidence Cards)**: Pre-validated, cited HSRA + SDOH facts (e.g., state- and tract-relevant baselines). If the answer exists here, we return it instantly — no LLM inference required.
- **P2 (LSARS Database)**: HSRA calculations, SDOH metrics, air quality data, and intervention-relevant context. The primary advisor model has this context pre-loaded and answers without tool calls.
- **P3 (Research Agent)**: Only when P1 and P2 are insufficient does a separate research model invoke tools (e.g., web search, disease impact lookups, pollutant database).

The critical design choice: **the primary advisor model has no tool-calling capability**. It can only answer from what it's given. This eliminates front-line hallucination and security risks.

The research agent is gated and auditable. Every tool call is logged. Every external source is cited.

**Result**: lower latency, lower cost, and investment answers grounded in authoritative evidence—not model speculation.

See how priority-based routing improves AI reliability at https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com/

## Post asset ideas

### Needed assets
- [ ] Architecture diagram showing P1 → P2 → P3 routing flow
- [ ] Example showing same question answered at different priority levels
- [ ] Code snippet or config showing advisor model (no tools) vs research model (with tools)

### Notes
- Emphasize the "no tool-calling for primary advisor" as a deliberate security/reliability choice
- Could show latency/cost comparison between P1, P2, P3 responses
- Consider showing the data manifest concept (how context is pre-loaded for P2)
