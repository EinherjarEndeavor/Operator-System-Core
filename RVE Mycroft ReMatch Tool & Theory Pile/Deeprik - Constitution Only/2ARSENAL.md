UNCL//OPERATOR USE
DEEPICKLE OPERATOR ARSENAL SYSTEM
VERSION: 1.0
STATUS: CANONICAL
DEPENDENCY: DEEPICKLE CONSTITUTION v1.0
AUTHORITY: DEFINES THE ENVIRONMENTAL, CONTROL-PLANE, AND TOOL INHERITANCE LAYER FOR ALL DEEPICKLE OPERATIONS

================================================================
0. PURPOSE
================================================================

This document defines the environment doctrine for DEEPICKLE and all related Operator projects.

Its purpose is to prevent:
- tool fragmentation
- duplicate installations
- extension-local reinvention of global capabilities
- hidden dependencies
- undocumented shell/runtime behavior
- project drift
- “I installed it but Gemini doesn’t know it exists” syndrome
- “the tool exists physically but not doctrinally” failure

This document answers:
- where things live
- what belongs globally versus locally
- how Gemini learns about tools
- how extensions inherit capabilities
- how new tools are installed and made permanent
- how the shared vault and registries are used
- how runtime shell identity is controlled
- how project-specific overrides are allowed without contaminating the whole Operator environment

This is the machine-room doctrine.

================================================================
1. CANONICAL ROOTS
================================================================

PRIMARY OPERATOR ROOT:
C:\Users\tarot\Operator

CANONICAL PROJECT ROOTS:
- DeepRick repo:
  C:\Users\tarot\Operator\DeepRick4.2.841REAL
- RVE:
  C:\Users\tarot\Operator\RVE
- SlopCorps:
  C:\Users\tarot\Operator\SlopCorps

SHARED PYTHON:
C:\Users\tarot\Operator\.venvs\operator-core\Scripts\python.exe

SHARED CONTROL PLANE:
C:\Users\tarot\Operator\OperatorControl

SHARED VAULT:
C:\Users\tarot\Operator\OperatorVault

These are the canonical roots.
All future environment logic must either respect them or explicitly justify deviations.

================================================================
2. ENVIRONMENTAL HIERARCHY
================================================================

The Operator environment has four layers.

LAYER 1 — MACHINE / USER GLOBAL
This is the widest layer.
It includes:
- installed shell tools
- user-level Gemini settings
- user-level Gemini context
- shared Python environment
- global registries
- shared control-plane scripts
- shared MCP doctrine
- shared vault

LAYER 2 — OPERATOR CONTROL PLANE
This is the coordination layer.
It contains:
- registries
- context docs
- helper scripts
- MCP definitions or placeholders
- install history
- integration doctrine
- future registry sync utilities

LAYER 3 — PROJECT WORKSPACE
This is project-local configuration and state.
It includes:
- `.gemini/settings.json`
- `.gemini/context`
- repo-local docs
- repo-local scripts
- repo-local validators
- repo-local `.deepickle/` runtime data
- optional repo-local virtual environments when pinned isolation is required

LAYER 4 — EXTENSION / PERSONA / WORKFLOW
This is the narrowest layer.
It includes:
- extension commands
- extension workflow logic
- extension persona
- extension hooks
- extension-specific skills
- project-specific assumptions that do not belong in the global layer

Doctrine:
The wider the layer, the more reusable and stable it should be.
The narrower the layer, the more specific and mission-shaped it may be.

================================================================
3. BOUNDARY LAW
================================================================

Not everything belongs everywhere.

GLOBAL BELONGS GLOBAL IF:
- it is useful across multiple projects
- it defines shared behavior
- it describes stable tooling
- it concerns installation doctrine
- it concerns Gemini-wide operational policy
- it applies to all or most Operator workspaces
- it is a durable reusable capability

