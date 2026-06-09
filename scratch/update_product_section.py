import os

txt_path = r"c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\1234.txt"
section_path = r"c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\sections\tsukie-product-details.liquid"

# Read 1234.txt
with open(txt_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the PNG badges style and HTML
badges_code = """      <!-- 1. PNG Trust Badges Section -->
      <style>
        .tsukie-pdp-badges {
          display: flex;
          flex-wrap: wrap;
          justify-content: flex-start;
          gap: 12px;
          margin-top: 14px;
          margin-bottom: 24px;
          width: 100%;
        }
        .tsukie-pdp-badge {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          background-color: transparent;
          padding: 0px;
          border-radius: 6px;
          flex: 0 0 auto !important;
          width: fit-content;
          max-width: 100%;
        }
        .tsukie-pdp-badge img {
          height: 18px !important;
          width: auto !important;
          object-fit: contain;
          flex-shrink: 0;
          image-rendering: -webkit-optimize-contrast;
        }
      </style>
      <div class="tsukie-pdp-badges">
        <div class="tsukie-pdp-badge">
          <img src="//tsukie.in/cdn/shop/files/1-01.png?v=1776420000&width=200" alt="Free Shipping" width="100" height="23" loading="lazy">
        </div>
        <div class="tsukie-pdp-badge">
          <img src="//tsukie.in/cdn/shop/files/1-03.png?v=1776420000&width=200" alt="7 Days Return" width="100" height="23" loading="lazy">
        </div>
        <div class="tsukie-pdp-badge">
          <img src="//tsukie.in/cdn/shop/files/1-02.png?v=1776419999&width=200" alt="Secure Payment" width="100" height="23" loading="lazy">
        </div>
      </div>"""

# 1. Replace the EMI CSS rules
emi_css = """.tsukie-emi{
  font-family:'Montserrat',sans-serif;
  font-size:12px;
  color:#666;
  margin-bottom:24px;
}
.tsukie-emi strong{color:#1e2a38;font-weight:500}"""

content = content.replace(emi_css, "")

# 2. Replace the EMI HTML block
emi_html = """      <div class="tsukie-emi">
        or <strong id="tsukie-emi-price">{{ product.selected_or_first_available_variant.price | divided_by: 3 | money }}/month</strong> with easy EMI
      </div>"""

content = content.replace(emi_html, badges_code)

# 3. Append schema block at the bottom
schema_block = """
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

content = content.strip() + "\\n" + schema_block

# Write to sections/tsukie-product-details.liquid
with open(section_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("tsukie-product-details.liquid updated successfully!")
