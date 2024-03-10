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
if DEBUG: print = out
def intspls():                                                   #
    ints = list(map(int, sys.stdin.readline().strip().split()))  #
    return ints if len(ints)>1 else ints[0]                      #
def intpls(): return int(input())                                #
def listpls(): return input().split()                            #
def stringpls(): return sys.stdin.readline().strip()             #
##################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def solve():
    for i in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        ss = sorted(nums)
        worry = 0
        if 0 in nums:
            for i in range(len(nums)):
                if ss[i] == worry+1:
                    worry = ss[i]
                elif ss[i] == worry: continue
                else:
                    break
        else:
            print(3)
            print("1 1")
            print("2 2")
            print(f"3 {len(nums)}")
            continue

        #debug(worry, "worry")
        if len(set(nums)) == 1:
            if len(nums) == 2:
                print(2)
                print("1 1")
                print("2 2")
                continue
            else:
                print(3)
                print("1 1")
                print("2 2")
                print(f"3 {len(nums)}")
                continue
        count = dict(Counter(nums))
        start = 1
        end = 0
        pockets = []
        tofind = list(range(worry+1))
        for i, num in enumerate(nums):
            end += 1
            if num in tofind:
                tofind.remove(num)
                if len(tofind) == 0:
                    pockets.append([start, end])
                    start = end+1
                    tofind = list(range(worry+1))
        
        if len(pockets) < 2:
            print(-1)
        else:
            pockets[-1][1] = len(nums)
            print(len(pockets))
            for pocket in pockets:
                print(f"{pocket[0]} {pocket[1]}")


#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
