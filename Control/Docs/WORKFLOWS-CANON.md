# WORKFLOW CANON

## INTRODUCTION
This document defines the canonical workflows for the Operator system. A workflow is a sequenced combination of techniques designed to achieve a specific macro-goal.

---

## 1. UNIVERSAL ULTRA WORKFLOW (/ComboStatus)
- **Purpose:** The default high-intensity reasoning loop for any non-trivial task.
- **Ideal Use Cases:** Strategic planning, complex problem solving, high-stakes analysis.
- **Step Order:**
    1. **Pre-Flight:** Environment/Mission check.
    2. **Intent Extraction:** Disambiguate goal.
    3. **Causal Mapping:** Trace dependencies/ripples.
    4. **Tree of Thought:** Generate 3 parallel paths.
    5. **Deep Think:** Recursive reasoning on the chosen path.
    6. **Chain of Density:** Compress and refine the draft.
    7. **Final Canon Pass:** Format and standardize output.
- **Why this order?** It moves from grounding (Pre-Flight) to expansion (ToT) to focus (Deep Think) to refinement (CoD).
- **Artifacts:** Final synthesized response or file.
- **What NOT to do:** Skip grounding or rush to the final draft.
- **Loop/Retry:** Re-run if Quality Gate fails or user requests `/combostatus xN`.
- **Stop Conditions:** Completion of artifact or Kill Criteria met.
- **Downgrade to:** Standard Single Pass if task complexity is low.

## 2. CORPUS-TO-CANON SYNTHESIS (/synth-c)
- **Purpose:** Transforming raw data or messy notes into an authoritative canon.
- **Ideal Use Cases:** Organizing "Pile" directories, creating documentation from chat logs.
- **Step Order:**
    1. **Retrieval Grounding:** Scan all raw sources via ripgrep.
    2. **Contradiction Scan:** Identify data conflicts.
    3. **Cross-Source Reconciliation:** Resolve conflicts via truth hierarchy.
    4. **Schema First:** Define the output structure.
    5. **Chain of Density:** Fuse data into the schema.
    6. **Canonicalization Pass:** Standardize terminology.
    7. **Artifact Compiler:** Final assembly.
- **Why this order?** Ensures all data is identified and cleaned before it is structured.
- **Artifacts:** A `.md` or `.json` canon file.
- **What NOT to do:** Ignore contradictions or use unverified raw text.
- **Loop/Retry:** If new raw data is discovered, re-run reconciliation.

## 3. SYSTEM/ARCHITECTURE DESIGN (/design)
- **Purpose:** Designing robust technical systems.
- **Ideal Use Cases:** Database schema design, MCP server architecture, script ecosystems.
- **Step Order:**
    1. **Assumption Audit:** Surface hidden premises.
    2. **Causal Mapping:** Map system-wide impacts.
    3. **Graph-of-Thought:** Map the network of components.
    4. **Failure Mode Forecast:** Predict breaking points.
    5. **Schema First:** Define data/interface contracts.
    6. **Red Team:** Attack the design for holes.
    7. **Decision Tree:** Finalize execution flow.
- **Why this order?** Forces the model to understand the "ripple effects" and "failures" before defining the final structure.
- **Artifacts:** Architecture Decision Record (ADR) or design doc.
- **What NOT to do:** Start coding before Red Teaming the design.

## 4. LONG-FORM REPORT/CHAPTER (/long)
- **Purpose:** Generating high-volume content without truncation.
- **Ideal Use Cases:** Manuals, dossiers, multi-page project reports.
- **Step Order:**
    1. **Skeleton-of-Thought:** Map the full table of contents.
    2. **Retrieval Grounding:** Gather evidence for all sections.
    3. **Sequential Expansion:** Write section-by-section using Turn Chaining.
    4. **Stage-Gated Validation:** Check Section N before writing N+1.
    5. **Abstraction Ladder:** Ensure consistent tone across sections.
    6. **Artifact Compiler:** Merge all sections.
- **Why this order?** Prevents the model from trying to do too much in one turn (Anti-Truncation).
- **Artifacts:** Multi-section Markdown document.
- **What NOT to do:** Attempt to generate >500 lines in one go.

