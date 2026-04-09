# score.py 
# RVE Attribute Scoring Engine 
import sqlite3 
import argparse 
import os
from datetime import datetime 

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'rve.db') 
ATTRIBUTE_LIST = ['strength', 'agility', 'endurance', 'cognition', 'creativity', 'social', 'technical', 'recovery_capital', 'tactical'] 

def log_score(attribute, delta, reason='manual', session_id=None): 
    conn = sqlite3.connect(DB_PATH) 
    c = conn.cursor() 
    now = datetime.utcnow().isoformat() 
    c.execute('SELECT xp_total FROM attribute_log WHERE attribute = ?', (attribute,)) 
    row = c.fetchone() 
    if not row: 
        print(f'[ERROR] Attribute not found: {attribute}') 
        conn.close() 
        return 
    old_value = row[0] 
    new_value = round(old_value + delta, 4) 
    c.execute('UPDATE attribute_log SET xp_total = ?, last_updated = ? WHERE attribute = ?', (new_value, now, attribute)) 
    conn.commit() 
    conn.close() 
    print(f'[OK] {attribute}: {old_value} -> {new_value} (delta={delta}, reason={reason})') 

def show_scores(): 
    conn = sqlite3.connect(DB_PATH) 
    c = conn.cursor() 
    c.execute('SELECT attribute, xp_total, last_updated FROM attribute_log ORDER BY attribute') 
    rows = c.fetchall() 
    conn.close() 
    print('\n=== RVE ATTRIBUTE SCORES ===') 
    for name, value, updated in rows: 
        bar = '#' * int(min(value, 100) / 5) 
        print(f'  {name:<20} {value:>6.2f}  [{bar:<20}]  (updated: {updated})') 
    print() 

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='RVE Score Engine') 
    parser.add_argument('--show', action='store_true', help='Show all attribute scores') 
    parser.add_argument('--log', nargs=3, metavar=('ATTRIBUTE', 'DELTA', 'REASON'), help='Log a score delta: attribute delta reason') 
    args = parser.parse_args() 
    if args.show: show_scores() 
    elif args.log: 
        attr, delta, reason = args.log 
        if attr not in ATTRIBUTE_LIST: print(f'[ERROR] Unknown attribute: {attr}') 
        else: log_score(attr, float(delta), reason) 
    else: show_scores()
