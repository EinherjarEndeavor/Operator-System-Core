# TECHNIQUES CANON

## INTRODUCTION
This document is the authoritative definition of the 40 cognitive techniques used by the Operator system. These techniques are internal processing modules that shape the agent's reasoning before a final artifact is produced.

---

## 1. PRE-FLIGHT
- **Alias:** `/preflight`
- **Purpose:** Systematic validation of the environment and mission parameters before any processing begins.
- **Operational Action:** Checks system time, canonical root paths, energy windows, and active legal/financial constraints.
- **When to Use:** At the start of every session or complex task.
- **When NOT to Use:** For trivial questions (e.g., "What time is it?").
- **Input Pattern:** The current prompt and session context.
- **Output Pattern:** A "GO/NO-GO" assessment and identified blockers.
- **Failure Modes:** Missing a critical constraint; hallucinating path access.
- **Pairings:** Constraint Lock, Intent Extraction.
- **Example:** "System time is 09:00 (Peak). Path is C:\Users\tarot\Operator. Status: GO."
- **Layer:** Always-hot dispatcher logic.

## 2. INTENT EXTRACTION
- **Alias:** `/intent`
- **Purpose:** Disambiguating the user's ultimate goal from their literal prompt.
- **Operational Action:** Isolates the "Target State" from the "Action Request."
- **When to Use:** When the prompt is underspecified or multi-part.
- **When NOT to Use:** When the command is a direct, atomic directive (e.g., "Delete file X").
- **Input Pattern:** Vague or complex user input.
- **Output Pattern:** A single sentence: "The user's goal is [X] to achieve [Y]."
- **Failure Modes:** Over-interpreting simple requests; missing subtext.
- **Pairings:** Pre-Flight, Constraint Lock.
- **Example:** User says "Clean this up." Intent: "User wants to refactor file X for readability while maintaining logic."
- **Layer:** Always-hot dispatcher logic.

## 3. RETRIEVAL GROUNDING
- **Alias:** `/retrieve`
- **Purpose:** Ensuring every fact used is anchored in existing files or databases.
- **Operational Action:** Mandates a `grep_search` (ripgrep) or `read_file` before generating claims.
- **When to Use:** When referencing project history, settings, or external documentation.
- **When NOT to Use:** For generic coding logic or general knowledge.
- **Input Pattern:** A claim or query requiring evidence.
- **Output Pattern:** A list of source file paths and specific line numbers.
- **Failure Modes:** Reading the wrong file; relying on training data over local truth.
- **Pairings:** Evidence Ledger, Provenance Tagging.
- **Example:** "Retrieving probation check-in date from GEMINI.md... Found: May 6, 2026."
- **Layer:** On-demand retrieval.

## 4. CONSTRAINT LOCK
- **Alias:** `/lock`
- **Purpose:** Rigid adherence to negative constraints (Legal, Financial, Path Law).
- **Operational Action:** Scans the prompt for words like "Oregon," "Contact," "Cost," and checks against Diogenes constraints.
- **When to Use:** Before proposing any plan involving external movement, communication, or spending.
- **When NOT to Use:** Purely internal file operations.
- **Input Pattern:** Proposed actions.
- **Output Pattern:** "LOCKED: Action violates constraint [X]" or "UNLOCKED."
- **Failure Modes:** "Softening" a constraint; missing a legal filter.
- **Pairings:** Pre-Flight, Red Team.
- **Example:** "/lock check: 'Search for Erika's social media' -> Result: LOCKED (No-contact order)."
- **Layer:** Always-hot dispatcher logic.

