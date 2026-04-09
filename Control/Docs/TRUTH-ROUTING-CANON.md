# TRUTH ROUTING CANON

Status: Proposed control document
Purpose: Define what belongs in each memory layer, what does not, and what level of proof is required before information is promoted.

## Executive judgment

The current project is worth doing.
The current risk is over-architecting before truth-routing rules are stable.

This system only needs to do four things well right now:
1. preserve direct facts without corruption
2. preserve tasks, obligations, and project state in structured form
3. preserve human-facing canon artifacts
4. prevent narrative or speculation from being silently promoted into ground truth

## Minimal practical layer stack

### Layer 0 — Active buffer / dispatcher
Use for:
- current mission
- active constraints
- command dispatcher rules
- retrieval instructions
- current session state

Do not use for:
- long registries
- full command encyclopedia
- raw corpora
- large profile dumps

### Layer 1 — Episodic logs
Use for:
- session traces
- actions taken
- tool calls
- import and migration logs
- audit trail

Do not use for:
- stable profile truth
- stable task state
- doctrine

### Layer 2 — Canonical structured truth
Use for:
- profile facts with provenance
- contact facts
- legal and program constraints
- treatment and benefits status
- work history facts
- certifications
- tasks
- obligations
- project records
- schedules and anchors

Do not use for:
- persuasive positioning
- self-branding language
- stylistic narration
- self-issued prestige claims unless explicitly tagged
- synthetic planning placeholders unless clearly marked provisional

### Layer 3 — Semantic / graph / advanced retrieval
Status: deferred
Do not block current progress on this layer.

### Layer 4 — Human-facing canon / artifacts
Use for:
- cover letters
- resumes
- doctrine docs
- workflow docs
- longform synthesis
- style and voice exemplars

Do not use for:
- exact operational state that must be queried like a database

## Allowed truth classes

### DIRECT_FACT
Definition: Explicitly stated in a source or directly clarified by the user.
Default handling: May enter Layer 2.

### SOURCE_CONFLICT
Definition: Two sources disagree.
Default handling: Do not canonize blindly. Require confirmation or conflict tagging.

### INFERRED_INTERPRETATION
Definition: Reasonable conclusion derived from facts, but not directly stated as truth.
Default handling: provisional only, or Layer 4 analysis; not default Layer 2 canon.

### ARTIFACT_NARRATIVE
Definition: Persuasive or presentational writing meant to influence an audience.
Default handling: Layer 4.

### SELF_ISSUED_CLAIM
Definition: User-created milestone or credential not institutionally verified.
Default handling: may be stored only if tagged as self-issued or self-verified.

### SYNTHETIC_PLACEHOLDER
Definition: invented scaffolding variable used for planning or gamification.
Default handling: never default canonical truth.

## Routing rules

Rule A — If it would be costly to discover it was guessed, it is not a Layer 2 fact.

Rule B — If the text is trying to persuade, it is artifact-first, not truth-first.

Rule C — If the item is useful but not certain, keep it provisional instead of deleting it.

Rule D — Direct later clarification outranks stale or conflicting file content when explicitly stated.

Rule E — Graph and semantic layers do not get built out before Layer 2 truth discipline is stable.

## Immediate implications

1. Keep layers 0, 1, 2, and 4 in play.
2. Treat Layer 3 as deferred.
3. Ingest structured facts selectively.
4. Store persuasive documents as artifacts unless specific fields are extracted with provenance.
5. Do not keep expanding architecture until the ingestion path is trustworthy.
