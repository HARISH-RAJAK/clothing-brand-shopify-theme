import os
import shutil
import glob

brain_dir = r'C:\Users\hp\.gemini\antigravity-ide\brain\8f068730-3b21-43a7-96ee-55f10e6b4b4b'
assets_dir = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\assets'

mapping = {
    'hero_banner_1': 'hero_banner_1.png',
    'hero_banner_2': 'hero_banner_2.png',
    'hero_banner_3': 'hero_banner_3.png',
    'real_women_1': 'real_women_1.png',
    'real_women_2': 'real_women_2.png'
}

for prefix, dest_name in mapping.items():
    search_pattern = os.path.join(brain_dir, f"{prefix}_*.png")
    matches = glob.glob(search_pattern)
    if matches:
        # get the latest match
        src_path = sorted(matches)[-1]
        dest_path = os.path.join(assets_dir, dest_name)
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_path} -> {dest_path}")
    else:
        print(f"No match found for prefix: {prefix}")
