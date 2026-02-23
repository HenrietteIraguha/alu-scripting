#!/usr/bin/python3
"""Module to count keywords in hot articles of a subreddit"""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Recursively counts keywords in titles of hot articles"""
    if counts is None:
        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0)

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "MyBot/0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1

    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, counts, after)
