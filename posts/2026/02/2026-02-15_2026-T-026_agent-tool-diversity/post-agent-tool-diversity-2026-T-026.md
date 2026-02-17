# The Agent Portfolio: Picking the Right Tool for the Dial

## Metadata
- **Post ID**: 2026-T-026
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

Most teams treat their AI agent like a favorite IDE: they pick one and stick with it. In "Vibe Engineering"—where we balance rapid exploration with production-grade shipping—that’s a recipe for stagnation. Different models have different "vibes," and matching the tool to the task is how you maintain 10x velocity without sacrificing quality.

We don't just use one agent; we manage a portfolio. Our workflow involves fast tab-switching between frontier models and specialized tools to catch different failure modes.

**The Agent Decision Tree:**

- **Continuous Exploration (CE) / High Vibe:** Use **Kimi K2.5** or **ChatGPT Codex**. They are cheap, fast, and "almost as good" as frontier models for rapid prototyping and "vibe coding" through initial assumptions.
- **Complex Refactoring / Mid-Dial:** Use **Cursor** or **Claude Code**. Their ability to index the local codebase and handle multi-file edits makes them the workhorses for turning a prototype into a structured system.
- **Hard Problems / High Engineering:** Use **OpenCode** (powered by Gemini 3 Flash) or **Claude 3.5 Sonnet**. When you're debugging a race condition in a 9-microservice stack or verifying 2,669+ tests, you need the highest reasoning capabilities available.

The goal isn't tool loyalty; it's workflow portability. By keeping our plans, tests, and evals in neutral markdown artifacts, we can swap agents mid-task to get a "second opinion" or a faster iteration loop.

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Matrix: Agent tools mapped by cost, speed, and reasoning depth
- [ ] Screenshot: A fast tab-switch between Kimi and Claude during a refactor
- [ ] Checklist: Artifacts required to make an agent workflow "portable"

### Matrix: Tool/Agent Tradeoffs (Cost vs Speed vs Reasoning)

| Tool/Agent | Cost | Speed | Reasoning | Best For |
|------------|------|-------|-----------|----------|
| explore | Free | Fast | Low | Codebase grep, pattern finding |
| librarian | Cheap | Medium | Medium | External docs, OSS examples |
| oracle | Expensive | Slow | High | Architecture decisions, debugging |
| metis | Expensive | Medium | High | Pre-planning analysis |
| momus | Expensive | Medium | High | Plan review, quality assurance |

### Category-to-Model Assignments (`.opencode/oh-my-opencode.json`)

| Category | Model | Domain |
|----------|-------|--------|
| visual-engineering | google/antigravity-gemini-3-pro-high | Frontend, UI/UX |
| ultrabrain | openai/gpt-5.3-codex (xhigh) | Hard logic, algorithms |
| deep | openai/gpt-5.3-codex (high) | Autonomous problem-solving |
| quick | google/antigravity-gemini-3-flash | Single-file changes |

### Checklist: Portable Agent Workflow Artifacts

- [ ] `AGENTS.md` with rules, architecture, and tool policy
- [ ] Jira ticket with acceptance criteria and scope boundaries
- [ ] Repo-local plan doc in `docs/plans/` with status tracking
- [ ] Deterministic test commands (`pytest`, Playwright, smoke)
- [ ] Traceable commit messages linking ticket and plan
- [ ] Deployment/report evidence folder with generated outputs
- [ ] MCP config pointer (`.mcp.json`) for reproducible tool access
