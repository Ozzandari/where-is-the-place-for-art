import sys, subprocess, os
sys.stdout.reconfigure(encoding='utf-8')
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

with open('index (2).html', encoding='utf-8') as f:
    c = f.read()

# Replace correctly:
c_man = c.replace('class="fullscreen-modal-overlay" id="manifestoModal"', 'class="fullscreen-modal-overlay open" id="manifestoModal"')
with open('test_man_view.html', 'w', encoding='utf-8') as f:
    f.write(c_man)

ss_man = os.path.abspath('screenshot_manifesto_view.png')
cmd = [edge_path, '--headless=new', f'--screenshot={ss_man}', '--window-size=1280,800', '--disable-gpu', 'file:///' + os.path.abspath('test_man_view.html').replace('\\', '/')]
subprocess.run(cmd)

# Mobile manifesto view
ss_man_mob = os.path.abspath('screenshot_manifesto_view_mobile.png')
cmd_mob = [edge_path, '--headless=new', f'--screenshot={ss_man_mob}', '--window-size=390,844', '--disable-gpu', 'file:///' + os.path.abspath('test_man_view.html').replace('\\', '/')]
subprocess.run(cmd_mob)

# Video view
c_vid = c.replace('class="fullscreen-modal-overlay" id="videoModal"', 'class="fullscreen-modal-overlay open" id="videoModal"')
# Also let's ensure videoGridContainer has content rendered
c_vid = c_vid.replace(
    '<div class="video-grid" id="videoGridContainer">',
    '''<div class="video-grid" id="videoGridContainer">
      <div class="video-item-card">
        <div class="video-item-frame">
          <div style="display:flex;align-items:center;justify-content:center;height:100%;color:#fff;background:#181818;font-size:18px;min-height:220px;">
            ▶️ YouTube Embed Player
          </div>
        </div>
        <div class="video-item-info">
          <h4 class="video-item-title">„სად არის ხელოვნების ადგილი?“ — გორი (ვიდეო 1)</h4>
          <p class="video-item-desc">დოკუმენტური ვიდეო მასალა გამოფენისა და ქალაქის შესახებ</p>
        </div>
      </div>
      <div class="video-item-card">
        <div class="video-item-frame">
          <div style="display:flex;align-items:center;justify-content:center;height:100%;color:#fff;background:#181818;font-size:18px;min-height:220px;">
            ▶️ YouTube Embed Player
          </div>
        </div>
        <div class="video-item-info">
          <h4 class="video-item-title">ურბანული სივრცეები და კონცეფცია (ვიდეო 2)</h4>
          <p class="video-item-desc">ნიკა სომხიშვილი და სოფო ცერცვაძე</p>
        </div>
      </div>'''
)
with open('test_vid_view.html', 'w', encoding='utf-8') as f:
    f.write(c_vid)

ss_vid = os.path.abspath('screenshot_video_view.png')
cmd_vid = [edge_path, '--headless=new', f'--screenshot={ss_vid}', '--window-size=1280,800', '--disable-gpu', 'file:///' + os.path.abspath('test_vid_view.html').replace('\\', '/')]
subprocess.run(cmd_vid)

for p in ['test_man_view.html', 'test_vid_view.html']:
    if os.path.exists(p): os.remove(p)

print('Screenshots generated successfully!')
