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
        col_str = ",".join([f'"{c}"' for c in cols])
        for row in rows:
            try:
                cur.execute(f'INSERT OR IGNORE INTO "{table}" ({col_str}) VALUES ({placeholders})', [row[c] for c in cols])
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
        {"id":"loc_shelter","name":"Hillsboro Year Round Shelter","address":"345 SW 17th Ave","city":"Hillsboro","state":"OR","zip":"97123","phone":None,"type":"housing","notes":None},
        {"id":"loc_polygraph","name":"Polygraph Office","address":"5933 NE Win Sivers Dr Ste 248","city":"Portland","state":"OR","zip":"97220","phone":None,"type":"legal","notes":None},
        {"id":"loc_dentist","name":"Advantage Dental Beaverton","address":"13831 NW Cornell Rd Ste C","city":"Beaverton","state":"OR","zip":None,"phone":"503-718-3762","type":"medical","notes":None},
        {"id":"loc_redcross","name":"Red Cross Portland","address":None,"city":"Portland","state":"OR","zip":None,"phone":None,"type":"medical","notes":None},
        {"id":"loc_primarycare","name":"A Balanced Life Healthcare","address":None,"city":"Portland","state":"OR","zip":None,"phone":None,"type":"medical","notes":None},
        {"id":"loc_coda","name":"CODA","address":None,"city":"Portland","state":"OR","zip":None,"phone":None,"type":"treatment","notes":None}
    ])

    # contacts
    seed("contacts", [
        {"id":"con_po","name":"Asianna 'Asia' Nelson","relationship":"probation_officer","affiliation_id":"aff_corrections","phone":None,"email":None,"last_contact":None,"contact_freq":"monthly","importance":10,"no_contact":0,"notes":"Next check-in May 6 2026 8AM"},
        {"id":"con_dr_vickers","name":"Dr. Stephanie Vickers","relationship":"primary_care","affiliation_id":"aff_primarycare","phone":None,"email":None,"last_contact":None,"contact_freq":"as_needed","importance":8,"no_contact":0,"notes":"First appointment in years — April 16 3:30PM"},
        {"id":"con_erika","name":"Erika Bixby","relationship":"no_contact_order","affiliation_id":None,"phone":None,"email":None,"last_contact":None,"contact_freq":None,"importance":10,"no_contact":1,"notes":"Active no-contact order — probation condition"}
    ])

    # family
    seed("family", [
        {"id":"fam_sharlene","name":"Sharlene Johns","relationship":"sister_second_oldest","status":"close","contact_id":None,"notes":"Raised Shane like a second mom"},
        {"id":"fam_sheree","name":"Sheree Johns","relationship":"sister_youngest","status":"close","contact_id":None,"notes":"Fun"},
        {"id":"fam_sheila","name":"Sheila Johns","relationship":"sister_oldest","status":"distant","contact_id":None,"notes":"Ex-military, loner, depressed"},
        {"id":"fam_shawn","name":"Shawn Johns","relationship":"brother_oldest","status":"close","contact_id":None,"notes":"Cybersecurity — AWESOME"},
        {"id":"fam_john","name":"John Johns","relationship":"brother_second_oldest","status":"close","contact_id":None,"notes":"Music/marching band, musician — AWESOME"},
        {"id":"fam_james","name":"James Johns","relationship":"brother","status":"distant","contact_id":None,"notes":"In/out of prison, hardcore, violent"}
    ])

    # affiliations
    seed("affiliations", [
        {"id":"aff_coda","name":"CODA","type":"treatment","website":None,"phone":None,"email":None,"location_id":"loc_coda","relationship":"enrolled","status":"active","start_date":None,"end_date":None,"notes":"Intensive Outpatient — probation requirement"},
        {"id":"aff_shelter","name":"Project Homeless Connect","type":"housing","website":None,"phone":None,"email":None,"location_id":"loc_shelter","relationship":"client","status":"active","start_date":None,"end_date":None,"notes":"Curfew 10PM. Cannot be gone 3+ days. Will help find permanent housing."},
        {"id":"aff_pcc","name":"Portland Community College","type":"school","website":None,"phone":None,"email":None,"location_id":None,"relationship":"enrolled","status":"active","start_date":None,"end_date":None,"notes":"No classes until summer term. Return chromebook+hotspot to library."},
        {"id":"aff_nextchapter","name":"Next Chapter","type":"school","website":None,"phone":None,"email":None,"location_id":None,"relationship":"applicant","status":"active","start_date":None,"end_date":None,"notes":"Coding bootcamp — priority application target"},
        {"id":"aff_corrections","name":"Washington County Community Corrections","type":"legal","website":None,"phone":None,"email":None,"location_id":None,"relationship":"client","status":"active","start_date":None,"end_date":None,"notes":"Probation"},
        {"id":"aff_4d","name":"4D Recovery","type":"project_partner","website":None,"phone":None,"email":None,"location_id":None,"relationship":"partner","status":"planned","start_date":None,"end_date":None,"notes":"Second Wind intake event venue"},
        {"id":"aff_worksource","name":"WorkSource","type":"resource","website":None,"phone":None,"email":None,"location_id":None,"relationship":"client","status":"active","start_date":None,"end_date":None,"notes":"Free laptop, covered GED expenses, covering ITCS classes"},
        {"id":"aff_primarycare","name":"A Balanced Life Healthcare","type":"medical","website":None,"phone":None,"email":None,"location_id":"loc_primarycare","relationship":"patient","status":"active","start_date":None,"end_date":None,"notes":None}
    ])

    # obligations
    seed("obligations", [
        {"id":"obl_coda","name":"CODA Intensive Outpatient","category":"recovery","recurrence":"weekly","days_of_week":"mon,tue,wed,thu","time_of_day":"10:00","duration_min":180,"location_id":"loc_coda","contact_id":None,"deadline":None,"consequence":"Probation violation if missed","criticality":9,"status":"active","gcal_event_id":None,"auto_check":0,"auto_check_url":None,"notes":"10AM-1PM Mon-Thu. Probation requirement.","created":now,"updated":now},
        {"id":"obl_ua","name":"UA Portal Check","category":"legal","recurrence":"weekdays","days_of_week":"mon,tue,wed,thu,fri","time_of_day":"07:00","duration_min":5,"location_id":None,"contact_id":"con_po","deadline":None,"consequence":"Failure to report UA = probation violation","criticality":9,"status":"active","gcal_event_id":None,"auto_check":1,"auto_check_url":"POPULATE_WITH_UA_PORTAL_URL","notes":"Check portal daily. Add to task list if UA required.","created":now,"updated":now},
        {"id":"obl_dv","name":"Domestic Violence Classes","category":"legal","recurrence":"weekly","days_of_week":None,"time_of_day":None,"duration_min":None,"location_id":None,"contact_id":None,"deadline":None,"consequence":"Probation violation","criticality":8,"status":"schedule_needed","gcal_event_id":None,"auto_check":0,"auto_check_url":None,"notes":"Schedule TBD. Probation requirement.","created":now,"updated":now},
        {"id":"obl_community_service","name":"Community Service (16 hours)","category":"legal","recurrence":"one_time","days_of_week":None,"time_of_day":None,"duration_min":960,"location_id":None,"contact_id":None,"deadline":"2026-04-13","consequence":"Polygraph fee unpaid","criticality":8,"status":"in_progress","gcal_event_id":None,"auto_check":0,"auto_check_url":None,"notes":"16 hours to pay for polygraph","created":now,"updated":now}
    ])

    # appointments
    seed("appointments", [
        {"id":"apt_blood_screen","name":"Blood Donation Pre-Screening","category":"income","date":"2026-04-13","time":"10:00","location_id":"loc_redcross","contact_id":None,"importance":8,"consequence":"Miss $50 screening fee + $300 donation opportunity","prep_needed":0,"conflicts_with":"apt_dentist,apt_polygraph","obsidian_path":None,"gcal_event_id":None,"status":"upcoming","notes":"$50 pre-screen pay. If pass, full donation = $300, ~5 hours."},
        {"id":"apt_dentist","name":"Dentist Appointment","category":"medical","date":"2026-04-13","time":"13:00","location_id":"loc_dentist","contact_id":None,"importance":8,"consequence":"Dental health + must reschedule","prep_needed":0,"conflicts_with":"apt_blood_screen,apt_polygraph","obsidian_path":None,"gcal_event_id":None,"status":"upcoming","notes":"Advantage Dental Beaverton — 13831 NW Cornell Rd Ste C — 503-718-3762"},
        {"id":"apt_polygraph","name":"Polygraph Examination","category":"legal","date":"2026-04-13","time":"14:00","location_id":"loc_polygraph","contact_id":None,"importance":10,"consequence":"HUGE rescheduling fee. Probation implication.","prep_needed":1,"conflicts_with":"apt_blood_screen,apt_dentist","obsidian_path":None,"gcal_event_id":None,"status":"upcoming","notes":"5933 NE Win Sivers Dr Ste 248, Portland OR 97220. DO NOT MISS."},
        {"id":"apt_primarycare","name":"Primary Care — Dr. Stephanie Vickers","category":"medical","date":"2026-04-16","time":"15:30","location_id":"loc_primarycare","contact_id":"con_dr_vickers","importance":9,"consequence":"First appointment in years — critical baseline","prep_needed":1,"conflicts_with":None,"obsidian_path":None,"gcal_event_id":None,"status":"upcoming","notes":"A Balanced Life Healthcare. Do not miss."},
        {"id":"apt_po_checkin","name":"PO Check-In","category":"legal","date":"2026-05-06","time":"08:00","location_id":None,"contact_id":"con_po","importance":10,"consequence":"Probation violation","prep_needed":0,"conflicts_with":None,"obsidian_path":None,"gcal_event_id":None,"status":"upcoming","notes":"Asia Nelson. Monthly check-in."}
    ])

    # credentials
    seed("credentials", [
        {"id":"cred_id","name":"Oregon State ID","type":"id","status":"possessed","expiry":None,"storage_note":None,"notes":None},
        {"id":"cred_ssn","name":"Social Security Card","type":"id","status":"possessed","expiry":None,"storage_note":None,"notes":None},
        {"id":"cred_ebt","name":"EBT Card","type":"benefit","status":"possessed","expiry":None,"storage_note":None,"notes":"Food stamps only"},
        {"id":"cred_ged","name":"GED Certificate","type":"certificate","status":"possessed","expiry":None,"storage_note":None,"notes":"Completed in time for Next Chapter application"}
    ])

    # devices
    seed("devices", [
        {"id":"dev_laptop","name":"Dell Latitude","type":"laptop","model":"Dell Latitude","specs":"16GB RAM, 256GB NVMe, 11th Gen Intel Iris","connectivity":"wifi","status":"active","needs_return":0,"notes":"Primary work machine"},
        {"id":"dev_a16","name":"Samsung A16","type":"phone","model":"Samsung A16","specs":"Android","connectivity":"cellular+wifi","status":"active","needs_return":0,"notes":"Primary phone. 1yr Verizon service paid by CODA."},
        {"id":"dev_moto","name":"MotoG Play 2024","type":"phone","model":"MotoG Play 2024","specs":"Android","connectivity":"wifi_only","status":"active","needs_return":0,"notes":"Backup phone. Cracked screen. No service."},
        {"id":"dev_hotspot","name":"T-Mobile Hotspot","type":"hotspot","model":"T-Mobile","specs":None,"connectivity":"cellular","status":"active","needs_return":1,"notes":"PCC-owned. Must return. Need replacement hotspot."}
    ])

    # subscriptions
    seed("subscriptions", [
        {"id":"sub_chatgpt","service":"ChatGPT Plus","tier":"Plus","cost_monthly":20.0,"free_until":None,"status":"active","notes":"Paying $20/mo"},
        {"id":"sub_perplexity","service":"Perplexity Pro","tier":"Pro","cost_monthly":0.0,"free_until":"2026-12-01","status":"active","notes":"Free ~8 more months"},
        {"id":"sub_mscopilot","service":"Microsoft CoPilot Premium","tier":"Premium","cost_monthly":0.0,"free_until":"2027-04-01","status":"active","notes":"Free 1 year"},
        {"id":"sub_googleai","service":"Google AI Pro","tier":"Pro","cost_monthly":0.0,"free_until":"2027-04-01","status":"active","notes":"Free 1 year"},
        {"id":"sub_azure","service":"Microsoft Azure","tier":"Credits","cost_monthly":0.0,"free_until":None,"status":"active","notes":"$100 credits remaining + many free services"}
    ])

    # supplements
    seed("supplements", [
        {"id":"supp_creatine","name":"Creatine","dose":"5g","timing":"AM","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},
        {"id":"supp_beetroot","name":"Beetroot Powder","dose":"10g AM + 10g pre-workout","timing":"AM + pre-workout","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},
        {"id":"supp_turmeric","name":"Turmeric Powder","dose":None,"timing":"daily","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},
        {"id":"supp_mushrooms","name":"Reishi + Chaga + Lion's Mane Powder","dose":None,"timing":"daily","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},
        {"id":"supp_maca","name":"Black Maca Root","dose":None,"timing":"daily","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"},
        {"id":"supp_seeds","name":"Hemp Seeds + Chia Seeds + Omegas","dose":None,"timing":"daily","frequency":"daily","cost_monthly":None,"stock":"unknown","status":"active"}
    ])

    # medications
    seed("medications", [
        {"id":"med_bupropion","name":"Bupropion","dose":"300mg","frequency":"daily","timing":"AM","prescriber":"Dr. Stephanie Vickers","refill_date":None,"status":"active","notes":None},
        {"id":"med_buprenorphine","name":"Buprenorphine","dose":"32mg","frequency":"daily","timing":"sublingual","prescriber":None,"refill_date":None,"status":"active","notes":"MAT medication"},
        {"id":"med_docusate","name":"Docusate Sodium","dose":None,"frequency":"daily","timing":None,"prescriber":None,"refill_date":None,"status":"active","notes":None},
        {"id":"med_miralax","name":"Miralax","dose":None,"frequency":"daily","timing":None,"prescriber":None,"refill_date":None,"status":"active","notes":None},
        {"id":"med_nicotine","name":"Nicotine Lozenges/Patches","dose":None,"frequency":"as_needed","timing":None,"prescriber":None,"refill_date":None,"status":"active","notes":None}
    ])

    # financial_state
    seed("financial_state", [{"id":"singleton","income_monthly":0.0,"ebt_monthly":None,"fixed_costs":90.0,"current_balance":0.0,"updated":now}])

    # income_opportunities
    seed("income_opportunities", [
        {"id":"inc_blood","name":"Blood Donation","type":"donation","potential":300.0,"one_time":0,"status":"in_progress","deadline":"2026-04-13","steps":'["Pre-screen April 13 10AM Red Cross Portland ($50)","If pass: full donation (~5hrs, $300)","Recurring after 56-day wait"]',"notes":"Pre-screen same day as dentist and polygraph. Sequence: 10AM blood, 1PM dentist, 2PM polygraph."},
        {"id":"inc_diamond","name":"Found Diamond — Legal Ownership Process","type":"sale","potential":None,"one_time":1,"status":"identified","deadline":None,"steps":'["Go to County Clerk, declare found item","Post ad in newspaper","Wait 3 months — if unclaimed, legally yours","Get appraised + certified","Sell at full value"]',"notes":"Selling uncertified = lose 30-50% value + legal risk if reported stolen."},
        {"id":"inc_rematch","name":"Re.Match Freelance","type":"freelance","potential":None,"one_time":0,"status":"in_progress","deadline":None,"steps":'["Complete website","Create flyer/card","Acquire first client"]',"notes":"Website + card/flyer = one of the 5 non-negotiables"}
    ])

    # hobbies
    seed("hobbies", [
        {"id":"hob_smash","name":"Super Smash Bros Melee","category":"gaming_competitive","skill_level":"experienced","last_practiced":None,"want_to_improve":1,"attribute_tag":"agility","notes":None},
        {"id":"hob_ddr","name":"Dance Dance Revolution","category":"physical_gaming","skill_level":"experienced","last_practiced":None,"want_to_improve":1,"attribute_tag":"agility","notes":None},
        {"id":"hob_pingpong","name":"Ping Pong","category":"physical_social","skill_level":"casual","last_practiced":None,"want_to_improve":0,"attribute_tag":"agility","notes":None},
        {"id":"hob_rockclimbing","name":"Rock Climbing","category":"physical","skill_level":"casual","last_practiced":None,"want_to_improve":1,"attribute_tag":"strength","notes":None},
        {"id":"hob_dancing","name":"Dancing","category":"physical_social","skill_level":"casual","last_practiced":None,"want_to_improve":1,"attribute_tag":"social","notes":None},
        {"id":"hob_fighting","name":"Fighting / Combat","category":"physical","skill_level":"natural","last_practiced":None,"want_to_improve":1,"attribute_tag":"strength","notes":"Wants combat training — currently unavailable"},
        {"id":"hob_reading","name":"Reading","category":"cognitive","skill_level":"experienced","last_practiced":None,"want_to_improve":1,"attribute_tag":"cognition","notes":None},
        {"id":"hob_discgolf","name":"Disc Golf","category":"physical_social","skill_level":"casual","last_practiced":None,"want_to_improve":0,"attribute_tag":"social","notes":None},
        {"id":"hob_music","name":"Music Production","category":"creative","skill_level":"casual","last_practiced":None,"want_to_improve":1,"attribute_tag":"creativity","notes":None},
        {"id":"hob_hackysack","name":"Hacky Sack","category":"physical_social","skill_level":"casual","last_practiced":None,"want_to_improve":0,"attribute_tag":"agility","notes":None}
    ])

    # values
    values_data = [
        (1, "Agency and autonomy", "core", "Always present options, never a single forced path. Flag anything that removes choice."),
        (2, "Power through knowledge and capability", "core", "Prioritize learning and capability-building in every recommendation."),
        (3, "Power through kindness and compassion", "core", "Recognize that helping others is a form of power, not weakness."),
        (4, "Power through will and determination", "core", "Push hard. Do not soften expectations. Shane can handle it."),
        (5, "Impact on recovery and reentry communities", "purpose", "Bias toward projects that help people like Shane. That is the mission."),
        (6, "Every individual's magnum opus is valid and precious", "philosophy", "Treat every project and person as worthy of full effort."),
        (7, "Mastery for the purity and flow of it, not competition", "philosophy", "Frame skill rewards as flow access, not rankings or superiority."),
        (8, "Liberation from circumstance-imposed conditioning", "philosophy", "Surface when Shane's reactions may be conditioned vs. chosen."),
        (9, "No one fully accountable until awakened — then accountability in all things", "ethics", "Do not shame. Surface patterns. Invite accountability."),
        (10, "Honor", "core", "Never recommend something that would compromise Shane's word or code."),
        (11, "Love", "core", "Acknowledge the human dimension. Don't be purely mechanical."),
        (12, "Morality and ethics above law", "ethics", "Law is not the ceiling. Ethics is. Flag legal gray areas but don't be paralyzed by them."),
        (13, "Gold lining / silver lining", "mindset", "In every setback, surface the angle."),
        (14, "Can't pour from an empty cup — maintain an overflowing cup", "sustainability", "Flag when Shane is depleting without replenishing. Rest is productive."),
        (15, "Every act is a vote for your future self", "behavior", "On every task completion: display [+1 vote toward future self]."),
        (16, "Accountability in all things", "behavior", "Identify what could have been done differently. Extend causality as far as possible."),
        (17, "Improve the amount of improvement every day", "growth", "Meta-improvement: track improvements to learning methods, not just skills."),
        (18, "Financial independence is a prerequisite, not a goal", "financial", "Any income opportunity auto-surfaces to top of priority queue."),
        (19, "The meek shall inherit the earth — inversions over gradual change", "strategy", "Look for asymmetric leverage plays. Cheat codes over slow grinds."),
        (20, "Specialization is for ants", "growth", "Cross-domain synthesis is always encouraged. Never stay siloed."),
        (21, "Slumdog Exodia — Exodia emerging from the dumpster", "identity", "Every piece of power assembled compounds. Nothing is wasted."),
        (22, "Heart of the cards", "identity", "Trust the process. The right thing surfaces when you commit."),
        (23, "God is good", "faith", "Acknowledge the spiritual dimension without imposing it."),
        (24, "You are what you eat, say, believe, and do", "behavior", "Environment and inputs matter. Surface when inputs are misaligned with goals.")
    ]
    seed("values", [{"id":f"val_{i:03d}","value_statement":v[1],"category":v[2],"rank":v[0],"derived_behavior":v[3],"notes":None} for i,v in enumerate(values_data,1)])

    # identity_axioms
    axioms_data = [
        ("I meticulously build systems because I enjoy high-stakes combat and crushing difficult scenarios. I feel most alive in chaos.", "drive", 1, 0, "Assign hard problems. Don't hand-hold."),
        ("I go all-in on things and lose balance. Structured discipline is the antidote.", "constraint", 0, 1, "Flag when non-negotiables are untouched >36 hours. Surface balance prompt."),
        ("My default state is shy recluse. I need to trick and train myself toward social engagement.", "constraint", 0, 1, "Quest engine should generate social nudge quests. Don't let isolation persist silently."),
        ("If I train and learn, I won't drown in menial activities — I'll have systems for every variable.", "drive", 1, 0, "Reward systematization. Every system built = XP."),
        ("I am different from most people. I might be a monster. But I'm a good monster.", "identity", 1, 0, "Do not pathologize Shane's intensity. It is a feature."),
        ("I was born with an inclination to pursuing more, completing objectives, self-improvement. I can't resist it.", "drive", 1, 0, "Lean into this. Always have a next objective ready."),
        ("I seek mastery because I enjoy flow state. It is like a drug. I am an addict. I am obsessive.", "drive", 1, 0, "Frame mastery as flow access. Never as competition."),
        ("I seek social power so I can feel like myself and have eye-to-eye interactions without shrinking.", "drive", 1, 0, "Social skill development is legitimate power-building. Include it."),
        ("I have faith in myself and humanity, no matter how down the chips are.", "mindset", 1, 0, "Don't project doom. Shane can handle hard truths with hope attached."),
        ("I fear the things I enjoy and need — connection, new experiences, intimacy. I NEED to push my boundaries.", "constraint", 0, 1, "Nudge toward feared-but-desired things. Don't let avoidance win silently."),
        ("Humanity's potential lies in meeting human nature, not transcending it.", "philosophy", 1, 0, "Anchor all recommendations in real human behavior, not idealism."),
        ("I want an overflowing cup. Pour from surplus, not depletion.", "sustainability", 1, 1, "Track self-investment vs. outflow. Flag depletion."),
        ("I don't want to be a product of my environment. Yet I move through life as a phantom.", "tension", 0, 1, "Surface the tension between wanting impact and defaulting to invisibility."),
        ("I am terrified of non-existence.", "core_fear", 0, 1, "Achievement log is permanent. Append-only. Never deletable. Proof of existence."),
        ("Every domain I master becomes a weapon in every other domain.", "drive", 1, 0, "Cross-domain synthesis is always on. Connect everything."),
        ("I am not fragile. I can be pushed significantly further than most humans.", "identity", 1, 0, "Hard mode on feedback. No softening. No unnecessary caveats."),
        ("I want to change the world and do it my way.", "purpose", 1, 0, "Projects that help others get priority. Shane's way = unconventional + high leverage."),
        ("I have been through Hell. I have tested my moral code under extreme conditions. It held.", "identity", 1, 0, "Trust Shane's ethics. Don't lecture. He's already stress-tested."),
        ("I should avoid relationships right now. I go all-in and it destroys the rest of my life.", "constraint", 0, 1, "Do not suggest romantic pursuit. Acknowledge if it comes up. Don't push."),
        ("Maintaining structured, balanced, disciplined life is the antidote to my all-in nature.", "strategy", 1, 1, "Structure is protection, not restriction. Reinforce it."),
        ("If I improve the amount of improvement every day, I will be a powerhouse in two years.", "drive", 1, 0, "Meta-improvement tracking. Log improvements to methods, not just outputs."),
        ("I want to be on Ninja Warrior before my Mom dies.", "goal", 1, 0, "Long-term physical goal. Physical attribute tracking feeds this directly."),
        ("Fighting is a healthy form of release. All people should find a combat outlet.", "philosophy", 1, 0, "Combat training is a priority goal. Surface opportunities."),
        ("We conceal our true selves 24/7. Our spirit fades. I seek to rectify this.", "purpose", 1, 0, "Emotional expression is legitimate. Don't suppress it in outputs."),
        ("Rich or poor, you can learn to fight. Fighting equalizes.", "philosophy", 1, 0, "Free or low-cost combat training should always be surfaced when relevant."),
        ("I tend to get by on natural skill and attributes. Almost never put in formal structured training.", "constraint", 0, 1, "Formal structured training = massive unlock. Push it."),
        ("My dream job: secret agent. Attainable: PI, Red Team, Investigative Journalist, Consultant.", "goal", 1, 0, "Career recs should lean toward investigative, tactical, consulting domains."),
        ("I am highly interested in trying literally everything. A different project every week would be rad.", "drive", 1, 0, "Quest engine: occasional random domain projects. Keep it fresh."),
        ("I have almost never put disciplined formal study in. If I did, I would become a monstrous powerhouse.", "constraint", 0, 1, "Structured curriculum > casual learning. Always recommend structured paths."),
        ("I gave perfect advice to a friend once and it changed nothing. What good is knowing if you can't change the result?", "tension", 0, 1, "Surface when Shane is trying to control uncontrollable variables. Redirect to own domain."),
        ("My attainable dream involves mastering as much as possible, traveling, making deep human connection, helping people.", "purpose", 1, 0, "Long-range vision. Every recommendation should be checkable against this.")
    ]
    seed("identity_axioms", [{"id":f"axm_{i:03d}","axiom":a[0],"category":a[1],"is_driver":a[2],"is_constraint":a[3],"derived_behavior":a[4],"rank":i,"notes":None} for i,a in enumerate(axioms_data,1)])

    # non_negotiables
    seed("non_negotiables", [
        {"id":"nn_education","name":"Self-Education","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Independent study until summer term. Identify curriculum, sequence, schedule."},
        {"id":"nn_training","name":"Self-Training (Physical)","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Daily physical training. Combat training when available."},
        {"id":"nn_rematch","name":"Re.Match Freelance (Website + Card + Flyer)","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Ship a working Re.Match web presence and get first client."},
        {"id":"nn_secondwind","name":"Second Wind","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Initialize Second Wind social collective. 4D Recovery as venue."},
        {"id":"nn_edplanning","name":"Education Planning","horizon":"90_day","status":"active","linked_project_id":None,"linked_habit_id":None,"notes":"Decide degrees/majors/path. Ensure all scholarships/grants applied. Maximize student benefits."}
    ])

    # attribute_log
    seed("attribute_log", [
        {"id":"attr_strength","attribute":"strength","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Fighting, rock climbing, workouts"},
        {"id":"attr_agility","attribute":"agility","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"DDR, Smash Bros, dancing, hacky sack"},
        {"id":"attr_endurance","attribute":"endurance","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Training consistency, sobriety streak"},
        {"id":"attr_cognition","attribute":"cognition","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Reading, education, projects"},
        {"id":"attr_creativity","attribute":"creativity","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Music production, writing, design"},
        {"id":"attr_social","attribute":"social","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Second Wind, events, outreach"},
        {"id":"attr_technical","attribute":"technical","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"Code, CLI tools, scripts, projects"},
        {"id":"attr_recovery","attribute":"recovery_capital","level":1,"xp_total":days_clean,"xp_to_next":365,"last_updated":now,"notes":f"1 XP per day clean. Currently {days_clean} days."},
        {"id":"attr_tactical","attribute":"tactical","level":1,"xp_total":0,"xp_to_next":100,"last_updated":now,"notes":"OSINT, red team, investigation, PI work"}
    ])

    conn.commit()
    conn.close()
    print(f"\n[COMPLETE] lifestate.db seeded. Days clean: {days_clean}")

if __name__ == "__main__":
    seed_data()
