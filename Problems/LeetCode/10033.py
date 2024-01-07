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

    q = deque()
    q.append(x)
    seen = set()
    steps = 0
    found = False
    while True:
        size = len(q)
        print(q)
        for _ in range(size):
            curr = q.popleft()
            if curr == y:
                return steps
            if curr not in seen:
                seen.add(curr)
                if curr%11 == 0:
                    q.append(curr//11)
                if curr%5 == 0:
                    q.append(curr//5)
                if curr != 0:
                    q.append(curr-1)
                if curr <= max(x,y)+13:
                    q.append(curr+1)
        steps += 1
        

#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    print(solve())                #
############################
