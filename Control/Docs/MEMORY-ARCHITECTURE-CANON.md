# MEMORY ARCHITECTURE CANON (v1.0)
## Authority: Sovereign Engineering | Status: ACTIVE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 1: LAYER STACK DEFINITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### LAYER 0: ACTIVE BUFFER (WORKING)
- **Purpose:** Immediate execution state, identity anchors, and rules of engagement.
- **Storage:** LLM Context Window + `GEMINI.md` (Global/Project).
- **Belongs:** Current goal, constraints (curfew/legal), behavioral mandates, recent 5-10 turns.
- **Must NOT Go:** Raw data tables, large document lists, long-term project archives.
- **Retrieval:** Always hot-loaded on session start.
- **Promotion:** Successful patterns identified here move to Layer 2/3.

#### LAYER 1: EPISODIC (LOGS)
- **Purpose:** Append-only history of actions, search queries, and session traces.
- **Storage:** SQLite (`everything.db`).
- **Belongs:** Tool execution logs, `grep` results, session metadata, achievement log.
- **Must NOT Go:** Canonical identity facts, specific project task lists.
- **Retrieval:** Via session history search or automated post-session audit.
- **Promotion:** Insights extracted from actions move to Layer 2 (Patterns).

#### LAYER 2: RELATIONAL (GROUND TRUTH)
- **Purpose:** Atomic facts, structured data, and formula-driven entities.
- **Storage:** SQLite (`lifestate.db`, `rve.db`, `rematch.db`, `arsenal.db`).
- **Belongs:** Profile facts, task objects, habit streaks, project state, legal obligations.
- **Must NOT Go:** Unstructured brainstorming, narrative journal text, semantic maps.
- **Retrieval:** Exact SQL queries based on UUID or category.
- **Promotion:** Entities validated as "Axioms" move to Layer 4.

#### LAYER 3: SEMANTIC (CONNECTIONS)
- **Purpose:** Non-linear relationships, pattern clustering, and cross-domain links.
- **Storage:** Neo4j Graph Database.
- **Belongs:** Entity-Link-Entity maps (e.g., "PO" -> "monitors" -> "residencies").
- **Must NOT Go:** Temporal logs, atomic values (e.g., specific dates), raw text files.
- **Retrieval:** Cypher queries for pattern detection or "Sensei" reflections.
- **Promotion:** Clusters with high density move to Layer 4 (Synthesized Wisdom).

#### LAYER 4: SYNTHESIZED (CANON)
- **Purpose:** High-density doctrine, permanent knowledge, and processed wisdom.
- **Storage:** Obsidian Vault (`Vault/`) + `Control/Docs/` (.md files).
- **Belongs:** Finalized PRDs, "Beautiful" failure audits, recovery doctrine, tool tutorials.
- **Must NOT Go:** Raw task data, unfinished drafts, conversational noise.
- **Retrieval:** Semantic search or direct file read.
- **Promotion:** Finality. Becomes foundational logic for Layer 0.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 2: PROMOTION RULES (THE FORGE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. **Ingestion:** Raw text enters `submissions/` or `Tier 1` context.
2. **Atomic Harvest:** AI identifies Facts (Tier 2), Tasks (Tier 2), or Links (Tier 3).
3. **Red-Team Validation:** AI checks for conflict against existing Tier 2/4 data.
4. **User-in-the-Loop:** User confirms commit via `CONFIRM-MERGE` or similar directive.
5. **Persistence:** Data is written to DBs. The raw source is archived/tagged.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 3: DUPLICATION PREVENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. **Exact-Match First:** Before any write, a query must check for existing `id`, `hash`, or `title`.
2. **No Overwrite by Default:** All manual synthesis docs must be versioned (`_v2.md`) or use `append` logic unless `overwrite` is explicitly commanded.
3. **Hash Auditing:** Future implementation will include a `hash` field in all Tier 2 tables to prevent redundant ingestion of the same file content.
