import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index (2).backup.html', encoding='utf-8', errors='replace') as f:
    text = f.read()

# -------------------------------------------------------------
# 1. Update CSS in <style>
# -------------------------------------------------------------
extra_css = """
    /* --- Fixed Bottom Action Bar (Manifesto & Videos) --- */
    .bottom-action-bar {
      position: fixed;
      bottom: max(16px, env(safe-area-inset-bottom, 16px));
      left: 50%;
      transform: translateX(-50%);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(18, 18, 18, 0.92);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      padding: 6px 12px;
      border-radius: 999px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.15);
      pointer-events: auto;
      transition: opacity 0.25s ease, transform 0.25s ease;
    }

    body.panel-open .bottom-action-bar {
      opacity: 0;
      pointer-events: none;
      transform: translate(-50%, 25px);
    }

    .bottom-bar-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: transparent;
      color: #ffffff;
      border: none;
      border-radius: 999px;
      padding: 9px 18px;
      font-family: var(--font);
      font-size: 14.5px;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s ease, transform 0.15s ease, color 0.2s ease;
      -webkit-tap-highlight-color: transparent;
      touch-action: manipulation;
    }

    .bottom-bar-btn:hover {
      background: rgba(255, 255, 255, 0.15);
      transform: translateY(-1px);
    }

    .bottom-bar-btn:active {
      transform: translateY(1px);
      background: rgba(255, 255, 255, 0.25);
    }

    .bottom-bar-btn svg {
      flex-shrink: 0;
      color: var(--brand-rose);
      transition: transform 0.2s ease;
    }

    .bottom-bar-btn:hover svg {
      transform: scale(1.1);
    }

    .bottom-bar-btn.manifesto-btn {
      background: rgba(200, 106, 118, 0.22);
      border: 1px solid rgba(200, 106, 118, 0.4);
    }
    .bottom-bar-btn.manifesto-btn:hover {
      background: rgba(200, 106, 118, 0.38);
    }

    /* --- Fullscreen Modal Cards (Manifesto & Video Gallery) --- */
    .fullscreen-modal-overlay {
      position: fixed;
      inset: 0;
      z-index: 2000;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.28s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .fullscreen-modal-overlay.open {
      opacity: 1;
      pointer-events: auto;
    }

    .fullscreen-modal-backdrop {
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.72);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }

    .fullscreen-modal-card {
      position: relative;
      background: #ffffff;
      width: min(820px, calc(100vw - 28px));
      max-height: calc(100vh - 40px);
      max-height: calc(100dvh - 40px);
      border-radius: 20px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.45);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      z-index: 2;
      transform: translateY(20px) scale(0.98);
      transition: transform 0.28s cubic-bezier(0.2, 0.9, 0.3, 1);
    }

    .fullscreen-modal-overlay.open .fullscreen-modal-card {
      transform: translateY(0) scale(1);
    }

    .fullscreen-modal-header {
      position: sticky;
      top: 0;
      background: #ffffff;
      border-bottom: 1px solid var(--line);
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 10;
    }

    .fullscreen-modal-title-wrap {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .modal-tag-badge {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      padding: 3px 8px;
      border-radius: 999px;
      background: var(--brand-rose-light);
      color: var(--brand-rose-dark);
      border: 1px solid var(--brand-rose-border);
    }

    .fullscreen-modal-title {
      margin: 0;
      font-size: 18px;
      font-weight: 700;
      color: var(--ink);
    }

    .fullscreen-close-btn {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: #f0f0f0;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #333333;
      transition: background 0.15s ease, transform 0.15s ease, color 0.15s ease;
      touch-action: manipulation;
      -webkit-tap-highlight-color: transparent;
      padding: 0;
      flex-shrink: 0;
    }

    .fullscreen-close-btn:hover {
      background: var(--brand-rose);
      color: #ffffff;
      transform: scale(1.05);
    }

    .fullscreen-close-btn:active {
      transform: scale(0.95);
    }

    .fullscreen-modal-scroll {
      padding: 24px 28px 36px 28px;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      color: var(--ink);
      line-height: 1.8;
      font-size: 15.5px;
    }

    /* Manifesto specific text styling */
    .manifesto-lead-question {
      font-size: 24px;
      font-weight: 800;
      color: var(--brand-rose-dark);
      margin: 0 0 16px 0;
      line-height: 1.3;
    }

    .manifesto-paragraph {
      margin: 0 0 18px 0;
      color: #2a2a2a;
      text-align: justify;
    }

    .manifesto-invite-highlight {
      background: #faf6f7;
      border-left: 4px solid var(--brand-rose);
      padding: 16px 20px;
      border-radius: 0 12px 12px 0;
      margin: 24px 0 20px 0;
      font-weight: 500;
      line-height: 1.8;
      color: var(--ink);
    }

    .manifesto-sign-off {
      margin-top: 24px;
      padding-top: 16px;
      border-top: 1px dashed var(--line);
      font-size: 14px;
      color: #555555;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .manifesto-sign-off strong {
      color: var(--ink);
      font-size: 15px;
    }

    /* Videos gallery styling */
    .video-grid {
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    .video-item-card {
      background: #fafafa;
      border: 1px solid var(--line);
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .video-item-card:hover {
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }

    .video-item-frame {
      position: relative;
      width: 100%;
      padding-top: 56.25%; /* 16:9 ratio */
      background: #000000;
    }

    .video-item-frame iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: none;
    }

    .video-item-info {
      padding: 14px 18px;
      background: #ffffff;
    }

    .video-item-title {
      margin: 0 0 4px 0;
      font-size: 16px;
      font-weight: 700;
      color: var(--ink);
    }

    .video-item-desc {
      margin: 0;
      font-size: 13.5px;
      color: #666666;
    }

    /* Mobile panel close button improvements */
    .hero-close-btn {
      touch-action: manipulation;
      -webkit-tap-highlight-color: transparent;
      width: 36px;
      height: 36px;
    }

    @media (max-width: 720px) {
      .fullscreen-modal-card {
        width: 100vw;
        height: 100vh;
        height: 100dvh;
        max-height: 100dvh;
        border-radius: 0;
      }
      .fullscreen-modal-scroll {
        padding: 18px 18px 80px 18px;
        font-size: 15px;
      }
      .manifesto-lead-question {
        font-size: 20px;
      }
      .bottom-action-bar {
        bottom: max(14px, env(safe-area-inset-bottom, 14px));
        padding: 5px 10px;
        gap: 6px;
      }
      .bottom-bar-btn {
        padding: 8px 14px;
        font-size: 13.5px;
      }
    }
"""

