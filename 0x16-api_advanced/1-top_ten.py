#!/usr/bin/python3
"""
Moduke that prints the titles of the first 10 hot posts listed for a given
subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'eric@iija'}

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data[:10]:
            print(post['data']['title'])
    else:
        print(None)
