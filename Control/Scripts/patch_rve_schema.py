import sqlite3
import uuid
from datetime import datetime

rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'

def patch_rve_schema():
    conn = sqlite3.connect(rve_db_path)
    cursor = conn.cursor()
    
    # 1. Patch Tasks Table (Full Design)
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
            due TEXT,
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
            estimated_fields INTEGER DEFAULT 0,
            needs_review INTEGER DEFAULT 0,
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
            estimate_error REAL
        )
    """)

    # 2. Patch Projects Table
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

    # 3. Patch Ideas Table (Pipeline States)
    cursor.execute("DROP TABLE IF EXISTS ideas")
    cursor.execute("""
        CREATE TABLE ideas (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            domain_id TEXT,
            stage TEXT DEFAULT 'captured',
            why TEXT,
            potential INTEGER DEFAULT 5,
            effort INTEGER DEFAULT 5,
            created TEXT,
            updated TEXT,
            notes TEXT
        )
    """)

    # 4. Patch Habits Table
    cursor.execute("DROP TABLE IF EXISTS habits")
    cursor.execute("""
        CREATE TABLE habits (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            domain_id TEXT,
            type TEXT DEFAULT 'binary',
            trigger TEXT,
            action TEXT,
            frequency TEXT DEFAULT 'daily',
            streak_current INTEGER DEFAULT 0,
            streak_best INTEGER DEFAULT 0,
            last_logged TEXT,
            active INTEGER DEFAULT 1,
            notes TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("RVE Schema patched to Full Design specifications.")

patch_rve_schema()
