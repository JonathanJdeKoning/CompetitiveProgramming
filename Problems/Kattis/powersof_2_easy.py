N, d = list(map(int, input().replace(","," ").split()))
d = str(2**d)
ans = 0
for i in range(1, N+1):
    if d in str(i):
        ans += 1
print(ans)