import sys, subprocess, os, time

sys.stdout.reconfigure(encoding='utf-8')
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Let's test by creating a tiny script that simulates click on manifesto and videos
test_html_manifesto = 'test_manifesto_open.html'
with open('index (2).html', encoding='utf-8') as f:
    c = f.read()

# Auto-open manifesto on load
c_man = c.replace('</body>', '<script>setTimeout(() => { document.getElementById("bottomManifestoBtn").click(); }, 300);</script></body>')
with open(test_html_manifesto, 'w', encoding='utf-8') as f:
    f.write(c_man)

ss_man = os.path.abspath('screenshot_manifesto_modal.png')
cmd = [edge_path, '--headless=new', f'--screenshot={ss_man}', '--window-size=1280,800', '--disable-gpu', 'file:///' + os.path.abspath(test_html_manifesto).replace('\\', '/')]
subprocess.run(cmd)
print('Manifesto screenshot size:', os.path.getsize(ss_man) if os.path.exists(ss_man) else 0)

# Auto-open videos on load
test_html_video = 'test_video_open.html'
c_vid = c.replace('</body>', '<script>setTimeout(() => { document.getElementById("bottomVideoBtn").click(); }, 300);</script></body>')
with open(test_html_video, 'w', encoding='utf-8') as f:
    f.write(c_vid)

ss_vid = os.path.abspath('screenshot_video_modal.png')
cmd2 = [edge_path, '--headless=new', f'--screenshot={ss_vid}', '--window-size=1280,800', '--disable-gpu', 'file:///' + os.path.abspath(test_html_video).replace('\\', '/')]
subprocess.run(cmd2)
print('Video screenshot size:', os.path.getsize(ss_vid) if os.path.exists(ss_vid) else 0)

# Clean up temporary test files
for p in [test_html_manifesto, test_html_video]:
    if os.path.exists(p): os.remove(p)
