import os
from itertools import combinations, permutations
from collections import deque, Counter, defaultdict
########################################################
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt") ##
########################################################

debugGreen = '\033[92m'
debugCyan = '\033[96m'
debugEnd = '\033[0m'
import sys 
from math import ceil, floor
def debug(var, name=""):
    if DEBUG:
        os.system('color')
        print(f"{debugGreen}{name.upper()}: {var}{debugEnd}")

def out(x):
    if DEBUG:
        sys.stdout.write(f"{debugCyan}{x}{debugEnd}\n")
    else:
        sys.stdout.write(f"{x}\n")
 
if DEBUG: print = out
def intspls(): 
    ints = list(map(int, sys.stdin.readline().strip().split()))
    return ints if len(ints)>1 else ints[0]
def stringpls(): return sys.stdin.readline().strip()

#####################
def solve():
    tc = intspls()
    for _ in range(tc):
        street = stringpls()
        addydata = input().split()
        numaddys = int(addydata[0])
        debug(street, "street")
        need = []
        while numaddys != 0:
            addys = input().split()
            if addys[0] == "+":
                total = list(range(int(addys[1]), int(addys[2])+1, int(addys[3])))
                need += total
                numaddys -= len(total)
            else:
                need.append(int(addys[0]))
                numaddys -= 1
        s = "".join([str(x) for x in need])
        print(street)
        print(" ".join(addydata))
        tt = 0
        for i in range(10):
            tt+= s.count(str(i))
            print(f"Make {s.count(str(i))} digit {i}")
        
        if tt != 1:
            out(f"In total {tt} digits")
        else:
            out(f"In total 1 digit")






#########################
if __name__ == "__main__":
    solve()

