#!/usr/bin/python3
"""Python script to export all data in the JSON format."""

import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url, verify=False).json()
    usernamedict = {}
    userdict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [userdict.get(t.get("userId")).append({"task": t.get("title"),
                                           "completed": t.get("completed"),
                                           "username": usernamedict.get(
        t.get("userId"))})
     for t in todo]
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)
