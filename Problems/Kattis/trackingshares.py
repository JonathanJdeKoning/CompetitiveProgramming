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
    sharedict = {}
    numcomps = intspls()
    days = []
    for i in range(numcomps):
        numshares = intspls()
        sharedict[i] = {}
        for j in range(numshares):
            shares, day = intspls()
            sharedict[i][day] = shares
            if day not in days:
                days.append(day)
    days = sorted(days)
    
    debug(sharedict, "sharedict")
    debug(days, "days")
    totals = []
    for day in days:
        total = 0
        for company, history in sharedict.items():
            try:
                total += history[max([x for x in history.keys() if x <= day])]
            except: pass
        totals.append(total)
    print(" ".join([str(x) for x in totals]))
                
#########################
if __name__ == "__main__":
    solve()

