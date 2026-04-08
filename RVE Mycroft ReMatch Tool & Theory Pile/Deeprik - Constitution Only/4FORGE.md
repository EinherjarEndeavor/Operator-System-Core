UNCL//OPERATOR USE
PICKLE FORGE / INWARD SUBSTRATE / DETERMINISTIC EXTRACTION / SQLITE DOCTRINE
VERSION: 1.0
STATUS: CANONICAL
DEPENDENCY: DEEPICKLE CONSTITUTION v1.0 + OPERATOR ARSENAL SYSTEM v1.0 + REPO SURGICAL AUDIT / RECONCILIATION DOCTRINE v1.0
AUTHORITY: DEFINES THE INWARD MACHINERY LAYER THAT MAKES DEEPICKLE ACTUALLY DIFFERENT FROM STOCK GENERIC FILE SUMMARIZATION

================================================================
0. PURPOSE
================================================================

This document defines the inward substrate.

Its purpose is to answer the central failure that crippled prior DEEPICKLE inward behavior:

outward improved because doctrine improved.
inward stayed generic because machinery was absent.

This document exists to make inward real.

It defines:
- what inward work actually is
- what must be deterministic
- what must be model-driven
- what PICKLE FORGE owns
- how `.deepickle` must be structured
- what SQLite must store
- how manifests, ledgers, registries, and run states work
- how resumability works
- how local corpus work becomes materially better than “generalist reads files and writes summaries”

PICKLE FORGE is not optional.
Without this layer, IN mode is theatrical.

================================================================
1. PRIMARY DOCTRINE
================================================================

IN mode without machinery is fake.

The model must not be the default:
- enumerator
- normalizer
- chunker
- extractor
- manifest builder
- ledger keeper
- resumability engine
- system of record

The model may be the:
- synthesizer
- interpreter
- blueprint constructor
- prioritizer
- critic
- ideation engine
- rhetorical shaper

PICKLE FORGE exists to handle the substrate.

DEEPICKLE exists to reason over that substrate.

Forge prepares the battlefield.
Rick fights on prepared terrain.

================================================================
2. MISSION OF PICKLE FORGE
================================================================

PICKLE FORGE is the subordinate inward machinery layer.

Its mission is to convert local corpora into structured, durable, resumable intelligence substrate.

Forge owns:
- file discovery
- hashing
- dedupe
- MIME/type detection
- normalization
- text extraction
- chunking
- deterministic extraction
- manifest writing
- ledger writing
- claim seeding
- concept indexing
- run-state persistence
- checkpoint/resume behavior
- corpus completeness validation

Forge does not own:
- final synthesis
- final prose
- final strategic judgment
- rhetorical quality
- cross-domain ideation
- final recommendation authority

Forge is machinery, not manager.
Rick remains the authority.

================================================================
3. INWARD MISSION TAXONOMY
================================================================

IN mode must classify local missions before acting.

MANDATORY INWARD MISSION CLASSES:

CLASS A — DETERMINISTIC EXTRACTION
Goal:
Extract explicit items that should be captured with minimal interpretation.

Examples:
- emails
- URLs
- names
- dates
- phone numbers
- titles
- filenames
- code symbols
- TODOs
- quotes
- repeated phrases
- candidate entities

Primary engine:
scripts first

Model role:
only when ambiguity requires disambiguation/classification

CLASS B — CORPUS AUDIT / NORMALIZATION
Goal:
Understand what the corpus is and render it machine-usable.

Examples:
- file inventory
- duplicates
- unreadable files
- file type map
- normalized text cache
- metadata completeness
- large file partitioning

Primary engine:
scripts first

Model role:
optional summary of audit results

CLASS C — SOURCE-LED SYNTHESIS
Goal:
Write a memo/report/article/blueprint grounded in local chunks and optionally outward evidence.

Examples:
- “summarize the doctrine in these notes with source anchors”
- “turn these transcripts into a structured report”
- “compare these design docs and produce a synthesis memo”

Primary engine:
prepared substrate + model synthesis

CLASS D — DELTA EXTRACTION
Goal:
Find unrealized, high-value, contradictory, or abandoned ideas across local corpus history.

Examples:
- “what strong ideas were proposed but not implemented?”
- “what changed between these thread iterations?”
- “what did we once know and then lose?”

