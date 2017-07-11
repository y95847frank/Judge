from celery import Celery
import sys
import filecmp
import os

app = Celery('tasks', backend='redis://localhost:6379', broker='pyamqp://localhost')

@app.task
def add(x, y):
    return x + y

@app.task(time_limit=3)
def eval(x, y):
    x = str(x)
    y = str(y)
    
    comand = 'python a.py < in/'+x+' > '+y
    os.system(comand)
    
    if filecmp.cmp(y, 'out/'+y) == True:
        return 1
    else:
        return 0
