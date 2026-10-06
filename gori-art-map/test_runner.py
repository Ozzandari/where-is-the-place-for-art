import sys, subprocess, os, time, json, urllib.request

sys.stdout.reconfigure(encoding='utf-8')
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_file = 'file:///' + os.path.abspath('index (2).html').replace('\\', '/')

# 1. First test: dump DOM to see if markers and buttons are present
cmd = [edge_path, '--headless=new', '--dump-dom', '--disable-gpu', html_file]
res = subprocess.run(cmd, capture_output=True)
dom = res.stdout.decode('utf-8', errors='replace')
print('DOM length:', len(dom))
print('Has bottom-action-bar:', 'bottom-action-bar' in dom)
print('Has bottomManifestoBtn:', 'bottomManifestoBtn' in dom)
print('Has bottomVideoBtn:', 'bottomVideoBtn' in dom)
print('Has manifestoModal:', 'manifestoModal' in dom)
print('Has videoModal:', 'videoModal' in dom)
print('Has filterChips:', 'filterChips' in dom)
print('Has openTraceModalBtn:', 'openTraceModalBtn' in dom)
print('Leaflet markers in DOM:', dom.count('leaflet-marker-icon'))
print('Leaflet tiles/canvas in DOM:', dom.count('leaflet-tile') + dom.count('maplibregl-canvas'))

# 2. Take desktop screenshot
ss_desktop = os.path.abspath('screenshot_desktop.png')
cmd_ss = [edge_path, '--headless=new', f'--screenshot={ss_desktop}', '--window-size=1280,800', '--disable-gpu', html_file]
subprocess.run(cmd_ss)
print('Desktop screenshot size:', os.path.getsize(ss_desktop) if os.path.exists(ss_desktop) else 0)

# 3. Take mobile screenshot
ss_mobile = os.path.abspath('screenshot_mobile.png')
cmd_ss_mob = [edge_path, '--headless=new', f'--screenshot={ss_mobile}', '--window-size=390,844', '--disable-gpu', html_file]
subprocess.run(cmd_ss_mob)
print('Mobile screenshot size:', os.path.getsize(ss_mobile) if os.path.exists(ss_mobile) else 0)
