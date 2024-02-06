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
    case = 0
    while True:
        case += 1
        try:
            rows, cols = list(map(int, input().split()))
            mat = []
            for _ in range(rows):
                mat.append(list(input()))
            count = 0

            seen = set()
            for i, row in enumerate(mat):
                for j, x in enumerate(row):
                    if x == "-" and (i,j) not in seen:
                        count += 1
                        q = deque([(i,j)])
                        while q:
                            debug(q, "q")
                            curr = q.popleft()
                            seen.add((curr[0],curr[1]))
                            directions = [[0,1],[1,0],[0,-1],[-1,0]]

                            debug(curr, "curr") 
                            for dy, dx in directions:
                                y = curr[0]
                                x = curr[1]
                                y += dy
                                x += dx
                                
                                if y >= rows or x >= cols or y<0 or x < 0 or (y,x) in seen:
                                    continue
                                if mat[y][x] == "-":
                                    q.append((y,x))
                            
            debug(seen, "seen")
            print(f"Case {case}: {count}")

        except EOFError:
            break

#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
