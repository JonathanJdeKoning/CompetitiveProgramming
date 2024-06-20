import heapq
import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    n = int(input())

    if n != 0: heapq.heappush(arr, n)
    else:
        if not arr:print(0)
        else:
            sys.stdout.write(str(heapq.heappop(arr))+"\n")