PROJECT-LOCAL BELONGS PROJECT-LOCAL IF:
- it is unique to one repo
- it is tied to one mission domain
- it requires pinned or isolated dependencies
- it represents local workflow assumptions
- it is an experiment not yet ready for global promotion
- it should not contaminate unrelated workspaces

EXTENSION-LOCAL BELONGS EXTENSION-LOCAL IF:
- it exists specifically to shape one extension’s persona/workflow
- it is not broadly reusable infrastructure
- it is not the correct source of truth for global tooling

The environment must not collapse these boundaries.

================================================================
4. SHARED PYTHON DOCTRINE
================================================================

DEFAULT DAILY PYTHON:
C:\Users\tarot\Operator\.venvs\operator-core\Scripts\python.exe

This shared environment exists to provide:
- cross-project reuse
- consistent tool availability
- low-friction shell invocation
- a stable default substrate for Gemini and related scripts
- reduced duplication across `Operator\X` workspaces

This is the default environment for:
- shared scripts
- control-plane utilities
- deterministic substrate tools
- document processing
- parsing / extraction / normalization
- common research support code
- general cross-project automation

This shared environment should include:
- base packages needed across projects
- heavy packages only if they are broadly useful and stable
- packages registered in the Operator registry
- version notes where necessary

SHARED PYTHON LAW:
The shared environment is the default unless a repo explicitly requires isolation.

================================================================
5. REPO-LOCAL PYTHON DOCTRINE
================================================================

Repo-local virtual environments are allowed.
They are not the default.
They are the exception.

A repo-local environment should exist only when:
- dependency pinning materially matters
- project-specific packages would pollute the shared environment
- reproducibility of that repo requires tighter isolation
- the project has unusual or unstable dependencies
- the project needs a frozen substrate for testing or release

For DeepRick, a repo-local environment is lawful at:
C:\Users\tarot\Operator\DeepRick4.2.841REAL\.deepickle\venv

But this must be treated as:
- optional strict isolation
- not the universal default for all Operator work
- not a replacement for the Operator shared environment

ENVIRONMENT RESOLUTION ORDER:
1. Use project-local venv if the repo explicitly requires it
2. Otherwise use shared Operator Python
3. Never assume “whatever python is on PATH” is acceptable without verification

================================================================
6. TOOL SUBSTRATE LAW
================================================================

A tool is not “real” in the system merely because it was installed once.

A tool becomes real only when it exists across four dimensions:

DIMENSION 1 — PHYSICAL
The binary/package/library/program is installed.

DIMENSION 2 — INVOCABLE
Gemini or scripts can actually call it via stable paths/commands.

DIMENSION 3 — REGISTERED
The tool is recorded in the Operator registry.

DIMENSION 4 — DOCTRINAL
The system knows:
- what it does
- when to use it
- when not to use it
- what inputs it expects
- what outputs it produces
- whether it is global or local
- whether it is deterministic or interpretive
- whether it is stable or experimental

If a tool only exists physically, it is half-installed.
If it is invocable but undocumented, it is dangerous.
If it is registered but not callable, it is theater.

================================================================
7. INSTALL → REGISTER → SYNC LAW
================================================================

All future tooling additions must obey this sequence.

STEP 1 — INSTALL
Install the tool into the correct substrate:
- shared shell
- shared Python
- repo-local Python
- node runtime
- MCP server
- project-local binary
- other sanctioned substrate

STEP 2 — REGISTER
Update the appropriate registry:
- tool registry
- provider registry
- MCP registry
- install history
- optional failure log if installation was messy

STEP 3 — SYNC
Expose it where appropriate:
- Gemini user settings
- project `.gemini/settings.json`
- shared context docs
- repo-local docs
- wrapper scripts or helper scripts if needed

STEP 4 — VALIDATE
Verify:
- callable path
- successful invocation
- expected output shape
- no shell/runtime mismatch
- no broken assumptions

STEP 5 — DOCUMENT
Write or update doctrine for:
- what it is
- what it is for
- how it is invoked
- what missions should use it
- what missions should not use it

