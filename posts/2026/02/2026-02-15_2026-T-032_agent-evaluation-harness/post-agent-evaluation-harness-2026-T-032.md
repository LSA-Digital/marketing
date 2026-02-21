# 797 Pollutants, 5 Significant Figures: The Reality of Agent Evals

## Metadata
- **Post ID**: 2026-T-032
- **Audience**: tech
- **Product**: LSARS, HSRA
- **Themes**: AGENTICAI_DEVOPS, FUTUREAI_PRODDEV
- **Expert**: Mike, Keith
- **Depends On**: —
- **Dependency Name**: —
- **Relationship**: Regression testing + pass/fail thresholds for tool-using workflows
- **Assets**: lsars-ca-risk-data.png, lsars-methodology-selector.png
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

797 pollutants validated to 5 significant figures against HARP2. That is the benchmark we set for our LSARS/HSRA evaluation harness. In the world of agentic systems, a demo that works "once" is a failure. Production-grade engineering requires moving beyond vibes and into rigorous, repeatable validation. If you can't measure the behavior of your agent across 84,807 census tracts with 50-state coverage, you aren't ready to ship.

We build evaluation harnesses that treat agent behavior as a first-class artifact. This means testing not just for "accuracy," but for tool correctness, safety boundaries, and stability. When an agent calls a tool, we verify it used the right arguments and respected escalation rules. We use "golden tasks"—representative workflows with known outcomes—to ensure that a model update or a prompt tweak doesn't break existing functionality.

Our dual methodology, combining CA-OEHHA and EPA-AirToxScreen standards, ensures that our agents operate within strict regulatory and scientific boundaries. By using mocks and fixtures for repeatable tool responses, we can run regression tests that block deployment if performance dips. This level of precision is what separates a "cool AI project" from a reliable piece of infrastructure. If it can't be regression-tested with the same rigor as a calculation engine, it isn't ready for CI/CD. We don't ship until the numbers match the ground truth.

## Artifacts
- Remote:
  - https://lsadigital.com

## Post asset ideas
- [ ] Table: HARP2 parity validation results for top pollutants
- [ ] Screenshot: A regression test failure blocking a CI/CD pipeline
- [ ] Diagram: The "Golden Task" lifecycle from intent to validation

### Screenshots

![Methodology selector showing EPA vs CA-OEHHA calculation system being validated](assets/lsars-methodology-selector.png)
*Methodology selector — EPA vs CA-OEHHA calculation system being validated*

![California risk data loaded, the output validated against HARP2 at 8 significant figures](assets/lsars-ca-risk-data.png)
*California risk data loaded — output validated against HARP2 at 8 significant figures*
