import glob

html_files = glob.glob('*.html')
html_files += glob.glob('assets/inc/template/*.html')

old_text = 'copyrights all rights reserved @2026 by <a href="index.html">white coat Studio</a> , powered by <a href="https://dexze.com/" target="_blank">Dexze</a>'
new_text = '&copy; 2026 <a href="index.html">White Coat Studio</a>. All rights reserved. Powered by <a href="https://dexze.com/" target="_blank">Dexze</a>.'

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
