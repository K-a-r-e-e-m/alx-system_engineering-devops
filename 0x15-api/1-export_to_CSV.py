#!/usr/bin/python3
"""This module export data to csv file"""


from csv import writer, QUOTE_ALL
from requests import get
from sys import argv


if __name__ == '__main__':
    todoList = get('https://jsonplaceholder.typicode.com/todos')

    userId = int(argv[1])
    user = get(f'https://jsonplaceholder.typicode.com/users/{userId}')

    userName = user.json().get('username')
    title = ''

    for task in todoList.json():
        if task.get('userId') == userId:
            title = task.get('title')
            completed = task.get('completed')
            with open(f'{userId}.csv', 'a') as csvFile:
                myfile = writer(csvFile, delimiter=',', quoting=QUOTE_ALL)
                myfile.writerow([userId, userName, completed, title])
