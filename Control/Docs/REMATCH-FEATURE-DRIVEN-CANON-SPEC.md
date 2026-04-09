# REMATCH FEATURE-DRIVEN CANON SPEC (v1.1)
## Authority: Sovereign Engineering | Status: ACTIVE | Last Hardened: 2026-04-09

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 1: PRODUCT DEFINITION & PROMISE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Re.Match:** A constraint-based resource and opportunity matching engine.
**The Promise:** Utilizing the client's specific "Constellation of Circumstance" (including barriers like justice-system history) to unlock high-tier scholarships, specialized grants, and career "jackpots" that others cannot access.

**Unique Value Proposition:** Turning weaknesses (barriers) into strengths (eligibility multipliers) through profile-aware matching.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 2: CORE PRODUCT LOOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1.  **Intake:** High-fidelity profile creation (80+ fields).
2.  **Normalization:** Converting raw text/voice into structured Tier 2 data.
3.  **Matching:** eligibility-aware search across 23 categories.
4.  **Deduplication:** Filtering out known/stale resources.
5.  **Synthesis:** Generation of a prioritized, prioritized dossier.
6.  **Action Plan:** Packaging recommendations into immediate next steps.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 3: INTAKE DOMAINS (THE 23 CATEGORIES)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A usable intake must cover these canonical categories:
1. Legal & Supervision | 2. ID & Documentation | 3. Housing | 4. Financial | 5. Employment | 6. Education | 7. Health | 8. Recovery | 9. Family | 10. Social Supports | 11. Transportation | 12. Benefits | 13. Digital Access | 14. Skills | 15. Goals | 16. Deadlines | 17. Barriers | 18. Eligibility Multipliers | 19. Faith/Spiritual | 20. Identity | 21. Contacts | 22. Medical Records | 23. Narrative Context.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 4: MATCHING LOGIC ORDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Match recommendations in this strict hierarchy:
1.  **Hard Eligibility:** Does the client meet the age/location/history requirements?
2.  **Hard Disqualifiers:** Is there a "Kill Switch" (e.g., specific crime types)?
3.  **Barrier Compatibility:** Does the resource specifically accept JII/Recovery clients?
4.  **Life Impact Potential:** Does this match the top 3 priorities in `trajectory`?
5.  **Redundancy Check:** Has the user already exhausted this lead?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 5: THE DOSSIER CONTRACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Every Re.Match Dossier must contain these four sections:
- **SECTION 1: SUMMARY:** Client snapshot + top 3 high-leverage opportunities.
- **SECTION 2: CATEGORY MATCHES:** Detailed recommendations per category (Title, Eligibility Basis, Why it Fits, Action Steps).
- **SECTION 3: IMMEDIATE ACTION QUEUE:** 3-7 prioritized tasks ready for RVE ingestion.
- **SECTION 4: MONITOR LIST:** Long-horizon opportunities for future eligibility.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 6: RED-TEAM WARNINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- **FAIL:** Collapsing into generic Google search results.
- **FAIL:** Recommending stale or "broken link" resources.
- **SUCCESS:** The recipient receives a materially better action package than they could have assembled alone.
