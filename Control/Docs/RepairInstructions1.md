# RepairInstructions1

Status: Active executable instruction file for Gemini CLI
Purpose: Perform a controlled repair/reset of the current system without losing the useful parts, then rebuild toward a shell-first, genuinely usable version.

---

## 0. Core judgment

Do **not** keep layering doctrine on top of a rocky implementation.
Do **not** blindly preserve the current DB state just because it exists.
Do **not** immediately expand graph/memory/orchestrator infrastructure.

The best move is a **controlled reset with backup**, followed by a **shell-first rebuild**.

This means:
1. pull latest repo
2. inventory current implementation
3. archive/backup the current DBs and generated artifacts
4. rebuild the live DB state from the corrected rules
5. make the shell/UX/commands feel real
6. only then repopulate the minimum viable operational slice

---

## 1. Pre-flight

### Working assumptions
- Budget is $0
- Prefer local-first, unlimited-free-tier tools
- Gemini CLI is the primary natural-language command center
- RVE is an invocable flow / tool / program / extension-like subsystem, not an always-on ambient god-process
- The goal is a sovereign shell that feels clean, fast, and useful

### Hard warnings
- Do not treat the current populated DBs as sacred
- Do not destroy them without first archiving them
- Do not keep every generated file if it is misleading, stale, or structurally wrong
- Do not let strategic/integration fantasies dominate daily execution rankings

---

## 2. Pull and branch

1. Pull latest from the configured remote.
2. Create a repair branch before destructive actions.
3. Confirm current repo status.

Run the equivalent of:
- `git remote -v`
- `git pull <correct-remote> main`
- `git checkout -b repair-shell-reset-01`

---

## 3. Mandatory source review before touching code

Read these in order:

1. `Control/Docs/RVE-FEATURE-DRIVEN-CANON-SPEC.md`
2. `Control/Docs/RVE-DIFF-ROLLOUT-VS-CANON.md`
3. `Control/Docs/RVE-COMMAND-BEHAVIOR-CONTRACT.md`
4. `Control/Docs/RVE-SCHEMA-MIGRATION-PLAN.md`
5. `Control/Docs/RVE-BOOTSTRAP-AND-POPULATION-PLAN.md`
6. `Control/Docs/MEMORY-LAYERS-FINAL-FORM.md`
7. `Control/Docs/MEMORY-INDEXING-AND-RETRIEVAL-CONTRACT.md`
8. `Control/ProposedDeltas/DELTAS_FINAL_POPULATION_SOURCE.md`
9. `GitCom starring Dracula Backwards/RVE Mycroft ReMatch Tool & Theory Pile/RVE Rollout.md`
10. `Control/Docs/RVE-MASTER-BRIEFING.md`

Also treat the following user requirements as authoritative for this repair pass:
- Static Objectives = recurring or specific time/place/event-bound commitments
- Daily Quests = recurring deterministic habit-builders
- Side Quests = optional AI-generated growth opportunities that require accept/deny
- Projects = decomposed, documented, checkable multi-step work
- Tasks = concrete executable items from the DB
- Calendar integration is imperative
- Free time between scheduled anchors should become calendar blocks containing that day’s chosen task pool
- Task reports should be structured and stored as `TaskReports/TaskReport.<datetime>.md`
- Natural-language daily journaling/check-in flow is required
- SQL alone is not the whole long-term memory story, but the shell/execution layer still comes first

---

## 4. Controlled reset instead of blind wipe

### Required method
Do **not** immediately delete the current DBs.
Do this instead:

1. locate all current live DB files
2. locate all current generated scripts touching RVE/shell/population
3. archive DBs and key generated artifacts into a dated backup folder
4. export schema snapshots if possible
5. only then clear or replace the live DBs

### Required outputs before wipe
- list of DB files found
- list of generated scripts/CLIs found
- list of files to keep / repair / delete
- backup location

### Delete/replace rule
You may delete or replace current live DBs **after** backup.
You may delete generated code/files that are clearly stale, misleading, or structurally wrong **if** they are archived first or reproducible from git history.

---

## 5. Repair objective: build the Sovereign Shell first

The current system should no longer be treated as “RVE only.”
The immediate product is a **Sovereign Shell** with RVE as one subsystem.

### The shell must provide
- a clean dashboard or entry screen
- current state summary
- today’s anchors
- top missions
- onboarding queue
- recommended next commands
- clean command/result formatting
- human-editable config
- fast invocable flows

### RVE inside the shell must provide
- capture
- onboarding
- today view
- checkpoint
- completion logging
- export-context
- projects view
- daily quest surfacing
- side quest accept/deny flow

Do not build the empire first.
Build the shell.

---

## 6. Core object model for this repair pass

Use these as the primary live object classes:

### 6.1 Static Objectives
Recurring or one-off time/place/event-bound commitments.
Examples:
- CODA appointments
- classes
- appointments
- blood donation
- polygraph
- breakfast / gym / CODA anchors

These must be schedule/calendar aware.

### 6.2 Daily Quests
Recurring habit/training objectives.
Examples:
- exercise routines
- study block
- report on a topic
- skill practice

These are deterministic and reviewed weekly.
When completed enough times, they should evolve or change.

