#!/usr/bin/python3
""" Fetches all users in API and exports API data to json file
"""
from requests import request
import json


if __name__ == '__main__':
    json_data = {}
    user_data = request('get', 'https://jsonplaceholder.typicode.com/users')
    todo_data = request('get', 'https://jsonplaceholder.typicode.com/todos')
    users = user_data.json()
    todo = todo_data.json()
    for user in users:
        json_list = []
        for item in todo:
            if user['id'] == item['userId']:
                item['username'] = user['username']
                json_list.append(item)
        json_data['{}'.format(user['id'])] = json_list

    with open('todo_all_employees.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file)
