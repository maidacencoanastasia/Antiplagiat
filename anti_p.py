import os

from antiplagiat import Antiplagiat

import time

TOKEN = '2a897d2c-aa87-4c8d-8f0a-a6f94b9e57f4'

api = Antiplagiat(TOKEN)

with open('example.txt', 'r') as fp:
    text = fp.read()


result = api.unique_text_add(text)
key = result['key']

while True:
    # дадим некоторое время на проверку
    time.sleep(200)
    result = api.unique_check(key)
    if result['status'] == 'done':
        print('Done!')
        # сделать чтото с отчетом
        #return
    elif result['status'] == 'error':
        print(f'Error: {result}')
        #return
    elif result['status'] == 'not found':
        print('Not found!')
        #return
    else:
        print('In progress...')