# Inject extra CSS before </style>
text = text.replace('</style>', extra_css + '\n  </style>')

# -------------------------------------------------------------
# 2. Update HTML Controls
# -------------------------------------------------------------

# Remove manifesto button from search wrapper
text = re.sub(
    r'<button class="manifesto-trigger-btn" id="openManifestoBtn"[^>]*>.*?</button>',
    '',
    text,
    flags=re.DOTALL
)

# Update search placeholder to "მოძებნე ადგილი გორში..."
text = text.replace('placeholder="მოძებნე ადგილი ან კატეგორია..."', 'placeholder="მოძებნე ადგილი გორში..."')

# Remove citizen trace button from action pills
text = re.sub(
    r'<button class="action-pill trace-pill" id="openTraceModalBtn"[^>]*>.*?</button>',
    '',
    text,
    flags=re.DOTALL
)

# Remove filter chips
text = re.sub(
    r'<nav class="filter-chips" id="filterChips"[^>]*>.*?</nav>',
    '',
    text,
    flags=re.DOTALL
)

# Remove mapPickBanner, traceModal, form[name="art-traces"], tracePhotoContainer
text = re.sub(
    r'<div class="map-pick-banner" id="mapPickBanner">.*?</div>\s*</div>',
    '',
    text,
    flags=re.DOTALL
)
text = re.sub(
    r'<div class="map-pick-banner" id="mapPickBanner">.*?</div>',
    '',
    text,
    flags=re.DOTALL
)
text = re.sub(
    r'<div class="modal-overlay" id="traceModal"[^>]*>.*?</div>\s*</div>\s*</div>',
    '',
    text,
    flags=re.DOTALL
)
text = re.sub(
    r'<form name="art-traces"[^>]*>.*?</form>',
    '',
    text,
    flags=re.DOTALL
)
text = re.sub(
    r'<div id="tracePhotoContainer" class="trace-photo-container"[^>]*>.*?</div>',
    '',
    text,
    flags=re.DOTALL
)

