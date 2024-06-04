#!/usr/bin/python3
"""Sub module."""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers of a subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        print(response.json()['data']['subscribers'])
    else:
        return 0
