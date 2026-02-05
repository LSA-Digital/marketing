# 3-Priority Data Routing: Answer from the Best Source First

## Metadata
- **Post ID**: 2026-T-010
- **Channel**: LinkedIn post
- **Target page**: [LSA Digital](https://www.linkedin.com/company/lsadigital/)
- **Product**: LSARS, HRA
- **Theme**: AI technology
- **Audience**: technical
- **Status**: draft
- **Poster**: company page
- **SME reviewer**: Mike Idengren
- **CTA**: see artifacts
- **Depends on**: 2026-B-010

## Post

Most AI systems treat every question the same: throw it at the LLM and hope for the best. That's why they hallucinate on domain questions and burn tokens on answers that were already in the database.

We built a 3-priority routing architecture that answers from the most authoritative source first—and only escalates when necessary.

**How it works:**

- **P1 (Evidence Cards)**: Pre-validated, state-specific health data with citations. If the answer exists here, we return it instantly—no LLM inference required.
- **P2 (LSARS Database)**: HRA calculations, SDOH metrics, air quality data. The primary advisor model has this context pre-loaded and answers without tool calls.
- **P3 (Research Agent)**: Only when P1 and P2 are insufficient does a separate research model invoke tools—web search, disease impact lookups, pollutant databases.

The critical design choice: **the primary advisor model has no tool-calling capability**. It can only answer from what it's given. This eliminates a class of hallucination and security risks.

The research agent is gated and auditable. Every tool call is logged. Every external source is cited.

**Result**: Lower latency, lower cost, and answers that come from authoritative data—not model speculation.

See how priority-based routing improves AI reliability at https://lsadigital.com

## Artifacts
- Local:
  - `./assets/README.md`
- Remote:
  - https://lsadigital.com/
