import re
import os

# Paths
original_pdp_path = "C:/Users/hp/.gemini/antigravity-ide/brain/8f068730-3b21-43a7-96ee-55f10e6b4b4b/scratch/product_template_custom_liquid.liquid"
output_pdp_path = "c:/Users/hp/Downloads/theme_export__tsukie-in-horizon__08JUN2026-0346pm/scratch/custom_liquid_rW9bhR.liquid"

# Read original code
with open(original_pdp_path, "r", encoding="utf-8") as f:
    code = f.read()

print(f"Original length: {len(code)} characters.")

replacements = []

# 1. Font import
old_import = "@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Montserrat:wght@300;400;500;600&display=swap');"
new_import = "@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Cormorant+Garamond:wght@300;400&family=Montserrat:wght@300;400;500;600&display=swap');"
replacements.append((old_import, new_import, "Font import"))

# 2. Title typography
old_title_css = """.tsukie-product-title{
  font-family:'Playfair Display',serif;
  font-size:36px;
  font-weight:400;
  color:#1e2a38;
  margin:0 0 12px;
  line-height:1.2;
}"""
new_title_css = """.tsukie-product-title{
  font-family:'Cormorant Garamond',serif;
  font-size:36px;
  font-weight:300;
  color:#1e2a38;
  margin:0 0 12px;
  line-height:1.2;
}"""
replacements.append((old_title_css, new_title_css, "Title typography CSS"))

# 3. Dynamic Badge container CSS
old_badge_css = """.tsukie-badge{
  position:absolute;
  top:16px;
  left:16px;
  background:#1e2a38;
  color:#d4c5a9;
  font-family:'Montserrat',sans-serif;
  font-size:10px;
  letter-spacing:1px;
  text-transform:uppercase;
  padding:6px 12px;
  font-weight:600;
  z-index: 2;
}"""
new_badge_css = """.tsukie-badge-container{
  position:absolute;
  top:16px;
  left:16px;
  display:flex;
  flex-direction:column;
  gap:6px;
  z-index: 2;
}
.tsukie-badge{
  background:#1e2a38;
  color:#d4c5a9;
  font-family:'Montserrat',sans-serif;
  font-size:10px;
  letter-spacing:1px;
  text-transform:uppercase;
  padding:6px 12px;
  font-weight:600;
  width:fit-content;
}"""
replacements.append((old_badge_css, new_badge_css, "Badge CSS"))

# 4. CTA Button styling
old_cta_css = """.tsukie-btn{
  padding:16px;
  font-family:'Montserrat',sans-serif;
  font-size:11px;
  letter-spacing:2px;
  text-transform:uppercase;
  font-weight:600;
  cursor:pointer;
  border:none;
  transition:all 0.2s;
  display:flex;
  align-items:center;
  justify-content:center;
  gap:8px;
}
.tsukie-btn:disabled{
  opacity:0.5;
  cursor:not-allowed;
}
.tsukie-btn-add{
  background:#1e2a38;
  color:#d4c5a9;
}
.tsukie-btn-add:hover:not(:disabled){
  background:#2a3a4e;
}
.tsukie-btn-buy{
  background:#5a4a3a;
  color:#d4c5a9;
  position: relative;
}
.tsukie-btn-buy:hover:not(:disabled){
  background:#6a5a4a;
}"""
new_cta_css = """.tsukie-btn{
  padding:16px;
  font-family:'Montserrat',sans-serif;
  font-size:11px;
  letter-spacing:2px;
  text-transform:uppercase;
  font-weight:600;
  cursor:pointer;
  transition:all 0.2s;
  display:flex;
  align-items:center;
  justify-content:center;
  gap:8px;
  box-sizing: border-box;
  border: 2px solid transparent;
  height: 52px;
}
.tsukie-btn:disabled{
  opacity:0.5;
  cursor:not-allowed;
}
.tsukie-btn-add{
  background:#1e2a38;
  color:#d4c5a9;
  border-color:#1e2a38;
}
.tsukie-btn-add:hover:not(:disabled){
  background:transparent;
  color:#1e2a38;
  border-color:#1e2a38;
}
.tsukie-btn-buy{
  background:transparent;
  color:#1e2a38;
  border-color:#1e2a38;
  position: relative;
}
.tsukie-btn-buy:hover:not(:disabled){
  background:#1e2a38;
  color:#d4c5a9;
}"""
replacements.append((old_cta_css, new_cta_css, "CTA buttons CSS"))

