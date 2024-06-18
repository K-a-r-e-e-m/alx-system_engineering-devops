#!/usr/bin/python3
"""This module export data to csv file"""


from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':

    users = get('https://jsonplaceholder.typicode.com/users/').json()
    for idForUser in users:

        user_id = idForUser.get('id')
        url = 'https://jsonplaceholder.typicode.com/todos'

        todoList = get(f'{url}?userId={user_id}')
        # or get(f'{url}', params={"userId": user_id})

        user = get(f'https://jsonplaceholder.typicode.com/users/{user_id}')

        userName = user.json().get('username')

        # Data of USER_ID that we need to store it in josn file
        data = {
            user_id: [{
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": userName
                    } for task in todoList.json()]
        }
        # loop only in json data without loop in user_id each time

        # Dump data to json file "USER_ID.json"
        with open('todo_all_employees.json', 'a') as file:
            dump(data, file)
