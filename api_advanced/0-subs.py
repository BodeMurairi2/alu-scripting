#!/usr/bin/python3
"""Module that returns number of subscribers 
from a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers for a subreddit"""
    headers = {
        'User-Agent': 'linux:subcountscript:v1.0 (by /u/bodemurairi)'
    }
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url=api_url, headers=headers, timeout=10)

        if response.status_code != 200:
            return 0

        response_data = response.json()
        return response_data['data']['subscribers']

    except requests.exceptions.RequestException:
        return 0
    except (KeyError, ValueError):
        return 0
