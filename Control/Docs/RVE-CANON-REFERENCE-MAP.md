# RVE CANON REFERENCE MAP

Status: Active reference index
Purpose: Make it obvious which existing documents are authoritative for which RVE concerns so implementation does not depend on memory, vibes, or random file hunting.

---

## 1. Core rule

RVE documentation should not be treated as one undifferentiated pile.
Different documents have different roles.

Use this map to determine which file is authoritative for which question.

---

## 2. Authority order for RVE implementation

### Tier 1 — Active implementation canon
Use these first when building or operating RVE.

1. `Control/Docs/RVE-FEATURE-DRIVEN-CANON-SPEC.md`
   - current MVP contract
   - state machine
   - onboarding rules
   - ranking and scheduling contract
   - minimum operational commands

2. `Control/Docs/RVE-DIFF-ROLLOUT-VS-CANON.md`
   - missing mechanics to patch forward from the original rollout
   - what to add, keep, or defer

3. `Control/ProposedDeltas/DELTAS_FINAL_POPULATION_SOURCE.md`
   - strongest current population source for profile truth, projects, tasks, contacts, axioms, and doctrine candidates

### Tier 2 — Historical design authority / deeper rationale
Use these when Tier 1 is too thin or when you need the original intent.

4. `GitCom starring Dracula Backwards/RVE Mycroft ReMatch Tool & Theory Pile/RVE Rollout.md`
   - original concept development
   - why the system should work the way it does
   - checkpoint/assistant/planning logic
   - broader self-teaching and life-OS rationale

5. `Control/Docs/RVE-MASTER-BRIEFING.md`
   - strong build-contract ideas
   - table schemas and commands
   - optional module ideas
   - useful implementation details that may exceed current MVP

### Tier 3 — Cross-cutting control docs
Use these when RVE touches truth routing, project priority, or corpus integration.

6. `Control/Docs/PROJECT-PORTFOLIO-CANON.md`
   - where RVE sits in the total system
   - why it outranks higher-tier projects right now

7. `Control/Docs/TRUTH-ROUTING-CANON.md`
   - what belongs in `lifestate.db`, what belongs in doctrine, and what is not structured truth

8. `Control/Docs/FAILURE-MODE-GUARDRAILS.md`
   - anti-slop, anti-canon-corruption, and anti-overbuild rules

9. `Control/Docs/SYSTEMS-AND-TOOLS-UPGRADE-ROADMAP.md`
   - when future expansions like retrieval, graph, automation, and public proof should happen

---

## 3. Question-to-document routing

### If the question is...

#### “What is RVE supposed to be right now?”
Read:
1. `RVE-FEATURE-DRIVEN-CANON-SPEC.md`
2. `RVE-DIFF-ROLLOUT-VS-CANON.md`

#### “What exact mechanics from the original design are easy to lose?”
Read:
1. `RVE-DIFF-ROLLOUT-VS-CANON.md`
2. `RVE Rollout.md`
3. `RVE-MASTER-BRIEFING.md`

#### “What should populate RVE right now?”
Read:
1. `DELTAS_FINAL_POPULATION_SOURCE.md`
2. `TRUTH-ROUTING-CANON.md`

#### “What belongs in lifestate vs rve vs doctrine?”
Read:
1. `TRUTH-ROUTING-CANON.md`
2. `DELTAS_FINAL_POPULATION_SOURCE.md`
3. `RVE-DIFF-ROLLOUT-VS-CANON.md`

#### “What project should outrank another?”
Read:
1. `PROJECT-PORTFOLIO-CANON.md`

#### “Should graph memory / retrieval / automation be built now?”
Read:
1. `SYSTEMS-AND-TOOLS-UPGRADE-ROADMAP.md`
2. `PROJECT-PORTFOLIO-CANON.md`

#### “What implementation choices are dangerous?”
Read:
1. `FAILURE-MODE-GUARDRAILS.md`
2. `RVE-DIFF-ROLLOUT-VS-CANON.md`

---

## 4. Indexing judgment

### Do we know these docs will be referenced properly just because they exist?
No.

Existence is not reference.
A file is only useful if there is:
- a clear authority order
- a query-to-document routing rule
- a predictable place to look first

That is the purpose of this file.

### Should they be indexed?
Yes.
Immediately.

At minimum:
- keep this reference map
- keep the file names stable
- keep top-level purposes explicit in each doc
- keep RVE implementation pointed at Tier 1 first, Tier 2 second, Tier 3 when needed

### Should they be graphed?
Eventually, yes.
But graphing is not the first requirement.

The order should be:
1. stable canon docs
2. explicit reference map / index
3. retrieval-friendly indexing
4. only then graph extracted entities/relations if the corpus scale justifies it

Graphing raw docs too early is a good way to create graph-shaped confusion.

---

## 5. Practical implementation rule

When Gemini or any future agent is operating on RVE:
1. check Tier 1 first
2. use Tier 2 to recover missing design intent
3. use Tier 3 to resolve routing, priority, and system-wide conflicts
4. do not freestyle from memory when a canon file exists

---

## 6. Final note

This file exists because RVE now has enough documentation that implementation could drift simply from using the wrong source first.
The answer is not “trust memory.”
The answer is a stable document map.
