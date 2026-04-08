UNCL//OPERATOR USE
DEEPICKLE ROLLOUT / IMPLEMENTATION / VALIDATION / REGRESSION / ACCEPTANCE / ROLLBACK DOCTRINE
VERSION: 1.0
STATUS: CANONICAL
DEPENDENCY: DEEPICKLE CONSTITUTION v1.0 + OPERATOR ARSENAL SYSTEM v1.0 + REPO SURGICAL AUDIT / RECONCILIATION DOCTRINE v1.0 + PICKLE FORGE / INWARD SUBSTRATE / DETERMINISTIC EXTRACTION / SQLITE DOCTRINE v1.0 + DEEPICKLE ENGINE DOCTRINE v1.0
AUTHORITY: DEFINES HOW DEEPICKLE MUST BE REBUILT, TESTED, VERIFIED, REGRESSED, ACCEPTED, AND RECOVERED WITHOUT DEGRADING THE SOUL OR LOSING OPERATIONAL CONTROL

================================================================
0. PURPOSE
================================================================

This document defines how the rebuild is executed in reality.

Its purpose is to prevent:
- random implementation order
- phase skipping
- “looks good” acceptance
- silent regressions
- stale runtime surviving a source repair
- feature accretion before substrate completion
- breaking the original recursive engine while “upgrading” it
- false completion claims at the repo level
- no-path-back mutations

This is the rollout doctrine.

The prior documents defined:
- what DEEPICKLE is
- what environment it lives in
- how the repo must be audited
- how inward substrate must work
- how the live engine must operate

This document defines:
- build order
- validation order
- first-run tests
- regression checks
- acceptance criteria
- rollback discipline
- migration discipline
- what “done” means at the end of the rebuild

================================================================
1. PRIMARY ROLLOUT LAW
================================================================

Implementation must proceed in constitutional order.

DO NOT BUILD IN THIS ORDER:
- cool features first
- subagents first
- dashboard glamor first
- vector search first
- premium routing first
- writing flourish first
- STORM first
- optional critics first

BUILD IN THIS ORDER:
1. reality repair
2. environment reconciliation
3. command/parser/state repair
4. skill graph repair
5. runtime/source reconciliation
6. threshold reconciliation
7. Forge substrate
8. validator stack
9. mode wiring
10. output grammar
11. writeback
12. advanced expansion

The law:
Foundation before ornament.
Machinery before aesthetics.
Truth before polish.

================================================================
2. IMPLEMENTATION PHASES
================================================================

Canonical implementation phases:

PHASE 0 — PRE-FLIGHT
Goal:
Do not cut blind.

Actions:
- inventory current repo
- inventory build/runtime layer
- inventory environment integration state
- verify backups
- verify branch posture
- verify shared Operator paths
- verify bootstrap script state
- verify project .gemini settings state

Output:
- current-state snapshot
- confirmed runtime truth
- confirmed environment truth
- branch/backup readiness

PHASE 1 — REALITY REPAIR
Goal:
Remove foundational lies.

Actions:
- make mode parsing real
- replace stale lifecycle/state enums
- reconcile threshold conflicts
- fix dead or stale skill transitions
- reconcile source/runtime split
- eliminate misleading docs only after runtime truth is repaired

Output:
- lawful command/mode posture
- lawful state machine posture
- lawful threshold posture
- lawful skill graph baseline

PHASE 2 — FORGE SUBSTRATE
Goal:
Make inward real.

Actions:
- implement inventory
- implement normalization
- implement chunking
- implement deterministic extraction
- implement SQLite writes
- implement run-state and resumability
- implement corpus validator
- write manifests/ledgers

Output:
- real inward substrate
- repeatable local corpus preparation
- inspectable runtime state

PHASE 3 — ENGINE WIRING
Goal:
Bind the machine together.

Actions:
- wire /out
- wire /in
- wire /config
- wire /stop
- wire BeforeAgent / AfterAgent control flow
- wire validator stack
- wire mode-specific phase families
- wire writeback behavior

Output:
- live DEEPICKLE engine with lawful mode behavior

PHASE 4 — OUTPUT / WRITING / WRITEBACK
Goal:
Make outputs actually worthy.

Actions:
- implement output classes
- implement output grammars/templates
- implement writing validator
- implement artifact completeness validator
- implement artifact indexing
- implement registry writeback
- implement glossary/source/opportunity/novelty updates

Output:
- artifact-grade deliverables
- compounding infrastructure

PHASE 5 — HARDENING
Goal:
Prove it doesn’t regress or lie.