# 5. Border outlines (replace the multiple border lines)
borders_to_replace = [
    ("border:1px solid rgba(30,42,56,0.15);", "border:1px solid #e0d9cd;"),
    ("border:1px solid rgba(30,42,56,0.08);", "border:1px solid #e0d9cd;"),
    ("border-right:1px solid rgba(30,42,56,0.08);", "border-right:1px solid #e0d9cd;"),
    ("border-top:1px solid rgba(30,42,56,0.08);", "border-top:1px solid #e0d9cd;"),
    ("border-bottom:1px solid rgba(30,42,56,0.08);", "border-bottom:1px solid #e0d9cd;"),
]
for old_b, new_b in borders_to_replace:
    replacements.append((old_b, new_b, f"Border: {old_b}"))

# 6. Remove EMI styles
emi_css = """.tsukie-emi{
  font-family:'Montserrat',sans-serif;
  font-size:12px;
  color:#666;
  margin-bottom:24px;
}
.tsukie-emi strong{color:#1e2a38;font-weight:500}"""
replacements.append((emi_css, "", "EMI CSS styling"))

# 7. Remove EMI HTML
emi_html = """      <div class="tsukie-emi">
        or <strong id="tsukie-emi-price">{{ product.selected_or_first_available_variant.price | divided_by: 3 | money }}/month</strong> with easy EMI
      </div>"""
replacements.append((emi_html, "", "EMI HTML"))

# 8. Size Guide Trigger
old_size_label = """<div class="tsukie-variant-label">{{ option.name }}</div>"""
new_size_label = """<div style="display:flex; align-items:center; gap:8px;">
                  <div class="tsukie-variant-label">{{ option.name }}</div>
                  {% if option.name == 'Size' or option.name == 'Size/Fits' or option.name == 'Fit' %}
                    <span style="color:#d4c5a9;">|</span>
                    <a href="#" onclick="tsukieOpenSizeGuide(event)" class="tsukie-size-guide-link" style="color:#a08766; text-decoration:underline; font-size:11px; font-family:'Montserrat',sans-serif; text-transform:uppercase; font-weight:600; letter-spacing:1px;">Size Guide</a>
                  {% endif %}
                </div>"""
replacements.append((old_size_label, new_size_label, "Size Guide link trigger"))

# 9. Thumbnail alt tags
old_thumb = """            <div class="tsukie-thumb {% if forloop.first %}active{% endif %}" onclick="tsukieChangeImage('{{ image | img_url: '1000x' }}', {{ forloop.index0 }})">"""
new_thumb = """            <div class="tsukie-thumb {% if forloop.first %}active{% endif %}" data-alt="{{ image.alt | escape }}" data-img-id="{{ image.id }}" onclick="tsukieChangeImage('{{ image | img_url: '1000x' }}', {{ forloop.index0 }})">"""
replacements.append((old_thumb, new_thumb, "Thumbnail data-alt"))

# 10. Dynamic badges HTML
old_badges_html = """          {% if product.tags contains 'bestseller' %}
            <div class="tsukie-badge">BESTSELLER</div>
          {% endif %}"""
new_badges_html = """          <div class="tsukie-badge-container">
            {% for tag in product.tags %}
              {% unless tag contains 'filter' or tag contains 'meta-' or tag contains 'custom-' or tag == 'all' %}
                <div class="tsukie-badge">{{ tag | upcase }}</div>
              {% endunless %}
            {% endfor %}
          </div>"""
replacements.append((old_badges_html, new_badges_html, "Dynamic Badges HTML"))

# 11. Special Offers Horizontal Strip Inside Form
old_btn_group = """        <div class="tsukie-btn-group">"""
new_btn_group = """<!-- Special Offers Strip -->
        <div class="tsukie-special-offers-strip">
          <div class="tsukie-offers-title">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581a1.125 1.125 0 001.59 0l4.318-4.318a1.125 1.125 0 000-1.59l-9.58-9.581a1.125 1.125 0 00-1.591-.659zm5.432 4.5a1.125 1.125 0 11-2.25 0 1.125 1.125 0 012.25 0z" /></svg>
            Special Offers
          </div>
          <div class="tsukie-offers-strip-items">
            <div class="tsukie-offer-strip-item" onclick="tsukieCopyCode(this, 'TSUKIE10')" title="Click to copy TSUKIE10">
              <span><strong>TSUKIE10</strong>: 10% Off</span>
              <span class="copy-lbl">Copy</span>
            </div>
            <div class="tsukie-offer-strip-item" onclick="tsukieCopyCode(this, 'TSUKIE25')" title="Click to copy TSUKIE25">
              <span><strong>TSUKIE25</strong>: 25% Off</span>
              <span class="copy-lbl">Copy</span>
            </div>
          </div>
        </div>
        
        <div class="tsukie-btn-group">"""
replacements.append((old_btn_group, new_btn_group, "Special offers strip above CTA"))

