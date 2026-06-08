import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\product.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

json_start = content.find('{')
data = json.loads(content[json_start:])

for s_name in ['custom_liquid_fcYHbw', 'custom_liquid_GTJVJL']:
    if s_name in data['sections']:
        section = data['sections'][s_name]
        code = section['settings'].get('custom_liquid', '')
        with open(f'scratch/{s_name}.liquid', 'w', encoding='utf-8') as out:
            out.write(code)
        print(f"Dumped {s_name} to scratch/{s_name}.liquid")
