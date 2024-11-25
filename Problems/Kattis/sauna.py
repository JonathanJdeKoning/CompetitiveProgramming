N = int(input())
mn = 0
mx = 2*10**5
for _ in range(N):
    low, high = list(map(int, input().split()))
    mn = max(mn, low)
    mx = min(mx, high)

if mx < mn:
    print("bad news")
else:
    print((mx-mn)+1, mn)