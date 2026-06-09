import os

in_path = r"c:/Users/hp/Downloads/theme_export__tsukie-in-horizon__08JUN2026-0346pm/scratch/pdp_extracted.liquid"
out_path = r"c:/Users/hp/Downloads/theme_export__tsukie-in-horizon__08JUN2026-0346pm/sections/tsukie-product-details.liquid"

with open(in_path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace size guide link
old_size_guide = """                  {% if option.name == 'Size' or option.name == 'Size/Fits' or option.name == 'Fit' %}
                    <span style="color:#d4c5a9;">|</span>
                    <a href="#" onclick="tsukieOpenSizeGuide(event)" class="tsukie-size-guide-link" style="color:#a08766; text-decoration:underline; font-size:11px; font-family:'Montserrat',sans-serif; text-transform:uppercase; font-weight:600; letter-spacing:1px;">Size Guide</a>
                  {% endif %}"""

new_size_guide = """                  {% if option.name == 'Size' or option.name == 'Size/Fits' or option.name == 'Fit' %}
                    {% if section.settings.show_size_guide %}
                      <span style="color:#d4c5a9;">|</span>
                      <a href="#" onclick="tsukieOpenSizeGuide(event)" class="tsukie-size-guide-link" style="color:#a08766; text-decoration:underline; font-size:11px; font-family:'Montserrat',sans-serif; text-transform:uppercase; font-weight:600; letter-spacing:1px;">Size Guide</a>
                    {% endif %}
                  {% endif %}"""

code = code.replace(old_size_guide, new_size_guide)

# Replace inventory message
old_inventory = """        <div class="tsukie-inventory" id="tsukie-inventory" {% if product.selected_or_first_available_variant.inventory_management and product.selected_or_first_available_variant.inventory_quantity < 10 and product.selected_or_first_available_variant.inventory_quantity > 0 %}{% else %}style="display:none"{% endif %}>
          Only <span id="tsukie-nav-qty">{{ product.selected_or_first_available_variant.inventory_quantity }}</span> left in stock
        </div>"""

new_inventory = """        {% if section.settings.show_inventory_urgency %}
        <div class="tsukie-inventory" id="tsukie-inventory" {% if product.selected_or_first_available_variant.inventory_management and product.selected_or_first_available_variant.inventory_quantity < 10 and product.selected_or_first_available_variant.inventory_quantity > 0 %}{% else %}style="display:none"{% endif %}>
          Only <span id="tsukie-nav-qty">{{ product.selected_or_first_available_variant.inventory_quantity }}</span> left in stock
        </div>
        {% endif %}"""

code = code.replace(old_inventory, new_inventory)

# Replace special offers
old_offers = """        {% assign offer1_code = product.metafields.custom.offer_1_code | default: 'TSUKIE10' %}
        {% assign offer1_text = product.metafields.custom.offer_1_text | default: 'Buy 1 get 10% off' %}
        {% assign offer2_code = product.metafields.custom.offer_2_code | default: 'TSUKIE25' %}
        {% assign offer2_text = product.metafields.custom.offer_2_text | default: 'Buy 2 get 25% off' %}
        <div class="tsukie-special-offers-strip">
          <div class="tsukie-offers-title">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581a1.125 1.125 0 001.59 0l4.318-4.318a1.125 1.125 0 000-1.59l-9.58-9.581a1.125 1.125 0 00-1.591-.659zm5.432 4.5a1.125 1.125 0 11-2.25 0 1.125 1.125 0 012.25 0z" /></svg>
            Special Offers
          </div>
          <div class="tsukie-offers-strip-items">
            <div class="tsukie-offer-strip-item" onclick="tsukieCopyCode(this, '{{ offer1_code }}')" title="Click to copy {{ offer1_code }}">
              <span><strong>{{ offer1_code }}</strong>: {{ offer1_text }}</span>
              <span class="copy-lbl">Copy</span>
            </div>
            <div class="tsukie-offer-strip-item" onclick="tsukieCopyCode(this, '{{ offer2_code }}')" title="Click to copy {{ offer2_code }}">
              <span><strong>{{ offer2_code }}</strong>: {{ offer2_text }}</span>
              <span class="copy-lbl">Copy</span>
            </div>
          </div>
        </div>"""

new_offers = """        {% assign offer1_code = product.metafields.custom.offer_1_code | default: section.settings.default_offer1_code | default: 'TSUKIE10' %}
        {% assign offer1_text = product.metafields.custom.offer_1_text | default: section.settings.default_offer1_text | default: 'Buy 1 get 10% off' %}
        {% assign offer2_code = product.metafields.custom.offer_2_code | default: section.settings.default_offer2_code | default: 'TSUKIE25' %}
        {% assign offer2_text = product.metafields.custom.offer_2_text | default: section.settings.default_offer2_text | default: 'Buy 2 get 25% off' %}
        {% if section.settings.show_special_offers %}
        <div class="tsukie-special-offers-strip">
          <div class="tsukie-offers-title">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581a1.125 1.125 0 001.59 0l4.318-4.318a1.125 1.125 0 000-1.59l-9.58-9.581a1.125 1.125 0 00-1.591-.659zm5.432 4.5a1.125 1.125 0 11-2.25 0 1.125 1.125 0 012.25 0z" /></svg>
            Special Offers
          </div>
          <div class="tsukie-offers-strip-items">
            <div class="tsukie-offer-strip-item" onclick="tsukieCopyCode(this, '{{ offer1_code }}')" title="Click to copy {{ offer1_code }}">
              <span><strong>{{ offer1_code }}</strong>: {{ offer1_text }}</span>
              <span class="copy-lbl">Copy</span>
            </div>
            <div class="tsukie-offer-strip-item" onclick="tsukieCopyCode(this, '{{ offer2_code }}')" title="Click to copy {{ offer2_code }}">
              <span><strong>{{ offer2_code }}</strong>: {{ offer2_text }}</span>
              <span class="copy-lbl">Copy</span>
            </div>
          </div>
        </div>
        {% endif %}"""

code = code.replace(old_offers, new_offers)

# Replace order status timeline
old_status = """      <div class="tsukie-order-status-v2">
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

new_status = """      {% if section.settings.show_order_status %}
      <div class="tsukie-order-status-v2">
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
      </div>
      {% endif %}"""

code = code.replace(old_status, new_status)

# Replace trust feature items
old_features = """      <div class="tsukie-features">
        <div class="tsukie-feature">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
          <div class="tsukie-feature-title">PREMIUM FABRIC</div>
          <div class="tsukie-feature-text">100% Viscose</div>
        </div>
        <div class="tsukie-feature">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 4v5h.582m15.356 2A8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 0 01-15.357-2m15.357 2H15"></path></svg>
          <div class="tsukie-feature-title">EASY EXCHANGE</div>
          <div class="tsukie-feature-text">14 days</div>
        </div>
        <div class="tsukie-feature">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
          <div class="tsukie-feature-title">SECURE PAYMENT</div>
          <div class="tsukie-feature-text">UPI · Cards · COD</div>
        </div>
      </div>"""

new_features = """      <div class="tsukie-features">
        <div class="tsukie-feature">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
          <div class="tsukie-feature-title">{{ section.settings.feature1_title }}</div>
          <div class="tsukie-feature-text">{{ section.settings.feature1_desc }}</div>
        </div>
        <div class="tsukie-feature">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 4v5h.582m15.356 2A8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 0 01-15.357-2m15.357 2H15"></path></svg>
          <div class="tsukie-feature-title">{{ section.settings.feature2_title }}</div>
          <div class="tsukie-feature-text">{{ section.settings.feature2_desc }}</div>
        </div>
        <div class="tsukie-feature">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
          <div class="tsukie-feature-title">{{ section.settings.feature3_title }}</div>
          <div class="tsukie-feature-text">{{ section.settings.feature3_desc }}</div>
        </div>
      </div>"""

code = code.replace(old_features, new_features)

schema_code = """
{% schema %}
{
  "name": "Tsukie Product Details",
  "tag": "section",
  "class": "shopify-section-tsukie-product",
  "settings": [
    {
      "type": "header",
      "content": "Product Information Settings"
    },
    {
      "type": "checkbox",
      "id": "show_size_guide",
      "label": "Show Size Guide Link",
      "default": true
    },
    {
      "type": "checkbox",
      "id": "show_inventory_urgency",
      "label": "Show Inventory Urgency Message",
      "default": true
    },
    {
      "type": "header",
      "content": "Special Offers Strip"
    },
    {
      "type": "checkbox",
      "id": "show_special_offers",
      "label": "Show Special Offers Strip",
      "default": true
    },
    {
      "type": "text",
      "id": "default_offer1_code",
      "label": "Fallback Offer 1 Code",
      "default": "TSUKIE10"
    },
    {
      "type": "text",
      "id": "default_offer1_text",
      "label": "Fallback Offer 1 Text",
      "default": "Buy 1 get 10% off"
    },
    {
      "type": "text",
      "id": "default_offer2_code",
      "label": "Fallback Offer 2 Code",
      "default": "TSUKIE25"
    },
    {
      "type": "text",
      "id": "default_offer2_text",
      "label": "Fallback Offer 2 Text",
      "default": "Buy 2 get 25% off"
    },
    {
      "type": "header",
      "content": "Order Status Timeline"
    },
    {
      "type": "checkbox",
      "id": "show_order_status",
      "label": "Show Order Status Tracker",
      "default": true
    },
    {
      "type": "header",
      "content": "Trust Badges Section"
    },
    {
      "type": "text",
      "id": "feature1_title",
      "label": "Feature 1 Title",
      "default": "PREMIUM FABRIC"
    },
    {
      "type": "text",
      "id": "feature1_desc",
      "label": "Feature 1 Description",
      "default": "100% Viscose"
    },
    {
      "type": "text",
      "id": "feature2_title",
      "label": "Feature 2 Title",
      "default": "EASY EXCHANGE"
    },
    {
      "type": "text",
      "id": "feature2_desc",
      "label": "Feature 2 Description",
      "default": "14 days"
    },
    {
      "type": "text",
      "id": "feature3_title",
      "label": "Feature 3 Title",
      "default": "SECURE PAYMENT"
    },
    {
      "type": "text",
      "id": "feature3_desc",
      "label": "Feature 3 Description",
      "default": "UPI · Cards · COD"
    }
  ]
}
{% endschema %}
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(code + schema_code)

print("Product details section file created successfully!")
