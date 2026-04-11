# RepairInstructions2

Status: Active executable instruction file for Gemini CLI
Purpose: Run a full, coherent, shell-first repair and V2 parallel rebuild that preserves the complete intended system shape from the beginning, including concurrent memory layers and RVE as an invocable extension/MCP-style subsystem.

---

## 0. Read this first

This is **not** a narrow RVE patch.
This is **not** a blind DB wipe.
This is **not** a graph-free simplification.
This is **not** a philosophy-only pass.

This is a **full repair architecture + V2 parallel rebuild plan**.

The system being repaired is a sovereign shell with these major components:
- shell / command center
- RVE as an invocable extension / MCP / program-like subsystem
- concurrent multi-layer memory fabric
- capability/tool/arsenal fabric
- growth / quest / reporting engine
- normie ecosystem integration

The goal is to stop improvising architecture while coding.

---

## 1. Core understanding to preserve

### 1.1 The system is bigger than RVE
RVE is a subsystem.
The larger product is a sovereign natural-language shell.

### 1.2 RVE should behave like an invocable extension or MCP
Do not treat RVE as an always-on ambient daemon.
Treat it as a cleanly invocable subsystem that can be called from the shell when needed.

### 1.3 Multiple memory forms must be active from the start
Do **not** reduce the plan to SQL-only now and “maybe graph later.”
The intended system requires concurrent memory modes from the beginning.

### 1.4 All active memory layers do not have equal authority
Concurrent is correct.
Equal authority is not.
The repair must define explicit authority roles.

### 1.5 The shell must feel clean and extension-like
The current failure mode is ugliness, sloppiness, and repeated on-the-fly process sprawl.
The repaired system must return stable, fast, clean outputs.

---

## 2. Hard constraints

- Budget = $0
- Prefer local-first, unlimited-free-tier tools
- Gemini CLI is the primary command center
- Do not destroy the current system before archive/backup
- Do not keep the current live DB state just because it exists
- Do not freestyle missing behavior when canon/requirements already exist
- Do not build only a shell with no memory fabric
- Do not build only a memory cathedral with no usable shell
- Do not collapse all memory modes into one incoherent blob

---

## 3. Authoritative requirement summary

These are active build laws for this run.

### RVE / execution requirements
- Static Objectives: recurring or specific time/place/event-bound commitments
- Daily Quests: recurring deterministic growth objectives reviewed weekly and capable of evolving
- Side Quests: optional AI-generated growth opportunities requiring accept/deny
- Projects: decomposed, documented, progress-visible multi-step work
- Tasks: concrete executable items
- Calendar integration is imperative
- Free time between scheduled items should become event blocks containing the selected task pool for that day/block
- Task reports should be structured in `TaskReports/TaskReport.<datetime>.md`
- A natural-language daily journal/check-in/final-log flow is required

### Higher-order memory requirements
- facts alone are insufficient
- derived profile / psyche / philosophical approaches / ethical boundaries / over-arching goals must be represented somewhere
- SQL alone is not enough for the final system
- the system must support discovering high-impact opportunities based on circumstance and network, not just explicit user requests

---

## 4. Repair method: V2 parallel rebuild, not blind wipe

### Why
Blindly wiping the current system risks losing useful structure and making progress feel fake.
A V2 parallel rebuild allows clean comparison and lower-risk convergence.

### Method
1. archive and inventory current state
2. design the complete V2 architecture inside the repo
3. build the V2 shell + V2 memory fabric in parallel
4. test with a minimal operational slice
5. only then promote or merge into the live path

If some live DBs must be wiped later, do that **after** backup and after V2 shape is locked.

---

## 5. Phase A — Inventory and freeze

### Required actions
- pull latest repo
- create a dedicated repair branch
- inspect current DB files
- inspect current generated scripts and CLIs
- inspect current command entry points
- inspect current dashboard/output surfaces if any
- classify files into: keep / repair / archive / delete
- archive DBs and generated artifacts into a dated backup folder
- export schema snapshots if possible

### Required output
Produce a report with:
- DB files found
- command/shell files found
- generated scripts found
- likely stale or misleading artifacts
- backup location

Do not code the rebuild before this is done.

