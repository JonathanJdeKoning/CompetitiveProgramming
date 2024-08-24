y,k,n = map(int, input().split())

out = []

md = y%k
for i in range((k-md), n+1,k):
    if y+i > n: break
    out.append(i)

if not out: print(-1)
else:print(" ".join(map(str, out)))

