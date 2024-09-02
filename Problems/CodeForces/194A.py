import heapq
n,k = map(int, input().split())

h = [-5]*n

curr = 5*n

while curr != k:
    heapq.heappush(h,1+heapq.heappop(h))
    curr -= 1
print(h.count(-2))
