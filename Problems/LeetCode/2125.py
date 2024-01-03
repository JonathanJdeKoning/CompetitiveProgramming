import os
###############
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt") ##
###############

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
    class Solution:
        def numberOfBeams(self, bank: List[str]) -> int:
            total = 0
            for i, row in enumerate(bank):
                poss = bank[i+1:]
                for pos in poss:
                    if "1" in pos:
                        total += pos.count("1")* row.count("1")
                        break
            return total

    


#########################
if __name__ == "__main__":
    solve()

