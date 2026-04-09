import sqlite3
import uuid
from datetime import datetime

# Paths
rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'
life_db_path = r'C:\Users\tarot\Operator\Control\lifestate.db'

timestamp = datetime.now().isoformat()

def commit_lifestate():
    conn = sqlite3.connect(life_db_path)
    cursor = conn.cursor()
    
    # 1. Profile Facts
    facts = [
        ("age", "identity", "35", "Final Delta Source"),
        ("gender", "identity", "Male", "Final Delta Source"),
        ("location", "logistics", "Hillsboro, OR shelter; Beaverton/Portland range", "Final Delta Source"),
        ("housing", "logistics", "Secured shelter indefinitely; stable for now", "Final Delta Source"),
        ("transport", "logistics", "Bus or MAX", "Final Delta Source"),
        ("mailing_address", "logistics", "1710 SW Harvey Way, Aloha, OR", "Final Delta Source"),
        ("internet_access", "logistics", "Active; access everywhere", "Final Delta Source"),
        ("id_checklist", "logistics", "ID and Social Security Card possessed", "Final Delta Source"),
        ("medical", "health", "Nerve compression palsy left hand; arms fall asleep; spinal/neck deviations; bad back; feet conditions; 5 teeth extracted", "Final Delta Source"),
        ("mental_health", "health", "Diagnosed depression, SUD, ADHD; hyperfocus patterns; psychosis history", "Final Delta Source"),
        ("insurance", "health", "OHP / CareOregon (Dental, Vision, Mental, Physical)", "Final Delta Source"),
        ("recovery_status", "recovery", "6 months sober (Fentanyl, Alcohol, Meth) as of Apr 2026", "Final Delta Source"),
        ("treatment_type", "recovery", "Intensive Outpatient at CODA", "Final Delta Source"),
        ("income_mode", "financial", "None; wants gig/freelance/temp; eligible for disability/SSI", "Final Delta Source"),
        ("income_goal", "financial", "$2,000/month", "Final Delta Source"),
        ("outstanding_fines", "financial", "$15,000 (Apt); $2,000 (Banks); $50 (Library)", "Final Delta Source"),
        ("legal_status", "legal", "On probation (Washington County); monthly meetings", "Final Delta Source"),
        ("skills", "competency", "AI/ML, Prompt Engineering, Agentic AI, CLI, Python, Linux, OSINT", "Final Delta Source")
    ]
    
    for key, cat, val, evidence in facts:
        cursor.execute("""
            INSERT OR REPLACE INTO profile_facts (id, fact, category, value, evidence, verified, confidence, source, created)
            VALUES (?, ?, ?, ?, ?, 1, 'HIGH', 'final_delta', ?)
        """, (str(uuid.uuid4()), key, cat, val, evidence, timestamp))

    # 2. Identity Axioms
    axioms = [
        "I meticulously build systems because I enjoy crushing difficult scenarios; I feel most alive in chaos.",
        "I grind now to acquire high-caliber passive output, allowing for future relaxation and human connection.",
        "My default is a shy recluse; I must guide/bamboozle myself toward travel, mastery, and impact.",
        "Mastery of menial activities via systematic methods reduces cognitive overhead.",
        "I am a 'good monster'—capable of extreme intensity without harming others.",
        "Mastery is my drug; I enjoy the flow state surge of mindless intent.",
        "I seek social power to eliminate pointless fear of human interaction.",
        "I want to maintain an overflowing cup—a fountain for others to fill from.",
        "Every domain I master becomes a weapon in every other domain.",
        "I am not fragile; I can be pushed significantly further than most humans.",
        "Humanity's potential lies in meeting human nature, not transcending it.",
        "Environment should be a product of me, not vice versa.",
        "Terrified of non-existence.",
        "I have tested my moral code through psychosis; my humanity is unbreakable.",
        "I go 'all-in' on relationships to my detriment; healthy balance is currently impossible.",
        "Discipline/Structure is the only counter to 'all-in' tendencies.",
        "If I improve the improvement every day, I will be a powerhouse in two years.",
        "Goal: Ninja Warrior before Mom dies.",
        "Combat is a healthy release for unidentified subconscious anger.",
        "Rectify the soul-fading caused by 24/7 emotion concealment.",
        "Fight or find an outlet that equalizes rich and poor.",
        "Fighting games are valid combat outlets.",
        "Tendency to get by on natural skill; discipline will create a monster.",
        "Disciplined study/training is the missing catalyst.",
        "Dream job: Secret Agent.",
        "Attainable jobs: PI, Red Teamer, Investigative Journalist, Personal Consultant.",
        "Infinite curiosity: One project per domain per week.",
        "Slumdog Exodia: Emerging from the dumpster as a completed, high-power entity.",
        "Specialization is for ants.",
        "Heart of the Cards.",
        "Improve the improvement daily."
    ]
    for i, axiom_text in enumerate(axioms):
        cursor.execute("""
            INSERT OR REPLACE INTO identity_axioms (id, axiom, category, is_driver, rank)
            VALUES (?, ?, 'philosophy', 1, ?)
        """, (str(uuid.uuid4()), axiom_text, i+1))

    # 3. Values
    values = [
        ("Agency / Autonomy", 1, "identity"),
        ("Power via Knowledge & Capability", 2, "capability"),
        ("Peace / Kindness", 3, "social"),
        ("Will & Determination", 4, "identity"),
        ("Impact (Recovery/Reentry)", 5, "purpose"),
        ("Absolute Honesty", 6, "identity"),
        ("Financial Independence", 7, "financial"),
        ("Honor", 8, "social"),
        ("Love", 9, "social"),
        ("Morality/Ethics above Law", 10, "identity")
    ]
    for name, rank, domain in values:
        cursor.execute("""
            INSERT OR REPLACE INTO values_registry (id, value_name, rank, domain, verified, created)
            VALUES (?, ?, ?, ?, 1, ?)
        """, (str(uuid.uuid4()), name, rank, domain, timestamp))

    conn.commit()
    conn.close()

