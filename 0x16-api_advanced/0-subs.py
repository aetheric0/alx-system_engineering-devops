#!/usr/bin/python3
""" Gets the number of subscribers from a subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """ Retrieves number of subscribers from a subreddit, returns 0
    if subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (compatible; MyRedditApp/1.0; +http://example.com)'
    }
    try:
        response = get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return int(data['data']['subscribers'])
        else:
            return 0
    except Exception as e:
        return e
