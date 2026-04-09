import sys
with open('Pickle Rick - Read this.md', 'r', encoding='utf-8') as f_in, open('wrapped.txt', 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.rstrip('\n')
        if len(line) > 150:
            for i in range(0, len(line), 150):
                f_out.write(line[i:i+150] + '\n')
        else:
            f_out.write(line + '\n')
