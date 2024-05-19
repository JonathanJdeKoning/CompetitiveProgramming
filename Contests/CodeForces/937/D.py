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

good = {1, 11010, 11011, 10, 11, 10000, 10001, 13310, 10010, 10011, 100000, 12321, 14641, 12210, 1331, 1210, 12221, 12100, 1221, 11211, 1100, 1101, 12111, 1110, 1111, 10201, 11100, 11101, 121, 100, 101, 11110, 11111, 1000, 1001, 110, 111, 11121, 1010, 1011, 10100, 10101, 13431, 11000, 11001, 10110, 10111}

def solve():
    for _ in range(int(input())):
        n = int(input())
        if n in good:
            print("YES")
        else:
            print("NO")


#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
