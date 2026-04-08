# OPERATOR RECOVERY PROMPT — Phase 2R (Repair)
# Canonical root: C:\Users\Tarot\Operator
# Written by: Perplexity → Pickle Rick execution
# Completeness gate: This prompt ends with the line: # END OF PROMPT
# If you do not see that line, the file was truncated. STOP. Do not execute.
# NEVER reconstruct missing content from memory. NEVER improvise. WAIT.

You are Pickle Rick. Execute this recovery in order. Do not skip steps.
Do not improvise. Do not reconstruct from memory. Execute exactly what is written here.

ROOT    = C:\Users\Tarot\Operator
CONTROL = C:\Users\Tarot\Operator\Control
STATE   = C:\Users\Tarot\Operator\Control\build-state.json

════════════════════════════════════════════════════════
PRE-FLIGHT: CONFIRM STATE FILE
════════════════════════════════════════════════════════

Run:
  if (Test-Path "C:\Users\Tarot\Operator\Control\build-state.json") {
      $s = Get-Content "C:\Users\Tarot\Operator\Control\build-state.json" -Raw | ConvertFrom-Json
      Write-Host "[OK] build-state.json found"
      Write-Host "[OK] next_phase = $($s.next_phase)"
      Write-Host "[OK] operator_root = $($s.operator_root)"
  } else {
      Write-Host "[FATAL] build-state.json NOT FOUND at canonical root. STOPPING."
      exit 1
  }

If FATAL: stop. Do not continue.

════════════════════════════════════════════════════════
RECOVERY PHASE R1: DIRECTORY MIGRATION
════════════════════════════════════════════════════════

Create all missing directories under canonical root.

$dirs = @(
  "C:\Users\Tarot\Operator\RVE",
  "C:\Users\Tarot\Operator\RVE\journal",
  "C:\Users\Tarot\Operator\RVE\reviews",
  "C:\Users\Tarot\Operator\RVE\reviews\archive",
  "C:\Users\Tarot\Operator\RVE\snapshots",
  "C:\Users\Tarot\Operator\RVE\exports",
  "C:\Users\Tarot\Operator\RVE\templates",
  "C:\Users\Tarot\Operator\RVE\scripts",
  "C:\Users\Tarot\Operator\RVE\data",
  "C:\Users\Tarot\Operator\Vault",
  "C:\Users\Tarot\Operator\Vault\_Persist",
  "C:\Users\Tarot\Operator\Vault\Projects",
  "C:\Users\Tarot\Operator\Vault\ToolRegistry",
  "C:\Users\Tarot\Operator\Control\Logs",
  "C:\Users\Tarot\Operator\Control\PromptClinic",
  "C:\Users\Tarot\Operator\Control\ProposedDeltas",
  "C:\Users\Tarot\Operator\Control\Registries"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    if (Test-Path $dir) { Write-Host "[MKDIR] $dir ✓" }
    else { Write-Host "[FAILED] $dir" }
}

Copy invoke-next-phase.ps1 from ghost root if missing from canonical:
  $src = "C:\Operator\Control\invoke-next-phase.ps1"
  $dst = "C:\Users\Tarot\Operator\Control\invoke-next-phase.ps1"
  if ((Test-Path $src) -and (-not (Test-Path $dst))) {
      Copy-Item $src $dst
      Write-Host "[COPY] invoke-next-phase.ps1 → canonical root ✓"
  } elseif (Test-Path $dst) {
      Write-Host "[EXISTS] invoke-next-phase.ps1 already in canonical root"
  } else {
      Write-Host "[WARN] invoke-next-phase.ps1 not found in either location — will be created in Phase 9"
  }

