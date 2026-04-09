import csv
import os

input_file = 're-match-default.csv'
output_dir = 'submissions'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, 1):
        alias = row.get('alias', '').strip()
        filename = f"{alias if alias else f'submission_{i}'}.txt"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, mode='w', encoding='utf-8') as out:
            out.write(f"--- Submission {i} ---\n")
            for key, value in row.items():
                if value: # Only write non-empty fields
                    out.write(f"{key}: {value}\n")
        
        print(f"[WRITE] {filepath}")
