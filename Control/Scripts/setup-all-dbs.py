import sqlite3
import os
import uuid
import shutil
from datetime import datetime, timezone

DB_DIR = r"C:\Users\tarot\operator\Control"
BACKUP_DIR = r"C:\Users\tarot\operator\Control\BrainArchive\pre-build"
TIMESTAMP = datetime.now(timezone.utc).isoformat()
SESSION_ID = str(uuid.uuid4())

os.makedirs(DB_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)

def get_conn(db_path):
    """Get SQLite connection with FK enforcement and WAL mode."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.row_factory = sqlite3.Row
    return conn

def safe_write_db(db_name, schema_fn):
    """Write DB via tmp file. Backup if exists. Return (conn, path)."""
    final_path = os.path.join(DB_DIR, db_name)
    tmp_path = final_path + ".tmp"
    backup_path = os.path.join(BACKUP_DIR, db_name + ".bak")

    if os.path.exists(final_path):
        shutil.copy2(final_path, backup_path)
        print(f"  [BACKUP] {backup_path}")

    conn = get_conn(tmp_path)
    schema_fn(conn)
    conn.commit()
    conn.close()

    if os.path.exists(final_path):
        os.remove(final_path)
    os.rename(tmp_path, final_path)

    size = os.path.getsize(final_path)
    print(f"  [WRITE] {final_path} ({size} bytes)")
    return final_path

def everything_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY, started_at TEXT NOT NULL, ended_at TEXT, session_type TEXT DEFAULT 'build', phase TEXT, model_used TEXT, context_pct_used REAL, turns_count INTEGER DEFAULT 0, summary TEXT, notes TEXT);
    CREATE TABLE IF NOT EXISTS action_types (type TEXT PRIMARY KEY, description TEXT, reversible INTEGER DEFAULT 0, requires_confirmation INTEGER DEFAULT 0, risk_level TEXT DEFAULT 'low');
    CREATE TABLE IF NOT EXISTS actions (id TEXT PRIMARY KEY, timestamp TEXT NOT NULL, session_id TEXT, actor TEXT DEFAULT 'ai', action_type TEXT NOT NULL, description TEXT, target_db TEXT, target_table TEXT, target_id TEXT, payload_json TEXT, reversible INTEGER DEFAULT 0, reversed INTEGER DEFAULT 0, verified INTEGER DEFAULT 1, notes TEXT, FOREIGN KEY (session_id) REFERENCES sessions(id), FOREIGN KEY (action_type) REFERENCES action_types(type));
    CREATE TABLE IF NOT EXISTS search_log (id TEXT PRIMARY KEY, timestamp TEXT NOT NULL, session_id TEXT, query TEXT, target_db TEXT, target_table TEXT, result_count INTEGER DEFAULT 0, execution_ms INTEGER, FOREIGN KEY (session_id) REFERENCES sessions(id));
    CREATE INDEX IF NOT EXISTS idx_actions_timestamp ON actions(timestamp);
    CREATE INDEX IF NOT EXISTS idx_actions_session_id ON actions(session_id);
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version', '1.0.0', ?), ('db_name', 'everything.db', ?), ('initialized_at', ?, ?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))
    action_types = [("DB_WRITE", "Insert/update/delete to any database", 0, 0, "low"), ("FILE_CREATE", "New file created", 0, 0, "low"), ("SYSTEM_PROMPT_CHANGE", "GEMINI.md or settings modified", 1, 1, "high")]
    conn.executemany("INSERT OR IGNORE INTO action_types VALUES (?,?,?,?,?)", action_types)

def rve_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS profile (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT, verified INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS domains (id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, color_code TEXT, icon TEXT, description TEXT, why TEXT, priority_rank INTEGER DEFAULT 5, active INTEGER DEFAULT 1, created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS projects (id TEXT PRIMARY KEY, title TEXT NOT NULL, domain_id TEXT, initiative TEXT, status TEXT DEFAULT 'active', stage TEXT DEFAULT 'planning', description TEXT, goal TEXT, success_criteria TEXT, why TEXT, target_date TEXT, completion_pct INTEGER DEFAULT 0, parent_project_id TEXT, session_id TEXT, created TEXT, updated TEXT, completed_at TEXT, archived_at TEXT, archive_reason TEXT, notes TEXT, tags TEXT, verified INTEGER DEFAULT 0, source TEXT DEFAULT 'manual', FOREIGN KEY (domain_id) REFERENCES domains(id));
    CREATE TABLE IF NOT EXISTS contexts (id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, description TEXT, icon TEXT, energy_level TEXT, location TEXT, active INTEGER DEFAULT 1, created TEXT);
    CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, title TEXT NOT NULL, domain_id TEXT, project_id TEXT, context_id TEXT, session_id TEXT, onboarded INTEGER DEFAULT 0, state TEXT DEFAULT 'captured', mandatory INTEGER DEFAULT 0, fixed INTEGER DEFAULT 0, recurring INTEGER DEFAULT 0, recurrence_pattern TEXT, atomic INTEGER DEFAULT 1, task_type TEXT DEFAULT 'standard', due TEXT, due_hard INTEGER DEFAULT 0, scheduled_for TEXT, duration_est_min INTEGER, energy_type TEXT, time_of_day_pref TEXT, urgency INTEGER DEFAULT 5, impact INTEGER DEFAULT 5, cascade_val INTEGER DEFAULT 5, compound_val INTEGER DEFAULT 5, friction INTEGER DEFAULT 5, immediate_benefit INTEGER DEFAULT 5, rve_score REAL DEFAULT 0.0, score_override INTEGER DEFAULT 0, score_override_reason TEXT, scoring_preset_id TEXT DEFAULT 'default', if_then_plan TEXT, action_plan TEXT, next_action TEXT, contact TEXT, contact_phone TEXT, website TEXT, location TEXT, blocked_by TEXT, blocks TEXT, relapse_risk_mitigation INTEGER DEFAULT 0, sober_support_required INTEGER DEFAULT 0, estimated_fields INTEGER DEFAULT 0, postpone_count INTEGER DEFAULT 0, last_postponed TEXT, postpone_reason TEXT, created TEXT, completed_at TEXT, actual_duration_min INTEGER, actual_difficulty INTEGER, actual_energy_used TEXT, completion_notes TEXT, ideas_spawned TEXT, notes TEXT, tags TEXT, source TEXT DEFAULT 'manual', verified INTEGER DEFAULT 0, FOREIGN KEY (domain_id) REFERENCES domains(id), FOREIGN KEY (project_id) REFERENCES projects(id), FOREIGN KEY (context_id) REFERENCES contexts(id));
    """)

