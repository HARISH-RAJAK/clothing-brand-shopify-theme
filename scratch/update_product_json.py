import json
import re

filepath = r"c:/Users/hp/Downloads/theme_export__tsukie-in-horizon__08JUN2026-0346pm/templates/product.json"

# Read product.json content
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Match and store header comment if present
comment_match = re.match(r'^(/\*.*?\*/\s*)', content, flags=re.DOTALL)
header_comment = comment_match.group(1) if comment_match else ""

# Strip C-style comments to parse JSON
content_clean = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
data = json.loads(content_clean)

# Delete custom_liquid_rW9bhR if present
if "custom_liquid_rW9bhR" in data["sections"]:
    del data["sections"]["custom_liquid_rW9bhR"]

# Add product_details section
data["sections"]["product_details"] = {
    "type": "tsukie-product-details",
    "settings": {
        "show_size_guide": True,
        "show_inventory_urgency": True,
        "show_special_offers": True,
        "default_offer1_code": "TSUKIE10",
        "default_offer1_text": "Buy 1 get 10% off",
        "default_offer2_code": "TSUKIE25",
        "default_offer2_text": "Buy 2 get 25% off",
        "show_order_status": True,
        "feature1_title": "PREMIUM FABRIC",
        "feature1_desc": "100% Viscose",
        "feature2_title": "EASY EXCHANGE",
        "feature2_desc": "14 days",
        "feature3_title": "SECURE PAYMENT",
        "feature3_desc": "UPI · Cards · COD"
    }
}

# Update order list
if "order" in data:
    new_order = []
    for item in data["order"]:
        if item == "custom_liquid_rW9bhR":
            new_order.append("product_details")
        else:
            new_order.append(item)
    data["order"] = new_order

# Convert back to JSON string
json_str = json.dumps(data, indent=2, ensure_ascii=False)

# Write back with header comment
with open(filepath, "w", encoding="utf-8") as f:
    f.write(header_comment + json_str + "\n")

print("templates/product.json updated successfully!")
