#!/usr/bin/python3
"""
This module extends the functionality of the previous script to export the
TODO list progress of an employee to a CSV file.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    user_id = sys.argv[1]
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                 user_id)

    user_response = requests.get(users_url)
    user_data = user_response.json()

    username = user_data.get('username')

    params = {'userId': user_id}

    todos_response = requests.get('{}/todos'.format(base_url), params=params)
    todos = todos_response.json()

    with open("{}.csv".format(user_id), mode='w', newline='') as csvfile:
        for todo in todos:
            completed = todo.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
