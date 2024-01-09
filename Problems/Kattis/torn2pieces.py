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
    ints = list(map(int, sys.stdin.readline().strip().split()))  #                     #
def intpls(): return int(input())                                #
def listpls(): return input().split()                            #
def stringpls(): return sys.stdin.readline().strip()             #
##################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def solve():
    numstations = intpls()
    q = deque([])
    stations = defaultdict(set)
    disc = defaultdict(str)
    for _ in range(numstations):
        data = listpls()
        main = data[0]
        others = data[1:]
        for other in others:
            stations[main].add(other)
            stations[other].add(main)
    debug(stations, "stations")

    start, end = listpls()
    q.append(start)
    seen = set()
    while q:
        curr = q.popleft()
        if curr in seen: continue
        if curr == end:
            ans = [end]
            while end != start:
                ans.append(disc[end])
                end = disc[end]
            print(" ".join(ans[::-1]))
            return 


        for child in stations[curr]:
            if not disc[child]:
                disc[child] = curr
            q.append(child)
        seen.add(curr)
    print("no route found")
        



#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
