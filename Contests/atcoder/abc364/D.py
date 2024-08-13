n,q = map(int, input().split())
a = sorted(list(map(int, input().split())))
qs = []
ans = []
for _ in range(q):
    b,k = map(int, input().split())
    qs.append((b,k))
