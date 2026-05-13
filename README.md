# Hacker News Scraper

A simple web scraper that fetches the top stories from Hacker News and exports them to a CSV file.

## Features

- Fetches the top 30 stories from Hacker News
- Displays the top 10 in the terminal
- Saves all stories (title, score, url) to a CSV file

## How to Run

```bash
git clone https://github.com/yourusername/hn-scraper.git
cd hn-scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Tech Used

- **requests** — handles HTTP requests to fetch the page
- **BeautifulSoup4** — parses the raw HTML to extract story data