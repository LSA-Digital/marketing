# From Chat to Diagram: The Architecture of Live Process Building

## Metadata
- **Post ID**: 2026-T-045
- **CTA**: see how we build AI process tools at [lsadigital.com](https://lsadigital.com)

## Post
Static process maps are a failure of synchronization. To solve this, we've implemented a real-time process design environment that bridges the gap between LLM reasoning and structured visual state. By integrating a persistent research widget directly into the ChatGPT and Claude.ai interfaces, we enable a bidirectional flow where the conversation state and the process model are always in sync.

**How it works:**
- **LLM-driven state updates**: When a user describes a process change, the LLM interprets intent and invokes `research_widget` with a ProcessNodesUpdate payload. Supported node types: start, decision, branch_yes/no, subprocess, merge, end.
- **Streaming preview rendering**: `ontoolinputpartial` captures progressively-complete JSON during generation. The widget "heals" partial data and renders real-time diagram previews before the tool call even completes.
- **Sandboxed communication**: Single-file ESM bundle (~538KB), vanilla DOM, zero direct network calls. All data flows: Widget → Host → Node.js MCP Proxy → Python Backend.

The critical design choice was the implementation of a four-channel communication model. We've proven reliable data exchange between the Widget and the Server, the Widget and the LLM context, the Widget and the LLM message stream, and the LLM back to the Widget. This ensures that whether a user is downloading research docs into the chat context or uploading updates from the chat to the backend, the integrity of the process model remains intact.

**Result:**
We have achieved 102/102 integration tests across five development phases. The prototype successfully demonstrates a progressive disclosure UI where collapsed panels show high-level metric chips while expanded views reveal the full, interactive process diagram. This architecture transforms the LLM from a simple text generator into a structured process engineering partner.

## Artifacts
- Remote:
  - https://lsadigital.com
  - https://lsadigital.com/products/epms

## Post asset ideas
- [ ] Diagram: The 4-channel communication architecture between LLM, Host, Proxy, and Widget.
- [ ] Code Snippet: Example of a ProcessNodesUpdate JSON payload with decision and branch nodes.
- [ ] Screenshot: The "healed" JSON preview rendering in the persistent floating panel.
