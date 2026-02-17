# Your Agent Greps for Keywords. That's Why It Misses the Function It Needs.

## Metadata
- **Post ID**: 2026-T-042
- **CTA**: see how we build AI DevOps workflows at [lsadigital.com](https://lsadigital.com)

## Post
Standard keyword search fails AI agents because code intent rarely matches literal strings. When an agent searches for "role assignment" and the codebase uses "grant_access_to_principal", grep returns zero results. The agent stalls, assuming the capability does not exist.

We replaced our complex graph-code infrastructure with ColGREP, a semantic search tool designed for agentic workflows. By moving away from the decommissioned Memgraph and Qdrant stack, we reduced architectural overhead while increasing search precision.

**How it works:**
- **LateOn-Code-edge model:** ColGREP uses ColBERT embeddings to rank code snippets by semantic purpose rather than character matching.
- **Hybrid search execution:** The tool supports a text pattern pre-filter via the -e flag, allowing agents to combine exact regex constraints with semantic ranking.
- **Automated index lifecycle:** An fswatch daemon monitors the filesystem to trigger index rebuilds, ensuring agents have fresh results within 8 seconds of a file save.

The critical design choice was prioritizing CLI performance and grep-compatibility over complex graph traversals. By supporting standard flags like -E, -F, and --include, we allowed our agents to adopt semantic search without rewriting their existing tool-use logic.

**Result:**
Our agents now find functions by intent across 1,180 files in lsars-hra and 605 files in epms. Query latency sits at ~50ms when using the persistent next-plaid-api Docker server. This is Vibe Engineering — vibe coding for exploration, production-grade engineering for shipping — in practice: rapid exploration backed by production-grade retrieval.

## Artifacts
- Remote:
  - https://lsadigital.com
- Local:
  - ColGREP architecture diagram in ~/dev/common/docs/COLGREP-CODEPATHFINDER-SETUP.md

## Post asset ideas
- [ ] Architecture diagram: ColGREP + next-plaid-api + fswatch pipeline
- [ ] Before/after comparison: grep vs colgrep results for same query
- [ ] Screenshot: colgrep CLI output with semantic results
