from collections import defaultdict
N = 8
bad = defaultdict(int)
for i in range(N):
    row = input()
    for j in range(N):
        if row[j] == "*":
            bad[(i,j)] += 1

ans = 0
def place_queen(queensleft, y, x):
    global ans
    if queensleft == 0: 
        ans += 1
        return
    mine = set()
    for n in range(N):
        mine.add((y,n))
        mine.add((n, x))
        if y+n < N and x+n < N:
            mine.add((y+n, x+n))
        if y-n > -1 and x-n > -1:
            mine.add((y-n, x-n))
        if y+n < N and x-n > -1:
            mine.add((y+n, x-n))
        if y-n > -1 and x+n < N:
            mine.add((y-n, x+n))
    for cell in mine:
        bad[cell] += 1


    for j in range(N):
        if (y+1,j) in bad:
            continue
        place_queen(queensleft-1, y+1, j)
    
    for cell in mine:
        bad[cell] -= 1
        if bad[cell] == 0: del bad[cell]

for j in range(N):
    if (0,j) in bad: continue
    place_queen(N-1, 0, j)
print(ans)