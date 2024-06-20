from math import ceil, floor
numWires, n = map(int, input().split())
wires = [int(input()) for _ in range(numWires)]

bestCut = 0

l = 1
r = max(wires) 

while l<=r:
    mid = (l+r)//2
    totalLengths = sum([wire//mid for wire in wires])
    if totalLengths < n:
        r = mid-1
        continue
    if mid > bestCut:
        bestCut = mid
    l=mid+1
print(bestCut)
    

