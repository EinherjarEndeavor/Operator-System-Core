# SHELL UPGRADE ROSTER

Status: Active roster
Purpose: Enumerate the complete desired upgrade surface for the Sovereign Shell so implementation, repair, and future architecture work do not keep improvising the shell as a vague wrapper around RVE.

---

## 1. Product identity

The Shell is the sovereign natural-language command center for the entire system.
It is the thing the user opens, trusts, and operates from.
RVE lives inside the Shell as an invocable subsystem rather than being the whole product.

The Shell exists to:
- reduce stress
- reduce re-derivation
- present the right information at the right time
- invoke the right subsystem cleanly
- route commands to tools, memory layers, and workflows without making the user babysit the plumbing

---

## 2. Primary problems the Shell must solve

1. Repeated re-derivation of what the system is and how to use it.
2. Ugly/sloppy command experiences where the model “figures it out again” every time.
3. Fragmentation across tasks, calendar, notes, memory, tools, and research.
4. Too much cognitive overhead in deciding what to do next.
5. Weak continuity across sessions and contexts.
6. Lack of a single clean entry point for the whole environment.

---

## 3. Shell upgrade objectives

### Objective A — One coherent entry surface
The user should be able to open the shell and immediately see:
- current state
- today’s anchors
- top missions
- current growth pressure / quests
- pending onboarding items
- recommended next commands

### Objective B — Extension-like command experience
Invocations should feel like a real extension/MCP/tool:
- fast
- stable
- cleanly formatted
- predictable
- not verbose process dump chaos

### Objective C — Command routing
The shell should know whether a request should route to:
- RVE
- memory/retrieval
- graph
- research workflow
- tool/arsenal registry
- calendar/tasks integrations
- external actions/browser/tooling

### Objective D — Context conservation
The shell should preserve and surface the right context without stuffing the active context window with every document or fact.

### Objective E — Growth catalysis
The shell should not merely organize life.
It should support skill growth, optional challenge, reflection, and self-expansion.

---

## 4. Required shell capabilities

### 4.1 Dashboard / home surface
Must support:
- current-state summary
- top 3 missions
- today’s anchors/static objectives
- onboarding queue
- daily quests summary
- side quest queue
- recommended next commands
- active projects snapshot
- alerts/warnings

### 4.2 Command palette / invocation surface
Must support natural-language and explicit command-style use.
Known current command families include:
- shell home
- shell status
- rve log
- rve onboard
- rve today
- rve checkpoint
- rve done
- rve export-context
- rve projects
- rve quests
- rve journal
- rve reports

### 4.3 Config surface
Must support human-editable config for:
- preferred shell style / formatting
- dashboard sections
- calendar integration settings
- quest intensity
- memory layer toggles/visibility
- notification preferences
- routing preferences if needed

### 4.4 Current-state compression
Must generate small useful summaries for:
- current day
- current mission state
- current constraints
- current active projects
- current top opportunities / burdens

### 4.5 Tool/capability invocation
Must be able to call:
- repo workflows
- scripts
- DB queries
- calendar/task integrations
- research tools
- approved MCP/extensions/tools

### 4.6 Recovery from ambiguity
If the user asks something vague, the shell should:
- route intelligently
- expose assumptions
- ask narrowly when required
- not reinvent the entire architecture every time

---

## 5. Shell subsystems it must coordinate

1. Execution Spine (RVE)
2. Memory Fabric
3. Capability Fabric / Arsenal Registry
4. Growth/Quest Engine
5. Calendar/Task Ecosystem Integration
6. Research / Canonization / Report workflows
7. Profile / Persona / Instruction layer

---

## 6. Memory-aware shell features

The shell must be aware that multiple memory layers exist concurrently.
It should be able to:
- read structured truth
- pull episodic history when useful
- surface canon docs
- invoke retrieval/index search
- query graph/relationship data
- use procedural memory for successful workflows
- respect the derived operator profile

It must not treat all memory forms as identical.

---

## 7. Required shell workflows

### Workflow 1 — Morning startup
- open shell
- display dashboard
- show anchors
- show top missions
- show daily quests
- propose best next command

### Workflow 2 — Midday transition
- checkpoint after event or task
- show available block
- show next anchor
- suggest best move + fallback

### Workflow 3 — Capture flow
- accept raw task/idea/obligation input quickly
- store it without demanding excessive metadata
- preserve raw phrasing

### Workflow 4 — Onboarding flow
- enrich pending items into clean operational state
- reveal only the missing fields needed

### Workflow 5 — End-of-day / export flow
- summarize what happened
- log completions/lessons
- export current context

### Workflow 6 — Research / retrieval flow
- find relevant canon/docs/backlog material quickly
- surface sources with provenance

### Workflow 7 — Growth flow
- surface quests and skill opportunities
- track reports/reviews
- keep growth pressure visible without being corny or overbearing

---

## 8. UI / experience upgrades the shell should eventually support

### Immediate desired upgrades
- cleaner output formatting
- stable result templates
- dashboard summary
- recommendation panel
- less process-noise in outputs

### Near-term upgrades
- polished theme/styling
- more deliberate shell persona/voice
- better project summaries
- better calendar/task block inspection
- cleaner configuration editing

### Later upgrades
- richer visual dashboard
- app/windowed shell or TUI
- phone-friendly shell views
- eventual standalone program if justified

---

## 9. Non-goals

The shell is not:
- just a prettier terminal prompt
- just a task list viewer
- just a memory database UI
- just a wrapper around one script
- just a philosophy engine

---

## 10. Red-team warnings

The shell fails when:
- it feels like a bundle of unrelated commands
- it makes the user think harder instead of less
- it forces re-explanation every session
- it surfaces too much noise
- it emits process dumps instead of decisions/results
- it behaves like unfinished scaffolding forever

The shell succeeds when:
- it feels like one coherent thing
- it reduces friction and stress
- it makes the next useful move obvious
- it provides a stable entry point for every major subsystem
