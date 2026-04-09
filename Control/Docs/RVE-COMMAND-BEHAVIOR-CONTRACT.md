# RVE COMMAND BEHAVIOR CONTRACT

Status: Active command contract
Purpose: Define the minimum usable behavior for the core RVE commands so Gemini does not patch only the schema while leaving command behavior vague.

---

## 1. Executive judgment

The current highest-leverage implementation move is not adding more theory.
It is making the core RVE commands behave predictably against the strengthened schema.

If the schema is patched but the commands are still vague, RVE will remain half-real.
If the commands are sharp, Gemini can operate the system even before every optional module exists.

---

## 2. Command priority order

Implement these in this order:
1. `rve log`
2. `rve onboard`
3. `rve today`
4. `rve checkpoint`
5. `rve done`
6. `rve export-context`
7. `rve projects`
8. `rve ideas`
9. `rve habits`

This order matches the actual operating loop:
- capture
- enrich
- choose
- transition
- learn
- export

---

## 3. Shared command rules

### Rule A — Never overclaim certainty
If fields were estimated, mark them as provisional.

### Rule B — Distinguish `captured`, `onboarding_pending`, and `ready`
Do not rank low-metadata tasks as if they are fully validated.

### Rule C — Favor small usable output over giant dumps
Every command should return the minimum set needed to drive action.

### Rule D — Query truth from the DB, not memory
Do not invent task/project state if the DB can answer it.

### Rule E — Commands should be transition-aware
RVE exists to help at moments of uncertainty, not just to display data.

---

## 4. Command contracts

### `rve log`

#### Purpose
Fast capture of a task, idea, obligation, or anchor candidate.

#### Input modes
- single-line capture
- short conversational capture
- structured prompt if needed

#### Minimum behavior
- create a new row with:
  - title
  - domain if inferable
  - state = `captured` or `onboarding_pending`
  - estimated_fields flag if Gemini guessed values
  - notes preserving raw user phrasing
- do not require full metadata up front

#### Return format
- item created
- current state
- which fields still need onboarding
- whether Gemini estimated anything

#### Failure condition
- command asks for 15 fields before allowing capture

---

### `rve onboard`

#### Purpose
Convert `captured` or `onboarding_pending` items into genuinely usable `ready` tasks.

#### Required onboarding fields for `ready`
- title
- domain/project
- urgency
- impact
- friction
- duration_est_min
- energy_type
- fixed or flexible status
- due_date or explicit no-deadline note when relevant

#### Minimum behavior
- show missing fields
- ask only for what is missing or uncertain
- preserve estimated/provisional markers until user confirmation or sufficient grounding exists
- promote to `ready` only when the minimum viable scheduling metadata is present

#### Return format
- onboarding result
- new state
- missing fields if still incomplete
- scoreability status

#### Failure condition
- promotes tasks to `ready` without enough metadata to schedule intelligently

---

### `rve today`

#### Purpose
Show the best currently actionable work for the current day or current block.

#### Required considerations
- fixed anchors first
- due pressure
- available time window
- current energy state
- task state
- score/rank

#### Minimum behavior
- separate fixed anchors from flexible tasks
- show only a small set of highest-fit tasks
- explain briefly why each was selected
- exclude blocked/waiting items unless explicitly requested

#### Return format
- anchors first
- top fit-ready tasks next
- any urgent onboarding-pending items that need enrichment

#### Failure condition
- dumps all tasks without fit logic

---

### `rve checkpoint`

#### Purpose
Serve as the transition-mode planner.

#### Trigger examples
- after treatment/group
- after workout
- after class
- after finishing a task
- before the next anchor

#### Required inputs
- what just finished
- current time
- current energy
- next fixed anchor
- available time block

#### Minimum behavior
- log what just ended if relevant
- calculate time until next fixed anchor
- surface best-fit next actions
- identify whether any pending tasks need onboarding
- suggest one main move and one fallback move

#### Return format
- transition summary
- available window
- next anchor
- best move now
- fallback move
- onboarding reminders if any

#### Failure condition
- behaves like a generic status screen with no transition intelligence

---

### `rve done`

#### Purpose
Mark a task complete and learn from the execution.

#### Required completion fields
- actual_duration_min
- actual_difficulty
- actual_energy_used
- completion_notes
- followup_spawned
- estimate_error

#### Minimum behavior
- mark task complete
- collect actual-vs-estimated info
- optionally spawn follow-up tasks or ideas
- preserve learning data in completion storage

#### Return format
- completion recorded
- estimate comparison
- spawned follow-ups if any

#### Failure condition
- only flips a status bit and learns nothing

---

### `rve export-context`

#### Purpose
Generate a compact current-state package for future sessions or external agents.

#### Must include
- active projects
- active obligations
- top tasks
- current anchors
- high-value constraints from lifestate
- current priorities

#### Minimum behavior
- compress to the smallest useful block
- prefer signal over exhaustiveness
- stay grounded in DB state

#### Failure condition
- giant unfiltered dump or vague summary with no operational value

---

### `rve projects`

#### Purpose
Show project state, next actions, and blockages.

#### Minimum behavior
- list active projects
- show status
- show next_action
- show blockers if any
- show linked open task count if feasible

#### Failure condition
- project records exist but still have no visible next action

---

### `rve ideas`

#### Purpose
Keep ideas alive without polluting active tasks.

#### Minimum behavior
- support staged pipeline
- allow promote-to-project or promote-to-task action
- allow pause/archive without deletion

#### Failure condition
- idea bucket becomes a graveyard

---

### `rve habits`

#### Purpose
Track lightweight recurring behavior without dominating the system.

#### Minimum behavior
- support binary and count habits
- support abstinence/reduction patterns
- show only a small actionable view

#### Failure condition
- habits become the center of the system instead of execution support

---

## 5. Minimum command acceptance tests

### Test 1
`rve log` can capture a raw task in under 20 seconds.

### Test 2
`rve onboard` can take a weak capture and make it genuinely ready.

### Test 3
`rve today` can show fit-matched work for the current day/window.

### Test 4
`rve checkpoint` can help at a real transition moment.

### Test 5
`rve done` records actual-vs-estimated learning data.

### Test 6
`rve export-context` creates a useful compact handoff block.

### Test 7
`rve projects` shows active projects with next actions.

---

## 6. Final rule

RVE is not operational because the DB exists.
RVE is operational when the command layer turns that DB into useful action under real-world conditions.