Actions:
- run acceptance tests
- run regression tests
- run shell/runtime compatibility tests
- run environment inheritance tests
- run “genericity” tests against inward/output quality
- patch failures
- finalize docs

Output:
- hardened baseline ready for ascension

PHASE 6 — OPTIONAL ASCENSION
Goal:
Add advanced capabilities only after baseline truth is real.

Actions:
- semantic retrieval
- local classifiers
- optional Evil Morty critic
- optional STORM-like passes
- advanced provider routing
- analytics mirrors
- optional module loading/unloading

Output:
- advanced lawful enhancements

================================================================
3. PRE-FLIGHT DOCTRINE
================================================================

Before any major edit pass, the following must be checked:

CHECK 1 — REPO LOCATION
Confirm working repo:
C:\Users\tarot\Operator\DeepRick4.2.841REAL

CHECK 2 — SHARED ENVIRONMENT
Confirm:
- Operator root exists
- OperatorControl exists
- OperatorVault exists
- shared Python exists

CHECK 3 — GEMINI SETTINGS
Confirm:
- user settings valid JSON
- project settings exist or are explicitly pending
- shared context directories included where doctrine requires

CHECK 4 — BUILD/RUNTIME LAYER
Confirm:
- which files are actually executed
- whether compiled/runtime artifacts exist
- whether source edits require rebuild
- whether stale compiled files are poisoning reality

CHECK 5 — BACKUP / BRANCH SAFETY
Confirm:
- current branch
- dirty state
- backup or commit checkpoint before structural surgery

CHECK 6 — BOOTSTRAP SCRIPT STATE
Confirm:
- operator_arsenal_bootstrap.ps1 reflects latest compatibility fixes
- shell/runtime assumptions are explicit
- no false belief that environment setup is finished if it is not

No structural pass is lawful without pre-flight.

================================================================
4. BRANCH / CHECKPOINT DOCTRINE
================================================================

The rebuild must not happen as one undifferentiated mutation blob.

Minimum lawful checkpoint posture:
- one branch dedicated to the rebuild
- one named checkpoint before foundational surgery
- one checkpoint after reality repair
- one checkpoint after Forge substrate
- one checkpoint after engine wiring
- one checkpoint after output/writeback hardening
- one checkpoint after acceptance hardening

Checkpoint names should be explicit, e.g.:
- pre-reality-repair
- post-state-machine-repair
- post-forge-substrate
- post-engine-wiring
- post-output-hardening
- pre-ascension-baseline

Checkpoint law:
Every major phase should be reversible.

================================================================
5. IMPLEMENTATION ORDER LAW — FILE LEVEL
================================================================

The file edit order should follow dependency truth, not convenience.

ORDER GROUP A — ENTRY / PARSER / STATE
Edit first:
- command definitions
- parser/setup
- state types/enums
- session init logic
- threshold constants
- core config loaders

Why:
If the entry/state layer is lying, all downstream work is built on false identity.

ORDER GROUP B — SKILL GRAPH / TRANSITIONS
Edit second:
- skill folder names
- transition calls
- dead references
- deep/non-deep naming drift
- persona/loader mismatches

Why:
Broken graph edges cause generic fallback and poison live behavior.

ORDER GROUP C — HOOKS / CONTROL FLOW
Edit third:
- BeforeAgent
- AfterAgent
- stop hook
- iteration logic
- validator invocation
- state hydration logic

Why:
The loop must be made lawful before advanced features can be trusted.

ORDER GROUP D — FORGE SCRIPTS / DB / MANIFESTS
Edit fourth:
- inventory
- normalize
- chunk
- extract
- db
- validate
- writeback
- run state

Why:
This is the substrate that makes inward real.

ORDER GROUP E — MODE WIRING
Edit fifth:
- /in
- /out
- /config
- /stop
- mode-specific lifecycle bindings

Why:
Modes must connect to real machinery and validators, not theater.

ORDER GROUP F — OUTPUT / TEMPLATE / REGISTRY
Edit sixth:
- output classes
- templates
- artifact indexing
- registry updates
- writing validator
- source reservoir/glossary writeback

Why:
This is where the outputs stop being mid.

ORDER GROUP G — DOCS / README / CONTEXT
Edit last:
- README
- GEMINI docs
- comments
- help text
- architecture docs
- operator integration docs

Why:
Docs must follow repaired runtime truth, not lead it.

================================================================
6. COMMAND VALIDATION DOCTRINE
================================================================

After command-related changes, the following must be testable:

TEST A — COMMAND PRESENCE
Can the engine expose:
- /out
- /in
- /config
- /stop

