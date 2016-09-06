import requests

token = "ed743104e919fa4a0ba48d0390cc5ee4"
github = 'https://github.com/svcastaneda/code2040-application'

def task_one():
    requests.post('http://challenge.code2040.org/api/register', data = {'token':token, 'github':github})

def task_two():
    return

def task_three():
    return

def task_four():
    return

def task_five():
    return


task_one()
task_two()
task_three()
task_four()
task_five()