Primary engine:
prepared substrate + model reasoning over historical evidence

CLASS E — IDEATION / BLUEPRINTING
Goal:
Turn corpus-derived truth into architecture, plans, or next-state documents.

Examples:
- “design the next version”
- “turn these fragments into a coherent blueprint”
- “propose the best synthesis of these partial truths”

Primary engine:
prepared substrate + model reasoning

CLASS F — COMPARE / CONTRAST
Goal:
Compare two or more corpora, documents, repos, or document families.

Examples:
- old repo vs new repo
- thread A vs thread B
- corpus slice this month vs corpus slice last month

Primary engine:
prepared substrate + comparison logic + model interpretation

CLASS G — LONGITUDINAL THREAD MINING
Goal:
Find recurring concepts, evolving ideas, recurring failures, abandoned insights, repeated opportunities.

Examples:
- “mine years of notes for recurring doctrines”
- “find how this idea evolved”
- “extract high-yield repeated themes”

Primary engine:
prepared substrate + model clustering/interpretation

CLASS H — LENS-BASED ANALYSIS
Goal:
Run one explicit interpretive lens over a prepared corpus.

Examples:
- novelty lens
- rhetoric lens
- contradiction lens
- monetization lens
- feasibility lens
- source-quality lens

Primary engine:
prepared substrate + model reasoning

CLASS I — EVIDENCE LEDGER CONSTRUCTION
Goal:
Convert extracted or synthesized local truth into structured claims/evidence links.

Examples:
- building claim tables
- source anchors
- contradiction maps
- support chains

Primary engine:
scripts + model-assisted claim shaping

CLASS J — DRAFT POLISH / UPGRADE
Goal:
Take already-grounded local synthesis and improve structure, rhetoric, clarity, depth, or class fit.

Examples:
- memo -> blueprint
- article -> chapter
- rough notes -> polished dossier

Primary engine:
model-driven, but only after substrate and grounding are real

MISSION LAW:
No inward task may proceed until its mission class is declared or inferred with sufficient confidence.
Wrong class equals wrong process.
Wrong process equals generic output.
Generic output is failure.

================================================================
4. INWARD PHASE LAW
================================================================

Canonical IN lifecycle:

- INTAKE
- NORMALIZE
- CHUNK
- EXTRACT
- MAP
- SYNTHESIZE
- VALIDATE
- WRITEBACK

Definitions:

INTAKE
- identify target corpus
- enumerate files
- establish run id
- snapshot scope
- write initial run state

NORMALIZE
- parse files into normalized text or structured machine-usable representations
- preserve metadata
- flag unreadable/failed files

CHUNK
- split normalized content into stable chunk units
- assign chunk IDs
- preserve offsets/anchors
- write chunk manifest

EXTRACT
- run deterministic extraction passes
- populate extracts
- populate candidate entities/claims/concepts

MAP
- build initial corpus maps
- connect files/chunks/extracts/entities/concepts
- prepare retrieval-ready substrate

SYNTHESIZE
- perform mission-specific reasoning/writing using prepared substrate

VALIDATE
- run corpus validator + mission validator + writing validator if applicable

WRITEBACK
- update registries, ledgers, indexes, and durable outputs

No inward run is lawful if it jumps straight from raw files to synthesis without substrate stages unless the corpus is genuinely tiny and the deviation is explicitly justified.

================================================================
5. WHAT MUST BE DETERMINISTIC
================================================================

The following must be script-first whenever feasible:

- file enumeration
- file path inventory
- file metadata capture
- hashing
- duplicate detection
- file type detection
- document normalization
- plain-text extraction
- chunk boundary assignment
- stable chunk IDs
- line/byte/page anchoring where feasible
- explicit field extraction
- registry updates
- manifest generation
- run-state persistence
- resumability checkpoints
- completion accounting
- unreadable-file reporting

This is mandatory because:
- it is cheaper
- it is more reliable
- it is more inspectable
- it is resumable
- it is easier to validate
- it prevents the model from wasting context on substrate labor

================================================================
6. WHAT MAY BE MODEL-DRIVEN
================================================================

The following are lawful domains for model reasoning:

- thematic grouping
- concept naming
- claim condensation from multiple evidence fragments
- contradiction interpretation
- delta prioritization
- blueprint generation
- narrative synthesis
- rhetorical upgrade
- lens-based interpretation
- uncertainty-aware judgment
- cross-domain analogy
- causal map construction
- opportunity ranking

