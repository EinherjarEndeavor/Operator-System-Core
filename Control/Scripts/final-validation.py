import sqlite3, os, sys

EXPECTED = {
    "rve.db":         18,
    "lifestate.db":   11,
    "arsenal.db":      6,
    "rematch.db":      6,
    "everything.db":   5,
    "errors.db":       4,
    "upgrades.db":     4,
    "supersource.db":  4,
    "wins.db":         3,
    "settings.db":     2,
}

ROOT = r"C:\Users\Tarot\Operator\Control"
all_ok = True

for db, expected in EXPECTED.items():
    path = os.path.join(ROOT, db)
    if not os.path.exists(path):
        print(f"[MISSING ] {db}")
        all_ok = False
        continue
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys = ON")
    tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
    actual = len(tables)
    conn.close()
    status = "OK      " if actual >= expected else "INCOMPLETE"
    flag   = "✓" if actual >= expected else "✗"
    print(f"[{status}] {flag} {db}: {actual} tables (min expected: {expected})")
    if actual < expected:
        all_ok = False

print()
if all_ok:
    print("ALL DATABASES VALID — Phase 3 (Neo4j) is unblocked")
    sys.exit(0)
else:
    print("ONE OR MORE DATABASES INCOMPLETE — review above before proceeding")
    sys.exit(1)