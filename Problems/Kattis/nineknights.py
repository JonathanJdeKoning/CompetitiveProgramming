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
    mat = []
    for _ in range(5):
        mat.append(list(stringpls()))
    eek = False 
    if sum(x.count("k") for x in mat) != 9:
        eek = True


    knights = []
    for i,row in enumerate(mat):
        for j,pos in enumerate(row):
            if pos == "k":
                knights.append((i,j))
    debug(knights, "knights")

    bad = []
    for knight in knights:
        y = knight[0]
        x = knight[1]


        bad.append((y+2,x+1))
        bad.append((y+2,x-1))
        bad.append((y-2,x+1))
        bad.append((y-2,x-1))
        bad.append((y+1,x+2))
        bad.append((y+1,x-2))
        bad.append((y-1,x+2))
        bad.append((y-1,x-2))
    for baddy in bad[:]:
        if baddy[0] < 0 or baddy[0]>4 or baddy[1] <0 or baddy[1] > 4:
            bad.remove(baddy)
    bad = sorted(list(set(bad)))
    debug(bad,"BAD")
    for knight in knights:
        if knight in bad:
            eek = True

    if eek:
        print("invalid")
    else:
        print("valid")

#########################
if __name__ == "__main__":
    solve()

