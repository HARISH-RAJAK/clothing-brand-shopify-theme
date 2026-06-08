import json

collection_path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\collection.json'
product_path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\product.json'

# --- Modify collection.json ---
with open(collection_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_start = content.find('{')
comment = content[:json_start]
collection_data = json.loads(content[json_start:])

# 1. Update Hero title custom liquid
hero_liquid = collection_data['sections']['custom_liquid_PzyxTY']['settings']['custom_liquid']

# Replace the gradient styling with solid Navy Blue (#1e2a38)
old_style_substring = ".tsukie-collection-title{"
new_style = """.tsukie-collection-title{
  font-family:'Playfair Display',serif;
  font-size:68px;
  line-height:1;
  font-weight:600;
  font-style:italic;
  margin:0 0 16px;
  color:#1e2a38;
}"""

if old_style_substring in hero_liquid:
    start_idx = hero_liquid.find(old_style_substring)
    end_idx = hero_liquid.find("}", start_idx) + 1
    hero_liquid = hero_liquid[:start_idx] + new_style + hero_liquid[end_idx:]

# Map title to 'The Edit' if it is 'Products'
old_title_code = '<h1 class="tsukie-collection-title">{{ collection.title }}</h1>'
new_title_code = """{%- assign collection_title = collection.title -%}
        {%- if collection_title == 'Products' or collection_title == 'products' -%}
          {%- assign collection_title = 'The Edit' -%}
        {%- endif -%}
        <h1 class="tsukie-collection-title">{{ collection_title }}</h1>"""

hero_liquid = hero_liquid.replace(old_title_code, new_title_code)
collection_data['sections']['custom_liquid_PzyxTY']['settings']['custom_liquid'] = hero_liquid

# 2. Update main section pagination size and native filters
main_section = collection_data['sections']['main']
main_section['settings']['products_per_page'] = 16

filters_block = main_section['blocks']['filters']
filters_block['settings']['enable_filtering'] = True
filters_block['settings']['enable_sorting'] = True
filters_block['settings']['color_scheme'] = "scheme-e5234ede-d196-4b3b-a9e2-6e7d24b8ca5c"

# 3. Add recently_viewed section definition
collection_data['sections']['recently_viewed'] = {
    "type": "tsukie-recently-viewed",
    "settings": {
        "heading": "Recently Viewed"
    }
}

# 4. Update order (remove toolbar, strip, add recently_viewed)
order = collection_data['order']
new_order = []
for section_name in order:
    if section_name in ['custom_liquid_gxTVPP', 'custom_liquid_4jmcfg']:
        continue
    new_order.append(section_name)

# Place recently_viewed before divider_dJVYfB
if 'divider_dJVYfB' in new_order:
    idx = new_order.index('divider_dJVYfB')
    new_order.insert(idx, 'recently_viewed')
else:
    new_order.append('recently_viewed')

collection_data['order'] = new_order

# Write back collection.json
with open(collection_path, 'w', encoding='utf-8') as f:
    f.write(comment + json.dumps(collection_data, indent=2))
print("Updated collection.json successfully!")


# --- Modify product.json ---
with open(product_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_start = content.find('{')
comment = content[:json_start]
product_data = json.loads(content[json_start:])

product_data['sections']['recently_viewed'] = {
    "type": "tsukie-recently-viewed",
    "settings": {
        "heading": "Recently Viewed"
    }
}

p_order = product_data['order']
if 'recently_viewed' not in p_order:
    p_order.append('recently_viewed')
product_data['order'] = p_order

with open(product_path, 'w', encoding='utf-8') as f:
    f.write(comment + json.dumps(product_data, indent=2))
print("Updated product.json successfully!")
