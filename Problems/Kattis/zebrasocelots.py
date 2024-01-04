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
    lenny = intspls()
    n = int("".join([input() for i in range(lenny)]).replace("Z", "1").replace("O", "0"), 2)

    pow = 1
    num = (2**lenny)-1
    print(num-n)

#########################
if __name__ == "__main__":
    solve()

