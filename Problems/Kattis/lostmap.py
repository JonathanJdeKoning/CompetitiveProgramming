import heapq
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]


best = [0]*n
left = set(range(1,n))
seen = [True]+[False]*(n-1)

h = []
for i in range(1,n):
    heapq.heappush(h, (mat[0][i], 0, i))
    best[i] = mat[0][i]

edges = 0
while True:
    while True:
        _, u, v = heapq.heappop(h)
        if seen[v]: continue
        break
    print(u+1,v+1)
    edges += 1
    if edges == n-1: break
    seen[v] = True
    left.discard(v)
    for w in left:
        if mat[v][w] < best[w]:
            best[w] = mat[v][w]
            heapq.heappush(h, (mat[v][w], v, w))