# Add Bottom Action Bar and Modals before <script
new_html_components = """
  <!-- Fixed Bottom Center Bar: Manifesto & Videos -->
  <div class="bottom-action-bar" id="bottomActionBar">
    <button class="bottom-bar-btn manifesto-btn" id="bottomManifestoBtn" type="button" aria-label="მანიფესტის გახსნა">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
      </svg>
      <span>მანიფესტი</span>
    </button>
    <button class="bottom-bar-btn" id="bottomVideoBtn" type="button" aria-label="ვიდეოების გახსნა">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M8 5v14l11-7z"/>
      </svg>
      <span>ვიდეოები</span>
    </button>
  </div>

  <!-- Fullscreen Manifesto Modal -->
  <div class="fullscreen-modal-overlay" id="manifestoModal" aria-hidden="true" role="dialog" aria-label="მანიფესტი">
    <div class="fullscreen-modal-backdrop" id="manifestoModalBackdrop"></div>
    <div class="fullscreen-modal-card">
      <div class="fullscreen-modal-header">
        <div class="fullscreen-modal-title-wrap">
          <span class="modal-tag-badge">მანიფესტი</span>
          <h2 class="fullscreen-modal-title">სად არის ხელოვნების ადგილი?</h2>
        </div>
        <button class="fullscreen-close-btn" id="closeManifestoModalBtn" type="button" aria-label="დახურვა">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
          </svg>
        </button>
      </div>
      <div class="fullscreen-modal-scroll" id="manifestoModalScroll">
        <h3 class="manifesto-lead-question">სად?</h3>
        <p class="manifesto-paragraph">სად არის ხელოვნების ადგილი, როცა სახელმწიფო პოლიტიკურ და სოციალურ კრიზისშია? როდესაც დემოკრატია - გაუქმებული,<br />კულტურა - დაცენზურებული,<br />სიტყვის თავისუფლება - წართმეული,<br />ხოლო პროტესტის გამოხატვა - დასჯადია.<br />როდესაც ერთმანეთის მიყოლებით იხურება სახელოვნებო სივრცეები, არტისტები ემიგრაციაში გარბიან, სახელმწიფო ინსტიტუტები კი ღიაა მხოლოდ პარტიის მიმართ ლოიალური პირებისთვის.</p>

        <p class="manifesto-paragraph">სად არის ხელოვნების ადგილი იმ ქალაქში, სადაც გზებზე ადამიანები იღუპებიან; სადაც გარევაჭრობა აკრძალულია, ნარკოვაჭრობაზე კი თვალს ხუჭავენ;<br />სადაც ერთადერთ წარმატებულ საქმედ ერთმანეთზე გადაჯაჭვული კვებისა და სილამაზის ინდუსტრიებია;<br />სადაც ხელოვნების სახლის რეზიდენტები „ექსტრემისტებად“ ირაცხებიან, მოქალაქეებზე მოძალადე პოლიციელები კი გმირებად.</p>

        <p class="manifesto-paragraph">სად არის ხელოვნების ადგილი, როცა ადამიანებს დილიდან დაღამებამდე მძიმე ფიზიკური შრომა უწევთ მხოლოდ იმისთვის, რომ შიმშილით არ დაიხოცონ, ავად გახდომა კი პირდაპირ სიკვდილს ნიშნავს.</p>

        <p class="manifesto-paragraph">სად არის ხელოვნების ადგილი იქ, სადაც მრავალსართულიანი კორპუსები შენდება - მდიდარი ქვეყნების უძრავი ქონების ფასად და არავინ იცის, ვინ ყიდულობს ამ ბინებს. სადაც დეველოპერები და ქალაქის მესვეურებს არ აინტერესებთ კულტურული მემკვიდრეობა, ამახინჯებენ ლანდშაფტს, ქალაქსა და საცხოვრებელ გარემოს.</p>

        <p class="manifesto-paragraph">სად არის ხელოვნების ადგილი, როცა სკოლაში ბავშვებს შიათ და ხარისხიანი განათლების მიღების საშუალება არ აქვთ, მშობლებს კი პროპაგანდა უწამლავს გონებას.</p>

        <p class="manifesto-lead-question" style="font-size: 19px; margin-top: 24px;">მაწანწალა ძაღლებით სავსე ქალაქში სად არის ხელოვნების ადგილი?</p>

        <div class="manifesto-invite-highlight">
          <strong>ნიკა სომხიშვილი</strong> და <strong>სოფიო ცერცვაძე</strong> გიწვევთ საიდუმლო გამოფენის საპოვნელად. ჩვენ მას ვმალავთ, რადგან არ ვიცით, ხვალ რის გამო დაგვიწყებს სახელმწიფო დევნას. ვაცხადებთ, რომ მთელი ქალაქი შეიძლება იქცეს ხელოვნების სივრცედ, იქნება ეს მტკვრის მარჯვენა სანაპირო, თუ საცხოვრებელ უბნებს შორის მრავალჯერადად განმეორებულ ობიექტთაგან ერთ-ერთი, ნომრით <strong>2115/4828</strong>
        </div>

        <div class="manifesto-sign-off">
          <strong>ნიკა სომხიშვილი</strong>
          <span>კურატორი: სოფო ცერცვაძე</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Fullscreen Video Gallery Modal -->
  <div class="fullscreen-modal-overlay" id="videoModal" aria-hidden="true" role="dialog" aria-label="ვიდეოები">
    <div class="fullscreen-modal-backdrop" id="videoModalBackdrop"></div>
    <div class="fullscreen-modal-card">
      <div class="fullscreen-modal-header">
        <div class="fullscreen-modal-title-wrap">
          <span class="modal-tag-badge">ვიდეოები</span>
          <h2 class="fullscreen-modal-title">გამოფენის ვიდეო მასალები</h2>
        </div>
        <button class="fullscreen-close-btn" id="closeVideoModalBtn" type="button" aria-label="დახურვა">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
          </svg>
        </button>
      </div>
      <div class="fullscreen-modal-scroll">
        <div class="video-grid" id="videoGridContainer">
          <!-- Videos dynamically rendered from EXHIBITION_VIDEOS in JS -->
        </div>
      </div>
    </div>
  </div>
"""