# 12. Remove Top Product Description Accordion Block
description_accordion_block = """        {% if product.description != blank %}
          <div class="tsukie-accordion-item">
            <div class="tsukie-accordion-header" onclick="tsukieToggleAccordion(this)">
              PRODUCT DESCRIPTION <span class="tsukie-accordion-icon">+</span>
            </div>
            <div class="tsukie-accordion-content">
              <div style="padding-top:12px;">{{ product.description }}</div>
            </div>
          </div>
        {% endif %}"""
replacements.append((description_accordion_block, "", "Product description accordion removal"))

# 13. Remove old vertical Special Offers CSS block
old_offers_css = """  /* Special Offers Section Styling */
  .tsukie-special-offers {
    background: #fdfbf7;
    border: 1px dashed #a08766;
    border-radius: 8px;
    padding: 16px;
    margin: 20px 0;
    font-family: 'Montserrat', sans-serif;
  }
  .tsukie-offers-title {
    font-size: 13px;
    font-weight: 700;
    color: #1e2a38;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 0 0 12px 0;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .tsukie-offers-title svg {
    width: 16px;
    height: 16px;
    color: #a08766;
  }
  .tsukie-offers-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .tsukie-offer-card {
    background: #fdfbf7;
    border: 1px solid rgba(160, 135, 102, 0.15);
    border-radius: 6px;
    padding: 12px 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    transition: all 0.2s ease;
  }
  .tsukie-offer-card:hover {
    border-color: #a08766;
  }
  .tsukie-offer-info {
    flex: 1;
  }
  .tsukie-offer-discount {
    font-size: 13px;
    font-weight: 700;
    color: #1e2a38;
    margin-bottom: 2px;
  }
  .tsukie-offer-desc {
    font-size: 11px;
    color: #666;
    font-weight: 400;
  }
  .tsukie-offer-code-wrap {
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .tsukie-offer-code {
    background: #f5f1ea;
    border: 1px dashed #a08766;
    font-family: monospace;
    font-weight: 700;
    font-size: 12px;
    color: #1e2a38;
    padding: 4px 8px;
    border-radius: 4px;
    letter-spacing: 0.5px;
  }
  .tsukie-copy-btn {
    background: transparent;
    border: 1px solid #1e2a38;
    color: #1e2a38;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.5px;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    text-transform: uppercase;
    transition: all 0.2s ease;
  }
  .tsukie-copy-btn:hover {
    background: #1e2a38;
    color: #d4c5a9;
  }
  @media(max-width: 480px) {
    .tsukie-offer-card {
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }
    .tsukie-offer-code-wrap {
      width: 100%;
      justify-content: space-between;
    }
  }"""
replacements.append((old_offers_css, "", "Old special offers CSS"))

# 14. Remove old vertical Special Offers HTML block
old_offers_html = """<div class="tsukie-special-offers">
  <div class="tsukie-offers-title">
    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581a1.125 1.125 0 001.59 0l4.318-4.318a1.125 1.125 0 000-1.59l-9.58-9.581a1.125 1.125 0 00-1.591-.659zm5.432 4.5a1.125 1.125 0 11-2.25 0 1.125 1.125 0 012.25 0z" /></svg>
    Special Offers
  </div>
  <div class="tsukie-offers-list">
    <div class="tsukie-offer-card">
      <div class="tsukie-offer-info">
        <div class="tsukie-offer-discount">Get 10% Off</div>
        <div class="tsukie-offer-desc">Buy any 1 item from our collection</div>
      </div>
      <div class="tsukie-offer-code-wrap">
        <div class="tsukie-offer-code">TSUKIE10</div>
        <button type="button" class="tsukie-copy-btn" onclick="tsukieCopyCode(this, 'TSUKIE10')">Copy</button>
      </div>
    </div>
    <div class="tsukie-offer-card">
      <div class="tsukie-offer-info">
        <div class="tsukie-offer-discount">Get 25% Off</div>
        <div class="tsukie-offer-desc">Buy any 2 items from our collection</div>
      </div>
      <div class="tsukie-offer-code-wrap">
        <div class="tsukie-offer-code">TSUKIE25</div>
        <button type="button" class="tsukie-copy-btn" onclick="tsukieCopyCode(this, 'TSUKIE25')">Copy</button>
      </div>
    </div>
  </div>
</div>"""
replacements.append((old_offers_html, "", "Old special offers HTML"))