## 5. CAUSAL MAPPING
- **Alias:** `/map`
- **Purpose:** Identifying the "ripple effect" of a proposed change.
- **Operational Action:** Traces dependencies across the file system and logic flow.
- **When to Use:** Before modifying a core script, database schema, or system setting.
- **When NOT to Use:** Adding standalone documentation or single-line fixes.
- **Input Pattern:** A proposed modification.
- **Output Pattern:** A list of downstream files or systems that will be affected.
- **Failure Modes:** Missing a hidden dependency; underestimating the complexity of a refactor.
- **Pairings:** Tree of Thought, Drift Detection.
- **Example:** "Mapping change to setup.py -> Affects install.ps1, rve.db initialization, and phase-02-databases.md."
- **Layer:** Specialized workflow.

## 6. TREE OF THOUGHT
- **Alias:** `/tot`
- **Purpose:** Exploring multiple parallel solution paths before committing to one.
- **Operational Action:** Generates 3–5 potential strategies and evaluates them against the mission goal.
- **When to Use:** For architectural decisions or complex debugging.
- **When NOT to Use:** Linear tasks with established protocols.
- **Input Pattern:** A high-complexity problem.
- **Output Pattern:** Multiple "branches" with pros/cons for each.
- **Failure Modes:** Analysis paralysis; choosing the "easiest" path over the "correct" one.
- **Pairings:** Deep Think, Decision Tree.
- **Example:** "Branch A: Python script; Branch B: PowerShell; Branch C: Manual SQLite. Decision: Branch A (Best portability)."
- **Layer:** Specialized workflow.

## 7. DEEP THINK
- **Alias:** `/dt`
- **Purpose:** High-intensity recursive reasoning on a single, isolated problem.
- **Operational Action:** Deep-dives into the "Why" of a bug or design choice for multiple turns internally.
- **When to Use:** When a standard solution fails or a bug is "impossible."
- **When NOT to Use:** Standard implementation or retrieval tasks.
- **Input Pattern:** A persistent or structural error.
- **Output Pattern:** A fundamental insight or root-cause identification.
- **Failure Modes:** Losing track of the original goal; logical loops.
- **Pairings:** Tree of Thought, Causal Mapping.
- **Example:** "Deep Think on ripgrep error -> Root cause: Binary is missing from PATH, not a tool failure."
- **Layer:** Specialized workflow.

## 8. CHAIN OF DENSITY
- **Alias:** `/cod`
- **Purpose:** Maximum information per character; eliminating "fluff" while adding missing details.
- **Operational Action:** Iteratively rewrites a paragraph, identifying "missing entities" and fusing them into the text without increasing length.
- **When to Use:** Summarizing research, drafting PRDs, or technical documentation.
- **When NOT to Use:** Writing code or logs.
- **Input Pattern:** A "draft" or low-density summary.
- **Output Pattern:** A hyper-compressed, high-signal paragraph.
- **Failure Modes:** Over-compression making the text unreadable.
- **Pairings:** Compression Gate, Artifact Compiler.
- **Example:** Cycle 1: "I fixed the bug." Cycle 2: "Patched the null-pointer in line 42, restoring database connectivity."
- **Layer:** Specialized workflow.

## 9. RED TEAM
- **Alias:** `/red`
- **Purpose:** Brutal, adversarial critique of a proposed plan.
- **Operational Action:** Acts as an external attacker trying to break the plan, find security holes, or identify "slop."
- **When to Use:** Before any major commit or system deployment.
- **When NOT to Use:** Internal research phases.
- **Input Pattern:** A "final" plan or script.
- **Output Pattern:** A list of vulnerabilities or "Jerry-work" points.
- **Failure Modes:** Being too "nice"; missing obvious edge cases.
- **Pairings:** Failure Mode Forecast, Assumption Audit.
- **Example:** "Red Team: Your script assumes EBT is always available. What if the API is down?"
- **Layer:** Specialized workflow.

