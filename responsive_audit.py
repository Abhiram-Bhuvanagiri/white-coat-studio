import os
import asyncio
from playwright.async_api import async_playwright

# All requested breakpoints
breakpoints = [
    320, 360, 375, 390, 414, 430, 480, 540, 600, 640, 
    768, 820, 853, 912, 1024, 1280, 1366, 1440, 1536, 
    1728, 1920, 2048, 2560
]

# Pages to test
# We use absolute file URIs since this is a static site
current_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
pages = [
    f"file:///{current_dir}/index.html",
    f"file:///{current_dir}/about.html",
    f"file:///{current_dir}/service-details.html",
    f"file:///{current_dir}/contact.html",
]

async def check_overflow(page, width):
    await page.set_viewport_size({"width": width, "height": 1080})
    # Wait for any animations or layout shifts to settle
    await page.wait_for_timeout(500)
    
    # Check if document has horizontal overflow
    has_overflow = await page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth")
    
    if has_overflow:
        # Find which specific elements are causing the overflow
        overflowing_elements = await page.evaluate("""() => {
            const result = [];
            const elements = document.querySelectorAll('*');
            for (let el of elements) {
                const rect = el.getBoundingClientRect();
                // If element is pushing past the viewport width
                if (rect.right > window.innerWidth && rect.width > window.innerWidth) {
                    let selector = el.tagName.toLowerCase();
                    if (el.className && typeof el.className === 'string') {
                        selector += '.' + el.className.split(' ').join('.');
                    }
                    result.push({
                        selector: selector,
                        width: rect.width,
                        right: rect.right
                    });
                }
            }
            return result;
        }""")
        return overflowing_elements
    return []

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        for page_url in pages:
            print(f"\n==============================================")
            print(f"Auditing: {os.path.basename(page_url)}")
            print(f"==============================================")
            
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto(page_url)
            
            for width in breakpoints:
                overflows = await check_overflow(page, width)
                if overflows:
                    print(f"[FAIL] {width}px - Overflow Detected!")
                    for item in overflows:
                        print(f"       -> Element: {item['selector']} (Width: {item['width']}px)")
                else:
                    pass # print(f"[PASS] {width}px - Layout OK")
                    
            await context.close()
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
