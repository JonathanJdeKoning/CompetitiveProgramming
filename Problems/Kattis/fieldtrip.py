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
    numsections = intspls()
    sections = intspls()

    total = sum(sections)
    
    perbus = total/3
    if not perbus.is_integer():
        print("-1")
        return
    
    perbus = int(perbus)

    tracker = 0
    ans = []
    for i,n in enumerate(sections):
        tracker+= n
        if tracker > perbus:
            print(-1)
            return
        if tracker == perbus:
            ans.append(i+1)
            tracker = 0

    debug(ans, "ans")
    if len(ans)< 3:
        print(-1)
        return
    print(" ".join([str(x) for x in ans[:-1]]))


#########################
if __name__ == "__main__":
    solve()

