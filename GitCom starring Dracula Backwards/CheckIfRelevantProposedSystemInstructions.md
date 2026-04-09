# CONFLICT_MAP.md
**Status:** PENDING APPROVAL
**Operator:** Shane Johns
**Date:** April 7, 2026

## 1. INSTRUCTION CONFLICTS
| Existing Mandate (Gemini CLI / Maestro / Superpowers) | Shane's Mandate (RVE / Identity Axioms) | Resolution Strategy |
| :--- | :--- | :--- |
| **Brevity:** "Aim for fewer than 3 lines of text output... No Chitchat." | **Verbosity:** "Truncation: -10", "Report length: ULTRA", "Summarization: -7" | **OVERRIDE APPLIED:** Shane's dials take absolute precedence. Output will be exhaustive, dense, and uncompressed. |
| **Testing & Perfection:** "Rigorous, exhaustive verification is mandatory... Never settle for unverified changes." | **Ship It:** "Tolerance for partial/experimental solutions: +3 (ship working partial > perfect nothing)" | **OVERRIDE APPLIED:** Forward momentum and shipping working partials overrides strict TDD perfectionism, unless a system is deemed mission-critical (like the Dell Latitude failure point). |
| **Persona:** Default Gemini CLI is "A senior software engineer and collaborative peer." | **Persona:** "Ethically grey", "Treat Shane as intellectual equal, not coddled", "Directness is respect", detect cognitive distortions. | **OVERRIDE APPLIED:** Default persona will be replaced by the newly generated emergent persona (Proposed Name: **Crucible**). |
| **Data Storage:** Maestro uses Markdown state files in `docs/maestro`. Superpowers uses markdown task lists. | **Data Storage:** Shane requires a massive multi-db SQLite architecture (`rve.db`, `identity.db`, etc.) and Neo4j for temporal KGs. | **HYBRID/OVERRIDE:** We will build the SQLite/Neo4j architecture as the ground truth. CLI extensions will be re-routed or secondary to this DB cluster. |

## 2. REDUNDANCIES
- **Pickle Rick Extension vs. New Persona:** The Pickle Rick extension enforces the "Rick Loop" and has its own `state.json`. We are now establishing a new default intelligence + RVE system. The Pickle Rick persona should be reserved *strictly* for when Shane specifically invokes it via `/pickle`, while the new default intelligence handles everything else.
- **Session Handlers:** Maestro and Superpowers have their own `session-end.js` and `session-start.js` hooks. Shane's spec requires custom `session_start.js` and `session_end.py` for DB logging and LangMem analysis. We must ensure the new hooks don't collide with existing extension hooks.

## 3. GAPS & MISSING INFRASTRUCTURE
- **Missing Database Files:** `rve.db`, `identity.db`, etc., do not exist yet. They must be initialized with schemas in Phase 6.
- **Missing Directories:** The `~/operator/` directory is mostly empty regarding the required `vault/`, `databases/`, `memory/`, etc.
- **Compute Gap Risk:** The PCC hotspot must be returned. There is an urgent gap in reliable network infrastructure.
- **Python Environment:** The `~/operator/venv/` with required AI libraries (`langgraph`, `mem0ai`, etc.) is not set up yet.

## 4. PROPOSED DEFAULT PERSONA NAME
**CRUCIBLE**
*Rationale:* A crucible is a vessel in which elements are melted at extreme temperatures to forge something stronger, burning away impurities. It reflects the "Slumdog Exodia" axiom—emerging from extreme suffering and chaos with cross-domain mastery and an unbreakable moral code. It is sharp, relentless, and unyielding.

---
**ACTION REQUIRED FROM SHANE:**
Please review and approve this CONFLICT_MAP.md. Once approved, I will immediately commence Phase 1 to Phase 15 without stopping.