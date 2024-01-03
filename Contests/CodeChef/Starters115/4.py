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
    tc = intspls()
    for _ in range(tc):
        n, x = intspls()
        
        if x == 0:
            print(" ".join([str(x) for x in range(1,n+1)]))

        elif x > n-2:
            print(-1)
            continue

        elif x == n-2:
            print(" ".join([str(n)]+list(map(str, list(range(1,n))))))

        else:
            stop = n-1
            stopidx = ((n-2)-1) - x
            print(" ".join([str(x) for x in range(1, stopidx+1)]+[str(stop)]+[str(x) for x in range(stopidx+1, stop)] + [str(n)]))



#########################
if __name__ == "__main__":
    solve()

