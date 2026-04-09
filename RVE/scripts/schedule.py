# schedule.py 
import sqlite3 
import argparse 
import os
from datetime import datetime, date 

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'rve.db') 

def show_schedule(): 
    print(f'\n=== SCHEDULE: {date.today().isoformat()} ===') 
    conn = sqlite3.connect(DB_PATH) 
    c = conn.cursor() 
    c.execute('SELECT start_time, end_time, domain_id, title FROM schedule_anchors WHERE active = 1 ORDER BY start_time ASC') 
    rows = c.fetchall() 
    if not rows: print('  (no anchors scheduled)') 
    else: 
        for start, end, dom, title in rows: print(f'  {start}-{end} | [{dom}] {title}') 
    conn.close() 
    print() 

if __name__ == '__main__': show_schedule()