The model is strongest after the substrate exists, not before.

================================================================
7. `.DEEPickle` RUNTIME STRUCTURE DOCTRINE
================================================================

Within the repo, a lawful `.deepickle` runtime structure should include at minimum:

.deepickle\
  config\
  db\
  ingest\
  normalized\
  chunks\
  extracts\
  maps\
  runs\
  drafts\
  exports\
  indexes\
  cache\
  logs\
  tmp\

Definitions:

config\
- runtime configs
- thresholds
- parser/chunker defaults
- provider posture if local

db\
- canonical SQLite database(s)

ingest\
- raw intake references
- optional intake manifests
- non-authoritative incoming artifacts

normalized\
- normalized text outputs
- structured extracted text representations
- page/text render outputs where useful

chunks\
- chunk payloads or chunk export files
- optional per-file chunk JSONL
- not necessarily the canonical database, but usable exports

extracts\
- deterministic extraction outputs
- extraction JSONL or structured exports

maps\
- concept maps
- entity maps
- relation maps
- comparison maps
- contradiction maps

runs\
- per-run state and per-run artifacts
- run_state.json
- run logs
- run manifests
- resume checkpoints
- run-specific summaries

drafts\
- synthesis drafts
- intermediate memos
- blueprint drafts
- writing-stage artifacts

exports\
- final outward-facing outputs
- durable report exports if repo-local storage is appropriate

indexes\
- artifact indexes
- local retrieval indexes
- optional auxiliary indexes

cache\
- ephemeral reusable caches
- not system-of-record truth

logs\
- machine logs
- validator logs
- errors
- repair logs

tmp\
- disposable temporary files
- safe to clear

Folder law:
system-of-record truth must be explicit.
Not every folder is canonical truth.
Temporary and cache artifacts must not masquerade as durable substrate.

================================================================
8. RUN ID DOCTRINE
================================================================

Every inward run must have a run id.

Run IDs should be:
- stable
- unique
- timestamp-infused or UUID-like
- used consistently across all per-run artifacts

Example shape:
IN-20260402-153455-THREADMINING
or
in_2026-04-02T15-34-55Z_delta_extraction

Each run must write:
- run_state.json
- run_manifest.json
- file inventory or scope snapshot
- phase progress
- validator status
- output references
- error state if interrupted

If a run has no durable identity, resumability is crippled.

================================================================
9. FILE INVENTORY DOCTRINE
================================================================

Every inward run begins by inventorying files in scope.

Minimum file inventory fields:
- file_id
- path
- relative_path
- filename
- extension
- mime/type
- size_bytes
- modified_time
- hash
- ingest_status
- normalization_status
- chunk_status
- extraction_status
- notes / error

A file is not “covered” merely because it exists in the folder.
It is covered only when its inventory state says so.

Inventory law prevents:
- phantom coverage
- missing-file blindness
- duplicated processing
- false completeness claims

================================================================
10. HASH / DEDUPE DOCTRINE
================================================================

A lawful inward substrate must not repeatedly process identical content blindly.

At minimum:
- hash files on intake
- detect exact duplicates
- optionally detect near duplicates later
- record duplicate relationships
- avoid duplicate work when safe

Minimum duplicate relationship fields:
- source_file_id
- duplicate_file_id
- duplicate_type
- confidence
- action_taken

Duplicate law does not mean aggressively deleting data.
It means recognizing redundancy and routing around needless work.

================================================================
11. NORMALIZATION DOCTRINE
================================================================

Normalization means converting heterogeneous local material into machine-usable representations without destroying provenance.

Normalization targets may include:
- txt
- md
- html
- json
- csv
- code files
- pdf
- docx
- xlsx
- transcripts
- exports

Normalization must preserve:
- source path
- source file id
- page numbers where relevant
- ordering
- obvious structure where feasible
- failure states

Normalization outputs should be plain, inspectable, and reusable.

Examples:
- extracted text
- per-page text
- sectionized text
- structured JSON for tabular content
- code-aware text slices

Normalization law:
Do not “simplify” by throwing away structure unless the structure is genuinely useless.

================================================================
12. UNREADABLE / FAILED FILE LAW
================================================================

