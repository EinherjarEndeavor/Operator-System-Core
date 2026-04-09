import sqlite3, pathlib

DB_PATH = r"C:\Users\tarot\Operator\Control\lifestate.db"
pathlib.Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    print("Creating lifestate.db tables...")
    
    tables = {
        "identity": """
            CREATE TABLE IF NOT EXISTS identity (
                id              TEXT PRIMARY KEY DEFAULT 'singleton',
                full_name       TEXT DEFAULT 'Shane W. Johns',
                alias           TEXT DEFAULT 'tar0t',
                age             INTEGER DEFAULT 35,
                sobriety_date   TEXT DEFAULT '2025-09-19',
                archetype       TEXT DEFAULT 'Slumdog Exodia',
                current_phase   TEXT DEFAULT 'early_recovery_rebuild',
                github          TEXT DEFAULT 'tar0tscepter',
                primary_phone   TEXT,
                backup_phone    TEXT,
                email           TEXT,
                updated         TEXT
            )
        """,
        "sobriety": """
            CREATE TABLE IF NOT EXISTS sobriety (
                id              TEXT PRIMARY KEY,
                substance       TEXT NOT NULL,
                sobriety_date   TEXT NOT NULL,
                milestones      TEXT DEFAULT '30,60,90,180,365,500,730,1000',
                last_milestone  INTEGER DEFAULT 0,
                next_milestone  INTEGER,
                status          TEXT DEFAULT 'active',
                notes           TEXT
            )
        """,
        "energy_profile": """
            CREATE TABLE IF NOT EXISTS energy_profile (
                id              TEXT PRIMARY KEY DEFAULT 'singleton',
                wake_time       TEXT DEFAULT '05:00',
                peak_start      TEXT DEFAULT '08:00',
                peak_end        TEXT DEFAULT '15:00',
                crash_start     TEXT DEFAULT '15:00',
                crash_end       TEXT DEFAULT '19:00',
                avg_start       TEXT DEFAULT '19:00',
                avg_end         TEXT DEFAULT '22:00',
                second_wind_start TEXT DEFAULT '22:00',
                second_wind_end TEXT DEFAULT '02:00',
                sleep_time      TEXT DEFAULT '22:00',
                notes           TEXT DEFAULT '5AM wake consistent. Peak is 8AM-3PM. Crash 3-7PM. Second wind 10PM-2AM if not asleep.',
                updated         TEXT
            )
        """,
        "energy_profile_history": """
            CREATE TABLE IF NOT EXISTS energy_profile_history (
                id              TEXT PRIMARY KEY,
                snapshot_date   TEXT NOT NULL,
                wake_time       TEXT,
                peak_start      TEXT,
                peak_end        TEXT,
                crash_start     TEXT,
                crash_end       TEXT,
                second_wind_start TEXT,
                second_wind_end TEXT,
                notes           TEXT
            )
        """,
        "energy_log": """
            CREATE TABLE IF NOT EXISTS energy_log (
                id              TEXT PRIMARY KEY,
                date            TEXT NOT NULL,
                time            TEXT,
                energy          INTEGER CHECK(energy BETWEEN 1 AND 10),
                mood            INTEGER CHECK(mood BETWEEN 1 AND 10),
                sleep_hours     REAL,
                notes           TEXT,
                checkpoint_num  INTEGER
            )
        """,
        "obligations": """
            CREATE TABLE IF NOT EXISTS obligations (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                category        TEXT,
                recurrence      TEXT,
                days_of_week    TEXT,
                time_of_day     TEXT,
                duration_min    INTEGER,
                location_id     TEXT,
                contact_id      TEXT,
                deadline        TEXT,
                consequence     TEXT,
                criticality     INTEGER DEFAULT 5 CHECK(criticality BETWEEN 1 AND 10),
                status          TEXT DEFAULT 'active',
                gcal_event_id   TEXT,
                auto_check      INTEGER DEFAULT 0,
                auto_check_url  TEXT,
                notes           TEXT,
                created         TEXT,
                updated         TEXT
            )
        """,
        "appointments": """
            CREATE TABLE IF NOT EXISTS appointments (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                category        TEXT,
                date            TEXT NOT NULL,
                time            TEXT,
                location_id     TEXT,
                contact_id      TEXT,
                importance      INTEGER DEFAULT 5 CHECK(importance BETWEEN 1 AND 10),
                consequence     TEXT,
                prep_needed     INTEGER DEFAULT 0,
                conflicts_with  TEXT,
                obsidian_path   TEXT,
                gcal_event_id   TEXT,
                status          TEXT DEFAULT 'upcoming',
                notes           TEXT
            )
        """,
        "contacts": """
            CREATE TABLE IF NOT EXISTS contacts (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                relationship    TEXT,
                affiliation_id  TEXT,
                phone           TEXT,
                email           TEXT,
                last_contact    TEXT,
                contact_freq    TEXT,
                importance      INTEGER DEFAULT 5,
                no_contact      INTEGER DEFAULT 0,
                notes           TEXT
            )
        """,
        "family": """
            CREATE TABLE IF NOT EXISTS family (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                relationship    TEXT,
                status          TEXT,
                contact_id      TEXT,
                notes           TEXT
            )
        """,
        "affiliations": """
            CREATE TABLE IF NOT EXISTS affiliations (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                type            TEXT,
                website         TEXT,
                phone           TEXT,
                email           TEXT,
                location_id     TEXT,
                relationship    TEXT,
                status          TEXT DEFAULT 'active',
                start_date      TEXT,
                end_date        TEXT,
                notes           TEXT
            )
        """,
        "locations": """
            CREATE TABLE IF NOT EXISTS locations (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                address         TEXT,
                city            TEXT,
                state           TEXT DEFAULT 'OR',
                zip             TEXT,
                phone           TEXT,
                type            TEXT,
                notes           TEXT
            )
        """,
        "credentials": """
            CREATE TABLE IF NOT EXISTS credentials (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                type            TEXT,
                status          TEXT DEFAULT 'possessed',
                expiry          TEXT,
                storage_note    TEXT,
                notes           TEXT
            )
        """,
        "devices": """
            CREATE TABLE IF NOT EXISTS devices (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                type            TEXT,
                model           TEXT,
                specs           TEXT,
                connectivity    TEXT,
                status          TEXT DEFAULT 'active',
                needs_return    INTEGER DEFAULT 0,
                notes           TEXT
            )
        """,
        "subscriptions": """
            CREATE TABLE IF NOT EXISTS subscriptions (
                id              TEXT PRIMARY KEY,
                service         TEXT NOT NULL,
                tier            TEXT,
                cost_monthly    REAL DEFAULT 0,
                free_until      TEXT,
                status          TEXT DEFAULT 'active',
                notes           TEXT
            )
        """,
        "supplements": """
            CREATE TABLE IF NOT EXISTS supplements (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                dose            TEXT,
                timing          TEXT,
                frequency       TEXT DEFAULT 'daily',
                cost_monthly    REAL,
                stock           TEXT DEFAULT 'unknown',
                status          TEXT DEFAULT 'active'
            )
        """,
        "medications": """
            CREATE TABLE IF NOT EXISTS medications (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                dose            TEXT,
                frequency       TEXT,
                timing          TEXT,
                prescriber      TEXT,
                refill_date     TEXT,
                status          TEXT DEFAULT 'active',
                notes           TEXT
            )
        """,
        "financial_state": """
            CREATE TABLE IF NOT EXISTS financial_state (
                id              TEXT PRIMARY KEY DEFAULT 'singleton',
                income_monthly  REAL DEFAULT 0,
                ebt_monthly     REAL,
                fixed_costs     REAL DEFAULT 90,
                current_balance REAL DEFAULT 0,
                updated         TEXT
            )
        """,
        "income_opportunities": """
            CREATE TABLE IF NOT EXISTS income_opportunities (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                type            TEXT,
                potential       REAL,
                one_time        INTEGER DEFAULT 0,
                status          TEXT DEFAULT 'identified',
                deadline        TEXT,
                steps           TEXT,
                notes           TEXT
            )
        """,
        "hobbies": """
            CREATE TABLE IF NOT EXISTS hobbies (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                category        TEXT,
                skill_level     TEXT DEFAULT 'casual',
                last_practiced  TEXT,
                want_to_improve INTEGER DEFAULT 0,
                attribute_tag   TEXT,
                notes           TEXT
            )
        """,
        "values": """
            CREATE TABLE IF NOT EXISTS "values" (
                id              TEXT PRIMARY KEY,
                value_statement TEXT NOT NULL,
                category        TEXT,
                rank            INTEGER,
                derived_behavior TEXT,
                notes           TEXT
            )
        """,
        "identity_axioms": """
            CREATE TABLE IF NOT EXISTS identity_axioms (
                id              TEXT PRIMARY KEY,
                axiom           TEXT NOT NULL,
                category        TEXT,
                is_driver       INTEGER DEFAULT 1,
                is_constraint   INTEGER DEFAULT 0,
                derived_behavior TEXT,
                rank            INTEGER,
                notes           TEXT
            )
        """,
        "non_negotiables": """
            CREATE TABLE IF NOT EXISTS non_negotiables (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                horizon         TEXT DEFAULT '90_day',
                status          TEXT DEFAULT 'active',
                linked_project_id TEXT,
                linked_habit_id TEXT,
                notes           TEXT
            )
        """,
        "attribute_log": """
            CREATE TABLE IF NOT EXISTS attribute_log (
                id              TEXT PRIMARY KEY,
                attribute       TEXT NOT NULL,
                level           INTEGER DEFAULT 1,
                xp_total        INTEGER DEFAULT 0,
                xp_to_next      INTEGER DEFAULT 100,
                last_updated    TEXT,
                notes           TEXT
            )
        """,
        "skill_log": """
            CREATE TABLE IF NOT EXISTS skill_log (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                domain          TEXT,
                level           INTEGER DEFAULT 1,
                xp_total        INTEGER DEFAULT 0,
                last_practiced  TEXT,
                linked_habit_id TEXT,
                attribute_tag   TEXT,
                notes           TEXT
            )
        """
    }

    for name, sql in tables.items():
        try:
            # Forcing table drop to ensure all new columns are created accurately
            cur.execute(f'DROP TABLE IF EXISTS "{name}"')
            cur.execute(sql)
            print(f"[OK] TABLE CREATED: {name}")
        except Exception as e:
            print(f"[ERROR] {name}: {e}")
            
    conn.commit()
    conn.close()
    print(f"[COMPLETE] {len(tables)} tables created in {DB_PATH}")

if __name__ == "__main__":
    migrate()