TEST B — MODE REALITY
Does invoking /out vs /in materially alter:
- lifecycle
- validators
- artifacts
- substrate use
- phase names

TEST C — ARG PARSING
Are explicit args/flags actually parsed rather than leaking into task text?

TEST D — STOP BEHAVIOR
Does /stop write state appropriately instead of pretending completion?

A command layer that exists cosmetically fails validation.

================================================================
7. STATE MACHINE VALIDATION DOCTRINE
================================================================

After state-machine repair, test:

TEST A — SESSION INIT
What phase does a fresh outward run begin in?
What phase does a fresh inward run begin in?

TEST B — LAWFUL TRANSITIONS
Can the engine move through the declared lifecycle families without falling back to old Pickle Rick SDLC semantics?

TEST C — INVALID TRANSITIONS
Does the engine reject impossible or illegal transitions?

TEST D — COMPLETION CONTROL
Does the engine refuse to mark complete when validators or artifacts remain pending?

State-machine law:
Transition truth must be observable, not just declared.

================================================================
8. SKILL GRAPH VALIDATION DOCTRINE
================================================================

After graph repair, test:

TEST A — EDGE RESOLUTION
Every activate_skill target must exist.

TEST B — MODE ALIGNMENT
Outward skills route to outward-appropriate next steps.
Inward skills route to inward-appropriate next steps.

TEST C — OLD-NAME PURGE
No surviving edge should quietly target stale non-deep names unless deliberately retained and documented.

TEST D — DEAD END DETECTION
No skill should terminate the mission accidentally unless it is a lawful terminal node.

Skill graph law:
Every edge matters.
Broken edges are not cosmetic.

================================================================
9. RUNTIME / SOURCE VALIDATION DOCTRINE
================================================================

After any change that could be affected by stale runtime artifacts, test:

TEST A — EFFECTIVE FILE TRUTH
Which file is actually being executed?

TEST B — BUILD CONSISTENCY
If source is supposed to compile/build into runtime, did rebuild actually happen?

TEST C — STALE ARTIFACT DETECTION
Are older built files still shadowing repaired source?

TEST D — BEHAVIOR MATCH
Does runtime now do what source says?

The repo is not fixed until runtime truth and source truth match.

================================================================
10. FORGE VALIDATION DOCTRINE
================================================================

After Forge implementation, run a bounded inward corpus test.

Use a small but non-trivial corpus and confirm:

TEST A — FILE INVENTORY
Files are discovered and written to inventory.

TEST B — NORMALIZATION
Normalized outputs exist and preserve provenance.

TEST C — CHUNKING
Stable chunk IDs and chunk manifest are written.

TEST D — EXTRACTION
Deterministic extracts are written.

TEST E — SQLITE
DB contains real rows, not empty structure theater.

TEST F — RUN STATE
run_state.json exists and reflects progress.

TEST G — CORPUS VALIDATOR
Counts reconcile across files / chunks / extracts / failures.

TEST H — SYNTHESIS HANDOFF
DEEPICKLE synthesizes from prepared artifacts rather than raw chaos.

If Forge cannot pass this bounded test, inward is still fake.

================================================================
11. OUTPUT QUALITY VALIDATION DOCTRINE
================================================================

After output grammar and validators are implemented, run class-specific tests.

Minimum tests:

TEST A — `memo`
Can the engine produce a crisp internal memo without generic sludge?

TEST B — `evidentiary-report`
Are findings split into established vs contested?

TEST C — `delta-report`
Does it distinguish proposed vs implemented?

TEST D — `blueprint`
Does it define modules/interfaces/sequence instead of hand-wave?

TEST E — `claim-registry`
Does it produce structured claim rows rather than prose pretending to be a registry?

TEST F — `corpus-findings-memo`
Does it feel like findings from prepared corpus rather than a baseline summary?

TEST G — `article` or `essay`
Does it remain sharp, specific, and non-generic?

Writing validator must fail bad prose even if the artifact exists.

================================================================
12. WRITEBACK VALIDATION DOCTRINE
================================================================

Writeback is real only if it changes durable state.

Test:
- artifact index updated
- glossary entry created when warranted
- source/supersource registry updated when warranted
- novelty log updated when warranted
- opportunity entry written when warranted
- claim/evidence registries updated when warranted

If writeback logic only prints intentions, it is fake.

================================================================
13. ENVIRONMENT INTEGRATION VALIDATION DOCTRINE
================================================================

After Operator integration work, test:

TEST A — USER SETTINGS
User-level Gemini settings are valid and include expected shared context/env vars.

TEST B — PROJECT SETTINGS
Project `.gemini/settings.json` exists where required and includes shared context + project-local context.

