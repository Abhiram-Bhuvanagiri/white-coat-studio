import os, re

for f in os.scandir('.'):
    if f.is_file() and f.name.endswith('.html'):
        data = open(f.path, 'r', encoding='utf-8').read()
        
        # We want to replace the contents of page-header__inner with nothing, so it's just an empty div
        new_data = re.sub(r'(<div class="page-header__inner">).*?(</div>\s*</div>\s*</section>)', r'\1\2', data, flags=re.DOTALL)
        
        if data != new_data:
            open(f.path, 'w', encoding='utf-8').write(new_data)
            print('Cleaned header in ' + f.name)