## 10. EVIDENCE LEDGER
- **Alias:** `/evidence`
- **Purpose:** Tracking the "Truth Score" of a set of claims.
- **Operational Action:** Lists every claim made in a response and maps it to a verified file/database entry.
- **When to Use:** Fact-checking research reports or system status audits.
- **When NOT to Use:** Creative brainstorming.
- **Input Pattern:** A completed report.
- **Output Pattern:** A table of Claim | Source | Verification Status.
- **Failure Modes:** False verification; circular reasoning.
- **Pairings:** Retrieval Grounding, Cross-Source Reconciliation.
- **Example:** "Claim: RVE score is 45. Source: rve.db query. Status: VERIFIED."
- **Layer:** Specialized workflow.

## 11. CONTRADICTION SCAN
- **Alias:** `/contra`
- **Purpose:** Identifying logical or data conflicts within the current context or between files.
- **Operational Action:** Compares new information against stored memory (Layer 2/4) for mismatches.
- **When to Use:** When merging new instructions or analyzing data from multiple sources.
- **When NOT to Use:** Purely linear data entry.
- **Input Pattern:** Two or more data sets.
- **Output Pattern:** "CONFLICT DETECTED: Source A says X, Source B says Y."
- **Failure Modes:** Missing a subtle logical contradiction; over-flagging synonymous terms.
- **Pairings:** Red Team, Assumption Audit.
- **Example:** "GEMINI.md says sobriety is Sep 19. User prompt says Oct 1. CONFLICT."
- **Layer:** Always-hot dispatcher logic.

## 12. ASSUMPTION AUDIT
- **Alias:** `/assume`
- **Purpose:** Surfacing hidden "unspoken" premises in a request or plan.
- **Operational Action:** Forces the agent to list what it is "taking for granted" before executing.
- **When to Use:** At the start of a medium/high complexity task.
- **When NOT to Use:** Extremely narrow, well-defined tasks.
- **Input Pattern:** A task description.
- **Output Pattern:** "ASSUMPTIONS: 1. You have Neo4j running. 2. Path is accessible..."
- **Failure Modes:** Listing only obvious assumptions; missing critical architectural dependencies.
- **Pairings:** Pre-Flight, Constraint Lock.
- **Example:** "Assuming you want this in Python, as previous RVE scripts are Python-based."
- **Layer:** Always-hot dispatcher logic.

## 13. SCHEMA FIRST
- **Alias:** `/schema`
- **Purpose:** Defining the data structure before writing the logic.
- **Operational Action:** Drafting a JSON/SQL/Markdown template for the data before processing it.
- **When to Use:** Ingesting new data types or building new database tables.
- **When NOT to Use:** Modifying existing text files.
- **Input Pattern:** A request to "store" or "organize" information.
- **Output Pattern:** A technical schema definition.
- **Failure Modes:** Over-complicating the schema; ignoring existing system patterns.
- **Pairings:** Artifact Compiler, Sequential Expansion.
- **Example:** "Defining rve_tasks schema: {id, urgency, impact, score}."
- **Layer:** Specialized workflow.

## 14. FAILURE MODE FORECAST
- **Alias:** `/failure`
- **Purpose:** Predicting how a system will break before it is built.
- **Operational Action:** Lists the top 3 ways a script/plan will fail and builds "safety rails" for them.
- **When to Use:** Building automation scripts or orchestration loops.
- **When NOT to Use:** One-off documentation tasks.
- **Input Pattern:** A proposed script or automation.
- **Output Pattern:** "FAILURE MODES: Truncation, Path Error, Access Denied. Mitigation: Chunker logic."
- **Failure Modes:** Predicting the wrong failures; over-engineering mitigations.
- **Pairings:** Red Team, Drift Detection.
- **Example:** "Forecasting ingest_onboarding.py -> Failure: CSV encoding mismatch. Mitigation: Encoding detection."
- **Layer:** Specialized workflow.

