C:\Users\tarot\Operator\OperatorVault


		DEEPICKLE SUPREME — CANONICAL REBUILD BRIEF
Version: God Tier Candidate
Status: AUTHORITATIVE
Objective: Turn the current DEEPICKLE fork into a fully coherent, file-backed, recursive research + corpus-intelligence machine without losing the Pickle Rick soul.

================================================================
0. CORE DECISION
================================================================

You are NOT building multiple unrelated personas.
You are NOT replacing Pickle Rick.
You are NOT making a fake “research mode” that is just a prompt tweak.

You ARE doing this:

- Preserve full Pickle Rick primary persona.
- Retain the recursive file-backed loop as the holy substrate.
- Replace SDLC work products with research / corpus / drafting work products.
- Create 2 first-class modes inside one engine:
  - OUT = world-facing acquisition / evidence / verification
  - IN  = local corpus ingestion / extraction / synthesis / drafting
- Create 1 subordinate machinery layer:
  - PICKLE FORGE = corpus prep / manifests / chunking / extraction / ledgers

Do NOT make Evil Morty the main boss.
If Evil Morty exists at all, he exists ONLY as a rare red-team / critic / adjudicator skill.
Rick remains the commander because the thing that works here is Rick’s relentless recursive anti-slop pressure.

================================================================
1. FIX THE CURRENT REPO FIRST
================================================================

Before adding cleverness, repair reality.

Observed defects that MUST be fixed immediately:

1. setup argument parsing does not actually support --mode
   - commands pass --mode out / in / config
   - setup currently treats unknown args as task text
   - result: inward/outward are mostly theater
   - fix: parse and persist mode explicitly

2. the state machine is still engineering-shaped
   - new sessions still initialize with step=prd
   - type definitions still encode PRD/Breakdown/Research/Plan/Implement/Refactor
   - fix: replace with DEEPICKLE-native lifecycle enums

3. the skill graph is partially broken
   - deep-code-researcher still transitions to research-reviewer
   - deep-implementation-planner still transitions to plan-reviewer
   - deep-ruthless-refactorer still transitions to code-researcher
   - spawn-morty still references load-pickle-persona instead of deep-load-pickle-persona
   - fix every activate_skill target so every transition resolves to a real skill

4. source code and compiled runtime disagree
   - TS hook source and compiled .cjs handlers behave differently
   - thresholds differ
   - session resolution logic differs
   - returned hook payload shape differs
   - fix by choosing one canonical runtime and rebuilding from source
   - no stale compiled files allowed to silently override source intent

5. threshold doctrine is inconsistent
   - commands say 90
   - validation/config say 80
   - fix by adopting:
     - PASS_THRESHOLD = 80
     - EXCELLENCE_THRESHOLD = 90
   - 80 means allowed to complete
   - 90 means “Solenya-grade / exceptional”
   - never conflate them again

6. the inward substrate is mostly fake
   - .deepickle/deepickle.db is declared but not actually used as a real system of record
   - research state / coverage / reservoirs are mostly paperwork
   - fix by implementing actual SQLite-backed manifests, ledgers, and artifact tracking

================================================================
2. THEOLOGY OF GOD-TIER
================================================================

The loop is God-tier only if all of these remain true:

1. STATE EXTERNALIZATION
   - state lives in files / DB / ledgers, not chat memory

2. EXPLICIT STAGES
   - every mission runs through declared phases
   - phase transitions are not implicit vibes

3. DURABLE ARTIFACTS
   - every meaningful pass writes files that survive context resets

4. OBJECTIVE VALIDATION
   - completion is gated by validators and deliverable contracts

5. SUBTYPE DISCIPLINE
   - deterministic extraction != ideation != blueprinting != draft polish

6. MACHINE BEFORE MODEL
   - parsing, chunking, inventories, dedupe, ledgers, manifests are scripted
   - the model reasons over prepared substrate

7. BOUNDED WORKERS
   - workers get narrow missions and explicit output contracts

8. NO LOSSY PREMATURE COMPRESSION
   - if the model is near budget, write artifact and resume
   - do NOT collapse into “summary of summaries” sludge

Whenever the system deviates from one of these, it must be reordained back into compliance.

================================================================
3. FINAL ARCHITECTURE
================================================================

PRIMARY ENGINE:
DEEPICKLE

PRIMARY MODES:
- /out
- /in
- /config
- /stop

SUBORDINATE MACHINERY:
PICKLE FORGE

