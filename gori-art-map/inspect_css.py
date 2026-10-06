import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index (2).backup.html', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

print("Lines count:", len(lines))
print(''.join(lines[2695:2735]))
print("...")
print(''.join(lines[-40:]))
