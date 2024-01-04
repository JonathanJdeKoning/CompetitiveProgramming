import os
from itertools import combinations, permutations
from collections import deque, Counter, defaultdict
########################################################
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt") ##
########################################################

import sys 
from math import ceil, floor, pi
def debug(var, name=""):
    if DEBUG: 
        print(f"{name.upper()}: {var}")

def intspls(): 
    ints = list(map(int, sys.stdin.readline().strip().split()))
    return ints if len(ints)>1 else ints[0]
def stringpls(): return sys.stdin.readline().strip()

#####################
def solve():
    def area(r, h):
        return 2*pi*r*h+2*pi*r*r

    while True:
        d, v = intspls()
        if d == v== 0: break
        
        trunk = area(d,d)
        debug(trunk, "trunk")
        print(trunk - v)
        


#########################
if __name__ == "__main__":
    solve()

