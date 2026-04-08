import sqlite3
conn = sqlite3.connect(r"C:\Users\Tarot\Operator\Control\settings.db")
conn.execute("PRAGMA foreign_keys = ON")
tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
print("TABLES:", tables)
try:
    cols = [r[1] for r in conn.execute("PRAGMA table_info(toggles)").fetchall()]
    print("TOGGLE COLUMNS:", cols)
    count = conn.execute("SELECT COUNT(*) FROM toggles").fetchone()[0]
    print("TOGGLE_COUNT:", count)
    if count > 0:
        rows = conn.execute("SELECT key, value, description FROM toggles LIMIT 10").fetchall()
        for row in rows:
            print(f"  TOGGLE: {row[0]} = {row[1]}  | {row[2]}")
    else:
        print("WARNING: toggles table is empty — settings.db needs seeding")
except Exception as e:
    print("ERROR:", e)
conn.close()