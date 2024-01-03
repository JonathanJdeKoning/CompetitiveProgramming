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
    numapples = intspls()
    apples = sorted(intspls(), reverse=True)

    mid = len(apples)//2
    perms = list(permutations(apples))
    print(min([abs(sum(x[:mid])- sum(x[mid:])) for x in perms]))
    





#########################
if __name__ == "__main__":
    solve()

