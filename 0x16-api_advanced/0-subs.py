#!/usr/bin/python3
"""Module for a function that returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """
       Queries the Reddit API and returns the number of subscribers for a
       given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'eric@iija'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        print(response.json()['data']['subscribers'])
    else:
        return 0
