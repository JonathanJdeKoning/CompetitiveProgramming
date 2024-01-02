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
    rounds = intspls()
    sven = stringpls()
    friends = intspls()
    friendlist = [stringpls() for _ in range(friends)]

    debug(rounds, "rounds")
    debug(sven, "sven")
    debug(friends, "friends")
    debug(friendlist, "friend list")

    realtotal = 0
    maxpoints = 0
    for i in range(rounds):
        spick = sven[i]
        fpicks = [x[i] for x in friendlist]

        rs = fpicks.count("R")
        ss = fpicks.count("S")
        ps = fpicks.count("P")

        rpoints = rs+ss*2
        spoints = ss+ps*2
        ppoints = ps+rs*2
        
        maxpoints += max([rpoints, spoints, ppoints])
        if spick == "S":
            realtotal+= ss
            realtotal += ps*2
        elif spick == "P":
            realtotal += ps
            realtotal += rs*2
        elif spick == "R":
            realtotal += rs
            realtotal += ss*2
    debug(realtotal, "realtotal")
    debug(maxpoints, "maxpoints")
    print("\n".join([str(x) for x in [realtotal, maxpoints]]))


#########################
if __name__ == "__main__":
    solve()

