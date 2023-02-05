#!/usr/bin/python3
"""
Python script that, uses REST API (https://jsonplaceholder.typicode.com/todos)
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":

    number_completed_todos = 0
    number_of_todos = 0
    completed_tasks = []
    users_url = 'https://jsonplaceholder.typicode.com/users/'
    user_url = users_url + sys.argv[1]
    user_infos = requests.get(user_url).json()

    user_name = user_infos.get("name")

    user_todos_url = users_url + sys.argv[1] + '/todos/'
    user_todos = requests.get(user_todos_url).json()

    for user_todo in user_todos:
        number_of_todos += 1
        if (user_todo.get("completed") is True):
            number_completed_todos += 1
            completed_tasks.append(user_todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        user_name,
        number_completed_todos,
        number_of_todos
    ))
    for task in completed_tasks:
        print("\t {}".format(task))
