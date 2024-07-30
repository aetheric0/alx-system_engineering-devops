#!/usr/bin/python3
""" Fetch API and export to JSON
"""

from requests import request
from sys import argv
import json


if __name__ == '__main__':
    json_data = {}
    list_data = []
    uid = int(argv[1])
    user_data = request('get',
                        'https://jsonplaceholder.typicode.com/users?id={}'
                        .format(uid))
    todo_data = request('get', 'https://jsonplaceholder.typicode.com/todos')
    user = user_data.json()
    todo = todo_data.json()
    for item in todo:
        if item['userId'] == uid:
            item['username'] = user[0]['username']
            list_data.append(item)
    json_data['{}'.format(uid)] = list_data
    with open('{}.json'.format(uid), 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file)
