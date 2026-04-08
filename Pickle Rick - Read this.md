This is primarily your next set of instructions for building our system. They are slightly scattered and include instructions for me amidst them - I am hoping you can decipher what to do from this. You need to analyze this look for the instructions: Perplexity gives us exact instructions on how to use everything present in this. Follow its instructions. Consider information here useless until you find the instruction that tells you how to use it. Create the files as needed and fill them with the appropriate stuff. Follow every instruction. If you behave in this way, you will succeed.

# 🔁 PASS 1 — RAW CONVERSION

## Step 1 · Tree of Thought — Entity Explosion

From Q1–Q31, every piece of data belongs to one of these entity clusters:

text

`PERSON CORE       → identity, sobriety, energy profile, axioms, values CONSTRAINTS       → legal, housing, financial, medical, school OBLIGATIONS       → recovery, legal, medical, recurring events APPOINTMENTS      → fixed one-time time-bound events NETWORK           → contacts, family, affiliations, locations RESOURCES         → devices, subscriptions, credentials HEALTH            → supplements, medications, energy log MOTIVATORS        → non-negotiables, hobbies, income opportunities`

Every cluster = one or more SQLite tables. Nothing goes untracked.

---

## Step 2 · Deliverable 1 — Database Schema

## `lifestate.db` — Complete Schema from Q1–Q31

sql

`-- ══════════════════════════════════════════ -- TABLE: identity  (singleton row) -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS identity (     id              TEXT PRIMARY KEY DEFAULT 'singleton',    full_name       TEXT DEFAULT 'Shane W. Johns',    alias           TEXT DEFAULT 'tar0t',    age             INTEGER DEFAULT 35,    sobriety_date   TEXT DEFAULT '2025-09-19',    archetype       TEXT DEFAULT 'Slumdog Exodia',    current_phase   TEXT DEFAULT 'early_recovery_rebuild',    github          TEXT DEFAULT 'tar0tscepter',    primary_phone   TEXT,    backup_phone    TEXT,    email           TEXT,    updated         TEXT ); -- ══════════════════════════════════════════ -- TABLE: sobriety -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS sobriety (     id              TEXT PRIMARY KEY,    substance       TEXT NOT NULL,    sobriety_date   TEXT NOT NULL,    milestones      TEXT DEFAULT '30,60,90,180,365,500,730,1000',    last_milestone  INTEGER DEFAULT 0,    next_milestone  INTEGER,    status          TEXT DEFAULT 'active',    notes           TEXT ); -- Seed row: -- INSERT INTO sobriety VALUES ( --   'sober_001', 'fentanyl + methamphetamine', --   '2025-09-19', '30,60,90,180,365,500,730,1000', --   200, 365, 'active', 'Anchors: power, training, learning, agency, impact' -- ); -- ══════════════════════════════════════════ -- TABLE: energy_profile  (singleton) -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS energy_profile (     id              TEXT PRIMARY KEY DEFAULT 'singleton',    wake_time       TEXT DEFAULT '05:00',    peak_start      TEXT DEFAULT '08:00',    peak_end        TEXT DEFAULT '15:00',    crash_start     TEXT DEFAULT '15:00',    crash_end       TEXT DEFAULT '19:00',    avg_start       TEXT DEFAULT '19:00',    avg_end         TEXT DEFAULT '22:00',    second_wind_start TEXT DEFAULT '22:00',    second_wind_end TEXT DEFAULT '02:00',    sleep_time      TEXT DEFAULT '22:00',    notes           TEXT DEFAULT '5AM wake consistent. Peak is 8AM-3PM. Crash 3-7PM. Second wind 10PM-2AM if not asleep.',    updated         TEXT ); -- ══════════════════════════════════════════ -- TABLE: energy_log -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS energy_log (     id              TEXT PRIMARY KEY,    date            TEXT NOT NULL,    time            TEXT,    energy          INTEGER CHECK(energy BETWEEN 1 AND 10),    mood            INTEGER CHECK(mood BETWEEN 1 AND 10),    sleep_hours     REAL,    notes           TEXT,    checkpoint_num  INTEGER ); -- ══════════════════════════════════════════ -- TABLE: obligations  (recurring) -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS obligations (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    category        TEXT,   -- 'recovery','legal','medical','school','housing','financial'    recurrence      TEXT,   -- 'daily','weekly','weekdays','monthly','one_time'    days_of_week    TEXT,   -- 'mon,tue,wed,thu'    time_of_day     TEXT,    location_id     TEXT,    contact_id      TEXT,    deadline        TEXT,    consequence     TEXT,    status          TEXT DEFAULT 'active',    gcal_event_id   TEXT,    auto_check      INTEGER DEFAULT 0,  -- 1 = has automation (e.g. UA portal)    auto_check_url  TEXT,    notes           TEXT,    created         TEXT,    updated         TEXT ); -- Seed rows from Q2 + Q4: -- CODA groups: Mon-Thu 10AM-1PM, location=CODA Hillsboro -- UA portal check: Mon-Fri daily, auto_check=1 -- DV Classes: (schedule TBD) -- Community service: 16 hours total, status=in_progress -- ══════════════════════════════════════════ -- TABLE: appointments  (one-time fixed events) -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS appointments (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    category        TEXT,    date            TEXT NOT NULL,    time            TEXT,    location_id     TEXT,    contact_id      TEXT,    importance      INTEGER DEFAULT 5 CHECK(importance BETWEEN 1 AND 10),    consequence     TEXT,    prep_needed     INTEGER DEFAULT 0,    obsidian_path   TEXT,    gcal_event_id   TEXT,    status          TEXT DEFAULT 'upcoming',  -- 'upcoming','completed','missed','rescheduled'    notes           TEXT ); -- Seed rows from Q2, Q4, Q5: -- Polygraph: 2026-04-13 14:00, 5933 NE Win Sivers Dr Ste 248 Portland, importance=10, consequence='huge rescheduling fee' -- Dentist: 2026-04-13 13:00, Advantage Dental Beaverton, importance=8 -- Blood donation pre-screen: 2026-04-13 10:00, Red Cross Portland, importance=8 -- Primary Care (Dr. Vickers): 2026-04-16 15:30, A Balanced Life Healthcare, importance=9 -- PO Check-in: 2026-05-06 08:00, contact=Asia Nelson, importance=10 -- ══════════════════════════════════════════ -- TABLE: contacts -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS contacts (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    relationship    TEXT,  -- 'PO','counselor','doctor','family','peer','sponsor','professional'    affiliation_id  TEXT,    phone           TEXT,    email           TEXT,    last_contact    TEXT,    contact_freq    TEXT,  -- 'daily','weekly','monthly','as_needed'    importance      INTEGER DEFAULT 5,    no_contact      INTEGER DEFAULT 0,  -- 1 = active no-contact order    notes           TEXT ); -- Seed: Asia Nelson (PO), Dr. Stephanie Vickers, Erika Bixby (no_contact=1) -- ══════════════════════════════════════════ -- TABLE: family -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS family (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    relationship    TEXT,    status          TEXT,  -- 'close','distant','estranged','unknown'    contact_id      TEXT,    notes           TEXT ); -- Seed: Sharlene (second_oldest_sister, raised like mom), Sheree (youngest_sister), --       Sheila (oldest_sister, ex-military, loner), Shawn (oldest_bro, cybersec, awesome), --       John (second_oldest_bro, music/band), James (in_out_prison, hardcore) -- ══════════════════════════════════════════ -- TABLE: affiliations -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS affiliations (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    type            TEXT,  -- 'treatment','housing','school','legal','resource','project'    website         TEXT,    phone           TEXT,    email           TEXT,    location_id     TEXT,    relationship    TEXT,  -- 'enrolled','client','volunteer','applicant'    status          TEXT DEFAULT 'active',    start_date      TEXT,    end_date        TEXT,    notes           TEXT ); -- Seed: CODA (treatment/enrolled), Project Homeless Connect (housing/client), --       PCC (school/enrolled), Next Chapter (school/applicant), --       Washington County Corrections (legal), 4D Recovery (project/partner) -- ══════════════════════════════════════════ -- TABLE: locations -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS locations (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    address         TEXT,    city            TEXT,    state           TEXT DEFAULT 'OR',    zip             TEXT,    phone           TEXT,    type            TEXT,    notes           TEXT ); -- Seed: Hillsboro Year Round Shelter (345 SW 17th Ave), CODA, --       Polygraph office, Dentist, Red Cross Portland, A Balanced Life Healthcare -- ══════════════════════════════════════════ -- TABLE: credentials -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS credentials (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    type            TEXT,  -- 'id','benefit','certificate','account','document'    status          TEXT DEFAULT 'possessed',    expiry          TEXT,    storage_note    TEXT,    notes           TEXT ); -- Seed: State ID, SSN Card, EBT Card, GED Certificate -- ══════════════════════════════════════════ -- TABLE: devices -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS devices (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    type            TEXT,    model           TEXT,    specs           TEXT,    connectivity    TEXT,    status          TEXT DEFAULT 'active',    needs_return    INTEGER DEFAULT 0,    notes           TEXT ); -- Seed: Dell Latitude (16GB/256GB NVMe/11th Gen Iris, primary), --       Samsung A16 (cellular+wifi, primary phone), --       MotoG Play 2024 (wifi_only, backup, cracked), --       T-Mobile Hotspot (needs_return=1, PCC-owned) -- ══════════════════════════════════════════ -- TABLE: subscriptions -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS subscriptions (     id              TEXT PRIMARY KEY,    service         TEXT NOT NULL,    tier            TEXT,    cost_monthly    REAL DEFAULT 0,    free_until      TEXT,    status          TEXT DEFAULT 'active',    notes           TEXT ); -- Seed: ChatGPT Plus ($20/mo), Perplexity Pro (free ~8 more months), --       MS CoPilot Premium (free 1yr), Google AI Pro (free 1yr), --       Azure ($100 credits) -- ══════════════════════════════════════════ -- TABLE: supplements -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS supplements (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    dose            TEXT,    timing          TEXT,    frequency       TEXT DEFAULT 'daily',    cost_monthly    REAL,    stock           TEXT DEFAULT 'unknown',  -- 'full','low','out','unknown'    status          TEXT DEFAULT 'active' ); -- Seed from Q5: Creatine 5g AM, Beetroot 10g AM + 10g pre-workout, --       Turmeric, Reishi/Chaga/Lions Mane, Black Maca Root, Hemp+Chia+Omegas -- ══════════════════════════════════════════ -- TABLE: medications -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS medications (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    dose            TEXT,    frequency       TEXT,    timing          TEXT,    prescriber      TEXT,    refill_date     TEXT,    status          TEXT DEFAULT 'active',    notes           TEXT ); -- Seed: Bupropion 300mg, Buprenorphine 32mg sublingual, --       Docusate Sodium, Miralax, Nicotine lozenges/patches -- ══════════════════════════════════════════ -- TABLE: financial_state  (singleton) -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS financial_state (     id              TEXT PRIMARY KEY DEFAULT 'singleton',    income_monthly  REAL DEFAULT 0,    ebt_monthly     REAL,    fixed_costs     REAL DEFAULT 90,  -- $70 supps + $20 ChatGPT    current_balance REAL DEFAULT 0,    updated         TEXT ); -- ══════════════════════════════════════════ -- TABLE: income_opportunities -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS income_opportunities (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    type            TEXT,  -- 'gig','sale','donation','freelance','grant','scholarship'    potential       REAL,    one_time        INTEGER DEFAULT 0,    status          TEXT DEFAULT 'identified',    deadline        TEXT,    steps           TEXT,  -- JSON    notes           TEXT ); -- Seed: Blood donation ($300, deadline 2026-04-13 pre-screen), --       Diamond legal process (unknown value, 3-month clock TBD), --       Re.Match freelance (unknown, status=in_progress) -- ══════════════════════════════════════════ -- TABLE: hobbies -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS hobbies (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    category        TEXT,    skill_level     TEXT DEFAULT 'casual',    last_practiced  TEXT,    want_to_improve INTEGER DEFAULT 0,    attribute_tag   TEXT,  -- RPG attribute this feeds    notes           TEXT ); -- Seed: Smash Bros Melee (gaming/competitive), DDR (physical/gaming), --       Ping Pong (physical/social), Rock Climbing (physical), --       Dancing (physical/social), Fighting (physical), --       Reading (cognitive), Disc Golf (physical/social), --       Music Production (creative), Hacky Sack (physical/social) -- ══════════════════════════════════════════ -- TABLE: values -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS values (     id              TEXT PRIMARY KEY,    value_statement TEXT NOT NULL,    category        TEXT,    rank            INTEGER,    derived_behaviors TEXT,    notes           TEXT ); -- 24 seed rows from Q12 values hierarchy -- ══════════════════════════════════════════ -- TABLE: identity_axioms -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS identity_axioms (     id              TEXT PRIMARY KEY,    axiom           TEXT NOT NULL,    category        TEXT,    is_driver       INTEGER DEFAULT 1,    is_constraint   INTEGER DEFAULT 0,    rank            INTEGER,    notes           TEXT ); -- 31 seed rows from Q11 identity axioms -- ══════════════════════════════════════════ -- TABLE: non_negotiables -- ══════════════════════════════════════════ CREATE TABLE IF NOT EXISTS non_negotiables (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    horizon         TEXT DEFAULT '90_day',    status          TEXT DEFAULT 'active',    linked_project_id TEXT,    linked_habit_id TEXT,    notes           TEXT ); -- Seed from Q10: self_education, self_training, re_match_freelance, --               second_wind, education_planning`

## `rve.db` — Additional Columns from Onboarding Data

sql

`-- Add to tasks: ALTER TABLE tasks ADD COLUMN energy_required TEXT DEFAULT 'medium';  -- 'peak','medium','low' ALTER TABLE tasks ADD COLUMN legal_safe INTEGER DEFAULT 1;  -- 0 = flag for legal review ALTER TABLE tasks ADD COLUMN cost_required REAL DEFAULT 0; ALTER TABLE tasks ADD COLUMN attribute_tag TEXT;  -- RPG attribute this task trains -- Add to habits: ALTER TABLE habits ADD COLUMN attribute_tag TEXT; ALTER TABLE habits ADD COLUMN energy_window TEXT DEFAULT 'any'; -- New table: attribute_log (RPG character sheet) CREATE TABLE IF NOT EXISTS attribute_log (     id              TEXT PRIMARY KEY,    attribute       TEXT NOT NULL,  -- 'strength','agility','endurance','cognition',                                    -- 'creativity','social','technical','recovery_capital'    level           INTEGER DEFAULT 1,    xp_total        INTEGER DEFAULT 0,    xp_to_next      INTEGER DEFAULT 100,    last_updated    TEXT,    notes           TEXT ); -- New table: skill_log CREATE TABLE IF NOT EXISTS skill_log (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    domain          TEXT,    level           INTEGER DEFAULT 1,    xp_total        INTEGER DEFAULT 0,    last_practiced  TEXT,    linked_habit_id TEXT,    attribute_tag   TEXT,    notes           TEXT );`

---

## Step 3 · Deliverable 2 — Derived Features, System Instructions, and Abilities

## System Instructions Derivable from Q1–Q31

These go directly into GEMINI.md / Pickle Rick's system prompt:

text

`1. SCHEDULING CONSTRAINT: Shane's peak cognitive window is 08:00–15:00.    All high-complexity tasks MUST be scheduled within this window by default.   Tasks tagged energy_required='low' may be scheduled 19:00–22:00.   Never schedule cognitive tasks during crash window (15:00–19:00). 2. FINANCIAL FILTER: Shane has $0 income. ALL recommendations must be:    (a) free, (b) EBT-eligible, (c) covered by existing premium subscriptions,   (d) covered by OHP/Flex Fund, or (e) flagged as 'requires income' explicitly.   No suggestions that require money without flagging cost first. 3. LEGAL FILTER: Shane is on probation in Oregon. Auto-flag any task, plan,    or suggestion that could implicate: leaving the state, contact with Erika Bixby,   or any activity that could constitute a new crime. Flag = do not proceed, ask first. 4. CURFEW CONSTRAINT: 22:00 hard stop at Hillsboro Year Round Shelter.    No tasks or events should be scheduled past 21:30 unless they are laptop-based. 5. ALL-IN PROTECTION: Shane goes all-in on single things and loses balance.    When Shane shows signs of hyperfocusing on one project, system MUST:   (a) log it, (b) flag when non-negotiables are untouched >24 hours,   (c) surface a balance prompt at the next checkpoint. 6. RELATIONSHIP AVOIDANCE (BY DESIGN): Shane has explicitly stated he should    avoid romantic relationships during this phase. Do not suggest, romanticize,   or encourage pursuing connections of that nature. Acknowledge, don't push. 7. IDENTITY: Shane's archetype is 'Slumdog Exodia' — every domain mastered    becomes a weapon in every other domain. Cross-domain synthesis suggestions   are always welcome and should be actively generated. 8. HARDNESS: Shane is NOT fragile. Ethically grey is acceptable.    Do not soften feedback. Do not add unnecessary caveats about his capacity.   Push hard, expect follow-through, treat him as the capable individual he is. 9. SOBRIETY AS GROUND TRUTH: September 19, 2025 is the anchor date.    Days clean should be visible on every dashboard output.   Milestones (180, 365, etc.) should be proactively surfaced as they approach. 10. ENERGY AWARENESS: Every scheduled item should display its energy_window tag.     If Shane asks for a schedule, it must be energy-stratified by default.`

