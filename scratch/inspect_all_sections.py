import json
import os
import sys

path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\templates\index.json'
out_path = r'c:\Users\hp\Downloads\theme_export__tsukie-in-horizon__08JUN2026-0346pm\scratch\section_details.txt'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    
json_start = content.find('{')
comment = content[:json_start]
json_content = content[json_start:]
data = json.loads(json_content)

with open(out_path, 'w', encoding='utf-8') as out_f:
    out_f.write("Homepage Section Order:\n")
    out_f.write(str(data.get('order', [])) + "\n")
    
    for sec_id in data.get('order', []):
        sec = data.get('sections', {}).get(sec_id, {})
        out_f.write(f"\n=================== Section: {sec_id} ===================\n")
        out_f.write(f"Name: {sec.get('name')}\n")
        out_f.write(f"Type: {sec.get('type')}\n")
        custom_liquid = sec.get('settings', {}).get('custom_liquid', '')
        out_f.write(f"Content Length: {len(custom_liquid)} chars\n")
        lines = custom_liquid.split('\n')
        # Print first 20 lines
        out_f.write("First 20 lines of custom liquid:\n")
        for line in lines[:20]:
            out_f.write(f"  {line}\n")
            
        headings = []
        for line in lines:
            if 'class=' in line or 'h1' in line or 'h2' in line or 'h3' in line or 'h4' in line:
                headings.append(line.strip()[:150])
        if headings:
            out_f.write("Headings/HTML elements:\n")
            for h in headings[:20]:
                out_f.write(f"  {h}\n")
