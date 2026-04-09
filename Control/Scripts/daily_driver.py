# daily_driver.py 
import sqlite3 
import os 
from datetime import datetime, date 

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'rve.db') 

def run_daily_briefing(): 
    now = datetime.now() 
    print('=' * 60) 
    print(f'  RVE DAILY BRIEFING | {date.today().isoformat()} | {now.strftime("%H:%M")}') 
    print('=' * 60) 
    conn = sqlite3.connect(DB_PATH) 
    c = conn.cursor() 
    
    print('\n[ATTRIBUTES]') 
    c.execute('SELECT attribute, level, xp_total FROM attribute_log ORDER BY xp_total DESC') 
    for name, lvl, xp in c.fetchall(): 
        bar = '#' * int(min(xp, 100) / 5) 
        print(f'  {name:<20} Lv{lvl} [{bar:<20}] {xp:.2f} XP') 
        
    print('\n[ACTIVE TASKS]') 
    c.execute('SELECT id, title, domain, rve_score FROM tasks WHERE state = "active" ORDER BY rve_score DESC LIMIT 5') 
    for tid, title, dom, score in c.fetchall(): 
        print(f'  [{tid}] {title:<35} | {dom:<15} | Score: {score}') 
        
    conn.close() 
    print('\n' + '=' * 60) 
    print('  [RVE] System Live. Build the vector.') 
    print('=' * 60) 

if __name__ == '__main__': run_daily_briefing()
