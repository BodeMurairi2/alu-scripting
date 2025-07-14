#!/usr/bin/python3
"""
 A function that queries the Reddit API and prints the titles.
"""

import requests


def top_ten(subreddit):
    """Prints the top ten hot posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:subcountscript:v1.0 (by /u/bodemurairi)'
    }
    response = requests.get(url=url,
                            headers=headers,
                            timeout=10,
                            allow_redirects=False
                            )

    response.raise_for_status()

    data = response.json()
    title_post = data['data']['children']

    if not title_post:
        print(f'No post found for {subreddit}')
        return

    if len(title_post) < 10:
        raise KeyError(f'Not many posts for {subreddit}\n'
                       f'Number of posts: {len(title_post)}')

    for post in range(10):
        print(title_post[post]['data']['title'])
