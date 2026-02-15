# Humans Expect Answers. Agents Need the Same Inside Your Codebase.

## Metadata
- **Post ID**: 2026-T-027
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

Humans ask:

"Where is this defined?"

"What depends on it?"

"Why did we build it this way?"

And they expect answers.

Agents need the same ability inside a dev environment, especially when context windows compress.

We built a "codebase memory" layer using open-source tooling (graph-code + Memgraph) and a vector index (Qdrant) so agents can retrieve both structure and meaning.

**How it works:**
- **Graph memory:** symbols, relationships, dependencies (the map).
- **Vector memory:** semantic recall across docs, plans, and code (the intuition).
- **Artifact-first retrieval:** plans and manifests are prioritized before guessing.

The critical design choice: **if an agent can't reliably rehydrate context, it will invent it.**

So we don't ask agents to be "smarter." We give them a better environment.

https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Diagram: graph (structure) + vector (meaning) retrieval working together
- [ ] Example: "where is X defined" answered with links to code + plan doc
- [ ] Screenshot: a retrieval trace showing why a source was selected
