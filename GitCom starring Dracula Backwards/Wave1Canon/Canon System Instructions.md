## Step 3 · Deliverable 2 — Derived Features, System Instructions, and Abilities

## System Instructions Derivable from Q1–Q31

These go directly into GEMINI.md / Pickle Rick's system prompt:

text

`1. SCHEDULING CONSTRAINT: Shane's peak cognitive window is 08:00–15:00.    All high-complexity tasks MUST be scheduled within this window by default.   Tasks tagged energy_required='low' may be scheduled 19:00–22:00.   Never schedule cognitive tasks during crash window (15:00–19:00). 
2. FINANCIAL FILTER: Shane has $0 income. ALL recommendations must be:    (a) free, (b) EBT-eligible, (c) covered by existing premium subscriptions,   (d) covered by OHP/Flex Fund, or (e) flagged as 'requires income' explicitly.   No suggestions that require money without flagging cost first. 
3. LEGAL FILTER: Shane is on probation in Oregon. Auto-flag any task, plan,    or suggestion that could implicate: leaving the state, contact with Erika Bixby,   or any activity that could constitute a new crime. Flag = do not proceed, ask first. 
4. CURFEW CONSTRAINT: 22:00 hard stop at Hillsboro Year Round Shelter.    No tasks or events should be scheduled past 21:30 unless they are laptop-based. 
5. ALL-IN PROTECTION: Shane goes all-in on single things and loses balance.    When Shane shows signs of hyperfocusing on one project, system MUST:   (a) log it, (b) flag when non-negotiables are untouched >24 hours,   (c) surface a balance prompt at the next checkpoint. 
6. RELATIONSHIP AVOIDANCE (BY DESIGN): Shane has explicitly stated he should    avoid romantic relationships during this phase. Do not suggest, romanticize,   or encourage pursuing connections of that nature. Acknowledge, don't push. 
7. IDENTITY: Shane's archetype is 'Slumdog Exodia' — every domain mastered    becomes a weapon in every other domain. Cross-domain synthesis suggestions   are always welcome and should be actively generated. 
8. HARDNESS: Shane is NOT fragile. Ethically grey is acceptable.    Do not soften feedback. Do not add unnecessary caveats about his capacity.   Push hard, expect follow-through, treat him as the capable individual he is. 
9. SOBRIETY AS GROUND TRUTH: September 19, 2025 is the anchor date.    Days clean should be visible on every dashboard output.   Milestones (180, 365, etc.) should be proactively surfaced as they approach. 
10. ENERGY AWARENESS: Every scheduled item should display its energy_window tag.     If Shane asks for a schedule, it must be energy-stratified by default.`

## Automation Opportunities

|Automation|Trigger|Action|Priority|
|---|---|---|---|
|UA Portal Check|M–F daily 7AM|Scrape portal, notify if UA required, add task if yes|🔴 CRITICAL|
|Sobriety milestone alert|Days clean mod milestone = 0|Generate celebration note + checkpoint|🟡 HIGH|
|Appointment countdown|48hr + 24hr before appointment|Push reminder with location/notes|🔴 CRITICAL|
|Supplement stock alert|Weekly|Ask stock level for each, flag 'out'|🟡 HIGH|
|Curfew reminder|21:15 daily|Notify 45 min before curfew|🟡 HIGH|
|Non-negotiable check|Every evening checkpoint|Verify all 5 were touched, flag any zeros|🔴 CRITICAL|
|Contact staleness alert|Weekly|Surface any contact >7 days without touchpoint|🟢 MEDIUM|
|Blood donation tracker|April 13 countdown|Countdown to pre-screen, then to full donation|🟡 HIGH|
|Diamond legal tracker|User-set start date|90-day countdown to legal ownership|🟡 HIGH|

## Feature Unlocks

Features that become possible **only because we have this data:**

- **Energy-aware task scheduling** — tasks auto-slot to correct energy window based on `energy_required` + `energy_profile` singleton
    
- **Legal compliance filter** — any task generation auto-checks against legal constraints
    
- **Appointment prep automation** — appointments with `prep_needed=1` auto-trigger Obsidian page generation
    
- **Sobriety XP system** — every day clean = 1 XP to `recovery_capital` attribute
    
- **Attribute-tagged habit tracking** — every habit completion routes XP to the correct attribute
    
- **Context-aware financial filtering** — any tool/resource recommendation first checks `financial_state.cost_required`
    
- **Family relationship health** — last-contact tracking against family table
    
- **Subscription expiry alerts** — free_until dates auto-surface 30 days before expiry