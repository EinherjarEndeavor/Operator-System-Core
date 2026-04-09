# REMATCH FEATURE-DRIVEN CANON SPEC

Status: Reinforced MVP Contract
Purpose: Convert the Re.Match concept from scattered mission prose into a buildable service definition, detailing the minimum viable matching logic and dossier output contract.

## 1. Product definition

Re.Match is a constraint-based resource and opportunity matching service for justice-involved, recovery, housing-insecure, and otherwise highly constrained people. It doesn't just "find jobs"—it utilizes the specific "constellation of circumstance" to unlock high-tier scholarships, specialized grants, and opportunities that others cannot access.

It is not generic job search. It is profile-aware matching plus dossier generation.

## 2. Primary user promise

If a client provides a complete enough profile, Re.Match can return a prioritized dossier of high-fit opportunities, supports, programs, and action steps that match both hard eligibility and real-life circumstance.

## 3. Core product loop

1. intake profile creation
2. profile normalization
3. opportunity database search / matching
4. deduplication and no-redundancy filtering
5. prioritized dossier generation
6. action-plan packaging
7. follow-up updates as circumstances change

## 4. Intake Domains

A usable intake must cover these domains:
1. identity/contact
2. location/transportation
3. housing status and barriers
4. legal / supervision constraints
5. recovery / treatment status
6. education and training
7. employment / income / benefits
8. health / insurance / support needs
9. goals, interests, and affinities
10. immediate deadlines / active applications / near-term priorities

## 5. Opportunity Record Minimum Fields

Each opportunity/support record should have, at minimum:
- title
- category/domain
- geographic scope
- hard eligibility criteria
- likely fit dimensions
- action steps
- key deadlines or timing constraints
- source/provenance
- notes / cautions / common blockers

## 6. Matching Logic Order

Match in this order:
1. hard eligibility
2. hard disqualifiers
3. geography / access fit
4. timing fit
5. barrier compatibility
6. likely life-impact potential
7. redundancy check

**Rule:** A recommendation must not appear simply because it is generally good. It must fit the specific profile and current circumstance.

## 7. Recommendation Classes

- **CLASS A — Immediate action:** Fits now, actionable now, high life impact.
- **CLASS B — Near-term setup:** Not immediately actionable, but should be prepared now for later use.
- **CLASS C — Monitor / revisit:** Potentially relevant later, but not worth current action.

## 8. Redundancy Rules & Review Triggers

**Redundancy Rules:** Do not recommend items that are already completed, actively pursued, or known and exhausted, UNLESS:
- eligibility situation changed
- timing window changed
- prior attempt failed for a now-resolved reason

**Review Triggers:** Require review before inclusion when:
- eligibility is uncertain
- geography/access is unclear
- recommendation is prestige-oriented but weakly actionable
- recommendation duplicates another item with lower value

## 9. Dossier Contract

Output is not just a list. Each dossier should include:

**Section 1 — Summary**
- client snapshot, most important constraints, most important opportunities, immediate next-step emphasis

**Section 2 — Category recommendations**
For each category:
- recommendation title, why it fits, eligibility basis, why it matters, action steps, notes/cautions

**Section 3 — Immediate action queue**
Top 3–7 next actions across the whole dossier.

**Section 4 — Deferred / monitor list**
Items worth keeping in view but not pursuing immediately.

## 10. Non-goals for current phase

Re.Match does not currently need:
- perfect end-to-end automation
- broad autonomous agent swarms
- production-scale client ops stack
- fancy ML matching beyond strong rule-based and AI-assisted reasoning

## 11. Acceptance criteria & Go-Live

Re.Match MVP is successful when:
1. one intake profile is normalized cleanly
2. one dossier is generated with clear category structure using existing opportunity knowledge
3. each recommendation has a traceable reason for inclusion and is non-redundant
4. the dossier contains an immediate action queue that would actually help the user

## 12. Red-team warning

Re.Match fails when:
- it becomes generic internet searching with better rhetoric
- it recommends the same stale resources repeatedly
- dossiers become long but not decisive
- intake captures many details but the output still feels vague

Re.Match wins when the recipient gets a materially better, more targeted next-step package than they could have assembled alone.
