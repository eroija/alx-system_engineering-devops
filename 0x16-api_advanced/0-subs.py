#!/usr/bin/python3
"""
Module for a function that returns the number of subscribers in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve the
        subscriber count for.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the
        subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyApp/0.0.1'}

    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        return 0
