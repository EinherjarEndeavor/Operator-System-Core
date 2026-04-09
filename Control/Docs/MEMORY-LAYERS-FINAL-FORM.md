# MEMORY LAYERS FINAL FORM

Status: Active canon
Purpose: Convert the sprawling layered-memory brainstorm into a practical final-form architecture that can actually be implemented without polluting active context or overbuilding too early.

---

## 1. Executive judgment

The repo now has substantially better RVE, truth-routing, source-selection, and execution doctrine than it has memory doctrine.

The current gap is not “more RVE theory.”
The current gap is that memory is still described mostly as a powerful intention, not as a tight final-form stack with explicit layer roles, authority rules, and implementation sequence.

This document is the final-form answer to that gap.

---

## 2. First rule

Memory is not one thing.
It is a stack of different storage and retrieval responsibilities.

If these responsibilities are mixed together, the system becomes:
- bloated
- unreliable
- hard to query
- easy to corrupt
- expensive in context

So the design rule is:
- structured truth stays structured
- active execution stays queryable
- human-facing canon stays human-facing
- retrieval is used for discovery
- graph is used for relationships
- active context stays thin

---

## 3. The final-form layer stack

### Layer 0 — Active operating buffer

#### Role
The thin live control layer for the current session.

#### Holds
- current mission
- active constraints
- command dispatcher rules
- query routing rules
- currently invoked project context
- current user request

#### Must stay small
Do not store:
- giant corpora
- full canon docs
- tool encyclopedias
- raw archives

#### Success condition
A model can operate intelligently without wasting active context on things that could be retrieved.

---

### Layer 1 — Episodic/session history

#### Role
A log of what happened in sessions and runs.

#### Holds
- session traces
- tool calls
- import/migration logs
- patch logs
- run outputs
- weekly reviews if stored as history

#### Use case
Helpful for audit, debugging, and reconstruction.

#### Not for
- stable profile truth
- stable task state
- final canon doctrine

---

### Layer 2 — Canonical structured truth

#### Role
The stable machine-readable truth layer.

#### Holds
- lifestate facts
- contacts
- supports
- constraints
- treatment/legal/health/school state
- RVE tasks
- RVE projects
- obligations
- anchors
- idea records
- habits if tracked structurally
- structured opportunity records for Re.Match

#### Storage forms
- SQLite first
- additive, provenance-aware rows
- explicit state fields

#### Not for
- persuasive writing
- broad narrative self-description
- ungrounded inferences
- doctrine prose
- giant raw reports

#### Success condition
A command can answer operational questions from Layer 2 without freehand reinterpretation.

---

### Layer 3 — Retrieval/index layer

#### Role
Fast search and retrieval over messy corpora and canon artifacts.

#### Holds
Not the raw documents themselves as the only truth, but an indexed representation of them.

#### Primary functions
- semantic retrieval
- chunk lookup
- metadata filtering
- source-grounded recall
- “find relevant docs/chunks about X”

#### Data sources
- AI deep research reports
- Wave1Canon ore reserve
- doctrine docs
- website/content source material
- extracted conversations and notes

#### Storage forms
- chunk registry
- embeddings / vector index
- metadata + provenance
- retrieval manifests

#### Not for
- replacing Layer 2
- storing raw operational truth instead of DB rows
- pretending relationship intelligence already exists

#### Success condition
You can reliably surface the right sources without manually digging through file swamps.

---

### Layer 4 — Human-facing canon/artifact layer

#### Role
The authored knowledge and deliverable layer.

#### Holds
- canon docs
- feature-driven specs
- battle plans
- build contracts
- website copy
- reports
- dossiers
- style exemplars
- identity axioms and doctrine

#### Key rule
Layer 4 is for human-legible reference and output quality.
It is not the same as machine-truth storage.

#### Success condition
Future-you and Gemini can operate from a small set of coherent documents instead of the ore reserve.

---

### Layer 5 — Graph / relationship layer

#### Role
Relationship intelligence over extracted entities and links.

#### Holds
- entities
- concepts
- tools
- projects
- reports
- people
- opportunities
- claims
- links between them

