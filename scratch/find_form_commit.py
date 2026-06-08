import subprocess
import json

def get_commits():
    output = subprocess.check_output(['git', 'log', '--format=%H %s']).decode('utf-8')
    commits = []
    for line in output.strip().splitlines():
        parts = line.split(' ', 1)
        if len(parts) == 2:
            commits.append((parts[0], parts[1]))
    return commits

def check_commit_json(commit_hash):
    try:
        content_bytes = subprocess.check_output(['git', 'show', f'{commit_hash}:templates/product.json'])
        lines = content_bytes.decode('utf-8').splitlines()
        clean = '\n'.join(line for line in lines if not line.strip().startswith('/*') and not line.strip().startswith('*') and not line.strip().startswith('*/'))
        data = json.loads(clean)
        for section_id, section in data.get('sections', {}).items():
            if section_id == 'custom_liquid_rW9bhR':
                custom_liquid = section.get('settings', {}).get('custom_liquid', '')
                has_form = '{% form' in custom_liquid.lower()
                return has_form, len(custom_liquid)
    except Exception as e:
        pass
    return False, 0

commits = get_commits()
print("Searching commits...")
for h, msg in commits:
    has_form, length = check_commit_json(h)
    if has_form:
        print(f"Commit {h[:8]} ({msg}): Has {{% form in custom_liquid_rW9bhR (length: {length})")
    else:
        print(f"Commit {h[:8]} ({msg}): NO {{% form in custom_liquid_rW9bhR (length: {length})")
