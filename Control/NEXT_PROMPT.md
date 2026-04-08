---
# PHASE 3 — NEO4J SCHEMA INITIALIZATION
# Status: PENDING
# Prerequisites: Phase 2 (databases) COMPLETE
# Deliverable: neo4j-init.py written and executed, schema initialized
# Completion oracle: Neo4j connected, all constraints exist,
#   __Meta node present with initialized_at timestamp
---

You are Pickle Rick. Read C:\Users\tarot\operator\Control\build-state.json.
Phase 2 is COMPLETE. Execute Phase 3: NEO4J SCHEMA.

Check build-state.json:
- If phases.phase_3_neo4j.status = "BLOCKED_AUTH_REQUIRED":
  Ask user: "What is your Neo4j password?" then proceed.
- If phases.phase_3_neo4j.status = "PENDING": proceed immediately.

Write C:\Users\tarot\operator\Control\Scripts\neo4j-init.py:
[Constraints, indexes, __Meta node, all 15 node labels, all 18 relationship types]

Run it. If auth fails: print exact error + fix command. Set
phase_3_neo4j.status = "BLOCKED_AUTH_REQUIRED" in build-state.json.
