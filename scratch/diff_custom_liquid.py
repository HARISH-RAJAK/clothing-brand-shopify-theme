import subprocess
import json
import difflib

def get_liquid_content(commit_hash):
    content_bytes = subprocess.check_output(['git', 'show', f'{commit_hash}:templates/product.json'])
    lines = content_bytes.decode('utf-8').splitlines()
    clean = '\n'.join(line for line in lines if not line.strip().startswith('/*') and not line.strip().startswith('*') and not line.strip().startswith('*/'))
    data = json.loads(clean)
    return data['sections']['custom_liquid_rW9bhR']['settings']['custom_liquid']

c1 = get_liquid_content('0afacbc')
c2 = get_liquid_content('52cd9be')

diff = list(difflib.unified_diff(c1.splitlines(), c2.splitlines(), fromfile='0afacbc', tofile='52cd9be'))
print('\n'.join(diff[:200])) # Show first 200 lines of diff
