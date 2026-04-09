# RVE SCHEMA MIGRATION PLAN

Status: Active migration plan
Purpose: Bridge the gap between the thinner current RVE implementation/schema and the stronger task, completion, project, idea, and context-export requirements defined in the rollout diff and implementation checklist.

---

## 1. Mission

Patch the current SQLite-backed RVE so it can support the real MVP behavior without forcing a destructive redesign.

This document exists to answer:
- what tables or fields need to change
- what can remain as-is
- what should be added now vs deferred
- how to migrate without corrupting existing data

---

## 2. Migration principles

1. Preserve existing working data whenever possible.
2. Prefer additive migration over destructive rebuild.
3. Add only fields required for real MVP behavior.
4. Do not add fantasy fields that no workflow currently uses.
5. Keep `lifestate.db` and `rve.db` role separation intact.

---

## 3. Database role split

### `lifestate.db`
Stores:
- profile truth
- constraints
- affiliations
- supports
- legal / health / school / recovery state
- contacts and node-level support context

### `rve.db`
Stores:
- tasks
- projects
- ideas
- habits
- completions
- obligations
- schedule anchors
- current execution state
- context export source material

Do not flatten these into one table space unless there is a compelling implementation reason and explicit review.

---

## 4. Core task-table migration

## Current need
The task object needs to support real RVE scheduling, staged onboarding, transition-mode use, and completion learning.

## Required fields
The `tasks` table should support, at minimum:
- `id`
- `title`
- `domain`
- `project_id`
- `state`
- `fixed`
- `location`
- `due_date`
- `duration_est_min`
- `energy_type`
- `urgency`
- `impact`
- `friction`
- `cascade`
- `compound`
- `immediate_benefit`
- `mandatory`
- `atomic`
- `action_plan`
- `contact`
- `website`
- `estimated_fields`
- `needs_review`
- `postpone_count`
- `if_then_plan`
- `notes`
- `created`
- `updated`
- `completed`
- `rve_score`

## Migration strategy

### Keep if already present
- id
- title
- domain
- project_id
- state
- urgency
- impact
- friction
- due_date
- fixed
- created
- updated
- completed
- rve_score
- notes

### Add now if missing
- `location TEXT`
- `duration_est_min INTEGER DEFAULT 30`
- `energy_type TEXT DEFAULT 'medium'`
- `cascade INTEGER DEFAULT 5`
- `compound INTEGER DEFAULT 5`
- `immediate_benefit INTEGER DEFAULT 5`
- `mandatory INTEGER DEFAULT 0`
- `atomic INTEGER DEFAULT 1`
- `action_plan TEXT`
- `contact TEXT`
- `website TEXT`
- `estimated_fields INTEGER DEFAULT 0`
- `needs_review TEXT`
- `postpone_count INTEGER DEFAULT 0`
- `if_then_plan TEXT`

### Optional later fields
Only add later if live use proves need:
- `actual_duration_min`
- `actual_difficulty`
- `actual_energy_used`
- `estimate_error`

These may instead belong in a dedicated completion log if that is cleaner.

---

## 5. Completion logging migration

## Problem
A simple `completed` timestamp is not enough if RVE is supposed to learn from execution.

## Preferred solution
Create or strengthen a dedicated completion-oriented table, for example `task_completions`, supporting:
- `id`
- `task_id`
- `completed_at`
- `actual_duration_min`
- `actual_difficulty`
- `actual_energy_used`
- `completion_notes`
- `followup_spawned`
- `estimate_error`

## Why separate table is preferred
- preserves repeatable or recurring-task history
- avoids bloating the main task row
- supports later analytics

## Fallback if no new table is acceptable
Add a JSON/text completion-notes field to tasks and store latest completion only.
This is weaker and should be treated as temporary.

---

## 6. Project-table migration

## Current need
Projects need to be more than titles. They must support visibility and next-action logic.

## Recommended fields
The `projects` table should support:
- `id`
- `title`
- `domain`
- `status`
- `goal`
- `priority`
- `next_action`
- `blockers`
- `progress_pct`
- `notes`
- `created`
- `updated`

## Add now if missing
- `goal TEXT`
- `priority INTEGER DEFAULT 5`
- `next_action TEXT`
- `blockers TEXT`
- `created TEXT`
- `updated TEXT`

---

## 7. Idea-pipeline migration

## Problem
Ideas should not remain a vague holding bin.

## Required state support
The `ideas` table should support meaningful stages, such as:
- captured
- contemplated
- prepared
- incubating
- activated
- paused
- archived

## Recommended fields
- `id`
- `title`
- `stage`
- `domain`
- `linked_project_id`
- `potential`
- `effort`
- `notes`
- `created`
- `updated`

## Migration action
If current `ideas.status` is too crude, either:
- rename semantic usage from `status` to stage values, or
- add `stage TEXT DEFAULT 'captured'`

Prefer explicit stage language.

---

## 8. Habit-table migration

## Current need
Habits should remain modular but usable.

## Minimum support
The habits module should support:
- binary habits
- count habits
- abstinence/reduction habits
- trigger-linked microhabits

## Recommended fields
- `id`
- `title`
- `domain`
- `type`
- `trigger`
- `action`
- `frequency`
- `status`
- `streak_current`
- `streak_best`
- `last_completed`
- `notes`

## Add now if missing
- `type TEXT DEFAULT 'binary'`
- `trigger TEXT`
- `action TEXT`

Keep this light.

---

## 9. Obligations and schedule anchors

## Current need
Recurring compliance/admin obligations and fixed anchors must be queryable separately from flexible work.

## Recommended approach
Ensure explicit support for:
- recurring obligations (`Daily UA Portal Check` class items)
- fixed schedule anchors (appointments, treatment, class, probation, meals if needed)

## Recommended tables
- `obligations`
- `schedule_anchors`

Minimum fields for anchors:
- `id`
- `title`
- `domain`
- `anchor_start`
- `anchor_end`
- `location`
- `recurrence`
- `notes`

---

## 10. Context export support

## Problem
RVE is meant to support broader AI use later.
Without a compact export path, that future integration becomes messy.

## Recommendation
Do not overbuild a context-memory layer now.
Instead ensure the schema supports generating a compact export from:
- active projects
- active obligations
- top ready tasks
- constraints from lifestate
- current week anchors

This is primarily a query/output problem, not a database-design excuse to add lots of new storage.

---

## 11. Weekly rolling/archive support

## Recommendation
Support week-bounded views and archives without requiring complex calendar infrastructure.

Possible implementation paths:
1. file-based weekly export snapshots
2. schedule table with `week_key`
3. archive folder or archive table for prior periods

Keep it simple.

---

## 12. Migration order

1. inspect current table schemas
2. add missing task fields
3. add or strengthen project fields
4. add or strengthen idea stages
5. add or strengthen habit trigger/type fields
6. ensure obligations and anchors are queryable
7. implement completion log strategy
8. validate existing data survived
9. only then populate from the final population source

---

## 13. Validation checks after migration

Migration is acceptable when:
- existing task rows still exist and are readable
- new captures can enter as `captured` or `onboarding_pending`
- a `ready` task can hold enough metadata to schedule intelligently
- project records can show `next_action`
- ideas can sit in meaningful stages
- habits can represent more than just a streak counter
- completion logging can preserve actual-vs-estimated data

---

## 14. Final rule

The goal is not a beautiful maximal schema.
The goal is the smallest schema that faithfully supports the real RVE behavior already agreed upon.
