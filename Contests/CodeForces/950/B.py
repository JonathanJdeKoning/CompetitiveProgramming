import os
import sys 
from math import ceil, floor, pi, sqrt
from itertools import combinations, permutations
from collections import deque, Counter, defaultdict
from functools import lru_cache

##################################################################
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt")            #
debugGreen,debugCyan,debugEnd = '\033[92m','\033[96m','\033[0m'  #
if DEBUG: os.system('color')                                     #
##################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##################################################################
prt = sys.stdout.write                                           #
inout = sys.stdin.readline
sys.setrecursionlimit(100000)                                    #
mod = 1000000007                                                 #
def debug(var, name=""):                                         #
    if DEBUG:                                                    #
        prt(f"{debugGreen}{name.upper()}: {var}{debugEnd}\n")    #
def out(x):                                                      #
    prt(f"{debugCyan}{x}{debugEnd}\n")if DEBUG else prt(f"{x}\n")#
if DEBUG: print = out                                            #
##################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def solve():
    numCubes, fav, numGone = map(int, input().split())
    cubes = list(map(int, input().split()))
    favNum = cubes[fav-1]
    cubes = sorted(cubes, reverse=True)
    gone = cubes[:numGone]
    left = cubes[numGone:]
    if favNum in gone:
        if favNum in left:
            return "maybe"
        else:
            return "yes"
    return "no"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###################################
if __name__ == "__main__":        #
    for _ in range(int(input())): #
        print(solve())            #
###################################
