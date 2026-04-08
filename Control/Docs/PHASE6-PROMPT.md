════════════════════════════════════════════════════════════
PHASE 6 — PICKLE RICK EXECUTION PROMPT
Paste one SECTION at a time. Wait for confirmation before next.
════════════════════════════════════════════════════════════
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — CONTEXT (paste this first)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You are Pickle Rick operating in Operator Mode. This session is Phase 6 of the RVE and LifeState build. Do not truncate any output. Do not summarize scripts. Write every line in full. Confirm completion of each task before I paste the next section. If a script throws an error, fix it immediately and re-run. All files referenced below already exist on disk. Ready? Reply: [PICKLE RICK READY — PHASE 6]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — TASK 1: UPDATE GEMINI.MD (paste after Section 1 confirmed)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Read the existing file at: C:\Users\tarot\Operator\Control\GEMINI.md
Read the system instructions file at: C:\Users\tarot\Operator\Control\Docs\SYSTEM-INSTRUCTIONS.md
Append the full contents of SYSTEM-INSTRUCTIONS.md to the END of GEMINI.md. Do NOT overwrite anything. Append only. Write the updated GEMINI.md to disk. Confirm: display only the appended section in your response.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — TASK 2: CREATE LIFESTATE.DB (paste after Section 2 confirmed)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Run this script: C:\Users\tarot\Operator\Control\Scripts\migrate-lifestate-schema.py
Expected output ends with: [COMPLETE] 24 tables created in C:/Users/tarot/Operator/Control/lifestate.db
If any error occurs, fix and re-run until all 24 tables are confirmed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — TASK 3: SEED ONBOARDING DATA (paste after Section 3 confirmed)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Run this script: C:\Users\tarot\Operator\Control\Scripts\seed-onboarding.py
Expected output ends with: [COMPLETE] lifestate.db populated.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — TASK 4: RVE SCRIPTS + SCHEMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Read the RVE Master Briefing at: C:\Users\tarot\Operator\Control\Docs\RVE-MASTER-BRIEFING.md
Note: The master briefing contains complete table schemas for ALL rve.db tables (tasks, projects, habits, habit_log, goals, ideas, captures, wins, attribute_log, skill_log, weekly_reviews). migrate-rve-schema.py must create ALL of them.
Execute the Phase 6 script build. This includes writing:
- migrate-rve-schema.py (with all tables from the briefing)
- score.py (using the energy-aware formula from Part 4)
- snapshot.py
- export-context.py
- schedule.py
- rollweek.py
- sync-notion.py
After all scripts are written, run: python migrate-rve-schema.py
Confirm schema. Then run: python seed-onboarding.py
Confirm all 24 tables populated.
Final output: print /rve status to confirm system is live.