# Place new HTML components right before the first <script
first_script_idx = text.find('<script')
text = text[:first_script_idx] + new_html_components + '\n  ' + text[first_script_idx:]

# -------------------------------------------------------------
# 3. Update JavaScript logic
# -------------------------------------------------------------

# In JS, remove filterChips listener and openManifestoBtn references
# Replace:
# const openManifestoBtn = document.getElementById('openManifestoBtn');
# const filterChips = document.getElementById('filterChips');
text = text.replace(
    "const openManifestoBtn = document.getElementById('openManifestoBtn');\n      const filterChips = document.getElementById('filterChips');",
    "// Filter chips and old manifesto trigger removed"
)
text = text.replace(
    "const openManifestoBtn = document.getElementById('openManifestoBtn');",
    "// openManifestoBtn removed"
)
text = text.replace(
    "const filterChips = document.getElementById('filterChips');",
    "// filterChips removed"
)

# Remove the old openManifestoBtn click listener
old_manifesto_listener = """      openManifestoBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        closeSearchDropdown();
        openManifestoOnly();
      });"""
text = text.replace(old_manifesto_listener, "// Old openManifestoBtn listener removed")

# Remove filterChips click listener and applyCategoryFilter
old_filter_block_pattern = r'// Filter Chips Functionality\s*filterChips\.addEventListener\(\'click\'.*?function webglSupported\(\)'
filter_replacement = """// Filter chips removed - all POIs always displayed
      function webglSupported()"""
text = re.sub(old_filter_block_pattern, filter_replacement, text, flags=re.DOTALL)

# Remove citizen traces system (section 3) from JS
# Find start of section 3:
# // 3. "დატოვე შენი კვალი" / CITIZEN ART TRACES SYSTEM
trace_start_idx = text.find('// 3. "დატოვე შენი კვალი" / CITIZEN ART TRACES SYSTEM')
if trace_start_idx != -1:
    # Find ending before </script>
    script_end_idx = text.rfind('})();\n  </script>')
    if script_end_idx == -1:
        script_end_idx = text.rfind('})();')
    print('Found trace system at', trace_start_idx, 'to', script_end_idx)
    text = text[:trace_start_idx] + text[script_end_idx:]

