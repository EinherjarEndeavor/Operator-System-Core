UNCL//OPERATOR USE
DEEPICKLE REPO SURGICAL AUDIT / RECONCILIATION DOCTRINE
VERSION: 1.0
STATUS: CANONICAL
DEPENDENCY: DEEPICKLE CONSTITUTION v1.0 + OPERATOR ARSENAL SYSTEM v1.0
AUTHORITY: DEFINES HOW THE CURRENT REPO MUST BE AUDITED, CLASSIFIED, RECONCILED, AND REPAIRED BEFORE OR DURING IMPLEMENTATION

================================================================
0. PURPOSE
================================================================

This document defines how to inspect the current DEEPICKLE repository without lying, without drifting into hype, and without confusing declared doctrine with actual runtime behavior.

Its job is to prevent:
- believing docs over code
- believing source over runtime
- believing commands over actual parser behavior
- believing scaffolding over machinery
- believing vibes over inspection
- attempting major expansion on a broken substrate
- patching symptoms while preserving structural falsehood

This is the surgical map doctrine.

The goal is not to produce an audit that sounds smart.
The goal is to determine, file by file and behavior by behavior:
- what is real
- what is partial
- what is fake
- what is mislabeled
- what is inherited from old Pickle Rick
- what must be fixed now
- what may be deferred
- what must not be allowed to survive the rebuild

================================================================
1. CORE AUDIT LAW
================================================================

The repository must be judged by runtime truth, not by self-description.

Priority of truth sources:

TIER 1 — OBSERVED EXECUTABLE BEHAVIOR
What actually happens when commands, hooks, scripts, and flows run.

TIER 2 — EFFECTIVE RUNTIME FILES
Compiled files, invoked scripts, hook handlers, actual command entrypoints, actual parser logic.

TIER 3 — SOURCE OF INTENDED RUNTIME
TypeScript/JS source intended to produce runtime behavior.

TIER 4 — CONFIG / STATE / ARTIFACT DECLARATIONS
JSON, TOML, DB declarations, scaffold files, templates, example configs.

TIER 5 — DOCS / README / GEMINI CONTEXT
README, extension docs, comments, plans, “this is supposed to do X” text.

Audit Law:
If Tier 5 says a capability exists and Tier 1–3 say it does not, the capability does not exist.
If Tier 3 says a capability exists and Tier 2 disagrees, runtime is the truth and source is stale or unbuilt.
If Tier 4 declares a substrate but no code writes to it, the substrate is aspirational.
If Tier 1 behaves generically despite DEEPICKLE doctrine, the repo is still functionally generic.

================================================================
2. AUDIT OBJECTIVES
================================================================

The audit must answer five questions.

QUESTION 1:
What does this repo actually do today?

QUESTION 2:
Which parts are genuine DEEPICKLE implementation and which parts are inherited Pickle Rick behavior still wearing the old soul-shape?

QUESTION 3:
Which features are declared but not materially implemented?

QUESTION 4:
Which mismatches between source, runtime, commands, docs, and config create false identity?

QUESTION 5:
What must be repaired in what order so the rebuild hardens instead of compounding confusion?

================================================================
3. AUDIT OUTPUT FORMAT
================================================================

All audit findings must be classified into one of these buckets.

BUCKET A — GENUINELY IMPLEMENTED
The behavior exists, executes, and materially matches doctrine.

BUCKET B — PARTIALLY IMPLEMENTED
There is real code or flow, but it is incomplete, inconsistent, weakly wired, or missing necessary downstream machinery.

BUCKET C — DECLARED BUT FAKE
Docs/config/scaffolds claim it exists, but there is no real machinery or runtime behavior behind it.

BUCKET D — MISLABELED
It exists, but it is called or described as something it is not.

BUCKET E — STALE INHERITANCE
Old Pickle Rick behavior remains and is still shaping the repo in ways that no longer match the intended identity.

BUCKET F — RUNTIME/SOURCE DIVERGENCE
Source says one thing, effective runtime does another.

BUCKET G — MUST FIX NOW
Defects that block the rebuild or poison everything downstream.

BUCKET H — MAY DEFER
Defects that are real but not foundational blockers.

Audit deliverables must be explicit enough that another operator could fix the repo from the audit alone.

================================================================
4. AUDIT DOMAIN MAP
================================================================

The audit must cover these domains in order.

