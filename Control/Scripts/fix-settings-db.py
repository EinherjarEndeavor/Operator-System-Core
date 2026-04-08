import sqlite3
from datetime import datetime, timezone

DB = r"C:\Users\Tarot\Operator\Control\settings.db"
NOW = datetime.now(timezone.utc).isoformat()

conn = sqlite3.connect(DB)
conn.execute("PRAGMA journal_mode=WAL")

conn.execute("""
CREATE TABLE IF NOT EXISTS toggles (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL DEFAULT 'true',
  description TEXT,
  updated_at TEXT
)""")

TOGGLES = [
  ("memory_enabled",             "true",  "Global memory persistence across sessions"),
  ("auto_snapshot",              "true",  "Auto-snapshot before destructive operations"),
  ("auto_neo4j_write",           "true",  "Mirror key facts to Neo4j automatically"),
  ("auto_everything_log",        "true",  "Log all AI actions to everything.db"),
  ("recovery_mode",              "false", "Activate recovery scoring preset"),
  ("proactive_pattern_detect",   "true",  "Auto-detect behavioral patterns from sessions"),
  ("delta_review_required",      "true",  "Require user review before applying deltas"),
  ("context_handover_enabled",   "true",  "Trigger handover protocol at 80% context"),
  ("journaling_enabled",         "true",  "Prompt for journal at session end"),
  ("rve_auto_score",             "true",  "Auto-calculate RVE score on task creation"),
  ("obsidian_sync",              "false", "Sync session notes to Obsidian vault"),
  ("github_sync",                "false", "Sync project files to GitHub"),
  ("notion_sync",                "false", "Sync tasks/projects to Notion"),
  ("verbose_logging",            "false", "Extra verbose action logging"),
  ("strict_write_doctrine",      "true",  "Enforce write-to-tmp-first rule"),
  ("sobriety_anchor_active",     "true",  "Surface sobriety anchor in daily context"),
  ("show_rve_score_in_output",   "true",  "Display RVE scores in task output"),
  ("allow_inference_promotion",  "true",  "Allow AI to promote inferences to facts"),
  ("mcp_neo4j_enabled",          "true",  "Use Neo4j MCP server for graph operations"),
  ("auto_win_detect",            "true",  "Auto-detect wins from completion events"),
]

conn.executemany(
  "INSERT OR REPLACE INTO toggles (key,value,description,updated_at) VALUES (?,?,?,?)",
  [(k,v,d,NOW) for k,v,d in TOGGLES]
)
conn.commit()

count = conn.execute("SELECT COUNT(*) FROM toggles").fetchone()[0]
print(f"[OK] settings.db toggles: {count}/20")
for row in conn.execute("SELECT key,value FROM toggles ORDER BY key"):
  print(f"  {row[0]} = {row[1]}")

conn.close()
if count < 20:
  print(f"[WARN] Expected 20 toggles, got {count}")
else:
  print("[OK] All 20 toggles confirmed")
