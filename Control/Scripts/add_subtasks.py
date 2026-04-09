import sqlite3
import uuid
from datetime import datetime

rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'

def add_integration_subtasks():
    conn = sqlite3.connect(rve_db_path)
    cursor = conn.cursor()
    ts = datetime.now().isoformat()
    
    subtasks = [
        ("Google Calendar Sync Integration", "rve_system", "proj_0", "API-level anchor sync"),
        ("Google Tasks Bridge", "rve_system", "proj_0", "Mobile-to-CLI task routing"),
        ("System Alerts & Notifications", "rve_system", "proj_0", "Alert integration for task windows")
    ]
    
    for title, domain, p_id, note in subtasks:
        cursor.execute("""
            INSERT INTO tasks (id, title, domain_id, project_id, state, atomic, urgency, impact, notes, created, updated)
            VALUES (?, ?, ?, ?, 'ready', 0, 10, 10, ?, ?, ?)
        """, (str(uuid.uuid4()), title, domain, p_id, note, ts, ts))
    
    conn.commit()
    conn.close()
    print("Integration subtasks added to RVE MVP.")

add_integration_subtasks()
