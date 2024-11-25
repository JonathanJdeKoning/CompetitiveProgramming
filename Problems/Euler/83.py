import heapq
directions = [(0,1),(1,0),(-1,0),(0,-1)]
mat = []
with open("mat.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        mat.append([int(x) for x in line.split(",")])
seen = set()
h = [(mat[0][0], 0, 0)]
end = (79,79)

while h:
    currDist, currY, currX = heapq.heappop(h)
    if (currY, currX) in seen: continue
    if (currY, currX) == end: exit(print(currDist))
    seen.add((currY, currX))

    for dy, dx in directions:
        y,x = currY+dy, currX+dx
        if min(y,x) == -1 or max(y,x) == 80 or (y,x) in seen: continue
        heapq.heappush(h, (mat[y][x]+currDist, y, x))