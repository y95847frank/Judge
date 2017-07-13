from celery import Celery
import sys
import filecmp
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
import resource
import shlex
import psutil

app = Celery('tasks', backend='redis://localhost:6379', broker='pyamqp://localhost')

@app.task
def add(x, y):
    return x + y

@app.task(time_limit=1)
def eval(x, y):
    x = 'in/'+str(x)
    y = str(y)

    myinput = open(x)
    myoutput = open('user_out/'+y, 'w')
   
    cmd = 'python  a.py'
    p = subprocess.Popen(shlex.split(cmd), stdin=myinput, stdout=myoutput, shell=False, stderr= PIPE)
    #p = subprocess.Popen('python a.py', stdin=myinput, stdout=myoutput, shell=True, stderr= PIPE)
    p.wait()
    myoutput.flush()
    info = resource.getrusage(resource.RUSAGE_CHILDREN)
    
    time = info.ru_utime+info.ru_stime, 
    out, err = p.communicate()
    
    #comand = 'python a.py < in/'+x+' > '+y
    #os.system(comand)
    
    if err:
        print err
        return (-1, err, time)

    if filecmp.cmp('user_out/'+y, 'out/'+y) == True:
        return (1, '', time)
    else:
        return (0, '', time)
