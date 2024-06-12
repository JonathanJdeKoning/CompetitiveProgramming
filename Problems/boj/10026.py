cow = []
human = []

n = int(input())
for _ in range(n):
    humrow = input()
    cowrow = humrow.replace("G", "R")
    cow.append(list(cowrow))
    human.append(list(humrow))

h = 0
c = 0
directions = [(0,-1),(0,1),(-1,0),(1,0)]
seen = set()
for i in range(n):
    for j in range(n):
        if (i,j) not in seen:
            cell = human[i][j]
            stack = [(i,j)]
            h += 1       
            while stack:
                curr = stack.pop()
                if curr in seen: continue
                seen.add(curr)

                for dy, dx in directions:
                    y = curr[0]+dy 
                    x = curr[1]+dx

                    if min(y,x)==-1 or max(y,x)==n or (y,x) in seen or human[y][x] != cell: continue
                    stack.append((y,x))

seen = set()
for i in range(n):
    for j in range(n):
        if (i,j) not in seen:
            cell = cow[i][j]
            stack = [(i,j)]
            c += 1       
            while stack:
                curr = stack.pop()
                if curr in seen: continue
                seen.add(curr)

                for dy, dx in directions:
                    y = curr[0]+dy 
                    x = curr[1]+dx

                    if min(y,x)==-1 or max(y,x)==n or (y,x) in seen or cow[y][x] != cell: continue
                    stack.append((y,x))


print(h,c)