# 15. Redesign PNG trust badges to premium SVG (SAFE: Replace only the img-row div!)
old_badges_html = """      <div class="tsukie-trust-badges-img-row">
        <div class="tsukie-trust-badge-img-item">
          <img src="//tsukie.in/cdn/shop/files/1-01.png?v=1776420000&amp;width=100" alt="COD Available" srcset="//tsukie.in/cdn/shop/files/1-01.png?v=1776420000&amp;width=100 100w" width="100" height="23" loading="lazy">
        </div>
        <div class="tsukie-trust-badge-img-item">
          <img src="//tsukie.in/cdn/shop/files/1-03.png?v=1776420000&amp;width=100" alt="Secure Checkout" srcset="//tsukie.in/cdn/shop/files/1-03.png?v=1776420000&amp;width=100 100w" width="100" height="23" loading="lazy">
        </div>
        <div class="tsukie-trust-badge-img-item">
          <img src="//tsukie.in/cdn/shop/files/1-02.png?v=1776419999&amp;width=100" alt="24/7 Support" srcset="//tsukie.in/cdn/shop/files/1-02.png?v=1776419999&amp;width=100 100w" width="100" height="23" loading="lazy">
        </div>
      </div>"""

new_badges_html = """      <div class="tsukie-premium-badges">
        <div class="tsukie-premium-badge-item">
          <svg fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M20.25 7.5l-.625 10.632a2.25 2.25 0 01-2.247 2.118H6.622a2.25 2.25 0 01-2.247-2.118L3.75 7.5M10 11.25h4M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125z" /></svg>
          <span class="tsukie-premium-badge-text">COD Available</span>
        </div>
        <div class="tsukie-premium-badge-item">
          <svg fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" /></svg>
          <span class="tsukie-premium-badge-text">Secure Checkout</span>
        </div>
        <div class="tsukie-premium-badge-item">
          <svg fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a.75.75 0 01-1.074-.765 5.99 5.99 0 011.524-2.238C4.034 16.556 3 14.379 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z" /></svg>
          <span class="tsukie-premium-badge-text">24/7 Support</span>
        </div>
      </div>"""
replacements.append((old_badges_html, new_badges_html, "SVG trust badges HTML"))

# 16. Replace old trust badge and order tracker CSS
old_badges_and_tracker_css = """  /* Trust Badges PNG Row */
  .tsukie-trust-badges-img-row {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    gap: 16px;
    margin: 16px 0;
  }
  .tsukie-trust-badge-img-item {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .tsukie-trust-badge-img-item img {
    max-width: 100px;
    height: auto;
    display: block;
  }
  @media (max-width: 480px) {
    .tsukie-trust-badges-img-row {
      gap: 10px;
    }
    .tsukie-trust-badge-img-item img {
      max-width: 85px;
    }
  }

  /* Order Status Section */
  .tsukie-order-status-v2 {
    text-align: center;
    margin-top: 28px;
    background: transparent;
  }
  .tsukie-status-title-v2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 16px;
    font-weight: 800;
    color: #1e2a38;
    letter-spacing: 0.5px;
    margin: 0 0 6px 0;
    text-transform: uppercase;
  }
  .tsukie-status-subtitle-v2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 13px;
    color: #4a4a4a;
    margin: 0 0 24px 0;
    font-weight: 400;
  }
  
  /* Timeline Grid Base Line (Zero Breaking on Mobile) */
  .tsukie-timeline-v2 {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    max-width: 420px;
    margin: 0 auto 12px;
    padding: 0 35px;
  }
  /* The Solid Connecting Line */
  .tsukie-timeline-v2::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 45px;
    right: 45px;
    height: 2px;
    background: #1e2a38;
    transform: translateY(-50%);
    z-index: 1;
  }
  .tsukie-node-v2 {
    position: relative;
    z-index: 2;
  }
  .tsukie-circle-v2 {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    border: 2px solid #1e2a38;
    background: #f5f1ea; /* Matching your theme background */
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .tsukie-circle-v2 svg {
    width: 18px;
    height: 18px;
    color: #1e2a38;
    stroke-width: 2.5;
  }
  
  /* Bottom Text Labels Layout */
  .tsukie-labels-grid-v2 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    max-width: 480px;
    margin: 0 auto;
    gap: 4px;
  }
  .tsukie-label-item-v2 {
    text-align: center;
    padding: 0 2px;
  }
  .tsukie-lbl-title-v2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 12px;
    font-weight: 700;
    color: #1e2a38;
    margin-bottom: 3px;
    line-height: 1.2;
  }
  .tsukie-lbl-date-v2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 11px;
    color: #666666;
    font-weight: 500;
    line-height: 1.2;
  }

  /* Mobile Responsive Viewport Tweaks */
  @media (max-width: 480px) {
    .tsukie-badge-title-v2 {
      font-size: 10px;
    }
    .tsukie-badge-card-v2 {
      padding: 10px 2px;
    }
    .tsukie-badge-card-v2 svg {
      width: 22px;
      height: 22px;
    }
    .tsukie-lbl-title-v2 {
      font-size: 10px;
    }
    .tsukie-lbl-date-v2 {
      font-size: 9px;
    }
    .tsukie-timeline-v2 {
      padding: 0 25px;
    }
    .tsukie-timeline-v2::before {
      left: 35px;
      right: 35px;
    }
    .tsukie-circle-v2 {
      width: 28px;
      height: 28px;
    }
    .tsukie-circle-v2 svg {
      width: 14px;
      height: 14px;
    }
  }"""

