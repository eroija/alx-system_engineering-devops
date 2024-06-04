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
    try:
        # Make a request to the Reddit API to get the subreddit information
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'User-Agent': 'MyApp/0.0.1'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the subscriber count from the response data
            subscriber_count = response.json()["data"]["subscribers"]
            return subscriber_count
        else:
            # The subreddit is invalid, return 0
            return 0
    except requests.exceptions.RequestException:
        # An error occurred while making the request, return 0
        return 0
