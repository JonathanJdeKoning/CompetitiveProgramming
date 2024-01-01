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
    n, = intpls()
    ans = {
        1:1,
        2:4,
        3:15,
        4:64,
        5:325,
        6:1956,
        7:13699,
        8:109600,
        9:986409,
        10:9864100,
        11:108505111
    }
    if n in ans:
        print(ans[n])
    else:
        print("JUST RUN!!")


#########################
if __name__ == "__main__":
    solve()