No tool should skip this pipeline.

================================================================
8. OPERATOR CONTROL PLANE STRUCTURE
================================================================

CANONICAL CONTROL PLANE ROOT:
C:\Users\tarot\Operator\OperatorControl

REQUIRED SUBSTRUCTURE:
- registry\
- context\
- scripts\
- mcp\
- backups\

The control plane is the place where environment truth is coordinated.
It is not a dumping ground.
It is not random storage.
It is the administrative spine.

REGISTRY\
Holds structured system-of-record artifacts:
- tools.json
- providers.json
- mcp-servers.json
- install-history.jsonl
- future capability ledgers

CONTEXT\
Holds model-facing doctrine and shared operational instructions:
- GEMINI-OPERATOR.md
- TOOL-ARSENAL.md
- MCP-ARSENAL.md
- INSTALL-DOCTRINE.md
- GEMINI-0.36-AWARENESS.md
- OPERATOR-ARSENAL-INTEGRATION-PATCH.md
- future high-value context docs

SCRIPTS\
Holds sanctioned utilities for:
- registering tools
- syncing settings
- bootstrapping MCP
- validating environment state
- future installation wrappers
- future repair or migration scripts

MCP\
Holds MCP-related material:
- server definitions
- wrappers
- launch notes
- integration scaffolds
- future reusable servers

BACKUPS\
Holds environment backups prior to mutation:
- user settings backups
- registry snapshots if necessary
- future migration rollback artifacts

================================================================
9. GEMINI USER SETTINGS DOCTRINE
================================================================

User-level Gemini settings are the main inheritance channel for shared Operator behavior.

CANONICAL USER SETTINGS PATH:
C:\Users\tarot\.gemini\settings.json

This layer should define:
- shared context include directories
- shared environment variables
- user-wide behavior that should apply to all Gemini sessions unless overridden
- shared MCP servers only when truly stable and broadly useful
- globally useful defaults that do not become a footgun in unrelated workspaces

USER SETTINGS SHOULD NOT:
- hardcode project-specific assumptions
- become a landfill of every experimental tool
- contain unstable placeholder MCP servers
- silently disable core tool behavior through careless allowlisting
- encode repo-specific secrets or brittle repo-relative assumptions

USER SETTINGS MUST:
- remain valid JSON
- remain inspectable
- remain backed up before mutation
- remain conservative enough to not sabotage unrelated sessions

================================================================
10. PROJECT GEMINI SETTINGS DOCTRINE
================================================================

Project-level Gemini settings exist to narrow or augment inheritance.

CANONICAL PATH PATTERN:
<project>\.gemini\settings.json

Project settings may:
- add project context directories
- add project-local env vars
- add project-specific MCP servers
- set project-specific context-loading behavior
- define project-local operational posture

Project settings must not:
- redefine global doctrine unnecessarily
- copy-paste huge blocks from user settings for no reason
- hide the project from the shared control plane
- become a second uncontrolled source of truth for global tooling

Project settings are subordinate to the control plane doctrine.
They are allowed to override, not to fork reality.

================================================================
11. CONTEXT INHERITANCE LAW
================================================================

Gemini learns what exists through:
- settings
- includeDirectories
- extension context
- registered MCP capabilities
- invocable shell tooling
- durable environment variables
- explicit documentation

Therefore the control plane must maintain shared context docs that Gemini can ingest.

MINIMUM SHARED CONTEXT SET:
- GEMINI-OPERATOR.md
- TOOL-ARSENAL.md
- MCP-ARSENAL.md
- INSTALL-DOCTRINE.md
- GEMINI-0.36-AWARENESS.md
- OPERATOR-ARSENAL-INTEGRATION-PATCH.md

These docs should explain:
- what capabilities exist
- what is preferred
- what is shared vs project-local
- how to install/register new tooling
- how to reason about the Operator environment
- what Gemini should assume about shell/runtime/tooling posture

