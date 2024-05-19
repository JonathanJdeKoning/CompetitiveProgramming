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
##################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    rep = None
    for _ in range(k):
        mx = 0
        for i, num in enumerate(nums[:-1]):
            diff = num - nums[i+1]
            if abs(diff) > mx:
                mx = abs(diff)

                if diff > 0:
                    rep = (i,nums[i+1])
                elif diff < 0:
                    rep  = (i+1, num)
        if rep:
            nums[rep[0]] = rep[1]
    return sum(nums)




#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    for _ in range(int(input())):
        print(solve())                #
############################
