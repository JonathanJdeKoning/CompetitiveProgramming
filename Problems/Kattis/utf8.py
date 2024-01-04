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
    numbytes = intspls()
    bytes = []
    type1 = 0
    type2 = 0
    type3 = 0
    type4 = 0
    needed = 0
    bad = False
    for _ in range(numbytes):
        bytes.append(stringpls())
    through = False
    for byte in bytes:
        if byte.startswith("10"):
            needed -= 1
            if needed < 0:
                bad = True
                break
        if byte.startswith("0"):
            if needed != 0: bad = True;break
            type1+=1
            needed = 0
        if byte.startswith("110"):
            if needed != 0: bad = True;break
            type2+=1
            needed = 1
        if byte.startswith("1110"):
            if needed != 0: bad = True;break
            type3+=1
            needed = 2
        if byte.startswith("11110"):
            if needed != 0: bad = True;break
            type4+= 1
            needed = 3
    if needed != 0:
        bad = True
    if not bad:
        print("\n".join([str(x) for x in [type1, type2, type3, type4]]))
    else:
        print("invalid")



#########################
if __name__ == "__main__":
    solve()

