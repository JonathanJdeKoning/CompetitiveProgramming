from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def ints(): return list(map(int, input().split()))
def intmat(R): return [ints() for _ in range(R)]
def outs(A, delim=" "): print(delim.join(map(str, A)))
def outmat(M): list(map(outs, M))
def rotmat(M): return list(zip(*M[::-1]))

##########################################################

R,C = ints()

M = intmat(R)

left = R*C
out = []
currDiag = -1
while True:
    currDiag += 1
    y, x = 0, currDiag
    diag = []
    while True:
        if y == R or x < 0:
            if currDiag %2==1:
                out.extend(diag)
            else:
                out.extend(diag[::-1])
            break
        else:
            if x < C:
                diag.append(M[y][x])
                left -= 1
                if left ==0:
                    if currDiag %2==1:
                        out.extend(diag)
                    else:
                        out.extend(diag[::-1])
                    break
            
            y += 1
            x -= 1
    if left == 0:
        break

outs(out)


