#!/usr/bin/python3
"""
 Queries the Reddit API and prints the titles of the first
10 hot posts listed
"""

import requests


def top_ten(subreddit):
    """queries 10 hottest posts of a subreddit"""
    headers = {'User-Agent': 'test23'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
