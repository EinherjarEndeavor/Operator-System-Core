# RVE FEATURE-DRIVEN CANON SPEC (v1.1)
## Authority: Sovereign Engineering | Status: ACTIVE | Last Hardened: 2026-04-09

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 1: PRODUCT DEFINITION & PROMISE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**RVE (Rolling Victory Engine):** A local-first, CLI-invoked personal command center designed to give a single human being — operating under real-world chaos, constraint, and ambition — a coherent, persistent, adaptive, AI-augmented operating system for their entire life.

**The Promise:** Convert chaos into structured execution through life-state capture, weighted task assessment, and context-aware scheduling.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 2: MVP GO-LIVE RULE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**RVE MVP is LIVE when Gemini can operate the task and obligation system from SQLite with consistency.**
- **Requires:** Stable task entry, ranking logic, and obligation retrieval.
- **Does NOT Require:** Graph memory, mobile UI, or perfect automated scripts.
- **Go-Live:** Once the 5 operational test cases (Section 10) work reliably in a real-world day.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 3: MINIMUM STATE MACHINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- `captured`: Quick entry; not yet scoreable.
- `onboarding_pending`: Needs metadata enrichment.
- `ready`: Validated for ranking and scheduling.
- `in_progress`: Active work phase.
- `blocked`: Delayed by external factors.
- `waiting`: Dependent on person/system/date.
- `completed`: Done and logged.
- `archived`: Operationally inactive.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 4: TASK ONBOARDING PROTOCOL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**MANDATORY FIELDS FOR `READY`:**
1.  **Title:** Atomic and actionable.
2.  **Domain/Project:** Correct classification.
3.  **Urgency & Impact (1-10):** Primary drivers.
4.  **Friction (1-10):** Activation cost.
5.  **Energy Type:** [high_cognitive, high_creative, high_physical, low_energy, zombie_capable, mandatory].
6.  **Duration Est (Min):** Estimated time to complete.

**SUB-TASK DECOMPOSITION:**
- **Tier 2 (Relational):** Tasks with `atomic=0` include a JSON array in the `action_plan` field for tracked steps.
- **Tier 4 (Synthesized):** Deep workflows live in `Vault/Workflows/[task_id].md`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 5: RANKING & SCHEDULING CONTRACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**COMPOSITE SCORE FORMULA (v1):**
`Score = (urgency x 0.25) + (impact x 0.20) + (cascade x 0.15) + (compound x 0.15) + (benefit x 0.10) + (mandatory_bonus x 0.10) + (low_friction_bonus x 0.05)`

**SCHEDULING PRIORITY:**
1.  Fixed Obligations / Schedule Anchors.
2.  Current Time Window vs. Duration.
3.  Current Energy State vs. Energy Type.
4.  Due Pressure.
5.  Rank Score.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 6: THE DAILY LOOP (MORNING COFFEE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**05:30 AUTO-RUN REQUIREMENTS:**
1.  **Newspaper Mode:** Aggregate News, Blogs, and Newsletters.
2.  **UA Portal Check:** Verify compliance credentials.
3.  **Quest Engine:** Surface 1 Daily Quest + 1 Side Quest.
4.  **Schedule Generation:** Propose day layout based on anchors and top `ready` tasks.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 7: OPERATIONAL COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Gemini must execute these via direct SQL/Terminal interaction:
- `rve log`: Quick capture.
- `rve onboard`: Enrich pending tasks.
- `rve today`: List rank-matched tasks for the current energy/window.
- `rve checkpoint`: Log completions and calibration data.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 8: RED-TEAM WARNINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- **FAIL:** Treating `captured` tasks as ranked truth.
- **FAIL:** Manual entry becoming too burdensome (Maintain "Surgical Capture").
- **SUCCESS:** Operating the day with less confusion than the previous cycle.