new_badges_and_tracker_css = """  /* Size Guide Modal Styles */
  .tsukie-size-guide-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 10000;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .tsukie-size-guide-modal-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(30, 42, 56, 0.6);
    backdrop-filter: blur(4px);
  }
  .tsukie-size-guide-modal-content {
    position: relative;
    background: #fdfbf7;
    border: 2px solid #d4c5a9;
    border-radius: 8px;
    width: 90%;
    max-width: 500px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    z-index: 10001;
  }
  .tsukie-size-guide-modal-close {
    position: absolute;
    top: 15px;
    right: 15px;
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #1e2a38;
    line-height: 1;
    padding: 0;
    transition: color 0.2s;
  }
  .tsukie-size-guide-modal-close:hover {
    color: #a08766;
  }
  .tsukie-size-guide-modal-title {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-style: italic;
    font-weight: 600;
    color: #1e2a38;
    margin: 0 0 20px;
    text-align: center;
  }
  .tsukie-size-guide-table-wrap {
    overflow-x: auto;
  }
  .tsukie-size-guide-table-wrap table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Montserrat', sans-serif;
    font-size: 13px;
  }
  .tsukie-size-guide-table-wrap th, 
  .tsukie-size-guide-table-wrap td {
    padding: 12px;
    border: 1px solid #e0d9cd;
    text-align: center;
  }
  .tsukie-size-guide-table-wrap th {
    background: #1e2a38;
    color: #d4c5a9;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 11px;
    letter-spacing: 1px;
  }
  .tsukie-size-guide-table-wrap tr:nth-child(even) {
    background: rgba(212, 197, 169, 0.1);
  }
  
  /* Special Offers Section Styling (Horizontal Strip above CTA) */
  .tsukie-special-offers-strip {
    background: #fdfbf7;
    border: 1px solid #e0d9cd;
    border-radius: 4px;
    padding: 10px 14px;
    margin-bottom: 20px;
    font-family: 'Montserrat', sans-serif;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
  }
  .tsukie-offers-title {
    font-size: 11px;
    font-weight: 700;
    color: #1e2a38;
    text-transform: uppercase;
    letter-spacing: 1px;
    display: flex;
    align-items: center;
    gap: 6px;
    flex-shrink: 0;
  }
  .tsukie-offers-title svg {
    width: 14px;
    height: 14px;
    color: #a08766;
  }
  .tsukie-offers-strip-items {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    flex: 1;
    justify-content: flex-end;
  }
  .tsukie-offer-strip-item {
    background: #f5f1ea;
    border: 1px dashed #d4c5a9;
    border-radius: 3px;
    padding: 6px 10px;
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    font-size: 11px;
    color: #1e2a38;
    transition: all 0.2s ease;
  }
  .tsukie-offer-strip-item:hover {
    border-color: #1e2a38;
    background: #e0d9cd;
  }
  .tsukie-offer-strip-item strong {
    font-weight: 700;
  }
  .tsukie-offer-strip-item .copy-lbl {
    font-size: 9px;
    text-transform: uppercase;
    font-weight: 600;
    color: #a08766;
    border-left: 1px solid rgba(30,42,56,0.15);
    padding-left: 6px;
  }
  
  /* Redesigned Order Status Tracker */
  .tsukie-order-status-v2 {
    text-align: center;
    margin: 28px 0;
    background: transparent;
  }
  .tsukie-status-title-v2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: #1e2a38;
    letter-spacing: 1.5px;
    margin: 0 0 6px 0;
    text-transform: uppercase;
  }
  .tsukie-status-subtitle-v2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 11px;
    color: #666;
    margin: 0 0 24px 0;
    font-weight: 400;
  }
  .tsukie-timeline-v2 {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    max-width: 380px;
    margin: 0 auto 12px;
    padding: 0 25px;
  }
  .tsukie-timeline-v2::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 35px;
    right: 35px;
    height: 1px;
    background: #e0d9cd;
    transform: translateY(-50%);
    z-index: 1;
  }
  .tsukie-node-v2 {
    position: relative;
    z-index: 2;
  }
  .tsukie-circle-v2 {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: 1px solid #1e2a38;
    background: #fdfbf7;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
  }
  .tsukie-circle-v2.active {
    background: #1e2a38;
    border-color: #1e2a38;
  }
  .tsukie-circle-v2 svg {
    width: 12px;
    height: 12px;
    color: #1e2a38;
    stroke-width: 2.5;
  }
  .tsukie-circle-v2.active svg {
    color: #d4c5a9;
  }
  .tsukie-labels-grid-v2 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    max-width: 440px;
    margin: 0 auto;
    gap: 4px;
  }
  .tsukie-label-item-v2 {
    text-align: center;
  }
  .tsukie-lbl-title-v2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 11px;
    font-weight: 600;
    color: #1e2a38;
    margin-bottom: 2px;
    line-height: 1.2;
  }
  .tsukie-lbl-date-v2 {
    font-family: 'Montserrat', sans-serif;
    font-size: 10px;
    color: #888;
    font-weight: 500;
    line-height: 1.2;
  }
  
  /* Premium SVG Trust Badges Row */
  .tsukie-premium-badges {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 24px 0;
    border-top: 1px solid #e0d9cd;
    border-bottom: 1px solid #e0d9cd;
    padding: 16px 0;
    background: transparent;
  }
  .tsukie-premium-badge-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 8px;
  }
  .tsukie-premium-badge-item svg {
    width: 24px;
    height: 24px;
    color: #1e2a38;
  }
  .tsukie-premium-badge-text {
    font-family: 'Montserrat', sans-serif;
    font-size: 11px;
    font-weight: 600;
    color: #1e2a38;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  
  @media(max-width:768px){
    .tsukie-special-offers-strip {
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }
    .tsukie-offers-strip-items {
      justify-content: flex-start;
      width: 100%;
      gap: 8px;
    }
  }
  @media (max-width: 480px) {
    .tsukie-lbl-title-v2 { font-size: 9px; }
    .tsukie-lbl-date-v2 { font-size: 8px; }
    .tsukie-timeline-v2 { padding: 0 15px; }
    .tsukie-timeline-v2::before { left: 25px; right: 25px; }
    .tsukie-circle-v2 { width: 20px; height: 20px; }
    .tsukie-circle-v2 svg { width: 10px; height: 10px; }
    .tsukie-premium-badge-text { font-size: 9px; letter-spacing: 0px; }
    .tsukie-premium-badge-item svg { width: 20px; height: 20px; }
  }"""
