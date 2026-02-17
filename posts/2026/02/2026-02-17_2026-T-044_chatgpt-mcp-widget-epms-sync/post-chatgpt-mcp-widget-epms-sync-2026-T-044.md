# We Built a ChatGPT Widget. The Hard Part Wasn't the UI.

## Metadata
- **Post ID**: 2026-T-044
- **CTA**: see how we build AI product tools at [lsadigital.com](https://lsadigital.com)

## Post
Building a UI that sits inside ChatGPT is straightforward. Building a bidirectional data bridge that maintains the integrity of a complex product management system (EPMS) while providing a seamless researcher experience is where the engineering challenge lies. We built the EPMS Widget using the Model Context Protocol (MCP) to turn ChatGPT into a live interface for our product backend.

**How it works:**
- **Multi-layer architecture**: The widget runs as an iframe inside ChatGPT, communicating via postMessage JSON-RPC to a Node.js MCP Proxy (port 3099), which forwards to the Python Backend (port 8000).
- **Directional UX convention**: ▲ means upload FROM chat TO app. ▼ means download FROM app INTO chat. Users see the direction of data flow at a glance.
- **Dual-mode context injection**: `updateModelContext` handles deferred injection of large datasets; `sendMessage` fires immediate triggers that require an instant LLM response.

**The critical design choice:**
We implemented a Node.js proxy because the current Python MCP SDK lacks `registerAppTool()` support. This proxy serves 24 tools, 13 resources, and 5 prompts, acting as the essential translation layer between the frontend widget and the backend logic. To ensure stability in restricted environments like the Claude.ai sandbox, the widget is compiled into a single-file ESM bundle (~538KB) using esbuild, as these environments reject multi-script patterns.

**Result:**
The prototype is fully functional with 102/102 integration tests passing across five development phases. By designing for both Human-UX (HUX) — the researcher's experience — and Agent-UX (AUX) — the LLM's ability to interface via MCP — we built a Vibe Engineering workflow: vibe coding for rapid exploration, production-grade engineering for shipping.

## Artifacts
- Remote:
  - https://lsadigital.com
  - https://lsadigital.com/products/epms

## Post asset ideas
- [ ] Diagram: The communication stack showing ChatGPT ↔ postMessage ↔ Node.js Proxy ↔ Python Backend.
- [ ] Code Snippet: The `updateModelContext` implementation for handling large product requirement documents.
- [ ] Screenshot: The progressive disclosure UI showing the transition from collapsed metric chips to expanded detail view.
