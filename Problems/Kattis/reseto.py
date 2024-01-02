import os
########################################################
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt") ##
########################################################

import sys 
from math import ceil, floor
def debug(var, name=""):
    if DEBUG: 
        print(f"{name.upper()}: {var}")

def intpls(): return map(int, sys.stdin.readline().strip().split())
def listpls(): return list(map(int, sys.stdin.readline().strip().split()))
def stringpls(): return sys.stdin.readline().strip()

#####################
def solve():
    n, k = intpls()

    def primesVanilla(n, k):
        if n == 2:
            return 2
        wowee = k
        r = [True] * (n+1)
        r[0] = r[1] = False
        for i in range(2,n+2):
            if r[i]:
                for j in range(i, n+1, i):
                    if r[j]:
                        r[j] = False
                        wowee -=1
                    
        
                    if wowee == 0:
                        return j
    print(primesVanilla(n, k))
#########################
if __name__ == "__main__":
    solve()

