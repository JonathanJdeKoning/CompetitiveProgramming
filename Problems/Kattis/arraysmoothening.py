import sys
import heapq
from collections import Counter
input = sys.stdin.readline
n,k = map(int, input().split())
nums=list(map(int, input().split()))
freq = [-x for x in list(Counter(nums).values())]
heapq.heapify(freq)
for _ in range(k):
    x = heapq.heappop(freq)
    heapq.heappush(freq, x+1)
sys.stdout.write(str(-min(freq))+"\n")
