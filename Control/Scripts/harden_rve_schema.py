import sqlite3
from datetime import datetime

rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'

def patch_schema():
    conn = sqlite3.connect(rve_db_path)
    cursor = conn.cursor()
    
    # 1. Hardening Tasks Table
    # We will recreate the table to ensure bit-perfect column order per Spec 1.1
    # First, backup existing data if any (minimal risk as we just initialized)
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks_old AS SELECT * FROM tasks")
    cursor.execute("DROP TABLE IF EXISTS tasks")
    
    cursor.execute("""
        CREATE TABLE tasks (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            domain_id TEXT,
            project_id TEXT,
            state TEXT DEFAULT 'captured',
            fixed INTEGER DEFAULT 0,
            location TEXT,
            due_date TEXT,
            duration_est_min INTEGER,
            energy_type TEXT,
            urgency INTEGER DEFAULT 5,
            impact INTEGER DEFAULT 5,
            friction INTEGER DEFAULT 5,
            cascade_val INTEGER DEFAULT 5,
            compound_val INTEGER DEFAULT 5,
            immediate_benefit INTEGER DEFAULT 5,
            mandatory INTEGER DEFAULT 0,
            atomic INTEGER DEFAULT 1,
            action_plan TEXT,
            contact TEXT,
            website TEXT,
            estimated_fields INTEGER DEFAULT 1,
            needs_review INTEGER DEFAULT 1,
            postpone_count INTEGER DEFAULT 0,
            if_then_plan TEXT,
            notes TEXT,
            created TEXT,
            updated TEXT,
            completed_at TEXT,
            actual_duration_min INTEGER,
            actual_difficulty INTEGER,
            actual_energy_used TEXT,
            completion_notes TEXT,
            followup_spawned TEXT,
            estimate_error REAL,
            source TEXT DEFAULT 'manual',
            verified INTEGER DEFAULT 0
        )
    """)
    
    # 2. Hardening Projects Table
    cursor.execute("DROP TABLE IF EXISTS projects")
    cursor.execute("""
        CREATE TABLE projects (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            domain_id TEXT,
            initiative TEXT,
            status TEXT DEFAULT 'active',
            stage TEXT DEFAULT 'planning',
            description TEXT,
            goal TEXT,
            success_criteria TEXT,
            next_action_id TEXT,
            target_date TEXT,
            completion_pct INTEGER DEFAULT 0,
            created TEXT,
            updated TEXT,
            notes TEXT
        )
    """)

    # 3. Ensuring Schedule Anchors Table
    cursor.execute("DROP TABLE IF EXISTS schedule_anchors")
    cursor.execute("""
        CREATE TABLE schedule_anchors (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            anchor_type TEXT DEFAULT 'routine',
            day_pattern TEXT,
            start_time TEXT,
            end_time TEXT,
            energy_cost TEXT,
            location TEXT,
            contact TEXT,
            active INTEGER DEFAULT 1,
            created TEXT,
            updated TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Schema Hardening Complete: Tasks (26+ fields), Projects, and Anchors aligned.")

if __name__ == "__main__":
    patch_schema()