DOMAIN 1 — COMMAND SURFACE
Inspect:
- command definitions
- slash commands
- command docs/help
- command entrypoints
- argument parsing
- help text vs actual accepted args

Questions:
- what commands actually exist?
- what flags are actually parsed?
- what commands still present old Pickle Rick SDLC assumptions?
- does `/in` and `/out` exist as real first-class commands or just as aliases/theater?
- does `--mode` materially control runtime or only leak into prompt text?

DOMAIN 2 — SETUP / PARSER / SESSION INIT
Inspect:
- setup.ts / setup.js or equivalent
- argument parsing logic
- state initialization logic
- session creation logic
- where mode is stored
- where thresholds are loaded
- how active session state is established

Questions:
- is mode parsed?
- is mode persisted?
- what is the initial lifecycle step?
- is the new lifecycle real or still engineering-shaped?
- how does a new run decide its mission identity?

DOMAIN 3 — LIFECYCLE ENUMS / STATE MACHINE
Inspect:
- types
- enums
- state transition tables
- hook assumptions
- stop logic
- active/inactive markers
- completion token handling

Questions:
- what are the real lifecycle states?
- are they still PRD/Breakdown/Research/Plan/Implement/Refactor?
- is there a DEEPICKLE-native lifecycle?
- are transitions explicit or improvised?
- does the loop still assume coding-task completion semantics?

DOMAIN 4 — SKILL GRAPH
Inspect:
- all skills
- all activate_skill calls
- transition edges between skills
- skill names in docs vs actual filesystem names
- deep-prefixed vs old non-deep skill references
- skill prerequisites
- any load-pickle-persona / load-deepickle-persona mismatches

Questions:
- which skills actually exist?
- which skill calls resolve?
- which calls point to dead or old names?
- where does fallback-to-generic behavior likely enter?
- is the graph a coherent DEEPICKLE graph or a broken old/new hybrid?

DOMAIN 5 — RUNTIME / COMPILED OUTPUTS
Inspect:
- compiled JS/CJS runtime files
- hook handlers
- built artifacts
- what the extension actually invokes
- whether stale compiled files are still taking precedence

Questions:
- does source match runtime?
- were source edits ever rebuilt?
- are compiled files stale?
- do hooks/cmds load source or compiled output?
- is the repo editing the wrong truth layer?

DOMAIN 6 — CONFIG / THRESHOLDS / RUBRICS
Inspect:
- config.json
- validation.json
- command defaults
- rubric docs
- state.json / re_state.json
- any completion-promise logic
- threshold constants

Questions:
- what is the actual pass threshold?
- what is the actual excellence threshold?
- how many conflicting values exist?
- which threshold is runtime truth?
- is completion still string-promise based instead of validator-gated?

DOMAIN 7 — INWARD SUBSTRATE
Inspect:
- `.deepickle` scaffolding
- DB declarations
- chunking scripts
- manifests
- ledgers
- file inventory logic
- extraction logic
- run-state logic
- resumability logic
- inward-specific workflow files

Questions:
- is there a real substrate or just a folder with hopes in it?
- is there real SQLite write/read logic?
- is there deterministic chunking?
- is there manifest production?
- are extraction ledgers real?
- does inward materially differ from “generalist reads files and writes summary”?

DOMAIN 8 — OUTWARD RESEARCH MACHINERY
Inspect:
- outward skills
- tool routing
- source handling
- evidence handling
- any contradiction map logic
- any source independence handling
- any premium routing or escalation logic

Questions:
- what outward capabilities are real?
- which are just doctrine?
- where is source adjudication actually enforced?
- how much is done by real machinery vs writing style?

DOMAIN 9 — HOOKS / LOOP CONTROL
Inspect:
- before/after hooks
- stop hook
- iteration increment logic
- max-iteration logic
- state hydration between iterations
- completion gating
- hook return shapes
- hook-specific state writing

Questions:
- what controls continuation?
- is the loop actually DEEPICKLE-native or still old Pickle Rick task-completion logic?
- are unresolved validator failures surfaced?
- is state rehydrated from files or from chat assumptions?
- do hooks materially enforce the doctrine?

DOMAIN 10 — OUTPUT SHAPE / ARTIFACTS
Inspect:
- templates
- generated output files
- artifact indexes
- output classes
- any per-class validators
- actual outputs produced in test runs

