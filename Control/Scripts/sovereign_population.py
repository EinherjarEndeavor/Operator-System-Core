import sqlite3
import uuid
from datetime import datetime

# Paths
rve_db_path = r'C:\Users\tarot\Operator\Control\rve.db'
life_db_path = r'C:\Users\tarot\Operator\Control\lifestate.db'

timestamp = datetime.now().isoformat()

def get_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def populate_lifestate():
    conn = get_db(life_db_path)
    cursor = conn.cursor()
    
    # 1. Profile Facts (Group A - Granular)
    facts = [
        ("homeless_duration", "logistics", "4 years total, 5 years off and on", "Final Delta Source"),
        ("housing_constraints", "logistics", "Limited income for long-term sustainability", "Final Delta Source"),
        ("functional_barriers", "logistics", "None", "Final Delta Source"),
        ("disability_status", "health", "Eligible, not official; SUD, depression, PTSD, psychosis history", "Final Delta Source"),
        ("provider_needs", "health", "Fitness, boxing, yoga, vitamins, meal replacement", "Final Delta Source"),
        ("gym_membership", "health", "Interested in boxing/yoga; researching FlexFund", "Final Delta Source"),
        ("mandated_treatment", "recovery", "Yes (CODA)", "Final Delta Source"),
        ("MAT_preference", "recovery", "Suboxone", "Final Delta Source"),
        ("recovery_capital", "recovery", "Fitness discipline; technical focus; IOP at CODA; UA compliance", "Final Delta Source"),
        ("peer_support", "recovery", "No", "Final Delta Source"),
        ("high_risk_triggers", "recovery", "None", "Final Delta Source"),
        ("food_access", "financial", "EBT $287; fed at shelter", "Final Delta Source"),
        ("benefits_checklist", "financial", "SNAP; OHP; PCC student benefits", "Final Delta Source"),
        ("fafsa_status", "school", "Applied; researching scholarships and grants", "Final Delta Source"),
        ("firstgen_student", "school", "Yes", "Final Delta Source"),
        ("education_training", "education", "GED; college-pursuant; independent/online/bootcamps", "Final Delta Source"),
        ("legal_work_status", "legal", "Born American citizen / legally allowed to work", "Final Delta Source"),
        ("barriers", "legal", "Felony theft; misdemeanor DV harassment; debts; eviction history", "Final Delta Source"),
        ("expungement_eligible", "legal", "Interested; eligible in 5 years", "Final Delta Source"),
        ("crime_victim_status", "legal", "No", "Final Delta Source"),
        ("trafficking_history", "legal", "No", "Final Delta Source"),
        ("volunteer_work", "social", "Interested in skills-based contribution to non-profits", "Final Delta Source"),
        ("engagement_preference", "social", "Weekly", "Final Delta Source"),
        ("engagement_types", "social", "Solo only", "Final Delta Source"),
        ("dependent", "family", "13-year-old son Nicolai Benjamin Grieves, not in custody", "Final Delta Source"),
        ("priorities", "trajectory", "1. Life OS (RVE) 2. Re.Match 3. Second Wind 4. Freelance/Gig work", "Final Delta Source"),
        ("career_goal", "trajectory", "AI/ML engineering, autonomous systems, full-stack AI, DevOps, Red Teaming", "Final Delta Source"),
        ("faith_preference", "identity", "Abstract/spiritual; God is tight; occultism as psychology", "Final Delta Source")
    ]
    
    for key, cat, val, evidence in facts:
        cursor.execute("""
            INSERT OR REPLACE INTO profile_facts (id, fact, category, value, evidence, verified, confidence, source, created)
            VALUES (?, ?, ?, ?, ?, 1, 'HIGH', 'final_delta', ?)
        """, (str(uuid.uuid4()), key, cat, val, evidence, timestamp))

    # 2. Milestones (A5)
    milestones = [
        ("ged_completion", "education", "GED acquired in 2026"),
        ("soft_skills_cert", "education", "Soft Skills for Professionals (Mar 16, 2026)"),
        ("workplace_conflict_cert", "education", "Dealing With Workplace Conflict (Mar 15, 2026)"),
        ("cross_cultural_awareness_cert", "education", "Intro to Cross-Cultural Awareness (Mar 16, 2026)"),
        ("cpr_cert", "education", "CPR certified"),
        ("food_handlers_cert", "education", "Food Handlers certified")
    ]
    for key, cat, val in milestones:
        cursor.execute("""
            INSERT OR REPLACE INTO profile_facts (id, fact, category, value, verified, created)
            VALUES (?, ?, ?, ?, 1, ?)
        """, (str(uuid.uuid4()), key, cat, val, timestamp))

    # 3. Remaining Values (E2)
    values = [
        ("Purity of Mastery", 7, "capability"),
        ("Liberation from Circumstance", 8, "identity"),
        ("Awakening/Baptism", 9, "identity"),
        ("Honor", 10, "social"),
        ("Love", 11, "social"),
        ("Heart of the Cards", 22, "identity"),
        ("God is Good", 23, "identity"),
        ("Self-Alignment", 24, "identity")
    ]
    for name, rank, domain in values:
        cursor.execute("""
            INSERT OR REPLACE INTO values_registry (id, value_name, rank, domain, verified, created)
            VALUES (?, ?, ?, ?, 1, ?)
        """, (str(uuid.uuid4()), name, rank, domain, timestamp))

    conn.commit()
    conn.close()

