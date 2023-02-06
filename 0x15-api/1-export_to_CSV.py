#!/usr/bin/python3
""" Python script to export data in the CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    users_url = 'https://jsonplaceholder.typicode.com/users/'
    USER_ID = sys.argv[1]

    USERNAME = requests.get(users_url + USER_ID).json().get("username")

    user_todos_url = users_url + USER_ID + '/todos/'
    user_todos = requests.get(user_todos_url).json()

    file_name = "{}.csv".format(USER_ID)
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for user_todo in user_todos:
            writer.writerow([USER_ID, USERNAME,
                             str(user_todo.get("completed")),
                             user_todo.get("title")])
