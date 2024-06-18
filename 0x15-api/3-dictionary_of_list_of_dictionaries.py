#!/usr/bin/python3
"""This module export data to csv file"""


from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':

    # URL of API that have users having tasks in todolist.
    api_url = 'https://jsonplaceholder.typicode.com'

    users = get(f'{api_url}/users/').json()  # GET request from API.

    data = {}  # Dictionary of data to dump in json file.
    for user in users:

        user_id = user.get('id')
        user_name = user.get('username')

        # GET request from API for all tasks to specific user.
        todoList = get(f'{api_url}/todos/?userId={user_id}').json()

        data[user_id] = []  # Another dictionary of all tasks of the user.

        for task in todoList:

            data[user_id].append({
                "username": user_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            })
            # { "1": [
            #           {"username": , "task": , "completed"}, {...}, {...} ...
            #
            #        ], "2": [...
            # }

    with open('todo_all_employees.json', 'w') as file:
        dump(data, file)
