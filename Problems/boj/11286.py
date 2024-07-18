import heapq
import sys
input = sys.stdin.readline
qs = int(input())
h = []
for _ in range(qs):
    q = int(input())

    if q==0:
        if not h: sys.stdout.write("0\n")
        else: sys.stdout.write(str(heapq.heappop(h)[1])+"\n")
    else:
        heapq.heappush(h, (abs(q),q))