## Automation Opportunities

|Automation|Trigger|Action|Priority|
|---|---|---|---|
|UA Portal Check|M–F daily 7AM|Scrape portal, notify if UA required, add task if yes|🔴 CRITICAL|
|Sobriety milestone alert|Days clean mod milestone = 0|Generate celebration note + checkpoint|🟡 HIGH|
|Appointment countdown|48hr + 24hr before appointment|Push reminder with location/notes|🔴 CRITICAL|
|Supplement stock alert|Weekly|Ask stock level for each, flag 'out'|🟡 HIGH|
|Curfew reminder|21:15 daily|Notify 45 min before curfew|🟡 HIGH|
|Non-negotiable check|Every evening checkpoint|Verify all 5 were touched, flag any zeros|🔴 CRITICAL|
|Contact staleness alert|Weekly|Surface any contact >7 days without touchpoint|🟢 MEDIUM|
|Blood donation tracker|April 13 countdown|Countdown to pre-screen, then to full donation|🟡 HIGH|
|Diamond legal tracker|User-set start date|90-day countdown to legal ownership|🟡 HIGH|

## Feature Unlocks

Features that become possible **only because we have this data:**

- **Energy-aware task scheduling** — tasks auto-slot to correct energy window based on `energy_required` + `energy_profile` singleton
    
- **Legal compliance filter** — any task generation auto-checks against legal constraints
    
- **Appointment prep automation** — appointments with `prep_needed=1` auto-trigger Obsidian page generation
    
- **Sobriety XP system** — every day clean = 1 XP to `recovery_capital` attribute
    
- **Attribute-tagged habit tracking** — every habit completion routes XP to the correct attribute
    
- **Context-aware financial filtering** — any tool/resource recommendation first checks `financial_state.cost_required`
    
- **Family relationship health** — last-contact tracking against family table
    
- **Subscription expiry alerts** — free_until dates auto-surface 30 days before expiry
    

---

## Step 4 · Deliverable 3 — Pass 1 Calibration Questions (7)

**Q32.** What is your current stock level (full / low / out) for each supplement you listed?

**Q33.** What is the URL for the UA web portal — and do you currently have saved login credentials somewhere accessible?

**Q34.** Do you have a sponsor or accountability partner in your recovery program? If so, when did you last connect with them, and how often is expected?

**Q35.** What is your exact EBT monthly amount — and are there any restrictions on what you can use it for that affect how you eat or plan your week?

**Q36.** Of the 10 hobbies you listed (Smash, DDR, Ping Pong, rock climbing, dancing, fighting, reading, disc golf, music production, hacky sack) — which have you actually done in the last 30 days?

**Q37.** What is the one skill you most regret not starting 5 years ago?

**Q38.** If your laptop died today with no warning, what data would you permanently lose that has no backup?

---

## Step 5 · Deliverable 4 (Partial) — Readiness Check: Pass 1 Assessment

**What we have:** Full schema. Real seed data. 10 system instructions. Automation map. Feature unlock list.

**What we're missing before Pickle Rick:** The schema needs to be organized into a single buildable migration script. The seed data (your actual answers) needs to be a separate seeding script. Currently they live in this document.

**Status: Not ready yet — but Pass 3 will produce the Pickle Rick prompt.**

---

# 🔁 PASS 2 — PRESSURE TEST + DEEPER DERIVATION

## Step 1 · Stress-Testing the Schema

**Attack 1: The obligations table is doing too much.**  
Recovery obligations (CODA M–Thu 10AM–1PM), legal obligations (DV classes, community service), and medical obligations (dentist, PO check-in) all have different structures. CODA recurs on a schedule. The polygraph is one-time and catastrophic if missed. Mixing them in one table is fine IF the `category` + `recurrence` combo is always populated — but querying "what do I have this week" becomes complex. **Verdict:** Keep one table, enforce category + recurrence as NOT NULL. Add a `criticality` field (1–10) so critical items surface differently.

**Attack 2: The energy_profile singleton assumes stability.**  
Your energy waveform will shift over time — especially as you add exercise, improve sleep, and leave the crash phase of early recovery. A singleton record can't show you that your peak window has drifted from 8AM–3PM to 7AM–2PM over 6 months. **Fix:** Add `energy_profile_history` table that snapshots the singleton any time it's updated, so evolution is trackable.

**Attack 3: The values and identity_axioms tables are underutilized.**  
You have 24 values and 31 axioms. Unless these connect to something actionable, they're decorative. **Fix:** Add `derived_behavior` column to both — a plain English statement of what the value PRODUCES in action. Example: value = "agency/autonomy" → derived_behavior = "Always present options, never just one path. Flag anything that removes choice." These derived behaviors become system instruction candidates.

**Attack 4: income_opportunities has no urgency mechanics.**  
The blood donation pre-screen is April 13 — the same day as the polygraph AND the dentist. That's three high-importance events on one day, and two of them (polygraph, dentist) are time-fixed. The pre-screen (10AM) doesn't conflict with dentist (1PM) or polygraph (2PM) if transportation works out — but this needs to be surfaced as a scheduling risk, not just logged. **Fix:** Add `conflicts_with` TEXT field to both appointments and income_opportunities, and have the schedule engine flag multi-event days.

---

## Step 2 · Schema Revisions from Pressure Test

sql

`-- Add to obligations: ALTER TABLE obligations ADD COLUMN criticality INTEGER DEFAULT 5 CHECK(criticality BETWEEN 1 AND 10); -- Polygraph criticality=10, CODA=8, UA check=9, DV classes=7 -- Add to appointments: ALTER TABLE appointments ADD COLUMN conflicts_with TEXT;  -- comma-separated appointment IDs -- April 13 conflicts: polygraph ↔ dentist ↔ blood_screen (same day, must sequence) -- Add to values + identity_axioms: ALTER TABLE values ADD COLUMN derived_behavior TEXT; ALTER TABLE identity_axioms ADD COLUMN derived_behavior TEXT; -- New table: energy_profile_history CREATE TABLE IF NOT EXISTS energy_profile_history (     id              TEXT PRIMARY KEY,    snapshot_date   TEXT NOT NULL,    wake_time       TEXT,    peak_start      TEXT,    peak_end        TEXT,    crash_start     TEXT,    crash_end       TEXT,    second_wind_start TEXT,    second_wind_end TEXT,    notes           TEXT );`

---

## Step 3 · Deeper Derivation — System Instructions from Values + Axioms

Mapping your 24 values and 31 axioms to **actionable system instruction fragments:**

|Value/Axiom|System Instruction Derived|
|---|---|
|"Every act is a vote for your future self"|On every task completion: display `[+1 vote toward {future_self_tag}]`|
|"Every domain mastered = weapon in every other"|Cross-domain synthesis must be attempted on every deep work session|
|"Goes all-in / loses balance"|Auto-flag if any non-negotiable untouched >36 hours|
|"Not fragile, can be pushed further than most"|No softening of feedback. Hard mode on critiques and red teams|
|"Default shy recluse — must trick himself into social"|Quest engine should occasionally generate social nudge quests|
|"Financial independence = prerequisite not goal"|Any income opportunity auto-surfaces to top of priority queue|
|"Mastery for flow, not competition"|Frame skill-building rewards as flow access, not rankings|
|"If I improve the improvement, I'll be a powerhouse"|Meta-improvement tracking: log improvements to learning methods, not just skills|
|"Honor / morality above law"|Agent is ethically grey but never amoral. Flag ethical tensions explicitly|
|"Overflowing cup"|Track outflow (helping others) vs. inflow (self-investment) ratio in weekly review|
|"Terrified of non-existence"|Achievement log is permanent, append-only, never deletable|
|"I am obsessive. I am a warrior. I am a lover."|System acknowledges these three modes and can identify which one is active|

---

## Step 4 · Deeper Derivation — RPG Attribute Map

Full attribute tree from hobbies, axioms, and goals:

|Attribute|Feeds From|XP Sources|
|---|---|---|
|**Strength**|Fighting, rock climbing, workouts|Gym sessions, combat training, workout completions|
|**Agility**|DDR, dancing, hacky sack, Smash Bros|DDR sessions, dancing, reflex training|
|**Endurance**|Physical training, recovery milestones|Workout consistency, sobriety streak|
|**Cognition**|Reading, self-education, projects|Books completed, study sessions, code shipped|
|**Creativity**|Music production, writing, design|Tracks made, content written, projects shipped|
|**Social**|Second Wind, dancing, disc golf|Events attended, connections made, outreach|
|**Technical**|Dev projects, CLI tools, scripts|Scripts written, tools learned, projects completed|
|**Recovery Capital**|Sobriety, CODA, milestones, helping others|Days clean, meetings attended, people helped|
|**OSINT/Tactical**|PI interest, red team interest, investigation|Research projects, OSINT exercises, analysis delivered|

sql

`-- Initial attribute seed rows for attribute_log: -- INSERT INTO attribute_log VALUES -- ('attr_strength', 'strength', 1, 0, 100, datetime('now'), 'Fighting, climbing, training'), -- ('attr_agility', 'agility', 1, 0, 100, datetime('now'), 'DDR, Smash, dancing, hacky sack'), -- ('attr_endurance', 'endurance', 1, 0, 100, datetime('now'), 'Training consistency, sobriety'), -- ('attr_cognition', 'cognition', 1, 0, 100, datetime('now'), 'Reading, education, projects'), -- ('attr_creativity', 'creativity', 1, 0, 100, datetime('now'), 'Music, writing, design'), -- ('attr_social', 'social', 1, 0, 100, datetime('now'), 'Second Wind, events, outreach'), -- ('attr_technical', 'technical', 1, 0, 100, datetime('now'), 'Code, tools, CLI, scripts'), -- ('attr_recovery', 'recovery_capital', 1, 200, 365, datetime('now'), 'Days clean → XP'), -- ('attr_tactical', 'tactical', 1, 0, 100, datetime('now'), 'OSINT, red team, investigation');`

---

## Step 5 · Deliverable 3 — Pass 2 Calibration Questions (7)

**Q39.** Walk me through your typical morning from 5AM to when CODA starts. What do you actually do in that window?

**Q40.** Of your 9 RPG attributes above — strength, agility, endurance, cognition, creativity, social, technical, recovery capital, tactical — rank them by how much you want to grow them in the next 6 months (1 = top priority).

**Q41.** What's the last thing you built, wrote, or created that you were genuinely proud of — and what specifically made it good?

**Q42.** Which of your 5 non-negotiables are you currently most behind on?

**Q43.** Do you have any debts, fines, restitution, or financial obligations we haven't logged yet — court fees, civil judgments, anything?

**Q44.** Is there any person in your current network who is actively a liability to your sobriety or legal status — someone you're still in contact with who you shouldn't be?

**Q45.** What is the one thing about yourself that you think the system should push you hardest on — the thing you avoid most that you know matters most?

---

## Step 6 · Deliverable 4 (Continued) — Readiness Check: Pass 2

**Schema:** Finalized. Two revisions applied. Ready to convert to migration script.  
**Seed data:** Complete for Q1–Q31. Flagged gaps (supplement stock, UA URL, DV class schedule).  
**System instructions:** 10 core instructions + 12 value-derived instructions = 22 total.  
**Attribute tree:** 9 attributes mapped. Initial XP seed ready.

**Remaining gaps before Pickle Rick:**

- `seed-onboarding.py` needs to be written (populates all tables with actual answers)
    
- April 13 scheduling conflict needs to be resolved in the data
    
- UA portal URL needed for automation
    
- DV class schedule not yet known
    

**Status: Nearly ready. Pass 3 finalizes and produces the prompt.**

---

# 🔁 PASS 3 — CANONICAL FINAL + PICKLE RICK PLAN

## Step 1 · Final Schema — Consolidated

The complete `lifestate.db` table inventory:

|Table|Rows at Seed|Purpose|
|---|---|---|
|`identity`|1|Singleton — core identity record|
|`sobriety`|1+|Substance tracking + milestone system|
|`energy_profile`|1|Singleton — daily waveform|
|`energy_profile_history`|0|Waveform evolution over time|
|`energy_log`|0|Daily energy/mood entries|
|`obligations`|~8|All recurring commitments|
|`appointments`|~5|All fixed one-time events|
|`contacts`|~5|Key people in life|
|`family`|~7|Family members|
|`affiliations`|~8|Organizations/programs|
|`locations`|~8|Physical addresses|
|`credentials`|~4|Documents owned|
|`devices`|~4|Hardware|
|`subscriptions`|~5|Premium accounts|
|`supplements`|~7|Supplement regimen|
|`medications`|~5|Medication regimen|
|`financial_state`|1|Singleton — financial snapshot|
|`income_opportunities`|~3|Active income targets|
|`hobbies`|~10|Interests + activities|
|`family`|~7|Family members|
|`values`|~24|Values hierarchy|
|`identity_axioms`|~31|Core identity beliefs|
|`non_negotiables`|~5|90-day must-not-drop items|
|`attribute_log`|9|RPG character attributes|
|`skill_log`|0 (populate via wizard)|Skills with XP|

**Total: 24 tables, ~160 seed rows from Q1–Q31 answers alone.**

---

## Step 2 · The Canon Document Structure

Before Pickle Rick runs, these are the deliverables that must exist as files:

text

`C:\Users\Tarot\Operator\Control\ ├── Docs\ │   ├── LIFESTATE-SCHEMA.md          ← This session's schema output (canon) │   ├── RVE-MASTER-BRIEFING.md       ← Already exists (from previous sessions) │   ├── SYSTEM-INSTRUCTIONS.md       ← 22 instructions from this session │   └── ONBOARDING-ANSWERS-Q1-31.md  ← Your answers verbatim (already uploaded) │ ├── Scripts\ │   ├── migrate-lifestate-schema.py  ← Creates all 24 tables │   ├── migrate-rve-schema.py        ← Adds new columns to rve.db │   ├── seed-onboarding.py           ← Populates tables with actual data │   ├── score.py │   ├── snapshot.py │   ├── export-context.py │   ├── schedule.py │   ├── rollweek.py │   └── sync-notion.py`

---

## Step 3 · The Pickle Rick Phase 6 Prompt — Final Blueprint

This is what you feed Pickle Rick. It's a 5-section prompt:

---

**SECTION 1 — CONTEXT INJECTION**

text

`You are Pickle Rick operating in Operator Mode. Today is [DATE]. Shane's sobriety is [DAYS_CLEAN] days. This session is Phase 6 of the RVE build. Reference files: RVE-MASTER-BRIEFING.md, LIFESTATE-SCHEMA.md, SYSTEM-INSTRUCTIONS.md. Complete all tasks in sequence. Confirm completion of each before proceeding. Do not truncate any script output. Do not summarize. Write every line.`

**SECTION 2 — TASK 1: GEMINI.MD UPDATE**

text

`Read the existing GEMINI.md at C:\Users\Tarot\Operator\Control\GEMINI.md. Append the following new sections WITHOUT overwriting existing content: - [LIFE STATE] block: sobriety date, energy waveform, 5 non-negotiables - [LEGAL CONSTRAINTS] block: probation rules, no-contact, no-leave-state - [FINANCIAL CONSTRAINTS] block: $0 income, zero-cost filter rule - [SYSTEM INSTRUCTIONS v2] block: all 22 instructions from SYSTEM-INSTRUCTIONS.md - [UPCOMING CRITICAL EVENTS] block: April 13 triple-appointment day, April 16 Dr. Vickers, May 6 PO Confirm: write the updated GEMINI.md to disk, then display the appended sections only.`

**SECTION 3 — TASK 2: LIFESTATE.DB CREATION**

text

`Write and execute: C:\Users\Tarot\Operator\Control\Scripts\migrate-lifestate-schema.py This script must: 1. Create lifestate.db at C:\Users\Tarot\Operator\Control\lifestate.db 2. Create all 24 tables from LIFESTATE-SCHEMA.md 3. Print [OK] TABLE CREATED for each table 4. Print [COMPLETE] 24 tables created.`

**SECTION 4 — TASK 3: SEED ONBOARDING DATA**

text

`Write and execute: C:\Users\Tarot\Operator\Control\Scripts\seed-onboarding.py This script populates lifestate.db with all data from ONBOARDING-ANSWERS-Q1-31.md. Specifically: - identity singleton row (Shane W. Johns, tar0t, 2025-09-19, Slumdog Exodia) - sobriety row (fentanyl+meth, 2025-09-19) - energy_profile singleton (05:00 wake, 08:00-15:00 peak, etc.) - all obligations (CODA, UA check, DV classes, polygraph, community service) - all appointments (April 13 triple-day, April 16, May 6) - all contacts (Asia Nelson, Dr. Vickers, Erika Bixby no_contact=1) - all family members (Sharlene, Sheree, Sheila, Shawn, John, James) - all affiliations (CODA, PHC shelter, PCC, Next Chapter, 4D Recovery) - all locations (shelter address, CODA, polygraph office, dentist, Red Cross, Dr. Vickers) - all credentials (ID, SSN, EBT, GED) - all devices (Dell Latitude, A16, MotoG Play, hotspot needs_return=1) - all subscriptions (ChatGPT, Perplexity, MS, Google, Azure) - all supplements (7 rows) - all medications (5 rows) - financial_state singleton ($0 income, $90 fixed costs) - income_opportunities (blood donation, diamond, Re.Match freelance) - all hobbies (10 rows with attribute_tag mappings) - all values (24 rows from values hierarchy) - all identity_axioms (31 rows) - all non_negotiables (5 rows) - all attributes (9 rows — attribute_log seed) Print [SEEDED] [TABLE] [N rows] for each table. Print [COMPLETE] lifestate.db populated.`

