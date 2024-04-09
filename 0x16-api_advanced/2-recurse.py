#!/usr/bin/python3
'''
queries the Reddit API and returns a list containing the titles 
of all hot articles for a given subreddit
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''gets list of all hot posts titles of a subreddit'''
    user_agent = {'User-Agent': 'test45'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = requests.get(url, headers=user_agent)
    if response.status_code == 200:
        data = response.json()['data']
        aft = data['after']
        posts = data['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if aft is not None:
            recurse(subreddit, hot_list, aft)
        return hot_list
    else:
        return None
