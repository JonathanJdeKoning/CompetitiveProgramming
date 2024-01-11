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
    a,b = list(map(int, input().split()))
    c,d = list(map(int, input().split()))
    e,f = list(map(int, input().split()))

    ul = [(c,d)]
    ur = [(c,d)]
    dl = [(c,d)]
    dr = [(c,d)]
    x = d
    y = c


    for i in range(8):
        x += 1
        y += 1

        if x > 8 or y > 8:
            break
        else:
            dr.append((y,x))
            if (y,x) == (e,f):
                break
    
    x = d
    y = c


    for i in range(8):
        x -= 1
        y -= 1

        if x < 1 or y < 1:
            break
        else:
            ul.append((y,x))
            if (y,x) == (e,f):
                break
    
    x = d
    y = c


    for i in range(8):
        x -= 1
        y += 1

        if x < 1 or y > 8:
            break
        else:
            dl.append((y,x))
            if (y,x) == (e,f):
                break
    x = d
    y = c



    for i in range(8):
        x += 1
        y -= 1
        if x < 1 or y > 8:
            break
        else:
            ur.append((y,x))
            if (y,x) == (e,f):
                break
    if a == e:
        if c == a:
            if b < d < f or f < d < b:
                return 2
            else:
                return 1
        else:
            return 1

    if b == f:
        if d == b:
            if a <c < e or e < c < a:
                
                return 2
            else:
                return 1
        else:
            return 1

    if (e,f) in ul:
        if (a,b) in ul:
            return 2
        return 1
    if (e,f) in ur:
        if (a,b) in ur:
            return 2
        return 1
    if (e,f) in dr:
        if (a,b) in dr:
            return 2
        return 1
    if (e,f) in dl:
        if (a,b) in dl:
            return 2
        return 1
    return 2

#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    print(solve())                #
############################
