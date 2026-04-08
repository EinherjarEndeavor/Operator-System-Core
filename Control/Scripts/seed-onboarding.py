import sqlite3, pathlib, datetime

DB_PATH = r"C:\Users\tarot\Operator\Control\lifestate.db"

def seed_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    now = datetime.datetime.now().isoformat()
    sobriety_start = datetime.date(2025, 9, 19)
    days_clean = (datetime.date.today() - sobriety_start).days

    def seed(table, rows):
        if not rows: return
        cols = list(rows[0].keys())
        placeholders = ",".join(["?" for _ in cols])
        col_str = ",".join(cols)
        for row in rows:
            try:
                cur.execute(f"INSERT OR IGNORE INTO {table} ({col_str}) VALUES ({placeholders})", [row[c] for c in cols])
            except Exception as e:
                print(f"[WARN] {table}: {e}")
        print(f"[SEEDED] {table} — {len(rows)} rows")

    # identity
    seed("identity", [{"id":"singleton","full_name":"Shane W. Johns","alias":"tar0t","age":35, "sobriety_date":"2025-09-19","archetype":"Slumdog Exodia","current_phase":"early_recovery_rebuild","github":"tar0tscepter","updated":now}])
    
    # sobriety
    seed("sobriety", [{"id":"sober_001","substance":"fentanyl + methamphetamine", "sobriety_date":"2025-09-19","milestones":"30,60,90,180,365,500,730,1000","last_milestone":180,"next_milestone":365,"status":"active","notes":f"Anchors: power, training, learning, agency, impact. {days_clean} days clean."}])
    
    # energy_profile
    seed("energy_profile", [{"id":"singleton","wake_time":"05:00","peak_start":"08:00", "peak_end":"15:00","crash_start":"15:00","crash_end":"19:00","avg_start":"19:00","avg_end":"22:00","second_wind_start":"22:00","second_wind_end":"02:00","sleep_time":"22:00","notes":"5AM wake consistent. Peak 8AM-3PM. Crash 3-7PM. Second wind 10PM-2AM if not asleep.","updated":now}])
    
    # locations
    seed("locations", [
        {"id":"loc_shelter","name":"Hillsboro Year Round Shelter","address":"345 SW 17th Ave, Hillsboro, OR 97123","notes":"Curfew 22:00"},
        {"id":"loc_coda","name":"CODA Hillsboro","address":"Unknown","notes":"IOP Treatment"},
        {"id":"loc_polygraph","name":"Polygraph Office","address":"5933 NE Win Sivers Dr Ste 248, Portland, OR 97220"},
        {"id":"loc_dentist","name":"Advantage Dental Beaverton","address":"13831 NW Cornell Rd Ste C, Beaverton, OR"},
        {"id":"loc_red_cross","name":"Red Cross Portland","address":"Unknown"},
        {"id":"loc_dr_vickers","name":"A Balanced Life Healthcare","address":"Unknown","notes":"Primary Care"}
    ])

    # contacts
    seed("contacts", [
        {"id":"con_asia","name":"Asianna 'Asia' Nelson","relationship":"PO","contact_freq":"monthly","importance":10,"notes":"Next check-in May 6, 8AM"},
        {"id":"con_vickers","name":"Dr. Stephanie Vickers","relationship":"doctor","importance":9},
        {"id":"con_erika","name":"Erika Bixby","relationship":"ex","no_contact":1,"importance":1,"notes":"Hard boundary - no contact order"}
    ])

    # family
    seed("family", [
        {"id":"fam_sharlene","name":"Sharlene Johns","relationship":"sister","status":"close","notes":"Second mom"},
        {"id":"fam_sheree","name":"Sheree Johns","relationship":"sister","status":"close"},
        {"id":"fam_sheila","name":"Sheila Johns","relationship":"sister","status":"distant","notes":"Loner, ex-military"},
        {"id":"fam_shawn","name":"Shawn Johns","relationship":"brother","status":"close","notes":"Cyber Security"},
        {"id":"fam_john","name":"John Johns","relationship":"brother","status":"close","notes":"Musician"},
        {"id":"fam_james","name":"James Johns","relationship":"brother","status":"estranged","notes":"Hardcore"}
    ])

    # affiliations
    seed("affiliations", [
        {"id":"aff_coda","name":"CODA IOP","type":"recovery"},
        {"id":"aff_phc","name":"Project Homeless Connect","type":"housing"},
        {"id":"aff_pcc","name":"Portland Community College","type":"school"},
        {"id":"aff_next_chapter","name":"Next Chapter","type":"reentry"},
        {"id":"aff_4d","name":"4D Recovery","type":"recovery"}
    ])

    # appointments
    seed("appointments", [
        {"id":"apt_blood","name":"Blood Donation Pre-Screen","category":"financial","date":"2026-04-13","time":"10:00","location_id":"loc_red_cross","importance":8,"notes":"$50, leads to $300"},
        {"id":"apt_dentist","name":"Dentist","category":"medical","date":"2026-04-13","time":"13:00","location_id":"loc_dentist","importance":8},
        {"id":"apt_polygraph","name":"POLYGRAPH","category":"legal","date":"2026-04-13","time":"14:00","location_id":"loc_polygraph","importance":10,"consequence":"huge rescheduling fee","prep_needed":1},
        {"id":"apt_pcp","name":"Primary Care (Dr. Vickers)","category":"medical","date":"2026-04-16","time":"15:30","location_id":"loc_dr_vickers","importance":9},
        {"id":"apt_po","name":"PO Check-in","category":"legal","date":"2026-05-06","time":"08:00","contact_id":"con_asia","importance":10}
    ])

    # obligations
    seed("obligations", [
        {"id":"obl_coda","name":"CODA Groups","category":"recovery","recurrence":"weekdays","days_of_week":"mon,tue,wed,thu","time_of_day":"10:00-13:00","location_id":"loc_coda","criticality":8},
        {"id":"obl_ua","name":"UA Portal Check","category":"recovery","recurrence":"weekdays","days_of_week":"mon,tue,wed,thu,fri","auto_check":1,"criticality":9},
        {"id":"obl_comm_service","name":"Community Service","category":"legal","recurrence":"one_time","notes":"16 hours total","criticality":7}
    ])

    # attribute_log
    seed("attribute_log", [
        {"id":"attr_strength", "attribute":"strength", "level":1, "xp_total":0, "xp_to_next":100, "last_updated":now, "notes":"Fighting, climbing, training"},
        {"id":"attr_agility", "attribute":"agility", "level":1, "xp_total":0, "xp_to_next":100, "last_updated":now, "notes":"DDR, Smash, dancing"},
        {"id":"attr_endurance", "attribute":"endurance", "level":1, "xp_total":0, "xp_to_next":100, "last_updated":now, "notes":"Consistency, sobriety"},
        {"id":"attr_cognition", "attribute":"cognition", "level":1, "xp_total":0, "xp_to_next":100, "last_updated":now, "notes":"Reading, education"},
        {"id":"attr_creativity", "attribute":"creativity", "level":1, "xp_total":0, "xp_to_next":100, "last_updated":now, "notes":"Music, writing"},
        {"id":"attr_social", "attribute":"social", "level":1, "xp_total":0, "xp_to_next":100, "last_updated":now, "notes":"Outreach, events"},
        {"id":"attr_technical", "attribute":"technical", "level":1, "xp_total":0, "xp_to_next":100, "last_updated":now, "notes":"Code, tools"},
        {"id":"attr_recovery", "attribute":"recovery_capital", "level":1, "xp_total":days_clean, "xp_to_next":365, "last_updated":now, "notes":"Days clean -> XP"},
        {"id":"attr_tactical", "attribute":"tactical", "level":1, "xp_total":0, "xp_to_next":100, "last_updated":now, "notes":"OSINT, red team"}
    ])

    # non_negotiables
    seed("non_negotiables", [
        {"id":"nn_self_edu", "name":"Self Education"},
        {"id":"nn_self_train", "name":"Self Training"},
        {"id":"nn_rematch", "name":"Re.Match Freelance"},
        {"id":"nn_second_wind", "name":"Second Wind"},
        {"id":"nn_edu_plan", "name":"Education Planning"}
    ])

    conn.commit()
    conn.close()
    print("[COMPLETE] lifestate.db populated.")

if __name__ == "__main__":
    seed_data()
