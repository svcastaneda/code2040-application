import requests
import json

token = "ed743104e919fa4a0ba48d0390cc5ee4"
github = 'https://github.com/svcastaneda/code2040-application'

def task_one():
    requests.post('http://challenge.code2040.org/api/register', data = {'token':token, 'github':github})

def task_two():
    d = post_token('http://challenge.code2040.org/api/reverse').text
    string = d[::-1]
    requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token': token, 'string':string})

def task_three():
    d = post_token('http://challenge.code2040.org/api/haystack').json()
    haystack = d["haystack"]
    needle = d["needle"]
    index = haystack.index(needle)

    requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token':token, 'needle':index})

def task_four():
    d = post_token('http://challenge.code2040.org/api/prefix').json()

    prefix = d["prefix"].lower()
    given_array = d["array"]

    array = []

    for item in given_array:
        if not item.lower().startswith(prefix):
            array.append(item)

    data = {'token':token, 'array':array}

    requests.post('http://challenge.code2040.org/api/prefix/validate', data = json.dumps(data))

from datetime import datetime, timedelta
def task_five():
    d = post_token('http://challenge.code2040.org/api/dating').json()
    datestamp = d["datestamp"]
    interval = d["interval"]

    parsed_time = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')
    new_time = parsed_time + timedelta(seconds=interval)
    new_formatted_time = new_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    requests.post('http://challenge.code2040.org/api/dating/validate', data = {'token':token, 'datestamp':new_formatted_time})

def post_token(url):
    return requests.post(url, data = {'token':token})

task_one()
task_two()
task_three()
task_four()
task_five()
