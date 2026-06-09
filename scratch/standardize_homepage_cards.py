import json
import re

filepath = r"templates/product.json" # Wait, homepage is index.json!
filepath = r"templates/index.json"

# Read index.json content
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Match and store header comment if present
comment_match = re.match(r'^(/\*.*?\*/\s*)', content, flags=re.DOTALL)
header_comment = comment_match.group(1) if comment_match else ""

# Strip C-style comments to parse JSON
content_clean = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
data = json.loads(content_clean)

# 1. Update custom_liquid_YqjbNx (New Arrivals)
if "custom_liquid_YqjbNx" in data["sections"]:
    sec = data["sections"]["custom_liquid_YqjbNx"]
    liquid = sec["settings"]["custom_liquid"]
    
    start_tag = "{% for product in collections.new-arrivals.products limit: 5 %}"
    end_pattern = "\n    </div>\n    \n    <div class=\"tsukie-viewall-wrapper\">"
    
    start_idx = liquid.find(start_tag)
    end_idx = liquid.find(end_pattern, start_idx)
    
    if start_idx != -1 and end_idx != -1:
        replacement = start_tag + "\n        {% render 'tsukie-product-card', product: product %}\n      {% endfor %}"
        new_liquid = liquid[:start_idx] + replacement + liquid[end_idx:]
        sec["settings"]["custom_liquid"] = new_liquid
        print("Updated custom_liquid_YqjbNx successfully.")
    else:
        print("Could not find loop markers in custom_liquid_YqjbNx.")

# 2. Update custom_liquid_ywjAVh (Best Sellers)
if "custom_liquid_ywjAVh" in data["sections"]:
    sec = data["sections"]["custom_liquid_ywjAVh"]
    liquid = sec["settings"]["custom_liquid"]
    
    start_tag = "{% for product in collections.all.products limit: 4 %}"
    end_pattern = "\n    </div>\n    \n    <div class=\"tsukie-viewall-wrapper\">"
    
    start_idx = liquid.find(start_tag)
    end_idx = liquid.find(end_pattern, start_idx)
    
    if start_idx != -1 and end_idx != -1:
        replacement = start_tag + "\n        {% render 'tsukie-product-card', product: product %}\n      {% endfor %}"
        new_liquid = liquid[:start_idx] + replacement + liquid[end_idx:]
        sec["settings"]["custom_liquid"] = new_liquid
        print("Updated custom_liquid_ywjAVh successfully.")
    else:
        print("Could not find loop markers in custom_liquid_ywjAVh.")

# 3. Update custom_liquid_8xRgKx (Best Sellers Alternative)
if "custom_liquid_8xRgKx" in data["sections"]:
    sec = data["sections"]["custom_liquid_8xRgKx"]
    liquid = sec["settings"]["custom_liquid"]
    
    start_tag = "{% for product in collections.all.products limit: 4 %}"
    end_pattern = "\n    </div>\n  </div>\n</div>"
    
    start_idx = liquid.find(start_tag)
    end_idx = liquid.find(end_pattern, start_idx)
    
    if start_idx != -1 and end_idx != -1:
        replacement = start_tag + "\n        {% render 'tsukie-product-card', product: product %}\n      {% endfor %}"
        new_liquid = liquid[:start_idx] + replacement + liquid[end_idx:]
        sec["settings"]["custom_liquid"] = new_liquid
        print("Updated custom_liquid_8xRgKx successfully.")
    else:
        print("Could not find loop markers in custom_liquid_8xRgKx.")

# Convert back to JSON string
json_str = json.dumps(data, indent=2, ensure_ascii=False)

# Write back with header comment
with open(filepath, "w", encoding="utf-8") as f:
    f.write(header_comment + json_str + "\n")

print("templates/index.json updated successfully!")
