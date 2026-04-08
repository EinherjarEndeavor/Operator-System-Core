import sqlite3, pathlib, os

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
                category        TEXT NOT NULL,
                recurrence      TEXT NOT NULL,
                days_of_week    TEXT,
                time_of_day     TEXT,
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
                obsidian_path   TEXT,
                gcal_event_id   TEXT,
                conflicts_with  TEXT,
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
                address         TEXT,
                phone           TEXT,
                notes           TEXT
            )
        """,
        "locations": """
            CREATE TABLE IF NOT EXISTS locations (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                address         TEXT,
                lat             REAL,
                lon             REAL,
                notes           TEXT
            )
        """,
        "credentials": """
            CREATE TABLE IF NOT EXISTS credentials (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                type            TEXT,
                status          TEXT,
                expiry          TEXT,
                notes           TEXT
            )
        """,
        "devices": """
            CREATE TABLE IF NOT EXISTS devices (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                type            TEXT,
                specs           TEXT,
                status          TEXT,
                needs_return    INTEGER DEFAULT 0,
                notes           TEXT
            )
        """,
        "subscriptions": """
            CREATE TABLE IF NOT EXISTS subscriptions (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                cost            REAL DEFAULT 0,
                expiry          TEXT,
                status          TEXT,
                notes           TEXT
            )
        """,
        "supplements": """
            CREATE TABLE IF NOT EXISTS supplements (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                dosage          TEXT,
                timing          TEXT,
                stock_level     TEXT,
                notes           TEXT
            )
        """,
        "medications": """
            CREATE TABLE IF NOT EXISTS medications (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                dosage          TEXT,
                timing          TEXT,
                refill_cadence  TEXT,
                notes           TEXT
            )
        """,
        "financial_state": """
            CREATE TABLE IF NOT EXISTS financial_state (
                id              TEXT PRIMARY KEY DEFAULT 'singleton',
                income          REAL DEFAULT 0,
                fixed_costs     REAL DEFAULT 0,
                ebt_amount      REAL DEFAULT 0,
                notes           TEXT,
                updated         TEXT
            )
        """,
        "income_opportunities": """
            CREATE TABLE IF NOT EXISTS income_opportunities (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                potential       REAL,
                deadline        TEXT,
                conflicts_with  TEXT,
                status          TEXT,
                notes           TEXT
            )
        """,
        "hobbies": """
            CREATE TABLE IF NOT EXISTS hobbies (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                last_practiced  TEXT,
                attribute_tag   TEXT,
                notes           TEXT
            )
        """,
        "values": """
            CREATE TABLE IF NOT EXISTS values_hierarchy (
                id              TEXT PRIMARY KEY,
                value           TEXT NOT NULL,
                derived_behavior TEXT,
                notes           TEXT
            )
        """,
        "identity_axioms": """
            CREATE TABLE IF NOT EXISTS identity_axioms (
                id              TEXT PRIMARY KEY,
                axiom           TEXT NOT NULL,
                derived_behavior TEXT,
                notes           TEXT
            )
        """,
        "non_negotiables": """
            CREATE TABLE IF NOT EXISTS non_negotiables (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL,
                period          TEXT DEFAULT '90-day',
                last_touched    TEXT,
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
            cur.execute(sql)
            print(f"[OK] TABLE CREATED: {name}")
        except Exception as e:
            print(f"[ERROR] {name}: {e}")
            
    conn.commit()
    conn.close()
    print(f"[COMPLETE] 24 tables created in {DB_PATH}")

if __name__ == "__main__":
    migrate()