replacements.append((old_badges_and_tracker_css, new_badges_and_tracker_css, "Trust badges & tracker CSS redesign"))

# 17. Replace old timeline tracker HTML (SAFE: replace only the div!)
old_tracker_html = """<!-- 2. Tracker Section -->
<div class="tsukie-order-status-v2">
  <h3 class="tsukie-status-title-v2">ORDER STATUS</h3>
  <p class="tsukie-status-subtitle-v2">Track your delivery and expected arrival time!</p>
  
  <!-- Tracker Node Line -->
  <div class="tsukie-timeline-v2">
    <div class="tsukie-node-v2">
      <div class="tsukie-circle-v2">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
      </div>
    </div>
    <div class="tsukie-node-v2">
      <div class="tsukie-circle-v2">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
      </div>
    </div>
    <div class="tsukie-node-v2">
      <div class="tsukie-circle-v2">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
      </div>
    </div>
  </div>
  
  <!-- Labels with Automated Live Real Dates -->
  <div class="tsukie-labels-grid-v2">
    <div class="tsukie-label-item-v2">
      <div class="tsukie-lbl-title-v2">Order Confirmed</div>
      <div class="tsukie-lbl-date-v2">{{ "now" | date: "%b %d %A" }}</div>
    </div>
    <div class="tsukie-label-item-v2">
      <div class="tsukie-lbl-title-v2">On Its Way</div>
      <div class="tsukie-lbl-date-v2">{{ "now" | date: "%s" | plus: 86400 | date: "%b %d %A" }}</div>
    </div>
    <div class="tsukie-label-item-v2">
      <div class="tsukie-lbl-title-v2">Arriving Soon</div>
      <div class="tsukie-lbl-date-v2">Expected {{ "now" | date: "%s" | plus: 259200 | date: "%b %d %A" }}</div>
    </div>
  </div>
</div>
<!-- END OF TRACKER CODES -->"""

