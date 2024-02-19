#!/usr/bin/python3
"""Gather data from an API"""
import csv
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
    with open("{}.csv".format(sys.argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([sys.argv[1], user.get("username"), todo.get(
            "completed"),
                         todo.get("title")]) for todo in todos]
