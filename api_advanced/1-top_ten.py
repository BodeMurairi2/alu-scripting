#!/usr/bin/python3
"""1-top_ten module

This script defines a function that queries the Reddit API and prints the
titles of the top 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:topten:v1.0 (by /u/bodemurairi)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])

        for post in posts:
            print(post["data"]["title"])
    except Exception:
        print(None)
