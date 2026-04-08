# RVE — MASTER BRIEFING
### For: Pickle Rick (Gemini CLI Agent)
### Version: 2.0 | Author: Shane Johns
### Purpose: Complete, unambiguous build contract — zero guessing required
---
# PART 1 — MISSION
RVE (Revival Vector Engine / Rolling Victory Engine) is a local-first, CLI-invoked personal command center. It captures life state, scores tasks by weighted formula, generates energy-stratified schedules, tracks habits and streaks, routes XP to an RPG character sheet, manages a quest engine, and serves as the canonical data source for all agent sessions. It is not a task manager. It is a personal operating system.

**Target user:** Shane Johns. 35. Recovery (fentanyl + meth, 200+ days clean). Hillsboro OR shelter. PCC student. Zero income. High ambition. Complex life. If it works here, it works anywhere.

**Build environment:**
- Windows 11 / PowerShell
- Gemini CLI + Pickle Rick + Superpowers extensions
- Python 3.x + SQLite (no server)
- Obsidian vault: `C:\Users\tarot\Operator\Vault`
- Databases: `C:\Users\tarot\Operator\Control\rve.db` + `lifestate.db`
---
# PART 2 — SCIENTIFIC FOUNDATION
Every feature exists because of research-backed behavioral mechanisms:
- **Self-monitoring changes behavior** — the act of logging tasks and completions increases follow-through. RVE's checkpoint model operationalizes this.
- **Implementation intentions** — specifying WHEN and WHERE increases execution rate by 2–3x. RVE's energy-stratified scheduling provides this automatically.
- **Variable reward + progress visibility** — RPG XP and level systems leverage dopamine-mediated reinforcement. Visible growth sustains engagement.
- **Identity-based habit formation** — tracking streaks and displaying attribute growth reinforces identity change ("I am someone who trains") over outcome goals.
- **Cognitive offloading** — externalized task systems reduce working memory load, freeing cognitive resources for execution.
---
# PART 3 — DATABASE ARCHITECTURE
## 3.1 Two-Database Design
`lifestate.db` — source of truth for WHO Shane is (identity, constraints, history)
`rve.db` — source of truth for WHAT Shane does (tasks, habits, progress, growth)
Scripts read from both. Neither overwrites the other. When the same data appears in both (e.g. attribute_log), rve.db is the write target; lifestate.db is the seed.

## 3.2 rve.db — Complete Table Schemas
```sql
CREATE TABLE IF NOT EXISTS tasks (
    id                TEXT PRIMARY KEY,
    title             TEXT NOT NULL,
    domain            TEXT,
    type              TEXT DEFAULT 'task',
    project_id        TEXT,
    state             TEXT DEFAULT 'active',
    urgency           INTEGER DEFAULT 5,
    impact            INTEGER DEFAULT 5,
    friction          INTEGER DEFAULT 5,
    energy_required   TEXT DEFAULT 'medium',
    due_date          TEXT,
    recurrence        TEXT,
    fixed             INTEGER DEFAULT 0,
    created           TEXT,
    updated           TEXT,
    completed         TEXT,
    rve_score         REAL DEFAULT 0,
    attribute_tag     TEXT,
    notes             TEXT
);

CREATE TABLE IF NOT EXISTS projects (
    id              TEXT PRIMARY KEY,
    title           TEXT NOT NULL,
    domain          TEXT,
    status          TEXT DEFAULT 'active',
    due_date        TEXT,
    progress_pct    REAL DEFAULT 0,
    attribute_tag   TEXT,
    notes           TEXT
);

CREATE TABLE IF NOT EXISTS habits (
    id                  TEXT PRIMARY KEY,
    title               TEXT NOT NULL,
    domain              TEXT,
    frequency           TEXT DEFAULT 'daily',
    streak_current      INTEGER DEFAULT 0,
    streak_best         INTEGER DEFAULT 0,
    streak_paused       INTEGER DEFAULT 0,
    last_completed      TEXT,
    xp_per_completion   INTEGER DEFAULT 10,
    attribute_tag       TEXT,
    status              TEXT DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS habit_log (
    id          TEXT PRIMARY KEY,
    habit_id    TEXT NOT NULL,
    date        TEXT NOT NULL,
    completed   INTEGER DEFAULT 1,
    xp_earned   INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS attribute_log (
    id          TEXT PRIMARY KEY,
    attribute   TEXT NOT NULL,
    level       INTEGER DEFAULT 1,
    xp_total    INTEGER DEFAULT 0,
    xp_to_next  INTEGER DEFAULT 100,
    last_updated TEXT
);

CREATE TABLE IF NOT EXISTS wins (
    id              TEXT PRIMARY KEY,
    title           TEXT NOT NULL,
    date            TEXT NOT NULL,
    xp_earned       INTEGER DEFAULT 0,
    attribute_tag   TEXT
);

CREATE TABLE IF NOT EXISTS ideas (
    id                  TEXT PRIMARY KEY,
    title               TEXT NOT NULL,
    status              TEXT DEFAULT 'raw',
    potential           INTEGER DEFAULT 5,
    effort              INTEGER DEFAULT 5
);
```
---
# PART 4 — SCORING ENGINE
## 4.1 Formula
```python
def compute_rve_score(task, current_hour):
    urgency  = task.urgency  or 5
    impact   = task.impact   or 5
    friction = task.friction or 5
    friction_inv = 11 - friction
    raw_score = (urgency * 0.30) + (impact * 0.35) + (friction_inv * 0.20)
    # Energy window modifier logic...
    return round(raw_score, 2)
```
---
# PART 5 — XP AND LEVEL SYSTEM
Level n total XP required = 100 * (1.5 ^ (n-1))
Level 1: 0 – 100
Level 2: 100 – 250
Level 3: 250 – 475
Level 4: 475 – 813
Level 5: 813 – 1,320
---
# PART 6 — HABIT STREAK MECHANICS
Calendar-day based. Miss 1 day = pause. Miss 2 days = reset.
---
# PART 7 — CHECKPOINT MODEL
CP1: 05:30 Morning Activation
CP2: 08:00 Peak Launch
CP3: 13:00 Midday Scan
CP4: 19:00 Evening Wind-Down
CP5: 21:00 Night Log
---
# PART 8 — QUEST ENGINE
Generates 3 quests per day: MAIN, SIDE, WILDCARD.
---
# PART 9 — /rve STATUS DASHBOARD SPEC
Output includes: Days Clean, Anchors, Top Tasks, Quests, Habits, Character Sheet, Flags.
---
# PART 10 — INTAKE WIZARD
Sequential questions for Title, Type, Domain, Urgency, Impact, Friction, and optional fields.
---
# PART 11 — OBSIDIAN INTEGRATION
Complexity-based page scope: Checklist (0), Section (1-3), Page (4-7), Folder (8-10).
---
# PART 12 — IDEA PIPELINE
Capture -> Raw -> Weekly Review -> Promote/Kill -> Task creation.
---
# PART 13 — CONTEXT EXPORT SPEC
Compact block under 2,000 tokens for session injection.
---
# PART 14 — SLASH COMMANDS
/rve status, /rve add, /rve score, /rve schedule, /rve snapshot, /rve week, /rve context, /rve sync, /rve quest, /rve win, /rve capture, /rve done, /rve ideas, /rve habits, /rve xp.
---
# PART 15 — SCHEDULE.PY SPEC
Energy window mapping and conflict detection with travel buffers.
---
# PART 16 — SYSTEM INTEGRATION MAP
Cross-database reads/writes between lifestate.db and rve.db, syncing with Notion and Obsidian.