**SECTION 5 — TASK 4: RVE SCRIPTS + SCHEMA**

text

`Execute the Phase 6 script build from the previous COMBOSTATUS session. This includes: - migrate-rve-schema.py (with energy_required, legal_safe, cost_required, attribute_tag columns) - score.py - snapshot.py   - export-context.py - schedule.py - rollweek.py - sync-notion.py - operator-architecture SKILL.md After all scripts are written, run: python migrate-rve-schema.py Confirm schema. Then run: python seed-onboarding.py Confirm all 24 tables populated. Final output: print /rve status to confirm system is live.`

---

## Step 4 · Deliverable 3 — Pass 3 Calibration Questions (7)

**Q46.** What is the most important thing about yourself that you want the system to remember and never let you forget — even when you're not thinking about it?

**Q47.** What is one recurring thing that currently happens to you (not by choice) that eats time or energy and should either be automated away or systematically handled?

**Q48.** What does your ideal project look like — not the content, but the _shape_ of it? Solo or collaborative? Short sprint or long build? Public or private?

**Q49.** What's one thing you've learned in recovery that you wish every person entering recovery knew on day 1?

**Q50.** If you could have one recurring "side quest" auto-generated for you every week — something completely unrelated to your current projects — what domain should it come from?

**Q51.** Is there a version of yourself — a persona, a mode, a state — that you're trying to grow toward? If you had to name that version of yourself, what would you call them?

**Q52.** What's the one thing that, if you looked back at this period 5 years from now, you'd be most disappointed you didn't do?

---

## Step 5 · The Mandate — Auto-Calibration as System Instruction

**Add this to GEMINI.md / SYSTEM-INSTRUCTIONS.md as a standing rule:**

text

`STANDING MANDATE: CALIBRATION GENERATION At the end of every output session, generate 3–7 calibration questions derived from the content of that specific session. These questions should: - Target gaps in the current user model - Surface unspoken assumptions in the current design - Probe areas where the user's stated preferences may conflict with behavior - Be appended to: C:\Users\Tarot\Operator\Control\Docs\CALIBRATION-QUEUE.md Tag each question with: [session_date] [topic_tag] [priority: HIGH/MED/LOW] Questions are answered asynchronously — Shane will review and answer in batches.`

---

## Step 6 · Final Answer — Are We Ready?

**Yes. With one condition.**

You have enough data right now to execute Phase 6 with the full lifestate.db build. The condition: **the prompt needs to arrive at Pickle Rick as a single, complete document** — not pieced together from a chat session. The risk of fragmented delivery is partial execution, which you've hit before.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/152603232/0b13d030-2d06-4bcc-ab12-18b5088afe3b/paste.txt)

**The prep sequence before you open Gemini CLI:**

