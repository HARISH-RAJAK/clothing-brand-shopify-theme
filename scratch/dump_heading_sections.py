import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
json_content = content[json_start:]
data = json.loads(json_content)

sections_to_dump = ['custom_liquid_pLiMzL', 'custom_liquid_nJYiF7', 'custom_liquid_izaKX4', 'custom_liquid_8xRgKx', 'custom_liquid_MMecBe']

for sec_id in sections_to_dump:
    sec = data.get('sections', {}).get(sec_id, {})
    print(f"\n=================== Section: {sec_id} ===================")
    print(f"Name: {sec.get('name')}")
    print(sec.get('settings', {}).get('custom_liquid', ''))
