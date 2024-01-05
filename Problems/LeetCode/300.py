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

    nums = [4,10,4,3,8,9]
    memo = [1]*len(nums)
    #[3, 1, 3, 3, 2, 1]
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                memo[i] = max(memo[i], 1+memo[j])
#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