Questions:
- does the repo produce artifact-shaped outputs or generic summaries?
- are output classes explicit?
- are writing validators real?
- do outputs preserve evidence/provenance?
- are durable artifacts indexed and written back?

DOMAIN 11 — OPERATOR ARSENAL INTEGRATION
Inspect:
- repo docs for shared environment awareness
- `.gemini/settings.json`
- context include directories
- shared python references
- vault references
- operator control plane references
- any local scripts that assume the shared environment

Questions:
- is the repo aware of the Operator Arsenal System?
- is it inheriting shared tooling or reinventing it?
- are project settings written?
- are shared context docs integrated?
- is shell/runtime policy explicit?

================================================================
5. AUDIT METHOD
================================================================

The audit must be performed in passes, not as one giant skim.

PASS 1 — FILESYSTEM REALITY
Map the repo and surrounding relevant files:
- commands
- hooks
- scripts
- skills
- configs
- build outputs
- `.gemini`
- `.deepickle`
- docs
- package/build metadata

Output:
filesystem map
high-value file shortlist
suspected divergence zones

PASS 2 — EXECUTION CHAIN MAP
Map the actual execution chain:
command -> parser -> state init -> hook -> worker/skill -> validation -> stop/continue

Output:
real control flow diagram
points where doctrine is enacted
points where doctrine is bypassed

PASS 3 — IDENTITY GAP ANALYSIS
Compare intended DEEPICKLE identity to actual runtime behavior.

Output:
real vs claimed capability matrix
old Pickle Rick inheritance map
fake or mislabeled components

PASS 4 — BREAKAGE MAP
Find exact blockers:
- broken skill calls
- stale compiled outputs
- unparsed flags
- missing DB writes
- missing validators
- old threshold constants
- dead commands
- shadow files not actually used

Output:
must-fix-now list
defer list
sequence risk analysis

PASS 5 — RECONCILIATION PLAN
Translate findings into a lawful implementation order.

Output:
repair sequence
which files change first
which files get deleted or rebuilt
which docs must be rewritten after runtime is fixed

================================================================
6. IDENTITY GAP DOCTRINE
================================================================

Every major claimed feature must be judged against three questions:

QUESTION A — DOES IT EXIST?
Is there executable behavior?

QUESTION B — DOES IT WORK?
Does it materially perform its intended role?

QUESTION C — DOES IT MATCH THE CLAIM?
Does the runtime behavior actually correspond to the name/doctrine/docs around it?

Examples:

Case 1:
A command named `/in` exists, but it only forwards task text into a generic loop with no mode-specific lifecycle, validator, or artifacts.
Classification:
MISLABELED + DECLARED BUT FAKE

Case 2:
A DB file is created in bootstrap, but nothing writes meaningful state to it.
Classification:
DECLARED BUT FAKE

Case 3:
A deep skill exists, but its transition points into old non-deep skill names.
Classification:
PARTIAL + STALE INHERITANCE + MUST FIX NOW

Case 4:
A source file claims new hook logic, but compiled runtime still uses older handlers.
Classification:
RUNTIME/SOURCE DIVERGENCE + MUST FIX NOW

================================================================
7. SOURCE VS RUNTIME RECONCILIATION LAW
================================================================

One of the most dangerous failure modes in this repo class is editing the wrong truth layer.

The audit must determine:
- which files are actually executed
- whether build outputs are stale
- whether runtime loads source or compiled code
- whether hooks are using generated artifacts that no longer match source
- whether docs describe source intent while runtime executes older behavior

If divergence exists, choose one lawful path:

PATH A — SOURCE-OF-TRUTH REBUILD
- repair source
- rebuild runtime
- delete/replace stale build outputs
- validate actual execution now matches source

PATH B — RUNTIME-OF-TRUTH HARDENING
- if build system is intentionally absent or irrelevant, repair the effective runtime directly
- then update source/doctrine so no split remains

Unlawful state:
keeping both layers divergent and hoping the model “understands” the intended one.

================================================================
8. THRESHOLD RECONCILIATION LAW
================================================================

Threshold conflict is not a cosmetic issue.
It corrupts completion law.

The audit must find every threshold-like control:
- pass score
- excellence score
- validator minimums
- command defaults
- stop conditions
- completion promise strings
- max-iteration caps
- score gating
- fallback completion paths

Then classify them:
- active runtime threshold
- documented threshold
- stale threshold
- conflicting threshold
- unused threshold