#### Use case
Answer relationship questions such as:
- what connects these projects?
- what tools recur across multiple reports?
- which concepts reinforce or contradict each other?
- what reports tie RVE, Re.Match, and recovery together?

#### Critical rule
Graph extracted structure, not raw paragraph dumps.

#### Success condition
The graph answers relationship questions better than retrieval alone.

---

## 4. Hot vs invocable memory

### Always-hot
Only keep these effectively hot:
- Layer 0 operating rules
- current project focus
- current command behavior rules
- query-to-document routing rules
- minimal user-specific constants needed for current work

### Invocable on demand
Retrieve when needed:
- deep canon docs
- source files
- retrieval chunks
- graph relations
- portfolio docs
- opportunity databases
- doctrine artifacts

This is how you preserve capability without poisoning active context.

---

## 5. Authority rules across layers

### Highest authority for direct truth
1. direct current clarification
2. Layer 2 structured truth
3. accepted canon docs in Layer 4
4. retrieved source docs from Layer 3
5. graph inferences from Layer 5

### Highest authority for authored design intent
1. accepted canon docs in Layer 4
2. stronger historical build-contract docs
3. raw brainstorm/source piles

### Important rule
Graph links and semantic retrieval do not outrank direct structured truth.
They support it.

---

## 6. Memory objects by project

### RVE
- Layer 2: tasks, projects, anchors, habits, ideas, completions
- Layer 4: canon specs, command contracts, rollout diffs
- Layer 3 later: retrieval over old RVE notes and doctrine
- Layer 5 later: relationships between projects, routines, obstacles, and outcomes

### Re.Match
- Layer 2: profile schema, opportunity records, dossiers, outcomes
- Layer 4: service canon, intake contract, dossier templates
- Layer 3 later: retrieval over research reports and resource corpora
- Layer 5 later: relationship mapping between profiles, opportunities, barriers, and results

### Deep Research Engine
- Layer 2: project state, task state, corpus manifests
- Layer 4: canonized reports and playbooks
- Layer 3: major home of document retrieval
- Layer 5 later: concept, report, and tool relationships

### Website / public layer
- Layer 2: project and publishing state
- Layer 4: public artifacts and copy
- Layer 3: source retrieval for writing and portfolio proof

---

## 7. What the repo still needed

Before this doc, the repo had:
- strong truth-routing doctrine
- strong RVE thickening
- strong project portfolio doctrine
- a good roadmap saying memory/retrieval/graph come later

But it still lacked a final-form memory document that answered:
- what each layer is actually for
- what stays hot vs invocable
- where retrieval fits
- where graph fits
- how Layer 2, Layer 3, Layer 4, and Layer 5 relate

That is what this file is intended to solve.

---

## 8. Implementation sequence

### Step 1
Stabilize Layer 2 and Layer 4 first.
This means:
- trustworthy lifestate and RVE DBs
- strong canon docs

### Step 2
Build Layer 3 retrieval.
This means:
- chunking
- embeddings/index
- metadata
- provenance
- query routines

### Step 3
Build Layer 5 graph only after Layer 3 is useful.
This means:
- extract entities/relations from selected corpora
- graph them with provenance
- query for relationships, not basic storage

### Step 4
Only then consider more aggressive automation over the stack.

---

## 9. Red-team warnings

The memory system fails when:
- Layer 0 becomes a garbage dump
- Layer 2 contains narrative and guesses as if they were facts
- Layer 3 is treated as if it were already a graph brain
- Layer 4 becomes another slop archive instead of canon
- Layer 5 is used before retrieval and truth are stable
- every problem is answered with “add another layer”

The memory system succeeds when:
- truth is stable
- execution is queryable
- canon is authored
- retrieval is reliable
- graph adds relationship intelligence later instead of confusion now

---

## 10. Final rule

Do not ask the graph to do the DB’s job.
Do not ask the DB to do the canon’s job.
Do not ask canon docs to replace retrieval.
Do not ask retrieval to replace direct truth.
Do not ask Layer 0 to carry the whole system.

Each layer should do one job well.
