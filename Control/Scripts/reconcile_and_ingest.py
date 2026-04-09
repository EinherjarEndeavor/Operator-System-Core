import sqlite3
import uuid
from datetime import datetime

# 1. Align rve.db with Part 5 Schema
rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'
life_db_path = r'C:\Users\tarot\Operator\Control\lifestate.db'

def setup_rve_schema():
    conn = sqlite3.connect(rve_db_path)
    cursor = conn.cursor()
    
    # Tables from ThisIsTheReportStandard.md.txt (Part 5)
    schema = [
        "CREATE TABLE IF NOT EXISTS profile (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT)",
        "CREATE TABLE IF NOT EXISTS domains (id TEXT PRIMARY KEY, name TEXT, color_code TEXT, active INTEGER DEFAULT 1)",
        "CREATE TABLE IF NOT EXISTS projects (id TEXT PRIMARY KEY, title TEXT, domain_id TEXT, initiative TEXT, status TEXT DEFAULT 'active', stage TEXT, description TEXT, goal TEXT, created TEXT, updated TEXT)",
        "CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, title TEXT NOT NULL, domain_id TEXT, project_id TEXT, onboarded INTEGER DEFAULT 0, state TEXT DEFAULT 'captured', mandatory INTEGER DEFAULT 0, fixed INTEGER DEFAULT 0, due TEXT, duration_est_min INTEGER, energy_type TEXT, location TEXT, urgency INTEGER, impact INTEGER, cascade_val INTEGER, compound_val INTEGER, friction INTEGER, immediate_benefit INTEGER, atomic INTEGER DEFAULT 1, contact TEXT, website TEXT, action_plan TEXT, if_then_plan TEXT, estimated_fields INTEGER DEFAULT 0, postpone_count INTEGER DEFAULT 0, notes TEXT, created TEXT, completed_at TEXT, actual_duration_min INTEGER, actual_difficulty INTEGER, actual_energy_used TEXT, completion_notes TEXT)",
        "CREATE TABLE IF NOT EXISTS obligations (id TEXT PRIMARY KEY, title TEXT, domain_id TEXT, frequency TEXT, day_of_week TEXT, time_of_day TEXT, location TEXT, contact TEXT, notes TEXT, active INTEGER DEFAULT 1)",
        "CREATE TABLE IF NOT EXISTS habits (id TEXT PRIMARY KEY, title TEXT, type TEXT, trigger TEXT, action TEXT, target_attribute TEXT, difficulty INTEGER, stage TEXT, streak INTEGER DEFAULT 0, last_logged TEXT, active INTEGER DEFAULT 1, notes TEXT)",
        "CREATE TABLE IF NOT EXISTS habit_log (id TEXT PRIMARY KEY, habit_id TEXT, date TEXT, completed INTEGER, notes TEXT)",
        "CREATE TABLE IF NOT EXISTS ideas (id TEXT PRIMARY KEY, title TEXT, domain_id TEXT, stage TEXT DEFAULT 'contemplation', why TEXT, notes TEXT, created TEXT, updated TEXT)",
        "CREATE TABLE IF NOT EXISTS schedule_anchors (id TEXT PRIMARY KEY, title TEXT, domain_id TEXT, week TEXT, day_of_week TEXT, start_time TEXT, end_time TEXT, location TEXT, recurs INTEGER DEFAULT 1, active INTEGER DEFAULT 1)",
        "CREATE TABLE IF NOT EXISTS if_then_plans (id TEXT PRIMARY KEY, cue TEXT, response TEXT, domain_id TEXT, linked_task_id TEXT, active INTEGER DEFAULT 1, notes TEXT)",
        "CREATE TABLE IF NOT EXISTS journal_entries (id TEXT PRIMARY KEY, date TEXT, type TEXT, file_path TEXT, tags TEXT, mood INTEGER, energy INTEGER, created TEXT)",
        "CREATE TABLE IF NOT EXISTS completions (id TEXT PRIMARY KEY, task_id TEXT, completed_at TEXT, actual_duration_min INTEGER, actual_difficulty INTEGER, actual_energy_used TEXT, notes TEXT, ideas_spawned TEXT)"
    ]
    
    for statement in schema:
        cursor.execute(statement)
    
    # Seed Domains
    domains = [
        ('school', 'School', '#4285f4'),
        ('recovery', 'Recovery', '#0f9d58'),
        ('legal_admin', 'Legal/Admin', '#ea4335'),
        ('health_fitness', 'Health/Fitness', '#fbbc04'),
        ('career', 'Career', '#f53b57'),
        ('coding_tech', 'Coding/Tech', '#673ab7'),
        ('creative', 'Creative', '#e91e63'),
        ('relationships', 'Relationships', '#3f51b5'),
        ('finances', 'Finances', '#ff9800'),
        ('housing', 'Housing', '#795548')
    ]
    cursor.executemany("INSERT OR IGNORE INTO domains (id, name, color_code) VALUES (?, ?, ?)", domains)
    
    conn.commit()
    conn.close()

def ingest_rematch_data():
    conn = sqlite3.connect(life_db_path)
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    
    # Re.Match Data Extraction
    facts = [
        ("Current Goal", "trajectory", "AI/ML Engineering & Autonomous Systems", "Re.Match Answers"),
        ("Income Mode", "financial", "Gig/Freelance (Target $2k/mo)", "Re.Match Answers"),
        ("Mailing Address", "logistics", "1710 SW Harvey Way, Aloha, OR", "Re.Match Answers"),
        ("Contact Phone", "identity", "971-490-1351", "Re.Match Answers"),
        ("Medical Constraint", "health", "Nerve compression palsy (left hand)", "Re.Match Answers"),
        ("Debt - Landlord", "financial", "$15,000", "Re.Match Answers"),
        ("Debt - Banks", "financial", "$2,000", "Re.Match Answers"),
        ("Treatment Status", "recovery", "Intensive Outpatient @ CODA (Mandated)", "Re.Match Answers"),
        ("Education Goal", "school", "Summer term enrollment (Plan by 5/1/26)", "Re.Match Answers"),
        ("Fitness Habit", "health", "Weight training, HIIT, Zone 2, Stairmaster", "Re.Match Answers"),
        ("Psychological Profile", "identity", "ADHD, Hyperfocus patterns, Self-directed", "Re.Match Answers")
    ]
    
    for fact, cat, val, evidence in facts:
        cursor.execute("""
            INSERT INTO profile_facts (id, fact, category, value, evidence, verified, confidence, source, created)
            VALUES (?, ?, ?, ?, ?, 1, 'HIGH', 'rematch_ingestion', ?)
        """, (str(uuid.uuid4()), fact, cat, val, evidence, timestamp))
    
    conn.commit()
    conn.close()

setup_rve_schema()
ingest_rematch_data()
print("RVE Schema Aligned & Re.Match Data Ingested.")
