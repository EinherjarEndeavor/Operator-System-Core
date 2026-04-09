import os
import pathlib
DB_PATH = r"C:\Users\tarot\Operator\Control\lifestate.db"
if os.path.exists(DB_PATH):
    try:
        os.remove(DB_PATH)
        print(f"Purged stale database at {DB_PATH}")
    except Exception as e:
        print(f"Warning: Could not remove {DB_PATH}: {e}")
