# RVE MVP OPERATIONAL CONTRACT

Status: Proposed hardening addendum
Parent document: `RVE-FEATURE-DRIVEN-CANON-SPEC.md`
Purpose: Make the RVE MVP precise enough to go live without waiting for further architecture refinement.

## 1. MVP definition

RVE MVP is live when Gemini can operate the task and obligation system from SQLite with enough consistency that the operator can trust it for daily decision support.

This does **not** require:
- graph memory
- complete automation
- perfect scripts
- mobile completion
- advanced UI

It **does** require:
- stable task entry
- stable retrieval
- stable ranking logic
- stable obligation/anchor retrieval
- stable project-state visibility

## 2. MVP authority sources

For current-phase RVE operation, authority resolves in this order:
1. direct user clarification in current session
2. current accepted RVE canon docs
3. direct database state in `rve.db` / `lifestate.db`
4. stronger build/spec docs like `ThisIsTheReportStandard.md.txt`
5. older doctrine / rollout / theory files

If lower-priority sources conflict with higher-priority sources, do not silently flatten them.

## 3. Mandatory task fields for MVP

A task may be stored as `captured` with only:
- title
- domain or project
- notes optional

A task may only become `ready` when it has at minimum:
- title
- state
- urgency
- impact
- friction
- duration estimate
- energy type
- due or explicit no-deadline status
- project or domain assignment

## 4. Minimum state machine

Use these states for MVP:
- `captured`
- `onboarding_pending`
- `ready`
- `in_progress`
- `blocked`
- `waiting`
- `completed`
- `archived`

### State rules
- `captured`: quick entry, not yet scoreable with confidence
- `onboarding_pending`: needs metadata enrichment
- `ready`: can be ranked and scheduled
- `in_progress`: currently being worked
- `blocked`: external blocker or missing requirement
- `waiting`: dependent on another person/system/date
- `completed`: done and logged
- `archived`: no longer operationally active

## 5. MVP commands Gemini must support

Gemini must be able to perform these intents reliably:
1. add task
2. enrich task
3. list top tasks
4. list tasks by project/domain/state
5. show obligations and anchors
6. show what fits in a given window
7. mark complete and log calibration
8. show blocked and waiting items
9. show active projects with next actions
10. capture idea separately from active task flow

## 6. Ranking logic contract

Gemini may calculate scores dynamically if fields are present.

Minimum ranking factors:
- urgency
- impact
- friction inverse
- duration fit
- energy match
- due pressure

Extended ranking factors, only if present and maintained:
- cascade value
- compound value
- immediate benefit
- postpone count

## 7. Scheduling / recommendation rules

When recommending what to do next, Gemini must check in this order:
1. fixed obligations and anchors
2. current time window size
3. current energy state
4. location constraints if relevant
5. due pressure
6. score rank among eligible `ready` tasks

Gemini must not recommend:
- blocked items as default next moves
- low-metadata tasks as if they were fully ranked
- tasks that do not fit the stated time window without flagging the mismatch

## 8. Five operational test cases

### Test 1 — Quick capture
Input: a raw task title
Success: task stored as `captured` or `onboarding_pending`

### Test 2 — Full onboarding
Input: one task enriched with metrics
Success: task reaches `ready` and can be ranked

### Test 3 — Window query
Input: "What can I do in 45 minutes at low energy?"
Success: Gemini returns only fit-matched tasks and explains why

### Test 4 — Obligation surface
Input: "What anchors and obligations do I have today?"
Success: Gemini returns schedule-relevant items cleanly

### Test 5 — Completion log
Input: mark task complete with actual duration/difficulty/energy
Success: task changes state and calibration data is preserved

## 9. Go-live rule

RVE should be considered live once the five test cases above work reliably enough to use in a real day.
Do not wait for perfect scripts or ideal architecture.

## 10. Hard red-team warnings

RVE MVP is compromised when:
- too many fields make manual entry unbearable
- Gemini treats low-metadata tasks as confidently ranked truth
- obligations are not queryable
- project state is still mostly narrative and not structured
- daily use keeps requiring system redesign before action

RVE MVP is healthy when:
- you can dump tasks in
- enrich the important ones
- retrieve what matters now
- operate your day with less confusion than before
