import os, re

# Read index.html to get the reference headers
index_data = open('index.html', 'r', encoding='utf-8').read()

header_match = re.search(r'(<header.*?</header>)', index_data, re.DOTALL)
stricky_match = re.search(r'(<div class="stricky-header.*?</div><!-- /\.[^>]*>)', index_data, re.DOTALL)

if not header_match or not stricky_match:
    print("Could not find headers in index.html")
    exit(1)

new_header = header_match.group(1)
new_stricky = stricky_match.group(1)

# Files to update
inner_pages = [
    'about.html',
    'contact.html',
    'service-details.html',
    'services-carousel.html',
    'services.html'
]

for f_name in inner_pages:
    if os.path.exists(f_name):
        data = open(f_name, 'r', encoding='utf-8').read()
        
        # Replace the <header> block
        data = re.sub(r'<header.*?</header>', new_header, data, flags=re.DOTALL)
        
        # Replace the stricky-header block
        data = re.sub(r'<div class="stricky-header.*?</div><!-- /\.[^>]*>', new_stricky, data, flags=re.DOTALL)
        
        # Completely remove the page-header section
        data = re.sub(r'<!--Page Header Start-->.*?<!--Page Header End-->\s*', '', data, flags=re.DOTALL | re.IGNORECASE)
        
        open(f_name, 'w', encoding='utf-8').write(data)
        print('Unified headers in ' + f_name)
