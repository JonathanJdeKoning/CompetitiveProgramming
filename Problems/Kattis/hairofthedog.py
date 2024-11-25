from itertools import pairwise
N = int(input())
ans = 0
A = [input() for _ in range(N)]
A.append("sober")
for a,b in pairwise(A):
    if a == "drunk" and b == "sober": ans += 1
print(ans)