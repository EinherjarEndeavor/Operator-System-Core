# setup.py 
import sqlite3 
import os 
import csv 
from datetime import datetime 

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'rve.db') 
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

print(f'[WRITE] {DB_PATH}') 
conn = sqlite3.connect(DB_PATH) 
c = conn.cursor() 

# --- PROFILE --- 
c.execute('''CREATE TABLE IF NOT EXISTS profile (key TEXT PRIMARY KEY, value TEXT, updated_at TEXT)''') 
# --- DOMAINS --- 
c.execute('''CREATE TABLE IF NOT EXISTS domains (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, color_code TEXT, active INTEGER DEFAULT 1)''') 
# --- PROJECTS --- 
c.execute('''CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, domain_id INTEGER, initiative TEXT, status TEXT DEFAULT 'active', stage TEXT, description TEXT, goal TEXT, created TEXT DEFAULT CURRENT_TIMESTAMP, updated TEXT DEFAULT CURRENT_TIMESTAMP)''') 
# --- TASKS --- 
c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, domain_id INTEGER, project_id INTEGER, onboarded INTEGER DEFAULT 0, state TEXT DEFAULT 'active', mandatory INTEGER DEFAULT 0, fixed INTEGER DEFAULT 0, due TEXT, duration_est_min INTEGER DEFAULT 30, energy_type TEXT DEFAULT 'medium', location TEXT, urgency REAL DEFAULT 5, impact REAL DEFAULT 5, cascade_val REAL DEFAULT 5, compound_val REAL DEFAULT 5, friction REAL DEFAULT 5, immediate_benefit REAL DEFAULT 5, atomic INTEGER DEFAULT 1, contact TEXT, website TEXT, action_plan TEXT, if_then_plan TEXT, estimated_fields INTEGER DEFAULT 0, postpone_count INTEGER DEFAULT 0, notes TEXT, created TEXT DEFAULT CURRENT_TIMESTAMP, completed_at TEXT, actual_duration_min INTEGER, actual_difficulty REAL, actual_energy_used TEXT, completion_notes TEXT, complexity TEXT, obsidian_path TEXT, rve_score REAL, tags TEXT, legal_safe INTEGER DEFAULT 1, cost_required REAL DEFAULT 0, attribute_tag TEXT)''') 
# --- OBLIGATIONS --- 
c.execute('''CREATE TABLE IF NOT EXISTS obligations (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, domain_id INTEGER, frequency TEXT, day_of_week TEXT, time_of_day TEXT, location TEXT, contact TEXT, notes TEXT, active INTEGER DEFAULT 1, criticality TEXT DEFAULT 'medium')''') 
# --- HABITS --- 
c.execute('''CREATE TABLE IF NOT EXISTS habits (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, type TEXT, trigger TEXT, action TEXT, target_attribute TEXT, difficulty TEXT DEFAULT 'medium', stage TEXT DEFAULT 'building', streak_current INTEGER DEFAULT 0, streak_best INTEGER DEFAULT 0, streak_paused INTEGER DEFAULT 0, last_completed TEXT, last_missed TEXT, total_completions INTEGER DEFAULT 0, xp_per_completion INTEGER DEFAULT 10, active INTEGER DEFAULT 1, notes TEXT, attribute_tag TEXT, complexity TEXT, obsidian_path TEXT)''') 
# --- HABIT LOG --- 
c.execute('''CREATE TABLE IF NOT EXISTS habit_log (id INTEGER PRIMARY KEY AUTOINCREMENT, habit_id INTEGER, date TEXT, time TEXT, completed INTEGER, energy TEXT, streak_at INTEGER, xp_earned REAL, notes TEXT)''') 
# --- IDEAS --- 
c.execute('''CREATE TABLE IF NOT EXISTS ideas (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, domain_id INTEGER, stage TEXT DEFAULT 'raw', why TEXT, notes TEXT, created TEXT DEFAULT CURRENT_TIMESTAMP, updated TEXT DEFAULT CURRENT_TIMESTAMP, potential REAL DEFAULT 5, effort REAL DEFAULT 5)''') 
# --- SCHEDULE ANCHORS --- 
c.execute('''CREATE TABLE IF NOT EXISTS schedule_anchors (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, domain_id INTEGER, week TEXT, day_of_week TEXT, start_time TEXT, end_time TEXT, location TEXT, recurs INTEGER DEFAULT 0, active INTEGER DEFAULT 1)''') 
# --- IF THEN PLANS --- 
c.execute('''CREATE TABLE IF NOT EXISTS if_then_plans (id INTEGER PRIMARY KEY AUTOINCREMENT, cue TEXT, response TEXT, domain_id INTEGER, linked_task_id INTEGER, active INTEGER DEFAULT 1, notes TEXT)''') 
# --- EXERCISES --- 
c.execute('''CREATE TABLE IF NOT EXISTS exercises (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, muscle_group TEXT, secondary_muscles TEXT, movement_type TEXT, compound INTEGER DEFAULT 0, equipment TEXT, intensity TEXT, duration_typical_min INTEGER, notes TEXT)''') 
# --- JOURNAL ENTRIES --- 
c.execute('''CREATE TABLE IF NOT EXISTS journal_entries (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, type TEXT, filepath TEXT, tags TEXT, mood REAL, energy TEXT, created TEXT DEFAULT CURRENT_TIMESTAMP)''') 
# --- COMPLETIONS --- 
c.execute('''CREATE TABLE IF NOT EXISTS completions (id INTEGER PRIMARY KEY AUTOINCREMENT, task_id INTEGER, completed_at TEXT, actual_duration_min INTEGER, actual_difficulty REAL, actual_energy_used TEXT, notes TEXT, ideas_spawned TEXT)''') 
# --- WINS --- 
c.execute('''CREATE TABLE IF NOT EXISTS wins (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, domain TEXT, category TEXT, date TEXT, description TEXT, xp_earned REAL, attribute_tag TEXT)''') 
# --- ATTRIBUTE LOG --- 
c.execute('''CREATE TABLE IF NOT EXISTS attribute_log (id INTEGER PRIMARY KEY AUTOINCREMENT, attribute TEXT, level INTEGER DEFAULT 1, xp_total REAL DEFAULT 0, xp_to_next REAL DEFAULT 100, last_updated TEXT DEFAULT CURRENT_TIMESTAMP, notes TEXT)''') 
# --- SKILL LOG --- 
c.execute('''CREATE TABLE IF NOT EXISTS skill_log (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, domain TEXT, level INTEGER DEFAULT 1, xp_total REAL DEFAULT 0, last_practiced TEXT, linked_habit_id INTEGER, attribute_tag TEXT, notes TEXT)''') 
# --- WEEKLY REVIEWS --- 
c.execute('''CREATE TABLE IF NOT EXISTS weekly_reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, week_start TEXT, week_end TEXT, tasks_completed INTEGER, tasks_planned INTEGER, habits_data TEXT, xp_gained REAL, non_negotiables_status TEXT, flags TEXT, notes TEXT, created TEXT DEFAULT CURRENT_TIMESTAMP)''') 
# --- CAPTURES --- 
c.execute('''CREATE TABLE IF NOT EXISTS captures (id INTEGER PRIMARY KEY AUTOINCREMENT, raw_text TEXT, source TEXT, created TEXT DEFAULT CURRENT_TIMESTAMP, processed INTEGER DEFAULT 0, processed_task_id INTEGER)''') 

# SEED DOMAINS 
domains = [('school', '#4A90D9'), ('recovery', '#27AE60'), ('legal_admin', '#E74C3C'), ('health_fitness', '#F39C12'), ('career', '#8E44AD'), ('coding_tech', '#16A085'), ('creative', '#D35400'), ('relationships', '#C0392B'), ('finances', '#2ECC71'), ('housing', '#7F8C8D')] 
for name, color in domains: c.execute('INSERT OR IGNORE INTO domains (name, color_code) VALUES (?, ?)', (name, color)) 

# SEED ATTRIBUTES 
attributes = ['strength','agility','endurance','cognition','creativity','social','technical','recovery_capital','tactical'] 
for attr in attributes: c.execute('INSERT OR IGNORE INTO attribute_log (attribute) VALUES (?)', (attr,)) 

conn.commit() 
conn.close() 
print('[DONE] setup.py complete')