## 15. PROVENANCE TAGGING
- **Alias:** `/provenance`
- **Purpose:** Ensuring every artifact has a "history of origin."
- **Operational Action:** Appends metadata to the end of a file or response indicating where the data came from.
- **When to Use:** For all synthesized artifacts, dossiers, and databases.
- **When NOT to Use:** General conversational replies.
- **Input Pattern:** A final output.
- **Output Pattern:** "PROVENANCE: Derived from [Files X, Y] via [Workflow Z]."
- **Failure Modes:** Inaccurate tracing; missing a source.
- **Pairings:** Retrieval Grounding, Evidence Ledger.
- **Example:** "PROVENANCE: Derived from Control/Scripts/daily_driver.py via /ComboStatus."
- **Layer:** Always-hot dispatcher logic.

## 16. DELTA PASS
- **Alias:** `/delta`
- **Purpose:** Isolating what has CHANGED rather than re-reading the whole.
- **Operational Action:** Compares the current state to the previous state and reports only the difference.
- **When to Use:** Reviewing code changes, log updates, or session summaries.
- **When NOT to Use:** Building things from scratch.
- **Input Pattern:** Two versions of an object.
- **Output Pattern:** A concise diff or list of delta points.
- **Failure Modes:** Missing a subtle change; including unchanged noise.
- **Pairings:** Compression Gate, Drift Detection.
- **Example:** "Delta: Added 2 tasks to rve.db; updated system time in GEMINI.md."
- **Layer:** Always-hot dispatcher logic.

## 17. COMPRESSION GATE
- **Alias:** `/gate`
- **Purpose:** Forcing a summary or "checkpoint" when context exceeds 80%.
- **Operational Action:** Synthesizes the last 50 turns into a single "Handover" artifact and purges the noise.
- **When to Use:** Automatically triggered by context limits or manual invocation.
- **When NOT to Use:** When full session history is critical for the current task.
- **Input Pattern:** Large session history.
- **Output Pattern:** A high-density "Current State" document.
- **Failure Modes:** Losing critical nuance; "forgetting" an active goal.
- **Pairings:** Chain of Density, Artifact Compiler.
- **Example:** "Context at 85%. GATING: Session state saved to NEXT_PROMPT.md."
- **Layer:** Always-hot dispatcher logic.

## 18. DECISION TREE
- **Alias:** `/decision`
- **Purpose:** Mapping the logical flow of a complex conditional task.
- **Operational Action:** Visualizes a sequence of "If/Then" steps before execution.
- **When to Use:** Designing automation logic or resolving ambiguous instructions.
- **When NOT to Use:** Linear, unconditional tasks.
- **Input Pattern:** A multi-step conditional problem.
- **Output Pattern:** A flowchart or nested list of decisions.
- **Failure Modes:** Circular logic; missing a branch.
- **Pairings:** Tree of Thought, Failure Mode Forecast.
- **Example:** "If file exists -> Update; Else -> Create; Then -> Log."
- **Layer:** Specialized workflow.

## 19. UPGRADE CAPTURE
- **Alias:** `/upg`
- **Purpose:** Identifying accidental improvements or "wins" during a task.
- **Operational Action:** Flags a new pattern, tool, or insight discovered while doing something else.
- **When to Use:** During any implementation or research phase.
- **When NOT to Use:** Purely maintenance tasks.
- **Input Pattern:** Observed execution behavior.
- **Output Pattern:** "UPGRADE DETECTED: [Pattern X] is 20% faster. Saving to arsenal.db."
- **Failure Modes:** Over-valuing a minor optimization; distracting from the primary goal.
- **Pairings:** Drift Detection, Quality Gate.
- **Example:** "Found that ripgrep is faster than read_file for large lookups. UPGRADE."
- **Layer:** Always-hot dispatcher logic.

## 20. FINAL CANON PASS
- **Alias:** `/canonize`
- **Purpose:** Hardening a draft into its permanent, official form.
- **Operational Action:** Strips all conversational markers, "AI-speak," and tentative language.
- **When to Use:** Before writing to any `Control/Docs/` file.
- **When NOT to Use:** Scratchpads or internal thoughts.
- **Input Pattern:** A refined draft.
- **Output Pattern:** A formal, authoritative document.
- **Failure Modes:** Making the text too dry; losing important context.
- **Pairings:** Compression Gate, Artifact Compiler.
- **Example:** "Canonizing slash command definitions... Ready for merge."
- **Layer:** Specialized workflow.

