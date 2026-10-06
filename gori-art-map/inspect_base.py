import sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'C:\Users\artho\.gemini\antigravity\scratch\gori-art-map\index (2).html'
with open(p, encoding='utf-8', errors='replace') as f:
    text = f.read()

idx = text.find('<aside class="panel"')
idx2 = text.find('<script', idx)
print("=== HTML BETWEEN ASIDE AND SCRIPT ===")
print(text[idx:idx2])
