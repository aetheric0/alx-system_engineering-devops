#!/usr/bin/python3
""" Fetches API from jsonplaceholder
"""

from requests import request
from sys import argv


if __name__ == '__main__':
    titles = []
    not_completed = 0
    completed = 0
    user_response = request('get',
        'https://jsonplaceholder.typicode.com/users?id={}'
        .format(argv[1]))
    todo_response = request(
        'get', 'https://jsonplaceholder.typicode.com/todos')
    employee = user_response.json()
    todo = todo_response.json()
    for item in todo:
        if item['userId'] == int(argv[1]):
            if item['completed'] == False:
                not_completed += 1
            else:
                completed += 1
                titles.append(item['title'])
    total_tasks = completed + not_completed
    print('Employee {} is done with tasks({}/{}):'
          .format(employee[0]['name'], completed, total_tasks))
    for title in titles:
        print('\t{}'.format(title))
