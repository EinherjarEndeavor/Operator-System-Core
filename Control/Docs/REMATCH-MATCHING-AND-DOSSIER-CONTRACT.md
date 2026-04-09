# REMATCH MATCHING AND DOSSIER CONTRACT

Status: Proposed hardening addendum
Parent document: `REMATCH-FEATURE-DRIVEN-CANON-SPEC.md`
Purpose: Define the minimum viable matching logic, dossier output contract, and review rules for Re.Match.

## 1. MVP definition

Re.Match MVP is working when one complete profile can be converted into one materially useful, non-redundant dossier containing high-fit recommendations with explicit next steps.

## 2. Intake domains

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

## 3. Opportunity record minimum fields

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

## 4. Matching logic order

Match in this order:
1. hard eligibility
2. hard disqualifiers
3. geography / access fit
4. timing fit
5. barrier compatibility
6. likely life-impact potential
7. redundancy check

### Rule
A recommendation must not appear simply because it is generally good.
It must fit the specific profile and current circumstance.

## 5. Recommendation classes

### CLASS A — Immediate action
Fits now, actionable now, high life impact.

### CLASS B — Near-term setup
Not immediately actionable, but should be prepared now for later use.

### CLASS C — Monitor / revisit
Potentially relevant later, but not worth current action.

## 6. Dossier contract

Each dossier should include:

### Section 1 — Summary
- client snapshot
- most important constraints
- most important opportunities
- immediate next-step emphasis

### Section 2 — Category recommendations
For each category:
- recommendation title
- why it fits
- eligibility basis
- why it matters
- action steps
- notes / cautions

### Section 3 — Immediate action queue
Top 3–7 next actions across the whole dossier.

### Section 4 — Deferred / monitor list
Items worth keeping in view but not pursuing immediately.

## 7. Redundancy rules

Do not recommend items that are already:
- completed
- actively pursued
- already known and exhausted

Unless:
- the eligibility situation changed
- the timing window changed
- the prior attempt failed for a now-resolved reason

## 8. Review triggers

Require review before inclusion when:
- eligibility is uncertain
- geography/access is unclear
- recommendation is prestige-oriented but weakly actionable
- recommendation duplicates another item with lower value

## 9. Acceptance criteria

Re.Match MVP is successful when:
1. one intake profile is normalized cleanly
2. one dossier is generated with clear category structure
3. each recommendation has a traceable reason for inclusion
4. the dossier contains an immediate action queue that would actually help the user

## 10. Red-team warning

Re.Match fails when:
- it becomes generic internet searching with better rhetoric
- it recommends the same stale resources repeatedly
- dossiers become long but not decisive
- intake captures many details but the output still feels vague

Re.Match wins when the recipient gets a materially better, more targeted next-step package than they could have assembled alone.
