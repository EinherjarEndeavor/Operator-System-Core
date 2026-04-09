import sqlite3
import uuid
import json
from datetime import datetime

rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'
life_db_path = r'C:\Users\tarot\Operator\Control\lifestate.db'

def get_db_connection(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def rve_log(title, domain_id=None, notes=None):
    conn = get_db_connection(rve_db_path)
    cursor = conn.cursor()
    task_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO tasks (id, title, domain_id, state, estimated_fields, needs_review, created, updated)
        VALUES (?, ?, ?, 'captured', 1, 1, ?, ?)
    """, (task_id, title, domain_id, timestamp, timestamp))
    conn.commit()
    conn.close()
    return f"Task '{title}' captured. ID: {task_id}"

def rve_done(task_id, actual_min, difficulty, energy_used, notes=None):
    conn = get_db_connection(rve_db_path)
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    
    # 1. Fetch estimate for error calculation
    cursor.execute("SELECT duration_est_min FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    est_min = row['duration_est_min'] if row and row['duration_est_min'] else actual_min
    est_error = (actual_min - est_min) / est_min if est_min != 0 else 0
    
    cursor.execute("""
        UPDATE tasks SET 
            state = 'completed', 
            completed_at = ?, 
            actual_duration_min = ?, 
            actual_difficulty = ?, 
            actual_energy_used = ?, 
            completion_notes = ?, 
            estimate_error = ?
        WHERE id = ?
    """, (timestamp, actual_min, difficulty, energy_used, notes, est_error, task_id))
    
    conn.commit()
    conn.close()
    return f"Task {task_id} completed and calibrated."

def rve_export_context():
    conn_rve = get_db_connection(rve_db_path)
    conn_life = get_db_connection(life_db_path)
    
    context = {
        "identity": [dict(r) for r in conn_life.execute("SELECT fact, value FROM profile_facts WHERE active=1").fetchall()],
        "active_projects": [dict(r) for r in conn_rve.execute("SELECT title, stage, goal FROM projects WHERE status='active'").fetchall()],
        "ready_tasks": [dict(r) for r in conn_rve.execute("SELECT title, urgency, impact, due FROM tasks WHERE state='ready' ORDER BY urgency DESC LIMIT 5").fetchall()],
        "obligations": [dict(r) for r in conn_rve.execute("SELECT title, start_time, day_pattern FROM schedule_anchors WHERE active=1").fetchall()]
    }
    
    conn_rve.close()
    conn_life.close()
    
    export_path = r'C:\Users\tarot\Operator\Control\exports\context-latest.json'
    with open(export_path, 'w') as f:
        json.dump(context, f, indent=2)
    return f"Context exported to {export_path}"

if __name__ == "__main__":
    print(rve_export_context())
