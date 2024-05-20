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
input = sys.stdin.readline
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
    s = list(map(int, input().split()))
    gen=a=b=c=defaultdict(int)
    for i in range(n-2):
        slc = s[i:i+3]
        
        bc,ac,ab=slc[:],slc[:],slc[:]
        bc[0]=ac[1]=ab[2]="?"
        
        total += a[tuple(bc)] + b[tuple(ac)] + c[tuple(ab)] - (3*gen[tuple(slc)])
       
        gen[tuple(slc)] += 1
        a[tuple(bc)]    += 1
        b[tuple(ac)]    += 1
        c[tuple(ab)]    += 1
    return total


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###################################
if __name__ == "__main__":        #
    for _ in range(int(input())): #
        print(solve())            #
###################################
