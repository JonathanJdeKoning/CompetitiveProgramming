n,c = map(int, input().split())
a = list(map(int, input().split()))

mx = 0
for i, n in enumerate(a[:-1]):
    mx = max(mx, (n-a[i+1])-c)
print(mx)
