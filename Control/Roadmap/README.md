# Step 0 Roadmap Index

Status: ACTIVE
Branch: `roadmap/step-0-operator-substrate`
Purpose: Provide a stable entrypoint for new threads, new agent runs, and implementation sessions so the Operator substrate architecture can be resumed without reconstruction.

---

## What this folder is for

This folder is the implementation handoff surface for Step 0.

It exists so that a new Gemini CLI session can:
1. pull one branch
2. read one roadmap index
3. understand the current target architecture
4. execute in the correct order without drifting back into theory-only work

This folder does **not** replace the canon docs in `Control/Docs/`.
It points to them and organizes them into an execution order.

---

## First-read documents

Read these first, in order:

1. `Control/Docs/STEP-0-OPERATOR-SUBSTRATE-CANON.md`
2. `Control/Docs/STEP-0-MEMORY-ARCHITECTURE-CANON.md`
3. `Control/Docs/STEP-0-CAUSAL-MAP-AND-OPERATING-MODEL.md`
4. `Control/Docs/STEP-0-EXECUTION-ORDER-AND-DEFERRED-WORK.md`
5. `Control/Roadmap/STEP-0-MASTER-ROADMAP.md`
6. `Control/Roadmap/STEP-0-HERMES-COMPATIBILITY-AND-SHARED-MEMORY.md`
7. `Control/Roadmap/GEMINI-STEP-0-EXECUTION-HANDOFF-PROMPT.md`

---

## Current target

The Step 0 target is:

**A better-than-standard Gemini CLI operator substrate whose main source of compounding power is canonical truth, layered memory, artifact retrieval, auditability, and self-improvement — with RVE as an early high-value consumer, not the entire system.**

---

## Current execution order

### Phase 0A — Doctrine locked
Use the Step 0 canon docs as build law.

### Phase 0B — Canonical DB family
Finish and verify:
- arsenal.db
- audit.db
- artifact_index.db
- lifestate.db
- rve.db
- student_resources.db

### Phase 0C — Registries
Build:
- tool / MCP / extension / skill / integration inventory
- credential registry metadata
- provenance/path/install registry

### Phase 0D — Audit + session archive loop
Build:
- session archive structure
- failure/friction log format
- append-only audit behavior

### Phase 0E — Artifact indexing
Build:
- file/doc/resource index
- tags/classifications/pointers
- retrieval-friendly structure for docs and archives

### Phase 0F — Context export layer
Build:
- current-state export
- project-specific export
- capability export
- recent-failure export

### Phase 0G — Continue RVE on the substrate
Use RVE as a consumer of the substrate, not the substrate itself.

---

## Rules for new threads / new runs

1. Do not restart architectural theory from scratch.
2. Do not treat RVE as the entire Step 0 target.
3. Do not productionize vector/graph/mem0 layers before the canonical substrate is stable.
4. Do not silently mutate canon docs without noting why.
5. For any build session, update roadmap docs if the architecture or implementation order materially changes.

---

## Operational note

If opening a fresh Gemini CLI thread, begin with the handoff prompt at:

`Control/Roadmap/GEMINI-STEP-0-EXECUTION-HANDOFF-PROMPT.md`

That file is the single best re-entry point.