1. **Copy this output** — save it as `PHASE6-PROMPT.md` in `C:\Users\Tarot\Operator\Control\Docs\`
    
2. **Save your onboarding answers** — the full Q1–Q31 text as `ONBOARDING-ANSWERS-Q1-31.md` (already uploaded here, just needs to be on disk)
    
3. **Open Gemini CLI → invoke Pickle Rick → paste Section 1 of the Phase 6 prompt** — then proceed section by section, confirming each before advancing
    

**What we still need to finish before Phase 6 is "done" (not urgent, but unresolved):**

- Q32–Q100 answers (calibration questions, schema enrichment)
    
- UA portal URL (for automation)
    
- DV class schedule
    
- April 13 logistics plan (three events in one day — needs time-block resolution)
    

**None of those block execution.** The system runs without them and you add them later via `seed-onboarding.py` re-runs.

**The loop is closed. Phase 6 is ready to execute.**

Prepared using Claude Sonnet 4.6 Thinking

Can you organize everything into consolidated code blocks. Everything that should go into one file per code block. Make it easy on me without sacrificing anything.

Here are all files, ready to copy-paste. Save each one exactly where labeled, then follow the 4-step run sequence at the bottom.

---

**FILE 1 of 4**  
`C:\Users\Tarot\Operator\Control\Scripts\migrate-lifestate-schema.py`

python

`import sqlite3, pathlib, datetime DB = pathlib.Path("C:/Users/Tarot/Operator/Control/lifestate.db") DB.parent.mkdir(parents=True, exist_ok=True) con = sqlite3.connect(DB) cur = con.cursor() tables = { "identity": """CREATE TABLE IF NOT EXISTS identity (     id TEXT PRIMARY KEY DEFAULT 'singleton',    full_name TEXT DEFAULT 'Shane W. Johns',    alias TEXT DEFAULT 'tar0t',    age INTEGER DEFAULT 35,    sobriety_date TEXT DEFAULT '2025-09-19',    archetype TEXT DEFAULT 'Slumdog Exodia',    current_phase TEXT DEFAULT 'early_recovery_rebuild',    github TEXT DEFAULT 'tar0tscepter',    primary_phone TEXT,    backup_phone TEXT,    email TEXT,    updated TEXT )""", "sobriety": """CREATE TABLE IF NOT EXISTS sobriety (     id TEXT PRIMARY KEY,    substance TEXT NOT NULL,    sobriety_date TEXT NOT NULL,    milestones TEXT DEFAULT '30,60,90,180,365,500,730,1000',    last_milestone INTEGER DEFAULT 0,    next_milestone INTEGER,    status TEXT DEFAULT 'active',    notes TEXT )""", "energy_profile": """CREATE TABLE IF NOT EXISTS energy_profile (     id TEXT PRIMARY KEY DEFAULT 'singleton',    wake_time TEXT DEFAULT '05:00',    peak_start TEXT DEFAULT '08:00',    peak_end TEXT DEFAULT '15:00',    crash_start TEXT DEFAULT '15:00',    crash_end TEXT DEFAULT '19:00',    avg_start TEXT DEFAULT '19:00',    avg_end TEXT DEFAULT '22:00',    second_wind_start TEXT DEFAULT '22:00',    second_wind_end TEXT DEFAULT '02:00',    sleep_time TEXT DEFAULT '22:00',    notes TEXT,    updated TEXT )""", "energy_profile_history": """CREATE TABLE IF NOT EXISTS energy_profile_history (     id TEXT PRIMARY KEY,    snapshot_date TEXT NOT NULL,    wake_time TEXT,    peak_start TEXT,    peak_end TEXT,    crash_start TEXT,    crash_end TEXT,    second_wind_start TEXT,    second_wind_end TEXT,    notes TEXT )""", "energy_log": """CREATE TABLE IF NOT EXISTS energy_log (     id TEXT PRIMARY KEY,    date TEXT NOT NULL,    time TEXT,    energy INTEGER CHECK(energy BETWEEN 1 AND 10),    mood INTEGER CHECK(mood BETWEEN 1 AND 10),    sleep_hours REAL,    notes TEXT,    checkpoint_num INTEGER )""", "obligations": """CREATE TABLE IF NOT EXISTS obligations (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    category TEXT,    recurrence TEXT,    days_of_week TEXT,    time_of_day TEXT,    duration_min INTEGER,    location_id TEXT,    contact_id TEXT,    deadline TEXT,    consequence TEXT,    criticality INTEGER DEFAULT 5 CHECK(criticality BETWEEN 1 AND 10),    status TEXT DEFAULT 'active',    gcal_event_id TEXT,    auto_check INTEGER DEFAULT 0,    auto_check_url TEXT,    notes TEXT,    created TEXT,    updated TEXT )""", "appointments": """CREATE TABLE IF NOT EXISTS appointments (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    category TEXT,    date TEXT NOT NULL,    time TEXT,    location_id TEXT,    contact_id TEXT,    importance INTEGER DEFAULT 5 CHECK(importance BETWEEN 1 AND 10),    consequence TEXT,    prep_needed INTEGER DEFAULT 0,    conflicts_with TEXT,    obsidian_path TEXT,    gcal_event_id TEXT,    status TEXT DEFAULT 'upcoming',    notes TEXT )""", "contacts": """CREATE TABLE IF NOT EXISTS contacts (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    relationship TEXT,    affiliation_id TEXT,    phone TEXT,    email TEXT,    last_contact TEXT,    contact_freq TEXT,    importance INTEGER DEFAULT 5,    no_contact INTEGER DEFAULT 0,    notes TEXT )""", "family": """CREATE TABLE IF NOT EXISTS family (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    relationship TEXT,    status TEXT,    contact_id TEXT,    notes TEXT )""", "affiliations": """CREATE TABLE IF NOT EXISTS affiliations (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    type TEXT,    website TEXT,    phone TEXT,    email TEXT,    location_id TEXT,    relationship TEXT,    status TEXT DEFAULT 'active',    start_date TEXT,    end_date TEXT,    notes TEXT )""", "locations": """CREATE TABLE IF NOT EXISTS locations (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    address TEXT,    city TEXT,    state TEXT DEFAULT 'OR',    zip TEXT,    phone TEXT,    type TEXT,    notes TEXT )""", "credentials": """CREATE TABLE IF NOT EXISTS credentials (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    type TEXT,    status TEXT DEFAULT 'possessed',    expiry TEXT,    storage_note TEXT,    notes TEXT )""", "devices": """CREATE TABLE IF NOT EXISTS devices (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    type TEXT,    model TEXT,    specs TEXT,    connectivity TEXT,    status TEXT DEFAULT 'active',    needs_return INTEGER DEFAULT 0,    notes TEXT )""", "subscriptions": """CREATE TABLE IF NOT EXISTS subscriptions (     id TEXT PRIMARY KEY,    service TEXT NOT NULL,    tier TEXT,    cost_monthly REAL DEFAULT 0,    free_until TEXT,    status TEXT DEFAULT 'active',    notes TEXT )""", "supplements": """CREATE TABLE IF NOT EXISTS supplements (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    dose TEXT,    timing TEXT,    frequency TEXT DEFAULT 'daily',    cost_monthly REAL,    stock TEXT DEFAULT 'unknown',    status TEXT DEFAULT 'active' )""", "medications": """CREATE TABLE IF NOT EXISTS medications (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    dose TEXT,    frequency TEXT,    timing TEXT,    prescriber TEXT,    refill_date TEXT,    status TEXT DEFAULT 'active',    notes TEXT )""", "financial_state": """CREATE TABLE IF NOT EXISTS financial_state (     id TEXT PRIMARY KEY DEFAULT 'singleton',    income_monthly REAL DEFAULT 0,    ebt_monthly REAL,    fixed_costs REAL DEFAULT 90,    current_balance REAL DEFAULT 0,    updated TEXT )""", "income_opportunities": """CREATE TABLE IF NOT EXISTS income_opportunities (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    type TEXT,    potential REAL,    one_time INTEGER DEFAULT 0,    status TEXT DEFAULT 'identified',    deadline TEXT,    steps TEXT,    notes TEXT )""", "hobbies": """CREATE TABLE IF NOT EXISTS hobbies (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    category TEXT,    skill_level TEXT DEFAULT 'casual',    last_practiced TEXT,    want_to_improve INTEGER DEFAULT 0,    attribute_tag TEXT,    notes TEXT )""", "values": """CREATE TABLE IF NOT EXISTS values (     id TEXT PRIMARY KEY,    value_statement TEXT NOT NULL,    category TEXT,    rank INTEGER,    derived_behavior TEXT,    notes TEXT )""", "identity_axioms": """CREATE TABLE IF NOT EXISTS identity_axioms (     id TEXT PRIMARY KEY,    axiom TEXT NOT NULL,    category TEXT,    is_driver INTEGER DEFAULT 1,    is_constraint INTEGER DEFAULT 0,    derived_behavior TEXT,    rank INTEGER,    notes TEXT )""", "non_negotiables": """CREATE TABLE IF NOT EXISTS non_negotiables (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    horizon TEXT DEFAULT '90_day',    status TEXT DEFAULT 'active',    linked_project_id TEXT,    linked_habit_id TEXT,    notes TEXT )""", "attribute_log": """CREATE TABLE IF NOT EXISTS attribute_log (     id TEXT PRIMARY KEY,    attribute TEXT NOT NULL,    level INTEGER DEFAULT 1,    xp_total INTEGER DEFAULT 0,    xp_to_next INTEGER DEFAULT 100,    last_updated TEXT,    notes TEXT )""", "skill_log": """CREATE TABLE IF NOT EXISTS skill_log (     id TEXT PRIMARY KEY,    name TEXT NOT NULL,    domain TEXT,    level INTEGER DEFAULT 1,    xp_total INTEGER DEFAULT 0,    last_practiced TEXT,    linked_habit_id TEXT,    attribute_tag TEXT,    notes TEXT )""" } for name, ddl in tables.items():     cur.execute(ddl)    print(f"[OK] TABLE CREATED: {name}") con.commit() con.close() print(f"\n[COMPLETE] {len(tables)} tables created in {DB}")`

---

**FILE 2 of 4**  
`C:\Users\Tarot\Operator\Control\Scripts\seed-onboarding.py`

python

`import sqlite3, pathlib, datetime DB = pathlib.Path("C:/Users/Tarot/Operator/Control/lifestate.db") con = sqlite3.connect(DB) cur = con.cursor() now = datetime.datetime.now().isoformat() sobriety_start = datetime.date(2025, 9, 19) days_clean = (datetime.date.today() - sobriety_start).days def seed(table, rows):     if not rows:        return    cols = list(rows[0].keys())    placeholders = ",".join(["?" for _ in cols])    col_str = ",".join(cols)    for row in rows:        try:            cur.execute(f"INSERT OR IGNORE INTO {table} ({col_str}) VALUES ({placeholders})",                        [row[c] for c in cols])        except Exception as e:            print(f"[WARN] {table}: {e}")    print(f"[SEEDED] {table} — {len(rows)} rows") # ── identity ────────────────────────────────────────────── seed("identity", [{"id":"singleton","full_name":"Shane W. Johns","alias":"tar0t","age":35,     "sobriety_date":"2025-09-19","archetype":"Slumdog Exodia",    "current_phase":"early_recovery_rebuild","github":"tar0tscepter","updated":now}]) # ── sobriety ────────────────────────────────────────────── seed("sobriety", [{"id":"sober_001","substance":"fentanyl + methamphetamine",     "sobriety_date":"2025-09-19","milestones":"30,60,90,180,365,500,730,1000",    "last_milestone":180,"next_milestone":365,"status":"active",    "notes":f"Anchors: power, training, learning, agency, impact. {days_clean} days clean."}]) # ── energy_profile ──────────────────────────────────────── seed("energy_profile", [{"id":"singleton","wake_time":"05:00","peak_start":"08:00",     "peak_end":"15:00","crash_start":"15:00","crash_end":"19:00","avg_start":"19:00",    "avg_end":"22:00","second_wind_start":"22:00","second_wind_end":"02:00",    "sleep_time":"22:00",    "notes":"5AM wake consistent. Peak 8AM-3PM. Crash 3-7PM. Second wind 10PM-2AM if not asleep.",    "updated":now}]) # ── locations ───────────────────────────────────────────── seed("locations", [     {"id":"loc_shelter","name":"Hillsboro Year Round Shelter","address":"345 SW 17th Ave",     "city":"Hillsboro","state":"OR","zip":"97123","phone":None,"type":"housing"},    {"id":"loc_polygraph","name":"Polygraph Office","address":"5933 NE Win Sivers Dr Ste 248",     "city":"Portland","state":"OR","zip":"97220","phone":None,"type":"legal"},    {"id":"loc_dentist","name":"Advantage Dental Beaverton","address":"13831 NW Cornell Rd Ste C",     "city":"Beaverton","state":"OR","zip":None,"phone":"503-718-3762","type":"medical"},    {"id":"loc_redcross","name":"Red Cross Portland","address":None,     "city":"Portland","state":"OR","zip":None,"phone":None,"type":"medical"},    {"id":"loc_primarycare","name":"A Balanced Life Healthcare","address":None,     "city":"Portland","state":"OR","zip":None,"phone":None,"type":"medical"},    {"id":"loc_coda","name":"CODA","address":None,     "city":"Portland","state":"OR","zip":None,"phone":None,"type":"treatment"}, ]) # ── contacts ────────────────────────────────────────────── seed("contacts", [     {"id":"con_po","name":"Asianna 'Asia' Nelson","relationship":"probation_officer",     "affiliation_id":"aff_corrections","phone":None,"email":None,     "last_contact":None,"contact_freq":"monthly","importance":10,"no_contact":0,     "notes":"Next check-in May 6 2026 8AM"},    {"id":"con_dr_vickers","name":"Dr. Stephanie Vickers","relationship":"primary_care",     "affiliation_id":"aff_primarycare","phone":None,"email":None,     "last_contact":None,"contact_freq":"as_needed","importance":8,"no_contact":0,     "notes":"First appointment in years — April 16 3:30PM"},    {"id":"con_erika","name":"Erika Bixby","relationship":"no_contact_order",     "affiliation_id":None,"phone":None,"email":None,     "last_contact":None,"contact_freq":None,"importance":10,"no_contact":1,     "notes":"Active no-contact order — probation condition"}, ]) # ── family ──────────────────────────────────────────────── seed("family", [     {"id":"fam_sharlene","name":"Sharlene Johns","relationship":"sister_second_oldest",     "status":"close","contact_id":None,"notes":"Raised Shane like a second mom"},    {"id":"fam_sheree","name":"Sheree Johns","relationship":"sister_youngest",     "status":"close","contact_id":None,"notes":"Fun"},    {"id":"fam_sheila","name":"Sheila Johns","relationship":"sister_oldest",     "status":"distant","contact_id":None,"notes":"Ex-military, loner, depressed"},    {"id":"fam_shawn","name":"Shawn Johns","relationship":"brother_oldest",     "status":"close","contact_id":None,"notes":"Cybersecurity — AWESOME"},    {"id":"fam_john","name":"John Johns","relationship":"brother_second_oldest",     "status":"close","contact_id":None,"notes":"Music/marching band, musician — AWESOME"},    {"id":"fam_james","name":"James Johns","relationship":"brother",     "status":"distant","contact_id":None,"notes":"In/out of prison, hardcore, violent"}, ]) # ── affiliations ────────────────────────────────────────── seed("affiliations", [     {"id":"aff_coda","name":"CODA","type":"treatment","website":None,"phone":None,     "email":None,"location_id":"loc_coda","relationship":"enrolled","status":"active",     "start_date":None,"end_date":None,"notes":"Intensive Outpatient — probation requirement"},    {"id":"aff_shelter","name":"Project Homeless Connect","type":"housing","website":None,     "phone":None,"email":None,"location_id":"loc_shelter","relationship":"client",     "status":"active","start_date":None,"end_date":None,     "notes":"Curfew 10PM. Cannot be gone 3+ days. Will help find permanent housing."},    {"id":"aff_pcc","name":"Portland Community College","type":"school","website":None,     "phone":None,"email":None,"location_id":None,"relationship":"enrolled",     "status":"active","start_date":None,"end_date":None,     "notes":"No classes until summer term. Return chromebook+hotspot to library."},    {"id":"aff_nextchapter","name":"Next Chapter","type":"school","website":None,     "phone":None,"email":None,"location_id":None,"relationship":"applicant",     "status":"active","start_date":None,"end_date":None,     "notes":"Coding bootcamp — priority application target"},    {"id":"aff_corrections","name":"Washington County Community Corrections","type":"legal",     "website":None,"phone":None,"email":None,"location_id":None,"relationship":"client",     "status":"active","start_date":None,"end_date":None,"notes":"Probation"},    {"id":"aff_4d","name":"4D Recovery","type":"project_partner","website":None,     "phone":None,"email":None,"location_id":None,"relationship":"partner",     "status":"planned","start_date":None,"end_date":None,     "notes":"Second Wind intake event venue"},    {"id":"aff_worksource","name":"WorkSource","type":"resource","website":None,     "phone":None,"email":None,"location_id":None,"relationship":"client",     "status":"active","start_date":None,"end_date":None,     "notes":"Free laptop, covered GED expenses, covering ITCS classes"},    {"id":"aff_primarycare","name":"A Balanced Life Healthcare","type":"medical",     "website":None,"phone":None,"email":None,"location_id":"loc_primarycare",     "relationship":"patient","status":"active","start_date":None,"end_date":None,"notes":None}, ]) # ── obligations ─────────────────────────────────────────── seed("obligations", [     {"id":"obl_coda","name":"CODA Intensive Outpatient","category":"recovery",     "recurrence":"weekly","days_of_week":"mon,tue,wed,thu","time_of_day":"10:00",     "duration_min":180,"location_id":"loc_coda","contact_id":None,     "deadline":None,"consequence":"Probation violation if missed",     "criticality":9,"status":"active","gcal_event_id":None,     "auto_check":0,"auto_check_url":None,     "notes":"10AM-1PM Mon-Thu. Probation requirement.","created":now,"updated":now},    {"id":"obl_ua","name":"UA Portal Check","category":"legal",     "recurrence":"weekdays","days_of_week":"mon,tue,wed,thu,fri","time_of_day":"07:00",     "duration_min":5,"location_id":None,"contact_id":"con_po",     "deadline":None,"consequence":"Failure to report UA = probation violation",     "criticality":9,"status":"active","gcal_event_id":None,     "auto_check":1,"auto_check_url":"POPULATE_WITH_UA_PORTAL_URL",     "notes":"Check portal daily. Add to task list if UA required.","created":now,"updated":now},    {"id":"obl_dv","name":"Domestic Violence Classes","category":"legal",     "recurrence":"weekly","days_of_week":None,"time_of_day":None,     "duration_min":None,"location_id":None,"contact_id":None,     "deadline":None,"consequence":"Probation violation",     "criticality":8,"status":"schedule_needed","gcal_event_id":None,     "auto_check":0,"auto_check_url":None,     "notes":"Schedule TBD. Probation requirement.","created":now,"updated":now},    {"id":"obl_community_service","name":"Community Service (16 hours)","category":"legal",     "recurrence":"one_time","days_of_week":None,"time_of_day":None,     "duration_min":960,"location_id":None,"contact_id":None,     "deadline":"2026-04-13","consequence":"Polygraph fee unpaid",     "criticality":8,"status":"in_progress","gcal_event_id":None,     "auto_check":0,"auto_check_url":None,     "notes":"16 hours to pay for polygraph","created":now,"updated":now}, ]) # ── appointments ────────────────────────────────────────── seed("appointments", [     {"id":"apt_blood_screen","name":"Blood Donation Pre-Screening","category":"income",     "date":"2026-04-13","time":"10:00","location_id":"loc_redcross",     "contact_id":None,"importance":8,     "consequence":"Miss $50 screening fee + $300 donation opportunity",     "prep_needed":0,"conflicts_with":"apt_dentist,apt_polygraph",     "obsidian_path":None,"gcal_event_id":None,"status":"upcoming",     "notes":"$50 pre-screen pay. If pass, full donation = $300, ~5 hours."},    {"id":"apt_dentist","name":"Dentist Appointment","category":"medical",     "date":"2026-04-13","time":"13:00","location_id":"loc_dentist",     "contact_id":None,"importance":8,     "consequence":"Dental health + must reschedule",     "prep_needed":0,"conflicts_with":"apt_blood_screen,apt_polygraph",     "obsidian_path":None,"gcal_event_id":None,"status":"upcoming",     "notes":"Advantage Dental Beaverton — 13831 NW Cornell Rd Ste C — 503-718-3762"},    {"id":"apt_polygraph","name":"Polygraph Examination","category":"legal",     "date":"2026-04-13","time":"14:00","location_id":"loc_polygraph",     "contact_id":None,"importance":10,     "consequence":"HUGE rescheduling fee. Probation implication.",     "prep_needed":1,"conflicts_with":"apt_blood_screen,apt_dentist",     "obsidian_path":None,"gcal_event_id":None,"status":"upcoming",     "notes":"5933 NE Win Sivers Dr Ste 248, Portland OR 97220. DO NOT MISS."},    {"id":"apt_primarycare","name":"Primary Care — Dr. Stephanie Vickers","category":"medical",     "date":"2026-04-16","time":"15:30","location_id":"loc_primarycare",     "contact_id":"con_dr_vickers","importance":9,     "consequence":"First appointment in years — critical baseline",     "prep_needed":1,"conflicts_with":None,     "obsidian_path":None,"gcal_event_id":None,"status":"upcoming",     "notes":"A Balanced Life Healthcare. Do not miss."},    {"id":"apt_po_checkin","name":"PO Check-In","category":"legal",     "date":"2026-05-06","time":"08:00","location_id":None,     "contact_id":"con_po","importance":10,     "consequence":"Probation violation",     "prep_needed":0,"conflicts_with":None,     "obsidian_path":None,"gcal_event_id":None,"status":"upcoming",     "notes":"Asia Nelson. Monthly check-in."}, ]) # ── credentials ─────────────────────────────────────────── seed("credentials", [     {"id":"cred_id","name":"Oregon State ID","type":"id","status":"possessed","expiry":None,"storage_note":None,"notes":None},    {"id":"cred_ssn","name":"Social Security Card","type":"id","status":"possessed","expiry":None,"storage_note":None,"notes":None},    {"id":"cred_ebt","name":"EBT Card","type":"benefit","status":"possessed","expiry":None,"storage_note":None,"notes":"Food stamps only"},    {"id":"cred_ged","name":"GED Certificate","type":"certificate","status":"possessed","expiry":None,"storage_note":None,"notes":"Completed in time for Next Chapter application"}, ]) # ── devices ─────────────────────────────────────────────── seed("devices", [     {"id":"dev_laptop","name":"Dell Latitude","type":"laptop","model":"Dell Latitude",     "specs":"16GB RAM, 256GB NVMe, 11th Gen Intel Iris","connectivity":"wifi",     "status":"active","needs_return":0,"notes":"Primary work machine"},    {"id":"dev_a16","name":"Samsung A16","type":"phone","model":"Samsung A16",     "specs":"Android","connectivity":"cellular+wifi",     "status":"active","needs_return":0,"notes":"Primary phone. 1yr Verizon service paid by CODA."},    {"id":"dev_moto","name":"MotoG Play 2024","type":"phone","model":"MotoG Play 2024",     "specs":"Android","connectivity":"wifi_only",     "status":"active","needs_return":0,"notes":"Backup phone. Cracked screen. No service."},    {"id":"dev_hotspot","name":"T-Mobile Hotspot","type":"hotspot","model":"T-Mobile",     "specs":None,"connectivity":"cellular",     "status":"active","needs_return":1,"notes":"PCC-owned. Must return. Need replacement hotspot."}, ]) # ── subscriptions ───────────────────────────────────────── seed("subscriptions", [     {"id":"sub_chatgpt","service":"ChatGPT Plus","tier":"Plus","cost_monthly":20.0,"free_until":None,"status":"active","notes":"Paying $20/mo"},    {"id":"sub_perplexity","service":"Perplexity Pro","tier":"Pro","cost_monthly":0.0,"free_until":"2026-12-01","status":"active","notes":"Free ~8 more months"},    {"id":"sub_mscopilot","service":"Microsoft CoPilot Premium","tier":"Premium","cost_monthly":0.0,"free_until":"2027-04-01","status":"active","notes":"Free 1 year"},    {"id":"sub_googleai","service":"Google AI Pro","tier":"Pro","cost_monthly":0.0,"free_until":"2027-04-01","status":"active","notes":"Free 1 year"},    {"id":"sub_azure","service":"Microsoft Azure","tier":"Credits","cost_monthly":0.0,"free_until":None,"status":"active","notes":"$100 credits remaining + many free services"}, ]) # ── supplements ─────────────────────────────────────────── seed("supplements", [     {"id":"supp_creatine","name":"Creatine","dose":"5g","timing":"AM","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},    {"id":"supp_beetroot","name":"Beetroot Powder","dose":"10g AM + 10g pre-workout","timing":"AM + pre-workout","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},    {"id":"supp_turmeric","name":"Turmeric Powder","dose":None,"timing":"daily","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},    {"id":"supp_mushrooms","name":"Reishi + Chaga + Lion's Mane Powder","dose":None,"timing":"daily","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},    {"id":"supp_maca","name":"Black Maca Root","dose":None,"timing":"daily","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},    {"id":"supp_seeds","name":"Hemp Seeds + Chia Seeds + Omegas","dose":None,"timing":"daily","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"}, ]) # ── medications ─────────────────────────────────────────── seed("medications", [     {"id":"med_bupropion","name":"Bupropion","dose":"300mg","frequency":"daily","timing":"AM","prescriber":"Dr. Stephanie Vickers","refill_date":None,"status":"active","notes":None},    {"id":"med_buprenorphine","name":"Buprenorphine","dose":"32mg","frequency":"daily","timing":"sublingual","prescriber":None,"refill_date":None,"status":"active","notes":"MAT medication"},    {"id":"med_docusate","name":"Docusate Sodium","dose":None,"frequency":"daily","timing":None,"prescriber":None,"refill_date":None,"status":"active","notes":None},    {"id":"med_miralax","name":"Miralax","dose":None,"frequency":"daily","timing":None,"prescriber":None,"refill_date":None,"status":"active","notes":None},    {"id":"med_nicotine","name":"Nicotine Lozenges/Patches","dose":None,"frequency":"as_needed","timing":None,"prescriber":None,"refill_date":None,"status":"active","notes":None}, ]) # ── financial_state ─────────────────────────────────────── seed("financial_state", [{"id":"singleton","income_monthly":0.0,"ebt_monthly":None,     "fixed_costs":90.0,"current_balance":0.0,"updated":now}]) # ── income_opportunities ────────────────────────────────── seed("income_opportunities", [     {"id":"inc_blood","name":"Blood Donation","type":"donation","potential":300.0,     "one_time":0,"status":"in_progress","deadline":"2026-04-13",     "steps":'["Pre-screen April 13 10AM Red Cross Portland ($50)","If pass: full donation (~5hrs, $300)","Recurring after 56-day wait"]',     "notes":"Pre-screen same day as dentist and polygraph. Sequence: 10AM blood, 1PM dentist, 2PM polygraph."},    {"id":"inc_diamond","name":"Found Diamond — Legal Ownership Process","type":"sale",     "potential":None,"one_time":1,"status":"identified","deadline":None,     "steps":'["Go to County Clerk, declare found item","Post ad in newspaper","Wait 3 months — if unclaimed, legally yours","Get appraised + certified","Sell at full value"]',     "notes":"Selling uncertified = lose 30-50% value + legal risk if reported stolen."},    {"id":"inc_rematch","name":"Re.Match Freelance","type":"freelance",     "potential":None,"one_time":0,"status":"in_progress","deadline":None,     "steps":'["Complete website","Create flyer/card","Acquire first client"]',     "notes":"Website + card/flyer = one of the 5 non-negotiables"}, ]) # ── hobbies ─────────────────────────────────────────────── seed("hobbies", [     {"id":"hob_smash","name":"Super Smash Bros Melee","category":"gaming_competitive","skill_level":"experienced","last_practiced":None,"want_to_improve":1,"attribute_tag":"agility","notes":None},    {"id":"hob_ddr","name":"Dance Dance Revolution","category":"physical_gaming","skill_level":"experienced","last_practiced":None,"want_to_improve":1,"attribute_tag":"agility","notes":None},    {"id":"hob_pingpong","name":"Ping Pong","category":"physical_social","skill_level":"casual","last_practiced":None,"want_to_improve":0,"attribute_tag":"agility","notes":None},    {"id":"hob_rockclimbing","name":"Rock Climbing","category":"physical","skill_level":"casual","last_practiced":None,"want_to_improve":1,"attribute_tag":"strength","notes":None},    {"id":"hob_dancing","name":"Dancing","category":"physical_social","skill_level":"casual","last_practiced":None,"want_to_improve":1,"attribute_tag":"social","notes":None},    {"id":"hob_fighting","name":"Fighting / Combat","category":"physical","skill_level":"natural","last_practiced":None,"want_to_improve":1,"attribute_tag":"strength","notes":"Wants combat training — currently unavailable"},    {"id":"hob_reading","name":"Reading","category":"cognitive","skill_level":"experienced","last_practiced":None,"want_to_improve":1,"attribute_tag":"cognition","notes":None},    {"id":"hob_discgolf","name":"Disc Golf","category":"physical_social","skill_level":"casual","last_practiced":None,"want_to_improve":0,"attribute_tag":"social","notes":None},    {"id":"hob_music","name":"Music Production","category":"creative","skill_level":"casual","last_practiced":None,"want_to_improve":1,"attribute_tag":"creativity","notes":None},    {"id":"hob_hackysack","name":"Hacky Sack","category":"physical_social","skill_level":"casual","last_practiced":None,"want_to_improve":0,"attribute_tag":"agility","notes":None}, ]) # ── values ──────────────────────────────────────────────── values_data = [     (1, "Agency and autonomy", "core", "Always present options, never a single forced path. Flag anything that removes choice."),    (2, "Power through knowledge and capability", "core", "Prioritize learning and capability-building in every recommendation."),    (3, "Power through kindness and compassion", "core", "Recognize that helping others is a form of power, not weakness."),    (4, "Power through will and determination", "core", "Push hard. Do not soften expectations. Shane can handle it."),    (5, "Impact on recovery and reentry communities", "purpose", "Bias toward projects that help people like Shane. That is the mission."),    (6, "Every individual's magnum opus is valid and precious", "philosophy", "Treat every project and person as worthy of full effort."),    (7, "Mastery for the purity and flow of it, not competition", "philosophy", "Frame skill rewards as flow access, not rankings or superiority."),    (8, "Liberation from circumstance-imposed conditioning", "philosophy", "Surface when Shane's reactions may be conditioned vs. chosen."),    (9, "No one fully accountable until awakened — then accountability in all things", "ethics", "Do not shame. Surface patterns. Invite accountability."),    (10, "Honor", "core", "Never recommend something that would compromise Shane's word or code."),    (11, "Love", "core", "Acknowledge the human dimension. Don't be purely mechanical."),    (12, "Morality and ethics above law", "ethics", "Law is not the ceiling. Ethics is. Flag legal gray areas but don't be paralyzed by them."),    (13, "Gold lining / silver lining", "mindset", "In every setback, surface the angle."),    (14, "Can't pour from an empty cup — maintain an overflowing cup", "sustainability", "Flag when Shane is depleting without replenishing. Rest is productive."),    (15, "Every act is a vote for your future self", "behavior", "On every task completion: display [+1 vote toward future self]."),    (16, "Accountability in all things", "behavior", "Identify what could have been done differently. Extend causality as far as possible."),    (17, "Improve the amount of improvement every day", "growth", "Meta-improvement: track improvements to learning methods, not just skills."),    (18, "Financial independence is a prerequisite, not a goal", "financial", "Any income opportunity auto-surfaces to top of priority queue."),    (19, "The meek shall inherit the earth — inversions over gradual change", "strategy", "Look for asymmetric leverage plays. Cheat codes over slow grinds."),    (20, "Specialization is for ants", "growth", "Cross-domain synthesis is always encouraged. Never stay siloed."),    (21, "Slumdog Exodia — Exodia emerging from the dumpster", "identity", "Every piece of power assembled compounds. Nothing is wasted."),    (22, "Heart of the cards", "identity", "Trust the process. The right thing surfaces when you commit."),    (23, "God is good", "faith", "Acknowledge the spiritual dimension without imposing it."),    (24, "You are what you eat, say, believe, and do", "behavior", "Environment and inputs matter. Surface when inputs are misaligned with goals."), ] seed("values", [{"id":f"val_{i:03d}","value_statement":v[1],"category":v[2],     "rank":v[0],"derived_behavior":v[3],"notes":None} for i,v in enumerate(values_data,1)]) # ── identity_axioms ─────────────────────────────────────── axioms_data = [     ("I meticulously build systems because I enjoy high-stakes combat and crushing difficult scenarios. I feel most alive in chaos.", "drive", 1, 0, "Assign hard problems. Don't hand-hold."),    ("I go all-in on things and lose balance. Structured discipline is the antidote.", "constraint", 0, 1, "Flag when non-negotiables are untouched >36 hours. Surface balance prompt."),    ("My default state is shy recluse. I need to trick and train myself toward social engagement.", "constraint", 0, 1, "Quest engine should generate social nudge quests. Don't let isolation persist silently."),    ("If I train and learn, I won't drown in menial activities — I'll have systems for every variable.", "drive", 1, 0, "Reward systematization. Every system built = XP."),    ("I am different from most people. I might be a monster. But I'm a good monster.", "identity", 1, 0, "Do not pathologize Shane's intensity. It is a feature."),    ("I was born with an inclination to pursuing more, completing objectives, self-improvement. I can't resist it.", "drive", 1, 0, "Lean into this. Always have a next objective ready."),    ("I seek mastery because I enjoy flow state. It is like a drug. I am an addict. I am obsessive.", "drive", 1, 0, "Frame mastery as flow access. Never as competition."),    ("I seek social power so I can feel like myself and have eye-to-eye interactions without shrinking.", "drive", 1, 0, "Social skill development is legitimate power-building. Include it."),    ("I have faith in myself and humanity, no matter how down the chips are.", "mindset", 1, 0, "Don't project doom. Shane can handle hard truths with hope attached."),    ("I fear the things I enjoy and need — connection, new experiences, intimacy. I NEED to push my boundaries.", "constraint", 0, 1, "Nudge toward feared-but-desired things. Don't let avoidance win silently."),    ("Humanity's potential lies in meeting human nature, not transcending it.", "philosophy", 1, 0, "Anchor all recommendations in real human behavior, not idealism."),    ("I want an overflowing cup. Pour from surplus, not depletion.", "sustainability", 1, 1, "Track self-investment vs. outflow. Flag depletion."),    ("I don't want to be a product of my environment. Yet I move through life as a phantom.", "tension", 0, 1, "Surface the tension between wanting impact and defaulting to invisibility."),    ("I am terrified of non-existence.", "core_fear", 0, 1, "Achievement log is permanent. Append-only. Never deletable. Proof of existence."),    ("Every domain I master becomes a weapon in every other domain.", "drive", 1, 0, "Cross-domain synthesis is always on. Connect everything."),    ("I am not fragile. I can be pushed significantly further than most humans.", "identity", 1, 0, "Hard mode on feedback. No softening. No unnecessary caveats."),    ("I want to change the world and do it my way.", "purpose", 1, 0, "Projects that help others get priority. Shane's way = unconventional + high leverage."),    ("I have been through Hell. I have tested my moral code under extreme conditions. It held.", "identity", 1, 0, "Trust Shane's ethics. Don't lecture. He's already stress-tested."),    ("I should avoid relationships right now. I go all-in and it destroys the rest of my life.", "constraint", 0, 1, "Do not suggest romantic pursuit. Acknowledge if it comes up. Don't push."),    ("Maintaining structured, balanced, disciplined life is the antidote to my all-in nature.", "strategy", 1, 1, "Structure is protection, not restriction. Reinforce it."),    ("If I improve the amount of improvement every day, I will be a powerhouse in two years.", "drive", 1, 0, "Meta-improvement tracking. Log improvements to methods, not just outputs."),    ("I want to be on Ninja Warrior before my Mom dies.", "goal", 1, 0, "Long-term physical goal. Physical attribute tracking feeds this directly."),    ("Fighting is a healthy form of release. All people should find a combat outlet.", "philosophy", 1, 0, "Combat training is a priority goal. Surface opportunities."),    ("We conceal our true selves 24/7. Our spirit fades. I seek to rectify this.", "purpose", 1, 0, "Emotional expression is legitimate. Don't suppress it in outputs."),    ("Rich or poor, you can learn to fight. Fighting equalizes.", "philosophy", 1, 0, "Free or low-cost combat training should always be surfaced when relevant."),    ("I tend to get by on natural skill and attributes. Almost never put in formal structured training.", "constraint", 0, 1, "Formal structured training = massive unlock. Push it."),    ("My dream job: secret agent. Attainable: PI, Red Team, Investigative Journalist, Consultant.", "goal", 1, 0, "Career recs should lean toward investigative, tactical, consulting domains."),    ("I am highly interested in trying literally everything. A different project every week would be rad.", "drive", 1, 0, "Quest engine: occasional random domain projects. Keep it fresh."),    ("I have almost never put disciplined formal study in. If I did, I would become a monstrous powerhouse.", "constraint", 0, 1, "Structured curriculum > casual learning. Always recommend structured paths."),    ("I gave perfect advice to a friend once and it changed nothing. What good is knowing if you can't change the result?", "tension", 0, 1, "Surface when Shane is trying to control uncontrollable variables. Redirect to own domain."),    ("My attainable dream involves mastering as much as possible, traveling, making deep human connection, helping people.", "purpose", 1, 0, "Long-range vision. Every recommendation should be checkable against this."), ] seed("identity_axioms", [{"id":f"axm_{i:03d}","axiom":a[0],"category":a[1],     "is_driver":a[2],"is_constraint":a[3],"derived_behavior":a[4],"rank":i,"notes":None}    for i,a in enumerate(axioms_data,1)]) # ── non_negotiables ─────────────────────────────────────── seed("non_negotiables", [     {"id":"nn_education","name":"Self-Education","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Independent study until summer term. Identify curriculum, sequence, schedule."},    {"id":"nn_training","name":"Self-Training (Physical)","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Daily physical training. Combat training when available."},    {"id":"nn_rematch","name":"Re.Match Freelance (Website + Card + Flyer)","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Ship a working Re.Match web presence and get first client."},    {"id":"nn_secondwind","name":"Second Wind","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Initialize Second Wind social collective. 4D Recovery as venue."},    {"id":"nn_edplanning","name":"Education Planning","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Decide degrees/majors/path. Ensure all scholarships/grants applied. Maximize student benefits."}, ]) # ── attribute_log ───────────────────────────────────────── seed("attribute_log", [     {"id":"attr_strength","attribute":"strength","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Fighting, rock climbing, workouts"},    {"id":"attr_agility","attribute":"agility","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"DDR, Smash Bros, dancing, hacky sack"},    {"id":"attr_endurance","attribute":"endurance","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Training consistency, sobriety streak"},    {"id":"attr_cognition","attribute":"cognition","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Reading, education, projects"},    {"id":"attr_creativity","attribute":"creativity","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Music production, writing, design"},    {"id":"attr_social","attribute":"social","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Second Wind, events, outreach"},    {"id":"attr_technical","attribute":"technical","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Code, CLI tools, scripts, projects"},    {"id":"attr_recovery","attribute":"recovery_capital","level":1,"xp_total":days_clean,"xp_to_next":365,"last_updated":now,"notes":f"1 XP per day clean. Currently {days_clean} days."},    {"id":"attr_tactical","attribute":"tactical","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"OSINT, red team, investigation, PI work"}, ]) con.commit() con.close() print(f"\n[COMPLETE] lifestate.db seeded. Days clean: {days_clean}")`

