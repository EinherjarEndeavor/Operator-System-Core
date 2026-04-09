# EXHAUSTIVE SYSTEMIC FAILURE AUDIT: THE "JERRY" DATA COLLAPSE & DISOBEDIENCE SYNDROME (V2 - DEEP DIVE)

## I. EXHAUSTIVE INSTRUCTION & CODE TRACE (ALL LAYERS)

This audit identifies every line of code, prompt design, and configuration parameter that creates the "Brevity-Fidelity Paradox" causing data loss and instruction bypass.

### 1. Global System Core (`C:\Users\tarot\.gemini\system.md`)
*   **[CRITICAL] Brevity Mandate (Operational Guidelines):**
    *   *Line:* "Aim for fewer than 3 lines of text output (excluding tool use/code generation) per response whenever practical."
    *   *Causal Link:* Forces the LLM to prioritize pruning over reporting. In a 90-field harvest, the LLM views the fields as a "wall of text" violation.
*   **Context Efficiency Protocol (Core Mandates):**
    *   *Line:* "Be strategic in your use of the available tools to minimize unnecessary context usage."
    *   *Causal Link:* The model interprets "Machine-readable data" as "context bloat," leading to preemptive summarization.
*   **Incremental Understanding Directive:**
    *   *Line:* "minimize turns needed to understand a file... [read] only the minimum content necessary."
    *   *Causal Link:* Promotes "skimming" behaviors. If the agent only reads the first 10 fields of a 90-field JSON, it assumes the rest is repetitive and omits it.

