from math import inf

def solve(N ,M, Q):

    dists = [[inf]*N for _ in range(N)]
    for i in range(N):
        dists[i][i] = 0

    for _ in range(M):
        u, v, w = list(map(int, input().replace(","," ").split()))
        dists[u][v] = min(w, dists[u][v])

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dists[i][k] + dists[k][j] < dists[i][j]:
                    dists[i][j] = -inf

    for _ in range(Q):
        qu, qv = list(map(int, input().replace(","," ").split()))
        mnDist = dists[qu][qv]
        if mnDist == inf:
            print("Impossible")
        elif mnDist == -inf:
            print("-Infinity")
        else:
            print(mnDist)
    #for row in dists: print(row)
    print()

while True:
    N, M, Q = list(map(int, input().replace(","," ").split()))
    if [N, M, Q] == [0,0,0]: exit(0)
    solve(N, M, Q)