Canonical law after reconciliation:
PASS_THRESHOLD = 80
EXCELLENCE_THRESHOLD = 90

Any surviving threshold logic that contradicts this must either:
- be explicitly justified as a separate mechanism
or
- be removed

================================================================
9. STATE MACHINE RECONCILIATION LAW
================================================================

The audit must determine whether the repo’s real lifecycle is still old Pickle Rick engineering-shaped.

If the state machine still initializes around:
- PRD
- Breakdown
- Research
- Plan
- Implement
- Refactor

then the repo’s deep identity is still structurally inherited.

That is unlawful for the rebuilt DEEPICKLE.

Lawful DEEPICKLE lifecycle families are:

OUT:
- FRAME
- SCOUT
- EVIDENCE
- VERIFY
- SYNTHESIZE
- VALIDATE
- WRITEBACK

IN:
- INTAKE
- NORMALIZE
- CHUNK
- EXTRACT
- MAP
- SYNTHESIZE
- VALIDATE
- WRITEBACK

CONFIG:
- READ
- MODIFY
- VERIFY
- WRITEBACK (optional)

STOP:
- explicit termination path

If the audit finds “new names but old semantics,” that still counts as stale inheritance.

================================================================
10. SKILL GRAPH RECONCILIATION LAW
================================================================

The skill graph must be treated as a graph, not a pile of folders.

The audit must extract:
- all skill nodes
- all edges (transitions)
- all missing targets
- all old-name references
- all mode-misaligned transitions
- all dead-end branches
- all silent fallback zones

Skill graph health questions:
- can each skill resolve its next lawful transition?
- does each transition belong to the correct mode?
- do any skills still assume code-centric output as default?
- where do deep skills call old names?
- where do names imply DEEPICKLE but bodies still embody Pickle Rick engineering semantics?

A skill is not considered real merely because the folder exists.
Its place in the graph must be lawful.

================================================================
11. INWARD SUBSTRATE RECONCILIATION LAW
================================================================

The audit must decide whether inward is real or theater.

Questions:
- Is there deterministic file enumeration?
- Is there normalization?
- Is there stable chunking?
- Are chunk IDs real?
- Are extracts written durably?
- Is there a claim seed registry?
- Is there a concept index?
- Is there resumable run state?
- Are local files processed through machinery before synthesis?
- Does the output shape materially differ from stock generic summary behavior?

If the answer to most of these is “no,” then inward is still fake regardless of how good the prompt tone sounds.

The audit must not allow rhetorical success on one file-reading run to be mistaken for substrate completion.

================================================================
12. OUTPUT RECONCILIATION LAW
================================================================

The audit must inspect actual generated outputs, not only templates.

Questions:
- What does the repo actually produce right now?
- Are outputs summary-shaped?
- Are outputs same-size / same-phrasing / same-structure as stock baseline behavior?
- Are outputs evidence-led?
- Do they feel blueprint-grade?
- Do they update registries?
- Do they write durable artifacts?
- Are classes explicit or implicit?
- Is writing being validated separately from research?

If outputs remain generic, the audit must trace that backward to cause:
- missing artifact grammar
- missing validator
- missing substrate
- broken graph
- bad state machine
- prompt compression
- runtime drift
- missing writeback
- wrong tool use

================================================================
13. OPERATOR INTEGRATION RECONCILIATION LAW
================================================================

The repo must be reconciled with the Operator Arsenal doctrine.

The audit must determine:
- are project `.gemini` settings present?
- do they include shared context directories?
- do they expose Operator env vars?
- is the repo aware of shared Python?
- is the repo aware of the shared vault?
- do docs reflect OperatorControl inheritance?
- are helper scripts placed where doctrine expects them?

If not, the repo is operating below the machine it sits inside.
That is wasted leverage and must be fixed.

================================================================
14. DOC TRUTH LAW
================================================================

Documentation is not allowed to overstate reality.

After audit, docs must be categorized as:
- truthful and current
- truthful but stale
- aspirational and mislabeled
- outdated and misleading
- inherited and no longer lawful

No README, GEMINI context, or comment should survive if it materially misdescribes runtime truth after reconciliation.

Doc updates happen after runtime repair, not instead of runtime repair.

================================================================
15. DELETE / REBUILD LAW
================================================================

Not every broken part should be patched.
Some parts should be deleted and rebuilt.

