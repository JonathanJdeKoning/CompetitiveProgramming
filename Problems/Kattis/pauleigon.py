import os
###############
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt") ##
###############

import sys 
from math import ceil, floor
def debug(var, name=""):
    if DEBUG: 
        print(f"{name.upper()}: {var}")

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

#####################
def solve():
    n, p, q = get_ints()
    rounds = p+q
    rots = int(floor(rounds/n))
    extra = rounds%n
    debug(rounds, "rounds")
    debug(rots, "Rotations")
    debug(extra, "extra")

    if rots%2 == 0:
        print("paul")
    else:
        print("opponent")



#########################
if __name__ == "__main__":
    solve()