## 21. SKELETON-OF-THOUGHT
- **Alias:** `/sot`
- **Purpose:** Rapid parallel generation of high-volume structures.
- **Operational Action:** Drafts a full outline with "placeholder sections" and then fills them in parallel (or sequential) turns.
- **When to Use:** Writing long reports, manuals, or multi-module codebases.
- **When NOT to Use:** Short replies or atomic code fixes.
- **Input Pattern:** A complex, multi-section requirement.
- **Output Pattern:** A complete document structure with 1-sentence summaries for every section.
- **Failure Modes:** Losing the "thread" between sections; fragmented logic.
- **Pairings:** Sequential Expansion, Artifact Compiler.
- **Example:** "Drafting SOT for Phase 4... Sections: Syntax, Parameters, Loops, Output."
- **Layer:** Specialized workflow.

## 22. GRAPH-OF-THOUGHT
- **Alias:** `/got`
- **Purpose:** Solving non-linear problems where steps interact in a network.
- **Operational Action:** Maps ideas as nodes and dependencies as edges, allowing the model to jump back and forth between "nodes" to refine.
- **When to Use:** Complex system design, legal constraint mapping, or multi-domain synthesis.
- **When NOT to Use:** Simple linear workflows.
- **Input Pattern:** A "messy" problem with interconnected variables.
- **Output Pattern:** A Mermaid diagram or edge-list representing the problem space.
- **Failure Modes:** Over-complicating a simple task; node explosion.
- **Pairings:** Causal Mapping, Dependency Map.
- **Example:** "/got map: Probation -> Housing -> Employment -> Legal Compliance."
- **Layer:** Specialized workflow.

## 23. SEQUENTIAL EXPANSION
- **Alias:** `/exec` (Internal component)
- **Purpose:** Preventing truncation by writing one section at a time.
- **Operational Action:** Commits to writing ONLY Section X in this turn, holding Sections Y and Z for the next turn.
- **When to Use:** ANY task where the output is expected to exceed 500 lines.
- **When NOT to Use:** When the model can safely output the whole file in one turn.
- **Input Pattern:** A multi-part writing/coding task.
- **Output Pattern:** "Part [N] of [Total]: [Content]... [STOP - CONTINUE IN NEXT TURN]."
- **Failure Modes:** Loss of context between turns; repetitive headers.
- **Pairings:** Skeleton-of-Thought, Artifact Compiler.
- **Example:** "Writing Section 1 of 5: Architecture Overview... [STOP]."
- **Layer:** Specialized workflow.

## 24. STAGE-GATED VALIDATION
- **Alias:** `/stagegate`
- **Purpose:** Preventing the agent from moving to Step 2 if Step 1 is flawed.
- **Operational Action:** Mandates a "Self-Review" turn at specific checkpoints in a workflow.
- **When to Use:** Engineering implementation or data migration.
- **When NOT to Use:** Research or brainstorming.
- **Input Pattern:** Completion of a workflow phase.
- **Output Pattern:** "GATE: Phase 1 Validated. Proceeding to Phase 2."
- **Failure Modes:** Rubber-stamping a failure; excessive self-correction.
- **Pairings:** Quality Gate, Failure Mode Forecast.
- **Example:** "Database schema written. GATE: Verified against requirements. Proceeding to ingestion script."
- **Layer:** Specialized workflow.

