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
    cases = intspls()
    prevh = 0
    prevm = 0
    top = 0
    for _ in range(cases):
        hours, miles = intspls()
        hours -= prevh
        miles -= prevm

        prevh += hours
        prevm += miles
        if miles == 0:
            continue
        if int(floor(miles/hours)) > top:
            top = int(floor(miles/hours))
    print(top)




#########################
if __name__ == "__main__":
    solve()

