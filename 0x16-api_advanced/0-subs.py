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
    myHeaders = {'User-agent': 'script by u/KareeeemHany'}
    res = get(url + 'r/' + subreddit + '/about.json', headers=myHeaders)
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
