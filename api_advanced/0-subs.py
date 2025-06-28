#!/usr/bin/python3
"""
Reddit Subscriber Counter Module

This module defines a function that returns the number of subscribers
for a given subreddit using Reddit's public API.

Usage:
    Call the `number_of_subscribers(subreddit)` function with a valid subreddit name.

Example:
    count = number_of_subscribers("python")
    print(count)
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Parameters:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers if successful, 0 otherwise.
    """
    headers = {
        'User-Agent': 'linux:subcountscript:v1.0 (by /u/bodemurairi)'
    }
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url=api_url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Error loading data. Status code: {response.status_code}")
            return 0

        response_data = response.json()
        return response_data['data']['subscribers']

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return 0
    except (KeyError, ValueError):
        print("Error parsing response data.")
        return 0
