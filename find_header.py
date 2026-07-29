import re
with open('about.html', 'r', encoding='utf-8') as f:
    data = f.read()

m = re.search(r'<section [^>]*>.*?About Us.*?</section>', data, re.DOTALL | re.IGNORECASE)
if m:
    print(m.group(0)[:500])
else:
    print("Not found")
