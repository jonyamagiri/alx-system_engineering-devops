#!/usr/bin/python3
"""
Python script that utilizes the REST API at https://jsonplaceholder.typicode.com/todos
 to retrieve information about an employee's progress on their TODO list, given their
  employee ID.
"""
import requests
import sys


def get_user_info(user_id: int) -> dict:
    """Retrieve user information by ID."""
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    return requests.get(url).json()


def get_user_todos(user_id: int) -> list:
    """Retrieve user todos by ID."""
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos/'
    return requests.get(url).json()


def get_completed_tasks(todos: list) -> list:
    """Filter completed todos and return their titles."""
    completed_tasks = []
    for todo in todos:
        if todo.get("completed") is True:
            completed_tasks.append(todo.get("title"))
    return completed_tasks


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user_info = get_user_info(user_id)
    user_todos = get_user_todos(user_id)

    user_name = user_info.get("name")
    completed_tasks = get_completed_tasks(user_todos)
    num_completed = len(completed_tasks)
    num_todos = len(user_todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user_name,
        num_completed,
        num_todos
    ))
    for task in completed_tasks:
        print("\t {}".format(task))
