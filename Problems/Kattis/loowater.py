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
    while True:
        numheads, numknights = intspls()
        if numheads == 0 and numknights == 0: break
        heads = []
        knights = []
        for _ in range(numheads):
            heads.append(intspls())
        for _ in range(numknights):
            knights.append(intspls())

        knights = sorted(knights)
        heads = sorted(heads)
        total = 0
    
        for head in heads:
            bad = True
            for knight in knights:
                if knight >= head:
                    total += knight
                    bad = False
                    knights.remove(knight)
                    break
            if bad:
                print("Loowater is doomed!")
                break
        if not bad:
            print(total)

#########################
if __name__ == "__main__":
    solve()