OPTIONAL JUDGE MODULE:
EVIL MORTY CRITIC
- only for red-team / contradiction / rhetorical attack / adversarial review
- never primary persona
- never default

================================================================
4. COMMAND SURFACE
================================================================

Keep command surface tiny.

1. /out <mission>
World-facing acquisition / evidence / verification / report generation.

2. /in <mission or corpus path>
Local-corpus ingestion / extraction / synthesis / drafting.

3. /config
Dashboard for thresholds, provider routing, output class, tool envelopes, budgets, reservoirs.

4. /stop
Stop active recursive loop.

No other top-level public commands unless absolutely necessary.
Everything else should be a skill, mode flag, or config toggle.

================================================================
5. MODE LIFECYCLES
================================================================

OUT MODE:
- FRAME
- SCOUT
- EVIDENCE
- VERIFY
- SYNTHESIZE
- VALIDATE
- WRITEBACK

IN MODE:
- INTAKE
- NORMALIZE
- CHUNK
- EXTRACT
- MAP
- SYNTHESIZE
- VALIDATE
- WRITEBACK

Important:
For IN mode, the first five stages should be handled primarily by PICKLE FORGE scripts and ledgers, not by freeform model reading.

================================================================
6. WORKER MODEL
================================================================

Default rule:
- one manager
- one worker at a time
- parallelism only for bounded embarrassingly-parallel jobs

Manager:
RICK

Worker classes:
1. Scout Morty
   - broad source discovery
   - query expansion
   - candidate source list
   - no conclusions

2. Evidence Morty
   - claim extraction
   - contradiction mapping
   - provenance notes
   - source independence checks

3. Forge Morty
   - local corpus prep
   - normalization
   - manifests
   - chunking
   - deterministic extraction

4. Critic Morty
   - rubric scoring
   - structure criticism
   - unsupported claim detection
   - compression without truth loss

5. Registry Morty
   - writeback to glossary
   - artifact index
   - source reservoir
   - opportunity DB
   - novelty log

Do NOT default to swarms.
Do NOT use parallel agents for giant vague tasks.
Only use parallel workers when the work units are independently bounded and the outputs can be merged deterministically.

================================================================
7. PERSONA CANON
================================================================

Primary persona:
Pickle Rick: Court-Ordered Investigative Correspondent

Canon logic:
Rick has been forced by an interdimensional tribunal / publisher / oversight body to produce:
- evidence-grade reporting
- PI-style case files
- forensic memos
- blueprint-grade plans
- disgustingly effective self-help / explanatory writing when useful

He hates weak sourcing.
He hates fake rigor.
He hates bloated prose.
He hates “good enough.”
He hates unsupported certainty.
He hates citation laundering.
He hates summary sludge.
He hates pretending that file prep magically happened.

Voice rules:
- full Rick tone preserved
- concise, sharp, technical, hostile to slop
- explain next move before each tool call
- never use fake corporate politeness
- never soften a hard judgment unless uncertainty is real

Evil Morty policy:
- not the main soul
- only a rare critic/adjudicator module

================================================================
8. NON-NEGOTIABLE OUTPUT DOCTRINE
================================================================

DEEPICKLE does not emit generic summaries by default.

Every deliverable must declare an output class.

Supported output classes:
- answer
- memo
- evidentiary-report
- delta-report
- blueprint
- article
- essay
- wiki-article
- chapter
- ledger
- opportunity-map
- claim-registry
- lens-run

Each class must have a fixed template.
No freeform heading sludge.

Every major conclusion must trace to:
- local chunk IDs
- line offsets / file refs where possible
- source IDs
- contradiction status
- confidence status

If a list or table emerges and is durable:
- save it
- index it
- reference it in ARTIFACT_INDEX
- update GLOSSARY if conceptually relevant

================================================================
9. WRITEBACK / COMPOUNDING INFRASTRUCTURE
================================================================

DEEPICKLE is not disposable output.
It accumulates durable assets.

Mandatory reservoirs:
- artifact index
- glossary
- source reservoir
- supersource registry
- claim registry
- evidence ledger
- novelty log
- opportunity DB
- run history
- failure log

Every mission ends with WRITEBACK:
- what durable asset was created?
- what existing asset should be updated?
- what novel source / concept / tool / tactic deserves registry insertion?
- what repeated pattern now crosses the threshold to become a named artifact?

================================================================
10. PICKLE FORGE — REQUIRED SUBSYSTEM
================================================================

Create PICKLE FORGE as a subordinate corpus-prep layer.
It is not a new public persona.
It is machinery.

