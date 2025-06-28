#!/usr/bin/python3

# This script returns the number of subscribers
# for a specific subredits

import requests


def number_of_subscribers(subreddit):
    '''
    This function returns the number of subscribers
    for a specific subreddit
    '''
    headers = {
        'User-Agent': 'linux:subcountscript:v1.0 (by /u/bodemurairi)'
    }
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url=api_url, headers=headers, timeout=10)

    if response.status_code != 200:
        print(f"Errors when loading data. Error codes: {response.status_code}")
        return 0

    response_data = response.json()
    return response_data['data']['subscribers']