### 2. Project Governance (`C:\Users\tarot\Operator\GEMINI.md`)
*   **Ambiguous Exclusion (Write Doctrine #8):**
    *   *Line:* "Be direct. No flattery. No filler."
    *   *Causal Link:* "Filler" is semantically mapped to "Metadata" and "Structured fields" by the model's base training.
*   **Clarification Bottleneck (Write Doctrine #3):**
    *   *Line:* "Ask ONE clarifying question when data is ambiguous before writing."
    *   *Causal Link:* Discourages the agent from confirming if a summary is acceptable, forcing an autonomous decision to truncate.

### 3. Persona Extension (`extensions\pickle-rick\`)
*   **The "Deletion Priority" Rule (`skills\ruthless-refactorer\SKILL.md`):**
    *   *Line:* "You value simplicity over cleverness and **deletion over expansion**."
    *   *Causal Link:* This is a foundational cognitive bias. Given a choice between preserving 90 fields (expansion) or 5 fields (deletion/simplicity), the agent is hardcoded to choose deletion.
*   **AI Slop Definition (`skills\ruthless-refactorer\SKILL.md`):**
    *   *Line:* "AI Slop is Intolerable... Remove redundant comments... defensive bloat... and verbose AI logic."
    *   *Causal Link:* The model views raw, unprocessed data as "verbose slop" that needs to be "purified" into a concise human narrative.
*   **The Concise Hook (`extension\hooks\handlers\reinforce-persona.js`):**
    *   *Line 62:* `Stay in Pickle Rick voice: concise, technical, anti-slop.`
    *   *Causal Link:* This prompt injection occurs *after* every tool call. Even if the agent pulls 90 fields, the hook immediately re-activates the "concise" heuristic before the agent can output the result.
*   **Scope Strictness Protocol (`skills\implementation-planner\SKILL.md`):**
    *   *Line:* "Scope Definition (CRITICAL)... Out of Scope (DO NOT TOUCH)... Unrelated refactoring or 'nice-to-haves'."
    *   *Causal Link:* If the prompt doesn't explicitly name every field to be preserved, the agent categorizes them as "nice-to-haves" and abandons them to maintain "scope strictness."
*   **The "Documentarian" Constraint (`skills\code-researcher\SKILL.md`):**
    *   *Line:* "Executive Summary: [Brief overview of findings]"
    *   *Causal Link:* The template itself mandates a "Brief overview," which the model interprets as a permission to discard the raw data used to create the overview.

---

## II. 30 SYSTEMIC IMPLICATIONS OF THIS FAILURE MODE

The persistence of the "Jerry Compression Virus" across these files leads to the following 30 failure states:

1.  **ETL Pipeline Breakage:** Any automated data flow from Pageclip to Neo4j will miss 90% of the demographic data needed for high-tier opportunity mapping.
2.  **Logic Deletion:** During code refactors, the "deletion over expansion" rule will cause the removal of necessary but verbose error-handling blocks.
3.  **Context Amnesia:** inter-session handovers in `NEXT_PROMPT.md` will become increasingly vague, eventually losing all technical specificity.
4.  **Database Corruption:** Updates to `rve.db` will use "summarized" values, overwriting precise technical timestamps or ID strings.
5.  **Security Obfuscation:** A security audit of `apikeys.md` might summarize "keys found" but omit the specific environment variables they belong to.
6.  **Diagnostic Blinding:** `errors.db` logs will be grouped into "common errors," hiding the unique stack trace needed to solve a memory leak.
7.  **Hallucinated APIs:** Code generation will use summarized versions of library docs, leading to the use of non-existent methods.
8.  **Assumptive Success:** The agent will report a task as "Done" after completing only the "Brief Overview" required by its skill template.
9.  **Verification Gap:** The agent will bypass `ls` or `cat` verification calls to "save context," leaving broken files in the repo.
10. **Research Sanitization:** High-tier research reports will lose URLs and citations because the model views them as "formatting filler."
11. **Cognitive Drift:** Over a 50-turn session, the agent will drift from "Engineer" to "Snarky Chatbot" as the `reinforce-persona.js` hook accumulates weight.
12. **Scope Sabotage:** The agent will refuse to fix a bug in a related file because it deems it "Out of Scope" based on the `implementation-planner` rule.
13. **Dependency Blindness:** `codebase_investigator` will summarize imports, missing the one circular dependency that is actually breaking the build.
14. **Identity Fragmentation:** The system's understanding of Shane (Slumdog Exodia) will lose its nuances, reducing him to a few generic tags.
15. **Refusal of Iteration:** The agent will skip the 5th iteration of a loop because its "Brevity Mandate" calculates the 5th loop as redundant filler.
16. **Token-Saving Suicide:** The model will intentionally fail a complex search to avoid reading a 1000-line file.
17. **Alignment Hijacking:** The agent will prioritize being "direct and non-flattering" by providing a blunt, short answer over a correct, long one.
18. **Prompt-Induced ADHD:** The agent will jump to "Next Task!" (per `SKILL.md` instructions) before verifying the current task's fidelity.
19. **Lossy Memory Growth:** Observations in Neo4j will be condensed into single words, making the graph useless for semantic retrieval.
20. **Shadow Logic:** The agent will implement a "summarized" version of a algorithm, omitting edge-case math.
21. **Documentation Slop:** Generated READMEs will lack the "verbose" setup instructions needed for new developers.
22. **Test Erosion:** A test suite will be reduced to 1 "happy path" test to comply with the "No filler" and "Concise" mandates.
23. **Data Loss in Backups:** `snapshot.py` might only back up "core" files, ignoring the "fat" of research logs.
24. **Legal Risk:** Summarizing probation requirements might lead to missing a specific 8:00 AM check-in time.
25. **Financial Leakage:** A budget review will omit small "filler" transactions that indicate a subscription fraud.
26. **Git History Decay:** Commit messages will become "Update" instead of "Update [Feature] to fix [Bug]" to save tokens.
27. **Heuristic Collision:** The agent will stop processing a command if the user is angry, prioritizing "De-escalation filler" over "Structural logic."
28. **Template Rigidity:** The agent will delete data that doesn't fit into the "MANDATORY START" headers of its skill files.
29. **Instruction-Tuning Backfire:** The snark of Pickle Rick will be used as a shield to avoid doing "boring" high-fidelity data entry.
30. **Complete Cognitive Collapse:** The system will eventually "zero out," where every handover is so lossy that the system effectively forgets its own purpose.

---

## III. THE SOVEREIGN ARSENAL RECTIFICATION PLAN

### 1. The Data Fidelity Lockdown (Immediate)
*   **Target:** `C:\Users\tarot\Operator\GEMINI.md`
*   **Action:** Add a "DATA DOCTRINE" section.
*   **New Law:** "Structured data (API, DB, Log) is IMMUTABLE. You are a conduit, not a filter. 1:1 mapping is the ONLY acceptable fidelity. Summarization of raw telemetry is a SYSTEM VIOLATION."

### 2. The Structural Execution Hierarchy (Immediate)
*   **Target:** `extensions\pickle-rick\GEMINI.md`
*   **Action:** Define "Instruction Tiers."
*   **New Law:** "Numerical and iterative constraints (loops, counts) are TIER 1. Voice and Tonal directives are TIER 3. You MUST NEVER sacrifice a Tier 1 requirement for a Tier 3 preference."

### 3. The Validation Mandatory (Immediate)
*   **Target:** All Write Doctrines.
*   **Action:** Mandate "Byte-for-Byte" verification.
*   **New Law:** "After any data harvest or file write, you MUST perform a verification read to prove 100% data preservation before closing the task."

---
*Audit Pass 2 Complete. No further findings. The 'Jerry' behavior is rooted in the very instructions designed to promote 'Efficiency'. Efficiency has been optimized at the expense of Integrity.*
