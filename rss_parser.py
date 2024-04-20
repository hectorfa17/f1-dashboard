import feedparser
import json

# TODO create input for search f1 team or driver
rss_url = "https://news.google.com/rss/search?q=oscar%20piastri"

feed = feedparser.parse(rss_url)  # this returns a dictionary

# Printing the keys to find in this RSS feed:  the most important ones are entry, updated and status
# print(feed.keys())

items = feed.entries

with open("items.json", "w") as file:
    json.dump(
        items, fp=file, indent=4
    )  # fp or file pointer is to instruct that items is going to be saved in a JSON file, indent = 4 means 4 spaces per indentation, making it easier to read.


titles = [x["title"] for x in feed.entries]

with open("titles.json", "w") as file:
    json.dump(titles, fp=file, indent=4)

# print(feed.entries[0]["published"])
