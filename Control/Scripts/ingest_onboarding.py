import sqlite3
import uuid
from datetime import datetime

db_path = r'C:\Users\tarot\Operator\Control\lifestate.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

timestamp = datetime.now().isoformat()

# 1. Ingest Profile Facts
facts = [
    ("User Age", "identity", "35", "DIOGENES ONBOARDING"),
    ("Sobriety Anchor", "recovery", "2025-09-19", "DIOGENES ONBOARDING"),
    ("Location", "logistics", "Hillsboro OR (Shelter)", "DIOGENES ONBOARDING"),
    ("Legal Status", "legal", "Probation (Washington County)", "DIOGENES ONBOARDING"),
    ("PO Name", "legal", "Asianna 'Asia' Nelson", "DIOGENES ONBOARDING")
]

for fact, cat, val, evidence in facts:
    cursor.execute("""
        INSERT INTO profile_facts (id, fact, category, value, evidence, verified, confidence, source, created)
        VALUES (?, ?, ?, ?, ?, 1, 'HIGH', 'onboarding', ?)
    """, (str(uuid.uuid4()), fact, cat, val, evidence, timestamp))

# 2. Ingest Attribute Log (D&D Stats)
# Mapping: Current Level = Stat, Notes = Target
attributes = [
    ("Strength", 11, "Target: 14"),
    ("Dexterity", 13, "Target: 14"),
    ("Agility", 11, "Target: 16"),
    ("Constitution", 12, "Target: 18"),
    ("Intelligence", 13, "Target: 17"),
    ("Wisdom", 16, "Target: 18"),
    ("Charisma", 12, "Target: 18")
]

for attr, lvl, notes in attributes:
    cursor.execute("""
        INSERT INTO attribute_log (id, attribute, level, xp_total, xp_to_next, last_updated, notes)
        VALUES (?, ?, ?, 0, 100, ?, ?)
    """, (str(uuid.uuid4()), attr, lvl, timestamp, notes))

# 3. Ingest Values Registry
values = [
    ("Eloquent Speech", "Behavioral excellence in communication.", "Identity alignment", 1, "social"),
    ("Helping Others", "Providing major life impact to as many as possible.", "Purpose alignment", 2, "social"),
    ("Absolute Honesty", "Living unapologetically honest.", "Psychological health", 3, "identity")
]

for name, desc, why, rank, domain in values:
    cursor.execute("""
        INSERT INTO values_registry (id, value_name, description, why_matters, rank, domain, verified, created)
        VALUES (?, ?, ?, ?, ?, ?, 1, ?)
    """, (str(uuid.uuid4()), name, desc, why, rank, domain, timestamp))

conn.commit()
conn.close()
print(f"Ingestion complete. Rows inserted: {len(facts) + len(attributes) + len(values)}")
