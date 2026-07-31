import glob

html_files = glob.glob('*.html')
html_files += glob.glob('assets/inc/template/*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    if "Copyright @ 2026 Whitecode Solutions, All rights reserved." in content:
        content = content.replace("Copyright @ 2026 Whitecode Solutions, All rights reserved.", "Copyright @ 2026 Dexze, All rights reserved.")
        modified = True
        
    if "Copyright @ 2026 White Coat Studio, All rights reserved." in content:
        content = content.replace("Copyright @ 2026 White Coat Studio, All rights reserved.", "Copyright @ 2026 Dexze, All rights reserved.")
        modified = True

    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
