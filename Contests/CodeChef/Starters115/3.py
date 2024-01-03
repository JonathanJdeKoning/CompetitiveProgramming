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
        bad = False
        n = intspls()
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        needed = (sum(a)+sum(b))/n
        debug(needed, "needed")
        if not needed.is_integer():
            print(-1)
            continue
        needed = int(needed)
        new = []
        for i in a:
            if (needed-i) in b:
                new.append(needed-i)
                b.remove(needed-i)
            else:
                bad = True
                break
        if bad:
            print(-1)
            continue

        print(" ".join([str(x) for x in a]))
        print(" ".join([str(x) for x in new]))


#########################
if __name__ == "__main__":
    solve()

