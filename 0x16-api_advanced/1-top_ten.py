#!/usr/bin/python3
"""
Return the number of subscribers for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print('None')
        return
    for i in range(10):
        print(response.json().get('data').get(
            'children')[i].get('data').get('title'))
