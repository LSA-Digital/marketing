# The Agent Evaluation Harness: Why Your Demo Fails in Production

## Metadata
- **Post ID**: 2026-T-032
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

We've had to do this for real - for example, parity/validation work (like HSRA/HARP2-style validation) forces you to treat evals as first-class artifacts, not vibes.

The demo worked.

Once.

Production doesn't care.

Agentic systems fail in production because teams ship behavior they can't measure.

So we build evaluation harnesses for tool-using workflows.

**What we evaluate (beyond "accuracy")**:
- **Task completion:** did it finish the job end-to-end?
- **Tool correctness:** did it call the right tool with the right arguments?
- **Safety boundaries:** did it respect permissions and escalation rules?
- **Stability:** does it still work after prompt/model/tool changes?

**How we build it:**
- **Golden tasks:** a small set of representative workflows.
- **Mocks/fixtures:** safe, repeatable tool responses.
- **Baselines:** compare against previous versions so regressions are obvious.
- **Pass/fail thresholds:** ship gates, not vibes.

The critical design choice: **if it can't be regression-tested, it isn't ready for CI/CD.**

https://lsadigital.com

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Diagram: eval harness layers (unit -> integration -> end-to-end)
- [ ] Example golden task with expected tool call sequence
- [ ] Screenshot: a regression report that blocks deployment
