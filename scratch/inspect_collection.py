import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\collection.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

json_start = content.find('{')
data = json.loads(content[json_start:])

print("Section order:")
for i, s in enumerate(data.get('order', []), 1):
    sec = data['sections'].get(s, {})
    sec_type = sec.get('type', '?')
    cl = sec.get('settings', {}).get('custom_liquid', '')
    cl_len = f" ({len(cl)} chars)" if cl else ""
    
    # Check for blocks
    blocks = sec.get('blocks', {})
    block_info = f" [{len(blocks)} blocks]" if blocks else ""
    
    print(f"  {i}. {s} [{sec_type}]{cl_len}{block_info}")
    
    # Print key settings for product-grid or collection-banner type sections
    settings = sec.get('settings', {})
    if sec_type in ('collection-banner', 'product-grid'):
        for k, v in settings.items():
            if k != 'custom_liquid':
                print(f"      {k}: {v}")
    
    # For custom-liquid, show first 200 chars
    if cl:
        snippet = cl[:300].replace('\n', ' ').replace('\r', '')
        print(f"      snippet: {snippet}...")
