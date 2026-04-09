# RVE FEATURE-DRIVEN CANON SPEC

Status: Proposed canon spec
Purpose: Reframe RVE as a concrete feature-driven system rather than a drifting doctrine pile.

## 1. Product definition

RVE is a local-first, Gemini-operated personal command center.
Its job is not to impress. Its job is to maintain accurate life state, store and rank action items, surface obligations, and help the operator decide what to do next under real-world constraints.

## 2. Primary user promise

If I put my tasks, obligations, projects, and constraints into RVE, I can ask Gemini what matters now, what I can do in a given window, what I am neglecting, and what the next correct move is.

## 3. Core features

### Feature 1 — Task reservoir
Store all action items with enough fields to rank and filter them.

Minimum useful fields:
- title
- domain/project
- state
- urgency
- impact
- friction
- duration estimate
- energy type
- due/deadline
- notes

Extended fields from the stronger briefing remain valid when useful:
- cascade value
- compound value
- immediate benefit
- atomic flag
- estimated_fields flag
- postpone_count
- completion calibration fields

### Feature 2 — Obligation and anchor tracking
RVE must be able to surface:
- fixed obligations
- recurring anchors
- schedule blocks
- non-negotiable constraints

### Feature 3 — Project-state retrieval
RVE must be able to answer:
- what projects are active
- what state each project is in
- what the next action is
- what is blocked

### Feature 4 — Scoring and ranking
RVE must support ranking by weighted metrics.
Gemini may compute scores dynamically if the fields are present.
A script is optional for MVP use.

### Feature 5 — Window-aware recommendation
Given a time window, energy state, and location, RVE should be able to suggest suitable work.

### Feature 6 — Daily briefing / checkpoint mode
RVE should provide:
- active anchors
- top tasks
- obligations
- notable flags
- current project pressure

### Feature 7 — Completion logging and calibration
When a task is completed, RVE should capture:
- actual duration
- actual difficulty
- actual energy used
- notes or spawned follow-up tasks

### Feature 8 — Idea / capture pipeline
Good ideas should be captured without polluting the active task reservoir.

## 4. Non-goals for current phase

RVE does not currently need:
- advanced graph memory
- large automation webs
- perfect UI/TUI
- full mobile stack
- broad integrations beyond Gemini + SQLite

## 5. Current MVP operational mode

Use Gemini CLI as the interface layer.
Use SQLite as the canonical storage layer.
Use manual task entry and guided onboarding instead of waiting for perfect scripts.

This means RVE is considered functional when Gemini can:
- add tasks with the required fields
- retrieve and rank tasks
- retrieve obligations and anchors
- summarize project state
- support daily decision-making

## 6. Required canon commands / interactions

RVE should support, at minimum, these operational intents:
- add task
- update task
- show top tasks
- show tasks by domain
- show obligations
- show schedule anchors
- show active projects
- show blocked items
- show what fits in a given time window
- mark task complete
- capture idea

Whether these are backed by scripts or by Gemini + DB queries is secondary for MVP.

## 7. Data quality rules

- no task enters ready state without minimum metadata
- ambiguous entries are provisional
- direct user input outranks old text files
- project state should not be inferred from vibe alone
- completion logs should produce calibration, not just closure

## 8. Acceptance criteria

RVE current phase is successful when the following are true:
1. tasks can be entered consistently
2. tasks can be ranked consistently
3. obligations and anchors are queryable
4. project states can be surfaced on demand
5. Gemini can drive the system without redesigning it every session

## 9. Proposed additions worth considering later

Only after MVP daily use reveals pain:
- anchor vs slayable explicit field
- gate fields (time/place/person/tool)
- richer weekly review outputs
- deeper XP/attribute integration
- export packages for other AI tools

## 10. Red-team warning

RVE fails when it becomes:
- a fantasy RPG shell with weak operational truth
- a doctrine pile with no daily utility
- a task graveyard with too many fields to maintain
- an automation dream dependent on infrastructure that is not stable

RVE wins when it becomes the smallest system that reliably helps the operator decide and act.
