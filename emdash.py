import os
import glob

chapters_dir = os.path.join(os.path.dirname(__file__), 'chapters')

for filepath in glob.glob(os.path.join(chapters_dir, '*.tex')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('--', '\\textemdash{}')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")