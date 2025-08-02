#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    url = requests.get(f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10',
                       headers=user,
                       timeout=10).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
