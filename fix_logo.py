import os, glob
for filepath in glob.glob('**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_style = 'max-width: 150px; height: auto;'
    new_style = 'max-width: 190px; height: auto;'
    
    if old_style in content:
        new_content = content.replace(old_style, new_style)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filepath}')
