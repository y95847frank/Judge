import sys
nums = raw_input()
nums = [int(s) for s in nums.split(',')]
num_sum = 0
flag = False
for n in nums:
    if flag == False:
        if n == 6:
            flag = True
        else:
            num_sum += n
    elif flag == True:
        if n == 7:
            flag = False
print num_sum
  