new_tracker_html = """      <div class="tsukie-order-status-v2">
        <h3 class="tsukie-status-title-v2">ORDER STATUS</h3>
        <p class="tsukie-status-subtitle-v2">Track your delivery and expected arrival time!</p>
        
        <div class="tsukie-timeline-v2">
          <div class="tsukie-node-v2">
            <div class="tsukie-circle-v2 active">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
            </div>
          </div>
          <div class="tsukie-node-v2">
            <div class="tsukie-circle-v2 active">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
            </div>
          </div>
          <div class="tsukie-node-v2">
            <div class="tsukie-circle-v2">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            </div>
          </div>
        </div>
        
        <div class="tsukie-labels-grid-v2">
          <div class="tsukie-label-item-v2">
            <div class="tsukie-lbl-title-v2">Order Confirmed</div>
            <div class="tsukie-lbl-date-v2">{{ "now" | date: "%b %d %A" }}</div>
          </div>
          <div class="tsukie-label-item-v2">
            <div class="tsukie-lbl-title-v2">On Its Way</div>
            <div class="tsukie-lbl-date-v2">{{ "now" | date: "%s" | plus: 86400 | date: "%b %d %A" }}</div>
          </div>
          <div class="tsukie-label-item-v2">
            <div class="tsukie-lbl-title-v2">Arriving Soon</div>
            <div class="tsukie-lbl-date-v2">Expected {{ "now" | date: "%s" | plus: 259200 | date: "%b %d %A" }}</div>
          </div>
        </div>
      </div>"""
replacements.append((old_tracker_html, new_tracker_html, "Tracker timeline HTML redesign"))

# 18. JS Helpers: Insert size guide, color filtering, recently viewed logic
old_js_start = "let tsukieCurrentImage = 0;"
new_js_start = """let tsukieCurrentImage = 0;
// Size Guide Modal JS
function tsukieOpenSizeGuide(e) {
  e.preventDefault();
  const modal = document.getElementById('tsukie-size-guide-modal');
  if (modal) modal.style.display = 'flex';
}
function tsukieCloseSizeGuide() {
  const modal = document.getElementById('tsukie-size-guide-modal');
  if (modal) modal.style.display = 'none';
}

// Color Filtered Gallery JS
function tsukieFilterImagesByColor(colorName) {
  if (!colorName) return;
  const thumbs = document.querySelectorAll('.tsukie-thumb');
  let firstMatch = null;
  let firstMatchIndex = -1;
  
  thumbs.forEach((thumb, idx) => {
    const alt = (thumb.getAttribute('data-alt') || '').toLowerCase();
    const color = colorName.toLowerCase();
    
    if (alt.includes(color) || color.includes(alt)) {
      thumb.style.display = 'block';
      if (firstMatch === null) {
        firstMatch = thumb;
        firstMatchIndex = idx;
      }
    } else {
      thumb.style.display = 'none';
    }
  });
  
  if (firstMatch) {
    const src = firstMatch.querySelector('img').src.replace('200x', '1000x').replace('_200x', '_1000x');
    tsukieChangeImage(src, firstMatchIndex);
  } else {
    thumbs.forEach(thumb => {
      thumb.style.display = 'block';
    });
  }
}

// Push to Recently Viewed
(function() {
  const currentId = '{{ product.id }}';
  if (currentId) {
    let viewed = JSON.parse(localStorage.getItem('viewedProducts') || '[]');
    viewed = viewed.filter(x => x !== currentId);
    viewed.unshift(currentId);
    viewed = viewed.slice(0, 10);
    localStorage.setItem('viewedProducts', JSON.stringify(viewed));
  }
})();"""
replacements.append((old_js_start, new_js_start, "JS Helpers injection"))

# 19. Initial color filter in JS options picker
old_opt_js = """    tsukieSelectedOptions[2] = defaultVar.option2;
    tsukieSelectedOptions[3] = defaultVar.option3;
  }
}"""
new_opt_js = """    tsukieSelectedOptions[2] = defaultVar.option2;
    tsukieSelectedOptions[3] = defaultVar.option3;
    
    // Also trigger initial filtering if there's a color option on load
    const colorIndex = tsukieProduct.options.findIndex(opt => opt.toLowerCase() === 'color' || opt.toLowerCase() === 'colour');
    if (colorIndex > -1) {
      const initialColor = defaultVar['option' + (colorIndex + 1)];
      if (initialColor) {
        setTimeout(() => tsukieFilterImagesByColor(initialColor), 100);
      }
    }
  }
}"""
replacements.append((old_opt_js, new_opt_js, "Initial color filter on load"))

# 20. Update tsukieCopyCode function to match copy label
old_copy_fn = """function tsukieCopyCode(btn, code) {
  navigator.clipboard.writeText(code).then(() => {
    const originalText = btn.textContent;
    btn.textContent = 'COPIED!';
    btn.style.backgroundColor = '#1e2a38';
    btn.style.color = '#d4c5a9';
    setTimeout(() => {
      btn.textContent = originalText;
      btn.style.backgroundColor = 'transparent';
      btn.style.color = '#1e2a38';
    }, 1500);
  });
}"""
new_copy_fn = """function tsukieCopyCode(el, code) {
  navigator.clipboard.writeText(code).then(() => {
    const copyLbl = el.querySelector('.copy-lbl');
    if (copyLbl) {
      const origText = copyLbl.textContent;
      copyLbl.textContent = 'COPIED!';
      copyLbl.style.color = '#1e2a38';
      setTimeout(() => {
        copyLbl.textContent = origText;
        copyLbl.style.color = '#a08766';
      }, 1500);
    }
  });
}"""
replacements.append((old_copy_fn, new_copy_fn, "tsukieCopyCode update"))

