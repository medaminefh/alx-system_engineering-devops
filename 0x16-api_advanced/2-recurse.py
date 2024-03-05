#!/usr/bin/python3
"""
Return the number of subscribers for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Return the number of subscribers for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    if response.json().get('data').get('after') is None:
        return hot_list
    after = response.json().get('data').get('after')
    for i in response.json().get('data').get('children'):
        hot_list.append(i.get('data').get('title'))
    return recurse(subreddit, hot_list, after)
