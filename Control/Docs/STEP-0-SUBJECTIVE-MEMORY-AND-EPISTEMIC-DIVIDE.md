# STEP 0 — SUBJECTIVE MEMORY AND THE EPISTEMIC DIVIDE

Status: ACTIVE
Purpose: Integrate subjective journaling, self-observation, and human-state analysis into the Operator substrate without corrupting technical truth, developer precision, or general-purpose reliability.

---

## 1. Executive judgment

The uploaded memory research adds one major architectural correction:

The system cannot treat all memory as one epistemic class.

Technical facts, schemas, commands, project rules, and tool behaviors do not obey the same truth model as:
- journal entries
- reflections
- frustrations
- moods
- bodily sensations
- temporary self-beliefs
- partially true personal narratives

If both are stored and retrieved under one undifferentiated memory regime, the system will either:
- become too rigid for human material, or
- become too mushy for technical work.

Therefore Step 0 must explicitly implement an **epistemic divide**.

---

## 2. The divide

### Objective state
Use for:
- technical facts
- code and system knowledge
- environment facts
- tool behavior
- verified user constraints
- project structure
- database truth
- durable operational procedures

Authority rule:
- explicit truth standards
- verification-first when feasible
- high resistance to silent overwrite

### Subjective state
Use for:
- journals
- reflections
- perceptions
- emotional states
- self-estimates
- emerging beliefs
- narrative interpretations
- physiological and psychological observations
- skill-friction reports

Authority rule:
- pattern recognition over strict fact assertion
- time-sensitive and revision-friendly
- should often be stored as observations, signals, hypotheses, or trends rather than permanent truths

---

## 3. Why this matters

A statement such as:
- "the Firecrawl key is stored in X"
requires a very different storage and retrieval logic than:
- "I feel incapable of learning this framework today"

The first should behave like technical truth.
The second should behave like a temporal state sample.

The system must be able to preserve both without confusing them.

---

## 4. Architectural consequence

The Operator substrate should gain a dedicated subjective-memory lane that is parallel to, not merged into, the technical truth lane.

This means:
- do not store journals directly into canonical technical truth stores
- do not let subjective retrieval contaminate technical tool selection by default
- do not let technical truth-verification logic invalidate legitimate subjective experience

Instead, create a separate subjective-memory subsystem with its own schemas, routing rules, consolidation rules, and retrieval triggers.

---

## 5. Recommended stores

### Canonical technical stores
Remain:
- arsenal.db
- audit.db
- artifact_index.db
- lifestate.db
- rve.db
- student_resources.db

### New subjective-memory lane
Recommended additions:

#### essence.db
Purpose:
- distilled human-state representations
- recurring patterns
- trigger maps
- opportunity vectors
- longitudinal skill-friction patterns
- state summaries derived from journals and observations

#### essence_logs/
Purpose:
- raw journals
- reflection files
- subjective observations
- optional physiological data exports
- low-level personal narrative artifacts

#### essence_graph (later)
Purpose:
- relations between triggers, beliefs, skills, constraints, opportunities, and recurring states
- graph representation of pattern links rather than plain fact storage

The raw human material should stay human-readable.
The distilled layer should stay structured.

---

## 6. Storage classes inside subjective memory

### Class A — Raw subjective entries
Examples:
- journals
- notes to self
- reflections after events
- sleep or stress observations

Properties:
- immutable or append-mostly
- human-readable
- not treated as final truth

### Class B — Distilled observations
Examples:
- recurring frustration themes
- repeated confidence dips around a skill
- emerging pattern of low energy after a certain workflow

Properties:
- generated from repeated evidence
- tagged with confidence and recency
- revision-friendly

### Class C — Behavioral hypotheses
Examples:
- probable trigger patterns
- probable high-flow conditions
- likely burnout precursors
- opportunity-vector candidates

Properties:
- explicitly marked as hypotheses
- should never be confused with hard truth

### Class D — Matured pattern signals
Examples:
- stable trigger map
- stable preferred learning conditions
- consistent environmental blockers
- well-supported skill progression signals

Properties:
- higher confidence
- still not identical to technical truth
- usable by planning and coaching layers

---

## 7. Retrieval rules

### Default technical mode
When the user is doing technical work:
- only objective memory is retrieved by default
- subjective memory is not injected unless clearly relevant

### Reflection mode
When the user is journaling, reviewing, or asking about patterns:
- subjective memory becomes eligible
- raw logs stay behind distilled summaries unless needed

### Hybrid coaching mode
When the user asks about performance, burnout, learning, opportunity, or stuck patterns:
- retrieve from both lanes
- but keep them visibly separated in the output

This separation is mandatory.

---

## 8. Consolidation logic

The uploaded research strongly supports a metabolism-style loop for subjective memory.

Recommended consolidation stages:

1. ingest raw entry into `essence_logs/`
2. classify signals, themes, and entities
3. compare against recent patterns
4. merge repeated low-value redundancy
5. preserve meaningful deviations
6. generate or update distilled observations in `essence.db`
7. periodically surface only the highest-value patterns back to the user

This is where ideas like prediction-error gating, selective forgetting, and offline consolidation become useful.

---

## 9. Rules for safety and honesty

### Rule A — No fake psychological certainty
The system may suggest patterns, not diagnose the user.

### Rule B — Signals are not verdicts
Linguistic shifts, repeated sentiments, or behavior patterns should be stored as evidence or hypotheses, not medical truths.

### Rule C — Subjective memory is local-first
Keep deeply personal material local unless explicitly exported.

### Rule D — Reviewable promotion
Do not silently convert a raw feeling into a durable life rule.

### Rule E — Technical work stays clean
Subjective memory must not quietly degrade the quality of technical execution.

---

## 10. Impact on Step 0

This changes Step 0 in one important way:

RVE is not the only early consumer of the substrate.
A dedicated subjective-memory lane is also an early consumer.

So Step 0 should now aim to establish:
- the general Operator substrate
- the canonical technical stores
- the audit/archive layer
- the artifact index
- the subjective-memory lane
- then RVE and other consumers on top

---

## 11. Final judgment

The correct answer to subjective journaling and human-state persistence is **not** to weaken technical truth.
It is to add a second lane with different epistemic rules.

The Operator substrate should therefore be designed around a dual-state memory architecture:
- objective memory for technical and operational truth
- subjective memory for human-state, narrative, and longitudinal pattern analysis

That is the cleanest path to building a powerful system that can understand both the machine-facing and human-facing sides of the operator without corrupting either.
