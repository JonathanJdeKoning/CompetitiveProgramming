import os
import sys 
from math import ceil, floor, pi, sqrt, gcd
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
    mx = -1
    mxy = -1
    x = int(input())

    for y in range(x-1,0,-1):
        if gcd(x,y)+1 > mx:
            mx = gcd(x,y)+1
            mxy = y

    return mxy


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###################################
if __name__ == "__main__":        #
    for _ in range(int(input())): #
        print(solve())            #
###################################
