from scraper import scrape_and_screenshot
from agents import spin_chapter, review_chapter
from human_loop import human_edit
from db import save_version

def run_workflow(url):
    print("🔍 Scraping web page...")
    raw = scrape_and_screenshot(url)
    print("✅ Web page scraped. Text saved to chapter1.txt.")

    print("✍️ Spinning with AI...")
    spun = spin_chapter(raw)
    print("✅ Spinning done.")

    print("🔎 Reviewing with AI...")
    reviewed = review_chapter(spun)
    print("✅ Review done.")

    print("👨‍💻 Human editing step...")
    final = human_edit(reviewed)

    print("💾 Saving final version to database...")
    save_version("Chapter1", final)
    print("🎉 Done! Everything completed successfully.")

if __name__ == "__main__":
    run_workflow("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")



