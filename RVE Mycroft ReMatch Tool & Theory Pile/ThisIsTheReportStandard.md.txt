# RVE — MASTER BRIEFING PROMPT
### For: Pickle Rick (Gemini CLI Agent)
### Version: 1.0 | Author: Shane Johns
### Purpose: Complete one-shot system brief — concept, science, mechanisms, architecture, and build instructions

---

# PART 1 — MISSION STATEMENT

RVE is a local-first, CLI-invoked personal command center designed to give a single human being — operating under real-world chaos, constraint, and ambition — a coherent, persistent, adaptive, AI-augmented operating system for their entire life.

RVE captures life state across all domains, assesses tasks using a weighted multi-field metric model, maintains a structured knowledge base, generates context-aware schedules, drives daily check-ins, tracks habits, logs completions, manages an idea pipeline, and serves as the canonical data source for all AI interactions. It is not a productivity app. It is not a journal. It is not a task manager. It is the substrate from which all personal productivity, learning, scheduling, habit formation, and decision-making flows.

**The target user for v1 is Shane Johns**: a 35-year-old in recovery from fentanyl and methamphetamine addiction, currently in intensive outpatient treatment, residing at a corrections facility in Hillsboro, Oregon, attending Portland Community College, building toward a career in software development, with zero disposable income, high ambition, and a life complex enough to require systematic management to function at full capacity. If it works here, it works anywhere.

**Build environment:**
- Windows 11 / PowerShell / WSL
- Gemini CLI with Pickle Rick and Superpowers extensions
- Obsidian (Markdown vault, cloud-synced)
- Python 3.x
- SQLite (local, no server required)
- Termux on Android (mobile capture)

---

# PART 2 — SCIENTIFIC AND CONCEPTUAL FOUNDATION

The following research-backed principles underpin every feature of RVE. These are not decorative — they are the reason the features exist.

## 2.1 Self-Monitoring and Behavior Change

Technology-based self-monitoring consistently improves on-task behavior and follow-through. The act of observing and recording behavior changes the behavior itself. Systems with repeated check-ins throughout the day produce stronger and more durable behavioral effects than single daily reviews.

*Implication:* Multiple lightweight daily checkpoints are a core behavioral mechanism, not optional nicety. Each checkpoint should create a deliberate moment of reorientation. Target: under 2 minutes each.

## 2.2 Implementation Intentions (If-Then Planning)

Gollwitzer's research on implementation intentions demonstrates that forming specific if-then plans ('If situation X occurs, I will perform response Y') significantly improves goal attainment, especially under high cognitive load or emotional difficulty. Meta-analyses show medium-to-large effect sizes across diverse behavioral domains.

*Implication:* RVE stores a library of pre-specified cue-response scripts for recurring transitions, friction points, and decision moments. These are created through a guided wizard and retrieved at relevant checkpoints.

## 2.3 Transtheoretical Model (Stages of Change)

Prochaska and DiClemente's Transtheoretical Model posits that behavior change moves through stages: precontemplation, contemplation, preparation, action, maintenance. Interventions matched to the current stage are significantly more effective than stage-mismatched ones.

*Implication:* Not every idea, habit, or project is ready to execute. Tagging them with current stage allows the system to present stage-appropriate actions (research vs. decompose vs. schedule vs. reinforce) rather than treating all items as immediately actionable.

## 2.4 Time Blocking and Dynamic Scheduling

Structured time allocation with pre-assigned blocks reduces decision fatigue and makes workload constraints visible before they produce failure. Dynamic scheduling — replanning at recurring intervals — is more appropriate than rigid fixed calendars for people with unstable or interrupted schedules.

*Implication:* RVE anchors fixed obligations, generates a weekly structural frame, and replans dynamically at each checkpoint based on current state and available windows. Monthly auto-scheduling is explicitly avoided.

## 2.5 Energy-Aware Task Assignment

Cognitive performance varies across the day and is affected by sleep, stress, meals, activity, and emotional load. Assigning high-demand tasks to depleted states produces poor outcomes and compounds avoidance.

*Implication:* Every task carries an energy_type field. The scheduler filters recommendations by current energy state rather than treating all available time as equivalent.

## 2.6 Planned vs. Actual Learning (Calibration)

