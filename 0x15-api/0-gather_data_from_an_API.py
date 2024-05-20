#!/usr/bin/python3
"""
This module provides functionality to fetch and display the TODO list
progress for an employee from a REST API using their employee ID.
"""
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]

    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                 employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                 employee_id)

    user_response = requests.get(users_url)
    user_data = user_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    print("Employee {} is done with tasks({}/{}):".format(
          user_data['name'], completed_tasks, total_tasks))

    for task in todos_data:

        if task['completed']:
            print("\t {}".format(task['title']))
