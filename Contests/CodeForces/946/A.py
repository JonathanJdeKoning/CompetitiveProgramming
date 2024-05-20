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
    ones, twos = map(int, input().split())
    screens = 0
    while True:
        twosneed = ceil(twos/2)
        leftover = None
        if twos%2==0:
            leftover = 7*twosneed
        else:
            leftover = 7*(twosneed-1)+11
        ones -= leftover
        need = twosneed
        while ones >0:
            need += 1
            ones -= 15
        return need


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###################################
if __name__ == "__main__":        #
    for _ in range(int(input())): #
        print(solve())            #
###################################
