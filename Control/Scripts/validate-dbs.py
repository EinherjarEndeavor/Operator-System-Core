import sqlite3
import os

DB_DIR = r"C:\Users\tarot\operator\Control"
dbs = [f for f in os.listdir(DB_DIR) if f.endswith(".db")]

for db in dbs:
    print(f"--- {db} ---")
    path = os.path.join(DB_DIR, db)
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [t[0] for t in cursor.fetchall()]
        print(f"TABLES: {tables}")
        conn.close()
    except Exception as e:
        print(f"FAILED: {e}")