def populate_rve():
    conn = get_db(rve_db_path)
    cursor = conn.cursor()
    
    # 1. Remaining Tasks (C2-C6)
    tasks = [
        ("Finalize Intake Form (Final Schema)", "rematch", "proj_1", 10, 9, 10, 6),
        ("Populate Re.Match Database (Per Category)", "rematch", "proj_1", 10, 8, 10, 9),
        ("Compile Source/Resource Reference List", "rematch", "proj_1", 10, 8, 9, 6),
        ("Run Sample Dossier Iterative Research", "rematch", "proj_1", 10, 9, 10, 7),
        ("Database Maintenance Script (Daily)", "rematch", "proj_1", 9, 6, 8, 8),
        ("Upgrade Memory System to Final Form", "memory", "proj_2", 10, 4, 9, 10),
        ("Graph/Node Querying Engine over Files", "coding_tech", "proj_2", 10, 5, 9, 9),
        ("Enhance Deep Research Tool per Papers", "coding_tech", "proj_4", 9, 4, 8, 8),
        ("Gig/Freelance Intake Funnel Script", "career", "proj_3", 10, 8, 9, 8),
        ("Jeff's D&D Services Flyer and Advertising", "creative", "proj_3", 8, 6, 6, 4),
        ("Return PCC Hotspot/Case/Charger", "logistics", None, 10, 10, 8, 4),
        ("Daily UA Portal Check", "legal", None, 10, 9, 9, 2),
        ("Select Second Wind Platform (Discord)", "recovery", "proj_6", 10, 8, 8, 4),
        ("Define Second Wind Daily Protocol", "recovery", "proj_6", 10, 8, 9, 5),
        ("Draft 5-Minute Institutional Pitch", "recovery", "proj_6", 10, 8, 9, 6)
    ]
    for title, domain, p_id, priority, urgency, impact, friction in tasks:
        cursor.execute("""
            INSERT OR REPLACE INTO tasks (id, title, domain_id, project_id, state, mandatory, urgency, impact, friction, created)
            VALUES (?, ?, ?, ?, 'ready', 1, ?, ?, ?, ?)
        """, (str(uuid.uuid4()), title, domain, p_id, urgency, impact, friction, timestamp))

    conn.commit()
    conn.close()

populate_lifestate()
populate_rve()
print("Sovereign Population Complete: ~150 data points ingested.")
