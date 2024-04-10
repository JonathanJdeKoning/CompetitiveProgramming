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
def solve():
    numships, attacks = map(int, input().split())
    ships = list(map(int, input().split()))
    ships = deque(ships)
    s = sum(ships)
    if s <= attacks: print(numships);return
    
    attacking_left = True
    total = 0
    while attacks > 0:
        left = ships[0]
        right = ships[-1]
        mn = min(left, right)

        cankill = False
        if left == right:
            cankill = attacks >= (left*2)-1
        else:
            if left == mn and attacking_left:
                cankill = attacks >= (left*2)-1
            elif left == mn and not attacking_left:
                cankill = attacks >= (left*2)
            elif right == mn and attacking_left:
                cankill = attacks >= (right*2)
            elif right == mn and not attacking_left:
                cankill = attacks >= (right*2) - 1
        if not cankill:
            print(total)
            return


        if left == right:
            if attacking_left:
                ships.popleft()
                ships[-1] = 1
            else:
                ships.pop()
                ships[0] = 1
            attacking_left = not attacking_left    
            attacks -= (left*2) -1
            total += 1
            continue
        else:
            leftdies = left < right
            if leftdies and attacking_left:
                ships.popleft()
                ships[-1] -= (left-1)
                attacks += 1
                attacking_left = not attacking_left
            elif leftdies and not attacking_left:
                ships.popleft()
                ships[-1] -= left
            elif not leftdies and attacking_left:
                ships.pop()
                ships[0] -= right
            elif not leftdies and not attacking_left:
                ships.pop()
                ships[0] -= (right-1)
                attacks += 1
                attacking_left = not attacking_left
            total += 1
            attacks -= mn*2
    print(total)
    return
         


#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    for _ in range(int(input())):
        solve()                #
############################