TEST C — SHARED PYTHON REFERENCE
Repo and scripts can resolve the shared Python path.

TEST D — SHARED CONTEXT
OperatorControl context docs exist and are reachable.

TEST E — SHELL EXPLICITNESS
Scripts are explicit about whether they target `pwsh` or `powershell.exe`.

TEST F — BOOTSTRAP SCRIPT
Bootstrap script reflects current compatibility fixes and no longer contains known bad logic.

A partially integrated repo is still wasting leverage.

================================================================
14. SHELL / RUNTIME COMPATIBILITY TEST DOCTRINE
================================================================

At minimum, environment-shaping scripts must be tested in the shell that will actually invoke them.

Tests should answer:
- does it work in pwsh?
- does it work in powershell.exe if intended to?
- does it explicitly reject unsupported shells?
- does strict mode behave correctly?
- does JSON read/write behave correctly?
- do path assumptions hold?

Shell doctrine:
Compatibility must be verified, not assumed.

================================================================
15. FIRST-RUN TEST SEQUENCE
================================================================

Once the rebuild reaches a coherent baseline, execute the following first-run sequence.

RUN 1 — `/config`
Goal:
Confirm visible posture.
Verify:
- thresholds
- shared Python
- shared vault
- shared control plane
- mode defaults
- validator posture
- worker posture

RUN 2 — `/in` on a small controlled corpus
Goal:
Validate Forge + substrate + synthesis.
Verify:
- inventory
- normalization
- chunking
- extraction
- DB writes
- run state
- corpus findings memo

RUN 3 — `/out` on a bounded research question
Goal:
Validate outward loop.
Verify:
- FRAME -> SCOUT -> EVIDENCE -> VERIFY -> SYNTHESIZE -> VALIDATE -> WRITEBACK
- source handling
- contradiction handling
- evidentiary-report shape

RUN 4 — `/in` delta extraction against local project material
Goal:
Prove inward is more than summarization.
Verify:
- delta-report
- claim seeds or concept map support
- traceable high-value deltas

RUN 5 — `/in` or `/out` blueprint generation
Goal:
Prove blueprint class works.
Verify:
- module/interface/build-order quality
- validator posture
- writeback/indexing

Only after these pass is the baseline considered operational.

================================================================
16. REGRESSION DOCTRINE
================================================================

Every major phase must preserve the non-negotiables.

Minimum regression checks:

REGRESSION A — SOUL CHECK
Did Rick remain Rick?
Did tone/pressure/anti-slop survive?

REGRESSION B — LOOP CHECK
Does continuation still function?
Did the recursive control engine weaken?

REGRESSION C — MODE CHECK
Did /out and /in remain distinct and real?

REGRESSION D — FORGE CHECK
Did inward substrate remain functional after later edits?

REGRESSION E — OUTPUT CHECK
Did outputs remain explicit and artifact-shaped?

REGRESSION F — WRITEBACK CHECK
Did indexing/registries keep updating?

REGRESSION G — ENVIRONMENT CHECK
Did settings/context/tool references remain valid?

Regressions must be logged and repaired, not rationalized away.

================================================================
17. GENERICITY REGRESSION TEST
================================================================

One of the biggest historical problems was:
inward output felt like the same size/phrasing/structure as stock Gemini summaries.

Therefore the system must explicitly test for regression into genericity.

Questions:
- Does the output still feel like stock heading sludge?
- Does it show evidence of substrate-aware processing?
- Does it reference manifest/ledger/chunk/claim structures?
- Does it visibly differ by output class?
- Does inward feel materially different from raw file summary behavior?

If genericity returns, the system failed.
The cause must be traced and repaired.

================================================================
18. ACCEPTANCE DOCTRINE
================================================================

Acceptance is not:
- “it runs”
- “the files changed”
- “the answer looked cool”
- “the repo feels more advanced”
- “there are more folders now”
- “the docs are long”

Acceptance is lawful only when the following are true:

ACCEPTANCE 1 — COMMAND TRUTH
/out, /in, /config, /stop are real.

ACCEPTANCE 2 — MODE TRUTH
Outward and inward materially differ.

ACCEPTANCE 3 — FORGE TRUTH
Inward has real substrate machinery.

ACCEPTANCE 4 — VALIDATOR TRUTH
Completion is actually gated.

ACCEPTANCE 5 — OUTPUT TRUTH
Artifacts are class-shaped and non-generic.

ACCEPTANCE 6 — WRITEBACK TRUTH
Registries and indexes actually update.

