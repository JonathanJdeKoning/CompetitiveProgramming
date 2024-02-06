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
    l2n = {"A":1, "B": 2, "C":3, "D": 4, "E": 5, "F": 6, "G":7, "H":8}
    n2l = {1: "A", 2:"B", 3:"C", 4:"D", 5: "E", 6:"F",7:"G",8:"H" }

    for _ in range(intpls()):
        x1,y1,x2,y2 = listpls()
        x1 = l2n[x1]
        x2 = l2n[x2]
        y1 = int(y1)
        y2 = int(y2)

        directions = [[1,1],[-1,-1],[1,-1],[-1,1]]
        poss = [[y1, x1]]
        for dy, dx in directions:
            x = x1
            y = y1
            while x < 9 and x > 0 and y <9 and y > 0:
                x+=dx
                y+=dy

                if x ==0 or x == 9 or y ==0 or y == 9:
                    continue
                poss.append([y,x])
            debug(poss, "poss")
        debug(f"{y2=} {x2=}")
        if [x2, y2] not in poss:
            print("Impossible")


#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