def lifestate_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS profile_facts (id TEXT PRIMARY KEY, fact TEXT NOT NULL, category TEXT, value TEXT, evidence TEXT, verified INTEGER DEFAULT 0, confidence TEXT DEFAULT 'LOW', source TEXT DEFAULT 'inferred', active INTEGER DEFAULT 1, superseded_by TEXT, session_id TEXT, created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS inferences (id TEXT PRIMARY KEY, inference TEXT NOT NULL, trigger TEXT, domain TEXT, evidence TEXT, verified INTEGER DEFAULT 0, promoted_to_fact INTEGER DEFAULT 0, promoted_fact_id TEXT, last_observed TEXT, occurrence_count INTEGER DEFAULT 1, confidence TEXT DEFAULT 'LOW', session_id TEXT, notes TEXT, created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS patterns (id TEXT PRIMARY KEY, name TEXT NOT NULL, description TEXT, type TEXT, domain TEXT, trigger TEXT, manifestation TEXT, consequence TEXT, mitigation TEXT, first_seen TEXT, last_seen TEXT, occurrence_count INTEGER DEFAULT 1, severity INTEGER DEFAULT 5, helpful INTEGER DEFAULT 0, active INTEGER DEFAULT 1, session_id TEXT, notes TEXT, verified INTEGER DEFAULT 0, created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS momentum_state (id TEXT PRIMARY KEY, domain TEXT NOT NULL UNIQUE, stage_of_change TEXT, self_efficacy INTEGER, motivation INTEGER, momentum TEXT, barriers TEXT, supports TEXT, last_updated TEXT, session_id TEXT, notes TEXT, verified INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS trajectory (id TEXT PRIMARY KEY, domain TEXT NOT NULL, snapshot_date TEXT, state_description TEXT, vector TEXT, metrics_json TEXT, session_id TEXT, notes TEXT, created TEXT);
    CREATE TABLE IF NOT EXISTS values_registry (id TEXT PRIMARY KEY, value_name TEXT NOT NULL UNIQUE, description TEXT, why_matters TEXT, rank INTEGER, domain TEXT, verified INTEGER DEFAULT 0, created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS fears (id TEXT PRIMARY KEY, fear TEXT NOT NULL, category TEXT, intensity INTEGER DEFAULT 5, rational INTEGER DEFAULT 1, origin TEXT, mitigation TEXT, domain TEXT, verified INTEGER DEFAULT 0, active INTEGER DEFAULT 1, session_id TEXT, created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS desires (id TEXT PRIMARY KEY, desire TEXT NOT NULL, category TEXT, intensity INTEGER DEFAULT 5, domain TEXT, feasibility INTEGER DEFAULT 5, timeline TEXT, linked_goals TEXT, verified INTEGER DEFAULT 0, active INTEGER DEFAULT 1, session_id TEXT, notes TEXT, created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS relationships (id TEXT PRIMARY KEY, name TEXT NOT NULL, relationship_type TEXT, contact_ref TEXT, support_type TEXT, trust_level INTEGER DEFAULT 5, recovery_support INTEGER DEFAULT 0, boundary_notes TEXT, last_contact TEXT, active INTEGER DEFAULT 1, session_id TEXT, notes TEXT, verified INTEGER DEFAULT 0, created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS constraints_registry (id TEXT PRIMARY KEY, constraint_text TEXT NOT NULL, category TEXT, severity INTEGER DEFAULT 5, start_date TEXT, end_date TEXT, domain TEXT, mitigation TEXT, verified INTEGER DEFAULT 0, active INTEGER DEFAULT 1, session_id TEXT, notes TEXT, created TEXT, updated TEXT);
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version','1.0.0',?), ('db_name','lifestate.db',?), ('initialized_at',?,?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))

def arsenal_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS tools (id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, display_name TEXT, category TEXT, subcategory TEXT, platform TEXT DEFAULT 'windows', language TEXT, installed INTEGER DEFAULT 0, install_method TEXT, install_command TEXT, uninstall_command TEXT, install_date TEXT, version TEXT, update_command TEXT, learned INTEGER DEFAULT 0, proficiency_level TEXT DEFAULT 'none', learning_priority INTEGER DEFAULT 5, last_used TEXT, use_count INTEGER DEFAULT 0, impact_score INTEGER DEFAULT 0, complexity_score INTEGER DEFAULT 0, learning_curve INTEGER DEFAULT 0, maintenance_cost INTEGER DEFAULT 0, reliability_score INTEGER DEFAULT 0, docs_path TEXT, docs_url TEXT, cookbook_path TEXT, human_guide_path TEXT, ai_guide_path TEXT, personal_use_cases TEXT, rve_tags TEXT, replaces TEXT, replaced_by TEXT, status TEXT DEFAULT 'active', problem_notes TEXT, mcp_server_key TEXT, session_id TEXT, notes TEXT, tags TEXT, verified INTEGER DEFAULT 0, source TEXT DEFAULT 'manual', created TEXT, updated TEXT);
    CREATE TABLE IF NOT EXISTS tool_combos (id TEXT PRIMARY KEY, chain_name TEXT NOT NULL UNIQUE, description TEXT, trigger TEXT, steps_json TEXT, tools_json TEXT, failure_modes TEXT, rve_domain_tags TEXT, verified INTEGER DEFAULT 0, session_id TEXT, created TEXT, last_used TEXT, use_count INTEGER DEFAULT 0, success_count INTEGER DEFAULT 0, notes TEXT);
    CREATE TABLE IF NOT EXISTS tool_docs (id TEXT PRIMARY KEY, tool_id TEXT NOT NULL, doc_type TEXT, title TEXT, content TEXT, source_url TEXT, local_path TEXT, fetched_at TEXT, quality_score INTEGER DEFAULT 0, relevance_score INTEGER DEFAULT 0, notes TEXT, FOREIGN KEY (tool_id) REFERENCES tools(id));
    CREATE TABLE IF NOT EXISTS tool_skills (id TEXT PRIMARY KEY, tool_id TEXT NOT NULL, skill_filename TEXT, skill_path TEXT, skill_content TEXT, auto_generated INTEGER DEFAULT 0, verified INTEGER DEFAULT 0, session_id TEXT, created TEXT, updated TEXT, FOREIGN KEY (tool_id) REFERENCES tools(id));
    CREATE TABLE IF NOT EXISTS tool_problems (id TEXT PRIMARY KEY, tool_id TEXT NOT NULL, problem TEXT NOT NULL, error_message TEXT, context TEXT, workaround TEXT, resolved INTEGER DEFAULT 0, resolution TEXT, session_id TEXT, created TEXT, resolved_at TEXT, FOREIGN KEY (tool_id) REFERENCES tools(id));
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version','1.0.0',?), ('db_name','arsenal.db',?), ('initialized_at',?,?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))

def rematch_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS opportunity_categories (id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, description TEXT, icon TEXT, priority_rank INTEGER DEFAULT 5);
    CREATE TABLE IF NOT EXISTS opportunities (id TEXT PRIMARY KEY, title TEXT NOT NULL, category_id TEXT, subcategory TEXT, description TEXT, what_it_provides TEXT, eligibility_criteria_json TEXT, income_limit REAL, age_min INTEGER, age_max INTEGER, location_required TEXT, citizenship_required TEXT, criminal_record_ok INTEGER DEFAULT 1, sobriety_required TEXT DEFAULT 'none', sobriety_min_days INTEGER DEFAULT 0, income_verification_required INTEGER DEFAULT 0, id_required TEXT, life_impact_score INTEGER DEFAULT 0, urgency_score INTEGER DEFAULT 0, difficulty_to_apply INTEGER DEFAULT 5, time_to_benefit TEXT, source_url TEXT, contact_name TEXT, contact_phone TEXT, contact_email TEXT, address TEXT, active INTEGER DEFAULT 1, last_verified TEXT, expiration_date TEXT, no_redundancy_hash TEXT UNIQUE, session_id TEXT, notes TEXT, tags TEXT, created TEXT, updated TEXT, FOREIGN KEY (category_id) REFERENCES opportunity_categories(id));
    CREATE TABLE IF NOT EXISTS profiles (id TEXT PRIMARY KEY DEFAULT 'primary', intake_json TEXT, income REAL, housing_status TEXT, employment_status TEXT, legal_status TEXT, sobriety_days INTEGER DEFAULT 0, location TEXT, age INTEGER, id_documents_held TEXT, created TEXT, last_updated TEXT);
    CREATE TABLE IF NOT EXISTS matches (id TEXT PRIMARY KEY, profile_id TEXT DEFAULT 'primary', opportunity_id TEXT NOT NULL, eligibility_pct INTEGER, impact_score INTEGER, match_date TEXT, status TEXT DEFAULT 'pending', applied_date TEXT, outcome_date TEXT, outcome_notes TEXT, session_id TEXT, FOREIGN KEY (profile_id) REFERENCES profiles(id), FOREIGN KEY (opportunity_id) REFERENCES opportunities(id));
    CREATE TABLE IF NOT EXISTS eligibility_checks (id TEXT PRIMARY KEY, profile_id TEXT DEFAULT 'primary', opportunity_id TEXT NOT NULL, check_date TEXT, criteria_results_json TEXT, overall_eligible INTEGER, eligibility_pct INTEGER, blocking_criteria TEXT, session_id TEXT, notes TEXT, FOREIGN KEY (profile_id) REFERENCES profiles(id), FOREIGN KEY (opportunity_id) REFERENCES opportunities(id));
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version','1.0.0',?), ('db_name','rematch.db',?), ('initialized_at',?,?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))

def supersource_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS source_types (type TEXT PRIMARY KEY, description TEXT, reliability_ceiling INTEGER DEFAULT 10, examples TEXT);
    CREATE TABLE IF NOT EXISTS sources (id TEXT PRIMARY KEY, url TEXT UNIQUE, domain_name TEXT, title TEXT, description TEXT, source_type TEXT, category TEXT, tags TEXT, quality_score INTEGER DEFAULT 0, reliability_tier TEXT, bias_rating TEXT DEFAULT 'unknown', last_verified TEXT, last_accessed TEXT, use_count INTEGER DEFAULT 0, cited_in TEXT, active INTEGER DEFAULT 1, paywalled INTEGER DEFAULT 0, requires_account INTEGER DEFAULT 0, session_id TEXT, notes TEXT, verified INTEGER DEFAULT 0, created TEXT, updated TEXT, FOREIGN KEY (source_type) REFERENCES source_types(type));
    CREATE TABLE IF NOT EXISTS source_evaluations (id TEXT PRIMARY KEY, source_id TEXT NOT NULL, evaluated_at TEXT, evaluator TEXT DEFAULT 'ai', accuracy_score INTEGER, depth_score INTEGER, currency_score INTEGER, bias_assessment TEXT, session_id TEXT, notes TEXT, FOREIGN KEY (source_id) REFERENCES sources(id));
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version','1.0.0',?), ('db_name','supersource.db',?), ('initialized_at',?,?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))

def upgrades_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS upgrade_categories (id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, description TEXT, icon TEXT);
    CREATE TABLE IF NOT EXISTS proposals (id TEXT PRIMARY KEY, title TEXT NOT NULL, idea TEXT NOT NULL, trigger TEXT, domain TEXT, category_id TEXT, problem_statement TEXT, solution TEXT, implementation_notes TEXT, method TEXT, needs_new_tech INTEGER DEFAULT 0, new_tech_required TEXT, estimated_lift TEXT, required_skills TEXT, time_estimate TEXT, complexity INTEGER DEFAULT 5, impact INTEGER DEFAULT 5, priority_score REAL DEFAULT 0.0, approval_status TEXT DEFAULT 'pending', approved_at TEXT, approved_by TEXT, rejected_reason TEXT, source TEXT DEFAULT 'session', session_id TEXT, created TEXT, resolved_at TEXT, implemented_at TEXT, notes TEXT, FOREIGN KEY (category_id) REFERENCES upgrade_categories(id));
    CREATE TABLE IF NOT EXISTS upgrade_dependencies (id TEXT PRIMARY KEY, upgrade_id TEXT NOT NULL, depends_on_upgrade_id TEXT NOT NULL, dependency_type TEXT DEFAULT 'requires', notes TEXT, FOREIGN KEY (upgrade_id) REFERENCES proposals(id), FOREIGN KEY (depends_on_upgrade_id) REFERENCES proposals(id));
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version','1.0.0',?), ('db_name','upgrades.db',?), ('initialized_at',?,?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))

def errors_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS error_categories (id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, description TEXT, icon TEXT);
    CREATE TABLE IF NOT EXISTS entries (id TEXT PRIMARY KEY, timestamp TEXT NOT NULL, category TEXT, severity INTEGER DEFAULT 5, domain TEXT, title TEXT, description TEXT NOT NULL, context TEXT, error_message TEXT, stack_trace TEXT, attempted_solutions TEXT, working_solution TEXT, root_cause TEXT, improvement_idea TEXT, upgrade_proposal_id TEXT, resolved INTEGER DEFAULT 0, resolved_at TEXT, surfaced_count INTEGER DEFAULT 0, recurrence_count INTEGER DEFAULT 1, first_occurrence TEXT, is_pattern INTEGER DEFAULT 0, pattern_id TEXT, session_id TEXT, notes TEXT, tags TEXT);
    CREATE TABLE IF NOT EXISTS error_patterns (id TEXT PRIMARY KEY, name TEXT NOT NULL, description TEXT, error_ids TEXT, frequency TEXT, mitigation TEXT, session_id TEXT, created TEXT, updated TEXT);
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version','1.0.0',?), ('db_name','errors.db',?), ('initialized_at',?,?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))

def wins_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS win_categories (id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE, description TEXT, icon TEXT);
    CREATE TABLE IF NOT EXISTS entries (id TEXT PRIMARY KEY, timestamp TEXT NOT NULL, category TEXT, domain TEXT, title TEXT, description TEXT, outcome TEXT, impact INTEGER DEFAULT 5, session_id TEXT, notes TEXT, tags TEXT);
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version','1.0.0',?), ('db_name','wins.db',?), ('initialized_at',?,?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))

def settings_schema(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS __meta (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS toggles (key TEXT PRIMARY KEY, value TEXT, description TEXT, updated_at TEXT);
    """)
    conn.execute("INSERT OR IGNORE INTO __meta VALUES ('schema_version','1.0.0',?), ('db_name','settings.db',?), ('initialized_at',?,?)", (TIMESTAMP, TIMESTAMP, TIMESTAMP, TIMESTAMP))
    toggles = [("memory_enabled", "true", "Global memory persistence", TIMESTAMP), ("auto_snapshot", "true", "Auto-snapshot before destructive ops", TIMESTAMP)]
    conn.executemany("INSERT OR IGNORE INTO toggles VALUES (?,?,?,?)", toggles)

def main():
    print(f"Initializing 10 databases in {DB_DIR}...")
    safe_write_db("everything.db", everything_schema)
    safe_write_db("rve.db", rve_schema)
    safe_write_db("lifestate.db", lifestate_schema)
    safe_write_db("arsenal.db", arsenal_schema)
    safe_write_db("rematch.db", rematch_schema)
    safe_write_db("supersource.db", supersource_schema)
    safe_write_db("upgrades.db", upgrades_schema)
    safe_write_db("errors.db", errors_schema)
    safe_write_db("wins.db", wins_schema)
    safe_write_db("settings.db", settings_schema)
    print("ALL DATABASES INITIALIZED.")

if __name__ == "__main__":
    main()


