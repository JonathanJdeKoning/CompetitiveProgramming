N, K = list(map(int, input().replace(","," ").split()))
ans = 0
for _ in range(N):
    n = int(input())
    while n%2==0:
        ans += 1
        n//=2
if ans >= K: print(1)
else: print(0)