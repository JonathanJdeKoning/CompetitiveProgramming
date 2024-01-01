import math

num, zeros = list(map(int, input().split()))

dby = int("1" + "0"*zeros)

newnum = round(num/dby)*dby
print(newnum)
