# Ground Conditions Change the Workflow. Your Agent Should Notice.

## Metadata
- **Post ID**: 2026-T-020
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

Most "AI workflow" posts assume a static pipeline.

Real operations don't work that way.

In MEDICODA, the capture mode changes the entire loop:

Are we capturing physician notes with iPhone voice capture?

Or direct entry?

If it's iPhone voice capture, the workflow has to account for drift between intent and documentation.

**What we built:** a dynamic AI workflow that adapts to ground conditions.

**How it works:**
- **Ingest:** an agent scans the captured notes.
- **Intent check:** it checks the system to see if documentation matches physician intent.
- **Escalate:** if it doesn't match, alerts are pushed so staff can fix documentation within a specific time frame.

This is also where Human-UX (HUX) and Agent-UX (AUX) collide:

If the agent can't reliably read the right artifacts, write the right tasks, and trigger the right alerts (AUX), humans end up doing manual reconciliation (bad HUX).

The critical design choice: **adaptation is a product feature, not a prompt trick.** It lives in tool contracts, audit trails, and escalation rules.

https://lsadigital.com

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/medicoda

## Post asset ideas
- [ ] Flow diagram: iPhone voice capture path vs direct entry path
- [ ] Screenshot/mock: alert pushed to staff with "intent mismatch" reason
- [ ] Example: escalation policy for time-bound documentation follow-up
