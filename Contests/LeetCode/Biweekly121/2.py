import os
import sys 
from math import ceil, floor, pi, inf
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
    x = 9995
    y = 909
    if x < y:
        retur
    memo = [inf]*(max(x,y)+13)
    memo[y]=0
    curr = 0 
    while True:
        if inf not in memo: break
        for i,pos in enumerate(memo):
            if pos == curr:
                inc = i+1
                dec = i-1
                div5 = i*5
                div11 = i*11
                try:
                    memo[inc] = min(pos+1, memo[inc])
                except: pass
                try:
                    memo[dec] = min(pos+1, memo[dec])
                except: pass
                try:
                    memo[div5] = min(pos+1, memo[div5])
                except: pass
                try:
                    memo[div11] = min(pos+1, memo[div11])
                except: pass
        curr += 1
        
    print(memo[x])
#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
