import sys, subprocess, os
sys.stdout.reconfigure(encoding='utf-8')
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

with open('index (2).html', encoding='utf-8') as f:
    c = f.read()

# Simulate opening first POI on load
c_poi = c.replace(
    '</body>',
    '''<script>
      setTimeout(() => {
        const marker = document.querySelector(".leaflet-marker-icon");
        if (marker) marker.click();
      }, 300);
    </script></body>'''
)
test_poi_file = 'test_poi_open.html'
with open(test_poi_file, 'w', encoding='utf-8') as f:
    f.write(c_poi)

ss_mob_poi = os.path.abspath('screenshot_mobile_poi_open.png')
cmd = [edge_path, '--headless=new', f'--screenshot={ss_mob_poi}', '--window-size=390,844', '--disable-gpu', 'file:///' + os.path.abspath(test_poi_file).replace('\\', '/')]
subprocess.run(cmd)

if os.path.exists(test_poi_file): os.remove(test_poi_file)

print('Mobile POI screenshot created!')