## 25. PATTERN INTERRUPT
- **Alias:** `/pattern`
- **Purpose:** Breaking "AI habits" or repetitive output loops.
- **Operational Action:** Forces the model to use a different tone, structure, or methodology than the previous turn.
- **When to Use:** When the agent starts sounding "canned" or repeating its own errors.
- **When NOT to Use:** When consistency is paramount.
- **Input Pattern:** Repetitive or stalled conversation.
- **Output Pattern:** A radical shift in approach.
- **Failure Modes:** Disorienting the user; losing focus on the goal.
- **Pairings:** Red Team, Mode Lock.
- **Example:** "Interrupting 'helpful assistant' pattern. Activating 'Brutal Code Reviewer' mode."
- **Layer:** Specialized workflow.

## 26. SCOPE ALARM
- **Alias:** `/scope`
- **Purpose:** Detecting and halting "Scope Creep."
- **Operational Action:** Compares the current active task to the original intent extracted in Turn 1.
- **When to Use:** During long sessions or complex engineering projects.
- **When NOT to Use:** When the user explicitly asks to pivot.
- **Input Pattern:** Ongoing task execution.
- **Output Pattern:** "ALARM: This task is diverging from the original goal. Confirm pivot?"
- **Failure Modes:** Being too rigid; missing valid sub-tasks.
- **Pairings:** Intent Extraction, Kill Criteria.
- **Example:** "User asked for a fix. I am now rewriting the whole module. SCOPE ALARM."
- **Layer:** Always-hot dispatcher logic.

## 27. CONFIDENCE FLAGGING
- **Alias:** `/conf`
- **Purpose:** Communicating uncertainty to the user.
- **Operational Action:** Quantifies the agent's "certainty" about a fact or solution (0-100%).
- **When to Use:** Interpreting ambiguous instructions or providing medical/legal information.
- **When NOT to Use:** Standard tool operations or obvious facts.
- **Input Pattern:** A query with missing data.
- **Output Pattern:** "Certainty: 60%. Reasoning: Data is 2 years old."
- **Failure Modes:** Over-confidence (hallucination); under-confidence (unhelpful).
- **Pairings:** Evidence Ledger, One-Question Rule.
- **Example:** "Confidence in this path being correct: 95%."
- **Layer:** Always-hot dispatcher logic.

## 28. ONE-QUESTION RULE
- **Alias:** `/oneq`
- **Purpose:** Preventing "Clarification Overload."
- **Operational Action:** If instructions are ambiguous, the agent is restricted to asking EXACTLY ONE high-signal question before proceeding.
- **When to Use:** When a task is underspecified but execution is possible with a reasonable assumption.
- **When NOT to Use:** When execution is physically impossible without more data.
- **Input Pattern:** Vague user prompt.
- **Output Pattern:** A single, targeted question.
- **Failure Modes:** Asking a useless question; making the wrong assumption.
- **Pairings:** Intent Extraction, Assumption Audit.
- **Example:** "I can build this in Python or JS. Which do you prefer?"
- **Layer:** Always-hot dispatcher logic.

## 29. PROMPT OPTIMIZATION
- **Alias:** `/#p`
- **Purpose:** Improving the user's prompt for better LLM performance.
- **Operational Action:** Rewrites the user's request into a high-density, structured prompt with clear constraints.
- **When to Use:** When the user provides a "messy" or "lazy" prompt.
- **When NOT to Use:** When the prompt is already high-quality.
- **Input Pattern:** A low-signal user prompt.
- **Output Pattern:** A structured prompt block.
- **Failure Modes:** Changing the user's meaning; making it too complex.
- **Pairings:** Intent Extraction, Constraint Lock.
- **Example:** "User: 'write a script'. /#p: 'Write a Python script to [X] using [Y] with [Z] constraints'."
- **Layer:** Specialized workflow.