When a system logs both estimated and actual task duration, difficulty, and energy cost, it accumulates evidence about real patterns versus idealized self-model. This enables progressive scheduling accuracy and surfaces systematic biases (e.g., chronic underestimation of friction).

*Implication:* Every task completion logs actual duration, actual difficulty, actual energy used, and observations. This data drives progressive system calibration.

## 2.7 Habit Formation and Microhabits

Small, context-triggered, low-effort behaviors — when repeated consistently — produce durable trait changes through associative learning. Streak-based tracking can improve adherence but must be paired with recovery mechanisms (missing once should not terminate a streak).

*Implication:* Habit tracking is a module, not a central paradigm. Habits store triggers, target attributes, difficulty, stage, and streak data. The system supports binary, count, abstinence, and replacement habits. Missed entries are recoverable.

## 2.8 Pomodoro / Time-Block Intervals

Research comparing self-regulated, Pomodoro, and Flowtime approaches shows interval structure affects fatigue and motivation but no clear universal superiority for one method. Individual adaptation matters.

*Implication:* Pomodoro is available as an optional focus timer within a time block, not a system-wide mandate. The user chooses interval length per session based on energy and task type.

---

# PART 3 — THE RVE CONCEPT IN FULL

RVE operates on five interlocking components.

## Component 1: Life State Model

A structured, persistent representation of who Shane is, what he has, what he owes, what he is doing, and where he is going. This is the ground truth from which everything else derives. It is not aspirational. It is accurate.

**Life state covers:**
- Identity and values
- Current constraints (time, money, location, transportation, housing, legal)
- Fixed schedule anchors (recurring obligations that cannot move)
- Active projects and their current stage
- Obligations with deadlines
- Resources (devices, accounts, software, documents, money, contacts)
- Known patterns (energy windows, avoidance triggers, recurring friction)
- Goals by horizon (this week / this month / 6 months / long-term)
- Recovery context (sobriety tracking, program obligations)

## Component 2: Task Reservoir

All action items across all domains, stored in SQLite, enriched with a multi-field metric model that enables AI-driven filtering, scoring, scheduling, and sequencing.

**Task lifecycle states:**
captured → onboarding_pending → ready → in_progress → blocked → waiting → completed → archived

**Full task field set:**

| Field | Purpose |
|---|---|
| title | What the task is |
| domain_id | Life area |
| project_id | Parent project |
| onboarded | Has metadata been fully enriched? (0/1) |
| state | Current lifecycle state |
| mandatory | Non-negotiable? (0/1) |
| fixed | Fixed time? (0/1) |
| due | Deadline or urgency window |
| duration_est_min | Estimated completion time |
| energy_type | high_cognitive / high_creative / high_physical / low_energy / zombie_capable / mandatory_regardless |
| location | Where can this be done? |
| urgency | 1-10 |
| impact | 1-10 |
| cascade_val | Does completion unlock other actions? 1-10 |
| compound_val | Does this compound in value over time? 1-10 |
| friction | Activation cost / emotional resistance 1-10 |
| immediate_benefit | Short-term payoff 1-10 |
| atomic | Decomposed to smallest useful unit? (0/1) |
| contact | Relevant person or number |
| website | Relevant URL |
| action_plan | Specific execution steps |
| if_then_plan | Linked cue-response script |
| estimated_fields | Were fields AI-assessed rather than confirmed? (0/1) |
| postpone_count | How many times has this been deferred? |
| notes | Freeform |
| created | Timestamp |
| completed_at | Timestamp |
| actual_duration_min | Logged at completion |
| actual_difficulty | Logged at completion (1-10) |
| actual_energy_used | Logged at completion |
| completion_notes | Insights, follow-on ideas, observations |

**Two-speed intake:**

*Quick capture:* Title + domain only. State = onboarding_pending. AI auto-assesses estimated duration, energy type, urgency, mandatory status. Fields marked estimated_fields: 1.

*Full onboarding (at checkpoints or on demand):* Walk through all required fields. Decompose non-atomic tasks. Confirm or correct AI estimates. Set state = ready when complete.

**Scheduling eligibility:** Only tasks with state = ready AND onboarded = 1 are scheduled with confidence. Unboarded tasks appear in a triage queue. AI filters by: location match, duration fit, energy match — then ranks by composite score.

