import sqlite3
import uuid
import json
from datetime import datetime

# Paths
rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'
life_db_path = r'C:\Users\tarot\Operator\Control\lifestate.db'

def get_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def rve_log(title, domain_id=None):
    conn = get_db(rve_db_path)
    cursor = conn.cursor()
    t_id = str(uuid.uuid4())
    ts = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO tasks (id, title, domain_id, state, estimated_fields, needs_review, created, updated)
        VALUES (?, ?, ?, 'captured', 1, 1, ?, ?)
    """, (t_id, title, domain_id, ts, ts))
    conn.commit()
    conn.close()
    return {"status": "captured", "id": t_id, "message": f"Task '{title}' logged. Onboarding pending."}

def rve_checkpoint(energy, available_min):
    conn = get_db(rve_db_path)
    cursor = conn.cursor()
    
    # Identify next anchor
    now_time = datetime.now().strftime("%H:%M")
    cursor.execute("SELECT title, start_time FROM schedule_anchors WHERE active=1 AND start_time > ? ORDER BY start_time ASC LIMIT 1", (now_time,))
    next_anchor = cursor.fetchone()
    
    # Recommend Tasks
    cursor.execute("""
        SELECT title, duration_est_min, urgency, impact 
        FROM tasks 
        WHERE state='ready' AND duration_est_min <= ? 
        ORDER BY urgency DESC, impact DESC LIMIT 2
    """, (available_min,))
    recommendations = [dict(r) for r in cursor.fetchall()]
    
    # Onboarding Alert
    cursor.execute("SELECT count(*) as count FROM tasks WHERE state='captured' OR state='onboarding_pending'")
    pending_count = cursor.fetchone()['count']
    
    conn.close()
    return {
        "next_anchor": dict(next_anchor) if next_anchor else None,
        "recommendations": recommendations,
        "onboarding_alert": f"{pending_count} tasks need enrichment" if pending_count > 0 else None
    }

def rve_export_context():
    conn_rve = get_db(rve_db_path)
    conn_life = get_db(life_db_path)
    
    context = {
        "projects": [dict(r) for r in conn_rve.execute("SELECT title, stage, goal FROM projects WHERE status='active'").fetchall()],
        "top_tasks": [dict(r) for r in conn_rve.execute("SELECT title, urgency, impact FROM tasks WHERE state='ready' ORDER BY urgency DESC LIMIT 5").fetchall()],
        "profile": [dict(r) for r in conn_life.execute("SELECT fact, value FROM profile_facts WHERE confidence='HIGH'").fetchall()]
    }
    
    conn_rve.close()
    conn_life.close()
    
    out_path = r'C:\Users\tarot\Operator\Control\exports\context-latest.json'
    with open(out_path, 'w') as f:
        json.dump(context, f, indent=2)
    return out_path

if __name__ == "__main__":
    # Internal test: Export check
    print(f"Context exported to: {rve_export_context()}")
