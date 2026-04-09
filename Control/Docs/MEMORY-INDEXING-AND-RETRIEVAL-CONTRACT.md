# MEMORY INDEXING AND RETRIEVAL CONTRACT

Status: Active contract
Purpose: Define the minimum viable indexing, retrieval, and later graph-ingest workflow so the memory system can move from theory to implementation without dumping raw slop into expensive infrastructure.

---

## 1. Executive judgment

The next major documentation gap after RVE hardening is not “more RVE docs.”
It is the bridge from file swamp to retrievable intelligence.

The repo already has:
- truth-routing rules
- source-selection rules
- Wave1Canon canonization rules
- a roadmap that says retrieval comes before graph
- a strong memory brainstorm describing the need

What it lacked was an explicit contract for:
- what gets indexed
- how it gets chunked
- what metadata must be attached
- when retrieval is “good enough”
- when graph ingest is justified

This document fills that gap.

---

## 2. The first principle

Do not build “memory” by shoveling raw documents into a single store and hoping insight appears.

Build it in this order:
1. select source classes
2. normalize and chunk
3. attach metadata and provenance
4. index for retrieval
5. prove retrieval usefulness
6. only then extract entities/relations for graph

---

## 3. Source classes for indexing

### Class A — High-value retrieval sources
Index early.

Examples:
- AI deep research reports
- canon docs
- feature-driven specs
- battle plans
- RVE rollout/master briefing/source doctrine
- curated project notes

### Class B — Raw but useful ore
Index after basic normalization.

Examples:
- Wave1Canon piles
- passover materials
- long brainstorm files
- extracted threads

### Class C — Structured truth mirrors
Usually do not index as raw documents first.
Prefer querying the DB directly.

Examples:
- `lifestate.db`
- `rve.db`
- structured opportunity records

### Class D — Sensitive or low-value artifacts
Index only if there is a real need and privacy handling is intentional.

---

## 4. Chunking contract

Each chunk should preserve enough meaning to be useful, but not become a mini-book.

### Good chunk characteristics
- one coherent idea or subsection
- enough local context to understand the point
- a stable title/header if possible
- explicit source file path
- stable chunk id

### Bad chunks
- giant whole-document blobs
- tiny fragments with no context
- mixed topics from unrelated sections

### Practical guidance
Use heading-aware chunking when possible.
Fallback to paragraph/block chunking when structure is weak.

---

## 5. Required metadata per chunk

Every retrievable chunk should carry:
- source_path
- source_class
- document_title
- chunk_id
- section_title if available
- created/imported timestamp
- provenance notes
- project tags if known
- domain tags if known
- sensitivity tag if needed

Optional but useful:
- authority class
- related project
- content type (doctrine/report/note/spec/artifact)
- confidence of extraction

---

## 6. Retrieval objectives

The retrieval layer must be able to answer questions like:
- what reports discuss topic X?
- what canon docs are relevant to project Y?
- what prior notes discuss concept Z?
- what source material supports this current build decision?

If retrieval cannot do that reliably, it is not ready for graph escalation.

---

## 7. Query modes

### Mode 1 — Document retrieval
Return the best whole documents.
Useful when the user wants the primary canonical source.

### Mode 2 — Chunk retrieval
Return the best local passages.
Useful for synthesis and precise grounding.

### Mode 3 — Filtered retrieval
Filter by:
- project
- domain
- authority class
- date/time range
- source type

### Mode 4 — Canon-first retrieval
Prefer Layer 4 canon docs over ore files when both discuss the same topic.

---

## 8. Canon-first routing rule

When a topic has both:
- a refined canon doc, and
- several raw source files

retrieval should prefer the canon doc first, then surface raw sources only when deeper trace-back or unresolved ambiguity is needed.

This prevents the ore reserve from constantly outranking refined truth.

---

## 9. Graph-ingest gate

Graph ingest is allowed only after retrieval is already useful.

### Graph-ingest justification questions
- are there relationship questions retrieval alone cannot answer well?
- do we have stable enough metadata and provenance?
- are the entities worth tracking explicitly?
- is the corpus large enough and connected enough to justify graph maintenance?

If the answer is no, stay at retrieval.

---

## 10. What gets graphed later

Graph later:
- projects
- tools
- reports
- concepts
- entities
- supports/opportunities
- people/orgs if useful and safe
- relationship edges with provenance

Do NOT graph first:
- every raw paragraph
- all duplicate source fragments
- everything with no entity extraction discipline

---

## 11. Minimum viable implementation sequence

### Step 1 — Pick corpus slices
Start with:
- canon docs
- AI deep research reports
- selected high-value doctrine files

### Step 2 — Normalize
Convert into retrieval-friendly text with stable paths and titles.

### Step 3 — Chunk + metadata
Chunk intelligently and attach metadata.

### Step 4 — Index
Build retrieval/search capability.

### Step 5 — Test
Prove that queries return useful grounded results.

### Step 6 — Expand corpus
Only after step 5 works.

### Step 7 — Graph selected extracted entities/relations
Only if justified by real query needs.

---

## 12. Acceptance criteria

The retrieval layer is acceptable when:
- you can find relevant source material quickly
- canon docs outrank raw duplicate sludge by default
- source provenance stays visible
- chunk results are coherent enough to synthesize from
- retrieval answers real questions better than manual file hunting

The graph layer is acceptable when:
- it answers relationship questions better than retrieval alone
- it is built from extracted structure, not raw dumps
- provenance remains attached to relationships

---

## 13. Red-team warnings

This system fails when:
- indexing becomes another giant ingestion ritual with no useful queries
- retrieval returns noisy fragments with no source confidence
- canon docs and raw sources are treated as equal by default
- graph becomes a status symbol instead of a force multiplier
- the user spends more time preparing memory than using it

This system succeeds when:
- relevant sources become easy to find
- canon becomes easier to operate from
- ore files become usable without polluting active context
- graph later adds real relationship intelligence instead of hype

---

## 14. Final rule

Index first.
Retrieve second.
Graph third.
Automate fourth.

Any other order increases the risk of building expensive confusion.
