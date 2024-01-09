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

    def outside(tup, rows, cols):
        y = tup[0]
        x = tup[1]

        if y<0 or x<0 or y>rows-1 or x>cols-1:
            return True
        return False


    r, c = intspls()
    mat = []
    for _ in range(r):
        mat.append(list(map(int, list(input()))))
    debug(mat, "mat")

    q = deque([(0,0)])
    start= (  0   ,  0   )
    end  = (r-1,c-1)
    debug(start, "start")
    debug(end, "end")
    steps = -1
    seen = set()
    while q:
        steps += 1
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == end:
                print(steps)
                return 
            y = curr[0]
            x = curr[1]
            hops = mat[y][x]

            u = (y-hops, x)
            d = (y+hops, x)
            l = (y, x-hops)
            ri = (y, x+hops)
            
            if not outside(u,r,c) and u not in seen:
                q.append(u)
                seen.add(u)
            if not outside(d,r,c) and d not in seen:
                q.append(d)
                seen.add(d)
            if not outside(l,r,c) and l not in seen:
                q.append(l)
                seen.add(l)
            if not outside(ri,r,c) and ri not in seen:
                q.append(ri)
                seen.add(ri)
    print(-1)


#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
