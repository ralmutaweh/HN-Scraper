import requests
from bs4 import BeautifulSoup
import csv


def fetch_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text
    

def parse_stories(html):
    soup = BeautifulSoup(html, "html.parser")

    stories_list = []
    rows = soup.select("tr.athing")
    for row in rows:
        title = row.select_one("span.titleline > a").text
        score = row.find_next_sibling("tr").select_one("span.score")
        if score is not None:
            score = score.text
        else:
            score = "0 points"

        url = row.select_one("span.titleline > a").get("href")

        stories_list.append({"title": title, "score": score, "url": url})

    return stories_list


def display_stories(stories):
    for i, story in enumerate(stories[:10]):
        print(f"{i + 1}. {story['title']} [{story['score']}]")


def save_to_csv(stories, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'score', 'url'])
        writer.writeheader()
        writer.writerows(stories)
       


if __name__ == "__main__":
    html = fetch_page("https://news.ycombinator.com/")
    stories = parse_stories(html)
    print("Top 10 Stories:")
    display_stories(stories)
    save_to_csv(stories, "Stories.csv")

