import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
json_content = content[json_start:]
data = json.loads(json_content)

for key, sec in data.get('sections', {}).items():
    if sec.get('type') == 'divider':
        print(f"Divider {key}: Settings: {sec.get('settings')}")