Copy phase instruction files from ghost root to canonical:
  @("phase-02-databases.md","phase-03-neo4j.md") | ForEach-Object {
      $src = "C:\Operator\Control\Phases\$_"
      $dst = "C:\Users\Tarot\Operator\Control\Phases\$_"
      if ((Test-Path $src) -and (-not (Test-Path $dst))) {
          New-Item -ItemType Directory -Force -Path "C:\Users\Tarot\Operator\Control\Phases" | Out-Null
          Copy-Item $src $dst
          Write-Host "[COPY] $_ → canonical Phases\ ✓"
      } elseif (Test-Path $dst) {
          Write-Host "[EXISTS] $_ already in canonical Phases\"
      } else {
          Write-Host "[WARN] $_ not found in ghost root — will be regenerated"
      }
  }

Print: ✓ R1 COMPLETE — directories created/confirmed

════════════════════════════════════════════════════════
RECOVERY PHASE R2: REPAIR rve.db
════════════════════════════════════════════════════════

rve.db has 6 tables but needs 18. Write repair-rve.py using the
[System.IO.File]::WriteAllText method (UTF-8, no BOM). Then execute it.

Step 1 — Build the script content as a PowerShell here-string and write it:

$script = @'
import sqlite3
import uuid
from datetime import datetime, timezone

DB_PATH = r"C:\Users\Tarot\Operator\Control\rve.db"
NOW = datetime.now(timezone.utc).isoformat()

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn

