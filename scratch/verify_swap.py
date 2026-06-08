import json

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

d = json.loads(content[content.find('{'):])

print("Section order:")
for i, s in enumerate(d['order'], 1):
    sec_type = d['sections'][s]['type']
    print(f"  {i}. {s} [{sec_type}]")

print()
h = d['sections']['tsukie_hero_banner']
print(f"Hero: type={h['type']}, blocks={list(h['blocks'].keys())}")

w = d['sections']['tsukie_seen_on_real_women']
print(f"Women: type={w['type']}, blocks={list(w['blocks'].keys())}")

# Confirm old sections are gone
print()
print(f"Old hero gone: {'custom_liquid_39iRXh' not in d['sections']}")
print(f"Old women gone: {'custom_liquid_seen_on_real_women' not in d['sections']}")
