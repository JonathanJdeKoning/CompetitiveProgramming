import os
import sys 
from math import ceil, floor, pi, sqrt, inf
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
    length = int(input())
    road = input()
    ones = road.count("1")
    zeros = 0 

    if ones == 0:
        print(length)
        return

    midpoint = length/2
    best = 0
    bestdist = abs(0-midpoint)
    for i,x in enumerate(road,start=1):
        if x == "1": ones -= 1
        if x == "0": zeros += 1

        if zeros >= ceil(i/2) and ones >= ceil((length-i)/2):
            dist = abs(i-midpoint)
            if dist < bestdist:
                best = i
                bestdist = dist
    print(best)
    return




#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    for _ in range(int(input())):
        solve()                #
############################
