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
    x1,y1 = intspls()
    x2,y2 = intspls()
    x3,y3 = intspls()
    points = [(x1, y1), (x2, y2), (x3,y3)]
    xs = [x1,x2,x3]
    ys = [y1,y2,y3]
    if len([x for x in xs if x in ys]) == 2:
        missingy = [x for x in xs if x not in ys][0]
        missingx = [y for y in ys if y not in xs][0]
        print(f"{missingx} {missingy}")
        return
    all = xs+ys
    for dot in all:
        if all.count(dot) >= 3:
            print(f"{[x for x in xs if xs.count(x) == 1][0]} {[y for y in ys if ys.count(y) == 1][0]}")
            return
    mid = None
    for i, point in enumerate(points):
        x = point[0]
        y = point[1]
        
        a,b = [x for x in points if x != point]

        
        ax = a[0]
        ay = a[1]
        bx = b[0]
        by = b[1]

        arise = ay-y
        arun = ax-x 
        brise = by - y
        brun = bx -x
        
        debug(point, "point")
        debug(a, "a")
        debug(b, "b")
        debug(arise, "a rise")
        debug(arun, "a run")
        debug(brise, "b rise")
        debug(brun, "b run")

        arisedist = abs(arise)
        brisedist = abs(brise)
        arundist = abs(arun)
        brundist = abs(brun)
        if abs(arise) == abs(brun) and abs(arun) == abs(brise):
            mid = point
            pos = []
            pos.append((ax+arisedist, arundist+ay))
            pos.append((ax-arisedist, arundist+ay))
            pos.append((arisedist+ax, ay-arundist))
            pos.append((ax-arisedist, ay-arundist))
            pos.append((brisedist+bx, brundist+by))
            pos.append((bx-brisedist, brundist+by))
            pos.append((brisedist+bx, by-brisedist))
            pos.append((bx-brisedist, by-brundist))
            debug(pos, "pos")
            ans = [x for x in pos if pos.count(x) == 2][0]
            print(f"{ans[0]} {ans[1]}")
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    solve()                #
############################
