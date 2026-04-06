import requests
import json
import os
from datetime import datetime

# API URLs
TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Headers
headers = {"User-Agent": "TrendPulse/1.0"}

# Categories
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"],
    "others": []
}

# Find category
def find_category(title):
    title = title.lower()
    for cat, words in categories.items():
        for word in words:
            if word in title:
                return cat
    return None

# Fetch top IDs
def get_top_ids():
    try:
        response = requests.get(TOP_URL, headers=headers)
        if response.status_code != 200:
            print("Failed to fetch top stories")
            return []
        return response.json()[:500]
    except Exception as e:
        print("Error:", e)
        return []

# Fetch story
def get_story(story_id):
    try:
        url = ITEM_URL.format(story_id)
        response = requests.get(url, headers=headers)
        return response.json()
    except:
        return None

# Main logic
def main():
    ids = get_top_ids()

    collected = []
    count = {cat: 0 for cat in categories}

    for story_id in ids:
        # Stop early if done
        if len(collected) >= 125:
            break

        story = get_story(story_id)

        if not story or "title" not in story:
            continue

        cat = find_category(story["title"])

        if not cat:
            cat = "others"

        # limit 25 per category
        if count[cat] >= 25:
            continue

        data = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": cat,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": datetime.now().isoformat()
        }

        collected.append(data)
        count[cat] += 1

    # Save file
    os.makedirs("data", exist_ok=True)
    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w") as f:
        json.dump(collected, f, indent=4)

    print("Collected", len(collected), "stories. Saved to", filename)


if __name__ == "__main__":
    main()