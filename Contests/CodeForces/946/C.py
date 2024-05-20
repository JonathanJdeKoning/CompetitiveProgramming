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
    total = 0
    n = int(input())
    gen = defaultdict(int)
    s = list(map(int, input().split()))
    first = defaultdict(int)
    second = defaultdict(int)
    third = defaultdict(int)
    for i in range(n-2):
        slc = s[i:i+3]
        one = slc[:]
        two = slc[:]
        three = slc[:]
        one[0] = "?"
        two[1] = "?"
        three[2] = "?"
        total += first[tuple(one)]-gen[tuple(slc)]
        total += second[tuple(two)]-gen[tuple(slc)]
        total += third[tuple(three)]-gen[tuple(slc)]
        gen[tuple(slc)] += 1
        first[tuple(one)] += 1
        second[tuple(two)] += 1
        third[tuple(three)] += 1
    #print(gen)
    #print(first)
    #print(second)
    #print(third)
    #for key, val in gen.items():
    return total


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###################################
if __name__ == "__main__":        #
    for _ in range(int(input())): #
        print(solve())            #
###################################
