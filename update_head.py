import glob
import os
import re

old_head = """<title>White Coat Solutions | Medical Marketing Agency</title>
<!-- favicons Icons -->
<link href="assets/images/favicons/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="assets/images/favicons/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="assets/images/favicons/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="assets/images/favicons/site.webmanifest" rel="manifest"/>"""

new_head = """<title>White Coat Studio | Medical Marketing Agency</title>
<!-- favicons Icons -->
<link href="assets/logo/white-coat.png" rel="icon" type="image/png"/>
<link href="assets/logo/white-coat.png" rel="apple-touch-icon"/>"""

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if old_head in content:
        content = content.replace(old_head, new_head)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Could not find exact block in {f}, skipping...")