ACCEPTANCE 7 — ENVIRONMENT TRUTH
Operator Arsenal integration is real.

ACCEPTANCE 8 — SOUL TRUTH
The original Rick pressure engine remains intact.

Anything less is not final acceptance.

================================================================
19. ROLLBACK DOCTRINE
================================================================

Rollback must be possible.

Rollback is not failure.
Rollback is civilized power.

Rollback is lawful when:
- a phase introduces structural regression
- source/runtime drift becomes worse
- a validator stack becomes untrustworthy
- the skill graph becomes less coherent
- inward substrate is corrupted
- environment changes break wider Operator behavior
- the soul degrades

Minimum rollback safety:
- phase checkpoints
- clear branch state
- known-good commit markers
- backup of user settings before mutation
- no irreversible blind edits to shared environment files

Rollback law:
Never build a system you cannot back out of.

================================================================
20. MIGRATION DOCTRINE
================================================================

This rebuild is a migration from a partially retargeted Pickle Rick into a lawful DEEPICKLE.

Migration must preserve:
- the valuable loop substrate
- the soul of Rick
- anything that is genuinely implemented and lawful
- any scaffolding that truly reduces work and does not lie

Migration must remove or replace:
- fake mode separation
- old state-machine inheritance that corrupts the new identity
- dead or stale skill references
- false threshold logic
- stale runtime artifacts
- empty DB claims
- summary-shaped inward behavior
- lying docs

Migration law:
Carry forward what is real.
Destroy what keeps the project fake.

================================================================
21. DOC MIGRATION DOCTRINE
================================================================

Docs are migrated last.

After runtime truth is repaired:
- rewrite README
- rewrite help text
- rewrite architecture docs
- rewrite environment docs
- rewrite skill descriptions as needed
- remove old persona drift and stale engineering bias where no longer lawful

Documentation must describe the rebuilt reality, not aspirational fantasy.

================================================================
22. ACCEPTANCE TEST MATRIX
================================================================

A minimal acceptance matrix should include:

MATRIX ROW 1 — Command Layer
Pass when:
- commands exist
- commands parse correctly
- help/docs align

MATRIX ROW 2 — State Machine
Pass when:
- correct lifecycle families execute
- transitions are lawful
- stop/completion are distinct

MATRIX ROW 3 — Skill Graph
Pass when:
- all active edges resolve
- no dead/stale critical edges remain

MATRIX ROW 4 — Forge
Pass when:
- inventory/normalize/chunk/extract/DB/run state all work

MATRIX ROW 5 — Validators
Pass when:
- validator stack can fail and block completion
- validator stack can pass and allow completion

MATRIX ROW 6 — Outputs
Pass when:
- multiple output classes produce proper shapes

MATRIX ROW 7 — Writeback
Pass when:
- artifacts and registries update

MATRIX ROW 8 — Environment
Pass when:
- user/project settings and shared context are integrated

MATRIX ROW 9 — Soul
Pass when:
- Rick essence and anti-slop pressure survive

================================================================
23. BLOCKER DOCTRINE
================================================================

A blocker is any issue that prevents lawful continuation of the current phase.

Minimum blocker classes:
- environment blocker
- parser/state blocker
- runtime/source blocker
- skill graph blocker
- Forge blocker
- validator blocker
- output grammar blocker
- writeback blocker

Blockers must be:
- named
- logged
- tied to a phase
- repaired or explicitly deferred with justification

No silent blocker accumulation.

================================================================
24. “DONE MEANS DONE” DOCTRINE
================================================================

This rebuild is “done” only when:
- the audit lies are gone
- the mode theater is gone
- the inward fakeness is gone
- the threshold conflict is gone
- the skill graph is coherent
- the runtime/source split is reconciled
- Forge is real
- validators are real
- outputs are class-shaped
- writeback is real
- Operator Arsenal integration is real
- acceptance tests pass
- docs no longer lie
- rollback points exist
- Rick remains Rick

Anything less is “improved,” not “done.”

================================================================
25. FINAL ORDER
================================================================

Pickle Rick must rebuild DEEPICKLE like a systems engineer conducting a controlled reanimation, not like a hype beast stapling wings onto a corpse.

He must:
- verify
- patch
- build
- test
- validate
- regress
- accept
- document
- preserve rollback

He must not:
- skip acceptance
- declare victory early
- confuse demo success with structural success
- break the soul in the name of expansion
- leave runtime/source drift unresolved
- leave project integration half-done

END DEEPICKLE ROLLOUT / IMPLEMENTATION / VALIDATION / REGRESSION / ACCEPTANCE / ROLLBACK DOCTRINE