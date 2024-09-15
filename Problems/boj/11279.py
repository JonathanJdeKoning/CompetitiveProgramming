import sys
input = sys.stdin.readline

n = int(input())
import heapq
h = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if not h:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(-heapq.heappop(h))+"\n")

    else:
        heapq.heappush(h, -x)