---

## 6. Phase B — Lock the V2 architecture before coding

Before changing implementation, define and confirm the V2 architecture **inside the repo**.
This must be explicit enough that subsequent coding does not improvise missing structure.

### V2 major layers

#### Layer 1 — Sovereign Shell
The direct user-facing command center.
Must provide:
- dashboard/home
- current-state summary
- current active missions
- today’s anchors
- onboarding queue
- recommended next commands
- clean result formatting
- config
- invocable subsystem entry points

#### Layer 2 — Execution Spine (RVE)
RVE as an invocable extension/MCP/program-like subsystem.
Must provide:
- Static Objectives
- Daily Quests
- Side Quests
- Projects
- Tasks
- checkpoints
- scheduling
- completion logging
- reports
- journal/check-ins
- context export

#### Layer 3 — Memory Fabric
All active from the beginning:
- structured truth memory
- episodic/session/log memory
- canon/doc memory
- retrieval/index memory
- graph/relationship memory
- procedural memory
- derived operator-profile memory

#### Layer 4 — Capability Fabric
- tool registry
- extension registry
- MCP registry
- browser and external actions
- policies / allowlists
- capability discovery
- install/use tracking

#### Layer 5 — Growth Engine
- daily quests
- side quests
- skill development
- optional nudges
- report/review mandates
- growth pressure
- exploration prompts

---

## 7. Phase C — Memory authority rules

All memory modes may be active from the start, but their roles must be explicit.

### 7.1 Structured truth memory
Authority for:
- operational facts
- active tasks/projects
- anchors/obligations
- schedule state
- core user state

### 7.2 Episodic memory
Authority for:
- what happened
- session logs
- completions
- reviews
- journal history

### 7.3 Canon/doc memory
Authority for:
- contracts
- doctrine
- workflows
- instructions
- stable source-of-truth design docs

### 7.4 Retrieval/index memory
Authority for:
- surfacing relevant sources/chunks
- source discovery
- backlog exploitation

### 7.5 Graph/relationship memory
Authority for:
- relationship discovery
- multi-hop linkage
- leverage discovery
- pattern surfacing

### 7.6 Procedural memory
Authority for:
- learned workflows
- successful command sequences
- repeated repair patterns
- shell behavior recipes

### 7.7 Derived operator-profile memory
Authority for:
- inferred psyche model
- motivation patterns
- ethical boundaries
- growth pressure logic
- mission orientation

### Critical rule
Graph/retrieval/profile layers must not silently override direct structured truth.
They must enrich or propose, not silently rewrite.

---

## 8. Phase D — Object model lock

The V2 object model must be explicit before schema rebuild.

### Required first-class objects
- StaticObjective
- DailyQuest
- SideQuest
- Project
- Task
- Anchor
- Obligation
- Report
- JournalEntry
- CheckIn
- ContactNode
- Skill
- Tool
- MemoryArtifact
- Capability

### Required behavioral distinctions

#### StaticObjective
Deterministic time/place/event-bound commitment.
Schedule/calendar native.

#### DailyQuest
Recurring deterministic growth objective.
Defined jointly by user + AI.
Reviewed weekly.
Must evolve after repeated completion.

#### SideQuest
AI-generated optional growth or leverage opportunity.
Requires accept/deny.
Must not silently occupy the schedule without acceptance.

#### Project
Multi-step, documented, decomposable work.
Must expose progress and next action.

#### Task
Concrete executable item.
Must support metrics and scheduling.

#### Report
Artifact generated from work.
Stored in `TaskReports/TaskReport.<datetime>.md`.
Must support human-authored content and AI-assisted structure.

#### JournalEntry / CheckIn
Natural-language operating log.
Must support AM planning, post-event reflections, and final-day review.

---

## 9. Phase E — Calendar and schedule contract

This is a core reality test.

### Required behavior
1. deterministic anchors go to calendar
2. appointments and recurring obligations go to calendar
3. free time between anchors becomes a block event
4. each free block event contains the selected task pool for that day/block
5. the user should be able to inspect a block and see what is intended there

### Example intent
- breakfast / wake / journal block
- gym block
- CODA block
- boxing block
- study/work block
- sleep block
- between-block task pool event

