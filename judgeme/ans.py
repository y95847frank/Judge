import sys
while 1:
    try:
        a = raw_input()
        print a[::-1]
    except:
        sys.exit()
