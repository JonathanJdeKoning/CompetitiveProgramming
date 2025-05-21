N, K = list(map(int, input().replace(","," ").split()))
sessions = []
for _ in range(N):
    sessions.append(list(map(int, input().replace(","," ").split())))


ans = 0
for a in range(1, K):
    for b in range(a+1, K+1):
        if len(set([sesh.index(a) > sesh.index(b) for sesh in sessions])) == 1: ans += 1

print(ans)