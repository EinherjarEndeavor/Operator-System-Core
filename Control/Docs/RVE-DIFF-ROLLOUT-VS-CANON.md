# RVE DIFF — ROLLOUT VS CURRENT CANON

Status: Active comparison and patch guidance
Purpose: Compare the original `RVE Rollout.md` concept stream and `RVE-MASTER-BRIEFING.md` build contract against the current hardened canon so critical design intent is not lost during implementation.

---

## 1. Source set used

### Historical concept / design intent
- `GitCom starring Dracula Backwards/RVE Mycroft ReMatch Tool & Theory Pile/RVE Rollout.md`
- `Control/Docs/RVE-MASTER-BRIEFING.md`

### Current active canon
- `Control/Docs/RVE-FEATURE-DRIVEN-CANON-SPEC.md`
- `Control/Docs/PROJECT-PORTFOLIO-CANON.md`
- `Control/ProposedDeltas/DELTAS_FINAL_POPULATION_SOURCE.md`

---

## 2. Executive judgment

The current canon is directionally correct, but the rollout thread and master briefing still contain important RVE mechanics that are either missing, under-specified, or not clearly routed.

The biggest risk is not that the current canon is wrong.
The biggest risk is that implementation will use the thinner current MVP contract and silently lose several high-value mechanics that were part of the real design.

The correct move is:
- keep the current MVP discipline
- pull forward the missing critical mechanics
- keep decorative or high-maintenance modules deferred

---

## 3. What the current canon gets right and should KEEP

### KEEP 1 — RVE as a local-first command center
This is fully consistent across the rollout, master briefing, and current canon.

### KEEP 2 — SQLite / structured truth as the operational core
The rollout matured toward structured storage, and the master briefing already positions `rve.db` and `lifestate.db` as the canonical machine layer.

### KEEP 3 — State machine with `captured -> onboarding_pending -> ready`
This is one of the strongest improvements in the current canon and should remain central.

### KEEP 4 — Weighted task assessment and context-aware scheduling
This is still the meat of the system.

### KEEP 5 — Checkpoint-based operation rather than one-shot planning
The rollout repeatedly converged on repeated check-ins and transition-aware replanning. This is correct.

### KEEP 6 — Manual truth + AI assistance
The rollout clearly wanted a living assistant. The current canon correctly keeps truth in the data layer and uses Gemini as the operator interface.

---

## 4. Critical additions that should be PULLED FORWARD into implementation

### ADD 1 — Two-database contract must remain explicit
The master briefing clearly states that `lifestate.db` is for WHO the user is and `rve.db` is for WHAT the user does.

This distinction is critical and should remain explicit in implementation.

**Implementation requirement:**
- `lifestate.db` holds profile truth, constraints, supports, affiliations, contacts, recovery/legal/health/school state
- `rve.db` holds tasks, projects, ideas, habits, completions, anchors, schedules, and execution state

### ADD 2 — Location and fixed/flexible status must be explicit first-class task fields
The rollout repeatedly emphasized that if a task has fixed time/location it belongs on the schedule; if not, it should be scheduled by weight and fit.

The current canon implies this, but the field contract is too thin.

**Implementation requirement:**
Every task object should explicitly support:
- `fixed`
- `location`
- `due_date` or equivalent timing field
- `duration_est_min`
- `energy_type`

### ADD 3 — Quick capture + estimated fields + later onboarding
The rollout strongly converged on a model where tasks can be captured instantly, auto-assessed provisionally, and then surfaced for onboarding later.

The current canon has `captured` and `onboarding_pending`, but not the richer enrichment logic.

**Implementation requirement:**
Add support for:
- `estimated_fields`
- `needs_review`
- `confidence_score` or equivalent review marker
- onboarding prompts at checkpoints

### ADD 4 — Transition mode / checkpoint planning should be richer than a generic command
The rollout specifically described using RVE at real transition points like breakfast, after group, after workout, and before the next anchor.

**Implementation requirement:**
`rve checkpoint` should support:
- what just finished
- current time
- next fixed anchor
- current energy
- available time block
- top options now

This is more valuable than a generic “show tasks” command.

### ADD 5 — Completion calibration fields are critical
The rollout strongly emphasized projected vs actual difficulty, projected vs actual time, notes, and ideas spawned from the work.

The current canon mentions completion logging but needs sharper implementation.

