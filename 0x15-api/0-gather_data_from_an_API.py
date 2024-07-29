#!/usr/bin/python3
"""This module gather data from an API"""


from requests import get
from sys import argv


if __name__ == '__main__':
    todoList = get('https://jsonplaceholder.typicode.com/todos/')

    employee = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    name = employee.json().get('name')

    totalTasks = 0
    doneTasks = 0
    taskTitle = []

    for task in todoList.json():
        if task.get('userId') == int(argv[1]):
            totalTasks += 1
            if task.get('completed'):
                doneTasks += 1
                taskTitle.append('\t ' + task.get('title'))

    print(f'Employee {name} is done with tasks({doneTasks}/{totalTasks}):')
    [print(line) for line in taskTitle]
