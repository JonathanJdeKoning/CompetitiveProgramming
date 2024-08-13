n,x,y = map(int, input().split())
from math import inf
import heapq
sweet = list(map(int, input().split()))
salt = list(map(int, input().split()))
dishes = [(sweet[i], salt[i]) for i in range(n)]

dishes.sort(reverse=True)
mn = n

for i, dish in enumerate(dishes, start=1):
    x-=dish[0]
    if x < 0:
        mn = min(mn, i)
        break

dishes.sort(reverse=True, key=lambda x:x[1])

for i, dish in enumerate(dishes, start=1):
    y-=dish[1]
    if y < 0:
        mn = min(mn, i)
        break

print(mn)

