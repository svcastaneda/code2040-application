import requests
import json

token = "ed743104e919fa4a0ba48d0390cc5ee4"
github = 'https://github.com/svcastaneda/code2040-application'

def task_one():
    requests.post('http://challenge.code2040.org/api/register', data = {'token':token, 'github':github})

def task_two():
    s = requests.post('http://challenge.code2040.org/api/reverse', data = {'token': token}).text
    string = s[::-1]
    requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token': token, 'string':string})

def task_three():
    d = requests.post('http://challenge.code2040.org/api/haystack', data = {'token':token}).text
    d = json.loads(d)
    haystack = d["haystack"]
    needle = d["needle"]
    index = haystack.index(needle)

    requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token':token, 'needle':index})

def task_four():
    return

def task_five():
    return


task_one()
task_two()
task_three()
task_four()
task_five()
