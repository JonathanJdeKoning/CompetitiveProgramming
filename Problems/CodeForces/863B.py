
from itertools import pairwise
N = int(input())
A = list(map(int, input().replace(","," ").split()))
A.sort()
ans = float("inf")

for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        new = A[:i] + A[i+1:j] + A[j+1:]
        inst = 0
        for k in range(0,len(new),2):
            inst += new[k+1] - new[k]
        ans = min(ans, inst)
print(ans)