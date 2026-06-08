import json
import os

# Paths
json_path = "templates/product.json"
liquid_path = "scratch/custom_liquid_rW9bhR.liquid"

if not os.path.exists(liquid_path):
    print(f"Error: {liquid_path} does not exist.")
    exit(1)

# Read product.json
with open(json_path, "r", encoding="utf-8") as f:
    orig_content = f.read()

# Separate comment and JSON
first_brace = orig_content.find("{")
comment_part = orig_content[:first_brace]
json_part = orig_content[first_brace:]

# Load JSON
data = json.loads(json_part)

# Read modified liquid
with open(liquid_path, "r", encoding="utf-8") as f:
    modified_liquid = f.read()

# Update JSON
data["sections"]["custom_liquid_rW9bhR"]["settings"]["custom_liquid"] = modified_liquid

# Save back
updated_json = json.dumps(data, indent=2, ensure_ascii=False)
final_content = comment_part + updated_json

with open(json_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print("Merged clean custom liquid code successfully back into templates/product.json!")
