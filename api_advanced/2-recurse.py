#!/usr/bin/python3
"""2-recurse module

This module defines a recursive function that queries the Reddit API
and returns a list of titles of all hot posts for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursive function to return all hot post titles of a subreddit."""
    if hot_list is None:
        hot_list = []

    headers = {
        'User-Agent': 'linux:recursivescript:v1.0 (by /u/bodemurairi)'
    }
    params = {'limit': 100, 'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])

    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
