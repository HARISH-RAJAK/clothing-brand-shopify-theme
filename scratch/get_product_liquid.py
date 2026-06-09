import json
import os
import re

filepath = r"c:/Users/hp/Downloads/theme_export__tsukie-in-horizon__08JUN2026-0346pm/templates/product.json"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Strip C-style comments
content_clean = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

data = json.loads(content_clean)

custom_liquid = data["sections"]["custom_liquid_rW9bhR"]["settings"]["custom_liquid"]

out_path = r"c:/Users/hp/Downloads/theme_export__tsukie-in-horizon__08JUN2026-0346pm/scratch/pdp_extracted.liquid"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(custom_liquid)

print("Extracted successfully to scratch/pdp_extracted.liquid!")
