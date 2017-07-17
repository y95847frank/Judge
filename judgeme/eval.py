"""
evaluate the program
"""

import sys
import json
from collections import defaultdict
from tasks import eval

FILE_NUM = sys.argv[1]


FILE_IN_LIST = []
FILE_OUT_LIST = []
for i in range(1, int(FILE_NUM)+1):
    FILE_IN_LIST.append(str(i)+'.in')
    FILE_OUT_LIST.append(str(i)+'.out')

RESULTS = [eval.delay(i, o) for i, o in zip(FILE_IN_LIST, FILE_OUT_LIST)]

GRADE = defaultdict()
TLE = 0
WA = 0
AC = 0
RE = 0

for result in RESULTS:
    try:
        (stdout, err_msg, time) = result.get()
    except BaseException as err_msg:
        TLE += 1
        continue
    if int(stdout) == 1:
        AC += 1
    elif int(stdout) == -1:
        RE += 1
        dot = err_msg.find(',')
        err_msg = err_msg[dot+1:]
        break
    else:
        WA += 1

GRADE['tl'] = str(TLE)
GRADE['wa'] = str(WA)
GRADE['ac'] = str(AC)

if RE == 0:
    GRADE['re'] = str(RE)
else:
    GRADE['re'] = err_msg

RESULT = json.dumps(GRADE)
print RESULT
