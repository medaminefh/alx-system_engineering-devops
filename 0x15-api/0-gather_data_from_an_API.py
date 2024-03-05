#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    '''Gather data from an API'''

    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    response = requests.get(url)
    user = response.json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    response = requests.get(url)
    todos = response.json()
    completed = [todo for todo in todos if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(todo.get("title"))) for todo in completed]