# MEMORY ARCHITECTURE CANON (v1.1)
## Authority: Sovereign Engineering | Status: ACTIVE | QC Pass: 2026-04-09

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 1: IMPLEMENTATION STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### A. CURRENTLY IMPLEMENTED (ACTIVE)
- **TIER 0 (WORKING):** LLM Context + `GEMINI.md` (Global/Project).
- **TIER 1 (EPISODIC):** SQLite (`everything.db`). History tracking.
- **TIER 2 (RELATIONAL):** SQLite (`lifestate.db`, `rve.db`). Fact/Task ground truth.
- **TIER 4 (SYNTHESIZED):** Obsidian Vault (`Vault/`) + `.md` docs in `Control/Docs/`.

#### B. RECOMMENDED NEAR-TERM (PHASE 1 REPAIR)
- **TIER 3 (SEMANTIC):** Neo4j Graph Database. (Required for non-linear pattern matching).
- **TIER 2 EXPANSION:** `arsenal.db` (Tooling), `rematch.db` (Opportunities).

#### C. DEFERRED / OPTIONAL (FUTURE)
- **VECTOR LAYER:** ChromaDB / Qdrant. (Not required until Vault exceeds 1,000+ files).
- **AGENTIC MEMORY:** Mem0 / Zep. (Deferred until multi-agent orchestration is stable).
- **STATEFUL REPL:** LangGraph / Temporal. (Deferred).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 2: RETRIEVAL & PRIORITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**SEMANTIC RETRIEVAL STRATEGY: HYBRID (SQL-FIRST)**
1. **SQL-FIRST (Tier 2):** Exact lookups for IDs, dates, legal constraints, and status.
2. **NEO4J-SECOND (Tier 3):** Relational discovery (e.g., "Find all people linked to education").
3. **VAULT-THIRD (Tier 4):** Contextual grounding and doctrinal synthesis.

**MINIMUM VIABLE STACK (CURRENT PHASE):**
- Tier 0 (Working) + Tier 2 (Relational/SQLite) + Tier 4 (Synthesized/Obsidian).
- *Note: Neo4j is excluded from MVS until routing failure is resolved.*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### SECTION 3: PROMOTION RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. **Ingestion:** Raw text enters `submissions/`.
2. **Atomic Harvest:** AI identifies Facts (Tier 2), Tasks (Tier 2), or Links (Tier 3).
3. **Validation:** Conflict check against existing canonical data.
4. **Commit:** Data written to SQLite. Raw source moved to `HarvestedSubmissions/`.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
