# quest_engine.py 
# RVE Quest & Mission Engine 
import sqlite3 
import argparse 
import os 
from datetime import datetime 

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'rve.db') 

def create_quest(title, domain, quest_type, xp_reward, deadline=None, notes=''): 
    conn = sqlite3.connect(DB_PATH) 
    c = conn.cursor() 
    now = datetime.utcnow().isoformat() 
    c.execute('''INSERT INTO tasks (title, domain, type, urgency, impact, friction, state, due_date, notes, created) 
                 VALUES (?, ?, ?, 5, 5, 5, 'active', ?, ?, ?)''', (title, domain, quest_type, deadline, notes, now)) 
    quest_id = c.lastrowid 
    conn.commit() 
    conn.close() 
    print(f'[OK] Quest created: ID={quest_id} | {title} [{quest_type}] +{xp_reward}xp') 
    return quest_id 

def list_quests(status='active'): 
    conn = sqlite3.connect(DB_PATH) 
    c = conn.cursor() 
    c.execute('SELECT id, title, domain, type, due_date FROM tasks WHERE state = ?', (status,)) 
    rows = c.fetchall() 
    conn.close() 
    print(f'\n=== QUESTS ({status}) ===') 
    for qid, title, domain, qtype, deadline in rows: 
        dl = f' | due: {deadline}' if deadline else '' 
        print(f'  [{qid}] {title:<30} [{qtype:<7}] [{domain:<15}]{dl}') 
    print() 

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='RVE Quest Engine') 
    parser.add_argument('--create', nargs='+', help='Create quest: TITLE DOMAIN TYPE XP_REWARD [DEADLINE] [NOTES]') 
    parser.add_argument('--list', metavar='STATUS', nargs='?', const='active', help='List quests') 
    args = parser.parse_args() 
    if args.create: 
        parts = args.create 
        if len(parts) < 4: print('[ERROR] Usage: --create TITLE DOMAIN TYPE XP [DEADLINE] [NOTES]') 
        else: 
            title, domain, qtype, xp = parts[0], parts[1], parts[2], int(parts[3]) 
            deadline = parts[4] if len(parts) > 4 else None 
            notes = parts[5] if len(parts) > 5 else '' 
            create_quest(title, domain, qtype, xp, deadline, notes) 
    else: list_quests()
