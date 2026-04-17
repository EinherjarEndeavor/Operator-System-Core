# STEP 0 — MEMORY ARCHITECTURE CANON

Status: ACTIVE
Purpose: Define the layered memory architecture for the Operator substrate so “memory” becomes a controlled force multiplier instead of a context-polluting blob.

---

## 1. Executive judgment

The memory system should be **multi-layered, role-separate, and canonical-first**.

The architecture must support future high-end capabilities like:
- Hermes-style self-improving workflows
- Clawhub-style ontology and self-improving agents
- future shared memory across Windows + WSL/Linux agents
- future graph and simulation-driven workflow optimization

But the build order must remain sane.

**Canonical truth must come first.**
All other memory layers consume, index, enrich, or retrieve around canonical truth.

---

## 2. Memory roles

### Role 1 — Canonical structured truth
Purpose:
- exact facts
- structured user state
- structured project/task state
- structured capability registry
- structured audit metadata

Backends:
- SQLite family of DBs
- selected markdown canon docs

This is the sovereign layer.

### Role 2 — Episodic / operational memory
Purpose:
- session traces
- terminal logs
- task execution history
- import/migration logs
- failure records
- postmortems
- adjudications

Backends:
- append-only logs
- audit.db
- archived session files

This is how the system learns from actual use instead of vibes.

### Role 3 — Artifact memory
Purpose:
- docs
- research reports
- notes
- archives
- uploads
- web captures
- canonical artifacts

Backends:
- artifact_index.db
- structured file trees
- markdown canon/docs

This is the retrievable knowledge layer.

### Role 4 — Semantic / vector memory
Purpose:
- retrieval over artifacts
- relevance ranking
- contextual surfacing of prior work
- retrieval across large corpora without ambient injection

Backends:
- vector store (deferred in implementation order)

This layer is assistive, not sovereign.

### Role 5 — Graph / ontology memory
Purpose:
- explicit entities and relations
- dependency maps
- workflow patterns
- tool-to-use-case relations
- project-to-resource relations
- user pattern discovery
- future shared multi-agent memory

Backends:
- graph database such as Neo4j (deferred in implementation order)

This layer is for structure discovery, routing, and relationship reasoning.

### Role 6 — Agent-context memory
Purpose:
- compact exports into agent sessions
- preference and recent-state recall
- cross-session continuity

Backends:
- compact JSON exports
- future mem0-style layers

This layer should never become the hidden source of truth.

---

## 3. Sovereignty rules

### Rule A — SQLite / canon first
The canonical source of truth remains SQLite + markdown canon.

### Rule B — Vector and graph are augmentation layers
They retrieve, relate, and enrich.
They do not silently redefine truth.

### Rule C — Agent memory is downstream
Any mem0-style or conversational memory system should consume exported truth and episodic summaries, not invent or overwrite core state.

### Rule D — Doctrine remains doctrine
Values, narrative, mission, archetypes, and philosophy may be indexed and retrievable, but they are not ordinary structured truth rows unless a doctrine-aware schema explicitly stores them as such.

### Rule E — Reviewable promotion
Information promoted from logs or artifacts into structured truth must pass review gates.

---

## 4. Recommended Step 0 DB family

### arsenal.db
Purpose:
- MCP servers
- extensions
- skills
- integrations
- credential registry metadata
- install paths
- health status

### audit.db
Purpose:
- append-only system reviews
- friction logs
- failure analyses
- schema decisions
- improvement proposals
- adjudication records

### artifact_index.db
Purpose:
- file path inventory
- tags
- titles
- summaries
- type/classification
- retrieval pointers

### lifestate.db
Purpose:
- stable or slow-moving structured user truth
- constraints, contacts, affiliations, locations, energy profile, real appointments

### rve.db
Purpose:
- execution state
- tasks, projects, obligations, schedule anchors, ideas, habits, completions

### student_resources.db
Purpose:
- domain-specific reference data for PCC/student support and related resources

These databases form the canonical base.

---

## 5. Recommended implementation order

### Phase 1 — Canonical truth
Build and populate the SQLite family with clean boundaries.

### Phase 2 — Episodic archive and audit
Ensure terminal sessions, failures, postmortems, and migration records are archived and queryable.

### Phase 3 — Artifact indexing
Index docs, notes, reports, uploads, and archives into artifact_index.db.

### Phase 4 — Context export layer
Create compact exports for:
- current user state
- current project state
- tool/capability state
- recent friction/failure state

### Phase 5 — Semantic retrieval
Add vector retrieval over docs and archives.
Only after canonical truth and artifact indexing are stable.

### Phase 6 — Graph / ontology layer
Add graph memory for entities, dependencies, workflow patterns, and multi-agent shared relations.

### Phase 7 — Agent-memory layer
Add mem0-style or equivalent contextual recall systems that consume canonical exports and episodic summaries.

---

## 6. Hermes-aligned future capability target

The long-range target is a system that can evolve from:
- passive archival
- to post-run optimization
- to guarded workflow interception
- to shared graph-backed multi-agent reasoning

But the safe progression is:
1. record
2. index
3. retrieve
4. relate
5. optimize
6. simulate

Trying to start at stage 6 creates chaos.

---

## 7. Shared-memory future with WSL / Linux

Future Hermes/OpenClaw/Gemini-on-Kali interoperability should use:
- shared canonical databases where appropriate
- shared artifact indexes
- context export artifacts
- graph-backed relation layers
- explicit sync points

Do not design around Linux-only tools now.
Design the canonical memory substrate so they can attach later.

---

## 8. Final judgment

The best Step 0 memory architecture is not one magic memory product.
It is a **layered memory family** in which:
- SQLite + canon docs are sovereign
- episodic archives preserve real experience
- artifact indexes preserve retrievability
- vector and graph layers enrich retrieval and relationships
- agent memory consumes exported state rather than rewriting truth

That is the memory architecture strong enough to grow toward Hermes-grade capability without poisoning the base.
