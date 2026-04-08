import sqlite3
con = sqlite3.connect("C:/Users/tarot/Operator/Control/lifestate.db")
tables = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print(f"Tables created: {len(tables)}")
for t in tables:
    print(f"  {t[0]}")
con.close()
