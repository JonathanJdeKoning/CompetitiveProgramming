import os
from itertools import combinations, permutations
from collections import deque, Counter, defaultdict
########################################################
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt") ##
########################################################

import sys 
from math import ceil, floor
def debug(var, name=""):
    if DEBUG: 
        print(f"{name.upper()}: {var}")

def intpls(): return map(int, sys.stdin.readline().strip().split())
def listpls(): return list(map(int, sys.stdin.readline().strip().split()))
def stringpls(): return sys.stdin.readline().strip()

#####################
def solve():
    s = stringpls()
    up = 0
    down = 0
    found = 0

    isup = s[0]=="U"
    for c in s[1:]:
        if c == "U":
            if not isup:
                up+= 1
        if c == "D":
            if isup:
                up+=2
            else:
                up+=1
        isup = True

    isup = s[0]=="U"
    for c in s[1:]:
        if c == "U":
            if isup:
                down += 1
            else:
                down += 2
        if c == "D":
            if isup:
                down += 1
        isup = False
    
    isup = s[0]=="U"
    for c in s[1:]:
        if c == "U":
            if isup:
                continue
            else:
                isup = True
                found += 1
        if c == "D":
            if isup:
                isup = False
                found += 1
            else:
                continue

    debug(up, "uppers")
    debug(down, "downers")
    debug(found, "founders")
    print("\n".join([str(up),str(down),str(found)]))


#########################
if __name__ == "__main__":
    solve()