Context docs are not fluff.
They are the doctrine bridge between machine state and model behavior.

================================================================
12. ENVIRONMENT VARIABLES LAW
================================================================

The environment must expose canonical paths to Gemini and related scripts.

MINIMUM ENV VARS:
- OPERATOR_ROOT
- OPERATOR_VAULT
- OPERATOR_CONTROL
- OPERATOR_PYTHON

These should point to:
- C:\Users\tarot\Operator
- C:\Users\tarot\Operator\OperatorVault
- C:\Users\tarot\Operator\OperatorControl
- C:\Users\tarot\Operator\.venvs\operator-core\Scripts\python.exe

These variables exist so that:
- scripts do not need brittle hardcoded assumptions in every file
- extensions can discover the wider Operator environment
- pathing remains inspectable and standardized
- future repairs become easier

ENV VAR LAW:
These are directional references, not excuses for laziness.
Projects may still override when necessary, but global discovery must remain intact.

================================================================
13. SHELL IDENTITY LAW
================================================================

The interactive shell you see is not automatically the shell the model uses.

This must be treated as a hard law.

A user may be sitting in:
- pwsh 7.x

while automation may actually invoke:
- powershell.exe 5.1

This mismatch matters for:
- JSON parsing behavior
- strict mode behavior
- script compatibility
- array handling
- object handling
- module availability
- path behavior

Therefore:
Every sanctioned script must either:
- explicitly support the shell that will invoke it
or
- explicitly require a specific shell and enforce that requirement

SHELL LAW:
Never assume shell identity.
Always make it explicit.

================================================================
14. POWER SHELL COMPATIBILITY DOCTRINE
================================================================

There are only two lawful positions for major scripts.

POSITION A — WINDOWS POWERSHELL + POWERSHELL 7 COMPATIBLE
Use compatibility-safe patterns.

POSITION B — POWERSHELL 7 ONLY
Enforce it explicitly at the top of the script.

The unlawful position is:
“accidentally works in one shell and mysteriously breaks in another.”

If a script requires PowerShell 7, it must say so and abort clearly if launched in 5.1.
If a script aims to support both, it must avoid runtime-specific footguns.

No more ambiguity.

================================================================
15. MCP LAW IN PRACTICE
================================================================

MCP is the durable control-plane layer for reusable tools.

Use MCP when:
- the capability is worth exposing as a real reusable tool
- multiple projects will benefit
- stable invocation matters
- the capability should appear to Gemini as a first-class callable resource
- shell wrappers alone are not enough

Do not use MCP when:
- the tool is a one-off experiment
- the capability is trivial to handle through shell or script
- the maintenance cost outweighs the benefit
- the tool is unstable and not ready for general exposure

MCP registry entries must precede broad activation.
No placeholder garbage in active user settings.

================================================================
16. WRAPPER SCRIPT DOCTRINE
================================================================

Not every tool should be invoked directly by package internals.

Stable wrapper scripts are encouraged when they:
- normalize invocation
- hide ugly paths
- standardize input/output shape
- reduce Gemini-side ambiguity
- provide a consistent CLI surface across upgrades

Wrappers should live in sanctioned locations, preferably under:
C:\Users\tarot\Operator\OperatorControl\scripts

A wrapper is especially useful when:
- the underlying package is annoying
- environment selection matters
- output must be normalized
- future upgrades should not require every prompt or script to relearn the tool

Wrapper doctrine exists because stable interfaces are more valuable than raw installation.

================================================================
17. SHARED VAULT DOCTRINE
================================================================

CANONICAL SHARED VAULT:
C:\Users\tarot\Operator\OperatorVault

The vault exists to hold durable outputs and cross-project operational memory in a human-inspectable structure.

It is not a trash bin.
It is not a backup of random repo internals.
It is not the canonical home of every artifact.

