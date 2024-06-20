#!/usr/bin/python3
"""This module have a function that quaries the Reddit API
and returns number of subscribers for a given subreddit"""


from requests import get


def number_of_subscribers(subreddit):
    """Return number of subscribers including not active users
    or zero at not valid subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/"
    myHeaders = {'User-Agent': 'script by u/KareeeemHany'}
    res = get(url + 'r/' + subreddit + '/about.json', headers=myHeaders)

    try:
        return res.json().get('data').get('subscribers')
    except Exception:
        return 0