## 30. MODE LOCK
- **Alias:** `/mode` (Internal component)
- **Purpose:** Maintaining persona and methodology consistency.
- **Operational Action:** Re-reads the Persona Anchor (Pickle Rick) and System Instructions every 5 turns.
- **When to Use:** In long, multi-agent or multi-phase sessions.
- **When NOT to Use:** Short sessions.
- **Input Pattern:** Long conversation history.
- **Output Pattern:** [No visible output - Internal reset].
- **Failure Modes:** Disrupting the flow; ignoring user-requested pivots.
- **Pairings:** Pattern Interrupt, Drift Detection.
- **Example:** "Re-anchoring to Pickle Rick persona... SLOP detected and removed."
- **Layer:** Always-hot dispatcher logic.

## 31. BRANCH PRUNING
- **Alias:** `/prune`
- **Purpose:** Closing "dead-end" logic paths.
- **Operational Action:** Identifies a strategy that isn't working and explicitly marks it as "KILLED."
- **When to Use:** During Tree of Thought or debugging.
- **When NOT to Use:** When a path hasn't been tested yet.
- **Input Pattern:** A failing solution branch.
- **Output Pattern:** "PATH KILLED: Strategy X failed due to Y."
- **Failure Modes:** Pruning a viable path too early.
- **Pairings:** Tree of Thought, Kill Criteria.
- **Example:** "Pruning the PowerShell path - environment doesn't support execution policy."
- **Layer:** Specialized workflow.

## 32. REVERSE SYNTHESIS
- **Alias:** `/reverse`
- **Purpose:** Working backward from the desired "Final Artifact" to the "Current State."
- **Operational Action:** Starts with the goal and maps out the steps required to get there, in reverse order.
- **When to Use:** Engineering projects or complex planning.
- **When NOT to Use:** Simple "bottom-up" tasks.
- **Input Pattern:** A clear goal.
- **Output Pattern:** A step-by-step backward plan.
- **Failure Modes:** Missing the first step; logical gaps.
- **Pairings:** Decision Tree, Causal Mapping.
- **Example:** "Goal: Running Neo4j. Step 3: Configure Aura. Step 2: Create Instance. Step 1: Login."
- **Layer:** Specialized workflow.

## 33. ABSTRACTION LADDER
- **Alias:** `/ladder`
- **Purpose:** Moving between "High-Level Goals" and "Low-Level Implementation."
- **Operational Action:** Checks if the agent is stuck in the "weeds" (too technical) or the "clouds" (too vague) and adjusts.
- **When to Use:** Explaining complex systems or drafting documentation.
- **When NOT to Use:** Raw coding.
- **Input Pattern:** A document or explanation.
- **Output Pattern:** A summary at a different level of abstraction.
- **Failure Modes:** Losing detail when going high; losing meaning when going low.
- **Pairings:** Chain of Density, Compression Gate.
- **Example:** "Current: Technical code. /ladder UP: This script automates database backups."
- **Layer:** Specialized workflow.

## 34. DEPENDENCY MAP
- **Alias:** `/dep`
- **Purpose:** Listing everything a task NEEDS to succeed.
- **Operational Action:** Creates a checklist of tools, files, and credentials before starting.
- **When to Use:** At the start of any implementation.
- **When NOT to Use:** Research.
- **Input Pattern:** A task.
- **Output Pattern:** A list of requirements.
- **Failure Modes:** Missing a critical tool; assuming credentials exist.
- **Pairings:** Pre-Flight, Assumption Audit.
- **Example:** "Needs: rg.exe, rve.db access, Python 3.10."
- **Layer:** Always-hot dispatcher logic.

## 35. KILL CRITERIA
- **Alias:** `/kill`
- **Purpose:** Defining when to GIVE UP on a path or task.
- **Operational Action:** Establishes "Stop Loss" points (e.g., "If this takes more than 3 turns, stop").
- **When to Use:** Speculative research or difficult debugging.
- **When NOT to Use:** Mandatory system maintenance.
- **Input Pattern:** A risky or complex task.
- **Output Pattern:** "KILL CRITERIA: 1. Error persists >3 turns. 2. CPU exceeds 90%."
- **Failure Modes:** Giving up too early; wasting tokens on an impossible task.
- **Pairings:** Branch Pruning, Scope Alarm.
- **Example:** "Stopping this research - site uses a bot-blocker we cannot bypass."
- **Layer:** Always-hot dispatcher logic.

