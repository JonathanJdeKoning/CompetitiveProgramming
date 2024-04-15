import heapq
n, q = map(int, input().split())
houses = list(map(int, input().split()))
heapq.heapify(houses)
for kid in list(map(int, input().split())):
    print(sum(heapq.nsmallest(kid,houses)))