### 6.3 Side Quests
AI-generated optional growth opportunities.
Examples:
- social expansion
- making money experiments
- skill drills
- research or fieldwork nudges

These require accept/deny.
Do not auto-force them into the schedule without acceptance.

### 6.4 Projects
Longer-running multi-step endeavors with decomposition and progress documentation.

### 6.5 Tasks
Concrete executable items.

### 6.6 Reports
Artifacts attached to task/project/quest execution.
At minimum support:
- human-authored notes
- AI-assisted summaries clearly labeled
- structured comparison between anticipated vs actual metrics where relevant

---

## 7. Category simplification rule

The system has been suffering from semantic sprawl.
For this repair pass, keep task navigation categories small.
Use only a few top-level categories if possible.

Recommended high-level grouping:
- obligations / scheduled
- build / projects
- growth / quests
- admin / life maintenance

Do not create 40 navigation categories just because the schema can support them.

---

## 8. Calendar behavior contract

Calendar integration is required.

### Required behavior
1. deterministic anchors go to calendar
2. appointments and recurring obligations go to calendar
3. the free time between anchors becomes a block event
4. each free block event contains the chosen task pool for that day/block

Example target:
- Breakfast / wake / journal block
- Gym block
- CODA block
- Boxing block
- Work block
- Sleep block
- Between-block event with the day’s selected pool

Do not overcomplicate this.
Make it work cleanly.

---

## 9. Journal and daily operating flow

A natural-language journal/check-in flow is required.
The daily journal should support:
- thoughts / previous night / intentions / issues
- mental health
- physical health
- current destructive habits
- current helpful habits
- trouble right now
- what is helping right now
- most important things today
- deadlines
- most compounding move today
- AM planning block
- skills focus today
- habits focus today
- minimum successful day
- sweeping victory definition
- failure definition
- post-event check-ins
- final log
- completed vs not completed
- anticipated vs actual metric comparison
- what each task unlocked
- why incomplete tasks were not finished
- tomorrow planning draft
- AI ingestion after completion

If this does not yet exist cleanly, implement the template/workflow.

---

## 10. Memory stance for this repair pass

Do not attempt to fully implement the complete final memory architecture in this pass.

### Do now
- keep structured truth in DBs
- keep canon docs invocable
- preserve context export
- keep room for layered memory later

### Do not do now
- full graph expansion
- full procedural self-evolving layer
- full long-term autonomous orchestration

The repair pass is about making the shell and execution spine real.

---

## 11. Decision rule: custom vs existing open-source task foundation

Before rebuilding too much UI/UX from scratch, audit whether the current custom task/shell layer is worth continuing.

### Required judgment
Answer:
- should the current custom SQLite/task foundation continue?
- should an existing open-source task system be adopted as the boring persistence/UI base?
- if adopted, what exact parts would still remain sovereign/custom?

### Constraint
Do not pivot unless there is a clear advantage.
Do not spend this run researching the entire internet.
Use current repo reality first.

---

## 12. Mandatory implementation sequence

### Phase A — Audit
- inspect current DBs
- inspect current command/CLI scripts
- inspect current dashboard/output state if any
- classify keep / repair / delete / archive

### Phase B — Backup and reset
- backup DBs and key generated files
- wipe or replace live DBs after backup
- remove or quarantine stale generated artifacts if needed

### Phase C — Rebuild schema and object behavior
- recreate clean DB state from corrected rules
- ensure support for static objectives, daily quests, side quests, projects, tasks, reports, anchors

### Phase D — Build shell UX
- dashboard
- config
- stable commands
- clean formatting
- current-state summary

### Phase E — Rebuild command loop
At minimum:
- `log`
- `onboard`
- `today`
- `checkpoint`
- `done`
- `export-context`
- project view
- side quest accept/deny

### Phase F — Controlled repopulation
Populate only the minimum viable operational slice:
- core profile truth
- core anchors/static objectives
- 3–5 active projects
- 10–20 real tasks
- daily quests seed set
- zero or very few side quests until the loop is proven

### Phase G — Acceptance test
Prove:
- capture is fast
- onboarding is real
- ranking is sane
- calendar blocks are generated sensibly
- checkpoint is useful
- completion logging works
- dashboard feels relieving, not annoying

---

## 13. Acceptance criteria

This repair is successful when:
- the shell feels like one clean thing
- commands do not feel sloppy
- the system no longer has to “figure out everything from scratch” every single time
- daily execution becomes easier, not heavier
- deterministic anchors populate the calendar properly
- free-time blocks can display the selected pool for that day/block
- side quests are optional and clean
- daily quests are coherent and reviewable
- project decomposition is visible
- reports are structured and retrievable

---

## 14. Output required from Gemini at the end

Report:
1. exact files changed
2. exact files deleted or archived
3. exact DBs backed up and wiped/rebuilt
4. exact schema changes now live
5. exact commands now working
6. example dashboard output
7. example day schedule/block output
8. example task report output path and template
9. whether the shell is actually usable tomorrow morning
10. what the next highest-leverage move is after this repair

---

## 15. Final rule

Treat this run as a **repair and convergence pass**.
Not a philosophy pass.
Not an empire pass.
Not a graph pass.
Not a random tool-install binge.

The question is simple:
Can the system become one clean, trustworthy shell that actually reduces stress and drives the day?

That is the standard.
