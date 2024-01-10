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
    mat = []
    rows, cols = intspls()
    for _ in range(rows):
        mat.append(list(input()))

    debug(mat, "mat")
    seen = set()
    lands = 0
    for i, row in enumerate(mat):
        for j, pos in enumerate(row):
            if (i,j) in seen: continue
            if pos == "#":
                q = deque([(i,j)])
                lands += 1
                while q:
                    for _ in range(len(q)):
                        curr = q.popleft()
                        if curr in seen: continue
                        debug(curr, "curr")
                        seen.add(curr)
                        y = curr[0]
                        x = curr[1]
                        
                        u = (y-1,x)
                        d = (y+1, x)
                        l = (y, x-1)
                        r = (y, x+1)

                        ul = (y-1, x-1)
                        ur = (y-1, x+1)
                        dl = (y+1, x-1)
                        dr = (y+1, x+1)

                        if u[0] >= 0 and u not in seen and mat[u[0]][u[1]]=="#":
                            q.append(u)
                        if d[0]<rows and d not in seen and mat[d[0]][d[1]]=="#":
                            q.append(d)
                        if l[1] >= 0 and l not in seen and mat[l[0]][l[1]]=="#":
                            q.append(l)
                        if r[1]<cols and r not in seen and mat[r[0]][r[1]]=="#":
                            q.append(r)

                        if ul[0] >= 0 and ul[1] >= 0 and ul not in seen and mat[ul[0]][ul[1]] == "#":
                            q.append(ul)
                        if ur[0] >= 0 and ur[1]<cols and ur not in seen and mat[ur[0]][ur[1]] == "#":
                            q.append(ur)
                        if dl[0] < rows and dl[1]>=0 and dl not in seen and mat[dl[0]][dl[1]] == "#":
                            q.append(dl)
                        if dr[0]<rows and dr[1]<cols and dr not in seen and mat[dr[0]][dr[1]] == "#":
                            q.append(dr)
    print(lands)
                        


#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