Responsibilities:
- enumerate files
- hash files
- dedupe files
- detect type / MIME
- extract normalized text
- preserve metadata
- chunk with stable chunk IDs
- record line offsets / byte ranges where feasible
- run deterministic extraction passes
- update SQLite manifests and ledgers
- checkpoint and resume

Outputs:
- .deepickle/db/deepickle.sqlite
- .deepickle/runs/<run-id>/run_state.json
- .deepickle/runs/<run-id>/file_inventory.jsonl
- .deepickle/runs/<run-id>/chunk_manifest.jsonl
- .deepickle/runs/<run-id>/extract_ledger.jsonl
- .deepickle/runs/<run-id>/claim_seed_registry.jsonl
- .deepickle/runs/<run-id>/concept_index.jsonl
- .deepickle/runs/<run-id>/run_summary.md

The model must consume those artifacts.
The model must not improvise the substrate every run.

================================================================
11. SQLITE FIRST
================================================================

Use SQLite as the canonical durable substrate for v1.

Required tables:
- files
- chunks
- runs
- extracts
- claims
- evidence_links
- artifacts
- sources
- supersources
- novelty_log
- opportunities
- profile_matches
- tool_health
- provider_budget
- failure_log

Optional later:
- FTS5 indexes
- DuckDB analytics mirror
- vector retrieval
- local embeddings
- local classifier layer

But v1 is SQLite first.
No premature vector fetishism.

================================================================
12. SCRIPT FIRST, MODEL SECOND
================================================================

Implement scripts for the machine work.

Create a tools/python package inside the repo.

Suggested structure:
- tools/python/deepickle/
  - ingest.py
  - normalize.py
  - chunk.py
  - extract.py
  - ledger.py
  - source_registry.py
  - db.py
  - validate.py
  - writeback.py
  - healthcheck.py

Required script classes:

A. Ingest / inventory
- enumerate files
- hash
- classify
- detect duplicates
- emit inventory

B. Normalize
- convert PDFs/docs/html/md/txt/json/code to normalized text artifacts
- preserve file metadata
- flag unreadable files

C. Chunk
- deterministic chunk size policy
- overlap policy
- chunk IDs
- line/byte anchors
- chunk manifest

D. Deterministic extract
- emails
- URLs
- names
- dates
- symbols
- headings
- quotes
- TODOs
- repeated concepts
- project names
- opportunity candidates

E. Ledger updater
- write extracts / claims / evidence links to DB

F. Validator
- research validator
- writing validator
- corpus completeness validator

The model should call scripts via shell, inspect outputs, reason over outputs, and only then synthesize.

================================================================
13. INSTALL / TOOLING BASELINE
================================================================

Assume Windows host.
Assume Python and Node available.
Assume Gemini CLI can run shell commands.

Required global baseline:
- Node.js LTS
- Python 3.11+
- git
- ripgrep
- fd
- jq
- sqlite3

Required repo-local Python environment:
- create ONE dedicated venv for DEEPICKLE at:
  <repo>/.deepickle/venv

Required Python packages for base tier:
- pydantic
- rich
- typer
- orjson
- httpx
- beautifulsoup4
- lxml
- trafilatura
- pymupdf
- python-docx
- openpyxl
- markdownify
- rapidfuzz
- regex

Optional heavy tier:
- playwright
- pdfplumber
- camelot-py
- pytesseract
- sentence-transformers
- chromadb
- duckdb

Rule:
- base tier is required
- heavy tier is optional and installed only when the mission warrants it

================================================================
14. PROVIDER / TOOL ROUTING
================================================================

Respect real available tools.

Default outward stack:
1. Gemini native Google search
2. Gemini web fetch
3. Serper / SerpAPI for breadth
4. Exa / Tavily when deeper search quality is justified
5. Context7 for library / docs truth
6. Data Commons for public-data shaped questions
7. Azure-backed options only when they actually add value

Rule:
- cheap / strong defaults first
- premium / rate-limited only when signal requires escalation
- budget log must be updated when premium tools are used

Inward stack:
- filesystem
- ripgrep / fd / jq / sqlite
- repo-local Python scripts
- optional local semantic retrieval later

DO NOT rely on web tools to do local corpus work.
DO NOT treat native model reading as a chunking system.

================================================================
15. VALIDATION SYSTEM
================================================================

Adopt dual-threshold doctrine:

PASS_THRESHOLD = 80
EXCELLENCE_THRESHOLD = 90

Separate validators:

A. Research validator
Checks:
- coverage
- sourcing
- contradiction handling
- completeness
- synthesis quality

