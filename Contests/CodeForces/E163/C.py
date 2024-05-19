import os
import sys 
from math import ceil, floor, pi, sqrt
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
sys.setrecursionlimit(100000)                                    #
mod = 1000000007                                                 #
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
    n = int(input())
    grid = []
    grid.append(input())
    grid.append(input())

    start = (0,0)
    end = (1,n-1)

    seen = set()
    q = deque([start])
    while q:
        curr = q.popleft()
        if curr[0] == 1 and curr[1]==n-2 or curr[0] == 0 and curr[1] ==n-1 or curr[0]==1 and curr[1]==n-1: 
            print("YES")
            return

        if curr in seen: continue
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for dy, dx in directions:
            y = curr[0]+dy
            x = curr[1]+dx

        
            if y!=-1 and x!=-1 and y!=2 and x!=n and (y,x) not in seen:
                seen.add((y,x))
                res = grid[y][x]
                if res == ">":
                    x+=1
                else:
                    x-=1
                

            if y!=-1 and x!=-1 and y!=2 and x!=n and (y,x) not in seen:
                q.append((y,x))
    print("NO")
    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    for _ in range(int(input())):
        solve()                #
############################
