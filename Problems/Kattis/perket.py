import os
from itertools import permutations, combinations
###############
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt") ##
###############

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
    numings = intspls()
    ings = []
    for _ in range(numings):
        ings.append(intspls())

    poss = []
    for i in range(1, numings+1):
        poss += list(combinations(ings, i))

    vals = []
    for val in poss:
        sour = 1
        bitt = 0
        for ing in val:
            sour*= ing[0]
            bitt+=ing[1]
        vals.append(abs(sour-bitt))

    debug(ings, "INGREDIENTS")
    debug(poss, "possible")
    debug(vals, "vals")
    print(min(vals))



#########################
if __name__ == "__main__":
    solve()

