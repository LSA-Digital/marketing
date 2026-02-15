# Don't Bolt MCP Onto Your Product. Design Human-UX (HUX) + Agent-UX (AUX) From Day 0.

## Metadata
- **Post ID**: 2026-T-017
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

We've built this in EPMS - for example, exposing an MCP server alongside the product UI so both Human-UX (HUX) and Agent-UX (AUX) are first-class from day 0.

Most "AI product" roadmaps have the same failure mode:

You ship a chat experience (Human-UX (HUX)).

Then you realize you also need tool-using agents.

And the product has no real tool surface.

We built EPMS with an MCP server for a specific reason: product managers want natural-language discovery, while developers (and agents) need a reliable API/tool layer. That's not a bolt-on. It's architecture.

**The key idea:** design Human-UX (HUX) and Agent-UX (AUX) together.

**How it works (in practice):**
- **HUX:** the UI makes intent, context, and artifacts easy to create and review.
- **AUX:** the tool surface is complete enough that an agent can actually do the work (create/read/update artifacts, run workflows, attach evidence) without guessing.
- **Governance hooks:** the tool layer supports approvals, audit logs, and bounded actions (what's allowed vs. escalated).

The critical design choice: **AUX can't be "whatever endpoints we happened to ship."** It has to be a first-class product surface. Otherwise you end up with partial tools that look impressive in demos and collapse under real workflows.

We've watched teams (including big vendors' early "agent" integrations) expose a subset of actions and call it done.

That creates a dead-end: the agent can do 20% of the workflow and a human still has to click the other 80%.

If you're building agentic workflows and want real delivery speed, start with the surfaces:

Human-UX (HUX): the interface where humans execute (create, review, decide, approve, intervene).

Agent-UX (AUX): the interface where agents execute (tool calls, schemas, permissions, error contracts, audit events).

https://lsadigital.com

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/epms

## Post asset ideas
- [ ] Diagram: EPMS UI (HUX) + MCP/tool surface (AUX) + governance hooks
- [ ] Screenshot: an EPMS artifact collection (markdown + spreadsheet) that an agent can query/update
- [ ] Example: "tool coverage" checklist (what agents must be able to do end-to-end)
