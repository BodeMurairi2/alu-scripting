#!/usr/bin/python3
"""
A  function that queries the Reddit API and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}
    response = requests.get(url,
                            headers=headers,
                            timeout=10,
                            allow_redirects=False
                            )
    if response.status_code != 200:
        return 0
    data = response.json().get('data')
    return data.get('subscribers')
