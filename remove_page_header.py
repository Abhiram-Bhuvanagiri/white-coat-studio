import os, re

for f in os.scandir('.'):
    if f.is_file() and f.name.endswith('.html'):
        data = open(f.path, 'r', encoding='utf-8').read()
        # Find the page-header section and remove it
        new_data = re.sub(r'<!--Page Header Start-->.*?<!--Page Header End-->\s*', '', data, flags=re.DOTALL | re.IGNORECASE)
        # If the comments aren't there, just match the section
        if new_data == data:
            new_data = re.sub(r'<section class="page-header">.*?</section>\s*', '', data, flags=re.DOTALL)
        
        if data != new_data:
            open(f.path, 'w', encoding='utf-8').write(new_data)
            print('Removed page-header in ' + f.name)