## 5. INGESTION-TO-DATABASE (/ingest)
- **Purpose:** Moving flat data into the Operator memory stack (SQL/Neo4j).
- **Ideal Use Cases:** Seeding onboarding data, migrating task logs, tool registry updates.
- **Step Order:**
    1. **Schema First:** Validate target DB structure.
    2. **Retrieval Grounding:** Clean and verify raw input.
    3. **Causal Mapping:** Check for existing records/conflicts.
    4. **Decision Tree:** Logic for Update vs. Insert.
    5. **Failure Mode Forecast:** Prepare for encoding/type errors.
    6. **Implementation Pass:** Execute the SQL/Cypher/Python.
    7. **Quality Gate:** Verify DB state post-ingest.
- **Why this order?** Protects database integrity by validating the plan before the write.
- **Artifacts:** Updated DB records + ingest log.
- **What NOT to do:** Bulk ingest without a conflict-resolution strategy.

## 6. FAILURE ANALYSIS / POST-MORTEM (/failure-audit)
- **Purpose:** Diagnosing and fixing recurrent system failures.
- **Ideal Use Cases:** Debugging broken loops, fixing path-law violations, analyzing truncated outputs.
- **Step Order:**
    1. **Evidence Ledger:** Catalog the exact failure symptoms.
    2. **Retrieval Grounding:** Check log files (`everything.db`, `errors.db`).
    3. **Deep Think:** Trace the logic to the root cause.
    4. **Assumption Audit:** Check what the failing script "takes for granted."
    5. **Red Team:** Verify that the "fix" doesn't introduce new bugs.
    6. **Delta Pass:** Report the specific code/protocol change.
- **Why this order?** Focuses on empirical evidence over guesswork.
- **Artifacts:** Post-mortem report + corrective patch.
- **What NOT to do:** Apply a "band-aid" fix without finding the root cause.

## 7. ENGINEERING / IMPLEMENTATION (/eng)
- **Purpose:** Writing functional, high-quality code.
- **Ideal Use Cases:** Feature implementation, script creation, automation.
- **Step Order:**
    1. **Dependency Map:** List required tools/libraries.
    2. **Constraint Lock:** Check for Path Law (lowercase tarot).
    3. **Sequential Expansion:** Build in logical modules.
    4. **Red Team:** Check for security/slop.
    5. **Stage-Gated Validation:** Run tests after every module.
    6. **Upgrade Capture:** Log discovered optimizations.
    7. **Final Canon Pass:** Clean up comments and formatting.
- **Why this order?** Ensures environment safety and incremental verification.
- **Artifacts:** Functional code + test report.

## 8. RESEARCH / DOSSIER (/synth-r)
- **Purpose:** Deep-dive investigation into a specific topic.
- **Ideal Use Cases:** Financial research, legal audit, tool comparison.
- **Step Order:**
    1. **Intent Extraction:** Define the research question.
    2. **Retrieval Grounding:** Exhaustive web/local search.
    3. **Contradiction Scan:** Identify conflicting reports.
    4. **Confidence Flagging:** Mark uncertain findings.
    5. **Chain of Density:** Fuse findings into a high-signal report.
    6. **Provenance Tagging:** Cite all sources.
- **Why this order?** Prioritizes sourcing and uncertainty management.
- **Artifacts:** High-density research report.

## 9. PROMPT OPTIMIZATION (/#p)
- **Purpose:** Turning weak instructions into high-performance prompts.
- **Ideal Use Cases:** Fixing failing sub-agent queries, refining workflows.
- **Step Order:**
    1. **Intent Extraction:** Find the "hidden goal."
    2. **Constraint Lock:** Identify required safety/logic rails.
    3. **Pattern Interrupt:** Remove conversational filler.
    4. **Abstraction Ladder:** Set the correct level of technical detail.
    5. **Canonicalization Pass:** Use standard Operator terminology.
- **Why this order?** Strips noise and adds structure based on intent.
- **Artifacts:** A refined prompt block.

## 10. DEBATE / RED-TEAM (/debate)
- **Purpose:** Stress-testing an idea or plan through adversarial dialogue.
- **Ideal Use Cases:** Challenging an architectural choice, verifying a complex plan.
- **Step Order:**
    1. **Assumption Audit:** Surface the premises.
    2. **Red Team:** Present 3 brutal counter-arguments.
    3. **Tree of Thought:** Explore the implications of the counter-arguments.
    4. **Cross-Source Reconciliation:** Find the "Steel-manned" synthesis.
    5. **Decision Tree:** Update the plan based on the debate.
- **Why this order?** Moves from destruction (Red Team) to constructive synthesis.
- **Artifacts:** "Battle-hardened" plan or decision.
