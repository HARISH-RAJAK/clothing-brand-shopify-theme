import json
import re

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
json_content = content[json_start:]
data = json.loads(json_content)

for sec_id, sec in data.get('sections', {}).items():
    custom_liquid = sec.get('settings', {}).get('custom_liquid', '')
    if not custom_liquid:
        continue
    # find images or urls
    urls = re.findall(r'https?://[^\s"\'\(\)]+', custom_liquid)
    img_tags = re.findall(r'<img[^>]+>', custom_liquid)
    if urls or img_tags:
        print(f"Section {sec_id} ({sec.get('name')}):")
        if urls:
            print("  URLs:", urls)
        if img_tags:
            print("  Images:", img_tags)
