from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def ints(): return list(map(int, input().split()))
def intmat(R): return [ints() for _ in range(R)]
def outs(A, delim=" "): print(delim.join(map(str, A)))
def outmat(M): list(map(outs, M))

##########################################################

N,M,X,Y = ints()
A = intmat(N)
B = intmat(X)

for i in range((N-X)+1):
    for j in range((M-Y)+1):
        good = True 
        for k in range(X):
            for l in range(Y):
                if A[i+k][j+l] != B[k][l]:
                    good = False

        if good:
            exit(print("YES"))
print("NO")