If this does not work, the system will still feel fake.

---

## 10. Phase F — Journal and reporting flow

The system must support the plain-language daily flow.

### Required journal/check-in structure
- thoughts / previous night / intentions / issues
- mental health
- physical health
- destructive habits active right now
- helpful habits active right now
- what is giving trouble right now
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
- post-event check-in fields
- final log
- finished vs unfinished
- why unfinished
- compare anticipated vs actual metrics
- identify what each task unlocked
- tomorrow plan draft
- AI ingestion of completed journal

If missing, create or repair the workflow/template.

---

## 11. Phase G — Shell UX contract

The shell must feel like a clean extension-like surface, not like an AI vomiting process steps.

### Required shell surfaces
- dashboard/home
- current-state summary
- top missions
- anchors today
- onboarding queue
- daily quests summary
- side quest queue
- recommended next commands
- config

### Required properties
- clean formatting
- stable outputs
- fast invocable flows
- not requiring the model to re-derive the whole system every time

### Required command surface
At minimum support:
- `shell home` or equivalent dashboard entry
- `rve log`
- `rve onboard`
- `rve today`
- `rve checkpoint`
- `rve done`
- `rve export-context`
- `rve projects`
- `rve quests`
- `rve journal`
- `rve reports`

If command names differ, keep behavior equivalent and document it clearly.

---

## 12. Phase H — Capability fabric

The system must know what tools and integrations it has, and use them intentionally.

### Required capability records
- tool/extension name
- install state
- capability tags
- trust/permission level
- preferred use cases
- known workflows
- successful use examples if available

### Required behavior
- Gemini remains the primary command center
- tool invocation should feel intentional and routed
- the shell should know when to use a tool vs when not to

Do not spend this pass installing every possible tool.
Build the registry/structure that will support it.

---

## 13. Phase I — Minimal live V2 implementation

After architecture is locked, build the minimum live V2 slice.

### Populate only the minimum viable slice
- core profile truth
- core anchors/static objectives
- 3–5 active projects
- 10–20 real tasks
- seed daily quests
- minimal side quests
- minimal graph entities for active system objects
- canon docs indexed
- minimal procedural memory seeded from accepted command flows

Do not saturate everything yet.

---

## 14. Phase J — Acceptance tests

The rebuild is acceptable when:
- shell feels like one clean thing
- dashboard is useful
- capture is fast
- onboarding is real
- ranking is sane
- deterministic anchors populate calendar correctly
- free-time blocks contain useful task pools
- daily quests work
- side quests require clean accept/deny
- journaling/check-ins work
- reports are structured and retrievable
- context export works
- multiple memory layers are all live in minimal meaningful form
- graph is active and queryable without corrupting truth
- retrieval works without replacing canon
- system reduces stress instead of adding it

---

## 15. Open-source foundation audit (required)

The user raised a serious alternative: adopt or wrap an existing open-source task/planner base rather than rebuilding every boring layer from scratch.

### Required judgment
Audit whether the current custom task/shell base should continue, or whether a boring existing foundation should be wrapped.

### Important rule
Do not pivot casually.
Do not spend this pass doing giant internet research.
Use repo reality and system needs first.

Report:
- continue current base / wrap existing foundation / undecided
- why
- which boring problems would be stolen instead of reinvented
- which sovereign layers must remain custom regardless

---

## 16. Required output from Gemini

At the end of this run, report:
1. exact files changed
2. exact files archived/deleted
3. exact DBs backed up / replaced / rebuilt
4. exact V2 architecture files created or reinforced
5. exact memory layers made live in minimal form
6. exact commands now working
7. example dashboard output
8. example calendar block output
9. example task report output path and template
10. whether the shell is usable tomorrow morning
11. whether the memory fabric is live in a meaningful way
12. what the next highest-leverage move is after this pass

---

## 17. Final rule

Do not solve this as “RVE only.”
Do not solve this as “memory only.”
Do not solve this as “graph only.”
Do not solve this as “docs only.”

Solve it as a **coherent sovereign shell** with:
- execution
- memory
- capability routing
- growth
- calendar reality

all designed together from the start, then implemented in a minimal but real V2 slice.