**Implementation requirement:**
On completion, support:
- `actual_duration_min`
- `actual_difficulty`
- `actual_energy_used`
- `completion_notes`
- `followup_spawned`
- `estimate_error` (derived or stored)

This is one of the main ways RVE becomes more accurate over time.

### ADD 6 — If-then plans should be included as a lightweight execution-support feature
The rollout included research-backed additions like implementation intentions.

**Implementation requirement:**
Allow optional `if_then_plan` on tasks, habits, or checkpoints.
This should not be required for everything, but should exist for repeated friction points.

### ADD 7 — Idea pipeline needs stronger state tracking
The rollout later introduced stages-of-change and stronger idea handling for back-burnered but valuable ideas.

**Implementation requirement:**
Ideas should not just be `raw`.
At minimum support a staged pipeline such as:
- captured
- contemplated
- prepared
- incubating
- activated
- paused
- archived

This preserves good ideas without polluting active execution.

### ADD 8 — Habits should remain modular but real
The master briefing includes habits and streaks. The later rollout clarifies that habit tracking should be optional and light, not the center of the system.

**Implementation requirement:**
Keep habit support, but treat it as a module.
Support:
- binary habits
- count habits
- abstinence/reduction habits
- trigger-linked microhabits

### ADD 9 — Context export is not optional if RVE is meant to support general AI use
The rollout explicitly wanted RVE to become a useful substrate for broader AI operation.
The master briefing includes a context export spec, but the current MVP canon does not emphasize it enough.

**Implementation requirement:**
Support an `rve export-context` function or equivalent artifact that summarizes:
- life state
- current projects
- current obligations
- current tasks
- active constraints
- current priorities

This is the bridge to general-purpose agent context later.

### ADD 10 — Weekly rolling schedule/archive behavior should exist
The rollout discussed weekly planning and archive rollover.

**Implementation requirement:**
Maintain a current-week schedule view and archive prior periods rather than flattening everything into one perpetual present.

---

## 5. Important things that should be DEMOTED or DEFERRED

### DEFER 1 — Full graph memory as an RVE dependency
Useful later, not needed to make RVE operational.

### DEFER 2 — Fully autonomous month-long scheduling
The rollout itself corrected away from this. Too brittle.

### DEFER 3 — Heavy RPG shell as a central dependency
XP, quests, levels, and streak mechanics can help some parts of engagement, but they must not outrank execution clarity.

### DEFER 4 — Always-on complexity for every entry
Rich schema is good. Mandatory heavy entry on every task is not.
Use staged capture.

### DEFER 5 — Overbuilt Morning Coffee automation as a gate for using RVE
Keep it as a module or later layer, not as a blocker for core usability.

---

## 6. Highest-priority implementation patches

### Patch 1 — Strengthen the task object
The task object should support at minimum:
- id
- title
- domain
- project_id
- state
- onboarded / onboarding_pending logic
- fixed
- location
- due_date
- duration_est_min
- energy_type
- urgency
- impact
- friction
- cascade
- compound
- immediate_benefit
- mandatory
- atomic
- action_plan
- contact
- website
- estimated_fields
- needs_review
- postpone_count
- if_then_plan
- notes

### Patch 2 — Strengthen completion logging
Add actual-vs-estimated fields.

### Patch 3 — Strengthen checkpoint flow
Make transition-mode planning explicit.

### Patch 4 — Strengthen idea/habit modules
Do not let them remain vague side notes.

### Patch 5 — Preserve two-database logic in implementation
Do not collapse everything into one generic database just because it is easier.

### Patch 6 — Add context export / current-state summary
This is required for broader AI usefulness.

---

## 7. Suggested implementation order

1. Preserve two-database design
2. Finalize strengthened task schema
3. Implement staged capture / onboarding_pending flow
4. Implement checkpoint command as transition planner
5. Implement completion calibration logging
6. Implement project + idea pipeline states
7. Implement habit module lightly
8. Implement weekly archive/current-week logic
9. Implement context export
10. Only then revisit gamification or graph expansion

---

## 8. Final judgment

### Missing critical things?
Yes.
The current canon still risks missing:
- stronger two-database separation
- richer staged intake metadata
- transition-mode checkpoint logic
- completion calibration fields
- idea pipeline maturity states
- context export as a first-class capability

### Is the current canon still usable?
Also yes.
It is not broken.
It is simply thinner than the real design trajectory.

### What should implementation do?
Implement the current canon, but patch it with the additions above before calling RVE finished.
