import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index (2).backup.html', encoding='utf-8', errors='replace') as f:
    html = f.read()

print('Original length:', len(html))

# 1. Remove filter chips from HTML
# Pattern: <nav class="filter-chips" id="filterChips" ... </nav>
html = re.sub(
    r'<nav class="filter-chips" id="filterChips"[^>]*>.*?</nav>',
    '',
    html,
    flags=re.DOTALL
)

# 2. In .action-pills-row, remove openTraceModalBtn
html = re.sub(
    r'<button class="action-pill trace-pill" id="openTraceModalBtn"[^>]*>.*?</button>',
    '',
    html,
    flags=re.DOTALL
)

# 3. In .search-wrapper, remove openManifestoBtn (since manifesto is now at bottom center)
html = re.sub(
    r'<button class="manifesto-trigger-btn" id="openManifestoBtn"[^>]*>.*?</button>',
    '',
    html,
    flags=re.DOTALL
)

# 4. Remove citizen trace modal (#traceModal), mapPickBanner, Netlify form, tracePhotoContainer
html = re.sub(
    r'<div class="map-pick-banner" id="mapPickBanner">.*?</div>\s*</div>', # handle carefully
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'<div class="map-pick-banner" id="mapPickBanner">.*?</div>',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'<div class="modal-overlay" id="traceModal"[^>]*>.*?</div>\s*</div>\s*</div>',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'<form name="art-traces"[^>]*>.*?</form>',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'<div id="tracePhotoContainer" class="trace-photo-container"[^>]*>.*?</div>',
    '',
    html,
    flags=re.DOTALL
)

print('After removing trace HTML, length:', len(html))
