import json
import os

def check_json(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    clean = '\n'.join(line for line in lines if not line.strip().startswith('/*') and not line.strip().startswith('*') and not line.strip().startswith('*/'))
    data = json.loads(clean)
    for section_id, section in data.get('sections', {}).items():
        custom_liquid = section.get('settings', {}).get('custom_liquid', '')
        if not custom_liquid:
            continue
        has_form = '{% form' in custom_liquid.lower()
        has_buy = 'buy' in custom_liquid.lower()
        has_cart = 'cart' in custom_liquid.lower()
        if has_form or has_buy or has_cart:
            print(f"Section {section_id}:")
            print(f"  Length: {len(custom_liquid)} chars")
            print(f"  Has form tag: {has_form}")
            print(f"  Has 'buy': {has_buy}")
            print(f"  Has 'cart': {has_cart}")
            if 'form' in custom_liquid.lower():
                print(f"  Has 'form' word: True")

print("--- Inspecting current templates/product.json ---")
check_json('templates/product.json')
