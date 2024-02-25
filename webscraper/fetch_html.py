import sys
from playwright.sync_api import sync_playwright

def fetch_html_content(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        html_content = page.content()
        browser.close()
        return html_content

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        content = fetch_html_content(url)
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print("Please provide a URL as an argument.")
