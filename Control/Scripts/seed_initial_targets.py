import sqlite3
import uuid
from datetime import datetime

rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'

def seed_tasks():
    conn = sqlite3.connect(rve_db_path)
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    
    tasks = [
        (str(uuid.uuid4()), "Develop PCC Summer Term Enrollment Plan", "school", 1, "captured", 1, 0, "2026-05-01", 120, "high_cognitive", 8, 9, 7, 8, 4, 10, timestamp),
        (str(uuid.uuid4()), "Finalize 90-day AI/ML Self-Education Curriculum", "coding_tech", 1, "captured", 1, 0, "2026-04-15", 180, "high_cognitive", 9, 10, 9, 9, 5, 10, timestamp),
        (str(uuid.uuid4()), "Request Medical History Records for DHS Voc-Rehab", "health_fitness", 1, "captured", 1, 0, "2026-04-20", 60, "low_energy", 7, 8, 8, 7, 6, 9, timestamp)
    ]
    
    for t_id, title, domain, onboarded, state, mandatory, fixed, due, dur, energy, urgency, impact, cascade, compound, friction, benefit, created in tasks:
        cursor.execute("""
            INSERT INTO tasks (id, title, domain_id, onboarded, state, mandatory, fixed, due, duration_est_min, energy_type, urgency, impact, cascade_val, compound_val, friction, immediate_benefit, created)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (t_id, title, domain, onboarded, state, mandatory, fixed, due, dur, energy, urgency, impact, cascade, compound, friction, benefit, created))
    
    conn.commit()
    conn.close()

seed_tasks()
print("First 3 SMART Targets Committed to RVE.")
