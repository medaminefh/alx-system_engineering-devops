#!/usr/bin/python3
"""fetch all data from an API and export to JSON"""
import json
import requests


if __name__ == "__main__":
    '''fetch all data from an API and export to JSON'''
    # fetch all users
    url = "https://jsonplaceholder.typicode.com/users"
    users_data = requests.get(url)
    # loop through all users and fetch their todos
    users = users_data.json()
    data = {}
    for user in users:
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user.get("id"))
        todos_data = requests.get(url)
        todos = todos_data.json()
        data[user.get("id")] = [{"task": todo.get("title"),
                                 "completed": todo.get("completed"),
                                 "username": user.get("username")}
                                for todo in todos]
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
