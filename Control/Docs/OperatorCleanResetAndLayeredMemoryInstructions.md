# Operator Clean Reset and Layered Memory Instructions

Status: Active executable instruction file for Gemini CLI
Purpose: Reset `\Operator\` into a clean daily-driver Gemini CLI workspace while preserving the current experimental system in `\Operator\SIP`, then prepare a layered but gated memory/capability/task environment that compounds power without becoming obnoxious.

---

## 0. Core mission

You are not continuing the current mutant workspace at the root.
You are preserving it under `SIP` and rebuilding the root `Operator` directory as a clean daily driver.

The clean daily driver must:
- feel close to vanilla Gemini CLI
- avoid broad memory fan-out on normal turns
- avoid implicit writes and auto-taskification
- keep RVE invocable rather than ambient
- support manual task/state use immediately
- support layered memory in a gated, non-competing way
- create an Obsidian Vault inside `\Operator\` for the human-facing side of the system
- prepare the machine-facing side for procedures, tool logs, audit trails, and future capability growth

---

## 1. Hard rules

1. Do **not** modify global Gemini CLI settings, global context, or global system instructions.
2. Do **not** delete the current experimental workspace. Move it under `\Operator\SIP`.
3. Do **not** preserve the current root workspace layout just because it exists.
4. Do **not** make memory layers ambient and eager.
5. Do **not** auto-store, auto-taskify, auto-questify, or auto-promote normal conversation.
6. Do **not** create custom MCPs/extensions if a robust existing one already fits.
7. Do **not** make graph or memory the main intention of every interaction.
8. Do **not** freewheel architecture beyond the explicit scope of this file.

---

## 2. Behavior target for clean `Operator`

The clean `Operator` workspace should behave like a mostly vanilla Gemini CLI daily driver that is simply:
- better informed
- less repetitive
- more context-conserving
- more capable when explicitly invoked

Default stance:
- read-only unless explicitly asked to change state
- use the narrowest sufficient layer
- keep outputs clean, compact, and result-oriented

---

## 3. Root workspace split

### Required result
Preserve the current experimental workspace under:
- `\Operator\SIP\`

Rebuild the root `\Operator\` as the clean daily driver.

### Do not move
- `.git`
- `.gitignore`
- whatever minimal root files are necessary to preserve the repo cleanly

### Move into `SIP`
All current experimental system content not needed for the new clean root.

### Report required
At the end, list exactly what was moved into `SIP`.

---

## 4. Required new root structure

Create or normalize the root `\Operator\` structure into:

- `db/`
- `memory/semantic/`
- `memory/graph/`
- `memory/procedures/`
- `docs/`
- `scripts/`
- `TaskReports/`
- `Vault/`
- `SIP/`

### Specific required files/subpaths
- `db/lifestate.db`
- `db/rve.db`
- `GEMINI.md`
- `README.md` if useful
- `docs/audits/`
- `docs/imports/`
- `memory/procedures/registry/`
- `memory/procedures/logs/`
- `memory/semantic/README.md`
- `memory/graph/README.md`

---

## 5. Obsidian Vault requirement

Create an Obsidian Vault in `\Operator\Vault\` designed for the human-facing side of the system.

### Vault purpose
This is the human PKM / doctrine / reflection / readable artifact side.
It is not the machine procedure store.

### Vault must include at minimum
- `Inbox/`
- `Daily/`
- `Projects/`
- `Reports/`
- `Doctrine/`
- `Profiles/`
- `Research/`
- `Reviews/`
- `Templates/`
- `Assets/`

### Required templates
Create templates for:
- Daily journal/check-in
- Task report
- Project brief
- Weekly review
- Doctrine note
- Research note

### Daily journal template must support
- thoughts / previous night / intentions / issues
- mental health
- physical health
- destructive habits active now
- helpful habits active now
- what is giving trouble now
- what is helping now
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
- anticipated vs actual metrics
- what each task unlocked
- tomorrow draft
- AI ingestion hook

This Vault should be clean enough for immediate human use.

---

## 6. Local-only `GEMINI.md` for clean daily-driver mode

Create a new local `GEMINI.md` at the root of `\Operator\`.

Its behavior rules must include:

### Default behavior
- No broad memory fan-out by default.
- No implicit writes.
- No auto-taskification.
- No automatic quest/project/report creation.
- RVE is invocable only, not ambient.
- Read-only unless explicitly asked to change state.

### Intent routing
- Task actions -> `db/rve.db`
- Profile/state actions -> `db/lifestate.db`
- Semantic memory -> only when explicitly relevant
- Graph lookup -> only when explicitly relevant
- Docs/canon -> only when needed
- Memory writes -> only when explicitly requested

### Output style
- clean
- compact
- stable
- result-first
- minimal process narration

### Additional shell rule
The system should prefer current-session context and a cached shell snapshot before interrogating all memory layers.

---

## 7. Layered memory design for clean daily driver

The clean daily driver should prepare multiple memory layers, but they must not interfere with each other or all activate on every turn.

### Layer A — Structured truth
Use:
- `db/lifestate.db`
- `db/rve.db`

Purpose:
- facts
- tasks
- projects
- anchors
- obligations
- current profile state

Authority:
- primary truth for direct operational state

### Layer B — Human-facing canon/docs
Use:
- `Vault/`
- `docs/`
- `TaskReports/`

Purpose:
- readable artifacts
- journals
- doctrine
- reports
- research notes

Authority:
- human-facing reference and authored source material

### Layer C — Semantic memory
Goal:
- active now if feasible using an existing robust memory tool/pattern
- reduce re-explanation
- remember useful recurring context

Important:
- do not make it ambient-write on every turn
- explicit remember/store and tightly scoped extraction only

### Layer D — Graph memory
Goal:
- active if feasible, but explicit-query oriented
- support relationship discovery, multi-hop linkage, and leverage surfacing

Important:
- do not poll graph on ordinary questions by default
- do not let graph override structured truth
- graph should enrich and connect, not replace truth

### Layer E — Procedural/machine memory
Use:
- `memory/procedures/`
- machine-facing logs/registries

Purpose:
- tool usage logs
- routing logs
- successful workflows
- prompt/procedure references
- promoted SOPs

Important:
- append/log oriented
- no silent freeform procedural mutation

---

## 8. Existing MCP/extension-first policy

Before creating any custom MCP server or extension, first look for a strong existing Gemini CLI extension, MCP, or compatible local tool that solves the problem more robustly.

### Required policy
For each desired capability:
1. identify whether an existing Gemini CLI extension/MCP/tool already fits
2. prefer the existing solution if it is robust enough
3. only create a custom MCP or wrapper if:
   - no suitable existing option exists
   - or the existing option lacks required hooks/behavior

### Required report
List:
- what existing MCPs/extensions/tools were found useful
- what was adopted as-is
- what was wrapped
- what still genuinely requires custom build

Do **not** fabricate a giant custom MCP suite if existing building blocks are enough.

---

## 9. Manual task system requirement

Expose task functionality immediately.
The task system in the clean driver should be manually usable from day one.

### Required capabilities
- add task
- list tasks
- update task
- complete task
- inspect current tasks/projects

### Important behavior
- keep it manual-first
- do not auto-generate side quests or aggressive RVE behaviors here unless explicitly invoked
- if an existing open-source task substrate is clearly better for daily-driver ergonomics, note that and structure toward it without forcing the full custom RVE stack into the clean root yet

`rve.db` should exist and be usable immediately.

---

## 10. Conversation / artifact audit scaffolding

Create a workflow-ready scaffold for auditing conversation files, failures, friction, retries, and insufficiencies.
This does **not** have to be always-on now, but it must be ready and navigable.

### Human-facing audit area
Use:
- `docs/audits/`

### Machine-facing audit area
Use:
- `memory/procedures/logs/`
- or structured logs if appropriate

### Audit targets to support later
- failed tool calls
- retries / multiple-attempt workflows
- frustration moments
- bad or hallucinated solutions
- obvious misses where a stronger route should have been taken
- candidate improvements / promoted fixes

### Create scaffolding for
- failure ledger
- friction ledger
- promoted fix registry
- conversation artifact imports

Do not make it ambiently noisy; just make it ready.

---

## 11. Artifact ingestion requirement

Deep research results, reports, and attached/pasted artifact-grade text must be queryable without polluting active context.

### Required behavior
Prepare the workspace so artifacts can be:
- stored
- indexed/queryable later
- linked to projects or audits
- ingested without being dumped into the prompt every turn

### Minimum structure
- `docs/imports/`
- linkage into the Vault and/or retrieval/index workflow later

This should support future retrieval without making every conversation heavy.

---

## 12. Tool and capability awareness

The clean daily driver should know what tools are available without turning tool inventory into prompt pollution.

### Create a capability scaffold for later use
Track at least:
- tool name
- install state
- what it is for
- when to use it
- trust/permission level if relevant
- notes/examples

This may live in docs and/or machine-facing procedure memory.

The shell should eventually be able to answer:
- what tools do I have?
- when should I use them?
- what is the preferred route for a given task?

without loading the whole registry every turn.

---

## 13. Graph setup decision for clean driver

Use the following standard:

### Preferred outcome
If Neo4j/graph can be set up now cleanly, do it in an explicit-query, non-ambient way.

### Acceptable fallback
If full graph activation is too much for this pass, scaffold it cleanly so it can be enabled without tearing up the workspace.

### Graph purpose in clean driver
- relationship discovery
- project/tool/doc/person/org linkages
- leverage surfacing
- not normal-turn default routing

Report which path was chosen and why.

---

## 14. Semantic memory setup decision for clean driver

Use the following standard:

### Preferred outcome
Activate an existing robust semantic memory layer now if possible.

### Constraint
It must not become an always-on writer that stores every utterance.

### Purpose
- reduce re-explanation
- preserve useful recurring context
- semantic recall when explicitly relevant

Report what was activated and how it is gated.

---

## 15. Initial root deliverable standard

At the end of this run, the clean `\Operator\` root should be:
- clean
- usable
- mostly vanilla-feeling
- manually task-capable
- memory-capable without obsession
- ready for human use and later layer growth

It should **not** feel like the old mutant workspace at the root.

---

## 16. Final output required from Gemini

Report:
1. exactly what was moved into `SIP`
2. the exact new root structure
3. files created or normalized
4. the contents/purpose of the new local `GEMINI.md`
5. whether graph was scaffolded or activated
6. whether semantic memory was scaffolded or activated
7. how manual task use is exposed now
8. what existing MCPs/extensions/tools were preferred before custom build
9. whether the Obsidian Vault is ready for immediate use
10. whether the root workspace now behaves like a clean daily driver

---

## 17. Final rule

This run is not about maximum architecture.
It is about creating a clean, powerful, low-friction daily driver with layered growth potential and no obnoxious ambient behavior.

That is the standard.
