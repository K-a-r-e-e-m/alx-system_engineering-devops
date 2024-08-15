#!/usr/bin/python3
"""This module have a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit.
"""


from requests import get


def top_ten(subreddit):
    """Return first 10 hot post or zero at not valid subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    myHeaders = {'User-Agent': 'script by u/KareeeemHany'}
    res = get(url, headers=myHeaders)

    if res.status_code == 200:
        res = res.json()
        for title in res['data']['children']:
            print(title['data']['title'])
    else:
        print("None")
