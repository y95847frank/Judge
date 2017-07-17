"""
Celery tasks worker
"""
import filecmp
import subprocess
import resource
import shlex
#import psutil
from subprocess import PIPE
#from subprocess import Popen
#from subprocess import STDOUT
from celery import Celery
from celery.utils.log import get_task_logger

LOGGER = get_task_logger(__name__)

app = Celery('tasks', backend='redis://localhost:6379', broker='pyamqp://localhost')

"""
evaluate program
"""
@app.task(time_limit=1)
def eval(test_in, test_out):
    """
    evaluate program
    """
    fin = 'in/'+str(test_in)
    fout = str(test_out)

    myinput = open(fin)
    myoutput = open('user_out/'+fout, 'w')
    cmd = 'python  a.py'
    sub_process = subprocess.Popen(shlex.split(cmd), stdin=myinput, stdout=myoutput, shell=False, stderr=PIPE)
    #p = subprocess.Popen('python a.py', stdin=myinput, stdout=myoutput, shell=True, stderr= PIPE)
    sub_process.wait()
    myoutput.flush()
    info = resource.getrusage(resource.RUSAGE_CHILDREN)
    time = info.ru_utime+info.ru_stime
    out, err = sub_process.communicate()
    _ = out
    #comand = 'python a.py < in/'+x+' > '+y
    #os.system(comand)
    if err:
        print err
        return (-1, err, time)
    elif filecmp.cmp('user_out/'+fout, 'out/'+fout) == 1:
        return (1, '', time)
    return (0, '', time)
