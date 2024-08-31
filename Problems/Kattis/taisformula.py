n = int(input())

samples = []

for _ in range(n):
    time, x = map(float, input().split())
    samples.append((time, x))

from itertools import pairwise

ans = 0
for (aTime, aX), (bTime, bX) in pairwise(samples):
    ans += (((aX+bX)/2)  * (bTime - aTime))/1000

print(ans)