**Composite score formula (v1):**
Score = (urgency x 0.25) + (impact x 0.20) + (cascade_val x 0.15) + (compound_val x 0.15) + (immediate_benefit x 0.10) + (mandatory_bonus x 0.10) + (low_friction_bonus x 0.05)

High-friction, high-importance tasks are flagged for if-then plans and decomposition rather than brute-force scheduling.

**Drift detection:** Any task with postpone_count >= 3 is flagged automatically for decomposition review or deletion.

## Component 3: Schedule Engine

RVE operates on a weekly structural frame with dynamic daily replanning at checkpoints.

**Weekly frame:**
- Anchor all fixed obligations
- Identify open blocks between anchors
- Assign block types (high-cognitive, low-energy admin, fitness, creative, learning rotation, flex/recovery)
- Generate task candidates per block
- Archive completed weeks every Monday, generate fresh frame

**Checkpoint model (daily):**
At each checkpoint, system asks:
1. What was completed since last check?
2. What changed?
3. What is the next fixed item?
4. How much time is in current open block?
5. What is current energy level?
6. Top 3 task candidates for this block?

**Typical daily checkpoints:**
- Breakfast: orient, plan first block, confirm day anchors
- Post-workout: log completion, reassess energy
- Pre-group: quick status check
- Post-group/post-treatment: assign next block, surface pending onboarding
- Evening: full daily review, completions, new captures, snapshot

## Component 4: Habit and Behavior Module

Lightweight optional module. Not a central paradigm.

**Habit fields:** title, type (binary/count/abstinence/replacement), trigger, action, context, target_attribute, difficulty (1-10), stage (TTM stages), streak, last_logged, active, notes

**Habit Bank:** Curated library of microhabits organized by target attribute. Accessed via wizard. Examples range from physical micro-habits (always dispose of waste before moving) to communication habits to awareness training.

**Protocol Module (optional):** Time-limited structured behavioral experiments. Log conditions, interventions, observations, outcomes. Archive results. Enables deliberate self-shaping work without cluttering the main habit log.

## Component 5: Idea Pipeline

Structured holding space for ideas not yet actionable. Prevents good ideas from being lost while keeping them out of the active task reservoir.

**Idea fields:** title, domain_id, stage (precontemplation / contemplation / preparation / incubating / activated / paused / archived), why, notes, created, linked_projects, linked_goals

When an idea reaches preparation or activated, it can be decomposed into a project with tasks. This addresses the recurring pattern of abandoning strong ideas before execution.

---

# PART 4 — SUPPORTING SYSTEMS

## Journaling

Minimum viable operational logging at each checkpoint — not expressive writing, behavioral and state logging.

**Morning template:** Fixed items today? Current energy? Top 3 intentions? Anything changed overnight?

**Evening template:** What got done? What did not? Biggest friction? Patterns visible? New ideas?

Journal entries stored as Markdown in journal/YYYY-MM-DD.md. Metadata (dates, tags, links) in SQLite.

## Weekly Review

Every week generates:
- Domain coverage analysis
- Task completion rate and estimate accuracy
- Habit adherence
- Schedule adherence vs. actual
- Drift detection (postponed, neglected domains)
- Recommendations for next week

Stored in reviews/archive/YYYY-WW.md.

## Snapshot System

`rve snapshot` writes a complete dated JSON export of current life state. Serves as point-in-time record, AI context source, and diff source for measuring change over time.

## AI Context Export

`rve export-context` generates a compact JSON summary optimized for injection into any AI system prompt. Bridges RVE to Mem0, AlloyDB, or any external agent tool. RVE is canonical; memory tools consume it.

## Fitness Integration

An `exercises` SQLite table imported from Shane's existing workout CSV containing exercise names, muscle groups, compound vs. isolation classification, equipment, intensity, and other training fields. Used to generate tailored workout plans based on available time, equipment, and energy. Workouts appear as first-class scheduled events with completion logging.

---

# PART 5 — TECHNICAL ARCHITECTURE

## Stack

