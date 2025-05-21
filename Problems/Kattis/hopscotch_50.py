from collections import defaultdict 
from math import inf
mp = defaultdict(list)
N,K = list(map(int, input().replace(","," ").split()))
dists = [[inf]*N for _ in range(N)]
mat = [[None]*N for _ in range(N)]
for i in range(N):
    row = list(map(int, input().replace(","," ").split()))
    for j in range(len(row)):
        mp[row[j]].append((i,j))
        mat[i][j] = row[j]

## ITS A DAG!!! TOPO SORT AND USE BELLMAN FORD IDIOT
def dist(t, u):
    a,b = t
    x,y = u
    return abs(a-x) + abs(y-b)

for y, x in mp[1]: dists[y][x] = 0
for i in range(1, K+1):
    for cy, cx in mp[i]:
        adj = i + 1
        for ny,nx in mp[adj]:
            if dists[ny][nx] > dists[cy][cx] + dist((ny,nx),(cy,cx)):
                dists[ny][nx] = dists[cy][cx] + dist((ny,nx),(cy,cx))

ans = inf
for i in range(N):
    for j in range(N):
        d = dists[i][j]
        b = mat[i][j]
        if b != K: continue
        ans = min(ans, d)

if ans == inf: print(-1)
else: print(ans)



