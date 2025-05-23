
from math import gcd
from itertools import pairwise 

N = int(input())
A = list(map(int, input().replace(","," ").split()))

toInsert = [gcd(a,b) == 1 for a,b in pairwise(A)]

new = []
for i in range(len(A)-1):
    num = A[i]
    nextNum = A[i+1]

    new.append(num)
    if not toInsert[i]:
        new.append(1)

new.append(A.pop())
print(toInsert.count(False))
print(" ".join([str(x) for x in new])) 
