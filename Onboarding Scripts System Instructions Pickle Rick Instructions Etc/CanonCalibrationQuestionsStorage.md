**Q32.** What is your current stock level (full / low / out) for each supplement you listed?

**Q33.** What is the URL for the UA web portal — and do you currently have saved login credentials somewhere accessible?

**Q34.** Do you have a sponsor or accountability partner in your recovery program? If so, when did you last connect with them, and how often is expected?

**Q35.** What is your exact EBT monthly amount — and are there any restrictions on what you can use it for that affect how you eat or plan your week?

**Q36.** Of the 10 hobbies you listed (Smash, DDR, Ping Pong, rock climbing, dancing, fighting, reading, disc golf, music production, hacky sack) — which have you actually done in the last 30 days?

**Q37.** What is the one skill you most regret not starting 5 years ago?

**Q38.** If your laptop died today with no warning, what data would you permanently lose that has no backup?
## Step 5 · Deliverable 3 — Pass 2 Calibration Questions (7)

**Q39.** Walk me through your typical morning from 5AM to when CODA starts. What do you actually do in that window?

**Q40.** Of your 9 RPG attributes above — strength, agility, endurance, cognition, creativity, social, technical, recovery capital, tactical — rank them by how much you want to grow them in the next 6 months (1 = top priority).

**Q41.** What's the last thing you built, wrote, or created that you were genuinely proud of — and what specifically made it good?

**Q42.** Which of your 5 non-negotiables are you currently most behind on?

**Q43.** Do you have any debts, fines, restitution, or financial obligations we haven't logged yet — court fees, civil judgments, anything?

**Q44.** Is there any person in your current network who is actively a liability to your sobriety or legal status — someone you're still in contact with who you shouldn't be?

**Q45.** What is the one thing about yourself that you think the system should push you hardest on — the thing you avoid most that you know matters most?
## Step 4 · Deliverable 3 — Pass 3 Calibration Questions (7)

**Q46.** What is the most important thing about yourself that you want the system to remember and never let you forget — even when you're not thinking about it?

**Q47.** What is one recurring thing that currently happens to you (not by choice) that eats time or energy and should either be automated away or systematically handled?

**Q48.** What does your ideal project look like — not the content, but the _shape_ of it? Solo or collaborative? Short sprint or long build? Public or private?

**Q49.** What's one thing you've learned in recovery that you wish every person entering recovery knew on day 1?

**Q50.** If you could have one recurring "side quest" auto-generated for you every week — something completely unrelated to your current projects — what domain should it come from?

**Q51.** Is there a version of yourself — a persona, a mode, a state — that you're trying to grow toward? If you had to name that version of yourself, what would you call them?

**Q52.** What's the one thing that, if you looked back at this period 5 years from now, you'd be most disappointed you didn't do?

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