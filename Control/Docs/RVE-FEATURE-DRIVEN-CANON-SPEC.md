# RVE FEATURE-DRIVEN CANON SPEC

Status: Reinforced MVP Contract
Purpose: Define the Rolling Victory Engine (RVE) as a concrete, live MVP product instead of a floating doctrine pile. Establish authoritative operational contracts for task handling and scheduling via Gemini + SQLite.

## 1. Product definition

RVE is a local-first, CLI-invoked personal command center designed to give a single human being — operating under real-world chaos, constraint, and ambition — a coherent, persistent, adaptive, AI-augmented operating system for their entire life.

Target User: A 35-year-old in recovery, currently in intensive outpatient treatment, residing at a corrections facility, attending community college, building toward a software development career, with zero disposable income and high ambition.

## 2. Primary user promise

RVE captures life state across all domains, assesses tasks using a weighted metric model, generates context-aware schedules, drives daily check-ins, tracks habits, and serves as the canonical data source for all AI interactions. It converts chaos into structured execution.

## 3. MVP Definition & Go-Live Rule

**MVP Definition:** RVE MVP is live when Gemini can operate the task and obligation system from SQLite with enough consistency that the operator can trust it for daily decision support.
This requires: stable task entry, stable retrieval, stable ranking logic, stable obligation/anchor retrieval, and stable project-state visibility.
This does NOT require: graph memory, perfect scripts, mobile completion, or advanced UI.

**Go-live rule:** RVE should be considered live once the 5 operational test cases (Section 10) work reliably enough to use in a real day. Do not wait for perfect scripts or ideal architecture. Gemini can run the logic directly against SQLite.

## 4. MVP Authority Sources & Authority Ladder

For current-phase RVE operation, authority resolves in this order:
1. Direct user clarification in current session
2. Current accepted RVE canon docs
3. Direct database state in `rve.db` / `lifestate.db`
4. Stronger build/spec docs (`ThisIsTheReportStandard.md.txt`)
5. Older doctrine / rollout / theory files

## 5. Minimum State Machine

Use these states for MVP:
- `captured`: quick entry, not yet scoreable with confidence
- `onboarding_pending`: needs metadata enrichment
- `ready`: can be ranked and scheduled
- `in_progress`: currently being worked
- `blocked`: external blocker or missing requirement
- `waiting`: dependent on another person/system/date
- `completed`: done and logged
- `archived`: no longer operationally active

## 6. Mandatory Task Fields for `ready`

A task may be stored as `captured` with only:
- `title`
- `domain` or `project`
- `notes` (optional)

A task may only become `ready` when it has at minimum:
- `title`
- `state`
- `urgency` (1-10)
- `impact` (1-10)
- `friction` (Activation cost 1-10)
- `duration_est_min`
- `energy_type` (high_cognitive / high_creative / high_physical / low_energy / zombie_capable / mandatory_regardless)
- `due` (Deadline or explicit no-deadline status)
- `domain_id` / `project_id`

*Extended fields (cascade_val, compound_val, immediate_benefit, postpone_count, actuals) are supported but not mandatory for MVP `ready` state.*

## 7. Ranking Logic Contract

Gemini must calculate scores dynamically for `ready` tasks.

**Composite score formula (v1):**
Score = (urgency x 0.25) + (impact x 0.20) + (cascade_val x 0.15) + (compound_val x 0.15) + (immediate_benefit x 0.10) + (mandatory_bonus x 0.10) + (low_friction_bonus x 0.05)
*Note: If extended fields are missing, Gemini uses the minimum ranking factors: urgency, impact, inverse friction, duration fit, energy match, and due pressure.*

## 8. Scheduling & Recommendation Rules

When recommending what to do next, Gemini must filter/check in this order:
1. fixed obligations and schedule anchors
2. current time window size vs. `duration_est_min`
3. current energy state vs. `energy_type`
4. location constraints if relevant
5. due pressure
6. score rank among eligible `ready` tasks

**Gemini must NOT recommend:**
- blocked items as default next moves
- low-metadata tasks as if they were fully ranked
- tasks that do not fit the stated time window without flagging the mismatch

## 9. Minimum Commands Gemini Must Support

Gemini must be able to perform these intents reliably against the SQLite database:
- `rve log` (Quick capture: add task with minimal fields, mark `onboarding_pending`)
- `rve task add` / `rve onboard` (Enrich a task to `ready` state)
- `rve today` / list top tasks (Filter by window/energy and sort by score)
- list tasks by project/domain/state
- show obligations and anchors
- `rve checkpoint` / mark complete and log calibration data (actual duration/difficulty)
- show blocked and waiting items
- show active projects with next actions

## 10. Five Operational Test Cases

- **Test 1 — Quick capture:** Input a raw task title. Success = stored as `captured` or `onboarding_pending`.
- **Test 2 — Full onboarding:** Enrich one task with metrics. Success = task reaches `ready` and can be ranked.
- **Test 3 — Window query:** "What can I do in 45 minutes at low energy?" Success = returns only fit-matched tasks and explains why.
- **Test 4 — Obligation surface:** "What anchors and obligations do I have today?" Success = returns schedule-relevant items cleanly.
- **Test 5 — Completion log:** Mark task complete with actual duration/difficulty/energy. Success = state changes and calibration data is preserved.

## 11. Non-goals for current phase
RVE does not currently need:
- Neo4j / Graph memory infrastructure
- Complete automated script suites (Gemini can execute raw SQL)
- Automated web research or TUI/Mobile apps

## 12. Red-Team Warnings
RVE MVP is compromised when:
- too many fields make manual entry unbearable
- Gemini treats low-metadata tasks as confidently ranked truth
- obligations are not queryable
- project state is still mostly narrative and not structured
- daily use keeps requiring system redesign before action

RVE MVP is healthy when: you can dump tasks in, enrich the important ones, retrieve what matters now, and operate your day with less confusion than before.
