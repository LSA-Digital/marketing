# The Day Our Agent Stopped Guessing: Building Codebase Memory

## Metadata
- **Post ID**: 2026-T-027
- **Audience**: tech
- **Product**: LSARS, HSRA
- **Themes**: FUTUREAI_DEVOPS, AGENTICAI_DEVOPS
- **Expert**: Mike, Keith
- **Depends On**: —
- **Dependency Name**: —
- **Relationship**: Codebase memory (graph + vector) so agents can rehydrate context reliably
- **Assets**: lsars-california-complexity.png, lsars-health-risk-advisor.png, lsars-hotspot-analysis.png
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

We were three weeks into the LSARS build when the "vibe" hit a wall. We had 9 microservices, 13 API routers, and a growing pile of 2,669+ test functions. Our agents were fast, but they were starting to hallucinate internal dependencies. They were "vibe coding" on top of a system they no longer fully understood.

The problem wasn't the model's intelligence; it was its memory. To fix it, we built a codebase memory layer that combined structural logic with semantic intuition.

We started with **Graph-code + Memgraph**. This gave our agents a literal map of the codebase—a symbol graph that tracked every function call, class inheritance, and microservice boundary. If an agent wanted to know what depended on the `aermod` service, it didn't have to grep; it just queried the graph.

But maps only tell you where things are, not what they *mean*. So we added **Qdrant** for semantic vectors. This allowed agents to search for "intuition"—finding relevant code patterns or old plan docs based on meaning rather than just keywords.

The result? Our agents stopped guessing. They started every task by "rehydrating" their context from the graph and the vector store. This is the essence of "Vibe Engineering": we give the agent the freedom to explore at high speed, but we anchor that exploration to a ground truth that lives inside the infrastructure, not just the prompt.

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Diagram: The Codebase Memory Layer (Graph + Vector + Agent)
- [ ] Screenshot: A Memgraph visualization of microservice dependencies
- [ ] Example: A Qdrant search result finding a relevant refactor pattern

### Screenshots

![LSARS with California loaded, showing the scale and complexity agents must understand](assets/lsars-california-complexity.png)
*LSARS with California loaded — the scale and complexity agents must understand*

![Hotspot Analysis panel showing analytical capability built on codebase memory](assets/lsars-hotspot-analysis.png)
*Hotspot Analysis panel — analytical capability built on codebase memory*

![Health Risk Advisor AI chatbot powered by graph and vector memory](assets/lsars-health-risk-advisor.png)
*Health Risk Advisor AI chatbot — the agent surface powered by graph + vector memory*
