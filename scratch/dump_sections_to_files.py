import json
import os

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'
scratch_dir = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\scratch'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
json_content = content[json_start:]
data = json.loads(json_content)

for sec_id, sec in data.get('sections', {}).items():
    custom_liquid = sec.get('settings', {}).get('custom_liquid', '')
    if custom_liquid:
        file_path = os.path.join(scratch_dir, f"{sec_id}.liquid")
        with open(file_path, 'w', encoding='utf-8') as sf:
            sf.write(custom_liquid)
        print(f"Wrote {sec_id} content to {file_path}")
