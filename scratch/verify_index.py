import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

json_start = content.find('{')
json_content = content[json_start:]

try:
    data = json.loads(json_content)
    print("[OK] index.json is VALID JSON")
    print(f"   Total sections: {len(data.get('sections', {}))}")
    print(f"   Order count: {len(data.get('order', []))}")
    print()
    
    print("Section order:")
    for i, sec_id in enumerate(data.get('order', []), 1):
        sec = data['sections'].get(sec_id, {})
        sec_type = sec.get('type', '?')
        cl = sec.get('settings', {}).get('custom_liquid', '')
        has_content = f" ({len(cl)} chars)" if cl else ""
        print(f"   {i:2d}. {sec_id} [{sec_type}]{has_content}")
    
    print()
    key_sections = [
        ('custom_liquid_39iRXh', 'Hero Banner'),
        ('custom_liquid_pLiMzL', 'Shop by Collection Head'),
        ('custom_liquid_nc9Wf6', 'Shop by Category Grid'),
        ('custom_liquid_nJYiF7', 'New Arrivals Head'),
        ('custom_liquid_YqjbNx', 'New Arrivals Grid'),
        ('custom_liquid_izaKX4', 'Best Sellers Head'),
        ('custom_liquid_ywjAVh', 'Best Sellers Grid'),
        ('custom_liquid_8xRgKx', 'Best Sellers secondary'),
        ('custom_liquid_dQUmQ6', 'Why Women Love Us'),
        ('custom_liquid_GaLWNF', 'Testimonials'),
        ('custom_liquid_seen_on_real_women', 'Seen on Real Women'),
        ('custom_liquid_MMecBe', 'Style in Motion'),
    ]
    
    print("Key section verification:")
    for sec_id, label in key_sections:
        if sec_id in data['sections']:
            cl = data['sections'][sec_id].get('settings', {}).get('custom_liquid', '')
            has_navy = '#1e2a38' in cl
            has_playfair = 'Playfair Display' in cl
            status_parts = []
            if has_navy: status_parts.append("navy")
            if has_playfair: status_parts.append("playfair")
            status = " | ".join(status_parts) if status_parts else ""
            print(f"   [OK] {label} ({sec_id}) [{len(cl)} chars] {status}")
        else:
            print(f"   [MISSING] {label} ({sec_id})")
    
    print()
    print("Mobile layout checks:")
    for sec_id, label in [('custom_liquid_YqjbNx', 'New Arrivals'), ('custom_liquid_ywjAVh', 'Best Sellers')]:
        cl = data['sections'][sec_id].get('settings', {}).get('custom_liquid', '')
        mobile_part = cl.split('@media(max-width:749px)')[-1] if '@media(max-width:749px)' in cl else ''
        has_vertical = 'grid-template-columns:repeat(2,1fr)' in mobile_part
        has_no_scroll = 'overflow-x:auto' not in mobile_part
        if has_vertical and has_no_scroll:
            print(f"   [OK] {label}: vertical 2-col grid on mobile")
        else:
            print(f"   [WARN] {label}: check mobile layout (vertical={has_vertical}, no-scroll={has_no_scroll})")
    
    nc9 = data['sections']['custom_liquid_nc9Wf6'].get('settings', {}).get('custom_liquid', '')
    if 'display:flex' in nc9 and 'scroll-snap-type:x mandatory' in nc9:
        print(f"   [OK] Shop by Category: horizontal scroll layout")
    
    hero = data['sections']['custom_liquid_39iRXh'].get('settings', {}).get('custom_liquid', '')
    slide_count = hero.count('tsukie-hero-slide"')
    print(f"   [OK] Hero banner: {slide_count} slides found")
    
    # Check badge standardization
    print()
    print("Badge standardization:")
    for sec_id, label in [('custom_liquid_YqjbNx', 'New Arrivals'), ('custom_liquid_ywjAVh', 'Best Sellers'), ('custom_liquid_8xRgKx', 'Best Sellers 2')]:
        cl = data['sections'][sec_id].get('settings', {}).get('custom_liquid', '')
        has_bestsellers = 'Bestsellers</span>' in cl
        has_old_badges = '#1 BESTSELLER' in cl or 'LOW STOCK' in cl or 'badge--new' in cl
        if has_bestsellers and not has_old_badges:
            print(f"   [OK] {label}: uniform Bestsellers badge")
        else:
            print(f"   [WARN] {label}: badge check (new={has_bestsellers}, old_removed={not has_old_badges})")
    
    # Check swatch order (price before swatches)
    print()
    print("Card layout (title > price > swatches):")
    for sec_id, label in [('custom_liquid_YqjbNx', 'New Arrivals'), ('custom_liquid_ywjAVh', 'Best Sellers')]:
        cl = data['sections'][sec_id].get('settings', {}).get('custom_liquid', '')
        price_pos = cl.find('tsukie-product-price')
        swatch_pos = cl.rfind('tsukie-color-swatches')
        if price_pos < swatch_pos and price_pos > 0:
            print(f"   [OK] {label}: price before swatches")
        else:
            print(f"   [WARN] {label}: check order (price@{price_pos}, swatches@{swatch_pos})")

except json.JSONDecodeError as e:
    print(f"[FAIL] JSON PARSE ERROR: {e}")
except Exception as e:
    print(f"[FAIL] ERROR: {e}")