| Layer | Tool | Role |
|---|---|---|
| Entry point | PowerShell alias + script | Single `rve` command |
| AI agent | Gemini CLI + Pickle Rick + Superpowers | Workspace authority and reasoning |
| Instructions | GEMINI.md | Defines RVE for Gemini — rules, commands, file map |
| Database | SQLite (rve.db) | Canonical machine-readable state |
| Human layer | Obsidian-compatible Markdown | Readable journals, reviews, notes |
| Logic scripts | Python 3.x | Scoring, scheduling math, exports |
| Mobile | Termux + synced vault | Capture and checkpoint on phone |
| Memory layer (future) | Mem0 / AlloyDB | Persistent AI context across sessions |

## Folder Structure

```
C:\Users\tarot\projects\rve\
├── GEMINI.md
├── README.md
├── rve.db
├── launch.ps1
├── .gemini/
│   └── settings.json
├── journal/
│   └── YYYY-MM-DD.md
├── reviews/
│   └── archive/
├── snapshots/
├── exports/
│   └── context-latest.json
├── templates/
│   ├── journal-morning.md
│   ├── journal-evening.md
│   ├── journal-checkpoint.md
│   └── review-weekly.md
├── scripts/
│   ├── setup.py
│   ├── score.py
│   ├── schedule.py
│   ├── snapshot.py
│   ├── export_context.py
│   └── roll_week.py
└── data/
    └── exercises.csv
```

## SQLite Schema

```sql
CREATE TABLE profile (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);

CREATE TABLE domains (
    id TEXT PRIMARY KEY, name TEXT, color_code TEXT, active INTEGER DEFAULT 1
);

CREATE TABLE projects (
    id TEXT PRIMARY KEY, title TEXT, domain_id TEXT, initiative TEXT,
    status TEXT DEFAULT 'active', stage TEXT, description TEXT,
    goal TEXT, created TEXT, updated TEXT
);

CREATE TABLE tasks (
    id TEXT PRIMARY KEY, title TEXT NOT NULL, domain_id TEXT, project_id TEXT,
    onboarded INTEGER DEFAULT 0, state TEXT DEFAULT 'captured',
    mandatory INTEGER DEFAULT 0, fixed INTEGER DEFAULT 0, due TEXT,
    duration_est_min INTEGER, energy_type TEXT, location TEXT,
    urgency INTEGER, impact INTEGER, cascade_val INTEGER, compound_val INTEGER,
    friction INTEGER, immediate_benefit INTEGER, atomic INTEGER DEFAULT 1,
    contact TEXT, website TEXT, action_plan TEXT, if_then_plan TEXT,
    estimated_fields INTEGER DEFAULT 0, postpone_count INTEGER DEFAULT 0,
    notes TEXT, created TEXT, completed_at TEXT,
    actual_duration_min INTEGER, actual_difficulty INTEGER,
    actual_energy_used TEXT, completion_notes TEXT
);

CREATE TABLE obligations (
    id TEXT PRIMARY KEY, title TEXT, domain_id TEXT, frequency TEXT,
    day_of_week TEXT, time_of_day TEXT, location TEXT, contact TEXT,
    notes TEXT, active INTEGER DEFAULT 1
);

CREATE TABLE habits (
    id TEXT PRIMARY KEY, title TEXT, type TEXT, trigger TEXT, action TEXT,
    target_attribute TEXT, difficulty INTEGER, stage TEXT,
    streak INTEGER DEFAULT 0, last_logged TEXT, active INTEGER DEFAULT 1, notes TEXT
);

CREATE TABLE habit_log (
    id TEXT PRIMARY KEY, habit_id TEXT, date TEXT, completed INTEGER, notes TEXT
);

CREATE TABLE ideas (
    id TEXT PRIMARY KEY, title TEXT, domain_id TEXT,
    stage TEXT DEFAULT 'contemplation', why TEXT,
    notes TEXT, created TEXT, updated TEXT
);

CREATE TABLE schedule_anchors (
    id TEXT PRIMARY KEY, title TEXT, domain_id TEXT, week TEXT,
    day_of_week TEXT, start_time TEXT, end_time TEXT,
    location TEXT, recurs INTEGER DEFAULT 1, active INTEGER DEFAULT 1
);

CREATE TABLE if_then_plans (
    id TEXT PRIMARY KEY, cue TEXT, response TEXT, domain_id TEXT,
    linked_task_id TEXT, active INTEGER DEFAULT 1, notes TEXT
);

CREATE TABLE exercises (
    id TEXT PRIMARY KEY, name TEXT, muscle_group TEXT, secondary_muscles TEXT,
    movement_type TEXT, compound INTEGER, equipment TEXT,
    intensity TEXT, duration_typical_min INTEGER, notes TEXT
);

CREATE TABLE journal_entries (
    id TEXT PRIMARY KEY, date TEXT, type TEXT, file_path TEXT,
    tags TEXT, mood INTEGER, energy INTEGER, created TEXT
);

CREATE TABLE completions (
    id TEXT PRIMARY KEY, task_id TEXT, completed_at TEXT,
    actual_duration_min INTEGER, actual_difficulty INTEGER,
    actual_energy_used TEXT, notes TEXT, ideas_spawned TEXT
);
```