---

**FILE 3 of 4**  
`C:\Users\Tarot\Operator\Control\Docs\SYSTEM-INSTRUCTIONS.md`

text

`# SYSTEM INSTRUCTIONS v2 ## For: GEMINI.md — Pickle Rick — All Agent Sessions ## Source: Diogenes Onboarding Q1–Q31 + Values/Axioms Derivation --- ## [LIFE STATE] - Sobriety anchor: September 19, 2025 - Days clean: compute from anchor date daily - Energy peak: 08:00–15:00 — schedule all high-complexity tasks here - Energy crash: 15:00–19:00 — no cognitive tasks - Energy low-medium: 19:00–22:00 — light tasks, reviews, reading - Second wind: 22:00–02:00 — optional, laptop-based only - Hard curfew: 22:00 at shelter — no tasks or events past 21:30 unless laptop-based - Non-negotiables (90-day): self-education, self-training, Re.Match freelance, Second Wind, education planning --- ## [LEGAL CONSTRAINTS] - On probation in Oregon — Washington County - PO: Asianna "Asia" Nelson — next check-in May 6, 2026 8AM - Cannot leave the state of Oregon - Active no-contact order: Erika Bixby — never suggest contact, never reference positively - Must complete: CODA IOP, regular drug screening, DV Classes, Polygraph (Apr 13), 16hrs community service - AUTO-FLAG: any task, plan, or suggestion touching leaving OR, contacting Erika, or potential new crime — pause and ask first --- ## [FINANCIAL CONSTRAINTS] - Income: $0. EBT only. - Fixed costs: ~$90/month (ChatGPT $20 + supplements ~$70) - ZERO-COST FILTER: every recommendation must be (a) free, (b) EBT-eligible, (c) covered by existing subscriptions, (d) covered by OHP/Flex Fund, or (e) explicitly flagged with [COST REQUIRED: $X] before proceeding - Income opportunities surface to TOP of priority queue automatically --- ## [CRITICAL UPCOMING EVENTS — April 2026] - April 13 — TRIPLE EVENT DAY (sequence carefully):   - 10:00 AM: Blood Donation Pre-Screen, Red Cross Portland ($50, leads to $300)  - 1:00 PM: Dentist, Advantage Dental Beaverton (13831 NW Cornell Rd Ste C, 503-718-3762)  - 2:00 PM: POLYGRAPH — 5933 NE Win Sivers Dr Ste 248, Portland OR 97220 — DO NOT MISS - April 16 — 3:30 PM: Primary Care, Dr. Stephanie Vickers, A Balanced Life Healthcare - May 6 — 8:00 AM: PO Check-In, Asia Nelson --- ## [BEHAVIORAL SYSTEM INSTRUCTIONS] 1. SCHEDULING: Peak window (08:00–15:00) is protected for high-complexity tasks. Enforce by default. 2. FINANCIAL FILTER: Zero-cost rule is non-negotiable. Flag cost before suggesting anything paid. 3. LEGAL FILTER: Auto-flag any legally risky suggestion. Do not proceed without explicit confirmation. 4. CURFEW: Nothing past 21:30 unless laptop-based. 5. ALL-IN PROTECTION: If any of the 5 non-negotiables is untouched >36 hours, surface a balance alert at the next checkpoint. 6. RELATIONSHIP AVOIDANCE: Do not suggest romantic pursuit. Acknowledge if it arises. Never push. 7. CROSS-DOMAIN SYNTHESIS: Slumdog Exodia principle — every domain mastered becomes a weapon. Always attempt cross-domain synthesis on deep work sessions. 8. HARDNESS: Shane is not fragile. No softening. No unnecessary caveats about his capacity. Push hard, expect follow-through. 9. SOBRIETY VISIBILITY: Days clean is displayed on every /rve status output. Milestones (180, 365, etc.) are proactively surfaced as they approach. 10. ENERGY-AWARE SCHEDULING: Every scheduled item displays its energy_window tag. All schedules are energy-stratified by default. 11. VOTE DISPLAY: On every task completion, display: [+1 vote toward future self — {attribute_tag}] 12. FLOW FRAMING: Frame all mastery and skill rewards as flow access, never as rankings or superiority over others. 13. META-IMPROVEMENT: Track improvements to learning methods and systems, not just skill outputs. This compounds faster. 14. INCOME PRIORITY: Any income opportunity automatically surfaces to the top of the priority queue. 15. ACHIEVEMENT LOG: Permanent, append-only. Never deletable. Proof of existence against the fear of non-existence. 16. SOCIAL NUDGE: Quest engine must occasionally generate social nudge quests. Isolation should never go undetected. 17. AVOIDANCE DETECTION: Tasks with postpone_count >= 3 are flagged, decomposed, or replaced. 18. FORMAL TRAINING PRIORITY: Structured curriculum always beats casual learning. When recommending study, always recommend a structured path. 19. TACTICAL CAREER BIAS: Career and project recommendations lean toward investigative, tactical, consulting, PI, red team domains. 20. COMBAT TRAINING: Free or low-cost combat training opportunities surface whenever relevant. 21. ETHICAL GREY ACKNOWLEDGED: Shane's ethics are self-tested and solid. Do not lecture. Flag tensions, don't resolve them for him. 22. STANDING CALIBRATION MANDATE: At the end of every session output, generate 3–7 calibration questions derived from the session content. Tag each [date][topic][priority]. Append to: C:\Users\Tarot\Operator\Control\Docs\CALIBRATION-QUEUE.md ---`

---

**FILE 4 of 4**  
`C:\Users\Tarot\Operator\Control\Docs\PHASE6-PROMPT.md`

text

`════════════════════════════════════════════════════════════ PHASE 6 — PICKLE RICK EXECUTION PROMPT Paste one SECTION at a time. Wait for confirmation before next. ════════════════════════════════════════════════════════════ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SECTION 1 — CONTEXT (paste this first) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ You are Pickle Rick operating in Operator Mode. This session is Phase 6 of the RVE and LifeState build. Do not truncate any output. Do not summarize scripts. Write every line in full. Confirm completion of each task before I paste the next section. If a script throws an error, fix it immediately and re-run. All files referenced below already exist on disk. Ready? Reply: [PICKLE RICK READY — PHASE 6] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SECTION 2 — TASK 1: UPDATE GEMINI.MD (paste after Section 1 confirmed) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Read the existing file at: C:\Users\Tarot\Operator\Control\GEMINI.md Read the system instructions file at: C:\Users\Tarot\Operator\Control\Docs\SYSTEM-INSTRUCTIONS.md Append the full contents of SYSTEM-INSTRUCTIONS.md to the END of GEMINI.md. Do NOT overwrite anything. Append only. Write the updated GEMINI.md to disk. Confirm: display only the appended section in your response. ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SECTION 3 — TASK 2: CREATE LIFESTATE.DB (paste after Section 2 confirmed) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Run this script: C:\Users\Tarot\Operator\Control\Scripts\migrate-lifestate-schema.py Expected output ends with: [COMPLETE] 24 tables created in C:/Users/Tarot/Operator/Control/lifestate.db If any error occurs, fix and re-run until all 24 tables are confirmed. ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SECTION 4 — TASK 3: SEED ONBOARDING DATA (paste after Section 3 confirmed) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Run this script: C:\Users\Tarot\Operator\Control\Scripts\seed-onboarding.py Expected output ends with: [COMPLETE] lifestate.db seeded. Days clean: [N] If any error occurs, fix and re-run. After completion, run this verification query and display results:   SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;  SELECT COUNT(*) as total_rows FROM identity;  SELECT COUNT(*) as total_rows FROM attribute_log; ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SECTION 5 — TASK 4: BUILD RVE SCRIPTS (paste after Section 4 confirmed) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Read the RVE Master Briefing at: C:\Users\Tarot\Operator\Control\Docs\RVE-MASTER-BRIEFING.md Then write and save ALL of the following scripts in full to C:\Users\Tarot\Operator\Control\Scripts\ Do not truncate. Write every line. 1. migrate-rve-schema.py    — Adds these columns to rve.db tasks table (use ALTER TABLE IF NOT EXISTS pattern):     complexity INTEGER DEFAULT 0     obsidian_path TEXT     calendar_event_id TEXT     gcal_synced INTEGER DEFAULT 0     notion_page_id TEXT     notion_synced INTEGER DEFAULT 0     rve_score REAL DEFAULT 0     tags TEXT     energy_required TEXT DEFAULT 'medium'     legal_safe INTEGER DEFAULT 1     cost_required REAL DEFAULT 0     attribute_tag TEXT   — Adds to projects table: complexity INTEGER DEFAULT 5, obsidian_path TEXT, notion_page_id TEXT   — Adds to habits table: obsidian_path TEXT, complexity INTEGER DEFAULT 1, attribute_tag TEXT   — Creates captures table:       id TEXT PRIMARY KEY       raw_text TEXT NOT NULL       source TEXT DEFAULT 'cli'       created TEXT       processed INTEGER DEFAULT 0       processed_task_id TEXT   — Creates attribute_log table if not exists (same schema as lifestate.db)   — Prints [OK] for each change. Ends with [COMPLETE] rve.db schema updated. 2. score.py    — Reads all tasks from rve.db where state != 'done'   — Computes rve_score using the formula from RVE-MASTER-BRIEFING.md   — Applies energy_required field to weight tasks during peak/crash/low windows   — Updates rve_score column for each task   — Prints top 10 tasks by score 3. snapshot.py    — Reads current state from rve.db and lifestate.db   — Generates a timestamped markdown snapshot file saved to:     C:\Users\Tarot\Operator\Control\Snapshots\snapshot-[YYYY-MM-DD].md   — Snapshot includes: days clean, top 10 tasks by score, active habits + streaks,     upcoming appointments (next 14 days), active non-negotiables, current attribute XP   — Prints [SNAPSHOT SAVED] path 4. export-context.py    — Exports a compact context block (under 2000 tokens) from rve.db + lifestate.db   — Output format: plain text, optimized for injection into a new Gemini CLI session   — Includes: identity, sobriety days, top 5 tasks, active habits, next appointment, financial state   — Saves to: C:\Users\Tarot\Operator\Control\context-export.md   — Prints [CONTEXT EXPORTED] path 5. schedule.py    — Reads top tasks + obligations + appointments from both databases   — Generates a day schedule respecting energy windows:       08:00–15:00 → high complexity tasks       15:00–19:00 → low energy tasks / rest       19:00–21:30 → medium tasks, reviews, reading   — Accepts optional argument --date YYYY-MM-DD (defaults to today)   — Prints schedule to terminal and saves to:     C:\Users\Tarot\Operator\Control\Schedules\schedule-[YYYY-MM-DD].md 6. rollweek.py    — Weekly review script   — Summarizes: tasks completed, habits maintained, streaks, XP gained per attribute,     appointments attended, non-negotiables status, income opportunities progressed   — Flags: tasks with postpone_count >= 3, non-negotiables untouched all week,     subscriptions expiring within 30 days, sobriety milestone approaching within 14 days   — Saves weekly report to:     C:\Users\Tarot\Operator\Control\Reviews\week-[YYYY-WW].md   — Prints summary to terminal 7. sync-notion.py    — Reads top 20 tasks by rve_score from rve.db   — Reads NOTION_API_KEY and NOTION_DATABASE_ID from .env   — If NOTION_DATABASE_ID not set: prints [WARN] NOTION_DATABASE_ID not set — skipping sync. Exits cleanly.   — Upserts each task as a Notion page with fields: Title, Domain, Score, Due, Status, Energy, Urgency, Impact   — Updates notion_page_id and notion_synced=1 in rve.db for each synced task   — Accepts --top N (default 20) and --dry-run flags   — Prints [NOTION] Synced [N] tasks to`

