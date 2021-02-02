#!/usr/bin/python3
"""Using this REST API, for a given employee ID,
   returns information about his/her TODO list progress"""


import requests
from sys import argv


def show_user(id):
    """"Return the user"""
    url = 'https://jsonplaceholder.typicode.com/users/'
    user = requests.get(url, params={'id': id}).json()
    return user


def show_todos(id):
    """Return the users todos"""
    url = 'https://jsonplaceholder.typicode.com/todos/'
    todos = requests.get(url, params={'userId': id}).json()
    return todos


def show_todo_list(user, todos):
    """Display on the standard output the employee TODO list progress"""
    employee_name = user[0]['name']
    todo_list = todos
    n_done_tasks = 0
    task_title = ''
    for todos in todo_list:
        if todos['completed'] is True:
            n_done_tasks += 1
            task_title += '\t' + todos['title'] + '\n'
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, n_done_tasks, len(todo_list)))
    print(task_title, end='')


if __name__ == '__main__':
    user = show_user(argv[1])
    todos = show_todos(argv[1])
    show_todo_list(user, todos)
