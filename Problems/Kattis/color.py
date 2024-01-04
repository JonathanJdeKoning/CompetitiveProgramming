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
    numsocks, capacity, diff = intspls()
    socks = sorted(list(map(int, input().split())))
    total = 1

    prev = socks[0]
    wash = capacity-1
    for sock in socks[1:]:
        if (sock-prev) <= diff and wash > 0: 
            wash -= 1
            if wash == 0:
                wash = capacity
                total += 1
        else:
            wash = capacity
            total += 1
        prev = sock
    print(total)

#########################
if __name__ == "__main__":
    solve()

