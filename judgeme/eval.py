import sys
import subprocess
import os
import filecmp

total = 2
c = 0
for i in range(1,total+1):
	out = str(i)+'.out'
	comand = 'python a.py < in/'+str(i)+'.in > '+out
	os.system(comand)
	if filecmp.cmp(out, 'out/'+out) == True:
		c+=1
print c,'/', total
#subprocess.Popen(["python", "-a", "arg1", "-b", "arg2"])