n  = int(input())

import heapq
a = list(map(int, input().split()))
h = []
for idx, val in enumerate(a, start=1):
    heapq.heappush(h, (-val, idx))

out = []
while h:
    val, idx = heapq.heappop(h)
    out.append(idx)

print(" ".join(map(str, out)))
