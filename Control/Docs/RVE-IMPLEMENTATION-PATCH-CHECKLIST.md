# RVE IMPLEMENTATION PATCH CHECKLIST

Status: Active implementation checklist
Purpose: Convert the RVE diff and reference-map guidance into a practical build sequence so implementation does not drift, stall, or skip critical mechanics.

---

## 1. Mission

Implement RVE as a usable local-first Gemini-operated command center without losing critical design intent from the rollout and master briefing.

This checklist is deliberately practical.
It is not another theory document.

---

## 2. First rule

Do not attempt to make RVE perfect before it is usable.

Apply patches in this order:
1. schema correctness
2. staged intake
3. checkpoint utility
4. completion learning
5. project / idea / habit support
6. context export
7. weekly rolling logic
8. only then decorative or optional modules

---

## 3. Required source order before changing anything

Read in this order:
1. `Control/Docs/RVE-FEATURE-DRIVEN-CANON-SPEC.md`
2. `Control/Docs/RVE-DIFF-ROLLOUT-VS-CANON.md`
3. `Control/Docs/RVE-CANON-REFERENCE-MAP.md`
4. `Control/ProposedDeltas/DELTAS_FINAL_POPULATION_SOURCE.md`
5. `GitCom starring Dracula Backwards/RVE Mycroft ReMatch Tool & Theory Pile/RVE Rollout.md`
6. `Control/Docs/RVE-MASTER-BRIEFING.md`

Do not start patching from memory.

---

## 4. Patch sequence

### PATCH A — Preserve the two-database model

#### Goal
Keep `lifestate.db` and `rve.db` distinct in role.

#### Must be true
- `lifestate.db` stores profile truth, constraints, affiliations, supports, legal/health/school/recovery state.
- `rve.db` stores tasks, projects, ideas, habits, completions, anchors, schedules, and execution logic.

#### Check
- No blind collapse into a single generic DB.
- Routing rules stay explicit.

---

### PATCH B — Strengthen the task schema

#### Goal
Make the task object match the real RVE design, not just the thin MVP shell.

#### Required fields
- id
- title
- domain
- project_id
- state
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

#### Must be true
- quick capture is possible without filling everything
- `ready` still requires enough metadata to rank and schedule meaningfully

---

### PATCH C — Implement staged capture and onboarding

#### Goal
Support fast intake without losing data quality.

#### Required behavior
- new task can be captured quickly
- AI can provisionally estimate some fields
- task is marked `captured` or `onboarding_pending`
- onboarding later enriches the missing fields
- only sufficiently clarified tasks should be treated as high-confidence scheduling candidates

#### Must be true
- low-friction capture exists
- richer later onboarding exists
- no false certainty from guessed fields

---

### PATCH D — Implement transition-mode checkpoint behavior

#### Goal
Make `rve checkpoint` useful at real life transitions.

#### Required inputs / outputs
At checkpoint, support:
- what just finished
- current time
- current energy
- next fixed anchor
- available time block
- best options now
- whether any pending tasks need onboarding

#### Must be true
- checkpoint is a real transition planner
- not just a passive dashboard

---

### PATCH E — Completion calibration logging

#### Goal
Let RVE learn from projected vs actual execution.

#### Required completion fields
- actual_duration_min
- actual_difficulty
- actual_energy_used
- completion_notes
- followup_spawned
- estimate_error (stored or derived)

#### Must be true
- completions are not just “done” stamps
- the system can improve its future estimates

---

### PATCH F — Project / idea / habit state support

#### Goal
Prevent projects, ideas, and habits from remaining vague blobs.

#### Project requirements
- explicit project records
- current status
- next-action visibility
- linkage to tasks

#### Idea requirements
Support a real idea pipeline, such as:
- captured
- contemplated
- prepared
- incubating
- activated
- paused
- archived

#### Habit requirements
Keep habits modular but real:
- binary habits
- count habits
- abstinence/reduction habits
- trigger-linked microhabits

---

### PATCH G — Context export

#### Goal
Make RVE useful as a substrate for broader AI usage.

#### Required output
A compact export that can summarize:
- life state
- active projects
- active obligations
- active tasks
- current constraints
- current priorities

#### Must be true
- RVE can feed other agents and sessions
- broader AI context does not depend on random memory

---

### PATCH H — Weekly rolling schedule/archive logic

#### Goal
Keep planning bounded in time and reviewable.

#### Required behavior
- current-week schedule view exists
- prior periods can be archived
- week rollover does not flatten everything into one eternal now

---

## 5. Acceptance tests

RVE patching is good enough when the following work:

### Test 1 — Quick capture
A vague task can be added in seconds and safely marked for later onboarding.

### Test 2 — Full onboarding
A pending task can be enriched until it is genuinely ready.

### Test 3 — Transition planning
At a real checkpoint, RVE can recommend what to do next based on time, energy, and the next anchor.

### Test 4 — Completion learning
A finished task can log actual duration, actual difficulty, and notes, and that information is preserved.

### Test 5 — Project visibility
RVE can show active projects and the next meaningful actions attached to them.

### Test 6 — Context export
RVE can produce a compact current-state package for a future session or external agent.

### Test 7 — Weekly continuity
The current week can be reviewed and prior periods preserved without confusion.

---

## 6. What to leave out for now

Do not let these delay core functionality:
- graph memory
- full autonomous month scheduling
- heavy gamification as a gate
- overbuilt Morning Coffee automation
- maximum-detail onboarding for every single field immediately

---

## 7. Final rule

If there is a tradeoff between:
- making RVE prettier
- making RVE more mythic
- making RVE more feature-complete
- making RVE more immediately usable

choose usability.

That is the only route by which the bigger design ever becomes real.
