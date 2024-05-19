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
    n, k, bodStart, sashStart = map(int, input().split())
    bodStart -= 1
    sashStart -= 1
    perm = list(map(lambda x: int(x)-1, input().split()))
    arr = list(map(int, input().split()))
    gold = max(arr)
    bodSeen = {bodStart}
    bodPath = [arr[bodStart]]
    bodCurr = bodStart


    t = k
    bodSum = sum(bodPath) 
    bodMax = bodSum*t
    t -= 1
    while t != 0:
        bodCurr = perm[bodCurr]
        if bodCurr in bodSeen: break
        
        bodMax = max(bodSum + arr[bodCurr]*t, bodMax)

        bodSum += arr[bodCurr]
        bodPath.append(arr[bodCurr])
        bodSeen.add(bodCurr)
        
        if arr[bodCurr] == gold: break
        t -= 1

    sashSeen = {sashStart}
    sashPath = [arr[sashStart]]
    sashCurr = sashStart


    t = k
    sashSum = sum(sashPath) 
    sashMax = sashSum*t
    t -= 1
    while t != 0:
        sashCurr = perm[sashCurr]
        if sashCurr in sashSeen: break
        
        sashMax = max(sashSum + arr[sashCurr]*t, sashMax)

        sashSum += arr[sashCurr]
        sashPath.append(arr[sashCurr])
        sashSeen.add(sashCurr)
        
        if arr[sashCurr] == gold: break
        t -= 1

    if bodMax > sashMax:
        return "Bodya"
    elif sashMax> bodMax:
        return "Sasha"
    return "Draw"


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###################################
if __name__ == "__main__":        #
    for _ in range(int(input())): #
        print(solve())            #
###################################
