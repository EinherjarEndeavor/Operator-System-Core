# MEMORY-ROUTING PROTOCOL (v1.0)
## Status: ACTIVE | Authority: Sovereign Engineering
## Purpose: Eliminate Truncation; Standardize Canonical Ingestion; Enforce Data Fidelity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 1: ACTIVE MEMORY TIERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Tier | Name | Medium | Persistence | Activation |
| :--- | :--- | :--- | :--- | :--- |
| **0** | **Working** | Context Window (LLM) | Volatile | Current Session |
| **1** | **Buffer** | `CURRENT_FOCUS.md` / `.tmp` | Semi-Persistent | Injected on Start |
| **2** | **Relational** | SQLite (`lifestate.db`, `rve.db`) | Permanent | SQL Queries (Exact) |
| **3** | **Semantic** | Neo4j Graph | Permanent | Cypher (Relational) |
| **4** | **Synthesized**| Obsidian Vault (`Vault/`) | Permanent | RAG / File Read |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 2: THE ROUTING MATRIX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Data Type | Primary Destination | Table / Path | Integrity Rule |
| :--- | :--- | :--- | :--- |
| **Fact** | `lifestate.db` | `profile_facts` | 1:1 Fidelity; No Summary |
| **Constraint** | `lifestate.db` | `constraints_registry`| Auto-flag on Plan Mode |
| **Preference** | `settings.db` | `user_preferences` | Persistence across sessions |
| **Project** | `rve.db` | `projects` | Linked to `tasks` |
| **Task** | `rve.db` | `tasks` | Weighted RVE Score |
| **Pattern** | `lifestate.db` | `patterns` | Requires 3+ observations |
| **Inference** | `lifestate.db` | `inferences` | Mark `estimated_fields=1` |
| **Doctrine** | `GEMINI.md` | Global / Project | Verified via CONFIRM-MERGE |
| **Source** | `everything.db` | `actions` / `search_log` | URL + Timestamp + Hash |
| **Tool** | `arsenal.db` | `registry` | Flagged LEARNED/ACTIVE |
| **Relationship** | Neo4j | (Node-Link-Node) | Semantic mapping only |
| **Event** | `everything.db` | `history` | Append-only; No delete |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 3: CANONICALITY STATES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. **CANONICAL:** Verified truth. Resides in SQL primary keys or `GEMINI.md`. Cannot be altered without explicit user directive.
2. **PROVISIONAL:** Raw data from `submissions/` or `HarvestedSubmissions/`. Awaiting audit.
3. **INFERRED:** AI-generated patterns or psychological profiles. Must be flagged as "estimated" until promoted.
4. **DEPRECATED:** Obsolete data. Moved to `BrainArchive/` or marked `status='inactive'`. NEVER deleted.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 4: PROMOTION RULES (THE FORGE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**The Workflow: Raw File -> Audit -> Candidate -> Validated -> Committed Memory**

1. **INGESTION:** Raw text is placed in `submissions/`.
2. **HARVESTING:** `LLM-AIx` pipeline (or `coder` agent) extracts atomic Facts, Tasks, and Axioms.
3. **AUDIT:** AI Red-Teams the extraction against existing DBs to prevent duplication.
4. **VALIDATION:** AI presents "Proposed Deltas" to the user for one-click approval.
5. **COMMIT:** Data is written to SQLite/Neo4j. The raw file is moved to `HarvestedSubmissions/processed/`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 5: DUPLICATION & RETRIEVAL RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- **NO-OVERWRITE POLICY:** When updating synthesis docs, use versioned appends. NEVER overwrite a 100KB file with a 9KB summary.
- **SQL-FIRST RETRIEVAL:** Always query SQLite for IDs, Dates, and Constraints before attempting "Semantic Search."
- **THE 15KB CAP:** Never attempt to output >15KB of text in a single chat turn. If volume is required, write a **Factory Script** to assemble the document in segments.
- **DENSITY CHECK:** Every "Canon" document must undergo a "Semantic Density Audit." Word-count-to-Information ratio must exceed 0.8.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 6: IMMEDIATE INGESTION TARGETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. `submissions/PHALANX_35.txt` -> Extract Tasks/Identity Axioms.
2. `GitCom starring Dracula Backwards/DIOGENES ONBOARDING.md` -> Fully populate `identity` and `values` tables.
3. `HarvestedSubmissions/AI_Assistant_Calibration_Profile.md` -> Commit to `settings.db`.
4. `re-match-default.csv` -> Seed `rematch.db`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 7: THE SOVEREIGN FACTORY (LIMITLESS GEN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For documents requiring "Limitless Scale" (e.g., The Second Wind Recovery Manual):
- **Phase A:** Sequential Extraction (1:1 harvesting of notes).
- **Phase B:** The Skeleton (High-density outline).
- **Phase C:** The Segmenter (Python script generates 5KB chunks sequentially).
- **Phase D:** The Assembler (Merges chunks with cross-referenced headers).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
