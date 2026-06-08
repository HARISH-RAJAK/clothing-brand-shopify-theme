import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

json_start = content.find('{')
comment = content[:json_start]
json_content = content[json_start:]
data = json.loads(json_content)

# ---- 1. Replace custom_liquid_39iRXh (Hero) with tsukie-hero-banner section ----
old_hero_id = 'custom_liquid_39iRXh'
new_hero_id = 'tsukie_hero_banner'

# Create new section entry
data['sections'][new_hero_id] = {
    "type": "tsukie-hero-banner",
    "blocks": {
        "slide_1": {
            "type": "slide",
            "settings": {
                "eyebrow": "SUMMER 2026 COLLECTION",
                "heading": "Dressed for the woman you already are",
                "description": "Premium silhouettes crafted for the modern Indian woman \u2014 luxurious fabrics, thoughtful fit, and enduring style. Starting at \u20b91,499.",
                "button_text": "SHOP NEW ARRIVALS",
                "button_url": "/collections/new-arrivals"
            }
        },
        "slide_2": {
            "type": "slide",
            "settings": {
                "eyebrow": "CHIC & ELEGANT",
                "heading": "Style in Peplum & Flared Tops",
                "description": "Discover curated sets and tops designed for comfort, grace, and premium everyday wear.",
                "button_text": "EXPLORE BEST SELLERS",
                "button_url": "/collections/all"
            }
        },
        "slide_3": {
            "type": "slide",
            "settings": {
                "eyebrow": "ESSENTIAL LUXURY",
                "heading": "Timeless Pieces For Your Wardrobe",
                "description": "Crafted with love, highlighting the natural body shape in sizes from XS to 4XL.",
                "button_text": "VIEW ALL COLLECTIONS",
                "button_url": "/collections"
            }
        }
    },
    "block_order": ["slide_1", "slide_2", "slide_3"],
    "settings": {}
}

# Replace in order array
order_list = data.get('order', [])
if old_hero_id in order_list:
    idx = order_list.index(old_hero_id)
    order_list[idx] = new_hero_id
    # Remove the old section
    if old_hero_id in data['sections']:
        del data['sections'][old_hero_id]
    print(f"Replaced {old_hero_id} with {new_hero_id} in order at position {idx}")

# ---- 2. Replace custom_liquid_seen_on_real_women with tsukie-seen-on-real-women ----
old_women_id = 'custom_liquid_seen_on_real_women'
new_women_id = 'tsukie_seen_on_real_women'

data['sections'][new_women_id] = {
    "type": "tsukie-seen-on-real-women",
    "blocks": {
        "item_1": {
            "type": "image_item",
            "settings": {
                "tag": "@PRIYA_ANAND"
            }
        },
        "item_2": {
            "type": "video_item",
            "settings": {
                "tag": "@ANJALI.S"
            }
        },
        "item_3": {
            "type": "image_item",
            "settings": {
                "tag": "@MEERA_M"
            }
        },
        "item_4": {
            "type": "video_item",
            "settings": {
                "tag": "@RIYA.SEN"
            }
        }
    },
    "block_order": ["item_1", "item_2", "item_3", "item_4"],
    "settings": {
        "eyebrow": "AS SEEN ON YOU",
        "heading": "Seen on Real Women",
        "description": "Candid moments of real women styling our timeless silhouettes. Tag us at #TsukieWomen to get featured."
    }
}

if old_women_id in order_list:
    idx = order_list.index(old_women_id)
    order_list[idx] = new_women_id
    if old_women_id in data['sections']:
        del data['sections'][old_women_id]
    print(f"Replaced {old_women_id} with {new_women_id} in order at position {idx}")

# Write back
with open(path, 'w', encoding='utf-8') as f:
    f.write(comment + json.dumps(data, indent=2, ensure_ascii=False))

print("Done! Both sections are now dynamic Shopify sections.")
