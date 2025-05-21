N,K = list(map(int, input().replace(","," ").split()))
spot = [input() for _ in range(N)]
non = [input() for _ in range(N)]

ans = 0
gen = set(["A", "C", "G", "T"])
for i in range(K):
    s = [cow[i] for cow in spot]
    t = [cow[i] for cow in non]
    makeup = set(s)
    inv = set(t)
    if len(makeup.intersection(inv)) == 0:
        ans += 1
print(ans)
