# Managing Context Windows Feels Like Managing 4MB of RAM in the 90s

## Metadata
- **Post ID**: 2026-T-029
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

If you're building with agents and you feel like you're back in the 90s squeezing code into 4MB of RAM...

You're not crazy.

Context is now a constrained resource.

And teams that treat it like "just prompts" bleed time.

**How we handle it (practical patterns):**
- **Write a memory artifact:** a short, durable project brief the agent can rehydrate from.
- **Keep manifests:** interfaces, data sources, tool permissions, and invariants in explicit lists.
- **Log decisions:** a tiny decision log beats tribal knowledge.
- **Scope retrieval:** pull only what's needed for the task; avoid dumping the repo.
- **Detect staleness:** force refresh when the agent is about to guess.

The critical design choice: **agents need a repeatable way to rehydrate context.** Otherwise they improvise. And improvisation looks like progress until it becomes rework.

Vibe Engineering is still fast.

But it's fast because the system supplies memory, not because the model is magical.

https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Template: project brief + manifests + decision log (one page)
- [ ] Diagram: "task -> scoped retrieval -> execute" loop
- [ ] Example: a staleness trigger that forces a context refresh
