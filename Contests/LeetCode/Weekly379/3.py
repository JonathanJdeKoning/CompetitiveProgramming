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
    nums1 = [9,8,4,7]
    nums2 = [5,5,9,5]
    n = len(nums1)//2
    both = nums1 + nums2
    count = dict(Counter(both).items())
    while (len(nums1) != n) or (len(nums2) != n):
        print(count)
        maxval = -1
        maxi = -1
        if len(nums2) == n:
            maxi = max(set(nums1), key=nums1.count)
        if len(nums1) == n:
            maxi = max(set(nums2), key = nums2.count)
        
        if len(nums1) != n and len(nums2) != n:
            for key, val in count.items():
                if val > maxval:
                    maxval = val
                    maxi = key

        print(maxi)
        if nums1.count(maxi)> nums2.count(maxi) or len(nums2) == n:
            nums1.remove(maxi)
        else:
            nums2.remove(maxi)
        count[maxi]-=1
    print(nums1)
    print(nums2)
    return(len(set(nums1+nums2)))
#~~~~~~~~~~~~~~~~~~~~~~~~~~
############################
if __name__ == "__main__": #
    print(solve())                #
############################
