#!/usr/bin/python3
"""
queries  Reddit API and returns the number of total subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of total subscribers
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    subscriber_count = response.json().get('data').get('subscribers')
    return subscriber_count
