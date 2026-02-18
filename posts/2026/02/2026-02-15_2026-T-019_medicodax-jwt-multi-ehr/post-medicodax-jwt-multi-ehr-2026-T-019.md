# Scaling Trust Across Epic and eClinicalWorks with JWT RS384

## Metadata
- **Post ID**: 2026-T-019
- **CTA**: book a working session at [lsadigital.com](https://lsadigital.com)

## Post

When we started building MEDICODAX, we knew that "just use an API key" was a non-starter for medical data. To handle 11 FHIR R4 resource types across multiple EHR vendors like Epic and eClinicalWorks, we had to build a robust identity layer from the ground up. This is Vibe Engineering—vibe coding for exploration + production-grade engineering for shipping—applied to the most sensitive data boundaries.

The story of our multi-EHR integration is one of moving from rapid prototyping to strict cryptographic enforcement. We implemented JWT RS384 authentication to ensure that every agentic tool call was signed and verifiable. But the real challenge was the drift in token lifecycles between vendors. Epic tokens have a 1-hour lifetime with a 60-second refresh buffer, while eClinicalWorks tokens expire in just 5 minutes (300 seconds). 

Managing these disparate constraints required a production-grade engineering mindset. We couldn't just "vibe" our way through token rotation in a regulated environment. We built a centralized auth manager that handles these specific vendor requirements while maintaining a unified interface for our AI pipeline. By drawing these hard JWT boundaries, we ensured that our Continuous Exploration (CE) of new medical workflows never compromised the security of the underlying patient data. We proved that you can move fast in healthcare, provided your engineering dial is set to 80/20 for the right parts of the system.

## Artifacts
- Remote:
  - https://www.lsadigital.com/products/medicoda

## Screenshots

### MEDICODAX Dashboard with EHR Integration
![MEDICODAX dashboard showing EHR integration and time savings metrics](assets/medicodax-dashboard-ehr-integration.png)
*Real-time integration with Epic and eClinicalWorks, tracking time savings across the medical coding pipeline.*

### Audit Logs with JWT Security Trail
![Audit logs showing JWT-secured operation trail](assets/medicodax-audit-logs-security.png)
*Every agentic tool call is signed and verifiable, with complete audit trails for compliance.*

### User Authentication Context
![User context showing authenticated identity and role information](assets/medicodax-user-auth-context.png)
*JWT RS384 authentication ensures every action is tied to a verified identity with scoped permissions.*

## Post asset ideas
- [ ] Diagram: JWT RS384 flow between MEDICODAX and Epic/eCW
- [ ] Table: Token lifecycle comparison (Epic vs. eCW) and refresh logic
- [ ] Code snippet: Scoped FHIR R4 resource access control in MEDICODAX
