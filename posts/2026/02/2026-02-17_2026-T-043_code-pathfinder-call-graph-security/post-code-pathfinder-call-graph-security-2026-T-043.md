# If You Can't Trace the Call Chain, You Can't Find the Vulnerability

## Metadata
- **Post ID**: 2026-T-043
- **CTA**: see how we build secure AI DevOps workflows at [lsadigital.com](https://lsadigital.com)

## Post
Traditional grep finds where a function is defined, but it cannot tell you who reaches it or what it reaches. In security analysis, the attack surface is defined by the transitive code trace—the path from untrusted input to sensitive operations. If your AI agents only search for text patterns, they are blind to the actual flow of execution.

We replaced our heavy graph-code infrastructure with Code-Pathfinder, a lightweight analysis engine served through a lazy-mcp proxy. It provides 9 specialized tools—including find_symbol, get_callers, get_callees, and resolve_import—to map call graphs across Python, Go, Java, and Docker files. By scoping analysis via the CODE_PATHFINDER_ROOT environment variable, we ensure zero overhead for projects that do not require it.

Our stance is that security-aware agents must navigate the codebase as a graph, not a flat text file.

**How it works:**
- **Transitive Trace:** Agents follow call chains transitively to identify every path from a vulnerable entry point to a sensitive sink.
- **Reverse Mapping:** The get_callers tool reveals the reverse call graph, exposing exactly which modules and functions can trigger a specific operation.
- **Boundary Resolution:** The resolve_import tool tracks execution across module boundaries, ensuring the trace remains intact even in complex, multi-file architectures.

A critical design choice was the move to a lazy-loading architecture, which reduced the initial context cost to approximately 5K tokens for tool definitions. Queries return in less than 100ms, providing near-instantaneous insights into the attack surface without the infrastructure burden of Memgraph or Qdrant.

**Result:**
Engineers and AI agents now perform deep security audits with surgical precision. By tracing forward with get_callees and backward with get_callers, we eliminate the guesswork inherent in pattern-based searching. The result is a verifiable, graph-based understanding of code security that scales with the complexity of the repository.

## Artifacts
- Remote:
  - https://lsadigital.com
- Local:
  - Code-Pathfinder MCP tool definitions in ~/dev/common/lazy-mcp/hierarchy/code-pathfinder/

## Post asset ideas
- [ ] Diagram: Forward + reverse call graph visualization
- [ ] Example: get_callers output tracing who calls a sensitive function
- [ ] Table: Code-Pathfinder's 9 MCP tools and their security use cases