Delete/rebuild is preferred when:
- compiled/runtime artifacts are stale and confusing
- naming is too polluted to salvage cleanly
- the state machine is irreparably old-shaped
- a feature is mostly fake scaffolding
- keeping it would preserve false identity
- the patch surface is larger than a clean replacement

Patch-in-place is preferred when:
- behavior is fundamentally real but incomplete
- interfaces are good but implementation is missing
- the change is local and low-risk
- the docs/command surface can remain stable while internals improve

Surgery law:
Do not preserve diseased tissue just because it already exists.

================================================================
16. MUST-FIX-NOW CATEGORIES
================================================================

Any audit finding that falls into one of these categories becomes MUST FIX NOW:

CATEGORY A — MODE THEATER
Mode is named but not real.

CATEGORY B — STATE-LIFECYCLE FALSEHOOD
Lifecycle remains structurally engineering-shaped or internally inconsistent.

CATEGORY C — BROKEN SKILL EDGE
Skill transitions point to dead, stale, or wrong targets.

CATEGORY D — RUNTIME/SOURCE SPLIT
Source says one thing, runtime does another.

CATEGORY E — COMPLETION CORRUPTION
Threshold conflict, stop logic confusion, or fake completion semantics.

CATEGORY F — INWARD FAKENESS
No real substrate behind inward claims.

CATEGORY G — DOCS THAT LIE ABOUT RUNTIME
Material mismatch that would mislead future work.

CATEGORY H — OPERATOR INTEGRATION GAP
Repo not properly integrated with the shared environment despite depending on it.

These must be resolved before advanced expansion work is allowed.

================================================================
17. MAY-DEFER CATEGORIES
================================================================

A defect may be deferred only if:
- it does not corrupt the core lifecycle
- it does not make docs lie
- it does not materially affect command truth
- it does not cause generic fallback in core missions
- it is additive, not foundational
- it can wait until the substrate is real

Typical lawful deferrals:
- advanced provider routing refinements
- semantic retrieval add-ons
- luxury writing styles
- optional Evil Morty critic
- STORM-like post-synthesis modules
- advanced dashboards beyond useful minimums
- non-essential analytics layers

Nothing foundational may be deferred merely because it is annoying.

================================================================
18. SURGICAL REPORT FORMAT
================================================================

The audit report produced by Pickle Rick should be structured like this:

SECTION 1 — CURRENT STATE SNAPSHOT
- repo shape
- bootstrap/environment shape
- confirmed runtime layer
- confirmed project settings state

SECTION 2 — CLAIM VS REALITY MATRIX
For each major claimed capability:
- claimed
- observed
- classification
- evidence

SECTION 3 — DEFECT LEDGER
For each defect:
- ID
- title
- category
- severity
- affected files
- observed behavior
- constitutional violation
- recommended action
- fix phase

SECTION 4 — RECONCILIATION DECISIONS
- patch
- rebuild
- delete
- defer

SECTION 5 — IMPLEMENTATION ORDER
Concrete file order and sequence.

SECTION 6 — DOC CLEANUP ORDER
Which docs wait until after runtime repair.

SECTION 7 — SUCCESS CRITERIA FOR NEXT PASS
What must be true before the audit phase is considered done.

================================================================
19. RECONCILIATION SUCCESS CONDITION
================================================================

The audit/reconciliation phase is complete only when:
- every major capability is classified honestly
- the real runtime layer is identified
- the command/path/state/hook/skill chain is mapped
- fake scaffolding is distinguished from real machinery
- old Pickle Rick inheritance is identified precisely
- threshold conflict is resolved conceptually
- inward fakeness is either disproven or acknowledged
- Operator integration state is verified
- a repair order exists that can be executed without ambiguity

Until then, implementation is proceeding blind.

================================================================
20. FINAL ORDER
================================================================

Pickle Rick must perform repo audit as a surgeon, not a hype man.

He must:
- inspect the repo
- inspect the runtime
- inspect the control plane
- inspect the settings
- inspect the bootstrap status
- map reality
- classify everything
- then cut in the correct order

He must not:
- trust docs first
- skip runtime verification
- preserve stale compiled artifacts out of laziness
- let fake inward capability remain implied
- let broken graph edges survive
- let mode theater continue
- let threshold conflict remain
- drift into implementation before the map is real

END REPO SURGICAL AUDIT / RECONCILIATION DOCTRINE