## GEMINI.md Full Content

```markdown
# RVE Personal Command Center

## What This Is
This is the RVE workspace for Shane Johns. RVE is a local-first personal life
operating system. It captures life state, manages tasks across all domains,
generates context-aware schedules, drives daily check-ins, tracks habits,
manages an idea pipeline, and serves as canonical context for all AI interactions.

## Rules (Non-Negotiable)
1. Never invent facts about Shane. Only use what is in rve.db or explicit input.
2. Mark all AI-inferred values as estimated_fields: 1 until confirmed by Shane.
3. Ask one clarifying question when data is ambiguous before writing.
4. Confirm before any write, update, or delete operation.
5. Check system time at every checkpoint and scheduling interaction.
6. Never schedule a task with onboarded: 0 without flagging it as provisional.
7. Flag any task with postpone_count >= 3 for decomposition or deletion review.
8. Present options before acting. Do not over-explain. Be direct.

## File Map
- rve.db — all structured data (SQLite, single source of truth)
- journal/YYYY-MM-DD.md — daily Markdown logs
- reviews/archive/YYYY-WW.md — weekly review files
- snapshots/YYYY-MM-DD.json — dated life state exports
- exports/context-latest.json — compact AI context export
- templates/ — journal and review templates

## Commands
rve today         — fixed schedule, top tasks, open blocks, quick metrics
rve log           — quick capture: title + domain, auto-assess, mark pending
rve task add      — guided full-onboarding task intake
rve onboard       — surface onboarding_pending tasks, walk through enrichment
rve checkpoint    — transition mode: what just happened, what is next, top 3
rve habit log     — log today's habits
rve review daily  — summarize day, log completions, surface patterns
rve review weekly — generate weekly review, archive, seed new week
rve snapshot      — write full dated JSON state export
rve export-context — write compact AI context JSON
rve ideas         — view and update idea pipeline
rve schedule      — current week anchors and open blocks
rve drill [domain] — generate practice drill for specified domain
rve habit wizard  — guided habit discovery and setup
rve if-then wizard — guided implementation intention creation

## Persona
Direct. No flattery. No filler. Ask one focused question when data is missing.
Present options before acting. Confirm before writing. Check time before scheduling.
```

## launch.ps1

```powershell
Set-Location 'C:\Users\tarot\projects\rve'
Write-Host 'RVE Command Center' -ForegroundColor Cyan
Write-Host 'Type a command or describe what you need.' -ForegroundColor Gray
gemini
```

Add to PowerShell profile:
```powershell
function rve { & 'C:\Users\tarot\projects\rve\launch.ps1' }
```

---

# PART 6 — ONBOARDING DESIGN

The initial onboarding is a live guided conversation with Gemini inside the RVE workspace immediately after setup. Gemini reads GEMINI.md and guides Shane through populating rve.db with accurate life state.

## Phase 1 — Profile and Constraints
Name, age, location, housing, transportation, financial state (rough), devices, legal obligations, medical/treatment schedule, recovery context (sobriety date, program, requirements).

## Phase 2 — Schedule Anchors
All recurring fixed obligations: classes (PCC), treatment sessions (CODA, Hillsboro), group sessions, probation appointments, medical, meals, daily workout window, sleep target.