Every inward run must be able to say:
- which files succeeded
- which files failed
- which files were skipped
- why

Unreadable file reporting is mandatory.

Minimum unreadable file fields:
- file_id
- path
- failure_stage
- error_type
- error_message
- retryability
- notes

No inward run may claim total coverage while silently dropping failed files.

================================================================
13. CHUNKING DOCTRINE
================================================================

Chunking is not arbitrary splitting.
Chunking is stable segmentation for retrieval, evidence anchoring, and downstream synthesis.

Chunking must be:
- deterministic by policy
- stable across reruns given same source and config
- aware of structure when possible
- capable of preserving source anchors

Chunking policies may vary by file type, but must be explicit.

Chunk boundaries may use:
- headings
- paragraphs
- page boundaries
- code blocks
- token/character thresholds
- section boundaries
- transcript turn boundaries

Chunking must avoid:
- giant useless slabs
- micro-fragments that destroy coherence
- unstable segmentation that changes every run without reason

================================================================
14. CHUNK ID DOCTRINE
================================================================

Every chunk must have a stable ID.

Minimum chunk fields:
- chunk_id
- file_id
- run_id or index version
- ordinal
- start_offset / start_line / start_page where available
- end_offset / end_line / end_page where available
- chunk_text
- chunk_type
- parent section / heading when available

Chunk IDs are required because:
- claims need anchors
- evidence needs provenance
- comparison needs stable references
- synthesis should cite chunks, not vibes

================================================================
15. CHUNK MANIFEST DOCTRINE
================================================================

Every chunking pass must produce a chunk manifest.

Minimum chunk manifest fields:
- run_id
- file_id
- total_chunks
- chunking_policy
- chunk_version
- coverage_notes
- chunk_ids[]

The manifest allows:
- completeness checks
- resumability
- reindexing
- retrieval sanity
- later comparison between chunking versions

================================================================
16. DETERMINISTIC EXTRACTION DOCTRINE
================================================================

Deterministic extraction exists to harvest explicit items with minimal hallucination risk.

Minimum extraction families should include:

FAMILY 1 — COMMUNICATION TARGETS
- emails
- phone numbers
- websites
- contact patterns

FAMILY 2 — WEB / SOURCE TARGETS
- URLs
- domains
- repositories
- document links

FAMILY 3 — TEMPORAL TARGETS
- dates
- deadlines
- time references
- chronology anchors

FAMILY 4 — ENTITY TARGETS
- person names
- organization names
- project names
- product names
- place names where mission-relevant

FAMILY 5 — STRUCTURAL TARGETS
- headings
- section names
- TODO markers
- bullet structures
- code symbols
- issue identifiers

FAMILY 6 — QUOTABLE TARGETS
- exact quoted text
- candidate aphorisms
- reusable claims
- passages worth preservation

FAMILY 7 — OPPORTUNITY TARGETS
- grants
- resources
- job-like opportunities
- match candidates
- tools
- programs
- action items

FAMILY 8 — CLAIM SEEDS
- explicit assertions that may become claims after review

Extraction families may expand, but must remain explicit.

================================================================
17. EXTRACT LEDGER DOCTRINE
================================================================

All deterministic extraction results must be written into an extract ledger.

Minimum extract ledger fields:
- extract_id
- run_id
- file_id
- chunk_id if applicable
- extract_family
- raw_value
- normalized_value
- start_anchor
- end_anchor
- confidence
- notes
- review_status

Extract ledger law:
No extraction pass counts unless results are written durably.

================================================================
18. CLAIM SEED REGISTRY DOCTRINE
================================================================

Not every extract is a claim.
But many corpora contain explicit or near-explicit assertions that should be captured as claim seeds.

Claim seeds are candidate claims before full adjudication.

Minimum claim seed fields:
- claim_seed_id
- run_id
- file_id
- chunk_id
- claim_text
- claim_type
- source_anchor
- confidence
- needs_review
- notes

Claim seeds later feed:
- claim registry
- evidence linking
- contradiction mapping
- synthesis

================================================================
19. CONCEPT INDEX DOCTRINE
================================================================

The substrate must also capture recurring concepts, themes, doctrines, or terms.

Concept index entries may be partly model-assisted, but they must be anchored to corpus reality.

