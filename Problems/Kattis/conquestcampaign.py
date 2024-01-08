import os
import sys 
from math import ceil, floor, pi
from itertools import combinations, permutations
from collections import deque, Counter, defaultdict

##################################################################
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt")            #
debugGreen,debugCyan,debugEnd = '\033[92m','\033[96m','\033[0m'  #
if DEBUG: os.system('color')                                     #
##################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##################################################################
prt = sys.stdout.write                                           #
def debug(var, name=""):                                         #
    if DEBUG:                                                    #
        prt(f"{debugGreen}{name.upper()}: {var}{debugEnd}\n")    #
def out(x):                                                      #
    prt(f"{debugCyan}{x}{debugEnd}\n")if DEBUG else prt(f"{x}\n")#
if DEBUG: print = out                                            #
def intspls():                                                   #
    ints = list(map(int, sys.stdin.readline().strip().split()))  #
    return ints if len(ints)>1 else ints[0]                      #
def intpls(): return int(input())                                #
def listpls(): return input().split()                            #
def stringpls(): return sys.stdin.readline().strip()             #
##################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def solve():
    r, c, n = intspls()
    points = [tuple(intspls()) for _ in range(n)]
    points = set(points)
    q = deque(points)
    steps = 0
    seen = set()
    while len(q) != 0:
        for node in range(len(q)):
            curr = q.popleft()
            y = curr[0]
            x = curr[1]
            if (y,x) in seen: 
                continue
            seen.add(curr)
            if y != 1:
                q.append((y-1, x))

            if y != r:
                q.append((y+1, x))

            if x != 1:
                q.append((y, x-1))

            if x != c:
                q.append((y, x+1))
        steps += 1
    print(steps-1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
