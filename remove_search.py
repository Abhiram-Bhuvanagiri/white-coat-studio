import glob

html_files = glob.glob('*.html')
html_files += glob.glob('assets/inc/template/*.html')

search_block = """<div class="main-menu__search-box">
<a class="main-menu__search searcher-toggler-box fal fa-search" href="#"></a>
</div>"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if search_block in content:
        content = content.replace(search_block, "")
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Removed search from {f}")