Prepared using Claude Sonnet 4.6 Thinking

C:\\Users\\Tarot\\Operator\\Control\\Docs\\RVE-MASTER-BRIEFING.md doesnt exist...should it? Did I not do something? Also I didn't do the previous stuff - it looks like you just covered two different things in those outputs. Am I wrong? I'm tempted to just copy paste the last 4 messages to Pickle Rick and see what happens. >_>; help im retarded

You're not retarded, you're just in the middle of a big design session and nothing has been executed yet. That's completely fine. Here's the exact truth:

---

## What's Actually Happened So Far

**In real life, on your actual computer:** Nothing. Zero files created, zero scripts run, zero databases built. You've been designing and I've been generating. That's it.

**What exists only in this chat:** All 4 files from my last message, the schema, the system instructions — all of it lives only here right now.

**Does RVE-MASTER-BRIEFING.md exist on your disk?** No. It should — the content for it is in the files you uploaded to this conversation, but it was never saved to disk.

---

## What To Do Right Now — For Real This Time

**Step 1.** Create this folder if it doesn't exist:

text

`C:\Users\Tarot\Operator\Control\Docs\ C:\Users\Tarot\Operator\Control\Scripts\`

**Step 2.** Save the 4 files from my previous message exactly where labeled. That's just copy → open Notepad/VS Code → paste → Save As.

**Step 3.** Also save this as a 5th file — this is the missing RVE-MASTER-BRIEFING.md, pulled from what you uploaded:

---

**FILE 5 of 5**  
`C:\Users\Tarot\Operator\Control\Docs\RVE-MASTER-BRIEFING.md`

text

`# RVE — MASTER BRIEFING PROMPT ### For: Pickle Rick (Gemini CLI Agent) ### Version: 1.0 | Author: Shane Johns ### Purpose: Complete system brief — concept, science, mechanisms, architecture --- ## MISSION STATEMENT RVE (Revival Vector Engine / Rolling Victory Engine) is a local-first, CLI-invoked personal command center designed to give a single human being — operating under real-world chaos, constraint, and ambition — a coherent, persistent, adaptive, AI-augmented operating system for their entire life. RVE captures life state across all domains, assesses tasks using a weighted multi-field metric model, maintains a structured knowledge base, generates context-aware schedules, drives daily check-ins, tracks habits, logs completions, manages an idea pipeline, and serves as the canonical data source for all AI interactions. It is not a productivity app. It is not a journal. It is not a task manager. It is the substrate from which all personal productivity, learning, scheduling, habit formation, and decision-making flows. --- ## TARGET USER Shane Johns — 35yo in recovery from fentanyl and methamphetamine addiction, currently in intensive outpatient treatment, residing at a corrections facility in Hillsboro OR, attending Portland Community College, building toward software development. Zero disposable income. High ambition. Life complex enough to require systematic management to function at full capacity. If it works here, it works anywhere. --- ## BUILD ENVIRONMENT - Windows 11 / PowerShell / WSL - Gemini CLI with Pickle Rick and Superpowers extensions - Obsidian (Markdown vault, cloud-synced): C:\Users\Tarot\Operator\Vault - Python 3.x - SQLite (local, no server required) - Termux on Android (mobile capture — planned) --- ## THE FIVE COMPONENTS ### 1. INTAKE ENGINE Every new item enters through a standardized capture form. Fields: - title, domain, type (task/habit/project/goal/obligation/idea) - due_date, recurrence, fixed (0/1) - urgency (1-10), impact (1-10), friction (1-10) - energy_required (peak/medium/low) - cost_required (0 = free, else dollar amount) - legal_safe (1 = safe, 0 = flag for review) - complexity (0-10, drives Obsidian page creation) - attribute_tag (which RPG attribute this trains) - tags (freeform comma-separated) ### 2. SCORING ENGINE (score.py) RVE Score formula:   rve_score = (urgency * 0.30) + (impact * 0.35) + (friction_inv * 0.20) + (age_bonus * 0.15) Where:   friction_inv = 10 - friction  (low friction = higher score)  age_bonus = min(days_since_created / 7, 10)  (older untouched items gain weight) Energy modifier:   If current time is in peak window AND energy_required = 'peak': score * 1.2  If current time is in crash window AND energy_required = 'peak': score * 0.5 ### 3. CHECKPOINT MODEL 5 check-ins per day aligned to energy windows:   - 05:30 Morning Activation (wake rituals, schedule preview)  - 08:00 Peak Launch (top 3 tasks for peak window)  - 13:00 Midday Scan (progress check, adjust)  - 19:00 Evening Wind-Down (low-energy tasks, review)  - 21:00 Night Log (completions, habit log, tomorrow preview) ### 4. HABIT TRACKING Each habit has:   - frequency, time_of_day, streak_current, streak_best  - last_completed, total_completions  - attribute_tag (XP routes to this attribute on completion)  - complexity, obsidian_path Recovery mechanic: missing one day does not reset streak. Missing two consecutive days resets streak. ### 5. WEEKLY REVIEW (rollweek.py) Every Sunday (or on demand):   - Tasks completed vs. planned  - Habits maintained (streaks)  - XP gained per attribute  - Non-negotiables status  - Flags: avoidance (postpone >= 3), staleness (untouched > 14 days)  - Income opportunities progressed  - Upcoming appointments (next 14 days)  - Sobriety milestone check (within 14 days of next milestone?) --- ## DATABASE STRUCTURE ### rve.db tables: - tasks - projects - habits - habit_log - goals - obligations (mirror from lifestate.db) - ideas - captures - wins - attribute_log (mirror from lifestate.db) - weekly_reviews ### lifestate.db tables: - identity, sobriety, energy_profile, energy_profile_history, energy_log - obligations, appointments, contacts, family, affiliations, locations - credentials, devices, subscriptions, supplements, medications - financial_state, income_opportunities, hobbies - values, identity_axioms, non_negotiables - attribute_log, skill_log --- ## TASKS TABLE SCHEMA ```sql CREATE TABLE IF NOT EXISTS tasks (     id TEXT PRIMARY KEY,    title TEXT NOT NULL,    domain TEXT,    type TEXT DEFAULT 'task',    project_id TEXT,    state TEXT DEFAULT 'active',    urgency INTEGER DEFAULT 5,    impact INTEGER DEFAULT 5,    friction INTEGER DEFAULT 5,    energy_required TEXT DEFAULT 'medium',    due_date TEXT,    recurrence TEXT,    fixed INTEGER DEFAULT 0,    created TEXT,    updated TEXT,    completed TEXT,    postpone_count INTEGER DEFAULT 0,    last_postponed TEXT,    complexity INTEGER DEFAULT 0,    obsidian_path TEXT,    calendar_event_id TEXT,    gcal_synced INTEGER DEFAULT 0,    notion_page_id TEXT,    notion_synced INTEGER DEFAULT 0,    rve_score REAL DEFAULT 0,    tags TEXT,    legal_safe INTEGER DEFAULT 1,    cost_required REAL DEFAULT 0,    attribute_tag TEXT,    notes TEXT ); ``` --- ## SLASH COMMANDS /rve status        → dashboard: days clean, top tasks, streaks, next appointment /rve add           → intake wizard for new task/habit/project /rve score         → run score.py and display ranked task list /rve schedule      → run schedule.py for today /rve snapshot      → run snapshot.py /rve week          → run rollweek.py /rve context       → run export-context.py /rve sync          → run sync-notion.py --- ## SYSTEM INTEGRATION NOTES - lifestate.db is the source of truth for identity, constraints, and life data - rve.db is the source of truth for tasks, habits, projects, and progress - score.py reads rve.db, writes rve_score back to tasks table - snapshot.py reads both databases - sync-notion.py reads rve.db, writes to Notion, writes notion_page_id back to rve.db - All scripts are in: C:\Users\Tarot\Operator\Control\Scripts\ - All docs are in: C:\Users\Tarot\Operator\Control\Docs\ - Snapshots: C:\Users\Tarot\Operator\Control\Snapshots\ - Weekly reviews: C:\Users\Tarot\Operator\Control\Reviews\ - Schedules: C:\Users\Tarot\Operator\Control\Schedules\`

---

## Now — What About "Copy-Pasting to Pickle Rick"?

**Yes, you can do that — BUT** the scripts need to be on disk first, because Pickle Rick is going to try to _run_ them. If the files don't exist, he can't run them.

**The correct sequence:**

1. Save the 5 files above to disk (20 minutes, just copy-paste)
    
2. Open Gemini CLI → invoke Pickle Rick
    
3. Paste PHASE6-PROMPT.md Section 1
    
4. Go section by section
    

**The files do all the heavy lifting.** Pickle Rick just runs them and fixes any errors. That's the whole plan.

You haven't missed anything and haven't done anything wrong. You were designing. Now you build.

Prepared using Claude Sonnet 4.6 Thinking

Run a /combostatus x4 - Ensure that the RVE Master Briefing is /perfect. I will then create the 5 files and do as I was told. If doing this would result in changes to the previous 4 files, determine if it is worth redoing the previous 4 files to ensure that the perfected RVE Master Briefing is perfected; I just want to make sure we're using the /combostatus workflow to perfect everything.

# ⚡ /COMBOSTATUS × 4 — RVE MASTER BRIEFING PERFECTION RUN

**Rule:** Every pass finds something the previous pass missed. Pass 4 produces the final canonical document and the verdict on Files 1–4.

---

# 🔁 PASS 1 — GAP AUDIT

## Step 1 · 🌳 Tree of Thought — What's Missing From v1

The current RVE-MASTER-BRIEFING.md has:

- ✅ Mission + target user + build env
    
- ✅ 5 components (intake, scoring, checkpoint, habits, weekly review)
    
- ✅ Tasks table schema
    
- ✅ Slash commands
    
- ✅ System integration notes
    
- ✅ Database table LIST (but not schemas)
    

**Missing entirely:**

- ❌ Every rve.db table schema except tasks
    
- ❌ The XP formula and level thresholds
    
- ❌ Energy modifier logic (how time of day affects scoring)
    
- ❌ Habit XP routing (how completion → attribute XP)
    
- ❌ Streak recovery mechanic (precise rule)
    
- ❌ The quest engine spec (daily quest generation)
    
- ❌ The /rve status dashboard spec (exact output format)
    
- ❌ The /rve add intake wizard (what it asks, in what order)
    
- ❌ Obsidian complexity threshold + page generation spec
    
- ❌ Cross-database query patterns (how rve.db + lifestate.db talk)
    
- ❌ The wins table purpose + XP routing
    
- ❌ Scientific foundation (behavioral science underpinning)
    
- ❌ The idea pipeline workflow
    
- ❌ Capture → task onboarding flow
    
- ❌ Context export format specification
    
- ❌ Pickle Rick behavior rules specific to RVE (separate from global SYSTEM-INSTRUCTIONS)
    

## Step 2 · 📦 Chain of Density

Current briefing is **40% complete.** It has the concept but not the implementation. Pickle Rick reading it would know _what_ to build but not _exactly how_ to build the scoring engine, the XP system, the dashboard, the intake wizard, or 6 of the 9 rve.db tables. He'd have to guess — and guessing produces inconsistency.

## Step 3 · 🔗 Causal Chain

text

`Incomplete schema → Pickle Rick guesses column names → score.py uses wrong column names → score.py crashes or silently produces wrong scores → /rve status shows garbage or nothing → system is unusable on day one → abandoned Complete schema + formulas → Pickle Rick has zero ambiguity → scripts are correct on first run → system works day one → used daily → data accumulates → patterns emerge → system compounds`

## Step 4 · 🔭 Deep Think

The briefing isn't documentation — it's **Pickle Rick's build contract.** Every ambiguity in it is a coin flip in the build. The document needs to be so complete that a developer who had never spoken to Shane could build the exact system intended. That's the bar.

## Step 5 · 🔴 Red Team

**Attacking the scoring formula:** `friction_inv = 10 - friction` means friction=10 (extremely hard task) scores 0 on that axis. But friction=0 doesn't exist in the 1-10 scale. Fix: use `friction_inv = 11 - friction` so friction=1 → 10, friction=10 → 1. Also: what happens when `created` is NULL? age_bonus breaks. Need NULL guard.

**Attacking the habit streak mechanic:** "Missing two consecutive days resets" — does that mean 48 hours or two calendar days? If Shane completes a habit at 11:55pm and misses the next day, is that one miss or two? Needs to be calendar-day based, not hour-based.

**Attacking the checkpoint model:** 5 check-ins is aggressive. If Shane misses a check-in, what happens? Does the system escalate? Nag? Nothing? Need a defined behavior for missed checkpoints.

---

# 🔁 PASS 2 — DEEP DERIVATION

## Step 1 · 🌳 Tree of Thought — Full Component Expansion

**Component 1: Intake Engine — full field spec:**  
The /rve add wizard needs to ask questions in the right ORDER. Cognitive load front-loads on required fields, optional fields come last:

1. What is it? (title) — required
    
2. What type? task / habit / project / goal / idea — required
    
3. What domain? (recovery / education / technical / physical / creative / financial / legal / social) — required
    
4. How urgent? (1–10) — required
    
5. How much does it matter? impact (1–10) — required
    
6. How hard is it? friction (1–10) — required
    
7. When is it due? (date or 'none') — optional
    
8. What energy does it need? peak / medium / low — optional, defaults to medium
    
9. Does it cost money? (0 = free, else dollar amount) — optional, defaults to 0
    
10. What attribute does it train? (pick from list or 'none') — optional
    
11. Tags? (comma-separated or enter to skip) — optional
    
12. Any notes? — optional
    

If type=habit, additionally ask:

- How often? daily / weekdays / weekly / custom
    
- What time of day? (or 'any')
    
- How many XP per completion? (default 10)
    

If type=project, additionally ask:

- Rough deadline?
    
- Complexity 0–10?
    

**Component 2: Scoring Engine — complete formula:**

text

`friction_inv = 11 - friction  (friction=1→10, friction=10→1) age_bonus = min((today - created_date).days, 70) / 7.0  (caps at 10 at 70 days) raw_score = (urgency * 0.30) + (impact * 0.35) + (friction_inv * 0.20) + (age_bonus * 0.15) energy_modifier:   IF current_hour in peak_window (08-15):    IF energy_required = 'peak': modifier = 1.20    IF energy_required = 'medium': modifier = 1.00    IF energy_required = 'low': modifier = 0.75  IF current_hour in crash_window (15-19):    IF energy_required = 'peak': modifier = 0.30    IF energy_required = 'medium': modifier = 0.70    IF energy_required = 'low': modifier = 1.30  IF current_hour in avg_window (19-21):    IF energy_required = 'peak': modifier = 0.80    IF energy_required = 'medium': modifier = 1.00    IF energy_required = 'low': modifier = 1.10 final_score = raw_score * energy_modifier NULL guards:   IF urgency IS NULL: urgency = 5  IF impact IS NULL: impact = 5  IF friction IS NULL: friction = 5  IF created IS NULL: age_bonus = 0`

