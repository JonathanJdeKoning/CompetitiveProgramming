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
    time, rows, cols = intspls()
    start = None
    mat = []
    for i in range(rows):
        row = input()
        mat.append(list(row))
        if "S" in row:
            start = (i, row.index("S"))

    debug(start, "start")
    debug(mat, "mat")
    q = deque([start])
    seen = set()
    steps = -1
    done = False
    while not done:
        steps += 1
        debug(q, "q")
        for _ in range(len(q)):
            curr = q.popleft()
            y = curr[0]
            x = curr[1]
            
            if x == 0 or y == 0 or x == cols-1 or y == rows-1:
                if steps <= time:
                    print(steps)
                else:
                    print("NOT POSSIBLE")
                done = True
                break
            up = (y-1, x)
            down = (y+1, x)
            left = (y, x-1)
            right = (y, x+1)

            rep = mat[up[0]][up[1]]
            if (rep == "0" or rep == "D") and up not in seen:
                q.append(up)
                seen.add(up)

            rep = mat[down[0]][down[1]]
            if (rep == "0" or rep == "U") and down not in seen:
                q.append(down)
                seen.add(down)

            rep = mat[left[0]][left[1]]
            if (rep == "0" or rep == "R") and left not in seen:
                q.append(left)
                seen.add(left)

            rep = mat[right[0]][right[1]]
            if (rep == "0" or rep == "L") and right not in seen:
                q.append(right)
                seen.add(right)
            if len(q) == 0:
                print("NOT POSSIBLE")
                done = True

#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
