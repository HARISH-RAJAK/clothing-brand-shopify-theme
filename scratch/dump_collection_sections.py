import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\collection.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

json_start = content.find('{')
data = json.loads(content[json_start:])

# Dump each custom liquid section to a file
for sec_id, sec in data.get('sections', {}).items():
    cl = sec.get('settings', {}).get('custom_liquid', '')
    if cl:
        out_path = f'scratch/collection_{sec_id}.liquid'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(cl)
        print(f"Dumped {sec_id} -> {out_path} ({len(cl)} chars)")
    
    # Also dump main section settings
    if sec.get('type') == 'main-collection':
        print(f"\nmain-collection settings:")
        for k, v in sec.get('settings', {}).items():
            print(f"  {k}: {v}")
        print(f"\nmain-collection blocks:")
        for bk, bv in sec.get('blocks', {}).items():
            print(f"  {bk}: type={bv.get('type')}, settings={bv.get('settings', {})}")