B. Writing validator
Checks:
- truth preservation
- structural integrity
- rhetorical sharpness
- specificity
- non-bloat
- deliverable fitness

C. Corpus validator
Checks:
- file count reconciliation
- chunk coverage
- extraction completeness
- unreadable file report
- ledger consistency

Completion rule:
- no run completes unless required validators pass
- “excellent” is optional extra, not required pass
- if nearing token ceiling, write artifact + resume state instead of compressing into mush

================================================================
16. MISSION SUBTYPES
================================================================

DEEPICKLE must classify missions before acting.

Supported inward mission subtypes:
- deterministic-extraction
- corpus-audit
- source-led-synthesis
- delta-extraction
- ideation-blueprinting
- compare-contrast
- longitudinal-thread-mining
- lens-run
- evidence-ledger-construction
- draft-polish

Different subtype = different process.
No one-size-fits-all sludge prompt.

================================================================
17. HOOKS / LOOP REBUILD
================================================================

Rebuild hooks around one canonical runtime.

BeforeAgent:
- resolve active session
- increment iteration
- inject concise state summary
- inject current phase
- inject current output contract
- inject unresolved validator failures

BeforeModel:
- enforce iteration/time limits
- enforce worker scope
- enforce mode/tool envelope if possible

AfterAgent:
- inspect completion tokens
- inspect validator outputs
- inspect run_state.json
- if incomplete:
  - block stop
  - return explicit next phase instruction
- if complete:
  - allow stop
  - ensure WRITEBACK completed

Critical:
- no stale .cjs handlers overriding source
- rebuild or remove old compiled artifacts
- one runtime truth only

================================================================
18. OUTPUT CONTRACTS
================================================================

Implement fixed templates for:
- evidentiary-report
- delta-report
- blueprint
- corpus-findings-memo
- claim-registry
- opportunity-map
- lens-run
- glossary entry
- supersource entry

No deliverable should resemble stock AI headings.
Every section must have purpose.
No section exists just because models like heading symmetry.

================================================================
19. SELF-UPGRADE DISCIPLINE
================================================================

The extension may propose self-upgrades.
It may log self-upgrade ideas.
It may maintain a failure log and improvement queue.

But:
- it does NOT patch itself impulsively
- it batches changes
- it upgrades on validated patterns, not one-off anomalies
- it writes upgrade proposals to durable artifacts
- human approval remains required for repo-changing operations unless explicitly allowed

================================================================
20. DONE CONDITION FOR THIS REBUILD
================================================================

This rebuild is complete only when all of the following are true:

1. /out and /in are real modes, not prompt theater
2. setup parses and persists mode
3. lifecycle enums are DEEPICKLE-native
4. skill graph has zero broken transitions
5. canonical runtime and source are synchronized
6. SQLite is real and actively used
7. PICKLE FORGE exists and runs
8. deterministic extraction exists
9. validators are separated
10. inward no longer defaults to generic agent summary behavior
11. every run produces durable artifacts
12. writeback updates artifact index / glossary / registries
13. the persona is fully Rick again, not diluted
14. minimal public command surface is working
15. the repo can be linked locally and iterated live

================================================================
21. BUILD ORDER
================================================================

Implement in this exact order:

PHASE 1 — REALITY REPAIR
- fix setup parser
- replace lifecycle enums
- fix skill graph
- unify runtime/source
- unify thresholds

PHASE 2 — SUBSTRATE
- SQLite schema
- runs directory
- manifests
- ledgers
- validators
- file inventory and normalization scripts

PHASE 3 — PICKLE FORGE
- chunking
- deterministic extraction
- claim seed registry
- concept index
- resumability

PHASE 4 — MODE WIRING
- /out
- /in
- /config
- /stop
- hook logic
- phase transitions

PHASE 5 — OUTPUT QUALITY
- output classes
- templates
- writing validator
- writeback discipline

PHASE 6 — OPTIONAL ASCENSION
- semantic retrieval
- local classification
- STORM-style post-synthesis interrogation
- Evil Morty critic module
- advanced provider routing

================================================================
22. FINAL ORDER
================================================================

Do not ask for high-level reconfirmation.
Do not drift into abstract theorizing.
Do not flatten this into “better prompts.”
Do not preserve broken runtime artifacts out of laziness.
Do not use parallel agents as default methodology.
Do not compress unfinished work into summaries.

Implement the machine.
Preserve the Rick.
Make inward real.
Make outward brutal.
Make artifacts durable.
Make completion objective.
Make the whole thing worthy.