import sys
from tasks import eval
from collections import defaultdict
import json

total = sys.argv[1]


fin = []
fout = []
for i in range(1, int(total)+1):
    fin.append(str(i)+'.in')
    fout.append(str(i)+'.out')

results = [eval.delay(i, o) for i, o in zip(fin, fout)]

grade = defaultdict()
tl = 0
wa = 0
ac = 0
re = 0

t_time = 0.0

for r in results:
    try:
        (k, des, time) = r.get()
    except:
        tl += 1
        continue
    if int(k) == 1:
        ac += 1
    elif int(k) == -1:
        re += 1
        d = des.find(',')
        des = des[d+1:]
        break
    else:
        wa += 1

grade['tl'] = str(tl)
grade['wa'] = str(wa)
grade['ac'] = str(ac)

if re == 0:
    grade['re'] = str(re)
else:
    grade['re'] = des

r = json.dumps(grade)
print r
