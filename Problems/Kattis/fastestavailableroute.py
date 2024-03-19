import os
import sys 
from math import ceil, floor, pi, sqrt
from itertools import combinations, permutations
from collections import deque

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
    h, w ,s = map(int, input().split())
    mat= []
    start = (0,0)
    for i in range(h):
        row = input()
        if "@" in row:
            start = (i,row.index("@"))
        mat.append(list(row))
    debug(mat, "mat")
    debug(start, "start")

    q = deque([start])
    steps = -1
    seen = set()
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    while q:
        steps += 1
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in seen: continue
            if mat[curr[0]][curr[1]] == "$":
                print(f"Your destination will arrive in {steps*s} meters")
                return
            seen.add(curr)

            for dy, dx in directions:
                y = curr[0]+ dy
                x = curr[1] + dx

                if y == -1 or x == -1 or y==h or x == w or (y,x) in seen: continue
                if mat[y][x]== "." or mat[y][x] == "$":
                    q.append((y,x))

            

        


#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
