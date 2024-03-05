#!/usr/bin/python3
"""
Return the number of subscribers for a given subreddit.
"""
import requests

word_count = {}


def count_words(subreddit, word_list, after=None):
    """
    Return the number of subscribers for a given subreddit.
    """
    if str(word_count) == '{}':
        for word in word_list:
            word_count[word] = 0
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    after = response.json().get('data').get('after')
    if after is None:
        sorted_list = sorted(word_count.items(),
                             key=lambda x: x[1], reverse=True)
        for i in sorted_list:
            print('{}: {}'.format(i[0], i[1]))
        return
    for i in response.json().get('data').get('children'):
        for word in word_list:
            if word in i.get('data').get('title'):
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return count_words(subreddit, word_list, after)
