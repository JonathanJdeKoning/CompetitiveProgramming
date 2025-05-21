from itertools import pairwise
N = int(input())
if N < 4: exit(print(0))

distFromStart = [0] + list(map(int, input().split()))
distBetween = [b-a for a, b in pairwise(distFromStart)]

mnDistBetween = min(distBetween[1:-1])
mnIdx = distBetween[1:-1].index(mnDistBetween) + 1
print(distFromStart[-1] + mnDistBetween)
print(N, 1, mnIdx+2, mnIdx+1)