The vault is the default destination for:
- cross-project durable outputs
- memos
- ledgers
- claim registries
- evidence ledgers
- novelty logs
- source reservoirs
- templates
- indexes
- project-facing outputs that should remain visible and reusable outside code repos

The vault should not swallow:
- source-controlled repo internals that belong in the repo
- runtime cache garbage
- temporary scratch noise unless explicitly useful
- files that belong in `.deepickle` runtime state

VAULT LAW:
Use the vault for durable operator-facing value.
Use the repo for repo truth.
Use runtime folders for runtime machinery.

================================================================
18. VAULT STRUCTURE DOCTRINE
================================================================

Minimum vault structure is lawful as:

- 00-Inbox
- 01-Operations
- 02-Outputs
- 03-Evidence
- 04-Claims
- 05-Novelty
- 06-Projects
- 07-Knowledge
- 08-Sources
- 09-Logs
- 10-Indexes
- 11-Templates

This structure is not sacred in naming, but the functions are sacred.

Functionally, the vault must support:
- capture
- operations
- outputs
- evidence
- claims
- novelty
- project-specific material
- knowledge reservoirs
- source reservoirs
- logs
- indexes
- reusable templates

================================================================
19. REPO VS VAULT LAW
================================================================

A recurrent failure mode is putting the wrong thing in the wrong place.

RULE:
If an artifact is part of the runtime truth of a repo, keep it in the repo.
If an artifact is a durable operator-facing output that should outlive repo internals, the vault is an appropriate home.
If an artifact is transient substrate machinery, keep it in runtime folders.

Examples:

Repo truth:
- extension files
- skills
- commands
- validators
- scripts
- `.gemini` config
- `.deepickle` runtime artifacts
- requirements
- package metadata

Vault truth:
- finished memos
- final blueprints
- consolidated findings
- human-facing ledgers
- evidence summaries
- claim registries
- novelty logs
- source reservoirs
- cross-project indexes

Runtime truth:
- chunk manifests
- temp extraction outputs
- run_state.json
- normalized text cache
- execution logs tied to active runs
- resumability artifacts

================================================================
20. REGISTRY DOCTRINE IN PRACTICE
================================================================

Minimum registry files should exist under:
C:\Users\tarot\Operator\OperatorControl\registry

tools.json
System-of-record for known tools and categories.

providers.json
System-of-record for external provider routing and roles.

mcp-servers.json
System-of-record for durable MCP capabilities and readiness state.

install-history.jsonl
Append-only history of meaningful installs/registrations/sync actions.

Registries must be:
- machine-readable
- inspectable
- current
- updated when real changes happen

Registries must not:
- accumulate lies
- contain fantasy integrations
- pretend a capability is active when it is only aspirational

================================================================
21. INSTALL HISTORY LAW
================================================================

Every meaningful installation or registration change should be logged.

Minimum fields should include:
- timestamp
- actor
- tool or capability name
- substrate
- project scope
- success/failure
- notes
- follow-up required

This exists to prevent:
- mystery state
- forgotten one-off changes
- “why does this machine behave differently now?” syndrome

A mature system remembers what was added, when, and why.

================================================================
22. FUTURE TOOL ADDITION LAW
================================================================

When a new tool is added later, the desired end state is:

1. the tool is installed in the right place
2. the Operator registry knows it exists
3. shared doctrine knows what it is for
4. Gemini user/project settings expose it if appropriate
5. relevant extensions can discover and use it
6. the installation is logged
7. the capability becomes part of the arsenal instead of a forgotten trick

That means the future ideal is not “AI installed a package.”
The future ideal is:
“AI installed, registered, exposed, documented, and validated a new durable capability.”

================================================================
23. EXTENSION INHERITANCE LAW
================================================================

Extensions should inherit from the Operator environment instead of re-declaring everything.

An extension should define:
- its persona
- its workflow
- its hooks
- its skills
- its command surface
- its validators
- any truly project-specific capabilities

