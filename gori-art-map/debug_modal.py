import sys, subprocess, os
sys.stdout.reconfigure(encoding='utf-8')

with open('index (2).html', encoding='utf-8') as f:
    text = f.read()

# Let's check where manifestoModal is placed:
idx = text.find('id="manifestoModal"')
print('Position of manifestoModal:', idx)
print('Before it:', repr(text[idx-200:idx]))

# Let's check why .fullscreen-modal-overlay.open might be hidden or overridden
idx_css = text.find('.fullscreen-modal-overlay')
print('CSS .fullscreen-modal-overlay:', text[idx_css:idx_css+400])