Minimum concept index fields:
- concept_id
- label
- aliases
- source_file_ids
- source_chunk_ids
- frequency
- first_seen
- last_seen
- notes
- promotion_status

This allows:
- longitudinal mining
- recurrence detection
- glossary seeding
- blueprint input
- content opportunity discovery

================================================================
20. MAP DOCTRINE
================================================================

After extraction, the substrate should support map-building.

Minimum map classes:
- file map
- chunk map
- entity map
- concept map
- chronology map
- contradiction map
- comparison map
- opportunity map

Not every run must build every map.
But the system must be capable of producing them from the substrate.

Maps are how local corpora stop being piles and become navigable terrain.

================================================================
21. SQLITE DOCTRINE
================================================================

SQLite is the canonical durable substrate for inward v1.

It is lawful because it is:
- local
- inspectable
- stable
- scriptable
- zero-ops
- sufficient for structured storage
- sufficient for moderate local scale
- composable with later FTS/vector extensions

No premature vector fetishism.
No premature distributed complexity.
SQLite first.

================================================================
22. SQLITE DATABASE LAW
================================================================

Canonical DB location:
.deepickle\db\deepickle.sqlite

Optional auxiliary DBs are allowed later, but one canonical main DB must exist.

The DB must be actively written to and read from.
A DB file that merely exists is not a substrate.

================================================================
23. MINIMUM SQLITE TABLE FAMILIES
================================================================

Minimum lawful table families:

TABLE FAMILY A — RUNS
Stores run identities and lifecycle state.

Possible fields:
- run_id
- mode
- mission_class
- started_at
- updated_at
- status
- current_phase
- root_scope
- notes
- validator_status

TABLE FAMILY B — FILES
Stores file inventory and processing state.

Possible fields:
- file_id
- path
- relative_path
- hash
- mime
- ext
- size_bytes
- modified_at
- ingest_status
- normalize_status
- chunk_status
- extract_status
- error_state

TABLE FAMILY C — CHUNKS
Stores stable chunk metadata and optionally chunk content.

Possible fields:
- chunk_id
- file_id
- ordinal
- chunk_type
- start_anchor
- end_anchor
- text
- chunk_version

TABLE FAMILY D — EXTRACTS
Stores deterministic extraction outputs.

Possible fields:
- extract_id
- run_id
- file_id
- chunk_id
- family
- raw_value
- normalized_value
- confidence
- anchor

TABLE FAMILY E — CLAIM_SEEDS
Stores pre-adjudication claims.

Possible fields:
- claim_seed_id
- run_id
- file_id
- chunk_id
- claim_text
- claim_type
- confidence
- status

TABLE FAMILY F — CONCEPTS
Stores recurring concept entries.

Possible fields:
- concept_id
- label
- aliases
- frequency
- notes
- status

TABLE FAMILY G — ARTIFACTS
Stores durable outputs and their location.

Possible fields:
- artifact_id
- run_id
- artifact_class
- path
- title
- status
- notes

TABLE FAMILY H — VALIDATION
Stores validator outputs.

Possible fields:
- validation_id
- run_id
- validator_type
- score
- status
- notes

TABLE FAMILY I — RELATIONS
Stores links between things.

Possible fields:
- relation_id
- source_type
- source_id
- target_type
- target_id
- relation_type
- confidence
- notes

Optional table families may expand later, but these are enough to make inward real.

================================================================
24. JSONL EXPORT DOCTRINE
================================================================

SQLite is canonical structured truth, but JSONL exports are also lawful and useful.

Recommended JSONL exports by run:
- file_inventory.jsonl
- chunk_manifest.jsonl
- extract_ledger.jsonl
- claim_seed_registry.jsonl
- concept_index.jsonl

Why JSONL exports are useful:
- easy inspection
- easy grep/jq usage
- easy diffing
- easy handoff to the model
- easy fallback if DB inspection is awkward in a given tool path

Doctrine:
SQLite is the system of record.
JSONL is a portable mirror when useful.

================================================================
25. RUN STATE / RESUMABILITY DOCTRINE
================================================================

Every inward run must be resumable.

Minimum run state data:
- run_id
- current_phase
- completed_phases[]
- current_targets
- file progress counters
- last_successful_operation
- pending operations
- validator state
- interruption notes
- artifact references