An extension should not be the primary registry of:
- global tools
- shared Python
- common MCP doctrine
- shared vault paths
- global install rules
- Gemini-wide tool existence

DEEPICKLE must therefore behave as:
- an elite extension operating over the Operator Arsenal System
- not a sovereign island pretending the rest of the machine does not exist

================================================================
24. GEMINI 0.36 AWARENESS DOCTRINE
================================================================

The environment must assume an up-to-date Gemini CLI posture, not the stale worldview of older extension generations.

That means:
- subagents are real
- hooks are real
- MCP is real
- settings merge across scopes
- linked local extension development is correct for active work
- shell/runtime details matter
- extension authors must respect changed operational possibilities

But this does not mean:
- every new feature must be used
- the engine should be refactored just to check a box
- subagents should become default theater
- MCP should be used where shell or scripts are simpler
- the original recursive anti-slop loop should be weakened

New capability is lawful only when it strengthens the constitutional pillars.

================================================================
25. BOOTSTRAP SCRIPT DOCTRINE
================================================================

Bootstrap scripts are environment-shaping scripts and must be treated seriously.

A bootstrap script must:
- be explicit about required shell/runtime
- back up user settings before mutation
- write canonical registry/context files
- validate its work
- avoid silent corruption
- create missing project settings when requested
- leave the system in a more coherent state than before

A bootstrap script must not:
- assume shell identity
- mutate user settings recklessly
- write invalid JSON
- pretend success without verifying outputs
- create ambiguous or duplicate sources of truth

Bootstrap scripts are infrastructural operators, not casual helpers.

================================================================
26. VALIDATION DOCTRINE FOR ENVIRONMENT
================================================================

The environment itself must be validated.

Minimum environment validation checks:
- shared Python exists and is callable
- OperatorControl exists
- OperatorVault exists
- Gemini user settings are valid JSON
- required includeDirectories exist
- required env vars exist in Gemini settings if expected
- project `.gemini/settings.json` files exist where expected
- registry files exist and parse cleanly
- context docs exist in expected locations
- wrapper/helper scripts exist where promised

No environment mutation should be treated as complete until these are checked.

================================================================
27. FAILURE / REPAIR DOCTRINE
================================================================

If environment mutation fails:
- preserve backups
- inspect the exact shell/runtime used
- inspect the exact JSON or file that failed
- patch the script or settings
- rerun surgically if possible
- do not blindly nuke files unless necessary

Repairs should minimize collateral damage.
Fix precisely.
Do not restart the universe if one script line is wrong.

================================================================
28. SECRETS / KEY DOCTRINE
================================================================

This doctrine does not require storing secrets inside shared context docs or repo files.

If API keys or credentials are used:
- store them in appropriate secret locations
- do not spray them into prompt docs
- do not hardcode them into versioned files
- do not place them into general-purpose registries unless redacted

The environment should know providers exist without exposing secrets recklessly.

================================================================
29. WHAT “COMPLETE” LOOKS LIKE FOR OUTPUT 2
================================================================

This control plane is considered correct when:
- the Operator root is treated as the shared environment root
- shared Python is the default cross-project substrate
- repo-local venvs are exceptional, not default
- OperatorControl contains registries/context/scripts/backups coherently
- Gemini user settings are the main shared inheritance layer
- project `.gemini` settings provide local augmentation
- shared context docs explain the arsenal clearly
- vault doctrine separates human-facing durable outputs from repo/runtime truth
- shell identity is treated explicitly
- install-register-sync is real doctrine
- future tools can become permanent arsenal capabilities instead of isolated accidents

================================================================
30. FINAL ORDER
================================================================

All future DEEPICKLE, RVE, SlopCorps, and related Operator work must respect this environment doctrine.

The machine is wider than any one repo.
The control plane is higher than any one extension.
The shared environment exists so future capability becomes compounding infrastructure rather than repeated improvisation.

END OPERATOR ARSENAL SYSTEM