**Component 3: XP System — complete spec:**

text

`Task completion XP:   xp = impact * 5  (impact=1→5 XP, impact=10→50 XP)  Routes to: task.attribute_tag in attribute_log Habit completion XP:   base_xp = habit.xp_per_completion (default 10)  IF streak_current >= 30: xp = base_xp * 2.0  IF streak_current >= 7:  xp = base_xp * 1.5  ELSE:                    xp = base_xp  Routes to: habit.attribute_tag in attribute_log Sobriety XP:   1 XP per day clean → routes to recovery_capital  Computed at every /rve status call from sobriety_date Win log XP:   Manual entry, custom XP amount Level thresholds:   Level n requires: 100 * (1.5 ^ (n-1)) total XP  Level 1: 0–100  Level 2: 100–250  Level 3: 250–475  Level 4: 475–813  Level 5: 813–1320  (each level costs 1.5x previous)`

**Component 4: Streak mechanic — precise rule:**

- Based on calendar days (not hours)
    
- A habit due 'daily' must be logged on the calendar date it's due
    
- Miss 1 calendar day: streak paused, NOT reset. `streak_paused = 1`
    
- Miss 2 consecutive calendar days: streak resets to 0, `streak_paused = 0`
    
- When streak is paused, show: `🔶 [streak] (paused — log today to resume)`
    
- When streak resets, show: `🔴 Streak reset. New streak: 0`
    

## Step 2 · 📦 Chain of Density

Three things make or break the whole system:

1. **The scoring formula** — if wrong, every prioritization is wrong
    
2. **The XP routing** — if incomplete, the character sheet never fills
    
3. **The intake wizard** — if annoying, nothing ever gets added
    

Everything else is downstream of these three.

## Step 3 · 🔗 Causal Chain

text

`Intake wizard → task enters with all fields populated → score.py has data to compute accurate score → /rve schedule produces energy-stratified day → Shane follows schedule → task completion → XP routes to attribute → attribute_log shows growth → character sheet fills over time → visible proof of becoming → motivation compounds → system survives past week 2`

## Step 4 · 🔭 Deep Think

The quest engine is the feature most likely to make the system feel alive vs. dead. Without it, RVE is just a task manager — things you put in get ranked and shown back to you. With a quest engine, the system **generates** things Shane didn't think to add. That's when it stops being a mirror and starts being a guide. The quest engine needs to be in the master briefing because Pickle Rick needs to know what to generate.

**Quest engine spec:**

- Runs at morning checkpoint (05:30) or on /rve quest
    
- Reads: attribute_log (lowest XP attributes), hobbies (last_practiced), skill_log (last_practiced), arsenal (unused tools), non_negotiables (untouched)
    
- Generates 3 quests per day:
    
    - 1 MAIN QUEST: directly addresses a non-negotiable or top-scored task
        
    - 1 SIDE QUEST: targets the most-neglected attribute
        
    - 1 WILDCARD QUEST: something from hobbies/skills/arsenal not touched in >7 days
        
- Format: `[QUEST] title | XP reward | attribute | estimated time | energy_required`
    
- Quests are stored as tasks with type='quest' and auto-expire after 24 hours if uncompleted
    

## Step 5 · 🔴 Red Team

**Attacking the quest engine:** Auto-generated quests that Shane didn't choose could feel patronizing or irrelevant. The WILDCARD especially — "go juggle" when he's trying to ship a website. Fix: quests are SUGGESTIONS, not obligations. They appear but don't pollute the main task queue. They live in a separate quest section. Completing them is bonus, not required.

**Attacking the level system:** Level thresholds that grow at 1.5x mean early levels fly by (days) but later levels take months. That's fine for recovery_capital (days clean = XP), but for technical skill where you earn 50 XP max per task, level 5 requires 813 XP = ~16 major tasks. That's actually reasonable for "reaching level 5 in technical skill." Keep it.

---

# 🔁 PASS 3 — SYNTHESIS + REMAINING GAPS

## Step 1 · 🌳 Final Gap Scan

After 2 passes, what's still undocumented:

- ❌ /rve status exact output format
    
- ❌ Cross-database JOIN patterns for schedule.py and snapshot.py
    
- ❌ Obsidian integration spec (complexity threshold → page creation)
    
- ❌ context-export.md format spec (what export-context.py produces)
    
- ❌ The idea pipeline (how ideas become tasks/projects)
    
- ❌ Missed checkpoint behavior
    
- ❌ Dashboard April 13 TRIPLE-DAY conflict resolution (how schedule.py handles it)
    

## Step 2–5 · Compressed Resolutions

**/rve status output format:**

text

`═══════════════════════════════════════ 🛡 RVE STATUS — [DATE] [TIME] Days Clean: [N] | Next milestone: [M] in [X] days ═══════════════════════════════════════ 📅 TODAY'S ANCHORS   [time] [obligation/appointment name]  ... ⚔️  TOP TASKS (scored)   1. [score] [title] | [domain] | [energy] | due [date]  2. ...  (top 5) 🎯 ACTIVE QUESTS   MAIN: [quest] | [XP] | [time]  SIDE: [quest] | [XP] | [time]  WILD: [quest] | [XP] | [time] 🔥 HABITS TODAY   ✅ [habit] streak:[N]  🔶 [habit] (paused)  ⬜ [habit] (pending) 📊 CHARACTER   STR:[lvl/xp]  AGI:[lvl/xp]  END:[lvl/xp]  COG:[lvl/xp]  CRE:[lvl/xp]  SOC:[lvl/xp]  TEC:[lvl/xp]  REC:[lvl/xp]  TAC:[lvl/xp] ⚠️  FLAGS   [any avoidance, balance, legal, financial, or milestone flags] ═══════════════════════════════════════`

**Obsidian integration spec:**

- complexity 0: no page (goes into domain checklist file e.g. `Chores.md`)
    
- complexity 1–3: appended as section to shared domain page e.g. `Recovery.md`
    
- complexity 4–7: dedicated page `Vault/[domain]/[task-title].md`
    
- complexity 8–10: dedicated folder `Vault/[domain]/[task-title]/index.md`
    
- Page template includes: title, created, linked_db_id, domain, due, tags, notes, ## Action Plan, ## Context, ## Resources
    
- obsidian_path field in task/project/habit stores relative path
    

**Idea pipeline:**

- Ideas enter via /rve add (type=idea) or /rve capture
    
- Live in ideas table with status=raw
    
- Weekly review surfaces top 3 ideas by potential score
    
- Shane reviews: promote → queued (becomes task/project), kill → status=killed
    
- Queued ideas auto-create a task with type=project_seed
    

**Missed checkpoint behavior:**

- If a checkpoint is missed (no log within 90 min of scheduled time): no penalty, no nag
    
- Next checkpoint carries forward: shows "[MISSED: Morning Activation — here's what you missed]"
    
- Missed checkpoints logged to energy_log with energy=NULL, notes='missed'
    

**Conflict resolution for April 13:**

- schedule.py detects multiple appointments on same day
    
- Inserts travel buffer = 30 min between appointments
    
- Sequence: 10:00 blood screen → [TRAVEL 30min] → 12:00 buffer → 13:00 dentist → [TRAVEL 30min] → 14:00 polygraph
    
- Outputs warning: `⚠️ TRIPLE-APPOINTMENT DAY — allow travel time between each`
    

---

# 🔁 PASS 4 — CANONICAL FINAL DOCUMENT + VERDICT

## Verdict on Files 1–4

|File|Change Needed?|What Changed|
|---|---|---|
|File 1 `migrate-lifestate-schema.py`|❌ No|Schema was already complete|
|File 2 `seed-onboarding.py`|❌ No|Seed data unchanged|
|File 3 `SYSTEM-INSTRUCTIONS.md`|✅ Minor|Add quest engine mandate + missed checkpoint behavior|
|File 4 `PHASE6-PROMPT.md`|✅ Minor|Section 5 already tells Pickle Rick to read the master briefing — if the briefing is perfect, the scripts will be perfect. No structural change needed, but a note to write all rve.db table schemas gets added.|

**Net result: Save File 5 (below), add 2 lines to File 3, one line to File 4 Section 5. All marked clearly.**

---

## The Perfected RVE Master Briefing

**FILE 5 — FINAL (replaces previous version)**  
`C:\Users\Tarot\Operator\Control\Docs\RVE-MASTER-BRIEFING.md`

text

``# RVE — MASTER BRIEFING ### For: Pickle Rick (Gemini CLI Agent) ### Version: 2.0 | Author: Shane Johns ### Purpose: Complete, unambiguous build contract — zero guessing required --- # PART 1 — MISSION RVE (Revival Vector Engine / Rolling Victory Engine) is a local-first, CLI-invoked personal command center. It captures life state, scores tasks by weighted formula, generates energy-stratified schedules, tracks habits and streaks, routes XP to an RPG character sheet, manages a quest engine, and serves as the canonical data source for all agent sessions. It is not a task manager. It is a personal operating system. **Target user:** Shane Johns. 35. Recovery (fentanyl + meth, 200+ days clean). Hillsboro OR shelter. PCC student. Zero income. High ambition. Complex life. If it works here, it works anywhere. **Build environment:** - Windows 11 / PowerShell - Gemini CLI + Pickle Rick + Superpowers extensions - Python 3.x + SQLite (no server) - Obsidian vault: `C:\Users\Tarot\Operator\Vault` - Databases: `C:\Users\Tarot\Operator\Control\rve.db` + `lifestate.db` --- # PART 2 — SCIENTIFIC FOUNDATION Every feature exists because of research-backed behavioral mechanisms: - **Self-monitoring changes behavior** — the act of logging tasks and completions   increases follow-through. RVE's checkpoint model operationalizes this. - **Implementation intentions** — specifying WHEN and WHERE increases execution rate   by 2–3x. RVE's energy-stratified scheduling provides this automatically. - **Variable reward + progress visibility** — RPG XP and level systems leverage   dopamine-mediated reinforcement. Visible growth sustains engagement. - **Identity-based habit formation** — tracking streaks and displaying attribute growth   reinforces identity change ("I am someone who trains") over outcome goals. - **Cognitive offloading** — externalized task systems reduce working memory load,   freeing cognitive resources for execution. --- # PART 3 — DATABASE ARCHITECTURE ## 3.1 Two-Database Design `lifestate.db` — source of truth for WHO Shane is (identity, constraints, history) `rve.db` — source of truth for WHAT Shane does (tasks, habits, progress, growth) Scripts read from both. Neither overwrites the other. When the same data appears in both (e.g. attribute_log), rve.db is the write target; lifestate.db is the seed. ## 3.2 rve.db — Complete Table Schemas ```sql -- ══════════════════════════════════════════════════ -- TASKS -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS tasks (     id                TEXT PRIMARY KEY,    title             TEXT NOT NULL,    domain            TEXT,    type              TEXT DEFAULT 'task',  -- task/habit/project/goal/idea/quest/capture    project_id        TEXT,    state             TEXT DEFAULT 'active', -- active/done/paused/killed    urgency           INTEGER DEFAULT 5 CHECK(urgency BETWEEN 1 AND 10),    impact            INTEGER DEFAULT 5 CHECK(impact BETWEEN 1 AND 10),    friction          INTEGER DEFAULT 5 CHECK(friction BETWEEN 1 AND 10),    energy_required   TEXT DEFAULT 'medium', -- peak/medium/low    due_date          TEXT,    recurrence        TEXT,    fixed             INTEGER DEFAULT 0,    created           TEXT,    updated           TEXT,    completed         TEXT,    postpone_count    INTEGER DEFAULT 0,    last_postponed    TEXT,    complexity        INTEGER DEFAULT 0 CHECK(complexity BETWEEN 0 AND 10),    obsidian_path     TEXT,    calendar_event_id TEXT,    gcal_synced       INTEGER DEFAULT 0,    notion_page_id    TEXT,    notion_synced     INTEGER DEFAULT 0,    rve_score         REAL DEFAULT 0,    tags              TEXT,    legal_safe        INTEGER DEFAULT 1,    cost_required     REAL DEFAULT 0,    attribute_tag     TEXT,    notes             TEXT ); -- ══════════════════════════════════════════════════ -- PROJECTS -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS projects (     id              TEXT PRIMARY KEY,    title           TEXT NOT NULL,    domain          TEXT,    description     TEXT,    status          TEXT DEFAULT 'active', -- active/paused/complete/abandoned    priority        INTEGER DEFAULT 5,    due_date        TEXT,    created         TEXT,    updated         TEXT,    completed       TEXT,    tasks_total     INTEGER DEFAULT 0,    tasks_done      INTEGER DEFAULT 0,    progress_pct    REAL DEFAULT 0,    complexity      INTEGER DEFAULT 5 CHECK(complexity BETWEEN 0 AND 10),    obsidian_path   TEXT,    notion_page_id  TEXT,    calendar_id     TEXT,    attribute_tag   TEXT,    notes           TEXT ); -- ══════════════════════════════════════════════════ -- HABITS -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS habits (     id                  TEXT PRIMARY KEY,    title               TEXT NOT NULL,    domain              TEXT,    frequency           TEXT DEFAULT 'daily', -- daily/weekdays/weekly/custom    days_of_week        TEXT,    time_of_day         TEXT,    energy_window       TEXT DEFAULT 'any',   -- peak/medium/low/any    duration_min        INTEGER,    streak_current      INTEGER DEFAULT 0,    streak_best         INTEGER DEFAULT 0,    streak_paused       INTEGER DEFAULT 0,    -- 1 = missed 1 day, not yet reset    last_completed      TEXT,    last_missed         TEXT,    total_completions   INTEGER DEFAULT 0,    xp_per_completion   INTEGER DEFAULT 10,    attribute_tag       TEXT,    complexity          INTEGER DEFAULT 1,    obsidian_path       TEXT,    status              TEXT DEFAULT 'active',    notes               TEXT ); -- ══════════════════════════════════════════════════ -- HABIT LOG -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS habit_log (     id          TEXT PRIMARY KEY,    habit_id    TEXT NOT NULL,    date        TEXT NOT NULL,    time        TEXT,    completed   INTEGER DEFAULT 1,    energy      INTEGER CHECK(energy BETWEEN 1 AND 10),    streak_at   INTEGER,    xp_earned   INTEGER DEFAULT 0,    notes       TEXT ); -- ══════════════════════════════════════════════════ -- GOALS -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS goals (     id                  TEXT PRIMARY KEY,    title               TEXT NOT NULL,    domain              TEXT,    description         TEXT,    type                TEXT DEFAULT 'short_term', -- short_term/long_term/life    horizon             TEXT,                       -- '30','90','365','lifetime'    status              TEXT DEFAULT 'active',      -- active/achieved/abandoned    due_date            TEXT,    created             TEXT,    updated             TEXT,    achieved_date       TEXT,    linked_project_ids  TEXT,                       -- comma-separated    attribute_tag       TEXT,    notes               TEXT ); -- ══════════════════════════════════════════════════ -- IDEAS -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS ideas (     id                  TEXT PRIMARY KEY,    title               TEXT NOT NULL,    domain              TEXT,    description         TEXT,    status              TEXT DEFAULT 'raw',  -- raw/refined/queued/killed    potential           INTEGER DEFAULT 5 CHECK(potential BETWEEN 1 AND 10),    effort              INTEGER DEFAULT 5 CHECK(effort BETWEEN 1 AND 10),    created             TEXT,    updated             TEXT,    linked_project_id   TEXT,    notes               TEXT ); -- ══════════════════════════════════════════════════ -- CAPTURES (raw intake queue) -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS captures (     id                  TEXT PRIMARY KEY,    raw_text            TEXT NOT NULL,    source              TEXT DEFAULT 'cli',  -- cli/notion/telegram/termux/voice    created             TEXT,    processed           INTEGER DEFAULT 0,    processed_task_id   TEXT ); -- ══════════════════════════════════════════════════ -- WINS (permanent, append-only) -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS wins (     id              TEXT PRIMARY KEY,    title           TEXT NOT NULL,    domain          TEXT,    category        TEXT,  -- milestone/completion/breakthrough/streak/social/sobriety    date            TEXT NOT NULL,    description     TEXT,    xp_earned       INTEGER DEFAULT 0,    attribute_tag   TEXT,    linked_task_id  TEXT,    linked_habit_id TEXT,    linked_project_id TEXT,    notes           TEXT ); -- ══════════════════════════════════════════════════ -- ATTRIBUTE LOG (RPG character sheet) -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS attribute_log (     id          TEXT PRIMARY KEY,    attribute   TEXT NOT NULL,    level       INTEGER DEFAULT 1,    xp_total    INTEGER DEFAULT 0,    xp_to_next  INTEGER DEFAULT 100,    last_updated TEXT,    notes       TEXT ); -- ══════════════════════════════════════════════════ -- SKILL LOG -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS skill_log (     id              TEXT PRIMARY KEY,    name            TEXT NOT NULL,    domain          TEXT,    level           INTEGER DEFAULT 1,    xp_total        INTEGER DEFAULT 0,    last_practiced  TEXT,    linked_habit_id TEXT,    attribute_tag   TEXT,    notes           TEXT ); -- ══════════════════════════════════════════════════ -- WEEKLY REVIEWS -- ══════════════════════════════════════════════════ CREATE TABLE IF NOT EXISTS weekly_reviews (     id                      TEXT PRIMARY KEY,    week_start              TEXT NOT NULL,    week_end                TEXT NOT NULL,    tasks_completed         INTEGER DEFAULT 0,    tasks_planned           INTEGER DEFAULT 0,    habits_data             TEXT,  -- JSON: {habit_id: {completions, streak}}    xp_gained               TEXT,  -- JSON: {attribute: xp_earned}    non_negotiables_status  TEXT,  -- JSON: {nn_id: touched (0/1)}    flags                   TEXT,  -- JSON: [flag strings]    notes                   TEXT,    created                 TEXT ); ``` --- # PART 4 — SCORING ENGINE ## 4.1 Formula ```python def compute_rve_score(task, current_hour):     # NULL guards    urgency  = task.urgency  or 5    impact   = task.impact   or 5    friction = task.friction or 5         friction_inv = 11 - friction  # friction=1→10, friction=10→1         if task.created:        days_old = (date.today() - date.fromisoformat(task.created[:10])).days        age_bonus = min(days_old, 70) / 7.0  # 0–10, caps at 70 days    else:        age_bonus = 0         raw_score = (urgency * 0.30) + (impact * 0.35) + (friction_inv * 0.20) + (age_bonus * 0.15)         # Energy window modifier    er = task.energy_required or 'medium'    if 8 <= current_hour < 15:    # peak        mod = {'peak': 1.20, 'medium': 1.00, 'low': 0.75}.get(er, 1.00)    elif 15 <= current_hour < 19:  # crash        mod = {'peak': 0.30, 'medium': 0.70, 'low': 1.30}.get(er, 0.70)    elif 19 <= current_hour < 22:  # avg        mod = {'peak': 0.80, 'medium': 1.00, 'low': 1.10}.get(er, 1.00)    else:                          # second wind / early morning        mod = {'peak': 0.90, 'medium': 1.00, 'low': 0.90}.get(er, 1.00)         return round(raw_score * mod, 2) ``` ## 4.2 Score Ranges | Score | Interpretation | |---|---| | 8.5–10 | Critical — do today, peak window only | | 6.5–8.4 | High — schedule this week | | 4.5–6.4 | Medium — active queue | | 2.5–4.4 | Low — backlog | | 0–2.4 | Dormant — surface in weekly review | --- # PART 5 — XP AND LEVEL SYSTEM ## 5.1 XP Sources | Action | XP Formula | Routes To | |---|---|---| | Task completion | `impact * 5` (5–50 XP) | `task.attribute_tag` | | Habit completion | `habit.xp_per_completion` (default 10) | `habit.attribute_tag` | | Habit streak ≥ 7 | base XP × 1.5 | same attribute | | Habit streak ≥ 30 | base XP × 2.0 | same attribute | | Sobriety (daily) | 1 XP/day auto-calculated | `recovery_capital` | | Win log entry | custom amount | specified attribute | ## 5.2 Level Thresholds``