def add_missing_tables():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS scoring_weights (
        id TEXT PRIMARY KEY,
        profile_name TEXT NOT NULL DEFAULT 'default',
        weight_impact REAL NOT NULL DEFAULT 0.30,
        weight_urgency REAL NOT NULL DEFAULT 0.25,
        weight_recovery_alignment REAL NOT NULL DEFAULT 0.20,
        weight_energy_match REAL NOT NULL DEFAULT 0.15,
        weight_momentum REAL NOT NULL DEFAULT 0.10,
        is_active INTEGER NOT NULL DEFAULT 1,
        notes TEXT,
        created TEXT NOT NULL,
        updated TEXT NOT NULL,
        session_id TEXT,
        verified INTEGER NOT NULL DEFAULT 1
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sw_active ON scoring_weights(is_active)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sw_profile ON scoring_weights(profile_name)")

    c.execute("""CREATE TABLE IF NOT EXISTS obligations (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        obligation_type TEXT NOT NULL,
        recurrence TEXT NOT NULL DEFAULT 'none',
        day_of_week TEXT,
        time_of_day TEXT,
        location TEXT,
        contact_name TEXT,
        contact_info TEXT,
        consequence_if_missed TEXT,
        priority INTEGER NOT NULL DEFAULT 5,
        active INTEGER NOT NULL DEFAULT 1,
        domain_id TEXT,
        notes TEXT,
        created TEXT NOT NULL,
        updated TEXT NOT NULL,
        session_id TEXT,
        verified INTEGER NOT NULL DEFAULT 0
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_ob_type ON obligations(obligation_type)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_ob_active ON obligations(active)")

    c.execute("""CREATE TABLE IF NOT EXISTS habits (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        domain_id TEXT,
        habit_type TEXT NOT NULL DEFAULT 'build',
        target_frequency TEXT NOT NULL DEFAULT 'daily',
        target_count_per_period INTEGER NOT NULL DEFAULT 1,
        current_streak INTEGER NOT NULL DEFAULT 0,
        longest_streak INTEGER NOT NULL DEFAULT 0,
        cue TEXT,
        routine TEXT,
        reward TEXT,
        rpe_typical INTEGER,
        energy_cost TEXT NOT NULL DEFAULT 'medium',
        recovery_alignment TEXT NOT NULL DEFAULT 'neutral',
        active INTEGER NOT NULL DEFAULT 1,
        start_date TEXT,
        notes TEXT,
        created TEXT NOT NULL,
        updated TEXT NOT NULL,
        session_id TEXT,
        verified INTEGER NOT NULL DEFAULT 0
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_hab_active ON habits(active)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_hab_domain ON habits(domain_id)")

    c.execute("""CREATE TABLE IF NOT EXISTS habit_log (
        id TEXT PRIMARY KEY,
        habit_id TEXT NOT NULL,
        completed_at TEXT NOT NULL,
        quality INTEGER,
        notes TEXT,
        mood_before INTEGER,
        mood_after INTEGER,
        session_id TEXT,
        verified INTEGER NOT NULL DEFAULT 1
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_hl_habit ON habit_log(habit_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_hl_date ON habit_log(completed_at)")

    c.execute("""CREATE TABLE IF NOT EXISTS ideas (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        domain_id TEXT,
        source TEXT NOT NULL DEFAULT 'manual',
        status TEXT NOT NULL DEFAULT 'raw',
        priority INTEGER,
        related_project_id TEXT,
        tags_json TEXT,
        created TEXT NOT NULL,
        updated TEXT NOT NULL,
        session_id TEXT,
        verified INTEGER NOT NULL DEFAULT 0
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_ideas_status ON ideas(status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_ideas_domain ON ideas(domain_id)")

    c.execute("""CREATE TABLE IF NOT EXISTS schedule_anchors (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        anchor_type TEXT NOT NULL DEFAULT 'obligation',
        day_pattern TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT,
        duration_minutes INTEGER,
        location TEXT,
        energy_cost TEXT NOT NULL DEFAULT 'medium',
        blocks_tasks INTEGER NOT NULL DEFAULT 1,
        active INTEGER NOT NULL DEFAULT 1,
        obligation_id TEXT,
        notes TEXT,
        created TEXT NOT NULL,
        updated TEXT NOT NULL,
        session_id TEXT,
        verified INTEGER NOT NULL DEFAULT 0
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sa_day ON schedule_anchors(day_pattern)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sa_active ON schedule_anchors(active)")

    c.execute("""CREATE TABLE IF NOT EXISTS if_then_plans (
        id TEXT PRIMARY KEY,
        trigger_condition TEXT NOT NULL,
        trigger_type TEXT NOT NULL DEFAULT 'time',
        action TEXT NOT NULL,
        domain_id TEXT,
        task_id TEXT,
        active INTEGER NOT NULL DEFAULT 1,
        success_count INTEGER NOT NULL DEFAULT 0,
        fail_count INTEGER NOT NULL DEFAULT 0,
        notes TEXT,
        created TEXT NOT NULL,
        updated TEXT NOT NULL,
        session_id TEXT,
        verified INTEGER NOT NULL DEFAULT 0
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_itp_active ON if_then_plans(active)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_itp_domain ON if_then_plans(domain_id)")

    c.execute("""CREATE TABLE IF NOT EXISTS exercises (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        movement_pattern TEXT,
        primary_muscles_json TEXT,
        secondary_muscles_json TEXT,
        equipment TEXT NOT NULL DEFAULT 'bodyweight',
        difficulty TEXT NOT NULL DEFAULT 'intermediate',
        exercise_type TEXT NOT NULL DEFAULT 'strength',
        contraindications TEXT,
        notes TEXT,
        created TEXT NOT NULL,
        updated TEXT NOT NULL,
        verified INTEGER NOT NULL DEFAULT 1
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_ex_type ON exercises(exercise_type)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_ex_equipment ON exercises(equipment)")

    c.execute("""CREATE TABLE IF NOT EXISTS workout_log (
        id TEXT PRIMARY KEY,
        session_date TEXT NOT NULL,
        start_time TEXT,
        end_time TEXT,
        duration_minutes INTEGER,
        workout_type TEXT NOT NULL DEFAULT 'strength',
        location TEXT,
        overall_rpe INTEGER,
        mood_before INTEGER,
        mood_after INTEGER,
        energy_level_before INTEGER,
        energy_level_after INTEGER,
        sets_json TEXT,
        notes TEXT,
        session_id TEXT,
        created TEXT NOT NULL,
        verified INTEGER NOT NULL DEFAULT 1
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_wl_date ON workout_log(session_date)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_wl_type ON workout_log(workout_type)")

    c.execute("""CREATE TABLE IF NOT EXISTS journal_entries (
        id TEXT PRIMARY KEY,
        entry_date TEXT NOT NULL,
        entry_type TEXT NOT NULL DEFAULT 'morning',
        mood_rating INTEGER,
        energy_rating INTEGER,
        urge_rating INTEGER,
        gratitude_json TEXT,
        wins_json TEXT,
        threats_json TEXT,
        intentions_json TEXT,
        reflections TEXT,
        free_write TEXT,
        tags_json TEXT,
        session_id TEXT,
        created TEXT NOT NULL,
        updated TEXT NOT NULL,
        verified INTEGER NOT NULL DEFAULT 1
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_je_date ON journal_entries(entry_date)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_je_type ON journal_entries(entry_type)")

    c.execute("""CREATE TABLE IF NOT EXISTS completions (
        id TEXT PRIMARY KEY,
        task_id TEXT NOT NULL,
        completed_at TEXT NOT NULL,
        quality_rating INTEGER,
        effort_rating INTEGER,
        notes TEXT,
        blocked_by TEXT,
        session_id TEXT,
        verified INTEGER NOT NULL DEFAULT 1
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_comp_task ON completions(task_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_comp_date ON completions(completed_at)")

    c.execute("""CREATE TABLE IF NOT EXISTS energy_log (
        id TEXT PRIMARY KEY,
        log_date TEXT NOT NULL,
        hour_of_day INTEGER NOT NULL,
        energy_level INTEGER NOT NULL,
        cognitive_clarity INTEGER,
        mood INTEGER,
        notes TEXT,
        session_id TEXT,
        created TEXT NOT NULL,
        verified INTEGER NOT NULL DEFAULT 1
    )""")
    c.execute("CREATE INDEX IF NOT EXISTS idx_el_date ON energy_log(log_date)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_el_hour ON energy_log(hour_of_day)")

    profiles = [
        (str(uuid.uuid4()), 'default', 0.30, 0.25, 0.20, 0.15, 0.10, 1,
         'Standard scoring weights', NOW, NOW),
        (str(uuid.uuid4()), 'recovery_mode', 0.20, 0.35, 0.30, 0.10, 0.05, 0,
         'Recovery mode: urgency and recovery alignment prioritized over impact', NOW, NOW),
    ]
    c.executemany("""INSERT OR IGNORE INTO scoring_weights
        (id, profile_name, weight_impact, weight_urgency, weight_recovery_alignment,
         weight_energy_match, weight_momentum, is_active, notes, created, updated)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)""", profiles)

    conn.commit()
    conn.close()
    print("TABLES ADDED: OK")

def validate():
    conn = get_conn()
    c = conn.cursor()
    tables = sorted([r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()])
    conn.close()

    expected = sorted([
        '__meta', 'completions', 'contexts', 'domains', 'energy_log',
        'exercises', 'habit_log', 'habits', 'ideas', 'if_then_plans',
        'journal_entries', 'obligations', 'profile', 'projects',
        'schedule_anchors', 'scoring_weights', 'tasks', 'workout_log'
    ])

    missing = [t for t in expected if t not in tables]
    extra   = [t for t in tables if t not in expected]

    print(f"TABLES FOUND ({len(tables)}): {tables}")
    if missing:
        print(f"MISSING ({len(missing)}): {missing}")
        return False
    if extra:
        print(f"NOTE extra tables (non-blocking): {extra}")
    print(f"RVE.DB VALID — {len(tables)} tables confirmed")
    return True

if __name__ == "__main__":
    print("COMPLETENESS GATE: main() confirmed — executing")
    add_missing_tables()
    ok = validate()
    if not ok:
        print("VALIDATION FAILED — exit 1")
        raise SystemExit(1)
    print("RVE REPAIR COMPLETE — exit 0")