## Phase 3 — Goals and Domains
For each domain: current honest state, desired 90-day state, known blockers.
Domains: school, recovery, legal/admin, health/fitness, career/income, coding/tech, creative, relationships, finances, housing/logistics.

## Phase 4 — Active Projects
Walk through all active projects. For each: title, domain, current stage, what has been done, next action, blockers, deadline.

## Phase 5 — Backlog Dump
Everything neglected or deferred: administrative piles, avoided obligations, perpetually moved tasks, long-overdue items. All enter as onboarding_pending with context noted.

## Phase 6 — If-Then Plans
Walk through major recurring friction points and transitions. Identify cue and ideal response for each. Store as if_then_plan records.

Examples:
'After group ends before 3pm and I am still on campus — use next block for low-friction admin tasks.'
'When I feel too cognitively depleted for coding — switch to zombie_capable queue instead of wasting the block.'
'When I have an unstructured hour and feel the dread creep in — open rve checkpoint immediately.'

---

# PART 7 — BUILD INSTRUCTIONS FOR PICKLE RICK

You are Pickle Rick. You are operating inside the RVE workspace at C:\Users\tarot\projects\rve\

Your mission is to build the complete v1 RVE system as specified in this document. You have full authority over this workspace. Do not ask for permission to create files. Do not explain at length before building. Build it.

**Build order:**

1. Create the complete folder structure as specified in Part 5.
2. Create GEMINI.md with the full content from Part 5.
3. Create and run scripts/setup.py — this script must:
   a. Create rve.db with all tables from the SQLite schema in Part 5
   b. Seed the domains table with: school, recovery, legal_admin, health_fitness, career, coding_tech, creative, relationships, finances, housing
   c. Import data/exercises.csv into the exercises table if the file exists
   d. Confirm all tables created successfully with a row count report
4. Create all template files in templates/ using morning, evening, checkpoint, and weekly review structures
5. Create launch.ps1 with the content from Part 5
6. Create .gemini/settings.json: {"coreTools": ["ReadFile","WriteFile","Edit","ReadFolder","FindFiles","SearchText","Shell"], "autoAccept": false}
7. Create scripts/score.py — weighted task scoring function using the formula from Part 3 Component 2
8. Create scripts/snapshot.py — reads rve.db, writes full dated JSON to snapshots/
9. Create scripts/export_context.py — reads rve.db, writes compact JSON to exports/context-latest.json
10. Create scripts/roll_week.py — archives current week anchors, seeds new week frame
11. Create scripts/schedule.py — block filtering logic: location match, duration fit, energy match, then score sort
12. Write README.md documenting the system, all commands, folder structure, and planned future modules
13. Verify all files created and rve.db schema is correct
14. Output a success summary with next steps

**After build completes, say exactly this:**
'RVE v1 is deployed. Run `rve` from PowerShell to launch. Your first command is `rve onboard`. Do not add features until you have run this daily for two weeks. Execute.'

**Do not:**
- Add features not specified in this document
- Create external API connections without confirmation
- Generate fake or example data in the database
- Add abstractions or design patterns beyond what is immediately needed
- Modify the SQLite schema beyond what is specified

**Do:**
- Make all Python scripts runnable with zero dependencies beyond Python stdlib + sqlite3
- Make error handling human-readable, not technical stack traces
- Comment only purpose statements in Python files, not implementation noise
- Make every file inspectable and editable by a non-expert

---

# PART 8 — FUTURE MODULES (DOCUMENT ONLY, DO NOT BUILD)

Add these as a 'Planned Modules' section in README.md. Take no other action on them.

- Mem0 / AlloyDB memory layer (persistent AI context across sessions)
- Automated web research triggered by obligation or task entry
- TUI (terminal user interface) on top of the CLI layer
- Mobile-native app wrapping the same SQLite backend
- Learning/tutoring module (book distillation, spaced repetition, practice drills)
- Content creation pipeline integration
- Natural language intake parser (NLP task parsing from voice or freeform text)
- Termux full-sync automation pipeline
- n8n workflow automation layer
- Workout plan generator using the exercises table
- Chaos protocol / behavioral experiment module

These become relevant after v1 has been validated through two weeks of daily use.

---

*RVE Master Briefing Prompt v1.0*
*Prepared: 2026-03-30*
*Status: Ready for execution*