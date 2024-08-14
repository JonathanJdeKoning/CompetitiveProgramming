n,a,b = map(int, input().split())

seen, left = -1, n
ans = 0
for i in range(n):
    seen += 1
    left -= 1
    if seen >= a and left <= b:
        ans += 1
print(ans)


