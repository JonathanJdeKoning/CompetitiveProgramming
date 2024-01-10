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
    num_islands, num_bridges = intspls()
    connections = defaultdict(list)
    for _ in range(num_bridges):
        data = intspls()
        connections[data[0]].append(data[1])
        connections[data[1]].append(data[0])
    debug(connections, "connections")

    q = deque([1])
    island_count = 0
    seen = set()
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in seen: continue
            island_count+= 1
            seen.add(curr)
            for node in connections[curr]:
                q.append(node)
    debug(island_count, "isldn count")
    if island_count == num_islands:
        print("YES")
    else:
        print("NO")



#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
