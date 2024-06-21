#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit."""


from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Return list of hot titels"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    myParams = {'limit': 100, 'after': after}
    myHeaders = {'User-Agent': 'script by u/KareeeemHany'}

    res = get(url, params=myParams, headers=myHeaders, allow_redirects=False)

    if res.status_code == 200:

        res = res.json()
        after = res.get('data').get('after')

        for t in res.get('data').get('children'):
            hot_list.append(t.get('data').get('title'))

        if after:
            recurse(subreddit, hot_list, after)

        return hot_list

    else:
        return None
