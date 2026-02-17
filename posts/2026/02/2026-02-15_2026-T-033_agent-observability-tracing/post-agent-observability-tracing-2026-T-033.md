# Beyond Logs: Tracing Agent Intent Through 13 API Routers

## Metadata
- **Post ID**: 2026-T-033
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

Monitoring an agentic system with standard logs is like trying to understand a movie by looking at a single frame every ten minutes. You might see the state, but you'll miss the story. In production, observability means being able to answer "Why did it do that?" at any point in a complex workflow. This requires more than just text files; it requires structured logging with request ID correlation that follows an intent from the initial prompt through every tool call and calculation layer.

In our LSARS architecture, a single user request might traverse 13 API routers and 4 distinct calculation layers. Without a unified trace timeline, debugging a failure becomes an exercise in guesswork. We implement end-to-end tracing that captures tool inputs and outputs, latency, and cost budgets per step. If an agent decides to retry a failed tool call or escalate to a human, the "why" is preserved in the trace. We use a specific error taxonomy to differentiate between transient failures that can be auto-recovered and structural failures that require a hard stop.

This level of technical depth is essential for maintaining control as you move from "vibe coding" exploration to production-grade CI/CD. By correlating request IDs across our 9 Docker microservices, we can reconstruct the exact context the agent used to make a decision. This isn't just for debugging; it's for optimization. When you can see the trace of a 7,294-line MCP server interaction, you can identify bottlenecks and refine tool permissions with surgical precision.

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Screenshot: A trace timeline showing request ID correlation across services
- [ ] Example: Structured log entry with intent and tool metadata
- [ ] Diagram: The 4 calculation layers and how traces flow through them

### Screenshots

![Pennsylvania view showing the 4-layer calculation architecture in action](assets/lsars-pa-layered-architecture.png)
*Pennsylvania view — 4-layer calculation architecture in action*

![Health Risk Advisor chatbot showing observable agent request/response interaction](assets/lsars-chatbot-observable.png)
*Health Risk Advisor chatbot — observable agent request/response interaction*
