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
    insts = []
    while True:
        try:
            op = input()
            if op == "up":
                insts.append((-1,0))
            elif op == "down":
                insts.append((1,0))
            elif op == "right":
                insts.append((0,1))
            elif op == "left":
                insts.append((0,-1))
        except EOFError:
            break

    path = [(0,0)]
    curr = [0,0]
    for inst in insts:
        curr[0] += inst[0]
        curr[1] += inst[1]
        path.append(tuple(curr))
    maxnegy = min([x[0] for x in path])
    maxnegx = min([x[1] for x in path])
    newpath = []
    for node in path:
        newpath.append((node[0]+abs(maxnegy)+1, node[1]+abs(maxnegx)+1))

    rows = max([x[0] for x in newpath])+2
    cols = max([x[1] for x in newpath])+2
    mat = []
    mat.append(list("#"*cols))
    for i in range(rows-2):
        s = "#" + " "*(cols-2) + "#"
        mat.append(list(s))
    mat.append(list("#"*cols))

    start = newpath[0]
    end = newpath[-1]

    
    for node in newpath[1:-1]:
        mat[node[0]][node[1]] = "*"



    mat[start[0]][start[1]] = "S"
    mat[end[0]][end[1]] = "E"
    for row in mat:
        print("".join(row))
#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
