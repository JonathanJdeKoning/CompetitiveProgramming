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

def intspls(): 
    ints = list(map(int, sys.stdin.readline().strip().split()))
    return ints if len(ints)>1 else ints[0]
def stringpls(): return sys.stdin.readline().strip()

#####################
def solve():
    s = stringpls()
    ree = 0
    total = 0
    for c in s[1:]:
        if c.islower():
            ree += 1
        else:
            debug(ree, "ree")
            while (ree+1)%4 != 0:
                ree += 1
                total += 1
            ree = 0
    print(total)




#########################
if __name__ == "__main__":
    solve()

