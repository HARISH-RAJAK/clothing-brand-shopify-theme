import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\product.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
json_content = content[json_start:]
data = json.loads(json_content)

for key, sec in data.get('sections', {}).items():
    custom_liquid = sec.get('settings', {}).get('custom_liquid', '')
    if 'tsukie-color-swatches' in custom_liquid or 'tsukie-product-card' in custom_liquid:
        print(f"Section {key}: Name: {sec.get('name')}, Type: {sec.get('type')}")
        print("Length:", len(custom_liquid))
        # Print snippet of swatches
        idx = custom_liquid.find('tsukie-color-swatches')
        print("Snippet near swatches:", custom_liquid[idx-200:idx+300])
