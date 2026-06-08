import os
import re

theme_dir = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm'

for root, dirs, files in os.walk(theme_dir):
    if '.git' in root or 'scratch' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.liquid') or file.endswith('.json'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if 'tsukie-product-card' in content:
                    print(f"Found tsukie-product-card in {os.path.relpath(path, theme_dir)}")
                if 'tsukie-color-swatches' in content:
                    print(f"Found tsukie-color-swatches in {os.path.relpath(path, theme_dir)}")
