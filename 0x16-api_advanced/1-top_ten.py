#!/usr/bin/python3
"""
Task 1
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for
    a given subreddit
    """
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    else:
        print(None)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

