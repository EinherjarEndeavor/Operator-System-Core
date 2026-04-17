USE SUPERPOWERS.

We are continuing Step 0 on this repository.
First, pull the latest docs from branch `roadmap/step-0-operator-substrate`.
Then read these files in order:

1. `Control/Roadmap/README.md`
2. `Control/Docs/STEP-0-OPERATOR-SUBSTRATE-CANON.md`
3. `Control/Docs/STEP-0-MEMORY-ARCHITECTURE-CANON.md`
4. `Control/Docs/STEP-0-CAUSAL-MAP-AND-OPERATING-MODEL.md`
5. `Control/Docs/STEP-0-EXECUTION-ORDER-AND-DEFERRED-WORK.md`

After reading them, do not restart architectural brainstorming.
Do not treat RVE as the entire Step 0 target.
Treat RVE as an early consumer of the Operator substrate.

MISSION
Identify the highest unfinished Step 0 implementation work and execute it.
Bias toward real artifacts, schema work, registries, auditability, retrieval, and context export.

PRIORITY ORDER
1. canonical DB family trust
2. tool / MCP / extension / skill / environment registry
3. session archive + audit loop
4. artifact indexing
5. context export layer
6. continue RVE on top of the substrate

RULES
- use the docs above as build law
- ask focused questions only when truly blocked
- prefer implementation over more theory
- update roadmap docs if architecture or order materially changes
- keep outputs direct and operational

OUTPUT FORMAT
Return exactly:
1. Docs Read Confirmation
2. Highest Unfinished Workstream
3. What You Will Build In This Run
4. Clarification Gate Or `none`
5. Execution Result
6. Any Roadmap Update Needed Or `none`
