#!/usr/bin/python3
"""Module to recursively get all hot articles for a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "MyBot/0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    if after is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, after)
