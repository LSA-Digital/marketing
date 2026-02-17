# Designing for Agent-UX (AUX): Beyond Human-Readable APIs

## Metadata
- **Post ID**: 2026-T-038
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

An API that is easy for a human to read can still be a nightmare for an AI agent. At LSA Digital, we prioritize Agent-UX (AUX) to ensure our systems are reliable at scale. This is a core pillar of Vibe Engineering: we use vibe coding for rapid exploration, but we ship with production-grade engineering that agents can actually navigate.

Consider our EPMS MCP server. It isn't just a collection of endpoints; it's a 7,294-line specialized interface designed for agentic interaction. We've implemented 14 specific MCP tool endpoints—including `entity_crud`, `hierarchy`, and `bulk`—that cover the full entity lifecycle across 33 database entities.

**Key AUX Design Patterns in EPMS:**
- **Idempotency by Default:** Operations like `copy_product` and `save_draft` use duplicate suppression. If an agent retries a call due to a timeout, it doesn't create a mess of duplicate records.
- **Strict Schema Contracts:** We use Pydantic models to enforce schema contracts. Agents get immediate, structured feedback if they deviate from the expected input.
- **Recovery-Oriented Errors:** Our error responses don't just say "400 Bad Request." They include specific recovery hints that tell the agent exactly what to do next to fix the call.

By designing for the agent first, we reduce the "hallucination surface" and ensure that Continuous Integration (CI/CD) remains stable even as agentic workflows become more complex.

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/epms

## Post asset ideas
- [ ] Code snippet: Pydantic model for `copy_product` with idempotency logic
- [ ] Comparison: Standard REST error vs. AUX-optimized recovery hint
- [ ] Diagram: The 14 MCP tool endpoints and their entity relationships

### Screenshots

![EPMS Kanban board — the UI built on the 14-tool MCP API](assets/epms-kanban-api-surface.png)
*EPMS Kanban board — the UI built on the 14-tool MCP API*

![Product detail showing entity relationships the API exposes](assets/epms-entity-relationships.png)
*Product detail — entity relationships the API exposes*
