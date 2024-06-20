#!/usr/bin/python3
"""This module have a function that quaries the Reddit API
and returns number of subscribers for a given subreddit"""


from requests import get


def number_of_subscribers(subreddit):
    """Return number of subscribers including not active users
    or zero at not valid subreddit"""

    url = "https://www.reddit.com/"
    myHeaders = {'User-Agent': 'Mozilla/5.0'}
    res = get(url + 'r/' + subreddit + '/about.json', headers=myHeaders)

    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
