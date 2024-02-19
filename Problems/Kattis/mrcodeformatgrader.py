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
def intspls():                                                   #
    ints = list(map(int, sys.stdin.readline().strip().split()))  #
    return ints if len(ints)>1 else ints[0]                      #
def intpls(): return int(input())                                #
def listpls(): return input().split()                            #
def stringpls(): return sys.stdin.readline().strip()     
from time import sleep#
##################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def solve():
    total, numerrors = intspls()
    errors = list(map(int, input().split()))
    corrs = []
    for i in range(1, total+1): 
        if i not in errors:
            corrs.append(i)

    
    idx = 0
    done = False

    wack = []
    while True:
        curr = errors[idx]
        next = idx+1
        prev = curr
        rng = [curr]
        while True:
            if next >= len(errors): 
                done =True
                break
            nexterr = errors[next]
            if nexterr == prev+1:
                prev = nexterr
                next += 1
                continue
            else:
                rng.append(prev)
                idx = next
                wack.append(rng)
                break
        if done: break
    print("Errors: ",end="")
    if len(wack) != 0:
        for i, rng in enumerate(wack):
            
            if i != len(wack)-1:
                if rng[0] == rng[1]:
                    print(f"{rng[0]}, ", end="")
                else:
                    print(f"{rng[0]}-{rng[1]}, ",end="")
            else:
                if rng[0] == rng[1]:
                    print(f"{rng[0]} ", end="")
                else:
                    print(f"{rng[0]}-{rng[1]} ",end="")

        print("and ", end="")
        curr = errors[-1]
        start = curr
        end = curr
        for i in range(len(errors)-2,-1,-1):
            if errors[i] != end-1:
                break
            else:
                end -= 1
        if start == end:
            print(start)
        else:
            print(f"{end}-{start}")
    else:
        if len(errors) == 1:
            print(errors[0])
        else:
            print(f"{errors[0]}-{errors[-1]}")






    
    idx = 0
    done = False

    wack = []
    while True:
        curr = corrs[idx]
        next = idx+1
        prev = curr
        rng = [curr]
        while True:
            if next >= len(corrs): 
                done =True
                break
            nexterr = corrs[next]
            if nexterr == prev+1:
                prev = nexterr
                next += 1
                continue
            else:
                rng.append(prev)
                idx = next
                wack.append(rng)
                break
        if done: break
    print("Correct: ", end="")
    if len(wack) != 0:
        for i, rng in enumerate(wack):
            if i != len(wack)-1:
                if rng[0] == rng[1]:
                    print(f"{rng[0]}, ", end="")
                else:
                    print(f"{rng[0]}-{rng[1]}, ",end="")
            else:
                if rng[0] == rng[1]:
                    print(f"{rng[0]} ", end="")
                else:
                    print(f"{rng[0]}-{rng[1]} ",end="")

        print("and ", end="")
        curr = corrs[-1]
        start = curr
        end = curr
        for i in range(len(corrs)-2,-1,-1):
            if corrs[i] != end-1:
                break
            else:
                end -= 1
        if start == end:
            print(start)
        else:
            print(f"{end}-{start}")
    else:
        if len(corrs) == 1:
            print(corrs[0])
        else:
            print(f"{corrs[0]}-{corrs[-1]}")




        



#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
