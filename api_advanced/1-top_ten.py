#!/usr/bin/python3
"""Module to print top 10 hot posts for a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    if not posts:
        print(None)
        return
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
