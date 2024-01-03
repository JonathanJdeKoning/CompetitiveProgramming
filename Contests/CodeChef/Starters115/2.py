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
        leaves, large, small = intspls()
        
        pos = 0
        small = int(floor(small/3))
        small = min(small, large)
        pos += small

        large -= small
        pos += int(floor(large/2))

        if pos >= leaves:
            print("YES")
        else:
            print("NO")
            


#########################
if __name__ == "__main__":
    solve()

