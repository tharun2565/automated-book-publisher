# 📚 Automated Book Publisher using AI & Agents

## 🚀 Overview

This project demonstrates an **AI-powered book publishing pipeline** that:
- Scrapes content from a URL (Wikisource)
- Uses Hugging Face LLMs to rewrite and review text
- Supports human-in-the-loop editing
- Saves final version locally
- Prepares for versioning and search via ChromaDB (future ready)

---

## 🧠 Technologies Used
- Python
- Playwright (web scraping + screenshots)
- Hugging Face Transformers (LLM API for rewriting & editing)
- dotenv (to keep API tokens secure)
- ChromaDB (future integration)
- Reinforcement Learning (planned for search flow)

---

## 🔧 How It Works

1. **Web Scraping**: Scrapes chapter from Wikisource.
2. **AI Writing**: Rewrites using Hugging Face LLM (Zephyr).
3. **AI Review**: Polishes content further.
4. **Human-in-the-loop**: Final edits or approval.
5. **Version Saved**: Saves final output as `final_chapter.txt`.

---

## 📂 File Structure


