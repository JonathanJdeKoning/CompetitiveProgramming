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
    rows, cols = intspls()
    mat = []
    for i in range(rows):
        mat.append(list(sys.stdin.readline().strip()))

    
    for i in range(intpls()):
        found = False
        y1,x1,y2,x2 = intspls()

        y1 -= 1
        y2 -= 1
        x1 -= 1
        x2 -= 1
        if mat[y1][x1] != mat[y2][x2]: 
            print("neither")
            continue
        person = None
        if mat[y1][x1] == "0": person = "binary"
        else:
            person = "decimal"
        
        start = mat[y1][x1]
        end = (y2,x2)
        
        q = deque([(y1,x1)])
        seen = set()
        while q:
            curr = q.popleft()
            if curr in seen: continue
            if curr == end: 
                print(person)
                found = True
                break
            seen.add(curr)
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for dy, dx in directions:
                y = curr[0] + dy
                x = curr[1] + dx
                
                if y < 0 or x < 0 or y >= rows or x >= cols: continue
        
                new = (y,x)
                if mat[new[0]][new[1]] != start:
                    continue
                if new not in seen:
                    q.append(new)
                    
        if not found:
            print("neither")







#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
