import sys
from collections import deque
from heapq import *
sys.stdin = open("day13.in", "r")
ans1 = 0
ans2 = 0
lines = [line.strip() for line in open("day13.in", "r")]
games = lines.count("")+1
for game in range(games):
    a = input().strip()
    ax, ay = list(map(int, "".join([x for x in a if x.isdigit() or x == ","]).split(",")))
    b = input().strip()
    bx, by = list(map(int, "".join([x for x in b if x.isdigit() or x == ","]).split(",")))
    p = input().strip()
    px, py = list(map(int, "".join([x for x in p if x.isdigit() or x == ","]).split(",")))
    h = [(0, 0, 0, 0, 0)]
    seen = set()
    while h:
        currCost, currA, currB, currX, currY = heappop(h)
        if currA > 100 or currB > 100 : continue
        if (currX, currY) in seen: continue
        seen.add((currX, currY))

        if currX == px and currY == py:
            ans1 += currCost
            break 

        heappush(h, (currCost+3, currA+1, currB, currX+ax, currY+ay))
        heappush(h, (currCost+1, currA, currB+1, currX+bx, currY+by))
        
    
    try:input()
    except EOFError: break


print(ans1)
print(ans2)
