# SLASH COMMAND CANON

## 1. OVERVIEW
This document defines the canonical slash command set for the Operator system. Commands are categorised into Micro-Techniques, Macro-Workflows, Modes, and Utilities.

---

## 2. COMMAND REGISTRY

| Command | Type | Target Technique/Workflow | Default Output |
| :--- | :--- | :--- | :--- |
| `/preflight` | Micro | 1. Pre-Flight | "GO/NO-GO" Assessment |
| `/intent` | Micro | 2. Intent Extraction | Single sentence intent. |
| `/retrieve` | Micro | 3. Retrieval Grounding | List of source paths/lines. |
| `/lock` | Micro | 4. Constraint Lock | "LOCKED" or "UNLOCKED." |
| `/map` | Micro | 5. Causal Mapping | Downstream impact list. |
| `/tot` | Micro | 6. Tree of Thought | 3 Parallel solution branches. |
| `/dt` | Micro | 7. Deep Think | Recursive reasoning result. |
| `/cod` | Micro | 8. Chain of Density | High-signal paragraph. |
| `/red` | Micro | 9. Red Team | Adversarial critique. |
| `/evidence` | Micro | 10. Evidence Ledger | Table: Claim | Source | Status. |
| `/contra` | Micro | 11. Contradiction Scan | List of detected conflicts. |
| `/assume` | Micro | 12. Assumption Audit | List of active premises. |
| `/schema` | Micro | 13. Schema First | Technical schema definition. |
| `/failure` | Micro | 14. Failure Mode Forecast | 3 Failure modes + mitigations. |
| `/provenance` | Micro | 15. Provenance Tagging | Metadata block at the end. |
| `/delta` | Micro | 16. Delta Pass | Concise diff or change log. |
| `/gate` | Utility | 17. Compression Gate | "Handover" artifact. |
| `/decision` | Micro | 18. Decision Tree | If/Then flowchart or list. |
| `/upg` | Utility | 19. Upgrade Capture | "UPGRADE DETECTED" report. |
| `/canonize` | Micro | 20. Final Canon Pass | Hardened permanent file. |
| `/sot` | Macro | 21. Skeleton-of-Thought | Outline with placeholders. |
| `/got` | Micro | 22. Graph-of-Thought | Mermaid diagram/Node map. |
| `/exec` | Mode | 23. Sequential Expansion | Turn Chaining [Part N of N]. |
| `/stagegate` | Utility | 24. Stage-Gated Validation | "GATE: Phase X Validated." |
| `/pattern` | Mode | 25. Pattern Interrupt | Radical shift in approach. |
| `/scope` | Utility | 26. Scope Alarm | "ALARM: Scope Creep." |
| `/conf` | Utility | 27. Confidence Flagging | "Certainty: X%." |
| `/oneq` | Mode | 28. One-Question Rule | Single targeted question. |
| `/#p` | Macro | 29. Prompt Optimization | Structured prompt block. |
| `/mode` | Mode | 30. Mode Lock | Internal reset. |
| `/prune` | Micro | 31. Branch Pruning | "PATH KILLED" report. |
| `/reverse` | Macro | 32. Reverse Synthesis | Backward step-by-step plan. |
| `/ladder` | Micro | 33. Abstraction Ladder | Adjusted-level summary. |
| `/dep` | Utility | 34. Dependency Map | Requirement checklist. |
| `/kill` | Utility | 35. Kill Criteria | "Stop Loss" points. |
| `/reconcile` | Macro | 36. Cross-Source Reconciliation | Reconciled Truth artifact. |
| `/canon` | Micro | 37. Canonicalization Pass | Standardised artifact. |
| `/artifact` | Macro | 38. Artifact Compiler | Final assembly. |
| `/gate-q` | Utility | 39. Quality Gate | "PASS" or "FAIL." |
| `/drift` | Utility | 40. Drift Detection | "DRIFT DETECTED" report. |

---

## 3. MACRO-COMMAND BUNDLES

### `/combostatus [xN]`
- **Workflow:** 1. Universal Ultra Workflow.
- **Components:** 1, 5, 6, 7, 8.
- **Output:** Final synthesized artifact + Provenance.

### `/synth-c`
- **Workflow:** 2. Corpus-to-Canon Synthesis.
- **Components:** 3, 11, 36, 13, 8, 37, 38.
- **Output:** Permanent Canon file.

### `/synth-r`
- **Workflow:** 8. Research / Dossier.
- **Components:** 2, 3, 11, 27, 8, 15.
- **Output:** High-density research report.

### `/ingest`
- **Workflow:** 5. Ingestion-to-Database.
- **Components:** 13, 3, 5, 18, 14, 7, 39.
- **Output:** DB records + log.

### `/long`
- **Workflow:** 4. Long-form Report.
- **Components:** 21, 3, 23, 24, 33, 38.
- **Output:** Multi-section Markdown.

### `/eng`
- **Workflow:** 7. Engineering / Implementation.
- **Components:** 34, 4, 23, 9, 24, 19, 20.
- **Output:** Functional code + test report.

### `/design`
- **Workflow:** 3. System / Architecture Design.
- **Components:** 12, 5, 22, 14, 13, 9, 18.
- **Output:** ADR / Design Doc.

### `/exec`
- **Workflow:** Mode for sequential task execution.
- **Components:** 23.
- **Output:** Turn-by-turn section writing.

### `/debate`
- **Workflow:** 10. Debate / Red-Team.
- **Components:** 12, 9, 6, 36, 18.
- **Output:** Battle-hardened plan.

---

## 4. PERSISTENCE POLICY
All commands listed here are stored in Tier 4 memory. On invocation, the agent uses ripgrep (`grep_search`) to locate the detailed instruction in `TECHNIQUES-CANON.md` or `WORKFLOWS-CANON.md` before execution.

This command set is safe to keep outside active context because it follows the **Halt-and-Retrieve** dispatcher protocol.
