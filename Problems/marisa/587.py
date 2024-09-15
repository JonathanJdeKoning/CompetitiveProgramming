x,a,b,c,d = map(int, input().split())
ans = 0

for i in range(1,x+1):
    if i <= 50:
        ans += a
    elif i <101:
        ans += b
    elif i < 151:
        ans += c
    else:
        ans += d


print(ans)
