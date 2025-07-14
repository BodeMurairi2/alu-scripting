#!/usr/bin/python3

"""Module that returns number of subscribers 
from a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers for a subreddit"""
    headers = {
        'User-Agent': 'linux:subcountscript:v1.0 (by /u/bodemurairi'
    }
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url=api_url, headers=headers, timeout=10, allow_redirects=False)

    response.raise_for_status()

    response_data = response.json()
    return response_data['data']['subscribers']
