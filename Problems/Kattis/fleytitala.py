d = int(input())
k = int(input())
ans = d

for i in range(min(k, 64)):
    d/=2
    ans += d

print(ans)


