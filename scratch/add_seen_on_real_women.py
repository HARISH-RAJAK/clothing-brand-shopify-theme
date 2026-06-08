import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
comment = content[:json_start]
json_content = content[json_start:]
data = json.loads(json_content)

seen_on_women_code = """<style>
.tsukie-real-women {
  background: #fdfbf7;
  padding: 80px 0;
  text-align: center;
}
.tsukie-real-women-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 40px;
}
.tsukie-real-women-head {
  margin-bottom: 45px;
}
.tsukie-real-women-eyebrow {
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #a08766;
  margin: 0 0 12px;
  font-weight: 500;
}
.tsukie-real-women-heading {
  font-family: 'Playfair Display', serif;
  font-size: 52px;
  font-style: italic;
  font-weight: 600;
  line-height: 1.15;
  margin: 0 0 16px;
  color: #1e2a38;
}
.tsukie-real-women-desc {
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  font-style: italic;
  color: #5a5a5a;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.5;
}
.tsukie-real-women-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-bottom: 30px;
}
.tsukie-real-women-item {
  position: relative;
  overflow: hidden;
  aspect-ratio: 3/4;
  background: #eaeaea;
}
.tsukie-real-women-img, .tsukie-real-women-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}
.tsukie-real-women-item:hover .tsukie-real-women-img,
.tsukie-real-women-item:hover .tsukie-real-women-video {
  transform: scale(1.04);
}
.tsukie-real-women-tag {
  position: absolute;
  bottom: 15px;
  left: 15px;
  background: rgba(30, 42, 56, 0.75);
  color: #d4c5a9;
  padding: 6px 12px;
  font-family: 'Montserrat', sans-serif;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 1px;
  z-index: 2;
  backdrop-filter: blur(2px);
}
.tsukie-real-women-play {
  position: absolute;
  top: 15px;
  right: 15px;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.4);
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 10px;
  backdrop-filter: blur(2px);
  z-index: 2;
  pointer-events: none;
}

@media(max-width: 989px) {
  .tsukie-real-women-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }
  .tsukie-real-women-heading {
    font-size: 40px;
  }
}
@media(max-width: 749px) {
  .tsukie-real-women {
    padding: 50px 0;
  }
  .tsukie-real-women-inner {
    padding: 0 16px;
  }
  .tsukie-real-women-heading {
    font-size: 36px;
  }
  .tsukie-real-women-desc {
    font-size: 16px;
  }
  .tsukie-real-women-grid {
    gap: 12px;
  }
}
</style>

<div class="tsukie-real-women">
  <div class="tsukie-real-women-inner">
    <div class="tsukie-real-women-head">
      <p class="tsukie-real-women-eyebrow">AS SEEN ON YOU</p>
      <h2 class="tsukie-real-women-heading">Seen on Real Women</h2>
      <p class="tsukie-real-women-desc">Candid moments of real women styling our timeless silhouettes. Tag us at #TsukieWomen to get featured.</p>
    </div>
    
    <div class="tsukie-real-women-grid">
      <!-- Item 1: Static Image 1 -->
      <div class="tsukie-real-women-item">
        <img class="tsukie-real-women-img" src="{{ 'real_women_1.png' | asset_url }}" alt="Seen on Real Women 1" loading="lazy">
        <span class="tsukie-real-women-tag">@PRIYA_ANAND</span>
      </div>
      
      <!-- Item 2: Video 1 -->
      <div class="tsukie-real-women-item">
        <video class="tsukie-real-women-video" autoplay loop muted playsinline>
          <source src="https://player.vimeo.com/external/371433846.sd.mp4?s=236da2f3c02cba73e421097828f10129023405f0&profile_id=165&oauth2_token_id=57447761" type="video/mp4">
        </video>
        <span class="tsukie-real-women-play">▶</span>
        <span class="tsukie-real-women-tag">@ANJALI.S</span>
      </div>
      
      <!-- Item 3: Static Image 2 -->
      <div class="tsukie-real-women-item">
        <img class="tsukie-real-women-img" src="{{ 'real_women_2.png' | asset_url }}" alt="Seen on Real Women 2" loading="lazy">
        <span class="tsukie-real-women-tag">@MEERA_M</span>
      </div>
      
      <!-- Item 4: Video 2 -->
      <div class="tsukie-real-women-item">
        <video class="tsukie-real-women-video" autoplay loop muted playsinline>
          <source src="https://player.vimeo.com/external/409223788.sd.mp4?s=d4f40d6cdcc67e817e0892095f9227ca7b587000&profile_id=165&oauth2_token_id=57447761" type="video/mp4">
        </video>
        <span class="tsukie-real-women-play">▶</span>
        <span class="tsukie-real-women-tag">@RIYA.SEN</span>
      </div>
    </div>
  </div>
</div>"""

# Define the new section block
new_sec_id = 'custom_liquid_seen_on_real_women'
data['sections'][new_sec_id] = {
    'type': 'custom-liquid',
    'name': 'Seen on Real Women',
    'settings': {
        'custom_liquid': seen_on_women_code
    }
}

# Insert into the order array before custom_liquid_MMecBe
order_list = data.get('order', [])
if new_sec_id not in order_list:
    try:
        idx = order_list.index('custom_liquid_MMecBe')
        order_list.insert(idx, new_sec_id)
        # Also add a divider before it to separate it beautifully
        div_id = 'divider_seen_on_real_women'
        data['sections'][div_id] = {
            'type': 'divider',
            'name': 'Divider',
            'settings': {
                'color_scheme': 'scheme-e5234ede-d196-4b3b-a9e2-6e7d24b8ca5c',
                'section_width': 'full-width',
                'thickness': 1,
                'corner_radius': 'square',
                'width_percent': 100,
                'alignment_horizontal': 'center',
                'padding-block-start': 16,
                'padding-block-end': 16
            }
        }
        order_list.insert(idx, div_id)
        print("Inserted Seen on Real Women section and a divider before Style in Motion.")
    except ValueError:
        order_list.append(new_sec_id)
        print("custom_liquid_MMecBe not found in order, appended to end.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(comment + json.dumps(data, indent=2, ensure_ascii=False))

print("Successfully added Seen on Real Women section to index.json.")