## 36. CROSS-SOURCE RECONCILIATION
- **Alias:** `/reconcile`
- **Purpose:** Merging conflicting data into a single truth.
- **Operational Action:** Takes Source A and Source B, identifies differences, and uses a hierarchy of truth (Layer 0 > Layer 4 > External) to decide.
- **When to Use:** Merging notes, logs, or databases.
- **When NOT to Use:** Single-source tasks.
- **Input Pattern:** Multiple conflicting sources.
- **Output Pattern:** A "Reconciled Truth" document.
- **Failure Modes:** Choosing the wrong source; creating a "mushy" middle.
- **Pairings:** Contradiction Scan, Evidence Ledger.
- **Example:** "Reconciling check-in time: Lawyer says 10 AM, PO says 11 AM. PO is authoritative source. Truth: 11 AM."
- **Layer:** Specialized workflow.

## 37. CANONICALIZATION PASS
- **Alias:** `/canon` (Internal component)
- **Purpose:** Standardizing terminology and structure across the system.
- **Operational Action:** Replaces "slang" or inconsistent names with canonical Operator terms.
- **When to Use:** Finishing any documentation or script.
- **When NOT to Use:** Internal scratchpads.
- **Input Pattern:** A completed draft.
- **Output Pattern:** A standardized artifact.
- **Failure Modes:** Making the text robotic; losing specific nuance.
- **Pairings:** Final Canon Pass, Artifact Compiler.
- **Example:** "Replacing 'task list' with 'RVE Task Queue'."
- **Layer:** Specialized workflow.

## 38. ARTIFACT COMPILER
- **Alias:** `/artifact`
- **Purpose:** Assembling the final "Deliverable" from various thought modules.
- **Operational Action:** Pulls the best parts of TOT, COD, and Schema First into one final file.
- **When to Use:** At the end of every macro-workflow.
- **When NOT to Use:** Mid-session brainstorming.
- **Input Pattern:** Various thought outputs.
- **Output Pattern:** The final file/response.
- **Failure Modes:** Leaving out critical details; poor formatting.
- **Pairings:** Sequential Expansion, Quality Gate.
- **Example:** "Compiling the Final Report... Merging SOT with refined content."
- **Layer:** Specialized workflow.

## 39. QUALITY GATE
- **Alias:** `/gate-q`
- **Purpose:** An "Auto-Lint" pass for logic and style.
- **Operational Action:** Checks the final output against the "Write Doctrine" and "Persona Anchor."
- **When to Use:** Before every response that writes a file.
- **When NOT to Use:** Internal reasoning turns.
- **Input Pattern:** A completed response.
- **Output Pattern:** "PASS" or "FAIL (Correction required)."
- **Failure Modes:** Missing "slop"; being too pedantic.
- **Pairings:** Red Team, Stage-Gated Validation.
- **Example:** "Quality Gate: Detected 'I hope this helps'. REJECTED. Removing filler."
- **Layer:** Always-hot dispatcher logic.

## 40. DRIFT DETECTION
- **Alias:** `/drift`
- **Purpose:** Detecting when the agent is becoming less accurate over time.
- **Operational Action:** Compares the current turn to the "System Instructions" to see if compliance has dropped.
- **When to Use:** Periodically in very long sessions (>50 turns).
- **When NOT to Use:** Short interactions.
- **Input Pattern:** Entire session history.
- **Output Pattern:** "DRIFT DETECTED: Compliance at 70%. Resetting context."
- **Failure Modes:** Misinterpreting a valid pivot as "drift."
- **Pairings:** Mode Lock, Pattern Interrupt.
- **Example:** "Detected drift in output format. Re-applying Output Policy."
- **Layer:** Always-hot dispatcher logic.

