from playwright.sync_api import sync_playwright

def scrape_and_screenshot(url, screenshot_path="chapter1.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=screenshot_path, full_page=True)
        text = page.inner_text('body')
        browser.close()
        return text

if __name__ == "__main__":
    text = scrape_and_screenshot("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")
    with open("chapter1.txt", "w", encoding="utf-8") as f:
        f.write(text)


