# Adapting to the Ground Truth: The MEDICODAX Workflow Story

## Metadata
- **Post ID**: 2026-T-020
- **Audience**: tech
- **Product**: MEDICODAX
- **Themes**: AGENTICAI_FIRST, TECH_UX
- **Expert**: Mike
- **Depends On**: —
- **Dependency Name**: —
- **Relationship**: Dynamic workflow adaptation (iPhone voice capture vs direct entry)
- **Assets**: medicodax-dashboard-time-savings.png, medicodax-mobile-queue-voice.png, medicodax-wizard-direct-entry.png
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

In medical coding, the "ground truth" isn't a static document; it's a moving target. When we built MEDICODAX, we realized that a rigid AI pipeline would fail the moment it hit the real-world variability of physician documentation. This is where Vibe Engineering—vibe coding for exploration + production-grade engineering for shipping—becomes a competitive advantage.

We designed a 3-step AI pipeline that adapts based on the capture mode. Whether it's voice capture via MobileEMNote or direct entry through EMClaimPacket, the system adjusts its logic. The pipeline first extracts data using gpt-4o-mini, then grades the Medical Decision Making (MDM) with gpt-4o, and finally generates a compliant attestation with gpt-4o-mini. This isn't just a prompt trick; it's a production-grade workflow backed by 203 test functions across 29 files.

The real story, however, is in the auditability. We implemented audit logging using SQLAlchemy event listeners to track every state change and adaptation. If a physician's intent captured via voice drifts from the final documentation, the system notices and triggers a status workflow for manual reconciliation. By building this level of observability into the core architecture, we ensure that our Continuous Exploration (CE) of new capture methods is always anchored to a reliable, auditable engineering foundation. We don't just ship AI; we ship workflows that survive the messy reality of clinical operations.

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/medicoda

## Screenshots

### Dashboard Time Savings Metrics
![Dashboard showing AI pipeline time savings metrics](assets/medicodax-dashboard-time-savings.png)
*Quantified impact of the 3-step AI pipeline on physician documentation time.*

### Mobile Queue Voice Submission Workflow
![Mobile Queue showing voice submission workflow for MobileEMNote path](assets/medicodax-mobile-queue-voice.png)
*Voice capture via MobileEMNote triggers the Extract → Grade → Attest pipeline with real-time adaptation.*

### E&M Record Wizard Direct Entry
![E&M Record wizard showing structured entry workflow for EMClaimPacket path](assets/medicodax-wizard-direct-entry.png)
*Direct entry through EMClaimPacket follows the same 3-step pipeline with different input handling.*

## Post asset ideas
- [ ] Diagram: The 3-step AI pipeline (Extract -> Grade -> Attest) with model assignments
- [ ] Workflow map: MobileEMNote (voice) vs. EMClaimPacket (direct) status transitions
- [ ] Code snippet: SQLAlchemy event listener implementation for audit logging
