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
    paths = intpls()
    for _ in range(paths):
        input()
        lens = intpls()
        
        safe = defaultdict(set)
        y,x = 0,0
        prev = (y,x)
        

        for i in range(lens):
            op = input()
            if op == "N": 
                y -=1
                safe[prev].add("N")
                safe[(y,x)].add("S")

            if op == "S": 
                y += 1
                safe[prev].add("S")
                safe[(y, x)].add("N")
            if op == "E": 
                x += 1
                safe[prev].add("E")
                safe[(y, x)].add("W")


            if op == "W": 
                x -= 1
                safe[prev].add("W")
                safe[(y,x)].add("E")

            prev = (y,x)
        end = (y,x)
        debug(safe, "safe") 

        
        y, x = 0,0
        q = deque([])
        q.append((y,x))
        
        seen = set()
        steps = 0
        done = False
        while True and not done:
            debug(q, "q")
            for _ in range(len(q)):
                curr = q.popleft()
                
                seen.add(curr)
                if curr == end: 
                    print(steps)
                    done = True
                    break
                
                y, x = curr[0], curr[1]

                down = (y+1, x)
                up = (y-1, x)
                left = (y, x-1)
                right = (y, x+1)

                if up not in seen and up in safe and "N" in safe[curr]:
                    q.append(up)
                if down not in seen and down in safe and "S" in safe[curr]:
                    q.append(down)
                if left not in seen and left in safe and "W" in safe[curr]:
                    q.append(left)
                if right not in seen and right in safe and "E" in safe[curr]:
                    q.append(right)
            steps += 1
            








#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
