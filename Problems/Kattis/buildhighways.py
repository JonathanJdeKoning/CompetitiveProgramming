n = int(input())

a = sorted(list(map(int, input().split())))

ans = 0
for num in a[1:]:
    ans += num+a[0]

print(ans)
