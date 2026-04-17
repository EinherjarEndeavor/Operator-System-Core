# STEP 0 — EXECUTION ORDER AND DEFERRED WORK

Status: ACTIVE
Purpose: Convert the Step 0 substrate doctrine into a disciplined execution sequence so the build can begin immediately without losing the architectural thread.

---

## 1. Executive judgment

Yes, a roadmap is still worth having.

Not because more brainstorming is needed.
Because this architecture is large enough that without a build order, execution will drift into:
- premature graph work
- premature memory-product integration
- overfitting the base to RVE
- random extension/tool accumulation without hardening the substrate

This roadmap is intentionally short, execution-coupled, and biased toward producing operational artifacts quickly.

---

## 2. Phase order

### Phase 0A — Lock doctrine
Deliverables:
- Step 0 substrate canon
- memory architecture canon
- causal map / operating model
- this execution-order doc

Exit condition:
- the target system is defined clearly enough that implementation can proceed without “what are we even building?” drift

### Phase 0B — Harden canonical DB family
Deliverables:
- stable schemas for arsenal.db, audit.db, artifact_index.db, lifestate.db, rve.db, student_resources.db
- clear table boundaries
- no table pretending to do five jobs

Exit condition:
- the canonical stores are trustworthy enough to start using immediately

### Phase 0C — Build registries
Deliverables:
- tool / MCP / extension / skill / integration inventory
- credential registry metadata (no plaintext secrets)
- path/install/provenance registry
- artifact/file inventory skeleton

Exit condition:
- the environment is legible instead of invisible

### Phase 0D — Build session archive + audit loop
Deliverables:
- session log archive structure
- failure / friction logging format
- append-only audit behavior
- first operator review workflow

Exit condition:
- the system can preserve operational history and mine it later

### Phase 0E — Build artifact indexing and retrieval
Deliverables:
- artifact_index.db population pipeline
- tags, classifications, and pointers for docs, notes, uploads, archives
- retrieval-friendly indexing over canon/docs

Exit condition:
- the user’s knowledge pile becomes discoverable rather than dead weight

### Phase 0F — Build context export layer
Deliverables:
- compact current-state export
- project-specific export
- capability/tool export
- recent-failure export

Exit condition:
- future agents and memory layers can consume grounded state without giant ambient context blobs

### Phase 0G — Continue RVE as first structured domain
Deliverables:
- clean RVE schemas and imports aligned to the substrate
- RVE as consumer of the base, not the base itself

Exit condition:
- immediate daily productivity value is online

### Phase 0H — Defer higher memory layers, but prepare attachment points
Deliverables:
- documented attachment points for vector retrieval, graph memory, mem0-style agent memory, and future Hermes/OpenClaw cooperation

Exit condition:
- the base can evolve later without rewrite

---

## 3. Immediate build priority

If execution starts now, the first real build priorities should be:

1. finish and verify the DB family
2. finish the tool/capability registry
3. finish session archive + audit behaviors
4. finish artifact indexing
5. finish context export
6. continue RVE on top of that

That is the shortest path to both:
- immediate utility
- long-range memory power

---

## 4. What is explicitly deferred

The following should be documented but not treated as Step 0 blocking work:

### Deferred memory expansions
- vector store productionization
- Neo4j / graph productionization
- mem0-style agent memory integration
- digital twin / simulation environment
- active middleware interception of every tool call

### Deferred self-improvement expansions
- auto-generated skills/scripts with CI gating
- immune-system middleware that blocks bad commands live
- multi-agent shared graph reasoning
- self-modifying package distribution flows

### Deferred product/module expansions
- full learning/tutoring engine
- research automation engine
- website/service surface
- Re.Match full database-first platform
- Second Wind / Forge systemization

These all remain future consumers or higher-order layers.

---

## 5. Powerful memory architecture target without premature build

The target state remains:
- canonical truth in SQLite + canon docs
- episodic archives for real experience
- artifact indexes for retrieval
- future vector retrieval over documents
- future graph relations over entities, workflows, and dependencies
- future agent-memory consumption of exported state

But Step 0 wins by making that future possible, not by fully building all of it at once.

---

## 6. Definition of success for Step 0

Step 0 is successful when:
- the environment is organized and legible
- canonical DBs exist and are populated enough to be useful
- tools/skills/MCPs are visible in a registry
- logs and failures are being archived
- docs/research/resources are indexable and retrievable
- context exports exist for future agents
- RVE can begin operating on top of the substrate
- future memory layers have clear attachment points

If those are true, the base is ready.

---

## 7. Final judgment

The correct move is:
- keep the roadmap
- keep it short
- use it to execute immediately
- resist the temptation to replace execution with more ideation

This is now an execution problem, not a concept problem.
