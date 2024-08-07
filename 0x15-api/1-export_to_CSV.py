#!/usr/bin/python3
""" Fetches API data and exports to CSV file
"""

from requests import request
from sys import argv


if __name__ == '__main__':
    csv_data = []
    user_data = request('get',
                        'https://jsonplaceholder.typicode.com/users?id={}'
                        .format(argv[1]))
    todo_list = request('get', 'https://jsonplaceholder.typicode.com/todos')
    user = user_data.json()
    todo = todo_list.json()
    for item in todo:
        if item['userId'] == int(argv[1]):
            csv_data.append('\"{}\",\"{}\",\"{}\",\"{}\"\n'.format(
                user[0]['id'],
                user[0]['username'],
                item['completed'],
                item['title']))
    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        for data_item in csv_data:
            csvfile.write(data_item)
