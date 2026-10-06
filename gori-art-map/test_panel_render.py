import sys, subprocess, os
sys.stdout.reconfigure(encoding='utf-8')
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

with open('index (2).html', encoding='utf-8') as f:
    c = f.read()

# Make panel open by default and populate some text
c_panel = c.replace(
    '<body>',
    '<body class="panel-open">'
)
c_panel = c_panel.replace(
    'id="pName"></span>',
    'id="pName">იოსებ სტალინის სახელმწიფო მუზეუმი</span>'
)
c_panel = c_panel.replace(
    'id="pAnswer"></h2>',
    'id="pAnswer">სტალინის მუზეუმში?</h2>'
)

test_file = 'test_panel_open.html'
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(c_panel)

ss = os.path.abspath('screenshot_mobile_panel_view.png')
cmd = [edge_path, '--headless=new', f'--screenshot={ss}', '--window-size=390,844', '--disable-gpu', 'file:///' + os.path.abspath(test_file).replace('\\', '/')]
subprocess.run(cmd)

if os.path.exists(test_file): os.remove(test_file)

print('Mobile Panel screenshot created!')
