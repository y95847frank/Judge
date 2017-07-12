from celery import Celery
import sys
import filecmp
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
import resource
#import psutil

app = Celery('tasks', backend='redis://localhost:6379', broker='pyamqp://localhost')

@app.task
def add(x, y):
    return x + y

@app.task(time_limit=0.5)
def eval(x, y):
    x = 'in/'+str(x)
    y = str(y)

    myinput = open(x)
    myoutput = open(y, 'w')
    
    p = subprocess.Popen('python a.py', stdin=myinput, stdout=myoutput, shell=True, stderr= PIPE)
    info = resource.getrusage(resource.RUSAGE_CHILDREN)
    myoutput.flush()
    p.wait()
    
    print  info
    out, err = p.communicate()
    
    #comand = 'python a.py < in/'+x+' > '+y
    #os.system(comand)
    
    if err:
        print err
        return (-1, err)

    if filecmp.cmp(y, 'out/'+y) == True:
        return (1, '')
    else:
        return (0, '')