def commit_rve():
    conn = sqlite3.connect(rve_db_path)
    cursor = conn.cursor()
    
    # 1. Projects
    projects = [
        ("proj_0", "RVE MVP", "system_core", "Execute Life OS as defined in Standard"),
        ("proj_1", "Re.Match", "social_impact", "Deploy constraint-based matching engine"),
        ("proj_2", "Memory Final Form", "system_spine", "Multi-tier relational/semantic engine"),
        ("proj_3", "Sovereign Website", "career", "Central portal for freelance/proof"),
        ("proj_4", "Research Variant", "capability", "Specialized Gemini/Pickle variant"),
        ("proj_5", "Altruism Engine", "purpose", "Rapid deployment of help via Re.Match"),
        ("proj_6", "Second Wind", "recovery", "Build social collective ecosystem")
    ]
    for p_id, title, initiative, goal in projects:
        cursor.execute("""
            INSERT OR REPLACE INTO projects (id, title, initiative, goal, status, created)
            VALUES (?, ?, ?, ?, 'active', ?)
        """, (p_id, title, initiative, goal, timestamp))

    # 2. Tasks
    tasks = [
        ("Create RVE Dashboard (MVP)", "rve_system", "proj_0", 10, 9, 10, 7),
        ("Design and Implement Journaling System", "rve_system", "proj_0", 10, 9, 9, 6),
        ("Finalize RVE Schema Optimization", "rve_system", "proj_0", 10, 9, 10, 7),
        ("Finalize Intake Form (Final Schema)", "rematch", "proj_1", 10, 9, 10, 6),
        ("Populate Re.Match Database", "rematch", "proj_1", 10, 8, 10, 9),
        ("Finalize and Launch Personal Website", "creative", "proj_3", 10, 8, 9, 6),
        ("Execute Mastery Through Compliance Audit", "legal", None, 10, 9, 10, 6),
        ("First PCP Visit Preparation", "health", None, 10, 10, 9, 5),
        ("Select Second Wind Platform (Discord)", "recovery", "proj_6", 10, 8, 8, 4)
    ]
    for title, domain, p_id, priority, urgency, impact, friction in tasks:
        cursor.execute("""
            INSERT OR REPLACE INTO tasks (id, title, domain_id, project_id, state, mandatory, urgency, impact, friction, created)
            VALUES (?, ?, ?, ?, 'ready', 1, ?, ?, ?, ?)
        """, (str(uuid.uuid4()), title, domain, p_id, urgency, impact, friction, timestamp))

    # 3. Schedule Anchors
    anchors = [
        ("Morning Coffee", "05:30", "06:00", "DAILY"),
        ("CODA IOP", "10:00", "13:00", "M-T-W-TH"),
        ("Daily Exercise", "08:00", "09:30", "DAILY"),
        ("Evening Review", "21:30", "22:00", "DAILY")
    ]
    for title, start, end, days in anchors:
        cursor.execute("""
            INSERT OR REPLACE INTO schedule_anchors (id, title, anchor_type, day_pattern, start_time, end_time, energy_cost, created, updated)
            VALUES (?, ?, 'routine', ?, ?, ?, 'high', ?, ?)
        """, (str(uuid.uuid4()), title, days, start, end, timestamp, timestamp))

    conn.commit()
    conn.close()

commit_lifestate()
commit_rve()
print("Canonical Data Commitment Complete.")
