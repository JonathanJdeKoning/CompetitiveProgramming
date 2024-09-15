n = int(input())
far = 99999
ans = 0
for _ in range(n):
    x,y = map(int, input().split())
    far = min(far, y)
    ans += far*x

print(ans)