# Now let's insert the new Manifesto and Video Gallery JS logic right before })();
new_js_logic = """
      // ========================================================
      // 🎥 ვიდეოების სია — აქ შეგიძლია ჩაამატო ან შეცვალო ვიდეოები!
      // ========================================================
      // როგორ ჩასვა ვიდეო:
      // 1. YouTube ვიდეოზე დააჭირე: Share -> Embed (ან აიღე ვიდეოს ლინკი)
      // 2. URL უნდა იყოს ამ ფორმატში: "https://www.youtube.com/embed/ვიდეოს_ID"
      //    მაგალითად, თუ ვიდეოა: https://www.youtube.com/watch?v=dQw4w9WgXcQ
      //    მაშინ embed ლინკია: https://www.youtube.com/embed/dQw4w9WgXcQ
      // ========================================================
      const EXHIBITION_VIDEOS = [
        {
          title: "„სად არის ხელოვნების ადგილი?“ — გორი (ვიდეო 1)",
          desc: "დოკუმენტური ვიდეო მასალა გამოფენისა და ქალაქის შესახებ",
          url: "https://www.youtube.com/embed/dQw4w9WgXcQ"
        },
        {
          title: "ურბანული სივრცეები და კონცეფცია (ვიდეო 2)",
          desc: "ნიკა სომხიშვილი და სოფო ცერცვაძე",
          url: "https://www.youtube.com/embed/dQw4w9WgXcQ"
        }
      ];

      function renderVideos() {
        const container = document.getElementById('videoGridContainer');
        if (!container) return;
        container.innerHTML = EXHIBITION_VIDEOS.map(v => `
          <div class="video-item-card">
            <div class="video-item-frame">
              <iframe 
                src="${v.url}" 
                title="${v.title}" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                allowfullscreen>
              </iframe>
            </div>
            <div class="video-item-info">
              <h4 class="video-item-title">${v.title}</h4>
              <p class="video-item-desc">${v.desc || ''}</p>
            </div>
          </div>
        `).join('');
      }

      // ========================================================
      // 📜 MANIFESTO & VIDEO MODALS CONTROLLERS
      // ========================================================
      const manifestoModal = document.getElementById('manifestoModal');
      const manifestoModalBackdrop = document.getElementById('manifestoModalBackdrop');
      const closeManifestoModalBtn = document.getElementById('closeManifestoModalBtn');
      const bottomManifestoBtn = document.getElementById('bottomManifestoBtn');

      const videoModal = document.getElementById('videoModal');
      const videoModalBackdrop = document.getElementById('videoModalBackdrop');
      const closeVideoModalBtn = document.getElementById('closeVideoModalBtn');
      const bottomVideoBtn = document.getElementById('bottomVideoBtn');

      function openManifestoModal() {
        closePanel();
        closeVideoModal();
        closeSearchDropdown();
        manifestoModal.classList.add('open');
        manifestoModal.setAttribute('aria-hidden', 'false');
      }

      function closeManifestoModal() {
        manifestoModal.classList.remove('open');
        manifestoModal.setAttribute('aria-hidden', 'true');
      }

      function openVideoModal() {
        closePanel();
        closeManifestoModal();
        closeSearchDropdown();
        renderVideos();
        videoModal.classList.add('open');
        videoModal.setAttribute('aria-hidden', 'false');
      }

      function closeVideoModal() {
        videoModal.classList.remove('open');
        videoModal.setAttribute('aria-hidden', 'true');
        // Stop videos on modal close by reloading iframe sources
        const iframes = videoModal.querySelectorAll('iframe');
        iframes.forEach(f => {
          const s = f.src;
          f.src = '';
          f.src = s;
        });
      }

      // Bottom bar button clicks
      bottomManifestoBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        openManifestoModal();
      });

      bottomVideoBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        openVideoModal();
      });

      // Close handlers for Manifesto (both click and touchend for reliable mobile closing)
      ['click', 'touchend'].forEach(evt => {
        closeManifestoModalBtn.addEventListener(evt, (e) => {
          e.stopPropagation();
          e.preventDefault();
          closeManifestoModal();
        });
      });
      manifestoModalBackdrop.addEventListener('click', closeManifestoModal);

      // Close handlers for Videos (both click and touchend)
      ['click', 'touchend'].forEach(evt => {
        closeVideoModalBtn.addEventListener(evt, (e) => {
          e.stopPropagation();
          e.preventDefault();
          closeVideoModal();
        });
      });
      videoModalBackdrop.addEventListener('click', closeVideoModal);

      // Close handlers for Location Panel Close Button (mobile + desktop)
      const closeBtn = document.getElementById('closeBtn');
      if (closeBtn) {
        ['click', 'touchend'].forEach(evt => {
          closeBtn.addEventListener(evt, (e) => {
            e.stopPropagation();
            e.preventDefault();
            closePanel();
          });
        });
      }

      // Close all modals on Escape key
      window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          closeManifestoModal();
          closeVideoModal();
          closePanel();
          closeSearchDropdown();
        }
      });
"""

# Inject before })();
last_closure_idx = text.rfind('})();')
text = text[:last_closure_idx] + new_js_logic + '\n    ' + text[last_closure_idx:]

# Save to index (2).html AND index.html
with open('index (2).html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully generated both index (2).html and index.html! New length:', len(text))
