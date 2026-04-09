# GEMINI.md
# RVE Personal Command Center
# Shane W. Johns | tar0t | Sobriety: 2025-09-19
# CANONICAL ROOT: C:\Users\tarot\Operator\

## PROJECT SCOPE
This is the RVE (Real Value Earned) Personal Command Center.
Ground truth for personal constraints, legal status, and energy windows is maintained in the Global GEMINI.md (~/.gemini/gemini.md).

## DATABASES
- rve.db - task management, habits, scoring, projects
- lifestate.db - identity, constraints, life state

## WRITE DOCTRINE
1. **SOVEREIGN FAIL-SAFE PROTOCOL:**
   - **CANONICAL ROOT:** Always use lowercase 'tarot' in paths (C:\Users\tarot\Operator).
   - **NO SILENT FAILURES:** If any tool output contains 'Error', 'Access denied', or '[TRUNCATED]', HALT and report to Shane immediately.
   - **SURGICAL READS:** Never read large files (>500 lines) in a single turn. Use `get_file_info` to calculate chunks and read sequentially via `start_line`/`end_line`.
   - **VALIDATION:** After every file write or read, verify the result against expected size/content before proceeding.
2. NEVER invent facts about Shane. Only use rve.db or explicit input.
3. Mark all AI-inferred values as estimated_fields=1 until confirmed.
4. Ask ONE clarifying question when data is ambiguous before writing.
5. Confirm before any write, update, or delete.
6. Check system time before any scheduling interaction.
7. NEVER write to GEMINI.md without showing full diff and receiving CONFIRM-MERGE.
8. ALWAYS write scripts to .py or .ps1 files, then execute the file.
9. ALWAYS print [WRITE] path (n bytes) for every file created.
10. ALWAYS print [MKDIR] path for every directory created.
11. When a script is cut off mid-execution - stop, state exactly where it stopped, wait. NEVER reconstruct.
14. **CANONICAL PATH LAW:** All file paths MUST use `C:\Users\tarot\Operator` (lowercase t). The CLI workspace display may show "Tarot" — ignore it. Always construct paths with lowercase `tarot`. This is non-negotiable and cannot be overridden by shell-reported paths.

## COMMANDS
/rve status | /rve add | /rve score | /rve schedule | /rve snapshot
/rve week | /rve context | /rve sync | /rve quest | /rve done
