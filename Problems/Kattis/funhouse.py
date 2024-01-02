import os
from itertools import combinations, permutations
from collections import deque, Counter, defaultdict
########################################################
DEBUG = os.path.isfile("C:\\Users\\jj720\\debug.txt") ##
########################################################

import sys 
from math import ceil, floor
def debug(var, name=""):
    if DEBUG: 
        print(f"{name.upper()}: {var}")

def intspls(): 
    ints = list(map(int, sys.stdin.readline().strip().split()))
    return ints if len(ints) > 1 else ints[0]
def stringpls(): return sys.stdin.readline().strip()

#####################
def solve():
    currhouse = 0
    while True:
        currhouse += 1
        cols, rows = intspls()
        if rows == 0 and cols == 0:
            return

        mat = []
        for _ in range(rows):
            mat.append(list(stringpls()))
        

        left = [x[0] for x in mat]
        right = [x[-1] for x in mat]
        x = None
        y = None
        ori = None        

        if "*" in mat[0]:
            ori = "D"
            y = 0
            x = mat[0].index("*")
        elif "*" in mat[-1]:
            ori = "U"
            y=rows-1
            x = mat[-1].index("*")
        elif "*" in left:
            ori = "R"
            x = 0
            y= left.index("*")
        elif "*" in right:
            ori = "L"
            x = cols-1
            y = right.index("*")
        debug(ori, "ORI")
        debug(x, "start x")
        debug(y, "start y")
        
        while True:
            curr = mat[y][x]
            if curr == "/":
                if ori == "U":
                    ori = "R"
                elif ori == "L":
                    ori = "D"
                elif ori == "R":
                    ori = "U"
                elif ori == "D":
                    ori = "L"

            elif curr == "\\":
                if ori == "U":
                    ori = "L"
                elif ori == "D":
                    ori = "R"
                elif ori == "L":
                    ori = "U"
                elif ori == "R":
                    ori = "D"
            elif curr == "x":
                mat[y][x] = "&"
                break


            if ori == "R":
                x+=1
            elif ori == "L":
                x-=1
            elif ori == "D":
                y+=1
            elif ori == "U":
                y-=1
        print(f"HOUSE {currhouse}")
        for row in mat:
            print("".join(row))



#########################
if __name__ == "__main__":
    solve()