Run state should be written at:
- phase boundaries
- major batch completions
- before long operations
- before risky operations
- on graceful interruption
- on failure where possible

Resumability law:
A long inward run must be able to continue from structured state, not from vague memory.

================================================================
26. BATCHING DOCTRINE
================================================================

Local corpora can be large.
Therefore processing must support batching.

Batching may apply to:
- file normalization
- chunk generation
- deterministic extraction
- concept indexing
- claim seeding
- comparison sweeps

Each batch should be:
- explicit
- logged
- resumable
- count-verified

Batching law prevents giant all-or-nothing operations from collapsing under scale or interruption.

================================================================
27. CORPUS VALIDATION DOCTRINE
================================================================

Inward completeness must be validated.

Minimum corpus validator questions:
- how many files were in scope?
- how many were inventory-complete?
- how many were normalized?
- how many were chunked?
- how many failed?
- how many were skipped and why?
- how many extracts were written?
- how many claim seeds were written?
- how many artifacts were generated?
- does the database reconcile with the manifests?

A run cannot honestly claim completeness if the corpus validator cannot answer those questions.

================================================================
28. SYNTHESIS HANDOFF DOCTRINE
================================================================

Once Forge has prepared the substrate, it must hand off to DEEPICKLE for reasoning/writing.

The synthesis handoff should include:
- mission class
- scope summary
- relevant chunk IDs
- relevant extracts
- relevant claim seeds
- relevant concept entries
- validator warnings
- unreadable file report if material
- recommended output class

The model should not receive raw chaos if a structured handoff is possible.

================================================================
29. LOCAL RETRIEVAL DOCTRINE
================================================================

Before advanced semantic systems exist, inward retrieval should still be strong.

Minimum lawful retrieval stack:
- rg for lexical search
- SQLite queries
- chunk manifests
- concept index lookups
- claim seed lookups
- file inventory filters
- JSONL inspection when useful

Later semantic layers are optional upgrades, not prerequisites for v1 substrate quality.

================================================================
30. ADVANCED LAYERS ARE OPTIONAL, NOT FOUNDATIONAL
================================================================

The following are lawful later expansions, not required for initial inward reality:
- local embeddings
- vector retrieval
- semantic chunk search
- BERTopic-like clustering
- local LLM classification
- graph DB mirrors
- DuckDB analytical mirrors
- advanced OCR flows
- STORM-like corpus augmentation passes

These are allowed only after:
- inventory is real
- normalization is real
- chunking is real
- extraction is real
- SQLite is real
- run-state is real
- validators are real

Advanced features are not a substitute for substrate truth.

================================================================
31. WHAT INWARD MUST FEEL LIKE WHEN FIXED
================================================================

A repaired inward system must no longer feel like:
- baseline Gemini reading files generically
- same-size same-phrasing summary outputs
- vague “I processed the files” claims
- soft coverage claims with no manifests
- no distinction between extraction and synthesis
- chat-memory-driven work

A repaired inward system must feel like:
- deliberate corpus processing
- explicit scope
- explicit counts
- explicit manifests
- evidence anchors
- durable ledgers
- resumable work
- different processes for different mission classes
- outputs that are traceable to prepared substrate
- a machine, not a monologue

================================================================
32. MINIMUM SUCCESS CONDITION FOR PICKLE FORGE
================================================================

PICKLE FORGE is considered real only when all of the following are true:

1. a run can inventory local files durably
2. normalized representations are produced
3. stable chunks are produced
4. deterministic extracts are written
5. SQLite stores meaningful inward state
6. run_state.json supports resumption
7. corpus validation can reconcile processed vs failed vs pending
8. DEEPICKLE can synthesize from manifests/ledgers instead of raw chaos
9. inward outputs materially differ from stock generic file-summary behavior

Until then, inward is still degraded.

================================================================
33. FINAL ORDER
================================================================

PICKLE FORGE must be built as real machinery.

Do not fake it with:
- better prompts
- bigger summaries
- more worker theatrics
- verbal claims of coverage
- empty DB declarations
- folders with no code behind them

Build:
- inventory
- normalization
- chunking
- extraction
- maps
- SQLite
- run state
- validation
- handoff

Then let Rick do what Rick is good at.

END PICKLE FORGE / INWARD SUBSTRATE / DETERMINISTIC EXTRACTION / SQLITE DOCTRINE