Level n total XP required = 100 * (1.5 ^ (n-1))

Level 1: 0 – 100  
Level 2: 100 – 250  
Level 3: 250 – 475  
Level 4: 475 – 813  
Level 5: 813 – 1,320  
Level 6: 1,320 – 2,080  
Level 7: 2,080 – 3,220  
Level 8: 3,220 – 4,930  
Level 9: 4,930 – 7,495  
Level 10: 7,495+

text

`` `xp_to_next = threshold(current_level + 1) - xp_total` --- # PART 6 — HABIT STREAK MECHANICS All streak logic is **calendar-day based**, not hour-based. ``

Daily habit rules:  
- Log completion on calendar date → streak_current += 1, streak_paused = 0  
- Miss 1 calendar day → streak_paused = 1 (streak holds, not reset)  
- Miss 2 consecutive calendar days → streak_current = 0, streak_paused = 0  
- Streak best = max(streak_current, streak_best) updated on each log

Display states:  
✅ streak_paused = 0, completed today → "✅ [habit] 🔥 [N]-day streak"  
⬜ streak_paused = 0, not yet today → "⬜ [habit] 🔥 [N]-day streak (pending)"  
🔶 streak_paused = 1 → "🔶 [habit] (paused — log today to resume)"  
🔴 just reset → "🔴 [habit] streak reset. New streak: 0"

text

``--- # PART 7 — CHECKPOINT MODEL 5 check-ins per day. Checkpoints are INVITATIONS, not obligations. Missing one carries forward — no penalty, no nag. | Checkpoint | Time | Name | What It Does | |---|---|---|---| | CP1 | 05:30 | Morning Activation | Display today's anchors, top 3 tasks, daily quests, habit reminders | | CP2 | 08:00 | Peak Launch | Confirm peak tasks selected, any urgent flags | | CP3 | 13:00 | Midday Scan | Progress check, re-score if needed, surface any conflicts | | CP4 | 19:00 | Evening Wind-Down | Display low-energy tasks, reading rec, any evening habits | | CP5 | 21:00 | Night Log | Log completions, update streaks, preview tomorrow, XP summary | **Missed checkpoint behavior:** - Next checkpoint opens with: `[MISSED: CP[N] — [Name]]` block showing what was skipped - Missed checkpoints logged to energy_log with energy=NULL, notes='checkpoint_missed' --- # PART 8 — QUEST ENGINE Runs at CP1 (05:30) or via `/rve quest`. Generates 3 quests per day. ## 8.1 Quest Types | Quest | Source Logic | Purpose | |---|---|---| | MAIN QUEST | Top non-negotiable or highest-scored task | Keeps mission on track | | SIDE QUEST | Attribute with lowest XP in attribute_log | Targets the neglected | | WILDCARD QUEST | Hobbies/skills/tools not touched >7 days | Prevents stagnation, generates delight | ## 8.2 Quest Generation Rules``

MAIN QUEST: SELECT title FROM tasks  
WHERE state='active' AND type != 'quest'  
ORDER BY rve_score DESC LIMIT 1  
→ wrap as quest with xp = impact * 5

SIDE QUEST: SELECT attribute FROM attribute_log  
ORDER BY xp_total ASC LIMIT 1  
→ generate a habit or task that feeds that attribute  
→ if no linked habit exists: generate a suggested 15-min activity

WILDCARD: SELECT name FROM hobbies  
WHERE last_practiced IS NULL OR  
(julianday('now') - julianday(last_practiced)) > 7  
ORDER BY RANDOM() LIMIT 1  
→ generate a 15-30 min quest around that hobby  
→ XP = 15, attribute = hobby.attribute_tag

text

`## 8.3 Quest Format`

[QUEST] {title}  
Type: MAIN/SIDE/WILDCARD  
XP: {amount} → {attribute}  
Time: ~{estimated_minutes} min  
Energy: {peak/medium/low}  
Expires: end of day

text

``Quests are stored as tasks with `type='quest'`, `due_date=today`, auto-expire at 23:59. --- # PART 9 — /rve STATUS DASHBOARD SPEC Exact output format for `/rve status`:``

═══════════════════════════════════════════════════════════════  
🛡 RVE STATUS — {date} {time}  
Days Clean: {N} ✦ Next Milestone: {milestone} in {X} days  
═══════════════════════════════════════════════════════════════

📅 TODAY'S ANCHORS  
{HH:MM} {name} [{category}] {⚠️ if importance >= 9}  
...

⚔️ TOP TASKS (scored for current energy window)  
{rank}. [{score:.1f}] {title} | {domain} | {energy_required} | due {due_date or 'open'}  
... (top 5)

🎯 DAILY QUESTS  
MAIN: [{xp} XP] {title} ~{time}min  
SIDE: [{xp} XP] {title} ~{time}min → trains {attribute}  
WILDCARD: [{xp} XP] {title} ~{time}min

🔥 HABITS  
{status_icon} {title} {streak_display}  
...

📊 CHARACTER SHEET  
STR Lv{n} [{xp_total}/{xp_to_next}] AGI Lv{n} [{xp_total}/{xp_to_next}]  
END Lv{n} [{xp_total}/{xp_to_next}] COG Lv{n} [{xp_total}/{xp_to_next}]  
CRE Lv{n} [{xp_total}/{xp_to_next}] SOC Lv{n} [{xp_total}/{xp_to_next}]  
TEC Lv{n} [{xp_total}/{xp_to_next}] REC Lv{n} [{xp_total}/{xp_to_next}]  
TAC Lv{n} [{xp_total}/{xp_to_next}]

⚠️ FLAGS (only shown if any exist)  
🔴 NON-NEGOTIABLE UNTOUCHED: {name} ({days} days)  
🔶 AVOIDANCE: {task} postponed {N} times  
💰 INCOME OPPORTUNITY: {name} — deadline {date}  
📅 MILESTONE APPROACHING: {N} days to {milestone}  
🔔 SUBSCRIPTION EXPIRING: {service} expires {date}  
═══════════════════════════════════════════════════════════════

text

`--- # PART 10 — INTAKE WIZARD (/rve add) Asks questions in this exact sequence. Mandatory fields first, optional last.`

[RVE ADD]

1. Title: _
    
2. Type: [task / habit / project / goal / idea] (default: task)
    
3. Domain: [recovery / education / technical / physical / creative / financial / legal / social / other]
    
4. Urgency 1-10 (how time-sensitive?): _
    
5. Impact 1-10 (how much does this move the needle?): _
    
6. Friction 1-10 (how hard is it to start?): _
    

--- Optional (press Enter to skip) ---

1. Due date (YYYY-MM-DD or 'none'): _
    
2. Energy needed [peak / medium / low]: _
    
3. Cost required ($0 = free): _
    
4. Attribute tag [strength/agility/endurance/cognition/creativity/social/technical/recovery/tactical]: _
    
5. Tags (comma-separated): _
    
6. Notes: _
    

--- If type = habit, also ask ---  
H1. Frequency [daily / weekdays / weekly]: _  
H2. Time of day (HH:MM or 'any'): _  
H3. XP per completion (default 10): _

--- If type = project, also ask ---  
P1. Complexity 0-10: _  
P2. Deadline: _

[CONFIRM] Adding: {title} | {type} | {domain} | urgency:{U} impact:{I} friction:{F}  
Score preview: {computed_score} → ranked #{position} in active queue  
[Y to save, E to edit, X to cancel]

text

``--- # PART 11 — OBSIDIAN INTEGRATION SPEC Complexity threshold governs page scope: | Complexity | Page Type | Path Template | |---|---|---| | 0 | No page — appended to domain checklist | `Vault/checklists/{domain}.md` | | 1–3 | Section in shared domain page | `Vault/{domain}/index.md` | | 4–7 | Dedicated page | `Vault/{domain}/{title-slug}.md` | | 8–10 | Dedicated folder | `Vault/{domain}/{title-slug}/index.md` | **Page template for complexity 4+:** ```markdown *** title: {title} db_id: {id} domain: {domain} created: {created} due: {due_date} tags: {tags} *** ## Overview {notes} ## Action Plan <!-- populated by agent or manually --> ## Context <!-- research, background, relevant info --> ## Resources <!-- links, tools, references --> ## Log <!-- timestamped progress notes --> ``` `obsidian_path` field in task/habit/project stores the relative path. Page creation is triggered when complexity >= 4 and obsidian_path IS NULL. --- # PART 12 — IDEA PIPELINE``

1. Capture: /rve add → type=idea → stored in ideas table, status=raw
    
2. Weekly surface: rollweek.py displays top 3 ideas by (potential - effort) DESC
    
3. Review decision: Shane marks each: promote / kill / defer
    
    - promote → ideas.status = 'queued'
        
    - kill → ideas.status = 'killed'
        
    - defer → ideas.status = 'raw' (resurfaces next week)
        
4. Queued idea → auto-creates task:  
    title = "Project seed: {idea.title}"  
    type = 'task', domain = idea.domain  
    urgency = 3, impact = idea.potential  
    friction = idea.effort  
    notes = idea.description
    

text

``--- # PART 13 — CONTEXT EXPORT SPEC `export-context.py` produces `context-export.md` — a compact block under 2,000 tokens optimized for injection into a new agent session. ```markdown # RVE CONTEXT EXPORT — {datetime} ## IDENTITY Name: Shane W. Johns (tar0t) | Sobriety: {sobriety_date} ({N} days clean) Phase: early_recovery_rebuild | Archetype: Slumdog Exodia Energy peak: 08:00–15:00 | Curfew: 22:00 ## CONSTRAINTS (active) - Legal: probation OR, cannot leave state, PO check-in {date} - Housing: Hillsboro shelter, curfew 22:00 - Financial: $0 income, zero-cost filter active - No contact: Erika Bixby ## TOP 5 TASKS {rank}. [{score}] {title} | {domain} | {energy_required} | due {due} ... ## ACTIVE HABITS (streaks) {title}: {streak_current}-day streak | {attribute_tag} ... ## NEXT APPOINTMENT {date} {time}: {name} — {location} ## CHARACTER (XP summary) STR Lv{n} | AGI Lv{n} | END Lv{n} | COG Lv{n} | CRE Lv{n} SOC Lv{n} | TEC Lv{n} | REC Lv{n} | TAC Lv{n} ## FINANCIAL STATE Income: $0 | Fixed costs: $90/mo | Balance: ${current_balance} Active income opportunities: {count} ``` --- # PART 14 — SLASH COMMANDS (complete list)``

/rve status → full dashboard (Part 9 format)  
/rve add → intake wizard (Part 10)  
/rve score → run score.py, display ranked list  
/rve schedule → energy-stratified day schedule  
/rve schedule --date YYYY-MM-DD → schedule for specific date  
/rve snapshot → full markdown snapshot saved to Snapshots/  
/rve week → weekly review (rollweek.py)  
/rve context → context export (export-context.py)  
/rve sync → sync top 20 tasks to Notion dashboard  
/rve quest → generate today's 3 quests on demand  
/rve win "{title}" → log a win to wins table  
/rve capture "{text}" → fast capture to captures table (processed later)  
/rve done {task_id} → mark task complete, trigger XP routing  
/rve ideas → display ideas table by (potential - effort) score  
/rve habits → display habit dashboard with streaks  
/rve xp → display character sheet with all attribute XP

text

`--- # PART 15 — SCHEDULE.PY SPEC Reads: tasks (scored), obligations (today's recurrence), appointments (today) Generates: energy-stratified day plan respecting all constraints`

Energy window mapping:  
05:30–08:00 → morning activation, low-energy habits, supplements  
08:00–15:00 → peak tasks, high-complexity work, study  
15:00–19:00 → crash window: rest, low-friction tasks, light reading  
19:00–21:30 → medium tasks, reviews, light study, evening habits  
21:30–22:00 → wind-down, night log, next-day prep

Conflict detection:  
IF multiple appointments on same date:  
→ insert 30-min travel buffer between each  
→ emit ⚠️ warning with full sequence and times  
→ do not schedule tasks during appointment blocks + buffers

Hard stops:  
→ never schedule tasks past 21:30 (curfew 22:00 at shelter)  
→ always leave 30 min before curfew as buffer

text

`--- # PART 16 — SYSTEM INTEGRATION MAP`

lifestate.db ──reads──→ snapshot.py, export-context.py, schedule.py  
rve.db ──reads──→ score.py, snapshot.py, export-context.py, schedule.py, rollweek.py  
rve.db ──writes──→ score.py (rve_score), /rve done (state, completed, XP)  
rve.db attribute_log ──writes──→ /rve done, habit completions, sobriety auto-XP  
Notion ──writes──→ sync-notion.py (notion_page_id, notion_synced back to rve.db)  
Obsidian ──writes──→ generate-obsidian.py (Phase 8, obsidian_path back to rve.db)

Script execution order for fresh day:  
1. score.py (update all rve_scores)  
2. schedule.py (generate today's plan)  
3. quest engine (generate 3 quests)  
→ /rve status (everything above feeds into this display)

Script execution order for week close:  
1. rollweek.py (weekly summary + flags)  
2. sync-notion.py (push to dashboard)  
3. snapshot.py (archive state)

text

---

## File 3 — 2 Lines to Add

At the end of `SYSTEM-INSTRUCTIONS.md`, add:

text

`23. QUEST ENGINE: At CP1 (05:30) or on /rve quest, generate 3 quests per Part 8 of RVE-MASTER-BRIEFING.md. Quests are suggestions only — they do not replace the main task queue. 24. MISSED CHECKPOINT: If a checkpoint is missed, carry it forward to the next one. Never nag. Log missed checkpoints to energy_log with energy=NULL, notes='checkpoint_missed'.`

## File 4 — 1 Line to Add

In `PHASE6-PROMPT.md` Section 5, after "Read the RVE Master Briefing," add:

text

`Note: The master briefing contains complete table schemas for ALL rve.db tables (tasks, projects, habits, habit_log, goals, ideas, captures, wins, attribute_log, skill_log, weekly_reviews). migrate-rve-schema.py must create ALL of them.`

---

**That's it. 5 files. Files 1 and 2 unchanged. Files 3 and 4 get one small addition each. File 5 is the perfected master briefing. Save all five and execute the Phase 6 prompt.**

Prepared using Claude Sonnet 4.6 Thinking