# 21. Add Size Guide modal HTML before closing </section>
old_section_close = "</section>"
new_section_close = """
<!-- Size Guide Modal Markup -->
<div class="tsukie-size-guide-modal" id="tsukie-size-guide-modal" style="display:none;">
  <div class="tsukie-size-guide-modal-overlay" onclick="tsukieCloseSizeGuide()"></div>
  <div class="tsukie-size-guide-modal-content">
    <button class="tsukie-size-guide-modal-close" onclick="tsukieCloseSizeGuide()">&times;</button>
    <h3 class="tsukie-size-guide-modal-title">Size Guide</h3>
    <div class="tsukie-size-guide-table-wrap">
      <table>
        <thead>
          <tr>
            <th>Size</th>
            <th>Bust (in)</th>
            <th>Waist (in)</th>
            <th>Hips (in)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>XS</td>
            <td>32</td>
            <td>26</td>
            <td>36</td>
          </tr>
          <tr>
            <td>S</td>
            <td>34</td>
            <td>28</td>
            <td>38</td>
          </tr>
          <tr>
            <td>M</td>
            <td>36</td>
            <td>30</td>
            <td>40</td>
          </tr>
          <tr>
            <td>L</td>
            <td>38</td>
            <td>32</td>
            <td>42</td>
          </tr>
          <tr>
            <td>XL</td>
            <td>40</td>
            <td>34</td>
            <td>44</td>
          </tr>
          <tr>
            <td>XXL</td>
            <td>42</td>
            <td>36</td>
            <td>46</td>
          </tr>
          <tr>
            <td>3XL</td>
            <td>44</td>
            <td>38</td>
            <td>48</td>
          </tr>
          <tr>
            <td>4XL</td>
            <td>46</td>
            <td>40</td>
            <td>50</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</section>"""
# Using rreplace (only replace the last occurrence)
def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

# 22. Hijacked reviews Widget updates
old_reviews_visible = "let visibleCount = 5;"
new_reviews_visible = "let visibleCount = 1;"
replacements.append((old_reviews_visible, new_reviews_visible, "Reviews count initial 1"))

old_reviews_limit = "allReviews.length > 5"
new_reviews_limit = "allReviews.length > 1"
replacements.append((old_reviews_limit, new_reviews_limit, "Reviews display check"))

old_reviews_see_more_text = 'style="max-width: 200px; padding: 12px 24px; border-radius: 0;">See More</button>'
new_reviews_see_more_text = 'style="max-width: 200px; padding: 12px 24px; border-radius: 0;">Load More</button>'
replacements.append((old_reviews_see_more_text, new_reviews_see_more_text, "See More -> Load More text"))

old_reviews_loading_text = "seeMoreBtn.textContent = 'See More';"
new_reviews_loading_text = "seeMoreBtn.textContent = 'Load More';"
replacements.append((old_reviews_loading_text, new_reviews_loading_text, "Load More loading text"))

old_reviews_see_less_reset = "visibleCount = 5;"
new_reviews_see_less_reset = "visibleCount = 1;"
replacements.append((old_reviews_see_less_reset, new_reviews_see_less_reset, "See Less count reset"))


# Execute all normal replacements
for old, new, desc in replacements:
    if old in code:
        code = code.replace(old, new)
        print(f"SUCCESS: {desc} applied.")
    else:
        print(f"FAILED: {desc} target not found!")

# Execute last section close replacement
if old_section_close in code:
    code = rreplace(code, old_section_close, new_section_close, 1)
    print("SUCCESS: Size Guide modal HTML added at end.")
else:
    print("FAILED: Size Guide modal HTML ending tag not found!")

# Final sanity check: does it contain {% form 'product' %}, tsukie-add-to-cart-btn, tsukie-buy-now-btn?
has_form_tag = "{% form 'product'" in code
has_add_btn = "tsukie-add-to-cart-btn" in code
has_buy_btn = "tsukie-buy-now-btn" in code

print(f"Form tag check: {has_form_tag}")
print(f"Add to Bag button check: {has_add_btn}")
print(f"Buy Now button check: {has_buy_btn}")

if has_form_tag and has_add_btn and has_buy_btn:
    print("All checks passed! Writing output file...")
    os.makedirs(os.path.dirname(output_pdp_path), exist_ok=True)
    with open(output_pdp_path, "w", encoding="utf-8") as f:
        f.write(code)
    print("Successfully wrote fixed custom liquid scratch file!")
else:
    print("ERROR: Form or buttons are missing! Will not write output.")
