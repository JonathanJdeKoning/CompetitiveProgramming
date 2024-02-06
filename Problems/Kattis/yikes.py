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
    for _ in range(int(input())):
        max_speed = float(input())
        cycle_speed = float(input())
        line_dist = float(input())
        start_time = float(input())
        radius = 0.5
        bikes = []
        start = -line_dist
        for i in range(10):
            bikes.append([start-2,start])
            start -= 4

        debug(bikes, "bikes")
        ## SKIP TO DASH
        move = cycle_speed*start_time
        move += cycle_speed*(max_speed/5)
        for i in range(len(bikes)):
            bike = bikes[i]
            bike[0] += move
            bike[1] += move
        debug(bikes, "bikes")

        for i,bike in enumerate(bikes):
            if bike[0] <= 0 and bike[1] >= 0:
                print(f"Collision with bicycle {i+1}")

        uptime = 1/max_speed
        upmove = cycle_speed*uptime
        if bikes[0][1] + upmove < 0:
            print("Max beats the first bicycle")












#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
