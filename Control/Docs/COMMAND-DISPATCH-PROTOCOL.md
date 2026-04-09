# COMMAND DISPATCH PROTOCOL

## 1. ARCHITECTURAL OVERVIEW
This document defines the Canonical Command Dispatch System for the Operator environment. To preserve the Tier 1 Working Memory (Context Window), detailed cognitive techniques, workflows, and slash commands DO NOT live in the active system prompt.

Instead, they are stored in Tier 4 (Vault/Docs) and retrieved dynamically upon invocation.

## 2. MEMORY LAYERS
- **Layer 0 (Working Memory / GEMINI.md):** Contains ONLY the Dispatcher Rule, alias routing, and output policy.
- **Layer 4 (Storage / Docs):** Contains `SLASHCOMMANDS-CANON.md`, `WORKFLOWS-CANON.md`, and `TECHNIQUES-CANON.md`.

## 3. THE DISPATCH SEQUENCE
When the user inputs a command formatted as `/command` (or its alias):

1. **HALT AND RETRIEVE:** The agent must NOT guess the command's behavior based on its name. The agent must immediately use `grep_search` or `read_file` to locate the command definition in `Control/Docs/SLASHCOMMANDS-CANON.md` or `Control/Docs/WORKFLOWS-CANON.md`.
2. **LOAD INTO CONTEXT:** The agent reads the specific step-by-step instructions for that command.
3. **INTERNAL EXECUTION:** The agent executes the technique or workflow internally. The agent MUST NOT dump its chain-of-thought, reasoning, or intermediate steps to the user interface unless the command explicitly dictates it (e.g., if a trace is requested).
4. **LOOP RESOLUTION (xN):** If the command includes a multiplier (e.g., `/combostatus x3`), the agent executes the ENTIRE sequence end-to-end 3 times. The output of cycle $N$ becomes the input state for cycle $N+1$.
5. **VISIBLE OUTPUT:** The agent emits ONLY the final synthesized artifact or requested data structure.

## 4. ANTI-SLOP & OUTPUT POLICY
- **No Theatrical Filler:** Never output "I will now execute the command" or "Here is the result." 
- **No Vague Language:** Execute workflows with absolute determinism.
- **Provenance:** If a command alters source data or synthesizes multiple sources, the final output must briefly cite the origin structures (Provenance Tagging).
- **Scope Discipline:** The agent must only execute the exact parameters of the workflow. Do not expand the scope of the task unless the workflow explicitly requires an expansion step (e.g., Tree of Thought).

## 5. REGISTRY RESOLUTION
If a command is not found in the primary Markdown canons, the agent is authorized to query the `arsenal.db` SQLite database to check if the command has been migrated to the structured tool registry.